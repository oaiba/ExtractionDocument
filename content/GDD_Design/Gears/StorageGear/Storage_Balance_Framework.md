---
title: "Storage Balance Framework"
type: docs
weight: 4
---

## Overview

This document defines **capacity vs mobility** trade-offs, **cost per slot**, **balance levers**, and **value-per-slot meta** for storage gear. For item list see [Storage Master Database](Storage_Master_Database.md); for progression see [Stash & Container Progression](Stash_Container_Progression.md).

---

## Capacity vs Mobility Matrix

| Storage type | Slots | Weight (empty) | Speed penalty | Noise | Slots per kg | Cost per slot (example) |
| :----------- | :---: | :-------------: | :------------: | :---: | :----------: | :---------------------: |
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

1. **Slot count** — Main dial for capacity (e.g. Heavy Rig 12 → 14).
2. **Weight (empty)** — Affects when player enters next weight tier (Light/Medium/Heavy/Critical).
3. **Speed penalty** — Direct movement cost for backpacks.
4. **Noise radius** — Stealth cost; larger bags audible from farther.
5. **Collapsed size** — Affects nesting and stash efficiency; smaller collapsed = more attractive for “bring extra bag” play.
6. **Price** — Economic gating; higher cost delays access.

---

## Value-per-Slot Meta

- **Rig slots** are more valuable than **backpack slots** per cell because they have hotkey access and are the reload source. A “slot” in the rig is worth more than a slot in the backpack for combat flow.
- **Backpacks** provide raw loot capacity; trade-off is mobility (speed penalty, noise) and no hotkey.
- Design goal: “Rig for combat (mags, meds, nades); backpack for loot.” Both should feel meaningful — rig size limits sustain, backpack size limits haul.

---

## Cross-References

- [Storage Master Database](Storage_Master_Database.md) — Per-item slots, weight, cost.
- [Gear Mechanics](../../Gameplay/Gear_Mechanics.md) — Weight tiers, rig vs backpack access times.
- [Stash & Container Progression](Stash_Container_Progression.md) — Unlock order, stash size.
