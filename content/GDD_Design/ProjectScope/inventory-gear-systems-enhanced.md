---
title: "Inventory & Gear Systems - Enhanced Edition"
linkTitle: "Inventory & Gear"
type: docs
weight: 60
version: 2.0
last_updated: 2026-02-11
---

> **Document Status**: Living Document - Updated Regularly  
> **Target Platform**: PC (Primary), Console (Secondary)  
> **Reference Games**: Escape from Tarkov, Arena Breakout: Infinite, Delta Force, Hunt: Showdown 1896, Gray Zone Warfare

---

## Executive Summary

This document outlines the comprehensive Inventory & Gear systems for our extraction shooter. The design philosophy centers on **meaningful choices**, **spatial puzzle-solving**, and **risk-reward balance**. Unlike traditional shooters where inventory is an afterthought, our system makes inventory management a core gameplay pillar that directly impacts tactical decisions, player progression, and moment-to-moment survival.

**Key Differentiators:**
- Tetris-style spatial inventory with rotation mechanics
- Weight-based movement penalties (realistic encumbrance)
- Zone-based armor protection system
- Tactical accessibility (where items are stored matters)
- Economic risk-reward loop (lose gear on death)

---

## 1. Design Philosophy & Core Pillars

### 1.1 Core Design Pillars

**Pillar 1: Spatial Puzzle Management**
- Inventory space is a physical constraint requiring spatial reasoning
- Items have real-world dimensions (1x1 bandage vs 4x2 rifle)
- Players must constantly optimize their loadout like a Tetris puzzle
- Rotation mechanics (90°) enable creative packing solutions
- *Design Goal*: Create satisfying "Tetris moments" when perfectly fitting high-value loot

**Pillar 2: Weight Has Consequences**
- Every item has realistic mass affecting movement
- Overburdening creates exponential penalties (stamina, speed, inertia)
- Prevents "Call of Duty movement" with 60kg+ loadouts
- Forces tactical choices: armor vs mobility, loot vs escape
- *Design Goal*: Make weight feel tangible and impactful

**Pillar 3: Risk-Reward Economics**
- High-tier gear increases survival but risks economic loss
- Insurance system provides partial safety net
- Secure container protects critical items
- Meta-game loop: invest in gear → raid → extract loot → upgrade → repeat
- *Design Goal*: Create meaningful "gearing fear" and "loot excitement"

**Pillar 4: Tactical Ergonomics**
- Item accessibility depends on storage location
- Magazines in backpack = no quick reload
- Meds in tactical rig = hotkey accessible
- Realistic simulation of "reaching for gear under fire"
- *Design Goal*: Reward preparation and punish poor loadout planning

### 1.2 Player Experience Goals

**New Player Experience:**
- Introduce systems gradually through tutorial raids
- Start with simple loadouts (pistol + small backpack)
- Progressive unlocking of equipment slots and features
- Clear visual feedback for weight/space constraints

**Veteran Player Mastery:**
- Min-max optimization of space and weight
- "Meta" knowledge of item values per slot
- Speed-looting techniques (muscle memory keybinds)
- Loadout planning for specific raid objectives

**Emotional Beats:**
- *Tension*: Managing limited space during hot loot
- *Satisfaction*: Perfect Tetris packing of valuable items
- *Fear*: Extracting with expensive gear while overweight
- *Loss*: Death and gear loss creating memorable moments
- *Triumph*: Successful extraction with full inventory

---

## 2. The Character Loadout System (Paper Doll)

### 2.1 Primary Interface

The character loadout is the player's pre-raid equipment screen, featuring:
- 3D character model (rotatable 360°)
- Equipment slots surrounding the model
- Real-time stat display (armor rating, weight, movement speed)
- Visual damage indicators (durability bars)

### 2.2 Equipment Slots - Detailed Breakdown

| Slot Name | Grid Size | Hotkey | Durability | Function & Design Notes |
|:----------|:----------|:-------|:-----------|:------------------------|
| **Headset** | 1x1 | No | N/A | **CRITICAL GAMEPLAY ITEM**<br>Modifies audio mix (compresses gunshots +20dB, amplifies footsteps -40dB)<br>Different models have unique EQ profiles<br>Example: ComTac 4 (warm bass), GSSH-01 (harsh treble)<br>*Balance Note*: Considered "mandatory meta" - all kits include one |
| **Helmet** | 2x2 | No | Yes | Zone-based protection (Top, Nape, Ears, Eyes, Jaws)<br>Can mount: NVGs, Visors, Lights, Cameras<br>Class 1-6 armor rating per zone<br>Weight: 0.8kg - 2.5kg<br>*Design Note*: Trade-off between coverage and weight |
| **Face Cover** | 1x1 | No | Some | Identity concealment + minor benefits<br>Types: Balaclava (no armor), Tactical Mask (Class 1-2)<br>Reduces skin reflection for stealth<br>Some provide minor flash/frag protection |
| **Body Armor** | Variable | No | Yes | *Used ONLY if wearing non-armored Tactical Rig*<br>Protects Thorax/Stomach zones<br>No storage capacity<br>Class 1-6 protection<br>Material types affect durability/weight/repair cost |
| **Tactical Rig** | Variable | **YES** | Varies | **CRITICAL SLOT** - Determines quick-access storage<br>Can be: Unarmored (pure storage) or Armored (replaces Body Armor)<br>Required for `R` key reload mechanic<br>Typical capacity: 12-24 slots (1x1 cells)<br>*Design Note*: Most important decision point for loadout |
| **Primary Weapon 1** | Weapon | **1** | Yes | Main weapon on sling (chest carry)<br>Fastest draw after melee<br>Weapon stats: Ergonomics, Recoil, Weight |
| **Primary Weapon 2** | Weapon | **2** | Yes | Secondary weapon on back<br>~0.5s slower draw than Primary 1<br>Used for role flexibility (DMR + CQB) |
| **Sidearm** | Weapon | **3** | Yes | Pistol in holster<br>Fastest weapon switch (~0.3s)<br>Last resort backup |
| **Scabbard** | Weapon | **V** | N/A | Melee weapon slot<br>Uses: Silent kills, breaking glass/doors, desperation<br>Instant switch (faster than sidearm) |
| **Pockets** | 4x1 | **4-0** | N/A | Built-in storage (always available)<br>Hotkey assignments possible<br>Typical use: Keys, loose meds, grenades<br>Cannot be lost on death |
| **Backpack** | Variable | No | N/A | Main loot storage (5x5 to 7x8 grid)<br>Items here **CANNOT** be hotkeyed<br>Weight affects movement significantly<br>Lost on death unless secured |
| **Secure Container** | Variable | No | N/A | **SURVIVES DEATH** - keeps contents always<br>Size: 2x2 (Standard) to 3x4 (EOD Edition)<br>*Anti-Abuse Rules*: Cannot place Found-In-Raid weapons, thermal scopes, or helmets while in raid<br>Can place: Keys, small valuables, meds, ammo |
| **Armband** | 1x1 | No | N/A | Purely cosmetic/team identification<br>No gameplay impact<br>Visible on left arm |
| **Special Slots** | - | - | - | Additional context-specific slots:<br>- Compass (if equipped)<br>- Rangefinder<br>- Radio (for VOIP communication) |

