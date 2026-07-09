---
title: "Inventory & Gear hệ thống - Enhanced Edition"
linkTitle: "Inventory & Gear"
type: docs
weight: 60
version: 2.0
last_updated: 2026-02-11
---

> **tài liệu Status**: Living tài liệu - Updated Regularly  
> **Target Platform**: PC (primary), Console (secondary)  
> **Reference Games**: Escape from Tarkov, Arena Breakout: Infinite, Delta Force, Hunt: Showdown 1896, Gray Zone Warfare

---

## Tóm Tắt Điều Hành

This tài liệu outlines the comprehensive Inventory & Gear hệ thống for our extraction shooter. The design philosophy centers on **meaningful choices**, **spatial puzzle-solving**, và **risk-reward balance**. Unlike traditional shooters where inventory is an afterthought, our hệ thống makes inventory management a cốt lõi gameplay pillar that directly impacts tactical quyết định, người chơi progression, và moment-to-moment survival.

**chính Differentiators:**
- Tetris-style spatial inventory với rotation cơ chế
- Weight-based movement penalties (realistic encumbrance)
- Zone-based giáp protection hệ thống
- Tactical accessibility (where items are stored matters)
- Economic risk-reward loop (lose gear on death)

---

## 1. Design Philosophy & cốt lõi Pillars

### 1.1 cốt lõi Design Pillars

**Pillar 1: Spatial Puzzle Management**
- Inventory space is a physical constraint requiring spatial reasoning
- Items have real-world dimensions (1x1 bandage vs 4x2 rifle)
- người chơi must constantly optimize their loadout like a Tetris puzzle
- Rotation cơ chế (90°) enable creative packing solutions
- *Design mục tiêu*: tạo satisfying "Tetris moments" khi perfectly fitting high-giá trị loot

**Pillar 2: Weight Has Consequences**
- Every item has realistic mass affecting movement
- Overburdening tạo exponential penalties (stamina, speed, inertia)
- Prevents "Call of Duty movement" với 60kg+ loadouts
- Forces tactical choices: giáp vs mobility, loot vs escape
- *Design mục tiêu*: Make weight feel tangible và impactful

**Pillar 3: Risk-Reward Economics**
- High-tier gear increases survival nhưng risks economic loss
- Insurance hệ thống provides partial safety net
- Secure container protects critical items
- Meta-game loop: invest in gear → raid → extract loot → upgrade → repeat
- *Design mục tiêu*: tạo meaningful "gearing fear" và "loot excitement"

**Pillar 4: Tactical Ergonomics**
- Item accessibility depends on storage location
- Magazines in backpack = no quick reload
- Meds in tactical rig = hotkey accessible
- Realistic simulation of "reaching for gear under fire"
- *Design mục tiêu*: Reward preparation và punish poor loadout planning

### 1.2 người chơi trải nghiệm Goals

**New người chơi trải nghiệm:**
- Introduce hệ thống gradually thông qua tutorial raids
- Start với simple loadouts (pistol + small backpack)
- Progressive unlocking of equipment slots và tính năng
- rõ visual feedback for weight/space constraints

**Veteran người chơi Mastery:**
- Min-max optimization of space và weight
- "Meta" knowledge of item values per slot
- Speed-looting techniques (muscle memory keybinds)
- Loadout planning for cụ thể raid objectives

**cảm xúc Beats:**
- *Tension*: Managing limited space trong khi hot loot
- *Satisfaction*: Perfect Tetris packing of valuable items
- *Fear*: Extracting với expensive gear while overweight
- *Loss*: Death và gear loss tạo memorable moments
- *Triumph*: Successful extraction với full inventory

---

## 2. The nhân vật Loadout hệ thống (Paper Doll)

### 2.1 primary Interface

The nhân vật loadout is the người chơi's pre-raid equipment màn hình, featuring:
- 3D nhân vật model (rotatable 360°)
- Equipment slots surrounding the model
- Real-thời gian stat display (giáp rating, weight, movement speed)
- Visual damage indicators (durability bars)

### 2.2 Equipment Slots - chi tiết Breakdown

