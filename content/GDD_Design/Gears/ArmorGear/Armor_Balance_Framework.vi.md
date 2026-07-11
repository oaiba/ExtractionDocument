---
title: "giáp Balance Framework"
type: docs
weight: 4
---

## Tổng Quan

Tài liệu này định nghĩa **Effective HP (EHP)**, **TTK impact**, **chi phí-efficiency**, **durability và repair math**, và **balance levers** for giáp. It aligns với the vũ khí-side [vũ khí Balance Framework](../../vũ khí/Weapon_Balance_Framework.md) và [Caliber & Ballistics](../../vũ khí/Caliber_Ballistics_System.md).

---

## Effective HP (EHP) by giáp Class

EHP represents how much damage (in equivalent unarmored thorax HP) a người chơi can take trước death. Base thorax HP = 85. “Immune” means round does not penetrate at full durability (only blunt damage).

| giáp class | Base HP protected | EHP vs 5.56 FMJ | vs 7.62 PS | vs 9×19 PST |
| :---------- | :---------------- | :-------------: | :--------: | :---------: |
| None | 85 | 85 | 85 | 85 |
| Class 2 | 85 | 102 (+20%) | 85 | 170 (+100%) |
| Class 3 | 85 | 142 (+67%) | 102 | 255 (+200%) |
| Class 4 | 85 | 213 (+150%) | 142 | Immune* |
| Class 5 | 85 | 340 (+300%) | 213 | Immune |
| Class 6 | 85 | 425 (+400%) | 340 | Immune |

*Immune = no penetration at full durability; blunt only.

---

## TTK Impact matrix

Shots to kill thorax depend on vũ khí, đạn, và target giáp. Design mục tiêu: Class 3–4 is the “sweet spot” for chi phí-efficient survival; Class 5–6 extends TTK significantly nhưng at high weight và chi phí. matrix nên được maintained alongside [vũ khí Balance Framework — TTK matrix](../../vũ khí/Weapon_Balance_Framework.md#ttk-matrix-vs-giáp-class) (vũ khí doc) so giáp và vũ khí patches stay nhất quán.

---

## chi phí-Efficiency Index

| giáp example | Class | giá trị ($) | Weight (kg) | EHP vs 5.56 | $/EHP | Protection per kg |
| :------------ | :---: | -------: | :---------: | :---------: | :----: | :---------------: |
| PACA | 2 | 1,000 | 1.9 | 102 | ~9.8 | 53.7 |
| 6B13 | 3 | 25,000 | 5.0 | 142 | ~176 | 28.4 |
| Trooper | 4 | 45,000 | 7.5 | 213 | ~211 | 28.4 |
| Redut-M | 5 | 120,000 | 10.0 | 340 | ~353 | 34.0 |
| Zabralo | 6 | 250,000 | 12.5 | 425 | ~588 | 34.0 |

Target: Class 3–4 offer best $/EHP for typical engagements; Class 5–6 has diminishing $/EHP nhưng dominant raw survivability và weight chi phí.

---

## Durability & Repair Math

### Durability loss per hit

- **Block (bullet stopped):** `DurabilityLoss = BulletArmorDamage × 1.0` (giáp absorbs; người chơi takes blunt only).
- **Penetration (bullet thông qua):** `DurabilityLoss = BulletArmorDamage × 0.5` (giáp loses less durability nhưng người chơi takes damage).

### Repair và max durability

sau each repair: `MaxDurability_new = MaxDurability_old × (1 − MaterialRepairLoss)`.

| Material | Repair max loss per repair |
| :------- | :------------------------ |
| Aramid | 2% |
| UHMWPE | 4% |
| Ceramic | 10% |
| Steel | 1% |
| Titanium | 3% |
| Aluminium | 8% |

Effective giá trị of giáp = number of repairs trước max durability drops so far that effective class drops. Ceramic vests protect well nhưng degrade quickly với repair; steel retains max durability longer.

---

## Balance Levers

khi tuning giáp in patches, cách dùng these levers:

1. **Durability pool** — Increase hoặc decrease hit points trước effective class drops.
2. **Material destructibility** — Change repair loss % (e.g. Ceramic 10% → 8%).
3. **Weight** — Shift mobility tier (e.g. move Trooper from Heavy to Medium band).
4. **Coverage zones** — Add hoặc remove zones (e.g. sides, neck) to change effective survival.
5. **Trader availability** — Gate by trader level hoặc quest to control access.
6. **Repair chi phí** — Economic sink; higher chi phí reduces “run same vest forever” behavior.

---

## Rarity–Power Curve

- **Common (Class 1–2):** High availability, low chi phí, minimal protection.
- **Uncommon (Class 3):** Standard military, affordable, good vs AI và low-pen đạn.
- **Rare (Class 4):** Solid PvP protection, moderate chi phí.
- **Epic (Class 5):** Dominant in most engagements, expensive.
- **Legendary (Class 6):** Near-invulnerable to non-AP, very rare/expensive.

**Rule:** No single item nên được strictly best in every stat. E.g. Class 6 Steel (very heavy) vs Class 5 UHMWPE (almost as good protection, much lighter) — situational và loadout-dependent.

**Tier** (per [Gear Tier hệ thống](../gear_tier_system/index.html)) is used for balance bracket và chi phí curve; progression = Tier + Rarity + người chơi/trader level.

---

## Tham Chiếu Chéo

- [Gear Tier hệ thống](../gear_tier_system/index.html) — giáp Tier (1–5) định nghĩa; balance bracket, chi phí curve.
- [giáp & Ballistics](armor/index.html) — Penetration check, blunt, material bảng.
- [Caliber & Ballistics hệ thống](../../vũ khí/Caliber_Ballistics_System.md) — Penetration power, giáp degradation formula.
- [vũ khí Balance Framework](../../vũ khí/Weapon_Balance_Framework.md) — TTK matrix, DPS, chi phí-efficiency.
- [giáp Master Database](armor_master_database/index.html) — Per-item durability, material, giá trị.
