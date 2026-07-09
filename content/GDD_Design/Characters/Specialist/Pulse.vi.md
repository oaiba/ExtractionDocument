---
title: "PULSE - D-84 \"Ohm\""
type: docs
---

## Operator Profile

> *"My nanobots see everything. Feel everything. Control everything."*

### Basic Information

| Attribute       | giá trị               |
| :-------------- | :------------------ |
| **Real Name**   | D-84 "Ohm" |
| **Codename**    | PULSE |
| **Class**       | Specialist          |
| **Nationality** | German |
| **Age**         | 31                  |
| **Height**      | 173 cm (5'8")       |
| **Weight**      | 65 kg (143 lbs)     |

### Background

D-84 "Ohm" was a leading nanotechnology researcher at Cambridge University, pioneering medical applications for nanobots. Her breakthrough in programmable nano-swarms could have revolutionized medicine—until a pharmaceutical conglomerate stole her research và weaponized it.

khi attempts to expose them thông qua legal channels failed, Maya took matters into her own hands. She recreated her technology from memory và now uses it in the Exclusion Zone, proving that her creations can save lives—và end those who abuse power.

### Personality Traits

- **Brilliant** - Genius-level intellect
- **Driven** - Obsessed với proving her worth
- **Compassionate** - Uses tech to giúp, not just hurt
- **Vindictive** - Never forgets a wrong

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
| **Footstep Volume** | 95% | Standard — tactical sneakers |
| **Ability Audio Radius** | 25 meters | Swarm buzzing is moderate volume |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT |
| EMP | 0% | Nano Swarm destroyed by EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 36 cm radius, 168 cm height |
| **Head Sphere** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Slim build, nano-canister harness on chest, tech goggles |
| **Class Accent Zones** | Yellow (#EAB308) on harness strips và goggle glow |
| **Swarm VFX (Top-Down)** | Silver particle cloud on ground (6m radius), shimmering/pulsing |
| **Swarm Audio Radius** | 25m — persistent insect-like buzzing |

<!-- REF_IMAGE: PULSE top-down view — showing operator với Nano Swarm deployed, silver particle cloud hiển thị rõ from above as 6m radius shimmer -->

### Nano Swarm Stat Block

| Property | giá trị | ghi chú |
| :------- | :---- | :---- |
| **Swarm Radius** | 6 meters | Stationary (can be redirected) |
| **Swarm Height** | 3 meters | Covers ground to upper floor |
| **địch Damage** | 8 HP/second | Tick every 0.5s |
| **Ally Healing** | 4 HP/second | Half of damage rate |
| **địch Slow** | -20% movement | While in swarm |
| **Duration** | 12 seconds | Full lifetime |
| **EMP Vulnerability** | Dispersed instantly | primary counter |
| **Fire Interaction** | Not affected | Fire does not destroy nanobots |

### Difficulty Rating

**Difficulty: 4/5** — Swarm placement và redirection require spatial awareness. Dual-mục đích (damage + heal) means constant quyết định-making about positioning.


## Abilities

### Active Ability: Nano Swarm

> *"Deploy a cloud of nanobots that damages địch và heals allies in the area."*

| Property     | giá trị      |
| :----------- | :--------- |
| **Cooldown** | 90 seconds |
| **Duration** | 12 seconds |
| **Charges**  | 1          |

#### Effects

| Effect  | Target           | giá trị              |
| :------ | :--------------- | :----------------- |
| Damage  | địch in swarm | 8 HP/second        |
| Healing | Allies in swarm  | 4 HP/second        |
| Slow    | địch          | -20% movement      |
| Vision  | địch          | Reduced visibility |

#### Swarm Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **Swarm + EMP (GLITCH)** | Swarm dispersed instantly — primary counter |
| **Swarm + Fire (IGNITION)** | Both effects stack on địch in overlap zone |
| **Swarm + Smoke (OBSIDIAN)** | Swarm operates thông qua smoke normally |
| **Swarm + AEGIS Shield** | Swarm passes thông qua Guardian Shield |
| **Swarm + BASTION Shield** | Swarm ignores Riot Shield — passes thông qua |
| **Swarm + MIRAGE Sensors** | Swarm does not affect sensors |
| **Swarm + SUTURE Drone** | Swarm heal + drone heal stack on allies |

#### Top-Down Swarm VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| Swarm deploy | Canister crack, silver particles expand to 6m radius |
| Swarm active | Shimmering silver cloud on ground, semi-transparent |
| địch in swarm | Red damage particles trail toward địch |
| Ally in swarm | Green healing particles trail toward ally |
| Swarm redirected | Cloud moves toward new target position |
| Swarm ending | Particles settle downward, shimmer fades |
| Swarm EMP'd | Brief blue flash, all particles scatter và vanish |


| Property   | giá trị                          |
| :--------- | :----------------------------- |
| Radius     | 6 meters                       |
| Height     | 3 meters                       |
| Mobility   | Stationary (can be redirected) |
| Visibility | Cloud of silver particles      |

#### Tactical Uses

| cách dùng Case             | Strategy                          |
| :------------------- | :-------------------------------- |
| **Area Denial**      | Block chokepoint                  |
| **Combat Support**   | Heal team while damaging địch  |
| **Extraction Hold**  | Place over extraction zone        |
| **Chase Prevention** | Swarm behind you while retreating |

#### upgrade Slots

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
| **Corrosive Bots**   | địch in swarm take +10% damage |
| **Mobile Swarm**     | Swarm slowly follows PULSE (1 m/s) |

**Slot 3 (Level 35):**
| Option                | Effect                           |
| :-------------------- | :------------------------------- |
| **Symbiosis**         | PULSE heals double in own swarm   |
| **giáp Dissolution** | Swarm reduces địch giáp by 20% |
| **Dual Deployment**   | 2 smaller swarms instead of 1    |

---

### Passive Ability: Nano-Infused

> *"The nanobots in her blood work constantly."*

| Condition               | Effect                            |
| :---------------------- | :-------------------------------- |
| Out of combat 5 seconds | Regenerate 2 HP/second            |
| In own swarm            | +10% movement speed               |
| Damaged by địch swarm  | Take 50% less damage (resistance) |

**Design Intent:** Self-sustaining operator who excels in attrition warfare.

---

## Loadout

### Default Loadout

| Slot          | Item                        | ghi chú                         |
| :------------ | :-------------------------- | :---------------------------- |
| **primary**   | P90                         | High capacity                 |
| **secondary** | G17 Pistol                  | Standard                      |
| **Tactical**  | Nano Grenades ×2, Medkit ×1 | Extra swarms + backup healing |
| **giáp**     | Medium Vest                 | 50 giáp                      |

### Recommended Loadouts

**Full Nano:**
| Slot      | Item            | Why               |
| :-------- | :-------------- | :---------------- |
| primary   | MP7             | Compact, accurate |
| secondary | Machine Pistol  | CQB backup        |
| Tactical  | Nano Grenade ×3 | Maximum coverage  |

**Survival Focus:**
| Slot      | Item               | Why                      |
| :-------- | :----------------- | :----------------------- |
| primary   | Vector             | Fast TTK                 |
| secondary | G17                | Reliable                 |
| Tactical  | Medkit ×2, Nano ×1 | Passive + active healing |

---

## Playstyle Guide

### Role in Team

**primary Role:** Area Control
- Place swarms at chính locations
- Zone địch away from objectives
- Provide ambient healing

**secondary Role:** Hybrid Support
- Not a full healer, nhưng supplements SUTURE/AEGIS
- Self-sustaining flanker
- Extended presence in combat

### Swarm Placement

**Good Placement:**
- Chokepoints
- Objectives (extraction, loot)
- Behind cover for healing
- Entry points to slow địch

**Bad Placement:**
- Wide open areas (easy to avoid)
- Where team won't benefit
- trước địch arrive (waste duration)

---

## Matchups

### Favorable Matchups

| Opponent    | Why Favorable                | Tactic                 |
| :---------- | :--------------------------- | :--------------------- |
| **MAMBA**   | Swarm slows his rush         | Fight in swarm         |
| **TARTARUS**   | Slows his CQB approach       | Keep distance in swarm |
| **BASTION** | Swarm damages thông qua shield | Surround với nano     |

### Even Matchups

| Opponent     | ghi chú               | chính to Winning             |
| :----------- | :------------------ | :------------------------- |
| **SUTURE**      | Both sustain        | Your damage vs his healing |
| **GOLIATH** | giáp vs nano       | Focus single target        |
| **MIRAGE**  | Control specialists | Map control battle         |

### Unfavorable Matchups

| Opponent    | Why Difficult         | Counter Strategy   |
| :---------- | :-------------------- | :----------------- |
| **GLITCH**  | EMP destroys swarm    | Deploy sau EMP   |
| **IGNITION**   | Fire damages you back | Avoid fire zones   |
| **SONAR** | Can see you in swarm  | Move unpredictably |

---

## Voice Lines

### Combat

| Trigger                 | Line                                |
| :---------------------- | :---------------------------------- |
| Ability Activation      | "Swarm deployed. They're learning." |
| địch in Swarm          | "They're feeling it now."           |
| Ally in Swarm (Healing) | "Let the nanobots work."            |
| Kill                    | "Science wins."                     |
| Reviving                | "The bots will stabilize you."      |

### Personality

| Trigger            | Line                               |
| :----------------- | :--------------------------------- |
| Match Start        | "Nanobots online. Let's begin."    |
| Extraction success | "Research successful. Extracting." |
| Low máu         | "Bots are working on it."          |

---

## Cosmetics

### Default Appearance

- **Outfit:** White lab coat over lightweight tactical vest, nanobot canisters on belt
- **Headgear:** High-tech visor / AR glasses với data readouts
- **Gloves:** White latex gloves (medical/scientific aesthetic)
- **tính năng:** Short natural hair, confident stance, silver nano-trace patterns on forearms

<!-- REF_IMAGE: PULSE default skin — top-down view showing lab coat over vest silhouette, AR glasses, nano canisters hiển thị rõ on belt, silver-particle aura effect -->

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
| **Silver Trace** | Faint silver nano-patterns hiển thị rõ on forearms (the bots in her blood) |

---

## Lore Connections

### Relationships

| nhân vật | Relationship |
| :-------- | :----------- |
| **GLITCH** | Fellow outcasts, share tech knowledge — closest friend/collaborator |
| **SUTURE** | Medical debate partners — SUTURE uses traditional medicine, PULSE uses nanotech. Mutual professional respect |
| **AEGIS** | Faith vs Science discussions — AEGIS prays, PULSE programs. Surprisingly good friends |
| **MAMBA** | MAMBA finds her nanobots unsettling — "Keep those things away from me" |

### Story Hooks

- Hunting the executives who stole her research at the pharmaceutical conglomerate
- Developing new nanobot applications in the field (quest chain: test prototypes for rewards)
- Secretly working on a cure for SUTURE's chronic condition using nano-medicine
- Discovered that Corporation is mass-producing her stolen nano-swarm tech for military cách dùng

---

## Design ghi chú (For Developers)

### Balance Considerations

- Swarm is the only dual-mục đích ability (damage + heal) — monitor effective healing per match
- Stationary deployment is the primary weakness — địch can simply walk away
- Mobile Swarm upgrade (Slot 2) should cap at 1 m/s movement — too fast makes it oppressive
- Dual Deployment (Slot 3) splits radius — 2x 4m swarms instead of 1x 6m, total area is less
- EMP hard-counters Nano Swarm — this is intentional và không nên be changed
- Self-healing passive (2 HP/sec out of combat) prevents chip-damage attrition — 5 second delay is critical
- Symbiosis upgrade (double heal in own swarm) makes PULSE nearly unkillable in swarm — she must sacrifice other Slot 3 options

### Ghi Chú Kỹ Thuật

| hệ thống | ghi chú |
| :----- | :---- |
| Swarm Particles | GPU particle hệ thống, limit 5000 particles per swarm |
| Damage Tick | Every 0.5 seconds (8 x 2 = 16 ticks per 12s duration) |
| Ally/địch Detection | Server-side detection, client-side visual feedback |
| Dual Swarm | Each swarm is independent particle hệ thống |

### Animation yêu cầu

- Swarm deploy animation (0.7 seconds — throw canister, nanobots emerge)
- Swarm active VFX (silver particle cloud, shimmering, semi-transparent)
- Healing VFX (green particle trails toward allies in swarm)
- Damage VFX (red particle trails targeting địch in swarm)
- Death animation: nanobots visibly scatter from body (dramatic tech failure)

### Audio yêu cầu

| Sound | ghi chú |
| :---- | :---- |
| Swarm deploy | Canister crack + rising electronic buzz |
| Swarm active | Persistent insect-like buzzing (louder near center) |
| Swarm healing | Soft harmonic hum overlay (ally feedback) |
| Swarm damage | Aggressive buzz + crackling (địch perspective) |
| Swarm end | Descending buzz, particles settle |
| Footsteps | Standard weight — tactical sneakers |

### Top-Down cụ thể ghi chú

- Swarm silver cloud phải được hiển thị rõ at minimum zoom — area denial information for both teams
- Red (địch damage) và green (ally heal) particle streams provide instant team understanding from above
- Swarm cloud nên được clearly distinct from OBSIDIAN smoke: silver/shimmering vs gray/opaque
- Dual Deployment upgrade splits into 2x 4m swarms — each nên được independently hiển thị rõ
- Swarm redirection animation should show cloud flowing toward new position (1-2 second travel thời gian)
- -10% vũ khí accuracy (Specialist class) means PULSE should avoid straight gunfights
