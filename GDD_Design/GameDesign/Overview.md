# Game Overview & Design Foundation

**[← Back to Index](../README.md)** | **[Next: Core Gameplay →](./CoreGameplay.md)**

---

## Executive Summary

**Extraction Topdown Mobile Multiplayer** is a hardcore tactical extraction shooter designed specifically for mobile platforms, combining the tension of games like Escape from Tarkov with the accessibility and session length suited for mobile gaming.

**Core Hook:** *Every raid risks everything. Extract with fortune or lose it all.*

---

## Game Concept

### Elevator Pitch

"Escape from Tarkov meets mobile gaming - a top-down tactical extraction shooter where every decision matters, every death hurts, and every successful extraction feels earned."

### High Concept Statement

> "The Dark Souls of mobile extraction shooters - where strategic depth, permanent loss, and meaningful player choices create an addictive, high-stakes gameplay experience optimized for touch controls and mobile sessions."

---

## Unique Selling Points (USP)

### 1. True Extraction Mechanics on Mobile (First of Its Kind)

**Market Gap:**
- **PC:** Tarkov, The Cycle → Hardcore but not portable
- **Mobile:** PUBG, COD Mobile → Battle Royale, not extraction
- **Our Solution:** Genuine extraction shooter built for mobile

**Key Differentiators:**
```
Traditional Mobile Shooters  |  Our Game
────────────────────────────────────────────
• Start equal each match     |  • Bring your own gear
• Battle Royale format        |  • Extraction-based
• Casual, fast-paced          |  • Tactical, high-stakes
• No permanent progression    |  • Persistent economy
• Low consequence             |  • Meaningful death penalty
```

---

### 2. Permanent Loss System (THE Core Mechanic)

**Philosophy:** Death must have weight

**Implementation:**
```
Death in Raid
    ↓
┌──────────────────────────────┐
│  LOST:                       │
│  • All items in backpack     │
│  • All equipped weapons      │
│  • All equipped armor        │
│  • All consumables used      │
│  • Operator in cooldown (5min)│
└──────────────────────────────┘
    ↓
┌──────────────────────────────┐
│  SAVED:                      │
│  • Secure Container contents │
│    (2x2 = 4 slots protected) │
│  • Account progression (XP)  │
│  • Stash items (not brought) │
│  • Quest progress            │
└──────────────────────────────┘
```

**Psychological Impact:**
- **Pre-Match:** "Can I afford to lose this loadout?"
- **In-Match:** "Should I extract now or risk for more?"
- **Post-Death:** "That hurt, but I learn" → Retry motivation
- **Post-Victory:** "I earned this!" → Dopamine spike

**Balance Considerations:**
- Death penalty severe enough to matter
- Not so punishing it causes rage-quit
- Secure Container provides safety net
- Account progression never lost
- Comeback mechanics for new players

---

### 3. Top-Down Perspective (Strategic Advantage)

**Why Top-Down Instead of FPS?**

**Mobile Advantages:**
```
Traditional FPS on Mobile:
├─ Thumb blocks screen
├─ Difficult aiming precision
├─ Motion sickness potential
├─ Cluttered UI
└─ Battery drain (3D rendering)

Top-Down Benefits:
├─ Full screen visibility
├─ Tactical overview
├─ Easier touch controls
├─ Cleaner UI layout
├─ Better performance
└─ Unique in genre
```

**Gameplay Implications:**
- **Strategic positioning** over twitch reflexes
- **Map awareness** and tactical planning
- **Cover system** more important
- **Ability usage** more impactful
- **Team coordination** visually clearer

**Artist Direction:**
```
Camera Angle: 45° isometric
├─ Height: 15-20m above ground
├─ Rotation: Fixed (for clarity)
├─ Zoom: Pinch gesture (±20%)
└─ Tilt: Slight for depth

Visual Style:
├─ High contrast (gameplay > realism)
├─ Clear silhouettes
├─ Color-coded threats
└─ Readable at 5" screens
```

---

### 4. Mobile-First Design Philosophy

**Principle:** Not a PC port, built ground-up for mobile

**Match Duration:**
```
PC Extraction Games: 30-45 minutes
Our Target: 10-15 minutes

Rationale:
├─ Commute-friendly
├─ Lunch break viable
├─ Battery considerate
├─ Attention span optimized
└─ Multiple matches per session
```

