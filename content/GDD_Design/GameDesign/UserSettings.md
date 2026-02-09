---
title: "User Settings & Configuration"
type: docs
---

## ⚙️ Design Philosophy

**"Power to the Player, Simplicity for the Casual."**
Settings should offer granular control for competitive players while providing simple, intelligent presets for casual users. All settings must be **saved to the cloud** and synced across devices.

---

## 🎮 1. Control Settings (Input)

### General Input
| Setting | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **Sensitivity** | Slider (0.1 - 5.0) | 1.0 | Global mouse/touch sensitivity. |
| **ADS Sensitivity** | Slider (0.1 - 2.0) | 0.8 | Sensitivity multiplier when Aiming Down Sights. |
| **Scope Sensitivity** | Slider (0.1 - 2.0) | 0.6 | Multiplier for high-zoom scopes (>4x). |
| **Invert Look** | Toggle | OFF | Invert Y-axis. |
| **Vibration** | Toggle | ON | Haptic feedback for shooting/damage. |

### Movement & Combat (Advanced)
| Setting | Option | Default | Description |
| :--- | :--- | :--- | :--- |
| **Crouch Mode** | Hold / Toggle | Toggle | "Hold" requires keeping the key pressed. "Toggle" switches state on press. |
| **Prone Mode** | Hold / Toggle | Toggle | Separate keybind available. Same logic as Crouch. |
| **Sprint Mode** | Hold / Toggle | Toggle | "Hold" stops sprinting on release. "Toggle" keeps sprinting until stop. |
| **Tactical Sprint** | Single Tap / Double Tap | Double Tap | Engage super-sprint (weapon up, slower fire time). |
| **Walk Mode** | Hold / Toggle | Hold | Silent movement modifier. Reduces noise by 60%. |
| **Lean Mode** | Hold / Toggle / Auto | Hold | Peek around corners. "Auto" leans when near edge and aiming. |
| **Auto-Lean** | ON / OFF | OFF | Automatically lean when aiming near a corner. |
| **Aim Mode** | Hold / Toggle | Hold | Aiming Down Sights (ADS) behavior. |
| **ADS Transition** | Smooth / Instant | Smooth | "Smooth" blends animation (realistic). "Instant" snaps view (competitive). |
| **Auto-Sprint** | OFF / Normal / Tactical | OFF | Automatically sprint when moving forward without holding Shift. |
| **Quick Throw** | ON / OFF | ON | Grenade throws immediately on key press. OFF = Hold to aim arc. |
| **Bolt Action Mode** | Release / Manual | Release | "Release" cycles bolt on key release. "Manual" requires extra click. |

### Controller / Mobile Specific
| Setting | Option | Default | Description |
| :--- | :--- | :--- | :--- |
| **Gyro Aiming** | OFF / Scope / Always | Scope | Use device tilt for fine adjustments. |
| **Gyro Sensitivity** | Slider (1-300%) | 100% | Separate X/Y axis sliders. |
| **Aim Assist** | Standard / Precision / Focusing | Standard | "Standard" slows near target. "Precision" slows only on hitbox. |
| **Aim Response Curve** | Standard / Linear / Dynamic | Standard | Input curve mapping. |
| **Stick Deadzone** | Slider (0.00 - 0.50) | 0.10 | Min input to register movement (fixes drift). |
| **Automations** | Auto-Loot / Auto-Open Doors | ON | Mobile QoL features. |

### Key Bindings & Input Mapping (PC Default)

**System:** Supports Primary and Secondary bindings for all actions.

#### Movement
| Action | Primary | Secondary | Context |
| :--- | :--- | :--- | :--- |
| **Move Forward** | `W` | | |
| **Move Backward** | `S` | | |
| **Move Left** | `A` | | |
| **Move Right** | `D` | | |
| **Jump / Vault** | `Space` | | Vaults if near obstacle. |
| **Sprint / Tac Sprint** | `L-Shift` | | Double-tap for Tac Sprint. |
| **Crouch / Slide** | `C` | `L-Ctrl` | Slide if sprinting. |
| **Prone** | `Z` | | Go prone instantly. |
| **Walk (Slow)** | `Caps Lock` | | Toggle silent walking. |
| **Lean Left** | `Q` | | |
| **Lean Right** | `E` | | |

