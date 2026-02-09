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
| Setting | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **Input Method** | Auto / KBM / Gamepad / Touch | Automatic | Preferred input device or detection mode. |
| **Sensitivity** | Slider (0.1 - 5.0) | 1.0 | Global mouse/touch sensitivity. |
| **ADS Sensitivity** | Slider (0.1 - 2.0) | 0.8 | Sensitivity multiplier when Aiming Down Sights. |
| **Scope Sensitivity** | Slider (0.1 - 2.0) | 0.6 | Multiplier for high-zoom scopes (>4x). |
| **Invert Look** | Toggle | OFF | Invert Y-axis. |
| **Look Response Curve** | Standard / Linear / Dynamic | Standard | Input curve mapping. |

### **Movement & Combat Behaviors**
| Setting | Option | Default | Description |
| :--- | :--- | :--- | :--- |
| **Crouch Mode** | Hold / Toggle | Toggle | "Hold" requires keeping the key pressed. |
| **Prone Mode** | Hold / Toggle | Toggle | Separate keybind available. |
| **Sprint Mode** | Hold / Toggle | Toggle | "Hold" stops sprinting on release. |
| **Tactical Sprint** | Single Tap / Double Tap | Double Tap | Engage super-sprint (weapon up, slower fire time). |
| **Walk Mode** | Hold / Toggle | Hold | Silent movement modifier. |
| **Lean Mode** | Hold / Toggle / Auto | Hold | Peek around corners. "Auto" leans when near edge. |
| **Aim Mode** | Hold / Toggle | Hold | Aiming Down Sights (ADS) behavior. |
| **ADS Transition** | Smooth / Instant | Smooth | "Smooth" blends animation (realistic). "Instant" snaps view. |
| **Quick Throw** | ON / OFF | ON | Grenade throws immediately on key press. |
| **Bolt Action Mode** | Release / Manual | Release | "Release" cycles bolt on key release. |

### **Controller & Mobile Specific**
| Setting | Option | Default | Description |
| :--- | :--- | :--- | :--- |
| **Vibration** | Toggle | ON | Haptic feedback for shooting/damage. |
| **Aim Assist** | Standard / Precision / Focusing | Standard | "Standard" slows near target. |
| **Stick Deadzone** | Slider (0.00 - 0.50) | 0.10 | Min input to register movement (fixes drift). |
| **Gyro Aiming** | OFF / Scope / Always | Scope | Use device tilt for fine adjustments. |
| **Gyro Sensitivity** | Slider (1-300%) | 100% | Separate X/Y axis sliders. |
| **Touch Mode** | Touchpad / Virtual Joystick | Joystick | **(Mobile)** Look via swiping or virtual stick. |
| **Automations** | Auto-Loot / Auto-Open Doors | ON | Mobile QoL features. |

### **Key Bindings (PC Default)**
*System support for Primary and Secondary bindings.*

#### **Movement**
| Action | Primary | Secondary | Context |
| :--- | :--- | :--- | :--- |
| **Move** | `W`,`A`,`S`,`D` | | |
| **Jump / Vault** | `Space` | | Vaults if near obstacle. |
| **Sprint** | `L-Shift` | | Double-tap for Tac Sprint. |
| **Crouch / Slide** | `C` | `L-Ctrl` | Slide if sprinting. |
| **Prone** | `Z` | | Go prone instantly. |
| **Walk (Slow)** | `Caps Lock` | | Toggle silent walking. |
| **Lean Left/Right** | `Q`, `E` | | |

#### **Combat**
| Action | Primary | Secondary | Context |
| :--- | :--- | :--- | :--- |
| **Fire** | `L-Click` | | |
| **Aim Down Sights** | `R-Click` | | |
| **Reload** | `R` | | Double-tap for Fast Reload. |
| **Weapon Swap** | `1`-`4` / `Scroll` | | Primary, Secondary, Melee, Utility. |
| **Melee** | `V` | | Quick melee strike. |
| **Fire Mode** | `B` | | Auto / Single / Burst. |
| **Interaction** | `F` | | Use / Loot / Revive. |

#### **Communication**
| Action | Primary | Secondary | Context |
| :--- | :--- | :--- | :--- |
| **Ping** | `Middle Mouse` | `Z` | Double tap for Danger. |
| **Push to Talk** | `Y` | | VoIP. |
| **Map** | `M` | | |
| **Inventory** | `Tab` | `I` | |

---

## 🖥️ 2. Graphics Settings (Visuals)

*Widgets arranged from core display settings to fine-tuning.*

### **Display & Performance**
| Setting | Options | Description |
| :--- | :--- | :--- |
| **Window Mode** | Fullscreen / Borderless / Windowed | Controls how the game window occupies the screen. |
| **Screen Resolution** | 1920x1080, 2560x1440, etc. | Native resolution of the display. |
| **Resolution Scale** | 0.0 - 100.0 | Internal rendering resolution (supersampling or downscaling). |
| **V-Sync** | OFF / ON | Synchronizes frame rate with monitor to prevent tearing. |
| **Frame Rate Limit** | Lobby (60), Game (Unlocked) | Caps maximum FPS to save power or stabilize frame times. |
| **NVIDIA Reflex** | OFF / ON / ON+BOOST | Low latency mode for competitive input. |