| Slot Name | Grid Size | Hotkey | Durability | Function & Design ghi chú |
|:----------|:----------|:-------|:-----------|:------------------------|
| **Headset** | 1x1 | No | N/A | **CRITICAL GAMEPLAY ITEM**<br>Modifies audio mix (compresses gunshots +20dB, amplifies footsteps -40dB)<br>Different models have unique EQ profiles<br>Example: ComTac 4 (warm bass), GSSH-01 (harsh treble)<br>*Balance Note*: Considered "mandatory meta" - all kits include one |
| **Helmet** | 2x2 | No | Yes | Zone-based protection (Top, Nape, Ears, Eyes, Jaws)<br>Can mount: NVGs, Visors, Lights, Cameras<br>Class 1-6 giáp rating per zone<br>Weight: 0.8kg - 2.5kg<br>*Design Note*: Trade-off between coverage và weight |
| **Face Cover** | 1x1 | No | Some | Identity concealment + minor benefits<br>Types: Balaclava (no giáp), Tactical Mask (Class 1-2)<br>Reduces skin reflection for stealth<br>Some provide minor flash/frag protection |
| **Body giáp** | Variable | No | Yes | *Used ONLY nếu wearing non-armored Tactical Rig*<br>Protects Thorax/Stomach zones<br>No storage capacity<br>Class 1-6 protection<br>Material types affect durability/weight/repair chi phí |
| **Tactical Rig** | Variable | **YES** | Varies | **CRITICAL SLOT** - Determines quick-access storage<br>Can be: Unarmored (pure storage) hoặc Armored (replaces Body giáp)<br>Required for `R` chính reload cơ chế<br>Typical capacity: 12-24 slots (1x1 cells)<br>*Design Note*: Most quan trọng quyết định point for loadout |
| **primary vũ khí 1** | vũ khí | **1** | Yes | Main vũ khí on sling (chest carry)<br>Fastest draw sau melee<br>vũ khí stats: Ergonomics, Recoil, Weight |
| **primary vũ khí 2** | vũ khí | **2** | Yes | secondary vũ khí on back<br>~0.5s slower draw than primary 1<br>Used for role flexibility (DMR + CQB) |
| **Sidearm** | vũ khí | **3** | Yes | Pistol in holster<br>Fastest vũ khí switch (~0.3s)<br>Last resort backup |
| **Scabbard** | vũ khí | **V** | N/A | Melee vũ khí slot<br>Uses: Silent kills, breaking glass/doors, desperation<br>Instant switch (faster than sidearm) |
| **Pockets** | 4x1 | **4-0** | N/A | Built-in storage (always available)<br>Hotkey assignments possible<br>Typical cách dùng: Keys, loose meds, grenades<br>Cannot be lost on death |
| **Backpack** | Variable | No | N/A | Main loot storage (5x5 to 7x8 grid)<br>Items here **CANNOT** be hotkeyed<br>Weight affects movement significantly<br>Lost on death unless secured |
| **Secure Container** | Variable | No | N/A | **SURVIVES DEATH** - keeps contents always<br>Size: 2x2 (Standard) to 3x4 (EOD Edition)<br>*Anti-Abuse Rules*: Cannot place Found-In-Raid vũ khí, thermal scopes, hoặc helmets while in raid<br>Can place: Keys, small valuables, meds, đạn |
| **Armband** | 1x1 | No | N/A | Purely cosmetic/team identification<br>No gameplay impact<br>hiển thị rõ on left arm |
| **Special Slots** | - | - | - | Additional context-cụ thể slots:<br>- Compass (nếu equipped)<br>- Rangefinder<br>- Radio (for VOIP communication) |

### 2.3 Visual Design yêu cầu

**UI/UX Specifications:**
- Grid-based drag-drop với smooth animations
- Color coding: Green (available space), Red (invalid placement), Yellow (equipped)
- Tooltip on hover showing: Item name, Weight, Size, giá trị, Durability
- Real-thời gian stat updates khi swapping gear
- Sound effects: Clinking metal, fabric rustling, clicks for satisfaction

**Accessibility tính năng:**
- Colorblind mode (pattern overlays)
- Scalable UI (100%-200%)
- Keybind remapping for all hotkeys
- Auto-sort function (controversial nhưng requested)

---

## 3. The Equipment hệ thống - Deep Dive

### 3.1 giáp & Ballistics cơ chế

**giáp Class hệ thống (1-6):**

| Class | Protection Level | Typical Threats Blocked | Example cách dùng Case |
|:------|:----------------|:------------------------|:-----------------|
| **1** | Shrapnel, Low-velocity | 9mm, Shotgun (distance), Shrapnel | Civilian protection |
| **2** | Pistol rounds | Most pistols, weak SMG rounds | Police/Security giáp |
| **3** | Rifle (non-AP) | 5.56x45, 7.62x39 (FMJ) | Standard military |
| **4** | Rifle (AP resistant) | 5.56 M855A1, most intermediate rounds | High-end military |
| **5** | AP rounds | 7.62x51 AP, .338 Lapua | Special forces |
| **6** | Extreme AP | 7.62x54R BS/Igolnik, .50 BMG (limited) | Tank crew, EOD |

**Coverage Zones (Hitbox hệ thống):**
- **Head Zones**: Top, Nape, Ears, Eyes, Jaws (individually protected by helmet parts)
- **Torso Zones**: 
  - Trauma Plate Area (heart/lungs) - Usually Class 5-6
  - Soft giáp Area (stomach/sides) - Usually Class 3-4
  - No Coverage (arms) - Unprotected
  
**Material Properties:**

| Material | Protection | Durability | Weight | Repair chi phí | ghi chú |
|:---------|:-----------|:-----------|:-------|:------------|:------|
| **Ceramic** |  |  | Medium | $ | Shatters quickly nhưng cheap to replace |
| **Steel** |  |  | High | $$ | Heavy nhưng lasts long, repairs well |
| **Aramid/Kevlar** |  |  | Low | $ | Soft giáp, flexible, low protection |
| **UHMWPE** |  |  | Low | $$$ | Modern polymer, lightweight nhưng expensive |
| **Titanium** |  |  | Medium | $$$$ | Premium, balanced stats, very costly |

**Blunt Damage hệ thống:**
- Even penetration failures cause damage based on bullet energy
- Formula: `BluntDamage = (BulletEnergy × 0.2) × (1 - ArmorAbsorption)`
- Example: 5.56 hitting Class 4 = ~8 HP blunt damage
- tạo "bruising" effect even on successful giáp stops
- Can still be lethal thông qua giáp in sustained fire

