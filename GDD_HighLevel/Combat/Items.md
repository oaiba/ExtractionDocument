# Items & Economy Systems

**[← Previous: Weapons](./Weapons.md)** | **[Index](../README.md)**

---

## Economy Philosophy

**Core Principles:**
1. **Player-Driven** - Market prices determined by supply/demand
2. **Risk Creates Value** - Rare items from dangerous zones worth more
3. **No Pay-to-Win** - Real money cannot buy gameplay advantages
4. **Fair Trading** - Systems prevent scams and exploitation
5. **Economic Sinks** - Prevent inflation through item loss and fees

---

## Item Categories

### 1. Weapons & Attachments
*See: [Weapons & Combat](./09_WeaponsCombat.md) for details*

**Economic Role:**
- Primary value holders
- High-risk items (lost on death)
- Create demand for constant replacement

---

### 2. Armor & Protection

#### Helmets

**Light Helmet (Common)**
- Armor Value: 30
- Headshot Reduction: 25%
- Durability: 3-5 hits
- Value: $800

**Medium Helmet (Uncommon)**
- Armor Value: 50
- Headshot Reduction: 40%
- Durability: 5-8 hits
- Value: $2,500

**Heavy Helmet (Rare)**
- Armor Value: 75
- Headshot Reduction: 50%
- Durability: 8-12 hits
- Value: $6,000

**Tactical Helmet (Epic)**
- Armor Value: 100
- Headshot Reduction: 60%
- Durability: 12-15 hits
- Special: Built-in night vision
- Value: $12,000

---

#### Body Armor

**Light Vest (Common)**
- Armor Value: 30
- Coverage: Chest only
- Movement: Normal speed
- Value: $1,000

**Medium Vest (Uncommon)**
- Armor Value: 50
- Coverage: Chest + Back
- Movement: -5% speed
- Value: $3,000

**Heavy Vest (Rare)**
- Armor Value: 80
- Coverage: Full torso
- Movement: -10% speed
- Value: $8,000

**Tactical Rig (Epic)**
- Armor Value: 100
- Coverage: Full torso + arms
- Movement: -15% speed
- Special: +4 inventory slots
- Value: $15,000

---

### 3. Backpacks & Storage

**Small Backpack (Common)**
- Inventory Slots: +6 (2x3)
- Value: $500

**Medium Backpack (Uncommon)**
- Inventory Slots: +12 (3x4)
- Value: $1,500

**Large Backpack (Rare)**
- Inventory Slots: +20 (4x5)
- Value: $4,000

**Tactical Backpack (Epic)**
- Inventory Slots: +30 (5x6)
- Movement: -5% speed (trade-off)
- Value: $10,000

---

### 4. Medical Supplies

**Bandage (Common)**
- Effect: +15 HP over 3 sec, stops bleeding
- Stack Size: 5
- Weight: 0.1 kg each
- Value: $50

**Medkit (Uncommon)**
- Effect: +50 HP over 5 sec
- Stack Size: 3
- Weight: 0.3 kg each
- Value: $200

**Combat Stim (Rare)**
- Effect: +30 HP instant, +10% speed for 10 sec
- Stack Size: 2
- Weight: 0.2 kg each
- Value: $800

**Surgery Kit (Epic)**
- Effect: Full heal (100 HP), 8 sec use
- Stack Size: 1
- Weight: 0.5 kg
- Value: $2,500

**Painkillers (Uncommon)**
- Effect: Reduces damage taken by 15% for 60 sec
- Stack Size: 3
- Weight: 0.1 kg each
- Value: $300

---

### 5. Consumables & Utilities

**Energy Drink (Common)**
- Effect: +20% sprint speed for 30 sec
- Stack Size: 3
- Value: $100

**Adrenaline Shot (Rare)**
- Effect: +30% all stats for 15 sec
- Stack Size: 1
- Value: $1,000

**Ration Pack (Common)**
- Effect: Restores stamina instantly
- Stack Size: 5
- Value: $50

---

### 6. Tactical Equipment

**Sensor Mine (Uncommon)**
- Effect: Detects enemies in 15m radius
- Duration: 60 seconds
- Stack Size: 2
- Value: $400