**Control Optimization:**
```
Left Thumb: Movement
├─ Virtual joystick
├─ Sprint: Push further
├─ Crouch: Edge tap
└─ Intuitive, familiar

Right Thumb: Action
├─ Tap: Shoot
├─ Hold: Aim
├─ Swipe: Camera rotate
└─ Contextual actions

UI Touch Targets:
├─ Minimum: 60x60px
├─ Critical buttons: 80x80px
├─ Spacing: 10px minimum
└─ Thumb-zone optimized
```

**Performance Targets:**
```
Frame Rate: 60 FPS stable
├─ High-end: 60 FPS locked
├─ Mid-range: 60 FPS dynamic
└─ Low-end: 30 FPS stable

Battery Consumption:
├─ 15-min match: <5% battery
├─ Thermal management
└─ Power-saving mode support

File Size:
├─ Initial download: <500MB
├─ Full install: <2GB
├─ Streaming assets: Optional HD textures
```

---

## Core Design Pillars

### Pillar #1: Meaningful Choices → Emotional Investment

**Philosophy:** Every decision should have weight

**Manifestation in Gameplay:**

**Pre-Match Choices:**
```
Loadout Decision Tree:
    ↓
"Cheap Loadout" ←→ "Expensive Loadout"
    ↓                      ↓
Less effective        More effective
Low risk              High risk
Easy to replace       Painful to lose
    ↓                      ↓
[Impacts entire match psychology]
```

**In-Match Choices:**
- **Loot or Leave?** - That container might have good stuff...or alert enemies
- **Fight or Flight?** - Can I win this? Is the risk worth it?
- **Extract or Continue?** - I have good loot, but there's more...
- **Help Teammate?** - Save them or save myself?

**Why It Matters:**
> "Players don't remember sequences of button presses. They remember the moment they chose greed over safety and paid the price. They remember extracting by the skin of their teeth with legendary loot. These **emotional memories** drive retention."

---

### Pillar #2: Risk vs Reward → The Core Tension

**Philosophy:** The best rewards require the greatest risks

**Implementation:**

**Loot Distribution Map:**
```
┌─────────────────────────────────────┐
│         MAP LAYOUT                  │
├─────────────────────────────────────┤
│                                     │
│  🟢 Safe Zone (Edge)                │
│  ├─ Loot: Common                    │
│  ├─ AI: Light                       │
│  ├─ Players: Rare                   │
│  └─ Risk: ★☆☆☆☆                    │
│                                     │
│    🟡 Mid Zone                      │
│    ├─ Loot: Common-Rare             │
│    ├─ AI: Medium                    │
│    ├─ Players: Moderate             │
│    └─ Risk: ★★★☆☆                  │
│                                     │
│      🔴 Hot Zone (Center)           │
│      ├─ Loot: Rare-Legendary        │
│      ├─ AI: Heavy + Boss            │
│      ├─ Players: High               │
│      └─ Risk: ★★★★★                │
│                                     │
│  💎 Supply Drop (Event)             │
│  ├─ Loot: Epic-Legendary guaranteed │
│  ├─ Alert: Map-wide notification    │
│  ├─ Players: ALL converge           │
│  └─ Risk: ★★★★★★                  │
└─────────────────────────────────────┘
```

**Time-Based Risk:**
```
0-5 minutes:
├─ Low tension
├─ Players spreading out
└─ Safe to loot edges

5-10 minutes:
├─ Rising tension
├─ Players colliding
├─ Decision: Extract or continue?
└─ Supply drops create hotspots

10-12 minutes:
├─ High tension
├─ Best-geared players remain
├─ "One more container" syndrome
└─ Extraction zones contested

12-15 minutes:
├─ EXTREME tension
├─ Contamination zone active
├─ Forced player interaction
└─ Desperate extractions

15:00 - Match End
└─ All remaining players DIE
```

**Psychological Pressure Points:**
```
The "Just One More" Trap:
    ↓
Player has good loot
    ↓
Sees one more container
    ↓
"Just ONE more..." (GREED)
    ↓
Opens container → Rare item!
    ↓
"Okay, ONE more..." (ESCALATING GREED)
    ↓
[Loop continues until...]
    ↓
├─ Extracted = Dopamine HIGH
└─ Died = Regret + Lesson Learned
```