**Durability & Degradation:**
- Each hit reduces giáp durability points
- Penetrations cause 2x durability loss
- Zero durability = giáp becomes Class 0 (useless)
- Repair cơ chế:
  - Trader repairs: Lose max durability permanently
  - Max durability affects protection effectiveness
  - Example: 50/70 giáp = ~71% effective protection

### 3.2 Tactical Rigs vs. Armored Rigs - Strategic Choice

**quyết định matrix:**

| Factor | Chest Rig (Unarmored) | Armored Rig | Body giáp + Chest Rig |
|:-------|:---------------------|:------------|:-----------------------|
| **Protection** | None | Class 3-5 | Class 4-6 |
| **Storage Slots** | 18-24 | 12-18 | 12-24 |
| **Weight** | 0.8-1.5kg | 8-12kg | 10-15kg |
| **chi phí** | $ | $$ | $$$ |
| **Flexibility** | Can swap rig mid-raid | Fixed setup | Can swap rig, keep giáp |
| **Best For** | Budget runs, Speed, Scav hunting | Mid-tier PvP, Balanced | High-tier raids, Tank builds |

**Popular Loadout Strategies:**
1. **Budget Rat**: PACA giáp + Berkut rig (Class 2 protection, 18 slots, 5kg total)
2. **Mid-Tier Chad**: 6B3TM Armored Rig (Class 4, 16 slots, 9.5kg)
3. **Full Send**: Slick Plate Carrier + Wartech TV-110 (Class 6 + 20 slots, 14kg)
4. **Speed Demon**: No giáp + Blackrock rig (0kg giáp, 20 slots, maximum mobility)

### 3.3 Headsets (Tactical Audio) - Critical Meta Item

**Audio Processing Technology:**
- **Active Noise Cancellation (ANC)**: Reduces deafening sounds
  - Gunfire compression: -30dB to -40dB
  - Explosion compression: -50dB
  - Prevents audio distortion và hearing damage
  
- **Ambient Sound Amplification (ASA)**: Boosts environmental audio
  - Footsteps: +15dB to +25dB
  - Voices: +10dB
  - Door/window interactions: +20dB
  - Grenade pin pulls: +15dB

**Headset Variety (EQ Profiles):**

| Model | EQ nhân vật | Pros | Cons | Best For |
|:------|:------------|:-----|:-----|:---------|
| **ComTac 4** | Warm, Bassy | Great for outdoor, Comfortable | Misses high-freq indoor sounds | Woods, Open areas |
| **GSSH-01** | Harsh, Treble-heavy | Excellent indoor clarity | Tiring long-term, Crunch artifacts | CQB, Factory |
| **Peltor Sport** | Balanced, Neutral | Versatile, Reliable | No cụ thể strengths | All-around |
| **Sordin Supreme** | Mid-focused | Great for voices, Team comms | Weak bass, Misses distant sounds | Team play |
| **MSA Sordin** | Enhanced clarity | Best long-range audio | Expensive, Heavy | Sniping, Overwatch |

**Gameplay Impact:**
- 90% of experienced người chơi cách dùng headsets
- Considered "mandatory meta" like in Tarkov
- Hearing địch first = massive tactical advantage
- Sound propagation thông qua materials (concrete vs wood)
- Vertical audio (above/below floor detection)

### 3.4 vũ khí Customization hệ thống

**Modular Design Philosophy:**
- vũ khí are platforms, not fixed items
- 40-100 attachments per vũ khí family
- Real-thời gian stat changes: Ergonomics, Recoil, Weight, Accuracy

**Customization Categories:**

1. **Receivers & Lower Parts**
   - Base platform selection
   - Fire mode groups (safe/semi/auto)
   - Receiver material (aluminum, polymer)

2. **Barrels**
   - Length affects: Velocity, Accuracy, Concealment
   - Threading for muzzle devices
   - vũ khí durability (barrel life)

3. **Muzzle Devices**
   - Suppressors: -25 to -35dB sound reduction, +recoil
   - Muzzle brakes: -30% vertical recoil, +sound
   - Flash hiders: -90% muzzle flash, neutral stats
   - Compensators: -20% horizontal recoil

4. **Stocks & Grips**
   - Ergonomics modifier: +5 to +35
   - Recoil control: -5% to -20%
   - Foldable stocks (reduce vũ khí size)
   - Cheek risers for optic height

5. **Optics & Sights**
   - Iron sights (0 ergo penalty)
   - Red dots (fast acquisition, +10 ergo)
   - Magnified scopes (zoom, -15 ergo, +weight)
   - Thermal/NV (extreme advantage, very expensive)

6. **Tactical Accessories**
   - Flashlights (blind địch, reveal position)
   - Lasers (hipfire accuracy, hiển thị rõ beam)
   - Foregrips (recoil reduction)
   - Canted sights (backup close-range)

**Meta Builds Examples:**

*M4A1 "Meta Recoil Build":*
- MOE Stock + RK-1 Grip + Wave MB = 48 Vertical Recoil (base: 75)
- chi phí: ~$120,000 Rubles
- Weight: 4.2kg (loaded)
- Ergonomics: 62

*AK-74N "Budget Performer":*
- Wood stock + Polymer grip + DTK-1 Muzzle = 63 Vertical Recoil
- chi phí: ~$25,000 Rubles
- Weight: 3.8kg
- Ergonomics: 42

---