**Claymore (Rare)**
- Effect: 80 damage in cone
- Trigger: Laser tripwire
- Stack Size: 1
- Value: $1,200

**Portable Cover (Epic)**
- Effect: Deploy temporary hard cover
- Duration: Permanent until destroyed
- Stack Size: 1
- Value: $3,000

---

### 7. Keys & Special Items

**Loot Room Key (Rare)**
- Use: Unlocks high-tier loot rooms
- Single-use
- Value: $5,000-10,000

**Safe Key (Epic)**
- Use: Opens safes with guaranteed rare loot
- Single-use
- Value: $8,000-15,000

**Supply Drop Beacon (Legendary)**
- Use: Calls personal supply drop
- Single-use
- Contents: Random Epic/Legendary items
- Value: $25,000

---

### 8. Crafting Materials

**Scrap Metal (Common)**
- Use: Basic weapon repairs
- Stack Size: 50
- Value: $10 each

**Electronics (Uncommon)**
- Use: Attachment crafting
- Stack Size: 20
- Value: $50 each

**Rare Components (Rare)**
- Use: High-tier crafting
- Stack Size: 10
- Value: $200 each

**Legendary Parts (Legendary)**
- Use: Legendary weapon crafting
- Stack Size: 5
- Value: $1,000 each

---

### 9. Quest Items

**Faction Documents**
- Faction-specific quest items
- No stack limit
- Value: Cannot be sold (quest use only)

**Intel Packages**
- Deliver to faction for reputation
- Single item
- Value: Reputation reward

**Artifact Pieces**
- Collect full set for legendary reward
- Part of larger quest chain
- Value: $500 each (partial value)

---

## Items Reference Tables

### Armor & Protection - Complete Specifications

#### Helmets

| Code Name          | Display Name      | Rarity   | Armor Value | Headshot Reduction | Durability (Hits) | Weight (kg) | Grid Size | Value ($) | Special Features      |
| ------------------ | ----------------- | -------- | ----------- | ------------------ | ----------------- | ----------- | --------- | --------- | --------------------- |
| ITEM_HELM_LIGHT    | Light Helmet      | Common   | 30          | 25%                | 3-5               | 0.8         | 2x2       | 800       | Basic protection      |
| ITEM_HELM_MEDIUM   | Medium Helmet     | Uncommon | 50          | 40%                | 5-8               | 1.2         | 2x2       | 2,500     | Good balance          |
| ITEM_HELM_HEAVY    | Heavy Helmet      | Rare     | 75          | 50%                | 8-12              | 1.8         | 2x2       | 6,000     | High protection       |
| ITEM_HELM_TACTICAL | Tactical Helmet   | Epic     | 100         | 60%                | 12-15             | 1.5         | 2x2       | 12,000    | Built-in night vision |
| ITEM_HELM_SPEC     | Specialist Helmet | Rare     | 60          | 45%                | 6-10              | 1.0         | 2x2       | 4,500     | +10% hearing range    |

#### Body Armor

| Code Name          | Display Name  | Rarity   | Armor Value | Coverage          | Movement Penalty | Weight (kg) | Grid Size | Inventory Bonus | Value ($) |
| ------------------ | ------------- | -------- | ----------- | ----------------- | ---------------- | ----------- | --------- | --------------- | --------- |
| ITEM_VEST_LIGHT    | Light Vest    | Common   | 30          | Chest only        | 0%               | 2.0         | 2x3       | -               | 1,000     |
| ITEM_VEST_MEDIUM   | Medium Vest   | Uncommon | 50          | Chest + Back      | -5%              | 3.5         | 2x3       | -               | 3,000     |
| ITEM_VEST_HEAVY    | Heavy Vest    | Rare     | 80          | Full torso        | -10%             | 5.5         | 2x3       | -               | 8,000     |
| ITEM_VEST_TACTICAL | Tactical Rig  | Epic     | 100         | Full torso + arms | -15%             | 6.0         | 2x3       | +4 slots        | 15,000    |
| ITEM_VEST_CARRIER  | Plate Carrier | Rare     | 90          | Full torso        | -8%              | 4.8         | 2x3       | +2 slots        | 10,000    |

---

### Backpacks & Storage

