---
title: Items & Economy Systems
type: docs
---

# Items & Economy Systems

### Economy Philosophy

**Core Principles:**

1. **Player-Driven** - Market prices determined by supply/demand
2. **Risk Creates Value** - Rare items from dangerous zones worth more
3. **No Pay-to-Win** - Real money cannot buy gameplay advantages
4. **Fair Trading** - Systems prevent scams and exploitation
5. **Economic Sinks** - Prevent inflation through item loss and fees

***

### Item Categories

#### 1. Weapons & Attachments

_See:_ [_Weapons & Combat_](Weapons.md) _for details on Weapons, Attachments, and Ammunition types_

**Economic Role:**

* Primary value holders
* High-risk items (lost on death)
* Create demand for constant replacement

***

#### 2. Armor & Protection

Armor uses **Class 1–6** (GOST-style) with zone-based protection. Display values and headshot reduction map from class; see [Gears — Armor & Ballistics](../Gears/ArmorGear/Armor.md) for mapping and [Gears — Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md) for full spec, materials, and zone coverage per item.

| Type           | Class (example) | Coverage (example)     | Move penalty | Value range      |
| -------------- | :-------------: | ---------------------- | ------------ | ---------------- |
| Light          |        2        | Chest only             | 0%           | \~$800–1,000     |
| Medium         |        3        | Chest + Back           | −5%          | \~$2,500–3,000   |
| Heavy          |        4        | Full torso             | −10%         | \~$6,000–8,000   |
| Tactical/Elite |       5–6       | Full torso + arms/neck | −15%         | \~$10,000–15,000 |

***

#### 3. Backpacks & Storage

Backpacks and tactical rigs define carry capacity and hotkey access. Full list and grid layouts: [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) and [Storage Master Database](../Gears/StorageGear/Storage_Master_Database.md).

| Tier   | Slots (example) | Move penalty | Value range     |
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
* Value: $50

**Medkit (Uncommon)**

* Effect: +50 HP over 5 sec
* Stack Size: 3
* Weight: 0.3 kg each
* Value: $200

**Combat Stim (Rare)**

* Effect: +30 HP instant, +10% speed for 10 sec
* Stack Size: 2
* Weight: 0.2 kg each
* Value: $800

**Surgery Kit (Epic)**

* Effect: Full heal (100 HP), 8 sec use
* Stack Size: 1
* Weight: 0.5 kg
* Value: $2,500

**Painkillers (Uncommon)**

* Effect: Reduces damage taken by 15% for 60 sec
* Stack Size: 3
* Weight: 0.1 kg each
* Value: $300

***

#### 5. Consumables & Utilities

**Energy Drink (Common)**

* Effect: +20% sprint speed for 30 sec
* Stack Size: 3
* Value: $100

**Adrenaline Shot (Rare)**

* Effect: +30% all stats for 15 sec
* Stack Size: 1
* Value: $1,000

**Ration Pack (Common)**

* Effect: Restores stamina instantly
* Stack Size: 5
* Value: $50

***

#### 6. Tactical Equipment

**Sensor Mine (Uncommon)**

* Effect: Detects enemies in 15m radius
* Duration: 60 seconds
* Stack Size: 2
* Value: $400

**Claymore (Rare)**

* Effect: 80 damage in cone
* Trigger: Laser tripwire
* Stack Size: 1
* Value: $1,200

**Portable Cover (Epic)**

* Effect: Deploy temporary hard cover
* Duration: Permanent until destroyed
* Stack Size: 1
* Value: $3,000

***

#### 7. Keys & Special Items

**Loot Room Key (Rare)**

* Use: Unlocks high-tier loot rooms
* Single-use
* Value: $5,000-10,000

**Safe Key (Epic)**

* Use: Opens safes with guaranteed rare loot
* Single-use
* Value: $8,000-15,000

**Supply Drop Beacon (Legendary)**

* Use: Calls personal supply drop
* Single-use
* Contents: Random Epic/Legendary items
* Value: $25,000

***

#### 8. Crafting Materials