## 4. The Grid hệ thống cơ chế - cốt lõi Technology

### 4.1 Item Physicality & Dimensions

**Size hệ thống:**
- All items defined by Width × Height in 1x1 cells
- Rotation: 90° increments (R chính while dragging)
- Visual representation matches grid size

**Common Item Sizes:**

| Item Category | Typical Size | Examples | Stack Size |
|:-------------|:------------|:---------|:-----------|
| Small consumables | 1x1 | Bandage, Pills, đạn (60rds) | Varies |
| Magazines | 1x2 | AR mags, Pistol mags | No stack |
| Grenades | 1x2 | Frag, Flash, Smoke | No stack |
| Pistols | 2x1 | Most handguns | N/A |
| SMGs | 2x2 - 3x2 | MP5, Vector | N/A |
| Rifles | 4x1 - 5x2 | M4, AK-74 (stock extended) | N/A |
| Sniper Rifles | 5x2 - 6x2 | SVD, M700 | N/A |
| Helmets | 2x2 | Most tactical helmets | N/A |
| giáp Vests | 3x3 - 4x4 | Plate carriers | N/A |
| Backpacks | 3x3 - 7x8 | (collapsed vs deployed) | N/A |

### 4.2 Stacking hệ thống

**Stackable Items:**
- Ammunition: 60 rounds per stack (caliber-cụ thể)
- Currency: 
  - Rubles: 500,000 per stack
  - Dollars: 50,000 per stack
  - Euros: 50,000 per stack
- Crafting materials: Varies (screws: 10, bolts: 15)

**Non-Stackable Items:**
- vũ khí, giáp, Attachments
- Keys (each unique)
- Quest items
- Most barter goods (design choice to tạo scarcity)

**Stacking Strategy Tips:**
- Always consolidate partial stacks trước raid
- cách dùng "Sort" function to auto-consolidate
- Prioritize full stacks for efficient space usage

### 4.3 Container Nesting (Bag-in-Bag)

**Nesting Rules:**
1. Containers can be placed inside larger containers
2. **Anti-Exploit**: Cannot nest identical container IDs
3. **Size yêu cầu**: Inner container must physically fit in outer grid
4. **Weight Accumulation**: All nested items add to total weight

**Practical Examples:**

 **Legal Nesting:**
- Berkut Backpack (5x5) inside Pilgrim Backpack (6x7)
- MBSS Backpack (4x5) inside Berkut (5x5)
- Scav Backpack (4x4) inside any larger bag

 **Illegal Nesting (Blocked):**
- Beta Backpack inside another Beta Backpack
- Same-ID container stacking (infinite space exploit)
- Container larger than available grid cells

**Economic Meta:**
- "THICC Case inside THICC Case" = 2x storage nhưng heavy
- Nested backpacks on PMC extractions = profit strategy
- Scav runs: Bring empty bag, fill với nested bags + loot

### 4.4 Folding & Collapsing cơ chế

**vũ khí Folding:**
- **Foldable Stocks**: AK-74, MPX, MP5 variants
- Size Reduction: Typically -1 width cell
  - Example: AK-74M 5x2 → 4x2 (folded)
- **Penalties khi Fired Folded:**
  - +300% vertical recoil
  - -80% ergonomics
  - Severe accuracy loss
  - Intended for transport, not combat

**Backpack Collapsing:**
- empty backpacks can be "rolled up"
- Collapsed sizes:
  - Small bags (MBSS): 3x3 → 2x2
  - Medium bags (Berkut): 5x5 → 3x3
  - Large bags (Pilgrim): 6x7 → 4x4
- *Design Intent*: Reward bringing extra bags for loot

**Container Management:**
- Item cases remain fixed size
- vũ khí cases: 5x5 external, 10x5 internal
- đạn cases: 2x2 external, 7x7 internal
- Med cases: 2x2 external, 7x5 internal

---

## 5. Encumbrance & Movement hệ thống

### 5.1 Weight Calculation

**Total Carried Weight Formula:**
```
TotalWeight = EquippedGear + InventoryContents + NestedContainers
```

**Base nhân vật Stats:**
- Strength Level affects max carry capacity
- Base Strength (Lvl 1): 25kg comfortable, 60kg max
- Elite Strength (Lvl 51): 35kg comfortable, 75kg max

### 5.2 Weight Threshold hệ thống (chi tiết)

| Tier | Weight Range | Movement Speed | Sprint Drain | Inertia | Jump | Noise | Special Effects |
|:-----|:------------|:--------------|:------------|:--------|:-----|:------|:---------------|
| **Light** | 0-25kg | 100% | 1.0x | Low | 100% | -5dB | None |
| **Medium** | 25-40kg | 85% | 1.5x | Medium | 75% | Normal | Cannot jump while sprinting |
| **Heavy** | 40-55kg | 60% | 2.5x | High | 40% | +8dB | No sprint stamina regen, Reduced turn speed |
| **Critical** | 55-70kg | 30% | N/A | Very High | 0% | +15dB | Cannot sprint, Cannot jump, Cannot prone quickly |
| **Overweight** | 70kg+ | 10% | N/A | Extreme | 0% | +25dB | Constant stamina drain, Cannot crouch-walk, Audible breathing |

### 5.3 Derived Penalties (chi tiết Breakdown)

**Inertia hệ thống:**
- Simulates realistic momentum và physics
- **Low Inertia** (Light load):
  - Instant direction changes
  - Responsive A-D strafing
  - Quick stop animation (~0.1s)
  
