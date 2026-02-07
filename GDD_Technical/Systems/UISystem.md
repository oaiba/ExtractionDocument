# UI System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: Audio System →](./AudioSystem.md)**

**Reference:** [High-Level User Interface Design](../../GDD_HighLevel/Visuals/UserInterface.md)

---

## Overview

The **UI System** manages all user interface elements including menus, HUD, widgets, popups, and touch controls. Built on UMG with mobile-first design principles.

**Responsibilities:**
- Screen/widget management
- HUD system (health, ammo, minimap)
- Touch controls (joystick, buttons)
- Menu navigation
- Popup/modal system
- Notification queue
- Drag-and-drop inventory
- Screen transitions
- Responsive scaling
- Input binding for UI

---

## Enums & Types

### ScreenType
Main screen type classification.

| Code Name           | Display Name    | Cache | Transition | Back Nav | Description                |
| :------------------ | :-------------- | :---- | :--------- | :------- | :------------------------- |
| `ST_MainMenu`       | Main Menu       | Yes   | Fade       | No       | Home screen hub            |
| `ST_OperatorSelect` | Operator Select | Yes   | Slide      | Yes      | Character selection screen |
| `ST_Loadout`        | Loadout         | Yes   | Slide      | Yes      | Weapon/gear setup          |
| `ST_Stash`          | Stash           | Yes   | Slide      | Yes      | Inventory management       |
| `ST_Shop`           | Shop            | No    | Fade       | Yes      | In-game store              |
| `ST_Quests`         | Quests          | Yes   | Slide      | Yes      | Mission tracker            |
| `ST_Social`         | Social          | Yes   | Slide      | Yes      | Friends and clan           |
| `ST_Settings`       | Settings        | Yes   | Scale      | Yes      | Options and configuration  |
| `ST_MatchLoading`   | Match Loading   | No    | Fade       | No       | Pre-match loading          |
| `ST_InGame`         | In Game         | No    | None       | No       | HUD during match           |
| `ST_PostMatch`      | Post Match      | No    | Fade       | No       | Victory/defeat results     |

---

### WidgetLayer
Widget Z-order layer.

| Code Name         | Display Name | Z-Index | Purpose         | Modal Block | Description            |
| :---------------- | :----------- | :------ | :-------------- | :---------- | :--------------------- |
| `WL_Background`   | Background   | 0       | Backdrop, video | No          | Background layer       |
| `WL_Content`      | Content      | 100     | Main screens    | No          | Primary screen content |
| `WL_Overlay`      | Overlay      | 200     | HUD elements    | No          | In-game HUD layer      |
| `WL_Popup`        | Popup        | 300     | Modals, dialogs | Yes         | Modal popup layer      |
| `WL_Notification` | Notification | 400     | Toast messages  | No          | Notification layer     |
| `WL_System`       | System       | 500     | Loading, errors | Yes         | System message layer   |
| `WL_Debug`        | Debug        | 1000    | Dev overlays    | No          | Debug tools layer      |

---

### HUDElement
HUD element type.

| Code Name               | Display Name       | Position      | Visibility   | Toggle | Description           |
| :---------------------- | :----------------- | :------------ | :----------- | :----- | :-------------------- |
| `HUD_HealthBar`         | Health Bar         | Top-Left      | Always       | Yes    | Player health display |
| `HUD_ArmorBar`          | Armor Bar          | Top-Left      | Always       | Yes    | Armor points display  |
| `HUD_StaminaBar`        | Stamina Bar        | Top-Left      | Sprinting    | Yes    | Sprint meter          |
| `HUD_AmmoCounter`       | Ammo Counter       | Bottom-Right  | Weapon held  | Yes    | Magazine/reserve ammo |
| `HUD_Minimap`           | Minimap            | Top-Right     | Always       | Yes    | Mini map display      |
| `HUD_Crosshair`         | Crosshair          | Center        | Aiming       | Yes    | Aim reticle           |
| `HUD_KillFeed`          | Kill Feed          | Top-Right     | On event     | Yes    | Kill notifications    |
| `HUD_ObjectiveTracker`  | Objective Tracker  | Left          | Quest active | Yes    | Quest progress        |
| `HUD_DamageIndicator`   | Damage Indicator   | Center        | On damage    | No     | Hit direction display |
| `HUD_InteractionPrompt` | Interaction Prompt | Center        | Near object  | No     | Context action prompt |
| `HUD_ExtractionTimer`   | Extraction Timer   | Top-Center    | Extracting   | No     | Extraction countdown  |
| `HUD_MatchTimer`        | Match Timer        | Top-Center    | In match     | Yes    | Match time remaining  |
| `HUD_PlayerCount`       | Player Count       | Top-Center    | In match     | Yes    | Remaining players     |
| `HUD_AbilityCooldown`   | Ability Cooldown   | Bottom-Center | Has ability  | Yes    | Ability ready state   |
| `HUD_CompassBar`        | Compass Bar        | Top-Center    | Always       | Yes    | Direction indicator   |
| `HUD_Ping`              | Ping               | World         | On ping      | No     | Team ping markers     |

---

### NotificationType
Notification display type.

| Code Name        | Display Name | Position   | Duration      | Priority | Description               |
| :--------------- | :----------- | :--------- | :------------ | :------- | :------------------------ |
| `NT_Toast`       | Toast        | Top-Center | 3s            | Low      | Brief info message        |
| `NT_Alert`       | Alert        | Center-Top | 5s            | High     | Warning notification      |
| `NT_Loot`        | Loot         | Right-Side | 2s            | Low      | Item pickup display       |
| `NT_Achievement` | Achievement  | Center     | 5s            | Medium   | Unlock celebration        |
| `NT_System`      | System       | Center     | Until dismiss | Critical | Errors, connection issues |
| `NT_Quest`       | Quest        | Left       | 4s            | Medium   | Quest updates             |
| `NT_LevelUp`     | Level Up     | Center     | 5s            | High     | XP milestone reached      |

---

### ButtonState
Button visual state.

| Code Name     | Display Name | Opacity | Scale | Interact | Description        |
| :------------ | :----------- | :------ | :---- | :------- | :----------------- |
| `BS_Normal`   | Normal       | 100%    | 1.0×  | Yes      | Default idle state |
| `BS_Hovered`  | Hovered      | 100%    | 1.05× | Yes      | Mouse hover (PC)   |
| `BS_Pressed`  | Pressed      | 90%     | 0.95× | Yes      | Touch/click down   |
| `BS_Disabled` | Disabled     | 50%     | 1.0×  | No       | Not interactable   |
| `BS_Selected` | Selected     | 100%    | 1.1×  | Yes      | Current selection  |
| `BS_Locked`   | Locked       | 70%     | 1.0×  | No       | Requires unlock    |

---

### TransitionType
Screen transition animation.

