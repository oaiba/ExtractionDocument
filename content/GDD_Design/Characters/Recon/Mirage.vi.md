---
title: "MIRAGE - Ananya Patel"
type: docs
---

## Operator Profile

> *"You think you're the hunter? You're already in my trap."*

### Basic Information

| Attribute | giá trị |
| :-------- | :---- |
| **Real Name** | Ananya Patel |
| **Codename** | MIRAGE |
| **Class** | Recon |
| **Nationality** | Indian |
| **Age** | 44 |
| **Height** | 175 cm (5'9") |
| **Weight** | 72 kg (159 lbs) |

<!-- REF_IMAGE: MIRAGE operator portrait — stocky build, tactical vest với sensor nodes, cold expression, cyberpunk utility belt với motion sensors -->

### Background

Viktor Volkov spent 20 years in FSB counter-intelligence, specializing in catching foreign spies on Russian soil. His elaborate trap networks và patient hunting style earned him the nickname "The Spider" among those who feared him.

sau growing disillusioned với the corruption eating Russia from within, Viktor disappeared — along với several classified files. Now he uses his expertise in the Exclusion Zone, setting traps for those foolish enough to wander into his web.

### Personality Traits

- **Patient** — Can wait hours for the perfect moment
- **Methodical** — Everything follows a plan
- **Cynical** — Believes everyone is corrupt
- **Protective** — Treats teammates like assets to preserve

---

## Combat Statistics

### Base Stats

| Stat | giá trị | Class Modifier | Final |
| :--- | :---- | :------------- | :---- |
| **máu** | 100 HP | -5% | 95 HP |
| **giáp** | 30 | - | 30 |
| **Sprint Speed** | 5.5 m/s | - | 5.5 m/s |
| **Crouch Speed** | 2.0 m/s | +15% | 2.3 m/s |
| **Footstep Volume** | 100% | -30% | 70% |

### Damage Modifiers

| Condition | Modifier |
| :-------- | :------- |
| Base vũ khí Damage | +0% (no class bonus) |
| Trap-assisted kill | +15 bonus damage from Shock Trap (upgrade) |
| Headshot Multiplier | 2.0x |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 110 | +10% (Recon class) |
| **Sprint Drain** | 9/second | -10% (Recon class) |
| **Recovery Rate** | 9.6/second | +20% (Recon class) |
| **Net Sprint Duration** | 12.2 seconds | Best efficiency |
| **Footstep Volume** | 70% | -30% (Recon class trait) |
| **Ability Audio Radius** | 5 meters | Sensors are nearly silent khi deployed |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT — sensors destroyed by fire |
| EMP | 0% | All sensors destroyed instantly by EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 40 cm radius, 182 cm height |
| **Head Sphere** | 14 cm radius |
| **Collision Profile** | Slim (-10% from mesh) |
| **Silhouette From Above** | Medium-slim build, tech harness hiển thị rõ, sensor pouches on belt |
| **Class Accent Zones** | Cyan (#06B6D4) on goggle glow và harness strips |
| **Sensor VFX (Top-Down)** | Small blinking devices on ground, 8m detection radius shown as faint circle khi ally walks near |
| **Sensor Audio** | Nearly silent — <5m detection range for địch |

<!-- REF_IMAGE: MIRAGE top-down view — showing operator với 3 motion sensors deployed, detection radius circles hiển thị rõ from above -->

### Motion Sensor Stat Block

| Property | giá trị | ghi chú |
| :------- | :---- | :---- |
| **Sensors Per Activation** | 3 | Deploy individually |
| **Detection Range** | 8 meters each | Overlapping for full coverage |
| **Sensor HP** | 20 | One-shot destroyable |
| **Duration** | Permanent | Until destroyed hoặc match end |
| **Mark Duration** | 4 seconds | sau detection |
| **EMP Vulnerability** | Destroyed instantly | primary counter |
| **Fire Vulnerability** | Destroyed on contact | secondary counter |
| **Visibility** | Subtle blinking light | Camo Sensors upgrade removes this |

### Difficulty Rating

**Difficulty: 4/5** — Sensor placement và coverage optimization require deep map knowledge. Trap Sense passive demands awareness of địch Recon setups.


## Abilities

### Active Ability: Motion Sensor Network

> *"Deploy interconnected sensors that detect và mark địch."*

| Property | giá trị |
| :------- | :---- |
| **Cooldown** | 60 seconds |
| **Duration** | Until destroyed hoặc match end |
| **Charges** | 3 sensors per activation |

#### Effects

| Effect | giá trị | ghi chú |
| :----- | :---- | :---- |
| Detection Range | 8 meters per sensor | Overlapping coverage best |
| Sensor HP | 20 | Destroyable by gunfire hoặc EMP |
| Alert Type | Audio + Visual ping | Directional indicator on HUD |
| Mark Duration | 4 seconds sau detection | địch hiển thị rõ thông qua walls |

#### Sensor Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **Sensor + EMP (GLITCH)** | All sensors in EMP radius destroyed instantly |
| **Sensor + Fire (IGNITION)** | Sensors destroyed by fire contact |
| **Sensor + Nano Swarm (PULSE)** | Sensors not affected by swarm |
| **Sensor + UAV Scan (SONAR)** | N/A — both are intel abilities |
| **Sensor + Smoke (OBSIDIAN)** | Sensors still detect thông qua smoke |
| **Sensor + TARTARUS Rage** | Sensors detect raging TARTARUS (louder footsteps trigger faster) |

#### Top-Down Sensor VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| Sensor deploy | Brief cyan flash on landing point |
| Sensor active | Small blinking device on ground (friendly: green glow, địch: not hiển thị rõ unless detected) |
| Sensor triggered | Red pulse expanding from sensor (8m radius flash), alarm chime |
| Sensor destroyed | Brief electrical spark + pop |


| Location | Effectiveness |
| :------- | :------------ |
| Doorways | High — Catches entries |
| Corners | High — Catches flanks |
| Behind cover | Medium — Late cảnh báo |
| Open areas | Low — Easy to spot/avoid |

#### upgrade Slots

**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extra Sensors** | 5 sensors per activation |
| **Hardened** | Sensor HP +15 (35 total) |
| **Wide Angle** | Detection range +3 meters (11m total) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **Slow Field** | Detected địch slowed 15% for 2 seconds |
| **Silent Alarm** | địch do not know they triggered sensor |
| **Networked** | nếu one sees địch, all mark them |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Shock Trap** | Detected địch take 15 damage |
| **Camo Sensors** | Sensors are nearly invisible |
| **Recall** | Can pick up sensors to redeploy |

---

### Passive Ability: Trap Sense

> *"trải nghiệm makes you recognize danger."*

| Condition | Effect |
| :-------- | :----- |
| Near địch trap/sensor | HUD cảnh báo (10m range) |
| Crouch detecting | Can see trap outline thông qua walls |
| Destroy địch trap | Gain 5-second địch position reveal |

**Design Intent:** MIRAGE is the anti-trap specialist. While SONAR provides active intel thông qua scanning, MIRAGE provides persistent, passive territorial control. He is the defensive Recon.

---

## Loadout

### Default Loadout

| Slot | Item | ghi chú |
| :--- | :--- | :---- |
| **primary** | AK-74u (Suppressed) | Russian reliability |
| **secondary** | Makarov Pistol | Soviet classic |
| **Tactical** | Motion Sensors x3, Claymore x1 | Layered traps |
| **giáp** | Light Vest | 30 giáp points |

### Recommended Loadouts

**The Spider's Web (Defensive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | Saiga-12 Shotgun | Close range punishment for trapped địch |
| secondary | Makarov Pistol | Backup |
| Tactical | Motion Sensors x3, Trip Mine x1 | Maximum area denial |

**Active Hunter (Aggressive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | AS Val (Suppressed) | Accurate, suppressed, mid-range |
| secondary | Stun Grenades x2 | Disable sau sensor trigger |
| Tactical | Motion Sensors x3 | Early cảnh báo while pushing |

---

## Playstyle Guide

### Role in Team

**primary Role:** Area Denial / Early cảnh báo
- Set sensor perimeters around objectives
- Alert team to incoming flanks
- Control chokepoints với trap + vũ khí combos

**secondary Role:** Counter-Intel
- Detect và destroy địch traps
- Deny SONAR scans by detecting sensors
- rõ buildings ahead of team push

### Combat Loop

```
1. Arrive at objective / extraction zone
2. Deploy 3 sensors at key entry points
3. Hold position and wait for triggers
4. When sensor trips — pre-aim the marked location
5. Engage with positional advantage (you know, they do not)
6. Redeploy sensors as they are destroyed
7. Repeat trap cycle
```

### Positioning

**Good Positions:**
- Behind his own sensor network
- In rooms với single entry points
- Near extraction zones (sensor perimeter)

**Bad Positions:**
- On the move mà không deployed sensors
- Open ground (sensors become useless)
- Same building as another Recon (redundant)

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **IGNITION** | Incendiary Rush is loud và predictable — sensors detect approach easily | Trap doorways, pre-aim fire paths |
| **TARTARUS** | Berserker Rush is linear — sensors give cảnh báo for easy kiting | Place sensors at CQB approach, backpedal và shoot |
| **GOLIATH** | Slow rotations, easy to track với sensor network | Surround với sensors, never let him close |

### Even Matchups

| Opponent | ghi chú | chính to Winning |
| :------- | :---- | :------------- |
| **SONAR** | Both intel operators — scan vs. traps | Pre-place sensors trước scan, maintain awareness |
| **AEGIS** | Guardian Shield protects pushes thông qua traps | Stack sensors to overwhelm shield timing |
| **MAMBA** | Combat Stim rushes can outrun sensor alerts | Layer sensors deeper, not just at entry |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **GLITCH** | EMP destroys all deployed sensors instantly | Space sensors apart, keep reserves |
| **OBSIDIAN** | Smoke blocks sensor engagement giá trị | Push thông qua smoke to trigger sensors manually |
| **SUTURE** | Healing drone sustains thông qua trap damage | Focus fire SUTURE directly, ignore drone |

---

## Voice Lines

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Sensors deployed. The web is set." |
| Sensor Triggered | "Movement detected. [Direction]." |
| Multiple Triggers | "Multiple contacts on sensors." |
| Kill | "Predictable." |
| Kill (Trap Assisted) | "Caught in my web." |
| Low máu | "Falling back. Sensors still active." |
| Reviving | "On your feet, comrade." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| địch Trap Detected | "địch trap. [Direction]." |
| Sensor Destroyed | "Sensor down. Blind spot at [Direction]." |
| Reloading | "Reloading. Watch the sensors." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "Patience. The prey will come to us." |
| Extraction Called | "Pull the web tight. They will try to stop us." |
| Extraction success | "Another successful hunt." |
| Squad Wipe | "The spider always wins." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Olive drab tactical vest over black base layer, utility harness với sensor modules
- **Headgear:** Black beret (Russian military style), tactical earpiece
- **Gloves:** Dark leather field gloves
- **Face:** Short graying beard, scar across bridge of nose, calculating eyes

<!-- REF_IMAGE: MIRAGE default skin — top-down view showing stocky silhouette với sensor equipment hiển thị rõ on belt, muted military color sơ đồ -->

### Unlockable Skins

| Skin | Rarity | Unlock |
| :--- | :----- | :----- |
| **Snow Web** | Common | Level 10 |
| **Night Watch** | Uncommon | 1,000 Credits |
| **Crimson Spider** | Rare | Level 25 |
| **FSB Classified** | Epic | Battle Pass S1 |
| **The Weaver** | Legendary | Season 1 Event |

### Signature Items

| Item | Description |
| :--- | :---------- |
| **Spider Brooch** | Small metal spider pin on collar |
| **Sensor Bandolier** | Belt of sensor modules across chest |
| **Old Dog Tags** | FSB unit tags, scratched và worn |

---

## Lore Connections

### Relationships

| nhân vật | Relationship |
| :-------- | :----------- |
| **SONAR** | Former adversaries trong khi Cold War-era proxy ops — uneasy respect born from mutual competence |
| **TARTARUS** | Both Russian, nhưng different ideology — MIRAGE despises TARTARUS's recklessness |
| **GOLIATH** | Old military connection — served in same regional command, share tactical language |
| **OBSIDIAN** | Hunted her once trong khi a covert operation in Japan — failed, respects her evasion |

### Story Hooks

- Stole classified FSB files detailing Corporation connections to Russian government
- Maintains a network of informants across the Exclusion Zone (quest givers)
- Searching for his former handler who sold agent identities
- Hidden sensor caches in every map — environmental easter eggs

---

## Design ghi chú (For Developers)

### Balance Considerations

- Sensors are persistent nhưng fragile (20 HP) — a single shot destroys them
- 3 sensors per activation với 60s cooldown gives steady nhưng not overwhelming coverage
- Trap Sense passive is strong against mirror matchups — monitor Recon vs Recon win rates
- Shock Trap upgrade (15 damage) is the highest-impact Slot 3 option — consider 12 damage nếu overperforming
- Camo Sensors upgrade should still show a faint shimmer — truly invisible sensors are not fun to play against

### Animation yêu cầu

- Sensor throw animation (0.5 seconds — quick underhand toss)
- Sensor deployment VFX (small pulse on landing, then ambient glow)
- Sensor trigger VFX (red pulse expanding from triggered sensor)
- Trap detection HUD (pulsing orange marker for địch traps)
- Death animation: collapses methodically (controlled, not dramatic)

### Audio yêu cầu

| Sound | ghi chú |
| :---- | :---- |
| Sensor deploy | Soft thud on surface + electronic chirp |
| Sensor active | Minimal ambient hum (nearly silent) |
| Sensor triggered | Sharp alarm chime (team-wide) |
| Sensor destroyed | Electric crackle + pop |
| Footsteps | Standard Recon — quiet tactical boots |
| Trap Sense alert | Low cảnh báo buzz khi near địch trap |

### Top-Down cụ thể ghi chú

- Sensors on the ground nên được hiển thị rõ to the owning team as small green dots from minimum zoom
- địch sensors should only appear nếu within detection range of friendly teams hoặc revealed by Trap Sense
- Sensor trigger red pulse phải được hiển thị rõ at minimum zoom — critical audio/visual alert
- Sensor placement animation nên được quick (0.5s) và not interrupt movement flow
- Camo Sensors upgrade visual shimmer nên được subtle nhưng discoverable by attentive người chơi at max zoom
