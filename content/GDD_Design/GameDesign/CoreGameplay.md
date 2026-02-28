---
title: "Core Gameplay Mechanics - Deep Dive"
type: docs
---

## Overview

This document provides comprehensive details on the core gameplay loop, minute-by-minute player experience, combat mechanics, and psychological design principles.

---

##  Core Gameplay Loop Structure

```
┌─────────────────────────────────────────────────────┐
│         PRE-MATCH (2-5 min)                         │
│  • Loadout Selection                                │
│  • Risk Assessment                                  │
│  • Strategic Planning                               │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│         IN-MATCH (10-15 min)                        │
│  Deployment → Looting → Combat → Extraction         │
│  [High Tension, Constant Decision Making]           │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│         POST-MATCH (2-5 min)                        │
│  • Victory/Defeat Screen                            │
│  • Loot Management                                  │
│  • Progression Review                               │
└─────────────────────────────────────────────────────┘
```

**Total Loop Time:** 14-25 minutes (optimized for mobile sessions)

---

## PRE-MATCH PHASE (2-5 minutes)

### Loadout Selection System

#### 1. Operator Selection
**Decision Framework:**
```
Mission Type → Operator Choice → Loadout Build
     ↓               ↓                  ↓
  PvP Focus      Assault           Aggressive Kit
  Loot Focus     Support/Recon     Defensive Kit
  Quest          Specialist        Mission Kit
```

**Strategic Considerations:**
- **Assault** - High risk, high kill potential
- **Support** - Sustain, team-oriented
- **Recon** - Information advantage, solo-friendly
- **Tank** - Defensive, extraction security
- **Specialist** - Utility, quest completion

#### 2. Gear Selection Philosophy

**Tier System:**
```
Budget Loadout ($5,000-10,000)
├─ Common weapons
├─ Light armor
├─ Basic medical supplies
└─ Low risk if lost

Standard Loadout ($15,000-25,000)
├─ Uncommon weapons
├─ Medium armor
├─ Good medical supplies
└─ Balanced risk/reward

Premium Loadout ($40,000-60,000)
├─ Rare+ weapons
├─ Heavy armor
├─ Full medical kit
└─ High risk, competitive advantage
```

**Loadout Decision Matrix:**
- **Account Balance** - Can you afford to lose it?
- **Quest Requirements** - Need specific items?
- **Skill Level** - Confident enough?
- **Map Knowledge** - Know the routes?
- **Time Available** - Can commit 15 min?

#### 3. Psychological Pre-Match Preparation

**Anticipation Building:**
- Review daily quests → Clear goals
- Check map conditions → Environmental awareness
- Inspect secure container → Protected assets
- Review death log → Learn from mistakes

**UI Elements:**
- **Risk Indicator** — Shows total loadout value at risk (uninsured highlighted separately)
- **Insurance Panel** — Insure gear with Viktor or Ada before deploying; see [Insurance System](InsuranceSystem.md) for full rules and insurer tradeoffs
- **Recommended Loadouts** — Based on active quest needs and account level
- **Quick Loadout Slots** — Save favorite builds (5–10 slots, unlocks via level progression)

> **🔗 Loadout Preparation GDD:** The full pre-raid screen UI specification — including the 3-column PC layout, mobile tab design, stash quick-access panel, gear preview viewport, squad team ready screen, and matchmaking transition — is documented in detail in [Loadout Preparation](LoadoutPreparation.md). This section covers the *design intent*; that GDD covers *implementation*.

> **🔗 Map & Zone Design:** Selection of which map to deploy to, weather conditions, and loot bias are detailed in [Map Design](MapDesign.md). Map cards shown on the prep screen pull zone tier and weather data from that document.



### Matchmaking (15-60 seconds)

**Matchmaking Criteria:**
```
Player Count: 15-20 players per match
├─ Solo players: 40%
├─ Duo teams: 30%
└─ Squad teams (3-4): 30%

Skill-based Matching:
├─ Account Level weighted
├─ Recent extraction rate
├─ Average loadout value
└─ Kill/Death ratio (minor weight)
```

**During Matchmaking:**
- **Map Preview** - Bird's eye view
- **Weather Condition** - Today's environmental hazard
- **Loot Hotspot Indicator** - High-traffic areas marked
- **Player Count Display** - Building anticipation
- **Loading Tips** - Rotate tactical advice

---

## IN-MATCH PHASE (10-15 minutes)

### Detailed Match Timeline