### 2.3 Visual Design Requirements

**UI/UX Specifications:**
- Grid-based drag-drop with smooth animations
- Color coding: Green (available space), Red (invalid placement), Yellow (equipped)
- Tooltip on hover showing: Item name, Weight, Size, Value, Durability
- Real-time stat updates when swapping gear
- Sound effects: Clinking metal, fabric rustling, clicks for satisfaction

**Accessibility Features:**
- Colorblind mode (pattern overlays)
- Scalable UI (100%-200%)
- Keybind remapping for all hotkeys
- Auto-sort function (controversial but requested)

---

## 3. The Equipment System - Deep Dive

### 3.1 Armor & Ballistics Mechanics

**Armor Class System (1-6):**

| Class | Protection Level | Typical Threats Blocked | Example Use Case |
|:------|:----------------|:------------------------|:-----------------|
| **1** | Shrapnel, Low-velocity | 9mm, Shotgun (distance), Shrapnel | Civilian protection |
| **2** | Pistol rounds | Most pistols, weak SMG rounds | Police/Security armor |
| **3** | Rifle (non-AP) | 5.56x45, 7.62x39 (FMJ) | Standard military |
| **4** | Rifle (AP resistant) | 5.56 M855A1, most intermediate rounds | High-end military |
| **5** | AP rounds | 7.62x51 AP, .338 Lapua | Special forces |
| **6** | Extreme AP | 7.62x54R BS/Igolnik, .50 BMG (limited) | Tank crew, EOD |

**Coverage Zones (Hitbox System):**
- **Head Zones**: Top, Nape, Ears, Eyes, Jaws (individually protected by helmet parts)
- **Torso Zones**: 
  - Trauma Plate Area (heart/lungs) - Usually Class 5-6
  - Soft Armor Area (stomach/sides) - Usually Class 3-4
  - No Coverage (arms) - Unprotected
  
**Material Properties:**

| Material | Protection | Durability | Weight | Repair Cost | Notes |
|:---------|:-----------|:-----------|:-------|:------------|:------|
| **Ceramic** | ★★★★★ | ★★☆☆☆ | Medium | $ | Shatters quickly but cheap to replace |
| **Steel** | ★★★★☆ | ★★★★★ | High | $$ | Heavy but lasts long, repairs well |
| **Aramid/Kevlar** | ★★☆☆☆ | ★★★★☆ | Low | $ | Soft armor, flexible, low protection |
| **UHMWPE** | ★★★★☆ | ★★★★☆ | Low | $$$ | Modern polymer, lightweight but expensive |
| **Titanium** | ★★★★★ | ★★★★☆ | Medium | $$$$ | Premium, balanced stats, very costly |

**Blunt Damage System:**
- Even penetration failures cause damage based on bullet energy
- Formula: `BluntDamage = (BulletEnergy × 0.2) × (1 - ArmorAbsorption)`
- Example: 5.56 hitting Class 4 = ~8 HP blunt damage
- Creates "bruising" effect even on successful armor stops
- Can still be lethal through armor in sustained fire

**Durability & Degradation:**
- Each hit reduces armor durability points
- Penetrations cause 2x durability loss
- Zero durability = armor becomes Class 0 (useless)
- Repair mechanics:
  - Trader repairs: Lose max durability permanently
  - Max durability affects protection effectiveness
  - Example: 50/70 armor = ~71% effective protection

### 3.2 Tactical Rigs vs. Armored Rigs - Strategic Choice

**Decision Matrix:**

| Factor | Chest Rig (Unarmored) | Armored Rig | Body Armor + Chest Rig |
|:-------|:---------------------|:------------|:-----------------------|
| **Protection** | None | Class 3-5 | Class 4-6 |
| **Storage Slots** | 18-24 | 12-18 | 12-24 |
| **Weight** | 0.8-1.5kg | 8-12kg | 10-15kg |
| **Cost** | $ | $$ | $$$ |
| **Flexibility** | Can swap rig mid-raid | Fixed setup | Can swap rig, keep armor |
| **Best For** | Budget runs, Speed, Scav hunting | Mid-tier PvP, Balanced | High-tier raids, Tank builds |

**Popular Loadout Strategies:**
1. **Budget Rat**: PACA armor + Berkut rig (Class 2 protection, 18 slots, 5kg total)
2. **Mid-Tier Chad**: 6B3TM Armored Rig (Class 4, 16 slots, 9.5kg)
3. **Full Send**: Slick Plate Carrier + Wartech TV-110 (Class 6 + 20 slots, 14kg)
4. **Speed Demon**: No armor + Blackrock rig (0kg armor, 20 slots, maximum mobility)