---

### Pillar #3: Tactical Depth → Skill Expression

**Philosophy:** Strategy and knowledge > Twitch reflexes

**Skill Dimensions:**

#### 1. Map Knowledge
```
Beginner:
└─ Knows extraction points

Intermediate:
├─ Knows loot locations
├─ Knows common routes
└─ Understands timings

Advanced:
├─ Knows optimal rotations
├─ Predicts player movements
├─ Knows sound trap spots
├─ Uses terrain advantage
└─ Masters ambush points
```

#### 2. Loadout Building
```
Amateur:
└─ "Bring best gear always"

Skilled:
├─ Matches loadout to goal
├─ Balances cost vs effectiveness
├─ Considers operator synergy
└─ Plans for weight management
```

#### 3. Combat Tactics
```
Spray and Pray:
└─ ☠️ Dies often

Tactical Player:
├─ Uses cover effectively
├─ Engages at optimal range
├─ Knows when to disengage
├─ Manages ability cooldowns
└─ Controls the engagement
```

#### 4. Economy Management
```
Poor Player:
├─ Always broke
├─ Can't afford gear
└─ Stuck in poverty loop

Wealthy Player:
├─ Knows what to loot
├─ Sells smartly
├─ Invests in right gear
├─ Completes profitable quests
└─ Sustainable economy
```

**Design Tools for Depth:**
- **Information asymmetry** - UAV, sensors create advantage
- **Positioning matters** - Cover, high ground, flanking
- **Ability combos** - Operator synergies in squads
- **Resource management** - Ammo, medical, stamina
- **Economic decisions** - What to loot, what to leave

---

### Pillar #4: Persistent Progression → Long-Term Investment

**Philosophy:** Your actions today impact tomorrow

**Progression Layers:**

#### Account Progression (Never Lost)
```
Level 1 → Level 50
├─ Unlocks: Operators, weapons, items
├─ Rewards: Credits, cosmetics
├─ Milestones: Every 5 levels
└─ Time Investment: ~100 hours
```

#### Operator Mastery (Per-Operator)
```
Mastery 0 → Mastery 10
├─ Unlocks: Operator-specific items
├─ Buffs: Small stat bonuses
├─ Cosmetics: Skins, emotes
└─ Time Investment: ~20 hours per operator
```

#### Stash Growth (Persistent Economy)
```
Starting Stash: 10x20 grid
├─ Extract loot → Add to stash
├─ Sell for credits
├─ Use for future raids
└─ Player wealth compounds
```

####Quest Progression
```
Quest Types:
├─ Tutorial Quests (1-5)
│   └─ Teach mechanics
├─ Faction Quests (ongoing)
│   └─ Story, unique rewards
├─ Daily Quests (resets)
│   └─ Bonus XP, credits
└─ Weekly Challenges
    └─ Premium rewards
```

**Progression Philosophy:**
> "Lose battles, never the war. Extracted loot and XP are yours forever. Bad raids teach lessons. Good raids build wealth. Long-term success through strategic thinking, not lucky streaks."

---

## Target Audience Deep Dive

### Primary Persona: "Hardcore Mobile Gamer"

**Demographics:**
```
Name: Alex
Age: 24
Gender: Male
Location: Urban, Asia/NA/EU
Device: iPhone 13 Pro / Samsung S22
Income:Disposable income for hobbies
```

**Gaming Background:**
```
Experience:
├─ 10+ years gaming
├─ Played Tarkov/Hunt on PC
├─ PUBG Mobile veteran
├─ Enjoys Dark Souls, roguelikes
└─ Values skill expression

Motivations:
├─ Seeks challenge
├─ Wants meaningful progression
├─ Competitive by nature
├─ Appreciates fair difficulty
└─ Willing to lose for mastery
```

**Pain Points with Current Mobile Games:**
```
❌ Too casual, no stakes
❌ P2W mechanics ruin balance
❌ Repetitive, no depth
❌ No consequences for poor play
❌ Progression feels hollow
```

**What Our Game Provides:**
```
✅ High-stakes gameplay
✅ Skill-based, fair
✅ Deep tactical systems
✅ Meaningful death penalty
✅ Persistent economy
```

