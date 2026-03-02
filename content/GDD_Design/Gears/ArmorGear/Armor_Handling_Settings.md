---

## title: "Armor Handling Settings"
type: docs
weight: 3

## Overview

This document defines **movement and ergonomics penalties** and **audio penalties** for armor. These values drive gameplay feel and the trade-off between protection and mobility. For class and zone definitions see [Armor & Ballistics](Armor.md); for balance context see [Armor Balance Framework](Armor_Balance_Framework.md).

---

## Movement Penalties (Per Item)

Penalties apply in addition to **total weight tier** (see [Gear Mechanics](../../Gameplay/Gear_Mechanics.md)). Values are per-piece for body armor; helmet penalties stack.


| Armor example | Class | Base move penalty | Sprint penalty | Turn speed | ADS speed |
| ------------- | ----- | ----------------- | -------------- | ---------- | --------- |
| PACA          | 2     | −2%               | −1%            | −1%        | −3%       |
| 6B13          | 3     | −5%               | −3%            | −3%        | −8%       |
| Trooper       | 4     | −8%               | −5%            | −5%        | −12%      |
| Redut-M       | 5     | −12%              | −8%            | −8%        | −18%      |
| Zabralo       | 6     | −18%              | −12%           | −12%       | −25%      |


**Helmets** add a small flat penalty (e.g. −1% to −3% move, −2% to −5% ADS) by weight; full-face helmets (Altyn, Rys-T) apply the higher end.

---

## Ergonomics Impact

**Formula:** `EffectiveErgo = WeaponErgo − ArmorErgoPenalty − HelmetErgoPenalty`

- **ADS speed** scales with EffectiveErgo (lower ergo = slower ADS).
- **Arm stamina drain** while ADSing increases as EffectiveErgo drops.
- **Weapon sway** (e.g. when standing or moving) worsens with lower EffectiveErgo.

Armor ergo penalties are per [Armor Master Database](Armor_Master_Database.md) (Ergo column). Heavy vests (Class 5–6) typically apply −18 to −25; light vests (Class 1–2) −3 to −4. Helmets add roughly −2 to −8 depending on coverage and weight.

---

## Audio Penalties (Helmets)


| Helmet type                        | Hearing reduction | Headset allowed | Notes                                             |
| ---------------------------------- | ----------------- | --------------- | ------------------------------------------------- |
| Open (no ear coverage)             | 0%                | Yes             | SSh-68, Light, Medium                             |
| Ear-covered (e.g. ULACH)           | −10%              | Yes (stacks)    | Standard military                                 |
| Full helmet + visor (Altyn, Rys-T) | −40%              | **No**          | Trade-off: max head protection, no enhanced audio |


Headsets amplify footsteps and compress gunfire. Wearing a full-face helmet blocks the headset slot, so the player gains head/face protection but loses audio intelligence — a defining trade-off in a sound-critical game.

---

## Top-Down Specific

In top-down view, **rotation speed** (turning the character to face a direction) is affected by armor. Heavy armor increases direction-change delay and reduces turn speed; light loadouts feel snappy. The gap between "I see the enemy" and "I can turn and shoot" is larger in heavy armor, rewarding lighter, riskier loadouts for reactive play.

---

## Cross-References

- [Armor & Ballistics](Armor.md) — Class and zones.
- [Armor Master Database](Armor_Master_Database.md) — Per-item weight and ergo.
- [Gear Mechanics](../../Gameplay/Gear_Mechanics.md) — Weight tiers, inertia, loadout examples.
- [Movement & Stamina](../../Gameplay/Movement_and_Stamina.md) — Speed and stamina numbers.
