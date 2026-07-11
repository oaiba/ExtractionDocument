---
title: Control System - Technical Design Sutureument
type: docs
---


### Related Sutureuments

| Sutureument              | Relationship            | Link                                                                                                                                        |
| ------------------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Controls Design**      | High-level input design | [GDD\_HighLevel/GameDesign/Controls.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_HighLevel/GameDesign/Controls.md) |
| **Character System**     | Movement implementation | [CharacterSystem.md](charactersystem/index.html)                                                                                                    |
| **Weapon System**        | Combat input handling   | [WeaponSystem.md](weaponsystem/index.html)                                                                                                          |
| **UI System**            | HUD input prompts       | [../Systems/UISystem.md](../systems/uisystem/index.html)                                                                                            |
| **Accessibility System** | Input accessibility     | [../Systems/AccessibilitySystem.md](../systems/accessibilitysystem/index.html)                                                                      |
| **Mobile Optimization**  | Touch performance       | [../Performance/Optimization.md](../performance/optimization/index.html)                                                                            |

***

### Overview

#### Purpose

The **Control System** provides a unified input abstraction layer that translates hardware-specific inputs into gameplay actions across all platforms (Mobile, PC, Console).

#### Core Functions

| Function                | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| **Input Abstraction**   | Convert raw hardware input into logical game actions  |
| **Platform Adaptation** | Support Touch, Keyboard/Mouse, Gamepad seamlessly     |
| **Movement Control**    | Handle twin-stick movement (move + aim independently) |
| **Action Binding**      | Map physical inputs to gameplay commands              |
| **Dynamic Switching**   | Auto-detect and switch between input methods          |
| **Customization**       | Allow key remapping and layout customization          |
| **Accessibility**       | Support one-handed mode, hold-to-toggle, etc.         |

#### Design Goals

```
1. RESPONSIVE - Input latency < 16ms (1 frame at 60 FPS)
2. CONSISTENT - Same gameplay feel across all platforms
3. CUSTOMIZABLE - Full remapping and accessibility options
4. INTUITIVE - Platform-native controls that feel natural
5. DYNAMIC - Seamless switching between input devices
```

***

### System Architecture

#### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CONTROL SYSTEM                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐           │
│  │   HARDWARE   │     │   INPUT      │     │   ACTION     │           │
│  │   INPUT      │───▶ │   PROCESSOR  │───▶│   DISPATCHER │           │
│  │   LAYER      │     │              │     │              │           │
│  └──────────────┘     └──────────────┘     └──────────────┘           │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  ┌──────────────┐    ┌──────────────┐     ┌──────────────┐           │
│  │ Touch Input  │    │ Input        │     │ Character    │           │
│  │ Keyboard     │    │ Smoothing    │     │ Controller   │           │
│  │ Mouse        │    │ Deadzone     │    │ Weapon       │          │
│  │ Gamepad      │    │ Sensitivity  │    │ UI System    │          │
│  │ Gyroscope    │    │              │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

#### Core Components

| Component            | Responsibility          | Dependencies     |
| -------------------- | ----------------------- | ---------------- |
| **InputManager**     | Central input handling  | None (Singleton) |
| **ActionMap**        | Binding definitions     | InputManager     |
| **InputProcessor**   | Smoothing, deadzone     | ActionMap        |
| **PlatformAdapter**  | Platform-specific logic | InputProcessor   |
| **RemappingManager** | Key customization       | ActionMap        |
| **TouchController**  | Mobile virtual controls | PlatformAdapter  |

***

### Enums & Types

#### EInputAction

Input action command type.

| Code Name          | Display Name   | Type            | PC Key | Console           | Mobile Touch               | Touch Zone    | Description           |
| ------------------ | -------------- | --------------- | ------ | ----------------- | -------------------------- | ------------- | --------------------- |
| `IA_Move`          | Move           | Value (Vector2) | WASD   | Left Stick        | Virtual Joystick           | Left 30%      | Character movement    |
| `IA_Look`          | Look           | Value (Vector2) | Mouse  | Right Stick       | Touch Drag                 | Right 50%     | Camera/aim direction  |
| `IA_Fire`          | Fire           | Button          | LMB    | RT/R2             | Fire Button (Hold/Tap)     | Bottom-Right  | Shoot weapon          |
| `IA_Aim`           | Aim            | Button          | RMB    | LT/L2             | ADS Button (Toggle)        | Right-Center  | Aim down sights       |
| `IA_Reload`        | Reload         | Button          | R      | X/Square          | Reload Button              | Action Bar    | Reload weapon         |
| `IA_Interact`      | Interact       | Button          | F      | A/Cross           | Context Button (Auto)      | Center        | Interact with objects |
| `IA_Jump`          | Jump           | Button          | Space  | A/Cross           | Jump Button                | Action Bar    | Jump/vault            |
| `IA_Crouch`        | Crouch         | Button          | C/Ctrl | B/Circle          | Crouch Button (Toggle)     | Action Bar    | Crouch/slide          |
| `IA_Sprint`        | Sprint         | Button          | Shift  | L3                | Joystick Edge Lock         | Left Zone     | Auto-sprint at edge   |
| `IA_Ability`       | Ability        | Button          | Q      | RB/R1             | Ability Button             | Top-Right     | Operator ability      |
| `IA_Melee`         | Melee          | Button          | V      | RS/R3             | Melee Button               | Action Bar    | Melee attack          |
| `IA_Grenade`       | Grenade        | Button          | G      | LB/L1             | Grenade Button (Hold+Drag) | Top-Left      | Throw grenade         |
| `IA_Ping`          | Ping           | Button          | MMB    | D-Pad Up          | Double-Tap Look Zone       | Right Zone    | Ping location         |
| `IA_Inventory`     | Inventory      | Button          | Tab    | D-Pad Down        | Inventory Icon             | Top-Right HUD | Open inventory        |
| `IA_Map`           | Map            | Button          | M      | Touchpad          | Map Icon                   | Top-Left HUD  | Open map              |
| `IA_SwapPrimary`   | Swap Primary   | Button          | 1      | D-Pad Left        | Primary Weapon Icon        | Weapon Bar    | Equip primary         |
| `IA_SwapSecondary` | Swap Secondary | Button          | 2      | D-Pad Right       | Secondary Weapon Icon      | Weapon Bar    | Equip secondary       |
| `IA_SwapSidearm`   | Swap Sidearm   | Button          | 3      | Y/Triangle        | Sidearm Icon               | Weapon Bar    | Equip sidearm         |
| `IA_QuickHeal`     | Quick Heal     | Button          | 4      | D-Pad Down (Hold) | Health Button (Hold)       | Bottom-Left   | Use healing item      |

