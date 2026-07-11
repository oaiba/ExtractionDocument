---
title: Gears System
linkTitle: Gears
type: docs
weight: 7
---

# Gears Documentation

**Gears** are the physical equipment that the Operator wears or carries in-raid: body armor, helmets, tactical rigs, backpacks, and secure containers. This section is the canonical hub for armor and storage gear design — specs, handling, balance, progression, and master databases.

This is distinct from [**Inventory & Gear**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Inventory_System/README.md) (Inventory\_System), which covers the general inventory system: grid mechanics, paper doll, looting flow, and future container types (stash, vehicle inventory, crate inventory). Gears = _what the Operator wears/carries_. Inventory\_System = _how inventory works overall_.

## Design Pillars

* **Protection Has Weight** — Better armor costs mobility; every class has a movement and ergonomics penalty.
* **Tactical Ergonomics** — Where items are stored (rig vs backpack) determines hotkey access and reload capability.
* **Visual Readability** — In top-down view, armor tier and silhouette must be readable at combat distance.

## Documentation Tree

| Section                                                                                                              | Description                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Gear Tier System](gear_tier_system/index.html)                                                                              | Canonical Gear Tier for Armor (1–5) and Storage (1–4). Progression = Tier + Rarity + player/trader level; no item level. Used for loot, craft, economy, UI.                    |
| [Armor Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/ArmorGear/README.md)     | Body armor, helmets, face shields, headsets: classes, zones, materials, penetration, blunt damage, ricochet. Master database, handling, balance, progression, visual identity. |
| [Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) | Tactical rigs, backpacks, secure containers, stash-only cases: grid layouts, reload rule, flat storage and backpack collapse, balance, stash progression.                      |

## Related Sections

* [**Inventory & Gear**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Inventory_System/README.md) — Grid system, paper doll, equipment slots, encumbrance overview, looting UX.
* [**Gameplay — Gear Mechanics**](../gameplay/gear_mechanics/index.html) — How gear affects raid: weight tiers, inertia, rig/backpack gameplay, loadout philosophy.
* [**Gameplay — Looting & Inventory**](../gameplay/looting_interactions/index.html) — Container interaction flow, search times, grid dimensions.
* [**Weapons — Caliber & Ballistics**](../weapons/caliber_ballistics_system/index.html) — Penetration vs armor class, blunt damage formula, armor degradation.