| Code Name     | Display Name | Duration | Direction  | Description        |
| :------------ | :----------- | :------- | :--------- | :----------------- |
| `TR_None`     | None         | 0ms      | N/A        | Instant switch     |
| `TR_Fade`     | Fade         | 300ms    | In/Out     | Fade to/from black |
| `TR_Slide`    | Slide        | 250ms    | Left/Right | Slide horizontally |
| `TR_Scale`    | Scale        | 200ms    | In/Out     | Zoom effect        |
| `TR_Dissolve` | Dissolve     | 400ms    | Cross      | Crossfade blend    |

---

### TouchZone
Touch input area designation.

| Code Name       | Display Name | Screen Area      | Purpose  | Description            |
| :-------------- | :----------- | :--------------- | :------- | :--------------------- |
| `TZ_LeftThumb`  | Left Thumb   | Bottom-Left 25%  | Movement | Movement joystick area |
| `TZ_RightThumb` | Right Thumb  | Bottom-Right 25% | Actions  | Action buttons area    |
| `TZ_TopLeft`    | Top Left     | Top-Left 20%     | Status   | Status info display    |
| `TZ_TopRight`   | Top Right    | Top-Right 20%    | Info     | Map and info area      |
| `TZ_Center`     | Center       | Center 40%       | Gameplay | Main gameplay area     |
| `TZ_FullScreen` | Full Screen  | Entire screen    | Camera   | Camera control touch   |

---

### TouchButton
Touch button type.

| Code Name       | Display Name | Toggle | Auto-Hide | Description      |
| :-------------- | :----------- | :----- | :-------- | :--------------- |
| `TB_Fire`       | Fire         | No     | No        | Shoot weapon     |
| `TB_ADS`        | ADS          | No     | No        | Aim down sights  |
| `TB_Reload`     | Reload       | No     | Yes       | Reload weapon    |
| `TB_WeaponSwap` | Weapon Swap  | No     | Yes       | Switch weapon    |
| `TB_Crouch`     | Crouch       | Yes    | No        | Crouch toggle    |
| `TB_Prone`      | Prone        | Yes    | No        | Prone toggle     |
| `TB_Jump`       | Jump         | No     | No        | Jump action      |
| `TB_Sprint`     | Sprint       | No     | No        | Sprint hold      |
| `TB_Interact`   | Interact     | No     | Yes       | Context interact |
| `TB_Inventory`  | Inventory    | No     | No        | Open inventory   |
| `TB_Ability`    | Ability      | No     | No        | Use ability      |
| `TB_Ping`       | Ping         | No     | No        | Ping location    |
| `TB_Map`        | Map          | No     | No        | Open map         |
| `TB_Pause`      | Pause        | No     | No        | Pause menu       |

---

## Code Names

### Screen Events

| Code Name              | Trigger           | Parameters             | Description                  |
| :--------------------- | :---------------- | :--------------------- | :--------------------------- |
| `UI_SCREEN_OPEN`       | Screen opens      | ScreenType, Transition | Screen displayed             |
| `UI_SCREEN_CLOSE`      | Screen closes     | ScreenType, Transition | Screen hidden                |
| `UI_SCREEN_TRANSITION` | Transition active | FromScreen, ToScreen   | Transition playing           |
| `UI_SCREEN_READY`      | Screen loaded     | ScreenType, LoadTime   | Screen ready for interaction |

### Widget Events

| Code Name         | Trigger          | Parameters      | Description        |
| :---------------- | :--------------- | :-------------- | :----------------- |
| `UI_WIDGET_SHOW`  | Widget shown     | WidgetID, Layer | Widget displayed   |
| `UI_WIDGET_HIDE`  | Widget hidden    | WidgetID        | Widget removed     |
| `UI_WIDGET_FOCUS` | Widget focused   | WidgetID        | Widget gains focus |
| `UI_WIDGET_BLUR`  | Widget unfocused | WidgetID        | Widget loses focus |

### HUD Events

| Code Name              | Trigger         | Parameters                     | Description             |
| :--------------------- | :-------------- | :----------------------------- | :---------------------- |
| `HUD_UPDATE`           | Value changed   | Element, OldValue, NewValue    | HUD element updated     |
| `HUD_FLASH`            | Flash effect    | Element, Color, Duration       | Element flash animation |
| `HUD_PULSE`            | Pulse effect    | Element, Intensity             | Element pulse animation |
| `HUD_DAMAGE_INDICATOR` | Damage received | Direction, Intensity           | Damage direction shown  |
| `HUD_KILL_FEED`        | Kill event      | KillerName, VictimName, Weapon | Kill added to feed      |

### Interaction Events

| Code Name         | Trigger        | Parameters         | Description            |
| :---------------- | :------------- | :----------------- | :--------------------- |
| `UI_BUTTON_CLICK` | Button clicked | ButtonID, Position | Button single tap      |
| `UI_BUTTON_HOLD`  | Button held    | ButtonID, Duration | Button long press      |
| `UI_DRAG_START`   | Drag begins    | WidgetID, Position | Item drag started      |
| `UI_DRAG_END`     | Drag ends      | WidgetID, Position | Item drag ended        |
| `UI_DROP`         | Item dropped   | WidgetID, TargetID | Item dropped on target |

### Notification Events

| Code Name       | Trigger             | Parameters           | Description            |
| :-------------- | :------------------ | :------------------- | :--------------------- |
| `NOTIF_SHOW`    | Notification shown  | NotifID, Type        | Notification displayed |
| `NOTIF_DISMISS` | Notification closed | NotifID, DismissType | Notification removed   |
| `NOTIF_QUEUE`   | Notification queued | NotifID, QueuePos    | Notification waiting   |

---

## Architecture

### Class Diagram

```
                    ┌─────────────────┐
                    │   UIManager     │
                    │  (Singleton)    │
                    └────────┬────────┘
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
┌───▼───────┐    ┌───────────▼───────────┐    ┌───────▼───────┐
│ScreenMgr  │    │     HUDManager        │    │ PopupManager  │
│           │    │                       │    │               │
└───────────┘    └───────────────────────┘    └───────────────┘
    │                        │                        │
    │            ┌───────────┼───────────┐            │
    │            │           │           │            │
    │    ┌───────▼───┐ ┌─────▼────┐ ┌────▼────┐       │
    │    │TouchInput │ │Notif     │ │Tooltip  │       │
    │    │ Manager   │ │ Manager  │ │ Manager │       │
    │    └───────────┘ └──────────┘ └─────────┘       │
    │                                                 │
    └─────────────────────────────────────────────────┘
```

---

## Core Classes

### UIManager

**Purpose:** Central UI controller and subsystem access.

