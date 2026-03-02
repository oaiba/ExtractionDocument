---
title: "PULSE - D-84 \"Ohm\""
type: docs
---

## Operator Profile

> *"My nanobots see everything. Feel everything. Control everything."*

### Basic Information

| Attribute       | Value               |
| :-------------- | :------------------ |
| **Real Name**   | D-84 "Ohm" |
| **Codename**    | PULSE |
| **Class**       | Specialist          |
| **Nationality** | German |
| **Age**         | 31                  |
| **Height**      | 173 cm (5'8")       |
| **Weight**      | 65 kg (143 lbs)     |

### Background

D-84 "Ohm" was a leading nanotechnology researcher at Cambridge University, pioneering medical applications for nanobots. Her breakthrough in programmable nano-swarms could have revolutionized medicine—until a pharmaceutical conglomerate stole her research and weaponized it.

When attempts to expose them through legal channels failed, Maya took matters into her own hands. She recreated her technology from memory and now uses it in the Exclusion Zone, proving that her creations can save lives—and end those who abuse power.

### Personality Traits

- **Brilliant** - Genius-level intellect
- **Driven** - Obsessed with proving her worth
- **Compassionate** - Uses tech to help, not just hurt
- **Vindictive** - Never forgets a wrong

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
| **Footstep Volume** | 95% | Standard — tactical sneakers |
| **Ability Audio Radius** | 25 meters | Swarm buzzing is moderate volume |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT |
| EMP | 0% | Nano Swarm destroyed by EMP |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 36 cm radius, 168 cm height |
| **Head Sphere** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Slim build, nano-canister harness on chest, tech goggles |
| **Class Accent Zones** | Yellow (#EAB308) on harness strips and goggle glow |
| **Swarm VFX (Top-Down)** | Silver particle cloud on ground (6m radius), shimmering/pulsing |
| **Swarm Audio Radius** | 25m — persistent insect-like buzzing |

<!-- REF_IMAGE: PULSE top-down view — showing operator with Nano Swarm deployed, silver particle cloud visible from above as 6m radius shimmer -->

### Nano Swarm Stat Block

| Property | Value | Notes |
| :------- | :---- | :---- |
| **Swarm Radius** | 6 meters | Stationary (can be redirected) |
| **Swarm Height** | 3 meters | Covers ground to upper floor |
| **Enemy Damage** | 8 HP/second | Tick every 0.5s |
| **Ally Healing** | 4 HP/second | Half of damage rate |
| **Enemy Slow** | -20% movement | While in swarm |
| **Duration** | 12 seconds | Full lifetime |
| **EMP Vulnerability** | Dispersed instantly | Primary counter |
| **Fire Interaction** | Not affected | Fire does not destroy nanobots |

### Difficulty Rating

**Difficulty: 4/5** — Swarm placement and redirection require spatial awareness. Dual-purpose (damage + heal) means constant decision-making about positioning.


## Abilities

### Active Ability: Nano Swarm

> *"Deploy a cloud of nanobots that damages enemies and heals allies in the area."*

| Property     | Value      |
| :----------- | :--------- |
| **Cooldown** | 90 seconds |
| **Duration** | 12 seconds |
| **Charges**  | 1          |

#### Effects

| Effect  | Target           | Value              |
| :------ | :--------------- | :----------------- |
| Damage  | Enemies in swarm | 8 HP/second        |
| Healing | Allies in swarm  | 4 HP/second        |
| Slow    | Enemies          | -20% movement      |
| Vision  | Enemies          | Reduced visibility |

#### Swarm Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **Swarm + EMP (GLITCH)** | Swarm dispersed instantly — primary counter |
| **Swarm + Fire (IGNITION)** | Both effects stack on enemies in overlap zone |
| **Swarm + Smoke (OBSIDIAN)** | Swarm operates through smoke normally |
| **Swarm + AEGIS Shield** | Swarm passes through Guardian Shield |
| **Swarm + BASTION Shield** | Swarm ignores Riot Shield — passes through |
| **Swarm + MIRAGE Sensors** | Swarm does not affect sensors |
| **Swarm + SUTURE Drone** | Swarm heal + drone heal stack on allies |

#### Top-Down Swarm VFX

| State | VFX From Above |
| :---- | :------------- |
| Swarm deploy | Canister crack, silver particles expand to 6m radius |
| Swarm active | Shimmering silver cloud on ground, semi-transparent |
| Enemy in swarm | Red damage particles trail toward enemy |
| Ally in swarm | Green healing particles trail toward ally |
| Swarm redirected | Cloud moves toward new target position |
| Swarm ending | Particles settle downward, shimmer fades |
| Swarm EMP'd | Brief blue flash, all particles scatter and vanish |


| Property   | Value                          |
| :--------- | :----------------------------- |
| Radius     | 6 meters                       |
| Height     | 3 meters                       |
| Mobility   | Stationary (can be redirected) |
| Visibility | Cloud of silver particles      |

#### Tactical Uses

| Use Case             | Strategy                          |
| :------------------- | :-------------------------------- |
| **Area Denial**      | Block chokepoint                  |
| **Combat Support**   | Heal team while damaging enemies  |
| **Extraction Hold**  | Place over extraction zone        |
| **Chase Prevention** | Swarm behind you while retreating |

#### Upgrade Slots

**Slot 1 (Level 5):**
| Option                | Effect                           |
| :-------------------- | :------------------------------- |
| **Extended Swarm**    | Duration +6 seconds (18s total)  |
| **Quick Replication** | Cooldown -20 seconds (70s total) |
| **Dense Cloud**       | Damage +3 HP/sec (11 total)      |

**Slot 2 (Level 20):**
| Option               | Effect                            |
| :------------------- | :-------------------------------- |
| **Medical Protocol** | Healing +3 HP/sec (7 total)       |
| **Corrosive Bots**   | Enemies in swarm take +10% damage |
| **Mobile Swarm**     | Swarm slowly follows PULSE (1 m/s) |

**Slot 3 (Level 35):**
| Option                | Effect                           |
| :-------------------- | :------------------------------- |
| **Symbiosis**         | PULSE heals double in own swarm   |
| **Armor Dissolution** | Swarm reduces enemy armor by 20% |
| **Dual Deployment**   | 2 smaller swarms instead of 1    |

---

### Passive Ability: Nano-Infused

> *"The nanobots in her blood work constantly."*

| Condition               | Effect                            |
| :---------------------- | :-------------------------------- |
| Out of combat 5 seconds | Regenerate 2 HP/second            |
| In own swarm            | +10% movement speed               |
| Damaged by enemy swarm  | Take 50% less damage (resistance) |

**Design Intent:** Self-sustaining operator who excels in attrition warfare.

---

## Loadout

### Default Loadout

| Slot          | Item                        | Notes                         |
| :------------ | :-------------------------- | :---------------------------- |
| **Primary**   | P90                         | High capacity                 |
| **Secondary** | G17 Pistol                  | Standard                      |
| **Tactical**  | Nano Grenades ×2, Medkit ×1 | Extra swarms + backup healing |
| **Armor**     | Medium Vest                 | 50 armor                      |

### Recommended Loadouts

**Full Nano:**
| Slot      | Item            | Why               |
| :-------- | :-------------- | :---------------- |
| Primary   | MP7             | Compact, accurate |
| Secondary | Machine Pistol  | CQB backup        |
| Tactical  | Nano Grenade ×3 | Maximum coverage  |

**Survival Focus:**
| Slot      | Item               | Why                      |
| :-------- | :----------------- | :----------------------- |
| Primary   | Vector             | Fast TTK                 |
| Secondary | G17                | Reliable                 |
| Tactical  | Medkit ×2, Nano ×1 | Passive + active healing |

---

## Playstyle Guide

### Role in Team

**Primary Role:** Area Control
- Place swarms at key locations
- Zone enemies away from objectives
- Provide ambient healing

**Secondary Role:** Hybrid Support
- Not a full healer, but supplements SUTURE/AEGIS
- Self-sustaining flanker
- Extended presence in combat

### Swarm Placement

**Good Placement:**
- Chokepoints
- Objectives (extraction, loot)
- Behind cover for healing
- Entry points to slow enemies

**Bad Placement:**
- Wide open areas (easy to avoid)
- Where team won't benefit
- Before enemies arrive (waste duration)

---

## Matchups

### Favorable Matchups

| Opponent    | Why Favorable                | Tactic                 |
| :---------- | :--------------------------- | :--------------------- |
| **MAMBA**   | Swarm slows his rush         | Fight in swarm         |
| **TARTARUS**   | Slows his CQB approach       | Keep distance in swarm |
| **BASTION** | Swarm damages through shield | Surround with nano     |

### Even Matchups

| Opponent     | Notes               | Key to Winning             |
| :----------- | :------------------ | :------------------------- |
| **SUTURE**      | Both sustain        | Your damage vs his healing |
| **GOLIATH** | Armor vs nano       | Focus single target        |
| **MIRAGE**  | Control specialists | Map control battle         |

### Unfavorable Matchups

| Opponent    | Why Difficult         | Counter Strategy   |
| :---------- | :-------------------- | :----------------- |
| **GLITCH**  | EMP destroys swarm    | Deploy after EMP   |
| **IGNITION**   | Fire damages you back | Avoid fire zones   |
| **SONAR** | Can see you in swarm  | Move unpredictably |

---

## Voice Lines

### Combat

| Trigger                 | Line                                |
| :---------------------- | :---------------------------------- |
| Ability Activation      | "Swarm deployed. They're learning." |
| Enemy in Swarm          | "They're feeling it now."           |
| Ally in Swarm (Healing) | "Let the nanobots work."            |
| Kill                    | "Science wins."                     |
| Reviving                | "The bots will stabilize you."      |

### Personality

| Trigger            | Line                               |
| :----------------- | :--------------------------------- |
| Match Start        | "Nanobots online. Let's begin."    |
| Extraction Success | "Research successful. Extracting." |
| Low Health         | "Bots are working on it."          |

---

## Cosmetics

### Default Appearance

- **Outfit:** White lab coat over lightweight tactical vest, nanobot canisters on belt
- **Headgear:** High-tech visor / AR glasses with data readouts
- **Gloves:** White latex gloves (medical/scientific aesthetic)
- **Features:** Short natural hair, confident stance, silver nano-trace patterns on forearms

<!-- REF_IMAGE: PULSE default skin — top-down view showing lab coat over vest silhouette, AR glasses, nano canisters visible on belt, silver-particle aura effect -->

### Unlockable Skins

| Skin | Rarity | Unlock |
| :--- | :----- | :----- |
| **Lab Technician** | Common | Level 10 |
| **Biohazard** | Uncommon | 1,000 Credits |
| **Nanosuit** | Rare | Level 25 |
| **Synthwave** | Epic | Battle Pass S2 |
| **Singularity** | Legendary | Season 4 Event |

### Signature Items

| Item | Description |
| :--- | :---------- |
| **Nano Canisters** | Glowing silver canisters on belt harness |
| **Cambridge Pin** | University crest pin on lab coat lapel |
| **Silver Trace** | Faint silver nano-patterns visible on forearms (the bots in her blood) |

---

## Lore Connections

### Relationships

| Character | Relationship |
| :-------- | :----------- |
| **GLITCH** | Fellow outcasts, share tech knowledge — closest friend/collaborator |
| **SUTURE** | Medical debate partners — SUTURE uses traditional medicine, PULSE uses nanotech. Mutual professional respect |
| **AEGIS** | Faith vs Science discussions — AEGIS prays, PULSE programs. Surprisingly good friends |
| **MAMBA** | MAMBA finds her nanobots unsettling — "Keep those things away from me" |

### Story Hooks

- Hunting the executives who stole her research at the pharmaceutical conglomerate
- Developing new nanobot applications in the field (quest chain: test prototypes for rewards)
- Secretly working on a cure for SUTURE's chronic condition using nano-medicine
- Discovered that Corporation is mass-producing her stolen nano-swarm tech for military use

---

## Design Notes (For Developers)

### Balance Considerations

- Swarm is the only dual-purpose ability (damage + heal) — monitor effective healing per match
- Stationary deployment is the primary weakness — enemies can simply walk away
- Mobile Swarm upgrade (Slot 2) should cap at 1 m/s movement — too fast makes it oppressive
- Dual Deployment (Slot 3) splits radius — 2x 4m swarms instead of 1x 6m, total area is less
- EMP hard-counters Nano Swarm — this is intentional and should NOT be changed
- Self-healing passive (2 HP/sec out of combat) prevents chip-damage attrition — 5 second delay is critical
- Symbiosis upgrade (double heal in own swarm) makes PULSE nearly unkillable in swarm — she must sacrifice other Slot 3 options

### Technical Notes

| System | Notes |
| :----- | :---- |
| Swarm Particles | GPU particle system, limit 5000 particles per swarm |
| Damage Tick | Every 0.5 seconds (8 x 2 = 16 ticks per 12s duration) |
| Ally/Enemy Detection | Server-side detection, client-side visual feedback |
| Dual Swarm | Each swarm is independent particle system |

### Animation Requirements

- Swarm deploy animation (0.7 seconds — throw canister, nanobots emerge)
- Swarm active VFX (silver particle cloud, shimmering, semi-transparent)
- Healing VFX (green particle trails toward allies in swarm)
- Damage VFX (red particle trails targeting enemies in swarm)
- Death animation: nanobots visibly scatter from body (dramatic tech failure)

### Audio Requirements

| Sound | Notes |
| :---- | :---- |
| Swarm deploy | Canister crack + rising electronic buzz |
| Swarm active | Persistent insect-like buzzing (louder near center) |
| Swarm healing | Soft harmonic hum overlay (ally feedback) |
| Swarm damage | Aggressive buzz + crackling (enemy perspective) |
| Swarm end | Descending buzz, particles settle |
| Footsteps | Standard weight — tactical sneakers |

### Top-Down Specific Notes

- Swarm silver cloud must be visible at minimum zoom — area denial information for both teams
- Red (enemy damage) and green (ally heal) particle streams provide instant team understanding from above
- Swarm cloud should be clearly distinct from OBSIDIAN smoke: silver/shimmering vs gray/opaque
- Dual Deployment upgrade splits into 2x 4m swarms — each should be independently visible
- Swarm redirection animation should show cloud flowing toward new position (1-2 second travel time)
- -10% weapon accuracy (Specialist class) means PULSE should avoid straight gunfights