### 3.3 Headsets (Tactical Audio) - Critical Meta Item

**Audio Processing Technology:**
- **Active Noise Cancellation (ANC)**: Reduces deafening sounds
  - Gunfire compression: -30dB to -40dB
  - Explosion compression: -50dB
  - Prevents audio distortion and hearing damage
  
- **Ambient Sound Amplification (ASA)**: Boosts environmental audio
  - Footsteps: +15dB to +25dB
  - Voices: +10dB
  - Door/window interactions: +20dB
  - Grenade pin pulls: +15dB

**Headset Variety (EQ Profiles):**

| Model | EQ Character | Pros | Cons | Best For |
|:------|:------------|:-----|:-----|:---------|
| **ComTac 4** | Warm, Bassy | Great for outdoor, Comfortable | Misses high-freq indoor sounds | Woods, Open areas |
| **GSSH-01** | Harsh, Treble-heavy | Excellent indoor clarity | Tiring long-term, Crunch artifacts | CQB, Factory |
| **Peltor Sport** | Balanced, Neutral | Versatile, Reliable | No specific strengths | All-around |
| **Sordin Supreme** | Mid-focused | Great for voices, Team comms | Weak bass, Misses distant sounds | Team play |
| **MSA Sordin** | Enhanced clarity | Best long-range audio | Expensive, Heavy | Sniping, Overwatch |

**Gameplay Impact:**
- 90% of experienced players use headsets
- Considered "mandatory meta" like in Tarkov
- Hearing enemy first = massive tactical advantage
- Sound propagation through materials (concrete vs wood)
- Vertical audio (above/below floor detection)

### 3.4 Weapon Customization System

**Modular Design Philosophy:**
- Weapons are platforms, not fixed items
- 40-100 attachments per weapon family
- Real-time stat changes: Ergonomics, Recoil, Weight, Accuracy

**Customization Categories:**

1. **Receivers & Lower Parts**
   - Base platform selection
   - Fire mode groups (safe/semi/auto)
   - Receiver material (aluminum, polymer)

2. **Barrels**
   - Length affects: Velocity, Accuracy, Concealment
   - Threading for muzzle devices
   - Weapon durability (barrel life)

3. **Muzzle Devices**
   - Suppressors: -25 to -35dB sound reduction, +recoil
   - Muzzle brakes: -30% vertical recoil, +sound
   - Flash hiders: -90% muzzle flash, neutral stats
   - Compensators: -20% horizontal recoil

4. **Stocks & Grips**
   - Ergonomics modifier: +5 to +35
   - Recoil control: -5% to -20%
   - Foldable stocks (reduce weapon size)
   - Cheek risers for optic height

5. **Optics & Sights**
   - Iron sights (0 ergo penalty)
   - Red dots (fast acquisition, +10 ergo)
   - Magnified scopes (zoom, -15 ergo, +weight)
   - Thermal/NV (extreme advantage, very expensive)

6. **Tactical Accessories**
   - Flashlights (blind enemies, reveal position)
   - Lasers (hipfire accuracy, visible beam)
   - Foregrips (recoil reduction)
   - Canted sights (backup close-range)

**Meta Builds Examples:**

*M4A1 "Meta Recoil Build":*
- MOE Stock + RK-1 Grip + Wave MB = 48 Vertical Recoil (base: 75)
- Cost: ~$120,000 Rubles
- Weight: 4.2kg (loaded)
- Ergonomics: 62

*AK-74N "Budget Performer":*
- Wood stock + Polymer grip + DTK-1 Muzzle = 63 Vertical Recoil
- Cost: ~$25,000 Rubles
- Weight: 3.8kg
- Ergonomics: 42

---

## 4. The Grid System Mechanics - Core Technology

### 4.1 Item Physicality & Dimensions

**Size System:**
- All items defined by Width × Height in 1x1 cells
- Rotation: 90° increments (R key while dragging)
- Visual representation matches grid size

**Common Item Sizes:**

| Item Category | Typical Size | Examples | Stack Size |
|:-------------|:------------|:---------|:-----------|
| Small consumables | 1x1 | Bandage, Pills, Ammo (60rds) | Varies |
| Magazines | 1x2 | AR mags, Pistol mags | No stack |
| Grenades | 1x2 | Frag, Flash, Smoke | No stack |
| Pistols | 2x1 | Most handguns | N/A |
| SMGs | 2x2 - 3x2 | MP5, Vector | N/A |
| Rifles | 4x1 - 5x2 | M4, AK-74 (stock extended) | N/A |
| Sniper Rifles | 5x2 - 6x2 | SVD, M700 | N/A |
| Helmets | 2x2 | Most tactical helmets | N/A |
| Armor Vests | 3x3 - 4x4 | Plate carriers | N/A |
| Backpacks | 3x3 - 7x8 | (collapsed vs deployed) | N/A |

### 4.2 Stacking System

**Stackable Items:**
- Ammunition: 60 rounds per stack (caliber-specific)
- Currency: 
  - Rubles: 500,000 per stack
  - Dollars: 50,000 per stack
  - Euros: 50,000 per stack
- Crafting materials: Varies (screws: 10, bolts: 15)

**Non-Stackable Items:**
- Weapons, Armor, Attachments
- Keys (each unique)
- Quest items
- Most barter goods (design choice to create scarcity)

**Stacking Strategy Tips:**
- Always consolidate partial stacks before raid
- Use "Sort" function to auto-consolidate
- Prioritize full stacks for efficient space usage

### 4.3 Container Nesting (Bag-in-Bag)

**Nesting Rules:**
1. Containers can be placed inside larger containers
2. **Anti-Exploit**: Cannot nest identical container IDs
3. **Size Requirement**: Inner container must physically fit in outer grid
4. **Weight Accumulation**: All nested items add to total weight