```
CLASS UIManager:
    STATIC instance: UIManager
    
    // Sub-managers
    screenManager: ScreenManager
    hudManager: HUDManager
    popupManager: PopupManager
    notificationManager: NotificationManager
    touchInputManager: TouchInputManager
    
    // Screen history
    screenHistory: List<ScreenType>
    currentScreen: ScreenType
    
    // Events
    OnScreenChanged: Event<(oldScreen, newScreen)>
    
    FUNCTION OpenScreen(screen: ScreenType, transition: TransitionType = TR_Fade):
        oldScreen = currentScreen
        
        screenManager.CloseCurrentScreen(transition)
        screenManager.OpenScreen(screen, transition)
        
        // Update history for back navigation
        IF CanNavigateBack(screen):
            screenHistory.Add(oldScreen)
        END IF
        
        currentScreen = screen
        
        OnScreenChanged.Broadcast(oldScreen, screen)
        
        EMIT EVENT "UI_SCREEN_OPEN" WITH (screen, transition)
    END FUNCTION
    
    FUNCTION CloseScreen(transition: TransitionType = TR_Fade):
        screenManager.CloseCurrentScreen(transition)
        
        EMIT EVENT "UI_SCREEN_CLOSE" WITH (currentScreen, transition)
    END FUNCTION
    
    FUNCTION GoBack():
        IF screenHistory.IsEmpty():
            RETURN
        END IF
        
        previousScreen = screenHistory.Pop()
        OpenScreen(previousScreen, TR_Slide)
    END FUNCTION
    
    FUNCTION GetCurrentScreen() -> ScreenType:
        RETURN currentScreen
    END FUNCTION
    
    FUNCTION IsScreenOpen(screen: ScreenType) -> Boolean:
        RETURN currentScreen == screen
    END FUNCTION
    
    FUNCTION CreateWidget(widgetClass: Class, layer: WidgetLayer) -> Widget:
        widget = Instantiate(widgetClass)
        widget.SetZOrder(GetZOrderForLayer(layer))
        RETURN widget
    END FUNCTION
    
    FUNCTION ShowWidget(widget: Widget):
        widget.SetVisibility(Visible)
        
        EMIT EVENT "UI_WIDGET_SHOW" WITH (widget.ID, widget.Layer)
    END FUNCTION
    
    FUNCTION HideWidget(widget: Widget):
        widget.SetVisibility(Hidden)
        
        EMIT EVENT "UI_WIDGET_HIDE" WITH (widget.ID)
    END FUNCTION
    
    FUNCTION SetHUDScale(scale: Float):
        hudManager.SetScale(scale)
    END FUNCTION
    
    FUNCTION SetButtonOpacity(opacity: Float):
        touchInputManager.SetButtonOpacity(opacity)
    END FUNCTION
```

---

### ScreenManager

**Purpose:** Screen lifecycle and transitions.

```
CLASS ScreenManager:
    // Registered screens
    registeredScreens: Map<ScreenType, WidgetClass>
    cachedScreens: Map<ScreenType, Widget>
    
    currentScreenWidget: Widget
    currentScreenType: ScreenType
    
    FUNCTION RegisterScreen(type: ScreenType, widgetClass: WidgetClass):
        registeredScreens[type] = widgetClass
    END FUNCTION
    
    FUNCTION OpenScreen(type: ScreenType, transition: TransitionType) -> Widget:
        widget = null
        
        // Check cache first
        IF cachedScreens.Contains(type):
            widget = cachedScreens[type]
        ELSE:
            widgetClass = registeredScreens[type]
            widget = CreateWidget(widgetClass)
            
            // Cache if cacheable
            IF ShouldCacheScreen(type):
                cachedScreens[type] = widget
            END IF
        END IF
        
        // Play transition
        PlayTransition(transition, false, LAMBDA:
            currentScreenWidget = widget
            currentScreenType = type
            widget.Show()
            
            EMIT EVENT "UI_SCREEN_READY" WITH (type, loadTime)
        END LAMBDA)
        
        RETURN widget
    END FUNCTION
    
    FUNCTION CloseCurrentScreen(transition: TransitionType):
        IF currentScreenWidget == null:
            RETURN
        END IF
        
        PlayTransition(transition, true, LAMBDA:
            currentScreenWidget.Hide()
        END LAMBDA)
    END FUNCTION
    
    FUNCTION PlayTransition(type: TransitionType, isOut: Boolean, onComplete: Callback):
        SWITCH type:
            CASE TR_None:
                onComplete()
            
            CASE TR_Fade:
                IF isOut:
                    AnimateFadeOut(0.3, onComplete)
                ELSE:
                    AnimateFadeIn(0.3, onComplete)
                END IF
            
            CASE TR_Slide:
                direction = isOut ? -1 : 1
                AnimateSlide(direction, 0.25, onComplete)
            
            CASE TR_Scale:
                IF isOut:
                    AnimateScaleOut(0.2, onComplete)
                ELSE:
                    AnimateScaleIn(0.2, onComplete)
                END IF
        END SWITCH
    END FUNCTION
    
    FUNCTION PreloadScreen(type: ScreenType):
        IF NOT cachedScreens.Contains(type):
            widgetClass = registeredScreens[type]
            widget = CreateWidget(widgetClass)
            cachedScreens[type] = widget
        END IF
    END FUNCTION

// Screen configurations
CONST SCREEN_CONFIGS = {
    ST_MainMenu: { widget: "WBP_MainMenu", cache: true, transition: TR_Fade },
    ST_OperatorSelect: { widget: "WBP_OperatorSelect", cache: true, transition: TR_Slide },
    ST_Loadout: { widget: "WBP_Loadout", cache: true, transition: TR_Slide },
    ST_Stash: { widget: "WBP_Stash", cache: true, transition: TR_Slide },
    ST_Shop: { widget: "WBP_Shop", cache: false, transition: TR_Fade },
    ST_Settings: { widget: "WBP_Settings", cache: true, transition: TR_Scale },
    ST_InGame: { widget: "WBP_GameHUD", cache: false, transition: TR_None },
    ST_PostMatch: { widget: "WBP_PostMatch", cache: false, transition: TR_Fade }
}
```

---

### HUDManager

**Purpose:** In-game HUD elements and updates.

