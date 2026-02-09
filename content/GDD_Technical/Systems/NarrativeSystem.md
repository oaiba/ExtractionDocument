---
title: "Narrative System - Technical Specification"
type: docs
---

## Overview

The **Narrative System** manages quests, faction reputation, dialogue, collectibles, and operator backstory progression. Designed for environmental storytelling with minimal UI interruption.

**Responsibilities:**
- Quest tracking and progression
- Faction reputation and unlocks
- Dialogue and voice line management
- Audio log collectibles
- Operator personal storylines
- Environmental narrative triggers
- Localized text delivery
- Quest item management

---

## Enums & Types

### QuestType
Quest category determining reset behavior and source.

| Code Name        | Display Name   | Reset     | Max Active | Source   | Description                       |
| :--------------- | :------------- | :-------- | :--------- | :------- | :-------------------------------- |
| `QT_Faction`     | Faction Quest  | Never     | 3          | NPC      | Given by faction representatives  |
| `QT_Personal`    | Personal Quest | Never     | 1          | Operator | Operator backstory progression    |
| `QT_Tutorial`    | Tutorial Quest | Once      | 1          | System   | Onboarding quests for new players |
| `QT_Daily`       | Daily Quest    | 24h       | 3          | System   | Daily rotating challenges         |
| `QT_Weekly`      | Weekly Quest   | 7d        | 5          | System   | Weekly rotating challenges        |
| `QT_Event`       | Event Quest    | Event end | 5          | Event    | Limited-time event quests         |
| `QT_Hidden`      | Hidden Quest   | Never     | N/A        | World    | Discovered through exploration    |
| `QT_Achievement` | Achievement    | Never     | N/A        | System   | Long-term permanent goals         |

---

### QuestState
Current state of a quest in the player's log.

| Code Name            | Display Name | UI Display   | Actions   | Description                      |
| :------------------- | :----------- | :----------- | :-------- | :------------------------------- |
| `QS_Locked`          | Locked       | Grayed out   | None      | Prerequisites not met            |
| `QS_Available`       | Available    | "!" icon     | Accept    | Can be accepted                  |
| `QS_Active`          | Active       | Progress bar | Track     | Currently in progress            |
| `QS_ReadyToComplete` | Ready        | "✓" icon     | Complete  | Objectives done, needs turn-in   |
| `QS_Completed`       | Completed    | Checkmark    | None      | Finished and rewarded            |
| `QS_Failed`          | Failed       | "X" icon     | Retry     | Time expired or failed condition |
| `QS_Abandoned`       | Abandoned    | None         | Re-accept | Player cancelled                 |

---

### QuestObjectiveType
Quest objective action type for progress tracking.

| Code Name             | Display Name    | Context   | Example              | Description                        |
| :-------------------- | :-------------- | :-------- | :------------------- | :--------------------------------- |
| `QOT_Collect`         | Collect         | ItemID    | 10 Scrap Metal       | Gather specific items              |
| `QOT_Kill`            | Kill            | EnemyType | 15 Scavengers        | Kill enemy count                   |
| `QOT_KillSpecific`    | Kill Specific   | BossID    | Kill Warden          | Kill specific enemy/boss           |
| `QOT_Extract`         | Extract         | None      | Extract 3 times      | Successfully extract               |
| `QOT_ExtractWithLoot` | Extract w/ Loot | Value     | Extract with $5000   | Extract with loot value            |
| `QOT_VisitZone`       | Visit Zone      | ZoneID    | Visit Power Plant    | Visit specific zone                |
| `QOT_Interact`        | Interact        | ObjectID  | Hack Terminal        | Interact with object               |
| `QOT_Escort`          | Escort          | NPCID     | Protect Data Courier | Protect NPC/item                   |
| `QOT_Survive`         | Survive         | Minutes   | Survive 10 min       | Survive time in match              |
| `QOT_Hack`            | Hack            | None      | Hack 3 Terminals     | Hack terminal count                |
| `QOT_Deliver`         | Deliver         | Location  | Bring to NPC         | Bring item to location             |
| `QOT_Photograph`      | Photograph      | ObjectID  | Scan Intel           | Scan/photo specific object         |
| `QOT_NoCondition`     | No Condition    | Condition | Without dying        | Complete without failing condition |

---

### Faction
Faction identity with colors and theme.