| Code Name         | Display Name      | Rarity   | Inventory Slots | Grid Layout | Movement Penalty | Weight (kg) | Value ($) | Durability      |
| ----------------- | ----------------- | -------- | --------------- | ----------- | ---------------- | ----------- | --------- | --------------- |
| ITEM_BAG_SMALL    | Small Backpack    | Common   | +6              | 2x3         | 0%               | 0.5         | 500       | Standard        |
| ITEM_BAG_MEDIUM   | Medium Backpack   | Uncommon | +12             | 3x4         | 0%               | 1.0         | 1,500     | Standard        |
| ITEM_BAG_LARGE    | Large Backpack    | Rare     | +20             | 4x5         | 0%               | 1.5         | 4,000     | Standard        |
| ITEM_BAG_TACTICAL | Tactical Backpack | Epic     | +30             | 5x6         | -5%              | 2.0         | 10,000    | Reinforced      |
| ITEM_BAG_ASSAULT  | Assault Pack      | Uncommon | +15             | 3x5         | 0%               | 1.2         | 2,500     | Water-resistant |

---

### Medical Supplies - Complete Specifications

| Code Name           | Display Name  | Rarity   | Heal Amount     | Heal Time | Stack Size | Weight (kg) | Grid Size | Value ($) | Special Effect      |
| ------------------- | ------------- | -------- | --------------- | --------- | ---------- | ----------- | --------- | --------- | ------------------- |
| ITEM_MED_BANDAGE    | Bandage       | Common   | +15 HP over 3s  | 3 sec     | 5          | 0.1         | 1x1       | 50        | Stops bleeding      |
| ITEM_MED_MEDKIT     | Medkit        | Uncommon | +50 HP over 5s  | 5 sec     | 3          | 0.3         | 1x2       | 200       | -                   |
| ITEM_MED_STIM       | Combat Stim   | Rare     | +30 HP instant  | 1 sec     | 2          | 0.2         | 1x1       | 800       | +10% speed 10s      |
| ITEM_MED_SURGERY    | Surgery Kit   | Epic     | +100 HP over 8s | 8 sec     | 1          | 0.5         | 2x2       | 2,500     | Removes all debuffs |
| ITEM_MED_PAINKILLER | Painkillers   | Uncommon | -               | 2 sec     | 3          | 0.1         | 1x1       | 300       | -15% dmg taken 60s  |
| ITEM_MED_BLOODBAG   | Blood Bag     | Rare     | +40 HP over 10s | 10 sec    | 1          | 0.4         | 1x2       | 1,200     | +20% max HP 2min    |
| ITEM_MED_FIRSTAID   | First Aid Kit | Common   | +25 HP over 4s  | 4 sec     | 4          | 0.2         | 1x2       | 120       | Basic healing       |

---

### Consumables & Utilities

| Code Name            | Display Name    | Rarity   | Effect            | Duration | Stack Size | Weight (kg) | Grid Size | Value ($) |
| -------------------- | --------------- | -------- | ----------------- | -------- | ---------- | ----------- | --------- | --------- |
| ITEM_CONS_ENERGY     | Energy Drink    | Common   | +20% sprint speed | 30 sec   | 3          | 0.2         | 1x1       | 100       |
| ITEM_CONS_ADRENALINE | Adrenaline Shot | Rare     | +30% all stats    | 15 sec   | 1          | 0.1         | 1x1       | 1,000     |
| ITEM_CONS_RATION     | Ration Pack     | Common   | Restore stamina   | Instant  | 5          | 0.3         | 1x1       | 50        |
| ITEM_CONS_WATER      | Water Bottle    | Common   | Restore hydration | Instant  | 4          | 0.5         | 1x1       | 30        |
| ITEM_CONS_PROTEIN    | Protein Bar     | Uncommon | +15% max stamina  | 60 sec   | 3          | 0.1         | 1x1       | 150       |

---

### Tactical Equipment