```
CLASS HUDManager:
    // HUD widget
    hudWidget: GameHUDWidget
    
    // Element visibility
    elementVisibility: Map<HUDElement, Boolean>
    
    // Active indicators
    activeDamageIndicators: List<DamageIndicatorData>
    killFeedEntries: List<KillFeedData>
    
    // Config
    maxKillFeedEntries: Integer = 5
    killFeedEntryDuration: Float = 5.0
    
    FUNCTION InitializeHUD():
        hudWidget = CreateWidget(GameHUDWidget)
        
        // Set default visibility
        FOR EACH element IN HUDElement.Values:
            elementVisibility[element] = true
        END FOR
    END FUNCTION
    
    FUNCTION DestroyHUD():
        hudWidget.Destroy()
        hudWidget = null
    END FUNCTION
    
    FUNCTION ShowElement(element: HUDElement):
        SetElementVisibility(element, true)
    END FUNCTION
    
    FUNCTION HideElement(element: HUDElement):
        SetElementVisibility(element, false)
    END FUNCTION
    
    FUNCTION SetElementVisibility(element: HUDElement, visible: Boolean):
        elementVisibility[element] = visible
        hudWidget.SetElementVisible(element, visible)
    END FUNCTION
    
    FUNCTION IsElementVisible(element: HUDElement) -> Boolean:
        RETURN elementVisibility[element]
    END FUNCTION
    
    FUNCTION UpdateHealth(current: Float, max: Float):
        percent = current / max
        hudWidget.healthBar.SetPercent(percent)
        hudWidget.healthText.SetText(FormatNumber(current))
        
        IF percent <= 0.25:
            FlashElement(HUD_HealthBar, Color.Red, 0.5)
        END IF
        
        EMIT EVENT "HUD_UPDATE" WITH (HUD_HealthBar, oldHealth, current)
    END FUNCTION
    
    FUNCTION UpdateArmor(current: Float, max: Float):
        percent = current / max
        hudWidget.armorBar.SetPercent(percent)
        hudWidget.armorText.SetText(FormatNumber(current))
        
        EMIT EVENT "HUD_UPDATE" WITH (HUD_ArmorBar, oldArmor, current)
    END FUNCTION
    
    FUNCTION UpdateStamina(current: Float, max: Float):
        percent = current / max
        hudWidget.staminaBar.SetPercent(percent)
        
        // Auto-hide when full
        SetElementVisibility(HUD_StaminaBar, percent < 1.0)
    END FUNCTION
    
    FUNCTION UpdateAmmo(magazine: Integer, reserve: Integer):
        hudWidget.ammoText.SetText(magazine + " / " + reserve)
        
        IF magazine <= 0:
            FlashElement(HUD_AmmoCounter, Color.Red, 0.3)
        ELSE IF magazine <= 5:
            hudWidget.ammoText.SetColor(Color.Yellow)
        ELSE:
            hudWidget.ammoText.SetColor(Color.White)
        END IF
    END FUNCTION
    
    FUNCTION UpdateMatchTimer(secondsRemaining: Float):
        minutes = Floor(secondsRemaining / 60)
        seconds = secondsRemaining MOD 60
        hudWidget.matchTimerText.SetText(Format("{0}:{1:00}", minutes, seconds))
        
        IF secondsRemaining <= 60:
            hudWidget.matchTimerText.SetColor(Color.Red)
        END IF
    END FUNCTION
    
    FUNCTION ShowDamageIndicator(direction: Vector3, intensity: Float):
        indicator = NEW DamageIndicatorData()
        indicator.direction = CalculateScreenDirection(direction)
        indicator.intensity = Clamp(intensity, 0, 1)
        indicator.remainingTime = 1.5
        
        activeDamageIndicators.Add(indicator)
        
        hudWidget.ShowDamageIndicator(indicator)
        
        EMIT EVENT "HUD_DAMAGE_INDICATOR" WITH (direction, intensity)
    END FUNCTION
    
    FUNCTION AddKillFeedEntry(data: KillFeedData):
        killFeedEntries.Insert(0, data)
        
        // Limit entries
        WHILE killFeedEntries.Count > maxKillFeedEntries:
            killFeedEntries.RemoveLast()
        END WHILE
        
        hudWidget.RefreshKillFeed(killFeedEntries)
        
        EMIT EVENT "HUD_KILL_FEED" WITH (data.killerName, data.victimName, data.weaponID)
    END FUNCTION
    
    FUNCTION ShowInteractionPrompt(actionText: String, objectName: String):
        hudWidget.interactionPrompt.Show()
        hudWidget.interactionPrompt.SetText(actionText, objectName)
    END FUNCTION
    
    FUNCTION HideInteractionPrompt():
        hudWidget.interactionPrompt.Hide()
    END FUNCTION
    
    FUNCTION ShowExtractionTimer(duration: Float, elapsed: Float):
        hudWidget.extractionTimer.Show()
        hudWidget.extractionTimer.SetProgress(elapsed / duration)
        hudWidget.extractionTimer.SetTime(duration - elapsed)
    END FUNCTION
    
    FUNCTION FlashElement(element: HUDElement, color: Color, duration: Float):
        hudWidget.FlashElement(element, color, duration)
        
        EMIT EVENT "HUD_FLASH" WITH (element, color, duration)
    END FUNCTION
    
    FUNCTION UpdateMinimapPlayerPosition(position: Vector2, rotation: Float):
        hudWidget.minimap.SetPlayerPosition(position)
        hudWidget.minimap.SetPlayerRotation(rotation)
    END FUNCTION
    
    FUNCTION AddMinimapMarker(id: String, position: Vector2, type: MinimapMarkerType):
        hudWidget.minimap.AddMarker(id, position, type)
    END FUNCTION
    
    FUNCTION RemoveMinimapMarker(id: String):
        hudWidget.minimap.RemoveMarker(id)
    END FUNCTION

STRUCT HUDLayoutData:
    // Health Bar
    healthPosition: Vector2 = (20, 20)
    healthSize: Vector2 = (200, 20)
    healthSegments: Integer = 10
    healthColor: Color = #DC2626  // Red
    
    // Armor Bar
    armorPosition: Vector2 = (20, 45)
    armorColor: Color = #3B82F6  // Blue
    
    // Stamina Bar
    staminaPosition: Vector2 = (20, 70)
    staminaColor: Color = #FBBF24  // Yellow
    
    // Ammo
    ammoPosition: Vector2 = (-100, -60)  // Relative to bottom-right
    ammoFontSize: Integer = 28
    
    // Minimap
    minimapPosition: Vector2 = (-170, 20)  // Relative to top-right
    minimapSize: Float = 150.0
    minimapZoom: Float = 200.0  // Meters radius
    
    // Crosshair
    crosshairColor: Color = #FFFFFF
    crosshairSize: Float = 1.0
    crosshairOpacity: Float = 1.0

STRUCT KillFeedData:
    killerName: String
    victimName: String
    weaponID: String
    isHeadshot: Boolean = false
    isLocalPlayer: Boolean = false
    timestamp: Float

STRUCT DamageIndicatorData:
    direction: Float  // Degrees from forward
    intensity: Float  // 0-1
    remainingTime: Float

ENUM MinimapMarkerType:
    Player, Teammate, Enemy, EnemyLastKnown,
    LootContainer, SupplyDrop, ExtractionZone,
    Objective, Ping, Danger
```

---

### TouchInputManager

**Purpose:** Touch controls for mobile gameplay.

