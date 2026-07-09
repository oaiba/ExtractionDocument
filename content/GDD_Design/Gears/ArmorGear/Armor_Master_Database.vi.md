---
title: "giáp Master Database"
type: docs
weight: 2
---

## Tổng Quan

This tài liệu is the **canonical list** of all giáp items: body vests, helmets, face shields, headsets, và armored rigs. For class hệ thống, zones, materials, và damage cơ chế Xem [giáp & Ballistics](giáp.md). For handling và balance Xem [giáp Handling Settings](Armor_Handling_Settings.md) và [giáp Balance Framework](Armor_Balance_Framework.md).

---

## Body giáp / Vests

Class 1–6 (GOST-style). Zones: Thorax (T), Stomach (S), Sides (A), Neck (N), Arms (R). Material determines durability loss và repair efficiency. **Tier** per [Gear Tier hệ thống](../Gear_Tier_System.md).

### Tier 1 (Class 1–2)


| Code       | Display Name    | Tier | Class | Zones | Material | Weight (kg) | Durability | Grid | Move % | Ergo | Repair Loss | giá trị ($) | Trader | Rarity |
| ---------- | --------------- | :--: | ----- | ----- | -------- | ----------- | ---------- | ---- | ------ | ---- | ----------- | --------- | ------ | ------ |
| VEST_PACA  | PACA Soft giáp | 1    | 2     | T     | Aramid   | 1.9         | 50         | 2×3  | −2     | −3   | 2%          | 1,000     | 1      | Common |
| VEST_PRESS | Press Vest      | 1    | 2     | T, S  | Aramid   | 2.2         | 55         | 2×3  | −2     | −4   | 2%          | 1,200     | 1      | Common |
| VEST_LIGHT | Light Vest      | 1    | 2     | T     | Aramid   | 2.0         | 45         | 2×3  | 0      | −3   | 2%          | 1,000     | 1      | Common |


### Tier 2 (Class 3)


| Code         | Display Name      | Tier | Class | Zones   | Material | Weight (kg) | Durability | Grid | Move % | Ergo | Repair Loss | giá trị ($) | Trader | Rarity   |
| ------------ | ----------------- | :--: | ----- | ------- | -------- | ----------- | ---------- | ---- | ------ | ---- | ----------- | --------- | ------ | -------- |
| VEST_6B13    | 6B13 Assault Vest | 2    | 3     | T, S    | Ceramic  | 5.0         | 70         | 3×3  | −5     | −8   | 10%         | 25,000    | 2      | Uncommon |
| VEST_MOD3M   | Module-3M         | 2    | 3     | T, S, A | UHMWPE   | 4.2         | 65         | 2×3  | −4     | −6   | 4%          | 22,000    | 2      | Uncommon |
| VEST_CERAMIC | Ceramic Carrier   | 2    | 3     | T, S    | Ceramic  | 4.8         | 60         | 2×3  | −5     | −7   | 10%         | 20,000    | 2      | Uncommon |
| VEST_MEDIUM  | Medium Vest       | 2    | 3     | T, S    | UHMWPE   | 3.5         | 60         | 2×3  | −5     | −6   | 4%          | 3,000     | 2      | Uncommon |


### Tier 3 (Class 4)


| Code           | Display Name          | Tier | Class | Zones   | Material | Weight (kg) | Durability | Grid | Move % | Ergo | Repair Loss | giá trị ($) | Trader | Rarity |
| -------------- | --------------------- | :--: | ----- | ------- | -------- | ----------- | ---------- | ---- | ------ | ---- | ----------- | --------- | ------ | ------ |
| VEST_TROOPER   | Trooper Plate Carrier | 3    | 4     | T       | Steel    | 7.5         | 85         | 3×3  | −8     | −12  | 1%          | 45,000    | 3      | Rare   |
| VEST_M1        | M1 Plate Carrier      | 3    | 4     | T, S    | UHMWPE   | 6.2         | 75         | 3×3  | −7     | −10  | 4%          | 50,000    | 3      | Rare   |
| VEST_COMPOSITE | Composite Vest        | 3    | 4     | T, S, A | Ceramic  | 6.0         | 65         | 2×3  | −8     | −11  | 10%         | 42,000    | 3      | Rare   |
| VEST_HEAVY     | Heavy Vest            | 3    | 4     | T, S, A | Steel    | 5.5         | 80         | 2×3  | −10    | −10  | 1%          | 8,000     | 3      | Rare   |
| VEST_CARRIER   | Plate Carrier         | 3    | 4     | T, S    | Titanium | 4.8         | 70         | 2×3  | −8     | −8   | 3%          | 10,000    | 3      | Rare   |


### Tier 4 (Class 5)


