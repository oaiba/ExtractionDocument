---
title: "Tutorial System - Technical Specification"
type: docs
---
# Tutorial System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: Save System →](./SaveSystem.md)**

**Reference:** [High-Level Tutorial Design](../../GDD_HighLevel/GameDesign/Tutorial.md)

---

## Overview

The **Tutorial System** manages player onboarding, contextual hints, and feature unlocking.

---

## Enums & Types

### TutorialStep
Tutorial progression step sequence.

| Code Name       | Display Name    | Order | Duration | Skippable | Description               |
| :-------------- | :-------------- | :---- | :------- | :-------- | :------------------------ |
| `TS_Welcome`    | Welcome         | 1     | 5s       | Yes       | Initial welcome screen    |
| `TS_Movement`   | Movement        | 2     | 30s      | No        | WASD / joystick basics    |
| `TS_Camera`     | Camera          | 3     | 20s      | No        | Look around controls      |
| `TS_Fire`       | Fire            | 4     | 25s      | No        | Shoot weapon basics       |
| `TS_Reload`     | Reload          | 5     | 15s      | No        | Reload weapon mechanics   |
| `TS_ADS`        | Aim Down Sights | 6     | 20s      | No        | Aim down sights targeting |
| `TS_Crouch`     | Crouch          | 7     | 15s      | Yes       | Crouch movement mechanics |
| `TS_Sprint`     | Sprint          | 8     | 15s      | Yes       | Sprint mechanics          |
| `TS_Interact`   | Interact        | 9     | 20s      | No        | Pick up items basics      |
| `TS_Loot`       | Loot            | 10    | 25s      | No        | Open containers           |
| `TS_Inventory`  | Inventory       | 11    | 30s      | No        | Manage inventory          |
| `TS_Equip`      | Equip           | 12    | 25s      | No        | Equip items               |
| `TS_Healing`    | Healing         | 13    | 20s      | No        | Use healing items         |
| `TS_Ability`    | Ability         | 14    | 25s      | No        | Use operator ability      |
| `TS_Minimap`    | Minimap         | 15    | 20s      | Yes       | Read minimap              |
| `TS_Extraction` | Extraction      | 16    | 30s      | No        | Call extraction           |
| `TS_Complete`   | Complete        | 17    | N/A      | N/A       | Tutorial finished         |

---

### HintCategory
Hint topic classification.

| Code Name       | Display Name | Color  | Icon       | Description                 |
| :-------------- | :----------- | :----- | :--------- | :-------------------------- |
| `HC_Movement`   | Movement     | Blue   | Joystick   | How to move                 |
| `HC_Combat`     | Combat       | Red    | Crosshair  | Fighting tips               |
| `HC_Looting`    | Looting      | Yellow | Box        | Item collection             |
| `HC_Inventory`  | Inventory    | Purple | Backpack   | Inventory management        |
| `HC_Navigation` | Navigation   | Cyan   | Compass    | Map/minimap usage           |
| `HC_Survival`   | Survival     | Green  | Heart      | Health and danger awareness |
| `HC_Extraction` | Extraction   | Orange | Helicopter | Extraction process          |
| `HC_Social`     | Social       | Pink   | People     | Squad features              |
| `HC_Economy`    | Economy      | Gold   | Coin       | Buying and selling          |
| `HC_Advanced`   | Advanced     | White  | Star       | Pro tips                    |

---

### HintPriority
Hint display priority level.

| Code Name       | Display Name | Queue Order   | Interrupt | Auto-Dismiss |
| :-------------- | :----------- | :------------ | :-------- | :----------- |
| `HP_Critical`   | Critical     | 1 (Immediate) | Yes       | No           |
| `HP_High`       | High         | 2             | Yes       | 8s           |
| `HP_Medium`     | Medium       | 3             | No        | 5s           |
| `HP_Low`        | Low          | 4             | No        | 4s           |
| `HP_Background` | Background   | 5             | No        | N/A          |

---

### HintTriggerType
Hint trigger condition.

| Code Name          | Display Name   | Auto-Detect | Threshold    | Description       |
| :----------------- | :------------- | :---------- | :----------- | :---------------- |
| `HT_FirstTime`     | First Time     | Yes         | 1 occurrence | First encounter   |
| `HT_ContextAction` | Context Action | Yes         | Proximity    | Near interactable |
| `HT_LowResource`   | Low Resource   | Yes         | < 25%        | Low health/ammo   |
| `HT_Timeout`       | Timeout        | Yes         | 60s idle     | Stuck or idle     |
| `HT_Manual`        | Manual         | No          | User request | Help menu         |
| `HT_Repeated`      | Repeated Fail  | Yes         | 3+ failures  | Failed attempts   |
| `HT_ZoneEnter`     | Zone Enter     | Yes         | Zone ID      | Enter area        |
| `HT_Combat`        | Combat         | Yes         | In combat    | Combat state      |

