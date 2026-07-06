---
title: "Progression System - Technical Specification"
type: docs
---

## Overview

The **Progression System** manages player leveling, XP distribution, operator progression, currencies, Battle Pass, quests, and rewards. Designed for meaningful advancement without pay-to-win mechanics.

**Responsibilities:**
- Account level progression
- Operator individual progression
- XP calculation and distribution
- Currency management (Credits, Tokens, Reputation)
- Battle Pass tier progression
- Quest tracking and completion
- Reward distribution
- Prestige system

---

## Enums & Types

### XPSource
XP earning source with base values.

| Code Name           | Display Name   | Base XP | Frequency   | Description          |
| :------------------ | :------------- | :------ | :---------- | :------------------- |
| `XPS_MatchComplete` | Match Complete | 100     | Per match   | Base match XP        |
| `XPS_Extraction`    | Extraction     | 200     | Per extract | Extraction bonus     |
| `XPS_Kill`          | Kill           | 50      | Per kill    | Enemy kill XP        |
| `XPS_Assist`        | Assist         | 25      | Per assist  | Kill assist XP       |
| `XPS_Survival`      | Survival       | 10      | Per minute  | Time survived        |
| `XPS_Loot`          | Loot           | 1       | Per $100    | Loot value extracted |
| `XPS_Quest`         | Quest          | Varies  | Per quest   | Quest completion     |
| `XPS_DailyLogin`    | Daily Login    | 50      | Daily       | Login bonus          |
| `XPS_BattlePass`    | Battle Pass    | Varies  | Per tier    | BP challenge XP      |

---

### CurrencyType
Currency type with earning and spending context.

| Code Name         | Display Name | Earn Method | Max          | Use Case      |
| :---------------- | :----------- | :---------- | :----------- | :------------ |
| `CT_Credits`      | Credits      | Gameplay    | 999M         | Soft currency |
| `CT_Tokens`       | Tokens       | Purchase    | 999K         | Premium       |
| `CT_FactionRep`   | Faction Rep  | Quests      | 100K/faction | Standing      |
| `CT_BattlePassXP` | BP XP        | Challenges  | N/A          | BP Tiers      |
| `CT_OperatorXP`   | Operator XP  | Gameplay    | N/A          | Operator lvl  |
| `CT_AccountXP`    | Account XP   | Gameplay    | N/A          | Account lvl   |

---

### RewardType
Reward item classification.

| Code Name       | Display Name | Tradeable | Rarity Range   | Description          |
| :-------------- | :----------- | :-------- | :------------- | :------------------- |
| `RT_Currency`   | Currency     | No        | N/A            | Credits, Tokens, Rep |
| `RT_Item`       | Item         | Yes       | Common-Epic    | Weapons, gear        |
| `RT_Cosmetic`   | Cosmetic     | No        | Rare-Legendary | Skins, emotes        |
| `RT_Operator`   | Operator     | No        | Epic           | Character unlock     |
| `RT_Title`      | Title        | No        | Uncommon-Epic  | Name badges          |
| `RT_StashSlots` | Stash Slots  | No        | Rare           | Inventory expansion  |
| `RT_XPBooster`  | XP Booster   | No        | Uncommon       | Temp XP multiplier   |
| `RT_Blueprint`  | Blueprint    | No        | Rare-Epic      | Crafting recipes     |

---

### QuestType
Quest category with reset behavior.

| Code Name        | Display Name | Reset  | Count       | XP Range  | Description        |
| :--------------- | :----------- | :----- | :---------- | :-------- | :----------------- |
| `QT_Daily`       | Daily        | 24h    | 3           | 100-300   | Daily challenges   |
| `QT_Weekly`      | Weekly       | 7d     | 5           | 500-2000  | Weekly challenges  |
| `QT_Story`       | Story        | Never  | N/A         | 500-5000  | Main storyline     |
| `QT_Seasonal`    | Seasonal     | Season | 20          | 1000-5000 | Season challenges  |
| `QT_Faction`     | Faction      | Never  | Per faction | 200-1000  | Faction rep quests |
| `QT_BattlePass`  | Battle Pass  | Season | 50          | 100-500   | BP challenges      |
| `QT_Achievement` | Achievement  | Never  | 100+        | 500-10000 | Permanent goals    |

---

### QuestObjectiveType
Quest objective action type.

| Code Name           | Display Name | Example Target | Description            |
| :------------------ | :----------- | :------------- | :--------------------- |
| `QOT_Extract`       | Extract      | 3              | Extract X times        |
| `QOT_Kill`          | Kill         | 15             | Kill X enemies         |
| `QOT_Damage`        | Damage       | 10000          | Deal X damage          |
| `QOT_Loot`          | Loot         | 5000           | Loot X credit value    |
| `QOT_Complete`      | Complete     | 5              | Complete X matches     |
| `QOT_SurviveTime`   | Survive      | 30 min         | Survive X minutes      |
| `QOT_UseAbility`    | Ability      | 10             | Use ability X times    |
| `QOT_VisitLocation` | Visit        | 5 zones        | Visit specific areas   |
| `QOT_Collect`       | Collect      | 20             | Collect specific items |

