---
title: "Storage Balance Framework"
type: docs
weight: 4
---

## Overview

This document defines **capacity vs mobility** trade-offs, **cost per slot**, **balance levers**, and **value-per-slot meta** for storage gear. For item list see [Storage Master Database](Storage_Master_Database.md); for progression see [Stash & Container Progression](Stash_Container_Progression.md).

---

## Capacity vs Mobility Matrix

*Capacity = sum of all subgrid cells; subgrid layout affects tactics (hotkey zones), not total capacity for balance.*

| Storage type | Total capacity (cells) | Weight (empty) | Speed penalty | Noise | Cells per kg | Cost per cell (example) |
| :----------- | :--------------------: | :-------------: | :------------: | :---: | :----------: | :---------------------: |
| Light Rig | 6 | 0.4 kg | 0% | None | 15.0 | ~833 |
| Heavy Rig | 12 | 0.8 kg | 0% | None | 15.0 | ~2,083 |
| Small BP | 9 | 0.5 kg | 0% | None | 18.0 | ~444 |
| Medium BP | 16 | 1.0 kg | −2% | 8 m | 16.0 | ~625 |
| Large BP | 25 | 2.0 kg | −5% | 12 m | 12.5 | ~880 |
| Raid Pack | 30 | 2.5 kg | −8% | 15 m | 12.0 | ~1,333 |

Rigs add no speed penalty by themselves but add weight (and thus contribute to weight tier in [Gear Mechanics](../../Gameplay/Gear_Mechanics.md)). Backpacks add both weight and a direct speed penalty and noise radius.

---

## Balance Levers

When tuning storage in patches:

1. **Total capacity (cells)** — Main dial for capacity (e.g. Heavy Rig 12 → 14 cells). One cell = one slot for balance formulas (cost per slot = cost ÷ total cells).
2. **Subgrid layout** — Number and size of subgrids is a separate lever: many small subgrids = more tactical choices (e.g. mag pouch vs main) but harder to fit large items; one large subgrid = easier packing, less tactical depth.
3. **Weight (empty)** — Affects when player enters next weight tier (Light/Medium/Heavy/Critical).
4. **Speed penalty** — Direct movement cost for backpacks.
5. **Noise radius** — Stealth cost; larger bags audible from farther.
6. **Collapsed size** — Affects stash efficiency and space when storing extra backpacks as items; smaller collapsed = more attractive for “bring extra bag” play.
7. **Price** — Economic gating; higher cost delays access.

---

## Value-per-Cell Meta

- **Rig cells** are more valuable than **backpack cells** (per cell) because they have hotkey access and are the reload source. One cell in the rig is worth more than one cell in the backpack for combat flow.
- **Backpacks** provide raw loot capacity; trade-off is mobility (speed penalty, noise) and no hotkey.
- Design goal: “Rig for combat (mags, meds, nades); backpack for loot.” Both should feel meaningful — rig total capacity limits sustain, backpack total capacity limits haul. Value per slot = price ÷ total capacity (cells).

---

## Cross-References

- [Storage Master Database](Storage_Master_Database.md) — Per-item total capacity (cells), subgrids, weight, cost.
- [Gear Mechanics](../../Gameplay/Gear_Mechanics.md) — Weight tiers, rig vs backpack access times.
- [Stash & Container Progression](Stash_Container_Progression.md) — Unlock order, stash size.
