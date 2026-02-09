---
title: "Networking System - Technical Design Document"
type: docs
---

## Overview

### Network Model

| Property           | Value                                    |
| :----------------- | :--------------------------------------- |
| **Architecture**   | Dedicated Server with EOS Relay fallback |
| **Authority**      | Server Authoritative                     |
| **Topology**       | Client-Server (Star)                     |
| **Protocol**       | UDP (Standard) / P2P (EOS Relay)         |
| **Cross-Platform** | Epic Online Services (EOS)               |

### Core Functions

| Function              | Description                       |
| :-------------------- | :-------------------------------- |
| **Replication**       | State synchronization             |
| **Client Prediction** | Hide latency                      |
| **Lag Compensation**  | Fair hit detection                |
| **Matchmaking**       | EOS Smart Sessions / Flex Match   |
| **Lobbies**           | Persistent cross-platform lobbies |
| **Anti-Cheat**        | Easy Anti-Cheat (EOS)             |

---

## System Architecture

```
        ┌──────────────┐
        │  EOS Cloud   │ (Matchmaking, Auth, Relay)
        └──────┬───────┘
               │
        ┌──────┴───────┐
        │              │
  ┌─────▼─────┐  ┌─────▼─────┐
  │ Game Svr 1│  │ Game Svr 2│ (Dedicated Servers)
  └─────┬─────┘  └─────┬─────┘
        │              │
  ┌─────┼───────┬──────┼─────┐
  │     │       │      │     │
┌─▼─┐ ┌─▼─┐   ┌─▼─┐  ┌─▼─┐ ┌─▼─┐
│PC │ │PS5│   │XBX│  │iOS│ │And│ (Cross-Platform Clients)
└───┘ └───┘   └───┘  └───┘ └───┘
```

---

## Enums & Types

### NetworkRole

| Code Name            | Display Name     | Authority | Replication |
| :------------------- | :--------------- | :-------- | :---------- |
| `NR_Server`          | Dedicated Server | Full      | Source      |
| `NR_ListenServer`    | Listen Server    | Full      | Source      |
| `NR_Client`          | Client           | None      | Receiver    |
| `NR_SimulatedProxy`  | Simulated Proxy  | None      | Simulated   |
| `NR_AutonomousProxy` | Autonomous Proxy | Local     | Predicted   |

### AuthProvider
Authentication provider for EOS Connect.

| Code Name   | Display Name | Platform  |
| :---------- | :----------- | :-------- |
| `AP_Epic`   | Epic Games   | PC        |
| `AP_Steam`  | Steam        | PC        |
| `AP_Google` | Google Play  | Android   |
| `AP_Apple`  | Apple ID     | iOS       |
| `AP_PSN`    | PlayStation  | PS5       |
| `AP_XBL`    | Xbox Live    | Xbox      |
| `AP_Device` | Device ID    | Guest/Dev |

### LobbyPrivacy
Visibility settings for lobbies.

| Code Name    | Display Name | Searchable | Invite Only |
| :----------- | :----------- | :--------- | :---------- |
| `LP_Public`  | Public       | Yes        | No          |
| `LP_Friends` | Friends Only | No         | Yes         |
| `LP_Private` | Private      | No         | Yes         |

### ConnectionState

| Code Name           | Display Name   | Timeout | UI State     |
| :------------------ | :------------- | :------ | :----------- |
| `CS_Disconnected`   | Disconnected   | N/A     | Main Menu    |
| `CS_Authenticating` | Authenticating | 15s     | Login Screen |
| `CS_Connecting`     | Connecting     | 30s     | Loading      |
| `CS_Connected`      | Connected      | N/A     | In-game      |
| `CS_Reconnecting`   | Reconnecting   | 60s     | Overlay      |
| `CS_TimedOut`       | Timed Out      | N/A     | Error        |

### MatchmakingState

| Code Name       | Display Name | Duration | Cancel |
| :-------------- | :----------- | :------- | :----- |
| `MMS_Idle`      | Idle         | N/A      | N/A    |
| `MMS_InLobby`   | In Lobby     | N/A      | Yes    |
| `MMS_Searching` | Searching    | 0-120s   | Yes    |
| `MMS_Found`     | Match Found  | 10s      | Yes    |
| `MMS_Joining`   | Joining      | 30s      | No     |

---

## Code Names

### EOS Events