---

### PrestigeRank
Prestige rank with visual border and XP bonus.

| Code Name       | Display Name | Border   | XP Bonus | Total XP Required |
| :-------------- | :----------- | :------- | :------- | :---------------- |
| `PR_None`       | None         | Default  | 0%       | 0                 |
| `PR_Prestige1`  | Prestige I   | Bronze   | +2%      | 1.5M              |
| `PR_Prestige2`  | Prestige II  | Silver   | +3%      | 3M                |
| `PR_Prestige3`  | Prestige III | Gold     | +4%      | 4.5M              |
| `PR_Prestige4`  | Prestige IV  | Platinum | +5%      | 6M                |
| `PR_Prestige5`  | Prestige V   | Diamond  | +6%      | 7.5M              |
| `PR_Prestige10` | Prestige X   | Rainbow  | +10%     | 15M               |

---

### MasteryRank
Weapon/operator mastery rank.

| Code Name     | Display Name | Points Required | Skin Unlock  |
| :------------ | :----------- | :-------------- | :----------- |
| `MR_Unranked` | Unranked     | 0               | None         |
| `MR_Bronze`   | Bronze       | 1,000           | Bronze skin  |
| `MR_Silver`   | Silver       | 5,000           | Silver skin  |
| `MR_Gold`     | Gold         | 15,000          | Gold skin    |
| `MR_Diamond`  | Diamond      | 50,000          | Diamond skin |

---

### FactionID
Faction identifier.

| Code Name                | Display Name        | Theme        | Primary Color |
| :----------------------- | :------------------ | :----------- | :------------ |
| `FID_SalvageCorps`       | Salvage Corps       | Industrial   | Orange        |
| `FID_TechSyndicate`      | Tech Syndicate      | Technology   | Cyan          |
| `FID_UndergroundNetwork` | Underground Network | Black Market | Purple        |
| `FID_Peacekeepers`       | Peacekeepers        | Military     | Blue          |

---

### FactionStanding
Faction reputation tier.

| Code Name     | Display Name | Rep Required | Discount |
| :------------ | :----------- | :----------- | :------- |
| `FS_Neutral`  | Neutral      | 0            | 0%       |
| `FS_Friendly` | Friendly     | 1,000        | 5%       |
| `FS_Honored`  | Honored      | 5,000        | 10%      |
| `FS_Revered`  | Revered      | 15,000       | 15%      |
| `FS_Exalted`  | Exalted      | 50,000       | 20%      |

---

## Code Names

### XP Events

| Code Name     | Trigger         | Parameters                  | Description             |
| :------------ | :-------------- | :-------------------------- | :---------------------- |
| `XP_GAINED`   | XP earned       | Amount, Source, Multiplier  | XP added to account     |
| `XP_LEVEL_UP` | Level increased | OldLevel, NewLevel, Rewards | Account level up        |
| `XP_PRESTIGE` | Prestige reset  | OldPrestige, NewPrestige    | Prestige rank increased |

### Currency Events

| Code Name               | Trigger         | Parameters              | Description       |
| :---------------------- | :-------------- | :---------------------- | :---------------- |
| `CURRENCY_ADD`          | Currency earned | Type, Amount, Source    | Currency added    |
| `CURRENCY_SPEND`        | Currency spent  | Type, Amount, ItemID    | Currency deducted |
| `CURRENCY_INSUFFICIENT` | Not enough      | Type, Required, Current | Purchase blocked  |

### Quest Events

| Code Name        | Trigger          | Parameters                     | Description |
| :--------------- | :--------------- | :----------------------------- | :---------- |
| `QUEST_ACCEPT`   | Quest started    | QuestID, Type                  | Quest added |
| `QUEST_PROGRESS` | Progress updated | QuestID, ObjectiveID, Progress | Progress    |
| `QUEST_COMPLETE` | Quest done       | QuestID, Rewards               | Completed   |
| `QUEST_RESET`    | Quests refreshed | Type                           | New quests  |

### Battle Pass Events

| Code Name         | Trigger        | Parameters              | Description    |
| :---------------- | :------------- | :---------------------- | :------------- |
| `BP_TIER_UP`      | Tier increased | OldTier, NewTier        | BP level up    |
| `BP_REWARD_CLAIM` | Reward claimed | Tier, RewardID, Premium | Reward claimed |
| `BP_SEASON_END`   | Season ended   | SeasonID, FinalTier     | Season end     |

---

## Architecture

### Class Diagram

```
                    ┌─────────────────────┐
                    │ ProgressionManager  │
                    │    (Singleton)      │
                    └─────────┬───────────┘
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                         │                         │
┌───▼─────────┐   ┌───────────▼───────────┐   ┌─────────▼───────┐
│  XPManager  │   │    CurrencyManager    │   │  QuestManager   │
│             │   │                       │   │                 │
└─────────────┘   └───────────────────────┘   └─────────────────┘
    │                         │                         │
    │         ┌───────────────┼───────────────┐        │
    │         │               │               │        │
    │   ┌─────▼─────┐  ┌──────▼──────┐  ┌─────▼─────┐ │
    │   │BattlePass │  │  Operator   │  │  Faction  │ │
    │   │  Manager  │  │ Progression │  │  Manager  │ │
    │   └───────────┘  └─────────────┘  └───────────┘ │
    │                                                   │
    └───────────────────────────────────────────────────┘
```