```
CLASS TouchInputManager:
    // Joystick
    movementJoystick: VirtualJoystickWidget
    
    // Action buttons
    actionButtons: Map<TouchButton, ActionButtonWidget>
    
    // Settings
    settings: TouchInputSettings
    
    // Active touch tracking
    activeTouches: Map<Integer, TouchZone>
    
    // Events
    OnButtonPressed: Event<(button)>
    OnButtonReleased: Event<(button)>
    
    FUNCTION GetMovementInput() -> Vector2:
        RETURN movementJoystick.GetInputVector()
    END FUNCTION
    
    FUNCTION IsJoystickActive() -> Boolean:
        RETURN movementJoystick.IsActive()
    END FUNCTION
    
    FUNCTION GetJoystickPosition() -> Vector2:
        RETURN movementJoystick.GetPosition()
    END FUNCTION
    
    FUNCTION GetLookInput() -> Vector2:
        // Calculate from touch delta in center/right area
        RETURN CalculateLookInput()
    END FUNCTION
    
    FUNCTION IsFirePressed() -> Boolean:
        RETURN actionButtons[TB_Fire].IsPressed()
    END FUNCTION
    
    FUNCTION IsADSPressed() -> Boolean:
        RETURN actionButtons[TB_ADS].IsPressed()
    END FUNCTION
    
    FUNCTION TriggerReload():
        OnButtonPressed.Broadcast(TB_Reload)
    END FUNCTION
    
    FUNCTION TriggerWeaponSwap():
        OnButtonPressed.Broadcast(TB_WeaponSwap)
    END FUNCTION
    
    FUNCTION IsCrouchToggled() -> Boolean:
        RETURN actionButtons[TB_Crouch].IsToggled()
    END FUNCTION
    
    FUNCTION SetSensitivity(sensitivity: Float):
        settings.sensitivity = sensitivity
    END FUNCTION
    
    FUNCTION SetLeftHandedMode(enabled: Boolean):
        settings.leftHandedMode = enabled
        RearrangeButtons()
    END FUNCTION
    
    FUNCTION SetButtonScale(scale: Float):
        settings.buttonScale = scale
        
        FOR EACH (type, button) IN actionButtons:
            button.SetScale(scale)
        END FOR
    END FUNCTION
    
    FUNCTION SetButtonOpacity(opacity: Float):
        settings.buttonOpacity = opacity
        
        FOR EACH (type, button) IN actionButtons:
            button.SetOpacity(opacity)
        END FOR
        
        movementJoystick.SetOpacity(opacity)
    END FUNCTION
    
    FUNCTION SetButtonPosition(button: TouchButton, position: Vector2):
        settings.customPositions[button] = position
        actionButtons[button].SetPosition(position)
    END FUNCTION
    
    FUNCTION GetButtonPosition(button: TouchButton) -> Vector2:
        RETURN actionButtons[button].GetPosition()
    END FUNCTION
    
    FUNCTION SaveLayout():
        SaveToSettings(settings)
    END FUNCTION
    
    FUNCTION LoadLayout():
        settings = LoadFromSettings()
        ApplySettings()
    END FUNCTION
    
    FUNCTION ResetToDefault():
        settings = NEW TouchInputSettings()
        ApplySettings()
    END FUNCTION
    
    FUNCTION ProcessTouchInput(position: Vector2, touchId: Integer, phase: TouchPhase):
        zone = DetermineZone(position)
        
        SWITCH phase:
            CASE Began:
                activeTouches[touchId] = zone
                HandleTouchBegan(position, zone)
            
            CASE Moved:
                HandleTouchMoved(position, touchId)
            
            CASE Ended:
                HandleTouchEnded(position, touchId)
                activeTouches.Remove(touchId)
        END SWITCH
    END FUNCTION

STRUCT TouchInputSettings:
    sensitivity: Float = 1.0
    aimSensitivity: Float = 0.8
    joystickDeadzone: Float = 0.15
    leftHandedMode: Boolean = false
    buttonScale: Float = 1.0
    buttonOpacity: Float = 0.6
    autoFire: Boolean = false
    holdToADS: Boolean = true
    customPositions: Map<TouchButton, Vector2>
```

---

### VirtualJoystickWidget

**Purpose:** On-screen joystick for movement.

```
CLASS VirtualJoystickWidget:
    // Visual elements
    outerRing: Image
    innerThumb: Image
    
    // Settings
    touchAreaSize: Float = 120.0
    visualSize: Float = 80.0
    deadzone: Float = 0.15
    opacity: Float = 0.6
    
    // State
    currentInput: Vector2
    isPressed: Boolean = false
    touchStartPosition: Vector2
    
    FUNCTION GetInputVector() -> Vector2:
        IF currentInput.Length() < deadzone:
            RETURN Vector2.Zero
        END IF
        
        // Normalize with deadzone compensation
        normalized = currentInput.Normalized()
        magnitude = (currentInput.Length() - deadzone) / (1.0 - deadzone)
        
        RETURN normalized * Clamp(magnitude, 0, 1)
    END FUNCTION
    
    FUNCTION GetInputMagnitude() -> Float:
        RETURN GetInputVector().Length()
    END FUNCTION
    
    FUNCTION IsActive() -> Boolean:
        RETURN isPressed
    END FUNCTION
    
    FUNCTION SetDeadzone(value: Float):
        deadzone = Clamp(value, 0, 0.5)
    END FUNCTION
    
    FUNCTION OnTouchStarted(position: Vector2):
        isPressed = true
        touchStartPosition = position
        
        // Show joystick at touch position
        outerRing.SetPosition(position)
        innerThumb.SetPosition(position)
        outerRing.SetOpacity(opacity)
        innerThumb.SetOpacity(opacity)
    END FUNCTION
    
    FUNCTION OnTouchMoved(position: Vector2):
        IF NOT isPressed:
            RETURN
        END IF
        
        // Calculate input
        delta = position - touchStartPosition
        maxDistance = visualSize / 2
        
        IF delta.Length() > maxDistance:
            delta = delta.Normalized() * maxDistance
        END IF
        
        currentInput = delta / maxDistance
        
        // Update thumb position
        innerThumb.SetPosition(touchStartPosition + delta)
    END FUNCTION
    
    FUNCTION OnTouchEnded():
        isPressed = false
        currentInput = Vector2.Zero
        
        // Hide or reset joystick
        outerRing.SetOpacity(opacity * 0.5)
        innerThumb.SetPosition(outerRing.GetPosition())
    END FUNCTION
```

---

### ActionButtonWidget

**Purpose:** Touch action button with visual feedback.

