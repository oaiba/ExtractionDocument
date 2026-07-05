---
title: Characters & Operators
linkTitle: Characters
type: docs
weight: 3
sidebar:
  open: false
---

# Characters & Operators

### The Squad Hierarchy

In **Extraction Shooter**, characters are defined not just by stats, but by their tactical utility in a squad. While every operator can shoot and loot, their unique abilities define the flow of combat.

> \[!NOTE] **Philosophy:** No "DPS" or "Tank" in the traditional MMO sense. Every bullet is lethal. Roles provide _utility_ and _sustain_, not invincibility.

#### Class Roster

{{< cards cols="3" >}}
{{< card link="Assault/" title="Assault" icon="fire" subtitle="Fraggers. Breachers. Frontline engage." >}}
{{< card link="Recon/" title="Recon" icon="eye" subtitle="Intel gathering. Sniping. Flanking." >}}
{{< card link="Support/" title="Support" icon="plus-circle" subtitle="Healing. Ammo resupply. Utility." >}}
{{< card link="Tank/" title="Tank" icon="shield-check" subtitle="Area denial. Heavy weapons. Crowd control." >}}
{{< card link="Specialist/" title="Specialist" icon="chip" subtitle="Cyberwarfare. Traps. Gadgets." >}}
{{< /cards >}}

***

### Design Philosophy

#### Core Principles

| Principle               | Description                                            | Example                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Class Identity**      | Each class has a defined combat role                   | Tank = Damage absorption                                                                                                                                        |
| **Character Diversity** | Multiple characters per class with different abilities | 2 Assault operators with different stims                                                                                                                        |
| **Visual Clarity**      | Instant recognition from top-down view                 | Unique silhouettes, color themes (see [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md)) |
| **Balanced Power**      | Abilities complement skill, not replace it             | +25% damage, not instant kill                                                                                                                                   |
| **Risk/Reward**         | Aggressive play has trade-offs                         | High damage = lower survivability                                                                                                                               |
| **Team Synergy**        | Operators work better together                         | Healer + Tank combo                                                                                                                                             |

#### Reference Games

Our Operator design draws inspiration from:

| Game                  | Inspiration Element                            | Our Implementation                                         |
| --------------------- | ---------------------------------------------- | ---------------------------------------------------------- |
| **Rainbow Six Siege** | Unique gadgets per operator                    | Active abilities with upgrade paths                        |
| **Apex Legends**      | Passive + Active ability combo                 | Dual ability system                                        |
| **The Finals**        | Class-based team dynamics (Light/Medium/Heavy) | 5 core classes with distinct roles                         |
| **Valorant**          | Ability cooldowns, weapon-first balance        | Cooldown-based abilities, gunplay matters more than powers |
| **Tarkov**            | High-stakes, tactical gameplay, gear fear      | Extraction focus, gear loss on death                       |
| **Hunt Showdown**     | Trait system, information warfare              | Passive abilities, audio-driven gameplay                   |

***

### Top-Down Viewport Design

In a top-down perspective, character readability is fundamentally different from first-person or third-person games. Players see operators from above at a steep camera angle (\~60 degrees), making **silhouette shape**, **color accent placement**, and **VFX radial clarity** the primary identification tools.

#### Silhouette Principles

| Principle               | Rule                                                               | Rationale                                                |
| ----------------------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| **Oversized Shoulders** | All operators use exaggerated shoulder/backpack proportions        | At 50% zoom, shoulder shape is the most visible feature  |
| **Headgear Silhouette** | Each class has a distinct headgear profile visible from above      | Helmet vs hood vs cap vs visor enables instant class ID  |
| **Weapon Readability**  | Primary weapon extends visibly from character model                | Players must see what weapon type an enemy carries       |
| **Color Accent Zones**  | Class accent color placed on shoulders and backpack (top surfaces) | Top surfaces receive the most camera exposure from above |
| **Distinct Body Mass**  | Tank = widest, Recon = narrowest, others scaled between            | Body width is the fastest subconscious class identifier  |

#### VFX Readability from Above

Ability VFX must read clearly from the top-down camera. All area-effect abilities use **radial indicators** projected onto the ground plane.

