---
title: "Live Operations System - Technical Specification"
type: docs
---

## Overview

The **Live Operations System** manages events, content scheduling, seasonal content, challenges, shop rotations, and player engagement features.

---

## Enums & Types

### EventType
Live event type classification.

| Code Name           | Display Name    | Duration  | Key Mechanic   | Description                  |
| :------------------ | :-------------- | :-------- | :------------- | :--------------------------- |
| `ET_DoubleXP`       | Double XP       | Weekend   | 2.0× XP        | +100% account XP gain        |
| `ET_DoubleCredits`  | Double Credits  | Weekend   | 2.0× Credits   | +100% credit gain from loot  |
| `ET_DoubleBP`       | Double BP       | Limited   | 2.0× BP XP     | +100% Battle Pass XP         |
| `ET_DoubleOperator` | Double Operator | Limited   | 2.0× Op XP     | +100% operator XP            |
| `ET_LimitedMode`    | Limited Mode    | 1-2 weeks | Special Mode   | Night Ops, Chaos, Hardcore   |
| `ET_Collection`     | Collection      | 2-4 weeks | Fragments      | Earn fragments for rewards   |
| `ET_FactionWar`     | Faction War     | 2 weeks   | Competition    | Team-based point competition |
| `ET_BossHunt`       | Boss Hunt       | 1-2 weeks | Community Goal | Community kill goal          |
| `ET_Holiday`        | Holiday         | 1-2 weeks | Themed Content | Seasonal themed event        |
| `ET_FlashSale`      | Flash Sale      | 24-72h    | Shop Discount  | Limited-time shop sale       |

---

### EventState
Current state of an event.

| Code Name      | Display Name | Visibility | Playable | UI Indicator    |
| :------------- | :----------- | :--------- | :------- | :-------------- |
| `ES_Scheduled` | Scheduled    | Hidden     | No       | None            |
| `ES_Teaser`    | Teaser       | Visible    | No       | "Coming Soon"   |
| `ES_Active`    | Active       | Visible    | Yes      | "Live"          |
| `ES_Ending`    | Ending       | Visible    | Yes      | "Ending Soon"   |
| `ES_Completed` | Completed    | Visible    | No       | "Claim Rewards" |
| `ES_Archived`  | Archived     | Hidden     | No       | None            |

---

### ChallengeType
Challenge reset frequency.

| Code Name        | Display Name | Reset Time | Count  | XP Reward      |
| :--------------- | :----------- | :--------- | :----- | :------------- |
| `CT_Daily`       | Daily        | 00:00 UTC  | 3      | 50-75 BP XP    |
| `CT_Weekly`      | Weekly       | Mon 00:00  | 5      | 200-300 BP XP  |
| `CT_Seasonal`    | Seasonal     | Season end | 20     | 500 BP XP      |
| `CT_Event`       | Event        | Event end  | Varies | Event currency |
| `CT_Tutorial`    | Tutorial     | Never      | 10     | 100 XP         |
| `CT_Achievement` | Achievement  | Never      | 50+    | 500-5000 XP    |

---

### ChallengeRequirementType
Challenge objective type.

| Code Name             | Display Name | Context Filter | Example             |
| :-------------------- | :----------- | :------------- | :------------------ |
| `CRT_MatchComplete`   | Matches      | Mode           | Finish X matches    |
| `CRT_Extraction`      | Extractions  | Map            | Extract X times     |
| `CRT_Kills`           | Kills        | Enemy type     | Kill X enemies      |
| `CRT_KillsWithWeapon` | Weapon Kills | Weapon class   | Kill with weapon    |
| `CRT_DamageDealt`     | Damage       | None           | Deal X damage       |
| `CRT_LootValue`       | Loot Value   | None           | Extract X value     |
| `CRT_ZoneVisit`       | Zone Visits  | Zone type      | Visit specific zone |
| `CRT_SquadPlay`       | Squad Play   | None           | Play with squad     |

---

### BattlePassTierType
Battle Pass reward track.

| Code Name     | Display Name  | Unlock   | Tier Range | Description          |
| :------------ | :------------ | :------- | :--------- | :------------------- |
| `BPT_Free`    | Free Track    | Auto     | 1-100      | Available to all     |
| `BPT_Premium` | Premium Track | Purchase | 1-100      | Requires BP purchase |
| `BPT_Bonus`   | Bonus Track   | Premium  | 101-110    | Extra tiers          |

---

### ShopCategory
Shop section organization.

| Code Name      | Display Name | Rotation  | Discount     |
| :------------- | :----------- | :-------- | :----------- |
| `SC_Featured`  | Featured     | Weekly    | None         |
| `SC_Daily`     | Daily        | 24h       | None         |
| `SC_Weekly`    | Weekly       | 7 days    | None         |
| `SC_Bundle`    | Bundles      | Varies    | 20-30%       |
| `SC_Token`     | Tokens       | Permanent | Bonus tokens |
| `SC_Starter`   | Starter Pack | Once      | 50%          |
| `SC_Returning` | Returning    | Once      | 40%          |
| `SC_Archive`   | Archive      | Permanent | None         |

---

## Code Names

### Event Lifecycle

