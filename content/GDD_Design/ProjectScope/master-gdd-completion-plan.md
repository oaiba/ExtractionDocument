# Master GDD Completion Plan
## AI Agent Task Assignment & Research Roadmap

**Document Type**: Master Planning & Orchestration  
**Purpose**: Guide AI agents to research and fill missing data in GDD  
**Status**: Active - Awaiting Agent Execution  
**Created**: 2026-02-11  
**Priority**: CRITICAL PATH  

---

## 📋 Executive Summary

This document provides a **comprehensive task breakdown** for AI agents to complete the Game Design Document (GDD) suite. Each agent is assigned specific research areas, deliverables, and integration points.

### Current GDD Status

| Document | Status | Completeness | Priority |
|:---------|:-------|:-------------|:---------|
| Design Pillars | ✅ Complete | 100% | DONE |
| Inventory & Gear | ✅ Complete | 100% | DONE |
| Competitive Analysis | ✅ Complete | 100% | DONE |
| AI Implementation Plan | ✅ Complete | 100% | DONE |
| **MVP Scope** | 🟡 Needs Expansion | 60% | HIGH |
| **Non-Goals** | 🟡 Needs Refinement | 70% | MEDIUM |
| **Project Scope** | 🟡 Needs Detail | 50% | HIGH |
| **Character & Operators** | ❌ Missing | 0% | CRITICAL |
| **Combat & Weapons** | ❌ Missing | 0% | CRITICAL |
| **Map Design** | ❌ Missing | 0% | CRITICAL |
| **Economy & Progression** | ❌ Missing | 0% | HIGH |
| **Monetization Model** | ❌ Missing | 0% | HIGH |
| **Technical Requirements** | ❌ Missing | 0% | HIGH |
| **Art & Audio Direction** | ❌ Missing | 0% | MEDIUM |
| **Narrative & Lore** | ❌ Missing | 0% | MEDIUM |
| **Live Ops & Seasons** | ❌ Missing | 0% | MEDIUM |
| **Social & Clan Systems** | ❌ Missing | 0% | LOW |

---

## 🤖 AI Agent Assignment Matrix

### Agent 1: Combat Systems Specialist

**Research Focus:** Gunplay, weapon mechanics, ballistics, TTK balance

**Primary Tasks:**

1. **Weapon System Deep Dive** (Priority: CRITICAL)
   - Research: Modern FPS weapon handling (Tarkov, CoD Mobile, PUBG Mobile)
   - Deliverable: Complete weapon stat database (30+ weapons)
   - Format: Markdown table with columns: Name, Type, Damage, RPM, Recoil, Range, Mag Size, Reload Time
   - Reference: `/mnt/user-data/uploads/inventory-systems.md` (weapon modding section)
   - Output Location: `/mnt/user-data/outputs/combat-weapons-database.md`
   - Deadline: 3 days

2. **Ballistics & TTK Calculator** (Priority: HIGH)
   - Research: Mobile shooter TTK standards (150-400ms optimal)
   - Deliverable: Ballistics simulation formulas
   - Include: Bullet drop, penetration, damage falloff
   - Integration: Links to armor system in inventory doc
   - Output: `/mnt/user-data/outputs/ballistics-system.md`
   - Deadline: 2 days

3. **Gunfight Flow Design** (Priority: MEDIUM)
   - Research: Engagement distances in mobile extraction shooters
   - Deliverable: Combat engagement matrix (CQB, Mid-range, Long-range)
   - Include: Optimal weapon per range, tactics, map zone suitability
   - Output: `/mnt/user-data/outputs/combat-flow-design.md`
   - Deadline: 2 days

**Research Sources:**
- Escape from Tarkov wiki (weapon stats)
- Arena Breakout: Infinite (mobile gunplay)
- Call of Duty Mobile (TTK benchmarks)
- Delta Force (weapon variety)
- Hunt: Showdown (historical weapon balance)

**Key Questions to Answer:**
- What's the ideal TTK for mobile (headshot vs body)?
- How many weapon classes do we need (minimum 5)?
- Should we have bullet drop at <50m (balance vs realism)?
- Weapon progression: linear power or horizontal variety?
- Mobile recoil control: how much auto-compensation?

**Deliverable Template:**
```markdown
# Combat & Weapons System

## Weapon Database

| Name | Type | Damage | RPM | Recoil | Mag | Reload | Unlock |
|:-----|:-----|:-------|:----|:-------|:----|:-------|:-------|
| AK-47 | AR | 40 | 600 | High | 30 | 2.5s | Lvl 1 |
| M4A1 | AR | 35 | 800 | Medium | 30 | 2.2s | Lvl 5 |
...

## Ballistics Model

### Damage Calculation
```
FinalDamage = BaseDamage × DistanceModifier × PenetrationModifier × HitboxMultiplier

Where:
- DistanceModifier = 1.0 at <25m, -10% per 25m beyond
- PenetrationModifier = ArmorClass / BulletPenetration
- HitboxMultiplier = 2.0 (head), 1.0 (torso), 0.8 (limbs)
```

## TTK Targets
- Close Range (<15m): 150-250ms (2-4 shots)
- Mid Range (15-50m): 300-450ms (4-7 shots)
- Long Range (50m+): 500-800ms (7-12 shots)
```

---

### Agent 2: Character & Operator Designer

**Research Focus:** Operator classes, abilities, progression

**Primary Tasks:**