| VFX Type           | Design Rule                                         | Example                                          |
| ------------------ | --------------------------------------------------- | ------------------------------------------------ |
| **Area of Effect** | Circular ground decal with class-colored edge ring  | PULSE Nano Swarm = silver/green circle on ground |
| **Directional**    | Cone or line projected forward from operator        | BASTION Shield = 120-degree arc indicator        |
| **Self-Buff**      | Subtle glow on operator model + minimap icon change | MAMBA Combat Stim = orange body glow             |
| **Deployable**     | World-space model with pulsing radius indicator     | SUTURE Healing Drone = green pulsing circle      |
| **Status Applied** | Colored icon above affected character's head        | Burn = flame icon, Slow = chain icon             |

> \[!NOTE] All VFX must remain readable at **minimum zoom** (furthest camera distance). If a VFX effect is only visible at maximum zoom, it fails the readability requirement. See [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) for VFX particle budgets and performance tiers.

#### Class Color Identification (Top-Down)

| Class      | Accent Color | Hex     | Top-Surface Placement       | Visibility Distance |
| ---------- | ------------ | ------- | --------------------------- | ------------------- |
| Assault    | Orange       | #F97316 | Shoulder patches, ammo belt | 80+ units           |
| Support    | White/Green  | #22C55E | Cross armband, backpack     | 80+ units           |
| Recon      | Cyan         | #06B6D4 | Goggle glow, tech strips    | 60+ units           |
| Tank       | Steel Blue   | #3B82F6 | Shoulder plates, visor      | 100+ units          |
| Specialist | Amber        | #F59E0B | Utility markings, goggles   | 60+ units           |

See [Style Guide](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/StyleGuide/README.md) for full color coding specifications.

***

### Hitbox & Collision

All operators use **capsule-based collision** with a separate head hitbox sphere. Hitbox dimensions vary by class to reflect body mass differences visible from above.

#### Hitbox Dimensions

| Operator | Capsule Radius | Capsule Height | Head Sphere Radius | Collision Profile |
| -------- | -------------- | -------------- | ------------------ | ----------------- |
| MAMBA    | 40 cm          | 180 cm         | 14 cm              | Standard          |
| IGNITION | 36 cm          | 168 cm         | 13 cm              | Standard          |
| TARTARUS | 44 cm          | 190 cm         | 15 cm              | Standard          |
| SUTURE   | 38 cm          | 176 cm         | 14 cm              | Standard          |
| AEGIS    | 34 cm          | 164 cm         | 13 cm              | Standard          |
| SONAR    | 34 cm          | 170 cm         | 13 cm              | Slim              |
| MIRAGE   | 40 cm          | 182 cm         | 14 cm              | Slim              |
| OBSIDIAN | 32 cm          | 160 cm         | 12 cm              | Slim              |
| BASTION  | 48 cm          | 188 cm         | 15 cm              | Heavy             |
| GOLIATH  | 46 cm          | 186 cm         | 15 cm              | Heavy             |
| GLITCH   | 36 cm          | 175 cm         | 13 cm              | Standard          |
| PULSE    | 38 cm          | 172 cm         | 13 cm              | Standard          |

**Collision Profiles:**

* **Slim** — 10% smaller hitbox than body mesh for Recon class advantage
* **Standard** — Hitbox matches body mesh 1:1
* **Heavy** — 5% larger hitbox than body mesh (trade-off for Tank armor)

**Head Hitbox Rules:**

* Headshot multiplier: 2.0x (see [Combat](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Combat/README.md) for damage formulas)
* Head sphere is always at the top of the capsule, regardless of animation state
* From top-down view, head hitbox is the primary visible target — this is intentional

***

### Status Effect System

Abilities can apply status effects to operators. Each effect has a base duration modified by class resistances.

#### Status Effects

| Effect    | Icon           | Base Duration        | Source Abilities                                                | Visual Cue (Top-Down)                                       |
| --------- | -------------- | -------------------- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| **Stun**  | Lightning bolt | 1.5 seconds          | BASTION Shield Bash, Flashbang grenade                          | Character freezes, spark particles above head               |
| **Slow**  | Chain links    | 3.0 seconds          | PULSE Nano Swarm (Napalm Stick upgrade), IGNITION fire exit     | Movement trail turns blue, character model drags            |
| **Burn**  | Flame          | 5.0 seconds (15 DPS) | IGNITION Incendiary Rush, Molotov                               | Orange flame particles on character, smoke trail            |
| **EMP**   | Circuit break  | 4.0 seconds          | GLITCH EMP Blast                                                | Blue static particles, HUD distortion (self view)           |
| **Blind** | Eye cross      | 2.0 seconds          | Flashbang grenade, IGNITION Flashpoint upgrade                  | White flash on operator model (top-down: bright white glow) |
| **Mark**  | Crosshair      | 5.0 seconds          | SONAR UAV Scan, MIRAGE Motion Sensor, TARTARUS Predator upgrade | Red outline visible through walls and from above            |

