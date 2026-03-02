---
title: "Weapon Balance Framework"
type: docs
weight: 3
---

## Overview

This document defines how weapon balance is measured, tuned, and maintained: DPS and TTK math, cost-efficiency, balance levers, patch process, meta health metrics, and seasonal rotation. Design reference: Helldivers 2 faction-specific effectiveness, Delta Force seasonal TTK rebalancing.

> **Cross-References:** [Weapon Arsenal](../Gameplay/WeaponArsenal.md) — base stats; [Caliber & Ballistics System](Caliber_Ballistics_System.md) — penetration and damage application; [Inventory & Gear — Armor](../Inventory_Gear/Armor.md) — armor classes 1–6.

---

## DPS Calculations

**Formula:** `DPS = (Damage × RPM) / 60`

Damage is per-shot base damage (before armor). RPM is rounds per minute. Shotguns use total damage per shot (pellet × pellets) and effective RPM.

### Primary Weapons — DPS Reference (Base)

| Weapon | Damage | RPM | DPS | Class |
| :------ | :----: | :-: | :-: | :---- |
| AK-47 | 35 | 600 | 350 | AR |
| M4A1 | 32 | 750 | 400 | AR |
| SCAR-H | 40 | 625 | 417 | AR |
| HK416 | 34 | 850 | 482 | AR |
| MP5 | 24 | 900 | 360 | SMG |
| Vector .45 | 28 | 1100 | 513 | SMG |
| P90 | 22 | 1000 | 367 | SMG |
| Remington 870 | 160 (8×20) | 60 | 160 (burst) | Shotgun |
| AA-12 | 144 (8×18) | 300 | 720 | Shotgun |
| M24 | 85 | 50 | 71 | Sniper |
| AWP | 120 | 40 | 80 | Sniper |
| M249 | 32 | 750 | 400 | LMG |
| PKM | 38 | 650 | 412 | LMG |
| MG42 | 35 | 1200 | 700 | LMG |

*DMR and pistol DPS are lower by design (semi-auto or backup role).*

**Design intent:** DPS alone does not define strength. Range, recoil, penetration, and cost matter. This table supports comparison within and across classes.

---

## TTK Matrix vs Armor Class

TTK = time to kill (100 HP target). Armor classes 1–6 from [Armor](../Inventory_Gear/Armor.md). Shots to kill depend on penetration and body part; below assumes chest, no penetration failure.

**Simplified TTK (seconds) — Chest, 100 HP + Armor**

| Weapon Type | Armor 1 | Armor 2 | Armor 3 | Armor 4 | Armor 5 | Armor 6 |
| :---------- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| SMG (FMJ) | 0.25 | 0.35 | 0.50 | 0.80+ | 1.0+ | 1.2+ |
| AR (FMJ) | 0.30 | 0.40 | 0.45 | 0.55 | 0.75+ | 1.0+ |
| AR (AP) | 0.35 | 0.40 | 0.45 | 0.50 | 0.55 | 0.65 |
| Shotgun (Buck) | 0.15 | 0.20 | 0.25 | 0.40+ | — | — |
| Sniper (Std) | 0 | 0 | 0 | 0 | 0 | 0–1 |
| LMG (FMJ) | 0.40 | 0.50 | 0.55 | 0.70+ | 0.90+ | 1.1+ |
| Pistol | 0.55 | 0.70 | 0.90+ | 1.2+ | — | — |

*0 = one-shot kill. "+" = marginal or requires many shots / AP ammo.*

Full TTK depends on [Caliber & Ballistics System](Caliber_Ballistics_System.md) penetration chance and damage falloff. This matrix is for high-level balance targets.

---

## Cost-Efficiency Index

**Formula:** `Cost-Efficiency = DPS / Weapon Cost (in thousands)`

Higher index = more damage per credit. Identifies value picks and premium options.

| Weapon | DPS | Cost ($) | Cost-Efficiency |
| :------ | :-: | :------: | :-------------: |
| AK-47 | 350 | 1,200 | 0.29 |
| M4A1 | 400 | 3,500 | 0.11 |
| MP5 | 360 | 800 | 0.45 |
| Glock 19 | ~170 | 300 | 0.57 |
| Remington 870 | 160 | 600 | 0.27 |
| HK416 | 482 | 6,500 | 0.07 |
| AWP | 80 | 16,000 | 0.005 |