1. **Operator Class System** (Priority: CRITICAL)
   - Research: Hero shooters with classes (Apex, Overwatch, Delta Force operators)
   - Deliverable: 5-8 operator profiles with unique abilities
   - Include: Backstory, visual description, passive/active abilities, playstyle
   - Balance: No pay-to-win, horizontal variety not vertical power
   - Output: `/mnt/user-data/outputs/character-operators.md`
   - Deadline: 4 days

2. **Operator Progression System** (Priority: HIGH)
   - Research: Mastery systems (Tarkov skills, Apex Legends trackers)
   - Deliverable: Per-operator leveling tree (1-50)
   - Include: XP requirements, unlock milestones, mastery bonuses
   - Balance: 2-5% stat bonuses max (skill>stats)
   - Output: Integrated into operator profiles doc
   - Deadline: 2 days

3. **Character Customization** (Priority: MEDIUM)
   - Research: Cosmetic systems (F2P friendly, no P2W)
   - Deliverable: Skin system, voice lines, animations
   - Monetization: Cosmetics only, no gameplay advantage
   - Output: `/mnt/user-data/outputs/character-customization.md`
   - Deadline: 2 days

**Research Sources:**
- Apex Legends (legend design, abilities)
- Valorant (agent balance, no P2W)
- Delta Force (operator system in extraction mode)
- Rainbow Six Siege (tactical operator variety)
- Arena Breakout (mobile-friendly classes)

**Key Questions to Answer:**
- How many operators at launch (MVP: 5, Target: 8)?
- Active abilities: cooldown-based or resource-based?
- Passive abilities: always-on or situational?
- Operator unlock: progression-based or monetization?
- Voice lines: full VO or text-only (budget)?

**Deliverable Template:**
```markdown
# Character & Operator System

## Operator: Viper (Assault Class)

**Identity:** Former special forces, aggressive playstyle  
**Role:** Entry fragger, close-quarters specialist  

**Stats:**
- Health: 100 HP (standard)
- Movement Speed: 1.0x (baseline)
- Starting Loadout: AK-74, Glock 17, 2x Bandages

**Passive Ability: Adrenaline Rush**
- Effect: +10% sprint speed after kill (5 seconds)
- Cooldown: None (trigger-based)

**Active Ability: Flashbang Grenade**
- Effect: Blinds enemies in 5m radius for 3 seconds
- Cooldown: 60 seconds
- Counterplay: Look away or close eyes

**Progression:**
- Lvl 10: +5% reload speed
- Lvl 20: +10% sprint stamina
- Lvl 30: Unlock "Smoke Grenade" alternative ability
- Lvl 50: Signature weapon skin (AK-47 "Viper")

**Monetization:**
- Base: Free (unlocked at Account Lvl 5)
- Skins: Paid (Jungle, Urban, Desert variants - $5-10 each)
```

---

### Agent 3: Map & Level Designer

**Research Focus:** Map layouts, points of interest, extraction points

**Primary Tasks:**

1. **Industrial Zone Map (Launch Map)** (Priority: CRITICAL)
   - Research: Extraction shooter map design (Tarkov Factory, Hunt maps)
   - Deliverable: Top-down layout with POIs, loot spawns, extracts
   - Include: Zone types (CQB, Sniper lanes, Loot hotspots)
   - Player count: 15-20 players
   - Map size: 500m x 500m (10-12 minute full traverse)
   - Output: `/mnt/user-data/outputs/map-industrial-zone.md`
   - Deadline: 5 days

2. **Loot Table System** (Priority: HIGH)
   - Research: Loot distribution systems (rarity tiers, spawn rates)
   - Deliverable: Loot table per zone type
   - Include: Common/Uncommon/Rare/Epic/Legendary spawn %
   - Balance: High-risk areas = high-reward loot
   - Output: `/mnt/user-data/outputs/loot-tables.md`
   - Deadline: 3 days

3. **Extract Point Design** (Priority: HIGH)
   - Research: Extract camping solutions (Hunt, Tarkov)
   - Deliverable: 4-6 extract points per map
   - Include: Safe (far), Risky (close), Vehicle (expensive), Dynamic (timed)
   - Balance: No "one true extract" (force variety)
   - Output: Integrated into map doc
   - Deadline: 2 days

**Research Sources:**
- Escape from Tarkov maps (Factory, Customs)
- Hunt: Showdown maps (verticality, compounds)
- CoD DMZ (Al Mazrah map design)
- Arena Breakout (mobile map size)
- Delta Force extraction maps

**Key Questions to Answer:**
- How many maps at launch (MVP: 1, Target: 3)?
- Map traversal time: 10-15 minutes full cross?
- How many POIs per map (8-12)?
- Loot hotspot design: centralized or distributed?
- Dynamic events (supply drops, boss spawns)?