- **Medium Inertia**:
  - 0.2s acceleration thời gian
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

**Stamina hệ thống:**
- Sprint Stamina: Depletes trong khi running/jumping
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
- Heavier người chơi make louder footsteps
- Gear rattling sounds increase với weight
- Breathing becomes audible at Critical+ tiers
- "Death sentence" at Overweight (everyone hears you)

**Tactical Implications:**
- Light loadouts: Aggressive playstyle, flanking, rushing
- Medium: Balanced approach, standard engagements
- Heavy: Defensive, hold positions, avoid chases
- Critical+: Extract immediately hoặc stash loot

---

## 6. In-Raid Interactions & người chơi UX

### 6.1 Looting cơ chế - Step-by-Step

**Opening Inventory (`Tab` chính):**
1. màn hình splits: Left (Vicinity/Containers), Right (Your inventory)
2. thời gian does NOT freeze (hardcore mode)
3. Audio muffled nhưng still audible (danger awareness)

**Vicinity Search hệ thống:**
- Auto-scans 1.5m radius sphere
- Shows loose floor items as icons
- Real-thời gian updates (items appear/disappear)
- Max 50 items displayed (performance limit)

**Container Search flow:**

1. **Initial trạng thái**: Container appears blacked out với "???" icons
2. **Search Action**: 
   - người chơi clicks "Search" button
   - Progress bar appears (duration: 1-5 seconds)
   - Duration modified by:
     - Perception Skill Level: -0.1s per level (max -5s at Elite)
     - Container type: Jacket (1s), Crate (2s), Safe (5s)
     - Light level: -50% speed in darkness
3. **Progressive Reveal**:
   - Items appear one-by-one as bar fills
   - High giá trị items revealed last (suspense cơ chế)
   - Can cancel search mid-way (partial reveal)
4. **Post-Search trạng thái**: Container remains open for instant access

**Unknown Item Examination:**
- New items show "?" icon + blurred image
- Middle-click hoặc "Examine" button to identify
- Examination thời gian: 0.5s - 2s (item complexity)
- Grants small XP reward (Attention skill)
- Cannot cách dùng/equip unexamined items

### 6.2 Quick Loot Techniques (Advanced)

**Keybind Shortcuts:**

| Action | Keybind | Description | cách dùng Case |
|:-------|:--------|:-----------|:---------|
| Quick Move | `Ctrl + Click` | Moves to first available space | Grab loot fast |
| Quick Equip | `Alt + Click` | Equips to correct slot | Swap giáp mid-raid |
| Discard | `Del` | Drops item on ground | Make space urgently |
| Rotate While Dragging | `R` | 90° rotation | Tetris optimization |
| Examine | `Middle Click` | Identify unknown item | Learn new items |
| Fold Stock | `Middle Click` (on vũ khí) | Toggle fold trạng thái | Pack vũ khí |
| Stack/Merge | `Ctrl + Click` (on stack) | Auto-combine partial stacks | đạn consolidation |
| Filter Search | `/` (in search bar) | Text filter containers | Find cụ thể items |

**Pro người chơi Strategies:**
1. **Pre-Raid Preparation**:
   - Leave empty space in cụ thể patterns
   - Pre-plan high-giá trị item slots
   - Memorize valuable item sizes
   
2. **In-Raid Optimization**:
   - Loot bodies in safe cover first
   - cách dùng "Ctrl+Click" for speed (muscle memory)
   - Delete low-giá trị items immediately
   - Rotate items while dragging for efficiency
   
3. **Extract Optimization**:
   - Final inventory sort trước extract
   - Consolidate stacks to free slots
   - Drop least valuable items nếu overweight
   - Emergency discard for weight tier management

### 6.3 Advanced Inventory Management

**giá trị Per Slot Calculation:**
- Mental math critical for efficiency
- Formula: `Value/Slot = Item Price ÷ (Width × Height)`
- Examples:
  - GPU (2x1 slot) = 800,000₽ / 2 = **400,000₽/slot**
  - Helmet (2x2 slot) = 60,000₽ / 4 = **15,000₽/slot**
  - Condensed Milk (1x1) = 18,000₽ / 1 = **18,000₽/slot**

**Loot Priority Hierarchy (Descending):**
1. Quest items (always take)
2. High giá trị/slot items (GPUs, LEDx, Bitcoins)
3. Keys (infinite giá trị potential)
4. Small high-tier đạn
5. vũ khí parts (cụ thể meta items)
6. Barter items for Safe House upgrades
7. vũ khí (only nếu space efficient hoặc needed)
8. Low giá trị/slot items (ditch immediately)

**Inventory Organization Best Practices:**
- Top rows: Medical supplies (quick access)
- Middle rows: đạn, mags, grenades
- Bottom rows: Barter items, valuables
- cách dùng containers to categorize (nếu brought in)

---

## 7. vũ khí Modding (Gunsmith hệ thống)

### 7.1 Gunsmith Interface Design

**UI Layout:**
- Center: 3D vũ khí model (rotatable, zoomable)
- Left Panel: available parts in stash (filtered by compatibility)
- Right Panel: hiện tại build stats + comparison
- Bottom: Quick presets bar

**Node-Based hệ thống:**
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

### 7.2 Compatibility Logic hệ thống

