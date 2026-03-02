---
title: "Storage Nesting & Folding"
type: docs
weight: 3
---

## Overview

This document defines **bag-in-bag (nesting)** rules and **backpack collapse** when empty. For item list see [Storage Master Database](Storage_Master_Database.md).

---

## Bag-in-Bag (Nesting) Rules

| Rule | Description |
| :--- | :---------- |
| **Size check** | **Total size** required in the parent = **(child container's footprint in cells)** + **(sum of cells of every item currently inside the child)**. Placement is allowed only if this total does not exceed the parent's **free capacity** (remaining empty cells). If it does not fit, placement is blocked. |
| **Same-ID block** | Cannot nest a container that has the same template ID as another container already in the same nesting chain (prevents infinite space exploit). |
| **Depth limit** | Maximum 2 levels: bag inside bag. “Bag in bag in bag” is blocked. |
| **Weight passthrough** | All items inside nested containers count toward total carried weight. |
| **In-raid nesting** | Players can place a found backpack inside their equipped backpack during raid, subject to the rules above. |
| **Container type** | Only **backpacks** can be nested. Tactical rigs, secure containers, and stash-only cases cannot be placed inside other containers (or only in stash as per design). |

**Footprint** = number of cells the child container occupies when placed as an item (e.g. Sling 2×3 = 6 cells). See [Storage Master Database](Storage_Master_Database.md) for grid sizes.

**Example:** Parent has 20 free cells. Child backpack has footprint 6 cells and contains items totaling 10 cells → total 16 cells ≤ 20 → placement allowed. If child contained 15 cells of items → 6 + 15 = 21 > 20 → placement blocked.

---

## Backpack Collapse

**Empty** backpacks can be **collapsed** to a smaller grid size (footprint) for storage or nesting. **Capacity (total cells) is unchanged** when collapsed — only the footprint (W×H when placed in stash or inside another bag) is reduced. Collapse/uncollapse has a short animation (e.g. 0.5–1.0 s). When the backpack contains any item, it must be in full (deployed) size.

| Backpack (example) | Full size | Collapsed size | Collapse time |
| :----------------- | :-------: | :------------: | :-----------: |
| Sling Bag | 2×3 | 1×2 | 0.5 s |
| Small | 3×3 | 2×2 | 0.5 s |
| Medium | 4×4 | 3×2 | 0.8 s |
| Large | 5×5 | 3×3 | 1.0 s |
| Raid Pack | 5×6 | 4×3 | 1.0 s |

Design intent: reward bringing an extra empty bag to fill with loot; collapsed bags take less space when stashing or when placing inside another bag.

---

## Weapon and Item Grid Size

Weapons are always in their **default state** in inventory. **Weapon grid size (W×H)** is **fixed per weapon type** (e.g. M4A1 always 5×2). Adding or removing **attachments** does **not** change a weapon's inventory size — the weapon always uses its default cell dimensions. For item size tables see [Inventory & Gear — Grid System](../../Inventory_Gear/_index.md) and [Weapon Arsenal](../../Gameplay/WeaponArsenal.md).

---

## Cross-References

- [Storage Master Database](Storage_Master_Database.md) — Backpack list, collapsed sizes.
- [Inventory & Gear — Grid System](../../Inventory_Gear/_index.md) — Grid overview, item dimensions.
- [Weapon Progression & Mastery](../../Weapons/Weapon_Progression_Mastery.md) — Weapon list.