| Code Name              | Display Name        | Primary Color | Secondary | Leader          | Description                      |
| :--------------------- | :------------------ | :------------ | :-------- | :-------------- | :------------------------------- |
| `F_SalvageCorps`       | Salvage Corps       | Orange        | Gray      | Viktor Koval    | Industrial workers, honest trade |
| `F_TechSyndicate`      | Tech Syndicate      | Cyan          | Black     | The Node        | Hackers, tech specialists        |
| `F_UndergroundNetwork` | Underground Network | Purple        | Gold      | The Broker      | Black market dealers             |
| `F_Peacekeepers`       | Peacekeepers        | Blue          | White     | Commander Reyes | Military remnants, order         |

---

### ReputationLevel
Faction standing tier with unlocks.

| Code Name    | Display Name | Rep Range   | Discount   | Quests | Description               |
| :----------- | :----------- | :---------- | :--------- | :----- | :------------------------ |
| `RL_Hostile` | Hostile      | -1000 to -1 | +50% price | Locked | Locked out, must repair   |
| `RL_Neutral` | Neutral      | 0           | 0%         | Basic  | Starting reputation       |
| `RL_Level1`  | Newcomer     | 100-499     | 0%         | Tier 1 | First standing tier       |
| `RL_Level2`  | Trusted      | 500-1499    | 5%         | Tier 2 | Access to vendor items    |
| `RL_Level3`  | Honored      | 1500-2999   | 10%        | Tier 3 | Special gear unlocks      |
| `RL_Level4`  | Inner Circle | 3000-4999   | 15%        | Tier 4 | Exclusive cosmetics       |
| `RL_Level5`  | Veteran      | 5000+       | 20%        | All    | Max standing, all unlocks |

---

### DialogueType
Voice line context and priority.

| Code Name            | Display Name     | Priority | Cooldown | Subtitle | Description               |
| :------------------- | :--------------- | :------- | :------- | :------- | :------------------------ |
| `DT_QuestGiver`      | Quest Giver      | Critical | 0s       | Yes      | NPC dialogue for quests   |
| `DT_CombatCallout`   | Combat Callout   | High     | 3s       | Brief    | Short combat voice lines  |
| `DT_CharacterMoment` | Character Moment | Low      | 30s      | Yes      | Ambient personality lines |
| `DT_SquadComm`       | Squad Comm       | High     | 2s       | Brief    | Team communication        |
| `DT_Ping`            | Ping             | Medium   | 1s       | No       | Ping responses            |
| `DT_Hurt`            | Hurt             | Critical | 2s       | No       | Damage reactions          |
| `DT_Death`           | Death            | Critical | 0s       | No       | Death voice lines         |
| `DT_Revival`         | Revival          | High     | 5s       | Brief    | Revive voice lines        |
| `DT_Extraction`      | Extraction       | High     | 5s       | Yes      | Extraction callouts       |
| `DT_Loot`            | Loot             | Medium   | 10s      | Brief    | Finding items             |
| `DT_Environmental`   | Environmental    | Low      | 60s      | Yes      | Zone-specific comments    |

---

### CollectibleType
Collectible item category for codex.

| Code Name           | Display Name   | Duration | XP Reward | Codex Category | Description                      |
| :------------------ | :------------- | :------- | :-------- | :------------- | :------------------------------- |
| `CLT_AudioLog`      | Audio Log      | 30-60s   | 100 XP    | Recordings     | Voice recordings with lore       |
| `CLT_Document`      | Document       | N/A      | 50 XP     | Files          | Text-based lore documents        |
| `CLT_Photo`         | Photo          | N/A      | 25 XP     | Gallery        | Image collectibles               |
| `CLT_Artifact`      | Artifact       | N/A      | 150 XP    | Artifacts      | Physical object collectibles     |
| `CLT_IntelFragment` | Intel Fragment | N/A      | 75 XP     | Intel          | Pieced together lore (3-5 parts) |

---

## Code Names

### Quest Events

| Code Name                  | Trigger             | Parameters                     | Description                |
| :------------------------- | :------------------ | :----------------------------- | :------------------------- |
| `QUEST_ACCEPT`             | Player accepts      | QuestID                        | Quest added to active      |
| `QUEST_PROGRESS`           | Objective updated   | QuestID, ObjectiveID, Progress | Progress toward objective  |
| `QUEST_OBJECTIVE_COMPLETE` | Objective done      | QuestID, ObjectiveID           | Single objective completed |
| `QUEST_AVAILABLE`          | Prerequisites met   | QuestID                        | Quest now available        |
| `QUEST_COMPLETE`           | All objectives done | QuestID, Rewards               | Quest completed            |
| `QUEST_FAIL`               | Failure condition   | QuestID, Reason                | Quest failed               |
| `QUEST_ABANDON`            | Player cancels      | QuestID                        | Quest abandoned            |