| Code Name          | Display Name      | Rarity   | Effect                    | Duration          | Deploy Time | Stack Size | Weight (kg) | Grid Size | Value ($) |
| ------------------ | ----------------- | -------- | ------------------------- | ----------------- | ----------- | ---------- | ----------- | --------- | --------- |
| ITEM_TAC_SENSOR    | Sensor Mine       | Uncommon | Detect enemies 15m        | 60 sec            | 2 sec       | 2          | 0.4         | 1x2       | 400       |
| ITEM_TAC_CLAYMORE  | Claymore          | Rare     | 80 dmg cone               | Until triggered   | 3 sec       | 1          | 1.0         | 2x2       | 1,200     |
| ITEM_TAC_COVER     | Portable Cover    | Epic     | Deploy hard cover         | Permanent         | 5 sec       | 1          | 3.0         | 2x3       | 3,000     |
| ITEM_TAC_BARRICADE | Barricade Kit     | Uncommon | Block doorway             | Permanent         | 4 sec       | 1          | 2.5         | 2x2       | 800       |
| ITEM_TAC_C4        | C4 Explosive      | Epic     | 150 dmg 10m radius        | Remote detonation | 3 sec       | 1          | 0.8         | 1x2       | 2,500     |
| ITEM_TAC_BEACON    | Extraction Beacon | Rare     | Call emergency extraction | Single-use        | 2 sec       | 1          | 0.3         | 1x1       | 5,000     |

---

### Keys & Special Items

| Code Name         | Display Name       | Rarity    | Use                         | Durability | Weight (kg) | Grid Size | Value ($)    | Drop Rate |
| ----------------- | ------------------ | --------- | --------------------------- | ---------- | ----------- | --------- | ------------ | --------- |
| ITEM_KEY_LOOTROOM | Loot Room Key      | Rare      | Unlock high-tier loot rooms | 1 use      | 0.1         | 1x1       | 5,000-10,000 | 5%        |
| ITEM_KEY_SAFE     | Safe Key           | Epic      | Open safes                  | 1 use      | 0.1         | 1x1       | 8,000-15,000 | 2%        |
| ITEM_KEY_SUPPLY   | Supply Drop Beacon | Legendary | Call personal supply drop   | 1 use      | 0.2         | 1x1       | 25,000       | 0.5%      |
| ITEM_KEY_BUNKER   | Bunker Key         | Epic      | Access bunker vault         | 3 uses     | 0.1         | 1x1       | 12,000       | 1%        |
| ITEM_KEY_OFFICE   | Office Key         | Uncommon  | Office rooms                | 5 uses     | 0.05        | 1x1       | 2,000        | 10%       |
| ITEM_KEY_MASTER   | Master Keycard     | Legendary | Universal access            | 1 use      | 0.1         | 1x1       | 50,000       | 0.1%      |

---

### Crafting Materials

| Code Name              | Display Name    | Rarity    | Use                 | Stack Size | Weight (kg) | Grid Size | Value ($) | Where to Find      |
| ---------------------- | --------------- | --------- | ------------------- | ---------- | ----------- | --------- | --------- | ------------------ |
| ITEM_CRAFT_SCRAP       | Scrap Metal     | Common    | Basic repairs       | 50         | 0.05        | 1x1       | 10        | Everywhere         |
| ITEM_CRAFT_ELECTRONICS | Electronics     | Uncommon  | Attachment crafting | 20         | 0.1         | 1x1       | 50        | Mid zones          |
| ITEM_CRAFT_RARECOMP    | Rare Components | Rare      | High-tier crafting  | 10         | 0.2         | 1x1       | 200       | Hot zones          |
| ITEM_CRAFT_LEGENDARY   | Legendary Parts | Legendary | Legendary crafting  | 5          | 0.3         | 1x1       | 1,000     | Safes, bosses      |
| ITEM_CRAFT_CIRCUITS    | Circuit Boards  | Uncommon  | Tech item crafting  | 25         | 0.08        | 1x1       | 80        | Electronics stores |
| ITEM_CRAFT_POLYMER     | Polymer         | Common    | Armor repairs       | 40         | 0.06        | 1x1       | 20        | Industrial zones   |
| ITEM_CRAFT_TOOLS       | Tool Kit        | Rare      | Upgrade items       | 1          | 1.0         | 2x2       | 500       | Supply drops       |

---

### Throwables & Grenades

