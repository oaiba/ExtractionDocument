---
title: "Control System - Design & Experience"
type: docs
---

##  Design Philosophy

The control system is the bridge between the player's intent and the game's action. Our core philosophy for controls is **"Fluidity First."**

- **Responsiveness**: Input latency must be imperceptible. Every button press should result in an immediate visual and auditory feedback.
- **Predictability**: The character should never do something the player didn't intend. Movement momentum should feel weighty but controllable.
- **Accessibility**: The game must be playable by everyone, regardless of platform or physical ability.
- **Platform Native**: Controls should not feel "ported." Mobile controls should feel like a native mobile game, and PC controls like a native PC shooter.

### Game Feel Goals (The "Why")
To ensure our controls deliver on the **High-Stakes Tension** pillar:

1.  **Crunchy Combat**: Firing a weapon must feel impactful.
    *   *Visuals*: Debris, sparks, and enemy flinch reactions are mandatory.
    *   *Input*: Recoil should require active management, not just be a static spread.
    *   *Audio*: Gunshots need environmental reverb (indoor vs. outdoor).

2.  **Weighty Movement**:
    *   *Inertia*: Movement has micro-acceleration/deceleration. It's not instant.
    *   *Momentum*: Sliding preserves speed; jumping from a sprint carries it.
    *   *Grounding*: Camera bob and footstep audio must sync perfectly.

---

##  Cross-Platform Strategy

### Mobile First (The "Feel")
Mobile is our primary target for accessibility. The challenge is handling complex inputs without a controller.
- **Virtual Stick Polish**: The movement stick must have a dynamic center (re-centers where the thumb touches) to prevent "drifting off" the control.
- **Smart Context**: Reduce screen clutter by making buttons context-sensitive. The "Vault" button only appears when near an obstacle. "Reload" is prioritized when mag is low.
- **Assisted Precision**: Since touch aiming is less precise, we implement a "soft friction" aim assist that slows down the reticle when hovering over enemies, rather than snapping to them.

### PC & Console Standards
For platforms with physical inputs, we adhere to industry standards to minimize learning curve.
- **PC**: High-precision mouse input with raw input support. Keyboard bindings fully remappable. UI designed for cursor navigation.
- **Console**: Twin-stick shooter paradigm. Left stick for movement, Right stick for aiming. Triggers for fire/aim. Rumble feedback is essential here.

---

##  Controller Support (Cross-Platform)

Both **PC** and **Mobile** platforms support external game controllers, providing a unified console-like experience across all devices.

### Supported Controllers

| Platform             | Supported Controllers                                                                                                                  |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| **PC**               | Xbox Series X/S, Xbox One, PlayStation DualSense (PS5), DualShock 4 (PS4), Nintendo Switch Pro, Generic XInput/DirectInput controllers |
| **Mobile (Android)** | Xbox controllers (Bluetooth), PlayStation controllers (Bluetooth), Razer Kishi, Backbone, GameSir, 8BitDo controllers                  |
| **Mobile (iOS)**     | Xbox controllers (Bluetooth), PlayStation DualSense/DualShock (Bluetooth), Backbone One, Razer Kishi, MFi-certified controllers        |

### Controller Features by Platform

| Feature                     | PC                                         | Mobile                        |
| :-------------------------- | :----------------------------------------- | :---------------------------- |
| **Full Button Mapping**     |  All buttons recognized                   |  All buttons recognized      |
| **Analog Stick Support**    |  Full analog input                        |  Full analog input           |
| **Trigger Analog**          |  Pressure-sensitive triggers              |  Pressure-sensitive triggers |
| **Vibration/Haptics**       |  Standard rumble + HD Haptics (DualSense) |  Device-dependent            |
| **Gyro Aiming**             |  DualSense/DualShock/Switch Pro           |  Limited support             |
| **Adaptive Triggers (PS5)** |  Full support                             |  Not supported               |
| **Touchpad (DualSense)**    |  As mouse/gesture input                   |  Not supported               |

---

##  Dynamic Input Switching

The game **automatically detects** and **seamlessly switches** between input methods without requiring a restart or menu navigation.

### PC: Keyboard/Mouse ↔ Controller