#### Class Resistances

| Class      | Stun Resist | Slow Resist | Burn Resist | EMP Resist | Notes                                         |
| ---------- | ----------- | ----------- | ----------- | ---------- | --------------------------------------------- |
| Assault    | 0%          | 0%          | 0%          | 0%         | No resistances — pure offense                 |
| Support    | 0%          | 10%         | 0%          | 0%         | Slight slow resist for reaching downed allies |
| Recon      | 15%         | 0%          | 0%          | 0%         | Stun resist for evasion                       |
| Tank       | 25%         | 25%         | 10%         | 0%         | Broad physical resistance                     |
| Specialist | 0%          | 0%          | 0%          | 50%        | Half EMP duration — they build the tech       |

> \[!NOTE] Individual operator passives may further modify resistances. See each operator's "Expanded Combat Statistics" section for operator-specific modifiers.

***

### Stamina System

Sprinting consumes stamina. When stamina is depleted, operators cannot sprint until partial recovery.

#### Base Stamina

| Parameter                | Value       | Notes                                        |
| ------------------------ | ----------- | -------------------------------------------- |
| **Stamina Pool**         | 100         | Universal base                               |
| **Sprint Drain**         | 10/second   | 10 seconds of continuous sprint              |
| **Recovery Rate**        | 8/second    | Recovers while walking or idle               |
| **Recovery Delay**       | 1.5 seconds | Delay after sprinting before recovery starts |
| **Exhaustion Threshold** | 0           | Cannot sprint at 0 stamina                   |
| **Minimum to Sprint**    | 20          | Must have 20+ stamina to start sprinting     |

#### Class Stamina Modifiers

| Class      | Pool Modifier  | Drain Modifier  | Recovery Modifier | Net Sprint Duration |
| ---------- | -------------- | --------------- | ----------------- | ------------------- |
| Assault    | +20% (120)     | Standard (10/s) | +10% (8.8/s)      | 12.0 seconds        |
| Support    | Standard (100) | Standard (10/s) | Standard (8/s)    | 10.0 seconds        |
| Recon      | +10% (110)     | -10% (9/s)      | +20% (9.6/s)      | 12.2 seconds        |
| Tank       | -20% (80)      | +20% (12/s)     | -10% (7.2/s)      | 6.7 seconds         |
| Specialist | Standard (100) | Standard (10/s) | Standard (8/s)    | 10.0 seconds        |

**Design Intent:** Tank operators commit to positions. They cannot sprint long distances — choosing where to fight is critical. Recon operators can reposition frequently. Assault operators have the longest sprint for aggressive entry.

***

### Ability Interaction Matrix

When abilities collide, the following rules apply. This matrix defines **what happens when one ability meets another** — critical for balance and counterplay.

#### Deployable vs. Ability Interactions

| Deployable                  | EMP Blast         | Incendiary Rush                                                | Nano Swarm                            | Smoke Screen                      | Berserker Rage | UAV Scan                            |
| --------------------------- | ----------------- | -------------------------------------------------------------- | ------------------------------------- | --------------------------------- | -------------- | ----------------------------------- |
| **Healing Drone** (SUTURE)  | Destroyed         | Not affected                                                   | Not affected                          | Not affected                      | N/A            | Revealed                            |
| **Guardian Shield** (AEGIS) | Destroyed         | Fire does NOT pass through                                     | Swarm ignores shield (passes through) | Smoke passes through              | N/A            | Does not reveal shield users inside |
| **Motion Sensors** (MIRAGE) | Destroyed         | Destroyed by fire                                              | Not affected                          | Not affected                      | N/A            | N/A                                 |
| **UAV** (SONAR)             | Destroyed (falls) | Not affected (airborne)                                        | Not affected (airborne)               | Blocks scan LOS to ground targets | N/A            | N/A                                 |
| **Nano Swarm** (PULSE)      | Destroyed         | Fire burns through swarm (both damage stack on enemies inside) | N/A                                   | Smoke does not interact           | N/A            | Revealed                            |
| **Riot Shield** (BASTION)   | Disabled (5 sec)  | Fire does NOT pass through                                     | Swarm ignores shield                  | Smoke passes through              | N/A            | Does not reveal shielded operator   |