**Design intent:** Common weapons score higher on cost-efficiency; rare weapons offer niche power (range, penetration, capacity) rather than raw value. Prevents "best gun" from being the most expensive in every situation.

---

## Rarity-Power Curve

Rarity should correlate with **niche power** and **flexibility**, not universal dominance.

| Rarity | Expected Power Profile | Balance Rule |
| :----- | :--------------------- | :----------- |
| Common | Strong in one niche (e.g. CQB, budget) | Can compete in optimal range |
| Uncommon | Broader effectiveness, still trade-offs | No clear "always pick" |
| Rare | Multiple strengths, higher ceiling | Weak in at least one band (e.g. CQB or range) |
| Epic | Peak in category or unique trait | Clear counterplay (cost, mobility, ammo) |
| Legendary | Prestige + small stat bump | Never mandatory for win rate |

**Validation:** No weapon should have >55% pick rate in ranked/competitive over a full season. No weapon should have <2% pick rate in its intended category unless intentionally niche.

---

## Balance Levers

Which stats to adjust per archetype when tuning:

| Archetype | Primary Levers | Secondary Levers | Avoid |
| :-------- | :------------- | :--------------- | :---- |
| AR | Damage, RPM, recoil recovery | Mag size, ADS time | Making one AR best at everything |
| SMG | Damage falloff, hip spread, RPM | Mag size, mobility | Buffing range into AR territory |
| Shotgun | Pellet count, spread, damage per pellet | Fire rate, capacity | One-shot at 15 m+ |
| Sniper | Damage, bullet velocity, scope-in time | Mag size, sway | Fast follow-up rivaling DMR |
| LMG | Recoil (sustained), mobility penalty, reload time | Damage, mag size | Making LMG mobile |
| DMR | Damage, semi-auto RPM cap, sway | Mag size, ADS | Overlapping sniper one-shot |
| Pistol | Damage, draw time, mag size | — | Making pistol primary-viable |

---

## Patch Balance Process

1. **Data collection (2+ weeks):** Pick rate, win rate delta, average TTK by weapon, death attribution, usage by map/phase.
2. **Internal playtest:** Proposed changes in closed build; focus on feel and outlier weapons.
3. **Community beta (optional):** Balance patch on PTR or limited rollout; collect feedback.
4. **Release:** Patch notes with rationale; monitor same metrics for 1–2 weeks post-patch.
5. **Hotfix criteria:** If a single weapon exceeds 60% pick rate or +8% win rate delta, expedite hotfix.

---

## Meta Health Metrics

KPIs for weapon balance (targets per season):

| Metric | Target | Action if Missed |
| :------ | :----- | :---------------- |
| Max single-weapon pick rate | < 55% | Nerf or buff alternatives |
| Min category representation | Each category ≥ 5% picks | Buff underused category or add incentives |
| Win rate delta (weapon) | No weapon > +5% vs average | Reduce overperformer effectiveness |
| TTK spread (within class) | No weapon 2× faster TTK than same-class median | Tighten damage/RPM spread |
| Cost-efficiency spread | Top value pick not > 3× bottom in same class | Adjust cost or base stats |

---

## Seasonal Rotation Framework

Weapon availability and emphasis shift per season to refresh meta:

| Levers | Description |
| :----- | :----------- |
| **Loot table weights** | Increase drop rate of underused weapons in high-tier zones |
| **Quest/BP rewards** | Feature specific weapons or attachments in battle pass |
| **Nerf/buff cycle** | 2–4 weapons tuned per season; document in patch notes |
| **Limited-time modes** | Modes that restrict or boost certain categories (e.g. "Pistol Only" week) |
| **New weapons** | 1–2 new weapons per season, preferably in underused category |

Rotation does not remove base weapons from the game; it changes their visibility and opportunity cost.

---

## Cross-References

- [Weapon Arsenal](../Gameplay/WeaponArsenal.md) — Base damage, RPM, cost.
- [Caliber & Ballistics System](Caliber_Ballistics_System.md) — Penetration, falloff, armor interaction.
- [Inventory & Gear — Armor](../Inventory_Gear/Armor.md) — Armor classes 1–6.
- [Weapon Categories Deep Dive](Weapon_Categories_Deep_Dive.md) — Role per genre.
