---
title: "Items & Gear Catalogue"
type: docs
weight: 26
---

## Overview

This document is the **authoritative item catalogue** for all equipable, consumable, and deployable items in the game. All items listed here exist in the game's loot economy and stash — they can be found in-raid, purchased from traders, or crafted in the Hideout.

> **Cross-References:** [Weapon Arsenal](WeaponArsenal.md) — weapons and attachments as items; [Gear Mechanics](Gear_Mechanics.md) — how armor condition, weight, and encumbrance rules work; [Medical System](Medical_System.md) — full medical healing rules, body-part HP, toxicity; [Loot Table Design](Loot_Table_Design.md) — where these items spawn per zone tier; [Looting & Inventory](Looting_Interactions.md) — inventory grid, secure container, FIR status, marketplace; [Hideout & Crafting](Hideout_Crafting.md) — crafting recipes using crafting materials.

---

## 1. Armor — Helmets

Helmets reduce headshot damage multiplier based on **Armor Class** (1–6) and durability. Display value maps from class; see [Gears — Armor & Ballistics](../Gears/ArmorGear/Armor.md#mapping-armor-class-to-display-value).

| Code Name | Display Name | Rarity | Class | Headshot Reduction | Weight (kg) | Grid | Value ($) | Special |
| :-------- | :----------- | :----- | :---: | :----------------: | :---------: | :--: | --------: | :------ |
| ITEM_HELM_LIGHT | Light Helmet | Common | 2 | 25% | 0.8 | 2×2 | 800 | Basic protection |
| ITEM_HELM_MEDIUM | Medium Helmet | Uncommon | 3 | 40% | 1.2 | 2×2 | 2,500 | Good balance |
| ITEM_HELM_HEAVY | Heavy Helmet | Rare | 4 | 50% | 1.8 | 2×2 | 6,000 | High protection |
| ITEM_HELM_TACTICAL | Tactical Helmet | Epic | 5 | 60% | 1.5 | 2×2 | 12,000 | Built-in night vision |
| ITEM_HELM_SPEC | Specialist Helmet | Rare | 3 | 45% | 1.0 | 2×2 | 4,500 | +10% hearing range |

**Full spec** (zones, material, ricochet, durability): [Gears — Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md). **Headshot multiplier system:** [Weapon Arsenal — Hit Location Multipliers](WeaponArsenal.md#hit-location-multipliers).

---

## 2. Armor — Body Vests

Body vests absorb damage to the chest/torso. **Armor Class** (1–6) and durability define protection; repair at Hideout Repair Bench.

| Code Name | Display Name | Rarity | Class | Coverage | Move Penalty | Weight (kg) | Grid | Value ($) |
| :-------- | :----------- | :----- | :---: | :------- | :----------: | :---------: | :--: | --------: |
| ITEM_VEST_LIGHT | Light Vest | Common | 2 | Chest only | 0% | 2.0 | 2×3 | 1,000 |
| ITEM_VEST_MEDIUM | Medium Vest | Uncommon | 3 | Chest + Back | −5% | 3.5 | 2×3 | 3,000 |
| ITEM_VEST_HEAVY | Heavy Vest | Rare | 4 | Full torso | −10% | 5.5 | 2×3 | 8,000 |
| ITEM_VEST_TACTICAL | Tactical Rig | Epic | 5 | Full torso + arms | −15% | 6.0 | 2×3 | 15,000 |
| ITEM_VEST_CARRIER | Plate Carrier | Rare | 4 | Full torso | −8% | 4.8 | 2×3 | 10,000 |

**Full spec** (zones, material, durability, repair): [Gears — Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md).

---

## 3. Backpacks & Storage

Backpacks increase inventory capacity. All backpack contents are **lost on death** (only Secure Container is protected). Tactical rigs provide hotkey slots; reload is from rig only.

| Code Name | Display Name | Rarity | Slots | Grid Layout | Move Penalty | Weight (kg) | Value ($) |
| :-------- | :----------- | :----- | :---: | :---------: | :----------: | :---------: | --------: |
| ITEM_BAG_SMALL | Small Backpack | Common | +6 | 2×3 | 0% | 0.5 | 500 |
| ITEM_BAG_MEDIUM | Medium Backpack | Uncommon | +12 | 3×4 | 0% | 1.0 | 1,500 |
| ITEM_BAG_LARGE | Large Backpack | Rare | +20 | 4×5 | 0% | 1.5 | 4,000 |
| ITEM_BAG_TACTICAL | Tactical Backpack | Epic | +30 | 5×6 | −5% | 2.0 | 10,000 |
| ITEM_BAG_ASSAULT | Assault Pack | Uncommon | +15 | 3×5 | 0% | 1.2 | 2,500 |

**Full spec** (rigs, backpacks, secure containers, slot layouts): [Gears — Storage Gear](../Gears/StorageGear/) and [Storage Master Database](../Gears/StorageGear/Storage_Master_Database.md). **Weight and Encumbrance:** [Gear Mechanics](Gear_Mechanics.md).

---

## 4. Medical Supplies

> For full healing rules, body part HP system, bleed treatment, and toxicity → see [Medical System](Medical_System.md).

This table provides the **item specs** for economic and looting purposes.

| Code Name | Display Name | Rarity | Heal Amount | Heal Time | Stack | Weight (kg) | Grid | Value ($) | Special Effect |
| :-------- | :----------- | :----- | :---------- | :-------: | :---: | :---------: | :--: | --------: | :------------- |
| ITEM_MED_BANDAGE | Bandage | Common | +15 HP over 3s | 3s | 5 | 0.1 | 1×1 | 50 | Stops bleeding |
| ITEM_MED_MEDKIT | Medkit | Uncommon | +50 HP over 5s | 5s | 3 | 0.3 | 1×2 | 200 | — |
| ITEM_MED_STIM | Combat Stim | Rare | +30 HP instant | 1s | 2 | 0.2 | 1×1 | 800 | +10% speed 10s |
| ITEM_MED_SURGERY | Surgery Kit | Epic | +100 HP over 8s | 8s | 1 | 0.5 | 2×2 | 2,500 | Removes all debuffs |
| ITEM_MED_PAINKILLER | Painkillers | Uncommon | — | 2s | 3 | 0.1 | 1×1 | 300 | −15% dmg taken 60s |
| ITEM_MED_BLOODBAG | Blood Bag | Rare | +40 HP over 10s | 10s | 1 | 0.4 | 1×2 | 1,200 | +20% max HP for 2min |
| ITEM_MED_FIRSTAID | First Aid Kit | Common | +25 HP over 4s | 4s | 4 | 0.2 | 1×2 | 120 | Basic healing |

---

## 5. Consumables & Utilities

Performance-enhancing consumables. All effects are temporary — no permanent stat boosts from consumables.

| Code Name | Display Name | Rarity | Effect | Duration | Stack | Weight (kg) | Grid | Value ($) |
| :-------- | :----------- | :----- | :----- | :------: | :---: | :---------: | :--: | --------: |
| ITEM_CONS_ENERGY | Energy Drink | Common | +20% sprint speed | 30s | 3 | 0.2 | 1×1 | 100 |
| ITEM_CONS_ADRENALINE | Adrenaline Shot | Rare | +30% all stats | 15s | 1 | 0.1 | 1×1 | 1,000 |
| ITEM_CONS_RATION | Ration Pack | Common | Restore stamina instantly | Instant | 5 | 0.3 | 1×1 | 50 |
| ITEM_CONS_WATER | Water Bottle | Common | Restore hydration | Instant | 4 | 0.5 | 1×1 | 30 |
| ITEM_CONS_PROTEIN | Protein Bar | Uncommon | +15% max stamina | 60s | 3 | 0.1 | 1×1 | 150 |

---

## 6. Tactical Equipment

Active deployables and traps. All deployables have placement animations (vulnerability window while deploying).

| Code Name | Display Name | Rarity | Effect | Duration | Deploy Time | Stack | Weight (kg) | Grid | Value ($) |
| :-------- | :----------- | :----- | :----- | :------: | :---------: | :---: | :---------: | :--: | --------: |
| ITEM_TAC_SENSOR | Sensor Mine | Uncommon | Detect enemies 15m radius | 60s | 2s | 2 | 0.4 | 1×2 | 400 |
| ITEM_TAC_CLAYMORE | Claymore | Rare | 80 dmg cone, laser trigger | Until triggered | 3s | 1 | 1.0 | 2×2 | 1,200 |
| ITEM_TAC_COVER | Portable Cover | Epic | Deploy hard cover | Permanent | 5s | 1 | 3.0 | 2×3 | 3,000 |
| ITEM_TAC_BARRICADE | Barricade Kit | Uncommon | Block doorway | Permanent | 4s | 1 | 2.5 | 2×2 | 800 |
| ITEM_TAC_C4 | C4 Explosive | Epic | 150 dmg, 10m radius, remote | Remote detonation | 3s | 1 | 0.8 | 1×2 | 2,500 |
| ITEM_TAC_BEACON | Extraction Beacon | Rare | Call emergency extraction | Single-use | 2s | 1 | 0.3 | 1×1 | 5,000 |

---

## 7. Throwables & Grenades

> See also [Weapon Arsenal — Grenade Quick Reference](WeaponArsenal.md#throwables--equipment) for tactical usage notes.

| Code Name | Display Name | Rarity | Damage | Radius | Fuse | Stack | Weight (kg) | Grid | Value ($) | Special |
| :-------- | :----------- | :----- | :----: | :----: | :--: | :---: | :---------: | :--: | --------: | :------ |
| ITEM_GREN_FRAG | Frag Grenade | Common | 100 direct / 50–10 falloff | 8m | 3s | 3 | 0.4 | 1×1 | 200 | Cookable |
| ITEM_GREN_FLASH | Flashbang | Common | 0 | 10m | 1.5s | 3 | 0.3 | 1×1 | 150 | 5s blind + disorient |
| ITEM_GREN_SMOKE | Smoke Grenade | Common | 0 | 8m | 2s | 3 | 0.3 | 1×1 | 100 | 15s cloud |
| ITEM_GREN_EMP | EMP Grenade | Rare | 0 | 15m | 2s | 2 | 0.3 | 1×1 | 800 | Disables abilities 10s |
| ITEM_GREN_INCENDIARY | Incendiary Grenade | Rare | 40/sec DoT | 6m | 2s | 2 | 0.4 | 1×1 | 600 | 8s burn |
| ITEM_GREN_STUN | Stun Grenade | Uncommon | 0 | 8m | 1.5s | 3 | 0.3 | 1×1 | 250 | 3s stun |

---

## 8. Keys & Special Items

Keys unlock gated loot areas. Single-use keys are permanently destroyed after use — they are high-value trade items.

| Code Name | Display Name | Rarity | Use | Durability | Weight (kg) | Grid | Value ($) | Drop Rate |
| :-------- | :----------- | :----- | :-- | :--------: | :---------: | :--: | --------: | :-------: |
| ITEM_KEY_LOOTROOM | Loot Room Key | Rare | Unlock high-tier loot rooms | 1 use | 0.1 | 1×1 | 5,000–10,000 | 5% |
| ITEM_KEY_SAFE | Safe Key | Epic | Open safes with guaranteed rare loot | 1 use | 0.1 | 1×1 | 8,000–15,000 | 2% |
| ITEM_KEY_SUPPLY | Supply Drop Beacon | Legendary | Call personal supply drop | 1 use | 0.2 | 1×1 | 25,000 | 0.5% |
| ITEM_KEY_BUNKER | Bunker Key | Epic | Access bunker vault | 3 uses | 0.1 | 1×1 | 12,000 | 1% |
| ITEM_KEY_OFFICE | Office Key | Uncommon | Office room access | 5 uses | 0.05 | 1×1 | 2,000 | 10% |
| ITEM_KEY_MASTER | Master Keycard | Legendary | Universal access | 1 use | 0.1 | 1×1 | 50,000 | 0.1% |

---

## 9. Crafting Materials

Materials used in Hideout crafting recipes. High-value bulk trade items on the marketplace.

> See [Hideout & Crafting](Hideout_Crafting.md) for full crafting recipes, Hideout module requirements, and crafting timers.

| Code Name | Display Name | Rarity | Use | Stack | Weight (kg) | Grid | Value ($) | Found In |
| :-------- | :----------- | :----- | :-- | :---: | :---------: | :--: | --------: | :------- |
| ITEM_CRAFT_SCRAP | Scrap Metal | Common | Basic weapon repairs | 50 | 0.05 | 1×1 | 10 | Everywhere |
| ITEM_CRAFT_ELECTRONICS | Electronics | Uncommon | Attachment crafting | 20 | 0.1 | 1×1 | 50 | Mid zones |
| ITEM_CRAFT_RARECOMP | Rare Components | Rare | High-tier crafting | 10 | 0.2 | 1×1 | 200 | Hot zones |
| ITEM_CRAFT_LEGENDARY | Legendary Parts | Legendary | Legendary item crafting | 5 | 0.3 | 1×1 | 1,000 | Safes, Boss drops |
| ITEM_CRAFT_CIRCUITS | Circuit Boards | Uncommon | Tech item crafting | 25 | 0.08 | 1×1 | 80 | Electronics stores |
| ITEM_CRAFT_POLYMER | Polymer | Common | Armor repairs | 40 | 0.06 | 1×1 | 20 | Industrial zones |
| ITEM_CRAFT_TOOLS | Tool Kit | Rare | Item upgrades | 1 | 1.0 | 2×2 | 500 | Supply drops |

---

## 10. Quest & Special Items

Quest items **cannot be sold** on the marketplace. They take up regular inventory slots — putting them in your Secure Container is the recommended strategy.

| Code Name | Display Name | Category | Weight (kg) | Grid | Sell Value | Notes |
| :-------- | :----------- | :------- | :---------: | :--: | :--------: | :---- |
| ITEM_QUEST_DOC_SALVAGE | Salvage Corps Document | Quest | 0.1 | 1×1 | Cannot sell | Faction quest |
| ITEM_QUEST_DOC_TECH | Tech Syndicate Data | Quest | 0.1 | 1×1 | Cannot sell | Faction quest |
| ITEM_QUEST_INTEL | Intel Package | Quest | 0.2 | 1×1 | Cannot sell | Reputation reward |
| ITEM_QUEST_ARTIFACT1 | Artifact Piece Alpha | Quest | 0.3 | 1×1 | $500 | Part 1 of 5 |
| ITEM_QUEST_ARTIFACT2 | Artifact Piece Beta | Quest | 0.3 | 1×1 | $500 | Part 2 of 5 |
| ITEM_QUEST_SAMPLE | Biological Sample | Quest | 0.5 | 1×2 | Cannot sell | Time-sensitive |
| ITEM_QUEST_HARDDRIVE | Encrypted Hard Drive | Quest | 0.4 | 1×1 | Cannot sell | Rare quest item |

---

## 11. Economy — Item Sources & Sinks

Understanding where items enter and leave the economy is critical for balance.

### Credit Sources (Inflow)

| Source | Rate |
| :----- | :--- |
| Extract loot and sell to traders/marketplace | $2,000–$20,000 per match |
| Quest rewards | $1,000–$10,000 per quest |
| Daily login bonus | $500/day |
| Level-up reward | $500–$2,000 per level |
| Achievements (one-time) | Varies |
| Event rewards | Varies |

### Credit Sinks (Outflow)

| Sink | Rate |
| :--- | :--- |
| Weapon purchases | $500–$20,000 |
| Armor purchases | $800–$15,000 |
| Medical supply restocking | $50–$2,500 per item |
| Stash expansion | $10,000 per upgrade |
| Marketplace listing + sale fees | 15% total of transaction |
| Insurance premium | 8–15% of item value |

### Anti-Inflation Measures

| Measure | Mechanism |
| :------ | :-------- |
| **Item Loss on Death** | Largest credit sink — removes items from economy permanently |
| **Transaction Fees** | 15% marketplace tax prevents rapid flipping |
| **Durability System** | Weapons and armor degrade — ongoing repair spend |
| **Supply-limited crafting materials** | Prevents infinite crafting loops |
| **Price floor (traders)** | Minimum vendor buyback price prevents item value from collapsing |

### Economic Balance Goals

| Indicator | Target |
| :-------- | :----- |
| Average player wealth | $50,000–$150,000 |
| Inflation rate | <5% per month |
| Market activity | 60%+ of players trade monthly |
| Price stability | <20% fluctuation week-to-week |

**Problem indicators requiring intervention:** Hyperinflation (prices double monthly), dead market (no trades), wealth concentration (top 1% has 50%+ of credits), item scarcity for key categories.

---

## Cross-References

- [Weapon Arsenal](WeaponArsenal.md) — Weapons and attachments as their own item catalogue section.
- [Gear Mechanics](Gear_Mechanics.md) — Item condition system, weight encumbrance thresholds, armor repair rules.
- [Medical System](Medical_System.md) — Full healing rules; medical item interactions with body-part HP, toxicity, bleed.
- [Loot Table Design](Loot_Table_Design.md) — Container types, zone loot tables, and where each category spawns.
- [Looting & Inventory](Looting_Interactions.md) — Grid inventory system, Secure Container rules, FIR status, marketplace/auction house.
- [Hideout & Crafting](Hideout_Crafting.md) — Crafting material consumption; Hideout module unlock gates; crafting recipe list.
- [GameDesign/Economy](../../GameDesign/Economy.md) — Macro economy design: flea market, trader tiers, inflation control.
- [GameDesign/Insurance System](../../GameDesign/InsuranceSystem.md) — Insurance cost formula and which items are insurable.
