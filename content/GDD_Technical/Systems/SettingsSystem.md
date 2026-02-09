---
title: "Settings System - Technical Specification"
type: docs
---

**[↔ View Design GDD: User Settings](../../GDD_Design/GameDesign/UserSettings.md)**

## ⚙️ Overview

The **Settings System** acts as the bridge between the Player UI preferences and the Core Engine implementations. It manages the lifecycle of settings from user input to persistent storage and engine application.

### Key Responsibilities
- **Storage**: Manage local `.ini` files and Cloud Sync payloads.
- **Application**: Real-time update of Engine Scalability, Audio Mixers, and Input Modifiers.
- **Validation**: Ensure user inputs stay within safe/performant ranges.
- **Abstraction**: Provide a unified interface for Cross-Platform settings (PC/Mobile).

---

## 🏗️ Architecture

### Class & Data Structure
The system is built on top of Unreal's `UGameUserSettings` but extended via a custom `UAdvancedSettingsSubsystem`.

#### **FUserSettingsData** (Main Struct)
```cpp
USTRUCT(BlueprintType)
struct FUserSettingsData {
    GENERATED_BODY()

    // Control Group
    UPROPERTY() float HorizontalSensitivity;
    UPROPERTY() float VerticalSensitivity;
    UPROPERTY() EInputResponseCurve ResponseCurve;
    UPROPERTY() bool bInvertLook;

    // Video Group
    UPROPERTY() int32 ResolutionQuality;
    UPROPERTY() int32 ViewDistanceQuality;
    UPROPERTY() bool bEnableVSync;

    // Audio Group
    UPROPERTY() TMap<FName, float> SoundClassVolumes; // Key: SC_SFX, SC_Music, etc.
};
```

---

## 🔧 Core Implementation

### 🎮 Control Implementation
| Technical Key | Engine Variable / Property | Implementation Detail |
| :--- | :--- | :--- |
| `LookSens` | `PlayerController->InputYawScale` | Multiplied by FrameDelta for consistent turn rate. |
| `ADS_Sens` | `InputModifier_Scale` | Applied dynamically to Enhanced Input Mapping Context. |
| `Deadzone` | `UInputSettings::Deadzone` | Min threshold applied before processing raw analog data. |
| `InputRef` | `EInputReferenceFrame` | Custom logic in `MovementController` to rotate input vector. |

### 🖥️ Graphics & Scalability
*Uses Unreal Engine Scalability Groups (`sg.*`).*

| Setting | console Variable (CVar) | Type | Range |
| :--- | :--- | :--- | :--- |
| **Res Scale** | `r.ScreenPercentage` | Float | 50.0 - 100.0 |
| **V-Sync** | `r.VSync` | Bool | 0 / 1 |
| **Reflex** | `r.NVIDIA.Reflex.Mode` | Enum | 0 (Off), 1 (On), 2 (Boost) |
| **View Dist.** | `sg.ViewDistanceQuality` | Int | 0 (Low) to 3 (Epic) |
| **Shadows** | `sg.ShadowQuality` | Int | 0 to 3 |

### 🔊 Audio Mixer & Submixes
Settings are applied to a `USoundControlBus` or directly to `USoundClass`.

| Mixer Channel | Sound Class Asset | Submix Effect |
| :--- | :--- | :--- |
| **Master** | `SC_Master` | Main Output Submix |
| **SFX** | `SC_SFX`, `SC_Weapon` | Dynamic Range Compressor (Night Mode) |
| **Voice** | `SC_VoiceChat` | Side-chain to lower Game SFX when active. |
| **Music** | `SC_Music` | EQ Filter (Treble/Bass Boost) |

---

## 💾 Persistence & Synchronization

### Local Storage
- **PC**: `%LOCALAPPDATA%/[ProjectName]/Saved/Config/Windows/GameUserSettings.ini`
- **Mobile**: Application Persistent Data Path (Binary Encrypted format).

### Cloud Sync Workflow
1. **Change Detected**: UI calls `ApplySettings()`.
2. **Local Save**: `UGameUserSettings::SaveSettings()` called immediately.
3. **Dirty Flag**: `bSettingsDirty` set to true.
4. **Cloud Hook**: `USaveSystem::NotifySettingsChanged()` triggers async upload to GameServer/iCloud/GooglePlay.

---

## 📝 Coding Standards & SDKs

### SDK Requirements
- **NVIDIA Reflex SDK**: For low-latency mode implementation.
- **DLSS/FSR SDK**: Integrated via Unreal Engine Plugins.
- **Steam Audio / Oculus Audio**: Spatialization for "Binaural Audio" setting.

### Event Codenames
| Code Name | Trigger | Payload |
| :--- | :--- | :--- |
| `SET_APPLY_ALL` | User clicks [APPLY] | null |
| `SET_RESET_DEF` | User clicks [RESET] | `ESettingGroup` |
| `SET_CHANGED_VID`| Resolution/Window changed | `FIntPoint` |
| `SET_KEY_REBIND`| Input remapping confirmed | `FKey`, `FName` Action |

---

## 📅 TODO List (Technical)

- [ ] (P0) Implement `UAdvancedSettingsSubsystem` skeleton.
- [ ] (P1) Map UI Sliders to `USoundControlBusMix`.
- [ ] (P1) Integrate NVIDIA Reflex Plugin.
- [ ] (P2) Create custom `UInputModifier` for Dynamic Sensitivity.
- [ ] (P3) Implement "Night Mode" Dynamic Range Compression Submix.