| Code Name            | Display Name       | Rarity   | Damage                       | Radius (m) | Fuse Time | Stack Size | Weight (kg) | Grid Size | Value ($) | Special           |
| -------------------- | ------------------ | -------- | ---------------------------- | ---------- | --------- | ---------- | ----------- | --------- | --------- | ----------------- |
| ITEM_GREN_FRAG       | Frag Grenade       | Common   | 100 (direct) 50-10 (falloff) | 8          | 3 sec     | 3          | 0.4         | 1x1       | 200       | Cookable          |
| ITEM_GREN_FLASH      | Flashbang          | Common   | 0 dmg                        | 10         | 1.5 sec   | 3          | 0.3         | 1x1       | 150       | 5s blind          |
| ITEM_GREN_SMOKE      | Smoke Grenade      | Common   | 0 dmg                        | 8          | 2 sec     | 3          | 0.3         | 1x1       | 100       | 15s duration      |
| ITEM_GREN_EMP        | EMP Grenade        | Rare     | 0 dmg                        | 15         | 2 sec     | 2          | 0.3         | 1x1       | 800       | Disable abilities |
| ITEM_GREN_INCENDIARY | Incendiary Grenade | Rare     | 40/sec DOT                   | 6          | 2 sec     | 2          | 0.4         | 1x1       | 600       | 8s burn           |
| ITEM_GREN_STUN       | Stun Grenade       | Uncommon | 0 dmg                        | 8          | 1.5 sec   | 3          | 0.3         | 1x1       | 250       | 3s stun           |

---

### Quest & Special Items

| Code Name              | Display Name           | Category | Weight (kg) | Grid Size | Sell Value  | Notes             |
| ---------------------- | ---------------------- | -------- | ----------- | --------- | ----------- | ----------------- |
| ITEM_QUEST_DOC_SALVAGE | Salvage Corps Document | Quest    | 0.1         | 1x1       | Cannot sell | Faction quest     |
| ITEM_QUEST_DOC_TECH    | Tech Syndicate Data    | Quest    | 0.1         | 1x1       | Cannot sell | Faction quest     |
| ITEM_QUEST_INTEL       | Intel Package          | Quest    | 0.2         | 1x1       | Cannot sell | Reputation reward |
| ITEM_QUEST_ARTIFACT1   | Artifact Piece Alpha   | Quest    | 0.3         | 1x1       | 500         | Part 1 of 5       |
| ITEM_QUEST_ARTIFACT2   | Artifact Piece Beta    | Quest    | 0.3         | 1x1       | 500         | Part 2 of 5       |
| ITEM_QUEST_SAMPLE      | Biological Sample      | Quest    | 0.5         | 1x2       | Cannot sell | Time-sensitive    |
| ITEM_QUEST_HARDDRIVE   | Encrypted Hard Drive   | Quest    | 0.4         | 1x1       | Cannot sell | Rare quest item   |

---

## Loot System

### Loot Spawn Mechanics

**Container Types:**

**Wooden Crate (Common)**
- Spawn Rate: Very High (every 20-30m)
- Loot Quality: Common (80%), Uncommon (20%)
- Average Value: $500-1,500
- Typical Contents: Bandages, ammo, basic attachments

**Metal Locker (Uncommon)**
- Spawn Rate: Medium (every 50-80m)
- Loot Quality: Uncommon (60%), Rare (30%), Common (10%)
- Average Value: $2,000-5,000
- Typical Contents: Armor, medkits, uncommon weapons

**Weapon Rack (Uncommon)**
- Spawn Rate: Low (3-5 per map)
- Loot Quality: Weapons only
- Guaranteed weapon spawn (Common to Rare)
- Average Value: $1,500-6,000

**Safe (Rare)**
- Spawn Rate: Very Low (1-2 per hot zone)
- Requires: Key or lockpick (time)
- Loot Quality: Rare (50%), Epic (40%), Legendary (10%)
- Average Value: $8,000-20,000
- Typical Contents: High-tier weapons, armor, cash

**Supply Drop (Event)**
- Spawn: Timed events (5:00, 10:00)
- Location: Random hot zone
- Loot Quality: Epic (70%), Legendary (30%)
- Average Value: $15,000-30,000
- Risk: Contested, attracts all players

---

### Loot Distribution by Zone