---

### Secondary Persona: "PC Gamer Going Mobile"

**Demographics:**
```
Name: Jordan
Age: 32
Gender: Male
Device: iPad Pro
Background: PC gamer, busy lifestyle
```

**Needs:**
```
• Shorter sessions (can't play PC 3 hours)
• Familiar hardcore mechanics
• Portable but not "dumbed down"
• Can play on commute
```

**Our Appeal:**
```
• 15-minute matches
• Tarkov-like mechanics
• Genuine tactical depth
• Mobile convenience
```

---

## Competitive Landscape Analysis

### Direct Competitors (Extraction Genre)

#### Escape from Tarkov (PC)

**What They Do Well:**
- Unmatched depth and realism
- Thriving economy
- Hardcore community
- Regular updates

**Where We Differentiate:**
```
Tarkov              →    Our Game
───────────────────────────────────────
PC only             →    Mobile-first
45-min matches      →    15-min matches
FPS perspective     →    Top-down tactical
Steep learning curve→    More accessible
Survival sim        →    Action-focused
$45 entry           →    Free-to-play
```

**Our Strategy:** *"Tarkov's intensity in your pocket"*

---

#### The Cycle: Frontier (PC, Shut Down)

**What We Learn:**
- Market wants extraction games
- But must balance hardcore/casual
- Must have sustainable economy
- Must avoid P2W

**Why They Failed:**
- Not accessible enough for casuals
- Too casual for hardcore fans
- Tried to please everyone
- Couldn't compete with Tarkov directly

**Our Lesson:** *"Be confidently hardcore. Own our niche."*

---

### Indirect Competitors (Mobile Shooters)

#### PUBG Mobile

**Strengths:**
- 100M+ players
- Polished controls
- Regular content
- Esports scene

**Weaknesses (Our Opportunities):**
- Battle Royale, not extraction
- Bloated with modes
- Arcade-y feel
- No persistent loot economy

**Our Positioning:** *"For players who want higher stakes than Battle Royale"*

---

#### Call of Duty Mobile

**Strengths:**
- AAA brand
- Excellent gunplay
- High production value

**Weaknesses (Our Opportunities):**
- Many P2W complaints
- No extraction mode
- Casual-focused
- Respawn-based modes

**Our Positioning:** *"Where every life actually matters"*

---

## Game World & Narrative

### Setting: Post-Collapse Industrial Zones

**Time Period:** 2035 (Near-Future)

**Backstory:**
```
2030: Environmental Disasters
    ↓
Corporate Zones Abandoned
    ↓
Lawless "Extraction Zones" Formed
    ↓
Mercenaries Enter for Salvage
    ↓
[Game Takes Place Here]
```

**Zones:**
```
Industrial complex
├─ Factories
├─ Warehouses
├─ Office buildings
├─ Underground facilities
└─ Contaminated areas

Urban Ruins
├─ Abandoned  apartments
├─ Shopping districts
├─ Metro systems
├─ Parks overgrown
└─ Military checkpoints
```

---

### Factions (Not Playable, Quest Givers)

#### 1. Salvage Corps
```
Identity: Blue-collar workers turned scavengers
Quests: Retrieve industrial materials
Rewards: Practical gear, tools
Philosophy: "Honest work in lawless lands"
```

#### 2. Tech Syndicate
```
Identity: Corporate treasure hunters
Quests: Recover advanced technology
Rewards: High-tech weapons, electronics
Philosophy: "Fortune favors the bold"
```

#### 3. Underground Network
```
Identity: Black market opportunists
Quests: Smuggle contraband
Rewards: Rare items, currency
Philosophy: "No questions asked"
```

#### 4. Peacekeepers
```
Identity: Ex-military trying to restore order
Quests: Eliminate threats, rescue civilians
Rewards: Military-grade equipment
Philosophy: "Duty above all"
```

**Faction System:**
```
Complete Quests → Gain Reputation
    ↓
Higher Reputation → Better Quests
    ↓
Max Reputation → Unique Operator unlocks
```

---

### Tone & Atmosphere