#### Mobile Touch Control Types

| Control Type         | Gesture          | Activation     | Customizable            | Description                         |
| -------------------- | ---------------- | -------------- | ----------------------- | ----------------------------------- |
| **Virtual Joystick** | Touch + Drag     | On finger down | Position, Size, Opacity | Floating or fixed position          |
| **Touch Drag**       | Swipe            | On finger move | Sensitivity, Invert     | Camera/aim control                  |
| **Button (Tap)**     | Single tap       | On touch up    | Position, Size          | Single action trigger               |
| **Button (Hold)**    | Press + hold     | Continuous     | Position, Size          | Sustained action (fire)             |
| **Button (Toggle)**  | Tap to toggle    | On touch up    | Position, Size          | State switch (crouch, ADS)          |
| **Context Button**   | Auto-appear      | Near target    | Threshold distance      | Appears when interactable nearby    |
| **Edge Lock**        | Joystick to edge | Auto-lock      | Threshold %             | Sprint activation at joystick limit |
| **Double-Tap**       | 2 quick taps     | On second tap  | Tap interval            | Alternative action trigger          |
| **Hold+Drag**        | Hold then drag   | Direction aim  | Sensitivity             | Grenade trajectory preview          |

#### Mobile Touch Zone Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│ [MAP]  [PING-MINI]         [MATCH INFO]           [INV] [SETTINGS]     │
│                                                              [ABILITY] │
│                                                                        │
│  [GRENADE]                                                   [AIM]     │
│ (Hold+Drag)                     LOOK ZONE                  (Toggle)    │
│                              (Touch Drag)                              │
│                                                                        │
│                    [INTERACT]                                          │
│                   (Context Auto)                            [FIRE]     │
│                                                            (Hold/Tap)  │
│  ┌─────────────┐                                                       │
│  │  JOYSTICK   │                                 [RELOAD] [JUMP]       │
│  │  (Floating) │   [HEALTH]                     [MELEE] [CROUCH]       │
│  └─────────────┘  (Hold Use)                                           │
│                                                                        │
│  [PRIMARY] [SECONDARY] [SIDEARM]                     [ACTION BAR]      │
│        WEAPON SWAP BAR                                                 │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Mobile Control Customization Options

| Setting                | Range                   | Default  | Description                   |
| ---------------------- | ----------------------- | -------- | ----------------------------- |
| **Button Size**        | 50% - 150%              | 100%     | Scale all buttons             |
| **Button Opacity**     | 20% - 100%              | 70%      | Transparency when not pressed |
| **Joystick Size**      | 80% - 150%              | 100%     | Movement joystick size        |
| **Joystick Type**      | Fixed / Floating        | Floating | Position behavior             |
| **Fire Mode**          | Tap / Hold / Auto       | Hold     | How fire button works         |
| **ADS Mode**           | Hold / Toggle           | Toggle   | How aim button works          |
| **Crouch Mode**        | Hold / Toggle           | Toggle   | How crouch button works       |
| **Sprint Lock**        | On / Off                | On       | Auto-sprint at joystick edge  |
| **Gyroscope**          | Off / ADS Only / Always | Off      | Motion aiming                 |
| **Gyro Sensitivity**   | 0.1 - 3.0               | 1.0      | Motion sensitivity            |
| **Look Sensitivity X** | 0.1 - 3.0               | 1.2      | Horizontal look speed         |
| **Look Sensitivity Y** | 0.1 - 3.0               | 1.0      | Vertical look speed           |
| **Aim Sensitivity**    | 0.1 - 2.0               | 0.6      | Sensitivity while ADS         |
| **Auto-Fire**          | Off / On                | Off      | Fire when aiming at enemy     |
| **Left-Hand Mode**     | Off / On                | Off      | Mirror control layout         |

***

#### EInputMethod

Input device type detection.

| Code Name      | Display Name | Platform   | Prompt Style | Aim Assist | Description       |
| -------------- | ------------ | ---------- | ------------ | ---------- | ----------------- |
| `EIM_Touch`    | Touch        | Mobile     | Touch icons  | Strong     | Touchscreen input |
| `EIM_Keyboard` | Keyboard     | PC         | Key labels   | None       | Keyboard input    |
| `EIM_Gamepad`  | Gamepad      | Console/PC | Button icons | Medium     | Controller input  |

***

#### EControlPreset

Control layout preset.

| Code Name           | Display Name  | Target  | Description                  |
| ------------------- | ------------- | ------- | ---------------------------- |
| `ECP_Default`       | Default       | All     | Standard layout              |
| `ECP_Console`       | Console       | Console | Console-optimized            |
| `ECP_Claw`          | Claw          | Mobile  | Claw grip layout             |
| `ECP_LeftHanded`    | Left Handed   | All     | Left-hand dominant           |
| `ECP_Accessibility` | Accessibility | All     | Simplified for accessibility |
| `ECP_Custom`        | Custom        | All     | User-defined mapping         |

***

#### EMovementMode

Advanced movement state.

