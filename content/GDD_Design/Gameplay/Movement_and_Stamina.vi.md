---
title: "Movement & Stamina hệ thống"
type: docs
weight: 2
---

### Tổng Quan

Movement in an extraction shooter is not just traversal — it is a constant tactical quyết định. Every step generates noise, consumes resources, và communicates information to other người chơi. The movement hệ thống được thiết kế để feel deliberate và weighty, rewarding người chơi who move với intention over those who sprint carelessly.

> Xem [cốt lõi Gameplay cơ chế](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/CoreGameplay/README.md) for cụ thể speed values và control sơ đồ layout. This tài liệu focuses on design intent, feel, và systemic interactions.

***

### Movement trạng thái

#### primary trạng thái

| trạng thái     | Speed Multiplier | Noise Level | Stamina Drain | Combat Capability                              | cách dùng Case                                      |
| --------- | :--------------: | ----------- | ------------- | ---------------------------------------------- | --------------------------------------------- |
| Walking   |   1.0x (5 m/s)   | Low         | None          | Full — can shoot, ADS, cách dùng items               | Default movement, cautious approach           |
| Sprinting |  1.5x (7.5 m/s)  | High        | 10/sec (Leg)  | None — cannot shoot hoặc ADS                     | Rotation between positions, fleeing           |
| Crouching |   0.6x (3 m/s)   | Very Low    | None          | Full + 10% accuracy bonus                      | Stealth approach, behind cover                |
| Prone     |   0.2x (1 m/s)   | Minimal     | None          | Full + 15% accuracy bonus, limited turn radius | Ambush, sniper positioning, hiding            |
| Slow Walk |   0.4x (2 m/s)   | Near Silent | None          | Full                                           | Listening for địch, close-quarters stealth |

#### trạng thái Transitions

```
Standing (Walk)
    |
    +-- Sprint (push joystick to edge / hold Shift)
    |       Returns to Walk when released or stamina depleted
    |
    +-- Crouch (tap crouch button / press C)
    |       Toggle. Can move while crouched.
    |
    +-- Prone (hold crouch button / press Z)
    |       Transition takes 0.8s. Vulnerable during animation.
    |       Stand up takes 0.6s.
    |
    +-- Slow Walk (half-press joystick / hold Alt)
            Near-silent movement for audio reconnaissance
```

#### Advanced Movement Actions

| Action                | Input                             | Duration | Noise     | Stamina chi phí | ghi chú                                                               |
| --------------------- | --------------------------------- | :------: | --------- | ------------ | ------------------------------------------------------------------- |
| Vault (low obstacle)  | Interact near waist-height object |   0.6s   | Medium    | 5 Leg        | Automatic khi moving toward climbable surface                      |
| Vault (high obstacle) | Interact near chest-height object |   1.2s   | High      | 10 Leg       | Slower, more exposed; cannot cancel mid-animation                   |
| Slide                 | Sprint + Crouch                   |   0.8s   | High      | 8 Leg        | Quick transition into crouch. Brief speed burst (2.0x for 0.3s)     |
| Door Breach           | Sprint into closed door           |   0.4s   | Very High | 5 Leg        | Slams door open với force. Loud, nhưng fast entry                    |
| Door Open (quiet)     | Interact với closed door         |   1.0s   | Low       | None         | Slow, controlled door opening. Minimal sound                        |
| Lean (left/right)     | Alt + Q/E                         |  Instant | None      | None         | Peek around corners mà không exposing full body                      |
| Ladder Climb          | Interact với ladder              | Variable | Medium    | 3 Leg/sec    | Cannot shoot while climbing. Ascending is faster than descending    |
| Jump                  | Jump button                       |   0.3s   | High      | 12 Leg       | Limited cách dùng — stamina-expensive, loud. Not a primary traversal tool |

**Design Intent**: Jumping is deliberately expensive to prevent bunny-hopping. The game rewards ground-level tactical movement, not aerial acrobatics.

#### Cross-Platform

Movement values (speed multipliers, stamina costs, noise) are identical on PC, console, và mobile. **Input:** PC uses WASD + Shift/C; mobile uses virtual stick và buttons; console uses left stick và face buttons. Same trạng thái transitions và penalties apply. Xem [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) for platform input layout.

***

### Stamina hệ thống