**Practical Examples:**

✅ **Legal Nesting:**
- Berkut Backpack (5x5) inside Pilgrim Backpack (6x7)
- MBSS Backpack (4x5) inside Berkut (5x5)
- Scav Backpack (4x4) inside any larger bag

❌ **Illegal Nesting (Blocked):**
- Beta Backpack inside another Beta Backpack
- Same-ID container stacking (infinite space exploit)
- Container larger than available grid cells

**Economic Meta:**
- "THICC Case inside THICC Case" = 2x storage but heavy
- Nested backpacks on PMC extractions = profit strategy
- Scav runs: Bring empty bag, fill with nested bags + loot

### 4.4 Folding & Collapsing Mechanics

**Weapon Folding:**
- **Foldable Stocks**: AK-74, MPX, MP5 variants
- Size Reduction: Typically -1 width cell
  - Example: AK-74M 5x2 → 4x2 (folded)
- **Penalties When Fired Folded:**
  - +300% vertical recoil
  - -80% ergonomics
  - Severe accuracy loss
  - Intended for transport, not combat

**Backpack Collapsing:**
- Empty backpacks can be "rolled up"
- Collapsed sizes:
  - Small bags (MBSS): 3x3 → 2x2
  - Medium bags (Berkut): 5x5 → 3x3
  - Large bags (Pilgrim): 6x7 → 4x4
- *Design Intent*: Reward bringing extra bags for loot

**Container Management:**
- Item cases remain fixed size
- Weapon cases: 5x5 external, 10x5 internal
- Ammo cases: 2x2 external, 7x7 internal
- Med cases: 2x2 external, 7x5 internal

---

## 5. Encumbrance & Movement System

### 5.1 Weight Calculation

**Total Carried Weight Formula:**
```
TotalWeight = EquippedGear + InventoryContents + NestedContainers
```

**Base Character Stats:**
- Strength Level affects max carry capacity
- Base Strength (Lvl 1): 25kg comfortable, 60kg max
- Elite Strength (Lvl 51): 35kg comfortable, 75kg max

### 5.2 Weight Threshold System (Detailed)

| Tier | Weight Range | Movement Speed | Sprint Drain | Inertia | Jump | Noise | Special Effects |
|:-----|:------------|:--------------|:------------|:--------|:-----|:------|:---------------|
| **Light** | 0-25kg | 100% | 1.0x | Low | 100% | -5dB | None |
| **Medium** | 25-40kg | 85% | 1.5x | Medium | 75% | Normal | Cannot jump while sprinting |
| **Heavy** | 40-55kg | 60% | 2.5x | High | 40% | +8dB | No sprint stamina regen, Reduced turn speed |
| **Critical** | 55-70kg | 30% | N/A | Very High | 0% | +15dB | Cannot sprint, Cannot jump, Cannot prone quickly |
| **Overweight** | 70kg+ | 10% | N/A | Extreme | 0% | +25dB | Constant stamina drain, Cannot crouch-walk, Audible breathing |

### 5.3 Derived Penalties (Detailed Breakdown)

**Inertia System:**
- Simulates realistic momentum and physics
- **Low Inertia** (Light load):
  - Instant direction changes
  - Responsive A-D strafing
  - Quick stop animation (~0.1s)
  
- **Medium Inertia**:
  - 0.2s acceleration time
  - Slight sliding on stop
  - Noticeable "tank feeling"
  
- **High Inertia** (Heavy load):
  - 0.5s acceleration/deceleration
  - Cannot quick-peek effectively
  - "Boat-like" movement feel
  
- **Extreme Inertia** (Overweight):
  - 1.0s+ to change direction
  - Almost impossible to dodge shots
  - Forces pre-planned movement

**Stamina System:**
- Sprint Stamina: Depletes during running/jumping
- Arm Stamina: Depletes while ADSing
- Both affected by weight tier

**Stamina Regeneration Rates:**

| Tier | Sprint Stamina Regen | Arm Stamina Regen | Standing Still Bonus |
|:-----|:--------------------|:------------------|:---------------------|
| Light | 100% | 100% | +50% |
| Medium | 75% | 85% | +30% |
| Heavy | 40% | 60% | +10% |
| Critical | 0% | 30% | 0% |
| Overweight | -20%/s (drain) | 15% | 0% |

**Audio Penalties:**
- Heavier players make louder footsteps
- Gear rattling sounds increase with weight
- Breathing becomes audible at Critical+ tiers
- "Death sentence" at Overweight (everyone hears you)

**Tactical Implications:**
- Light loadouts: Aggressive playstyle, flanking, rushing
- Medium: Balanced approach, standard engagements
- Heavy: Defensive, hold positions, avoid chases
- Critical+: Extract immediately or stash loot

---

## 6. In-Raid Interactions & Player UX

### 6.1 Looting Mechanics - Step-by-Step

**Opening Inventory (`Tab` key):**
1. Screen splits: Left (Vicinity/Containers), Right (Your inventory)
2. Time does NOT freeze (hardcore mode)
3. Audio muffled but still audible (danger awareness)

**Vicinity Search System:**
- Auto-scans 1.5m radius sphere
- Shows loose floor items as icons
- Real-time updates (items appear/disappear)
- Max 50 items displayed (performance limit)

**Container Search Flow:**

1. **Initial State**: Container appears blacked out with "???" icons
2. **Search Action**: 
   - Player clicks "Search" button
   - Progress bar appears (duration: 1-5 seconds)
   - Duration modified by:
     - Perception Skill Level: -0.1s per level (max -5s at Elite)
     - Container type: Jacket (1s), Crate (2s), Safe (5s)
     - Light level: -50% speed in darkness
3. **Progressive Reveal**:
   - Items appear one-by-one as bar fills
   - High value items revealed last (suspense mechanic)
   - Can cancel search mid-way (partial reveal)