| Code Name    | Display Name    | Speed Mult | Stamina Cost | Can Fire | Description       |
| ------------ | --------------- | ---------- | ------------ | -------- | ----------------- |
| `EMM_Walk`   | Walk            | 1.0×       | 0/s          | Yes      | Normal walking    |
| `EMM_Sprint` | Sprint          | 1.5×       | 10/s         | No       | Fast running      |
| `EMM_Crouch` | Crouch          | 0.6×       | 0/s          | Yes      | Crouching         |
| `EMM_Slide`  | Slide           | 1.8×       | 15 (burst)   | Limited  | Sliding           |
| `EMM_Vault`  | Vault           | 0.5×       | 5 (burst)    | No       | Climbing obstacle |
| `EMM_ADS`    | Aim Down Sights | 0.5×       | 0/s          | Yes      | Aiming weapon     |

***

#### ETouchZone

Mobile touch screen zone.

| Code Name           | Display Name   | Screen Area     | Function | Customizable |
| ------------------- | -------------- | --------------- | -------- | ------------ |
| `ETZ_LeftStick`     | Left Stick     | Bottom-Left 30% | Movement | Yes          |
| `ETZ_RightLook`     | Right Look     | Right 50%       | Aim/Look | Yes          |
| `ETZ_FireButton`    | Fire Button    | Bottom-Right    | Shoot    | Yes          |
| `ETZ_AimButton`     | Aim Button     | Right-Center    | ADS      | Yes          |
| `ETZ_ActionButtons` | Action Buttons | Right-Bottom    | Actions  | Yes          |
| `ETZ_AbilityButton` | Ability Button | Right-Top       | Ability  | Yes          |

***

#### EAimAssistLevel

Aim assist strength setting.

| Code Name     | Display Name   | Magnetism | Slowdown | Snap   | Target         |
| ------------- | -------------- | --------- | -------- | ------ | -------------- |
| `EAAL_Off`    | Off            | 0%        | 0%       | Off    | PC/Pro         |
| `EAAL_Low`    | Low            | 20%       | 15%      | Off    | Console        |
| `EAAL_Medium` | Medium         | 40%       | 30%      | Off    | Console        |
| `EAAL_High`   | High           | 60%       | 50%      | Weak   | Console/Mobile |
| `EAAL_Touch`  | Touch (Mobile) | 80%       | 60%      | Strong | Mobile         |

***

#### EControlReferenceFrame

Defines how directional input is interpreted relative to the game world.

| Code Name             | Display Name       | Up Input Means... | Best For               |
| --------------------- | ------------------ | ----------------- | ---------------------- |
| `ECRF_CameraRelative` | Camera Relative    | Top of Screen     | Standard Top-Down/ISO  |
| `ECRF_WorldRelative`  | World Relative     | Global North (Y+) | Fixed Camera isometric |
| `ECRF_Character`      | Character Relative | Character Forward | Tank Controls          |

***

#### EFacingBehavior

Defines how the character body orients itself during movement.

| Code Name          | Display Name  | Behavior                                | Use Case                    |
| ------------------ | ------------- | --------------------------------------- | --------------------------- |
| `EFB_FaceAim`      | Face Aim      | Body always faces reticle/aim direction | Tactical Shooters, Strafing |
| `EFB_FaceMovement` | Face Movement | Body rotates to face movement direction | Adventure, Exploration      |

***

#### EAimConstraint

Limits the cursor or aim point behavior.

| Code Name        | Display Name   | Behavior                            |
| ---------------- | -------------- | ----------------------------------- |
| `EAC_None`       | Free Cursor    | Unbounded mouse/aim movement        |
| `EAC_Clamped`    | Clamped Radius | Cursor constrained within radius R  |
| `EAC_ScreenEdge` | Screen Edge    | Cursor constrained to screen bounds |

***

### Code Names

#### Input Events

| Code Name              | Trigger          | Parameters               | Description            |
| ---------------------- | ---------------- | ------------------------ | ---------------------- |
| `INPUT_ACTION`         | Action triggered | ActionID, Value          | Input action received  |
| `INPUT_METHOD_CHANGED` | Device switched  | OldMethod, NewMethod     | Input device changed   |
| `INPUT_REMAP`          | Key remapped     | ActionID, OldKey, NewKey | Control remapped       |
| `INPUT_PRESET_APPLIED` | Preset selected  | PresetID                 | Control preset applied |

#### Movement Input Events

| Code Name            | Trigger         | Parameters       | Description          |
| -------------------- | --------------- | ---------------- | -------------------- |
| `CTRL_MOVE_START`    | Movement begins | Direction        | Started moving       |
| `CTRL_MOVE_STOP`     | Movement ends   | -                | Stopped moving       |
| `CTRL_SPRINT_TOGGLE` | Sprint toggled  | IsActive         | Sprint state changed |
| `CTRL_CROUCH_TOGGLE` | Crouch toggled  | IsActive         | Crouch state changed |
| `CTRL_SLIDE_START`   | Slide triggered | Direction, Speed | Started sliding      |

#### Combat Input Events

| Code Name         | Trigger        | Parameters | Description      |
| ----------------- | -------------- | ---------- | ---------------- |
| `CTRL_FIRE_START` | Fire pressed   | -          | Started firing   |
| `CTRL_FIRE_STOP`  | Fire released  | -          | Stopped firing   |
| `CTRL_AIM_START`  | ADS pressed    | -          | Entered aim mode |
| `CTRL_AIM_STOP`   | ADS released   | -          | Exited aim mode  |
| `CTRL_RELOAD`     | Reload pressed | -          | Reload triggered |

#### Touch Events (Mobile)

| Code Name             | Trigger           | Parameters           | Description            |
| --------------------- | ----------------- | -------------------- | ---------------------- |
| `TOUCH_JOYSTICK_MOVE` | Joystick dragged  | Direction, Magnitude | Virtual joystick input |
| `TOUCH_LOOK_DRAG`     | Look zone dragged | Delta                | Look area touch        |
| `TOUCH_BUTTON_TAP`    | Button tapped     | ButtonID             | Button pressed         |
| `TOUCH_GESTURE`       | Gesture detected  | GestureType          | Special gesture        |

#### HUD Events

