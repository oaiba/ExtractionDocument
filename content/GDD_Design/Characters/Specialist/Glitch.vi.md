---
title: "GLITCH - Maya Torres"
type: docs
---

## Operator Profile

> *"Your gadgets, your abilities, your plans—all worthless. I just hit the off switch."*

### Basic Information

| Attribute       | giá trị                     |
| :-------------- | :------------------------ |
| **Real Name**   | Maya Torres |
| **Codename**    | GLITCH                    |
| **Class**       | Specialist                |
| **Nationality** | American |
| **Age**         | 27                        |
| **Height**      | 175 cm (5'9")             |
| **Weight**      | 68 kg (150 lbs)           |

### Background

Maya Torres was a prodigy at MIT trước dropping out to join the NSA's elite cyber warfare division. His ability to find exploits in any hệ thống made him invaluable—until he discovered the agency was using his tools for mass surveillance on American citizens.

He leaked what he could và went underground, using his skills to level the playing field for those mà không technological advantages. In the Exclusion Zone, where tech can mean the difference between life và death, GLITCH makes sure no one has an unfair edge.

### Personality Traits

- **Anti-authority** - Distrusts all institutions
- **Clever** - Always three moves ahead
- **Sardonic** - Uses humor as deflection
- **Ethical** - Has lines he won't cross

---

## Combat Statistics

### Base Stats

| Stat                | giá trị   | Class Modifier | Final   |
| :------------------ | :------ | :------------- | :------ |
| **máu**          | 100 HP  | -              | 100 HP  |
| **giáp**           | 50      | -              | 50      |
| **Sprint Speed**    | 5.5 m/s | -              | 5.5 m/s |
| **Walk Speed**      | 3.5 m/s | -              | 3.5 m/s |
| **vũ khí Accuracy** | 100%    | -10%           | 90%     |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 100 | Standard (Specialist class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8/second | Standard |
| **Net Sprint Duration** | 10.0 seconds | Average |
| **Footstep Volume** | 95% | Slightly quieter than average — sneakers |
| **Ability Audio Radius** | 40 meters | EMP pulse is very loud — major audio tell |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT |
| EMP | 100% | Immune to địch GLITCH EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 38 cm radius, 175 cm height |
| **Head Sphere** | 14 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Medium build, antenna array on backpack, arm-mounted hacking interface hiển thị rõ |
| **Class Accent Zones** | Yellow (#EAB308) on tech strips và backpack antenna |
| **EMP VFX (Top-Down)** | Blue-white expanding ring from operator (15m radius), static distortion on affected units |
| **EMP Audio Radius** | 40m — loud pulse crack audible at extreme range |

<!-- REF_IMAGE: GLITCH top-down view — showing operator với EMP blast active, blue-white expanding ring hiển thị rõ from above, static effects on địch in radius -->

### Difficulty Rating

**Difficulty: 4/5** — EMP timing is everything. Using it too early wastes it; too late và shields/drones already did their job. Reading địch tech usage is critical.


## Abilities

### Active Ability: EMP Blast

> *"Release an electromagnetic pulse that disables all technology in the area."*

| Property     | giá trị                         |
| :----------- | :---------------------------- |
| **Cooldown** | 110 seconds                   |
| **Duration** | Instant (effects last 10 sec) |
| **Charges**  | 1                             |

#### Effects

| Effect             | Target                 | Duration   |
| :----------------- | :--------------------- | :--------- |
| Ability Disable    | địch operators        | 10 seconds |
| Gadget Destruction | All gadgets in range   | Permanent  |
| HUD Disruption     | địch                | 5 seconds  |
| Shield Destruction | AEGIS, BASTION shields | Instant    |

#### EMP Interaction matrix

| Target | Effect | Duration |
| :----- | :----- | :------- |
| **AEGIS Guardian Shield** | Destroyed instantly | Permanent (until redeployed) |
| **BASTION Riot Shield** | disabled (not destroyed) | 5 seconds |
| **SUTURE Healing Drone** | Destroyed instantly | Permanent |
| **SONAR UAV** | Destroyed, falls from sky | Permanent |
| **MIRAGE Sensors** | All in radius destroyed | Permanent |
| **PULSE Nano Swarm** | Dispersed instantly | Permanent |
| **MAMBA Combat Stim** | Cancelled | Immediate |
| **TARTARUS Berserker Rage** | Cancelled | Immediate |
| **OBSIDIAN Smoke màn hình** | Not affected | N/A — smoke is chemical, not tech |
| **GOLIATH Overcharge** | Bonus giáp stripped | Immediate |
| **địch HUD** | Static distortion | 5 seconds |

#### Top-Down EMP VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| EMP charging | Blue-white glow building on GLITCH's arm device |
| EMP blast | Blue-white ring expanding outward from operator (15m radius) |
| EMP on địch | Blue static sparks on affected operator, HUD disruption VFX |
| Gadget destroyed | Blue flash + debris scatter from gadget position |
| Shield broken | Dramatic shatter VFX on AEGIS dome / BASTION arc flicker |


| Property       | giá trị                  |
| :------------- | :--------------------- |
| Radius         | 15 meters              |
| Vertical Range | Full height            |
| Line of Sight  | Not required           |
| Friendly Fire  | No (allies unaffected) |

#### What Gets disabled

| Category | Affected |
| :------- | :------- |
| **Destroys** | AEGIS Shield, Healing Drone, Motion Sensors, Turrets |
| **Disables** | Combat Stim, Berserker, UAV Scan, Smoke Emitters |
| **Immune** | Passive abilities, vũ khí, giáp |

#### upgrade Slots

**Slot 1 (Level 5):**
| Option              | Effect                                  |
| :------------------ | :-------------------------------------- |
| **Longer Blackout** | Disable duration +5 seconds (15s total) |
| **Quick Hack**      | Cooldown -25 seconds (85s total)        |
| **Wide Signal**     | Radius +5 meters (20m total)            |

**Slot 2 (Level 20):**
| Option              | Effect                                  |
| :------------------ | :-------------------------------------- |
| **hệ thống Shock**    | disabled địch take 10 damage         |
| **Sensor Overload** | disabled địch are also slowed 20%    |
| **Cascade Failure** | Destroyed gadgets explode for 15 damage |

**Slot 3 (Level 35):**
| Option             | Effect                                           |
| :----------------- | :----------------------------------------------- |
| **Total Blackout** | Also disables địch minimap for 20 seconds       |
| **Power Drain**    | Killing a disabled địch reduces cooldown by 20s |
| **Counter-Tech**   | Immune to being EMP'd/disabled yourself          |

---

### Passive Ability: Hacker's Toolkit

> *"Every hệ thống has a backdoor. I just know where to look."*

| Condition             | Effect                                    |
| :-------------------- | :---------------------------------------- |
| Interacting với tech | +20% speed                                |
| Near địch gadget     | See outline thông qua walls (5m)            |
| Destroying gadget     | Reveal người chơi who placed it for 3 seconds |

**Interactions Affected:**
- Hacking terminals
- Opening locked containers
- Disarming traps
- Accessing intel points

---

## Loadout

### Default Loadout

| Slot          | Item                      | ghi chú            |
| :------------ | :------------------------ | :--------------- |
| **primary**   | MAC-10 SMG                | Compact, fast    |
| **secondary** | G17 Pistol                | Standard         |
| **Tactical**  | EMP Grenades ×2, Lockpick | Extra disruption |
| **giáp**     | Medium Vest               | 50 giáp         |

### Recommended Loadouts

**Hard Counter:**
| Slot      | Item        | Why                |
| :-------- | :---------- | :----------------- |
| primary   | UMP-45      | Stable, accurate   |
| secondary | G17         | -                  |
| Tactical  | EMP Nade ×3 | Maximum disruption |

**Loot Focused:**
| Slot      | Item                | Why             |
| :-------- | :------------------ | :-------------- |
| primary   | VSS                 | Quiet looting   |
| secondary | Silenced Pistol     | Stay quiet      |
| Tactical  | Lockpick ×2, EMP ×1 | Access + safety |

---

## Playstyle Guide

### Role in Team

**primary Role:** Counter-Tech
- Disable địch abilities trước fight
- Destroy defensive gadgets
- Enable team pushes

**secondary Role:** Objective Specialist
- Fast hacking/interaction
- First to locked areas
- Intel gathering

### EMP Timing

**Perfect Timing:**
- Right trước team push
- khi địch activates ability (cancel it)
- Against defensive setup

**Bad Timing:**
- khi no địch tech nearby
- While solo (wasted potential)
- On cooldown trước chính fight

---

## Matchups

### Favorable Matchups

| Opponent    | Why Favorable              | Tactic               |
| :---------- | :------------------------- | :------------------- |
| **AEGIS**   | Shield destroyed instantly | EMP > Push           |
| **SUTURE**     | Drone destroyed            | Kill drone first     |
| **BASTION** | Shield disabled            | EMP ends his defense |
| **MIRAGE** | Sensors destroyed          | rõ his traps      |

### Even Matchups

| Opponent     | ghi chú                   | chính to Winning    |
| :----------- | :---------------------- | :---------------- |
| **SONAR**  | Both tech-focused       | Timing war        |
| **PULSE**     | Both disable            | Who EMPs first    |
| **GOLIATH** | giáp buff not disabled | Focus fire anyway |

### Unfavorable Matchups

| Opponent  | Why Difficult                           | Counter Strategy |
| :-------- | :-------------------------------------- | :--------------- |
| **MAMBA** | sau EMP, he still out-guns you        | Team support     |
| **TARTARUS** | Berserker can activate trước/sau EMP | Keep range       |
| **IGNITION** | Fire isn't tech                         | Avoid fire zones |

---

## Voice Lines

### Combat

| Trigger               | Line                            |
| :-------------------- | :------------------------------ |
| Ability Activation    | "EMP out! hệ thống down!"        |
| Gadget Destroyed      | "Nice toy. Had a nice toy."     |
| Kill (disabled địch) | "Should've gone analog."        |
| Hacking               | "I'm in."                       |
| Reviving              | "Stay với me, got work to do." |

### Personality

| Trigger            | Line                                |
| :----------------- | :---------------------------------- |
| Match Start        | "Let's see what toys they brought." |
| Extraction success | "Data secured. We're out."          |
| Detecting Gadget   | "I see you... hackable."            |

---

## Cosmetics

### Default Appearance

- **Outfit:** Black hoodie under lightweight tactical vest, multiple USB drives on belt
- **Headgear:** Black beanie với tech goggles pushed up on forehead
- **Gloves:** Fingerless gloves (hacker aesthetic, touch-màn hình compatible)
- **Face:** Youthful, slight stubble, always watching màn hình

<!-- REF_IMAGE: GLITCH default skin — top-down view showing lean silhouette, hoodie under vest, tech goggles on forehead, utility belt với EMP device -->

### Unlockable Skins

| Skin | Rarity | Unlock |
| :--- | :----- | :----- |
| **White Hat** | Common | Level 10 |
| **Darknet** | Uncommon | 1,000 Credits |
| **Anonymous** | Rare | Level 25 |
| **Mainframe** | Epic | Battle Pass S2 |
| **Ghost in the Shell** | Legendary | Crossover Event |

### Signature Items

| Item | Description |
| :--- | :---------- |
| **USB Bandolier** | Row of encrypted USB drives on chest harness |
| **Binary Tattoo** | Circuit-pattern tattoo on left forearm |
| **Laptop Stickers** | Hacker collective logos on laptop (hiển thị rõ in lobby) |

---

## Lore Connections

### Relationships

| nhân vật | Relationship |
| :-------- | :----------- |
| **SONAR** | Complicated — she hunted leakers like him at the CIA, now forced allies |
| **PULSE** | Fellow outcasts, share tech knowledge — closest friend in the roster |
| **AEGIS** | She represents the institutions he hates — philosophical tension |
| **MAMBA** | MAMBA distrusts him — "Too many secrets." GLITCH finds the suspicion amusing |

### Story Hooks

- Leaked NSA surveillance tools are now being used by Corporation — feels responsible
- Maintains a dark web presence under the alias "Z3R0_DAY"
- Seeking the pharmaceutical exec who weaponized PULSE's nano research
- Dead drop quest chain — encrypted messages hidden across all maps

---

## Design ghi chú (For Developers)

### Balance Considerations

- EMP Blast is the strongest counter-ability in the game — 110s cooldown is justified
- EMP không nên cancel passive abilities hoặc deactivate vũ khí — only active abilities và deployables
- Shield Destruction is instant và permanent — AEGIS và BASTION Người chơi nên hear a distinct "shield broken" audio cue
- -10% vũ khí accuracy class trait ensures GLITCH loses straight gunfights — his power is in disruption timing
- Cascade Failure upgrade (Slot 2) explosive damage should have a minimum range to prevent self-harm from nearby gadget destruction

### Animation yêu cầu

- EMP activation (0.8 seconds — pull device from vest, slam button)
- EMP pulse VFX (expanding blue-white ring from operator)
- Hacking animation (fast typing gesture on arm-mounted interface)
- Gadget detection HUD (blue outline thông qua walls at 5m)
- Death animation: collapses backward, device sparks (tech failure)

### Audio yêu cầu

| Sound | ghi chú |
| :---- | :---- |
| EMP activate | Rising electronic whine + sharp pulse crack |
| EMP effect (địch perspective) | Static burst + HUD distortion noise |
| Hacking interaction | Rapid keyboard clicks + data transfer chirps |
| Gadget detected | Soft electronic ping (only GLITCH hears) |
| Footsteps | Standard weight — sneakers on concrete |

### Top-Down cụ thể ghi chú

- EMP expanding ring phải được hiển thị rõ at minimum zoom — largest VFX radius in the game (15m)
- Static distortion on affected địch nên được hiển thị rõ from top-down (blue sparking particles)
- Gadget destruction VFX must clearly communicate which gadgets were destroyed
- GLITCH is immune to địch EMP — this is a critical balance point in mirror matchups
- -10% vũ khí accuracy penalty means GLITCH should lose aim duels — his power is in EMP timing
- Tech Scavenge passive (hack địch gadgets) should show a rõ interaction prompt from above