```
CLASS ActionButtonWidget:
    // Identity
    buttonType: TouchButton
    
    // Visual elements
    buttonCore: Button
    iconImage: Image
    cooldownOverlay: Image
    labelText: TextBlock
    
    // State
    isPressed: Boolean = false
    isToggled: Boolean = false
    isEnabled: Boolean = true
    
    // Config
    config: ActionButtonConfig
    
    FUNCTION IsPressed() -> Boolean:
        RETURN isPressed
    END FUNCTION
    
    FUNCTION IsToggled() -> Boolean:
        RETURN isToggled
    END FUNCTION
    
    FUNCTION SetEnabled(enabled: Boolean):
        isEnabled = enabled
        
        IF enabled:
            buttonCore.SetOpacity(1.0)
        ELSE:
            buttonCore.SetOpacity(0.5)
        END IF
    END FUNCTION
    
    FUNCTION SetIcon(icon: Texture2D):
        iconImage.SetTexture(icon)
    END FUNCTION
    
    FUNCTION SetCooldown(duration: Float, elapsed: Float):
        progress = elapsed / duration
        cooldownOverlay.SetPercent(1.0 - progress)
        cooldownOverlay.SetVisibility(progress < 1.0)
    END FUNCTION
    
    FUNCTION Flash(color: Color):
        PlayAnimation(CreateFlashAnimation(color, 0.2))
    END FUNCTION
    
    FUNCTION OnButtonPressed():
        IF NOT isEnabled:
            RETURN
        END IF
        
        isPressed = true
        
        IF config.isToggle:
            isToggled = NOT isToggled
        END IF
        
        // Visual feedback
        buttonCore.SetScale(0.95)
        
        // Haptic
        IF config.hapticIntensity > 0:
            TriggerHaptic(config.hapticIntensity)
        END IF
        
        TouchInputManager.OnButtonPressed.Broadcast(buttonType)
    END FUNCTION
    
    FUNCTION OnButtonReleased():
        isPressed = false
        buttonCore.SetScale(1.0)
        
        TouchInputManager.OnButtonReleased.Broadcast(buttonType)
    END FUNCTION

STRUCT ActionButtonConfig:
    defaultPosition: Vector2
    size: Vector2
    color: Color
    iconPath: String
    isToggle: Boolean = false
    autoHide: Boolean = false
    hapticIntensity: Float = 0.3

// Button configurations
CONST BUTTON_CONFIGS = {
    TB_Fire: { pos: (-80, -100), size: (100, 100), color: #F04444, icon: "T_Icon_Fire", toggle: false, haptic: 0.5 },
    TB_ADS: { pos: (-180, -100), size: (70, 70), color: #6B7280, icon: "T_Icon_ADS", toggle: false, haptic: 0.3 },
    TB_Reload: { pos: (-80, -200), size: (70, 70), color: #FBBF24, icon: "T_Icon_Reload", autoHide: true, haptic: 0.3 },
    TB_Crouch: { pos: (180, -80), size: (70, 70), color: #6B7280, icon: "T_Icon_Crouch", toggle: true, haptic: 0.2 },
    TB_Interact: { pos: (80, -160), size: (80, 80), color: #06B6D4, icon: "T_Icon_Interact", autoHide: true, haptic: 0.4 }
}
```

---

### PopupManager

**Purpose:** Modal dialogs and popups.

```
CLASS PopupManager:
    // Active popups
    activePopups: List<PopupWidget>
    popupContainer: CanvasPanel
    
    FUNCTION ShowConfirmPopup(title: String, message: String, onConfirm: Callback, onCancel: Callback) -> PopupWidget:
        popup = CreatePopup(ConfirmPopupWidget)
        popup.Setup(title, message)
        popup.OnConfirm.AddListener(onConfirm)
        popup.OnCancel.AddListener(onCancel)
        
        ShowPopup(popup)
        
        RETURN popup
    END FUNCTION
    
    FUNCTION ShowInfoPopup(title: String, message: String) -> PopupWidget:
        popup = CreatePopup(InfoPopupWidget)
        popup.Setup(title, message)
        
        ShowPopup(popup)
        
        RETURN popup
    END FUNCTION
    
    FUNCTION ShowInputPopup(title: String, placeholder: String, onSubmit: Callback<String>) -> PopupWidget:
        popup = CreatePopup(InputPopupWidget)
        popup.Setup(title, placeholder)
        popup.OnSubmit.AddListener(onSubmit)
        
        ShowPopup(popup)
        
        RETURN popup
    END FUNCTION
    
    FUNCTION ShowCustomPopup(popupClass: Class) -> PopupWidget:
        popup = CreatePopup(popupClass)
        
        ShowPopup(popup)
        
        RETURN popup
    END FUNCTION
    
    FUNCTION ShowLoadingPopup(message: String) -> LoadingWidget:
        popup = CreatePopup(LoadingWidget)
        popup.SetMessage(message)
        
        ShowPopup(popup)
        
        RETURN popup
    END FUNCTION
    
    FUNCTION DismissPopup(popup: PopupWidget):
        AnimatePopupOut(popup, LAMBDA:
            activePopups.Remove(popup)
            popup.Destroy()
            
            // Remove modal block if no popups
            IF activePopups.IsEmpty():
                HideModalBackground()
            END IF
        END LAMBDA)
    END FUNCTION
    
    FUNCTION DismissAllPopups():
        FOR EACH popup IN activePopups.ToList():
            DismissPopup(popup)
        END FOR
    END FUNCTION
    
    FUNCTION HasActivePopup() -> Boolean:
        RETURN NOT activePopups.IsEmpty()
    END FUNCTION
    
    FUNCTION ShowPopup(popup: PopupWidget):
        activePopups.Add(popup)
        popupContainer.AddChild(popup)
        
        ShowModalBackground()
        AnimatePopupIn(popup)
    END FUNCTION
    
    FUNCTION AnimatePopupIn(popup: PopupWidget):
        popup.SetScale(0.8)
        popup.SetOpacity(0)
        
        AnimateTo(popup, { scale: 1.0, opacity: 1.0 }, 0.25, EaseOutBack)
    END FUNCTION
    
    FUNCTION AnimatePopupOut(popup: PopupWidget, onComplete: Callback):
        AnimateTo(popup, { scale: 0.8, opacity: 0 }, 0.2, EaseInBack, onComplete)
    END FUNCTION
```

---

### NotificationManager

**Purpose:** Toast and notification system.