---

## Core Classes

### ProgressionManager

**Purpose:** Central progression controller.

```
CLASS ProgressionManager:
    STATIC instance: ProgressionManager
    
    // Account data
    accountLevel: Integer = 1
    accountXP: Integer = 0
    prestigeRank: PrestigeRank = PR_None
    
    // Sub-managers
    xpManager: XPManager
    currencyManager: CurrencyManager
    questManager: QuestManager
    battlePassManager: BattlePassManager
    operatorProgression: OperatorProgressionManager
    factionManager: FactionManager
    
    // Events
    OnLevelUp: Event<(oldLevel, newLevel, rewards)>
    OnPrestige: Event<(oldPrestige, newPrestige)>
    OnXPGained: Event<(amount, source)>
    
    FUNCTION Initialize():
        xpManager = NEW XPManager()
        currencyManager = NEW CurrencyManager()
        questManager = NEW QuestManager()
        battlePassManager = NEW BattlePassManager()
        operatorProgression = NEW OperatorProgressionManager()
        factionManager = NEW FactionManager()
        
        LoadPlayerData()
    END FUNCTION
    
    FUNCTION AddXP(amount: Integer, source: XPSource):
        // Apply multipliers
        finalAmount = xpManager.CalculateFinalXP(amount, source)
        
        accountXP += finalAmount
        
        EMIT EVENT "XP_GAINED" WITH (finalAmount, source, GetActiveMultiplier())
        
        // Check level up
        WHILE accountXP >= GetXPToNextLevel():
            LevelUp()
        END WHILE
    END FUNCTION
    
    FUNCTION LevelUp():
        oldLevel = accountLevel
        accountXP -= GetXPToNextLevel()
        accountLevel += 1
        
        // Grant rewards
        rewards = GetRewardsForLevel(accountLevel)
        GrantRewards(rewards)
        
        OnLevelUp.Broadcast(oldLevel, accountLevel, rewards)
        
        EMIT EVENT "XP_LEVEL_UP" WITH (oldLevel, accountLevel, rewards)
    END FUNCTION
    
    FUNCTION GetXPToNextLevel() -> Integer:
        // Formula: BaseXP * (1 + (Level-1) * GrowthRate)
        CONST BASE_XP = 1000
        CONST GROWTH_RATE = 0.15
        
        RETURN BASE_XP * (1 + (accountLevel - 1) * GROWTH_RATE)
    END FUNCTION
    
    FUNCTION GetLevelProgress() -> Float:
        RETURN accountXP / GetXPToNextLevel()
    END FUNCTION
    
    FUNCTION CanPrestige() -> Boolean:
        RETURN accountLevel >= 100 AND prestigeRank < PR_Prestige10
    END FUNCTION
    
    FUNCTION Prestige():
        IF NOT CanPrestige():
            RETURN
        END IF
        
        oldPrestige = prestigeRank
        prestigeRank = GetNextPrestigeRank(prestigeRank)
        
        // Reset level but keep items
        accountLevel = 1
        accountXP = 0
        
        // Grant prestige rewards
        rewards = GetPrestigeRewards(prestigeRank)
        GrantRewards(rewards)
        
        OnPrestige.Broadcast(oldPrestige, prestigeRank)
        
        EMIT EVENT "XP_PRESTIGE" WITH (oldPrestige, prestigeRank)
    END FUNCTION
    
    FUNCTION GetPrestigeXPBonus() -> Float:
        SWITCH prestigeRank:
            CASE PR_Prestige1: RETURN 0.02
            CASE PR_Prestige2: RETURN 0.03
            CASE PR_Prestige3: RETURN 0.04
            CASE PR_Prestige4: RETURN 0.05
            CASE PR_Prestige5: RETURN 0.06
            // ...
            CASE PR_Prestige10: RETURN 0.10
            DEFAULT: RETURN 0.0
        END SWITCH
    END FUNCTION
```

---

### XPManager

**Purpose:** XP calculation and boosters.

