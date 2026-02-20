---
title: "CIPHER - Alex Nakamura"
type: docs
---

## Operator Profile

> *"Your gadgets, your abilities, your plans—all worthless. I just hit the off switch."*

### Basic Information

| Attribute       | Value                     |
| :-------------- | :------------------------ |
| **Real Name**   | Alexander "Alex" Nakamura |
| **Codename**    | CIPHER                    |
| **Class**       | Specialist                |
| **Nationality** | Japanese-American         |
| **Age**         | 27                        |
| **Height**      | 175 cm (5'9")             |
| **Weight**      | 68 kg (150 lbs)           |

### Background

Alex Nakamura was a prodigy at MIT before dropping out to join the NSA's elite cyber warfare division. His ability to find exploits in any system made him invaluable—until he discovered the agency was using his tools for mass surveillance on American citizens.

He leaked what he could and went underground, using his skills to level the playing field for those without technological advantages. In the Exclusion Zone, where tech can mean the difference between life and death, CIPHER makes sure no one has an unfair edge.

### Personality Traits

- **Anti-authority** - Distrusts all institutions
- **Clever** - Always three moves ahead
- **Sardonic** - Uses humor as deflection
- **Ethical** - Has lines he won't cross

---

## Combat Statistics

### Base Stats

| Stat                | Value   | Class Modifier | Final   |
| :------------------ | :------ | :------------- | :------ |
| **Health**          | 100 HP  | -              | 100 HP  |
| **Armor**           | 50      | -              | 50      |
| **Sprint Speed**    | 5.5 m/s | -              | 5.5 m/s |
| **Walk Speed**      | 3.5 m/s | -              | 3.5 m/s |
| **Weapon Accuracy** | 100%    | -10%           | 90%     |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 100 | Standard (Specialist class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8/second | Standard |
| **Net Sprint Duration** | 10.0 seconds | Average |
| **Footstep Volume** | 95% | Slightly quieter than average — sneakers |
| **Ability Audio Radius** | 40 meters | EMP pulse is very loud — major audio tell |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT |
| EMP | 100% | Immune to enemy CIPHER EMP |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 38 cm radius, 175 cm height |
| **Head Sphere** | 14 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Medium build, antenna array on backpack, arm-mounted hacking interface visible |
| **Class Accent Zones** | Yellow (#EAB308) on tech strips and backpack antenna |
| **EMP VFX (Top-Down)** | Blue-white expanding ring from operator (15m radius), static distortion on affected units |
| **EMP Audio Radius** | 40m — loud pulse crack audible at extreme range |

<!-- REF_IMAGE: CIPHER top-down view — showing operator with EMP blast active, blue-white expanding ring visible from above, static effects on enemies in radius -->

### Difficulty Rating

**Difficulty: 4/5** — EMP timing is everything. Using it too early wastes it; too late and shields/drones already did their job. Reading enemy tech usage is critical.


## Abilities

### Active Ability: EMP Blast

> *"Release an electromagnetic pulse that disables all technology in the area."*

| Property     | Value                         |
| :----------- | :---------------------------- |
| **Cooldown** | 110 seconds                   |
| **Duration** | Instant (effects last 10 sec) |
| **Charges**  | 1                             |

#### Effects

| Effect             | Target                 | Duration   |
| :----------------- | :--------------------- | :--------- |
| Ability Disable    | Enemy operators        | 10 seconds |
| Gadget Destruction | All gadgets in range   | Permanent  |
| HUD Disruption     | Enemies                | 5 seconds  |
| Shield Destruction | ANGEL, BULWARK shields | Instant    |

#### EMP Interaction Matrix

| Target | Effect | Duration |
| :----- | :----- | :------- |
| **ANGEL Guardian Shield** | Destroyed instantly | Permanent (until redeployed) |
| **BULWARK Riot Shield** | Disabled (not destroyed) | 5 seconds |
| **DOC Healing Drone** | Destroyed instantly | Permanent |
| **PHANTOM UAV** | Destroyed, falls from sky | Permanent |
| **SPECTER Sensors** | All in radius destroyed | Permanent |
| **FLUX Nano Swarm** | Dispersed instantly | Permanent |
| **VIPER Combat Stim** | Cancelled | Immediate |
| **HAVOC Berserker Rage** | Cancelled | Immediate |
| **WRAITH Smoke Screen** | Not affected | N/A — smoke is chemical, not tech |
| **FORTRESS Overcharge** | Bonus armor stripped | Immediate |
| **Enemy HUD** | Static distortion | 5 seconds |

#### Top-Down EMP VFX

| State | VFX From Above |
| :---- | :------------- |
| EMP charging | Blue-white glow building on CIPHER's arm device |
| EMP blast | Blue-white ring expanding outward from operator (15m radius) |
| EMP on enemy | Blue static sparks on affected operator, HUD disruption VFX |
| Gadget destroyed | Blue flash + debris scatter from gadget position |
| Shield broken | Dramatic shatter VFX on ANGEL dome / BULWARK arc flicker |


| Property       | Value                  |
| :------------- | :--------------------- |
| Radius         | 15 meters              |
| Vertical Range | Full height            |
| Line of Sight  | Not required           |
| Friendly Fire  | No (allies unaffected) |

#### What Gets Disabled

| Category | Affected |
| :------- | :------- |
| **Destroys** | ANGEL Shield, Healing Drone, Motion Sensors, Turrets |
| **Disables** | Combat Stim, Berserker, UAV Scan, Smoke Emitters |
| **Immune** | Passive abilities, Weapons, Armor |

#### Upgrade Slots

**Slot 1 (Level 5):**
| Option              | Effect                                  |
| :------------------ | :-------------------------------------- |
| **Longer Blackout** | Disable duration +5 seconds (15s total) |
| **Quick Hack**      | Cooldown -25 seconds (85s total)        |
| **Wide Signal**     | Radius +5 meters (20m total)            |

**Slot 2 (Level 20):**
| Option              | Effect                                  |
| :------------------ | :-------------------------------------- |
| **System Shock**    | Disabled enemies take 10 damage         |
| **Sensor Overload** | Disabled enemies are also slowed 20%    |
| **Cascade Failure** | Destroyed gadgets explode for 15 damage |

**Slot 3 (Level 35):**
| Option             | Effect                                           |
| :----------------- | :----------------------------------------------- |
| **Total Blackout** | Also disables enemy minimap for 20 seconds       |
| **Power Drain**    | Killing a disabled enemy reduces cooldown by 20s |
| **Counter-Tech**   | Immune to being EMP'd/disabled yourself          |

---

### Passive Ability: Hacker's Toolkit

> *"Every system has a backdoor. I just know where to look."*

| Condition             | Effect                                    |
| :-------------------- | :---------------------------------------- |
| Interacting with tech | +20% speed                                |
| Near enemy gadget     | See outline through walls (5m)            |
| Destroying gadget     | Reveal player who placed it for 3 seconds |

**Interactions Affected:**
- Hacking terminals
- Opening locked containers
- Disarming traps
- Accessing intel points

---

## Loadout

### Default Loadout

| Slot          | Item                      | Notes            |
| :------------ | :------------------------ | :--------------- |
| **Primary**   | MAC-10 SMG                | Compact, fast    |
| **Secondary** | G17 Pistol                | Standard         |
| **Tactical**  | EMP Grenades ×2, Lockpick | Extra disruption |
| **Armor**     | Medium Vest               | 50 armor         |

### Recommended Loadouts

**Hard Counter:**
| Slot      | Item        | Why                |
| :-------- | :---------- | :----------------- |
| Primary   | UMP-45      | Stable, accurate   |
| Secondary | G17         | -                  |
| Tactical  | EMP Nade ×3 | Maximum disruption |

**Loot Focused:**
| Slot      | Item                | Why             |
| :-------- | :------------------ | :-------------- |
| Primary   | VSS                 | Quiet looting   |
| Secondary | Silenced Pistol     | Stay quiet      |
| Tactical  | Lockpick ×2, EMP ×1 | Access + safety |

---

## Playstyle Guide

### Role in Team

**Primary Role:** Counter-Tech
- Disable enemy abilities before fight
- Destroy defensive gadgets
- Enable team pushes

**Secondary Role:** Objective Specialist
- Fast hacking/interaction
- First to locked areas
- Intel gathering

### EMP Timing

**Perfect Timing:**
- Right before team push
- When enemy activates ability (cancel it)
- Against defensive setup

**Bad Timing:**
- When no enemy tech nearby
- While solo (wasted potential)
- On cooldown before key fight

---

## Matchups

### Favorable Matchups

| Opponent    | Why Favorable              | Tactic               |
| :---------- | :------------------------- | :------------------- |
| **ANGEL**   | Shield destroyed instantly | EMP > Push           |
| **DOC**     | Drone destroyed            | Kill drone first     |
| **BULWARK** | Shield disabled            | EMP ends his defense |
| **SPECTER** | Sensors destroyed          | Clear his traps      |

### Even Matchups

| Opponent     | Notes                   | Key to Winning    |
| :----------- | :---------------------- | :---------------- |
| **PHANTOM**  | Both tech-focused       | Timing war        |
| **FLUX**     | Both disable            | Who EMPs first    |
| **FORTRESS** | Armor buff not disabled | Focus fire anyway |

### Unfavorable Matchups

| Opponent  | Why Difficult                           | Counter Strategy |
| :-------- | :-------------------------------------- | :--------------- |
| **VIPER** | After EMP, he still out-guns you        | Team support     |
| **HAVOC** | Berserker can activate before/after EMP | Keep range       |
| **BLAZE** | Fire isn't tech                         | Avoid fire zones |

---

## Voice Lines

### Combat

| Trigger               | Line                            |
| :-------------------- | :------------------------------ |
| Ability Activation    | "EMP out! Systems down!"        |
| Gadget Destroyed      | "Nice toy. Had a nice toy."     |
| Kill (Disabled Enemy) | "Should've gone analog."        |
| Hacking               | "I'm in."                       |
| Reviving              | "Stay with me, got work to do." |

### Personality

| Trigger            | Line                                |
| :----------------- | :---------------------------------- |
| Match Start        | "Let's see what toys they brought." |
| Extraction Success | "Data secured. We're out."          |
| Detecting Gadget   | "I see you... hackable."            |

---

## Cosmetics

### Default Appearance

- **Outfit:** Black hoodie under lightweight tactical vest, multiple USB drives on belt
- **Headgear:** Black beanie with tech goggles pushed up on forehead
- **Gloves:** Fingerless gloves (hacker aesthetic, touch-screen compatible)
- **Face:** Youthful, slight stubble, always watching screens

<!-- REF_IMAGE: CIPHER default skin — top-down view showing lean silhouette, hoodie under vest, tech goggles on forehead, utility belt with EMP device -->

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
| **Laptop Stickers** | Hacker collective logos on laptop (visible in lobby) |

---

## Lore Connections

### Relationships

| Character | Relationship |
| :-------- | :----------- |
| **PHANTOM** | Complicated — she hunted leakers like him at the CIA, now forced allies |
| **FLUX** | Fellow outcasts, share tech knowledge — closest friend in the roster |
| **ANGEL** | She represents the institutions he hates — philosophical tension |
| **VIPER** | VIPER distrusts him — "Too many secrets." CIPHER finds the suspicion amusing |

### Story Hooks

- Leaked NSA surveillance tools are now being used by Corporation — feels responsible
- Maintains a dark web presence under the alias "Z3R0_DAY"
- Seeking the pharmaceutical exec who weaponized FLUX's nano research
- Dead drop quest chain — encrypted messages hidden across all maps

---

## Design Notes (For Developers)

### Balance Considerations

- EMP Blast is the strongest counter-ability in the game — 110s cooldown is justified
- EMP should NOT cancel passive abilities or deactivate weapons — only active abilities and deployables
- Shield Destruction is instant and permanent — ANGEL and BULWARK players should hear a distinct "shield broken" audio cue
- -10% weapon accuracy class trait ensures CIPHER loses straight gunfights — his power is in disruption timing
- Cascade Failure upgrade (Slot 2) explosive damage should have a minimum range to prevent self-harm from nearby gadget destruction

### Animation Requirements

- EMP activation (0.8 seconds — pull device from vest, slam button)
- EMP pulse VFX (expanding blue-white ring from operator)
- Hacking animation (fast typing gesture on arm-mounted interface)
- Gadget detection HUD (blue outline through walls at 5m)
- Death animation: collapses backward, device sparks (tech failure)

### Audio Requirements

| Sound | Notes |
| :---- | :---- |
| EMP activate | Rising electronic whine + sharp pulse crack |
| EMP effect (enemy perspective) | Static burst + HUD distortion noise |
| Hacking interaction | Rapid keyboard clicks + data transfer chirps |
| Gadget detected | Soft electronic ping (only CIPHER hears) |
| Footsteps | Standard weight — sneakers on concrete |

### Top-Down Specific Notes

- EMP expanding ring must be visible at minimum zoom — largest VFX radius in the game (15m)
- Static distortion on affected enemies should be visible from top-down (blue sparking particles)
- Gadget destruction VFX must clearly communicate which gadgets were destroyed
- CIPHER is immune to enemy EMP — this is a critical balance point in mirror matchups
- -10% weapon accuracy penalty means CIPHER should lose aim duels — his power is in EMP timing
- Tech Scavenge passive (hack enemy gadgets) should show a clear interaction prompt from above

