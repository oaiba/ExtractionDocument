---
title: "Accessibility System - Technical Specification"
type: docs
---

## Overview

The **Accessibility System** provides visual, auditory, motor, and cognitive accommodations for players with different needs.

---

## Enums & Types

### ColorblindMode
Colorblind correction filter modes.

| Code Name          | Display Name | Description                                |
| :----------------- | :----------- | :----------------------------------------- |
| `CBM_Off`          | Off          | No color correction applied                |
| `CBM_Protanopia`   | Protanopia   | Red-weak correction (red→orange shift)     |
| `CBM_Deuteranopia` | Deuteranopia | Green-weak correction (green→yellow shift) |
| `CBM_Tritanopia`   | Tritanopia   | Blue-yellow correction (blue→cyan shift)   |
| `CBM_Monochromacy` | Monochromacy | Full grayscale mode                        |

---

### TextSize
UI text scaling multiplier.

| Code Name       | Display Name | Scale | Description       |
| :-------------- | :----------- | :---- | :---------------- |
| `TS_Small`      | Small        | 75%   | Compact text      |
| `TS_Normal`     | Normal       | 100%  | Default text size |
| `TS_Large`      | Large        | 150%  | Larger text       |
| `TS_ExtraLarge` | Extra Large  | 200%  | Maximum text size |

---

### SubtitleMode
Subtitle display configuration.

| Code Name         | Display Name  | Description                     |
| :---------------- | :------------ | :------------------------------ |
| `SM_Off`          | Off           | No subtitles displayed          |
| `SM_DialogueOnly` | Dialogue Only | Spoken dialogue only            |
| `SM_All`          | All Sounds    | Dialogue + environmental sounds |

---

### AimAssistLevel
Aim assist strength for touch/controller.

| Code Name    | Display Name | Friction | Magnetism | Lock-On |
| :----------- | :----------- | :------- | :-------- | :------ |
| `AAL_Off`    | Off          | 0%       | 0%        | 0%      |
| `AAL_Low`    | Low          | 20%      | 0%        | 0%      |
| `AAL_Medium` | Medium       | 40%      | 15%       | 0%      |
| `AAL_High`   | High         | 60%      | 30%       | 50%     |
| `AAL_Max`    | Maximum      | 80%      | 50%       | 80%     |

---

### InputToggleType
Input behavior for actions.

| Code Name    | Display Name | Description                     |
| :----------- | :----------- | :------------------------------ |
| `ITT_Hold`   | Hold         | Action active while button held |
| `ITT_Toggle` | Toggle       | Single press toggles on/off     |

---

### AccessibilityPreset
Pre-configured accessibility profiles.

| Code Name             | Display Name      | Primary Settings                     |
| :-------------------- | :---------------- | :----------------------------------- |
| `AP_Default`          | Default           | Standard settings                    |
| `AP_VisionImpaired`   | Vision Impaired   | Large text, high contrast            |
| `AP_ColorBlind`       | Color Blind       | Colorblind filter, symbol indicators |
| `AP_HardOfHearing`    | Hard of Hearing   | Subtitles all, sound visualizer      |
| `AP_MotorLimited`     | Motor Limited     | Max aim assist, auto actions         |
| `AP_CognitiveSupport` | Cognitive Support | Simplified HUD, frequent hints       |
| `AP_Custom`           | Custom            | User-defined                         |

---

### SoundVisualizerPosition
Position of visual sound indicators.

| Code Name     | Display Name | Description            |
| :------------ | :----------- | :--------------------- |
| `SVP_Edge`    | Screen Edge  | Icons at screen edges  |
| `SVP_Ring`    | Compass Ring | Icons around crosshair |
| `SVP_Minimap` | Minimap      | Indicators on minimap  |

---

## Code Names

### System Events

| Code Name                      | Trigger            | Description                  |
| :----------------------------- | :----------------- | :--------------------------- |
| `ACC_PRESET_APPLIED`           | Preset selected    | Accessibility preset applied |
| `ACC_COLORBLIND_ENABLED`       | Colorblind on      | Filter enabled               |
| `ACC_SUBTITLE_ENABLED`         | Subtitles on       | Subtitle mode activated      |
| `ACC_TEXT_SIZE_CHANGED`        | Text size changed  | UI scale adjusted            |
| `ACC_SOUND_VISUALIZER_ENABLED` | Visualizer on      | Sound visualization enabled  |
| `ACC_AIM_ASSIST_CHANGED`       | Aim assist changed | Aim assist level adjusted    |