**Deliverable Template:**
```markdown
# Map Design: Industrial Zone

## Overview
- Size: 500m x 500m
- Theme: Abandoned factory complex + surrounding slums
- Player Count: 15-20
- Raid Duration: 15-20 minutes
- Weather: Clear/Rain/Fog (dynamic)
- Time: Day/Night cycle

## Key Points of Interest (POIs)

### 1. The Foundry (Central Building)
- Type: High-risk, high-reward loot zone
- Layout: 3 floors, multiple entry points
- Loot: Epic/Legendary weapons, rare attachments
- AI Presence: Heavy (8-10 scavengers)
- Tactics: CQB, vertical combat

### 2. Warehouse District (West)
- Type: Medium-risk, balanced loot
- Layout: Open warehouses, containers, rooftops
- Loot: Common/Uncommon gear, barter items
- AI Presence: Medium (4-6 scavengers)
- Tactics: Mid-range, flanking opportunities

[... continue for all POIs ...]

## Loot Spawn Tables

### Foundry (High Tier)
| Rarity | Spawn Rate | Item Types |
|:-------|:-----------|:-----------|
| Common | 20% | Basic ammo, bandages |
| Uncommon | 30% | Med kits, attachments |
| Rare | 30% | High-tier weapons, armor |
| Epic | 15% | Modded weapons, keys |
| Legendary | 5% | Thermal scopes, rare quest items |

## Extract Points

### 1. Main Gate (Safe - 400m from center)
- Time to Extract: 15 seconds
- Risk: Low (far from hotspots)
- Availability: Always open

### 2. Helipad (Risky - 100m from center)
- Time to Extract: 10 seconds
- Risk: High (central, exposed)
- Availability: Opens at 10 minutes remaining

[... continue for all extracts ...]
```

---

### Agent 4: Economy & Progression Architect

**Research Focus:** Currency systems, trader mechanics, hideout upgrades

**Primary Tasks:**

1. **Currency & Economy Model** (Priority: CRITICAL)
   - Research: F2P mobile economies (soft vs hard currency)
   - Deliverable: Complete economy flowchart
   - Include: Earn rates, sinks, conversion ratios
   - Balance: F2P viable, whales have cosmetic spending
   - Output: `/mnt/user-data/outputs/economy-model.md`
   - Deadline: 4 days

2. **Trader Reputation System** (Priority: HIGH)
   - Research: Tarkov traders, RPG reputation systems
   - Deliverable: 3-5 faction traders with rep tiers
   - Include: Items unlocked per tier, quest requirements
   - Integration: Links to character progression
   - Output: `/mnt/user-data/outputs/trader-system.md`
   - Deadline: 3 days

3. **Hideout Upgrade Tree** (Priority: HIGH)
   - Research: Base-building progression (Fallout Shelter, mobile builders)
   - Deliverable: 8-10 hideout modules with 3 levels each
   - Include: Costs, benefits, dependencies
   - Balance: Meaningful but not mandatory
   - Output: `/mnt/user-data/outputs/hideout-upgrades.md`
   - Deadline: 3 days

**Research Sources:**
- Clash of Clans (base upgrade systems)
- Fallout Shelter (module progression)
- Escape from Tarkov (hideout, traders)
- Arena Breakout (mobile economy balance)
- Warframe (reputation grinds)

**Key Questions to Answer:**
- How many currencies (1 soft, 1 hard, or more)?
- Premium currency exchange rate to USD?
- Inflation prevention: how to balance sinks?
- Insurance system: cost vs return rate?
- First-time user experience (FTUE) economy?

**Deliverable Template:**
```markdown
# Economy & Progression System

## Currency Model

### Soft Currency: Credits (₡)
- **Earn Rate**: 5,000-15,000 ₡ per successful raid
- **Uses**: Buy weapons, armor, meds, trader items
- **Sinks**: Hideout upgrades, repairs, insurance
- **Inflation Control**: Item durability, repair costs

### Hard Currency: Gold (⚙)
- **Earn Rate**: 50-100 ⚙ per day (daily quests, events)
- **Purchase**: $0.99 = 100⚙, $9.99 = 1,200⚙, $49.99 = 7,000⚙
- **Uses**: Cosmetics, Battle Pass, stash expansion, convenience
- **NO USES**: Weapons, armor, stat boosts (NO P2W)

## Trader System

### Trader: Petrov (Weapons Dealer)

**Tiers:**
- **Neutral (0-1000 rep)**: Basic rifles, pistols, shotguns
- **Friendly (1001-3000 rep)**: Attachments, mid-tier weapons, discounts 10%
- **Honored (3001-6000 rep)**: High-tier weapons, rare attachments, discounts 20%
- **Exalted (6001+ rep)**: Exclusive weapons, custom builds, discounts 30%

**Reputation Gain:**
- Complete Petrov's quests: +50-200 rep
- Sell weapon loot to Petrov: +1 rep per 1000₡ value
- Kill rival faction: +10 rep

## Hideout Modules

### Stash Module
- **Level 1**: 10x28 grid, Cost: Free
- **Level 2**: 10x38 grid, Cost: 2M ₡, Req: Account Lvl 10
- **Level 3**: 10x48 grid, Cost: 5M ₡, Req: Medstation Lvl 2

### Medstation
- **Level 1**: +10% heal speed, Cost: 500K ₡
- **Level 2**: +20% heal speed, craft bandages, Cost: 1.5M ₡
- **Level 3**: +30% heal speed, craft surgery kits, Cost: 3M ₡
```

---

### Agent 5: Monetization & LiveOps Strategist

**Research Focus:** F2P monetization, battle pass, seasons

**Primary Tasks:**

1. **Monetization Model** (Priority: CRITICAL)
   - Research: Ethical F2P (no P2W) - Apex, Valorant, Arena Breakout
   - Deliverable: Complete monetization strategy
   - Include: What's sold, pricing, conversion funnels
   - Principle: NEVER sell gameplay advantage
   - Output: `/mnt/user-data/outputs/monetization-strategy.md`
   - Deadline: 4 days