| Scenario                     | Behavior                                                                          |
| :--------------------------- | :-------------------------------------------------------------------------------- |
| **Controller Connected**     | System detects controller. Player can use either input at any time.               |
| **Any Keyboard/Mouse Input** | UI prompts switch to Keyboard/Mouse icons (e.g., "[F] Interact").                 |
| **Any Controller Input**     | UI prompts switch to Controller icons (e.g., "[A] Interact").                     |
| **Mixed Input**              | Last-used input determines UI prompts. Both inputs work simultaneously.           |
| **Controller Disconnected**  | Automatic fallback to Keyboard/Mouse. Pause menu if in combat (optional setting). |

**PC Input Settings:**
| Option                             | Description                                                                  | Default      |
| :--------------------------------- | :--------------------------------------------------------------------------- | :----------- |
| **Preferred Input**                | Force UI to always show specific input icons (Auto / Keyboard / Controller). | Auto         |
| **Controller Disconnect Behavior** | Pause game, Show warning only, or Ignore.                                    | Show Warning |
| **Simultaneous Input**             | Allow both controller and keyboard/mouse at the same time.                   | On           |

### Mobile: Touch ↔ Controller

| Scenario                      | Behavior                                                          |
| :---------------------------- | :---------------------------------------------------------------- |
| **No Controller**             | Touch controls displayed (Virtual joystick, on-screen buttons).   |
| **Controller Connected**      | Touch UI elements fade/hide. Controller icons appear for prompts. |
| **Touch Input Detected**      | Touch UI elements reappear. Prompts switch to touch icons.        |
| **Controller Input Detected** | Touch UI elements hide again. Prompts switch to controller icons. |
| **Controller Disconnected**   | Immediate fallback to touch controls. Brief notification shown.   |

**Mobile Input Settings:**
| Option                             | Description                                                                                   | Default           |
| :--------------------------------- | :-------------------------------------------------------------------------------------------- | :---------------- |
| **Preferred Input**                | Force UI to always show specific input (Auto / Touch / Controller).                           | Auto              |
| **Hide Touch UI with Controller**  | Completely hide on-screen buttons, or keep as secondary option.                               | Hide              |
| **Controller Disconnect Behavior** | Resume with touch, Pause game, or Show warning.                                               | Resume with Touch |
| **Hybrid Mode**                    | Keep touch controls visible while using controller (e.g., touch to look, controller to move). | Off               |

### Visual Feedback During Switch

- **Smooth Transition Animation**: Touch buttons fade out (0.3s) when controller is detected, fade in when touch is used.
- **Audio Cue**: Subtle "click" sound when input method switches.
- **Notification Toast**: Brief message: "Controller Connected" / "Using Touch Controls".

---

##  Controller Layout Options

When a controller is connected on any platform, players can choose from standard layouts:

| Preset Name  | Description                                                 | Platform |
| :----------- | :---------------------------------------------------------- | :------- |
| **Default**  | Standard twin-stick shooter layout.                         | All      |
| **Tactical** | Crouch/Prone swapped to R3 for faster reactions.            | All      |
| **Flipped**  | Fire/Aim on bumpers (LB/RB) instead of triggers (LT/RT).    | All      |
| **Southpaw** | Inverted stick controls (Movement on Right, Aim on Left).   | All      |
| **Legacy**   | Classic FPS layout (non-twin-stick, look is on left stick). | All      |
| **Custom**   | Full remapping of all controller buttons.                   | All      |

### Controller-Specific Settings

| Option                     | Description                                 | Default |
| :------------------------- | :------------------------------------------ | :------ |
| **Stick Deadzone (Inner)** | Dead area in stick center to prevent drift. | 10%     |
| **Stick Deadzone (Outer)** | Threshold for max input.                    | 90%     |
| **Trigger Deadzone**       | Minimum trigger pull to register input.     | 5%      |
| **Aim Acceleration**       | Speed increase when stick is held at max.   | Medium  |
| **Aim Assist Strength**    | Friction/slowdown when aiming near enemies. | Medium  |
| **Vibration Intensity**    | Strength of controller rumble.              | 100%    |
| **Invert Y-Axis**          | Inverted look controls.                     | Off     |
| **Swap Sticks**            | Swap left and right stick functions.        | Off     |

