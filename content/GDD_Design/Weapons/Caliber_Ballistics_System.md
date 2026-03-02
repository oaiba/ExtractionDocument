---
title: "Caliber & Ballistics System"
type: docs
weight: 4
---

## Overview

This document defines how bullets interact with armor, durability, distance, and materials: penetration chance, damage falloff, armor degradation, blunt damage, ricochet, and caliber sharing. Armor classes and zones are in [Armor & Ballistics](../Inventory_Gear/Armor.md).

> **Cross-References:** [Weapon Arsenal](../Gameplay/WeaponArsenal.md) — ammo tables by caliber; [Weapon Balance Framework](Weapon_Balance_Framework.md) — TTK and balance; [Inventory & Gear — Armor](../Inventory_Gear/Armor.md) — armor classes 1–6, zones, materials.

---

## Penetration Chance Formula

When a bullet hits an armored zone, the server resolves:

**Penetration Power (PP):** Each ammo type has a numeric penetration class (0–8) matching the ammo table in [Weapon Arsenal](../Gameplay/WeaponArsenal.md) (e.g. FMJ Low = 2, AP High = 5, .338 Ultimate = 7).

**Effective Armor Class (EAC):**  
`EAC = ArmorClass + (1 - DurabilityPercent) × 2`  
Durability is 0–1. At 100% durability, EAC = ArmorClass. At 50% durability, EAC = ArmorClass + 1. At 0%, armor is effectively bypassed for penetration (blunt still applies).

**Penetration Chance:**  
`PenChance = clamp( (PP - EAC + 2) / 4 , 0 , 1 )`  
- If PP ≥ EAC + 2: 100% penetrate.  
- If PP ≤ EAC - 2: 0% penetrate (block).  
- In between: linear interpolation (e.g. PP = EAC → 50% chance).

**On Penetration:** Damage is reduced by residual energy factor: `Damage × (0.6 + 0.2 × (PP - EAC))`, clamped to 60–100% of base damage. Armor takes durability damage (see Armor Degradation).

**On Block:** No health damage from the bullet; blunt damage still applies. Armor takes higher durability damage than on penetration.

---

## Damage Falloff Curves

Damage scales with distance. Below: multiplier applied to base damage (1.0 = no falloff). Distance is 2D horizontal range (top-down).

**Formula (per caliber family):**  
`Multiplier = 1.0` for `range ≤ effectiveRange`;  
`Multiplier = max(0.25, 1.0 - (range - effectiveRange) / falloffDistance)` for `range > effectiveRange`.

### Reference Falloff (Damage Multiplier by Distance)

| Caliber Family | Effective Range | Falloff Distance | 0 m | 20 m | 40 m | 60 m | 80 m | 100 m |
| :------------- | :-------------: | :---------------: | :-: | :--: | :--: | :--: | :--: | :---: |
| 9×19mm / .45 | 15 m | 25 m | 1.0 | 0.95 | 0.75 | 0.55 | 0.35 | 0.25 |
| 5.56 / 5.7 | 35 m | 50 m | 1.0 | 1.0 | 1.0 | 0.90 | 0.70 | 0.50 |
| 7.62×39 | 30 m | 45 m | 1.0 | 1.0 | 0.95 | 0.80 | 0.60 | 0.40 |
| 7.62×51 / 54R | 50 m | 70 m | 1.0 | 1.0 | 1.0 | 1.0 | 0.85 | 0.65 |
| .338 / .50 BMG | 80 m | 100 m | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.95 |
| 12 Gauge (Buckshot) | 8 m | 15 m | 1.0 | 0.70 | 0.40 | 0.25 | 0.25 | 0.25 |
| 12 Gauge (Slug) | 25 m | 40 m | 1.0 | 1.0 | 0.90 | 0.65 | 0.45 | 0.25 |

---

## Armor Degradation Math

Each hit to armor reduces its durability. Durability loss depends on penetration result and caliber.

**On Penetration:**  
`DurabilityLoss = BaseDmg × 0.015 × (1 + (EAC - PP))`  
Capped per hit (e.g. max 8% per shot). Higher penetration vs lower armor = less durability loss (bullet passes through "cleaner").

**On Block:**  
`DurabilityLoss = BaseDmg × 0.025 × (1 + (PP - EAC))`  
Capped per hit (e.g. max 12%). Stopped rounds dump more energy into the plate.

**Effective class reduction:** As durability drops, EAC increases (see Penetration Chance). At 50% durability, armor is treated as roughly one class worse; at 25%, two classes worse. At 0% the armor is destroyed (no protection; weight remains until dropped). See [Gear Mechanics](../Gameplay/Gear_Mechanics.md) for gameplay impact.

---

## Blunt Damage Formula

When a bullet is **blocked** by armor, the wearer still takes blunt trauma.