---

## Core Classes

### AccessibilityManager

**Purpose:** Central controller for accessibility settings.

```
CLASS AccessibilityManager:
    currentSettings: AccessibilitySettings
    
    // Events
    OnSettingsChanged: Event<()>
    
    FUNCTION ApplyPreset(preset: AccessibilityPreset):
        settings = GetPresetSettings(preset)
        ApplySettings(settings)
        EMIT EVENT "ACC_PRESET_APPLIED" WITH (preset)
    END FUNCTION
    
    FUNCTION ApplySettings(settings: AccessibilitySettings):
        currentSettings = settings
        
        // Visual
        SetColorblindMode(settings.ColorblindMode)
        SetTextSize(settings.TextSize)
        SetHighContrast(settings.bHighContrast)
        SetScreenShake(settings.Photosensitivity.ScreenShakeIntensity)
        SetFlashEffects(settings.Photosensitivity.bDisableFlashing)
        
        // Audio
        SetSubtitleMode(settings.Subtitles.Mode)
        SetSubtitleSize(settings.Subtitles.Size)
        SetSoundVisualization(settings.bSoundVisualization)
        SetMonoAudio(settings.bMonoAudio)
        
        // Motor
        SetAimAssist(settings.AimAssist.Level)
        SetInputToggleTypes(settings.InputTypes)
        SetAutoActions(settings.AutoActions)
        
        // Cognitive
        SetSimplifiedHUD(settings.SimplifiedMode.bSimplifiedHUD)
        
        OnSettingsChanged.Broadcast()
    END FUNCTION

    FUNCTION SetColorblindMode(mode: ColorblindMode):
        // Update post-process volume
        params = GetColorblindParams(mode)
        PostProcessManager.SetColorblindParams(params)
    END FUNCTION
```

---

### SoundVisualizer

**Purpose:** Visual indicators for audio events.

```
CLASS SoundVisualizer:
    activeIndicators: List<SoundIndicator>
    
    FUNCTION DisplaySoundIndicator(sound: SoundEvent, position: Vector3):
        type = GetSoundType(sound)
        
        indicator = NEW SoundIndicator()
        indicator.Type = type
        indicator.WorldPosition = position
        indicator.Lifetime = 2.0
        
        activeIndicators.Add(indicator)
        HUDManager.ShowIndicator(indicator)
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        FOR EACH indicator IN activeIndicators:
             indicator.Lifetime -= deltaTime
             IF indicator.Lifetime <= 0:
                 HUDManager.RemoveIndicator(indicator)
                 activeIndicators.Remove(indicator)
             END IF
        END FOR
    END FUNCTION
```

---

## Data Structures

```
STRUCT AccessibilitySettings:
    // Visual
    ColorblindMode: ColorblindMode
    TextSize: TextSize
    bHighContrast: Boolean
    Photosensitivity: PhotosensitivitySettings
    
    // Audio
    Subtitles: SubtitleSettings
    bSoundVisualization: Boolean
    bMonoAudio: Boolean
    
    // Motor
    AimAssist: AimAssistSettings
    AutoActions: AutoActionSettings
    InputTypes: Map<InputAction, InputToggleType>
    
    // Cognitive
    SimplifiedMode: SimplifiedModeSettings

STRUCT ColorblindParams:
    RedShift: LinearColor
    GreenShift: LinearColor
    BlueShift: LinearColor
    Intensity: Float

STRUCT AimAssistSettings:
    Level: AimAssistLevel
    Structure: AimAssistParams

STRUCT AimAssistParams:
    Friction: Float
    Magnetism: Float
    LockOn: Float
    SnapDistance: Float

STRUCT AutoActionSettings:
    bAutoSprint: Boolean
    bAutoFire: Boolean
    bAutoPickup: Boolean
    bAutoReload: Boolean
    bAutoVault: Boolean
```

---

## TODO: Implementation Tasks

### HIGH Priority 
- [ ] AccessibilityManager core
- [ ] Colorblind post-process shader
- [ ] Subtitle system basic implementation
- [ ] Aim assist parameter integration

### MEDIUM Priority 
- [ ] Sound visualization system
- [ ] UI scaling logic
- [ ] Input toggle/hold system
- [ ] Preset configuration

### LOW Priority 
- [ ] Text-to-speech integration
- [ ] Screen reader support
- [ ] One-handed mode configuration