##  Core Mechanics UX

### Movement & Traversal
- **Weight vs. Agility**: Operators should have mass. Sprinting shouldn't be instant max speed; there's a short ramp-up. Stopping has a slight deceleration.
- **Stamina Management**: Running out of stamina shouldn't feel like hitting a wall. The character slows to a jog, with heavy breathing audio cues.
- **Vaulting**: Fluid transitions. Players shouldn't get stuck on knee-high geometry. Auto-vault options for mobile.

### Combat Controls
- **Firing Feedback**: 
  - **Visual**: Screen shake (subtle), muzzle flash, crosshair expansion.
  - **Audio**: Punchy sound effects, shell casing sounds.
  - **Haptic**: Vibration on fire (Mobile/Console).
- **Recoil Control**: Predictable patterns that can be learned. Visual recoil (camera kick) should align with actual bullet spread.

### Interactions
- **The "Use" Key**: A single context button (F / Tap Screen) handles opening doors, looting, and reviving.
- **Priority System**: If multiple interactables are close (e.g., a door next to a loot bag), priority is given to the most urgent action (Revive > Door > Loot).
- **Hold vs. Press**: Dangerous actions (Reviving, Extraction) use "Hold to Confirm" to prevent accidental triggers.

---

##  Accessibility & Customization

### Remapping
- **Full Remapping**: Every action can be rebound on PC/Console.
- **HUD Layout (Mobile)**: Players can move, resize, and change opacity of every on-screen button.

### Visual & Audio Assists
- **Colorblind Modes**: Protanopia, Deuteranopia, Tritanopia filters for UI elements (Enemy outlines, Reticles, Pings).
- **Visual Audio cues**: Option to show visual indicators for footsteps and gunfire direction (Mobile/Hearing impaired).

### Input Assists
- **Auto-Sprint**: Option to always sprint when moving forward.
- **Auto-Fire (Mobile)**: Option to automatically fire when reticle is over an enemy (within range).
- **Toggle Aim/Crouch**: Options to set actions as specific Toggles or Holds.

---

##  Haptics & Feedback

Haptics are crucial for immersion and gameplay information.

- **Combat Haptics**: Distinct vibrations for firing different weapon calibers.
- **Damage Haptics**: Directional vibration (if supported) when taking damage.
- **UI Haptics**: Light "taps" when hovering over buttons or confirming actions.
- **Status Haptics**: A heartbeat pulse when health is critical.

---

##  Detailed Input Schemes

### Movement Input

| Action            | Mobile                       | PC Keyboard            | Console Gamepad       |
| :---------------- | :--------------------------- | :--------------------- | :-------------------- |
| **Move Forward**  | Virtual Stick Up             | W                      | Left Stick Up         |
| **Move Backward** | Virtual Stick Down           | S                      | Left Stick Down       |
| **Strafe Left**   | Virtual Stick Left           | A                      | Left Stick Left       |
| **Strafe Right**  | Virtual Stick Right          | D                      | Left Stick Right      |
| **Sprint**        | Double-tap + Hold Stick Edge | Shift (Hold)           | L3 (Click Left Stick) |
| **Crouch**        | Crouch Button (Toggle)       | C / Ctrl (Toggle/Hold) | B / Circle (Toggle)   |
| **Prone**         | Hold Crouch Button (2s)      | Z                      | Hold B / Circle (2s)  |
| **Jump / Vault**  | Jump Button                  | Space                  | A / Cross             |
| **Slide**         | Crouch while Sprinting       | Ctrl while Sprinting   | B while Sprinting     |

### Combat Input

| Action                    | Mobile                        | PC                     | Console                     |
| :------------------------ | :---------------------------- | :--------------------- | :-------------------------- |
| **Fire**                  | Fire Button / Auto-Fire Zone  | LMB (Left Mouse)       | RT / R2                     |
| **Aim Down Sights (ADS)** | ADS Button (Toggle)           | RMB (Hold)             | LT / L2 (Hold)              |
| **Reload**                | Reload Button / Auto          | R                      | X / Square                  |
| **Switch Weapon**         | Weapon Slot Buttons           | 1, 2, 3 / Scroll Wheel | Y / Triangle                |
| **Melee**                 | Melee Button                  | V / Mouse Wheel Click  | RS / R3 (Click Right Stick) |
| **Throw Grenade**         | Grenade Button (Hold to Cook) | G (Tap) / Hold for Arc | RB / R1                     |

