---
title: "Ranked System - Technical Specification"
type: docs
---

## Overview

The **Ranked System** manages competitive matchmaking, ranking, leaderboards, and seasonal rewards.

---

## Enums & Types

### RankTier
Ranked tier progression with RP thresholds.

| Code Name         | Display Name | RP Required | Division | Border Color        | Description                   |
| :---------------- | :----------- | :---------- | :------- | :------------------ | :---------------------------- |
| `RT_Bronze_III`   | Bronze III   | 0           | 3        | Bronze              | Entry tier, division 3        |
| `RT_Bronze_II`    | Bronze II    | 100         | 2        | Bronze              | Entry tier, division 2        |
| `RT_Bronze_I`     | Bronze I     | 200         | 1        | Bronze              | Entry tier, division 1        |
| `RT_Silver_III`   | Silver III   | 300         | 3        | Silver              | Beginner tier, division 3     |
| `RT_Silver_II`    | Silver II    | 400         | 2        | Silver              | Beginner tier, division 2     |
| `RT_Silver_I`     | Silver I     | 500         | 1        | Silver              | Beginner tier, division 1     |
| `RT_Gold_III`     | Gold III     | 600         | 3        | Gold                | Intermediate tier, division 3 |
| `RT_Gold_II`      | Gold II      | 700         | 2        | Gold                | Intermediate tier, division 2 |
| `RT_Gold_I`       | Gold I       | 800         | 1        | Gold                | Intermediate tier, division 1 |
| `RT_Platinum_III` | Platinum III | 1000        | 3        | Platinum            | Advanced tier, division 3     |
| `RT_Platinum_II`  | Platinum II  | 1200        | 2        | Platinum            | Advanced tier, division 2     |
| `RT_Platinum_I`   | Platinum I   | 1400        | 1        | Platinum            | Advanced tier, division 1     |
| `RT_Diamond_III`  | Diamond III  | 1500        | 3        | Diamond             | Expert tier, division 3       |
| `RT_Diamond_II`   | Diamond II   | 1700        | 2        | Diamond             | Expert tier, division 2       |
| `RT_Diamond_I`    | Diamond I    | 1900        | 1        | Diamond             | Expert tier, division 1       |
| `RT_Master`       | Master       | 2000        | N/A      | Master (Animated)   | Elite tier, no divisions      |
| `RT_Champion`     | Champion     | Top 500     | N/A      | Champion (Animated) | Top 500 players globally      |

---

### RankedQueueType
Queue type for ranked matchmaking.

| Code Name   | Display Name | Party Size | Squad Balance | Description                      |
| :---------- | :----------- | :--------- | :------------ | :------------------------------- |
| `RQT_Solo`  | Solo         | 1          | Solo only     | Solo queue, fair 1v1 environment |
| `RQT_Duo`   | Duo          | 2          | Duo only      | Duo queue, paired teams          |
| `RQT_Squad` | Squad        | 3          | Mixed squads  | Full squad queue                 |

---

### MatchResultType
Match outcome classification for RP calculation.

| Code Name          | Display Name  | Base RP | Survival % | Description                  |
| :----------------- | :------------ | :------ | :--------- | :--------------------------- |
| `MRT_Extracted`    | Extracted     | +30     | 100%       | Successfully extracted       |
| `MRT_Death_Late`   | Death (Late)  | -10     | 75-99%     | Died in final phase          |
| `MRT_Death_Mid`    | Death (Mid)   | -15     | 40-74%     | Died mid-match               |
| `MRT_Death_Early`  | Death (Early) | -25     | 0-39%      | Died early in match          |
| `MRT_Disconnected` | Disconnected  | -50     | N/A        | Left/disconnected from match |

---

### LeaderboardType
Leaderboard category for rankings.

| Code Name           | Display Name    | Scope  | Reset  | Description                |
| :------------------ | :-------------- | :----- | :----- | :------------------------- |
| `LT_Global_RP`      | Global RP       | Global | Season | Total RP ranking           |
| `LT_Regional_RP`    | Regional RP     | Region | Season | RP by region               |
| `LT_Weekly_RP`      | Weekly RP       | Global | Weekly | RP gained this week        |
| `LT_Kills`          | Kills           | Global | Season | Total kill ranking         |
| `LT_ExtractionRate` | Extraction Rate | Global | Season | % successful extractions   |
| `LT_Wealth`         | Wealth          | Global | Season | Total loot value extracted |

---

### BanType
Penalty ban classification.