#### Buff vs. Debuff Interactions

| Buff/Ability                   | Can be EMP'd?               | Cleansed by Stim? | Blocked by Shield?                                    | Affected by Smoke?                                        |
| ------------------------------ | --------------------------- | ----------------- | ----------------------------------------------------- | --------------------------------------------------------- |
| **Combat Stim** (MAMBA)        | Yes — cancelled immediately | N/A (is the stim) | N/A                                                   | No                                                        |
| **Berserker Rage** (TARTARUS)  | Yes — cancelled immediately | No                | N/A                                                   | No                                                        |
| **Armor Overcharge** (GOLIATH) | Yes — bonus armor stripped  | No                | N/A                                                   | No                                                        |
| **Burn** (IGNITION)            | No — not tech-based         | No                | Guardian Shield blocks fire source, not existing burn | No                                                        |
| **Mark** (SONAR/MIRAGE)        | No — already applied        | No                | No                                                    | Smoke blocks NEW scans but does not remove existing marks |

***

### Operator Classes

#### Class Overview Matrix

| Class                                                                                                                      | Role                | Primary Stat  | Team Value | Solo Viability | Operators |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- | ---------- | -------------- | --------- |
| [**ASSAULT**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/README.md)       | Frontline Aggressor | Damage        | Medium     | High           | 3         |
| [**SUPPORT**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/README.md)       | Team Healer         | Healing       | Very High  | Low            | 2         |
| [**RECON**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/README.md)           | Intel Specialist    | Information   | High       | Very High      | 3         |
| [**TANK**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/README.md)             | Damage Sponge       | Survivability | High       | Medium         | 2         |
| [**SPECIALIST**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/README.md) | Tech Disruptor      | Utility       | High       | High           | 2         |

#### Unlock Progression

```
ACCOUNT LEVEL 1  -> Assault (MAMBA) - Free starter
ACCOUNT LEVEL 1  -> Support (SUTURE) - Free starter
ACCOUNT LEVEL 5  -> Assault (IGNITION) - 5,000 Credits or Quest
ACCOUNT LEVEL 8  -> Recon (SONAR) - 5,000 Credits or Quest
ACCOUNT LEVEL 10 -> Tank (BASTION) - 7,500 Credits or Quest
ACCOUNT LEVEL 12 -> Recon (MIRAGE) - 7,500 Credits or Quest
ACCOUNT LEVEL 15 -> Specialist (GLITCH) - 10,000 Credits or Quest
ACCOUNT LEVEL 18 -> Support (AEGIS) - 10,000 Credits or Quest
ACCOUNT LEVEL 20 -> Tank (GOLIATH) - 12,000 Credits or Quest
ACCOUNT LEVEL 22 -> Assault (TARTARUS) - 12,000 Credits or Quest
ACCOUNT LEVEL 25 -> Recon (OBSIDIAN) - 15,000 Credits or Quest
ACCOUNT LEVEL 28 -> Specialist (PULSE) - 15,000 Credits or Quest
```

**Design Intent:** Starter operators (MAMBA, SUTURE) represent the two core loops — killing and surviving. New classes unlock steadily to introduce complexity without overwhelming new players.

***

### Class Details

#### 1. ASSAULT CLASS — Frontline Aggressors

**Role:** High damage dealers who lead the charge into combat.

**Class Traits:**

* +10% Base Sprint Speed
* +5% Weapon Damage
* -10% Maximum Armor

**Operators:**

| Operator                                                                                                                                   | Codename | Ability         | Specialty            |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------- | --------------- | -------------------- |
| [Thuy "Mamba" Nguyen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Mamba/README.md)         | MAMBA    | Combat Stim     | Damage Amplification |
| [Ji-yoon "Ignition" Kwon](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Ignition/README.md)  | IGNITION | Incendiary Rush | Area Denial          |
| [Carlos "Tartarus" Mendes](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Tartarus/README.md) | TARTARUS | Berserker Rage  | Close Combat         |

[View All Assault Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/README.md)

***

#### 2. SUPPORT CLASS — Team Lifelines

**Role:** Keep teammates alive and enable sustained combat.

**Class Traits:**

* +20% Healing Item Effectiveness
* +15% Revive Speed
* -5% Movement Speed

**Operators:**