| Code       | Display Name | Tier | Class | Zones      | Material | Weight (kg) | Durability | Grid | Move % | Ergo | Repair Loss | giá trị ($) | Trader | Rarity |
| ---------- | ------------ | :--: | ----- | ---------- | -------- | ----------- | ---------- | ---- | ------ | ---- | ----------- | --------- | ------ | ------ |
| VEST_REDUT | Redut-M      | 4    | 5     | T, S, A    | Titanium | 10.0        | 85         | 3×4  | −12    | −18  | 3%          | 120,000   | 4      | Epic   |
| VEST_KILLA | Killa giáp  | 4    | 5     | T, S, A    | UHMWPE   | 9.2         | 80         | 3×3  | −11    | −16  | 4%          | 95,000    | 4      | Epic   |
| VEST_GEN4  | Gen4 Full    | 4    | 5     | T, S, A, N | UHMWPE   | 11.0        | 90         | 3×4  | −13    | −20  | 4%          | 140,000   | 4      | Epic   |


### Tier 5 (Class 6)


| Code         | Display Name        | Tier | Class | Zones      | Material | Weight (kg) | Durability | Grid | Move % | Ergo | Repair Loss | giá trị ($) | Trader    | Rarity    |
| ------------ | ------------------- | :--: | ----- | ---------- | -------- | ----------- | ---------- | ---- | ------ | ---- | ----------- | --------- | --------- | --------- |
| VEST_ZABRALO | Zabralo Mk.2        | 5    | 6     | T, S, A, N | Steel    | 12.5        | 100        | 4×4  | −18    | −25  | 1%          | 250,000   | 4 Exalted | Legendary |
| VEST_SLICK   | Slick Plate Carrier | 5    | 6     | T          | UHMWPE   | 10.5        | 80         | 3×3  | −15    | −22  | 4%          | 200,000   | 4 Exalted | Legendary |


---

## Helmets

Zones: Top (Top), Nape (N), Ears (E), Eyes (Ey), Jaws (J). Ricochet: Low / Med / High. Blocks Headset: some helmets prevent equipping headsets. **Tier** per [Gear Tier hệ thống](../Gear_Tier_System.md).


| Code          | Display Name      | Tier | Class | Zones            | Material | Weight (kg) | Ricochet | Durability | Grid | Blocks Headset | NVG Mount | giá trị ($) | Rarity   | ghi chú                 |
| ------------- | ----------------- | :--: | ----- | ---------------- | -------- | ----------- | -------- | ---------- | ---- | -------------- | --------- | --------- | -------- | --------------------- |
| HELM_SSH68    | SSh-68 (Steel)    | 2    | 3     | Top, N           | Steel    | 1.5         | High     | 40         | 2×2  | No             | No        | 8,000     | Rare     | No ears/face          |
| HELM_6B47     | 6B47              | 2    | 3     | Top, N, E        | UHMWPE   | 1.2         | Med      | 35         | 2×2  | No             | Yes       | 15,000    | Uncommon | Standard military     |
| HELM_LIGHT    | Light Helmet      | 1    | 2     | Top, N           | Aramid   | 0.8         | Med      | 25         | 2×2  | No             | No        | 800       | Common   | Basic                 |
| HELM_MEDIUM   | Medium Helmet     | 2    | 3     | Top, N, E        | UHMWPE   | 1.2         | Med      | 40         | 2×2  | No             | Yes       | 2,500     | Uncommon | Good balance          |
| HELM_HEAVY    | Heavy Helmet      | 3    | 4     | Top, N, E        | Steel    | 1.8         | High     | 55         | 2×2  | No             | Yes       | 6,000     | Rare     | High protection       |
| HELM_ULACH    | ULACH             | 3    | 4     | Top, N, E        | UHMWPE   | 1.8         | Med      | 50         | 2×2  | No             | Yes       | 35,000    | Rare     | Standard choice       |
| HELM_TACTICAL | Tactical Helmet   | 4    | 5     | Top, N, E        | Titanium | 1.5         | Med      | 60         | 2×2  | No             | Yes       | 12,000    | Epic     | Built-in NV           |
| HELM_SPEC     | Specialist Helmet | 2    | 3     | Top, N, E        | UHMWPE   | 1.0         | Med      | 35         | 2×2  | No             | Yes       | 4,500     | Rare     | +10% hearing          |
| HELM_AIRFRAME | Airframe          | 3    | 4     | Top, N, E        | UHMWPE   | 1.4         | Med      | 48         | 2×2  | No             | Yes       | 45,000    | Rare     | Modular               |
| HELM_ALTYN    | Altyn             | 4    | 5     | Top, N, E, Ey, J | Steel    | 2.5         | Low      | 65         | 2×2  | **Yes**        | No        | 85,000    | Epic     | Full face; no headset |
| HELM_RYS      | Rys-T             | 4    | 5     | Top, N, E, Ey, J | Titanium | 2.2         | Low      | 60         | 2×2  | **Yes**        | No        | 75,000    | Epic     | Full face; no headset |


