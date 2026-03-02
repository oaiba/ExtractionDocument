---
title: "Storage Nesting & Folding"
type: docs
weight: 3
---

## Overview

This document defines **bag-in-bag (nesting)** rules, **weapon folding** (grid size and penalties when fired folded), and **backpack collapse** when empty. For item list see [Storage Master Database](Storage_Master_Database.md).

---

## Bag-in-Bag (Nesting) Rules

| Rule | Description |
| :--- | :---------- |
| **Size check (capacity)** | Inner container's **total capacity** (sum of all subgrid cells) must be ≤ 60% of outer container's **total capacity**. Total capacity is the primary number; see [Storage Master Database](Storage_Master_Database.md). |
| **Physical fit (optional)** | Optionally, inner must also physically fit in the outer grid: e.g. inner's largest subgrid (or bounding box) W×H fits inside **one** of the outer's subgrids (outer subgrid with W ≥ inner W, H ≥ inner H). If not used, only the capacity check above applies. |
| **Same-ID block** | Cannot nest a container that has the same template ID as another container already in the same nesting chain (prevents infinite space exploit). |
| **Depth limit** | Maximum 2 levels: bag inside bag. “Bag in bag in bag” is blocked. |
| **Weight passthrough** | All items inside nested containers count toward total carried weight. |
| **In-raid nesting** | Players can place a found backpack inside their equipped backpack during raid, subject to the rules above. |
| **Container type** | Only **backpacks** can be nested. Tactical rigs, secure containers, and stash-only cases cannot be placed inside other containers (or only in stash as per design). |

**Examples:** Berkut (4×5) inside Pilgrim (6×7) = legal. Same-sized or same-ID bag inside same bag = blocked. Nested backpacks on extract = valid strategy for extra loot capacity.

---

## Weapon Folding

Some weapons have **foldable stocks**. When folded, grid size is reduced (e.g. one fewer column). Folding/unfolding takes time.

| Weapon (example) | Foldable | Base size | Folded size | Fold time | Unfold time |
| :--------------- | :------: | :-------: | :---------: | :-------: | :---------: |
| AK-74M | Yes (stock) | 5×2 | 4×2 | 1.0 s | 1.5 s |
| MP5A3 | Yes (stock) | 3×2 | 2×2 | 0.8 s | 1.2 s |
| M4A1 | No (fixed) | 5×2 | 5×2 | — | — |

**Penalties when firing weapon folded:** +300% vertical recoil, −80% ergonomics, no ADS (hipfire only). Folding is for transport and stash space, not combat.

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

## Cross-References

- [Storage Master Database](Storage_Master_Database.md) — Backpack list, collapsed sizes.
- [Inventory & Gear — Grid System](../../Inventory_Gear/_index.md) — Grid overview, item dimensions.
- [Weapon Progression & Mastery](../../Weapons/Weapon_Progression_Mastery.md) — Weapon list; foldable weapons are a subset.