| Operator                                                                                                                                 | Codename | Ability         | Specialty         |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------- | ----------------- |
| [Tariq "Suture" Al-Sayed](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Suture/README.md)  | SUTURE   | Healing Drone   | Area Healing      |
| [Victoria "Aegis" Sterling](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Aegis/README.md) | AEGIS    | Guardian Shield | Damage Prevention |

[View All Support Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/README.md)

***

#### 3. RECON CLASS — Information Specialists

**Role:** Gather intel, scout enemy positions, and enable ambushes.

**Class Traits:**

* +15% Crouch Movement Speed
* -30% Footstep Volume
* -5% Maximum Health

**Operators:**

| Operator                                                                                                                                   | Codename | Ability        | Specialty      |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------- | -------------- | -------------- |
| [Kaito "Sonar" Nakamura](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Sonar/README.md)        | SONAR    | UAV Scan       | Area Reveal    |
| [Ananya "Mirage" Patel](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Mirage/README.md)        | MIRAGE   | Motion Sensors | Trap Detection |
| [Unit N-7 "Obsidian" "Nero"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Obsidian/README.md) | OBSIDIAN | Smoke Screen   | Visual Denial  |

[View All Recon Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/README.md)

***

#### 4. TANK CLASS — Frontline Defenders

**Role:** Absorb damage, hold positions, and protect teammates.

**Class Traits:**

* +25% Maximum Armor Capacity
* +10% Armor Damage Reduction
* -15% Sprint Speed

**Operators:**

| Operator                                                                                                                               | Codename | Ability          | Specialty          |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------- | ------------------ |
| [Mikhail "Bastion" Ivanov](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Bastion/README.md) | BASTION  | Riot Shield      | Frontal Protection |
| [Wei "Goliath" Chen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Goliath/README.md)       | GOLIATH  | Armor Overcharge | Team Defense       |

[View All Tank Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/README.md)

***

#### 5. SPECIALIST CLASS — Tech Disruptors

**Role:** Utility, control, counter enemy abilities.

**Class Traits:**

* +2 Inventory Slots
* +20% Gadget Interaction Speed
* -10% Weapon Accuracy

**Operators:**

| Operator                                                                                                                                | Codename | Ability    | Specialty      |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------- | -------------- |
| [Maya "Glitch" Torres](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Glitch/README.md) | GLITCH   | EMP Blast  | Ability Denial |
| [D-84 "Pulse" "Ohm"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Pulse/README.md)    | PULSE    | Nano Swarm | Area Control   |

[View All Specialist Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/README.md)

***

### Operator Balance Matrix

#### Combat Statistics

| Operator | Class      | Difficulty | Combat Power | Survivability | Utility | Team Value | Solo Viability | Total |
| -------- | ---------- | :--------: | :----------: | :-----------: | :-----: | :--------: | :------------: | :---: |
| MAMBA    | Assault    |     2/5    |     9/10     |      6/10     |   4/10  |    6/10    |      8/10      |   33  |
| IGNITION | Assault    |     3/5    |     8/10     |      5/10     |   6/10  |    7/10    |      7/10      |   33  |
| TARTARUS | Assault    |     4/5    |     10/10    |      4/10     |   3/10  |    5/10    |      9/10      |   31  |
| SUTURE   | Support    |     1/5    |     5/10     |      7/10     |   8/10  |    10/10   |      4/10      |   34  |
| AEGIS    | Support    |     3/5    |     4/10     |      8/10     |   9/10  |    10/10   |      3/10      |   34  |
| SONAR    | Recon      |     2/5    |     6/10     |      5/10     |   9/10  |    8/10    |      9/10      |   37  |
| MIRAGE   | Recon      |     4/5    |     7/10     |      5/10     |   8/10  |    7/10    |      8/10      |   35  |
| OBSIDIAN | Recon      |     5/5    |     5/10     |      6/10     |  10/10  |    8/10    |      7/10      |   36  |
| BASTION  | Tank       |     2/5    |     7/10     |     10/10     |   5/10  |    8/10    |      5/10      |   35  |
| GOLIATH  | Tank       |     3/5    |     6/10     |      9/10     |   7/10  |    9/10    |      4/10      |   35  |
| GLITCH   | Specialist |     4/5    |     5/10     |      6/10     |  10/10  |    7/10    |      7/10      |   35  |
| PULSE    | Specialist |     5/5    |     6/10     |      5/10     |   9/10  |    8/10    |      6/10      |   34  |