```
┌─────────────┬────────────────────────────────────────────────────┐
│   TIME      │              WHAT HAPPENS                          │
├─────────────┼────────────────────────────────────────────────────┤
│  0:00-0:30  │ DEPLOYMENT                                         │
│             │ • Players spawn at edges (random, balanced)        │
│             │ • 10-second spawn protection                       │
│             │ • Orient, plan first move                          │
├─────────────┼────────────────────────────────────────────────────┤
│  0:30-3:00  │ EARLY LOOTING                                      │
│             │ • Spread across map                                │
│             │ • Low-risk containers                              │
│             │ • AI encounters                                    │
│             │ • First item acquisitions                          │
├─────────────┼────────────────────────────────────────────────────┤
│  3:00-5:00  │ MID LOOTING & POSITIONING                          │
│             │ • Players moving toward mid-zones                  │
│             │ • Increased loot quality                           │
│             │ • First player sightings                           │
│             │ • Tactical positioning starts                      │
├─────────────┼────────────────────────────────────────────────────┤
│  5:00-5:30  │ SUPPLY DROP #1 (Event)                             │
│             │ • High-tier loot announced                         │
│             │ • Creates hotspot                                  │
│             │ • Players converge OR avoid                        │
│             │ • First major PvP spike                            │
├─────────────┼────────────────────────────────────────────────────┤
│  5:30-8:00  │ MID-GAME COMBAT PHASE                              │
│             │ • Player paths collide                             │
│             │ • PvP encounters frequent                          │
│             │ • Loot from kills                                  │
│             │ • Early extractions begin                          │
├─────────────┼────────────────────────────────────────────────────┤
│  8:00-10:00 │ PEAK TENSION                                       │
│             │ • Best-geared players remain                       │
│             │ • "One more container" decisions                   │
│             │ • Extraction vs greed dilemma                      │
│             │ • Reduced player count (~8-12 left)                │
├─────────────┼────────────────────────────────────────────────────┤
│ 10:00-10:30 │ SUPPLY DROP #2 (Event)                             │
│             │ • Legendary loot possible                          │
│             │ • High-stakes decision point                       │
│             │ • Major combat if contested                        │
├─────────────┼────────────────────────────────────────────────────┤
│ 10:30-12:00 │ LATE GAME - EXTRACTION FOCUS                       │
│             │ • Players head to extraction zones                 │
│             │ • Extraction points become contested               │
│             │ • Maximum inventory value                          │
│             │ • High-stakes final encounters                     │
├─────────────┼────────────────────────────────────────────────────┤
│ 12:00-12:30 │ CONTAMINATION WARNING                              │
│             │ • Zone appears on map (red)                        │
│             │ • 30-second warning                                │
│             │ • Players scramble to safe zones                   │
│             │ • Panic extraction attempts                        │
├─────────────┼────────────────────────────────────────────────────┤
│ 12:30-15:00 │ CONTAMINATION ACTIVE                               │
│             │ • Playable area shrinks                            │
│             │ • Damage escalates: 10→25→50 HP/sec                │
│             │ • Forced player interaction                        │
│             │ • Desperate extraction attempts                    │
├─────────────┼────────────────────────────────────────────────────┤
│ 15:00       │ MATCH ENDS                                         │
│             │ • All remaining players die                        │
│             │ • Force extraction impossible                      │
│             │ • Loot lost for stragglers                         │
└─────────────┴────────────────────────────────────────────────────┘
```

---

### Movement & Controls (Mobile-Optimized)

#### Control Scheme
```
Left Side: Movement Joystick
├─ Drag to move
├─ Push further = Sprint
├─ Tap edge = Crouch toggle
└─ Double-tap center = Stop

Right Side: Action/Aim Zone
├─ Tap to shoot
├─ Hold to aim
├─ Swipe to rotate camera
└─ Multi-finger gestures

Bottom UI:
├─ Ability button (cooldown shown)
├─ Reload button (auto-hide when full)
├─ Medical quick-use (contextual)
├─ Grenade/tactical slot
└─ Interaction prompt (context-sensitive)

Top UI:
├─ Minimap (pinch to zoom)
├─ Health/Armor bars
├─ Stamina indicator
├─ Time remaining
└─ Contamination warning

``` 

#### Movement Mechanics

**Movement States:**
```
Walking (default)
├─ Speed: 5 m/s
├─ Noise: Low
├─ Stamina: No drain
└─ Use case: Stealth approach

Sprinting
├─ Speed: 7.5 m/s (1.5x)
├─ Noise: High
├─ Stamina: Drain 10/sec
├─ Cannot shoot while sprinting
└─ Use case: Rotation, escape

Crouching
├─ Speed: 3 m/s (0.6x)
├─ Noise: Very Low
├─ Stamina: No drain
├─ Accuracy bonus: +10%
└─ Use case: Stealth, cover

```