4. **Post-Search State**: Container remains open for instant access

**Unknown Item Examination:**
- New items show "?" icon + blurred image
- Middle-click or "Examine" button to identify
- Examination time: 0.5s - 2s (item complexity)
- Grants small XP reward (Attention skill)
- Cannot use/equip unexamined items

### 6.2 Quick Loot Techniques (Advanced)

**Keybind Shortcuts:**

| Action | Keybind | Description | Use Case |
|:-------|:--------|:-----------|:---------|
| Quick Move | `Ctrl + Click` | Moves to first available space | Grab loot fast |
| Quick Equip | `Alt + Click` | Equips to correct slot | Swap armor mid-raid |
| Discard | `Del` | Drops item on ground | Make space urgently |
| Rotate While Dragging | `R` | 90° rotation | Tetris optimization |
| Examine | `Middle Click` | Identify unknown item | Learn new items |
| Fold Stock | `Middle Click` (on weapon) | Toggle fold state | Pack weapons |
| Stack/Merge | `Ctrl + Click` (on stack) | Auto-combine partial stacks | Ammo consolidation |
| Filter Search | `/` (in search bar) | Text filter containers | Find specific items |

**Pro Player Strategies:**
1. **Pre-Raid Preparation**:
   - Leave empty space in specific patterns
   - Pre-plan high-value item slots
   - Memorize valuable item sizes
   
2. **In-Raid Optimization**:
   - Loot bodies in safe cover first
   - Use "Ctrl+Click" for speed (muscle memory)
   - Delete low-value items immediately
   - Rotate items while dragging for efficiency
   
3. **Extract Optimization**:
   - Final inventory sort before extract
   - Consolidate stacks to free slots
   - Drop least valuable items if overweight
   - Emergency discard for weight tier management

### 6.3 Advanced Inventory Management

**Value Per Slot Calculation:**
- Mental math critical for efficiency
- Formula: `Value/Slot = Item Price ÷ (Width × Height)`
- Examples:
  - GPU (2x1 slot) = 800,000₽ / 2 = **400,000₽/slot**
  - Helmet (2x2 slot) = 60,000₽ / 4 = **15,000₽/slot**
  - Condensed Milk (1x1) = 18,000₽ / 1 = **18,000₽/slot**

**Loot Priority Hierarchy (Descending):**
1. Quest items (always take)
2. High value/slot items (GPUs, LEDx, Bitcoins)
3. Keys (infinite value potential)
4. Small high-tier ammo
5. Weapon parts (specific meta items)
6. Barter items for hideout upgrades
7. Weapons (only if space efficient or needed)
8. Low value/slot items (ditch immediately)

**Inventory Organization Best Practices:**
- Top rows: Medical supplies (quick access)
- Middle rows: Ammo, mags, grenades
- Bottom rows: Barter items, valuables
- Use containers to categorize (if brought in)

---

## 7. Weapon Modding (Gunsmith System)

### 7.1 Gunsmith Interface Design

**UI Layout:**
- Center: 3D weapon model (rotatable, zoomable)
- Left Panel: Available parts in stash (filtered by compatibility)
- Right Panel: Current build stats + comparison
- Bottom: Quick presets bar

**Node-Based System:**
```
[Receiver]
    ├─ [Handguard]
    │   ├─ [Foregrip]
    │   ├─ [Tactical Device]
    │   └─ [Side Rails]
    ├─ [Barrel]
    │   └─ [Muzzle Device]
    ├─ [Optics Mount]
    │   ├─ [Primary Optic]
    │   └─ [Backup Sight]
    ├─ [Stock/Tube]
    │   └─ [Stock]
    ├─ [Pistol Grip]
    └─ [Magazine]
```

### 7.2 Compatibility Logic System

**Automatic Validation:**
- Ghost slots show valid attachments only
- Red highlight for conflicts (e.g., muzzle blocks suppressor)
- Yellow warning for sub-optimal choices
- Green checkmark for optimal meta builds

**Conflict Examples:**
- Long barrel + Short handguard = Exposed barrel (ugly but functional)
- Suppressor + Muzzle brake = Cannot equip both
- Heavy stock + Light buffer = Incompatible threading
- High-profile optic + Low rail = Clearance issue

### 7.3 Live Stat Calculation

**Real-Time Updates:**
- **Ergonomics**: 0-100 scale (affects ADS speed, stamina drain)
- **Vertical Recoil**: 20-150 scale (lower is better)
- **Horizontal Recoil**: 20-150 scale
- **Effective Distance**: Meters (barrel length, caliber)
- **Total Weight**: Kilograms
- **Muzzle Velocity**: m/s (affects ballistics)
- **Durability Burn**: Rounds until cleaning needed

**Comparison Mode:**
- Side-by-side stat bars (current vs new)
- Red/Green arrows showing improvement/degradation
- Percentage change labels
- "Meta rating" indicator (community consensus)

### 7.4 Preset System

**Saving Builds:**
1. Complete weapon customization
2. Click "Save as Preset"
3. Name build (e.g., "M4 - CQB Meta")
4. Preset saved to library

**Using Presets:**
- **Auto-Purchase**: Buys all missing parts from traders
- **Auto-Assemble**: Equips all parts automatically
- **Partial Build**: Warns if parts unavailable
- **Cost Preview**: Shows total expense before buying

**Preset Sharing:**
- Export preset code (alphanumeric string)
- Import community builds
- Ranked by popularity/effectiveness
- Wiki integration for "current meta" builds

---

## 8. Stash Management (Meta-Game Economy)

### 8.1 Stash Progression System

**Base Stash Sizes:**
- **Standard Edition**: 10×28 (280 cells)
- **Left Behind Edition**: 10×38 (380 cells)
- **Prepare for Escape Edition**: 10×48 (480 cells)
- **Edge of Darkness (EOD)**: 10×68 (680 cells)