**Visual Tone:**
```
Color Palette:
├─ Base: Desaturated (gray, brown, green)
├─ Accents:危険 orange, tech blue
├─ Loot: Color-coded rarity
└─ Atmosphere: Gritty, oppressive

Lighting:
├─ Overcast skies (tension)
├─ God rays through ruins (beauty in decay)
├─ Harsh industrial lights
└─ Dynamic weather (rain, fog)
```

**Audio Atmosphere:**
```
Ambient:
├─ Wind through broken buildings
├─ Distant industrial hums
├─ Dripping water
├─ Metal creaking
└─ Occasional animal sounds

Tension:
├─ Footsteps AMPLIFIED
├─ Distant gunshots
├─ Radio static  
├─ Heartbeat when low health
└─ Contamination alarm
```

**Emotional Tone:**
```
Pre-Match: Anticipation, planning
In-Match: Paranoia, tension, greed
Combat: Intensity, focus
Successful Extract: Relief, exhilaration
Death: Frustration → Determination
```

---

## Monetization Philosophy

### Free-to-Play, Never Pay-to-Win

**Core Principle:**
> "Spend money to look good and progress faster. Never spend money to win easier."

**Monetization Pillars:**

#### 1. Battle Pass (Primary Revenue)
```
Free Track:
├─ Basic rewards
├─ Some operators
└─ Decent progression

Premium Track ($9.99/season):
├─ Exclusive cosmetics
├─ 2x XP boost
├─ Premium currency income
├─ Instant operator unlocks
└─ Value: ~$50 worth of items
```

#### 2. Cosmetics (Evergreen Revenue)
```
Skins:
├─ Operator skins
├─ Weapon skins
├─ Backpack skins
└─ Emotes/Finishers

Price Ranges:
├─ Common: $0.99-2.99
├─ Rare: $4.99-7.99
└─ Legendary: $14.99-19.99
```

#### 3. Convenience (Optional Time-Savers)
```
Stash Expansion: $4.99 per tier
Secure Container Upgrade: $9.99 (2x2 → 2x3)
Operator Unlock: $4.99 each
Loadout Slots: $2.99 for extras

Note: ALL obtainable free through play
```

**What We DON'T Sell:**
```
❌ Better weapons
❌ Better armor
❌ Stat boosts
❌ Loot crates (RNG)
❌ Exclusive power
```

---

---

## 🌎 Marketing & Distribution Strategy

### Target Markets
*   **Primary:** Southeast Asia (SEA), Brazil, India (Strong Mobile Hardcore Shooter Demographic).
*   **Secondary:** North America, Western Europe (Focus on "PC Quality on Mobile").

### Distribution Channels
*   **Mobile:** Google Play Store, Apple App Store.
*   **PC:** Steam (Early Access potentially), Epic Games Store.
*   **Community:** Discord (Primary Hub), Reddit, Twitter/X.

### Go-To-Market Plan
1.  **Phase 1: Awareness (Pre-Alpha)** - Developer Blogs, Concept Art teases, Discord community building.
2.  **Phase 2: Engagement (Alpha)** - Closed invite-only tests for influencers and hardcore community members.
3.  **Phase 3: Hype (Beta)** - Open Beta, sponsored streams, "Drop" campaigns for access keys.
4.  **Phase 4: Launch** - Global rollout, Season 1 Battle Pass, cross-platform marketing push.

---

## 📝 Document Ownership & Changelog

| Role            | Owner              | Approver           |
| :-------------- | :----------------- | :----------------- |
| **Author**      | Lead Game Designer | Creative Director  |
| **Tech Review** | Networking Lead    | Technical Director |
| **Art Review**  | Art Director       | Art Lead           |

**Recent Changes:**
*   **v1.1 (2026-02-09):** Added "Marketing & Distribution Strategy" section.
*   **v1.0 (2026-02-07):** Initial comprehensive draft.

---

## Success Metrics & KPIs

### Engagement Metrics

**Session Metrics:**
```
Target Session Length: 25-40 minutes
├─ 2-3 matches per session
├─ Time in menus: <15%
└─ Time in match: >80%

Daily Active Users (DAU):
├─ Month 1: 50K
├─ Month 3: 150K
├─ Month 6: 300K+
```

**Retention Targets:**
```
D1: 45% (strong tutorial)
D7: 25% (hooked by core loop)
D30: 12% (long-term fans)
```

