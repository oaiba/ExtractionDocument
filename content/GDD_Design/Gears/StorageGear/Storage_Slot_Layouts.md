---
title: "Storage Slot Layouts"
type: docs
weight: 2
---

## Overview

This document defines **per-rig grid layouts**, the **reload-from-rig rule**, **hotkey mapping** (PC and mobile), and **secure container** access. Full item list: [Storage Master Database](Storage_Master_Database.md).

---

## Reload Rule

**Magazines can only be loaded into the weapon from the Tactical Rig or Pockets.** Magazines stored in the Backpack or Secure Container are not available for the reload key (e.g. R); the player must open the inventory screen, drag a magazine from backpack to rig (or weapon), then close inventory — a 1.0+ second vulnerable window. This rewards putting mags in the rig and punishes “mags only in backpack” loadouts.

---

## Rig Slot Layouts (Examples)

Layouts define which cells are 1×1, 1×2, 2×2, or 1×3. Hotkey slots are assigned in order (e.g. left-to-right, top-to-bottom) up to the rig’s hotkey count.

### Standard Rig (3×3, 9 slots)

```
+---+---+---+
|1x1|1x1|1x1|   Row 1: grenades, loose ammo, meds
+---+---+---+
|  1x2  |1x1|   Row 2: magazine + med/painkiller
+---+---+---+
|  1x2  |1x1|   Row 3: magazine + utility
+---+---+---+
Hotkey: typically slots 1–4 = first four eligible cells (e.g. top row + first 1×2)
```

### Heavy Rig (3×4, 12 slots)

```
+---+---+---+---+
|1x1|1x1|1x1|1x1|
+---+---+---+---+
|  1x2  |  1x2  |
+---+---+---+---+
|  1x2  |1x1|1x1|
+---+---+---+---+
Hotkey: 6 slots — e.g. top row (4) + first two 1×2 (2)
```

Exact layout per rig (Chest Harness, Light, Recon, Assault, Heavy, Blackrock, each armored rig) should be defined in data/design docs; the above illustrates the pattern. Slot type (1×1, 1×2, 2×2, 1×3) determines what items can be placed (e.g. 1×2 = standard mags, 2×2 = drum mag or large med).

---

## Hotkey Mapping

| Slot position | Hotkey (PC example) | Mobile | Max item size | Best use |
| :------------ | :------------------: | :----: | :-----------: | :------- |
| Rig slot 1 | 4 | Quick slot 1 | 1×1 | Grenade |
| Rig slot 2 | 5 | Quick slot 2 | 1×2 | Med |
| Rig slot 3 | 6 | Quick slot 3 | 1×2 | Magazine |
| Rig slots 4–6 | 7–9 or 0 | Quick slots 4–6 | per cell | Mags, meds, nades |
| Pockets 1–4 | 7–0 (configurable) | Quick slots 7+ | 1×1 | Keys, pills, cash |

Number of hotkey slots depends on the rig (see [Storage Master Database](Storage_Master_Database.md)). Same cooldown/animation on PC and mobile for parity.

---

## Secure Container Access

- **No hotkey** — Secure container is accessed only by opening the inventory and dragging items in/out.
- **Access time** — Same as opening inventory + drag + close (~1.0+ s); not usable as “quick use” in combat.
- **Restrictions** — In-raid: cannot place weapons, thermal scopes, NVG, or armor/helmets into the secure container. Can place keys, ammo, meds, valuables. Can always remove. See [Storage Master Database — Secure container restrictions](Storage_Master_Database.md#secure-container-restrictions).

---

## Cross-References

- [Storage Master Database](Storage_Master_Database.md) — Rig list, slot counts, hotkey slots.
- [Gear Mechanics](../../Gameplay/Gear_Mechanics.md) — Quick-access vs grid-access table, access times.
- [Looting & Inventory](../../Gameplay/Looting_Interactions.md) — Grid dimensions, container interaction flow.