**Scrap Metal (Common)**

* Use: Basic weapon repairs
* Stack Size: 50
* Value: $10 each

**Electronics (Uncommon)**

* Use: Attachment crafting
* Stack Size: 20
* Value: $50 each

**Rare Components (Rare)**

* Use: High-tier crafting
* Stack Size: 10
* Value: $200 each

**Legendary Parts (Legendary)**

* Use: Legendary weapon crafting
* Stack Size: 5
* Value: $1,000 each

***

#### 9. Quest Items

**Faction Documents**

* Faction-specific quest items
* No stack limit
* Value: Cannot be sold (quest use only)

**Intel Packages**

* Deliver to faction for reputation
* Single item
* Value: Reputation reward

**Artifact Pieces**

* Collect full set for legendary reward
* Part of larger quest chain
* Value: $500 each (partial value)

***

### Items Reference Tables

#### Armor & Protection - Complete Specifications

Full spec (per-item class, zones, material, durability, value): [**Gears — Armor Master Database**](../Gears/ArmorGear/Armor_Master_Database.md). Hit locations and damage model: [Weapon Arsenal](../Gameplay/WeaponArsenal.md#hit-location-multipliers).

#### Backpacks & Storage

Full spec (rigs, backpacks, secure containers, stash cases): [**Gears — Storage Master Database**](../Gears/StorageGear/Storage_Master_Database.md).

***

#### Medical Supplies - Complete Specifications

| Code Name             | Display Name  | Rarity   | Heal Amount     | Heal Time | Stack Size | Weight (kg) | Grid Size | Value ($) | Special Effect      |
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

| Code Name              | Display Name    | Rarity   | Effect            | Duration | Stack Size | Weight (kg) | Grid Size | Value ($) |
| ---------------------- | --------------- | -------- | ----------------- | -------- | ---------- | ----------- | --------- | --------- |
| ITEM\_CONS\_ENERGY     | Energy Drink    | Common   | +20% sprint speed | 30 sec   | 3          | 0.2         | 1x1       | 100       |
| ITEM\_CONS\_ADRENALINE | Adrenaline Shot | Rare     | +30% all stats    | 15 sec   | 1          | 0.1         | 1x1       | 1,000     |
| ITEM\_CONS\_RATION     | Ration Pack     | Common   | Restore stamina   | Instant  | 5          | 0.3         | 1x1       | 50        |
| ITEM\_CONS\_WATER      | Water Bottle    | Common   | Restore hydration | Instant  | 4          | 0.5         | 1x1       | 30        |
| ITEM\_CONS\_PROTEIN    | Protein Bar     | Uncommon | +15% max stamina  | 60 sec   | 3          | 0.1         | 1x1       | 150       |

***

#### Tactical Equipment

| Code Name            | Display Name      | Rarity   | Effect                    | Duration          | Deploy Time | Stack Size | Weight (kg) | Grid Size | Value ($) |
| -------------------- | ----------------- | -------- | ------------------------- | ----------------- | ----------- | ---------- | ----------- | --------- | --------- |
| ITEM\_TAC\_SENSOR    | Sensor Mine       | Uncommon | Detect enemies 15m        | 60 sec            | 2 sec       | 2          | 0.4         | 1x2       | 400       |
| ITEM\_TAC\_CLAYMORE  | Claymore          | Rare     | 80 dmg cone               | Until triggered   | 3 sec       | 1          | 1.0         | 2x2       | 1,200     |
| ITEM\_TAC\_COVER     | Portable Cover    | Epic     | Deploy hard cover         | Permanent         | 5 sec       | 1          | 3.0         | 2x3       | 3,000     |
| ITEM\_TAC\_BARRICADE | Barricade Kit     | Uncommon | Block doorway             | Permanent         | 4 sec       | 1          | 2.5         | 2x2       | 800       |
| ITEM\_TAC\_C4        | C4 Explosive      | Epic     | 150 dmg 10m radius        | Remote detonation | 3 sec       | 1          | 0.8         | 1x2       | 2,500     |
| ITEM\_TAC\_BEACON    | Extraction Beacon | Rare     | Call emergency extraction | Single-use        | 2 sec       | 1          | 0.3         | 1x1       | 5,000     |

***

#### Keys & Special Items

| Code Name           | Display Name       | Rarity    | Use                         | Durability | Weight (kg) | Grid Size | Value ($)    | Drop Rate |
| ------------------- | ------------------ | --------- | --------------------------- | ---------- | ----------- | --------- | ------------ | --------- |
| ITEM\_KEY\_LOOTROOM | Loot Room Key      | Rare      | Unlock high-tier loot rooms | 1 use      | 0.1         | 1x1       | 5,000-10,000 | 5%        |
| ITEM\_KEY\_SAFE     | Safe Key           | Epic      | Open safes                  | 1 use      | 0.1         | 1x1       | 8,000-15,000 | 2%        |
| ITEM\_KEY\_SUPPLY   | Supply Drop Beacon | Legendary | Call personal supply drop   | 1 use      | 0.2         | 1x1       | 25,000       | 0.5%      |
| ITEM\_KEY\_BUNKER   | Bunker Key         | Epic      | Access bunker vault         | 3 uses     | 0.1         | 1x1       | 12,000       | 1%        |
| ITEM\_KEY\_OFFICE   | Office Key         | Uncommon  | Office rooms                | 5 uses     | 0.05        | 1x1       | 2,000        | 10%       |
| ITEM\_KEY\_MASTER   | Master Keycard     | Legendary | Universal access            | 1 use      | 0.1         | 1x1       | 50,000       | 0.1%      |

***

#### Crafting Materials

| Code Name                | Display Name    | Rarity    | Use                 | Stack Size | Weight (kg) | Grid Size | Value ($) | Where to Find      |
| ------------------------ | --------------- | --------- | ------------------- | ---------- | ----------- | --------- | --------- | ------------------ |
| ITEM\_CRAFT\_SCRAP       | Scrap Metal     | Common    | Basic repairs       | 50         | 0.05        | 1x1       | 10        | Everywhere         |
| ITEM\_CRAFT\_ELECTRONICS | Electronics     | Uncommon  | Attachment crafting | 20         | 0.1         | 1x1       | 50        | Mid zones          |
| ITEM\_CRAFT\_RARECOMP    | Rare Components | Rare      | High-tier crafting  | 10         | 0.2         | 1x1       | 200       | Hot zones          |
| ITEM\_CRAFT\_LEGENDARY   | Legendary Parts | Legendary | Legendary crafting  | 5          | 0.3         | 1x1       | 1,000     | Safes, bosses      |
| ITEM\_CRAFT\_CIRCUITS    | Circuit Boards  | Uncommon  | Tech item crafting  | 25         | 0.08        | 1x1       | 80        | Electronics stores |
| ITEM\_CRAFT\_POLYMER     | Polymer         | Common    | Armor repairs       | 40         | 0.06        | 1x1       | 20        | Industrial zones   |
| ITEM\_CRAFT\_TOOLS       | Tool Kit        | Rare      | Upgrade items       | 1          | 1.0         | 2x2       | 500       | Supply drops       |

***

#### Throwables & Grenades

| Code Name              | Display Name       | Rarity   | Damage                       | Radius (m) | Fuse Time | Stack Size | Weight (kg) | Grid Size | Value ($) | Special           |
| ---------------------- | ------------------ | -------- | ---------------------------- | ---------- | --------- | ---------- | ----------- | --------- | --------- | ----------------- |
| ITEM\_GREN\_FRAG       | Frag Grenade       | Common   | 100 (direct) 50-10 (falloff) | 8          | 3 sec     | 3          | 0.4         | 1x1       | 200       | Cookable          |
| ITEM\_GREN\_FLASH      | Flashbang          | Common   | 0 dmg                        | 10         | 1.5 sec   | 3          | 0.3         | 1x1       | 150       | 5s blind          |
| ITEM\_GREN\_SMOKE      | Smoke Grenade      | Common   | 0 dmg                        | 8          | 2 sec     | 3          | 0.3         | 1x1       | 100       | 15s duration      |
| ITEM\_GREN\_EMP        | EMP Grenade        | Rare     | 0 dmg                        | 15         | 2 sec     | 2          | 0.3         | 1x1       | 800       | Disable abilities |
| ITEM\_GREN\_INCENDIARY | Incendiary Grenade | Rare     | 40/sec DOT                   | 6          | 2 sec     | 2          | 0.4         | 1x1       | 600       | 8s burn           |
| ITEM\_GREN\_STUN       | Stun Grenade       | Uncommon | 0 dmg                        | 8          | 1.5 sec   | 3          | 0.3         | 1x1       | 250       | 3s stun           |

***

#### Quest & Special Items

| Code Name                 | Display Name           | Category | Weight (kg) | Grid Size | Sell Value  | Notes             |
| ------------------------- | ---------------------- | -------- | ----------- | --------- | ----------- | ----------------- |
| ITEM\_QUEST\_DOC\_SALVAGE | Salvage Corps Document | Quest    | 0.1         | 1x1       | Cannot sell | Faction quest     |
| ITEM\_QUEST\_DOC\_TECH    | Tech Syndicate Data    | Quest    | 0.1         | 1x1       | Cannot sell | Faction quest     |
| ITEM\_QUEST\_INTEL        | Intel Package          | Quest    | 0.2         | 1x1       | Cannot sell | Reputation reward |
| ITEM\_QUEST\_ARTIFACT1    | Artifact Piece Alpha   | Quest    | 0.3         | 1x1       | 500         | Part 1 of 5       |
| ITEM\_QUEST\_ARTIFACT2    | Artifact Piece Beta    | Quest    | 0.3         | 1x1       | 500         | Part 2 of 5       |
| ITEM\_QUEST\_SAMPLE       | Biological Sample      | Quest    | 0.5         | 1x2       | Cannot sell | Time-sensitive    |
| ITEM\_QUEST\_HARDDRIVE    | Encrypted Hard Drive   | Quest    | 0.4         | 1x1       | Cannot sell | Rare quest item   |

***

### Loot System

#### Loot Spawn Mechanics

**Container Types:**

**Wooden Crate (Common)**

* Spawn Rate: Very High (every 20-30m)
* Loot Quality: Common (80%), Uncommon (20%)
* Average Value: $500-1,500
* Typical Contents: Bandages, ammo, basic attachments

**Metal Locker (Uncommon)**

* Spawn Rate: Medium (every 50-80m)
* Loot Quality: Uncommon (60%), Rare (30%), Common (10%)
* Average Value: $2,000-5,000
* Typical Contents: Armor, medkits, uncommon weapons

**Weapon Rack (Uncommon)**

* Spawn Rate: Low (3-5 per map)
* Loot Quality: Weapons only
* Guaranteed weapon spawn (Common to Rare)
* Average Value: $1,500-6,000

**Safe (Rare)**

* Spawn Rate: Very Low (1-2 per hot zone)
* Requires: Key or lockpick (time)
* Loot Quality: Rare (50%), Epic (40%), Legendary (10%)
* Average Value: $8,000-20,000
* Typical Contents: High-tier weapons, armor, cash

**Supply Drop (Event)**

* Spawn: Timed events (5:00, 10:00)
* Location: Random hot zone
* Loot Quality: Epic (70%), Legendary (30%)
* Average Value: $15,000-30,000
* Risk: Contested, attracts all players

***

#### Loot Distribution by Zone

**Safe Zones (Map Edges)**

* Container Density: High
* Quality: 70% Common, 25% Uncommon, 5% Rare
* Risk: Low (AI only)
* Reward: Stable but modest

**Mid Zones**

* Container Density: Medium
* Quality: 40% Common, 40% Uncommon, 18% Rare, 2% Epic
* Risk: Medium (AI + players)
* Reward: Balanced risk/reward

**Hot Zones (Center)**

* Container Density: Low pero High Quality
* Quality: 20% Uncommon, 50% Rare, 25% Epic, 5% Legendary
* Risk: Very High (PvP combat)
* Reward: Highest value

**Contamination Zone (Late Game)**

* Container Density: Medium
* Quality: 30% Rare, 50% Epic, 20% Legendary
* Risk: Extreme (contamination damage + combat)
* Reward: Best loot before match end

***

#### Dynamic Loot Scaling

**Player Count Adjustment:**

* More players alive = More loot spawns
* Prevents loot drought
* Encourages exploration

**Time-Based:**

* Early game (0-5 min): Basic loot common
* Mid game (5-10 min): Quality increases
* Late game (10-15 min): Best loot in dangerous zones

**Death-Based:**

* Each player death: Small loot quality increase globally
* Compensates surviving players
* Rewards skilled survival

***

### Inventory Management

#### Grid-Based System

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

* Small (1x1): Ammo, consumables, keys
* Medium (1x2): Pistols, attachments, meds
* Large (2x2): SMGs, armor pieces
* Very Large (2x3): Assault rifles, helmets
* Huge (2x4): Sniper rifles, LMGs

**Tetris-Style Rotation:**

* Rotate items to fit
* Efficient packing rewarded
* Strategic space management

***

#### Secure Container

**Purpose:** Protect high-value items from death loss

**Standard Container (Free):**

* Size: 2x2 (4 slots)
* Cannot be upgraded in-match

**Expanded Container (Premium/Quest):**

* Size: 2x3 (6 slots)
* Unlock: Level 25 or Premium
* Permanent upgrade

**Container Rules:**

* Can only place items IN during raid
* Cannot take items OUT during raid
* Prevents container abuse
* Preserves risk/reward balance

***

#### Weight & Encumbrance

**Weight System:**

* Each item has weight (kg)
* Total weight affects movement

**Weight Thresholds:**

| Weight Total | Movement Speed | Stamina Drain | Effects          |
| ------------ | -------------- | ------------- | ---------------- |
| 0-15 kg      | 100%           | Normal        | None             |
| 15-25 kg     | 90%            | +20%          | Slight slowdown  |
| 25-35 kg     | 75%            | +50%          | Heavy encumbered |
| 35+ kg       | 60%            | +100%         | Severely slowed  |

**Strategic Decisions:**

* More loot = slower escape
* Drop items if chased
* Balance greed vs survival

***

### Player Trading & Marketplace

#### Direct Trading (Post-Launch Feature)

**Face-to-Face Trading:**

* Players can trade in lobby
* Drag and drop items
* Both accept = complete trade
* No fees for direct trades

**Safety Features:**

* Trade window shows both offers
* Confirmation required from both
* Cannot scam ifboth see everything
* Trade history logged

***

#### Auction House

**Listing Items:**

* List item for specific price
* Set buyout price (optional)
* Listing fee: 5% of starting bid
* Duration: 24, 48, or 72 hours

**Bidding:**

* Players bid on items
* Automatic outbid notifications
* Last-minute extensions (anti-snipe)
* Highest bid wins

**Fees:**

* Listing fee: 5% (non-refundable)
* Sale fee: 10% (from final sale price)
* Total cost: 15% to seller
* Purpose: Credit sink (prevent inflation)

***

#### Market Dynamics

**Supply & Demand:**

* Prices fluctuate based on availability
* Rare items cost more
* Common items cheap
* Weekend events affect prices

**Price Floors:**

* Minimum vendor price (prevents crashes)
* Prevents item value from hitting $0
* Maintains economic stability

**Market Manipulation Prevention:**

* Transaction limits
* Price change limits (max 50% jump/day)
* Whale detection (large bulk buys flagged)

***

#### Popular Trade Items

**High-Demand Items:**

1. Epic/Legendary weapons
2. Rare keys
3. Armor (always needed)
4. Medical supplies (consumable)
5. Crafting materials (bulk trading)

**Profitable Flipping:**

* Buy low during high supply
* Sell high during scarcity
* Weekend events create opportunities
* Requires market knowledge

***

### Crafting System (Future Feature)

#### Crafting Basics

**Workbench (Stash):**

* Combine materials to create items
* Unlock recipes through progression
* Time-based (instant or wait)

**Example Recipes:**

**Medkit (Uncommon)**

* Materials: 5x Bandages + 2x Medical Supplies
* Craft Time: Instant
* Output: 1x Medkit
* Cost Savings: 20% vs buying

**Rare Weapon (Customization)**

* Materials: Base weapon + 3x Rare Components + Attachments
* Craft Time: Instant
* Output: Weapon with pre-installed attachments
* Benefit: Saves attachment installation time

**Armor Repair:**

* Materials: Damaged armor + Scrap Metal
* Output: Repaired armor (80% durability)
* Cheaper than buying new

***

### Economic Sinks & Sources

#### Credit Sources (Inflow)

**Primary:**

* Extract loot and sell: $2,000-20,000 per match
* Quest rewards: $1,000-10,000 per quest
* Daily login: $500/day
* Level-up: $500-2,000 per level

**Secondary:**

* Achievements: One-time bonuses
* Events: Limited-time earnings
* Referrals: $5,000 per friend (max 10)

***

#### Credit Sinks (Outflow)

**Primary:**

* Weapon purchases: $500-20,000
* Armor purchases: $800-15,000
* Medical supplies: $50-2,500
* Stash expansion: $10,000 per upgrade

**Secondary:**

* Marketplace fees: 15% of transactions
* Name changes: $1,000
* Cosmetic purchases: $500-5,000
* Insurance (future): Based on gear value

***

#### Anti-Inflation Measures

**Item Loss on Death:**

* Largest credit sink
* Removes items from economy
* Creates constant demand
* Prevents supply saturation

**Transaction Fees:**

* 15% marketplace tax
* Prevents rapid flipping
* Stabilizes prices
* Removes credits from economy

**Durability System (Future):**

* Weapons degrade with use
* Require repair or replacement
* Ongoing credit expenditure
* Balances high-tier weapon accessibility

***

### Item Insurance (Future Feature)

#### How It Works

**Pre-Match Insurance:**

* Pay fee (20-30% of item value)
* If you die, item returned (80% chance)
* 24-hour wait for return
* Does NOT work if extracted by enemy

**Benefits:**

* Reduce risk of expensive loadouts
* Encourage using good gear
* Still lose if looted by players

**Limitations:**

* Only insured items returned
* Secure container items don't need insurance
* Max 3 insured items per match

***

### Black Market (Future PvE Feature)

**Concept:** High-risk AI trader in dangerous zones

**How It Works:**

* NPC trader spawns in contaminated areas
* Sells Epic/Legendary items
* Accepts cash only (in-raid currency)
* Risk: PvP + contamination while shopping

**Special Offers:**

* Rotating inventory
* Discounted rare items
* Exclusive black market weapons
* Intel items

***

### Season al Economy Events

**Double Loot Weekend:**

* All containers have 2x loot
* Prices drop due to supply increase
* Good time to buy and stockpile

**Rare Item Event:**

* Increased spawn rate of specific item type
* Example: "Sniper Week" - more snipers spawn
* Strategic selling window

**Trader Special:**

* NPC vendors discount specific categories
* 20-30% off selected items
* Limited-time offers

***

### Economic Balance Goals

**Healthy Economy Indicators:**

* Average player wealth: $50,000-150,000
* Inflation rate: <5% per month
* Market activity: 60%+ of players trade monthly
* Price stability: <20% fluctuation week-to-week

**Problem Indicators:**

* Hyperinflation (prices double monthly)
* Dead market (no trades happening)
* Wealth concentration (top 1% has 50%+ wealth)
* Item scarcity (specific items unobtainable)

**Developer Interventions:**

* Adjust loot spawn rates
* Modify marketplace fees
* Special events to inject/remove credits
* Emergency balance patches