**Stash Upgrades (Hideout):**
- Level 1 → 2: +10 rows (+100 cells), Cost: 3.5M₽
- Level 2 → 3: +10 rows, Cost: 8.5M₽
- Level 3 → 4: +10 rows, Cost: 15M₽
- Max Stash (Level 4): 10×68 cells (all editions equal)

### 8.2 Container System (Solution to Hoarding)

**Essential Containers:**

| Container | External Size | Internal Size | Efficiency Ratio | Best For | Cost |
|:----------|:-------------|:-------------|:----------------|:---------|:-----|
| **Scav Junkbox** | 4×4 (16) | 16×16 (256) | **16:1** | Barter items only | 1.2M₽ |
| **Items Case** | 2×2 (4) | 8×8 (64) | **16:1** | Any item type | 2.5M₽ |
| **Weapon Case** | 5×5 (25) | 10×5 (50) | **2:1** | Weapons, attachments | 600K₽ |
| **Ammo Case** | 2×2 (4) | 7×7 (49) | **12:1** | Ammunition, mags | 350K₽ |
| **Medicine Case** | 2×2 (4) | 7×5 (35) | **8.75:1** | Medical supplies | 280K₽ |
| **Magazine Case** | 2×2 (4) | 6×6 (36) | **9:1** | Magazines only | 180K₽ |
| **Grenade Case** | 2×2 (4) | 7×7 (49) | **12:1** | Grenades, throwables | 350K₽ |
| **Keytool** | 1×1 (1) | 4×4 (16) | **16:1** | Keys, keycards | 250K₽ |
| **Docs Case** | 1×2 (2) | 4×4 (16) | **8:1** | Keys, money, maps | 350K₽ |
| **THICC Items Case** | 3×3 (9) | 14×14 (196) | **21.8:1** | Ultimate storage | 18M₽ |
| **THICC Weapon Case** | 5×5 (25) | 15×8 (120) | **4.8:1** | Massive weapon storage | 11M₽ |

**Strategic Investment Priority:**
1. **Early Game**: Scav Junkbox (immediate value)
2. **Mid Game**: Ammo Case, Med Case, Weapon Case
3. **Late Game**: Items Case, THICC Cases
4. **Always Useful**: Keytool, Docs Case (bring in-raid)

### 8.3 Stash Organization Strategies

**"Zone" System:**
- **Top Zone** (Rows 1-10): Active gear (ready-to-raid)
  - Weapons, armor, rigs for next raid
  - Frequently used items
  
- **Middle Zone** (Rows 11-40): Storage containers
  - Organize by container type
  - Group related items (all ammo cases together)
  
- **Bottom Zone** (Rows 41+): Long-term storage
  - Quest items for future tasks
  - Hideout upgrade materials
  - Rarely used items

**Auto-Sort Controversy:**
- **Pro**: Instant organization, saves time
- **Con**: Destroys custom layouts, breaks muscle memory
- **Community Consensus**: Avoid using after establishing layout
- **Alternative**: Manual "sort by category" folders concept

**Optimal Layout Example (EOD Stash):**
```
Rows 1-5: Current loadout sets (5 full kits)
Rows 6-10: Spare weapons wall
Rows 11-15: Scav Junkboxes ×4 (barter items)
Rows 16-20: Ammo Cases ×5, Med Cases ×3
Rows 21-25: Weapon Cases ×3
Rows 26-30: Items Cases ×4 (valuables)
Rows 31-40: Armor/helmet storage
Rows 41-50: Quest item organization
Rows 51-68: THICC Cases ×3 (ultimate storage)
```

### 8.4 Economic Decision-Making

**Sell vs. Keep Matrix:**

| Item Type | Sell If... | Keep If... |
|:----------|:-----------|:-----------|
| Weapons | Not using within 3 raids | Meta build or needed for quest |
| Armor | Durability <40% | Class 5+ and >60% |
| Barter Items | Not needed for hideout | Required for upgrade or craft |
| Ammo | Have 500+ rounds | Good AP ammo, <300 rounds |
| Meds | Have 20+ of type | Rare or valuable (Surv12) |
| Keys | Looted room 5+ times | Rare spawns or quest |

**Value Timing Strategy:**
- Some items spike in value during events
- Quest items more valuable when quest is active
- Hideout materials surge when new upgrades unlock
- Monitor Flea Market trends for profit

---

## 9. Development Implementation Guide

### 9.1 Technical Architecture

**Data Structure Example (JSON):**
```json
{
  "itemID": "guid_a1b2c3d4",
  "tpl": "template_id_m4a1_base",
  "location": {
    "x": 0,
    "y": 0,
    "r": 0,  // rotation: 0=horizontal, 1=vertical
    "parentId": "backpack_guid_xyz789",
    "slotId": "main"  // or "pocket_1", "tactical_rig", etc.
  },
  "upd": {
    "Repairable": {
      "Durability": 92,
      "MaxDurability": 100
    },
    "FireMode": {
      "FireMode": "fullauto"
    },
    "Foldable": {
      "Folded": false
    },
    "Sight": {
      "ScopesCurrentCalibPointIndexes": [0],
      "ScopesSelectedModes": [0]
    }
  },
  "mods": {
    "mod_barrel": ["item_guid_barrel_10inch"],
    "mod_stock": ["item_guid_stock_moe"],
    ...
  }
}
```

### 9.2 Server-Side Validation (Critical)

**Anti-Cheat Measures:**
1. **Grid Overlap Prevention**:
   - Server validates all item placements
   - Checks for overlapping items
   - Rejects invalid grid positions
   
2. **Weight Hacking Detection**:
   - Server calculates total weight independently
   - Compares client-reported vs actual
   - Flags discrepancies >5% for review
   
3. **Container Exploit Prevention**:
   - Validates nesting rules server-side
   - Prevents infinite loops (container ID tracking)
   - Checks size constraints
   