| Code Name         | Trigger | Parameters | Description       |
| :---------------- | :------ | :--------- | :---------------- |
| `EVENT_SCHEDULED` | Created | EventID    | Event scheduled   |
| `EVENT_START`     | Active  | EventID    | Event playable    |
| `EVENT_ENDING`    | Warning | EventID    | Event ending soon |
| `EVENT_COMPLETE`  | Ended   | EventID    | Event finished    |

### Challenge Events

| Code Name            | Trigger | Parameters   | Description        |
| :------------------- | :------ | :----------- | :----------------- |
| `CHALLENGE_PROGRESS` | Update  | ID, Progress | Progress updated   |
| `CHALLENGE_COMPLETE` | Done    | ID, Rewards  | Challenge finished |
| `CHALLENGE_CLAIM`    | Claimed | ID           | Reward claimed     |

### Battle Pass Events

| Code Name     | Trigger  | Parameters | Description        |
| :------------ | :------- | :--------- | :----------------- |
| `BP_TIER_UP`  | Level Up | Tier, XP   | BP level increased |
| `BP_PURCHASE` | Bought   | Cost       | Premium unlocked   |

---

## Core Classes

### LiveOpsManager

**Purpose:** Central controller for live events and configs.

```
CLASS LiveOpsManager:
    activeEvents: Map<String, EventData>
    remoteConfig: ConfigData
    
    // Subsystems
    eventManager: EventManager
    challengeManager: ChallengeManager
    battlePassManager: BattlePassManager
    shopManager: ShopManager
    
    FUNCTION FetchRemoteConfig():
        config = NetworkClient.GetRemoteConfig()
        ApplyConfig(config)
    END FUNCTION
    
    FUNCTION GetActiveEvents() -> List<EventData>:
        RETURN eventManager.GetActiveEvents()
    END FUNCTION
```

---

### EventManager

**Purpose:** Check event schedules and status.

```
CLASS EventManager:
    events: List<EventData>
    
    FUNCTION GetActiveEvents() -> List<EventData>:
        currentTime = GetServerTime()
        return events.Filter(e => 
            e.StartTime <= currentTime AND 
            e.EndTime > currentTime
        )
    END FUNCTION
    
    FUNCTION JoinEvent(eventID: String):
        event = GetEvent(eventID)
        IF event.IsActive():
            NetworkClient.JoinEvent(eventID)
        END IF
    END FUNCTION
    
    FUNCTION CheckEventMultipliers():
        // Calculate total active multipliers
    END FUNCTION
```

---

### ChallengeManager

**Purpose:** Track challenge progress.

```
CLASS ChallengeManager:
    activeChallenges: List<ChallengeData>
    
    FUNCTION UpdateProgress(type: ChallengeRequirementType, amount: Integer, context: String):
        FOR EACH challenge IN activeChallenges:
            IF challenge.Requirement == type AND challenge.ContextFilterMatches(context):
                 challenge.CurrentProgress += amount
                 CheckCompletion(challenge)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION CheckCompletion(challenge: ChallengeData):
        IF challenge.CurrentProgress >= challenge.TargetAmount:
             challenge.bIsComplete = true
             EMIT EVENT "CHALLENGE_COMPLETE" WITH (challenge.ID)
        END IF
    END FUNCTION
```

---

### BattlePassManager

**Purpose:** Handle BP progression.

```
CLASS BattlePassManager:
    currentTier: Integer
    currentXP: Integer
    bPremiumOwned: Boolean
    
    FUNCTION AddXP(amount: Integer):
        currentXP += amount
        xpToNext = GetXPForTier(currentTier + 1)
        
        WHILE currentXP >= xpToNext:
            currentXP -= xpToNext
            currentTier++
            EMIT EVENT "BP_TIER_UP" WITH (currentTier)
            xpToNext = GetXPForTier(currentTier + 1)
        END WHILE
    END FUNCTION
    
    FUNCTION ClaimReward(tier: Integer):
        IF tier > currentTier: RETURN
        
        rewards = GetRewardsForTier(tier)
        InventoryManager.AddItems(rewards)
    END FUNCTION
```

---

## Data Structures

```
STRUCT EventData:
    EventID: String
    EventType: EventType
    State: EventState
    StartTime: DateTime
    EndTime: DateTime
    Multipliers: Map<String, Float>

STRUCT ChallengeData:
    ChallengeID: String
    Type: ChallengeType
    Requirement: ChallengeRequirementType
    TargetAmount: Integer
    CurrentProgress: Integer
    Rewards: List<ItemReward>
    bIsComplete: Boolean

STRUCT BattlePassData:
    SeasonID: String
    MaxTiers: Integer
    PremiumCost: Integer
    Tiers: List<BattlePassTier>

STRUCT BattlePassTier:
    Level: Integer
    FreeRewards: List<ItemReward>
    PremiumRewards: List<ItemReward>
```

---

## TODO: Implementation Tasks

### HIGH Priority 
- [ ] LiveOpsManager config fetching
- [ ] EventManager scheduling logic
- [ ] ChallengeManager progress tracking
- [ ] BattlePassManager XP logic

### MEDIUM Priority 
- [ ] ShopManager rotation logic
- [ ] Remote config integration
- [ ] Event scheduling tools

### LOW Priority 
- [ ] Community goal tracking
- [ ] A/B testing framework support
- [ ] Advanced notification scheduling