**Automatic Validation:**
- Ghost slots show valid attachments only
- Red highlight for conflicts (e.g., muzzle blocks suppressor)
- Yellow cảnh báo for sub-optimal choices
- Green checkmark for optimal meta builds

**Conflict Examples:**
- Long barrel + Short handguard = Exposed barrel (ugly nhưng functional)
- Suppressor + Muzzle brake = Cannot equip both
- Heavy stock + Light buffer = Incompatible threading
- High-profile optic + Low rail = Clearance issue

### 7.3 Live Stat Calculation

**Real-thời gian Updates:**
- **Ergonomics**: 0-100 scale (affects ADS speed, stamina drain)
- **Vertical Recoil**: 20-150 scale (lower is better)
- **Horizontal Recoil**: 20-150 scale
- **Effective Distance**: Meters (barrel length, caliber)
- **Total Weight**: Kilograms
- **Muzzle Velocity**: m/s (affects ballistics)
- **Durability Burn**: Rounds until cleaning needed

**Comparison Mode:**
- Side-by-side stat bars (hiện tại vs new)
- Red/Green arrows showing improvement/degradation
- Percentage change labels
- "Meta rating" indicator (community consensus)

### 7.4 Preset hệ thống

**Saving Builds:**
1. Complete vũ khí customization
2. Click "Save as Preset"
3. Name build (e.g., "M4 - CQB Meta")
4. Preset saved to library

**Using Presets:**
- **Auto-purchase**: Buys all missing parts from traders
- **Auto-Assemble**: Equips all parts automatically
- **Partial Build**: Warns nếu parts unavailable
- **chi phí preview**: Shows total expense trước buying

**Preset Sharing:**
- Export preset code (alphanumeric string)
- Import community builds
- Ranked by popularity/effectiveness
- Wiki integration for "hiện tại meta" builds

---

## 8. Stash Management (Meta-Game Economy)

### 8.1 Stash Progression hệ thống

**Base Stash Sizes:**
- **Standard Edition**: 10×28 (280 cells)
- **Left Behind Edition**: 10×38 (380 cells)
- **Prepare for Escape Edition**: 10×48 (480 cells)
- **Edge of Darkness (EOD)**: 10×68 (680 cells)

**Stash Upgrades (Safe House):**
- Level 1 → 2: +10 rows (+100 cells), chi phí: 3.5M₽
- Level 2 → 3: +10 rows, chi phí: 8.5M₽
- Level 3 → 4: +10 rows, chi phí: 15M₽
- Max Stash (Level 4): 10×68 cells (all editions equal)

### 8.2 Container hệ thống (Solution to Hoarding)

**Essential Containers:**

| Container | External Size | Internal Size | Efficiency Ratio | Best For | chi phí |
|:----------|:-------------|:-------------|:----------------|:---------|:-----|
| **Scav Junkbox** | 4×4 (16) | 16×16 (256) | **16:1** | Barter items only | 1.2M₽ |
| **Items Case** | 2×2 (4) | 8×8 (64) | **16:1** | Any item type | 2.5M₽ |
| **vũ khí Case** | 5×5 (25) | 10×5 (50) | **2:1** | vũ khí, attachments | 600K₽ |
| **đạn Case** | 2×2 (4) | 7×7 (49) | **12:1** | Ammunition, mags | 350K₽ |
| **Medicine Case** | 2×2 (4) | 7×5 (35) | **8.75:1** | Medical supplies | 280K₽ |
| **Magazine Case** | 2×2 (4) | 6×6 (36) | **9:1** | Magazines only | 180K₽ |
| **Grenade Case** | 2×2 (4) | 7×7 (49) | **12:1** | Grenades, throwables | 350K₽ |
| **Keytool** | 1×1 (1) | 4×4 (16) | **16:1** | Keys, keycards | 250K₽ |
| **Docs Case** | 1×2 (2) | 4×4 (16) | **8:1** | Keys, money, maps | 350K₽ |
| **THICC Items Case** | 3×3 (9) | 14×14 (196) | **21.8:1** | Ultimate storage | 18M₽ |
| **THICC vũ khí Case** | 5×5 (25) | 15×8 (120) | **4.8:1** | Massive vũ khí storage | 11M₽ |

**Strategic Investment Priority:**
1. **Early Game**: Scav Junkbox (immediate giá trị)
2. **Mid Game**: đạn Case, Med Case, vũ khí Case
3. **Late Game**: Items Case, THICC Cases
4. **Always Useful**: Keytool, Docs Case (bring in-raid)

### 8.3 Stash Organization Strategies

**"Zone" hệ thống:**
- **Top Zone** (Rows 1-10): Active gear (ready-to-raid)
  - vũ khí, giáp, rigs for next raid
  - Frequently used items
  
- **Middle Zone** (Rows 11-40): Storage containers
  - Organize by container type
  - Group related items (all đạn cases together)
  
- **Bottom Zone** (Rows 41+): Long-term storage
  - Quest items for future tasks
  - Safe House upgrade materials
  - Rarely used items

**Auto-Sort Controversy:**
- **Pro**: Instant organization, saves thời gian
- **Con**: Destroys custom layouts, breaks muscle memory
- **Community Consensus**: Avoid using sau establishing layout
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

### 8.4 Economic quyết định-Making

**Sell vs. Keep matrix:**

