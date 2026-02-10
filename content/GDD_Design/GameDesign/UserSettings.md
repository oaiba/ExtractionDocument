---
title: "User Settings & Configuration - Enhanced Edition"
type: docs
version: 2.0
game_genre: Hero Extraction Shooter Multiplayer Crossplatform
---

**[↔ View Technical Spec: Settings System](../../GDD_Technical/Systems/SettingsSystem.md)**

## ⚙️ Design Philosophy

**"Power to the Player, Simplicity for the Casual."**

Settings should offer granular control for competitive players while providing simple, intelligent presets for casual users. All settings must be **saved to the cloud** and synced across devices with **conflict resolution** for crossplatform play.

### 🎯 Core Principles
- **Competitive Integrity:** Performance and clarity settings prioritized
- **Accessibility First:** Comprehensive options for all players
- **Hero Identity:** Settings that enhance character-specific gameplay
- **Extraction Focus:** UI/UX optimized for high-stakes decision-making
- **Cross-Platform Parity:** Fair experience across PC, Console, Mobile

### 📐 Enhanced UI Wireframe
```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  SETTINGS                                                  [PRESET: CUSTOM]  │
│                                                                      [ X ]   │
├──────────────────────────────────────────────────────────────────────────────┤
│  [🎮 CONTROLS]  [🖥️ GRAPHICS]  [🔊 AUDIO]  [📡 GAMEPLAY]  [🦸 HERO]  [💾 ACC] │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─ MOUSE SENSITIVITY ──────────────────────────────────────────────────┐  │
│   │  GENERAL ───────────────────────────────── [ 1.0 ] [|||||·          ] │  │
│   │  ADS MULTIPLIER ───────────────────────── [ 0.8 ] [||||·           ] │  │
│   │  SCOPE 1-2x ───────────────────────────── [ 0.8 ] [||||·           ] │  │
│   │  SCOPE 3-4x ───────────────────────────── [ 0.6 ] [|||·            ] │  │
│   │  SCOPE 6x+ ────────────────────────────── [ 0.4 ] [||·             ] │  │
│   │  VEHICLE SENSITIVITY ──────────────────── [ 0.9 ] [||||·           ] │  │
│   └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   INVERT LOOK (Y-AXIS) ───────────────────────────────── [ OFF ] [ ○     ]  │
│   INVERT LOOK (X-AXIS) ───────────────────────────────── [ OFF ] [ ○     ]  │
│   VIBRATION ──────────────────────────────────────────── [ ON  ] [     ● ]  │
│   VIBRATION INTENSITY ──────────────────────────────────── [ 75% ] [||||·  ] │
│                                                                              │
│   [ 🎯 ADVANCED AIM SETTINGS ]          [ ⌨️ EDIT KEYBINDINGS ]             │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│  [ ↺ RESET TO DEFAULT ]  [ 📋 IMPORT ]  [ CANCEL ]  [ APPLY ]  [ SAVE ]     │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎮 1. CONTROL SETTINGS (Input)

*Settings organized by competitive importance and usage frequency.*

### **1.1 Primary Input & Detection**
| Setting                     | Gameplay Tag                        | Type                              | Default   | Description                                                         |
| :-------------------------- | :---------------------------------- | :-------------------------------- | :-------- | :------------------------------------------------------------------ |
| **Input Method**            | `Settings.Input.Method`             | Auto / KBM / Gamepad / Touch      | Automatic | Preferred input device or auto-detection mode.                      |
| **Input Device Switching**  | `Settings.Input.DeviceSwitching`    | Seamless / Manual / Disabled      | Seamless  | Switch between KBM and controller mid-game without menu navigation. |
| **Last Input Memory**       | `Settings.Input.LastMemory`         | Toggle                            | ON        | Remember last used input per-session.                               |

### **1.2 Mouse & Keyboard Sensitivity**
| Setting                     | Gameplay Tag                           | Type                   | Default | Description                                         |
| :-------------------------- | :------------------------------------- | :--------------------- | :------ | :-------------------------------------------------- |
| **General Sensitivity**     | `Settings.Input.Sensitivity.Global`    | Slider (0.1 - 10.0)    | 1.0     | Global mouse sensitivity.                           |
| **ADS Sensitivity**         | `Settings.Input.Sensitivity.ADS`       | Slider (0.1 - 2.0)     | 0.8     | Sensitivity multiplier when Aiming Down Sights.     |
| ~~**Scope 1-2x**~~              | `Settings.Input.Sensitivity.Scope1x`   | Slider (0.1 - 2.0)     | 0.8     | Red dot, holo, low magnification.                   |
| ~~**Scope 3-4x**~~              | `Settings.Input.Sensitivity.Scope3x`   | Slider (0.1 - 2.0)     | 0.6     | Medium zoom scopes.                                 |
| ~~**Scope 6x+**~~               | `Settings.Input.Sensitivity.Scope6x`   | Slider (0.1 - 2.0)     | 0.4     | High magnification scopes (Sniper).                 |
| **Vehicle Sensitivity**     | `Settings.Input.Sensitivity.Vehicle`   | Slider (0.1 - 2.0)     | 0.9     | Sensitivity when driving/piloting.                  |
| **Spectator Sensitivity**   | `Settings.Input.Sensitivity.Spectator` | Slider (0.1 - 2.0)     | 1.2     | Free camera when spectating teammates.              |
| **Mouse Acceleration**      | `Settings.Input.MouseAcceleration`     | Toggle                 | OFF     | Dynamic sensitivity based on mouse velocity.        |
| **Raw Input**               | `Settings.Input.RawInput`              | Toggle                 | ON      | Bypass OS mouse settings (recommended for comp).    |
| **Pointer Precision**       | `Settings.Input.PointerPrecision`      | Toggle                 | OFF     | Windows "Enhance pointer precision" override.       |
| **DPI Scaling**             | `Settings.Input.DPIScaling`            | Toggle                 | OFF     | Compensate for Windows DPI settings.                |

### **1.3 Controller Sensitivity**
| Setting                     | Gameplay Tag                              | Type                | Default | Description                                        |
| :-------------------------- | :---------------------------------------- | :------------------ | :------ | :------------------------------------------------- |
| **Horizontal Sensitivity**  | `Settings.Input.Controller.SensitivityH`  | Slider (1 - 20)     | 10      | Right stick horizontal sensitivity.                |
| **Vertical Sensitivity**    | `Settings.Input.Controller.SensitivityV`  | Slider (1 - 20)     | 8       | Right stick vertical sensitivity.                  |
| **ADS Sensitivity**         | `Settings.Input.Controller.ADSSens`       | Slider (0.5 - 2.0)  | 0.8     | Controller sensitivity modifier when ADS.          |
| **Vehicle Sensitivity**     | `Settings.Input.Controller.VehicleSens`   | Slider (0.5 - 2.0)  | 1.0     | Controller sensitivity for vehicles.               |
| **Look Acceleration**       | `Settings.Input.Controller.Acceleration`  | Slider (0 - 10)     | 3       | How quickly max turn speed is reached.             |
| **Look Deadzone**           | `Settings.Input.Controller.LookDeadzone`  | Slider (0.00 - 0.50)| 0.10    | Right stick minimum input threshold.               |
| **Move Deadzone**           | `Settings.Input.Controller.MoveDeadzone`  | Slider (0.00 - 0.50)| 0.15    | Left stick minimum input threshold.                |
| **Trigger Deadzone**        | `Settings.Input.Controller.TriggerDead`   | Slider (0.00 - 0.50)| 0.05    | L2/R2 trigger activation threshold.                |
| **Response Curve**          | `Settings.Input.Controller.ResponseCurve` | Linear / Standard / Dynamic / Expo | Standard | Stick input curve.                      |

### **1.4 Advanced Input Settings**
| Setting                     | Gameplay Tag                           | Option                            | Default  | Description                                                |
| :-------------------------- | :------------------------------------- | :-------------------------------- | :------- | :--------------------------------------------------------- |
| **Invert Look (Y-Axis)**    | `Settings.Input.InvertLookY`           | Toggle                            | OFF      | Invert vertical camera movement.                           |
| **Invert Look (X-Axis)**    | `Settings.Input.InvertLookX`           | Toggle                            | OFF      | Invert horizontal camera movement.                         |
| **Look Response Curve**     | `Settings.Input.ResponseCurve`         | Standard / Linear / Dynamic / Expo| Standard | Input curve mapping for precision vs speed.                |
| **ADS Transition Speed**    | `Settings.Input.ADSTransitionSpeed`    | Slider (0.1 - 2.0)                | 1.0      | How quickly camera zooms in/out when ADSing.               |
| **FOV Affected Sensitivity**| `Settings.Input.FOVScaling`            | Toggle                            | OFF      | Scale sensitivity with FOV changes (monitor distance).     |
| **Per-Optic Sensitivity**   | `Settings.Input.PerOpticSens`          | Toggle                            | OFF      | Allow unique sensitivity for each optic attachment.        |
| **Uniform Soldier Aiming**  | `Settings.Input.UniformSoldierAim`     | Toggle                            | OFF      | Maintain 1:1 relationship between hip and ADS sensitivity. |
| **Separate Vehicle Controls**| `Settings.Input.SeparateVehicle`      | Toggle                            | OFF      | Different bindings for vehicle vs on-foot.                 |

### **1.5 Movement & Combat Behaviors**
| Setting                     | Gameplay Tag                              | Option                     | Default     | Description                                                          |
| :-------------------------- | :---------------------------------------- | :------------------------- | :---------- | :------------------------------------------------------------------- |
| **Crouch Mode**             | `Settings.Control.CrouchBehavior`         | Hold / Toggle              | Toggle      | "Hold" requires keeping the key pressed.                             |
| **Prone Mode**              | `Settings.Control.ProneBehavior`          | Hold / Toggle              | Toggle      | Separate from crouch, allows full prone.                             |
| **Sprint Mode**             | `Settings.Control.SprintBehavior`         | Hold / Toggle / Auto       | Hold        | "Auto" sprints when moving forward at max speed.                     |
| ~~**Tactical Sprint**~~         | `Settings.Control.TacSprintBehavior`      | Single Tap / Double Tap    | Double Tap  | Engage super-sprint (weapon up, slower ready time).                  |
| ~~**Auto Tactical Sprint**~~    | `Settings.Control.AutoTacSprint`          | Toggle                     | OFF         | Automatically engage tac sprint after X seconds of normal sprint.    |
| **Walk Mode**               | `Settings.Control.WalkBehavior`           | Hold / Toggle              | Hold        | Silent movement modifier (reduced audio).                            |
| **Slide Mode**              | `Settings.Control.SlideBehavior`          | Auto / Hold Crouch         | Auto        | "Auto" slides when crouching while sprinting.                        |
| **Mantle Behavior**         | `Settings.Control.MantleBehavior`         | Automatic / Manual / Hybrid| Automatic   | "Hybrid" requires jump near object; "Auto" mantles on contact.       |
| **Vault Speed**             | `Settings.Control.VaultSpeed`             | Realistic / Fast           | Fast        | "Realistic" slower but retains weapon; "Fast" holsters weapon.       |
| **Auto-Mantle Height**      | `Settings.Control.AutoMantleHeight`       | Low / Medium / High        | Medium      | Maximum height for automatic climbing.                               |

### **1.6 Aiming & Shooting Behaviors**
| Setting                     | Gameplay Tag                              | Option                  | Default  | Description                                                     |
| :-------------------------- | :---------------------------------------- | :---------------------- | :------- | :-------------------------------------------------------------- |
| **Aim Mode**                | `Settings.Control.AimBehavior`            | Hold / Toggle           | Hold     | Aiming Down Sights (ADS) behavior.                              |
| **Aim Transition**          | `Settings.Control.ADSTransition`          | Smooth / Instant        | Smooth   | "Smooth" blends animation; "Instant" snaps view immediately.    |
| **Toggle ADS Release**      | `Settings.Control.ToggleADSRelease`       | Fire / Click            | Click    | How to exit toggle ADS: firing or clicking aim again.           |
| **ADS on Reload**           | `Settings.Control.ADSOnReload`            | Exit / Maintain / Hybrid| Maintain | Camera behavior when reloading while ADS.                       |
| ~~**Lean Mode**~~               | `Settings.Control.LeanBehavior`           | Hold / Toggle / Context | Hold     | Peek around corners. "Context" auto-leans near cover.           |
| ~~**Auto Lean**~~               | `Settings.Control.AutoLean`               | Toggle                  | OFF      | Automatically lean when ADSing near cover edge.                 |
| **Quick Throw Grenade**     | `Settings.Combat.QuickThrow`              | Toggle                  | ON       | Grenade throws immediately on key press vs cook.                |
| **Grenade Arc Display**     | `Settings.Combat.GrenadeArc`              | Full / Partial / OFF    | Partial  | Trajectory preview. "OFF" for hardcore/realistic.               |
| **Fire Mode Change**        | `Settings.Combat.FireModeChange`          | Hold / Tap              | Tap      | Switch between auto/semi/burst fire modes.                      |
| **Bolt Action Mode**        | `Settings.Combat.BoltActionMode`          | Auto / Manual           | Auto     | "Auto" cycles bolt on trigger release; "Manual" requires input. |
| ~~**One-Tap ADS**~~             | `Settings.Combat.OneTapADS`               | Toggle                  | OFF      | Single click for instant ADS + fire (QuickScope assist).        |
| ~~**Hold Breath Duration**~~    | `Settings.Combat.HoldBreathDuration`      | Realistic / Extended    | Realistic| Stamina-based (5s) vs arcade (10s) steady scope.                |
| **Weapon Swap Speed**       | `Settings.Combat.WeaponSwapSpeed`         | Realistic / Fast        | Realistic| Animation speed for switching weapons.                          |

### **1.7 Interaction & Looting**
| Setting                     | Gameplay Tag                           | Option                    | Default  | Description                                                      |
| :-------------------------- | :------------------------------------- | :------------------------ | :------- | :--------------------------------------------------------------- |
| **Interact Mode**           | `Settings.Control.InteractBehavior`    | Hold / Tap                | Tap      | "Hold" shows context menu; "Tap" for instant pickup.             |
| **Interact Hold Duration**  | `Settings.Control.InteractHoldTime`    | Slider (0.1s - 2.0s)      | 0.5s     | Time required to hold for interactions.                          |
| **Context Menu Priority**   | `Settings.Loot.ContextPriority`        | Smart / Always Show       | Smart    | "Smart" auto-picks single item; "Always" shows menu.             |
| **Loot on Approach**        | `Settings.Loot.AutoLoot`               | Ammo Only / All / OFF     | Ammo Only| Automatically pick up items when walking over them.              |
| **Auto-Reload Empty**       | `Settings.Combat.AutoReload`           | Toggle                    | ON       | Automatically reload when magazine empty.                        |
| **Reload Canceling**        | `Settings.Combat.ReloadCancel`         | Anytime / After New Mag   | Anytime  | When weapon is ready after starting reload.                      |
| **Use/Open Door**           | `Settings.Control.DoorBehavior`        | Same Key / Separate       | Same Key | Use same key for doors and interactions or separate.             |
| **Door Opening Speed**      | `Settings.Control.DoorSpeed`           | Slow / Normal / Fast      | Normal   | How quickly character opens doors (affects audio cues).          |
| **Zipline Auto-Attach**     | `Settings.Control.ZiplineAttach`       | Auto / Manual             | Auto     | Grab ziplines automatically when near or require input.          |
| **Contextual Reload**       | `Settings.Combat.ContextualReload`     | Toggle                    | ON       | Pressing reload near ammo box auto-refills all weapons.          |

### **1.8 Hero Ability Controls**
| Setting                      | Gameplay Tag                          | Option                  | Default | Description                                                  |
| :--------------------------- | :------------------------------------ | :---------------------- | :------ | :----------------------------------------------------------- |
| **Ability Casting**          | `Settings.Hero.AbilityCasting`        | Instant / Confirm       | Instant | "Confirm" requires second click to activate (prevents accidents).|
| **Ultimate Confirmation**    | `Settings.Hero.UltimateConfirm`       | Toggle                  | ON      | Always require double-tap for ultimate ability.              |
| **Ability Queueing**         | `Settings.Hero.AbilityQueue`          | Toggle                  | ON      | Queue next ability during current animation.                 |
| **Self-Cast Modifier**       | `Settings.Hero.SelfCastModifier`      | Double Tap / Hold Alt   | Hold Alt| How to cast support abilities on yourself vs teammates.      |
| **Quick Cast (MOBA Style)**  | `Settings.Hero.QuickCast`             | ON / OFF                | OFF     | Abilities fire at cursor on keypress (no click required).    |
| **Ability Smart Target**     | `Settings.Hero.SmartTargeting`        | Toggle                  | ON      | Prioritize allies for healing, enemies for damage.           |
| **Ability Range Preview**    | `Settings.Hero.RangePreview`          | Always / Hold Key / OFF | Hold Key| Show AoE radius and range indicators.                        |
| **Ability Cooldown Voice**   | `Settings.Hero.CooldownVoice`         | Toggle                  | ON      | Hero announces when abilities ready.                         |

### **1.9 Controller & Platform-Specific**
| Setting                     | Gameplay Tag                              | Option                          | Default  | Description                                               |
| :-------------------------- | :---------------------------------------- | :------------------------------ | :------- | :-------------------------------------------------------- |
| **Vibration**               | `Settings.Input.Vibration`                | Toggle                          | ON       | Haptic feedback for shooting/damage/actions.              |
| **Vibration Intensity**     | `Settings.Input.VibrationIntensity`       | Slider (0 - 200%)               | 100%     | Separate sliders for Left/Right motor.                    |
| **Adaptive Triggers (PS5)**| `Settings.Input.AdaptiveTriggers`         | OFF / Weapon Feel / Immersive   | Immersive| R2 trigger resistance based on weapon.                    |
| **Trigger Effect Strength** | `Settings.Input.TriggerStrength`          | Slider (0 - 150%)               | 100%     | Adjust adaptive trigger resistance.                       |
| **Aim Assist**              | `Settings.Input.AimAssist`                | OFF / Standard / Precision / Focus | Standard | Controller magnetism. PC crossplay may force OFF.       |
| **Aim Assist Strength**     | `Settings.Input.AimAssistStrength`        | Slider (0 - 100%)               | 100%     | Fine-tune aim assist pull.                                |
| **Rotation Assist**         | `Settings.Input.RotationAssist`           | Toggle                          | ON       | Helps track moving targets (strafing enemies).            |
| **Slowdown Assist**         | `Settings.Input.SlowdownAssist`           | Toggle                          | ON       | Reduces sensitivity when aiming near enemy.               |
| **Aim Assist Window**       | `Settings.Input.AimAssistWindow`          | Narrow / Standard / Wide        | Standard | Size of magnetism bubble around targets.                  |
| **Aim Assist Through Smoke**| `Settings.Input.AimAssistSmoke`          | ON / OFF                        | OFF      | Whether aim assist works through smoke/gas.               |

### **1.10 Gyro Aiming (Mobile/Switch/PS5)**
| Setting                     | Gameplay Tag                              | Option                    | Default | Description                                            |
| :-------------------------- | :---------------------------------------- | :------------------------ | :------ | :----------------------------------------------------- |
| **Gyro Aiming**             | `Settings.Input.Gyro.Mode`                | OFF / ADS Only / Always   | ADS Only| Use device tilt for camera control.                    |
| **Gyro Sensitivity X**      | `Settings.Input.Gyro.SensitivityX`        | Slider (1 - 500%)         | 100%    | Horizontal gyro sensitivity.                           |
| **Gyro Sensitivity Y**      | `Settings.Input.Gyro.SensitivityY`        | Slider (1 - 500%)         | 100%    | Vertical gyro sensitivity.                             |
| **Gyro Invert X**           | `Settings.Input.Gyro.InvertX`             | Toggle                    | OFF     | Invert horizontal gyro input.                          |
| **Gyro Invert Y**           | `Settings.Input.Gyro.InvertY`             | Toggle                    | OFF     | Invert vertical gyro input.                            |
| **Gyro Smoothing**          | `Settings.Input.Gyro.Smoothing`           | Slider (0 - 10)           | 3       | Reduce jitter in gyro input.                           |
| **Gyro Reset Binding**      | `Settings.Input.Gyro.ResetBind`           | Touch Pad / Select        | Touch Pad| Button to recenter gyro orientation.                  |
| **Gyro Always On**          | `Settings.Input.Gyro.AlwaysOn`            | Toggle                    | OFF     | Gyro active even when not touching screen (mobile).    |

### **1.11 Mobile Touch Controls**
| Setting                     | Gameplay Tag                              | Option                       | Default     | Description                                          |
| :-------------------------- | :---------------------------------------- | :--------------------------- | :---------- | :--------------------------------------------------- |
| **Touch Mode**              | `Settings.Input.Touch.Mode`               | Touchpad / Virtual Joystick  | Joystick    | Look via swiping anywhere or virtual stick.          |
| **HUD Layout Preset**       | `Settings.Input.Touch.Layout`             | Default / Claw / Thumbs / Custom | Default | Pre-configured button layouts for play styles.       |
| **Custom Layout Editor**    | `Settings.Input.Touch.CustomEditor`       | Button                       | -           | Open visual editor to position all controls.         |
| **Button Opacity**          | `Settings.Input.Touch.Opacity`            | Slider (0 - 100%)            | 60%         | Transparency of on-screen controls.                  |
| **Button Scale**            | `Settings.Input.Touch.Scale`              | Slider (50 - 200%)           | 100%        | Size of virtual buttons and joysticks.               |
| **Fire Button Mode**        | `Settings.Input.Touch.FireMode`           | Tap / Hold / Auto            | Tap         | "Auto" fires when crosshair on enemy.                |
| **Auto-Run**                | `Settings.Input.Touch.AutoRun`            | Toggle                       | ON          | Double-tap movement joystick to auto-run.            |
| **Auto-Loot**               | `Settings.Input.Touch.AutoLoot`           | Toggle                       | ON          | Automatically pick up nearby items.                  |
| **Auto-Open Doors**         | `Settings.Input.Touch.AutoDoors`          | Toggle                       | ON          | Walk through doors without interaction.              |
| **Peek & Fire**             | `Settings.Input.Touch.PeekFire`           | Toggle                       | ON          | Aim automatically leans around cover.                |
| **Quick Scope**             | `Settings.Input.Touch.QuickScope`         | Toggle                       | OFF         | Auto-ADS when tapping fire with snipers.             |
| **3D Touch Support**        | `Settings.Input.Touch.3DTouch`            | Toggle                       | ON          | Pressure-sensitive actions (iOS devices).            |
| **Haptic Feedback**         | `Settings.Input.Touch.Haptic`             | Toggle                       | ON          | Vibration when firing/taking damage.                 |

---

## 🖥️ 2. GRAPHICS & VISUAL SETTINGS (Video)

*Settings organized by performance impact and competitive advantage.*

### **2.1 Display & Window**
| Setting                     | Gameplay Tag                         | Options                                 | Default    | Description                                                        |
| :-------------------------- | :----------------------------------- | :-------------------------------------- | :--------- | :----------------------------------------------------------------- |
| **Display Mode**            | `Settings.Video.DisplayMode`         | Fullscreen / Borderless / Windowed      | Fullscreen | "Borderless" for alt-tab; "Fullscreen" for performance.            |
| **Resolution**              | `Settings.Video.Resolution`          | Native / 1920x1080 / 2560x1440 / etc.   | Native     | Render resolution.                                                 |
| **Render Scale**            | `Settings.Video.RenderScale`         | Slider (50 - 200%)                      | 100%       | Internal resolution multiplier (supersampling/upscaling).          |
| **Aspect Ratio**            | `Settings.Video.AspectRatio`         | 16:9 / 16:10 / 21:9 / Auto              | Auto       | Forced aspect ratio (adds letterboxing if mismatch).               |
| **VSync**                   | `Settings.Video.VSync`               | OFF / ON / Adaptive / Fast Sync         | OFF        | Sync framerate to monitor refresh. OFF for competitive.            |
| **Frame Rate Limit**        | `Settings.Video.FPSLimit`            | 30 / 60 / 120 / 144 / 240 / Unlimited   | Unlimited  | Cap maximum FPS to reduce heat/power.                              |
| **NVIDIA Reflex**           | `Settings.Video.Reflex`              | OFF / ON / ON+Boost                     | ON+Boost   | (NVIDIA) Reduce system latency. Always ON for competitive.         |
| **AMD Anti-Lag**            | `Settings.Video.AntiLag`             | OFF / ON                                | ON         | (AMD) Reduce input lag.                                            |
| **Intel XeSS Frame Gen**    | `Settings.Video.XeSSFrameGen`        | OFF / ON                                | OFF        | (Intel Arc) Frame generation.                                      |

### **2.2 Graphics Quality Presets**
| Preset              | Target Hardware           | Description                                                                    |
| :------------------ | :------------------------ | :----------------------------------------------------------------------------- |
| **Low**             | GTX 1050 / Mobile         | Maximum performance. Minimal effects, low textures, reduced view distance.     |
| **Medium**          | GTX 1660 / PS4 / Xbox One | Balanced quality. Good for 1080p 60 FPS.                                       |
| **High**            | RTX 2060 / PS5 / Xbox X   | Enhanced visuals. For high-end 1080p or mid-tier 1440p.                        |
| **Ultra**           | RTX 3080+ / High-end PC   | Maximum fidelity. 4K HDR, ray tracing, for enthusiast rigs.                    |
| **Performance**     | Competitive Priority      | Disables motion blur, reduces effects, prioritizes clarity and frame rate.     |
| **Battery Saver**   | Mobile / Laptop           | Reduces GPU load, caps FPS, extends battery life.                              |
| **Custom**          | User-defined              | Manual control of all settings.                                                |

### **2.3 Advanced Graphics Settings**
| Setting                     | Gameplay Tag                                | Options                    | Impact    | Description                                                       |
| :-------------------------- | :------------------------------------------ | :------------------------- | :-------- | :---------------------------------------------------------------- |
| **Texture Quality**         | `Settings.Video.TextureQuality`             | Low / Medium / High / Ultra| VRAM      | Resolution of surface textures.                                   |
| **Texture Streaming**       | `Settings.Video.TextureStreaming`           | OFF / ON                   | Low       | Load textures dynamically (reduces VRAM, may cause pop-in).       |
| **Texture Streaming Budget**| `Settings.Video.TextureStreamBudget`        | Slider (1-8 GB)            | VRAM      | VRAM allocated for streaming.                                     |
| **Mesh Quality**            | `Settings.Video.MeshQuality`                | Low / Medium / High        | CPU/VRAM  | Polygon density of models.                                        |
| **LOD Distance**            | `Settings.Video.LODDistance`                | Near / Medium / Far        | CPU       | When models switch to lower detail versions.                      |
| **View Distance**           | `Settings.Video.ViewDistance`               | Low / Medium / High / Ultra| CPU/GPU   | **Critical:** How far players/objects render. Ultra for snipers.  |
| **Foliage Quality**         | `Settings.Video.FoliageQuality`             | Low / Medium / High        | GPU       | Grass/tree density. "Low" improves visibility in forests.         |
| **Foliage Draw Distance**   | `Settings.Video.FoliageDistance`            | Near / Medium / Far        | GPU       | How far vegetation renders.                                       |
| **Shadow Quality**          | `Settings.Video.ShadowQuality`              | OFF / Low / Medium / High  | GPU       | Shadow resolution and distance. OFF for competitive clarity.      |
| **Shadow Distance**         | `Settings.Video.ShadowDistance`             | Near / Medium / Far        | GPU       | How far shadows render.                                           |
| **Dynamic Shadows**         | `Settings.Video.DynamicShadows`             | OFF / ON                   | GPU       | Real-time shadows from moving objects.                            |
| **Contact Shadows**         | `Settings.Video.ContactShadows`             | OFF / ON                   | GPU       | Detailed shadows near object contact points.                      |
| **Effects Quality**         | `Settings.Video.EffectsQuality`             | Low / Medium / High        | GPU       | Muzzle flashes, explosions, particles, ability VFX.               |
| **Post-Processing**         | `Settings.Video.PostProcessQuality`         | Low / Medium / High / OFF  | GPU       | Bloom, lens flares, color grading. "OFF" for competitive.         |
| **Anti-Aliasing Method**    | `Settings.Video.AntiAliasing`               | OFF / FXAA / TAA / MSAA 2x-8x / DLAA | GPU | Edge smoothing. TAA recommended. MSAA expensive.         |
| **Anti-Aliasing Quality**   | `Settings.Video.AAQuality`                  | Low / Medium / High        | GPU       | Quality of chosen AA method.                                      |
| **Upscaling Technology**    | `Settings.Video.Upscaling`                  | Native / DLSS / FSR / XeSS / TSR | GPU/AI | AI upscaling. DLSS (NVIDIA), FSR (AMD/Universal), XeSS (Intel).|
| **Upscaling Mode**          | `Settings.Video.UpscalingMode`              | Quality / Balanced / Performance / Ultra Performance | GPU | Quality vs FPS tradeoff.                        |
| **Sharpening**              | `Settings.Video.Sharpening`                 | Slider (0 - 100%)          | GPU       | Image sharpening (useful with TAA/upscaling).                     |

### **2.4 Ray Tracing & Advanced Lighting**
| Setting                     | Gameplay Tag                                | Options                    | Impact    | Description                                                       |
| :-------------------------- | :------------------------------------------ | :------------------------- | :-------- | :---------------------------------------------------------------- |
| **Ray Tracing**             | `Settings.Video.RayTracing`                 | OFF / Hybrid / Full        | RTX GPU   | Realistic lighting. Massive performance cost.                     |
| **Ray Traced Shadows**      | `Settings.Video.RTShadows`                  | OFF / ON                   | RTX GPU   | Accurate real-time shadows.                                       |
| **Ray Traced Reflections**  | `Settings.Video.RTReflections`              | OFF / ON                   | RTX GPU   | Realistic reflections on surfaces.                                |
| **Ray Traced Global Illumination** | `Settings.Video.RTGI`                | OFF / ON                   | RTX GPU   | Indirect lighting bounces.                                        |
| **Ray Tracing Quality**     | `Settings.Video.RTQuality`                  | Low / Medium / High / Ultra| RTX GPU   | Sample count and denoising quality.                               |
| **Ambient Occlusion**       | `Settings.Video.AmbientOcclusion`           | OFF / SSAO / HBAO+ / RTAO  | GPU       | Contact shadows in crevices. OFF for competitive.                 |
| **Screen Space Reflections**| `Settings.Video.SSR`                        | OFF / Low / High           | GPU       | Real-time reflections on surfaces (non-RT).                       |
| **Global Illumination**     | `Settings.Video.GlobalIllumination`         | OFF / Low / High           | GPU       | Indirect lighting (non-RT).                                       |
| **Volumetric Lighting**     | `Settings.Video.Volumetric`                 | OFF / Low / Medium / High  | GPU       | God rays, fog, smoke. Beautiful but expensive.                    |
| **Volumetric Fog Quality**  | `Settings.Video.VolumetricFogQuality`       | Low / Medium / High        | GPU       | Density and detail of atmospheric fog.                            |

### **2.5 Post-Processing Effects**
| Setting                     | Gameplay Tag                            | Options                     | Impact | Description                                                    |
| :-------------------------- | :-------------------------------------- | :-------------------------- | :----- | :------------------------------------------------------------- |
| **Depth of Field**          | `Settings.Video.DepthOfField`           | OFF / Low / High            | GPU    | Camera focus blur. **Always OFF** for competitive clarity.     |
| **Motion Blur**             | `Settings.Video.MotionBlur`             | OFF / World Only / Full     | GPU    | Blur during camera movement. **Always OFF** for competitive.   |
| **Motion Blur Intensity**   | `Settings.Video.MotionBlurIntensity`    | Slider (0 - 100%)           | GPU    | Strength of motion blur effect.                                |
| **Chromatic Aberration**    | `Settings.Video.ChromaticAberration`    | OFF / ON                    | Low    | Color fringing at screen edges. OFF recommended.               |
| **Film Grain**              | `Settings.Video.FilmGrain`              | Slider (0.0 - 1.0)          | Low    | Visual noise overlay. 0.0 recommended.                         |
| **Vignette**                | `Settings.Video.Vignette`               | OFF / ON                    | Low    | Screen edge darkening. OFF for maximum visibility.             |
| **Lens Flare**              | `Settings.Video.LensFlare`              | OFF / ON                    | Low    | Light reflections. Can obscure vision, OFF recommended.        |
| **Lens Distortion**         | `Settings.Video.LensDistortion`         | OFF / ON                    | Low    | Fisheye effect. OFF for competitive.                           |
| **Bloom**                   | `Settings.Video.Bloom`                  | OFF / Low / Medium / High   | GPU    | Glow around bright lights. Low recommended.                    |
| **Light Shafts**            | `Settings.Video.LightShafts`            | OFF / ON                    | GPU    | Sun/light beams through objects.                               |
| **Screen Space Reflections Quality** | `Settings.Video.SSRQuality`    | Low / Medium / High         | GPU    | Quality of non-RT reflections.                                 |

### **2.6 Field of View & Camera**
| Setting                     | Gameplay Tag                            | Options                     | Default | Description                                                    |
| :-------------------------- | :-------------------------------------- | :-------------------------- | :------ | :------------------------------------------------------------- |
| **Field of View (FOV)**     | `Settings.Video.FOV`                    | Slider (60 - 120)           | 90      | Horizontal FOV. Higher = more peripheral vision.               |
| **FOV Scaling Method**      | `Settings.Video.FOVScaling`             | Horizontal / Vertical / Aspect Ratio Dependent | Horizontal | How FOV changes with aspect ratio.|
| ~~**Weapon FOV**~~              | `Settings.Video.WeaponFOV`              | Slider (50 - 100)           | 70      | Viewmodel field of view. Lower = less weapon obstruction.      |
| ~~**Independent Weapon FOV**~~  | `Settings.Video.IndependentWeaponFOV`   | OFF / ON                    | ON      | Weapon FOV separate from player FOV.                           |
| **Vehicle FOV**             | `Settings.Video.VehicleFOV`             | Slider (60 - 120)           | 100     | Separate FOV when in vehicles.                                 |
| ~~**ADS FOV Override**~~        | `Settings.Video.ADSFOVOverride`         | OFF / ON                    | OFF     | Maintain FOV when ADS (affects zoom feel).                     |
| **Camera Shake**            | `Settings.Video.CameraShake`            | Slider (0 - 100%)           | 50%     | Intensity of weapon recoil shake.                              |
| ~~**Head Bob**~~                | `Settings.Video.HeadBob`                | Slider (0 - 100%)           | 50%     | Walking/running camera sway.                                   |
| **Sprint FOV Effect**       | `Settings.Video.SprintFOVEffect`        | OFF / Subtle / Standard     | Standard| FOV widens slightly when sprinting.                            |

### **2.7 Display & Color**
| Setting                     | Gameplay Tag                            | Options                                       | Description                                                   |
| :-------------------------- | :-------------------------------------- | :-------------------------------------------- | :------------------------------------------------------------ |
| **Brightness**              | `Settings.Video.Brightness`             | Slider (-100% to +100%)                       | Global brightness adjustment.                                 |
| **Contrast**                | `Settings.Video.Contrast`               | Slider (-100% to +100%)                       | Contrast adjustment.                                          |
| **Gamma**                   | `Settings.Video.Gamma`                  | Slider (1.0 - 3.0)                            | Midtone brightness.                                           |
| **HDR**                     | `Settings.Video.HDR`                    | OFF / ON                                      | High Dynamic Range (requires HDR monitor).                    |
| **HDR Brightness**          | `Settings.Video.HDR.Brightness`         | Slider (100 - 10000 Nits)                     | Peak brightness calibration.                                  |
| **HDR Paper White**         | `Settings.Video.HDR.PaperWhite`         | Slider (80 - 400 Nits)                        | White level calibration.                                      |
| **Color Blind Mode**        | `Settings.Video.ColorBlind.Mode`        | OFF / Protanopia / Deuteranopia / Tritanopia / Achromatopsia | Color vision deficiency support.        |
| **Color Blind Strength**    | `Settings.Video.ColorBlind.Strength`    | Slider (0 - 100%)                             | Intensity of color correction.                                |
| **Color Blind UI Only**     | `Settings.Video.ColorBlind.UIOnly`      | OFF / ON                                      | Apply color correction to UI only, not world.                 |
| **Interface Contrast**      | `Settings.Video.InterfaceContrast`      | Standard / High / Maximum                     | UI element visibility against backgrounds.                    |
| **Enemy Highlight**         | `Settings.Video.EnemyHighlight`         | OFF / Subtle / Standard / Strong              | Outline/glow around hostile players.                          |
| **Teammate Highlight**      | `Settings.Video.TeammateHighlight`      | OFF / Subtle / Standard / Strong              | Outline/glow around friendly players.                         |
| **Highlight Color (Enemy)** | `Settings.Video.HighlightColorEnemy`    | Red / Orange / Yellow / Purple / Custom       | Choose highlight color for enemies.                           |
| **Highlight Color (Ally)**  | `Settings.Video.HighlightColorAlly`     | Blue / Green / Cyan / Custom                  | Choose highlight color for teammates.                         |
| **Saturation**              | `Settings.Video.Saturation`             | Slider (0 - 200%)                             | Color intensity. 100% = normal.                               |
| **Color Temperature**       | `Settings.Video.ColorTemperature`       | Cool / Neutral / Warm                         | Blue tint vs orange tint.                                     |

### **2.8 Performance & Monitoring**
| Setting                     | Gameplay Tag                            | Options                     | Description                                                    |
| :-------------------------- | :-------------------------------------- | :-------------------------- | :------------------------------------------------------------- |
| **Performance Stats**       | `Settings.Video.PerformanceStats`       | OFF / Simple / Detailed     | On-screen performance overlay.                                 |
| **Show FPS**                | `Settings.Video.ShowFPS`                | OFF / ON                    | Display current framerate.                                     |
| **FPS Counter Position**    | `Settings.Video.FPSPosition`            | Top Left / Top Right / Bottom Left / Bottom Right | Position of FPS counter.                     |
| **Show Frame Time**         | `Settings.Video.ShowFrameTime`          | OFF / ON                    | Display ms per frame (1000/FPS).                               |
| **Show Ping**               | `Settings.Video.ShowPing`               | OFF / ON                    | Display network latency.                                       |
| **Show Packet Loss**        | `Settings.Video.ShowPacketLoss`         | OFF / ON                    | Display % of lost packets.                                     |
| **Show Network Graph**      | `Settings.Video.NetworkGraph`           | OFF / ON                    | Real-time bandwidth/latency visualization.                     |
| **Show GPU Temp**           | `Settings.Video.ShowGPUTemp`            | OFF / ON                    | Display graphics card temperature.                             |
| **Show CPU Temp**           | `Settings.Video.ShowCPUTemp`            | OFF / ON                    | Display processor temperature.                                 |
| **Show VRAM Usage**         | `Settings.Video.ShowVRAM`               | OFF / ON                    | Display video memory usage.                                    |
| **Show System Latency**     | `Settings.Video.ShowLatency`            | OFF / ON                    | Display end-to-end system latency (NVIDIA Reflex).             |
| **Stats Text Size**         | `Settings.Video.StatsTextSize`          | Small / Medium / Large      | Size of performance overlay text.                              |

### **2.9 Advanced Rendering**
| Setting                     | Gameplay Tag                            | Options                     | Description                                                    |
| :-------------------------- | :-------------------------------------- | :-------------------------- | :------------------------------------------------------------- |
| **Render Pipeline**         | `Settings.Video.Pipeline`               | Forward / Deferred          | Rendering architecture. Deferred better for many lights.       |
| **Particle Quality**        | `Settings.Video.ParticleQuality`        | Low / Medium / High         | Smoke, dust, ability effects quality.                          |
| **Particle Density**        | `Settings.Video.ParticleDensity`        | Slider (10 - 100%)          | Number of particles rendered.                                  |
| **Decal Quality**           | `Settings.Video.DecalQuality`           | Low / Medium / High         | Bullet holes, blood, scorch marks.                             |
| **Max Decals**              | `Settings.Video.MaxDecals`              | Slider (10 - 500)           | Maximum decals before culling old ones.                        |
| **Water Quality**           | `Settings.Video.WaterQuality`           | Low / Medium / High         | Water reflections and ripples.                                 |
| **Tessellation**            | `Settings.Video.Tessellation`           | OFF / ON                    | Geometry detail enhancement (DX11+ GPUs).                      |
| **Anisotropic Filtering**   | `Settings.Video.AnisotropicFiltering`   | OFF / 2x / 4x / 8x / 16x    | Texture clarity at angles. 16x recommended.                    |

---

## 🔊 3. AUDIO SETTINGS (Sound)

*Settings optimized for competitive audio positioning and immersion.*

### **3.1 Volume Mixer**
| Setting                     | Gameplay Tag                       | Range       | Description                                                    |
| :-------------------------- | :--------------------------------- | :---------- | :------------------------------------------------------------- |
| **Master Volume**           | `Settings.Audio.MasterVolume`      | 0 - 100%    | Global output volume.                                          |
| **SFX Volume**              | `Settings.Audio.SFXVolume`         | 0 - 100%    | **Critical:** Footsteps, gunshots, reloads, environmental cues.|
| **Footstep Volume**         | `Settings.Audio.FootstepVolume`    | 0 - 200%    | Separate control for footstep sounds.                          |
| **Gunfire Volume**          | `Settings.Audio.GunfireVolume`     | 0 - 200%    | Your weapon vs enemy weapon volume.                            |
| **Explosion Volume**        | `Settings.Audio.ExplosionVolume`   | 0 - 200%    | Grenades, ability explosions.                                  |
| **Dialogue Volume**         | `Settings.Audio.DialogueVolume`    | 0 - 100%    | Hero voice lines, character callouts.                          |
| **Voice Chat**              | `Settings.Audio.VoiceVolume`       | 0 - 200%    | Volume of incoming teammate communications.                    |
| **UI Volume**               | `Settings.Audio.UIVolume`          | 0 - 100%    | Clicks, inventory sounds, notifications, pings.                |
| **Music (In-Game)**         | `Settings.Audio.MusicInGame`       | 0 - 100%    | Raid/match music. Recommended LOW/OFF for competitive.         |
| **Music (Menu)**            | `Settings.Audio.MusicMenu`         | 0 - 100%    | Lobby and menu background music.                               |
| **Music (Extraction)**      | `Settings.Audio.MusicExtraction`   | 0 - 100%    | Music that plays near/during extraction. Can mask footsteps.   |
| **Music (Victory/Defeat)**  | `Settings.Audio.MusicEndGame`      | 0 - 100%    | End-of-match music.                                            |
| **Ambient**                 | `Settings.Audio.AmbientVolume`     | 0 - 100%    | Wind, rain, wildlife, room tone, atmospheric sounds.           |
| **Vehicle**                 | `Settings.Audio.VehicleVolume`     | 0 - 100%    | Engine sounds, movement, impacts.                              |

### **3.2 Audio Output**
| Setting                     | Gameplay Tag                       | Options                              | Description                                              |
| :-------------------------- | :--------------------------------- | :----------------------------------- | :------------------------------------------------------- |
| **Output Device**           | `Settings.Audio.OutputDevice`      | System Default / Device Name         | Hardware speaker/headphone selection.                    |
| **Speaker Configuration**   | `Settings.Audio.SpeakerConfig`     | Stereo / 5.1 / 7.1 / Headphones      | Audio channel configuration.                             |
| **Headphone Type**          | `Settings.Audio.HeadphoneType`     | On-Ear / Over-Ear / In-Ear / Buds    | Optimize HRTF for headphone style.                       |
| **Mono Audio**              | `Settings.Audio.MonoAudio`         | OFF / ON                             | Combine stereo to mono (accessibility).                  |
| **Audio Sample Rate**       | `Settings.Audio.SampleRate`        | 44.1kHz / 48kHz / 96kHz              | Higher = better quality, more CPU.                       |

### **3.3 Voice Chat (VoIP)**
| Setting                     | Gameplay Tag                          | Options                           | Description                                           |
| :-------------------------- | :------------------------------------ | :-------------------------------- | :---------------------------------------------------- |
| **Voice Chat**              | `Settings.Audio.VoIP.Enabled`         | OFF / ON                          | Enable/disable voice chat globally.                   |
| **Chat Mode**               | `Settings.Audio.VoIP.Mode`            | Push-to-Talk / Open Mic / Muted   | Activation method.                                    |
| **PTT Behavior**            | `Settings.Audio.VoIP.PTTBehavior`     | While Held / Toggle               | Press once to talk vs hold to talk.                   |
| **Input Device**            | `Settings.Audio.VoIP.InputDevice`     | System Default / Microphone Name  | Microphone selection.                                 |
| **Input Sensitivity**       | `Settings.Audio.VoIP.Sensitivity`     | Slider (-60dB to 0dB)             | Mic activation threshold (for Open Mic).              |
| **Noise Suppression**       | `Settings.Audio.VoIP.NoiseSuppression`| OFF / Standard / AI-Enhanced      | Remove background noise. "AI" uses RNNoise/Krisp.     |
| **Echo Cancellation**       | `Settings.Audio.VoIP.EchoCancellation`| OFF / ON                          | Prevent feedback loop.                                |
| **Automatic Gain Control**  | `Settings.Audio.VoIP.AGC`             | OFF / ON                          | Normalize microphone volume automatically.            |
| **Voice Activity LED**      | `Settings.Audio.VoIP.ActivityLED`     | OFF / ON                          | Show indicator when mic is transmitting.              |
| **Ducking**                 | `Settings.Audio.VoIP.Ducking`         | OFF / 25% / 50% / 75%             | Lower game audio when teammates talk.                 |
| **Voice Chat Volume**       | `Settings.Audio.VoIP.OutputVolume`    | Slider (0 - 200%)                 | Boost teammate voice volume separately.               |
| **Record Own Voice**        | `Settings.Audio.VoIP.RecordMic`       | OFF / ON                          | Include own voice in clips/highlights.                |
| **Proximity Chat**          | `Settings.Audio.VoIP.ProximityChat`   | OFF / ON                          | Enable proximity-based voice with nearby players.     |
| **Proximity Range**         | `Settings.Audio.VoIP.ProximityRange`  | Short (10m) / Medium (25m) / Long (50m) | How far proximity chat reaches.             |
| **Team Voice Privacy**      | `Settings.Audio.VoIP.TeamPrivacy`     | Team Only / Proximity + Team      | Can enemies hear team voice in proximity mode.        |

### **3.4 Advanced Audio**
| Setting                     | Gameplay Tag                          | Options                              | Description                                                       |
| :-------------------------- | :------------------------------------ | :----------------------------------- | :---------------------------------------------------------------- |
| **Audio Quality**           | `Settings.Audio.Quality`              | Low / Medium / High / Ultra          | Sample rate and codec quality.                                    |
| **Dynamic Range**           | `Settings.Audio.DynamicRange`         | Hi-Fi / Night Mode / TV / Loudness War | "Night Mode" compresses loud sounds. "Hi-Fi" preserves dynamics.|
| **Loudness Equalization**   | `Settings.Audio.LoudnessEqualization` | OFF / ON                             | Windows loudness equalization override.                           |
| **EQ Preset**               | `Settings.Audio.EQPreset`             | Flat / Bass Boost / Treble Boost / Footsteps / Custom | "Treble Boost" highlights footsteps.  |
| **Custom EQ**               | `Settings.Audio.CustomEQ`             | 10-band Equalizer                    | Manual frequency adjustment (Hz bands).                           |
| **3D Audio / Spatial**      | `Settings.Audio.Spatial`              | OFF / Binaural / Windows Sonic / Dolby Atmos / DTS:X | HRTF for directional sound. "Binaural" for headphones.|
| **HRTF Profile**            | `Settings.Audio.HRTF.Profile`         | Generic / Personalized               | Use generic head model or custom calibrated profile.              |
| **Virtualization Quality**  | `Settings.Audio.VirtualizationQuality`| Low / Medium / High                  | 3D audio processing quality.                                      |
| **Sound Occlusion**         | `Settings.Audio.Occlusion`            | OFF / Simple / Realistic             | Sound muffled through walls. "Realistic" = heavy CPU.             |
| **Reverb Quality**          | `Settings.Audio.ReverbQuality`        | Low / Medium / High                  | Environmental acoustics (echo in buildings).                      |
| **Environmental Audio**     | `Settings.Audio.Environmental`        | OFF / Low / Medium / High            | Context-aware sound (indoors vs outdoors).                        |
| **Sound Lock (Limiter)**    | `Settings.Audio.SoundLock`            | OFF / ON                             | Hard limiter to prevent hearing damage from spikes (gunshots).    |
| **Sound Lock Threshold**    | `Settings.Audio.SoundLockThreshold`   | Slider (-30dB to 0dB)                | Maximum loudness before limiting.                                 |
| **Mute on Focus Loss**      | `Settings.Audio.MuteOnFocusLoss`      | OFF / ON                             | Mute game when Alt-Tabbed (Windows).                              |
| **Loudness Normalization**  | `Settings.Audio.LoudnessNorm`         | OFF / ON                             | Even out volume across different sound sources.                   |

### **3.5 Subtitles & Captions**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Subtitles**               | `Settings.Audio.Subtitles.Enabled`    | OFF / ON                    | Display text for dialogue and voice lines.               |
| **Subtitle Size**           | `Settings.Audio.Subtitles.Size`       | Small / Medium / Large / XL | Font size.                                               |
| **Subtitle Background**     | `Settings.Audio.Subtitles.Background` | None / Semi / Solid         | Background opacity for readability.                      |
| **Speaker Names**           | `Settings.Audio.Subtitles.SpeakerName`| OFF / ON                    | Show who is speaking in subtitles.                       |
| **Speaker Color Coding**    | `Settings.Audio.Subtitles.ColorCode`  | OFF / ON                    | Different colors for different speakers.                 |
| **Sound Captions**          | `Settings.Audio.Captions`             | OFF / Important / All       | Visual indicators for sounds (footsteps, gunshots).      |
| **Caption Style**           | `Settings.Audio.Captions.Style`       | Icon / Text / Icon+Text     | How sound captions display.                              |
| **Caption Direction**       | `Settings.Audio.Captions.Direction`   | OFF / ON                    | Show directional arrows for sounds.                      |
| **Caption Distance**        | `Settings.Audio.Captions.ShowDistance`| OFF / ON                    | Show estimated distance to sound source.                 |

---

## 📡 4. GAMEPLAY & INTERFACE (HUD)

*Settings for combat feedback, UI visibility, and gameplay assistance.*

### **4.1 HUD Customization**
| Setting                     | Gameplay Tag                          | Options                        | Description                                                  |
| :-------------------------- | :------------------------------------ | :----------------------------- | :----------------------------------------------------------- |
| **HUD Preset**              | `Settings.HUD.Preset`                 | Minimal / Standard / Full / Competitive | Quick toggle for HUD complexity.                     |
| **HUD Opacity**             | `Settings.HUD.Opacity`                | Slider (0 - 100%)              | Overall HUD transparency.                                    |
| **HUD Scale**               | `Settings.HUD.Scale`                  | Slider (50 - 150%)             | Size of all HUD elements.                                    |
| **Safe Zone**               | `Settings.HUD.SafeZone`               | Slider (0 - 10%)               | Inset HUD elements from screen edges (for TVs).              |
| **HUD Color Scheme**        | `Settings.HUD.ColorScheme`            | Default / Monochrome / Neon / Custom | Visual theme for UI.                                  |
| **Dynamic HUD**             | `Settings.HUD.Dynamic`                | OFF / ON                       | Hide elements when not needed (adaptive UI).                 |

### **4.2 Crosshair & Reticle**
| Setting                     | Gameplay Tag                          | Options                        | Description                                                  |
| :-------------------------- | :------------------------------------ | :----------------------------- | :----------------------------------------------------------- |
| **Crosshair Preset**        | `Settings.HUD.Crosshair.Preset`       | Cross / Dot / Circle / T-Shape / Custom | Base reticle shape.                                   |
| **Crosshair Color**         | `Settings.HUD.Crosshair.Color`        | RGB Picker / Presets           | High contrast color recommended (Cyan/Green).                |
| **Crosshair Thickness**     | `Settings.HUD.Crosshair.Thickness`    | Slider (1 - 5)                 | Line width.                                                  |
| **Crosshair Length**        | `Settings.HUD.Crosshair.Length`       | Slider (1 - 20)                | Length of crosshair lines.                                   |
| **Crosshair Gap**           | `Settings.HUD.Crosshair.Gap`          | Slider (0 - 20)                | Space between lines.                                         |
| **Crosshair Outline**       | `Settings.HUD.Crosshair.Outline`      | OFF / ON                       | Black border for visibility on any background.               |
| **Crosshair Opacity**       | `Settings.HUD.Crosshair.Opacity`      | Slider (0 - 100%)              | Transparency.                                                |
| **Center Dot**              | `Settings.HUD.Crosshair.CenterDot`    | OFF / ON                       | Center dot in addition to crosshair.                         |
| **Center Dot Size**         | `Settings.HUD.Crosshair.DotSize`      | Slider (1 - 10)                | Pixel size of center dot.                                    |
| **Dynamic Crosshair**       | `Settings.HUD.Crosshair.Dynamic`      | OFF / Spread / Color / Both    | Expands when moving/firing and/or changes color.             |
| **Dynamic Spread Scale**    | `Settings.HUD.Crosshair.SpreadScale`  | Slider (0.5 - 2.0)             | How much crosshair expands.                                  |
| **Dynamic Color Change**    | `Settings.HUD.Crosshair.DynamicColor` | Target Color                   | Color when crosshair is dynamic.                             |
| **Per-Weapon Crosshair**    | `Settings.HUD.Crosshair.PerWeapon`    | OFF / ON                       | Different crosshair for each weapon type.                    |

### **4.3 Hit Feedback**
| Setting                     | Gameplay Tag                          | Options                        | Description                                                  |
| :-------------------------- | :------------------------------------ | :----------------------------- | :----------------------------------------------------------- |
| **Hit Indicator**           | `Settings.HUD.HitIndicator`           | OFF / Crosshair / Screen Edge / Both | Feedback when bullets connect.                         |
| **Hit Marker Style**        | `Settings.HUD.HitMarkerStyle`         | X / + / Circle / Custom        | Visual shape of hit marker.                                  |
| **Hit Marker Color**        | `Settings.HUD.HitMarkerColor`         | White / Red / Yellow / Custom  | Color of standard hit marker.                                |
| **Hit Marker Sound**        | `Settings.HUD.HitMarkerSound`         | OFF / Standard / Satisfying / Bass Heavy | Audio confirmation of hits.                       |
| **Headshot Indicator**      | `Settings.HUD.HeadshotIndicator`      | OFF / Different Color / Different Sound / Both | Unique feedback for headshots.             |
| **Headshot Sound**          | `Settings.HUD.HeadshotSound`          | OFF / Distinct / Exaggerated   | Unique sound for headshots.                                  |
| **Headshot Color**          | `Settings.HUD.HeadshotColor`          | Red / Gold / Custom            | Hit marker color for headshots.                              |
| **Damage Numbers**          | `Settings.HUD.DamageNumbers`          | OFF / Stacked / Floating       | Display damage dealt. "Stacked" combines (15→30→45).         |
| **Damage Number Style**     | `Settings.HUD.DamageStyle`            | Standard / Large / Compact     | Size and presentation.                                       |
| **Damage Number Color**     | `Settings.HUD.DamageNumberColor`      | Dynamic / Static               | Change color based on damage type.                           |
| **Critical Hit Feedback**   | `Settings.HUD.CriticalFeedback`       | OFF / Color / Size / Both      | Highlight critical damage differently.                       |
| **Shield Break Indicator**  | `Settings.HUD.ShieldBreak`            | OFF / Visual / Audio / Both    | Special feedback when breaking enemy shields.                |

### **4.4 Health, Armor & Status**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Health Bar Style**        | `Settings.HUD.HealthBar.Style`        | Bar / Segments / Numerical  | How health displays.                                     |
| **Health Bar Visibility**   | `Settings.HUD.HealthBar.Visibility`   | Always / Dynamic / Low Only | "Dynamic" hides when full; "Low" shows when damaged.     |
| **Health Numbers**          | `Settings.HUD.HealthNumbers`          | OFF / Current / Current+Max / Percentage | Show exact HP value.                          |
| **Armor Display**           | `Settings.HUD.ArmorDisplay`           | Bar / Plate Icons / Both    | Visualize armor/shields.                                 |
| **Armor Number**            | `Settings.HUD.ArmorNumbers`           | OFF / ON                    | Show numeric armor value.                                |
| **Status Effects**          | `Settings.HUD.StatusEffects`          | Icons / Text / Both / OFF   | Bleeding, poison, fractures, debuffs.                    |
| **Status Effect Timers**    | `Settings.HUD.StatusTimers`           | OFF / ON                    | Countdown timers for status effects.                     |
| **Low Health Warning**      | `Settings.HUD.LowHealthWarning`       | OFF / Visual / Audio / Both | Screen effects and sound when critically wounded.        |
| **Low Health Threshold**    | `Settings.HUD.LowHealthThreshold`     | Slider (10-50%)             | HP% to trigger low health warning.                       |
| **Health Regeneration UI**  | `Settings.HUD.HealthRegen`            | OFF / ON                    | Show healing over time animation.                        |
| **Stamina Bar**             | `Settings.HUD.StaminaBar`             | Always / When Active / OFF  | Sprint/hold breath meter visibility.                     |

### **4.5 Minimap & Compass**
| Setting                     | Gameplay Tag                          | Options                        | Description                                              |
| :-------------------------- | :------------------------------------ | :----------------------------- | :------------------------------------------------------- |
| **Minimap**                 | `Settings.HUD.Minimap.Enabled`        | OFF / ON                       | Show/hide minimap.                                       |
| **Minimap Size**            | `Settings.HUD.Minimap.Size`           | Slider (50 - 200%)             | Minimap dimensions.                                      |
| **Minimap Zoom**            | `Settings.HUD.Minimap.Zoom`           | Slider (0.5x - 3.0x)           | Map scale.                                               |
| **Minimap Position**        | `Settings.HUD.Minimap.Position`       | Top Left / Top Right / Bottom Left / Bottom Right | Minimap screen location.                |
| **Minimap Rotation**        | `Settings.HUD.Minimap.Rotation`       | Fixed North / Rotates          | "Rotates" keeps player facing up.                        |
| **Minimap Opacity**         | `Settings.HUD.Minimap.Opacity`        | Slider (0 - 100%)              | Transparency.                                            |
| **Show Teammates**          | `Settings.HUD.Minimap.Teammates`      | Always / Nearby / OFF          | Display allied player positions.                         |
| **Teammate Colors**         | `Settings.HUD.Minimap.TeammateColors` | Unique / All Blue / OFF        | Color-code squad members.                                |
| **Show Objectives**         | `Settings.HUD.Minimap.Objectives`     | OFF / ON                       | Extraction points, mission markers.                      |
| **Show Loot Crates**        | `Settings.HUD.Minimap.Loot`           | OFF / ON                       | High-value loot locations.                               |
| **Show Vehicles**           | `Settings.HUD.Minimap.Vehicles`       | OFF / ON                       | Vehicle positions on map.                                |
| **Show Gunfire**            | `Settings.HUD.Minimap.Gunfire`        | OFF / ON                       | Gunshot indicators on minimap.                           |
| **Gunfire Fade Time**       | `Settings.HUD.Minimap.GunfireFade`    | Short (2s) / Medium (5s) / Long (10s) | How long gunfire indicators stay.                |
| **Compass**                 | `Settings.HUD.Compass.Style`          | Top Bar / Minimap Edge / Both / OFF | Directional aid.                                    |
| **Compass Markers**         | `Settings.HUD.Compass.Markers`        | Distance / Icons / Both        | Show pings and objectives on compass.                    |
| **Elevation Markers**       | `Settings.HUD.Compass.Elevation`      | OFF / ON                       | Show up/down arrows for vertical positioning.            |

### **4.6 Kill Feed & Notifications**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Kill Feed**               | `Settings.HUD.KillFeed.Style`         | Full / Icons Only / OFF     | Combat log in corner.                                    |
| **Kill Feed Duration**      | `Settings.HUD.KillFeed.Duration`      | Short (3s) / Medium (5s) / Long (10s) | How long kills stay visible.                   |
| **Kill Feed Position**      | `Settings.HUD.KillFeed.Position`      | Top Right / Top Left / Bottom Right | Screen location.                                |
| **Show Weapon Icons**       | `Settings.HUD.KillFeed.WeaponIcons`   | OFF / ON                    | Display weapon used in kills.                            |
| **Show Distance**           | `Settings.HUD.KillFeed.Distance`      | OFF / ON                    | Show range of kills in feed.                             |
| **Highlight Own Kills**     | `Settings.HUD.KillFeed.HighlightOwn`  | OFF / ON                    | Make your kills more visible.                            |
| **Show Assists**            | `Settings.HUD.KillFeed.ShowAssists`   | OFF / ON                    | Display assists in kill feed.                            |
| **Kill Notifications**      | `Settings.HUD.KillNotifications`      | Full / Name Only / Minimal / OFF | On-screen popup when you get a kill.                |
| **Multi-Kill Announcer**    | `Settings.HUD.MultiKillAnnouncer`     | OFF / Visual / Audio / Both | "Double Kill", "Triple Kill" announcements.              |
| **Assist Notifications**    | `Settings.HUD.AssistNotifications`    | OFF / ON                    | Show when you assisted kills.                            |
| **XP Gain Popup**           | `Settings.HUD.XPPopup`                | OFF / Compact / Detailed    | Show XP/objective completion notifications.              |
| **Medal Display**           | `Settings.HUD.Medals`                 | OFF / ON                    | Show achievement medals during match.                    |

### **4.7 Weapon & Equipment HUD**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Ammo Counter Style**      | `Settings.HUD.AmmoCounter.Style`      | Standard / Compact / Numeric / Magazine | Display format.                                  |
| **Ammo Counter Position**   | `Settings.HUD.AmmoCounter.Position`   | Bottom Right / Bottom Center / Top Right | Screen location.                           |
| **Low Ammo Warning**        | `Settings.HUD.LowAmmoWarning`         | OFF / Color / Flash / Both  | Alert when magazine nearly empty.                        |
| **Low Ammo Threshold**      | `Settings.HUD.LowAmmoThreshold`       | Slider (10-50%)             | Remaining ammo % to trigger warning.                     |
| **Weapon Name Display**     | `Settings.HUD.WeaponName`             | Always / On Switch / OFF    | Show current weapon name.                                |
| **Fire Mode Indicator**     | `Settings.HUD.FireMode`               | OFF / ON                    | Display auto/semi/burst mode.                            |
| **Ammo Reserve Display**    | `Settings.HUD.AmmoReserve`            | OFF / ON                    | Show total ammo count beyond current magazine.           |
| **Equipment Cooldowns**     | `Settings.HUD.EquipmentCooldowns`     | Progress Bar / Timer / Both | Grenade/equipment recharge.                              |
| **Quick Slots**             | `Settings.HUD.QuickSlots.Visibility`  | Always / Auto-Hide / Wheel  | Hotbar (keys 4-9) visibility.                            |
| **Quick Slot Numbers**      | `Settings.HUD.QuickSlots.ShowNumbers` | OFF / ON                    | Display key bindings on items.                           |
| **Throwable Arc**           | `Settings.HUD.ThrowableArc`           | Full / Partial / OFF        | Grenade trajectory preview.                              |

### **4.8 Hero-Specific HUD**
| Setting                     | Gameplay Tag                         | Options                     | Description                                           |
| :-------------------------- | :----------------------------------- | :-------------------------- | :---------------------------------------------------- |
| **Ability UI Style**        | `Settings.HUD.Abilities.Style`       | Icons / Hotkeys / Both / OFF | How abilities display.                               |
| **Ability Position**        | `Settings.HUD.Abilities.Position`    | Bottom Center / Bottom Right / Custom | Screen location of ability UI.            |
| **Ability Cooldown Format** | `Settings.HUD.Abilities.Cooldown`    | Radial / Numeric / Both     | Cooldown visualization.                               |
| **Ability Charges**         | `Settings.HUD.Abilities.Charges`     | OFF / ON                    | Show number of charges for multi-use abilities.       |
| **Ability Range Indicators**| `Settings.HUD.Abilities.Range`       | OFF / ON                    | Show AoE/range previews.                              |
| **Ultimate Status**         | `Settings.HUD.Ultimate.Visibility`   | Always / When Ready / Percent / OFF | Ultimate ability charge state.                 |
| **Ultimate Ready Notification** | `Settings.HUD.Ultimate.Notification` | OFF / Visual / Audio / Both | Alert when ultimate is ready.                  |
| **Ultimate Charge Display** | `Settings.HUD.Ultimate.ChargeStyle`  | Percentage / Orbs / Bar     | How ultimate charge shows.                            |
| **Passive Ability Icon**    | `Settings.HUD.Passive.Show`          | OFF / ON                    | Display passive ability reminder.                     |
| **Hero Portrait**           | `Settings.HUD.HeroPortrait`          | 2D / 3D / OFF               | Character avatar in HUD.                              |
| **Hero Voice Lines Volume** | `Settings.HUD.VoiceLines.Frequency`  | All / Important Only / OFF  | How often hero speaks.                                |
| **Hero Emote Wheel Style**  | `Settings.HUD.EmoteWheel.Style`      | Radial / Grid / List        | Layout of emote/ping menu.                            |

### **4.9 Team & Social HUD**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Teammate Nameplates**     | `Settings.HUD.Nameplates.Teammates`   | Always / Distance-Based / OFF | Show names above allies.                               |
| **Nameplate Distance**      | `Settings.HUD.Nameplates.Distance`    | Slider (10m - 200m)         | Maximum distance to show names.                          |
| **Teammate Health Bars**    | `Settings.HUD.TeammateHealth`         | Always / Low Health / OFF   | See teammate HP status.                                  |
| **Teammate Armor Display**  | `Settings.HUD.TeammateArmor`          | OFF / ON                    | Show teammate shield/armor bars.                         |
| **Teammate Status Icons**   | `Settings.HUD.TeammateStatus`         | OFF / ON                    | Show if teammate is healing, reloading, etc.             |
| **Teammate Hero Icons**     | `Settings.HUD.TeammateHeroIcons`      | Hero Icon / Arrow / Both / OFF | How to identify squadmates.                           |
| **Ping System Style**       | `Settings.HUD.Ping.Style`             | 3D / 2D / Both              | World markers vs screen icons.                           |
| **Ping Visibility**         | `Settings.HUD.Ping.Visibility`        | Always / Timed (10s) / Manual Clear | How long pings stay visible.                      |
| **Ping Distance Display**   | `Settings.HUD.Ping.Distance`          | OFF / ON                    | Display distance to pinged location.                     |
| **Ping Color Coding**       | `Settings.HUD.Ping.ColorCode`         | By Type / By Player / OFF   | Different colors for different ping types or players.    |
| **Teammate Outlines**       | `Settings.HUD.TeammateOutlines`       | Always / Through Walls / OFF | Highlight allies.                                       |
| **Outline Opacity**         | `Settings.HUD.OutlineOpacity`         | Slider (0 - 100%)           | Transparency of player outlines.                         |
| **Squad Status Panel**      | `Settings.HUD.SquadStatus`            | Detailed / Compact / OFF    | Show squad health/ammo/status summary.                   |
| **Downed Teammate Alert**   | `Settings.HUD.DownedAlert`            | OFF / Visual / Audio / Both | Special notification when ally is downed.                |

### **4.10 Loot & Interaction**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Loot Highlight**          | `Settings.HUD.Loot.Highlight`         | OFF / Subtle / Standard / Strong | Colored outline around loot.                        |
| **Loot Rarity Colors**      | `Settings.HUD.Loot.RarityColors`      | OFF / ON                    | Color-code items by rarity.                              |
| **Loot Labels**             | `Settings.HUD.Loot.Labels`            | Always / On Hover / OFF     | Show item names in world.                                |
| **Loot Label Distance**     | `Settings.HUD.Loot.LabelDistance`     | Slider (1m - 50m)           | How far to show loot labels.                             |
| **Loot Quality Filter**     | `Settings.HUD.Loot.QualityFilter`     | Show All / Rare+ / Epic+ / Legendary Only | Only show high-tier loot labels.            |
| **Quick Loot Window**       | `Settings.HUD.QuickLoot`              | OFF / ON                    | Popup inventory when looking at loot.                    |
| **Loot Beam**               | `Settings.HUD.LootBeam`               | OFF / Epic+ / Legendary Only | Vertical light beam on rare items.                      |
| **Interaction Prompts**     | `Settings.HUD.InteractionPrompts`     | Full / Icon Only / Minimal  | Detail level of "Press E to..." messages.                |
| **Interaction Prompt Size** | `Settings.HUD.InteractionSize`        | Small / Medium / Large      | Size of interaction text.                                |
| **Auto-Sort Inventory**     | `Settings.Gameplay.AutoSort`          | OFF / ON                    | Automatically organize inventory Tetris-style.           |
| **Double Click Action**     | `Settings.Gameplay.DoubleClickAction` | Use / Equip / Inspect       | Default action for items.                                |
| **Inventory Grid Style**    | `Settings.HUD.InventoryGrid`          | Tetris / List / Hybrid      | Inventory management layout.                             |

### **4.11 Objectives & Extraction**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Extraction Timer**        | `Settings.HUD.ExtractionTimer`        | Always / When Nearby / OFF  | Show time until extraction opens/closes.                 |
| **Extraction Distance**     | `Settings.HUD.ExtractionDistance`     | OFF / ON                    | Display distance to extraction zone.                     |
| **Extraction Warning**      | `Settings.HUD.ExtractionWarning`      | OFF / Visual / Audio / Both | Alert when extraction closing soon.                      |
| **Extraction Indicator**    | `Settings.HUD.ExtractionIndicator`    | Compass / 3D Marker / Both  | How to show extraction location.                         |
| **Mission Objectives Style**| `Settings.HUD.Objectives.Style`       | Compact / Detailed / OFF    | Quest/task tracker.                                      |
| **Objective Markers**       | `Settings.HUD.Objectives.Markers`     | 3D / Minimap / Both / OFF   | How to show quest locations.                             |
| **Objective Distance**      | `Settings.HUD.Objectives.ShowDistance`| OFF / ON                    | Display range to objectives.                             |
| **Raid Timer**              | `Settings.HUD.RaidTimer`              | Always / Final 10min / Final 5min / OFF | Remaining time in match.                       |
| **Match Progress Bar**      | `Settings.HUD.MatchProgress`          | OFF / ON                    | Visual indicator of match progression.                   |

### **4.12 Death & Spectator**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Death Cam**               | `Settings.HUD.DeathCam`               | Full Replay / Killer POV / Skip | Replay of how you died.                              |
| **Death Cam Duration**      | `Settings.HUD.DeathCam.Duration`      | 3s / 5s / 10s / Full Replay | How long death cam plays.                                |
| **Death Cam Auto-Skip**     | `Settings.HUD.DeathCam.AutoSkip`      | OFF / ON                    | Automatically skip to spectator after death cam.         |
| **Show Killer Info**        | `Settings.HUD.KillerInfo`             | Full / Name+Distance / Name Only / OFF | Display killer's weapon and distance.         |
| **Damage Recap**            | `Settings.HUD.DamageRecap`            | Detailed / Simple / OFF     | Show how much damage you took and from where.            |
| **Spectator Mode**          | `Settings.HUD.Spectator.Mode`         | Free Cam / Follow / Cycle   | Camera control when dead.                                |
| **Spectator UI**            | `Settings.HUD.Spectator.UI`           | Full HUD / Minimal / OFF    | Show teammate's HUD when spectating.                     |
| **Spectator X-Ray**         | `Settings.HUD.Spectator.XRay`         | OFF / ON                    | See player outlines through walls when spectating.       |
| **Revive Timer Display**    | `Settings.HUD.ReviveTimer`            | OFF / ON                    | Show countdown before permanent death.                   |

---

## 🦸 5. HERO & CHARACTER SETTINGS

*Settings unique to hero-based gameplay mechanics.*

### **5.1 Hero Preferences**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Default Hero**            | `Settings.Hero.Default`               | Hero Name / Last Played / Random | Auto-select hero in lobby.                          |
| **Hero Auto-Lock**          | `Settings.Hero.AutoLock`              | OFF / ON                    | Confirm selection immediately vs manual confirm.         |
| **Random Hero Pool**        | `Settings.Hero.RandomPool`            | All / Favorites / Role-Based | When using random selection.                            |
| **Hero Voice Language**     | `Settings.Hero.VoiceLanguage`         | Original / Localized        | Use English VO or translated.                            |
| **Hero Voice Volume**       | `Settings.Hero.VoiceVolume`           | Slider (0 - 200%)           | Separate volume for character dialogue.                  |

### **5.2 Ability Feedback & Behavior**
| Setting                     | Gameplay Tag                        | Options                     | Description                                           |
| :-------------------------- | :---------------------------------- | :-------------------------- | :---------------------------------------------------- |
| **Ability Activation Flash**| `Settings.Hero.AbilityFlash`        | Full / Minimal / OFF        | Screen effect when using abilities.                   |
| **Ability Sound Effects**   | `Settings.Hero.AbilitySFX`          | Full / Minimal / OFF        | Volume of ability audio cues.                         |
| **Ability VFX Quality**     | `Settings.Hero.AbilityVFX`          | High / Medium / Low         | Visual effects quality for powers.                    |
| **Self Ability VFX**        | `Settings.Hero.SelfAbilityVFX`      | Full / Reduced / Minimal    | VFX intensity for your own abilities.                 |
| **Enemy Ability Alerts**    | `Settings.Hero.EnemyAbilityAlerts`  | Visual / Audio / Both / OFF | Warnings when enemies use abilities nearby.           |
| **Ability Combo Hints**     | `Settings.Hero.ComboHints`          | OFF / Beginner Only / Always | Show suggested ability combinations.                 |
| **Ultimate Charge from Damage** | `Settings.Hero.UltChargeFromDamage` | Full / Reduced / OFF   | Gain ultimate charge from dealing damage.             |

### **5.3 Cosmetics & Animation**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| ~~**First Person Arms**~~       | `Settings.Hero.FPArms`                | Hero Sleeves / Generic      | Show character-specific arms or neutral gloves.          |
| **Finishers Enabled**       | `Settings.Hero.Finishers.Enabled`     | OFF / ON                    | Enable execution animations on downed enemies.           |
| **Finisher Camera**         | `Settings.Hero.Finishers.Camera`      | Cinematic / ~~First Person~~ / Skip | View during finishers.                              |
| **Finisher Frequency**      | `Settings.Hero.Finishers.Frequency`   | Every Kill / Occasionally / Rare | How often finishers trigger automatically.         |
| **Inspect Animations**      | `Settings.Hero.InspectAnims`          | Full / Shortened / OFF      | Weapon/gear inspect animations.                          |
| **Emote Animations**        | `Settings.Hero.Emotes.Length`         | Full / Short / OFF          | Duration of emotes and taunts.                           |
| **Emote Interrupt**         | `Settings.Hero.Emotes.Interrupt`      | Any Action / Combat Only    | What cancels emotes.                                     |
| **Victory Pose**            | `Settings.Hero.VictoryPose`           | Enabled / Disabled          | Show hero pose on match victory.                         |
| **Lobby Idle Animation**    | `Settings.Hero.LobbyIdle`             | OFF / ON                    | Character animations in main menu.                       |
| **Skin Preview Quality**    | `Settings.Hero.SkinPreviewQuality`    | High / Medium / Low         | Detail level in cosmetics menu.                          |

---

## 💾 6. ACCOUNT & SYSTEM SETTINGS

*Account management, privacy, social, and platform settings.*

### **6.1 Account Information**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Username**                | `Settings.Account.Username`           | Text Field                  | Display name (may require purchase to change).           |
| **Account Linking**         | `Settings.Account.Linking`            | Steam / EGS / PSN / Xbox / Apple | Connect platform accounts.                          |
| **Cross-Progression**       | `Settings.Account.CrossProgression`   | OFF / ON                    | Sync progress across platforms.                          |
| **Cloud Saves**             | `Settings.Account.CloudSaves`         | OFF / ON                    | Backup settings and progress to cloud.                   |
| **Data Center Region**      | `Settings.Account.DataCenter`         | Auto / NA East / NA West / EU / Asia / etc. | Preferred server location.                |
| **Download Region**         | `Settings.Account.DownloadRegion`     | Auto / Select Region        | Preferred CDN for updates.                               |

### **6.2 Privacy & Visibility**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Profile Visibility**      | `Settings.Privacy.ProfileVisibility`  | Public / Friends Only / Private | Who can view your stats and loadouts.                 |
| **Online Status**           | `Settings.Privacy.OnlineStatus`       | Online / Appear Offline / Invisible | Show as online to friends.                        |
| **Streamer Mode**           | `Settings.Privacy.StreamerMode`       | OFF / ON                    | Hides names, server IP, and sensitive info.              |
| **Hide Match History**      | `Settings.Privacy.HideMatchHistory`   | OFF / ON                    | Prevent others from seeing recent matches.               |
| **Hide Loadouts**           | `Settings.Privacy.HideLoadouts`       | OFF / ON                    | Prevent others from seeing your weapon builds.           |
| **Anonymous Mode**          | `Settings.Privacy.AnonymousMode`      | OFF / ON                    | Replace name with "Player_123" in all modes.             |
| **Stat Tracking**           | `Settings.Privacy.StatTracking`       | Public / Friends Only / Private | Who can see your K/D, win rate, etc.                  |
| **Career Profile**          | `Settings.Privacy.CareerProfile`      | Public / Friends Only / Private | Who can view career progression.                      |
| **Recently Played With**    | `Settings.Privacy.RecentlyPlayed`     | Show / Hide                 | Display recent teammates in social menu.                 |

### **6.3 Matchmaking & Crossplay**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Crossplay**               | `Settings.Account.Crossplay`          | All Platforms / Console Only / OFF | Matchmaking with other platforms.                 |
| **Input-Based Matchmaking** | `Settings.Account.InputMatchmaking`   | OFF / ON                    | Prefer matching with same input method (KBM vs Controller).|
| **Preferred Squad Size**    | `Settings.Matchmaking.SquadSize`      | Solo / Duo / Trio / Squad (4) | Auto-fill preference.                              |
| **Fill Empty Slots**        | `Settings.Matchmaking.FillSlots`      | OFF / ON                    | Allow random teammates in squad.                         |
| **Skill-Based Matchmaking** | `Settings.Matchmaking.SBMM`           | Enabled / Disabled          | Match with similar skill players (if available).         |
| **Ping Limit**              | `Settings.Matchmaking.PingLimit`      | 50ms / 100ms / 150ms / 200ms / Unlimited | Maximum acceptable latency for matches.       |
| **Matchmaking Priority**    | `Settings.Matchmaking.Priority`       | Speed / Connection / Skill  | What to prioritize in queue.                             |
| **Beginner Protection**     | `Settings.Matchmaking.BeginnerProtect`| OFF / ON                    | Avoid matching new players with veterans.                |

### **6.4 Social & Friends**
| Setting                     | Gameplay Tag                       | Options                     | Description                                           |
| :-------------------------- | :--------------------------------- | :-------------------------- | :---------------------------------------------------- |
| **Friend Requests**         | `Settings.Social.FriendRequests`   | Everyone / Friends of Friends / Closed | Who can send you friend requests.          |
| **Party Invites**           | `Settings.Social.PartyInvites`     | Everyone / Friends Only / Closed | Who can invite you to groups.                    |
| **Join in Progress**        | `Settings.Social.JoinInProgress`   | Friends / Invite Only / OFF | Allow joining your active match.                      |
| **Friend Notifications**    | `Settings.Social.Notifications`    | All / Important / OFF       | Alerts when friends come online or invite you.        |
| **Friend Request Sound**    | `Settings.Social.RequestSound`     | OFF / ON                    | Audio alert for friend requests.                      |
| **Show Presence**           | `Settings.Social.ShowPresence`     | Detailed / Basic / OFF      | Let friends see what you're doing in-game.            |
| **Auto-Decline Invites**    | `Settings.Social.AutoDecline`      | OFF / When In Match / Always | Reject all invites when busy.                        |
| **Whisper Notifications**   | `Settings.Social.WhisperNotif`     | OFF / ON                    | Alert for private messages.                           |

### **6.5 Text Chat**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Text Chat**               | `Settings.Chat.Enabled`               | OFF / ON                    | Enable/disable text chat globally.                       |
| **Chat Channels**           | `Settings.Chat.Channels`              | All / Team Only / Party Only / OFF | Which chat channels to show.                      |
| **Chat Visibility**         | `Settings.Chat.Visibility`            | Always / On Key Press / Fade Out | When chat window displays.                        |
| **Chat Fade Time**          | `Settings.Chat.FadeTime`              | 3s / 5s / 10s / Never       | How long before chat fades.                              |
| **Chat Font Size**          | `Settings.Chat.FontSize`              | Small / Medium / Large      | Text size.                                               |
| **Chat Opacity**            | `Settings.Chat.Opacity`               | Slider (0 - 100%)           | Background transparency.                                 |
| **Profanity Filter**        | `Settings.Chat.ProfanityFilter`       | OFF / ON                    | Censor offensive language.                               |
| **Mute Enemy Chat**         | `Settings.Chat.MuteEnemies`           | OFF / ON                    | Block messages from opponents (proximity chat).          |
| **Chat Timestamps**         | `Settings.Chat.Timestamps`            | OFF / ON                    | Show message send times.                                 |
| **Emote Text Display**      | `Settings.Chat.EmoteText`             | OFF / ON                    | Show text description of emotes in chat.                 |
| **Link Preview**            | `Settings.Chat.LinkPreview`           | OFF / ON                    | Show preview of shared links.                            |

### **6.6 Notifications**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Push Notifications**      | `Settings.Notifications.Push`         | OFF / ON                    | System notifications when game closed (mobile/desktop).  |
| **In-Game Notifications**   | `Settings.Notifications.InGame`       | All / Critical / OFF        | Popups for events, rewards, friends.                     |
| **Toast Duration**          | `Settings.Notifications.ToastDuration`| Short (3s) / Medium (5s) / Long (8s) | How long notifications stay.                  |
| **Daily Rewards Reminder**  | `Settings.Notifications.DailyRewards` | OFF / ON                    | Alert for unclaimed daily login bonuses.                 |
| **Event Notifications**     | `Settings.Notifications.Events`       | OFF / ON                    | Notify about limited-time events and seasons.            |
| **Battle Pass Progress**    | `Settings.Notifications.BattlePass`   | OFF / ON                    | Notify when BP tier completed.                           |
| **Achievement Popups**      | `Settings.Notifications.Achievements` | OFF / ON                    | Show achievement unlock notifications.                   |

### **6.7 Language & Region**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Text Language**           | `Settings.Localization.TextLanguage`  | Select Language             | UI and subtitles.                                        |
| **Audio Language**          | `Settings.Localization.AudioLanguage` | Select Language / Match Text | Voice overs and dialogue.                               |
| **Time Format**             | `Settings.Localization.TimeFormat`    | 12-hour / 24-hour           | Clock display.                                           |
| **Date Format**             | `Settings.Localization.DateFormat`    | MM/DD/YYYY / DD/MM/YYYY / YYYY-MM-DD | Date display.                                 |
| **Number Format**           | `Settings.Localization.NumberFormat`  | 1,000.00 / 1.000,00 / etc.  | Decimal and thousand separators.                         |
| **Temperature Unit**        | `Settings.Localization.Temperature`   | Celsius / Fahrenheit        | (If environmental effects exist).                        |

### **6.8 Accessibility**
| Setting                     | Gameplay Tag                             | Options                     | Description                                           |
| :-------------------------- | :--------------------------------------- | :-------------------------- | :---------------------------------------------------- |
| **Colorblind Mode**         | `Settings.Accessibility.ColorblindMode`  | OFF / Protanopia / Deuteranopia / Tritanopia / Achromatopsia | Color vision support.     |
| **Colorblind Strength**     | `Settings.Accessibility.ColorblindStr`   | Slider (0 - 100%)           | Intensity of color correction.                        |
| **High Contrast Mode**      | `Settings.Accessibility.HighContrast`    | OFF / ON                    | Increase UI element visibility.                       |
| **Text Size**               | `Settings.Accessibility.TextSize`        | Small / Medium / Large / XL / XXL | Global UI text scaling.                         |
| **UI Scale**                | `Settings.Accessibility.UIScale`         | Slider (50 - 200%)          | Overall UI element scaling.                           |
| **Cursor Size**             | `Settings.Accessibility.CursorSize`      | Slider (50 - 200%)          | Menu cursor size (not aim crosshair).                 |
| **Cursor Color**            | `Settings.Accessibility.CursorColor`     | System / White / Yellow / Custom | Menu cursor color.                                |
| **Reduce Motion**           | `Settings.Accessibility.ReduceMotion`    | OFF / ON                    | Disable camera shake, head bob, screen effects.       |
| **Camera Shake**            | `Settings.Accessibility.CameraShake`     | Slider (0 - 100%)           | Intensity of weapon recoil shake.                     |
| **Head Bob**                | `Settings.Accessibility.HeadBob`         | Slider (0 - 100%)           | Walking/running camera sway.                          |
| **Screen Flash Reduction**  | `Settings.Accessibility.FlashReduction`  | OFF / ON                    | Reduce intensity of flashbangs, bright effects.       |
| **Button Mashing to Hold**  | `Settings.Accessibility.ButtonMash`      | OFF / ON                    | Convert rapid-tap actions to hold.                    |
| **Hold to Confirm**         | `Settings.Accessibility.HoldConfirm`     | OFF / ON                    | Require hold vs tap for important actions.            |
| **Assistive Aim**           | `Settings.Accessibility.AssistiveAim`    | OFF / ON                    | Enhanced aim assist for accessibility needs.          |
| **Auto-Ping Enemies**       | `Settings.Accessibility.AutoPing`        | OFF / ON                    | Automatically ping enemies you shoot.                 |
| **Simplified HUD**          | `Settings.Accessibility.SimplifiedHUD`   | OFF / ON                    | Remove non-essential UI elements.                     |
| **Navigation Assistance**   | `Settings.Accessibility.NavAssist`       | OFF / Waypoint / Full       | Help finding objectives/extraction.                   |

### **6.9 Performance & Diagnostics**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Network Diagnostics**     | `Settings.Performance.NetworkDiag`    | OFF / ON                    | Show detailed connection info.                           |
| **Client Performance**      | `Settings.Performance.ClientPerf`     | OFF / ON                    | CPU/GPU usage overlay.                                   |
| **Memory Usage Display**    | `Settings.Performance.MemoryDisplay`  | OFF / ON                    | Show RAM/VRAM usage.                                     |
| **Packet Loss Detection**   | `Settings.Performance.PacketLoss`     | OFF / ON                    | Alert on unstable connection.                            |
| **Auto-Adjust Quality**     | `Settings.Performance.AutoAdjust`     | OFF / ON                    | Dynamically lower settings to maintain FPS.              |
| **FPS Target**              | `Settings.Performance.FPSTarget`      | 30 / 60 / 90 / 120 / 144    | Auto-adjust aims for this framerate.                     |
| **Render Latency Mode**     | `Settings.Performance.RenderLatency`  | Low / Normal / Ultra Low    | CPU-GPU pipeline optimization (NVIDIA Reflex, etc).      |
| **Network Smoothing**       | `Settings.Performance.NetSmoothing`   | OFF / Low / Medium / High   | Interpolation for laggy connections.                     |
| **Tick Rate Display**       | `Settings.Performance.TickRate`       | OFF / ON                    | Show server tick rate.                                   |

### **6.10 Data & Telemetry**
| Setting                     | Gameplay Tag                          | Options                     | Description                                              |
| :-------------------------- | :------------------------------------ | :-------------------------- | :------------------------------------------------------- |
| **Telemetry**               | `Settings.Data.Telemetry`             | Full / Anonymous / OFF      | Share gameplay data for improvements.                    |
| **Crash Reporting**         | `Settings.Data.CrashReporting`        | OFF / ON                    | Send crash logs to developers.                           |
| **Personalized Ads**        | `Settings.Data.PersonalizedAds`       | OFF / ON                    | Use data for targeted advertising.                       |
| **Gameplay Recording**      | `Settings.Data.GameplayRecording`     | OFF / Highlights / Full     | Allow recording of gameplay for analysis.                |
| **Data Collection**         | `Settings.Data.Collection`            | Essential Only / All        | What data is collected.                                  |

---

## 🎯 7. ADVANCED & DEVELOPER SETTINGS

*Settings for power users, content creators, and testing.*

### **7.1 Keybindings & Macros**
| Setting                     | Gameplay Tag                          | Description                                                       |
| :-------------------------- | :------------------------------------ | :---------------------------------------------------------------- |
| **Custom Keybinds**         | `Settings.Advanced.Keybinds`          | Full rebinding of all actions with primary/secondary support.    |
| **Keybind Profiles**        | `Settings.Advanced.KeybindProfiles`   | Save/load different keybind configurations.                       |
| **Combo Keys**              | `Settings.Advanced.ComboKeys`         | Allow multi-key bindings (Ctrl+Shift+E).                          |
| **Macro Support**           | `Settings.Advanced.Macros`            | Record and playback input sequences (if allowed by anti-cheat).   |
| **Keybind Import/Export**   | `Settings.Advanced.KeybindExport`     | Share keybind configs via files.                                  |
| **On-Screen Keybind Help**  | `Settings.Advanced.KeybindHelp`       | Show what keys do in overlay.                                     |

### **7.2 Content Creation**
| Setting                     | Gameplay Tag                          | Options                     | Description                                           |
| :-------------------------- | :------------------------------------ | :-------------------------- | :---------------------------------------------------- |
| **Replay System**           | `Settings.Content.Replay`             | OFF / ON                    | Record matches for replay.                            |
| **Replay Quality**          | `Settings.Content.ReplayQuality`      | Low / Medium / High / Ultra | File size vs quality.                                 |
| **Replay Storage Limit**    | `Settings.Content.ReplayStorage`      | Slider (1-100 GB)           | Max disk space for replays.                           |
| **Auto-Record Highlights**  | `Settings.Content.AutoHighlights`     | OFF / ON                    | Automatically capture kills/objectives.               |
| **Screenshot Hotkey**       | `Settings.Content.ScreenshotKey`      | Keybind                     | Instant screenshot button.                            |
| **Screenshot Format**       | `Settings.Content.ScreenshotFormat`   | PNG / JPG / BMP             | File format and quality.                              |
| **Screenshot Resolution**   | `Settings.Content.ScreenshotRes`      | Native / 2x / 4K / 8K       | Capture at higher resolution than render.             |
| **Screenshot Location**     | `Settings.Content.ScreenshotLocation` | Folder Path                 | Where to save screenshots.                            |
| **Kill Cam Export**         | `Settings.Content.KillCamExport`      | OFF / ON                    | Save death cams as clips.                             |
| **Video Recording**         | `Settings.Content.VideoRecording`     | OFF / Manual / Auto         | Built-in video capture.                               |
| **Recording Bitrate**       | `Settings.Content.RecordingBitrate`   | Slider (5-100 Mbps)         | Video quality.                                        |
| **Recording Audio**         | `Settings.Content.RecordingAudio`     | Game / Game+Mic / All       | What audio to capture.                                |

### **7.3 Debug & Testing**
| Setting                     | Gameplay Tag                          | Options                     | Description                                           |
| :-------------------------- | :------------------------------------ | :-------------------------- | :---------------------------------------------------- |
| **Show Debug Info**         | `Settings.Debug.ShowDebugInfo`        | OFF / ON                    | Display dev info overlay (coords, velocity).          |
| **Hitbox Visualization**    | `Settings.Debug.Hitboxes`             | OFF / ON                    | Render hitboxes and hurtboxes (if enabled).           |
| **Network Graph**           | `Settings.Debug.NetworkGraph`         | OFF / Simple / Detailed     | Real-time packet flow visualization.                  |
| **Console Access**          | `Settings.Debug.Console`              | OFF / ON                    | Enable developer console.                             |
| **Console Key**             | `Settings.Debug.ConsoleKey`           | Keybind                     | Button to open console.                               |
| **Show FPS Graph**          | `Settings.Debug.FPSGraph`             | OFF / ON                    | Frametime graph overlay.                              |
| **Bot Matches**             | `Settings.Debug.BotMatches`           | OFF / ON                    | Practice against AI (if available).                   |
| **God Mode**                | `Settings.Debug.GodMode`              | OFF / ON                    | Invincibility (testing only).                         |
| **Noclip**                  | `Settings.Debug.Noclip`               | OFF / ON                    | Fly through walls (testing only).                     |

---

## 📋 SETTING PRESETS & PROFILES

### **Competitive Preset**
Optimized for maximum performance and competitive advantage:
- Graphics: Low-Medium (view distance High, shadows OFF)
- FPS Limit: Unlimited
- Motion Blur: OFF
- Depth of Field: OFF
- FOV: 90-100
- All performance overlays: ON

### **Immersive Preset**
Balanced graphics for story/casual play:
- Graphics: High-Ultra
- Ray Tracing: ON (if supported)
- Music: Medium
- Cinematic effects: ON

### **Battery Saver (Mobile/Laptop)**
Extends battery life:
- Graphics: Low
- FPS: 30-60 cap
- Reduced particle effects
- Lower audio quality

### **Streamer Preset**
Optimized for content creation:
- Streamer Mode: ON
- High graphics but stable FPS
- Optimal audio mix for stream
- Replay system: ON

---

## 🔧 IMPLEMENTATION NOTES

### **Cloud Sync & Conflict Resolution**
- All settings sync across devices via user account
- Last-write-wins for simple settings
- Platform-specific settings stored separately (mobile HUD layout doesn't override PC keybinds)
- Conflict resolution prompt on login if settings changed on multiple devices

### **Competitive Integrity Locks**
Certain settings may be locked in ranked/competitive modes:
- FOV capped at 110
- Forced enemy outlines ON
- Motion blur forced OFF
- Minimum graphics quality enforced
- Certain accessibility features allowed

### **Performance Profiling**
Settings system should detect hardware and recommend preset:
- **Low-End** (GTX 1050 / mobile): Low preset, 60 FPS target
- **Mid-Range** (RTX 2060 / console): Medium-High, 90-120 FPS
- **High-End** (RTX 4070+): Ultra, 144+ FPS
- **Competitive**: Performance preset regardless of hardware

### **Accessibility & Regulations**
- CVAA compliance for subtitles and colorblind options
- COPPA compliance for users under 13
- GDPR compliance for data collection toggles
- Photosensitivity warnings for high-contrast modes
- WCAG 2.1 AA compliance for UI

### **Version Control**
- Settings version number tracked
- Migration system for deprecated settings
- Default value changes announced in patch notes
- Backup settings before major updates

### **Platform-Specific Considerations**
- **PC**: Full keybind customization, raw input, uncapped FPS
- **Console**: Controller focus, aim assist by default, 60/120 FPS modes
- **Mobile**: Touch layout customization, battery saver mode, auto-quality
- **Cloud Gaming**: Input latency compensation, bandwidth-aware quality

### **Anti-Cheat Integration**
- Certain settings monitored for exploits
- Macros may be restricted or require approval
- Debug settings disabled in competitive modes
- Settings hash validation

---

## 📊 COMPARISON: EXTRACTION SHOOTER STANDARDS

### **Settings from Escape from Tarkov**
- ✅ Per-scope sensitivity
- ✅ Head bobbing control
- ✅ Sound occlusion
- ✅ Compression/dynamic range
- ✅ Network diagnostics

### **Settings from Hunt: Showdown**
- ✅ Audio occlusion quality
- ✅ Separate boss audio
- ✅ Spatial audio (Binaural)
- ✅ Dark sight FOV

### **Settings from The Cycle: Frontier**
- ✅ Ping system customization
- ✅ Storm intensity
- ✅ Loot rarity filters
- ✅ Extraction timer display

### **Settings from Apex Legends (Hero Shooter)**
- ✅ Per-legend settings
- ✅ Ability hints
- ✅ Ping wheel customization
- ✅ Colorblind mode with strength
- ✅ Damage number styles

---

## 🔗 RELATED DOCUMENTATION
- [Technical Implementation: Settings System](../../GDD_Technical/Systems/SettingsSystem.md)
- [UI/UX Design Guide](../../GDD_UI/UIDesignPhilosophy.md)
- [Input System Architecture](../../GDD_Technical/Systems/InputSystem.md)
- [Accessibility Standards](../../GDD_Design/AccessibilityGuidelines.md)
- [Competitive Integrity Rules](../../GDD_Design/CompetitiveBalance.md)
- [Hero Design Documentation](../../GDD_Design/HeroDesign.md)
- [Network Architecture](../../GDD_Technical/Systems/NetworkingSystem.md)

---

**Document Version:** 2.0
**Last Updated:** [Current Date]
**Contributors:** Game Design Team, UX Team, Engineering Team
**Status:** Enhanced - Ready for Implementation

**Change Log:**
- v2.0: Complete overhaul with hero-specific settings, advanced accessibility, crossplatform features, extraction-focused UI, competitive integrity options
- v1.0: Initial settings documentation