4. **Item Duplication Protection**:
   - UUID tracking for all items
   - Database uniqueness constraints
   - Transaction rollback on conflicts

**Validation Checklist (Every Move):**
- [ ] Item fits in target grid
- [ ] No overlap with existing items
- [ ] Weight limit not exceeded
- [ ] Nesting rules satisfied
- [ ] Item exists and owned by player
- [ ] Target container has capacity
- [ ] Action timestamp reasonable (no time manipulation)

### 9.3 Client-Side Implementation

**Drag & Drop Library Recommendations:**
- **Unreal Engine**: Enhanced Input + Slate DragDrop system
- **Unity**: Custom IBeginDragHandler, IDragHandler, IEndDragHandler
- **Web (if applicable)**: React DnD, Interact.js

**Grid Cell Checking Algorithm:**
```pseudo
function canPlaceItem(item, gridX, gridY, rotation):
  itemWidth, itemHeight = getItemSize(item, rotation)
  
  for y in range(gridY, gridY + itemHeight):
    for x in range(gridX, gridX + itemWidth):
      if !isWithinGridBounds(x, y):
        return false
      if isCellOccupied(x, y):
        return false
  
  return true
```

**Performance Optimization:**
- Grid occupancy stored as 2D boolean array (fast lookups)
- Only validate affected cells on item move
- Cache item size calculations
- Use object pooling for UI elements (inventory slots)
- Lazy load container contents (only when opened)

### 9.4 UI/UX Design Specifications

**Visual Feedback Requirements:**
- **Drag State**: Item follows cursor with 50% opacity
- **Valid Placement**: Green outline on grid cells
- **Invalid Placement**: Red outline, shake animation
- **Snap-to-Grid**: Magnetic snapping for satisfying feel
- **Sound Effects**:
  - Pickup: Light "clink" or "rustle"
  - Place: Heavier "thud" based on item weight
  - Invalid: "Error buzz" sound
  - Stack merge: Satisfying "cash register" ding

**Color Coding System:**
- **White**: Common items
- **Green**: Uncommon
- **Blue**: Rare
- **Purple**: Epic
- **Orange**: Legendary
- **Red**: Quest/Unique
- **Yellow**: Found in Raid (FiR) status

**Tooltip Information Architecture:**
```
┌─────────────────────────────┐
│ [ICON] Item Name            │
│ Rarity Badge | FiR Badge    │
├─────────────────────────────┤
│ Size: 2x3 | Weight: 1.5kg   │
│ Value: ₽125,000            │
│ Durability: 85/100 ████░░  │
├─────────────────────────────┤
│ Short description text...   │
├─────────────────────────────┤
│ STATS:                      │
│ • Armor Class: 4            │
│ • Protection Zones: T,S,A   │
│ • Material: Ceramic         │
├─────────────────────────────┤
│ Required for:               │
│ • Quest "Punisher Pt. 4"    │
│ • Hideout Upgrade: Lvl 2    │
└─────────────────────────────┘
```

---

## 10. Playtesting & Iteration Plan

### 10.1 Metrics to Track

**Quantitative Data:**
- Average time spent in inventory (in-raid vs stash)
- Inventory open frequency per raid
- Items discarded per raid (indicates space pressure)
- Weight tier distribution (% raids at each tier)
- Container usage statistics (which bought most)
- Item rotation usage (how often players use R key)
- Failed item placements (UX friction point)

**Qualitative Feedback:**
- Player surveys on "inventory satisfaction"
- Interviews about "frustration points"
- Observations of first-time player behavior
- Community feedback on forums/Discord

### 10.2 Balance Tuning Targets

**Ideal Benchmarks:**
- 70% of players should run Medium weight tier
- 15% Light (speed runners), 10% Heavy (tanks), 5% Critical (loot hoarders)
- Inventory time should be <30% of raid duration
- 80% of players should use at least 1 storage container
- Auto-sort usage <20% (indicates good layout design)

### 10.3 Known Issues & Future Improvements

**Current Limitations:**
- Auto-sort algorithm not smart enough (v1.0)
- Lack of "loadout presets" for full kits
- No search/filter in stash (huge QoL missing)
- Container nesting rules confusing for new players
- Weight penalties feel too harsh >60kg (common feedback)

**Roadmap Items:**
- **v1.1**: Search bar for stash, Loadout preset system
- **v1.2**: Smart auto-sort (remembers player preferences)
- **v1.3**: Mobile app for stash management (out-of-game)
- **v2.0**: Dynamic container sizes, New container types
- **v2.5**: AI-assisted inventory optimization suggestions

---

## 11. Competitive Analysis - Key Takeaways

### 11.1 What We're Copying (Proven Successful)

**From Escape from Tarkov:**
- Tetris grid system (industry standard now)
- Weight-based movement penalties (hardcore feel)
- Zone-based armor (realistic ballistics)
- Found in Raid (FiR) system (anti-RMT measure)

**From Arena Breakout: Infinite:**
- Cleaner UI/UX (less overwhelming for new players)
- Better onboarding tooltips
- Faster looting animations (QoL)

**From Delta Force:**
- Operator ability system integration
- Vehicle storage mechanics
- Multiple extraction methods

**From Hunt: Showdown:**
- Trait system affecting inventory (future feature)
- Perma-death consequences for gear
- Prestige system integration

### 11.2 What We're Improving (Innovation Points)

**Our Unique Features:**
1. **Hybrid Weight System**: Combines realistic physics with arcadey accessibility
   - Hardcore mode: Full realism
   - Standard mode: -25% weight penalties
   
2. **AI-Assisted Sorting**: Machine learning predicts player preferences
   - Learns from manual organization patterns
   - Suggests optimal layouts
   
3. **Cross-Raid Loadout Persistence**: Save full loadouts with one click
   - "Loadout slots" system (5 presets)
   - Quick-swap entire kit before raid
   