#### Dual-Bar Design

Stamina is divided into two independent pools, each governing different action types:

**Leg Stamina**

| Property         | giá trị                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| Maximum          | 100 points (base, improvable via Endurance skill)                                                 |
| Recovery Rate    | 4 points/sec (standing still), 2 points/sec (walking)                                             |
| Sprint Drain     | -10 points/sec                                                                                    |
| Jump chi phí        | -12 points per jump                                                                               |
| Vault chi phí       | -5 to -10 points depending on obstacle height                                                     |
| Depleted Penalty | Cannot sprint, cannot jump. Walking speed reduced to 0.8x. Heavy breathing audio (audible at 10m) |

**Arm Stamina**

| Property         | giá trị                                                             |
| ---------------- | ----------------------------------------------------------------- |
| Maximum          | 80 points (base, improvable via Strength skill)                   |
| Recovery Rate    | 3 points/sec (vũ khí lowered), 1 point/sec (vũ khí raised)        |
| ADS Drain        | -3 points/sec (scales với vũ khí weight)                         |
| Grenade Throw    | -15 points per throw                                              |
| Melee Attack     | -10 points per swing                                              |
| Depleted Penalty | Cannot ADS. vũ khí sway increased by 300%. Melee deals 50% damage |

#### Stamina Recovery Conditions

```
FULL RECOVERY (4 Leg/sec, 3 Arm/sec)
  Condition: Standing still, weapon lowered
  Use: Safe room, behind hard cover

PARTIAL RECOVERY (2 Leg/sec, 1 Arm/sec)
  Condition: Walking with weapon raised
  Use: Cautious repositioning

NO RECOVERY (0/sec)
  Condition: Sprinting, or weight > 35 kg
  Use: N/A — player must stop to recover

NEGATIVE RECOVERY (stamina continues to drain)
  Condition: Overweight + walking (weight > 40 kg)
  Use: Emergency only — player is over-looted and must drop items
```

#### Exhaustion trạng thái

khi either stamina bar reaches 0:

* **Leg Exhaustion**: Forced to walk at 0.8x speed. Heavy breathing sound is generated (audible to địch at 10m). Cannot jump hoặc vault. Lasts until Leg Stamina recovers to 20+.
* **Arm Exhaustion**: Cannot aim down sights. Massive vũ khí sway. Melee is weakened. Lasts until Arm Stamina recovers to 15+.

**Design Intent**: Exhaustion is a soft failure trạng thái. It does not kill the người chơi, nhưng it makes them extremely vulnerable. This punishes reckless sprinting và rewards stamina management.

***

### Weight và Encumbrance hệ thống

Total carried weight directly impacts movement speed, stamina drain, và noise generation.

#### Weight Sources

| Item Category    | Typical Weight       | Examples                                          |
| ---------------- | -------------------- | ------------------------------------------------- |
| primary vũ khí   | 2.5-5.0 kg           | AK-47: 3.3 kg, M4A1: 3.0 kg, SVD: 4.3 kg          |
| secondary vũ khí | 0.8-1.5 kg           | Pistols, knives                                   |
| Body giáp       | 3.0-12.0 kg          | Light vest: 3 kg, Heavy plate carrier: 12 kg      |
| Helmet           | 0.5-2.5 kg           | Light: 0.5 kg, Heavy ballistic: 2.5 kg            |
| Backpack (empty) | 0.5-2.0 kg           | Small: 0.5 kg, Large: 2.0 kg                      |
| Medical Supplies | 0.1-1.5 kg per item  | Bandage: 0.1 kg, Grizzly: 1.5 kg                  |
| Ammunition       | 0.5-2.0 kg per stack | Varies by caliber và quantity                    |
| Loot Items       | Variable             | GPU: 0.5 kg, Fuel Can: 4.0 kg, Gold Chain: 0.1 kg |

#### Weight Thresholds

| Weight Range | Movement Speed | Stamina Drain Modifier              | Noise Modifier            | Additional Effects                                       |
| ------------ | -------------- | ----------------------------------- | ------------------------- | -------------------------------------------------------- |
| 0-15 kg      | 100% (Normal)  | 1.0x                                | Normal                    | None                                                     |
| 15-25 kg     | 90%            | 1.2x (+20%)                         | Slightly louder footsteps | None                                                     |
| 25-35 kg     | 75%            | 1.5x (+50%)                         | Noticeably louder         | Equipment rattle noise added                             |
| 35-45 kg     | 60%            | 2.0x (+100%)                        | Loud                      | Cannot sprint. Jump height reduced                       |
| 45+ kg       | 45%            | Cannot recover stamina while moving | Very loud                 | Cannot sprint hoặc jump. Movement generates constant noise |

