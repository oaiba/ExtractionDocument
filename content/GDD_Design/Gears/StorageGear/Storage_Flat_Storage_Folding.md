---
title: "Storage: Flat Storage & Folding"
type: docs
weight: 3
---

## Overview

This document defines **flat storage** (no bag-in-bag), **backpack collapse** when empty, and how weapons with attachments are stored. For item list see [Storage Master Database](storage_master_database/index.html).

---

## Flat Storage (No Nesting)

There is **no bag-in-bag (nesting) logic**. When a bag, chest rig, armor gear, weapon, or attachment is placed inside another container (e.g. a backpack), it is treated as a **normal item**: it occupies only its own **footprint (W×H)** in cells. There is no "container inside container"; the contents of that item are not considered for placement, and the player does not open a nested grid.

- **One Storage Gear = one Storage.** Each Storage Gear (backpack, tactical rig, secure container, etc.) has a **single Storage**. Every item placed in that Storage is **at the same level** (flat); there are no nested containers. Putting a bag, rig, armor, or weapon "into" a backpack simply places that item as a normal grid item in the backpack's Storage.
- **Player inventory** holds **multiple Storage Gears** (e.g. tactical rig + backpack + secure container). Each has its own Storage; items are not nested across Storage Gears.
- **Placement** only requires that the item **fits** by footprint (W×H) in the Storage grid. There are no depth limits, same-ID chain rules, or "total = footprint + contents of child" checks.

Design intent: simpler UX, no infinite-space exploits, clearer balance (capacity = one flat grid per Storage Gear).

---

## Backpack Collapse

**Empty** backpacks can be **collapsed** to a smaller grid size (footprint) for storage in stash or when placed as an item in another container's Storage. **Capacity (total cells) is unchanged** when collapsed — only the footprint (W×H when placed in stash or as an item in a container) is reduced. Collapse/uncollapse has a short animation (e.g. 0.5–1.0 s). When the backpack contains any item, it must be in full (deployed) size.

| Backpack (example) | Full size | Collapsed size | Collapse time |
| :----------------- | :-------: | :------------: | :-----------: |
| Sling Bag | 2×3 | 1×2 | 0.5 s |
| Small | 3×3 | 2×2 | 0.5 s |
| Medium | 4×4 | 3×2 | 0.8 s |
| Large | 5×5 | 3×3 | 1.0 s |
| Raid Pack | 5×6 | 4×3 | 1.0 s |

Design intent: reward bringing an extra empty bag to fill with loot; collapsed bags take less space when stashing or when placed as an item in a container.

---

## Weapon and Item Grid Size

Weapons are always in their **default state** in inventory. **Weapon grid size (W×H)** is **fixed per weapon type** (e.g. M4A1 always 5×2). Adding or removing **attachments** does **not** change a weapon's inventory size — the weapon always uses its default cell dimensions. When a weapon (with or without attachments) is **stored in a backpack** (or any Storage), it **keeps all attachments** and its **size remains unchanged** (the default W×H for that weapon type). For item size tables see [Inventory & Gear — Grid System](../../inventory_system/_index/index.html) and [Weapon Arsenal](../../gameplay/weaponarsenal/index.html).

---

## Cross-References

- [Storage Master Database](storage_master_database/index.html) — Backpack list, collapsed sizes, flat storage.
- [Inventory & Gear — Grid System](../../inventory_system/_index/index.html) — Grid overview, item dimensions.
- [Weapon Progression & Mastery](../../weapons/weapon_progression_mastery/index.html) — Weapon list.