2. **Battle Pass System** (Priority: HIGH)
   - Research: Modern battle pass design (Fortnite, Apex, CoD)
   - Deliverable: 100-tier battle pass structure
   - Include: Free vs Premium tracks, XP requirements
   - Balance: Generous free track (30% value), Premium adds cosmetics
   - Output: `/mnt/user-data/outputs/battle-pass-design.md`
   - Deadline: 3 days

3. **Seasonal Content Plan** (Priority: HIGH)
   - Research: Live service cadences (3-month seasons standard)
   - Deliverable: Year 1 seasonal roadmap
   - Include: New content per season (operators, maps, events)
   - Retention: Keep players engaged without burnout
   - Output: `/mnt/user-data/outputs/seasonal-roadmap.md`
   - Deadline: 3 days

**Research Sources:**
- Apex Legends (ethical F2P model)
- Valorant (cosmetics-only monetization)
- Arena Breakout: Infinite (mobile battle pass)
- Clash Royale (season pass systems)
- Warframe (premium currency balance)

**Key Questions to Answer:**
- Battle Pass price ($5-10 range?)?
- Premium currency pricing tiers?
- How to prevent "pay-to-skip" feeling?
- Seasonal exclusive content (FOMO balance)?
- Loot boxes legal/ethical stance?

**Deliverable Template:**
```markdown
# Monetization & Live Ops Strategy

## Core Monetization Principles
1. **NO Pay-to-Win**: NEVER sell gameplay advantage
2. **Generous Free Path**: F2P players can compete at highest level
3. **Respect Player Time**: No energy systems, no forced ads
4. **Transparency**: Show exactly what you buy (no loot boxes)
5. **Long-term Value**: Encourage spending through quality, not pressure

## Revenue Streams

### 1. Battle Pass ($9.99 / season)
- **Target Attach Rate**: 35-40% of active players
- **Content**: 100 tiers, cosmetics, XP boosts (not P2W)
- **Free Track**: 30% of total value (generous)
- **Premium Track**: +70% value (weapon skins, operator skins, emotes)

### 2. Cosmetic Store
- **Operator Skins**: $5-15 (based on rarity/quality)
- **Weapon Skins**: $3-10
- **Emotes/Finishers**: $2-5
- **Bundles**: $20-30 (20% discount vs individual)
- **Rotation**: Weekly featured items, limited-time exclusives

### 3. Convenience Items (NO P2W)
- **Stash Expansion**: $5 per +10 rows (max 3 purchases)
- **Loadout Slots**: $3 per slot (save pre-built kits)
- **Character Slots**: $5 per slot (alt accounts)
- **Name Change**: $10 (one-time convenience)

### 4. Premium Currency (Gold ⚙)
- **Pricing**:
  - $0.99 = 100⚙
  - $4.99 = 600⚙ (+20% bonus)
  - $9.99 = 1,200⚙ (+20%)
  - $19.99 = 2,600⚙ (+30%)
  - $49.99 = 7,000⚙ (+40%)
  - $99.99 = 15,000⚙ (+50%)

## Season 1 Content Plan (Months 1-3)

**Theme**: "The Collapse" - Explore what happened to Aethelgard

**New Content:**
- 2 New Operators (Tank, Specialist)
- 1 New Map (Urban Zone - partial)
- 8 New Weapons
- 20+ New Cosmetics
- Main Quest Chapter 2 (3 hours)
- Limited-Time Event (Week 6-8): "Supply Drop Frenzy"

**Battle Pass:**
- 100 Tiers
- Tier 1: Assault Rifle Skin
- Tier 25: Operator Skin (common)
- Tier 50: Weapon Charm
- Tier 75: Operator Skin (rare)
- Tier 100: Exclusive Finisher + Legendary Weapon Skin

**Revenue Target**: $500K (conservative, based on 10K MAU × 35% attach × $9.99 + store sales)
```

---

### Agent 6: Technical Requirements Specialist

**Research Focus:** Mobile performance, server architecture, anti-cheat

**Primary Tasks:**

1. **Mobile Hardware Requirements** (Priority: CRITICAL)
   - Research: Mobile game optimization (Unity/Unreal benchmarks)
   - Deliverable: Min/Recommended/Ideal device specs
   - Include: iOS and Android targets, performance budgets
   - Target: 60 FPS on mid-range devices (2023-2024)
   - Output: `/mnt/user-data/outputs/technical-requirements.md`
   - Deadline: 3 days

2. **Server Architecture Design** (Priority: CRITICAL)
   - Research: Dedicated server models (Agones, Kubernetes)
   - Deliverable: Server architecture diagram
   - Include: Matchmaking, authoritative server, anti-cheat
   - Scalability: 100K concurrent players (launch target)
   - Output: `/mnt/user-data/outputs/server-architecture.md`
   - Deadline: 4 days

3. **Anti-Cheat Strategy** (Priority: HIGH)
   - Research: Mobile anti-cheat (Easy Anti-Cheat, BattlEye)
   - Deliverable: Multi-layer anti-cheat plan
   - Include: Client-side, server-side, behavioral analysis
   - F2P Challenge: Free accounts = more cheaters
   - Output: `/mnt/user-data/outputs/anti-cheat-system.md`
   - Deadline: 3 days

**Research Sources:**
- Unreal Engine mobile optimization guides
- Unity mobile performance best practices
- Agones (Kubernetes game servers)
- EasyAntiCheat documentation
- Arena Breakout (mobile optimization case study)

**Key Questions to Answer:**
- Engine choice: Unity vs Unreal Engine 5?
- Min device specs (RAM, GPU, OS version)?
- Network latency tolerance (<100ms? <50ms?)?
- Anti-cheat: third-party or custom?
- Data storage: player inventories, match history?