---

### Balance Metrics

**Extraction Success Rate:**
```
Target: 35% overall

By Skill Level:
├─ Beginner: 20% (learning)
├─ Intermediate: 35% (balanced)
└─ Advanced: 50% (mastery)

By Loadout Value:
├─ Budget (<$10K): 40% (less contested)
├─ Standard ($10-30K): 35% (balanced)
└─ Premium (>$30K): 25% (hunted)
```

**Time to Kill (TTK):**
```
Close Range: 0.8-1.5 sec
Mid Range: 1.5-2.5 sec
Long Range: 2.0-3.5 sec

Rationale: Fast enough for mobile, slow enough for tactics
```

---

### Economy Health

**Inflation Control:**
```
Money Supply:
├─ Income: Extracted loot value
├─ Sinks: Vendor purchases, deaths
└─ Target: Stable prices

Monitoring:
├─ Average player wealth
├─ Item price trends
├─ Loot extraction rates
└─ Adjustments via loot tables
```

---

## Development & Design Constraints

### Technical Constraints

**Performance:**
```
Minimum Spec:
├─ Device: 2018+ (iPhone X, Android equivalent)
├─ RAM: 3GB+
├─ Storage: 2GB free
└─ OS: iOS 13+, Android 10+

Target Spec:
├─ 2021+ (iPhone 13, Flagship Android)
├─ Best experience
└─ All features enabled
```

**Network:**
```
Bandwidth: Optimized for 4G
├─ Tick rate: 20Hz
├─ Lag compensation
└─ Reconnect support (3-min grace)

Server Regions:
├─ NA East, West
├─ EU West, East
├─ Asia (SEA, East Asia)
└─ Latency-based matchmaking
```

---

### Design Constraints

**Mobile UX Requirements:**
```
✓ Touch targets: 60x60px minimum
✓ One-thumb playable (future)
✓ Readable on 5" screens
✓ Battery-efficient
✓ Playable with gloves (accessibility)
✓ Landscape orientation only
```

**Content Cadence:**
```
Weekly: New quests, events
Monthly: Balance patches
Quarterly: New operators, weapons
Yearly: New maps, major features
```

---

## Risk Mitigation

### Design Risks

#### Risk: "Too Hardcore for Mobile Audience"

**Mitigation:**
```
• Strong tutorial (5 missions)
• Progressive difficulty (bot matches 1-10)
• Scavenger mode (low-stakes practice)
• Generous secure container
• Clear feedback on mistakes
```

#### Risk: "Frustrating Death Penalty Causes Churn"

**Mitigation:**
```
• Small XP on death (not total loss)
• Secure container safety net
• Insurance system (future)
• "Comeback" quests for poor players
• Clear death recap (learn from it)
```

#### Risk: "Economy Inflation/Deflation"

**Mitigation:**
```
• Dynamic loot tables
• Money sinks (repairs, upgrades)
• Seasonal economy resets (optional)
• Live monitoring dashboard
• Quick adjustment capability
```

---

## Future Vision & Roadmap

### Launch (Version 1.0)
```
Content:
├─ 5 Operators
├─ 3 Maps
├─ 30+ Weapons
├─ 100+ Items
├─ Core game modes
└─ Battle Pass Season 1
```

### Year 1 Post-Launch
```
Q1: New operator, new map
Q2: Ranked mode, clan system
Q3: New operators (2), weapon expansion
Q4: Holiday events, major balance pass
```

### Year 2+ Long-Term
```
• Cross-play with PC version
• Base-building meta-game
•Co-op PvE raids
• Expanded world/lore
• Esports ecosystem
```

---

## Core Design Philosophy Summary

**What We Are:**
- Hardcore tactical extraction shooter
- Mobile-first, not mobile-port
- Skill-based, fair, meaningful

**What We're NOT:**
- Casual arcade shooter
- Pay-to-win cash grab
- Watered-down PC port

**Our Promise to Players:**
> "Your time matters. Your choices matter. Your skill matters. We will never compromise the integrity of the game for short-term profit. Every update will respect the hardcore tactical vision."

---

**[← Back to Index](../README.md)** | **[Next: Core Gameplay →](./CoreGameplay.md)**