#### Combat
| Action | Primary | Secondary | Context |
| :--- | :--- | :--- | :--- |
| **Fire** | `L-Click` | | |
| **Aim Down Sights** | `R-Click` | | |
| **Reload** | `R` | | Double-tap R for Fast Reload (Drop mag). |
| **Next Weapon** | `Wheel Up` | `1` | |
| **Prev Weapon** | `Wheel Down` | `2` | |
| **Equip Primary** | `1` | | |
| **Equip Secondary** | `2` | | |
| **Equip Melee** | `3` | | |
| **Equip Throwable** | `4` | `G` | |
| **Melee Attack** | `V` | | Quick melee strike. |
| **Fire Mode** | `B` | | Auto / Single / Burst. |
| **Check Ammo (Hud)** | `T` | `Alt+T` | Visual check of mag. |
| **Inspect Weapon** | `L` | | Cool animation. |

#### Interactions
| Action | Primary | Secondary | Context |
| :--- | :--- | :--- | :--- |
| **Interact / Use** | `F` | | Open door, Loot container. |
| **Secondary Interact** | `H` | | Check door lock, Place marker. |
| **Inventory** | `Tab` | `I` | Open Tetris grid. |
| **Map** | `M` | | Open Full Map. |
| **Flashlight / Laser** | `T` | | Toggle attachment. |
| **Night Vision** | `N` | | Toggle NVG (If equipped). |
| **Hold Breath** | `L-Shift` | | While ADS only. |

#### Communication & UI
| Action | Primary | Secondary | Context |
| :--- | :--- | :--- | :--- |
| **Ping / Mark** | `Middle Mouse` | `Z` | Ping location. Double tap for Danger. |
| **Push to Talk** | `Y` | | VoIP. |
| **Chat Wheel** | `J` | | Quick comms (Need Ammo, Help). |
| **Text Chat** | `Enter` | | |
| **Vote Yes** | `F1` | | |
| **Vote No** | `F2` | | |
| **Screenshot** | `F12` | | |

### 🛠️ Engine Headers (Input)
*From `SettingsWidget.h`*

#### Input Configuration
| Setting Name | Options | Description |
| :--- | :--- | :--- |
| **Input Method** | Automatic, Touch, KBM, Gamepad, Gyro | Preferred input device or detection mode. |
| **Reference Frame** | Camera, World, Character | Determines if "Up" is relative to View, North, or Character. |
| **Touch Mode** | Touchpad, Virtual Joystick | **(Mobile)** Look via swiping anywhere or using a stick. |
| **Look Response Curve** | Float (0.5 to 2.0) | Adjusts the acceleration profile of camera movement. |

#### Sensitivity Ranges
| Setting Name | Range | Description |
| :--- | :--- | :--- |
| **Mouse Sensitivity** | X/Y Float Sliders | Accuracy and speed of mouse-driven look. |
| **Gamepad Sensitivity**| X/Y Float Sliders | Rotation speed when using controller thumbsticks. |
| **Touch Joystick Sens.**| X/Y Float Sliders | Sensitivity of the virtual movement/look stick. |
| **Touch Swipe Sens.** | X/Y Float Sliders | Sensitivity of screen-drag look gestures. |

#### Aiming & Behavior
| Setting Name | Options | Description |
| :--- | :--- | :--- |
| **Aim Assist** | Boolean (On/Off) | Toggles sticky/magnetic targeting for controllers. |
| **Gyro Aiming** | Boolean (On/Off) | Enables camera control via device rotation. |
| **Toggle ADS** | Boolean (True=Toggle, False=Hold) | Determines if Aiming-Down-Sights requires holding a button. |
| **Facing Behavior** | Face Aim, Face Movement | Does the character face the reticle or move direction? |
| **Aim Constraint** | None, Clamped Radius, Screen Edge | Limits cursor movement relative to the character. |
| **Max Aim Radius** | Float | Maximum distance the cursor can move from center. |
| **Min Aim Radius** | Float | Minimum "deadzone" for cursor placement. |

---

## 🖥️ 2. Graphics Settings (Visuals)

### Display
*   **Window Mode:** Fullscreen / Borderless / Windowed.
*   **NVIDIA Reflex:** OFF / ON / ON+BOOST (Reduces input latency).
*   **V-Sync:** OFF (Competitive) / ON.
*   **Frame Rate Limit:** Lobby (60), Game (Unlocked/144/240).

### Upscaling & Sharpening
| Setting | Options | Description |
| :--- | :--- | :--- |
| **Upscaling** | DLSS / FSR / XeSS / OFF | Resolution scaling for FPS. |
| **Quality Mode** | Performance / Balanced / Quality | | "Performance" renders lower internal res. "Quality" aims for native. |
| **Sharpening** | Slider (0 - 100) | | Contrast Adaptive Sharpening (CAS) intensity. |

