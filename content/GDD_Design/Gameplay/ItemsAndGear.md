---
title: Items & Gear Catalogue
type: docs
weight: 26
---

# Items & Gear Catalogue

### Overview

This document is the **authoritative item catalogue** for all equipable, consumable, and deployable items in the game. All items listed here exist in the game's loot economy and stash — they can be found in-raid, purchased from traders, or crafted in the Safe House.

> **Cross-References:** [Weapon Arsenal](WeaponArsenal.md) — weapons and attachments as items; [Gear Mechanics](Gear_Mechanics.md) — how armor condition, weight, and encumbrance rules work; [Medical System](Medical_System.md) — full medical healing rules, body-part HP, toxicity; [Loot Table Design](Loot_Table_Design.md) — where these items spawn per zone tier; [Looting & Inventory](Looting_Interactions.md) — inventory grid, secure container, FIR status, marketplace; [Safe House Design](../GameDesign/Safe_House_Design.md) — crafting recipes using crafting materials.

***

### 1. Armor — Helmets

Helmets reduce headshot damage multiplier based on **Armor Class** (1–6) and durability. Display value maps from class; see [Gears — Armor & Ballistics](../Gears/ArmorGear/Armor.md#mapping-armor-class-to-display-value).

| Code Name            | Display Name      | Rarity   | Class | Headshot Reduction | Weight (kg) | Grid | Value ($) | Special               |
| -------------------- | ----------------- | -------- | :---: | :----------------: | :---------: | :--: | --------: | --------------------- |
| ITEM\_HELM\_LIGHT    | Light Helmet      | Common   |   2   |         25%        |     0.8     |  2×2 |       800 | Basic protection      |
| ITEM\_HELM\_MEDIUM   | Medium Helmet     | Uncommon |   3   |         40%        |     1.2     |  2×2 |     2,500 | Good balance          |
| ITEM\_HELM\_HEAVY    | Heavy Helmet      | Rare     |   4   |         50%        |     1.8     |  2×2 |     6,000 | High protection       |
| ITEM\_HELM\_TACTICAL | Tactical Helmet   | Epic     |   5   |         60%        |     1.5     |  2×2 |    12,000 | Built-in night vision |
| ITEM\_HELM\_SPEC     | Specialist Helmet | Rare     |   3   |         45%        |     1.0     |  2×2 |     4,500 | +10% hearing range    |

**Full spec** (zones, material, ricochet, durability): [Gears — Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md). **Headshot multiplier system:** [Weapon Arsenal — Hit Location Multipliers](WeaponArsenal.md#hit-location-multipliers).

***

### 2. Armor — Body Vests

Body vests absorb damage to the chest/torso. **Armor Class** (1–6) and durability define protection; repair at Safe House Repair Bench.

| Code Name            | Display Name  | Rarity   | Class | Coverage          | Move Penalty | Weight (kg) | Grid | Value ($) |
| -------------------- | ------------- | -------- | :---: | ----------------- | :----------: | :---------: | :--: | --------: |
| ITEM\_VEST\_LIGHT    | Light Vest    | Common   |   2   | Chest only        |      0%      |     2.0     |  2×3 |     1,000 |
| ITEM\_VEST\_MEDIUM   | Medium Vest   | Uncommon |   3   | Chest + Back      |      −5%     |     3.5     |  2×3 |     3,000 |
| ITEM\_VEST\_HEAVY    | Heavy Vest    | Rare     |   4   | Full torso        |     −10%     |     5.5     |  2×3 |     8,000 |
| ITEM\_VEST\_TACTICAL | Tactical Rig  | Epic     |   5   | Full torso + arms |     −15%     |     6.0     |  2×3 |    15,000 |
| ITEM\_VEST\_CARRIER  | Plate Carrier | Rare     |   4   | Full torso        |      −8%     |     4.8     |  2×3 |    10,000 |

**Full spec** (zones, material, durability, repair): [Gears — Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md).

***

### 3. Backpacks & Storage

Backpacks increase inventory capacity. All backpack contents are **lost on death** (only Secure Container is protected). Tactical rigs provide hotkey slots; reload is from rig only.

| Code Name           | Display Name      | Rarity   | Slots | Grid Layout | Move Penalty | Weight (kg) | Value ($) |
| ------------------- | ----------------- | -------- | :---: | :---------: | :----------: | :---------: | --------: |
| ITEM\_BAG\_SMALL    | Small Backpack    | Common   |   +6  |     2×3     |      0%      |     0.5     |       500 |
| ITEM\_BAG\_MEDIUM   | Medium Backpack   | Uncommon |  +12  |     3×4     |      0%      |     1.0     |     1,500 |
| ITEM\_BAG\_LARGE    | Large Backpack    | Rare     |  +20  |     4×5     |      0%      |     1.5     |     4,000 |
| ITEM\_BAG\_TACTICAL | Tactical Backpack | Epic     |  +30  |     5×6     |      −5%     |     2.0     |    10,000 |
| ITEM\_BAG\_ASSAULT  | Assault Pack      | Uncommon |  +15  |     3×5     |      0%      |     1.2     |     2,500 |

**Full spec** (rigs, backpacks, secure containers, slot layouts): [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) and [Storage Master Database](../Gears/StorageGear/Storage_Master_Database.md). **Weight and Encumbrance:** [Gear Mechanics](Gear_Mechanics.md).

***

### 4. Medical Supplies

> For full healing rules, body part HP system, bleed treatment, and toxicity → see [Medical System](Medical_System.md).

This table provides the **item specs** for economic and looting purposes.

| Code Name             | Display Name  | Rarity   | Heal Amount     | Heal Time | Stack | Weight (kg) | Grid | Value ($) | Special Effect       |
| --------------------- | ------------- | -------- | --------------- | :-------: | :---: | :---------: | :--: | --------: | -------------------- |
| ITEM\_MED\_BANDAGE    | Bandage       | Common   | +15 HP over 3s  |     3s    |   5   |     0.1     |  1×1 |        50 | Stops bleeding       |
| ITEM\_MED\_MEDKIT     | Medkit        | Uncommon | +50 HP over 5s  |     5s    |   3   |     0.3     |  1×2 |       200 | —                    |
| ITEM\_MED\_STIM       | Combat Stim   | Rare     | +30 HP instant  |     1s    |   2   |     0.2     |  1×1 |       800 | +10% speed 10s       |
| ITEM\_MED\_SURGERY    | Surgery Kit   | Epic     | +100 HP over 8s |     8s    |   1   |     0.5     |  2×2 |     2,500 | Removes all debuffs  |
| ITEM\_MED\_PAINKILLER | Painkillers   | Uncommon | —               |     2s    |   3   |     0.1     |  1×1 |       300 | −15% dmg taken 60s   |
| ITEM\_MED\_BLOODBAG   | Blood Bag     | Rare     | +40 HP over 10s |    10s    |   1   |     0.4     |  1×2 |     1,200 | +20% max HP for 2min |
| ITEM\_MED\_FIRSTAID   | First Aid Kit | Common   | +25 HP over 4s  |     4s    |   4   |     0.2     |  1×2 |       120 | Basic healing        |

***

### 5. Consumables & Utilities

Performance-enhancing consumables. All effects are temporary — no permanent stat boosts from consumables.

| Code Name              | Display Name    | Rarity   | Effect                    | Duration | Stack | Weight (kg) | Grid | Value ($) |
| ---------------------- | --------------- | -------- | ------------------------- | :------: | :---: | :---------: | :--: | --------: |
| ITEM\_CONS\_ENERGY     | Energy Drink    | Common   | +20% sprint speed         |    30s   |   3   |     0.2     |  1×1 |       100 |
| ITEM\_CONS\_ADRENALINE | Adrenaline Shot | Rare     | +30% all stats            |    15s   |   1   |     0.1     |  1×1 |     1,000 |
| ITEM\_CONS\_RATION     | Ration Pack     | Common   | Restore stamina instantly |  Instant |   5   |     0.3     |  1×1 |        50 |
| ITEM\_CONS\_WATER      | Water Bottle    | Common   | Restore hydration         |  Instant |   4   |     0.5     |  1×1 |        30 |
| ITEM\_CONS\_PROTEIN    | Protein Bar     | Uncommon | +15% max stamina          |    60s   |   3   |     0.1     |  1×1 |       150 |

***

### 6. Tactical Equipment

Active deployables and traps. All deployables have placement animations (vulnerability window while deploying).

| Code Name            | Display Name      | Rarity   | Effect                      |      Duration     | Deploy Time | Stack | Weight (kg) | Grid | Value ($) |
| -------------------- | ----------------- | -------- | --------------------------- | :---------------: | :---------: | :---: | :---------: | :--: | --------: |
| ITEM\_TAC\_SENSOR    | Sensor Mine       | Uncommon | Detect enemies 15m radius   |        60s        |      2s     |   2   |     0.4     |  1×2 |       400 |
| ITEM\_TAC\_CLAYMORE  | Claymore          | Rare     | 80 dmg cone, laser trigger  |  Until triggered  |      3s     |   1   |     1.0     |  2×2 |     1,200 |
| ITEM\_TAC\_COVER     | Portable Cover    | Epic     | Deploy hard cover           |     Permanent     |      5s     |   1   |     3.0     |  2×3 |     3,000 |
| ITEM\_TAC\_BARRICADE | Barricade Kit     | Uncommon | Block doorway               |     Permanent     |      4s     |   1   |     2.5     |  2×2 |       800 |
| ITEM\_TAC\_C4        | C4 Explosive      | Epic     | 150 dmg, 10m radius, remote | Remote detonation |      3s     |   1   |     0.8     |  1×2 |     2,500 |
| ITEM\_TAC\_BEACON    | Extraction Beacon | Rare     | Call emergency extraction   |     Single-use    |      2s     |   1   |     0.3     |  1×1 |     5,000 |

***

### 7. Throwables & Grenades

> See also [Weapon Arsenal — Grenade Quick Reference](WeaponArsenal.md#throwables--equipment) for tactical usage notes.

| Code Name              | Display Name       | Rarity   |           Damage           | Radius | Fuse | Stack | Weight (kg) | Grid | Value ($) | Special                |
| ---------------------- | ------------------ | -------- | :------------------------: | :----: | :--: | :---: | :---------: | :--: | --------: | ---------------------- |
| ITEM\_GREN\_FRAG       | Frag Grenade       | Common   | 100 direct / 50–10 falloff |   8m   |  3s  |   3   |     0.4     |  1×1 |       200 | Cookable               |
| ITEM\_GREN\_FLASH      | Flashbang          | Common   |              0             |   10m  | 1.5s |   3   |     0.3     |  1×1 |       150 | 5s blind + disorient   |
| ITEM\_GREN\_SMOKE      | Smoke Grenade      | Common   |              0             |   8m   |  2s  |   3   |     0.3     |  1×1 |       100 | 15s cloud              |
| ITEM\_GREN\_EMP        | EMP Grenade        | Rare     |              0             |   15m  |  2s  |   2   |     0.3     |  1×1 |       800 | Disables abilities 10s |
| ITEM\_GREN\_INCENDIARY | Incendiary Grenade | Rare     |         40/sec DoT         |   6m   |  2s  |   2   |     0.4     |  1×1 |       600 | 8s burn                |
| ITEM\_GREN\_STUN       | Stun Grenade       | Uncommon |              0             |   8m   | 1.5s |   3   |     0.3     |  1×1 |       250 | 3s stun                |

***

### 8. Keys & Special Items

Keys unlock gated loot areas. Single-use keys are permanently destroyed after use — they are high-value trade items.

| Code Name           | Display Name       | Rarity    | Use                                  | Durability | Weight (kg) | Grid |    Value ($) | Drop Rate |
| ------------------- | ------------------ | --------- | ------------------------------------ | :--------: | :---------: | :--: | -----------: | :-------: |
| ITEM\_KEY\_LOOTROOM | Loot Room Key      | Rare      | Unlock high-tier loot rooms          |    1 use   |     0.1     |  1×1 | 5,000–10,000 |     5%    |
| ITEM\_KEY\_SAFE     | Safe Key           | Epic      | Open safes with guaranteed rare loot |    1 use   |     0.1     |  1×1 | 8,000–15,000 |     2%    |
| ITEM\_KEY\_SUPPLY   | Supply Drop Beacon | Legendary | Call personal supply drop            |    1 use   |     0.2     |  1×1 |       25,000 |    0.5%   |
| ITEM\_KEY\_BUNKER   | Bunker Key         | Epic      | Access bunker vault                  |   3 uses   |     0.1     |  1×1 |       12,000 |     1%    |
| ITEM\_KEY\_OFFICE   | Office Key         | Uncommon  | Office room access                   |   5 uses   |     0.05    |  1×1 |        2,000 |    10%    |
| ITEM\_KEY\_MASTER   | Master Keycard     | Legendary | Universal access                     |    1 use   |     0.1     |  1×1 |       50,000 |    0.1%   |

***

### 9. Crafting Materials

Materials used in Safe House crafting recipes. High-value bulk trade items on the marketplace.

> See [Safe House Design](../GameDesign/Safe_House_Design.md) for full crafting recipes, Safe House module requirements, and crafting timers.

| Code Name                | Display Name    | Rarity    | Use                     | Stack | Weight (kg) | Grid | Value ($) | Found In           |
| ------------------------ | --------------- | --------- | ----------------------- | :---: | :---------: | :--: | --------: | ------------------ |
| ITEM\_CRAFT\_SCRAP       | Scrap Metal     | Common    | Basic weapon repairs    |   50  |     0.05    |  1×1 |        10 | Everywhere         |
| ITEM\_CRAFT\_ELECTRONICS | Electronics     | Uncommon  | Attachment crafting     |   20  |     0.1     |  1×1 |        50 | Mid zones          |
| ITEM\_CRAFT\_RARECOMP    | Rare Components | Rare      | High-tier crafting      |   10  |     0.2     |  1×1 |       200 | Hot zones          |
| ITEM\_CRAFT\_LEGENDARY   | Legendary Parts | Legendary | Legendary item crafting |   5   |     0.3     |  1×1 |     1,000 | Safes, Boss drops  |
| ITEM\_CRAFT\_CIRCUITS    | Circuit Boards  | Uncommon  | Tech item crafting      |   25  |     0.08    |  1×1 |        80 | Electronics stores |
| ITEM\_CRAFT\_POLYMER     | Polymer         | Common    | Armor repairs           |   40  |     0.06    |  1×1 |        20 | Industrial zones   |
| ITEM\_CRAFT\_TOOLS       | Tool Kit        | Rare      | Item upgrades           |   1   |     1.0     |  2×2 |       500 | Supply drops       |

***

### 10. Quest & Special Items

Quest items **cannot be sold** on the marketplace. They take up regular inventory slots — putting them in your Secure Container is the recommended strategy.

| Code Name                 | Display Name           | Category | Weight (kg) | Grid |  Sell Value | Notes             |
| ------------------------- | ---------------------- | -------- | :---------: | :--: | :---------: | ----------------- |
| ITEM\_QUEST\_DOC\_SALVAGE | Salvage Corps Document | Quest    |     0.1     |  1×1 | Cannot sell | Faction quest     |
| ITEM\_QUEST\_DOC\_TECH    | Tech Syndicate Data    | Quest    |     0.1     |  1×1 | Cannot sell | Faction quest     |
| ITEM\_QUEST\_INTEL        | Intel Package          | Quest    |     0.2     |  1×1 | Cannot sell | Reputation reward |
| ITEM\_QUEST\_ARTIFACT1    | Artifact Piece Alpha   | Quest    |     0.3     |  1×1 |     $500    | Part 1 of 5       |
| ITEM\_QUEST\_ARTIFACT2    | Artifact Piece Beta    | Quest    |     0.3     |  1×1 |     $500    | Part 2 of 5       |
| ITEM\_QUEST\_SAMPLE       | Biological Sample      | Quest    |     0.5     |  1×2 | Cannot sell | Time-sensitive    |
| ITEM\_QUEST\_HARDDRIVE    | Encrypted Hard Drive   | Quest    |     0.4     |  1×1 | Cannot sell | Rare quest item   |

***

### 11. Economy — Item Sources & Sinks

Understanding where items enter and leave the economy is critical for balance.

#### Credit Sources (Inflow)

| Source                                       | Rate                     |
| -------------------------------------------- | ------------------------ |
| Extract loot and sell to traders/marketplace | $2,000–$20,000 per match |
| Quest rewards                                | $1,000–$10,000 per quest |
| Daily login bonus                            | $500/day                 |
| Level-up reward                              | $500–$2,000 per level    |
| Achievements (one-time)                      | Varies                   |
| Event rewards                                | Varies                   |

#### Credit Sinks (Outflow)

| Sink                            | Rate                     |
| ------------------------------- | ------------------------ |
| Weapon purchases                | $500–$20,000             |
| Armor purchases                 | $800–$15,000             |
| Medical supply restocking       | $50–$2,500 per item      |
| Stash expansion                 | $10,000 per upgrade      |
| Marketplace listing + sale fees | 15% total of transaction |
| Insurance premium               | 8–15% of item value      |

#### Anti-Inflation Measures

| Measure                               | Mechanism                                                        |
| ------------------------------------- | ---------------------------------------------------------------- |
| **Item Loss on Death**                | Largest credit sink — removes items from economy permanently     |
| **Transaction Fees**                  | 15% marketplace tax prevents rapid flipping                      |
| **Durability System**                 | Weapons and armor degrade — ongoing repair spend                 |
| **Supply-limited crafting materials** | Prevents infinite crafting loops                                 |
| **Price floor (traders)**             | Minimum vendor buyback price prevents item value from collapsing |

#### Economic Balance Goals

| Indicator             | Target                        |
| --------------------- | ----------------------------- |
| Average player wealth | $50,000–$150,000              |
| Inflation rate        | <5% per month                 |
| Market activity       | 60%+ of players trade monthly |
| Price stability       | <20% fluctuation week-to-week |

**Problem indicators requiring intervention:** Hyperinflation (prices double monthly), dead market (no trades), wealth concentration (top 1% has 50%+ of credits), item scarcity for key categories.

***

### Cross-References

* [Weapon Arsenal](WeaponArsenal.md) — Weapons and attachments as their own item catalogue section.
* [Gear Mechanics](Gear_Mechanics.md) — Item condition system, weight encumbrance thresholds, armor repair rules.
* [Medical System](Medical_System.md) — Full healing rules; medical item interactions with body-part HP, toxicity, bleed.
* [Loot Table Design](Loot_Table_Design.md) — Container types, zone loot tables, and where each category spawns.
* [Looting & Inventory](Looting_Interactions.md) — Grid inventory system, Secure Container rules, FIR status, marketplace/auction house.
* [Safe House Design](../GameDesign/Safe_House_Design.md) — Crafting material consumption; Safe House module unlock gates; crafting recipe list.
* [GameDesign/Economy](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Economy.md) — Macro economy design: flea market, trader tiers, inflation control.
* [GameDesign/Insurance System](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/InsuranceSystem.md) — Insurance cost formula and which items are insurable.
