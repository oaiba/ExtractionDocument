---
title: "Social & Multiplayer System - Technical Specification"
type: docs
---

## Overview

The **Social System** manages squad formation, cross-platform parties, voice/text chat, ping system, clans, and friends lists using **Epic Online Services (EOS)**.

---

## Enums & Types

### SquadRole
Squad member role assignment.

| Code Name      | Display Name | Max Per Squad | Icon  | Description                   |
| :------------- | :----------- | :------------ | :---- | :---------------------------- |
| `SR_Leader`    | Leader       | 1             | Crown | Squad leader, can kick/invite |
| `SR_Point`     | Point        | 1             | Arrow | Front-line, entry specialist  |
| `SR_Support`   | Support      | 1             | Cross | Medic/support role            |
| `SR_Overwatch` | Overwatch    | 1             | Eye   | Rear guard, sniper position   |
| `SR_None`      | None         | 3             | None  | No assigned role              |

### FriendPlatform
Source platform for friend relationship.

| Code Name  | Display Name   | Icon       |
| :--------- | :------------- | :--------- |
| `FP_EOS`   | Epic Friends   | Epic Logo  |
| `FP_Steam` | Steam Friends  | Steam Logo |
| `FP_PSN`   | PSN Friends    | PS Logo    |
| `FP_XBL`   | Xbox Friends   | Xbox Logo  |
| `FP_Local` | Local Contacts | Phone      |

### PartyState
Current state of the squad/party.

| Code Name        | Display Name | Description                       |
| :--------------- | :----------- | :-------------------------------- |
| `PS_Lobby`       | In Lobby     | Building squad, selecting loadout |
| `PS_Matchmaking` | Matchmaking  | Searching for a game              |
| `PS_InGame`      | In Game      | Currently in a match              |
| `PS_PostGame`    | Post Game    | Viewing results                   |

### VoiceChatChannel
Voice communication channel.

| Code Name       | Display Name | Range     | Privacy | Description             |
| :-------------- | :----------- | :-------- | :------ | :---------------------- |
| `VCC_Squad`     | Squad        | Unlimited | Private | Squad-only voice chat   |
| `VCC_Proximity` | Proximity    | 15m       | Public  | Nearby players can hear |
| `VCC_Muted`     | Muted        | N/A       | N/A     | Voice disabled          |

---

## Code Names

### Squad Events

| Code Name             | Trigger       | Parameters      | Description            |
| :-------------------- | :------------ | :-------------- | :--------------------- |
| `SQUAD_CREATED`       | Squad formed  | PartyID         | New party created      |
| `SQUAD_JOINED`        | Player joined | PUID, PartyID   | Player joined party    |
| `SQUAD_LEFT`          | Player left   | PUID, Reason    | Player left party      |
| `SQUAD_INVITE`        | Invite recv   | FromPUID, Valid | Invite received        |
| `SQUAD_LEADER_CHANGE` | Leader swap   | NewLeaderPUID   | Leadership transferred |

### Social Events

| Code Name         | Trigger       | Parameters        | Description                |
| :---------------- | :------------ | :---------------- | :------------------------- |
| `FRIEND_PRESENCE` | Status change | PUID, Status, App | Friend came online/offline |
| `FRIEND_INVITE`   | Friend req    | FromPUID          | Friend request received    |
| `BLOCK_USER`      | Blocked       | PUID              | User blocked               |

---

## Core Classes

### SquadManager

**Purpose:** Manage cross-platform parties via EOS.

```
CLASS SquadManager:
    currentPartyID: String
    partyMembers: List<PartyMember>
    localPlayerRole: SquadRole
    partyState: PartyState
    
    // Dependencies
    EOSLobbyManager: LobbyManager
    
    FUNCTION CreateParty():
        // Create EOS Lobby as "Party"
        EOSLobbyManager.CreateLobby(4, LP_Friends)
        partyState = PS_Lobby
    END FUNCTION
    
    FUNCTION InviteFriend(targetPUID: String):
        // Use EOS Overlay or direct invite
        LobbyInterface.SendInvite(targetPUID)
    END FUNCTION
    
    FUNCTION JoinParty(inviteId: String):
        LobbyInterface.JoinLobby(inviteId, OnPartyJoined)
    END FUNCTION
    
    FUNCTION SetReadyState(isReady: Boolean):
        // Update member attribute
        EOSLobbyManager.UpdateMemberAttribute("Ready", isReady)
        CheckAllReady()
    END FUNCTION
    
    FUNCTION CheckAllReady():
        IF AllMembersReady() AND IsLeader():
             StartMatchmaking()
        END IF
    END FUNCTION
    
    FUNCTION StartMatchmaking():
        partyState = PS_Matchmaking
        EOSLobbyManager.UpdateLobbyAttribute("State", "Searching")
        MatchmakingSystem.StartSearch(currentPartyID)
    END FUNCTION
```

### FriendManager

**Purpose:** Aggregates friends from multiple platforms.

```
CLASS FriendManager:
    friendsList: Map<String, FriendData>
    blockedUsers: Set<String>
    
    FUNCTION Initialize():
        // Load EOS friends
        EOSFriends.QueryFriends(OnEOSFriendsLoaded)
        
        // Load Platform friends (Steam/Console)
        PlatformFriends.Query(OnPlatformFriendsLoaded)
    END FUNCTION
    
    FUNCTION OnEOSFriendsLoaded(friends: List<EOSFriend>):
        FOR EACH f IN friends:
            friendsList[f.PUID] = ConvertToFriendData(f, FP_EOS)
            SubscribeToPresence(f.PUID)
        END FOR
    END FUNCTION
    
    FUNCTION GetOnlineFriends() -> List<FriendData>:
        return friendsList.Filter(f => f.Status == FS_Online OR f.Status == FS_InGame)
    END FUNCTION
    
    FUNCTION SendFriendRequest(targetPUID: String):
        EOSFriends.SendInvite(targetPUID)
    END FUNCTION
```

### VoiceChatComponent

**Purpose:** Voice communication via EOS Voice.

```
CLASS VoiceChatComponent:
    currentRoom: String
    bIsTalking: Boolean
    
    FUNCTION JoinRoom(roomName: String):
        EOSVoice.JoinRoom(roomName, OnRoomJoined)
    END FUNCTION
    
    FUNCTION SetOutputVolume(puid: String, volume: Float):
        EOSVoice.SetRemoteVolume(puid, volume)
    END FUNCTION
    
    FUNCTION Update():
        // Tick voice processing
        IF AudioInput.IsSpeaking():
             bIsTalking = true
             EMIT EVENT "VOICE_TX_START"
        END IF
    END FUNCTION
```

---

## Data Structures

```
STRUCT PartyMember:
    PUID: String
    DisplayName: String
    Platform: FriendPlatform
    Role: SquadRole
    bIsReady: Boolean
    Loadout: LoadoutData

STRUCT FriendData:
    PUID: String
    DisplayName: String
    Platform: FriendPlatform
    Status: FriendStatus
    RichPresence: String // "In Menu", "Playing Map X"
```