### **Upscaling & Quality**
| Setting | Options | Description |
| :--- | :--- | :--- |
| **Overall Quality** | Low / Medium / High / Epic | Master preset affecting all detail settings below. |
| **Upscaling** | DLSS / FSR / XeSS / OFF | AI reconstruction for higher FPS. |
| **Quality Mode** | Performance / Balanced / Quality | "Performance" renders lower internal res. |
| **Sharpening** | Slider (0 - 100) | Contrast Adaptive Sharpening (CAS) intensity. |

### **Detailed Environment**
| Setting | Option (Low-Ultra) | Impact | Description |
| :--- | :--- | :--- | :--- |
| **View Distance** | Low - Cinematic | CPU | Culling distance for objects/players. **Critical**. |
| **Shadow Quality** | Low - Cinematic | GPU | "Low" removes dynamic shadows on small props. |
| **Texture Quality** | Low - Cinematic | VRAM | Surface detail resolution. |
| **Anti-Aliasing** | Low - Cinematic | GPU | Edge smoothing method (TAA, FXAA). |
| **Post-Processing** | Low - Cinematic | GPU | Bloom, Ambient Occlusion, Depth of Field quality. |
| **Visual Effects** | Low - Cinematic | CPU | Particle density (sparks, smoke, debris). |
| **Foliage Quality** | Low - Cinematic | CPU | Density of grass/bushes. Does not affect hitboxes. |
| **Global Illumination** | SSGI / Lumen | GPU | Indirect lighting quality. |
| **Reflections** | Screen Space / Ray Traced | GPU | SSR is standard. RT is heavy. |

### **Visibility & Accessibility**
| Setting | Option | Description |
| :--- | :--- | :--- |
| **Field of View (FOV)** | 60 - 110 | Horizontal FOV. (Mobile capped at 90). |
| **Motion Blur** | OFF / ON | *Always OFF* for competitive. |
| **Chromatic Aberration**| OFF / ON | Color fringing at screen edges. OFF recommended for clarity. |
| **Film Grain** | Slider (0.0 - 1.0) | Visual noise. |
| **Colorblind Mode** | Protanopia / Deuteranopia / Tritanopia | Adjusts UI/Enemy colors for visibility. |
| **Brightness/HDR** | Slider | Gamma or Nits calibration. |

---

## 🔊 3. Audio Settings (Sound)

*Widgets arranged by mixer importance.*

### **Volume Mixer**
| Setting | Range | Description |
| :--- | :--- | :--- |
| **Master Volume** | 0 - 100% | Global output volume. |
| **SFX Volume** | 0 - 100% | **Critical:** Footsteps, gunshots, reloads. |
| **Voice Chat** | 0 - 100% | Volume of incoming teammate comms. |
| **UI Volume** | 0 - 100% | Clicks, inventory sounds, notifications. |
| **Music (Raid)** | 0 - 100% | In-game music. Recommended Low/OFF for competitive. |
| **Music (Menu)** | 0 - 100% | Menu ambience. |
| **Ambient** | 0 - 100% | Wind, rain, room tone. |

### **Voice Chat (VoIP)**
| Setting | Option | Description |
| :--- | :--- | :--- |
| **Mode** | Push-to-Talk / Open Mic / Mute | Activation method. |
| **Input Device** | System Default / Microphone X | Hardware Selection. |
| **Output Device** | System Default / Headset X | Hardware Selection. |

### **Advanced Audio**
| Setting | Option | Description |
| :--- | :--- | :--- |
| **Dynamic Range** | Hi-Fi / Night Mode / TV | "Night Mode" compresses loud sounds (explosions) to save ears. |
| **EQ Preset** | Flat / Bass Boost / Treble Boost | "Treble Boost" highlights footsteps. |
| **Binaural Audio** | ON / OFF | Advanced HRTF (Spatial Audio) for directional accuracy. |
| **Sound Lock** | ON / OFF | Hard limiter to prevent hearing damage from spikes. |
| **Mute on Focus Loss** | ON / OFF | Mute game when Alt-Tabbed. |

---

## 📡 4. Gameplay & Interface (HUD)

*Widgets arranged by HUD customization and account privacy.*

### **HUD & Interface**
| Setting | Option | Description |
| :--- | :--- | :--- |
| **Crosshair Style** | Cross / Dot / Circle | Base shape of the reticle. |
| **Crosshair Color** | RGB Slider | High contrast color recommended. |
| **Damage Numbers** | OFF / Stacked / Floating | "Stacked" combines numbers (15..30..45). |
| **Kill Feed** | Full / Icons / OFF | Notifications when players die. |
| **Health Bar** | Always / Dynamic | "Dynamic" hides when full. |
| **Compass** | Top Bar / Minimap / OFF | Directional aid. |

### **Interaction & Loot**
| Setting | Option | Description |
| :--- | :--- | :--- |
| **Highlight Loot** | ON / OFF | Colored outline around loose loot. |
| **Quick Slots** | Always Show / Auto-Hide | Visibility of hotbar (4-9). |
| **Auto-Sort Stash** | ON / OFF | Automatically arranges items (Tetris). |
| **Double Click Action** | Use / Inspect / Take | Default action for inventory items. |

### **Account & Privacy**
| Setting | Option | Description |
| :--- | :--- | :--- |
| **Streamer Mode** | ON / OFF | Hides names ("Player123") and server IP. |
| **Data Center** | Auto / Region Select | Preferred server location. |
| **Crossplay** | ON / OFF | Matchmaking with other platforms (Console only). |
| **Language** | Select Language | Text and Audio localization. |

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
