---
title: "Storage Slot Layouts"
type: docs
weight: 2
---

## Tổng Quan

Tài liệu này định nghĩa **per-rig grid layouts**, the **reload-from-rig rule**, **hotkey mapping** (PC và mobile), và **secure container** access. Full item list: [Storage Master Database](Storage_Master_Database.md).

---

## Subgrid & Placement Rules

A container is made of **one hoặc more subgrids**. Each subgrid has dimensions (W×H) và optional **slot-type constraints** (e.g. 1×1 only, hoặc allows 1×2, 2×2).

- **Placement:** An item can be placed only nếu it **fits in at least one subgrid** — i.e. the item’s width và height do not exceed that subgrid’s W và H, và the subgrid’s slot-type rules allow that item size (e.g. 1×2 mag in a subgrid that allows 1×2).
- **Hotkey:** Hotkeys are assigned only to cells in **quick-access subgrids** (e.g. rig: mag pouch và utility subgrids = hotkey; main compartment may have no hotkey hoặc hotkey in a second row). Which subgrids are “quick access” is per container in [Storage Master Database](Storage_Master_Database.md).

---

## Reload Rule

**Magazines can only be loaded into the vũ khí from the Tactical Rig hoặc Pockets.** Magazines stored in the Backpack hoặc Secure Container are not available for the reload chính (e.g. R); the người chơi must open the inventory màn hình, drag a magazine from backpack to rig (hoặc vũ khí), then close inventory — a 1.0+ second vulnerable window. This rewards putting mags in the rig và punishes “mags only in backpack” loadouts.

*Optional design:* Reload may be restricted to magazines in a **quick-access (Mag Pouch) subgrid** only; nếu so, mags in other rig subgrids would require opening inventory to reload. hiện tại baseline: reload from **any cell in the rig** for simplicity.

---

## Rig Slot Layouts (Examples)

Layouts are defined by **subgrids**; each subgrid has W×H và optional slot-type (1×1, 1×2, 2×2, 1×3). **Total capacity = sum of all subgrid cells.** Hotkey slots map to quick-access subgrids (Xem [Storage Master Database](Storage_Master_Database.md)).

### Standard Rig — Total capacity 9 cells

Subgrid A (Main): 3×2 = 6 cells. Subgrid B (Mag): 1×3 = 3 cells.

```
Subgrid A (Main, 3×2):          Subgrid B (Mag, 1×3):
+---+---+---+                   +---+
|1x1|1x1|1x1|  hotkey 1–3       |1x2|
+---+---+---+                   +---+
|  1x2  |1x1|  hotkey 4         |1x2|  hotkey
+---+---+---+                   +---+
                                |1x1|
                                +---+
```

**Total capacity = 9 cells.** Hotkey typically maps to Subgrid A (4 slots) và Subgrid B (mag slots). Mags in Subgrid B = quick reload.

### Heavy Rig — Total capacity 12 cells

Single subgrid (Main) 3×4 = 12 cells; all cells can be hotkey-eligible (6 hotkey slots).

```
+---+---+---+---+
|1x1|1x1|1x1|1x1|   Row 1
+---+---+---+---+
|  1x2  |  1x2  |   Row 2
+---+---+---+---+
|  1x2  |1x1|1x1|   Row 3
+---+---+---+---+
Hotkey: 6 slots — e.g. top row (4) + first two 1×2 (2)
```

**Total capacity = 12 cells.** Reload can be from any rig cell (hoặc, as a design option, restricted to a dedicated “Mag Pouch” subgrid khi the rig has one).

Exact layout per rig (Chest Harness, Light, Recon, Assault, Heavy, Blackrock, each armored rig) is in [Storage Master Database](Storage_Master_Database.md); the above illustrates the subgrid pattern. Slot type (1×1, 1×2, 2×2, 1×3) determines what items can be placed (e.g. 1×2 = standard mags, 2×2 = drum mag hoặc large med).

---

## Hotkey Mapping

| Slot position | Hotkey (PC example) | Mobile | Max item size | Best cách dùng |
| :------------ | :------------------: | :----: | :-----------: | :------- |
| Rig slot 1 | 4 | Quick slot 1 | 1×1 | Grenade |
| Rig slot 2 | 5 | Quick slot 2 | 1×2 | Med |
| Rig slot 3 | 6 | Quick slot 3 | 1×2 | Magazine |
| Rig slots 4–6 | 7–9 hoặc 0 | Quick slots 4–6 | per cell | Mags, meds, nades |
| Pockets 1–4 | 7–0 (configurable) | Quick slots 7+ | 1×1 | Keys, pills, cash |

Number of hotkey slots depends on the rig (Xem [Storage Master Database](Storage_Master_Database.md)). Same cooldown/animation on PC và mobile for parity.

---

## Secure Container Access

- **No hotkey** — Secure container is accessed only by opening the inventory và dragging items in/out.
- **Access thời gian** — Same as opening inventory + drag + close (~1.0+ s); not usable as “quick cách dùng” in combat.
- **Restrictions** — In-raid: cannot place vũ khí, thermal scopes, NVG, hoặc giáp/helmets into the secure container. Can place keys, đạn, meds, valuables. Can always remove. Xem [Storage Master Database — Secure container restrictions](Storage_Master_Database.md#secure-container-restrictions).

---

## Tham Chiếu Chéo

- [Storage Master Database](Storage_Master_Database.md) — Rig list, slot counts, hotkey slots.
- [Gear cơ chế](../../Gameplay/Gear_Mechanics.md) — Quick-access vs grid-access bảng, access times.
- [Looting & Inventory](../../Gameplay/Looting_Interactions.md) — Grid dimensions, container interaction flow.