| Code Name            | Trigger          | Parameters            | Description          |
| -------------------- | ---------------- | --------------------- | -------------------- |
| `HUD_PROMPT_SHOW`    | Prompt displayed | ActionID, PromptType  | Input prompt shown   |
| `HUD_PROMPT_HIDE`    | Prompt hidden    | ActionID              | Input prompt removed |
| `HUD_LAYOUT_CHANGED` | Layout modified  | LayoutID              | HUD layout changed   |
| `HUD_BUTTON_MOVED`   | Button moved     | ButtonID, NewPosition | Touch button moved   |

***

### Core Classes

#### InputManager

**Purpose:** Central singleton that coordinates all input processing.

**Pseudocode:**

```
CLASS InputManager:
    
    // Singleton instance
    STATIC instance: InputManager
    
    // Current state
    currentInputMethod: EInputMethod
    actionMap: ActionMap
    inputProcessor: InputProcessor
    
    // Settings
    sensitivity: Float = 1.0
    invertY: Boolean = false
    aimAssistLevel: EAimAssistLevel
    referenceFrame: EControlReferenceFrame = ECRF_CameraRelative
    facingBehavior: EFacingBehavior = EFB_FaceAim
    aimConstraint: EAimConstraint = EAC_Clamped
    
    // Initialize on game start
    FUNCTION Initialize():
        DetectPlatform()
        LoadActionMap()
        LoadUserSettings()
        RegisterInputCallbacks()
    END FUNCTION
    
    // Called every frame
    FUNCTION ProcessInput(deltaTime):
        // Get raw input from hardware
        rawInput = GetRawInput()
        
        // Process through input processor (deadzone, smoothing)
        processedInput = inputProcessor.Process(rawInput)
        
        // Dispatch to appropriate systems
        FOR EACH action IN processedInput.triggeredActions:
            DispatchAction(action)
        END FOR
        
        // Check for input method changes
        IF DetectMethodChange():
            SwitchInputMethod()
            EMIT EVENT "INPUT_METHOD_CHANGED"
        END IF
    END FUNCTION
    
    // Dispatch action to listeners
    FUNCTION DispatchAction(action):
        SWITCH action.type:
            CASE Movement:
                CharacterController.HandleMovement(action.value)
            CASE Combat:
                WeaponSystem.HandleCombatInput(action)
            CASE Interaction:
                InteractionSystem.HandleInteraction(action)
            CASE UI:
                UISystem.HandleUIInput(action)
        END SWITCH
    END FUNCTION
    
    // Auto-detect input method from last input
    FUNCTION DetectMethodChange():
        IF lastInput.source != currentInputMethod:
            RETURN true
        END IF
        RETURN false
    END FUNCTION
```

**Relationships:**

* → **CharacterController**: Sends movement commands
* → **WeaponSystem**: Sends combat commands (fire, reload, aim)
* → **UISystem**: Notifies of input method changes for prompt updates
* → **InteractionSystem**: Sends interact commands

***

#### ActionMap

**Purpose:** Defines mappings between hardware inputs and game actions.

**Pseudocode:**

```
CLASS ActionMap:
    
    // Binding storage
    bindings: Map<EInputAction, List<InputBinding>>
    
    // Platform-specific defaults
    pcDefaults: Map<EInputAction, KeyCode>
    consoleDefaults: Map<EInputAction, GamepadButton>
    mobileDefaults: Map<EInputAction, TouchZone>
    
    // Load default bindings for current platform
    FUNCTION LoadDefaults(platform):
        SWITCH platform:
            CASE PC:
                bindings = CreateBindingsFrom(pcDefaults)
            CASE Console:
                bindings = CreateBindingsFrom(consoleDefaults)
            CASE Mobile:
                bindings = CreateBindingsFrom(mobileDefaults)
        END SWITCH
    END FUNCTION
    
    // Get all bindings for an action
    FUNCTION GetBindings(action: EInputAction) -> List<InputBinding>:
        RETURN bindings[action]
    END FUNCTION
    
    // Check if input triggers any action
    FUNCTION CheckInput(input: RawInput) -> EInputAction?:
        FOR EACH (action, bindingList) IN bindings:
            FOR EACH binding IN bindingList:
                IF binding.Matches(input):
                    RETURN action
                END IF
            END FOR
        END FOR
        RETURN null
    END FUNCTION
    
    // Remap an action to new key
    FUNCTION RemapAction(action, newKey):
        // Check for conflicts
        conflictAction = FindActionWithKey(newKey)
        IF conflictAction != null:
            EMIT WARNING "Key conflict with " + conflictAction
            RETURN false
        END IF
        
        // Apply new binding
        oldKey = bindings[action].primary
        bindings[action].primary = newKey
        
        EMIT EVENT "INPUT_REMAP" WITH (action, oldKey, newKey)
        SaveToUserSettings()
        RETURN true
    END FUNCTION
```

**Data Structure:**

```
InputBinding:
    action: EInputAction          // What game action this triggers
    primaryKey: KeyCode           // Main key/button
    secondaryKey: KeyCode         // Alternative key (optional)
    modifiers: List<KeyCode>      // Shift, Ctrl, etc.
    inputType: ButtonType         // Press, Hold, Release, Axis
    isRemappable: Boolean         // Can user change this?
```

***

#### InputProcessor

**Purpose:** Process raw input through smoothing, deadzone, and sensitivity.

**Pseudocode:**