| Code Name            | Display Name         | Duration | Scope        | Description             |
| :------------------- | :------------------- | :------- | :----------- | :---------------------- |
| `BT_None`            | None                 | N/A      | N/A          | No active ban           |
| `BT_Warning`         | Warning              | N/A      | Notification | First offense warning   |
| `BT_Ranked7Day`      | 7-Day Ranked Ban     | 7 days   | Ranked only  | Short ranked suspension |
| `BT_Ranked30Day`     | 30-Day Ranked Ban    | 30 days  | Ranked only  | Long ranked suspension  |
| `BT_RankedPermanent` | Permanent Ranked Ban | Forever  | Ranked only  | Permanent ranked ban    |
| `BT_FullBan`         | Full Ban             | Forever  | All modes    | Complete account ban    |

---

## Code Names

### Rank Events

| Code Name       | Trigger        | Parameters             | Description          |
| :-------------- | :------------- | :--------------------- | :------------------- |
| `RANK_PROMOTED` | Tier increased | OldTier, NewTier       | Player ranked up     |
| `RANK_DEMOTED`  | Tier decreased | OldTier, NewTier       | Player ranked down   |
| `RANK_RESET`    | Season reset   | OldRank, NewRank, Type | Soft/hard rank reset |

### Season Events

| Code Name       | Trigger         | Parameters                  | Description                |
| :-------------- | :-------------- | :-------------------------- | :------------------------- |
| `SEASON_START`  | Season begins   | SeasonID, StartDate         | New season started         |
| `SEASON_END`    | Season ends     | SeasonID, EndDate           | Season concluded           |
| `SEASON_REWARD` | Rewards claimed | SeasonID, PeakRank, Rewards | Season rewards distributed |

### Match Events

| Code Name         | Trigger   | Parameters        | Description        |
| :---------------- | :-------- | :---------------- | :----------------- |
| `MATCH_RP_GAINED` | RP earned | Amount, Breakdown | Positive RP change |
| `MATCH_RP_LOST`   | RP lost   | Amount, Breakdown | Negative RP change |

### Leaderboard Events

| Code Name                  | Trigger          | Parameters       | Description           |
| :------------------------- | :--------------- | :--------------- | :-------------------- |
| `LEADERBOARD_UPDATE`       | Rankings updated | Type, PlayerRank | Leaderboard refreshed |
| `LEADERBOARD_RANK_CHANGED` | Position changed | OldRank, NewRank | Player rank shifted   |

### Penalty Events

| Code Name          | Trigger         | Parameters            | Description              |
| :----------------- | :-------------- | :-------------------- | :----------------------- |
| `PENALTY_APPLIED`  | Penalty issued  | PenaltyType, Duration | Penalty added to account |
| `COOLDOWN_STARTED` | Cooldown active | Duration, Reason      | Queue cooldown started   |

---

## Core Classes

### RankedManager

**Purpose:** Manage player rank, RP, and season state.

```
CLASS RankedManager:
    currentRank: RankInfo
    currentRP: Integer
    lossStreak: Integer = 0
    demotionShieldRemaining: Integer = 0
    
    FUNCTION QueueForRanked(type: RankedQueueType) -> Boolean:
        requirements = GetQueueRequirements()
        
        IF NOT CheckRequirements(requirements):
            RETURN false
        END IF
        
        // Cannot queue if banned
        IF activeBan != BT_None:
            RETURN false
        END IF
        
        RankedMatchmaker.FindMatch(type, GetLocalPlayerIDs())
        RETURN true
    END FUNCTION
    
    FUNCTION LeaveQueue():
        RankedMatchmaker.CancelSearch()
    END FUNCTION
    
    FUNCTION ProcessMatchResult(result: MatchResult):
        rpChange = CalculateRPChange(result)
        
        previousTier = currentRank.Tier
        currentRP += rpChange
        
        // Handle demotion protection
        IF rpChange < 0 AND demotionShieldRemaining > 0:
             // Prevent dropping below threshold if shielded
             currentRP = Max(currentRP, GetThreshold(currentRank.Tier))
             demotionShieldRemaining -= 1
        END IF
        
        UpdateRankTier()
        newTier = currentRank.Tier
        
        IF newTier > previousTier:
             EMIT EVENT "RANK_PROMOTED" WITH (previousTier, newTier)
             demotionShieldRemaining = 3 // Grant shield on promotion
        ELSE IF newTier < previousTier:
             EMIT EVENT "RANK_DEMOTED" WITH (previousTier, newTier)
        END IF
        
        IF rpChange >= 0:
             EMIT EVENT "MATCH_RP_GAINED" WITH (rpChange, result)
             lossStreak = 0
        ELSE:
             EMIT EVENT "MATCH_RP_LOST" WITH (rpChange, result)
             lossStreak += 1
        END IF
    END FUNCTION
    
    FUNCTION CalculateRPChange(result: MatchResult) -> Integer:
        baseRP = 0
        
        SWITCH result.Outcome:
            CASE MRT_Extracted: baseRP = 30
            CASE MRT_Death_Late: baseRP = -10
            CASE MRT_Death_Mid: baseRP = -15
            CASE MRT_Death_Early: baseRP = -25
        END SWITCH
        
        // Performance modifiers
        baseRP += result.Kills * 5
        baseRP += result.HighValueLoot * 10
        
        IF result.bSquadWipe: baseRP += 10
        IF result.Placement <= 3: baseRP += 10
        IF result.SurvivalTime >= 600: baseRP += 5
        
        // Rank modifier
        rankDiff = result.AvgOpponentRank - currentRank.RP
        rankMod = 1.0 + (rankDiff * 0.0005) // Slight adjustment based on opponent difficulty
        
        // Apply streak protection if applicable
        IF lossStreak >= 3:
             baseRP = baseRP / 2 // Reduce loss by 50%
        END IF
        
        RETURN RoundToInt(baseRP * rankMod)
    END FUNCTION

    FUNCTION UpdateRankTier():
        // Logic to update CurrentRank.Tier based on CurrentRP and Thresholds
        // ...
    END FUNCTION
```