**Deliverable Template:**
```markdown
# Technical Requirements & Architecture

## Device Specifications

### Minimum (30 FPS, Low Settings)
- **Android**: Snapdragon 660, 3GB RAM, Android 8.0+, OpenGL ES 3.0
- **iOS**: iPhone 8, A11 Bionic, 2GB RAM, iOS 14+, Metal
- **Storage**: 4GB

### Recommended (60 FPS, Medium Settings)
- **Android**: Snapdragon 778G, 6GB RAM, Android 11+
- **iOS**: iPhone 12, A14 Bionic, 4GB RAM, iOS 15+
- **Storage**: 6GB

### Ideal (60 FPS, High Settings)
- **Android**: Snapdragon 8 Gen 2, 8GB RAM, Android 12+
- **iOS**: iPhone 14 Pro, A16 Bionic, 6GB RAM, iOS 16+
- **Storage**: 8GB

## Performance Budgets
- Frame Time: 16.67ms (60 FPS target)
- Draw Calls: <1500 per frame
- Tris: <2M on screen (LOD aggressive)
- Texture Memory: <1.5GB
- CPU Budget: 10ms (game logic + physics)
- Network: <100ms latency (p95)

## Server Architecture

### Stack
- **Game Server**: Dedicated C++ server (Unreal)
- **Orchestration**: Agones on Google Kubernetes Engine (GKE)
- **Matchmaking**: Custom service (Go lang)
- **Backend**: Node.js + PostgreSQL (inventory, accounts)
- **CDN**: Cloudflare (static assets)

### Capacity Planning
- **Launch**: 100K concurrent players (10K raids active)
- **Scale Target**: 500K concurrent (50K raids)
- **Regions**: US West, US East, EU, Asia Pacific
- **Server Lifetime**: 20 min per match, auto-shutdown

## Anti-Cheat System

### Layer 1: Client-Side (EasyAntiCheat)
- Kernel-level driver (Android root detection)
- Memory scanning (aimbot, ESP detection)
- Input validation (macro detection)

### Layer 2: Server-Side Validation
- Movement validation (speed hacks, teleport)
- Hit registration verification (aimbot detection)
- Inventory validation (item duplication, weight hacks)
- Statistically impossible actions flagged

### Layer 3: Behavioral Analysis (AI-powered)
- Player reporting system
- Automated pattern recognition (kill/death ratios, headshot %)
- Manual review queue (human verification)
```

---

### Agent 7: Art & Audio Director

**Research Focus:** Visual style, sound design, music

**Primary Tasks:**

1. **Art Direction Document** (Priority: HIGH)
   - Research: Tactical shooter art styles (realistic vs stylized)
   - Deliverable: Visual style guide
   - Include: Color palette, lighting, UI design, character style
   - Balance: High fidelity for marketing, optimized for mobile
   - Output: `/mnt/user-data/outputs/art-direction.md`
   - Deadline: 4 days

2. **Audio Design Bible** (Priority: MEDIUM)
   - Research: Tactical audio (Hunt: Showdown, Tarkov)
   - Deliverable: Sound design principles
   - Include: Weapon sounds, footsteps, ambient, music
   - Critical: Audio is information (pillar: sound-first design)
   - Output: `/mnt/user-data/outputs/audio-design.md`
   - Deadline: 3 days

3. **UI/UX Design System** (Priority: HIGH)
   - Research: Mobile game UI (clean, minimal, functional)
   - Deliverable: UI component library
   - Include: HUD layout, menus, inventory UI, color scheme
   - Mobile-First: Touch targets, readability, performance
   - Output: `/mnt/user-data/outputs/ui-ux-system.md`
   - Deadline: 3 days

**Research Sources:**
- Hunt: Showdown (audio direction)
- Arena Breakout (mobile UI/UX)
- Call of Duty Mobile (HUD design)
- The Division 2 (UI aesthetics)
- Apex Legends (visual clarity)

**Key Questions to Answer:**
- Realistic vs stylized art style?
- UI color scheme (dark vs light, military vs tech)?
- Footstep audio range (15m? 20m? 30m?)?
- Music: ambient only or dynamic combat tracks?
- Voice acting: full VO or minimal callouts?

**Deliverable Template:**
```markdown
# Art & Audio Direction

## Visual Style Guide

### Core Aesthetic
- **Theme**: Gritty realism with cinematic flair
- **Palette**: Desaturated (70% saturation), earthy tones
- **Lighting**: Physically-based (PBR), dramatic contrasts
- **Detail Level**: High for marketing, LOD-optimized for gameplay

### Color Palette
- **Primary**: Slate Gray (#4A5859), Rust Orange (#C64F27)
- **Accent**: Tactical Green (#3B6B4F), Warning Yellow (#E6A028)
- **UI**: Dark Charcoal (#1C1C1E), White (#FFFFFF)

### Character Design
- **Style**: Realistic proportions, tactical gear authenticity
- **Silhouette**: Clear class distinction at 50m
- **Detail**: Worn, lived-in aesthetic (dirt, scratches, patches)

## Audio Design Principles

### Weapon Sounds
- **Philosophy**: Bass-heavy, realistic, directional
- **Gunshots**: 2-layer system (crack + boom)
- **Suppressors**: -30dB, emphasize action sound
- **Distant Shots**: Low-pass filter, echo delay

### Footsteps
- **Material System**: 8 surface types (metal, wood, concrete, dirt, grass, water, gravel, glass)
- **Audible Range**: 20m (crouch walk), 30m (normal walk), 40m (sprint)
- **Occlusion**: Walls reduce volume -20dB, floors -10dB
- **Player Feedback**: Own footsteps quieter (-10dB vs enemy)

### Ambient Sound
- **Layers**: Wind (constant), machinery (intermittent), wildlife (rare)
- **Dynamic**: Weather changes mix (rain = +10dB ambient)
- **Purpose**: Mask player sounds, create atmosphere

### Music
- **Menu**: Ambient electronic, 80 BPM, moody
- **Raid**: Minimal music (combat tension through silence)
- **Extract**: Victory swell (orchestral, 30 seconds)

## UI/UX System

### HUD Layout (Mobile)
```
[Minimap]                    [Ammo/Health]
                                 
                                 
       [Crosshair]
                                 
                                 