```
CLASS InputProcessor:
    
    // Settings
    deadzoneInner: Float = 0.15
    deadzoneOuter: Float = 0.95
    smoothingFactor: Float = 0.1
    sensitivityX: Float = 1.0
    sensitivityY: Float = 1.0
    
    // State
    previousInput: Vector2
    smoothedInput: Vector2
    
    // Main processing pipeline
    FUNCTION Process(rawInput: Vector2) -> Vector2:
        // Step 1: Apply deadzone
        processed = ApplyDeadzone(rawInput)
        
        // Step 2: Apply sensitivity
        processed.x = processed.x * sensitivityX
        processed.y = processed.y * sensitivityY
        
        // Step 3: Apply smoothing (for mobile/gamepad)
        IF currentInputMethod IN [Touch, Gamepad]:
            processed = ApplySmoothing(processed)
        END IF
        
        // Step 4: Clamp to valid range
        processed = Clamp(processed, -1.0, 1.0)
        
        RETURN processed
    END FUNCTION
    
    // Radial deadzone implementation
    FUNCTION ApplyDeadzone(input: Vector2) -> Vector2:
        magnitude = input.Length()
        
        // Inside inner deadzone - no input
        IF magnitude < deadzoneInner:
            RETURN Vector2.Zero
        END IF
        
        // Outside outer deadzone - full input
        IF magnitude > deadzoneOuter:
            RETURN input.Normalized()
        END IF
        
        // Lerp between deadzones
        normalizedMagnitude = (magnitude - deadzoneInner) / (deadzoneOuter - deadzoneInner)
        RETURN input.Normalized() * normalizedMagnitude
    END FUNCTION
    
    // Exponential smoothing
    FUNCTION ApplySmoothing(input: Vector2) -> Vector2:
        smoothedInput = Lerp(previousInput, input, smoothingFactor)
        previousInput = smoothedInput
        RETURN smoothedInput
    END FUNCTION

    // Reticle/Cursor Constraint Logic (Mouse/Gamepad)
    FUNCTION ApplyAimConstraint(rawInput: Vector2, charPosition: Vector2) -> Vector2:
        IF aimConstraint == EAC_Clamped:
            offset = rawInput - charPosition
            IF offset.Length() > maxAimRadius:
                RETURN charPosition + offset.Normalized() * maxAimRadius
            END IF
        END IF
        RETURN rawInput
    END FUNCTION
```

**Platform-Specific Settings:**

| Platform     | Deadzone Inner | Deadzone Outer | Smoothing | Notes                    |
| ------------ | -------------- | -------------- | --------- | ------------------------ |
| PC (Mouse)   | 0              | 1.0            | None      | Direct 1:1 mapping       |
| PC (Gamepad) | 0.15           | 0.95           | 0.1       | Standard deadzone        |
| Console      | 0.18           | 0.92           | 0.15      | Slightly larger deadzone |
| Mobile       | 0.1            | 0.98           | 0.2       | More smoothing           |

***

#### MovementController

**Purpose:** Handle twin-stick movement and rotation independently.

**Pseudocode:**

```
CLASS MovementController:
    
    // References
    character: Character
    cameraController: CameraController
    
    // Movement state
    currentMode: EMovementMode = Walk
    moveDirection: Vector2
    lookDirection: Vector2
    
    // Process movement input
    FUNCTION HandleMovementInput(moveInput: Vector2, lookInput: Vector2):
        // Resolve movement based on settings (Camera vs World vs Character relative)
        worldMoveDir = ResolveMovementFrame(moveInput)
        
        // Store for physics update
        moveDirection = worldMoveDir
        
        // Handle look direction based on input method
        IF InputManager.currentInputMethod == Mouse:
            // PC: Project mouse to ground plane
            lookDirection = CalculateMouseLookDirection()
        ELSE:
            // Gamepad/Mobile: Use input vector directly
            lookDirection = lookInput
        END IF
        
        // Update character
        UpdateCharacterMovement()
        UpdateCharacterRotation()
    END FUNCTION
    
    // Convert input to camera-relative world direction
    FUNCTION ConvertToWorldSpace(input: Vector2) -> Vector3:
        cameraRight = cameraController.GetRightVector()
        cameraForward = cameraController.GetForwardVector()
        
        // Project camera vectors to ground plane (ignore Y)
        cameraRight.y = 0
        cameraForward.y = 0
        cameraRight.Normalize()
        cameraForward.Normalize()
        
        // Combine input with camera directions
        worldDir = (cameraRight * input.x) + (cameraForward * input.y)
        
        RETURN worldDir.Normalized()
    END FUNCTION
    
    // PC: Calculate look direction from mouse position
    FUNCTION CalculateMouseLookDirection() -> Vector2:
        // Raycast from mouse to ground plane
        mousePos = Input.GetMousePosition()
        ray = cameraController.ScreenToWorldRay(mousePos)
        
        // Find intersection with ground
        groundHit = Raycast(ray, GroundPlane)
        
        IF groundHit.success:
            // Direction from character to hit point
            toTarget = groundHit.point - character.position
            toTarget.y = 0
            
            // Apply Aim Constraint (Clamping) at the input level if needed
            // But usually handled in UI/Crosshair, here we just get direction
            
            RETURN toTarget.Normalized()
        END IF
        
        RETURN character.forwardDirection
    END FUNCTION
    
    // Resolve movement vector based on User Settings
    FUNCTION ResolveMovementFrame(input: Vector2) -> Vector3:
        SWITCH settings.referenceFrame:
            CASE ECRF_CameraRelative:
                RETURN ConvertToCameraSpace(input)
            CASE ECRF_WorldRelative:
                RETURN Vector3(input.x, 0, input.y) // Direct mapping to World X/Z
            CASE ECRF_Character:
                // Move relative to character's current forward
                RETURN (character.forward * input.y) + (character.right * input.x)
        END SWITCH
    END FUNCTION
    
    // Apply movement to character (called in physics update)
    FUNCTION UpdateCharacterMovement():
        // Calculate speed based on mode
        baseSpeed = character.baseSpeed
        speedMult = GetSpeedMultiplier(currentMode)
        finalSpeed = baseSpeed * speedMult
        
        // Check stamina for sprint
        IF currentMode == Sprint:
            IF character.stamina <= 0:
                SetMovementMode(Walk)
                finalSpeed = baseSpeed
            ELSE:
                character.ConsumeStamina(10 * deltaTime)
            END IF
        END IF
        
        // Apply velocity
        character.velocity = moveDirection * finalSpeed
    END FUNCTION
    
    // Apply rotation to character
    FUNCTION UpdateCharacterRotation():
        targetRotation = character.rotation
        
        // Decide rotation based on Facing Behavior setting
        SWITCH settings.facingBehavior:
            CASE EFB_FaceAim:
                // Standard Shooter: Face where we are aiming
                IF lookDirection.Length() > 0.1:
                    targetRotation = LookRotation(lookDirection)
                END IF
                
            CASE EFB_FaceMovement:
                // Adventure Style: Face where we are running
                // Exception: Always face aim if firing or ADS
                IF IsFiringOrADS():
                    targetRotation = LookRotation(lookDirection)
                ELSE IF moveDirection.Length() > 0.1:
                    targetRotation = LookRotation(moveDirection)
                END IF
        END SWITCH

        // Smooth rotation
        character.rotation = SmoothRotate(
            character.rotation, 
            targetRotation, 
            rotationSpeed * deltaTime
        )
    END FUNCTION
```

