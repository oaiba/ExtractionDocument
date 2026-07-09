---
title: "Storage: Flat Storage & Folding"
type: docs
weight: 3
---

## Tổng Quan

Tài liệu này định nghĩa **flat storage** (no bag-in-bag), **backpack collapse** khi empty, và how vũ khí với attachments are stored. For item list Xem [Storage Master Database](Storage_Master_Database.md).

---

## Flat Storage (No Nesting)

There is **no bag-in-bag (nesting) logic**. khi a bag, chest rig, giáp gear, vũ khí, hoặc attachment is placed inside another container (e.g. a backpack), it is treated as a **normal item**: it occupies only its own **footprint (W×H)** in cells. There is no "container inside container"; the contents of that item are not considered for placement, và the người chơi does not open a nested grid.

- **One Storage Gear = one Storage.** Each Storage Gear (backpack, tactical rig, secure container, etc.) has a **single Storage**. Every item placed in that Storage is **at the same level** (flat); there are no nested containers. Putting a bag, rig, giáp, hoặc vũ khí "into" a backpack simply places that item as a normal grid item in the backpack's Storage.
- **người chơi inventory** holds **multiple Storage Gears** (e.g. tactical rig + backpack + secure container). Each has its own Storage; items are not nested across Storage Gears.
- **Placement** only requires that the item **fits** by footprint (W×H) in the Storage grid. There are no depth limits, same-ID chain rules, hoặc "total = footprint + contents of child" checks.

Design intent: simpler UX, no infinite-space exploits, clearer balance (capacity = one flat grid per Storage Gear).

---

## Backpack Collapse

**empty** backpacks can be **collapsed** to a smaller grid size (footprint) for storage in stash hoặc khi placed as an item in another container's Storage. **Capacity (total cells) is unchanged** khi collapsed — only the footprint (W×H khi placed in stash hoặc as an item in a container) is reduced. Collapse/uncollapse has a short animation (e.g. 0.5–1.0 s). khi the backpack contains any item, it phải được in full (deployed) size.

| Backpack (example) | Full size | Collapsed size | Collapse thời gian |
| :----------------- | :-------: | :------------: | :-----------: |
| Sling Bag | 2×3 | 1×2 | 0.5 s |
| Small | 3×3 | 2×2 | 0.5 s |
| Medium | 4×4 | 3×2 | 0.8 s |
| Large | 5×5 | 3×3 | 1.0 s |
| Raid Pack | 5×6 | 4×3 | 1.0 s |

Design intent: reward bringing an extra empty bag to fill với loot; collapsed bags take less space khi stashing hoặc khi placed as an item in a container.

---

## vũ khí và Item Grid Size

vũ khí are always in their **default trạng thái** in inventory. **vũ khí grid size (W×H)** is **fixed per vũ khí type** (e.g. M4A1 always 5×2). Adding hoặc removing **attachments** does **not** change a vũ khí's inventory size — the vũ khí always uses its default cell dimensions. khi a vũ khí (với hoặc mà không attachments) is **stored in a backpack** (hoặc any Storage), it **keeps all attachments** và its **size remains unchanged** (the default W×H for that vũ khí type). For item size tables Xem [Inventory & Gear — Grid hệ thống](../../Inventory_System/_index.md) và [vũ khí Arsenal](../../Gameplay/WeaponArsenal.md).

---

## Tham Chiếu Chéo

- [Storage Master Database](Storage_Master_Database.md) — Backpack list, collapsed sizes, flat storage.
- [Inventory & Gear — Grid hệ thống](../../Inventory_System/_index.md) — Grid overview, item dimensions.
- [vũ khí Progression & Mastery](../../vũ khí/Weapon_Progression_Mastery.md) — vũ khí list.