[Sprint]  [Crouch]          [Reload] [Aim]
```

### Design Principles
- **Minimal**: Only show critical info (health, ammo, minimap)
- **Customizable**: Players can move/resize HUD elements
- **Colorblind Safe**: 3 modes (Deuteranopia, Protanopia, Tritanopia)
- **Touch Targets**: 44pt minimum (Apple guidelines)

### Menu Style
- **Layout**: Card-based, swipe navigation
- **Typography**: Roboto (readable, military feel)
- **Icons**: Flat, 2-color (white + accent)
- **Animations**: Smooth 60 FPS, <200ms transitions
```

---

### Agent 8: Narrative & Lore Writer

**Research Focus:** World-building, quest narratives, character backstories

**Primary Tasks:**

1. **World Bible: Aethelgard** (Priority: MEDIUM)
   - Research: Extraction shooter narratives (Tarkov, Hunt lore)
   - Deliverable: Complete world history, factions, timeline
   - Include: "The Collapse" event, current state, mysteries
   - Integration: Environmental storytelling (pillar 3)
   - Output: `/mnt/user-data/outputs/narrative-world-bible.md`
   - Deadline: 5 days

2. **Faction Lore & Quests** (Priority: MEDIUM)
   - Research: Faction systems (Warframe, Destiny)
   - Deliverable: 3-5 faction profiles with quest lines
   - Include: Motivations, conflicts, key NPCs
   - Quest Design: 20+ hours of content across factions
   - Output: `/mnt/user-data/outputs/faction-quests.md`
   - Deadline: 4 days

3. **Operator Backstories** (Priority: LOW)
   - Research: Character writing for shooters
   - Deliverable: 1-2 page backstory per operator
   - Include: Origin, motivation, personality, relationships
   - Voice: Military thriller tone, grounded
   - Output: Integrated into character doc (Agent 2)
   - Deadline: 3 days

**Research Sources:**
- Escape from Tarkov (world-building)
- Hunt: Showdown (environmental lore)
- Metro 2033 (post-collapse atmosphere)
- The Division (faction conflicts)
- Warframe (quest writing)

**Key Questions to Answer:**
- What caused The Collapse (mystery reveal timeline)?
- How many factions (3-5 for depth)?
- Are factions morally gray or good/evil?
- How much lore is environmental vs told?
- Voice acting budget (full VO or text-only)?

**Deliverable Template:**
```markdown
# Narrative & Lore: Aethelgard

## World Overview

### The Collapse (20 Years Ago)
Aethelgard, once a thriving industrial hub, fell in a single catastrophic event known simply as "The Collapse." Theories abound: a failed weapons test, corporate sabotage, extraterrestrial intervention. The truth remains buried in the ruins.

**Immediate Aftermath:**
- 80% population evacuated or perished
- Government authority dissolved
- Military fragmented into warlord factions
- Corporations seized control of resources

**Present Day:**
- Lawless zone divided among three major factions
- Independent contractors (players) hired for dirty work
- Rumors of what caused The Collapse drive exploration
- High-value tech salvage attracts scavengers worldwide

## Factions

### 1. The Militia (Local Survivors)
**Ideology**: Protect what remains, rebuild society  
**Leader**: Commander Elena Volkov (NPC)  
**Territory**: Industrial Zone (player starting area)  
**Resources**: Manpower, local knowledge, salvaged tech  

**Quests:**
- "Reclaim the Foundry" (Lvl 5) - Clear AI, mark territory
- "Medical Supply Run" (Lvl 10) - Retrieve meds from hospital
- "Rescue Operation" (Lvl 15) - Extract militia member from hostile zone

### 2. Nexus Corporation (Tech Salvagers)
**Ideology**: Profit above all, extract valuable tech  
**Leader**: Dr. Marcus Hayes (NPC)  
**Territory**: Research Complex (northern zone)  
**Resources**: Advanced tech, wealth, private security  

**Quests:**
- "Data Recovery" (Lvl 8) - Retrieve hard drive from server room
- "Rival Elimination" (Lvl 12) - Kill Militia scouts
- "Prototype Retrieval" (Lvl 20) - Secure experimental weapon

### 3. The Scavengers (Opportunists)
**Ideology**: Survival by any means, no loyalty  
**Leader**: None (anarchic collective)  
**Territory**: Slums and Underground (southern zone)  
**Resources**: Numbers, desperation, guerrilla tactics  

**Quests:**
- "Supply Theft" (Lvl 7) - Steal from Militia or Nexus
- "Black Market Deal" (Lvl 11) - Trade illegal goods
- "Sabotage Mission" (Lvl 18) - Destroy Nexus facility

## Main Story Arc (30 Hours)

**Chapter 1: Arrival** (5 hours)
- Player arrives in Aethelgard as independent contractor
- Tutorial missions introduce world and factions
- Mystery: Strange signal detected from Collapse epicenter

**Chapter 2: Investigations** (10 hours)
- Piece together what caused The Collapse
- Faction quests reveal conflicting evidence
- Discovery: Pre-Collapse tech still active underground

**Chapter 3: The Truth** (8 hours)
- Access restricted zones with faction help
- Confront ethical dilemma: reveal truth or keep secret?
- Climax: Player choice affects faction relationships

**Chapter 4: Consequences** (7 hours)
- Fallout from player's choice
- Final confrontation with chosen faction's enemies
- Ending: Aethelgard's fate decided (multiple endings)
```