**Difficulty Key:** 1/5 = Beginner-friendly, 5/5 = Requires deep game knowledge and precise ability timing.

**Balance Philosophy:** No operator should exceed 8/10 in more than two categories. Total score across all categories should fall within 31-37 points to maintain parity. See [Gameplay Balance](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/README.md) for detailed tuning rules.

#### Counter Matrix

| Operator | Strong Against     | Weak Against       | Key Ability Interaction                                                   |
| -------- | ------------------ | ------------------ | ------------------------------------------------------------------------- |
| MAMBA    | SONAR, SUTURE      | BASTION, GLITCH    | Stim cancelled by EMP; stim out-damages SUTURE heal rate                  |
| IGNITION | OBSIDIAN, GOLIATH  | MIRAGE, PULSE      | Fire destroys Motion Sensors; fire + swarm stack damage on shared targets |
| TARTARUS | AEGIS, GLITCH      | BASTION, SUTURE    | Rage cancelled by EMP; can push through Guardian Shield                   |
| SUTURE   | All (Sustain)      | MAMBA, TARTARUS    | Drone destroyed by EMP; stim burst exceeds heal rate                      |
| AEGIS    | IGNITION, TARTARUS | GLITCH, MIRAGE     | Shield destroyed instantly by EMP; fire cannot pass through shield        |
| SONAR    | GOLIATH, PULSE     | MAMBA, OBSIDIAN    | Scan blocked by smoke; scan reveals all deployables                       |
| MIRAGE   | IGNITION, TARTARUS | GLITCH, AEGIS      | Sensors destroyed by EMP and fire; sensors detect Berserker approach      |
| OBSIDIAN | BASTION, MAMBA     | SONAR, PULSE       | Smoke blocks shield vision; smoke blocks UAV scan LOS                     |
| BASTION  | MAMBA, TARTARUS    | OBSIDIAN, GLITCH   | Shield disabled by EMP (5s); shield blocks fire and bullets               |
| GOLIATH  | IGNITION, MIRAGE   | SONAR, PULSE       | Overcharge armor stripped by EMP; absorbs fire DoT                        |
| GLITCH   | AEGIS, BASTION     | MAMBA, TARTARUS    | EMP destroys all deployables and disables active buffs                    |
| PULSE    | SONAR, MIRAGE      | IGNITION, OBSIDIAN | Swarm destroyed by EMP; swarm ignores shields (passes through)            |

**Reading the Counter Matrix:** "Strong Against" means the operator has an inherent advantage in a 1v1 scenario due to ability matchups. The "Key Ability Interaction" column explains WHY — this is critical for balance discussions. Skill always matters more than counters.

***

### Team Compositions

#### Recommended Squad Compositions (3-Player)

| Comp Name           | Composition                 | Playstyle             | Strength               | Weakness                  |
| ------------------- | --------------------------- | --------------------- | ---------------------- | ------------------------- |
| **Rush Meta**       | MAMBA + TARTARUS + SUTURE   | Aggressive push       | High damage, sustained | No intel, no area control |
| **Intel Control**   | SONAR + MIRAGE + GLITCH     | Information dominance | Never surprised        | Low damage output         |
| **Goliath Hold**    | BASTION + SUTURE + IGNITION | Defensive extraction  | Hard to push           | Slow rotations            |
| **Balanced**        | MAMBA + SUTURE + SONAR      | All-around            | Flexible               | No hard counter to Tanks  |
| **Stealth Extract** | OBSIDIAN + MIRAGE + PULSE   | Avoid combat          | Maximum loot, low risk | Loses direct fights       |

#### Duo Synergies

| Duo                | Synergy                     | Strategy                                |
| ------------------ | --------------------------- | --------------------------------------- |
| MAMBA + SUTURE     | Assault heals               | Aggressive pushing with sustain backup  |
| BASTION + TARTARUS | Tank leads, Assault follows | Shield creates opening, TARTARUS closes |
| SONAR + GLITCH     | Intel + Disable             | Full information control of engagement  |
| GOLIATH + AEGIS    | Double defense              | Nearly unkillable extraction fortress   |
| OBSIDIAN + MIRAGE  | Stealth duo                 | Silent map traversal, avoid all combat  |

***

### Operator Progression

#### Individual Leveling

**Max Level per Operator:** 50