**Weight System Impact:**
```
0-15 kg: Normal movement (100%)
15-25 kg: Slightly slower (90%, +20% stamina drain)
25-35 kg: Noticeably slower (75%, +50% stamina drain)
35+ kg: Heavily encumbered (60%, +100% stamina drain, NO sprint)
```

**Design Rationale:**
- Encourages inventory management
- Creates "dump loot to escape" decisions
- Rewards light loadouts for mobility
- Punishes excessive looting

---

### Combat Mechanics Deep Dive

#### Engagement Flow
```
DETECTION
    ↓
  [Decision Point]
    ↓
┌───────────┴───────────┐
│                       │
FIGHT                 FLEE
│                       │
├─ Assess Gear         ├─ Sprint away
├─ Check Positioning   ├─ Use cover
├─ Ability Ready?      ├─ Break line of sight
└─ Commit or Disengage └─ Reposition
    ↓                       ↓
  COMBAT                   [Re-evaluate]
    ↓                          ↓
┌─────┴─────┐           Return to Detection
│           │
WIN       LOSE
│           │
Loot      Death
```

#### Combat Systems

**1. Cover System**
```
Soft Cover (Wood, Thin Metal)
├─ Damage Reduction: 30%
├─ Penetrable by high-caliber weapons
├─ Visual: Yellow outline
└─ Examples: Crates, doors, cars

Hard Cover (Concrete, Thick Metal)
├─ Damage Reduction: 70%
├─ Non-penetrable
├─ Visual: Blue outline
└─ Examples: Walls, bunkers, containers
```

**Auto-Cover Mechanics:**
- Character auto-crouches near cover
- Peek system (slide finger while  in cover)
- Blind fire option (reduced accuracy)

**2. Damage Calculation**
```
Base Damage
    ↓
[Distance Falloff Applied]
    ↓
[Armor Absorption - 70% absorbed first]
    ↓
[Headshot/Limb Multiplier]
    ↓
Final Damage to Health
```

**Headshot System:**
```
No Helmet
└─ 2.0x damage multiplier

Light Helmet (30 armor)
├─ 1.75x multiplier
└─ Reduces by 25%

Medium Helmet (50 armor)
├─ 1.6x multiplier
└─ Reduces by 40%

Heavy Helmet (75 armor)
├─ 1.5x multiplier
└─ Reduces by 50%
```

**Limb Damage:**
```
Head: 2.0x (with helmet modifiers)
Chest: 1.0x (full damage)
Arms: 0.75x (reduced damage)
Legs: 0.75x (reduced damage)
```

**3. Time-to-Kill (TTK) Targets**
```
Close Range (0-15m):
├─ SMG: 0.8-1.2 sec
├─ AR: 1.0-1.5 sec
└─ Shotgun: 0.3-0.6 sec

Mid Range (15-40m):
├─ AR: 1.2-1.8 sec
├─ LMG: 1.5-2.0 sec
└─ SMG: 2.0-3.0 sec (falloff)

Long Range (40m+):
├─ Sniper: 0.5-1.0 sec
├─ AR: 2.5-3.5 sec
└─ DMR: 1.5-2.5 sec
```

**Design Philosophy:** TTK balanced for mobile - fast enough to be decisive, slow enough for tactical play.

---

### Looting Mechanics

#### Loot container Types
```
Wooden Crate
├─ Loot Quality: Common-Uncommon (80/20)
├─ Search Time: 2 seconds
├─ Items: 2-4
└─ Spawn Rate: High (every zone)

Metal Locker
├─ Loot Quality: Common-Rare (50/40/10)
├─ Search Time: 3 seconds
├─ Items: 3-5
└─ Spawn Rate: Medium (mid zones)

Weapon Rack
├─ Loot Quality: Weapons only, Uncommon-Epic
├─ Search Time: 4 seconds
├─ Items: 1-2 weapons
└─ Spawn Rate: Low (hot zones)

Safe
├─ Loot Quality: Rare-Legendary (60/30/10)
├─ Search Time: 8 seconds (lockpick) or instant (key)
├─ Items: 4-8 high-value
└─ Spawn Rate: Very Low (2-3 per map)

Supply Drop
├─ Loot Quality: Epic-Legendary (70/30)
├─ Search Time: 5 seconds
├─ Items: 5-10
└─ Spawn: Event-based (5:00, 10:00)

Dead Player Body
├─ Loot Quality: Player's entire inventory
├─ Search Time: 3 seconds
├─ Items: Variable (could be 20+ items)
└─ Risk: High (killer might be watching)
```