### Detailed Quality
| Setting | Level (Low-Ultra) | Cost | Description |
| :--- | :--- | :--- | :--- |
| **Texture Quality** | Low - Ultra | VRAM | Surface detail. |
| **Texture Filtering** | Bilinear - Anisotropic 16x | GPU | Texture clarity at angles. |
| **LOD Quality** | 1.0 - 2.5 | CPU | Distance objects degrade to low-poly. Critical for spotting enemies. |
| **Shadow Quality** | Low - Ultra | GPU | "Low" removes dynamic shadows on small props. |
| **Contact Shadows** | ON / OFF | GPU | Small shadows on ground details. |
| **Global Illumination** | SSGI / Lumen (High) | GPU | HBAO/SSAO alternatives. |
| **Reflections** | Screen Space / Ray Traced | GPU | SSR is standard. RT is heavy. |
| **Volumetric Fog** | Low / Medium / High | GPU | "Low" improves visibility in fog. |
| **Particles** | Low / High | CPU | Sparks, debris. "Low" recommended for FPS. |
| **Foliage Density** | Low / High | CPU | *Competitive Rule:* Grass renders at same distance for all, but "High" makes it thicker. |
| **Distortion** | OFF / ON | GPU | Heat haze, explosion shockwaves. |

### Post-Processing (Visibility)
| Setting | Option | Description |
| :--- | :--- | :--- |
| **Motion Blur** | OFF / ON | *Always OFF* for competitive. |
| **Depth of Field** | OFF / ON | Blurs weapon/background when aiming. OFF recommended. |
| **Film Grain** | Slider (0.0 - 1.0) | Visual noise. Set to 0.0. |
| **Chromatic Aberration** | OFF / ON | Color fringing at screen edges. OFF for clarity. |
| **Bloom** | OFF / ON | Glowing lights. OFF reduces glare. |

### Color & Accessibility
| Setting | Options | Description |
| :--- | :--- | :--- | :--- |
| **Colorblind Mode** | Protanopia / Deuteranopia / Tritanopia | Adjusts UI colors (Enemy Red -> Orange). |
| **Brightness** | Slider | Gamma correction. |
| **Motion Blur** | OFF / ON | Strength of blur during camera movement. |
| **Field of View (FOV)** | 60 - 110 | Horizontal FOV. (Mobile capped at 90). |

### 🛠️ Engine Headers (Graphics)
*From `UGameUserSettings`*

| Setting Name | Options / Range | Description |
| :--- | :--- | :--- |
| **Screen Resolution** | List of FIntPoint (e.g., 1920x1080) | Sets the display resolution. |
| **Fullscreen Mode** | 0: Fullscreen, 1: Windowed Fullscreen, 2: Windowed | Controls how the game window occupies the screen. |
| **VSync** | Boolean (On/Off) | Synchronizes frame rate with monitor refresh rate to prevent tearing. |
| **Dynamic Resolution** | Boolean (On/Off) | Automatically scales resolution to Maintain target FPS. |
| **Frame Rate Limit** | Float (0 = Unlimited) | Caps the maximum FPS. |
| **Overall Quality** | 0: Low, 1: Medium, 2: High, 3: Epic, 4: Cinematic | Quickly applies a quality preset to all scalability settings. |
| **Resolution Scale** | Float (0.0 - 100.0) | Adjusts the internal rendering resolution. |
| **View Distance Quality**| 0 - 4 (Low to Cinematic) | Controls the culling distance for 3D objects. |
| **Shadow Quality** | 0 - 4 (Low to Cinematic) | Adjusts the resolution and filtering of shadows. |
| **Global Illumination** | 0 - 4 (Low to Cinematic) | Controls the quality of indirect lighting (e.g., Lumen). |
| **Reflection Quality** | 0 - 4 (Low to Cinematic) | Adjusts the quality and method of reflections. |
| **Anti-Aliasing** | 0 - 4 (Low to Cinematic) | Reduces jagged edges on geometry. |
| **Texture Quality** | 0 - 4 (Low to Cinematic) | Controls the resolution of textures loaded into memory. |
| **Visual Effects (VFX)** | 0 - 4 (Low to Cinematic) | Adjusts particle counts and shader complexity for effects. |
| **Post-Processing** | 0 - 4 (Low to Cinematic) | Quality of screen-space effects (Bloom, AO, DOF). |
| **Foliage Quality** | 0 - 4 (Low to Cinematic) | Controls the density and LODs of trees and grass. |
| **Shading Quality** | 0 - 4 (Low to Cinematic) | Adjusts material shader complexity. |
| **HDR Output** | Boolean (On/Off) | Enables High Dynamic Range output on supported displays. |
| **HDR Display Nits** | Integer (Default: 1000) | Sets peak brightness level for HDR calibration. |

---

## 🔊 3. Audio Settings (Sound)

