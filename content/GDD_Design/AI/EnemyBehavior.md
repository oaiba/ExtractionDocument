---
title: "AI & Enemy Behavior Design"
type: docs
---

##  AI Design Philosophy

**Core Principle:** AI should enhance the extraction experience, not replace PvP

AI enemies serve as:
- **Loot guardians** - Protect valuable areas
- **Tension creators** - Keep players on edge even without PvP contact
- **Skill tests** - Predictable patterns that reward mastery
- **Sound traps** - Engaging AI creates noise, attracting players

**NOT:**
- Main adversaries (PvP is the core tension)
- Unfair or unpredictable
- Bullet sponges
- Trivially easy

---

##  Enemy Types

### Tier 1: Fodder (Common)

**Purpose:** Easy to kill, noise makers, loot pinatas

#### Scavenger
```
Visual: Ragged civilian clothing, makeshift weapons
Health: 50 HP
Armor: None
Damage: 10-15 per hit (melee) / 15-20 (pistol)
Speed: Walk (3 m/s), Sprint (5 m/s)
Detection Range: 15m (vision), 10m (sound)
Behavior: Patrol → Alert → Engage → Flee (when low HP)
```

**Spawn Locations:** Edge zones, mid zones
**Loot Drop:** Common items, ammo, medical supplies
**Threat Level:** 

**Behavior Details:**
- Patrols in small area (10m radius)
- Alerts nearby scavengers when engaged
- Flees at 20% HP
- Does NOT pursue beyond patrol area

---

#### Looter
```
Visual: Hoodie, backpack, SMG
Health: 75 HP
Armor: Light (25 armor)
Damage: 18-22 per hit (SMG)
Speed: Walk (3.5 m/s), Sprint (6 m/s)
Detection Range: 20m (vision), 15m (sound)
Behavior: Patrol → Alert → Take Cover → Engage
```

**Spawn Locations:** Mid zones, near loot containers
**Loot Drop:** Uncommon items, sometimes rare
**Threat Level:** 

**Behavior Details:**
- Searches containers (can be ambushed)
- Uses cover during combat
- Calls for backup if possible
- More accurate than Scavengers

---

### Tier 2: Soldiers (Uncommon)

**Purpose:** Actual threats, require tactical approach

#### Guard
```
Visual: Military fatigues, body armor, assault rifle
Health: 100 HP
Armor: Medium (50 armor)
Damage: 25-30 per hit (AR)
Speed: Walk (4 m/s), Sprint (6 m/s)
Detection Range: 30m (vision), 20m (sound)
Behavior: Patrol (formations) → Alert Team → Suppress → Flank
```

**Spawn Locations:** Hot zones, POI entrances
**Loot Drop:** Rare items, military gear
**Threat Level:** 

**Behavior Details:**
- Patrols in pairs
- Uses suppressive fire
- One flanks while other suppresses
- Throws grenades into cover
- Does NOT flee

---

#### Sniper
```
Visual: Ghillie suit or overwatch position
Health: 80 HP
Armor: Light (25 armor)
Damage: 60-80 per hit (sniper rifle)
Speed: Stationary / Reposition (5 m/s)
Detection Range: 60m (vision), 25m (sound)
Behavior: Overwatch → Aim (laser warning) → Fire → Reposition
```

**Spawn Locations:** Elevated positions, guard towers
**Loot Drop:** Rare weapons, optics
**Threat Level:** 

**Behavior Details:**
- Does NOT patrol (stationary overwatch)
- Laser sight warns players (1.5s before shot)
- Repositions after 3 shots
- Vulnerable during repositioning
- Audio cue: Loud shot echo (alerts other players)

---

### Tier 3: Elites (Rare)

**Purpose:** Mini-bosses, guard high-value loot

#### Heavy
```
Visual: Full body armor, LMG, slow movement
Health: 200 HP
Armor: Heavy (100 armor)
Damage: 35-40 per hit (LMG)
Speed: Walk (2.5 m/s), NO sprint
Detection Range: 25m (vision), 30m (sound)
Behavior: Advance → Suppress → Pursue relentlessly
```

**Spawn Locations:** Hot zone centers, vaults
**Loot Drop:** Epic items, LMG, heavy armor
**Threat Level:** 

**Behavior Details:**
- Announced by heavy footsteps (audio warning)
- Cannot be staggered easily
- Weak point: Backpack (2x damage)
- Slow turn rate (flank effective)
- Does NOT retreat

---

#### Operative
```
Visual: Tactical gear, night vision, suppressed weapons
Health: 120 HP
Armor: Medium (50 armor)
Damage: 30-35 per hit (suppressed AR)
Speed: Walk (4 m/s), Sprint (7 m/s)
Detection Range: 40m (vision), 35m (sound)
Behavior: Stealth approach → Flank → Engage → Smoke retreat
```

**Spawn Locations:** Random spawn, event reinforcements
**Loot Drop:** Epic items, tactical equipment
**Threat Level:** 