**Movement Modes:**

| Mode   | Entry Condition                     | Exit Condition                      | Speed Mult      |
| ------ | ----------------------------------- | ----------------------------------- | --------------- |
| Walk   | Default                             | Sprint/Crouch input                 | 1.0×            |
| Sprint | Shift + Moving forward + HasStamina | ReleaseShift OR OutOfStamina OR ADS | 1.5×            |
| Crouch | Press Crouch while not sprinting    | Press Crouch again                  | 0.6×            |
| Slide  | Press Crouch while sprinting        | SlideTimer expires                  | 1.8× (decaying) |
| ADS    | Hold ADS button                     | Release ADS                         | 0.5×            |

***

#### TouchController

**Purpose:** Handle mobile-specific virtual controls.

**Pseudocode:**

```
CLASS TouchController:
    
    // Virtual control references
    moveJoystick: VirtualJoystick
    lookZone: TouchZone
    actionButtons: List<TouchButton>
    
    // Touch tracking
    activeTouches: Map<FingerId, TouchData>
    
    // Initialize touch controls
    FUNCTION Initialize():
        // Create floating joystick (left side)
        moveJoystick = CreateFloatingJoystick(
            zone: LeftThird,
            size: 150px,
            deadzone: 0.15,
            isFloating: true
        )
        
        // Create look zone (right side)
        lookZone = CreateLookZone(
            zone: RightHalf,
            sensitivity: UserSettings.lookSensitivity
        )
        
        // Create action buttons
        CreateActionButtons()
    END FUNCTION
    
    // Process all active touches
    FUNCTION ProcessTouches():
        FOR EACH touch IN Input.GetTouches():
            SWITCH touch.phase:
                CASE Began:
                    HandleTouchBegan(touch)
                CASE Moved:
                    HandleTouchMoved(touch)
                CASE Ended, Cancelled:
                    HandleTouchEnded(touch)
            END SWITCH
        END FOR
        
        // Update virtual controls
        UpdateJoystick()
        UpdateLookZone()
    END FUNCTION
    
    // Handle new touch
    FUNCTION HandleTouchBegan(touch):
        // Determine which zone was touched
        zone = GetZoneForPosition(touch.position)
        
        SWITCH zone:
            CASE LeftThird:
                // Start joystick at touch position
                moveJoystick.Activate(touch.position)
                activeTouches[touch.id] = { type: Joystick, startPos: touch.position }
                
            CASE RightHalf:
                // Check if touching a button
                button = GetButtonAtPosition(touch.position)
                IF button != null:
                    button.Press()
                    activeTouches[touch.id] = { type: Button, button: button }
                ELSE:
                    // Start look drag
                    activeTouches[touch.id] = { type: Look, startPos: touch.position }
                END IF
        END SWITCH
    END FUNCTION
    
    // Handle touch movement
    FUNCTION HandleTouchMoved(touch):
        touchData = activeTouches[touch.id]
        
        IF touchData.type == Joystick:
            // Update joystick position
            delta = touch.position - touchData.startPos
            moveJoystick.UpdatePosition(delta)
            
            // Calculate input vector
            inputVector = moveJoystick.GetNormalizedInput()
            EMIT EVENT "TOUCH_JOYSTICK_MOVE" WITH inputVector
            
        ELSE IF touchData.type == Look:
            // Calculate look delta
            delta = touch.deltaPosition * lookSensitivity
            EMIT EVENT "TOUCH_LOOK_DRAG" WITH delta
        END IF
    END FUNCTION
    
    // Handle touch end
    FUNCTION HandleTouchEnded(touch):
        touchData = activeTouches[touch.id]
        
        IF touchData.type == Joystick:
            moveJoystick.Deactivate()
            EMIT EVENT "CTRL_MOVE_STOP"
            
        ELSE IF touchData.type == Button:
            touchData.button.Release()
        END IF
        
        activeTouches.Remove(touch.id)
    END FUNCTION
```

