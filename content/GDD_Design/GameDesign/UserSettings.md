---
title: "User Settings & Configuration"
type: docs
---

**[↔ View Technical Spec: Settings System](../../GDD_Technical/Systems/SettingsSystem.md)**

## ⚙️ Design Philosophy

**"Power to the Player, Simplicity for the Casual."**
Settings should offer granular control for competitive players while providing simple, intelligent presets for casual users. All settings must be **saved to the cloud** and synced across devices.

### 📐 UI Wireframe Visualization
```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  SETTINGS                                                            [ X ]   │
├──────────────────────────────────────────────────────────────────────────────┤
│  [ 🎮 CONTROLS ]  [ 🖥️ GRAPHICS ]  [ 🔊 AUDIO ]  [ 📡 GAMEPLAY ]  [ 💾 ACC ]  │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SENSITIVITY ─────────────────────────────────────── [ 1.0 ] [|||||·     ]  │
│   ADS MULTIPLIER ──────────────────────────────────── [ 0.8 ] [||||·      ]  │
│                                                                              │
│   INVERT LOOK ─────────────────────────────────────────── [ OFF ] [ ○     ]  │
│   VIBRATION ───────────────────────────────────────────── [ ON  ] [     ● ]  │
│                                                                              │
│   CROUCH MODE ─────────────────────────────────────────── <  TOGGLE  >       │
│   SPRINT MODE ─────────────────────────────────────────── <   HOLD   >       │
│                                                                              │
│   ...                                                                        │
│                                                                              │
│   [ EDIT KEYBINDINGS ]                                                       │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│  [ ↺ RESET ]                                  [ CANCEL ]  [ APPLY ]  [ OK ]  │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎮 1. Control Settings (Input)

*Widgets arranged by usage frequency and importance.*

### **Primary Input**
| Setting                 | Gameplay Tag                        | Type                         | Default   | Description                                     |
| :---------------------- | :---------------------------------- | :--------------------------- | :-------- | :---------------------------------------------- |
| **Input Method**        | `Settings.Input.Method`             | Auto / KBM / Gamepad / Touch | Automatic | Preferred input device or detection mode.       |
| **Sensitivity**         | `Settings.Input.Sensitivity.Global` | Slider (0.1 - 5.0)           | 1.0       | Global mouse/touch sensitivity.                 |
| **ADS Sensitivity**     | `Settings.Input.Sensitivity.ADS`    | Slider (0.1 - 2.0)           | 0.8       | Sensitivity multiplier when Aiming Down Sights. |
| **Scope Sensitivity**   | `Settings.Input.Sensitivity.Scope`  | Slider (0.1 - 2.0)           | 0.6       | Multiplier for high-zoom scopes (>4x).          |
| **Invert Look**         | `Settings.Input.InvertLook`         | Toggle                       | OFF       | Invert Y-axis.                                  |
| **Look Response Curve** | `Settings.Input.ResponseCurve`      | Standard / Linear / Dynamic  | Standard  | Input curve mapping.                            |

### **Movement & Combat Behaviors**
| Setting              | Gameplay Tag                         | Option                  | Default    | Description                                                  |
| :------------------- | :----------------------------------- | :---------------------- | :--------- | :----------------------------------------------------------- |
| **Crouch Mode**      | `Settings.Control.CrouchBehavior`    | Hold / Toggle           | Toggle     | "Hold" requires keeping the key pressed.                     |
| **Prone Mode**       | `Settings.Control.ProneBehavior`     | Hold / Toggle           | Toggle     | Separate keybind available.                                  |
| **Sprint Mode**      | `Settings.Control.SprintBehavior`    | Hold / Toggle           | Toggle     | "Hold" stops sprinting on release.                           |
| **Tactical Sprint**  | `Settings.Control.TacSprintBehavior` | Single Tap / Double Tap | Double Tap | Engage super-sprint (weapon up, slower fire time).           |
| **Walk Mode**        | `Settings.Control.WalkBehavior`      | Hold / Toggle           | Hold       | Silent movement modifier.                                    |
| **Lean Mode**        | `Settings.Control.LeanBehavior`      | Hold / Toggle / Auto    | Hold       | Peek around corners. "Auto" leans when near edge.            |
| **Aim Mode**         | `Settings.Control.AimBehavior`       | Hold / Toggle           | Hold       | Aiming Down Sights (ADS) behavior.                           |
| **ADS Transition**   | `Settings.Control.ADSTransition`     | Smooth / Instant        | Smooth     | "Smooth" blends animation (realistic). "Instant" snaps view. |
| **Quick Throw**      | `Settings.Combat.QuickThrow`         | ON / OFF                | ON         | Grenade throws immediately on key press.                     |
| **Bolt Action Mode** | `Settings.Combat.BoltActionMode`     | Release / Manual        | Release    | "Release" cycles bolt on key release.                        |

### **Controller & Mobile Specific**
| Setting              | Gameplay Tag                      | Option                          | Default  | Description                                     |
| :------------------- | :-------------------------------- | :------------------------------ | :------- | :---------------------------------------------- |
| **Vibration**        | `Settings.Input.Vibration`        | Toggle                          | ON       | Haptic feedback for shooting/damage.            |
| **Aim Assist**       | `Settings.Input.AimAssist`        | Standard / Precision / Focusing | Standard | "Standard" slows near target.                   |
| **Stick Deadzone**   | `Settings.Input.Deadzone`         | Slider (0.00 - 0.50)            | 0.10     | Min input to register movement (fixes drift).   |
| **Gyro Aiming**      | `Settings.Input.Gyro.Mode`        | OFF / Scope / Always            | Scope    | Use device tilt for fine adjustments.           |
| **Gyro Sensitivity** | `Settings.Input.Gyro.Sensitivity` | Slider (1-300%)                 | 100%     | Separate X/Y axis sliders.                      |
| **Touch Mode**       | `Settings.Input.Touch.Mode`       | Touchpad / Virtual Joystick     | Joystick | **(Mobile)** Look via swiping or virtual stick. |
| **Automations**      | `Settings.Input.Touch.Automation` | Auto-Loot / Auto-Open Doors     | ON       | Mobile QoL features.                            |

### **Key Bindings (PC Default)**
*System support for Primary and Secondary bindings.*

#### **Movement**
| Action              | Gameplay Tag          | Primary         | Secondary | Context                    |
| :------------------ | :-------------------- | :-------------- | :-------- | :------------------------- |
| **Move**            | `Input.Action.Move`   | `W`,`A`,`S`,`D` |           |                            |
| **Jump / Vault**    | `Input.Action.Jump`   | `Space`         |           | Vaults if near obstacle.   |
| **Sprint**          | `Input.Action.Sprint` | `L-Shift`       |           | Double-tap for Tac Sprint. |
| **Crouch / Slide**  | `Input.Action.Crouch` | `C`             | `L-Ctrl`  | Slide if sprinting.        |
| **Prone**           | `Input.Action.Prone`  | `Z`             |           | Go prone instantly.        |
| **Walk (Slow)**     | `Input.Action.Walk`   | `Caps Lock`     |           | Toggle silent walking.     |
| **Lean Left/Right** | `Input.Action.Lean`   | `Q`, `E`        |           |                            |

#### **Combat**
| Action              | Gameplay Tag              | Primary            | Secondary | Context                             |
| :------------------ | :------------------------ | :----------------- | :-------- | :---------------------------------- |
| **Fire**            | `Input.Action.Fire`       | `L-Click`          |           |                                     |
| **Aim Down Sights** | `Input.Action.ADS`        | `R-Click`          |           |                                     |
| **Reload**          | `Input.Action.Reload`     | `R`                |           | Double-tap for Fast Reload.         |
| **Weapon Swap**     | `Input.Action.WeaponSwap` | `1`-`4` / `Scroll` |           | Primary, Secondary, Melee, Utility. |
| **Melee**           | `Input.Action.Melee`      | `V`                |           | Quick melee strike.                 |
| **Fire Mode**       | `Input.Action.FireMode`   | `B`                |           | Auto / Single / Burst.              |
| **Interaction**     | `Input.Action.Interact`   | `F`                |           | Use / Loot / Revive.                |

#### **Communication**
| Action           | Gameplay Tag                   | Primary        | Secondary | Context                |
| :--------------- | :----------------------------- | :------------- | :-------- | :--------------------- |
| **Ping**         | `Input.Action.Ping`            | `Middle Mouse` | `Z`       | Double tap for Danger. |
| **Push to Talk** | `Input.Action.PushToTalk`      | `Y`            |           | VoIP.                  |
| **Map**          | `Input.Action.Map`             | `M`            |           |                        |
| **Inventory**    | `Input.Action.InventoryAction` | `Tab`          | `I`       |                        |

---

## 🖥️ 2. Graphics Settings (Visuals)

*Widgets arranged from core display settings to fine-tuning.*

### **Display & Performance**
| Setting               | Gameplay Tag                    | Options                            | Description                                                   |
| :-------------------- | :------------------------------ | :--------------------------------- | :------------------------------------------------------------ |
| **Window Mode**       | `Settings.Video.WindowMode`     | Fullscreen / Borderless / Windowed | Controls how the game window occupies the screen.             |
| **Screen Resolution** | `Settings.Video.Resolution`     | 1920x1080, 2560x1440, etc.         | Native resolution of the display.                             |
| **Resolution Scale**  | `Settings.Video.ResScale`       | 0.0 - 100.0                        | Internal rendering resolution (supersampling or downscaling). |
| **V-Sync**            | `Settings.Video.VSync`          | OFF / ON                           | Synchronizes frame rate with monitor to prevent tearing.      |
| **Frame Rate Limit**  | `Settings.Video.FrameRateLimit` | Lobby (60), Game (Unlocked)        | Caps maximum FPS to save power or stabilize frame times.      |
| **NVIDIA Reflex**     | `Settings.Video.Reflex`         | OFF / ON / ON+BOOST                | Low latency mode for competitive input.                       |

### **Upscaling & Quality**
| Setting             | Gameplay Tag                      | Options                          | Description                                        |
| :------------------ | :-------------------------------- | :------------------------------- | :------------------------------------------------- |
| **Overall Quality** | `Settings.Video.QualityPreset`    | Low / Medium / High / Epic       | Master preset affecting all detail settings below. |
| **Upscaling**       | `Settings.Video.UpscalingMode`    | DLSS / FSR / XeSS / OFF          | AI reconstruction for higher FPS.                  |
| **Quality Mode**    | `Settings.Video.UpscalingQuality` | Performance / Balanced / Quality | "Performance" renders lower internal res.          |
| **Sharpening**      | `Settings.Video.Sharpening`       | Slider (0 - 100)                 | Contrast Adaptive Sharpening (CAS) intensity.      |

### **Detailed Environment**
| Setting                 | Gameplay Tag                        | Option (Low-Ultra)        | Impact | Description                                         |
| :---------------------- | :---------------------------------- | :------------------------ | :----- | :-------------------------------------------------- |
| **View Distance**       | `Settings.Video.ViewDistance`       | Low - Cinematic           | CPU    | Culling distance for objects/players. **Critical**. |
| **Shadow Quality**      | `Settings.Video.ShadowQuality`      | Low - Cinematic           | GPU    | "Low" removes dynamic shadows on small props.       |
| **Texture Quality**     | `Settings.Video.TextureQuality`     | Low - Cinematic           | VRAM   | Surface detail resolution.                          |
| **Anti-Aliasing**       | `Settings.Video.AntiAliasing`       | Low - Cinematic           | GPU    | Edge smoothing method (TAA, FXAA).                  |
| **Post-Processing**     | `Settings.Video.PostProcessing`     | Low - Cinematic           | GPU    | Bloom, Ambient Occlusion, Depth of Field quality.   |
| **Visual Effects**      | `Settings.Video.VFXQuality`         | Low - Cinematic           | CPU    | Particle density (sparks, smoke, debris).           |
| **Foliage Quality**     | `Settings.Video.FoliageQuality`     | Low - Cinematic           | CPU    | Density of grass/bushes. Does not affect hitboxes.  |
| **Global Illumination** | `Settings.Video.GlobalIllumination` | SSGI / Lumen              | GPU    | Indirect lighting quality.                          |
| **Reflections**         | `Settings.Video.Reflections`        | Screen Space / Ray Traced | GPU    | SSR is standard. RT is heavy.                       |

### **Visibility & Accessibility**
| Setting                  | Gameplay Tag                         | Option                                 | Description                                                  |
| :----------------------- | :----------------------------------- | :------------------------------------- | :----------------------------------------------------------- |
| **Field of View (FOV)**  | `Settings.Video.FOV`                 | 60 - 110                               | Horizontal FOV. (Mobile capped at 90).                       |
| **Motion Blur**          | `Settings.Video.MotionBlur`          | OFF / ON                               | *Always OFF* for competitive.                                |
| **Chromatic Aberration** | `Settings.Video.ChromaticAberration` | OFF / ON                               | Color fringing at screen edges. OFF recommended for clarity. |
| **Film Grain**           | `Settings.Video.FilmGrain`           | Slider (0.0 - 1.0)                     | Visual noise.                                                |
| **Colorblind Mode**      | `Settings.Accessibility.Colorblind`  | Protanopia / Deuteranopia / Tritanopia | Adjusts UI/Enemy colors for visibility.                      |
| **Brightness/HDR**       | `Settings.Video.Brightness`          | Slider                                 | Gamma or Nits calibration.                                   |

---

## 🔊 3. Audio Settings (Sound)

*Widgets arranged by mixer importance.*

### **Volume Mixer**
| Setting           | Gameplay Tag                   | Range    | Description                                         |
| :---------------- | :----------------------------- | :------- | :-------------------------------------------------- |
| **Master Volume** | `Settings.Audio.MasterVolume`  | 0 - 100% | Global output volume.                               |
| **SFX Volume**    | `Settings.Audio.SFXVolume`     | 0 - 100% | **Critical:** Footsteps, gunshots, reloads.         |
| **Voice Chat**    | `Settings.Audio.VoiceVolume`   | 0 - 100% | Volume of incoming teammate comms.                  |
| **UI Volume**     | `Settings.Audio.UIVolume`      | 0 - 100% | Clicks, inventory sounds, notifications.            |
| **Music (Raid)**  | `Settings.Audio.MusicRaid`     | 0 - 100% | In-game music. Recommended Low/OFF for competitive. |
| **Music (Menu)**  | `Settings.Audio.MusicMenu`     | 0 - 100% | Menu ambience.                                      |
| **Ambient**       | `Settings.Audio.AmbientVolume` | 0 - 100% | Wind, rain, room tone.                              |

### **Voice Chat (VoIP)**
| Setting           | Gameplay Tag                       | Option                         | Description         |
| :---------------- | :--------------------------------- | :----------------------------- | :------------------ |
| **Mode**          | `Settings.Audio.VoIP.Mode`         | Push-to-Talk / Open Mic / Mute | Activation method.  |
| **Input Device**  | `Settings.Audio.VoIP.InputDevice`  | System Default / Microphone X  | Hardware Selection. |
| **Output Device** | `Settings.Audio.VoIP.OutputDevice` | System Default / Headset X     | Hardware Selection. |

### **Advanced Audio**
| Setting                | Gameplay Tag                     | Option                           | Description                                                    |
| :--------------------- | :------------------------------- | :------------------------------- | :------------------------------------------------------------- |
| **Dynamic Range**      | `Settings.Audio.DynamicRange`    | Hi-Fi / Night Mode / TV          | "Night Mode" compresses loud sounds (explosions) to save ears. |
| **EQ Preset**          | `Settings.Audio.EQPreset`        | Flat / Bass Boost / Treble Boost | "Treble Boost" highlights footsteps.                           |
| **Binaural Audio**     | `Settings.Audio.Binaural`        | ON / OFF                         | Advanced HRTF (Spatial Audio) for directional accuracy.        |
| **Sound Lock**         | `Settings.Audio.SoundLock`       | ON / OFF                         | Hard limiter to prevent hearing damage from spikes.            |
| **Mute on Focus Loss** | `Settings.Audio.MuteOnFocusLoss` | ON / OFF                         | Mute game when Alt-Tabbed.                                     |

---

## 📡 4. Gameplay & Interface (HUD)

*Widgets arranged by HUD customization and account privacy.*

### **HUD & Interface**
| Setting             | Gameplay Tag                   | Option                   | Description                              |
| :------------------ | :----------------------------- | :----------------------- | :--------------------------------------- |
| **Crosshair Style** | `Settings.HUD.Crosshair.Style` | Cross / Dot / Circle     | Base shape of the reticle.               |
| **Crosshair Color** | `Settings.HUD.Crosshair.Color` | RGB Slider               | High contrast color recommended.         |
| **Damage Numbers**  | `Settings.HUD.DamageNumbers`   | OFF / Stacked / Floating | "Stacked" combines numbers (15..30..45). |
| **Kill Feed**       | `Settings.HUD.KillFeed`        | Full / Icons / OFF       | Notifications when players die.          |
| **Health Bar**      | `Settings.HUD.HealthBar`       | Always / Dynamic         | "Dynamic" hides when full.               |
| **Compass**         | `Settings.HUD.Compass`         | Top Bar / Minimap / OFF  | Directional aid.                         |

### **Interaction & Loot**
| Setting                 | Gameplay Tag                      | Option                  | Description                            |
| :---------------------- | :-------------------------------- | :---------------------- | :------------------------------------- |
| **Highlight Loot**      | `Settings.Gameplay.LootHighlight` | ON / OFF                | Colored outline around loose loot.     |
| **Quick Slots**         | `Settings.HUD.QuickSlots`         | Always Show / Auto-Hide | Visibility of hotbar (4-9).            |
| **Auto-Sort Stash**     | `Settings.Gameplay.AutoSort`      | ON / OFF                | Automatically arranges items (Tetris). |
| **Double Click Action** | `Settings.Gameplay.DoubleClick`   | Use / Inspect / Take    | Default action for inventory items.    |

### **Account & Privacy**
| Setting           | Gameplay Tag                    | Option               | Description                                      |
| :---------------- | :------------------------------ | :------------------- | :----------------------------------------------- |
| **Streamer Mode** | `Settings.Account.StreamerMode` | ON / OFF             | Hides names ("Player123") and server IP.         |
| **Data Center**   | `Settings.Account.DataCenter`   | Auto / Region Select | Preferred server location.                       |
| **Crossplay**     | `Settings.Account.Crossplay`    | ON / OFF             | Matchmaking with other platforms (Console only). |
| **Language**      | `Settings.Account.Language`     | Select Language      | Text and Audio localization.                     |

---

### 📝 Technical Implementation Notes (Engine Headers)
*Reference for Engineers integrating `UGameUserSettings`, `SettingsWidget.h`, and `UAdvancedGameSettings`.*

#### **Input Implementation**
- **Reference Frame:** Camera vs World vs Character relative input.
- **Facing Behavior:** Face Aim vs Face Movement.
- **Aim Constraint:** Clamped Radius vs Screen Edge (for Twin-stick feel).
- **Control Curves:** Customizable float curves for stick response.

#### **Graphics Implementation**
- Scalability Groups: `sg.ViewDistanceQuality`, `sg.ShadowQuality`, `sg.PostProcessQuality`, `sg.TextureQuality`, `sg.EffectsQuality`, `sg.FoliageQuality`, `sg.ShadingQuality`.
- Display: `r.VSync`, `r.DynamicRes.OperationMode`, `t.MaxFPS`.

#### **Audio Implementation**
- Sound Classes: `SC_Master`, `SC_Music`, `SC_SFX`, `SC_UI`, `SC_Voice`, `SC_Ambient`.
- Mix Modifiers: Dynamic Range Compression managed via Submix Effects.