| Level | Unlock                                         |
| ----- | ---------------------------------------------- |
| 1     | Base operator unlocked                         |
| 5     | Ability Upgrade Slot 1 (choose 1 of 3 options) |
| 10    | Cosmetic Skin 1                                |
| 15    | Stat Boost 1 (+5% Health)                      |
| 20    | Ability Upgrade Slot 2 (choose 1 of 3 options) |
| 25    | Cosmetic Skin 2                                |
| 30    | Stat Boost 2 (+5% Stamina)                     |
| 35    | Ability Upgrade Slot 3 (choose 1 of 3 options) |
| 40    | Elite Cosmetic Skin                            |
| 45    | Stat Boost 3 (+5% Sprint Speed)                |
| 50    | Prestige Cosmetics + Title                     |

#### Prestige System

After reaching Level 50, operators can be **Prestiged**:

* Reset to Level 1
* Gain Prestige Badge (visible to other players in lobby and kill feed)
* Unlock exclusive Prestige cosmetics per prestige level
* +5% XP bonus for that operator (stacks per prestige)
* Max Prestige: 5

**Prestige Rewards:**

| Prestige | Reward                                                |
| -------- | ----------------------------------------------------- |
| 1        | Bronze badge + weapon charm                           |
| 2        | Silver badge + unique skin                            |
| 3        | Gold badge + voice line pack                          |
| 4        | Diamond badge + animated banner                       |
| 5        | Obsidian badge + legendary title + unique kill effect |

***

### Cosmetic System

#### Customization Options

| Type             | Description                   | Acquisition                  |
| ---------------- | ----------------------------- | ---------------------------- |
| **Skins**        | Full operator visual change   | Credits, Battle Pass, Events |
| **Headgear**     | Helmets, hats, masks          | Credits, Battle Pass         |
| **Gloves**       | Hand cosmetics                | Credits only                 |
| **Weapon Skins** | Applied to equipped weapons   | Credits, Battle Pass         |
| **Emotes**       | Victory poses, taunts         | Battle Pass, Events          |
| **Kill Effects** | Visual effect on eliminations | Premium Currency only        |
| **Voice Packs**  | Alternate voice lines         | Premium Currency only        |

All cosmetics are purely visual — no gameplay advantage. See [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) for character model specifications and visual guidelines.

#### Rarity Tiers

| Tier      | Color          | Drop Rate | Purchase Price       |
| --------- | -------------- | --------- | -------------------- |
| Common    | Gray #9CA3AF   | 60%       | 500 Credits          |
| Uncommon  | Green #22C55E  | 25%       | 1,000 Credits        |
| Rare      | Blue #3B82F6   | 10%       | 2,500 Credits        |
| Epic      | Purple #A855F7 | 4%        | Premium only         |
| Legendary | Gold #EAB308   | 1%        | Battle Pass / Events |

***

### Future Operators (Roadmap)

#### Season 1 (Launch + 3 months)

| Operator     | Class      | Ability Preview                                       | Design Status |
| ------------ | ---------- | ----------------------------------------------------- | ------------- |
| **SHADOW**   | Recon      | Invisibility cloak (limited duration, breaks on fire) | Concept       |
| **ENGINEER** | Specialist | Deployable turret (limited ammo, hackable by GLITCH)  | Concept       |

#### Season 2 (6 months)

| Operator  | Class   | Ability Preview                                        | Design Status |
| --------- | ------- | ------------------------------------------------------ | ------------- |
| **PYRO**  | Assault | Fire damage specialist (upgraded Molotov, heat vision) | Concept       |
| **MERCY** | Support | Mass revive (long cooldown, partial health restore)    | Concept       |

#### Season 3+ (9 months+)

* New class consideration: **COMMANDER** (tactical calldowns — artillery markers, supply drops)
* Community-voted operator concepts (seasonal votes)
* Crossover event operators (licensed characters with unique abilities)

***

### Cross-References

| Topic             | Sutureument                                                                                                              | What It Covers                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Character visuals | [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) | Operator model specs, silhouette guide, poly budgets, cyberpunk elements |
| Character style   | [Style Guide](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/StyleGuide/README.md)     | Class color coding, gear layering system, top-down readability           |
| Audio design      | [Audio Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Audio/README.md)                 | Voice line recording specs, combat callout systems                       |
| Gameplay balance  | [Gameplay](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/README.md)                  | TTK, damage formulas, ability cooldown framework                         |
| UI representation | [HUD Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/UI_UX/HUD_Design/README.md)        | How operators display on HUD, teammate status panels                     |
