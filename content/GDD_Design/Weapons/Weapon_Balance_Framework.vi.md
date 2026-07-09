---
title: "vũ khí Balance Framework"
type: docs
weight: 3
---

## Tổng Quan

Tài liệu này định nghĩa how vũ khí balance is measured, tuned, và maintained: DPS và TTK math, chi phí-efficiency, balance levers, patch process, meta máu metrics, và seasonal rotation. Design reference: Helldivers 2 faction-cụ thể effectiveness, Delta Force seasonal TTK rebalancing.

> **Cross-References:** [vũ khí Arsenal](../Gameplay/WeaponArsenal.md) — base stats; [Caliber & Ballistics hệ thống](Caliber_Ballistics_System.md) — penetration và damage application; [Gears — giáp & Ballistics](../Gears/ArmorGear/giáp.md) — giáp classes 1–6.

---

## DPS Calculations

**Formula:** `DPS = (Damage × RPM) / 60`

Damage is per-shot base damage (trước giáp). RPM is rounds per minute. Shotguns cách dùng total damage per shot (pellet × pellets) và effective RPM.

### primary vũ khí — DPS Reference (Base)

| vũ khí | Damage | RPM | DPS | Class |
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

*DMR và pistol DPS are lower by design (semi-auto hoặc backup role).*

**Design intent:** DPS alone does not define strength. Range, recoil, penetration, và chi phí matter. This bảng supports comparison within và across classes.

---

## TTK matrix vs giáp Class

TTK = thời gian to kill (100 HP target). giáp classes 1–6 from [Gears — giáp](../Gears/ArmorGear/giáp.md). Shots to kill depend on penetration và body part; below assumes chest, no penetration failure.

**Simplified TTK (seconds) — Chest, 100 HP + giáp**

| vũ khí Type | giáp 1 | giáp 2 | giáp 3 | giáp 4 | giáp 5 | giáp 6 |
| :---------- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| SMG (FMJ) | 0.25 | 0.35 | 0.50 | 0.80+ | 1.0+ | 1.2+ |
| AR (FMJ) | 0.30 | 0.40 | 0.45 | 0.55 | 0.75+ | 1.0+ |
| AR (AP) | 0.35 | 0.40 | 0.45 | 0.50 | 0.55 | 0.65 |
| Shotgun (Buck) | 0.15 | 0.20 | 0.25 | 0.40+ | — | — |
| Sniper (Std) | 0 | 0 | 0 | 0 | 0 | 0–1 |
| LMG (FMJ) | 0.40 | 0.50 | 0.55 | 0.70+ | 0.90+ | 1.1+ |
| Pistol | 0.55 | 0.70 | 0.90+ | 1.2+ | — | — |

*0 = one-shot kill. "+" = marginal hoặc requires many shots / AP đạn.*

Full TTK depends on [Caliber & Ballistics hệ thống](Caliber_Ballistics_System.md) penetration chance và damage falloff. This matrix is for high-level balance targets.

---

## chi phí-Efficiency Index

**Formula:** `Cost-Efficiency = DPS / Weapon Cost (in thousands)`

Higher index = more damage per credit. Identifies giá trị picks và premium options.

| vũ khí | DPS | chi phí ($) | chi phí-Efficiency |
| :------ | :-: | :------: | :-------------: |
| AK-47 | 350 | 1,200 | 0.29 |
| M4A1 | 400 | 3,500 | 0.11 |
| MP5 | 360 | 800 | 0.45 |
| Glock 19 | ~170 | 300 | 0.57 |
| Remington 870 | 160 | 600 | 0.27 |
| HK416 | 482 | 6,500 | 0.07 |
| AWP | 80 | 16,000 | 0.005 |

**Design intent:** Common vũ khí score higher on chi phí-efficiency; rare vũ khí offer niche power (range, penetration, capacity) rather than raw giá trị. Prevents "best gun" from being the most expensive in every situation.

---

## Rarity-Power Curve

Rarity should correlate với **niche power** và **flexibility**, not universal dominance.