### Interaction & Ability Input

| Action                 | Mobile                        | PC                 | Console         |
| :--------------------- | :---------------------------- | :----------------- | :-------------- |
| **Interact**           | Context Button (Auto-appears) | F / E              | A / Cross       |
| **Use Ability**        | Ability Icon (Tap)            | Q                  | LB / L1         |
| **Tactical Equipment** | Equipment Icon                | Middle Mouse / 4   | D-Pad Up        |
| **Quick Ping**         | Double-tap Screen             | Middle Mouse Click | D-Pad Left      |
| **Open Map**           | Map Button                    | M / Tab            | Touchpad / View |
| **Open Inventory**     | Inventory Button              | Tab / I            | D-Pad Down      |

---

##  Sensitivity & Tuning

### Look/Aim Sensitivity
Players must have fine-grained control over how their input translates to camera movement.

- **General Sensitivity**: Base multiplier for all look input (1-100 scale).
- **ADS Sensitivity Multiplier**: Separate multiplier when aiming down sights (0.5x - 2.0x of General).
- **Per-Scope Sensitivity**: Unique sensitivity values for each scope magnification (1x, 2x, 4x, 8x).
- **Vertical/Horizontal Ratio**: Option to use different sensitivities for X and Y axes.

### Aim Acceleration & Curves
- **Linear Response**: Direct 1:1 mapping of input to camera speed. Preferred by PC players for precision.
- **Exponential Curve**: Slow movement for small inputs, fast for large inputs. Better for analog sticks.
- **Aim Acceleration (Console/Mobile)**: Gradual speed increase when stick is held at max deflection. **Tunable ON/OFF**.

### Deadzone Configuration (Gamepad/Touch)
- **Inner Deadzone**: Area around stick center where no input is registered. Prevents drift.
- **Outer Deadzone**: Threshold before input is considered "max." Ensures full speed is reachable.
- **Default Values**: Inner 10%, Outer 90%. Fully customizable by player.

### Advanced Control & Movement Settings
Inspired by competitive tactical shooters and top-down standards, these settings allow players to fine-tune the "feel" of control.

| Category | Setting | Options | Description |
| :--- | :--- | :--- | :--- |
| **Movement Axis** | **Input Reference Frame** | **Camera Relative (Default)**<br>World Relative<br>Character Relative | Defines what "Up" means on the stick/keyboard.<br>• *Camera*: Up = Top of screen.<br>• *World*: Up = North (Fixed Compass).<br>• *Character*: Up = Forward (Tank Control). |
| **Facing Logic** | **Strafing Behavior** | **Face Aim Direction (Default)**<br>Face Movement Direction | Defines character orientation.<br>• *Face Aim*: Character always looks at reticle (Tactical/Shooter).<br>• *Face Movement*: Character looks where they run (Adventure/RPGs). |
| **Traversal** | **Auto-Vault / Climb** | **Sprint Only (Default)**<br>Always<br>Off (Manual) | Determines when the character automatically hops over low obstacles.<br>• *Sprint Only*: Only vaults when sprinting into an object.<br>• *Always*: Vaults whenever moving into an object.<br>• *Off*: Requires dedicated Jump/Vault button press. |
| **Traversal** | **Sprint Behavior** | **Toggle (Default)**<br>Hold<br>Tactical Auto-Sprint | • *Toggle*: Press to start/stop.<br>• *Hold*: Sprint only while held.<br>• *Tactical Auto-Sprint*: Automatically engage sprint after moving forward for X seconds. |
| **Aiming** | **Reticle Constraint** | **Clamped to Radius**<br>Screen Edge<br>Free Cursor | (Mouse Only) Limits how far the cursor can move from character.<br>• *Clamped*: Cursor stays within X meters of player (great for twin-stick feel).<br>• *Screen Edge*: Standard cursor usage.<br>• *Free*: Unbounded. |
| **Aiming** | **Dynamic Aiming** | **Hold to Precision**<br>Toggle<br>Off | Changes camera/reticle behavior when right-click/LT is used.<br>• *Hold*: Tightens crosshair & slows movement while held.<br>• *Toggle*: Click to enter/exit precision stance. |
| **Mouse** | **Confine Cursor** | **On (Fullscreen)**<br>Always<br>Off | Keeps mouse cursor inside game window (Critical for multi-monitor setups). |
| **Tech** | **Input Buffering** | **Short (Default)**<br>None<br>Long | queues the next action (e.g., Vault after Reload) if pressed slightly early. |