**Safe Zones (Map Edges)**
- Container Density: High
- Quality: 70% Common, 25% Uncommon, 5% Rare
- Risk: Low (AI only)
- Reward: Stable but modest

**Mid Zones**
- Container Density: Medium
- Quality: 40% Common, 40% Uncommon, 18% Rare, 2% Epic
- Risk: Medium (AI + players)
- Reward: Balanced risk/reward

**Hot Zones (Center)**
- Container Density: Low pero High Quality
- Quality: 20% Uncommon, 50% Rare, 25% Epic, 5% Legendary
- Risk: Very High (PvP combat)
- Reward: Highest value

**Contamination Zone (Late Game)**
- Container Density: Medium
- Quality: 30% Rare, 50% Epic, 20% Legendary
- Risk: Extreme (contamination damage + combat)
- Reward: Best loot before match end

---

### Dynamic Loot Scaling

**Player Count Adjustment:**
- More players alive = More loot spawns
- Prevents loot drought
- Encourages exploration

**Time-Based:**
- Early game (0-5 min): Basic loot common
- Mid game (5-10 min): Quality increases
- Late game (10-15 min): Best loot in dangerous zones

**Death-Based:**
- Each player death: Small loot quality increase globally
- Compensates surviving players
- Rewards skilled survival

---

## Inventory Management

### Grid-Based System

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
- Small (1x1): Ammo, consumables, keys
- Medium (1x2): Pistols, attachments, meds
- Large (2x2): SMGs, armor pieces
- Very Large (2x3): Assault rifles, helmets
- Huge (2x4): Sniper rifles, LMGs

**Tetris-Style Rotation:**
- Rotate items to fit
- Efficient packing rewarded
- Strategic space management

---

### Secure Container

**Purpose:** Protect high-value items from death loss

**Standard Container (Free):**
- Size: 2x2 (4 slots)
- Cannot be upgraded in-match

**Expanded Container (Premium/Quest):**
- Size: 2x3 (6 slots)
- Unlock: Level 25 or Premium
- Permanent upgrade

**Container Rules:**
- Can only place items IN during raid
- Cannot take items OUT during raid
- Prevents container abuse
- Preserves risk/reward balance

---

### Weight & Encumbrance

**Weight System:**
- Each item has weight (kg)
- Total weight affects movement

**Weight Thresholds:**
| Weight Total | Movement Speed | Stamina Drain | Effects          |
| ------------ | -------------- | ------------- | ---------------- |
| 0-15 kg      | 100%           | Normal        | None             |
| 15-25 kg     | 90%            | +20%          | Slight slowdown  |
| 25-35 kg     | 75%            | +50%          | Heavy encumbered |
| 35+ kg       | 60%            | +100%         | Severely slowed  |

**Strategic Decisions:**
- More loot = slower escape
- Drop items if chased
- Balance greed vs survival

---

## Player Trading & Marketplace

### Direct Trading (Post-Launch Feature)

**Face-to-Face Trading:**
- Players can trade in lobby
- Drag and drop items
- Both accept = complete trade
- No fees for direct trades

**Safety Features:**
- Trade window shows both offers
- Confirmation required from both
- Cannot scam ifboth see everything
- Trade history logged

---

### Auction House

**Listing Items:**
- List item for specific price
- Set buyout price (optional)
- Listing fee: 5% of starting bid
- Duration: 24, 48, or 72 hours

**Bidding:**
- Players bid on items
- Automatic outbid notifications
- Last-minute extensions (anti-snipe)
- Highest bid wins

**Fees:**
- Listing fee: 5% (non-refundable)
- Sale fee: 10% (from final sale price)
- Total cost: 15% to seller
- Purpose: Credit sink (prevent inflation)

---

### Market Dynamics

**Supply & Demand:**
- Prices fluctuate based on availability
- Rare items cost more
- Common items cheap
- Weekend events affect prices

**Price Floors:**
- Minimum vendor price (prevents crashes)
- Prevents item value from hitting $0
- Maintains economic stability

**Market Manipulation Prevention:**
- Transaction limits
- Price change limits (max 50% jump/day)
- Whale detection (large bulk buys flagged)

---

### Popular Trade Items

**High-Demand Items:**
1. Epic/Legendary weapons
2. Rare keys
3. Armor (always needed)
4. Medical supplies (consumable)
5. Crafting materials (bulk trading)