| Item Type | Sell nếu... | Keep nếu... |
|:----------|:-----------|:-----------|
| vũ khí | Not using within 3 raids | Meta build hoặc needed for quest |
| giáp | Durability <40% | Class 5+ và >60% |
| Barter Items | Not needed for Safe House | Required for upgrade hoặc craft |
| đạn | Have 500+ rounds | Good AP đạn, <300 rounds |
| Meds | Have 20+ of type | Rare hoặc valuable (Surv12) |
| Keys | Looted room 5+ times | Rare spawns hoặc quest |

**giá trị Timing Strategy:**
- Some items spike in giá trị trong khi events
- Quest items more valuable khi quest is active
- Safe House materials surge khi new upgrades unlock
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

**Validation checklist (Every Move):**
- [ ] Item fits in target grid
- [ ] No overlap với existing items
- [ ] Weight limit not exceeded
- [ ] Nesting rules satisfied
- [ ] Item exists và owned by người chơi
- [ ] Target container has capacity
- [ ] Action timestamp reasonable (no thời gian manipulation)

### 9.3 Client-Side Implementation

**Drag & Drop Library Recommendations:**
- **Unreal Engine**: Enhanced Input + Slate DragDrop hệ thống
- **Unity**: Custom IBeginDragHandler, IDragHandler, IEndDragHandler
- **Web (nếu applicable)**: React DnD, Interact.js

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
- cách dùng object pooling for UI elements (inventory slots)
- Lazy load container contents (only khi opened)

### 9.4 UI/UX Design Specifications

**Visual Feedback yêu cầu:**
- **Drag trạng thái**: Item follows cursor với 50% opacity
- **Valid Placement**: Green outline on grid cells
- **Invalid Placement**: Red outline, shake animation
- **Snap-to-Grid**: Magnetic snapping for satisfying feel
- **Sound Effects**:
  - Pickup: Light "clink" hoặc "rustle"
  - Place: Heavier "thud" based on item weight
  - Invalid: "Error buzz" sound
  - Stack merge: Satisfying "cash register" ding

