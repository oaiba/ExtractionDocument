# Analytics System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: Security System →](../Core/SecuritySystem.md)**

---

## Overview

The **Analytics System** handles data collection for player behavior, game economy, and technical performance. It is designed to be privacy-compliant and performance-neutral.

---

## Enums & Types

### AnalyticsEventType
Category of analytics event.

| Code Name         | Display Name | Priority | Description                  |
| :---------------- | :----------- | :------- | :--------------------------- |
| `AET_Gameplay`    | Gameplay     | High     | Match flow, kills, deaths    |
| `AET_Economy`     | Economy      | Critical | Gold flow, item transactions |
| `AET_System`      | System       | Medium   | Settings, UI navigation      |
| `AET_Performance` | Performance  | Low      | Framerate, memory usage      |
| `AET_Error`       | Error        | Critical | Crashes, exceptions          |

---

### EconomyActionType
Type of economic transaction.

| Code Name     | Display Name | Effect                    |
| :------------ | :----------- | :------------------------ |
| `EAT_Earn`    | Earn         | Currency added (Source)   |
| `EAT_Spend`   | Spend        | Currency removed (Sink)   |
| `EAT_Trade`   | Trade        | Player-to-player transfer |
| `EAT_Discard` | Discard      | Item destroyed            |

---

### PlayerDeathReason
Context for player death.

| Code Name           | Display Name               |
| :------------------ | :------------------------- |
| `PDR_Weapon`        | Weapon Damage              |
| `PDR_Environmental` | Environmental (Fall, Fire) |
| `PDR_AI`            | AI Enemy                   |
| `PDR_Bleedout`      | Bleeding Status            |
| `PDR_Suicide`       | Self-inflicted             |

---

## Code Names

### Analytic Events

| Code Name         | Trigger          | Parameters               | Description             |
| :---------------- | :--------------- | :----------------------- | :---------------------- |
| `MATCH_START`     | Match begins     | MapID, Mode, PlayerCount | Match session start     |
| `MATCH_END`       | Match finishes   | Duration, Winner, Reason | Match session end       |
| `PLAYER_KILL`     | Player gets kill | VictimID, WeaponID, Dist | Kill recorded           |
| `PLAYER_DEATH`    | Player dies      | KillerID, Reason, Pos    | Death recorded          |
| `ITEM_ACQUIRED`   | Item obtained    | ItemID, Source           | Item added to inventory |
| `CURRENCY_CHANGE` | Balance update   | Type, Amount, Reason     | Currency flow           |

---

## Core Classes

### AnalyticsManager

**Purpose:** Central hub for buffering and sending telemetry.

```
CLASS AnalyticsManager:
    eventBuffer: List<AnalyticsEvent>
    sessionID: String
    userID: String
    
    FUNCTION Initialize():
        sessionID = GenerateUUID()
        userID = LoginManager.GetUserID()
    END FUNCTION
    
    FUNCTION TrackEvent(eventName: String, parameters: Map<String, Any>, priority: AnalyticsEventType):
        event = NEW AnalyticsEvent()
        event.Name = eventName
        event.Timestamp = GetUTCDate()
        event.SessionID = sessionID
        event.UserID = userID
        event.Parameters = parameters
        
        eventBuffer.Add(event)
        
        IF priority == AET_Critical OR eventBuffer.Count >= MAX_BUFFER_SIZE:
             FlushBuffer()
        END IF
    END FUNCTION
    
    FUNCTION FlushBuffer():
        IF eventBuffer.IsEmpty(): RETURN
        
        serializedData = Serialize(eventBuffer)
        NetworkClient.SendTelemetry(serializedData)
        eventBuffer.Clear()
    END FUNCTION
```

---

### EconomyTracker

**Purpose:** specialized tracking for economy health.

```
CLASS EconomyTracker:
    FUNCTION TrackTransaction(type: EconomyActionType, resourceID: String, amount: Integer, source: String):
        params = {
            "Action": type,
            "Resource": resourceID,
            "Amount": amount,
            "SourceContext": source,
            "PlayerLevel": ProgressionManager.GetLevel()
        }
        
        AnalyticsManager.TrackEvent("ECONOMY_TRANSACTION", params, AET_Economy)
    END FUNCTION
```

---

### PerformanceMonitor

**Purpose:** Track client stability and performance.

```
CLASS PerformanceMonitor:
    FUNCTION SnapshotPerformance():
        fps = Graphics.GetAverageFPS()
        memory = System.GetUsedMemory()
        ping = Network.GetPing()
        
        params = {
            "FPS": fps,
            "MemoryMB": memory,
            "PingMS": ping,
            "Map": MapManager.GetCurrentMap()
        }
        
        AnalyticsManager.TrackEvent("PERF_SNAPSHOT", params, AET_Performance)
    END FUNCTION
```

---

## Data Structures

```
STRUCT AnalyticsEvent:
    Name: String
    Timestamp: DateTime
    SessionID: String
    UserID: String
    Parameters: Map<String, Any>

STRUCT TelemetryConfig:
    EndpointURL: String
    FlushInterval: Float
    MaxBufferSize: Integer
    SampleRate: Float
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] AnalyticsManager buffer logic
- [ ] Network client integration
- [ ] Core event definitions (Match, Kill, Economy)

### MEDIUM Priority 🟡
- [ ] Performance monitoring hooks
- [ ] Economy transaction wrapper
- [ ] Data serialization (JSON/Protobuf)

### LOW Priority 🟢
- [ ] Heatmap data collection (Position tracking)
- [ ] Crash reporting integration
- [ ] Real-time dashboard support

---

**[← Back to Index](../README.md)** | **[Next: Security System →](../Core/SecuritySystem.md)**