**Profitable Flipping:**
- Buy low during high supply
- Sell high during scarcity
- Weekend events create opportunities
- Requires market knowledge

---

## Crafting System (Future Feature)

### Crafting Basics

**Workbench (Stash):**
- Combine materials to create items
- Unlock recipes through progression
- Time-based (instant or wait)

**Example Recipes:**

**Medkit (Uncommon)**
- Materials: 5x Bandages + 2x Medical Supplies
- Craft Time: Instant
- Output: 1x Medkit
- Cost Savings: 20% vs buying

**Rare Weapon (Customization)**
- Materials: Base weapon + 3x Rare Components + Attachments
- Craft Time: Instant
- Output: Weapon with pre-installed attachments
- Benefit: Saves attachment installation time

**Armor Repair:**
- Materials: Damaged armor + Scrap Metal
- Output: Repaired armor (80% durability)
- Cheaper than buying new

---

## Economic Sinks & Sources

### Credit Sources (Inflow)

**Primary:**
- Extract loot and sell: $2,000-20,000 per match
- Quest rewards: $1,000-10,000 per quest
- Daily login: $500/day
- Level-up: $500-2,000 per level

**Secondary:**
- Achievements: One-time bonuses
- Events: Limited-time earnings
- Referrals: $5,000 per friend (max 10)

---

### Credit Sinks (Outflow)

**Primary:**
- Weapon purchases: $500-20,000
- Armor purchases: $800-15,000
- Medical supplies: $50-2,500
- Stash expansion: $10,000 per upgrade

**Secondary:**
- Marketplace fees: 15% of transactions
- Name changes: $1,000
- Cosmetic purchases: $500-5,000
- Insurance (future): Based on gear value

---

### Anti-Inflation Measures

**Item Loss on Death:**
- Largest credit sink
- Removes items from economy
- Creates constant demand
- Prevents supply saturation

**Transaction Fees:**
- 15% marketplace tax
- Prevents rapid flipping
- Stabilizes prices
- Removes credits from economy

**Durability System (Future):**
- Weapons degrade with use
- Require repair or replacement
- Ongoing credit expenditure
- Balances high-tier weapon accessibility

---

## Item Insurance (Future Feature)

### How It Works

**Pre-Match Insurance:**
- Pay fee (20-30% of item value)
- If you die, item returned (80% chance)
- 24-hour wait for return
- Does NOT work if extracted by enemy

**Benefits:**
- Reduce risk of expensive loadouts
- Encourage using good gear
- Still lose if looted by players

**Limitations:**
- Only insured items returned
- Secure container items don't need insurance
- Max 3 insured items per match

---

## Black Market (Future PvE Feature)

**Concept:** High-risk AI trader in dangerous zones

**How It Works:**
- NPC trader spawns in contaminated areas
- Sells Epic/Legendary items
- Accepts cash only (in-raid currency)
- Risk: PvP + contamination while shopping

**Special Offers:**
- Rotating inventory
- Discounted rare items
- Exclusive black market weapons
- Intel items

---

## Season al Economy Events

**Double Loot Weekend:**
- All containers have 2x loot
- Prices drop due to supply increase
- Good time to buy and stockpile

**Rare Item Event:**
- Increased spawn rate of specific item type
- Example: "Sniper Week" - more snipers spawn
- Strategic selling window

**Trader Special:**
- NPC vendors discount specific categories
- 20-30% off selected items
- Limited-time offers

---

## Economic Balance Goals

**Healthy Economy Indicators:**
- Average player wealth: $50,000-150,000
- Inflation rate: <5% per month
- Market activity: 60%+ of players trade monthly
- Price stability: <20% fluctuation week-to-week

**Problem Indicators:**
- Hyperinflation (prices double monthly)
- Dead market (no trades happening)
- Wealth concentration (top 1% has 50%+ wealth)
- Item scarcity (specific items unobtainable)

**Developer Interventions:**
- Adjust loot spawn rates
- Modify marketplace fees
- Special events to inject/remove credits
- Emergency balance patches

---

**[← Previous: Weapons & Combat](./Weapons.md)** | **[High-Level Index](./README.md)**
