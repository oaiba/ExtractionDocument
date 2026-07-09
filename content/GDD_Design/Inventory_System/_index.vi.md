---
title: "Inventory System - Core Mechanics"
linkTitle: Inventory System
type: docs
weight: 60
version: 2.1
last_updated: 2026-03-04T00:00:00.000Z
---

> **Document Status**: Living Document - cập nhật thường xuyên\
> **Target Platform**: PC (Primary), Console (Secondary)\
> **Reference Games**: Escape from Tarkov, Arena Breakout: Infinite, Delta Force, Hunt: Showdown 1896, Gray Zone Warfare

***

### Scope: Inventory vs Gears

**Gears** ([../Gears/](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/README.md)) = trang bị vật lý Operator **mặc hoặc mang** vào raid: body armor, helmet, tactical rig, backpack, secure container. Toàn bộ **spec** armor và storage (class, material, slot layout, balance) nằm trong **Gears/ArmorGear** và **Gears/StorageGear**.

**Inventory_System** (section này) = **hệ inventory tổng quát**: grid mechanic, paper doll, equipment slot, encumbrance overview, looting UX. Expansion sau này có thể thêm: Vehicle_Inventory, Global_Stash_System, Crate_System, v.v.

***

### Executive Summary

Thiết kế Inventory & Gear xoay quanh **lựa chọn có ý nghĩa**, **giải đố không gian**, và **cân bằng risk-reward**. Các điểm khác biệt chính: grid kiểu Tetris có rotation, movement penalty theo weight, armor theo zone (xem Gears), tactical accessibility (rig = reload source), và economic risk (mất gear khi chết).

***

### 1. Design Philosophy & Core Pillars

#### 1.1 Core Design Pillars

**Pillar 1: Spatial Puzzle Management** - Inventory space là giới hạn vật lý; item có kích thước (bandage 1x1 vs rifle 4x2); rotation (90 độ) cho phép pack sáng tạo. Mục tiêu: tạo "Tetris moments" đã tay.

**Pillar 2: Weight Has Consequences** - Mọi item có khối lượng; quá tải gây penalty lên stamina, speed, và inertia. Mục tiêu: trade-off armor vs mobility, loot vs escape.

**Pillar 3: Risk-Reward Economics** - Gear tier cao tăng khả năng sống sót nhưng khuếch đại mất mát khi chết; insurance và secure container làm mềm loop. Mục tiêu: "gearing fear" và "loot excitement."

**Pillar 4: Tactical Ergonomics** - Vị trí cất item quan trọng: magazine trong rig = reload nhanh; trong backpack = phải mở inventory. Mục tiêu: thưởng cho chuẩn bị tốt, phạt loadout planning kém.

#### 1.2 Player Experience Goals

* **New players:** Giới thiệu dần, starter loadout đơn giản, feedback rõ cho weight/space.
* **Veterans:** Min-max space/weight, value-per-slot meta, speed-looting keybind.
* **Emotional beats:** Căng thẳng (space giới hạn), thỏa mãn (pack hoàn hảo), sợ hãi (extract khi overweight), mất mát (death), chiến thắng (extract với inventory đầy).

***

### 2. The Character Loadout System (Paper Doll)

#### 2.1 Primary Interface

Pre-raid screen: 3D character model (xoay được), equipment slot quanh model, real-time stat (armor rating, weight, movement speed), durability indicator.

#### 2.2 Equipment Slots