#### Strategic Implications

The weight hệ thống tạo a chính tension in every raid:

* **Going in light** (10-15 kg loadout) means maximum mobility và stealth, nhưng less combat power và less loot capacity.
* **Going in heavy** (25+ kg loadout) means maximum combat power và giáp, nhưng slower movement, louder footsteps, và an inability to quickly disengage.
* **The loot dilemma**: A người chơi who enters at 15 kg và fills their backpack to 35 kg must now move at 75% speed với 1.5x stamina drain. They must choose between _dropping loot to move faster_ hoặc _accepting reduced mobility to keep the haul_.

**Design Intent**: Weight should never be ignorable. Mid-raid weight gain is the primary tool that transforms a confident hunter into a cautious prey.

***

### Surface Interaction và Noise

Different ground surfaces generate different levels of noise, tạo meaningful terrain choices:

#### Surface Noise bảng

| Surface                   | Walk Noise (audible range) | Sprint Noise (audible range) | Crouch Noise (audible range) | Visual Cue                     |
| ------------------------- | :------------------------: | :--------------------------: | :--------------------------: | ------------------------------ |
| Concrete/Asphalt          |             10m            |              25m             |              4m              | Common, default                |
| Metal (grating, catwalks) |             15m            |              35m             |              8m              | Industrial areas, warehouses   |
| Wood (floorboards)        |             12m            |              28m             |              5m              | Residential buildings          |
| Gravel/Debris             |             14m            |              32m             |              7m              | Roads, construction zones      |
| Grass/Dirt                |             6m             |              18m             |              2m              | Open fields, forest            |
| Water (shallow)           |             20m            |              40m             |              12m             | Streams, flooded areas         |
| Glass (broken)            |             18m            |              35m             |              10m             | Shattered windows, trap hazard |

#### Sound Design Principles

* **Directional Audio**: All footstep sounds are fully spatialized in 3D. người chơi với headphones can determine the direction và approximate distance of địch movement.
* **Material Recognition**: Experienced người chơi learn to identify surfaces by sound. Metal clanging means an địch is on the catwalk above. Glass crunching means they crossed a window.
* **Deliberate Pathing**: người chơi who memorize surface layouts can plan routes that minimize noise (e.g., walking on grass around a building rather than crossing the gravel parking lot).

***

### nhân vật Skills (Long-term Progression)

Physical attributes improve thông qua repeated cách dùng over the course of a wipe cycle:

#### Endurance (Leg Stamina)

|    Level   | Max Leg Stamina |         Sprint Drain Reduction         | Unlock                        |
| :--------: | :-------------: | :------------------------------------: | ----------------------------- |
|      1     |       100       |                   0%                   | Starting giá trị                |
|     10     |       110       |                -5% drain               | Passive — gained by sprinting |
|     25     |       125       |               -12% drain               |                               |
|     40     |       140       |               -20% drain               |                               |
| 51 (Elite) |       150       | -25% drain, breath recovery speed +30% |                               |

#### Strength (Arm Stamina và Weight)

|                                                                                                                                    Level                                                                                                                                    | Max Arm Stamina |       Weight Threshold Bonus       | Unlock                                   |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------: | :--------------------------------: | ---------------------------------------- |
|                                                                                                                                      1                                                                                                                                      |        80       |                0 kg                | Starting giá trị                           |
|                                                                                                                                      10                                                                                                                                     |        85       |           +2 kg per tier           | Passive — gained by carrying heavy loads |
|                                                                                                                                      25                                                                                                                                     |        92       |           +5 kg per tier           |                                          |
|                                                                                                                                      40                                                                                                                                     |       100       |           +8 kg per tier           |                                          |
|                                                                                                                                  51 (Elite)                                                                                                                                 |       110       | +10 kg per tier, melee damage +20% |                                          |
| **Design Intent**: Skills provide long-term progression that incentivizes continued play. However, the bonuses are incremental (not transformative), so a skilled low-level người chơi can still outperform a high-level người chơi thông qua better positioning và quyết định-making. |                 |                                    |                                          |