**Behavior Details:**
- Can approach silently (no footsteps until 10m)
- Uses flashbangs before engaging
- Retreats with smoke grenades when damaged
- Most intelligent AI type
- Coordinates with other Operatives

---

### Tier 4: Bosses (Legendary)

**Purpose:** High-risk, high-reward encounters

#### The Warden (Map 1 - Industrial Decay)
```
Visual: Heavily modified exosuit, construction theme
Health: 500 HP
Armor: 200 armor (regenerates slowly)
Damage: Variable (see phases)
Speed: Walk (3 m/s), Charge (10 m/s)
Detection Range: Map-wide when triggered
Location: Central hot zone (Reactor Core)
```

**Phases:**
| Phase | HP Threshold | Behavior    | Attacks                                    |
| :---- | :----------- | :---------- | :----------------------------------------- |
| 1     | 100-75%      | Stalking    | Ground slam (AoE), debris throw            |
| 2     | 75-50%       | Aggressive  | Adds charge attack, faster attacks         |
| 3     | 50-25%       | Berserk     | Continuous charge, environment destruction |
| 4     | 25-0%        | Desperation | All attacks + calls reinforcements         |

**Loot Drop:** Legendary weapon/armor guaranteed, rare crafting materials
**Threat Level:** 

**Design Notes:**
- Announced 30 seconds before appearing (alarm sounds)
- Creates massive noise (attracts players)
- Can be avoided (not mandatory)
- Intended for squad coordination

---

#### The Director (Map 2 - Urban Ruins)
```
Visual: Corporate executive suit + combat augments
Health: 400 HP
Armor: 150 armor (depleting shields)
Damage: Drone attacks + personal sidearm
Speed: Walk (4 m/s), Teleport (short range blink)
Detection Range: Drone network (entire POI)
Location: Corporate Tower (top floor)
```

**Mechanics:**
- Controls 4 attack drones
- Drones must be destroyed first (80 HP each)
- Shields regenerate if drones are alive
- Blinks away when attacked directly
- Final phase: Overcharges remaining drones (explode on death)

**Loot Drop:** Legendary tech items, electronic components
**Threat Level:** 

---

##  AI Behavior Systems

### Detection System

**Three Detection States:**

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   UNAWARE   │────→│    ALERT    │────→│   ENGAGED   │
│  (Patrol)   │←────│ (Searching) │←────│  (Combat)   │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                    │
      └───────────────────┴────────────────────┘
                    (Timer expires)
```

**Transition Triggers:**

| From    | To      | Trigger                           |
| :------ | :------ | :-------------------------------- |
| Unaware | Alert   | Noise heard (footsteps, gunfire)  |
| Unaware | Alert   | Peripheral vision (edge of cone)  |
| Unaware | Engaged | Direct vision (center of cone)    |
| Alert   | Engaged | Player spotted during search      |
| Alert   | Unaware | 30 seconds no contact             |
| Engaged | Alert   | Line of sight lost for 10 seconds |
| Engaged | Unaware | 60 seconds no contact (rare)      |

### Vision System

**Vision Cone:**
```
          Player
             ▼
    ┌───────────────┐
    │   Peripheral  │  60° total angle
    │  ┌─────────┐  │
    │  │ Direct  │  │  30° center (immediate detection)
    │  └─────────┘  │
    └───────────────┘
         Enemy
         