```
CLASS XPManager:
    // XP values per source
    CONST BASE_XP_VALUES = {
        XPS_MatchComplete: 100,
        XPS_Extraction: 200,
        XPS_Kill: 50,
        XPS_Assist: 25,
        XPS_Survival: 10,
        XPS_Loot: 1,
        XPS_DailyLogin: 50
    }
    
    // Active boosters
    activeBoosters: List<ActiveXPBooster>
    
    FUNCTION CalculateFinalXP(baseAmount: Integer, source: XPSource) -> Integer:
        amount = baseAmount
        
        // Apply source multiplier
        amount *= GetSourceMultiplier(source)
        
        // Apply prestige bonus
        amount *= (1.0 + GetPrestigeBonus())
        
        // Apply active boosters
        amount *= GetActiveBoosterMultiplier()
        
        // Apply event bonus (double XP weekends, etc)
        amount *= GetEventMultiplier()
        
        RETURN Round(amount)
    END FUNCTION
    
    FUNCTION CalculateMatchXP(matchData: MatchResultData) -> Integer:
        totalXP = BASE_XP_VALUES[XPS_MatchComplete]
        
        IF matchData.extracted:
            totalXP += BASE_XP_VALUES[XPS_Extraction]
        END IF
        
        totalXP += matchData.playerKills * BASE_XP_VALUES[XPS_Kill]
        totalXP += matchData.aiKills * (BASE_XP_VALUES[XPS_Kill] / 2)
        totalXP += matchData.assists * BASE_XP_VALUES[XPS_Assist]
        totalXP += matchData.survivalMinutes * BASE_XP_VALUES[XPS_Survival]
        totalXP += (matchData.lootValueExtracted / 100) * BASE_XP_VALUES[XPS_Loot]
        
        // Apply all multipliers
        totalXP = CalculateFinalXP(totalXP, XPS_MatchComplete)
        
        RETURN totalXP
    END FUNCTION
    
    FUNCTION AddXPBooster(multiplier: Float, durationSeconds: Float):
        booster = NEW ActiveXPBooster()
        booster.multiplier = multiplier
        booster.remainingTime = durationSeconds
        
        activeBoosters.Add(booster)
    END FUNCTION
    
    FUNCTION GetActiveBoosterMultiplier() -> Float:
        total = 1.0
        
        FOR EACH booster IN activeBoosters:
            total += (booster.multiplier - 1.0)
        END FOR
        
        RETURN total
    END FUNCTION
    
    FUNCTION UpdateBoosters(deltaTime: Float):
        FOR i = activeBoosters.Count - 1 DOWNTO 0:
            activeBoosters[i].remainingTime -= deltaTime
            
            IF activeBoosters[i].remainingTime <= 0:
                activeBoosters.RemoveAt(i)
            END IF
        END FOR
    END FUNCTION

STRUCT MatchResultData:
    extracted: Boolean
    playerKills: Integer
    aiKills: Integer
    assists: Integer
    survivalMinutes: Integer
    lootValueExtracted: Integer
    completedQuestIDs: List<String>
    isRanked: Boolean
```

---

### CurrencyManager

**Purpose:** Currency transactions and balance.

```
CLASS CurrencyManager:
    // Balances
    balances: Map<CurrencyType, Integer>
    
    // Transaction history
    transactionLog: List<CurrencyTransaction>
    
    // Events
    OnCurrencyChanged: Event<(type, oldBalance, newBalance)>
    OnInsufficientFunds: Event<(type, required, current)>
    
    FUNCTION Initialize():
        balances[CT_Credits] = 10000  // Starting credits
        balances[CT_Tokens] = 0
        
        FOR EACH faction IN GetAllFactions():
            balances[faction.repType] = 0
        END FOR
    END FUNCTION
    
    FUNCTION GetBalance(type: CurrencyType) -> Integer:
        RETURN balances[type] OR 0
    END FUNCTION
    
    FUNCTION HasEnough(type: CurrencyType, amount: Integer) -> Boolean:
        RETURN GetBalance(type) >= amount
    END FUNCTION
    
    FUNCTION AddCurrency(type: CurrencyType, amount: Integer, reason: String) -> Boolean:
        IF amount <= 0:
            RETURN false
        END IF
        
        oldBalance = GetBalance(type)
        newBalance = Min(oldBalance + amount, GetMaxBalance(type))
        
        balances[type] = newBalance
        
        LogTransaction(type, amount, reason, false)
        
        OnCurrencyChanged.Broadcast(type, oldBalance, newBalance)
        
        EMIT EVENT "CURRENCY_ADD" WITH (type, amount, reason)
        
        RETURN true
    END FUNCTION
    
    FUNCTION SpendCurrency(type: CurrencyType, amount: Integer, reason: String) -> Boolean:
        IF NOT HasEnough(type, amount):
            OnInsufficientFunds.Broadcast(type, amount, GetBalance(type))
            
            EMIT EVENT "CURRENCY_INSUFFICIENT" WITH (type, amount, GetBalance(type))
            
            RETURN false
        END IF
        
        oldBalance = GetBalance(type)
        newBalance = oldBalance - amount
        
        balances[type] = newBalance
        
        LogTransaction(type, amount, reason, true)
        
        OnCurrencyChanged.Broadcast(type, oldBalance, newBalance)
        
        EMIT EVENT "CURRENCY_SPEND" WITH (type, amount, reason)
        
        RETURN true
    END FUNCTION
    
    FUNCTION GetMaxBalance(type: CurrencyType) -> Integer:
        SWITCH type:
            CASE CT_Credits: RETURN 999999999
            CASE CT_Tokens: RETURN 999999
            CASE CT_FactionRep: RETURN 100000
            DEFAULT: RETURN MAX_INT
        END SWITCH
    END FUNCTION
    
    FUNCTION LogTransaction(type: CurrencyType, amount: Integer, reason: String, isSpend: Boolean):
        transaction = NEW CurrencyTransaction()
        transaction.type = type
        transaction.amount = amount
        transaction.reason = reason
        transaction.isSpend = isSpend
        transaction.timestamp = GetCurrentTime()
        transaction.balanceAfter = GetBalance(type)
        
        transactionLog.Add(transaction)
        
        // Keep only last 100 transactions
        IF transactionLog.Count > 100:
            transactionLog.RemoveAt(0)
        END IF
    END FUNCTION

STRUCT CurrencyTransaction:
    type: CurrencyType
    amount: Integer
    reason: String
    isSpend: Boolean
    timestamp: DateTime
    balanceAfter: Integer
```

