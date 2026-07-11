---
title: "Storage Slot Layouts"
type: docs
weight: 2
---

## Overview

This document defines **per-rig grid layouts**, the **reload-from-rig rule**, **hotkey mapping** (PC and mobile), and **secure container** access. Full item list: [Storage Master Database](storage_master_database/index.html).

---

## Subgrid & Placement Rules

A container is made of **one or more subgrids**. Each subgrid has dimensions (W×H) and optional **slot-type constraints** (e.g. 1×1 only, or allows 1×2, 2×2).

- **Placement:** An item can be placed only if it **fits in at least one subgrid** — i.e. the item’s width and height do not exceed that subgrid’s W and H, and the subgrid’s slot-type rules allow that item size (e.g. 1×2 mag in a subgrid that allows 1×2).
- **Hotkey:** Hotkeys are assigned only to cells in **quick-access subgrids** (e.g. rig: mag pouch and utility subgrids = hotkey; main compartment may have no hotkey or hotkey in a second row). Which subgrids are “quick access” is per container in [Storage Master Database](storage_master_database/index.html).

---

## Reload Rule

**Magazines can only be loaded into the weapon from the Tactical Rig or Pockets.** Magazines stored in the Backpack or Secure Container are not available for the reload key (e.g. R); the player must open the inventory screen, drag a magazine from backpack to rig (or weapon), then close inventory — a 1.0+ second vulnerable window. This rewards putting mags in the rig and punishes “mags only in backpack” loadouts.

*Optional design:* Reload may be restricted to magazines in a **quick-access (Mag Pouch) subgrid** only; if so, mags in other rig subgrids would require opening inventory to reload. Current baseline: reload from **any cell in the rig** for simplicity.

---

## Rig Slot Layouts (Examples)

Layouts are defined by **subgrids**; each subgrid has W×H and optional slot-type (1×1, 1×2, 2×2, 1×3). **Total capacity = sum of all subgrid cells.** Hotkey slots map to quick-access subgrids (see [Storage Master Database](storage_master_database/index.html)).

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

**Total capacity = 9 cells.** Hotkey typically maps to Subgrid A (4 slots) and Subgrid B (mag slots). Mags in Subgrid B = quick reload.

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

**Total capacity = 12 cells.** Reload can be from any rig cell (or, as a design option, restricted to a dedicated “Mag Pouch” subgrid when the rig has one).

Exact layout per rig (Chest Harness, Light, Recon, Assault, Heavy, Blackrock, each armored rig) is in [Storage Master Database](storage_master_database/index.html); the above illustrates the subgrid pattern. Slot type (1×1, 1×2, 2×2, 1×3) determines what items can be placed (e.g. 1×2 = standard mags, 2×2 = drum mag or large med).

---

## Hotkey Mapping

| Slot position | Hotkey (PC example) | Mobile | Max item size | Best use |
| :------------ | :------------------: | :----: | :-----------: | :------- |
| Rig slot 1 | 4 | Quick slot 1 | 1×1 | Grenade |
| Rig slot 2 | 5 | Quick slot 2 | 1×2 | Med |
| Rig slot 3 | 6 | Quick slot 3 | 1×2 | Magazine |
| Rig slots 4–6 | 7–9 or 0 | Quick slots 4–6 | per cell | Mags, meds, nades |
| Pockets 1–4 | 7–0 (configurable) | Quick slots 7+ | 1×1 | Keys, pills, cash |

Number of hotkey slots depends on the rig (see [Storage Master Database](storage_master_database/index.html)). Same cooldown/animation on PC and mobile for parity.

---

## Secure Container Access

- **No hotkey** — Secure container is accessed only by opening the inventory and dragging items in/out.
- **Access time** — Same as opening inventory + drag + close (~1.0+ s); not usable as “quick use” in combat.
- **Restrictions** — In-raid: cannot place weapons, thermal scopes, NVG, or armor/helmets into the secure container. Can place keys, ammo, meds, valuables. Can always remove. See [Storage Master Database — Secure container restrictions](Storage_Master_Database.md#secure-container-restrictions).

---

## Cross-References

- [Storage Master Database](storage_master_database/index.html) — Rig list, slot counts, hotkey slots.
- [Gear Mechanics](../../gameplay/gear_mechanics/index.html) — Quick-access vs grid-access table, access times.
- [Looting & Inventory](../../gameplay/looting_interactions/index.html) — Grid dimensions, container interaction flow.
