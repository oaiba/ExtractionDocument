---
title: "MIRAGE - Ananya Patel"
type: docs
---

## Operator Profile

> *"You think you're the hunter? You're already in my trap."*

### Basic Information

| Attribute | Value |
| :-------- | :---- |
| **Real Name** | Ananya Patel |
| **Codename** | MIRAGE |
| **Class** | Recon |
| **Nationality** | Indian |
| **Age** | 44 |
| **Height** | 175 cm (5'9") |
| **Weight** | 72 kg (159 lbs) |

<!-- REF_IMAGE: MIRAGE operator portrait — stocky build, tactical vest with sensor nodes, cold expression, cyberpunk utility belt with motion sensors -->

### Background

Viktor Volkov spent 20 years in FSB counter-intelligence, specializing in catching foreign spies on Russian soil. His elaborate trap networks and patient hunting style earned him the nickname "The Spider" among those who feared him.

After growing disillusioned with the corruption eating Russia from within, Viktor disappeared — along with several classified files. Now he uses his expertise in the Exclusion Zone, setting traps for those foolish enough to wander into his web.

### Personality Traits

- **Patient** — Can wait hours for the perfect moment
- **Methodical** — Everything follows a plan
- **Cynical** — Believes everyone is corrupt
- **Protective** — Treats teammates like assets to preserve

---

## Combat Statistics

### Base Stats

| Stat | Value | Class Modifier | Final |
| :--- | :---- | :------------- | :---- |
| **Health** | 100 HP | -5% | 95 HP |
| **Armor** | 30 | - | 30 |
| **Sprint Speed** | 5.5 m/s | - | 5.5 m/s |
| **Crouch Speed** | 2.0 m/s | +15% | 2.3 m/s |
| **Footstep Volume** | 100% | -30% | 70% |

### Damage Modifiers

| Condition | Modifier |
| :-------- | :------- |
| Base Weapon Damage | +0% (no class bonus) |
| Trap-assisted kill | +15 bonus damage from Shock Trap (upgrade) |
| Headshot Multiplier | 2.0x |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 110 | +10% (Recon class) |
| **Sprint Drain** | 9/second | -10% (Recon class) |
| **Recovery Rate** | 9.6/second | +20% (Recon class) |
| **Net Sprint Duration** | 12.2 seconds | Best efficiency |
| **Footstep Volume** | 70% | -30% (Recon class trait) |
| **Ability Audio Radius** | 5 meters | Sensors are nearly silent when deployed |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT — sensors destroyed by fire |
| EMP | 0% | All sensors destroyed instantly by EMP |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 40 cm radius, 182 cm height |
| **Head Sphere** | 14 cm radius |
| **Collision Profile** | Slim (-10% from mesh) |
| **Silhouette From Above** | Medium-slim build, tech harness visible, sensor pouches on belt |
| **Class Accent Zones** | Cyan (#06B6D4) on goggle glow and harness strips |
| **Sensor VFX (Top-Down)** | Small blinking devices on ground, 8m detection radius shown as faint circle when ally walks near |
| **Sensor Audio** | Nearly silent — <5m detection range for enemies |

<!-- REF_IMAGE: MIRAGE top-down view — showing operator with 3 motion sensors deployed, detection radius circles visible from above -->

### Motion Sensor Stat Block

| Property | Value | Notes |
| :------- | :---- | :---- |
| **Sensors Per Activation** | 3 | Deploy individually |
| **Detection Range** | 8 meters each | Overlapping for full coverage |
| **Sensor HP** | 20 | One-shot destroyable |
| **Duration** | Permanent | Until destroyed or match end |
| **Mark Duration** | 4 seconds | After detection |
| **EMP Vulnerability** | Destroyed instantly | Primary counter |
| **Fire Vulnerability** | Destroyed on contact | Secondary counter |
| **Visibility** | Subtle blinking light | Camo Sensors upgrade removes this |

### Difficulty Rating

**Difficulty: 4/5** — Sensor placement and coverage optimization require deep map knowledge. Trap Sense passive demands awareness of enemy Recon setups.


## Abilities

### Active Ability: Motion Sensor Network

> *"Deploy interconnected sensors that detect and mark enemies."*

| Property | Value |
| :------- | :---- |
| **Cooldown** | 60 seconds |
| **Duration** | Until destroyed or match end |
| **Charges** | 3 sensors per activation |

#### Effects

| Effect | Value | Notes |
| :----- | :---- | :---- |
| Detection Range | 8 meters per sensor | Overlapping coverage best |
| Sensor HP | 20 | Destroyable by gunfire or EMP |
| Alert Type | Audio + Visual ping | Directional indicator on HUD |
| Mark Duration | 4 seconds after detection | Enemies visible through walls |

#### Sensor Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **Sensor + EMP (CIPHER)** | All sensors in EMP radius destroyed instantly |
| **Sensor + Fire (BLAZE)** | Sensors destroyed by fire contact |
| **Sensor + Nano Swarm (FLUX)** | Sensors not affected by swarm |
| **Sensor + UAV Scan (PHANTOM)** | N/A — both are intel abilities |
| **Sensor + Smoke (WRAITH)** | Sensors still detect through smoke |
| **Sensor + HAVOC Rage** | Sensors detect raging HAVOC (louder footsteps trigger faster) |

#### Top-Down Sensor VFX

| State | VFX From Above |
| :---- | :------------- |
| Sensor deploy | Brief cyan flash on landing point |
| Sensor active | Small blinking device on ground (friendly: green glow, enemy: not visible unless detected) |
| Sensor triggered | Red pulse expanding from sensor (8m radius flash), alarm chime |
| Sensor destroyed | Brief electrical spark + pop |


| Location | Effectiveness |
| :------- | :------------ |
| Doorways | High — Catches entries |
| Corners | High — Catches flanks |
| Behind cover | Medium — Late warning |
| Open areas | Low — Easy to spot/avoid |

#### Upgrade Slots

**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extra Sensors** | 5 sensors per activation |
| **Hardened** | Sensor HP +15 (35 total) |
| **Wide Angle** | Detection range +3 meters (11m total) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **Slow Field** | Detected enemies slowed 15% for 2 seconds |
| **Silent Alarm** | Enemies do not know they triggered sensor |
| **Networked** | If one sees enemy, all mark them |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Shock Trap** | Detected enemies take 15 damage |
| **Camo Sensors** | Sensors are nearly invisible |
| **Recall** | Can pick up sensors to redeploy |

---

### Passive Ability: Trap Sense

> *"Experience makes you recognize danger."*

| Condition | Effect |
| :-------- | :----- |
| Near enemy trap/sensor | HUD warning (10m range) |
| Crouch detecting | Can see trap outline through walls |
| Destroy enemy trap | Gain 5-second enemy position reveal |

**Design Intent:** MIRAGE is the anti-trap specialist. While PHANTOM provides active intel through scanning, MIRAGE provides persistent, passive territorial control. He is the defensive Recon.

---

## Loadout

### Default Loadout

| Slot | Item | Notes |
| :--- | :--- | :---- |
| **Primary** | AK-74u (Suppressed) | Russian reliability |
| **Secondary** | Makarov Pistol | Soviet classic |
| **Tactical** | Motion Sensors x3, Claymore x1 | Layered traps |
| **Armor** | Light Vest | 30 armor points |

### Recommended Loadouts

**The Spider's Web (Defensive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | Saiga-12 Shotgun | Close range punishment for trapped enemies |
| Secondary | Makarov Pistol | Backup |
| Tactical | Motion Sensors x3, Trip Mine x1 | Maximum area denial |

**Active Hunter (Aggressive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | AS Val (Suppressed) | Accurate, suppressed, mid-range |
| Secondary | Stun Grenades x2 | Disable after sensor trigger |
| Tactical | Motion Sensors x3 | Early warning while pushing |

---

## Playstyle Guide

### Role in Team

**Primary Role:** Area Denial / Early Warning
- Set sensor perimeters around objectives
- Alert team to incoming flanks
- Control chokepoints with trap + weapon combos

**Secondary Role:** Counter-Intel
- Detect and destroy enemy traps
- Deny PHANTOM scans by detecting sensors
- Clear buildings ahead of team push

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
- In rooms with single entry points
- Near extraction zones (sensor perimeter)

**Bad Positions:**
- On the move without deployed sensors
- Open ground (sensors become useless)
- Same building as another Recon (redundant)

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **BLAZE** | Incendiary Rush is loud and predictable — sensors detect approach easily | Trap doorways, pre-aim fire paths |
| **HAVOC** | Berserker Rush is linear — sensors give warning for easy kiting | Place sensors at CQB approach, backpedal and shoot |
| **FORTRESS** | Slow rotations, easy to track with sensor network | Surround with sensors, never let him close |

### Even Matchups

| Opponent | Notes | Key to Winning |
| :------- | :---- | :------------- |
| **PHANTOM** | Both intel operators — scan vs. traps | Pre-place sensors before scan, maintain awareness |
| **ANGEL** | Guardian Shield protects pushes through traps | Stack sensors to overwhelm shield timing |
| **VIPER** | Combat Stim rushes can outrun sensor alerts | Layer sensors deeper, not just at entry |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **CIPHER** | EMP destroys all deployed sensors instantly | Space sensors apart, keep reserves |
| **WRAITH** | Smoke blocks sensor engagement value | Push through smoke to trigger sensors manually |
| **DOC** | Healing drone sustains through trap damage | Focus fire DOC directly, ignore drone |

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
| Low Health | "Falling back. Sensors still active." |
| Reviving | "On your feet, comrade." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| Enemy Trap Detected | "Enemy trap. [Direction]." |
| Sensor Destroyed | "Sensor down. Blind spot at [Direction]." |
| Reloading | "Reloading. Watch the sensors." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "Patience. The prey will come to us." |
| Extraction Called | "Pull the web tight. They will try to stop us." |
| Extraction Success | "Another successful hunt." |
| Squad Wipe | "The spider always wins." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Olive drab tactical vest over black base layer, utility harness with sensor modules
- **Headgear:** Black beret (Russian military style), tactical earpiece
- **Gloves:** Dark leather field gloves
- **Face:** Short graying beard, scar across bridge of nose, calculating eyes

<!-- REF_IMAGE: MIRAGE default skin — top-down view showing stocky silhouette with sensor equipment visible on belt, muted military color scheme -->

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
| **Old Dog Tags** | FSB unit tags, scratched and worn |

---

## Lore Connections

### Relationships

| Character | Relationship |
| :-------- | :----------- |
| **PHANTOM** | Former adversaries during Cold War-era proxy ops — uneasy respect born from mutual competence |
| **HAVOC** | Both Russian, but different ideology — MIRAGE despises HAVOC's recklessness |
| **FORTRESS** | Old military connection — served in same regional command, share tactical language |
| **WRAITH** | Hunted her once during a covert operation in Japan — failed, respects her evasion |

### Story Hooks

- Stole classified FSB files detailing Corporation connections to Russian government
- Maintains a network of informants across the Exclusion Zone (quest givers)
- Searching for his former handler who sold agent identities
- Hidden sensor caches in every map — environmental easter eggs

---

## Design Notes (For Developers)

### Balance Considerations

- Sensors are persistent but fragile (20 HP) — a single shot destroys them
- 3 sensors per activation with 60s cooldown gives steady but not overwhelming coverage
- Trap Sense passive is strong against mirror matchups — monitor Recon vs Recon win rates
- Shock Trap upgrade (15 damage) is the highest-impact Slot 3 option — consider 12 damage if overperforming
- Camo Sensors upgrade should still show a faint shimmer — truly invisible sensors are not fun to play against

### Animation Requirements

- Sensor throw animation (0.5 seconds — quick underhand toss)
- Sensor deployment VFX (small pulse on landing, then ambient glow)
- Sensor trigger VFX (red pulse expanding from triggered sensor)
- Trap detection HUD (pulsing orange marker for enemy traps)
- Death animation: collapses methodically (controlled, not dramatic)

### Audio Requirements

| Sound | Notes |
| :---- | :---- |
| Sensor deploy | Soft thud on surface + electronic chirp |
| Sensor active | Minimal ambient hum (nearly silent) |
| Sensor triggered | Sharp alarm chime (team-wide) |
| Sensor destroyed | Electric crackle + pop |
| Footsteps | Standard Recon — quiet tactical boots |
| Trap Sense alert | Low warning buzz when near enemy trap |

### Top-Down Specific Notes

- Sensors on the ground should be visible to the owning team as small green dots from minimum zoom
- Enemy sensors should only appear if within detection range of friendly teams or revealed by Trap Sense
- Sensor trigger red pulse must be visible at minimum zoom — critical audio/visual alert
- Sensor placement animation should be quick (0.5s) and not interrupt movement flow
- Camo Sensors upgrade visual shimmer should be subtle but discoverable by attentive players at max zoom