| Rarity | Expected Power Profile | Balance Rule |
| :----- | :--------------------- | :----------- |
| Common | Strong in one niche (e.g. CQB, budget) | Can compete in optimal range |
| Uncommon | Broader effectiveness, still trade-offs | No rõ "always pick" |
| Rare | Multiple strengths, higher ceiling | Weak in at least one band (e.g. CQB hoặc range) |
| Epic | Peak in category hoặc unique trait | rõ counterplay (chi phí, mobility, đạn) |
| Legendary | Prestige + small stat bump | Never mandatory for win rate |

**Validation:** No vũ khí should have >55% pick rate in ranked/competitive over a full season. No vũ khí should have <2% pick rate in its intended category unless intentionally niche.

---

## Balance Levers

Which stats to adjust per archetype khi tuning:

| Archetype | primary Levers | secondary Levers | Avoid |
| :-------- | :------------- | :--------------- | :---- |
| AR | Damage, RPM, recoil recovery | Mag size, ADS thời gian | Making one AR best at everything |
| SMG | Damage falloff, hip spread, RPM | Mag size, mobility | Buffing range into AR territory |
| Shotgun | Pellet count, spread, damage per pellet | Fire rate, capacity | One-shot at 15 m+ |
| Sniper | Damage, bullet velocity, scope-in thời gian | Mag size, sway | Fast follow-up rivaling DMR |
| LMG | Recoil (sustained), mobility penalty, reload thời gian | Damage, mag size | Making LMG mobile |
| DMR | Damage, semi-auto RPM cap, sway | Mag size, ADS | Overlapping sniper one-shot |
| Pistol | Damage, draw thời gian, mag size | — | Making pistol primary-viable |

---

## Patch Balance Process

1. **Data collection (2+ weeks):** Pick rate, win rate delta, average TTK by vũ khí, death attribution, usage by map/phase.
2. **Internal playtest:** Proposed changes in closed build; focus on feel và outlier vũ khí.
3. **Community beta (optional):** Balance patch on PTR hoặc limited rollout; collect feedback.
4. **Release:** Patch ghi chú với rationale; monitor same metrics for 1–2 weeks post-patch.
5. **Hotfix criteria:** nếu a single vũ khí exceeds 60% pick rate hoặc +8% win rate delta, expedite hotfix.

---

## Meta máu Metrics

KPIs for vũ khí balance (targets per season):

| Metric | Target | Action nếu Missed |
| :------ | :----- | :---------------- |
| Max single-vũ khí pick rate | < 55% | Nerf hoặc buff alternatives |
| Min category representation | Each category ≥ 5% picks | Buff underused category hoặc add incentives |
| Win rate delta (vũ khí) | No vũ khí > +5% vs average | Reduce overperformer effectiveness |
| TTK spread (within class) | No vũ khí 2× faster TTK than same-class median | Tighten damage/RPM spread |
| chi phí-efficiency spread | Top giá trị pick not > 3× bottom in same class | Adjust chi phí hoặc base stats |

---

## Seasonal Rotation Framework

vũ khí availability và emphasis shift per season to refresh meta:

| Levers | Description |
| :----- | :----------- |
| **Loot bảng weights** | Increase drop rate of underused vũ khí in high-tier zones |
| **Quest/BP rewards** | tính năng cụ thể vũ khí hoặc attachments in battle pass |
| **Nerf/buff cycle** | 2–4 vũ khí tuned per season; tài liệu in patch ghi chú |
| **Limited-thời gian modes** | Modes that restrict hoặc boost certain categories (e.g. "Pistol Only" week) |
| **New vũ khí** | 1–2 new vũ khí per season, preferably in underused category |

Rotation does not remove base vũ khí from the game; it changes their visibility và opportunity chi phí.

---

## Tham Chiếu Chéo

- [vũ khí Arsenal](../Gameplay/WeaponArsenal.md) — Base damage, RPM, chi phí.
- [Caliber & Ballistics hệ thống](Caliber_Ballistics_System.md) — Penetration, falloff, giáp interaction.
- [Gears — giáp & Ballistics](../Gears/ArmorGear/giáp.md) — giáp classes 1–6; [giáp Master Database](../Gears/ArmorGear/Armor_Master_Database.md) — per-item specs.
- [vũ khí Categories Deep Dive](Weapon_Categories_Deep_Dive.md) — Role per genre.