**Touch Zone Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  ┌───────────┐                        ┌──────┐  ┌──────┐   │
│  │ ABILITY   │                        │ AIM  │  │ FIRE │   │
│  └───────────┘                        └──────┘  └──────┘   │
│                                                              │
│                           LOOK ZONE                          │
│                          (Drag to aim)                       │
│                                                              │
│  ┌───────────┐                                 ┌─────────┐  │
│  │           │                                 │ RELOAD  │  │
│  │ JOYSTICK  │                                 ├─────────┤  │
│  │  (Float)  │                                 │  JUMP   │  │
│  │           │                                 ├─────────┤  │
│  └───────────┘                                 │ CROUCH  │  │
│                                                └─────────┘  │
└─────────────────────────────────────────────────────────────┘
```

***

#### RemappingManager

**Purpose:** Handle key remapping and control customization.

**Pseudocode:**

```
CLASS RemappingManager:
    
    // Active bindings
    currentBindings: Map<EInputAction, KeyBinding>
    currentPreset: EControlPreset
    
    // Remap an action to a new key
    FUNCTION RemapAction(action: EInputAction, newKey: KeyCode) -> Boolean:
        // Check if key is reserved (system keys)
        IF IsReservedKey(newKey):
            ShowError("This key cannot be remapped")
            RETURN false
        END IF
        
        // Check for conflicts
        conflictingAction = FindConflict(newKey)
        IF conflictingAction != null:
            // Prompt user to swap or cancel
            result = ShowConflictDialog(action, conflictingAction, newKey)
            
            IF result == Swap:
                // Swap bindings
                oldKey = currentBindings[action]
                currentBindings[conflictingAction] = oldKey
                currentBindings[action] = newKey
            ELSE IF result == Cancel:
                RETURN false
            END IF
        ELSE:
            // No conflict, just assign
            currentBindings[action] = newKey
        END IF
        
        // Mark preset as custom
        currentPreset = Custom
        
        // Save to user settings
        SaveBindings()
        
        // Notify systems
        EMIT EVENT "INPUT_REMAP"
        
        RETURN true
    END FUNCTION
    
    // Apply a preset layout
    FUNCTION ApplyPreset(preset: EControlPreset):
        SWITCH preset:
            CASE Default:
                currentBindings = LoadDefaultBindings()
            CASE Console:
                currentBindings = LoadConsoleBindings()
            CASE Claw:
                currentBindings = LoadClawBindings()
            CASE LeftHanded:
                currentBindings = MirrorBindings(LoadDefaultBindings())
            CASE Accessibility:
                currentBindings = LoadAccessibilityBindings()
            CASE Custom:
                currentBindings = LoadUserBindings()
        END SWITCH
        
        currentPreset = preset
        SaveBindings()
        
        EMIT EVENT "INPUT_PRESET_APPLIED" WITH preset
    END FUNCTION
    
    // Reset all bindings to default
    FUNCTION ResetToDefaults():
        ApplyPreset(Default)
        ClearUserBindings()
    END FUNCTION
    
    // Get current binding for action
    FUNCTION GetBinding(action: EInputAction) -> KeyBinding:
        RETURN currentBindings[action]
    END FUNCTION
    
    // Get all bindings (for settings UI)
    FUNCTION GetAllBindings() -> List<BindingInfo>:
        result = []
        FOR EACH (action, binding) IN currentBindings:
            result.Add({
                action: action,
                displayName: GetDisplayName(action),
                currentKey: binding.primary,
                defaultKey: GetDefaultKey(action),
                isRemappable: IsRemappable(action)
            })
        END FOR
        RETURN result
    END FUNCTION
```

***

#### AimAssistController

**Purpose:** Provide aim assistance for gamepad and touch input.

**Pseudocode:**

```
CLASS AimAssistController:
    
    // Settings
    level: EAimAssistLevel
    magnetismStrength: Float
    slowdownStrength: Float
    snapStrength: Float
    
    // State
    currentTarget: Character = null
    isActive: Boolean = false
    
    // Apply aim assist to look input
    FUNCTION ApplyAimAssist(rawLookInput: Vector2, aimOrigin: Vector3, aimDirection: Vector3) -> Vector2:
        // Skip if disabled or using mouse
        IF level == Off OR InputManager.currentInputMethod == Mouse:
            RETURN rawLookInput
        END IF
        
        // Find potential targets
        targets = FindTargetsInCone(aimOrigin, aimDirection, maxAngle: 45, maxDistance: 50)
        
        IF targets.IsEmpty():
            currentTarget = null
            RETURN rawLookInput
        END IF
        
        // Get closest target to crosshair
        closestTarget = GetClosestToCrosshair(targets)
        currentTarget = closestTarget
        
        // Calculate angle to target
        directionToTarget = (closestTarget.position - aimOrigin).Normalized()
        angleToTarget = AngleBetween(aimDirection, directionToTarget)
        
        // Apply magnetism (pull toward target)
        magnetismInput = ApplyMagnetism(rawLookInput, directionToTarget, angleToTarget)
        
        // Apply slowdown (reduce sensitivity near target)
        slowedInput = ApplySlowdown(magnetismInput, angleToTarget)
        
        // Apply snap (optional, for mobile)
        IF snapStrength > 0 AND angleToTarget < 15:
            snappedInput = ApplySnap(slowedInput, directionToTarget)
            RETURN snappedInput
        END IF
        
        RETURN slowedInput
    END FUNCTION
    
    // Pull aim toward target
    FUNCTION ApplyMagnetism(input: Vector2, targetDir: Vector3, angle: Float) -> Vector2:
        // Magnetism falloff based on distance from target
        magnetismFactor = 1.0 - (angle / 45.0)  // Full at 0°, zero at 45°
        magnetismFactor = magnetismFactor * magnetismStrength
        
        // Blend input toward target direction
        targetInput2D = ProjectToScreen(targetDir)
        blendedInput = Lerp(input, targetInput2D, magnetismFactor)
        
        RETURN blendedInput
    END FUNCTION
    
    // Reduce sensitivity near target
    FUNCTION ApplySlowdown(input: Vector2, angle: Float) -> Vector2:
        // Slowdown increases as we get closer to target
        slowdownFactor = 1.0 - (slowdownStrength * (1.0 - angle / 45.0))
        
        RETURN input * slowdownFactor
    END FUNCTION
```

***

#### CameraController

**Purpose:** Manages camera positioning, parallax effects, and dynamic FOV.

**Pseudocode:**

```
CLASS CameraController:
    
    // Settings
    baseFOV: Float = 60.0
    dynamicFOVFactor: Float = 5.0 // How much FOV widens with speed
    parallaxMult: Float = 0.5
    
    // Limits
    minZoom: Float = 10.0
    maxZoom: Float = 40.0
    
    // Update Camera Transform
    FUNCTION UpdateCamera(deltaTime):
        // 1. Follow Target (Character)
        targetPos = character.position
        
        // 2. Apply "Lead" (look ahead)
        velocityOffset = character.velocity * leadFactor
        desiredPos = targetPos + velocityOffset + currentZoomOffset
        
        // 3. Smooth Damp
        transform.position = Vector3.SmoothDamp(transform.position, desiredPos, smoothTime)
        
        // 4. Update Dynamic Effects
        UpdateDynamicFOV()
        UpdateParallaxLayers()
    END FUNCTION
    
    // Widen FOV based on speed to give "sense of speed"
    FUNCTION UpdateDynamicFOV():
        speedRatio = character.velocity.Length() / character.maxSpeed
        targetFOV = baseFOV + (speedRatio * dynamicFOVFactor)
        currentFOV = Lerp(currentFOV, targetFOV, deltaTime * 2.0)
        camera.fieldOfView = currentFOV
    END FUNCTION
    
    // Simulate depth for top-down view
    FUNCTION UpdateParallaxLayers():
        // Move background layers slower than foreground to create depth
        // This is usually a shader or separate camera stack effect
        FOR EACH layer IN parallaxLayers:
            offset = (transform.position - lastFramePos) * (layer.depth * parallaxMult)
            layer.MoveOpposite(offset)
        END FOR
    END FUNCTION