---

## Face Shields & Visors

Attach to compatible helmets hoặc are standalone. Zone: Eyes (Ey) hoặc Jaws (J). Vision Penalty: % reduction to visual clarity khi equipped. **Tier** per [Gear Tier hệ thống](../Gear_Tier_System.md).


| Code           | Display Name        | Tier | Class | Zone  | Material | Durability | Vision Penalty | giá trị ($) | Rarity   |
| -------------- | ------------------- | :--: | ----- | ----- | -------- | ---------- | -------------- | --------- | -------- |
| VISOR_GLASS    | Face Shield (Glass) | 1    | 1     | Ey, J | Glass    | 20         | 5%             | 3,000     | Uncommon |
| VISOR_CERAMIC  | Reinforced Visor    | 1    | 2     | Ey, J | Ceramic  | 30         | 8%             | 8,000     | Rare     |
| VISOR_MANDIBLE | Mandible Guard      | 1    | 2     | J     | UHMWPE   | 25         | 0%             | 5,000     | Uncommon |
| VISOR_TACTICAL | Tactical Visor      | 2    | 3     | Ey    | Ceramic  | 40         | 10%            | 15,000    | Rare     |


---

## Headsets

No giáp giá trị. Modify audio: compress loud sounds (gunfire), amplify ambient (footsteps). EQ profile affects tactical clarity. Xem [giáp & Ballistics](giáp.md) for gameplay impact; helmets that block ears cannot cách dùng headsets. **Tier** per [Gear Tier hệ thống](../Gear_Tier_System.md) (by Rarity: Uncommon = 2, Rare = 3).


| Code        | Display Name   | Tier | EQ Profile        | Weight (kg) | Grid | giá trị ($) | Trader | Rarity   |
| ----------- | -------------- | :--: | ----------------- | ----------- | ---- | --------- | ------ | -------- |
| HEAD_COMTAC | ComTac 4       | 3    | Warm, bassy       | 0.2         | 1×1  | 18,000    | 2      | Rare     |
| HEAD_GSSH   | GSSH-01        | 2    | Harsh, treble     | 0.15        | 1×1  | 12,000    | 1      | Uncommon |
| HEAD_PELTOR | Peltor Sport   | 2    | Balanced, neutral | 0.2         | 1×1  | 15,000    | 2      | Uncommon |
| HEAD_SORDIN | Sordin Supreme | 3    | Mid-focused       | 0.22        | 1×1  | 25,000    | 3      | Rare     |
| HEAD_MSA    | MSA Sordin     | 3    | Enhanced clarity  | 0.25        | 1×1  | 35,000    | 3      | Rare     |


---

## Armored Rigs

Rigs that provide both storage và body giáp. They **replace** a separate body giáp vest. For grid layout, slot count, và hotkey mapping Xem [Storage Master Database](../StorageGear/Storage_Master_Database.md). giáp stats below. **Tier** per [Gear Tier hệ thống](../Gear_Tier_System.md) (by giáp Class).


| Code         | Display Name          | Tier | giáp Class | Zones   | Material | Grid Layout | Slots | Hotkey Slots | Weight (kg) | giá trị ($) | Rarity   |
| ------------ | --------------------- | :--: | ----------- | ------- | -------- | ----------- | ----- | ------------ | ----------- | --------- | -------- |
| RIG_6B3TM    | 6B3TM Armored Rig     | 3    | 4           | T, S    | Ceramic  | 3×4         | 16    | 6            | 9.5         | 45,000    | Rare     |
| RIG_TV110    | Wartech TV-110        | 3    | 4           | T, S, A | UHMWPE   | 3×4         | 20    | 6            | 8.0         | 55,000    | Rare     |
| RIG_ARMORED  | Armored Rig (Generic) | 2    | 3           | T, S    | Ceramic  | 3×4         | 12    | 6            | 3.5         | 25,000    | Uncommon |
| RIG_DEFENDER | Defender 2            | 4    | 5           | T, S, A | Titanium | 3×4         | 14    | 6            | 11.0        | 95,000    | Epic     |


---

## Tham Chiếu Chéo

- [Gear Tier hệ thống](../Gear_Tier_System.md) — giáp Tier (1–5) định nghĩa; progression = Tier + Rarity + người chơi/trader level.
- [giáp & Ballistics](giáp.md) — Class hệ thống, zones, materials, penetration, blunt, ricochet.
- [giáp Handling Settings](Armor_Handling_Settings.md) — Equip times, movement/ergo/audio penalties.
- [giáp Balance Framework](Armor_Balance_Framework.md) — EHP, chi phí-efficiency, durability math.
- [Storage Master Database](../StorageGear/Storage_Master_Database.md) — Tactical rigs (unarmored + armored), slot layouts.