---

### QuestManager

**Purpose:** Quest tracking and rewards.

```
CLASS QuestManager:
    // Quest data
    activeQuests: Map<String, ActiveQuest>
    completedQuestIDs: Set<String>
    
    // Daily/Weekly
    currentDailyIDs: List<String>
    currentWeeklyIDs: List<String>
    lastDailyReset: DateTime
    lastWeeklyReset: DateTime
    
    // Tracked quest
    trackedQuestID: String
    
    // Events
    OnQuestAccepted: Event<(questID, questType)>
    OnQuestProgress: Event<(questID, objectiveID, progress)>
    OnQuestComplete: Event<(questID, rewards)>
    OnDailyReset: Event<()>
    
    FUNCTION AcceptQuest(questID: String) -> Boolean:
        IF activeQuests.Contains(questID):
            RETURN false
        END IF
        
        questData = GetQuestData(questID)
        
        IF questData == null:
            RETURN false
        END IF
        
        IF questData.requiredLevel > GetAccountLevel():
            RETURN false
        END IF
        
        activeQuest = NEW ActiveQuest()
        activeQuest.questID = questID
        activeQuest.acceptedAt = GetCurrentTime()
        
        FOR EACH objective IN questData.objectives:
            activeQuest.objectiveProgress[objective.id] = 0
        END FOR
        
        activeQuests[questID] = activeQuest
        
        OnQuestAccepted.Broadcast(questID, questData.type)
        
        EMIT EVENT "QUEST_ACCEPT" WITH (questID, questData.type)
        
        RETURN true
    END FUNCTION
    
    FUNCTION UpdateProgress(objectiveType: String, amount: Integer, context: String = ""):
        FOR EACH (questID, quest) IN activeQuests:
            IF quest.isComplete:
                CONTINUE
            END IF
            
            questData = GetQuestData(questID)
            
            FOR EACH objective IN questData.objectives:
                IF objective.type == objectiveType:
                    IF context == "" OR objective.context == context:
                        oldProgress = quest.objectiveProgress[objective.id]
                        newProgress = Min(oldProgress + amount, objective.targetAmount)
                        quest.objectiveProgress[objective.id] = newProgress
                        
                        OnQuestProgress.Broadcast(questID, objective.id, newProgress)
                        
                        EMIT EVENT "QUEST_PROGRESS" WITH (questID, objective.id, newProgress)
                    END IF
                END IF
            END FOR
            
            CheckQuestCompletion(questID)
        END FOR
    END FUNCTION
    
    FUNCTION CheckQuestCompletion(questID: String):
        quest = activeQuests[questID]
        questData = GetQuestData(questID)
        
        allComplete = true
        
        FOR EACH objective IN questData.objectives:
            IF quest.objectiveProgress[objective.id] < objective.targetAmount:
                IF NOT objective.isOptional:
                    allComplete = false
                    BREAK
                END IF
            END IF
        END FOR
        
        IF allComplete:
            quest.isComplete = true
            GrantRewards(questData)
            
            completedQuestIDs.Add(questID)
            
            OnQuestComplete.Broadcast(questID, questData.rewards)
            
            EMIT EVENT "QUEST_COMPLETE" WITH (questID, questData.rewards)
        END IF
    END FUNCTION
    
    FUNCTION RefreshDailyQuests():
        // Remove old daily quests from active
        FOR EACH dailyID IN currentDailyIDs:
            activeQuests.Remove(dailyID)
        END FOR
        
        // Select 3 random daily quests
        currentDailyIDs = SelectRandomQuests(QT_Daily, 3)
        lastDailyReset = GetCurrentTime()
        
        OnDailyReset.Broadcast()
        
        EMIT EVENT "QUEST_RESET" WITH (QT_Daily)
    END FUNCTION
    
    FUNCTION GetDailyResetTime() -> TimeSpan:
        nextReset = GetNextMidnightUTC()
        RETURN nextReset - GetCurrentTime()
    END FUNCTION
    
    FUNCTION GetWeeklyResetTime() -> TimeSpan:
        nextReset = GetNextMondayMidnightUTC()
        RETURN nextReset - GetCurrentTime()
    END FUNCTION

STRUCT ActiveQuest:
    questID: String
    objectiveProgress: Map<String, Integer>
    acceptedAt: DateTime
    isComplete: Boolean = false
    rewardClaimed: Boolean = false

STRUCT QuestData:
    questID: String
    type: QuestType
    title: String
    description: String
    objectives: List<QuestObjective>
    rewards: List<RewardData>
    requiredLevel: Integer = 0
    prerequisiteQuestID: String
    factionID: FactionID
    isRepeatable: Boolean = false

STRUCT QuestObjective:
    id: String
    type: QuestObjectiveType
    description: String
    targetAmount: Integer
    context: String
    isOptional: Boolean = false
```