Detection Range by State:
- Unaware: 50% normal range
- Alert: 100% normal range  
- Engaged: 150% normal range
```

**Visibility Modifiers:**
| Condition | Detection Speed |
| :-------- | :-------------- |
| Standing  | Normal          |
| Crouching | -30%            |
| Prone     | -60%            |
| Moving    | +50%            |
| Sprinting | +100%           |
| Firing    | Immediate       |
| In light  | +30%            |
| In shadow | -30%            |

### Sound System

**Sound Propagation:**
```
Footsteps (Walk): 10m radius
Footsteps (Sprint): 25m radius
Gunfire (Suppressed): 30m radius
Gunfire (Unsuppressed): 80m radius
Explosions: 150m radius
Ability Use: 40m radius (varies)
```

**Sound Occlusion:**
- Walls reduce sound by 50%
- Closed doors reduce by 75%
- Open areas: Full propagation

### Patrol System

**Patrol Types:**

| Type          | Description                 | Used By             |
| :------------ | :-------------------------- | :------------------ |
| **Point**     | Stand in one location       | Snipers, Guards     |
| **Path**      | Follow waypoints            | Scavengers, Looters |
| **Random**    | Wander within area          | Scavengers          |
| **Pair**      | Two AI coordinated          | Guards, Elites      |
| **Formation** | 3+ AI in tactical formation | Hot zone squads     |

**Patrol Behavior:**
- Stop at waypoints (1-5 seconds)
- Look around at waypoints
- Investigate sounds during patrol
- Return to patrol after alert timeout

---

##  Combat Behavior

### Engagement Rules

**Aggression by Type:**
| Type      | Behavior               | Retreat Trigger |
| :-------- | :--------------------- | :-------------- |
| Scavenger | Cautious, flee early   | 20% HP          |
| Looter    | Moderate, use cover    | 15% HP          |
| Guard     | Aggressive, no retreat | Never           |
| Sniper    | Evasive, reposition    | When flanked    |
| Heavy     | Relentless pursuit     | Never           |
| Operative | Tactical, coordinate   | 30% HP (smoke)  |

### Cover Usage

**Cover Selection Priority:**
1. Hard cover (walls, concrete)
2. Soft cover (cars, furniture)
3. Distance from threat
4. Angle to threat

**Cover Behavior:**
- Peek and shoot (2-3 shots)
- Reload behind cover
- Switch cover if flanked
- Grenade flush if player camps

### Suppression

**When AI Uses Suppression:**
- Player behind cover for 5+ seconds
- Multiple AI present
- Heavy/Guard types

**Suppression Effect on Player:**
- Camera shake (light)
- Reduced accuracy if standing
- Audio feedback (bullets snapping)

### Flanking

**Flank Trigger:**
- Player stationary in cover for 10+ seconds
- 2+ AI present
- One AI suppresses, one moves

**Flank Path:**
- Attempt wide angle (90°+)
- Use cover during movement
- Coordinate timing with suppressor

---

##  Difficulty Scaling

### Dynamic Difficulty

**NOT used** - We want consistent, learnable AI

### Spawn Density by Zone

| Zone | Fodder       | Soldiers     | Elites       | Boss |
| :--- | :----------- | :----------- | :----------- | :--- |
| Edge | Low (2-4)    | None         | None         | No   |
| Mid  | Medium (4-8) | Low (2-3)    | Rare (0-1)   | No   |
| Hot  | High (6-10)  | Medium (4-6) | Common (2-3) | Yes  |

### Respawn Rules

**General:**
- AI does NOT respawn during a single match
- Cleared areas stay cleared
- Exception: Reinforcement events

**Reinforcement Events:**
- Trigger: Supply drop, boss fight, timed event
- Warning: 30 seconds audio cue
- Spawn from map edges
- Limited count (5-10 AI)

---

##  AI Personality Variants

Each AI type has personality variants affecting behavior:

### Aggression
| Level      | Behavior                      |
| :--------- | :---------------------------- |
| Coward     | Flee early, poor accuracy     |
| Cautious   | Heavy cover use, slow advance |
| Normal     | Balanced                      |
| Aggressive | Rush tactics, less cover      |
| Berserker  | Suicide charge (rare variant) |

### Accuracy
| Level         | Hit Rate |
| :------------ | :------- |
| Poor          | 15%      |
| Below Average | 25%      |
| Average       | 40%      |
| Above Average | 55%      |
| Marksman      | 70%      |

**Distribution:**
- Fodder: Poor to Average
- Soldiers: Below Average to Above Average
- Elites: Average to Marksman

---

##  AI Audio Design

### Detection Audio
| State           | Sound                   |
| :-------------- | :---------------------- |
| Unaware → Alert | "What was that?" grunt  |
| Alert → Engaged | "There! Enemy!" callout |
| Engaged → Alert | "Lost visual"           |
| Alert → Unaware | Relaxed sigh            |

### Combat Audio
- Reload calls: "Reloading!"
- Throw grenade: "Grenade out!"
- Flanking: "Moving!" 
- Suppressing: "Covering fire!"
- Low HP: Pain sounds, panicked breathing

### Ambient AI
- Idle chatter (background noise)
- Radio checks
- Coughing, shuffling
- Equipment sounds

---

##  AI Balancing Guidelines

### Kill Time (TTK) Targets

| AI Type   | Player TTK (target) | AI TTK (player target) |
| :-------- | :------------------ | :--------------------- |
| Scavenger | 1-2 seconds         | 8-10 seconds           |
| Looter    | 2-3 seconds         | 6-8 seconds            |
| Guard     | 3-5 seconds         | 4-6 seconds            |
| Sniper    | 2-3 seconds         | 6-8 seconds            |
| Heavy     | 8-15 seconds        | 5-7 seconds            |
| Operative | 4-6 seconds         | 4-6 seconds            |
| Boss      | 60-120 seconds      | 30-60 seconds          |

### Solo vs Squad Balance

**AI should be:**
- Soloable with skill and caution
- Faster/easier with squad coordination
- Never trivial regardless of squad size

**Scaling (OPTIONAL for hot zones):**
| Players in Area | AI Damage | AI Health |
| :-------------- | :-------- | :-------- |
| 1               | 100%      | 100%      |
| 2               | 110%      | 110%      |
| 3+              | 120%      | 125%      |

---

##  AI Content Roadmap

### Launch
- All Tier 1-3 AI types
- 1 Boss (The Warden)
- Basic behavior systems

### Season 2
- The Director boss
- Operative elite type
- Improved flanking AI

### Season 3
- New boss for Map 3
- AI events (raids)
- Faction-specific AI variants

### Future
- AI faction wars (environmental events)
- Wandering mini-bosses
- Seasonal boss variants