---

### Agent 9: Social & Clan Systems Designer

**Research Focus:** Squad play, clans, VOIP, social features

**Primary Tasks:**

1. **Squad & Party System** (Priority: LOW)
   - Research: Modern squad systems (Apex, CoD)
   - Deliverable: Party formation, voice chat, shared loot
   - Include: Solo queue protection, squad sizes (2-4)
   - Balance: Solo players must be viable
   - Output: `/mnt/user-data/outputs/squad-system.md`
   - Deadline: 3 days

2. **Clan System** (Priority: LOW - Post-Launch)
   - Research: Clan features (Clash of Clans, Destiny)
   - Deliverable: Clan creation, perks, events
   - Include: Clan wars, shared stash, reputation
   - Deferred: Not MVP, but plan architecture
   - Output: `/mnt/user-data/outputs/clan-system.md`
   - Deadline: 2 days

3. **VOIP & Communication** (Priority: MEDIUM)
   - Research: In-game voice chat (Apex, Valorant)
   - Deliverable: VOIP system design
   - Include: Proximity chat, squad chat, text chat
   - Moderation: Toxicity prevention, reporting
   - Output: `/mnt/user-data/outputs/communication-system.md`
   - Deadline: 2 days

**Research Sources:**
- Apex Legends (ping system, VOIP)
- Destiny 2 (clan systems)
- Clash of Clans (clan structure)
- Valorant (voice chat + moderation)
- Sea of Thieves (proximity chat)

**Key Questions to Answer:**
- Squad sizes: 2-player, 3-player, or 4-player squads?
- Proximity VOIP: risky but immersive?
- Clan features at launch or deferred?
- Friend list size limits?
- Spectator mode for dead squadmates?

---

## 🔄 Integration & Dependencies

### Document Dependency Graph

```
Design Pillars (DONE)
    ├─→ Combat Systems (Agent 1)
    ├─→ Character/Operators (Agent 2)
    ├─→ Map Design (Agent 3)
    ├─→ Economy (Agent 4)
    └─→ Monetization (Agent 5)

Inventory & Gear (DONE)
    ├─→ Combat Systems (weapon stats)
    ├─→ Map Design (loot tables)
    └─→ Economy (pricing, repairs)

Competitive Analysis (DONE)
    ├─→ All Agents (benchmarking)
    └─→ Monetization (F2P best practices)

Character/Operators (Agent 2)
    ├─→ Combat Systems (weapon preferences)
    ├─→ Narrative (backstories)
    └─→ Monetization (unlocks, skins)

Map Design (Agent 3)
    ├─→ Combat Systems (engagement distances)
    ├─→ Economy (loot values)
    └─→ Narrative (environmental storytelling)

Economy (Agent 4)
    ├─→ Monetization (currency conversion)
    ├─→ Map Design (loot value balance)
    └─→ Technical (database schema)

Technical Requirements (Agent 6)
    ├─→ All Agents (feasibility check)
    └─→ Budget/Timeline constraints
```

### Cross-Agent Communication Protocol

**Weekly Sync Meeting**: Every Monday, all agents present progress
- Show deliverables
- Raise blockers
- Identify dependencies
- Adjust timelines

**Async Communication**: Shared Notion/Google Docs workspace
- Comment on each other's work
- Flag conflicts early
- Share research findings

**Version Control**: All markdown files in GitHub repo
- Branch per agent
- Pull requests for review
- Merge to main weekly

---

## ✅ Quality Standards

### Deliverable Acceptance Criteria