---

### BattlePassManager

**Purpose:** Battle Pass progression and rewards.

```
CLASS BattlePassManager:
    // Configuration
    CONST MAX_TIERS = 100
    CONST XP_PER_TIER = 1000
    CONST PREMIUM_COST_TOKENS = 1000
    CONST SEASON_DURATION_DAYS = 90
    
    // State
    currentSeasonID: String
    currentTier: Integer = 1
    currentXP: Integer = 0
    premiumUnlocked: Boolean = false
    
    claimedFreeTiers: Set<Integer>
    claimedPremiumTiers: Set<Integer>
    
    // Events
    OnTierUp: Event<(oldTier, newTier)>
    OnRewardClaimed: Event<(tier, rewardID, isPremium)>
    OnSeasonEnd: Event<(seasonID, finalTier)>
    
    FUNCTION AddBattlePassXP(amount: Integer, source: String):
        currentXP += amount
        
        WHILE currentXP >= XP_PER_TIER AND currentTier < MAX_TIERS:
            TierUp()
        END WHILE
    END FUNCTION
    
    FUNCTION TierUp():
        oldTier = currentTier
        currentXP -= XP_PER_TIER
        currentTier += 1
        
        OnTierUp.Broadcast(oldTier, currentTier)
        
        EMIT EVENT "BP_TIER_UP" WITH (oldTier, currentTier)
    END FUNCTION
    
    FUNCTION GetTierProgress() -> Float:
        RETURN currentXP / XP_PER_TIER
    END FUNCTION
    
    FUNCTION IsPremiumUnlocked() -> Boolean:
        RETURN premiumUnlocked
    END FUNCTION
    
    FUNCTION UnlockPremium() -> Boolean:
        IF premiumUnlocked:
            RETURN false
        END IF
        
        IF NOT CurrencyManager.SpendCurrency(CT_Tokens, PREMIUM_COST_TOKENS, "Battle Pass Premium"):
            RETURN false
        END IF
        
        premiumUnlocked = true
        
        RETURN true
    END FUNCTION
    
    FUNCTION CanClaimReward(tier: Integer, isPremium: Boolean) -> Boolean:
        IF tier > currentTier:
            RETURN false
        END IF
        
        IF isPremium AND NOT premiumUnlocked:
            RETURN false
        END IF
        
        IF isPremium:
            RETURN NOT claimedPremiumTiers.Contains(tier)
        ELSE:
            RETURN NOT claimedFreeTiers.Contains(tier)
        END IF
    END FUNCTION
    
    FUNCTION ClaimReward(tier: Integer, isPremium: Boolean) -> Boolean:
        IF NOT CanClaimReward(tier, isPremium):
            RETURN false
        END IF
        
        reward = GetRewardForTier(tier, isPremium)
        
        IF reward == null:
            RETURN false
        END IF
        
        GrantReward(reward)
        
        IF isPremium:
            claimedPremiumTiers.Add(tier)
        ELSE:
            claimedFreeTiers.Add(tier)
        END IF
        
        OnRewardClaimed.Broadcast(tier, reward.itemID, isPremium)
        
        EMIT EVENT "BP_REWARD_CLAIM" WITH (tier, reward.itemID, isPremium)
        
        RETURN true
    END FUNCTION
    
    FUNCTION GetSeasonTimeRemaining() -> TimeSpan:
        seasonEnd = GetSeasonEndDate(currentSeasonID)
        RETURN seasonEnd - GetCurrentTime()
    END FUNCTION
    
    FUNCTION GetActiveChallenges() -> List<BattlePassChallenge>:
        // Return current week's challenges
        currentWeek = GetCurrentWeekOfSeason()
        RETURN challenges.Where(c => c.week == currentWeek AND NOT c.isComplete)
    END FUNCTION

STRUCT BattlePassReward:
    tier: Integer
    isPremium: Boolean
    type: RewardType
    itemID: String
    amount: Integer
    rarity: Rarity

STRUCT BattlePassChallenge:
    challengeID: String
    description: String
    targetAmount: Integer
    currentProgress: Integer
    xpReward: Integer
    week: Integer
    isComplete: Boolean
```

---

### OperatorProgressionManager

**Purpose:** Individual operator progression.