### Advanced Mix
| Setting | Option | Default | Description |
| :--- | :--- | :--- | :--- |
| **Dynamic Range** | Hi-Fi / Night Mode / TV | Hi-Fi | "Night Mode" compresses loud sounds (explosions) to make footsteps clearer. |
| **EQ Preset** | Flat / Bass Boost / Treble Boost | Flat | "Treble Boost" highlights footsteps. |
| **Binaural Audio** | ON / OFF | ON | Advanced HRTF algorithm (Steam Audio / Oculus). |
| **Sound Lock** | ON / OFF | OFF | Hard limiter preventing sounds over X decibels. |
| **Mute on Focus Loss** | ON / OFF | ON | Mute game when Alt-Tabbed. |

### Volume Mixers
| Channel | Range | Description |
| :--- | :--- | :--- |
| **Master Volume** | 0 - 100% | Global output volume for all sounds. |
| **Music (Menu)** | 0 - 100% | Volume of music in Main Menu, Loading Screens, and Stash. |
| **Music (Raid)** | 0 - 100% | *Warning:* Music clips can mask footsteps. Recommended 0% for competitive. |
| **SFX (Gunshot)** | 0 - 100% | Volume of firing sounds (yours and enemies). |
| **SFX (Footsteps)** | 0 - 100% | Volume of movement sounds. *Competitive:* Keep this maxed. |
| **UI Volume** | 0 - 100% | Volume of clicks, hover effects, and inventory interactions. |
| **Voice Chat** | 0 - 100% | Volume of incoming teammate voice communication. |
| **Ambient** | 0 - 100% | Volume of wind, rain, birds, and room tones. |

### Voice Chat (VoIP)
*   **Mode:** Push-to-Talk / Open Mic / Mute.
*   **Input Device:** Select microphone.
*   **Output Device:** Select headset/speakers.

### 🛠️ Engine Headers (Audio)
*From `UAdvancedGameSettings`*

| Setting Name | Options / Range | Description |
| :--- | :--- | :--- |
| **Master Volume** | Slider (0.0 - 1.0) | Global volume multiplier for the entire game. |
| **Music Volume** | Slider (0.0 - 1.0) | Multiplier for the Music sound class. |
| **SFX Volume** | Slider (0.0 - 1.0) | Multiplier for Sound Effects (SFX) sound class. |
| **Audio Quality Level** | Integer (0 - 3) | Controls resource allocation for the audio engine. |
| **Enable Vibration** | Boolean (On/Off) | Toggles haptic feedback on supported controllers/devices. |

---

## 📡 4. Gameplay & Interface (HUD)

### Crosshair Customization (Valorant Style)
| Setting | Option | Description |
| :--- | :--- | :--- |
| **Show Crosshair** | ON / OFF | Master toggle for crosshair visibility. |
| **Style** | Cross / Dot / Circle | Base shape of the reticle. |
| **Color** | RGB Slider | Green/Cyan recommended for contrast. |
| **Center Dot** | ON / OFF, Opacity | Small pixel dot in exact screen center. |
| **Outlines** | ON / OFF, Thickness | Black outline improves visibility on bright backgrounds (snow/sky). |
| **Dynamic** | ON / OFF | Crosshair expands when moving/firing to show Accuracy/Firing Error. |

### Interactive Objects (Loot)
| Setting | Option | Default | Description |
| :--- | :--- | :--- | :--- |
| **Double Click** | Use / Inspect / Take | Use | Action performed when double-clicking an item in stash. |
| **Quick Slots** | Always Show / Auto-Hide | Always | Visibility of hotbar (4-9) at bottom of screen. |
| **Highlight Loot** | ON / OFF | ON | Renders a colored outline around loose loot on the ground. |
| **Auto-Sort Stash** | ON / OFF | OFF | Automatically arranges stash items (Tetris) to maximize space. |

### HUD Elements
| Setting | Options | Description |
| :--- | :--- | :--- |
| **Health Bar** | Always / Dynamic / Polychrome | "Dynamic" hides when full. "Polychrome" changes color (Green->Red) with damage. |
| **Stamina Bar** | Always / Dynamic | "Dynamic" auto-hides when stamina is > 90%. |
| **Compass** | Top Bar / Minimap / OFF | Location aid. "Top Bar" shows 360 bearing tape. |
| **Damage Numbers** | OFF / Stacked / Floating | "Stacked" combines numbers (15..30..45). "Floating" shows individual hits. |
| **Kill Feed** | Full / Icons / OFF | Notifications when players die. "Icons" shows Weapon + Name. |

---

## 💾 5. Account & Privacy

*   **Streamer Mode:** Hides your name ("Player123") and server IP. Delays matchmaking status.
*   **Crossplay:** ON / OFF (Console only).
*   **Data Center:** Auto / Select Region (e.g., Asia, NA-West).
*   **Delete Account:** GDPR compliance link.