### Faction Events

| Code Name          | Trigger        | Parameters                    | Description          |
| :----------------- | :------------- | :---------------------------- | :------------------- |
| `FACTION_REP_GAIN` | Rep earned     | FactionID, Amount, Source     | Reputation increased |
| `FACTION_REP_LOSS` | Rep lost       | FactionID, Amount, Reason     | Reputation decreased |
| `FACTION_LEVEL_UP` | Tier increased | FactionID, OldLevel, NewLevel | Faction level up     |
| `FACTION_UNLOCK`   | Item unlocked  | FactionID, UnlockID           | New item available   |

### Dialogue Events

| Code Name           | Trigger           | Parameters                | Description                |
| :------------------ | :---------------- | :------------------------ | :------------------------- |
| `DIALOGUE_TRIGGER`  | Dialogue started  | DialogueID, SpeakerID     | Dialogue sequence began    |
| `DIALOGUE_COMPLETE` | Dialogue ended    | DialogueID                | Dialogue sequence finished |
| `VOICELINE_PLAY`    | Voice line played | OperatorID, LineID        | Voice line started         |
| `VOICELINE_QUEUE`   | Voice line queued | OperatorID, LineID, Delay | Voice line added to queue  |

### Collectible Events

| Code Name           | Trigger         | Parameters          | Description               |
| :------------------ | :-------------- | :------------------ | :------------------------ |
| `COLLECTIBLE_FOUND` | Item discovered | CollectibleID, Type | Collectible picked up     |
| `COLLECTIBLE_PLAY`  | Audio played    | CollectibleID       | Audio log played          |
| `LORE_UNLOCK`       | Lore completed  | LoreID, Category    | Lore entry unlocked       |
| `CODEX_UPDATE`      | Codex updated   | Category, EntryID   | Codex entry added/updated |

---

## Architecture

### Class Diagram

```
                    ┌─────────────────┐
                    │NarrativeManager │
                    │  (Singleton)    │
                    └────────┬────────┘
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
┌───▼───────┐    ┌───────────▼───────────┐    ┌───────▼───────┐
│QuestManager│   │  FactionManager       │    │DialogueManager│
│            │   │                       │    │               │
└────────────┘   └───────────────────────┘    └───────────────┘
    │                        │                        │
    │            ┌───────────┼───────────┐            │
    │            │           │           │            │
    │    ┌───────▼───┐ ┌─────▼────┐ ┌────▼────┐       │
    │    │Collectible│ │ Codex    │ │VoiceLine│       │
    │    │ Manager   │ │ Manager  │ │ Manager │       │
    │    └───────────┘ └──────────┘ └─────────┘       │
    │                                                 │
    └─────────────────────────────────────────────────┘
```

---

## Core Classes

### NarrativeManager

**Purpose:** Central narrative controller.

```
CLASS NarrativeManager:
    STATIC instance: NarrativeManager

    // Sub-managers
    questManager: QuestManager
    factionManager: FactionManager
    dialogueManager: DialogueManager
    collectibleManager: CollectibleManager
    codexManager: CodexManager

    FUNCTION Initialize():
        questManager.Initialize()
        factionManager.Initialize()
        // ...
    END FUNCTION

    // Global Event Handlers
    FUNCTION OnMatchComplete(result: MatchResult):
        questManager.ProcessMatchResult(result)
    END FUNCTION
    
    FUNCTION OnItemCollected(itemID: String):
        questManager.UpdateProgress(QOT_Collect, 1, itemID)
        collectibleManager.OnItemFound(itemID)
    END FUNCTION
    
    FUNCTION OnEnemyKilled(enemyID: String, weaponID: String):
        questManager.UpdateProgress(QOT_Kill, 1, enemyID)
    END FUNCTION
    
    FUNCTION OnZoneEntered(zoneID: String):
        questManager.UpdateProgress(QOT_VisitZone, 1, zoneID)
    END FUNCTION
```

---

