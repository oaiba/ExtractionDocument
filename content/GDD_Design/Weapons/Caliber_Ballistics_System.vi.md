---
title: "Caliber & Ballistics hệ thống"
type: docs
weight: 4
---

## Tổng Quan

Tài liệu này định nghĩa how bullets interact với giáp, durability, distance, và materials: penetration chance, damage falloff, giáp degradation, blunt damage, ricochet, và caliber sharing. giáp classes và zones are in [Gears — giáp & Ballistics](../gears/armorgear/armor/index.html).

> **Cross-References:** [vũ khí Arsenal](../gameplay/weaponarsenal/index.html) — đạn tables by caliber; [vũ khí Balance Framework](weapon_balance_framework/index.html) — TTK và balance; [Gears — giáp & Ballistics](../gears/armorgear/armor/index.html) — giáp classes 1–6, zones, materials; [giáp Master Database](../gears/armorgear/armor_master_database/index.html) — per-item coverage và class.

---

## Player-Readable Ballistics Contract

Ballistics có thể dùng server math, nhưng player-facing result phải dễ hiểu. Nếu shot gây ít damage hơn kỳ vọng, game phải cho lý do readable qua HUD, audio, VFX, hoặc death recap.

| Result | System Cause | Required Feedback |
| :--- | :--- | :--- |
| Penetration | Ammo penetration vượt effective armor class | Flesh hit marker cộng armor damage cue nếu có armor |
| Partial penetration | Armor giảm energy nhưng damage vẫn đi qua | Muted hit marker, armor spark, reduced damage recap line |
| Block | Armor chặn health damage; blunt có thể apply | Hard armor impact, blocked/no-penetration marker, durability feedback |
| Ricochet | Glancing hit trên helmet/armor | Deflect sound, spark ngắn, concussion nếu applicable |
| Falloff | Range vượt effective band | Death recap và weapon detail show reduced damage at range |
| Material penetration | Cover giảm hoặc chặn bullet | Impact trên material, pass-through cue chỉ khi damage apply |
| Armor break | Durability xuống unusable state | Armor warning trên victim HUD và debrief item condition |

Armor interaction không được chỉ là hidden math. Player không cần formula trong combat, nhưng cần biết vấn đề là aim, range, ammo, armor, cover, hay durability.

---

## Penetration Chance Formula

khi a bullet hits an armored zone, the server resolves:

**Penetration Power (PP):** Each đạn type has a numeric penetration class (0–8) matching the đạn bảng in [vũ khí Arsenal](../gameplay/weaponarsenal/index.html) (e.g. FMJ Low = 2, AP High = 5, .338 Ultimate = 7).

**Effective giáp Class (EAC):**  
`EAC = ArmorClass + (1 - DurabilityPercent) × 2`  
Durability is 0–1. At 100% durability, EAC = ArmorClass. At 50% durability, EAC = ArmorClass + 1. At 0%, giáp is effectively bypassed for penetration (blunt still applies).

**Penetration Chance:**  
`PenChance = clamp( (PP - EAC + 2) / 4 , 0 , 1 )`  
- nếu PP ≥ EAC + 2: 100% penetrate.  
- nếu PP ≤ EAC - 2: 0% penetrate (block).  
- In between: linear interpolation (e.g. PP = EAC → 50% chance).

**On Penetration:** Damage is reduced by residual energy factor: `Damage × (0.6 + 0.2 × (PP - EAC))`, clamped to 60–100% of base damage. giáp takes durability damage (see giáp Degradation).

**On Block:** No máu damage from the bullet; blunt damage still applies. giáp takes higher durability damage than on penetration.

---

## Damage Falloff Curves

Damage scales với distance. Below: multiplier applied to base damage (1.0 = no falloff). Distance is 2D horizontal range (top-down).

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

## giáp Degradation Math

Each hit to giáp reduces its durability. Durability loss depends on penetration kết quả và caliber.

**On Penetration:**  
`DurabilityLoss = BaseDmg × 0.015 × (1 + (EAC - PP))`  
Capped per hit (e.g. max 8% per shot). Higher penetration vs lower giáp = less durability loss (bullet passes thông qua "cleaner").

**On Block:**  
`DurabilityLoss = BaseDmg × 0.025 × (1 + (PP - EAC))`  
Capped per hit (e.g. max 12%). Stopped rounds dump more energy into the plate.

**Effective class reduction:** As durability drops, EAC increases (see Penetration Chance). At 50% durability, giáp is treated as roughly one class worse; at 25%, two classes worse. At 0% the giáp is destroyed (no protection; weight remains until dropped). Xem [Gear cơ chế](../gameplay/gear_mechanics/index.html) for gameplay impact.