---

##  Control Layout Presets

### Mobile Layout Options

| Preset Name    | Description                                                         | Best For                      |
| :------------- | :------------------------------------------------------------------ | :---------------------------- |
| **Default**    | Balanced button placement with medium touch zones.                  | New players, general use.     |
| **Claw**       | Buttons moved to top corners for multi-finger grip (claw players).  | Competitive players.          |
| **Minimal**    | Less on-screen clutter, context-heavy buttons.                      | Immersive, casual play.       |
| **One-Handed** | All controls consolidated to one side (portrait or landscape edge). | Accessibility.                |
| **Gyro-Aim**   | Reduced touch aim zone, relies on device tilt for fine-tuning.      | Players with gyro experience. |

### Console Layout Options

| Preset Name  | Description                                               |
| :----------- | :-------------------------------------------------------- |
| **Default**  | Standard twin-stick shooter layout.                       |
| **Tactical** | Crouch/Prone swapped to R3 for faster reactions.          |
| **Flipped**  | Fire/Aim on bumpers instead of triggers.                  |
| **Southpaw** | Inverted stick controls (Movement on Right, Aim on Left). |
| **Legacy**   | Classic FPS layout (non-twin-stick).                      |

### PC Keyboard Layout Options

PC players have diverse preferences based on their gaming background. We provide multiple presets while allowing **full remapping**.

| Preset Name                    | Description                                                                     | Inspired By                       |
| :----------------------------- | :------------------------------------------------------------------------------ | :-------------------------------- |
| **Default (Tactical Shooter)** | WASD movement, Shift sprint, Ctrl crouch, Space jump, Q ability.                | Valorant, CS2                     |
| **MMO Style**                  | WASD movement, abilities on 1-4, Tab for inventory, Alt for walk.               | WoW, FFXIV                        |
| **Arrow Keys**                 | Arrow keys for movement, Numpad for actions.                                    | Classic PC gamers, accessibility. |
| **ESDF Movement**              | Shifts movement one key right (ESDF), freeing more keys on the left.            | Hardcore FPS players.             |
| **Left-Handed (IJKL)**         | Movement on IJKL for right-hand dominant players using mouse on left.           | Left-handed players.              |
| **One-Hand Only**              | All essential actions accessible with one hand (left side of keyboard + mouse). | Accessibility, streamers.         |

### Keyboard Customization Options

**Full Key Rebinding:**
- Every action can be rebound to any key.
- **Conflict Detection**: System warns if a key is already assigned.
- **Multi-Bind Support**: Assign multiple keys to the same action (e.g., both C and Ctrl for Crouch).
- **"Unbind" Option**: Allow actions to have no key assigned (for unused features).

**Movement Modifiers:**
| Option          | Description                                                 | Default |
| :-------------- | :---------------------------------------------------------- | :------ |
| **Sprint Type** | Toggle (press once to start/stop) or Hold (hold to sprint). | Hold    |
| **Crouch Type** | Toggle or Hold.                                             | Toggle  |
| **Prone Type**  | Toggle or Hold.                                             | Toggle  |
| **Walk Key**    | Optional slow-walk key for stealthy movement.               | Alt     |

**Combat Modifiers:**
| Option                        | Description                                                 | Default |
| :---------------------------- | :---------------------------------------------------------- | :------ |
| **ADS Type**                  | Toggle (click to aim, click to stop) or Hold.               | Hold    |
| **Fire Mode Toggle**          | Dedicated key to switch between Auto/Semi/Burst fire modes. | B       |
| **Quick Throw vs. Aim Throw** | Tap G for quick throw, Hold G for aim trajectory.           | Enabled |
| **Lean Keys**                 | Q/E for leaning left/right (if lean mechanic exists).       | Q/E     |

