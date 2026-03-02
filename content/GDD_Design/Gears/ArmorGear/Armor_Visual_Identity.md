---
title: "Armor Visual Identity"
type: docs
weight: 6
---

## Overview

This document defines **top-down silhouette**, **rarity color-coding**, **damage state visuals**, and **UI icons** for armor so that class and condition are readable in a top-down extraction shooter. For class and item list see [Armor & Ballistics](Armor.md) and [Armor Master Database](Armor_Master_Database.md).

---

## Top-Down Silhouette Guide

In top-down view, armor must be readable from above. Differentiation is achieved via shoulder profile, color hint, and helmet shape.

| Armor class | Shoulder profile | Color hint | Helmet shape | Readability distance |
| :---------- | :--------------- | :--------- | :----------- | :------------------- |
| None | Slim, fabric | Neutral | None | N/A |
| Class 1–2 | Slim, slight pad | Light tan | Open bowl | ~3 tiles |
| Class 3 | Medium, plates | Olive / gray | Covered ears | ~4 tiles |
| Class 4 | Medium+, carrier | Dark green | Military | ~5 tiles |
| Class 5 | Wide, full plate | Dark gray | Full + visor | ~6 tiles |
| Class 6 | Very wide, tank | Black / dark | Enclosed | ~7 tiles |

**Design intent:** At combat range, players can estimate threat level (armor tier) and choose engagement or reposition. Heavier armor is visually “bigger” and darker.

---

## Rarity Color-Coding

- **Ground loot:** Rarity shown by **outline glow** (e.g. White / Green / Blue / Purple / Orange) so players can prioritize without opening inventory.
- **Equipped:** No glow — equipped armor is read by **silhouette and color hint** only, to avoid clutter and keep identification skill-based.

Rarity palette should match the rest of the game (e.g. Common = white, Uncommon = green, Rare = blue, Epic = purple, Legendary = orange).

---

## Damage State Visual

Armor condition (durability %) should be visible on the character and in UI.

| Durability band | Visual on character | Notes |
| :-------------- | :------------------ | :---- |
| 100–75% | Clean | No damage cues |
| 74–50% | Scuff marks, slight discoloration | Clearly used |
| 49–25% | Visible cracks/tears, darker | Clearly damaged |
| 24–0% | Heavy damage, red/dark overlay | Near-destroyed |

Helmets: visor cracks at low durability can obscure vision (see [Armor & Ballistics](Armor.md) — visors). Vests: torn fabric or plate damage on the model.

---

## UI Icons

- **Inventory icon:** 2D icon with clear outline, **class number badge** (1–6), and **durability bar** (e.g. green → yellow → red).
- **Tooltip:** Full stat preview — class, zones, current/max durability, material, weight, value. Optional: “Effective class” when durability is below 100% (e.g. “~Class 3.5” at 70% durability).

Icons should be consistent in size and style with weapons and other gear; class badge ensures quick scan in stash and loot screens.

---

## Cross-References

- [Armor Master Database](Armor_Master_Database.md) — Per-item class, weight, rarity.
- [Weapon Visual & Audio Identity](../../Weapons/Weapon_Visual_Audio_Identity.md) — Rarity and readability standards (align with weapons).
- [Visuals — Style Guide](../../Visuals/StyleGuide.md) — Color and UI consistency if present.