---

## Blunt Damage Formula

khi a bullet is **blocked** by giáp, the wearer still takes blunt trauma.

**Formula (from [Gears — giáp](../gears/armorgear/armor/index.html)):**
`BluntDmg = BaseDmg × BluntFactor × (1 - DurabilityPercent)`

**BluntFactor** by caliber family (example values):

| Caliber Family | BluntFactor | Typical kết quả (100% giáp, 50 dmg) |
| :------------- | :---------: | :---------------------------------- |
| 9×19 / .45 | 0.04 | 0 (full giáp) to ~2 HP (low durability) |
| 5.56 / 7.62×39 | 0.06 | 0 to ~3 HP |
| 7.62×51 / 54R | 0.08 | 0 to ~4 HP |
| .338 / .50 | 0.12 | 0 to ~6 HP |
| 12 Gauge | 0.10 | 0 to ~5 HP (per hit) |

kết quả is clamped to 1–5 HP per shot và may add minor stamina drain. Design intent: being shot in giáp still has a chi phí; it does not fully negate pressure.

---

## Ricochet Chance Tables

Helmets (và some body giáp) have a ricochet chance. At shallow impact angles, a high-pen round can deflect và deal 0 HP (concussion only).

**Ricochet Chance by Helmet Class:**

| Helmet Class | Ricochet Chance | Concussion Duration |
| :----------- | :-------------: | :------------------ |
| 1–2 | High (40%) | 1 s |
| 3 | Medium (25%) | 2 s |
| 4 | Medium (20%) | 2.5 s |
| 5–6 | Low (10%) | 3 s |

**Angle rule:** Ricochet only considered khi impact angle (from surface normal) &gt; 60° (glancing). Perpendicular hits never ricochet. Concussion: ringing ears, short blur, no HP damage.

---

## Subsonic vs Supersonic

**Supersonic rounds:** Produce audible crack (bullet crack) past the shooter; detectable by địch. Muzzle report và crack are two separate audio events for positioning.

**Subsonic rounds:** No crack; only muzzle report (và impact). Used by VSS, suppressed 9mm/.45 với subsonic đạn. Trade-off: lower velocity, more drop/falloff in games that model it; in our top-down, subsonic mainly affects audio signature và effective range (velocity still used for falloff).

**Suppressor interaction:** Suppressor reduces muzzle report range (Xem [vũ khí Attachment hệ thống](../gameplay/weapon_attachment_system/index.html)). It does not remove bullet crack for supersonic đạn. Subsonic + suppressor = minimal audio signature.

---

## Penetration thông qua Materials

Bullets can penetrate environmental cover. kết quả: pass-thông qua với damage reduction và/hoặc chance to stop.

| Material | Penetration | Damage Loss | ghi chú |
| :------- | :---------- | :---------- | :---- |
| Wood (crate, thin wall) | Full | −20% | nhất quán pass-thông qua |
| Drywall | Full | −30% | Two layers = two checks |
| Glass | Full | −10% | Can shatter; visibility |
| Thin metal (sheet, car door) | 50% chance | −40% | One check per layer |
| Sandbags | 25% chance | −50% | Low pen rounds often stop |
| Concrete (wall) | No | — | No penetration |
| Vehicle body (engine block) | No | — | Hard block |
| người chơi (over-penetration) | Full | Minimal loss | Second target takes reduced damage |

Penetration order: environment first, then người chơi. nếu bullet stops in material, no người chơi damage.

---

## Caliber Sharing matrix

vũ khí that share the same caliber share đạn pools. Strategic implication: one đạn type can feed primary và sidearm hoặc multiple primaries.

| Caliber | primary vũ khí | secondary / Other |
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

**Implications:** Looting 5.56 đạn benefits M4/HK416/AUG/M249. Carrying a Glock + MP5 allows a single 9×19 đạn stack. Balance: shared đạn increases flexibility nhưng does not grant free power—magazine capacity và vũ khí stats still differ.

---

## Tham Chiếu Chéo

- [vũ khí Arsenal](../gameplay/weaponarsenal/index.html) — đạn types, penetration class, velocity per caliber.
- [Gears — giáp & Ballistics](../gears/armorgear/armor/index.html) — giáp classes, zones, materials, damage cơ chế; [giáp Master Database](../gears/armorgear/armor_master_database/index.html) — per-item specs.
- [vũ khí Balance Framework](weapon_balance_framework/index.html) — TTK và balance targets.
- [Gear cơ chế](../gameplay/gear_mechanics/index.html) — giáp durability và weight tier.