#### Dynamic Loot Scaling

**Base formula:**
```
Loot Quality = Base_Rate * Zone_Multiplier * Time_Multiplier * Death_Multiplier

Where:
Zone_Multiplier:
├─ Safe Zone: 0.8x
├─ Mid Zone: 1.0x
└─ Hot Zone: 1.4x

Time_Multiplier:
├─ 0-5 min: 1.0x
├─ 5-10 min: 1.1x
└─ 10-15 min: 1.25x (reward late stay)

Death_Multiplier:
├─ More player deaths → Better loot spawns
└─ Scales from 1.0x to 1.3x
```

**Rationale:** Encourage risk-taking and late-game tension

---

### Extraction Mechanics

#### Extraction Process (30-second timer)

**Step-by-Step:**
```
1. Reach Extraction Zone
   └─ Marked on map (green helicopter icon)
   
2. Enter Zone
   └─ UI prompt: "Hold E to Call Extraction"
   
3. Activate Extraction
   ├─ 30-second countdown begins
   ├─ Audio cue: Helicopter approaching
   ├─ Visual: Smoke grenade, lights
   └─ Map notification: "Player Extracting at Zone A!"
   
4. Defend Position
   ├─ Cannot leave zone (timer resets)
   ├─ Can take damage (timer resets)
   ├─ Can shoot/use abilities
   └─ Team must all be in zone
   
5. Successful Extraction
   └─ Fade to black, victory screen
```

####  Extraction Zone Types

**Standard Extraction (3-4 per map)**
```
Always Active
├─ Known locations
├─ 30-second timer
├─ Open to all players
└─ Most contested
```

**Emergency Extraction (1-2 per map)**
```
Requires Special Item/Quest
├─ Hidden locations
├─ 15-second timer (faster)
├─ Single-use
└─ High risk to reach
```

**Vehicle Extraction (1 per map)**
```
Limited Capacity (4 players max)
├─ First-come-first-served
├─ 45-second timer (longer)
├─ Vehicle arrival noise
└─ Very exposed
```

#### Extraction Interruption

**Timer Resets When:**
- Leave extraction zone (even 1 step)
- Take ANY  damage
- Team member dies
- Extraction zone attacked (grenade, ability)

**Counter-Play:**
- Attackers can camp extractions
- Smoke grenades help
- Decoy abilities viable
- Team coordination critical

---

### Risk vs Reward Psychology

#### The "Greed Loop"

**Player Mental Process:**
```
"I have good loot now..."
    ↓
"But there's a safe nearby..."
    ↓
"Just ONE more container..."
    ↓
[Encounters another player]
    ↓
┌─────────┴─────────┐
│                   │
WIN               LOSE
│                   │
"I can push more"  "I should've extracted"
│                   │
Cycle continues    Learn from loss
```

**Design Mechanisms:**
1. **Secure Container** - Always saved, encourages risk
2. **Visible Loot Value** - See what you're risking
3. **Time Pressure** - Contamination forces decisions
4. **Extraction Sounds** - "Others are escaping!"
5. **Quest Pressure** - "I need one more item..."

#### Decision Framework Design

Every major decision follows this pattern:
```
SITUATION
    ↓
INFO GATHERING
├─ Listen for footsteps
├─ Check minimap
├─ Assess inventory value
└─ Check time remaining
    ↓
RISK ASSESSMENT
├─ Can I win this fight?
├─ Is it worth the risk?
├─ Do I have escape routes?
└─ What do I lose if I die?
    ↓
DECISION
├─ Engage
├─ Avoid
├─ Extract
└─ Continue looting
    ↓
CONSEQUENCE
└─ [Learn for next time]
```

---

## POST-MATCH PHASE (2-5 minutes)

### Victory Screen (Successful Extraction)

**Display Breakdown:**
```
┌──────────────────────────────────────┐
│  EXTRACTION SUCCESSFUL               │
├──────────────────────────────────────┤
│  [Operator 3D Model - Celebrating]   │
│                                      │
│  Survival Time: 12:34                │
│  Players Eliminated: 3               │
│  Distance Traveled: 842m             │
│                                      │
│  ═══ LOOT ACQUIRED ═══               │
│  [Grid showing all items]            │
│  Total Value: $45,280                │
│                                      │
│  ═══ REWARDS ═══                     │
│  Base XP: 1,200                      │
│  Survival Bonus: +300                │
│  Kill Bonus: +450 (3 kills)          │
│  Extraction Bonus: +500              │
│  ────────────────                    │
│  Total XP: 2,450                     │
│                                      │
│  Credits Earned: $3,200              │
│  Operator XP: +850                   │
│                                      │
│  [Continue]  [Share]  [Replay]       │
└──────────────────────────────────────┘
```