### QuestManager

**Purpose:** Quest lifecycle management.

```
CLASS QuestManager:
    allQuests: List<QuestData>
    acceptedQuests: Map<String, QuestData>
    completedQuests: Set<String>
    trackedQuestID: String
    maxActiveQuests: Integer = 5
    
    // Events
    OnQuestStateChanged: Event<(QuestID, NewState)>
    OnQuestProgress: Event<(QuestID, ObjectiveID, Current, Target)>
    OnQuestComplete: Event<(QuestID, Rewards)>

    FUNCTION GetAvailableQuests() -> List<QuestData>:
        available = []
        FOR EACH quest IN allQuests:
            IF quest.CurrentState == QS_Available:
                available.Add(quest)
            END IF
        END FOR
        RETURN available
    END FUNCTION
    
    FUNCTION AcceptQuest(questID: String) -> Boolean:
        IF acceptedQuests.Count >= maxActiveQuests:
             RETURN false
        END IF
        
        quest = GetQuestByID(questID)
        quest.CurrentState = QS_Active
        acceptedQuests[questID] = quest
        
        EMIT EVENT "QUEST_ACCEPT" WITH (questID)
        OnQuestStateChanged.Broadcast(questID, QS_Active)
        
        RETURN true
    END FUNCTION
    
    FUNCTION UpdateProgress(type: QuestObjectiveType, amount: Integer, context: String):
        FOR EACH quest IN acceptedQuests.Values:
             FOR EACH objective IN quest.Objectives:
                 IF objective.Type == type AND objective.TargetID == context AND NOT objective.bComplete:
                     objective.CurrentAmount += amount
                     
                     EMIT EVENT "QUEST_PROGRESS" WITH (quest.QuestID, objective.ObjectiveID, objective.CurrentAmount)
                     OnQuestProgress.Broadcast(quest.QuestID, objective.ObjectiveID, objective.CurrentAmount, objective.TargetAmount)
                     
                     IF objective.CurrentAmount >= objective.TargetAmount:
                         objective.bComplete = true
                         EMIT EVENT "QUEST_OBJECTIVE_COMPLETE" WITH (quest.QuestID, objective.ObjectiveID)
                         CheckQuestCompletion(quest)
                     END IF
                 END IF
             END FOR
        END FOR
    END FUNCTION
    
    FUNCTION CheckQuestCompletion(quest: QuestData):
        IF quest.AreAllObjectivesComplete():
            quest.CurrentState = QS_ReadyToComplete
            OnQuestStateChanged.Broadcast(quest.QuestID, QS_ReadyToComplete)
        END IF
    END FUNCTION
    
    FUNCTION CompleteQuest(questID: String):
        quest = acceptedQuests[questID]
        IF quest.CurrentState == QS_ReadyToComplete:
            quest.CurrentState = QS_Completed
            acceptedQuests.Remove(questID)
            completedQuests.Add(questID)
            
            GrantRewards(quest)
            
            EMIT EVENT "QUEST_COMPLETE" WITH (questID, quest.Rewards)
            OnQuestComplete.Broadcast(questID, quest.Rewards)
        END IF
    END FUNCTION
```

---

### FactionManager

**Purpose:** Reputation and faction progression.

```
CLASS FactionManager:
    factionReputation: Map<Faction, Integer>
    unlockedItems: Map<Faction, List<String>>

    // Events
    OnReputationChanged: Event<(Faction, NewAmount)>
    OnLevelUp: Event<(Faction, NewLevel)>

    FUNCTION GetReputation(faction: Faction) -> Integer:
        RETURN factionReputation.GetOrDefault(faction, 0)
    END FUNCTION
    
    FUNCTION GetReputationLevel(faction: Faction) -> ReputationLevel:
        rep = GetReputation(faction)
        // Check ranges
        IF rep >= 5000: RETURN RL_Level5
        IF rep >= 3000: RETURN RL_Level4
        // ...
        RETURN RL_Neutral
    END FUNCTION
    
    FUNCTION AddReputation(faction: Faction, amount: Integer):
        current = GetReputation(faction)
        newAmount = current + amount
        factionReputation[faction] = newAmount
        
        oldLevel = GetReputationLevel(faction) // based on current
        // update map
        
        newLevel = GetReputationLevel(faction) // based on newAmount
        
        EMIT EVENT "FACTION_REP_GAIN" WITH (faction, amount)
        OnReputationChanged.Broadcast(faction, newAmount)
        
        IF newLevel > oldLevel:
             EMIT EVENT "FACTION_LEVEL_UP" WITH (faction, oldLevel, newLevel)
             OnLevelUp.Broadcast(faction, newLevel)
             UnlockTierRewards(faction, newLevel)
        END IF
    END FUNCTION
```