---

### TutorialState
Tutorial completion state.

| Code Name        | Display Name | Progress |
| :--------------- | :----------- | :------- |
| `TST_NotStarted` | Not Started  | 0%       |
| `TST_InProgress` | In Progress  | Variable |
| `TST_Completed`  | Completed    | 100%     |
| `TST_Skipped`    | Skipped      | 0%       |
| `TST_Failed`     | Failed       | Variable |

---

### TooltipType
Tooltip display format.

| Code Name        | Display Name | Content         | Auto-Position |
| :--------------- | :----------- | :-------------- | :------------ |
| `TT_Simple`      | Simple       | Text only       | Yes           |
| `TT_WithIcon`    | With Icon    | Icon + text     | Yes           |
| `TT_Interactive` | Interactive  | With button     | Yes           |
| `TT_Rich`        | Rich         | Full info       | No            |
| `TT_ItemInfo`    | Item Info    | Item stats      | No            |
| `TT_AbilityInfo` | Ability Info | Ability details | No            |

---

## Code Names

### Tutorial Flow Events

| Code Name           | Trigger         | Parameters       | Description      |
| :------------------ | :-------------- | :--------------- | :--------------- |
| `TUT_STEP_START`    | Step begins     | StepID, StepName | Step active      |
| `TUT_STEP_COMPLETE` | Step done       | StepID, Duration | Step finished    |
| `TUT_SKIP`          | Skip requested  | Progress         | Tutorial skipped |
| `TUT_RESET`         | Reset requested | Reason           | Tutorial restart |

### Hint Events

| Code Name      | Trigger     | Parameters          | Description    |
| :------------- | :---------- | :------------------ | :------------- |
| `HINT_SHOW`    | Hint seen   | HintID, Priority    | Hint displayed |
| `HINT_DISMISS` | Hint closed | HintID, DismissType | Hint removed   |
| `HINT_QUEUE`   | Hint queued | HintID, Pos         | Added to queue |
| `HINT_TRIGGER` | Triggered   | Type, Context       | Trigger logic  |

### Tooltip Events

| Code Name      | Trigger | Parameters     | Description     |
| :------------- | :------ | :------------- | :-------------- |
| `TOOLTIP_SHOW` | Shown   | TooltipID, Pos | Tooltip visible |
| `TOOLTIP_HIDE` | Hidden  | TooltipID      | Tooltip removed |

### Progress Events

| Code Name        | Trigger    | Parameters     | Description       |
| :--------------- | :--------- | :------------- | :---------------- |
| `FTX_COMPLETE`   | First time | EventID, Count | Event experienced |
| `FEATURE_UNLOCK` | Unlock     | FeatureID      | Feature available |

---

## Core Classes

### TutorialManager

**Purpose:** Manage tutorial flow and tracking.

```
CLASS TutorialManager:
    currentStep: TutorialStep
    completedSteps: Set<TutorialStep>
    bTutorialComplete: Boolean
    
    // Dependencies
    onboardingManager: OnboardingManager
    hintManager: HintManager
    tooltipManager: TooltipManager
    ftxTracker: FTXTracker
    
    // Events
    OnStepComplete: Event<(step)>
    OnTutorialComplete: Event<()>
    
    FUNCTION StartTutorial():
        IF bTutorialComplete: RETURN
        
        currentStep = TS_Welcome
        onboardingManager.ShowStep(TS_Welcome)
    END FUNCTION
    
    FUNCTION AdvanceStep():
        completedSteps.Add(currentStep)
        EMIT EVENT "TUT_STEP_COMPLETE" WITH (currentStep)
        OnStepComplete.Broadcast(currentStep)
        
        nextStep = GetNextStep(currentStep)
        
        IF nextStep == TS_Complete:
            CompleteTutorial()
        ELSE:
            currentStep = nextStep
            onboardingManager.ShowStep(nextStep)
            EMIT EVENT "TUT_STEP_START" WITH (nextStep)
        END IF
    END FUNCTION
    
    FUNCTION CompleteTutorial():
        bTutorialComplete = true
        onboardingManager.HideAll()
        EMIT EVENT "TUT_COMPLETE"
        OnTutorialComplete.Broadcast()
        // Save progress
    END FUNCTION
```

