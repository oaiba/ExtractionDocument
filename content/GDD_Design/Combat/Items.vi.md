---
title: "Items & Economy hệ thống"
type: docs
---

### Economy Philosophy

**cốt lõi Principles:**

1. **người chơi-Driven** - Market prices determined by supply/demand
2. **Risk tạo giá trị** - Rare items from dangerous zones worth more
3. **No pay-to-win** - Real money cannot mua gameplay advantages
4. **Fair Trading** - hệ thống prevent scams và exploitation
5. **Economic Sinks** - Prevent inflation thông qua item loss và fees

***

### Combat Item Source-Of-Truth Boundary

Trang này mô tả combat-facing item usage và economic intent. Nó không định nghĩa lại item instance ownership, stash placement, entitlement, FIR, contraband, durability lifecycle, hoặc overflow rules; các phần đó thuộc [Inventory System](../inventory_system/_index/index.html), [Gear Tier System](../gears/gear_tier_system/index.html), và [Economy](../gamedesign/economy/index.html).

| Item Family | Combat Contract | Source-Of-Truth Link |
| :--- | :--- | :--- |
| Weapons / ammo | Damage, handling, role, feedback, ammo/armor interaction | [Weapons](../weapons/_index/index.html) |
| Armor | Protection, movement cost, durability, readable failure | [Armor Gear](../gears/armorgear/armor/index.html) |
| Medical | Recovery timing, vulnerability, status clarity | [Medical System](../gameplay/medical_system/index.html) |
| Tactical equipment | Sound, vision, denial, extraction counterplay | [Combat Feel](../gameplay/combat_feel_topdown/index.html) |
| Loot / barter | Chỉ value và risk context | [Inventory System](../inventory_system/_index/index.html) |

Combat items phải giữ no-paid-power rule: premium purchase có thể grant cosmetic entitlement, nhưng không grant superior combat item instances.

***

### Item Categories

#### 1. vũ khí & Attachments

_See:_ [_Weapons & Combat_](vũ khí.md) _for chi tiết on vũ khí, Attachments, và Ammunition types_

**Economic Role:**

* primary giá trị holders
* High-risk items (lost on death)
* tạo demand for constant replacement

***

#### 2. giáp & Protection

giáp uses **Class 1–6** (GOST-style) với zone-based protection. Display values và headshot reduction map from class; Xem [Gears — giáp & Ballistics](../gears/armorgear/armor/index.html) for mapping và [Gears — giáp Master Database](../gears/armorgear/armor_master_database/index.html) for full spec, materials, và zone coverage per item.

| Type           | Class (example) | Coverage (example)     | Move penalty | giá trị range      |
| -------------- | :-------------: | ---------------------- | ------------ | ---------------- |
| Light          |        2        | Chest only             | 0%           | \~$800–1,000     |
| Medium         |        3        | Chest + Back           | −5%          | \~$2,500–3,000   |
| Heavy          |        4        | Full torso             | −10%         | \~$6,000–8,000   |
| Tactical/Elite |       5–6       | Full torso + arms/neck | −15%         | \~$10,000–15,000 |

***

#### 3. Backpacks & Storage

Backpacks và tactical rigs define carry capacity và hotkey access. Full list và grid layouts: [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) và [Storage Master Database](../gears/storagegear/storage_master_database/index.html).

| Tier   | Slots (example) | Move penalty | giá trị range     |
| ------ | :-------------: | ------------ | --------------- |
| Small  |     6 (2×3)     | 0%           | \~$500          |
| Medium | 12–16 (3×4–4×4) | 0–−2%        | \~$1,500–10,000 |
| Large  | 20–30 (4×5–5×6) | −5% to −8%   | \~$4,000–40,000 |

***

#### 4. Medical Supplies

**Bandage (Common)**

* Effect: +15 HP over 3 sec, stops bleeding
* Stack Size: 5
* Weight: 0.1 kg each
* giá trị: $50

**Medkit (Uncommon)**

* Effect: +50 HP over 5 sec
* Stack Size: 3
* Weight: 0.3 kg each
* giá trị: $200

**Combat Stim (Rare)**