```

***

### Platform-Specific Implementation

#### PC (Mouse & Keyboard)

| Aspect               | Implementation                           |
| -------------------- | ---------------------------------------- |
| **Movement**         | WASD keys, camera-relative               |
| **Aiming**           | Mouse position projected to ground plane |
| **Fire**             | Left Mouse Button (hold for auto)        |
| **Look Sensitivity** | User-configurable, default 1.0           |
| **Aim Assist**       | Disabled by default                      |
| **Key Remapping**    | Full remapping support                   |

#### Console (Gamepad)

| Aspect               | Implementation                 |
| -------------------- | ------------------------------ |
| **Movement**         | Left Stick, camera-relative    |
| **Aiming**           | Right Stick (twin-stick)       |
| **Fire**             | Right Trigger (analog)         |
| **Look Sensitivity** | User-configurable, default 0.8 |
| **Aim Assist**       | Medium by default              |
| **Response Curve**   | Exponential for precision      |

#### Mobile (Touch)

| Aspect                | Implementation                      |
| --------------------- | ----------------------------------- |
| **Movement**          | Floating virtual joystick (left)    |
| **Aiming**            | Touch drag on right side            |
| **Fire**              | Dedicated button + Auto-fire option |
| **Look Sensitivity**  | User-configurable, default 1.2      |
| **Aim Assist**        | Strong by default                   |
| **HUD Customization** | Full button layout customization    |

***

### System Relationships

#### Dependency Diagram

```
                    ┌────────────────────┐
                    │   CONTROL SYSTEM   │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ CHARACTER       │  │ WEAPON          │  │ UI              │
│ SYSTEM          │  │ SYSTEM          │  │ SYSTEM          │
│                 │  │                 │  │                 │
│ • Movement      │  │ • Fire          │  │ • Input prompts │
│ • Rotation      │  │ • Aim           │  │ • Button icons  │
│ • State machine │  │ • Reload        │  │ • Touch controls│
└─────────────────┘  └─────────────────┘  └─────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ INTERACTION     │  │ INVENTORY       │  │ ACCESSIBILITY   │
│ SYSTEM          │  │ SYSTEM          │  │ SYSTEM          │
│                 │  │                 │  │                 │
│ • Interact      │  │ • Quick select  │  │ • Remapping     │
│ • Context menus │  │ • Item use      │  │ • One-handed    │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

#### Integration Points

| Target System           | Interface                | Data                            |
| ----------------------- | ------------------------ | ------------------------------- |
| **CharacterSystem**     | `HandleMovement()`       | Vector2 direction, MovementMode |
| **WeaponSystem**        | `HandleCombatInput()`    | Fire, Aim, Reload states        |
| **UISystem**            | `OnInputMethodChanged()` | Current input method            |
| **InteractionSystem**   | `HandleInteract()`       | Interact action triggered       |
| **InventorySystem**     | `HandleQuickSelect()`    | Slot selection                  |
| **AccessibilitySystem** | `GetRemappedAction()`    | Custom bindings                 |

***

### Performance Considerations

#### Optimization Targets

| Metric             | Target | Current |
| ------------------ | ------ | ------- |
| Input Latency      | < 16ms | TODO    |
| Touch Processing   | < 2ms  | TODO    |
| Active Touch Limit | 10     | 10      |
| Memory Usage       | < 5 MB | TODO    |

#### Optimization Strategies

```
1. INPUT POLLING
   • Poll input once per frame, not per action
   • Cache processed input for multi-system use
   • Use event-driven updates for UI

2. TOUCH OPTIMIZATION
   • Limit active touch tracking
   • Use spatial hashing for button detection
   • Pool touch event objects

3. MEMORY
   • Reuse input structures
   • Avoid allocations in hot path
   • Cache binding lookups
```

***

### TODO: Implementation Tasks

#### HIGH Priority 

* [ ] Implement InputManager core loop
* [ ] Create ActionMap with all bindings
* [ ] Implement MovementController twin-stick logic
* [ ] Create TouchController for mobile
* [ ] Implement aim assist system

#### MEDIUM Priority 

* [ ] Add remapping UI and persistence
* [ ] Implement control presets
* [ ] Add sensitivity curves
* [ ] Create gyroscope aiming option
* [ ] Input method auto-detection

#### LOW Priority 

* [ ] Advanced customization (per-action sensitivity)
* [ ] Macro/combo support
* [ ] Controller vibration feedback
* [ ] Input replay for debugging

***

### References

#### External Sutureumentation

* [Unity Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.0/manual/index.html) - If using Unity
* [Unreal Enhanced Input](https://docs.unrealengine.com/5.0/en-US/enhanced-input-in-unreal-engine/) - If using Unreal
* [Mobile Game Input Best Practices](https://developer.android.com/games/develop/gamepad) - Android guidelines
* [Apple HIG - Game Controllers](https://developer.apple.com/design/human-interface-guidelines/game-controllers) - iOS guidelines

#### Industry Examples

* **Call of Duty Mobile** - Touch control reference
* **PUBG Mobile** - Virtual joystick implementation
* **Fortnite** - Cross-platform input handling
* **Apex Legends** - Aim assist tuning