4. **Dynamic Container Expansion**: Containers level up with use
   - "Well-used Medcase" gains +2 slots after 100 uses
   - Encourages long-term item relationships

5. **Social Features**: 
   - Stash sharing with squad (view-only)
   - Gift items to friends (trade system)
   - Shared squad stash (clan feature)

---

## 12. Accessibility & Inclusivity

### 12.1 Difficulty Modes

**Casual Mode:**
- -25% weight penalties
- +50% stash size
- Auto-sort improved intelligence
- Highlighted "valuable items" in containers
- Tutorial tooltips always available

**Standard Mode:**
- Balanced design (as documented above)
- Default experience

**Hardcore Mode:**
- +25% weight penalties
- No auto-sort function
- No examine shortcuts (must inspect manually)
- Realistic search times (no skill speed-up)
- Limited UI information

### 12.2 Accessibility Features

**Visual Accessibility:**
- Colorblind modes (Deuteranopia, Protanopia, Tritanopia)
- High contrast mode
- Adjustable UI scale (80% - 200%)
- Icon-based item recognition (not color-dependent)

**Physical Accessibility:**
- Full keybind remapping
- Mouse sensitivity sliders (separate for inventory vs gameplay)
- Toggle vs hold options for all actions
- Macro support (within fairness rules)

**Cognitive Accessibility:**
- Adjustable tutorial system (skip/repeat)
- Complexity levels (hide advanced stats initially)
- Reference wiki integration (in-game tooltips)
- Practice mode (zero-stakes inventory management)

---

## 13. Monetization Considerations

### 13.1 Ethical F2P Integration (If Applicable)

**Acceptable Paid Features:**
- Cosmetic stash themes (visual reskins)
- Additional loadout preset slots (convenience)
- Stash expansion (but achievable in-game too)
- Special containers with unique looks (same capacity as in-game)

**NEVER Sell:**
- Pay-to-win items (better stats)
- Exclusive storage sizes (P2W advantage)
- Faster looting animations (competitive advantage)
- Anything affecting gameplay balance

### 13.2 Premium Edition Differences

**Standard vs. Premium:**
- Stash Size: 10×28 vs 10×48 (or both upgradeable to 10×68)
- Secure Container: 2×2 vs 3×3 (significant but not gamebreaking)
- Starting Containers: 0 vs 1 of each basic type
- Cosmetics: Basic vs Unique weapon skins, stash themes

**Progression Balance:**
- Standard players should reach parity within 200 hours
- Premium gives head-start, not permanent advantage
- All content accessible to all players eventually

---

## 14. Localization & Cultural Considerations

### 14.1 Text Localization Challenges

**Item Name Translation:**
- Military jargon varies by region (AK-74 vs Type 74)
- Slang terms need cultural equivalents
- Measurement units (kg vs lbs, toggleable)

**UI Text Expansion:**
- Some languages take 40% more space (German)
- Grid labels must be abbreviation-friendly
- Icon-heavy design reduces text dependency

### 14.2 Cultural Sensitivity

**Armor & Gear Branding:**
- Avoid real military unit insignias (legal issues)
- Generic faction names instead of real countries
- Respect cultural symbols (no offensive emblems)

**Looting Mechanics:**
- Some cultures sensitive to corpse looting
- Option to "transfer gear" instead of "loot body" (language)

---

## 15. Conclusion & Vision

This Inventory & Gear system is designed to be a **core gameplay pillar**, not an afterthought. Players should feel:
- **Satisfaction** from spatial puzzle-solving
- **Tension** from weight management under pressure
- **Progression** from stash organization and optimization
- **Mastery** from efficient looting techniques

By studying the best-in-class extraction shooters and innovating beyond them, we aim to create an inventory system that is:
- **Deep enough** to engage hardcore players
- **Accessible enough** to welcome newcomers
- **Fair** in monetization and balance
- **Respectful** of player time and effort

**Next Steps:**
1. Prototype core grid system (2 weeks)
2. Implement weight system with visual feedback (3 weeks)
3. Build container nesting logic (2 weeks)
4. Create gunsmith interface (4 weeks)
5. Playtest with 50 players, iterate based on feedback (ongoing)

---

## Appendix A: Glossary of Terms

- **ADS**: Aim Down Sights
- **AP**: Armor Piercing (ammunition type)
- **Chad**: Slang for heavily geared player
- **EOD**: Edge of Darkness (premium edition)
- **Ergo**: Ergonomics stat
- **Extract**: Leave the raid successfully
- **FiR**: Found in Raid status
- **Keytool**: Small key storage container
- **Meta**: Most Effective Tactics Available
- **PMC**: Player Character (main account)
- **Rat**: Slang for low-gear, sneaky player
- **Rig**: Tactical vest / chest rig
- **Scav**: AI enemy or player scavenger mode
- **Stash**: Persistent out-of-raid storage
- **Tetris**: Spatial inventory management gameplay

---

## Appendix B: Reference Materials

**Competitor Analysis Documents:**
- Escape from Tarkov Wiki: https://escapefromtarkov.fandom.com
- Arena Breakout Guide: (internal document)
- Delta Force Documentation: https://www.playdeltaforce.com

**Design Resources:**
- Realistic Firearm Specifications: https://modernfirearms.net
- Armor Ballistics Data: https://www.nij.gov/topics/equipment
- Military Gear Reference: https://soldiersystems.net

**Development Tools:**
- Grid System Tutorial: (link to internal docs)
- Unreal Engine Drag-Drop API: (documentation)
- Server Validation Best Practices: (security document)

---

**Document Author**: Claude AI (Game Design Consultant)  
**Reviewed By**: [Pending Team Review]  
**Approval Status**: Draft - Awaiting Stakeholder Sign-Off  
**Version History**:
- v1.0 (2024-01-15): Initial draft
- v2.0 (2026-02-11): Enhanced edition with competitive analysis and modern GDD practices