| Slot Name | Grid Size | Hotkey | Durability | Notes |
| -------------------- | --------- | ------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Headset** | 1x1 | No | N/A | Audio mix (nén gunfire, khuếch đại footstep). EQ thay đổi theo model. Xem [Gears - Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md#headsets). |
| **Helmet** | 2x2 | No | Yes | Zone protection (Top, Nape, Ears, Eyes, Jaws). Class 1-6. Xem [Gears/ArmorGear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/ArmorGear/README.md). |
| **Face Cover** | 1x1 | No | Some | Concealment + optional Class 1-2. |
| **Body Armor** | Variable | No | Yes | Chỉ dùng khi không dùng Armored Rig. Thorax/Stomach. Class 1-6. [Gears - Armor](../Gears/ArmorGear/Armor.md). |
| **Tactical Rig** | Variable | **YES** | Varies | **Reload source.** Unarmored hoặc Armored (thay body armor). Thường 12-24 slot. [Gears/StorageGear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md). |
| **Primary 1 / 2** | Weapon | **1** / **2** | Yes | Chest / back. |
| **Sidearm** | Weapon | **3** | Yes | Holster, swap nhanh nhất. |
| **Scabbard** | Weapon | **V** | N/A | Melee. |
| **Pockets** | 4x1 | **4-0** | N/A | Built-in; hotkeyable; key, med, nade. |
| **Backpack** | Variable | No | N/A | Loot chính; không hotkey; mất khi chết. [Gears/StorageGear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md). |
| **Secure Container** | Variable | No | N/A | **Sống sót qua death.** 2x2 đến 3x4. In-raid: không cho weapon/thermal/NVG/helmet vào. [Storage Gear](../Gears/StorageGear/Storage_Master_Database.md#secure-containers). |
| **Armband** | 1x1 | No | N/A | Cosmetic / team ID. |

#### 2.3 UI/UX

Grid drag-drop, color coding (green/red/yellow), tooltip (name, weight, size, value, durability), keybind remapping, optional auto-sort. Accessibility: colorblind mode, scalable UI.

***

### 3. Equipment Overview (Armor & Storage)

**Armor & ballistics** - Class 1-6, zone, material, penetration, blunt, ricochet: [Gears - Armor & Ballistics](../Gears/ArmorGear/Armor.md). Danh sách item đầy đủ: [Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md).

**Tactical rigs vs armored rigs** - Unarmored rig = nhiều slot hơn, không protection; armored rig = ít slot hơn + Class 3-5. Decision matrix và loadout example: [Gears - Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) và [Gear Mechanics](../Gameplay/Gear_Mechanics.md).

**Headsets** - ANC/ASA, EQ profile (ComTac, GSSH, Peltor, Sordin, MSA). Liệt kê trong [Armor Master Database - Headsets](../Gears/ArmorGear/Armor_Master_Database.md#headsets).

***

### 4. Grid System Overview

#### 4.1 Item Dimensions & Rotation

Mọi item: Width x Height trong cell 1x1. Rotation: 90 độ (R khi kéo). **Weapon grid size cố định theo weapon type;** thêm hoặc bỏ attachment không thay đổi kích thước inventory của weapon.

| Category | Typical Size | Examples |
| ----------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Consumables | 1x1 | Bandage, pills, ammo stack |
| Magazines | 1x2 | AR mag, pistol mag |
| Grenades | 1x2 | Frag, flash, smoke |
| Pistols | 2x1 | Handguns |
| SMGs | 2x2 - 3x2 | MP5, Vector |
| Rifles | 4x1 - 5x2 | M4, AK-74 |
| Sniper | 5x2 - 6x2 | SVD, M700 |
| Helmets | 2x2 | Tactical helmets |
| Armor Vests | 3x3 - 4x4 | Plate carriers |
| Backpacks | 3x3 - 7x8 | Collapsed vs deployed; capacity = tổng cell theo container (xem [Storage Master Database](../Gears/StorageGear/Storage_Master_Database.md)) |

#### 4.2 Stacking

Stackable: ammo (ví dụ 60/stack), currency, crafting material. Non-stackable: weapon, armor, attachment, key, quest item. Gộp partial stack trước raid.

#### 4.3 Flat Storage & Folding

**Không bag-in-bag:** Mỗi Storage Gear có một Storage duy nhất; tất cả item bên trong cùng cấp (flat). Bag, rig, armor, weapon, và attachment đặt trong container là item bình thường (chỉ có footprint). **Backpack collapse:** Backpack trống có thể collapse về size nhỏ hơn. Full rule: [Gears - Flat Storage & Folding](../Gears/StorageGear/Storage_Flat_Storage_Folding.md).

***

### 5. Encumbrance & Movement

Total weight = equipped gear + inventory (toàn bộ item trong mọi Storage Gear và slot). Weight tier (Light -> Medium -> Heavy -> Critical -> Overweight) ảnh hưởng movement speed, sprint, inertia, jump, noise. Full formula, threshold, inertia, stamina regen: [Gear Mechanics](../Gameplay/Gear_Mechanics.md) và [Movement & Stamina](../Gameplay/Movement_and_Stamina.md).

***

### 6. In-Raid Interactions & UX

#### 6.1 Looting

**Open inventory (ví dụ Tab):** Split view - trái: vicinity/container, phải: inventory của bạn. Time không freeze; audio bị muffled nhưng vẫn nghe được.

**Container search:** Progress bar (1-5 s theo container type và Perception skill). Item reveal dần; có thể cancel. Examination: unknown item hiện "?" cho đến khi examine (0.5-2 s).

#### 6.2 Keybinds (examples)

| Action | Keybind | Use |
| ----------- | ------------ | ------------------ |
| Quick Move | Ctrl + Click | Ô trống đầu tiên |
| Quick Equip | Alt + Click | Slot đúng |
| Discard | Del | Drop |
| Rotate | R | 90 độ khi kéo |
| Examine | Middle Click | Identify |

#### 6.3 Value & Priority

Value/slot = Price / (W x H). Priority: quest items -> high value/slot -> keys -> AP ammo -> meta parts -> barter -> weapons -> low value (drop).

***

### 7. Weapon Modding (Gunsmith)

Weapon là platform với 40-100+ attachment trên mỗi family. Node-based build (receiver, barrel, handguard, optics, stock, v.v.); live stat comparison; preset và sharing. Full UI và compatibility: [Gunsmith System](Gunsmith_System.md). Weapon spec: [Weapon Arsenal](../Gameplay/WeaponArsenal.md) và section [Weapons](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Weapons/README.md).

***

### 8. Stash & Containers

Xem [**Stash Design**](../Stash_Design.md) cho full Stash specification (grid, container, progression, UI/UX). Stash size theo edition và Safe House level; container unlock path (Scav Junkbox, Ammo/Med/Weapon Case, Items Case, THICC); secure container upgrade (Alpha -> Beta -> Gamma/Kappa). Full table: [Gears - Stash & Container Progression](../Gears/StorageGear/Stash_Container_Progression.md).

***

### 9. Implementation Notes

* **Data:** Item placement dùng grid coordinate, rotation, parentId (container), slotId. Server validate overlap, weight, placement rule.
* **Anti-cheat:** Server-side grid và weight check; không tin client cho capacity hoặc duplicate.
* **UX:** Drag state, valid/invalid placement feedback, snap-to-grid, SFX. Xem technical note hiện có trong repo.

***

### Appendix A: Glossary

**ADS** Aim Down Sights - **EOD** Edge of Darkness (premium) - **FiR** Found in Raid - **Rig** Tactical vest (reload source) - **Stash** Persistent out-of-raid storage - **Tetris** Spatial grid inventory

***

### Appendix B: Related Docs

* [**Stash Design**](../Stash_Design.md) - Full Stash specification (independent document).
* [**Gears**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/README.md) - Armor & Storage gear spec (ArmorGear, StorageGear).
* [**Gameplay - Gear Mechanics**](../Gameplay/Gear_Mechanics.md) - Weight tier, loadout philosophy, extraction.
* [**Gameplay - Looting & Inventory**](../Gameplay/Looting_Interactions.md) - Container search time, grid dimension.
* [**Container Mechanics**](Container_Mechanics.md) - High-level container type và mechanic (secure container, nesting).
* [**Looting & FIR Rules**](Looting_And_FIR_Rules.md) - Loot loop, FIR status, corpse looting.
* [**Medical & Survival Systems**](Medical_And_Survival_Systems.md) - Injury type, med, stimulant, hydration/energy.
* [**Gunsmith System**](Gunsmith_System.md) - Weapon modding, ergonomics, malfunction, overheating.
