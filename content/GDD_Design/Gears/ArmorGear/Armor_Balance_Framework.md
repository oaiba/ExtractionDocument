---
title: "Armor Balance Framework"
type: docs
weight: 4
---

## Overview

This document defines **Effective HP (EHP)**, **TTK impact**, **cost-efficiency**, **durability and repair math**, and **balance levers** for armor. It aligns with the weapon-side [Weapon Balance Framework](../../weapons/weapon_balance_framework/index.html) and [Caliber & Ballistics](../../weapons/caliber_ballistics_system/index.html).

---

## Effective HP (EHP) by Armor Class

EHP represents how much damage (in equivalent unarmored thorax HP) a player can take before death. Base thorax HP = 85. “Immune” means round does not penetrate at full durability (only blunt damage).

| Armor class | Base HP protected | EHP vs 5.56 FMJ | vs 7.62 PS | vs 9×19 PST |
| :---------- | :---------------- | :-------------: | :--------: | :---------: |
| None | 85 | 85 | 85 | 85 |
| Class 2 | 85 | 102 (+20%) | 85 | 170 (+100%) |
| Class 3 | 85 | 142 (+67%) | 102 | 255 (+200%) |
| Class 4 | 85 | 213 (+150%) | 142 | Immune* |
| Class 5 | 85 | 340 (+300%) | 213 | Immune |
| Class 6 | 85 | 425 (+400%) | 340 | Immune |

*Immune = no penetration at full durability; blunt only.

---

## TTK Impact Matrix

Shots to kill thorax depend on weapon, ammo, and target armor. Design goal: Class 3–4 is the “sweet spot” for cost-efficient survival; Class 5–6 extends TTK significantly but at high weight and cost. Matrix should be maintained alongside [Weapon Balance Framework — TTK Matrix](../../Weapons/Weapon_Balance_Framework.md#ttk-matrix-vs-armor-class) (weapon doc) so armor and weapon patches stay consistent.

---

## Cost-Efficiency Index

| Armor example | Class | Value ($) | Weight (kg) | EHP vs 5.56 | $/EHP | Protection per kg |
| :------------ | :---: | -------: | :---------: | :---------: | :----: | :---------------: |
| PACA | 2 | 1,000 | 1.9 | 102 | ~9.8 | 53.7 |
| 6B13 | 3 | 25,000 | 5.0 | 142 | ~176 | 28.4 |
| Trooper | 4 | 45,000 | 7.5 | 213 | ~211 | 28.4 |
| Redut-M | 5 | 120,000 | 10.0 | 340 | ~353 | 34.0 |
| Zabralo | 6 | 250,000 | 12.5 | 425 | ~588 | 34.0 |

Target: Class 3–4 offers best $/EHP for typical engagements; Class 5–6 has diminishing $/EHP but dominant raw survivability and weight cost.

---

## Durability & Repair Math

### Durability loss per hit

- **Block (bullet stopped):** `DurabilityLoss = BulletArmorDamage × 1.0` (armor absorbs; player takes blunt only).
- **Penetration (bullet through):** `DurabilityLoss = BulletArmorDamage × 0.5` (armor loses less durability but player takes damage).

### Repair and max durability

After each repair: `MaxDurability_new = MaxDurability_old × (1 − MaterialRepairLoss)`.

| Material | Repair max loss per repair |
| :------- | :------------------------ |
| Aramid | 2% |
| UHMWPE | 4% |
| Ceramic | 10% |
| Steel | 1% |
| Titanium | 3% |
| Aluminium | 8% |

Effective value of armor = number of repairs before max durability drops so far that effective class drops. Ceramic vests protect well but degrade quickly with repair; steel retains max durability longer.

---

## Balance Levers

When tuning armor in patches, use these levers:

1. **Durability pool** — Increase or decrease hit points before effective class drops.
2. **Material destructibility** — Change repair loss % (e.g. Ceramic 10% → 8%).
3. **Weight** — Shift mobility tier (e.g. move Trooper from Heavy to Medium band).
4. **Coverage zones** — Add or remove zones (e.g. sides, neck) to change effective survival.
5. **Trader availability** — Gate by trader level or quest to control access.
6. **Repair cost** — Economic sink; higher cost reduces “run same vest forever” behavior.

---

## Rarity–Power Curve

- **Common (Class 1–2):** High availability, low cost, minimal protection.
- **Uncommon (Class 3):** Standard military, affordable, good vs AI and low-pen ammo.
- **Rare (Class 4):** Solid PvP protection, moderate cost.
- **Epic (Class 5):** Dominant in most engagements, expensive.
- **Legendary (Class 6):** Near-invulnerable to non-AP, very rare/expensive.

**Rule:** No single item should be strictly best in every stat. E.g. Class 6 Steel (very heavy) vs Class 5 UHMWPE (almost as good protection, much lighter) — situational and loadout-dependent.

**Tier** (per [Gear Tier System](../gear_tier_system/index.html)) is used for balance bracket and cost curve; progression = Tier + Rarity + player/trader level.

---

## Cross-References

- [Gear Tier System](../gear_tier_system/index.html) — Armor Tier (1–5) definition; balance bracket, cost curve.
- [Armor & Ballistics](armor/index.html) — Penetration check, blunt, material table.
- [Caliber & Ballistics System](../../weapons/caliber_ballistics_system/index.html) — Penetration power, armor degradation formula.
- [Weapon Balance Framework](../../weapons/weapon_balance_framework/index.html) — TTK matrix, DPS, cost-efficiency.
- [Armor Master Database](armor_master_database/index.html) — Per-item durability, material, value.