**Inventory & UI Shortcuts:**
| Option             | Description                                                           | Default            |
| :----------------- | :-------------------------------------------------------------------- | :----------------- |
| **Weapon Slots**   | Direct access to primary (1), secondary (2), melee (3), grenades (4). | 1, 2, 3, 4         |
| **Quick Heal**     | Dedicated key to use healing item without opening inventory.          | 5 or H             |
| **Quick Armor**    | Dedicated key to equip armor plate.                                   | 6 or J             |
| **Last Weapon**    | Swap to previously equipped weapon.                                   | Q (if not ability) |
| **Holster Weapon** | Put weapon away for faster movement.                                  | X                  |

**Communication Shortcuts:**
| Option               | Description                                    | Default          |
| :------------------- | :--------------------------------------------- | :--------------- |
| **Push-to-Talk**     | Hold to transmit voice.                        | V                |
| **Text Chat**        | Open text chat input.                          | Enter            |
| **Quick Ping**       | Contextual ping (Enemy, Item, Location).       | Middle Mouse / Z |
| **Ping Wheel**       | Hold to open radial ping menu.                 | Hold Z           |
| **Team Comms Wheel** | Quick voice lines (Need Ammo, Cover Me, etc.). | C                |

**Mouse Button Options:**
| Option                    | Description                                          | Default         |
| :------------------------ | :--------------------------------------------------- | :-------------- |
| **Mouse Button 4 (Side)** | Assignable action (e.g., Melee, Ping, Push-to-Talk). | Melee           |
| **Mouse Button 5 (Side)** | Assignable action.                                   | Quick Ping      |
| **Mouse Wheel Up**        | Assignable (default: Next Weapon).                   | Next Weapon     |
| **Mouse Wheel Down**      | Assignable (default: Previous Weapon).               | Previous Weapon |
| **Mouse Wheel Click**     | Assignable (default: Ping).                          | Ping            |

### Advanced Keyboard Settings

**Double-Tap Actions:**
| Option                            | Description                                      | Default |
| :-------------------------------- | :----------------------------------------------- | :------ |
| **Double-Tap W to Sprint**        | Sprint by quickly pressing W twice.              | Off     |
| **Double-Tap Direction to Dodge** | Quick dodge/roll by double-tapping movement key. | Off     |
| **Double-Tap Crouch to Prone**    | Quickly drop to prone by tapping crouch twice.   | Off     |

**Hold Duration Settings:**
| Option                     | Description                                                  | Default |
| :------------------------- | :----------------------------------------------------------- | :------ |
| **Hold Interact Duration** | Time to hold F for important interactions (Revive, Extract). | 1.5s    |
| **Hold Grenade to Cook**   | Max cook time before auto-throw.                             | 3.0s    |

**Key Repeat / Spam Protection:**
- **Debounce Time**: Minimum time between repeated key presses being registered (prevents accidental double-inputs).
- **Default**: 50ms (adjustable 0-200ms).

---

##  Camera & Perspective

### Top-Down Camera Behavior
- **Fixed Angle**: Camera maintains a constant isometric-style angle above the player.
- **Height Variation**: Camera slightly adjusts height based on environment (closer in buildings, further in open areas).
- **Zoom Control**: Player can adjust zoom level within a defined range (default: middle of range).

### Camera Smoothing
- **Follow Speed**: Camera smoothly follows character movement, slight delay to prevent jarring motion.
- **Aim Offset**: When aiming, camera shifts slightly in the aim direction to provide more forward vision.
- **Death Cam**: On death, camera briefly tracks killer before transitioning to spectate/respawn screen.

### Visual Parallax & Depth Perception
To address the lack of depth in a standard top-down view, we implement a **Parallax Illusion** system.
- **Multi-Plane Perspective**: Objects at different elevations (rooftops, tree canopies vs. ground level) scroll at slightly different rates relative to the camera movement. This artificial parallax creates a convincing 3D "pop" and helps players judge the height of obstacles.
- **Dynamic FoV Adjustment**: Subtle Field-of-View changes based on movement speed enhance the sense of speed and depth, reducing the "flatness" of the isometric view.

---

##  Context-Sensitive Controls