| Code Name          | Trigger       | Parameters   | Description             |
| :----------------- | :------------ | :----------- | :---------------------- |
| `EOS_AUTH_SUCCESS` | Login success | PUID, EpikID | Authenticated with EOS  |
| `EOS_AUTH_FAIL`    | Login fail    | ErrorCode    | Auth failed             |
| `EOS_LOBBY_JOIN`   | Joined lobby  | LobbyID      | Entered a lobby         |
| `EOS_LOBBY_LEFT`   | Left lobby    | LobbyID      | Exited a lobby          |
| `EOS_LOBBY_UPDATE` | Data update   | Attr, Value  | Lobby attribute changed |

### Connection Events

| Code Name        | Trigger            | Parameters       | Description          |
| :--------------- | :----------------- | :--------------- | :------------------- |
| `NET_CONNECT`    | Client connects    | ClientID, IP     | New client connected |
| `NET_DISCONNECT` | Client disconnects | ClientID, Reason | Client disconnected  |
| `NET_TIMEOUT`    | Connection timeout | ClientID         | Connection timed out |

---

## Core Classes

### EOSManager

**Purpose:** Wrapper for Epic Online Services platform interface.

```
CLASS EOSManager:
    STATIC instance: EOSManager
    productUserID: String
    epicAccountID: String
    
    FUNCTION Initialize():
        // Init platform interface
        config = CreatePlatformConfig()
        PlatformInterface.Initialize(config)
    END FUNCTION
    
    FUNCTION Login(provider: AuthProvider, token: String):
        credentials = NEW Credentials()
        credentials.Type = provider
        credentials.Token = token
        
        AuthInterface.Login(credentials, OnLoginComplete)
    END FUNCTION
    
    FUNCTION OnLoginComplete(result: LoginCallbackInfo):
        IF result.ResultCode == Success:
            productUserID = result.LocalUserId
            ConnectInterface.Login(productUserID) // Link to Product User ID
            EMIT EVENT "EOS_AUTH_SUCCESS"
        ELSE:
            EMIT EVENT "EOS_AUTH_FAIL" WITH (result.ResultCode)
        END IF
    END FUNCTION
```

### LobbyManager

**Purpose:** Manages EOS Lobby lifecycle and attributes.

```
CLASS LobbyManager:
    currentLobbyID: String
    currentLobbyDetails: LobbyDetails
    bIsHost: Boolean
    
    FUNCTION CreateLobby(maxPlayers: Integer, privacy: LobbyPrivacy):
        options = NEW CreateLobbyOptions()
        options.MaxPlayers = maxPlayers
        options.PermissionLevel = privacy
        options.BucketId = "ExtractionGame:Region:GameMode"
        
        LobbyInterface.CreateLobby(options, OnLobbyCreated)
    END FUNCTION
    
    FUNCTION SearchLobbies(filters: List<Attribute>):
        search = NEW LobbySearch()
        search.SetMaxResults(10)
        
        FOR EACH filter IN filters:
             search.SetParameter(filter.Key, filter.Value, filter.Op)
        END FOR
        
        search.Find(OnLobbySearchComplete)
    END FUNCTION
    
    FUNCTION UpdateLobbyAttribute(key: String, value: String):
        IF NOT bIsHost: RETURN
        
        modification = NEW LobbyModification(currentLobbyID)
        modification.AddAttribute(key, value)
        LobbyInterface.UpdateLobby(modification, OnLobbyUpdated)
    END FUNCTION
```

### NetworkManager

**Purpose:** Central networking controller for game sessions.

```
CLASS NetworkManager:
    STATIC instance: NetworkManager
    
    connectionState: ConnectionState
    replicatedActors: Map<String, NetworkedActor>
    
    // Events
    OnClientConnected: Event<(clientID)>
    OnClientDisconnected: Event<(clientID, reason)>
    
    FUNCTION ConnectToSession(sessionInfo: SessionResult):
        connectionState = CS_Connecting
        
        // Get connection string from session (IP or P2P ID)
        connectString = sessionInfo.GetConnectionString()
        
        // Attempt transport connection
        NetworkDriver.Connect(connectString)
    END FUNCTION

    FUNCTION SpawnNetworkedActor(actorClass: Type, position: Vector3, ownerID: String) -> NetworkedActor:
        // Spawning logic (same as previous)
        actor = Instantiate(actorClass, position)
        actor.actorID = GenerateNetworkID()
        // ... replication setup ...
        RETURN actor
    END FUNCTION
```

---

## Data Structures

```
STRUCT NetworkedActor:
    actorID: String
    ownerClientID: String
    role: NetworkRole
    replicatedProperties: Map<String, Property>

STRUCT LobbyDetails:
    LobbyID: String
    HostID: String
    MemberCount: Integer
    MaxMembers: Integer
    Attributes: Map<String, String>
    Members: List<LobbyMember>

STRUCT LobbyMember:
    ProductUserID: String
    Attributes: Map<String, String> // Ready state, skin, char
```