**Formula (from [Armor](../Inventory_Gear/Armor.md)):**  
`BluntDmg = BaseDmg × BluntFactor × (1 - DurabilityPercent)`

**BluntFactor** by caliber family (example values):

| Caliber Family | BluntFactor | Typical Result (100% armor, 50 dmg) |
| :------------- | :---------: | :---------------------------------- |
| 9×19 / .45 | 0.04 | 0 (full armor) to ~2 HP (low durability) |
| 5.56 / 7.62×39 | 0.06 | 0 to ~3 HP |
| 7.62×51 / 54R | 0.08 | 0 to ~4 HP |
| .338 / .50 | 0.12 | 0 to ~6 HP |
| 12 Gauge | 0.10 | 0 to ~5 HP (per hit) |

Result is clamped to 1–5 HP per shot and may add minor stamina drain. Design intent: being shot in armor still has a cost; it does not fully negate pressure.

---

## Ricochet Chance Tables

Helmets (and some body armor) have a ricochet chance. At shallow impact angles, a high-pen round can deflect and deal 0 HP (concussion only).

**Ricochet Chance by Helmet Class:**

| Helmet Class | Ricochet Chance | Concussion Duration |
| :----------- | :-------------: | :------------------ |
| 1–2 | High (40%) | 1 s |
| 3 | Medium (25%) | 2 s |
| 4 | Medium (20%) | 2.5 s |
| 5–6 | Low (10%) | 3 s |

**Angle rule:** Ricochet only considered when impact angle (from surface normal) &gt; 60° (glancing). Perpendicular hits never ricochet. Concussion: ringing ears, short blur, no HP damage.

---

## Subsonic vs Supersonic

**Supersonic rounds:** Produce audible crack (bullet crack) past the shooter; detectable by enemies. Muzzle report and crack are two separate audio events for positioning.

**Subsonic rounds:** No crack; only muzzle report (and impact). Used by VSS, suppressed 9mm/.45 with subsonic ammo. Trade-off: lower velocity, more drop/falloff in games that model it; in our top-down, subsonic mainly affects audio signature and effective range (velocity still used for falloff).

**Suppressor interaction:** Suppressor reduces muzzle report range (see [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md)). It does not remove bullet crack for supersonic ammo. Subsonic + suppressor = minimal audio signature.

---

## Penetration Through Materials

Bullets can penetrate environmental cover. Result: pass-through with damage reduction and/or chance to stop.

| Material | Penetration | Damage Loss | Notes |
| :------- | :---------- | :---------- | :---- |
| Wood (crate, thin wall) | Full | −20% | Consistent pass-through |
| Drywall | Full | −30% | Two layers = two checks |
| Glass | Full | −10% | Can shatter; visibility |
| Thin metal (sheet, car door) | 50% chance | −40% | One check per layer |
| Sandbags | 25% chance | −50% | Low pen rounds often stop |
| Concrete (wall) | No | — | No penetration |
| Vehicle body (engine block) | No | — | Hard block |
| Player (over-penetration) | Full | Minimal loss | Second target takes reduced damage |

Penetration order: environment first, then player. If bullet stops in material, no player damage.

---

## Caliber Sharing Matrix

Weapons that share the same caliber share ammo pools. Strategic implication: one ammo type can feed primary and sidearm or multiple primaries.

| Caliber | Primary Weapons | Secondary / Other |
| :------ | :-------------- | :----------------- |
| 9×19mm | MP5 | Glock 19, P226 |
| .45 ACP | Vector .45, UMP-45 | M1911, USP-S |
| 5.56×45mm | M4A1, HK416, AUG, M249 | — |
| 7.62×39mm | AK-47, RPK | — |
| 7.62×51mm | SCAR-H, M24, MG42 | — |
| 7.62×54mmR | SVD, PKM | — |
| 5.7×28mm | P90 | — |
| 4.6×30mm | MP7 | — |
| 12 Gauge | All shotguns | — |
| .338 Lapua | AWP | — |
| .50 BMG | M107 | — |
| 9×39mm | VSS | — |

**Implications:** Looting 5.56 ammo benefits M4/HK416/AUG/M249. Carrying a Glock + MP5 allows a single 9×19 ammo stack. Balance: shared ammo increases flexibility but does not grant free power—magazine capacity and weapon stats still differ.

---

## Cross-References

- [Weapon Arsenal](../Gameplay/WeaponArsenal.md) — Ammo types, penetration class, velocity per caliber.
- [Inventory & Gear — Armor](../Inventory_Gear/Armor.md) — Armor classes, zones, materials, damage mechanics.
- [Weapon Balance Framework](Weapon_Balance_Framework.md) — TTK and balance targets.
- [Gear Mechanics](../Gameplay/Gear_Mechanics.md) — Armor durability and weight tier.
