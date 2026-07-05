---
title: Armor Gear
linkTitle: Armor
type: docs
weight: 1
---

# Armor Gear Documentation

This section covers all armor worn by the Operator: body vests, helmets, face shields, headsets, and armored rigs. Armor uses a **Class 1–6** (GOST-style) system with zone-based protection, materials, durability, and repair.

## Documentation Tree

| Document                                              | Description                                                                                                                                              |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Armor & Ballistics](Armor.md)                        | Core spec: armor classes 1–6, hitboxes & coverage zones, material properties, penetration check, blunt damage, ricochet. Mapping Class to display value. |
| [Armor Master Database](Armor_Master_Database.md)     | Full item list: body vests, helmets, face shields, headsets, armored rigs — Code, Class, zones, material, weight, durability, value, trader, rarity.     |
| [Armor Handling Settings](Armor_Handling_Settings.md) | Equip/remove times, movement penalty, sprint/turn/ADS penalty, ergonomics impact, audio penalties (hearing), top-down rotation feel.                     |
| [Armor Balance Framework](Armor_Balance_Framework.md) | Effective HP vs caliber, TTK impact matrix, cost-efficiency index, durability & repair math, balance levers, rarity–power curve.                         |
| [Armor Progression](Armor_Progression.md)             | Trader unlock gating, Safe House repair bench progression, armor crafting recipes, Found-in-Raid armor condition.                                        |
| [Armor Visual Identity](Armor_Visual_Identity.md)     | Top-down silhouette guide, shoulder profile per class, rarity color-coding (ground vs equipped), damage state visuals, UI icons.                         |

## Related Sections

* [**Gear Tier System**](../Gear_Tier_System.md) — Armor Tier (1–5) definition; progression = Tier + Rarity + player/trader level.
* [**Storage Gear — Armored Rigs**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) — Rigs that include built-in armor; see Storage Master Database.
* [**Weapons — Caliber & Ballistics**](../../Weapons/Caliber_Ballistics_System.md) — Penetration power vs armor class, blunt damage formula.
* [**Gameplay — Gear Mechanics**](../../Gameplay/Gear_Mechanics.md) — Armor weight vs protection table, loadout examples.