**Psychological Design:**
- Dopamine hit from victory
- Clear loot showcase
- Pride in performance stats
- Social sharing encouragement

---

### Defeat Screen (Killed in Action)

**Display Breakdown:**
```┌──────────────────────────────────────┐
│  KILLED IN ACTION                    │
├──────────────────────────────────────┤
│  [Death Recap]                       │
│  Killed by: [Player Name]            │
│  Using: AK-47                        │
│  Distance: 23m                       │
│  Body Shots: 4, Head: 1              │
│                                      │
│  ═══ ITEMS LOST ═══                  │
│  [Grid showing lost items]           │
│  Total Value Lost: $32,150           │
│                                      │
│  ═══ SECURED ITEMS ═══               │
│  [Secure Container 2x2]              │
│  Saved: $8,200                       │
│                                      │
│  Performance:                        │
│  Survival Time: 8:42                 │
│  Damage Dealt: 384                   │
│  Players Hit: 2                      │
│                                      │
│  Consolation XP: 450                 │
│                                      │
│  [Retry]  [Change Loadout] [Stash]  │
└──────────────────────────────────────┘
```

**Psychological Design:**
- Not overly punishing visually
- Clear learning opportunity (death recap)
- Small XP consolation
- Highlight secured items (not total loss)
- Easy retry to prevent rage quit

---

### Session Structure

**Ideal 30-Minute Session:**
```
0:00 - Login
├─ Daily reward claim
├─ Quest check
└─ BP progress review

0:03 - Match #1 Prep
├─ Loadout selection
└─ Mental preparation

0:06 - Match #1 (13 min)
└─ Result: Death at 8:30

0:19 - Quick Break
├─ Review death
├─ Adjust loadout
└─ 1-minute breather

0:21 - Match #2 Prep
└─ Different strategy

0:24 - Match #2 (15 min)
└─ Result: Successful extraction!

0:39 - Loot Management
├─ Sort stash
├─ Sell items
├─ Craft upgrades
└─ Quest turn-ins

0:45 - Decision Point
├─ Start Match #3?
└─ Or logout satisfied

Natural session: 30-45 minutes (2-3 matches)
```

---

## Advanced Mechanics

### Squad Coordination

**Roles in Squad:**
```
Point Man (Recon/Assault)
├─ Leads movement
├─ First contact
└─ Calls enemy positions

Support (Support/Specialist)
├─ Healing duty
├─ Utility deployment
└─ Resource management

Heavy (Tank/LMG Assault)
├─ Suppressive fire
├─ Zone control
└─ Extraction security

Flex (Any Operator)
├─ Adapts to situation
├─ Backup role
└─ Quest focus
```

**Squad Communication (Voice Not Required):**
- Ping system (location, enemy, item)
- Quick chat wheel
- Minimap markers
- Auto-callouts

---

### Information Warfare

**Sound Design:**
```
Footsteps:
├─ Audible: 15m (walking), 30m (sprinting)
├─ Material-based (metal, wood, concrete)
├─ Directional audio (3D)
└─ Volume based on surface

Gunshots:
├─ Audible: 100m+
├─ Distinct per weapon type
├─ Suppressed: 50% range reduction
└─ Draws attention

Looting Sounds:
├─ Container open: 10m
├─ Item pickup: 5m
└─ Inventory management: 3m

Abilities:
├─ Each has unique audio
├─ Range: 20-40m depending on type
└─ Identifiable by enemies
```

**Visual Information:**
```
Muzzle Flash:
├─ Visible: 50m
├─ Reveals position
└─ Brief but noticeable

Movement:
├─ Character visible: Line of sight
├─ Minimap: 0m (no constant reveal)
└─ UAV: Temporary reveal (ability)

Loot Beam:
├─ Rare+ items have vertical beam
├─ Visible: 30m
└─ Risk: Reveals your location if you loot
```

---

## Metrics & Balance

### Target Metrics

**Match Pacing:**
- Average match duration: 12 minutes
- Extraction success rate: 35%
- Average kills per match: 1.5
- Average loot value extracted: $25,000

**Player Distribution:**
```
Match Start: 20 players
├─ 3 min: 18 players (-2 early deaths)
├─ 6 min: 15 players (-3 combat)
├─ 9 min: 11 players (-4 extracted/died)
└─ 12 min: 6 players remain
    ├─ 3 extract successfully
    └─ 3 die to contamination/combat
```