---

### DialogueManager

**Purpose:** Dialogue playback and voice lines.

```
CLASS DialogueManager:
    voiceLineQueue: List<QueuedVoiceLine>
    currentDialogueID: String
    voiceLineCooldowns: Map<String, Float>
    defaultVoiceLineCooldown: Float = 5.0
    
    FUNCTION PlayDialogue(dialogueID: String):
        currentDialogueID = dialogueID
        EMIT EVENT "DIALOGUE_TRIGGER" WITH (dialogueID)
        // Trigger UI display
    END FUNCTION
    
    FUNCTION QueueVoiceLine(operatorID: String, type: DialogueType, delay: Float = 0.0):
        line = SelectLine(operatorID, type)
        IF line != null:
             queuedLine = NEW QueuedVoiceLine(line, delay)
             voiceLineQueue.Add(queuedLine)
             EMIT EVENT "VOICELINE_QUEUE" WITH (operatorID, line.LineID, delay)
        END IF
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        // Process queue
        IF voiceLineQueue.HasItems():
            nextLine = voiceLineQueue.Peek()
            nextLine.Delay -= deltaTime
            ifnextLine.Delay <= 0:
                 PlayVoiceLine(nextLine.Data)
                 voiceLineQueue.Pop()
            END IF
        END IF
    END FUNCTION
```

---

### CollectibleManager

**Purpose:** Collectible tracking and codex updates.

```
CLASS CollectibleManager:
    discoveredCollectibles: Set<String>
    
    FUNCTION DiscoverCollectible(collectibleID: String):
        IF NOT discoveredCollectibles.Contains(collectibleID):
            discoveredCollectibles.Add(collectibleID)
            
            data = GetCollectibleData(collectibleID)
            EMIT EVENT "COLLECTIBLE_FOUND" WITH (collectibleID, data.Type)
            
            // Add XP
            ProgressionManager.AddXP(data.XPReward)
            
            // Update Codex
            CodexManager.UnlockEntry(data.CodexCategory, data.LoreEntryID)
        END IF
    END FUNCTION
    
    FUNCTION PlayAudioLog(logID: String):
        data = GetAudioLog(logID)
        IF data != null:
             AudioManager.PlaySound(data.AudioClip)
             EMIT EVENT "COLLECTIBLE_PLAY" WITH (logID)
        END IF
    END FUNCTION
```

---

## Data Structures

```
STRUCT QuestData:
    QuestID: String
    DisplayName: String
    Description: String
    QuestType: QuestType
    CurrentState: QuestState
    Faction: Faction
    RequiredReputation: ReputationLevel
    Objectives: List<QuestObjective>
    PrerequisiteQuests: List<String>
    Rewards: QuestRewards

STRUCT QuestObjective:
    ObjectiveID: String
    Description: String
    Type: QuestObjectiveType
    TargetAmount: Integer
    CurrentAmount: Integer
    TargetID: String
    bOptional: Boolean

STRUCT FactionData:
    FactionID: Faction
    DisplayName: String
    LeaderName: String
    Tiers: List<FactionTier>

STRUCT FactionTier:
    Level: ReputationLevel
    RequiredReputation: Integer
    VendorDiscount: Float
    UnlockIDs: List<String>

STRUCT DialogueLine:
    Text: String
    AudioClip: SoundBase
    Duration: Float
    SpeakerID: String

STRUCT CollectibleData:
    CollectibleID: String
    Type: CollectibleType
    DisplayName: String
    LoreEntryID: String
    XPReward: Integer
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] QuestManager logic (Accept, Progress, Complete)
- [ ] FactionManager reputation logic
- [ ] DialogueManager basic playback

### MEDIUM Priority 🟡
- [ ] Voice line prioritization/queuing
- [ ] CollectibleManager discovery logic
- [ ] UI integration (Quest Log, HUD)

### LOW Priority 🟢
- [ ] Complex quest chains (Branching)
- [ ] Dynamic environmental dialogue
- [ ] Codex UI implementation