```
CLASS NotificationManager:
    // Active notifications
    activeNotifications: List<NotificationWidget>
    notificationQueue: List<PendingNotification>
    
    // Limits
    maxToasts: Integer = 3
    maxLootNotifications: Integer = 5
    
    FUNCTION ShowToast(message: String, duration: Float = 3.0):
        notification = NEW PendingNotification()
        notification.type = NT_Toast
        notification.message = message
        notification.duration = duration
        
        QueueNotification(notification)
    END FUNCTION
    
    FUNCTION ShowAlert(message: String, severity: AlertSeverity = Warning):
        notification = NEW PendingNotification()
        notification.type = NT_Alert
        notification.message = message
        notification.duration = 5.0
        notification.severity = severity
        
        // Alerts show immediately
        DisplayNotification(notification)
    END FUNCTION
    
    FUNCTION ShowLootNotification(item: ItemData):
        notification = NEW PendingNotification()
        notification.type = NT_Loot
        notification.itemData = item
        notification.duration = 2.0
        
        QueueNotification(notification)
    END FUNCTION
    
    FUNCTION ShowAchievement(achievement: AchievementData):
        notification = NEW PendingNotification()
        notification.type = NT_Achievement
        notification.achievementData = achievement
        notification.duration = 5.0
        
        // Achievements are modal-like
        DisplayNotification(notification)
    END FUNCTION
    
    FUNCTION ShowQuestUpdate(questName: String, progress: String):
        notification = NEW PendingNotification()
        notification.type = NT_Quest
        notification.message = questName + ": " + progress
        notification.duration = 4.0
        
        QueueNotification(notification)
    END FUNCTION
    
    FUNCTION ShowLevelUp(newLevel: Integer):
        notification = NEW PendingNotification()
        notification.type = NT_LevelUp
        notification.message = "Level " + newLevel
        notification.duration = 5.0
        
        DisplayNotification(notification)
    END FUNCTION
    
    FUNCTION ClearAll():
        FOR EACH notif IN activeNotifications.ToList():
            DismissNotification(notif)
        END FOR
        
        notificationQueue.Clear()
    END FUNCTION
    
    FUNCTION ClearType(type: NotificationType):
        FOR EACH notif IN activeNotifications.ToList():
            IF notif.type == type:
                DismissNotification(notif)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION ProcessQueue():
        WHILE notificationQueue.Count > 0 AND CanShowMore():
            pending = notificationQueue.RemoveFirst()
            DisplayNotification(pending)
        END WHILE
    END FUNCTION
    
    FUNCTION RemoveExpiredNotifications():
        FOR EACH notif IN activeNotifications.ToList():
            notif.remainingTime -= DeltaTime
            
            IF notif.remainingTime <= 0:
                DismissNotification(notif)
            END IF
        END FOR
    END FUNCTION

STRUCT PendingNotification:
    type: NotificationType
    message: String
    duration: Float
    widgetClass: Class
    itemData: ItemData
    achievementData: AchievementData
    severity: AlertSeverity

ENUM AlertSeverity:
    Info, Warning, Error, Critical

// Notification positioning
CONST NOTIFICATION_LAYOUTS = {
    NT_Toast: { anchor: TopCenter, offset: (0, 60), duration: 3.0, max: 3 },
    NT_Alert: { anchor: TopCenter, offset: (0, 120), duration: 5.0, max: 1 },
    NT_Loot: { anchor: RightCenter, offset: (-20, 0), duration: 4.0, max: 5 },
    NT_Achievement: { anchor: Center, offset: (0, 0), duration: 5.0, max: 1 },
    NT_LevelUp: { anchor: Center, offset: (0, -100), duration: 4.0, max: 1 }
}
```

---

### InventoryWidget

**Purpose:** Inventory grid with drag-drop support.

```
CLASS InventoryWidget:
    // Visual elements
    itemGrid: UniformGridPanel
    detailPanel: ItemDetailPanel
    filterDropdown: ComboBox
    sortDropdown: ComboBox
    searchBox: EditableTextBox
    capacityText: TextBlock
    
    // State
    slotWidgets: List<InventorySlotWidget>
    selectedSlot: InventorySlotWidget
    draggedSlot: InventorySlotWidget
    
    // Filter/Sort
    currentFilter: ItemCategory
    currentSortMode: InventorySortMode
    
    FUNCTION RefreshInventory():
        items = InventoryManager.GetAllItems()
        
        // Apply filters
        filteredItems = ApplyFilters(items)
        
        // Apply sort
        sortedItems = ApplySort(filteredItems)
        
        // Update grid
        PopulateGrid(sortedItems)
        
        // Update capacity display
        capacityText.SetText(items.Count + " / " + InventoryManager.GetCapacity())
    END FUNCTION
    
    FUNCTION SetFilter(filter: ItemCategory):
        currentFilter = filter
        RefreshInventory()
    END FUNCTION
    
    FUNCTION SetSortMode(mode: InventorySortMode):
        currentSortMode = mode
        RefreshInventory()
    END FUNCTION
    
    FUNCTION SelectItem(slot: InventorySlotWidget):
        IF selectedSlot != null:
            selectedSlot.SetSelected(false)
        END IF
        
        selectedSlot = slot
        slot.SetSelected(true)
        
        // Show details
        detailPanel.ShowItem(slot.GetItem())
    END FUNCTION
    
    FUNCTION DeselectItem():
        IF selectedSlot != null:
            selectedSlot.SetSelected(false)
            selectedSlot = null
        END IF
        
        detailPanel.Hide()
    END FUNCTION
    
    FUNCTION PopulateGrid(items: List<ItemData>):
        // Clear existing
        FOR EACH slot IN slotWidgets:
            slot.ClearItem()
        END FOR
        
        // Populate slots
        FOR i = 0 TO items.Count:
            IF i < slotWidgets.Count:
                slotWidgets[i].SetItem(items[i])
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION ApplyFilters(items: List<ItemData>) -> List<ItemData>:
        result = items
        
        // Category filter
        IF currentFilter != AllCategories:
            result = result.Where(item => item.category == currentFilter)
        END IF
        
        // Search filter
        searchText = searchBox.GetText().ToLower()
        IF searchText.Length > 0:
            result = result.Where(item => item.name.ToLower().Contains(searchText))
        END IF
        
        RETURN result
    END FUNCTION
    
    FUNCTION ApplySort(items: List<ItemData>) -> List<ItemData>:
        SWITCH currentSortMode:
            CASE Rarity:
                RETURN items.OrderByDescending(item => item.rarity)
            CASE Value:
                RETURN items.OrderByDescending(item => item.value)
            CASE Name:
                RETURN items.OrderBy(item => item.name)
            CASE Recent:
                RETURN items.OrderByDescending(item => item.acquiredAt)
            CASE Type:
                RETURN items.OrderBy(item => item.category)
        END SWITCH
    END FUNCTION

ENUM InventorySortMode:
    Rarity, Value, Name, Recent, Type
```

---

### ScreenAdapter

**Purpose:** Responsive scaling for different devices.