### Dynamic Button Visibility (Mobile)
To reduce screen clutter, certain buttons only appear when relevant:
- **Vault Button**: Appears when near vaultable geometry.
- **Reload Button**: Highlighted when ammo is low (< 30%).
- **Interact Prompt**: Appears over interactable objects with icon indicating action type (Door, Loot, Revive).
- **Vehicle Controls**: Mount/Dismount, Drive, Brake replace certain buttons when in/near vehicles.

### Action Priority System
When multiple actions are possible, the game selects the most important one:

| Priority | Action                    | Reasoning                             |
| :------- | :------------------------ | :------------------------------------ |
| 1        | Revive Teammate           | Life-saving action, highest priority. |
| 2        | Defuse/Plant Objective    | Mission-critical.                     |
| 3        | Use Extraction Point      | End-game goal.                        |
| 4        | Open Door/Gate            | Traversal.                            |
| 5        | Loot Item/Container       | Resource gathering.                   |
| 6        | Interact with Environment | Low priority (Switches, etc.).        |

---

##  Tutorial & Onboarding

### First-Time User Experience (FTUE)

**Phase 1: Movement Basics**
- Guided prompt to use virtual stick / WASD.
- Short obstacle course teaching Sprint, Crouch, Vault.
- Checkpoint: Player reaches a destination using all movement types.

**Phase 2: Combat Basics**
- Firing range with static targets.
- Introduction to ADS, Reloading, Weapon Switching.
- Checkpoint: Player eliminates all targets.

**Phase 3: Interaction & Ability**
- Tutorial on looting containers.
- Introduction to Operator Ability with context of when to use it.
- Checkpoint: Player uses ability to achieve a goal (e.g., heal self, reveal enemy).

**Phase 4: Full Simulation**
- Practice match vs. AI bots with all systems enabled.
- Subtle prompts if player forgets an action.

### In-Game Reminders
- **Contextual Tips**: "Hold [Crouch] while sprinting to slide!"
- **Low Ammo Warning**: Visual + audio cue when magazine is low.
- **Ability Ready Indicator**: Audio chime when ability comes off cooldown.

---

##  Competitive Control Considerations

### Input Fairness
- **Cross-Platform Matchmaking**: If enabled, aim assist for controller/touch players is balanced against raw mouse input.
- **Input Display**: Match results can show which input method each player used.
- **Ranked Queues**: Separate queues for Input Type (Touch, Controller, M&K) can be considered for high tiers.

### Anti-Cheat Measures (Input Related)
- **Input Velocity Limits**: Flag inputs that exceed humanly possible speeds (aimbot detection).
- **No Third-Party Mapping**: Disable remapping tools that could be used for macros (on Console/Mobile stores).
- **Gyro Anti-Abuse**: Limit gyro sensitivity to prevent "flick" exploits.

### Response Time Requirements
- **Target Input Latency**: < 16ms (1 frame at 60fps).
- **Server Tick Rate**: 60Hz for responsive hit registration.
- **Rollback/Prediction**: Client-side prediction for movement to mask network latency.

---

##  Control Analytics & Telemetry

Understanding how players use controls helps us iterate.

### Metrics to Collect
- **Button Usage Frequency**: Which buttons are pressed most/least?
- **Layout Changes**: How many players customize their HUD layout?
- **Sensitivity Distribution**: What is the average sensitivity players settle on?
- **Aim Assist Engagement**: How often does aim assist activate? Correlation with kills?
- **Accessibility Feature Usage**: % of players using Auto-Fire, Colorblind modes, etc.

### Feedback Loops
- **A/B Testing**: Test different default sensitivity values or button placements.
- **Player Surveys**: In-game feedback prompts after first few matches.
- **Community Input**: Monitor subreddit/Discord for control-related complaints.

---

##  Future Control Enhancements

- **Gyro Aiming Support**: Fine-tune aiming on Mobile and Switch by tilting the device.
- **Adaptive Trigger Support (PS5)**: Resistance on triggers when firing different weapon types.
- **External Controller Support (Mobile)**: Pair Bluetooth controllers for a console-like experience.
- **Voice Commands**: Basic actions like "Reload," "Ping," "Open Map" via voice (Accessibility).
- **Eye Tracking (PC)**: Experimental aim-where-you-look for ultra-immersive gameplay.