**Color Coding hệ thống:**
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
│ • Safe House Upgrade: Lvl 2 │
└─────────────────────────────┘
```

---

## 10. Playtesting & Iteration Plan

### 10.1 Metrics to Track

**Quantitative Data:**
- Average thời gian spent in inventory (in-raid vs stash)
- Inventory open frequency per raid
- Items discarded per raid (indicates space pressure)
- Weight tier distribution (% raids at each tier)
- Container usage statistics (which bought most)
- Item rotation usage (how often người chơi cách dùng R chính)
- failed item placements (UX friction point)

**Qualitative Feedback:**
- người chơi surveys on "inventory satisfaction"
- Interviews about "frustration points"
- Observations of first-thời gian người chơi behavior
- Community feedback on forums/Discord

### 10.2 Balance Tuning Targets

**Ideal Benchmarks:**
- 70% of Người chơi nên run Medium weight tier
- 15% Light (speed runners), 10% Heavy (tanks), 5% Critical (loot hoarders)
- Inventory thời gian nên được <30% of raid duration
- 80% of Người chơi nên cách dùng at least 1 storage container
- Auto-sort usage <20% (indicates good layout design)

### 10.3 Known Issues & Future Improvements

**hiện tại Limitations:**
- Auto-sort algorithm not smart enough (v1.0)
- Lack of "loadout presets" for full kits
- No search/filter in stash (huge QoL missing)
- Container nesting rules confusing for new người chơi
- Weight penalties feel too harsh >60kg (common feedback)

**Roadmap Items:**
- **v1.1**: Search bar for stash, Loadout preset hệ thống
- **v1.2**: Smart auto-sort (remembers người chơi preferences)
- **v1.3**: Mobile app for stash management (out-of-game)
- **v2.0**: Dynamic container sizes, New container types
- **v2.5**: AI-assisted inventory optimization suggestions

---

## 11. Competitive Analysis - chính Takeaways

### 11.1 What We're Copying (Proven Successful)

**From Escape from Tarkov:**
- Tetris grid hệ thống (industry standard now)
- Weight-based movement penalties (hardcore feel)
- Zone-based giáp (realistic ballistics)
- Found in Raid (FiR) hệ thống (anti-RMT measure)

**From Arena Breakout: Infinite:**
- Cleaner UI/UX (less overwhelming for new người chơi)
- Better onboarding tooltips
- Faster looting animations (QoL)

**From Delta Force:**
- Operator ability hệ thống integration
- Vehicle storage cơ chế
- Multiple extraction methods

**From Hunt: Showdown:**
- Trait hệ thống affecting inventory (future tính năng)
- Perma-death consequences for gear
- Prestige hệ thống integration

### 11.2 What We're Improving (Innovation Points)

**Our Unique tính năng:**
1. **Hybrid Weight hệ thống**: Combines realistic physics với arcadey accessibility
   - Hardcore mode: Full realism
   - Standard mode: -25% weight penalties
   
2. **AI-Assisted Sorting**: Machine learning predicts người chơi preferences
   - Learns from manual organization patterns
   - Suggests optimal layouts
   
3. **Cross-Raid Loadout Persistence**: Save full loadouts với one click
   - "Loadout slots" hệ thống (5 presets)
   - Quick-swap entire kit trước raid
   
4. **Dynamic Container Expansion**: Containers level up với cách dùng
   - "Well-used Medcase" gains +2 slots sau 100 uses
   - Encourages long-term item relationships

5. **Social tính năng**: 
   - Stash sharing với squad (view-only)
   - Gift items to friends (trade hệ thống)
   - shared squad stash (clan tính năng)

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
- Default trải nghiệm

**Hardcore Mode:**
- +25% weight penalties
- No auto-sort function
- No examine shortcuts (must kiểm tra manually)
- Realistic search times (no skill speed-up)
- Limited UI information

### 12.2 Accessibility tính năng

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
- Adjustable tutorial hệ thống (skip/repeat)
- Complexity levels (hide advanced stats initially)
- Reference wiki integration (in-game tooltips)
- Practice mode (zero-stakes inventory management)

---

## 13. Monetization Considerations

### 13.1 Ethical F2P Integration (nếu Applicable)

**Acceptable Paid tính năng:**
- cosmetic stash themes (visual reskins)
- Additional loadout preset slots (convenience)
- Stash expansion (nhưng achievable in-game too)
- Special containers với unique looks (same capacity as in-game)

**NEVER Sell:**
- pay-to-win items (better stats)
- Exclusive storage sizes (P2W advantage)
- Faster looting animations (competitive advantage)
- Anything affecting gameplay balance

### 13.2 Premium Edition Differences

**Standard vs. Premium:**
- Stash Size: 10×28 vs 10×48 (hoặc both upgradeable to 10×68)
- Secure Container: 2×2 vs 3×3 (significant nhưng not gamebreaking)
- Starting Containers: 0 vs 1 of each basic type
- Cosmetics: Basic vs Unique vũ khí skins, stash themes

**Progression Balance:**
- Standard Người chơi nên reach parity within 200 hours
- Premium gives head-start, not permanent advantage
- All content accessible to all người chơi eventually

---

## 14. Localization & Cultural Considerations

### 14.1 Text Localization Challenges

**Item Name Translation:**
- Military jargon varies by region (AK-74 vs Type 74)
- Slang terms need cultural equivalents
- Measurement units (kg vs lbs, toggleable)

**UI Text Expansion:**
- Some languages take 40% more space (German)
- Grid labels phải được abbreviation-friendly
- Icon-heavy design reduces text dependency

### 14.2 Cultural Sensitivity

**giáp & Gear Branding:**
- Avoid real military unit insignias (legal issues)
- Generic faction names instead of real countries
- Respect cultural symbols (no offensive emblems)

**Looting cơ chế:**
- Some cultures sensitive to corpse looting
- Option to "transfer gear" instead of "loot body" (language)

---

## 15. Conclusion & Vision

This Inventory & Gear hệ thống được thiết kế để be a **cốt lõi gameplay pillar**, not an afterthought. Người chơi nên feel:
- **Satisfaction** from spatial puzzle-solving
- **Tension** from weight management under pressure
- **Progression** from stash organization và optimization
- **Mastery** from efficient looting techniques

By studying the best-in-class extraction shooters và innovating beyond them, we aim to tạo an inventory hệ thống that is:
- **Deep enough** to engage hardcore người chơi
- **Accessible enough** to welcome newcomers
- **Fair** in monetization và balance
- **Respectful** of người chơi thời gian và effort

**Next Steps:**
1. Prototype cốt lõi grid hệ thống (2 weeks)
2. Implement weight hệ thống với visual feedback (3 weeks)
3. Build container nesting logic (2 weeks)
4. tạo gunsmith interface (4 weeks)
5. Playtest với 50 người chơi, iterate based on feedback (ongoing)

---

## Appendix A: Glossary of Terms

- **ADS**: Aim Down Sights
- **AP**: giáp Piercing (ammunition type)
- **Chad**: Slang for heavily geared người chơi
- **EOD**: Edge of Darkness (premium edition)
- **Ergo**: Ergonomics stat
- **Extract**: Leave the raid successfully
- **FiR**: Found in Raid status
- **Keytool**: Small chính storage container
- **Meta**: Most Effective Tactics available
- **PMC**: người chơi nhân vật (main account)
- **Rat**: Slang for low-gear, sneaky người chơi
- **Rig**: Tactical vest / chest rig
- **Scav**: AI địch hoặc người chơi scavenger mode
- **Stash**: Persistent out-of-raid storage
- **Tetris**: Spatial inventory management gameplay

---

## Appendix B: Reference Materials

**Competitor Analysis Documents:**
- Escape from Tarkov Wiki: https://escapefromtarkov.fandom.com
- Arena Breakout Guide: (internal tài liệu)
- Delta Force Documentation: https://www.playdeltaforce.com

**Design Resources:**
- Realistic Firearm Specifications: https://modernfirearms.net
- giáp Ballistics Data: https://www.nij.gov/topics/equipment
- Military Gear Reference: https://soldiersystems.net

**Development Tools:**
- Grid hệ thống Tutorial: (link to internal docs)
- Unreal Engine Drag-Drop API: (documentation)
- Server Validation Best Practices: (security tài liệu)

---

**tài liệu Author**: Claude AI (Game Design Consultant)  
**Reviewed By**: [pending Team Review]  
**Approval Status**: Draft - Awaiting Stakeholder Sign-Off  
**Version History**:
- v1.0 (2024-01-15): Initial draft
- v2.0 (2026-02-11): Enhanced edition với competitive analysis và modern GDD practices