**All documents must include:**
1. ✅ Research sources cited (min 5 per doc)
2. ✅ Competitive analysis (what competitors do)
3. ✅ Original design decisions (not just copying)
4. ✅ Metrics and targets (measurable success)
5. ✅ Integration points (how it connects to other systems)
6. ✅ Visual aids (tables, diagrams, flowcharts)
7. ✅ Examples and templates (show, don't just tell)
8. ✅ Balancing rationale (why these numbers?)

**Markdown Formatting:**
- Proper headers (H1 for title, H2 for sections)
- Tables for data (readable, aligned)
- Code blocks for formulas/schemas
- Bullet points for lists
- Bold/italic for emphasis (sparingly)

**Tone & Voice:**
- Professional but not dry
- Specific, not vague (actual numbers, not "some")
- Opinionated but justified (explain why)
- Developer-friendly (implementable)

---

## 📊 Progress Tracking

### Task Dashboard

| Agent | Primary Focus | Status | Progress | Blocker | ETA |
|:------|:-------------|:-------|:---------|:--------|:----|
| Agent 1 | Combat & Weapons | 🔴 Not Started | 0% | Waiting for assignment | 7 days |
| Agent 2 | Characters & Operators | 🔴 Not Started | 0% | Waiting for assignment | 8 days |
| Agent 3 | Map & Level Design | 🔴 Not Started | 0% | Waiting for assignment | 10 days |
| Agent 4 | Economy & Progression | 🔴 Not Started | 0% | Waiting for assignment | 10 days |
| Agent 5 | Monetization & LiveOps | 🔴 Not Started | 0% | Waiting for assignment | 10 days |
| Agent 6 | Technical Requirements | 🔴 Not Started | 0% | Waiting for assignment | 10 days |
| Agent 7 | Art & Audio | 🔴 Not Started | 0% | Waiting for assignment | 10 days |
| Agent 8 | Narrative & Lore | 🔴 Not Started | 0% | Waiting for assignment | 12 days |
| Agent 9 | Social Systems | 🔴 Not Started | 0% | Waiting for assignment | 7 days |

**Status Legend:**
- 🔴 Not Started
- 🟡 In Progress
- 🟢 Complete (Pending Review)
- ✅ Approved

---

## 📅 Timeline & Milestones

### Phase 1: Core Systems (Weeks 1-2)
**Priority: Combat, Characters, Map**

- Day 1-3: Agent 1 (Combat & Weapons)
- Day 1-4: Agent 2 (Characters & Operators)
- Day 1-5: Agent 3 (Map Design)
- **Milestone**: Core gameplay pillars defined

### Phase 2: Meta Systems (Weeks 2-3)
**Priority: Economy, Monetization, Technical**

- Day 7-10: Agent 4 (Economy & Progression)
- Day 7-10: Agent 5 (Monetization & LiveOps)
- Day 7-10: Agent 6 (Technical Requirements)
- **Milestone**: Meta loops and tech stack defined

### Phase 3: Polish & Narrative (Weeks 3-4)
**Priority: Art, Audio, Narrative, Social**

- Day 14-17: Agent 7 (Art & Audio Direction)
- Day 14-18: Agent 8 (Narrative & Lore)
- Day 14-17: Agent 9 (Social Systems)
- **Milestone**: Complete GDD suite ready

### Phase 4: Review & Integration (Week 4)
**All Agents: Cross-review and refinement**

- Day 21-23: Peer review all documents
- Day 24-25: Address conflicts and gaps
- Day 26-27: Final integration and formatting
- Day 28: **FINAL DELIVERY**

**Total Timeline**: 4 weeks (28 days)

---

## 🚀 Post-Completion Next Steps

### Once All Documents Complete:

1. **GDD Master Assembly**
   - Compile all agent work into unified GDD
   - Create table of contents and navigation
   - Cross-link all documents
   - Generate PDF export for stakeholders

2. **Technical Specification Handoff**
   - Convert GDD to Jira/Linear tickets
   - Assign development tasks to engineering team
   - Set up sprint planning based on MVP scope

3. **Art Bible Creation**
   - Use Agent 7's work to create visual style guide
   - Commission concept art based on descriptions
   - Create UI/UX mockups in Figma

4. **Prototype Development**
   - Build greybox environment (Month 1)
   - Implement core combat loop (Month 2)
   - Playtest and iterate (Month 3-4)

5. **Investor/Publisher Pitch**
   - Create pitch deck using GDD insights
   - Produce vertical slice video
   - Prepare financial projections
   - Secure funding for full production

---

## 📞 Support & Escalation

### Questions or Blockers?

**For clarification on assignments:**
- Contact: Project Lead
- Response Time: <24 hours

**For technical feasibility questions:**
- Contact: Agent 6 (Technical Specialist)
- Response Time: <48 hours

**For design conflicts:**
- Contact: Creative Director
- Escalation: Design Pillars are final authority

**For timeline concerns:**
- Contact: Project Manager
- Flexibility: Can extend by 1 week max

---

## 📚 Appendix: Research Resource Library

### Recommended Reading/Viewing

**Extraction Shooter Design:**
- Tarkov Wiki: https://escapefromtarkov.fandom.com
- Hunt: Showdown Dev Blogs: https://www.huntshowdown.com/news
- Arena Breakout Guides: YouTube channels
- Delta Force Gameplay: Twitch streamers

**GDD Best Practices:**
- "How to Write a GDD" (Game Developer article)
- "One-Page GDD" (Stone Librande GDC talk)
- "Living Documents" (GitBook best practices)

**Mobile Game Design:**
- "Mobile Game Design Essentials" (Book)
- Unity Mobile Optimization Guide
- Unreal Engine Mobile Documentation

**F2P Monetization:**
- "Free-to-Play: Making Money From Games" (Book)
- "Ethical F2P Design" (GDC talks)
- Apex Legends Monetization Case Study

---

## ✨ Final Notes

**To All Agents:**

This is a **collaborative effort**. Your work will directly shape the game millions of players will experience. Take pride in your research, be thorough in your documentation, and don't hesitate to challenge assumptions if you find better solutions.

**Remember:**
- Quality over speed (better to take an extra day than deliver poor work)
- Research-driven decisions (cite your sources)
- Player-first mindset (will this make the game more fun?)
- Integration awareness (how does your work affect others?)

**Good luck, and let's build something amazing!**

---

**Document Maintainer**: Claude AI (Planning Orchestrator)  
**Last Updated**: 2026-02-11  
**Status**: ACTIVE - Awaiting Agent Execution  
**Next Review**: Upon 50% completion of all tasks