```
CLASS ScreenAdapter:
    // Design reference: 1920x1080
    CONST DESIGN_WIDTH = 1920.0
    CONST DESIGN_HEIGHT = 1080.0
    
    FUNCTION GetScreenSize() -> Vector2:
        RETURN GetViewportSize()
    END FUNCTION
    
    FUNCTION GetScreenAspectRatio() -> Float:
        size = GetScreenSize()
        RETURN size.X / size.Y
    END FUNCTION
    
    FUNCTION GetDPIScale() -> Float:
        RETURN GetPlatformDPIScale()
    END FUNCTION
    
    FUNCTION ScaleToScreen(designSize: Vector2) -> Vector2:
        scale = CalculateScale()
        RETURN designSize * scale
    END FUNCTION
    
    FUNCTION GetSafeZoneInset(edge: SafeZoneEdge) -> Float:
        safeZone = GetPlatformSafeZone()
        
        SWITCH edge:
            CASE Top: RETURN safeZone.top
            CASE Bottom: RETURN safeZone.bottom
            CASE Left: RETURN safeZone.left
            CASE Right: RETURN safeZone.right
        END SWITCH
    END FUNCTION
    
    FUNCTION IsTablet() -> Boolean:
        diagonalInches = GetScreenDiagonalInches()
        RETURN diagonalInches >= 7.0
    END FUNCTION
    
    FUNCTION IsNotched() -> Boolean:
        RETURN GetSafeZoneInset(Top) > 20
    END FUNCTION
    
    FUNCTION CalculateScale() -> Vector2:
        screenSize = GetScreenSize()
        
        scaleX = screenSize.X / DESIGN_WIDTH
        scaleY = screenSize.Y / DESIGN_HEIGHT
        
        // Use minimum to maintain aspect ratio
        uniformScale = Min(scaleX, scaleY)
        
        RETURN Vector2(uniformScale, uniformScale)
    END FUNCTION

ENUM SafeZoneEdge:
    Top, Bottom, Left, Right

// Touch target minimum sizes (in dp)
CONST TOUCH_TARGET_SIZES:
    SmallButton = 60.0
    MediumButton = 80.0
    LargeButton = 100.0
    TouchPadding = 20.0
    MinSpacing = 16.0
    ScreenMargin = 24.0
```

---

### UIAnimationPresets

**Purpose:** Common UI animation effects.

```
// Animation preset functions
FUNCTION CreateFadeIn(duration: Float = 0.3) -> WidgetAnimation:
    RETURN AnimateFromTo({ opacity: 0 }, { opacity: 1 }, duration, EaseOutQuad)
END FUNCTION

FUNCTION CreateFadeOut(duration: Float = 0.3) -> WidgetAnimation:
    RETURN AnimateFromTo({ opacity: 1 }, { opacity: 0 }, duration, EaseInQuad)
END FUNCTION

FUNCTION CreatePopIn(duration: Float = 0.25) -> WidgetAnimation:
    RETURN AnimateFromTo({ scale: 0.8, opacity: 0 }, { scale: 1.0, opacity: 1 }, duration, EaseOutBack)
END FUNCTION

FUNCTION CreatePopOut(duration: Float = 0.2) -> WidgetAnimation:
    RETURN AnimateFromTo({ scale: 1.0, opacity: 1 }, { scale: 0.8, opacity: 0 }, duration, EaseInBack)
END FUNCTION

FUNCTION CreateSlideFromLeft(duration: Float = 0.3) -> WidgetAnimation:
    RETURN AnimateFromTo({ translateX: -100 }, { translateX: 0 }, duration, EaseOutQuad)
END FUNCTION

FUNCTION CreateSlideFromRight(duration: Float = 0.3) -> WidgetAnimation:
    RETURN AnimateFromTo({ translateX: 100 }, { translateX: 0 }, duration, EaseOutQuad)
END FUNCTION

FUNCTION CreateSlideFromBottom(duration: Float = 0.3) -> WidgetAnimation:
    RETURN AnimateFromTo({ translateY: 100 }, { translateY: 0 }, duration, EaseOutQuad)
END FUNCTION

FUNCTION CreatePulse(duration: Float = 0.5, count: Integer = 2) -> WidgetAnimation:
    RETURN AnimateSequence([
        { scale: 1.0 },
        { scale: 1.1 },
        { scale: 1.0 }
    ], duration / count, RepeatCount: count)
END FUNCTION

FUNCTION CreateShake(intensity: Float = 5.0, duration: Float = 0.3) -> WidgetAnimation:
    RETURN AnimateSequence([
        { translateX: intensity },
        { translateX: -intensity },
        { translateX: intensity / 2 },
        { translateX: -intensity / 2 },
        { translateX: 0 }
    ], duration / 5)
END FUNCTION

FUNCTION CreateFlash(color: Color, duration: Float = 0.2) -> WidgetAnimation:
    RETURN AnimateSequence([
        { tintColor: color },
        { tintColor: White }
    ], duration)
END FUNCTION

ENUM UIEasing:
    Linear,
    EaseInQuad,
    EaseOutQuad,
    EaseInOutQuad,
    EaseOutBack,   // For pop-in effects
    EaseInBack,    // For pop-out effects
    EaseOutElastic // Bouncy
```

---

## UI Settings Data

```
STRUCT UISettings:
    // HUD
    hudScale: Float = 1.0
    minimapSize: Float = 150.0
    minimapZoom: Float = 200.0
    showDamageNumbers: Boolean = true
    showKillFeed: Boolean = true
    showQuestTracker: Boolean = true
    
    // Crosshair
    crosshairStyle: CrosshairStyle = Cross
    crosshairColor: Color = #FFFFFF
    crosshairSize: Float = 1.0
    crosshairOpacity: Float = 1.0
    
    // Touch Controls
    sensitivity: Float = 1.0
    buttonScale: Float = 1.0
    buttonOpacity: Float = 0.6
    leftHandedMode: Boolean = false
    autoFire: Boolean = false
    holdToADS: Boolean = true
    
    // Accessibility
    textScale: Float = 1.0
    highContrastMode: Boolean = false
    reduceMotion: Boolean = false

ENUM CrosshairStyle:
    Dot, Cross, Circle, Dynamic
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] UIManager core
- [ ] ScreenManager with transitions
- [ ] HUDManager with health/ammo
- [ ] TouchInputManager with joystick
- [ ] Action button widgets

### MEDIUM Priority 🟡
- [ ] PopupManager with modals
- [ ] NotificationManager with queue
- [ ] Inventory grid with drag-drop
- [ ] Minimap widget
- [ ] Crosshair customization

### LOW Priority 🟢
- [ ] Widget animation system
- [ ] Responsive scaling
- [ ] Button layout editor
- [ ] HUD element positioning
- [ ] Advanced minimap features

---

## Testing Checklist

- [ ] Screen transitions smooth
- [ ] All buttons respond to touch
- [ ] Joystick deadzone works
- [ ] HUD elements update correctly
- [ ] Minimap markers accurate
- [ ] Damage indicators show direction
- [ ] Kill feed scrolls properly
- [ ] Notifications queue correctly
- [ ] Popups block input behind
- [ ] Inventory drag-drop works
- [ ] Settings persist across sessions
- [ ] UI scales on different devices
- [ ] Safe zones respected on notched devices

---

**[← Back to Index](../README.md)** | **[Next: Audio System →](./AudioSystem.md)**