* Effect: +30 HP instant, +10% speed for 10 sec
* Stack Size: 2
* Weight: 0.2 kg each
* giá trị: $800

**Surgery Kit (Epic)**

* Effect: Full heal (100 HP), 8 sec cách dùng
* Stack Size: 1
* Weight: 0.5 kg
* giá trị: $2,500

**Painkillers (Uncommon)**

* Effect: Reduces damage taken by 15% for 60 sec
* Stack Size: 3
* Weight: 0.1 kg each
* giá trị: $300

***

#### 5. Consumables & Utilities

**Energy Drink (Common)**

* Effect: +20% sprint speed for 30 sec
* Stack Size: 3
* giá trị: $100

**Adrenaline Shot (Rare)**

* Effect: +30% all stats for 15 sec
* Stack Size: 1
* giá trị: $1,000

**Ration Pack (Common)**

* Effect: Restores stamina instantly
* Stack Size: 5
* giá trị: $50

***

#### 6. Tactical Equipment

**Sensor Mine (Uncommon)**

* Effect: Detects địch in 15m radius
* Duration: 60 seconds
* Stack Size: 2
* giá trị: $400

**Claymore (Rare)**

* Effect: 80 damage in cone
* Trigger: Laser tripwire
* Stack Size: 1
* giá trị: $1,200

**Portable Cover (Epic)**

* Effect: Deploy temporary hard cover
* Duration: Permanent until destroyed
* Stack Size: 1
* giá trị: $3,000

***

#### 7. Keys & Special Items

**Loot Room chính (Rare)**

* cách dùng: Unlocks high-tier loot rooms
* Single-cách dùng
* giá trị: $5,000-10,000

**Safe chính (Epic)**

* cách dùng: Opens safes với guaranteed rare loot
* Single-cách dùng
* giá trị: $8,000-15,000

**Supply Drop Beacon (Legendary)**

* cách dùng: Calls personal supply drop
* Single-cách dùng
* Contents: Random Epic/Legendary items
* giá trị: $25,000

***

#### 8. Crafting Materials

**Scrap Metal (Common)**

* cách dùng: Basic vũ khí repairs
* Stack Size: 50
* giá trị: $10 each

**Electronics (Uncommon)**

* cách dùng: Attachment crafting
* Stack Size: 20
* giá trị: $50 each

**Rare Components (Rare)**

* cách dùng: High-tier crafting
* Stack Size: 10
* giá trị: $200 each

**Legendary Parts (Legendary)**

* cách dùng: Legendary vũ khí crafting
* Stack Size: 5
* giá trị: $1,000 each

***

#### 9. Quest Items

**Faction Documents**

* Faction-cụ thể quest items
* No stack limit
* giá trị: Cannot be sold (quest cách dùng only)

**Intel Packages**

* Deliver to faction for reputation
* Single item
* giá trị: Reputation reward

**Artifact Pieces**

* Collect full set for legendary reward
* Part of larger quest chain
* giá trị: $500 each (partial giá trị)

***

### Items Reference Tables

#### giáp & Protection - Complete Specifications