---

### RankedMatchmaker

**Purpose:** Handle matchmaking logic for ranked queues.

```
CLASS RankedMatchmaker:
    initialRankRange: Float = 100.0
    expansionPerMinute: Float = 100.0
    maxRankRange: Float = 500.0
    maxQueueTime: Float = 180.0
    
    FUNCTION FindMatch(type: RankedQueueType, playerIDs: List<String>):
        request = NEW MatchRequest()
        request.Type = type
        request.Players = playerIDs
        request.AvgRP = CalculateAvgRP(playerIDs)
        
        NetworkClient.SubmitMatchRequest(request)
    END FUNCTION
    
    FUNCTION CancelSearch():
        NetworkClient.CancelMatchRequest()
    END FUNCTION
```

---

### SeasonSystem

**Purpose:** Manage season lifecycle and resets.

```
CLASS SeasonSystem:
    currentSeason: SeasonConfig
    
    FUNCTION ApplySoftReset():
        // Mid-season reset logic
        // Example: Master -> Diamond II
        oldRank = RankedManager.GetPlayerRank()
        newRank = CalculateSoftResetRank(oldRank)
        
        RankedManager.SetRank(newRank)
        EMIT EVENT "RANK_RESET" WITH (oldRank, newRank, "Soft")
    END FUNCTION
    
    FUNCTION ApplyHardReset():
        // End of season reset
        oldRank = RankedManager.GetPlayerRank()
        newRank = RT_Bronze_III // Or placement matches state
        
        RankedManager.SetRank(newRank)
        RankedManager.SetPlacementMatches(5)
        
        EMIT EVENT "RANK_RESET" WITH (oldRank, newRank, "Hard")
    END FUNCTION
```

---

### LeaderboardSystem

**Purpose:** Manage global and regional leaderboards.

```
CLASS LeaderboardSystem:
    FUNCTION RequestLeaderboard(type: LeaderboardType, count: Integer):
        data = NetworkClient.GetLeaderboard(type, count)
        // Update UI with data
        EMIT EVENT "LEADERBOARD_UPDATE" WITH (type, data)
    END FUNCTION
```

---

## Data Structures

```
STRUCT RankInfo:
    Tier: RankTier
    RP: Integer
    Division: Integer
    GamesPlayed: Integer
    Wins: Integer
    PeakRank: RankTier

STRUCT MatchResult:
    Outcome: MatchResultType
    Kills: Integer
    HighValueLoot: Integer // Count of generic high value items context
    Placement: Integer
    SurvivalTime: Float
    bSquadWipe: Boolean
    AvgOpponentRank: Integer

STRUCT SeasonConfig:
    DurationDays: Integer = 90
    ActsPerSeason: Integer = 2
    StartDate: DateTime
    EndDate: DateTime
    SeasonName: String
    PlacementMatches: Integer = 5

STRUCT RankProtection:
    DemotionShieldGames: Integer = 2
    StreakProtectionAfter: Integer = 3
    StreakProtectionGames: Integer = 2
    StreakLossReduction: Float = 0.5
    RankFloor: RankTier = RT_Bronze_III

STRUCT LeaderboardEntry:
    Rank: Integer
    PlayerID: String
    DisplayName: String
    RP: Integer
    Wins: Integer
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] RankedManager core logic
- [ ] RP calculation algorithm
- [ ] Rank progression and demotion logic
- [ ] Queue restrictions implementation

### MEDIUM Priority 🟡
- [ ] Season management (Reset logic)
- [ ] Leaderboard backend integration
- [ ] Champion rank decay logic

### LOW Priority 🟢
- [ ] Match history storage
- [ ] Career statistics tracking
- [ ] Pro league integration features



