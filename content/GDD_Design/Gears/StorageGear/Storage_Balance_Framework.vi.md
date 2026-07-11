---
title: "Storage Balance Framework"
type: docs
weight: 4
---

## Tổng Quan

Tài liệu này định nghĩa **capacity vs mobility** trade-offs, **chi phí per slot**, **balance levers**, và **giá trị-per-slot meta** for storage gear. For item list Xem [Storage Master Database](storage_master_database/index.html); for progression Xem [Stash & Container Progression](stash_container_progression/index.html).

---

## Capacity vs Mobility matrix

*Capacity = sum of all subgrid cells; subgrid layout affects tactics (hotkey zones), not total capacity for balance.*

| Storage type | Total capacity (cells) | Weight (empty) | Speed penalty | Noise | Cells per kg | chi phí per cell (example) |
| :----------- | :--------------------: | :-------------: | :------------: | :---: | :----------: | :---------------------: |
| Light Rig | 6 | 0.4 kg | 0% | None | 15.0 | ~833 |
| Heavy Rig | 12 | 0.8 kg | 0% | None | 15.0 | ~2,083 |
| Small BP | 9 | 0.5 kg | 0% | None | 18.0 | ~444 |
| Medium BP | 16 | 1.0 kg | −2% | 8 m | 16.0 | ~625 |
| Large BP | 25 | 2.0 kg | −5% | 12 m | 12.5 | ~880 |
| Raid Pack | 30 | 2.5 kg | −8% | 15 m | 12.0 | ~1,333 |

Rigs add no speed penalty by themselves nhưng add weight (và thus contribute to weight tier in [Gear cơ chế](../../gameplay/gear_mechanics/index.html)). Backpacks add both weight và a direct speed penalty và noise radius.

---

## Balance Levers

khi tuning storage in patches:

1. **Total capacity (cells)** — Main dial for capacity (e.g. Heavy Rig 12 → 14 cells). One cell = one slot for balance formulas (chi phí per slot = chi phí ÷ total cells).
2. **Subgrid layout** — Number và size of subgrids is a separate lever: many small subgrids = more tactical choices (e.g. mag pouch vs main) nhưng harder to fit large items; one large subgrid = easier packing, less tactical depth.
3. **Weight (empty)** — Affects khi người chơi enters next weight tier (Light/Medium/Heavy/Critical).
4. **Speed penalty** — Direct movement chi phí for backpacks.
5. **Noise radius** — Stealth chi phí; larger bags audible from farther.
6. **Collapsed size** — Affects stash efficiency và space khi storing extra backpacks as items; smaller collapsed = more attractive for “bring extra bag” play.
7. **giá** — Economic gating; higher chi phí delays access.

---

## giá trị-per-Cell Meta

- **Rig cells** are more valuable than **backpack cells** (per cell) vì they have hotkey access và are the reload source. One cell in the rig is worth more than one cell in the backpack for combat flow.
- **Backpacks** provide raw loot capacity; trade-off is mobility (speed penalty, noise) và no hotkey.
- Design mục tiêu: “Rig for combat (mags, meds, nades); backpack for loot.” Both should feel meaningful — rig total capacity limits sustain, backpack total capacity limits haul. giá trị per slot = giá ÷ total capacity (cells).

---

## Tham Chiếu Chéo

- [Storage Master Database](storage_master_database/index.html) — Per-item total capacity (cells), subgrids, weight, chi phí.
- [Gear cơ chế](../../gameplay/gear_mechanics/index.html) — Weight tiers, rig vs backpack access times.
- [Stash & Container Progression](stash_container_progression/index.html) — Unlock order, stash size.