***

### Vertical Movement & Special Traversal

#### Stairs

Stairs are navigated as flat ramps in gameplay (no step-over animation per stair). From top-down they appear as diagonal crosshatch lines.

| Property                 | giá trị                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------- |
| Movement speed on stairs | 80% of flat speed (upward), 90% (downward)                                                           |
| Stamina drain on stairs  | +20% upward; normal downward                                                                         |
| Noise generation         | Same surface type as floor material connected to stairs                                              |
| Camera on stairs         | Smooth altitude transition between floors (0.5s interpolation per [Camera hệ thống](Camera_System.md)) |
| Prone on stairs          | Not allowed — nhân vật auto-stands khi entering stair zone                                         |

#### Ladders

Ladders provide vertical access between floors in cụ thể buildings.

| Property                             | giá trị                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Ladder climb speed                   | 1.5 m/s (very slow — deliberate vulnerability)                                                  |
| Stamina drain (climbing)             | **Arm Stamina** only — 15 points/sec                                                            |
| Combat on ladder                     | Cannot fire primary vũ khí while climbing. Pistol can be drawn nhưng với −20% accuracy.          |
| Noise on ladder                      | Metal rung contact — audible 12m                                                                |
| Dismount options                     | Top: step off (1.5s animation). Bottom: fast drop (instant, no fall damage from ladder bottom). |
| Camera on ladder                     | Fixed overhead for horizontal; transitions smoothly as altitude changes                         |
| Arm Stamina depletion at 0 on ladder | nhân vật begins to lose grip → forces dismount. Fall damage may apply from height.             |

#### Fall Damage

| Fall Distance |          Damage          | Status Effect                             | ghi chú                                 |
| ------------- | :----------------------: | ----------------------------------------- | ------------------------------------- |
| 0–2m          |           0 HP           | None                                      | Safe jump height                      |
| 2–4m          |     20–40 HP to Legs     | None                                      | Moderate fall; survivable             |
| 4–6m          |     60–100 HP to Legs    | Fracture (50% chance to one Leg)          | Serious fall                          |
| 6–8m          | 150+ HP to Legs + Thorax | Fracture (80% chance, both legs possible) | Often lethal mà không treatment        |
| 8m+           |   Lethal (1000 damage)   | —                                         | Instant kill zone; avoid at all costs |

**Fall damage mitigation:**

* Crouching on land (hold crouch button trong khi fall): −30% fall damage và fracture chance nếu timed within 0.5s of landing.
* Prone immediately on land (hold prone trong khi fall): −50% fall damage for very low falls only (≤3m).
* Scout class passive (nếu applicable in future iteration): reduced fall damage.

**Overweight + fall:** Critical và Overweight encumbrance adds +30% to fall damage (less control trong khi impact).

#### Water Traversal (Swimming)

| Property                 | giá trị                                                                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Swim speed**           | 0.35x (1.75 m/s) — slower than prone walk                                                                                                                |
| **Stamina drain (swim)** | Both Leg và Arm stamina drain simultaneously at 8 pts/sec                                                                                               |
| **Noise (swimming)**     | Splashing — audible 20m                                                                                                                                  |
| **Combat in water**      | Can hold pistol above water — fire với −30% accuracy. No primary vũ khí while swimming.                                                                |
| **Gear in water**        | Wet gear: armored rigs và backpacks absorb water — weight increases by +10% while wet. Returns to normal weight sau 30s out of water.                 |
| **Depth threshold**      | Shallow water (≤0.5m): normal walk speed, minor splash noise. Deep water (>0.5m): swimming trạng thái activates.                                              |
| **Camera in water**      | Standard top-down altitude; water surface rendered semi-transparent to show nhân vật underneath.                                                        |
| **Drowning**             | nếu Arm và Leg Stamina both reach 0 while swimming: −10 HP/sec until one stamina bar recovers. Not instantly lethal — nhưng tạo extreme urgency.       |
| **Contaminated water**   | Flooded areas trong khi Chemical Spill hazard: −5 HP/sec in addition to normal contamination damage. Xem [Environmental Hazards](Environmental_Hazards.md). |

***