```
CLASS OperatorProgressionManager:
    // Operator data
    operatorProgress: Map<String, OperatorProgressData>
    
    // Events
    OnOperatorLevelUp: Event<(operatorID, newLevel)>
    OnMasteryRankUp: Event<(operatorID, oldRank, newRank)>
    
    FUNCTION GetOperatorLevel(operatorID: String) -> Integer:
        data = GetOperatorData(operatorID)
        RETURN data?.level OR 1
    END FUNCTION
    
    FUNCTION GetOperatorXP(operatorID: String) -> Integer:
        data = GetOperatorData(operatorID)
        RETURN data?.xp OR 0
    END FUNCTION
    
    FUNCTION AddOperatorXP(operatorID: String, amount: Integer):
        data = GetOrCreateOperatorData(operatorID)
        
        data.xp += amount
        
        WHILE data.xp >= GetXPForNextOperatorLevel(data.level):
            OperatorLevelUp(operatorID, data)
        END WHILE
    END FUNCTION
    
    FUNCTION OperatorLevelUp(operatorID: String, data: OperatorProgressData):
        data.xp -= GetXPForNextOperatorLevel(data.level)
        data.level += 1
        
        // Grant level unlock
        unlock = GetUnlockForLevel(operatorID, data.level)
        
        IF unlock != null:
            GrantUnlock(operatorID, unlock)
        END IF
        
        OnOperatorLevelUp.Broadcast(operatorID, data.level)
        
        EMIT EVENT "OPERATOR_LEVEL_UP" WITH (operatorID, data.level)
    END FUNCTION
    
    FUNCTION GetMasteryRank(operatorID: String) -> MasteryRank:
        data = GetOperatorData(operatorID)
        
        IF data == null:
            RETURN MR_Unranked
        END IF
        
        IF data.masteryPoints >= 50000:
            RETURN MR_Diamond
        ELSE IF data.masteryPoints >= 15000:
            RETURN MR_Gold
        ELSE IF data.masteryPoints >= 5000:
            RETURN MR_Silver
        ELSE IF data.masteryPoints >= 1000:
            RETURN MR_Bronze
        ELSE:
            RETURN MR_Unranked
        END IF
    END FUNCTION
    
    FUNCTION AddMasteryPoints(operatorID: String, amount: Integer):
        data = GetOrCreateOperatorData(operatorID)
        
        oldRank = GetMasteryRank(operatorID)
        data.masteryPoints += amount
        newRank = GetMasteryRank(operatorID)
        
        IF newRank != oldRank:
            OnMasteryRankUp.Broadcast(operatorID, oldRank, newRank)
            
            EMIT EVENT "MASTERY_RANK_UP" WITH (operatorID, oldRank, newRank)
        END IF
    END FUNCTION

STRUCT OperatorProgressData:
    level: Integer = 1
    xp: Integer = 0
    masteryPoints: Integer = 0
    unlockedAbilitySlots: List<Integer>
    unlockedSkins: List<String>

// Operator level unlock milestones
CONST OPERATOR_LEVEL_UNLOCKS = {
    5:  { type: RT_AbilitySlot, id: "SLOT_1", desc: "Ability Upgrade Slot 1" },
    10: { type: RT_Cosmetic, id: "SKIN_COMMON", desc: "Operator Skin 1" },
    15: { type: RT_StatBoost, id: "HEALTH_5", desc: "+5% Max Health" },
    20: { type: RT_AbilitySlot, id: "SLOT_2", desc: "Ability Upgrade Slot 2" },
    25: { type: RT_Cosmetic, id: "SKIN_RARE", desc: "Operator Skin 2 (Rare)" },
    50: { type: RT_Cosmetic, id: "SKIN_LEGENDARY", desc: "Prestige Skin (Legendary)" }
}
```

---

### FactionManager

**Purpose:** Faction reputation and unlocks.

```
CLASS FactionManager:
    // Reputation
    factionReputations: Map<FactionID, Integer>
    
    // Events
    OnReputationChanged: Event<(faction, oldRep, newRep)>
    OnStandingChanged: Event<(faction, oldStanding, newStanding)>
    
    FUNCTION GetReputation(faction: FactionID) -> Integer:
        RETURN factionReputations[faction] OR 0
    END FUNCTION
    
    FUNCTION GetStanding(faction: FactionID) -> FactionStanding:
        rep = GetReputation(faction)
        
        IF rep >= 50000:
            RETURN FS_Exalted
        ELSE IF rep >= 15000:
            RETURN FS_Revered
        ELSE IF rep >= 5000:
            RETURN FS_Honored
        ELSE IF rep >= 1000:
            RETURN FS_Friendly
        ELSE:
            RETURN FS_Neutral
        END IF
    END FUNCTION
    
    FUNCTION AddReputation(faction: FactionID, amount: Integer, reason: String):
        oldRep = GetReputation(faction)
        oldStanding = GetStanding(faction)
        
        newRep = Min(oldRep + amount, 100000)
        factionReputations[faction] = newRep
        
        newStanding = GetStanding(faction)
        
        OnReputationChanged.Broadcast(faction, oldRep, newRep)
        
        IF newStanding != oldStanding:
            OnStandingChanged.Broadcast(faction, oldStanding, newStanding)
        END IF
    END FUNCTION
    
    FUNCTION GetReputationProgress(faction: FactionID) -> Float:
        rep = GetReputation(faction)
        standing = GetStanding(faction)
        
        currentThreshold = GetThresholdForStanding(standing)
        nextThreshold = GetThresholdForStanding(GetNextStanding(standing))
        
        IF nextThreshold == currentThreshold:
            RETURN 1.0  // Max standing
        END IF
        
        RETURN (rep - currentThreshold) / (nextThreshold - currentThreshold)
    END FUNCTION
    
    FUNCTION GetFactionDiscount(faction: FactionID) -> Float:
        SWITCH GetStanding(faction):
            CASE FS_Neutral: RETURN 0.0
            CASE FS_Friendly: RETURN 0.05
            CASE FS_Honored: RETURN 0.10
            CASE FS_Revered: RETURN 0.15
            CASE FS_Exalted: RETURN 0.20
        END SWITCH
    END FUNCTION
    
    FUNCTION CanPurchaseFactionItem(faction: FactionID, itemID: String) -> Boolean:
        unlock = GetFactionUnlock(faction, itemID)
        
        IF unlock == null:
            RETURN false
        END IF
        
        currentStanding = GetStanding(faction)
        
        RETURN currentStanding >= unlock.requiredStanding
    END FUNCTION
```