---

### OnboardingManager

**Purpose:** Handle UI overlay and step visuals.

```
CLASS OnboardingManager:
    activeStep: TutorialStep
    
    FUNCTION ShowStep(step: TutorialStep):
        data = GetStepData(step)
        // Update UI widget with title, desc, objective
        
        IF data.HighlightElement != "":
            HighlightUIElement(data.HighlightElement)
        END IF
        
        activeStep = step
    END FUNCTION
    
    FUNCTION HighlightUIElement(elementID: String):
        // Visual highlight logic
    END FUNCTION
```

---

### HintManager

**Purpose:** Manage contextual hints and queue.

```
CLASS HintManager:
    hintQueue: List<HintData>
    seenHints: Set<String>
    activeHint: HintData
    
    FUNCTION ShowHint(hintID: String):
        IF seenHints.Contains(hintID): RETURN
        
        hint = GetHintData(hintID)
        QueueHint(hint)
    END FUNCTION
    
    FUNCTION QueueHint(hint: HintData):
        hintQueue.Add(hint)
        SortQueueByPriority()
        TryShowNextHint()
    END FUNCTION
    
    FUNCTION TryShowNextHint():
        IF activeHint != null: RETURN
        IF hintQueue.IsEmpty(): RETURN
        
        nextHint = hintQueue.Pop()
        DisplayHint(nextHint)
        seenHints.Add(nextHint.ID)
        EMIT EVENT "HINT_SHOW" WITH (nextHint.ID)
    END FUNCTION
    
    FUNCTION RegisterTrigger(hintID: String, trigger: HintTriggerType, threshold: Float):
        // Setup trigger logic
    END FUNCTION
```

---

### TooltipManager

**Purpose:** Show informational tooltips.

```
CLASS TooltipManager:
    currentTooltip: TooltipWidget
    
    FUNCTION ShowTooltip(tooltipID: String, position: Vector2):
        data = GetTooltipData(tooltipID)
        // Spawn/Update tooltip widget
        EMIT EVENT "TOOLTIP_SHOW" WITH (tooltipID)
    END FUNCTION
    
    FUNCTION HideTooltip():
        // Remove widget
        EMIT EVENT "TOOLTIP_HIDE"
    END FUNCTION
```

---

### FTXTracker

**Purpose:** Track first-time experiences and unlocks.

```
CLASS FTXTracker:
    eventCounts: Map<String, Integer>
    unlockedFeatures: Set<String>
    
    FUNCTION TrackEvent(eventID: String):
        count = eventCounts.GetOrDefault(eventID, 0) + 1
        eventCounts[eventID] = count
        
        IF count == 1:
            EMIT EVENT "FTX_COMPLETE" WITH (eventID)
        END IF
        
        CheckFeatureUnlocks()
    END FUNCTION
    
    FUNCTION CheckFeatureUnlocks():
        FOR EACH feature IN FeatureDatabase:
            IF IsLocked(feature) AND RequirementsMet(feature):
                UnlockFeature(feature.ID)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION UnlockFeature(featureID: String):
        unlockedFeatures.Add(featureID)
        EMIT EVENT "FEATURE_UNLOCK" WITH (featureID)
        // Show unlock notification
    END FUNCTION
```

---

## Data Structures

```
STRUCT TutorialStepData:
    Step: TutorialStep
    Title: String
    Description: String
    Objective: String
    HighlightElement: String
    ControlsToShow: List<TouchButton>
    bBlockInput: Boolean

STRUCT HintData:
    HintID: String
    Category: HintCategory
    Priority: HintPriority
    Title: String
    Description: String
    Cooldown: Float
    MaxShowCount: Integer
    
STRUCT FeatureUnlockRequirement:
    Description: String
    RequiredValue: Integer
    TrackedStat: String // e.g., "AccountLevel"
    RequiredTutorialStep: TutorialStep
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] TutorialManager state machine
- [ ] Onboarding UI overlay
- [ ] HintManager queue system
- [ ] Tutorial step data definitions

### MEDIUM Priority 🟡
- [ ] Tooltip system
- [ ] Visual highlighting for UI
- [ ] Trigger system for hints

### LOW Priority 🟢
- [ ] Feature unlock notifications
- [ ] Tutorial skip logic
- [ ] Replay tutorial functionality

---

**[← Back to Index](../README.md)** | **[Next: Save System →](./SaveSystem.md)**