Full spec (per-item class, zones, material, durability, giá trị): [**Gears — giáp Master Database**](../gears/armorgear/armor_master_database/index.html). Hit locations và damage model: [vũ khí Arsenal](../Gameplay/WeaponArsenal.md#hit-location-multipliers).

#### Backpacks & Storage

Full spec (rigs, backpacks, secure containers, stash cases): [**Gears — Storage Master Database**](../gears/storagegear/storage_master_database/index.html).

***

#### Medical Supplies - Complete Specifications

| Code Name             | Display Name  | Rarity   | Heal Amount     | Heal thời gian | Stack Size | Weight (kg) | Grid Size | giá trị ($) | Special Effect      |
| --------------------- | ------------- | -------- | --------------- | --------- | ---------- | ----------- | --------- | --------- | ------------------- |
| ITEM\_MED\_BANDAGE    | Bandage       | Common   | +15 HP over 3s  | 3 sec     | 5          | 0.1         | 1x1       | 50        | Stops bleeding      |
| ITEM\_MED\_MEDKIT     | Medkit        | Uncommon | +50 HP over 5s  | 5 sec     | 3          | 0.3         | 1x2       | 200       | -                   |
| ITEM\_MED\_STIM       | Combat Stim   | Rare     | +30 HP instant  | 1 sec     | 2          | 0.2         | 1x1       | 800       | +10% speed 10s      |
| ITEM\_MED\_SURGERY    | Surgery Kit   | Epic     | +100 HP over 8s | 8 sec     | 1          | 0.5         | 2x2       | 2,500     | Removes all debuffs |
| ITEM\_MED\_PAINKILLER | Painkillers   | Uncommon | -               | 2 sec     | 3          | 0.1         | 1x1       | 300       | -15% dmg taken 60s  |
| ITEM\_MED\_BLOODBAG   | Blood Bag     | Rare     | +40 HP over 10s | 10 sec    | 1          | 0.4         | 1x2       | 1,200     | +20% max HP 2min    |
| ITEM\_MED\_FIRSTAID   | First Aid Kit | Common   | +25 HP over 4s  | 4 sec     | 4          | 0.2         | 1x2       | 120       | Basic healing       |

***

#### Consumables & Utilities

| Code Name              | Display Name    | Rarity   | Effect            | Duration | Stack Size | Weight (kg) | Grid Size | giá trị ($) |
| ---------------------- | --------------- | -------- | ----------------- | -------- | ---------- | ----------- | --------- | --------- |
| ITEM\_CONS\_ENERGY     | Energy Drink    | Common   | +20% sprint speed | 30 sec   | 3          | 0.2         | 1x1       | 100       |
| ITEM\_CONS\_ADRENALINE | Adrenaline Shot | Rare     | +30% all stats    | 15 sec   | 1          | 0.1         | 1x1       | 1,000     |
| ITEM\_CONS\_RATION     | Ration Pack     | Common   | Restore stamina   | Instant  | 5          | 0.3         | 1x1       | 50        |
| ITEM\_CONS\_WATER      | Water Bottle    | Common   | Restore hydration | Instant  | 4          | 0.5         | 1x1       | 30        |
| ITEM\_CONS\_PROTEIN    | Protein Bar     | Uncommon | +15% max stamina  | 60 sec   | 3          | 0.1         | 1x1       | 150       |

***

#### Tactical Equipment

| Code Name            | Display Name      | Rarity   | Effect                    | Duration          | Deploy thời gian | Stack Size | Weight (kg) | Grid Size | giá trị ($) |
| -------------------- | ----------------- | -------- | ------------------------- | ----------------- | ----------- | ---------- | ----------- | --------- | --------- |
| ITEM\_TAC\_SENSOR    | Sensor Mine       | Uncommon | Detect địch 15m        | 60 sec            | 2 sec       | 2          | 0.4         | 1x2       | 400       |
| ITEM\_TAC\_CLAYMORE  | Claymore          | Rare     | 80 dmg cone               | Until triggered   | 3 sec       | 1          | 1.0         | 2x2       | 1,200     |
| ITEM\_TAC\_COVER     | Portable Cover    | Epic     | Deploy hard cover         | Permanent         | 5 sec       | 1          | 3.0         | 2x3       | 3,000     |
| ITEM\_TAC\_BARRICADE | Barricade Kit     | Uncommon | Block doorway             | Permanent         | 4 sec       | 1          | 2.5         | 2x2       | 800       |
| ITEM\_TAC\_C4        | C4 Explosive      | Epic     | 150 dmg 10m radius        | Remote detonation | 3 sec       | 1          | 0.8         | 1x2       | 2,500     |
| ITEM\_TAC\_BEACON    | Extraction Beacon | Rare     | Call emergency extraction | Single-cách dùng        | 2 sec       | 1          | 0.3         | 1x1       | 5,000     |

***

#### Keys & Special Items

| Code Name           | Display Name       | Rarity    | cách dùng                         | Durability | Weight (kg) | Grid Size | giá trị ($)    | Drop Rate |
| ------------------- | ------------------ | --------- | --------------------------- | ---------- | ----------- | --------- | ------------ | --------- |
| ITEM\_KEY\_LOOTROOM | Loot Room chính      | Rare      | Unlock high-tier loot rooms | 1 cách dùng      | 0.1         | 1x1       | 5,000-10,000 | 5%        |
| ITEM\_KEY\_SAFE     | Safe chính           | Epic      | Open safes                  | 1 cách dùng      | 0.1         | 1x1       | 8,000-15,000 | 2%        |
| ITEM\_KEY\_SUPPLY   | Supply Drop Beacon | Legendary | Call personal supply drop   | 1 cách dùng      | 0.2         | 1x1       | 25,000       | 0.5%      |
| ITEM\_KEY\_BUNKER   | Bunker chính         | Epic      | Access bunker vault         | 3 uses     | 0.1         | 1x1       | 12,000       | 1%        |
| ITEM\_KEY\_OFFICE   | Office chính         | Uncommon  | Office rooms                | 5 uses     | 0.05        | 1x1       | 2,000        | 10%       |
| ITEM\_KEY\_MASTER   | Master Keycard     | Legendary | Universal access            | 1 cách dùng      | 0.1         | 1x1       | 50,000       | 0.1%      |

***

#### Crafting Materials

| Code Name                | Display Name    | Rarity    | cách dùng                 | Stack Size | Weight (kg) | Grid Size | giá trị ($) | Where to Find      |
| ------------------------ | --------------- | --------- | ------------------- | ---------- | ----------- | --------- | --------- | ------------------ |
| ITEM\_CRAFT\_SCRAP       | Scrap Metal     | Common    | Basic repairs       | 50         | 0.05        | 1x1       | 10        | Everywhere         |
| ITEM\_CRAFT\_ELECTRONICS | Electronics     | Uncommon  | Attachment crafting | 20         | 0.1         | 1x1       | 50        | Mid zones          |
| ITEM\_CRAFT\_RARECOMP    | Rare Components | Rare      | High-tier crafting  | 10         | 0.2         | 1x1       | 200       | Hot zones          |
| ITEM\_CRAFT\_LEGENDARY   | Legendary Parts | Legendary | Legendary crafting  | 5          | 0.3         | 1x1       | 1,000     | Safes, bosses      |
| ITEM\_CRAFT\_CIRCUITS    | Circuit Boards  | Uncommon  | Tech item crafting  | 25         | 0.08        | 1x1       | 80        | Electronics stores |
| ITEM\_CRAFT\_POLYMER     | Polymer         | Common    | giáp repairs       | 40         | 0.06        | 1x1       | 20        | Industrial zones   |
| ITEM\_CRAFT\_TOOLS       | Tool Kit        | Rare      | upgrade items       | 1          | 1.0         | 2x2       | 500       | Supply drops       |

***

#### Throwables & Grenades

| Code Name              | Display Name       | Rarity   | Damage                       | Radius (m) | Fuse thời gian | Stack Size | Weight (kg) | Grid Size | giá trị ($) | Special           |
| ---------------------- | ------------------ | -------- | ---------------------------- | ---------- | --------- | ---------- | ----------- | --------- | --------- | ----------------- |
| ITEM\_GREN\_FRAG       | Frag Grenade       | Common   | 100 (direct) 50-10 (falloff) | 8          | 3 sec     | 3          | 0.4         | 1x1       | 200       | Cookable          |
| ITEM\_GREN\_FLASH      | Flashbang          | Common   | 0 dmg                        | 10         | 1.5 sec   | 3          | 0.3         | 1x1       | 150       | 5s blind          |
| ITEM\_GREN\_SMOKE      | Smoke Grenade      | Common   | 0 dmg                        | 8          | 2 sec     | 3          | 0.3         | 1x1       | 100       | 15s duration      |
| ITEM\_GREN\_EMP        | EMP Grenade        | Rare     | 0 dmg                        | 15         | 2 sec     | 2          | 0.3         | 1x1       | 800       | Disable abilities |
| ITEM\_GREN\_INCENDIARY | Incendiary Grenade | Rare     | 40/sec DOT                   | 6          | 2 sec     | 2          | 0.4         | 1x1       | 600       | 8s burn           |
| ITEM\_GREN\_STUN       | Stun Grenade       | Uncommon | 0 dmg                        | 8          | 1.5 sec   | 3          | 0.3         | 1x1       | 250       | 3s stun           |

***

#### Quest & Special Items

| Code Name                 | Display Name           | Category | Weight (kg) | Grid Size | Sell giá trị  | ghi chú             |
| ------------------------- | ---------------------- | -------- | ----------- | --------- | ----------- | ----------------- |
| ITEM\_QUEST\_DOC\_SALVAGE | Salvage Corps tài liệu | Quest    | 0.1         | 1x1       | Cannot sell | Faction quest     |
| ITEM\_QUEST\_DOC\_TECH    | Tech Syndicate Data    | Quest    | 0.1         | 1x1       | Cannot sell | Faction quest     |
| ITEM\_QUEST\_INTEL        | Intel Package          | Quest    | 0.2         | 1x1       | Cannot sell | Reputation reward |
| ITEM\_QUEST\_ARTIFACT1    | Artifact Piece Alpha   | Quest    | 0.3         | 1x1       | 500         | Part 1 of 5       |
| ITEM\_QUEST\_ARTIFACT2    | Artifact Piece Beta    | Quest    | 0.3         | 1x1       | 500         | Part 2 of 5       |
| ITEM\_QUEST\_SAMPLE       | Biological Sample      | Quest    | 0.5         | 1x2       | Cannot sell | thời gian-sensitive    |
| ITEM\_QUEST\_HARDDRIVE    | Encrypted Hard Drive   | Quest    | 0.4         | 1x1       | Cannot sell | Rare quest item   |

***

### Loot hệ thống

#### Loot Spawn cơ chế

**Container Types:**

**Wooden Crate (Common)**

* Spawn Rate: Very High (every 20-30m)
* Loot Quality: Common (80%), Uncommon (20%)
* Average giá trị: $500-1,500
* Typical Contents: Bandages, đạn, basic attachments

**Metal Locker (Uncommon)**

* Spawn Rate: Medium (every 50-80m)
* Loot Quality: Uncommon (60%), Rare (30%), Common (10%)
* Average giá trị: $2,000-5,000
* Typical Contents: giáp, medkits, uncommon vũ khí

**vũ khí Rack (Uncommon)**

* Spawn Rate: Low (3-5 per map)
* Loot Quality: vũ khí only
* Guaranteed vũ khí spawn (Common to Rare)
* Average giá trị: $1,500-6,000

**Safe (Rare)**

* Spawn Rate: Very Low (1-2 per hot zone)
* Requires: chính hoặc lockpick (thời gian)
* Loot Quality: Rare (50%), Epic (40%), Legendary (10%)
* Average giá trị: $8,000-20,000
* Typical Contents: High-tier vũ khí, giáp, cash

**Supply Drop (Event)**

* Spawn: Timed events (5:00, 10:00)
* Location: Random hot zone
* Loot Quality: Epic (70%), Legendary (30%)
* Average giá trị: $15,000-30,000
* Risk: Contested, attracts all người chơi

***

#### Loot Distribution by Zone

**Safe Zones (Map Edges)**

* Container Density: High
* Quality: 70% Common, 25% Uncommon, 5% Rare
* Risk: Low (AI only)
* Reward: Stable nhưng modest

**Mid Zones**

* Container Density: Medium
* Quality: 40% Common, 40% Uncommon, 18% Rare, 2% Epic
* Risk: Medium (AI + người chơi)
* Reward: Balanced risk/reward

**Hot Zones (Center)**

* Container Density: Low pero High Quality
* Quality: 20% Uncommon, 50% Rare, 25% Epic, 5% Legendary
* Risk: Very High (PvP combat)
* Reward: Highest giá trị

**Contamination Zone (Late Game)**

* Container Density: Medium
* Quality: 30% Rare, 50% Epic, 20% Legendary
* Risk: Extreme (contamination damage + combat)
* Reward: Best loot trước match end

***

#### Dynamic Loot Scaling

**người chơi Count Adjustment:**

* More người chơi alive = More loot spawns
* Prevents loot drought
* Encourages exploration

**thời gian-Based:**

* Early game (0-5 min): Basic loot common
* Mid game (5-10 min): Quality increases
* Late game (10-15 min): Best loot in dangerous zones

**Death-Based:**

* Each người chơi death: Small loot quality increase globally
* Compensates surviving người chơi
* Rewards skilled survival

***

### Inventory Management

#### Grid-Based hệ thống

**Inventory Layout:**

```
┌─────────────────────┐
│ Secure Container    │  Always Safe (2x2)
│ ┌──┬──┐             │
│ │░░│░░│             │
│ ├──┼──┤             │
│ │░░│░░│             │
│ └──┴──┘             │
├─────────────────────┤
│ Backpack Space      │  Lost on Death
│ ┌──┬──┬──┬──┬──┐   │
│ │  │  │  │  │  │   │
│ ├──┼──┼──┼──┼──┤   │
│ │  │  │  │  │  │   │
│ ├──┼──┼──┼──┼──┤   │
│ │  │  │  │  │  │   │
│ └──┴──┴──┴──┴──┘   │
└─────────────────────┘
```

**Item Sizes:**

* Small (1x1): đạn, consumables, keys
* Medium (1x2): Pistols, attachments, meds
* Large (2x2): SMGs, giáp pieces
* Very Large (2x3): Assault rifles, helmets
* Huge (2x4): Sniper rifles, LMGs

**Tetris-Style Rotation:**

* Rotate items to fit
* Efficient packing rewarded
* Strategic space management

***

#### Secure Container

**mục đích:** Protect high-giá trị items from death loss

**Standard Container (Free):**

* Size: 2x2 (4 slots)
* Cannot be upgraded in-match

**Expanded Container (Premium/Quest):**

* Size: 2x3 (6 slots)
* Unlock: Level 25 hoặc Premium
* Permanent upgrade

**Container Rules:**

* Can only place items IN trong khi raid
* Cannot take items OUT trong khi raid
* Prevents container abuse
* Preserves risk/reward balance

***

#### Weight & Encumbrance

**Weight hệ thống:**

* Each item has weight (kg)
* Total weight affects movement

**Weight Thresholds:**

| Weight Total | Movement Speed | Stamina Drain | Effects          |
| ------------ | -------------- | ------------- | ---------------- |
| 0-15 kg      | 100%           | Normal        | None             |
| 15-25 kg     | 90%            | +20%          | Slight slowdown  |
| 25-35 kg     | 75%            | +50%          | Heavy encumbered |
| 35+ kg       | 60%            | +100%         | Severely slowed  |

**Strategic quyết định:**

* More loot = slower escape
* Drop items nếu chased
* Balance greed vs survival

***

### người chơi Trading & Marketplace

#### Direct Trading (Post-Launch tính năng)

**Face-to-Face Trading:**

* Người chơi có thể trade in lobby
* Drag và drop items
* Both accept = complete trade
* No fees for direct trades

**Safety tính năng:**

* Trade window shows both offer
* Confirmation required from both
* Cannot scam ifboth see everything
* Trade history logged

***

#### Auction House

**Listing Items:**

* List item for cụ thể giá
* Set buyout giá (optional)
* Listing fee: 5% of starting bid
* Duration: 24, 48, hoặc 72 hours

**Bidding:**

* người chơi bid on items
* Automatic outbid notifications
* Last-minute extensions (anti-snipe)
* Highest bid wins

**Fees:**

* Listing fee: 5% (non-refundable)
* Sale fee: 10% (from final sale giá)
* Total chi phí: 15% to seller
* mục đích: Credit sink (prevent inflation)

***

#### Market Dynamics

**Supply & Demand:**

* Prices fluctuate based on availability
* Rare items chi phí more
* Common items cheap
* Weekend events affect prices

**giá Floors:**

* Minimum vendor giá (prevents crashes)
* Prevents item giá trị from hitting $0
* Maintains economic stability

**Market Manipulation Prevention:**

* Transaction limits
* giá change limits (max 50% jump/day)
* Whale detection (large bulk buys flagged)

***

#### Popular Trade Items

**High-Demand Items:**

1. Epic/Legendary vũ khí
2. Rare keys
3. giáp (always needed)
4. Medical supplies (consumable)
5. Crafting materials (bulk trading)

**Profitable Flipping:**

* mua low trong khi high supply
* Sell high trong khi scarcity
* Weekend events tạo opportunities
* Requires market knowledge

***

### Crafting hệ thống (Future tính năng)

#### Crafting Basics

**Workbench (Stash):**

* Combine materials to tạo items
* Unlock recipes thông qua progression
* thời gian-based (instant hoặc wait)

**Example Recipes:**

**Medkit (Uncommon)**

* Materials: 5x Bandages + 2x Medical Supplies
* Craft thời gian: Instant
* Output: 1x Medkit
* chi phí Savings: 20% vs buying

**Rare vũ khí (Customization)**

* Materials: Base vũ khí + 3x Rare Components + Attachments
* Craft thời gian: Instant
* Output: vũ khí với pre-installed attachments
* Benefit: Saves attachment installation thời gian

**giáp Repair:**

* Materials: Damaged giáp + Scrap Metal
* Output: Repaired giáp (80% durability)
* Cheaper than buying new

***

### Economic Sinks & Sources

#### Credit Sources (Inflow)

**primary:**

* Extract loot và sell: $2,000-20,000 per match
* Quest rewards: $1,000-10,000 per quest
* Daily login: $500/day
* Level-up: $500-2,000 per level

**secondary:**

* Achievements: One-thời gian bonuses
* Events: Limited-thời gian earnings
* Referrals: $5,000 per friend (max 10)

***

#### Credit Sinks (Outflow)

**primary:**

* vũ khí purchases: $500-20,000
* giáp purchases: $800-15,000
* Medical supplies: $50-2,500
* Stash expansion: $10,000 per upgrade

**secondary:**

* Marketplace fees: 15% of transactions
* Name changes: $1,000
* cosmetic purchases: $500-5,000
* Insurance (future): Based on gear giá trị

***

#### Anti-Inflation Measures

**Item Loss on Death:**

* Largest credit sink
* Removes items from economy
* tạo constant demand
* Prevents supply saturation

**Transaction Fees:**

* 15% marketplace tax
* Prevents rapid flipping
* Stabilizes prices
* Removes credits from economy

**Durability hệ thống (Future):**

* vũ khí degrade với cách dùng
* Require repair hoặc replacement
* Ongoing credit expenditure
* Balances high-tier vũ khí accessibility

***

### Item Insurance (Future tính năng)

#### How It Works

**Pre-Match Insurance:**

* Pay fee (20-30% of item giá trị)
* nếu you die, item returned (80% chance)
* 24-hour wait for return
* Does NOT work nếu extracted by địch

**Benefits:**

* Reduce risk of expensive loadouts
* Encourage using good gear
* Still lose nếu looted by người chơi

**Limitations:**

* Only insured items returned
* Secure container items don't need insurance
* Max 3 insured items per match

***

### Black Market (Future PvE tính năng)

**Concept:** High-risk AI trader in dangerous zones

**How It Works:**

* NPC trader spawns in contaminated areas
* Sells Epic/Legendary items
* Accepts cash only (in-raid currency)
* Risk: PvP + contamination while shopping

**Special offer:**

* Rotating inventory
* Discounted rare items
* Exclusive black market vũ khí
* Intel items

***

### Season al Economy Events

**Double Loot Weekend:**

* All containers have 2x loot
* Prices drop due to supply increase
* Good thời gian to mua và stockpile

**Rare Item Event:**

* Increased spawn rate of cụ thể item type
* Example: "Sniper Week" - more snipers spawn
* Strategic selling window

**Trader Special:**

* NPC vendors discount cụ thể categories
* 20-30% off selected items
* Limited-thời gian offer

***

### Economic Balance Goals

**Healthy Economy Indicators:**

* Average người chơi wealth: $50,000-150,000
* Inflation rate: <5% per month
* Market activity: 60%+ of người chơi trade monthly
* giá stability: <20% fluctuation week-to-week

**Problem Indicators:**

* Hyperinflation (prices double monthly)
* Dead market (no trades happening)
* Wealth concentration (top 1% has 50%+ wealth)
* Item scarcity (cụ thể items unobtainable)

**Developer Interventions:**

* Adjust loot spawn rates
* Modify marketplace fees
* Special events to inject/remove credits
* Emergency balance patches