---

### DailyLoginManager

**Purpose:** Daily login rewards and streaks.

```
CLASS DailyLoginManager:
    // State
    currentStreak: Integer = 0
    lastLoginDate: DateTime
    monthlyLoginCount: Integer = 0
    
    // 7-day cycle rewards
    CONST DAILY_CYCLE_REWARDS = [
        { day: 1, rewards: [{ type: CT_Credits, amount: 500 }] },
        { day: 2, rewards: [{ type: CT_Credits, amount: 750 }] },
        { day: 3, rewards: [{ type: CT_Credits, amount: 1000 }, { type: RT_Cosmetic, id: "SKIN_COMMON" }] },
        { day: 4, rewards: [{ type: CT_Credits, amount: 1500 }] },
        { day: 5, rewards: [{ type: CT_Credits, amount: 2000 }, { type: RT_Cosmetic, id: "SKIN_RARE" }] },
        { day: 6, rewards: [{ type: CT_Credits, amount: 2500 }] },
        { day: 7, rewards: [{ type: CT_Credits, amount: 5000 }, { type: CT_Tokens, amount: 100 }] }
    ]
    
    FUNCTION CheckDailyLogin():
        today = GetCurrentDate()
        
        IF lastLoginDate == null:
            // First login ever
            currentStreak = 1
        ELSE IF today == lastLoginDate:
            // Already logged in today
            RETURN
        ELSE IF today == lastLoginDate + 1 day:
            // Consecutive day
            currentStreak += 1
        ELSE:
            // Streak broken
            currentStreak = 1
        END IF
        
        lastLoginDate = today
        monthlyLoginCount += 1
        
        // Grant daily reward
        GrantDailyReward()
        
        // Check monthly milestone
        CheckMonthlyMilestone()
    END FUNCTION
    
    FUNCTION GetDayInCycle() -> Integer:
        // Returns 1-7 based on current streak
        RETURN ((currentStreak - 1) MOD 7) + 1
    END FUNCTION
    
    FUNCTION GetTodayReward() -> DailyReward:
        day = GetDayInCycle()
        RETURN DAILY_CYCLE_REWARDS[day - 1]
    END FUNCTION
    
    FUNCTION GrantDailyReward():
        reward = GetTodayReward()
        
        FOR EACH item IN reward.rewards:
            GrantRewardItem(item)
        END FOR
    END FUNCTION
    
    FUNCTION CheckMonthlyMilestone():
        // Monthly cumulative rewards
        CONST MONTHLY_MILESTONES = {
            7:  { desc: "Week 1", rewards: [{ type: CT_Credits, amount: 5000 }] },
            14: { desc: "Week 2", rewards: [{ type: RT_XPBooster, amount: 1 }] },
            21: { desc: "Week 3", rewards: [{ type: CT_Tokens, amount: 50 }] },
            30: { desc: "Month", rewards: [{ type: RT_Cosmetic, id: "OP_SKIN_MONTHLY" }] }
        }
        
        IF MONTHLY_MILESTONES.Contains(monthlyLoginCount):
            milestone = MONTHLY_MILESTONES[monthlyLoginCount]
            
            FOR EACH reward IN milestone.rewards:
                GrantRewardItem(reward)
            END FOR
        END IF
    END FUNCTION
```

---

## TODO: Implementation Tasks

### HIGH Priority 
- [ ] ProgressionManager core
- [ ] XPManager with calculation
- [ ] CurrencyManager with transactions
- [ ] QuestManager with daily/weekly
- [ ] Level up flow with rewards

### MEDIUM Priority 
- [ ] BattlePassManager
- [ ] OperatorProgressionManager
- [ ] FactionManager
- [ ] Prestige system
- [ ] Mastery system

### LOW Priority 
- [ ] DailyLoginManager
- [ ] LevelRewardManager
- [ ] Achievement integration
- [ ] Leaderboard integration
- [ ] Analytics events

---

## Testing Checklist

- [ ] XP calculates correctly per source
- [ ] Level up triggers at correct XP
- [ ] Prestige resets level but keeps items
- [ ] Currencies add/spend correctly
- [ ] Daily quests reset at midnight
- [ ] Weekly quests reset on Monday
- [ ] Quest progress tracks correctly
- [ ] Quest rewards grant properly
- [ ] Battle Pass tiers up correctly
- [ ] Premium rewards only for premium
- [ ] Operator XP separate from account
- [ ] Faction rep increases correctly
- [ ] Daily login streak tracks
- [ ] No duplicate reward claims



