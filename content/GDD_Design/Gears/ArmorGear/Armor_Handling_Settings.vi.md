---
title: "giáp Handling Settings"
type: docs
weight: 3
---

## Tổng Quan

Tài liệu này định nghĩa **movement và ergonomics penalties** và **audio penalties** for giáp. These values drive gameplay feel và the trade-off between protection và mobility. For class và zone definitions Xem [giáp & Ballistics](giáp.md); for balance context Xem [giáp Balance Framework](Armor_Balance_Framework.md).

---

## Movement Penalties (Per Item)

Penalties apply in addition to **total weight tier** (Xem [Gear cơ chế](../../Gameplay/Gear_Mechanics.md)). Values are per-piece for body giáp; helmet penalties stack.


| giáp example | Class | Base move penalty | Sprint penalty | Turn speed | ADS speed |
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

- **ADS speed** scales với EffectiveErgo (lower ergo = slower ADS).
- **Arm stamina drain** while ADSing increases as EffectiveErgo drops.
- **vũ khí sway** (e.g. khi standing hoặc moving) worsens với lower EffectiveErgo.

giáp ergo penalties are per [giáp Master Database](Armor_Master_Database.md) (Ergo column). Heavy vests (Class 5–6) typically apply −18 to −25; light vests (Class 1–2) −3 to −4. Helmets add roughly −2 to −8 depending on coverage và weight.

---

## Audio Penalties (Helmets)


| Helmet type                        | Hearing reduction | Headset allowed | ghi chú                                             |
| ---------------------------------- | ----------------- | --------------- | ------------------------------------------------- |
| Open (no ear coverage)             | 0%                | Yes             | SSh-68, Light, Medium                             |
| Ear-covered (e.g. ULACH)           | −10%              | Yes (stacks)    | Standard military                                 |
| Full helmet + visor (Altyn, Rys-T) | −40%              | **No**          | Trade-off: max head protection, no enhanced audio |


Headsets amplify footsteps và compress gunfire. Wearing a full-face helmet blocks the headset slot, so the người chơi gains head/face protection nhưng loses audio intelligence — a defining trade-off in a sound-critical game.

---

## Top-Down cụ thể

In top-down view, **rotation speed** (turning the nhân vật to face a direction) is affected by giáp. Heavy giáp increases direction-change delay và reduces turn speed; light loadouts feel snappy. The gap between "I see the địch" và "I can turn và shoot" is larger in heavy giáp, rewarding lighter, riskier loadouts for reactive play.

---

## Tham Chiếu Chéo

- [giáp & Ballistics](giáp.md) — Class và zones.
- [giáp Master Database](Armor_Master_Database.md) — Per-item weight và ergo.
- [Gear cơ chế](../../Gameplay/Gear_Mechanics.md) — Weight tiers, inertia, loadout examples.
- [Movement & Stamina](../../Gameplay/Movement_and_Stamina.md) — Speed và stamina thông số.
