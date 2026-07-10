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

### Inventory System Model

Inventory model định nghĩa cách physical item tồn tại qua world loot, stash, loadout, containers, traders, rewards, và post-raid transfer. Model này tách khỏi Commerce entitlement: cosmetic ownership có thể unlock presentation, nhưng combat gear power vẫn là physical, earned, found, crafted, traded, hoặc quest-granted.

| Entity | Định nghĩa | Yêu cầu UI / Design |
| ------ | ---------- | ------------------- |
| `Item` | Object player thấy được và có thể inspect, move, equip, consume, sell, turn in, hoặc grant | Luôn có category, display name, footprint/slot rule, value context, allowed actions |
| `ItemTemplate` | Static data dùng chung cho mọi copy của item | Định nghĩa category, base weight, footprint, max durability, rarity, tier, tags, valid containers, valid slots |
| `ItemInstance` | Một copy cụ thể owned hoặc world-spawned | Mang durability, ammo count, FIR, insurance, ownership, lock, attachment, location state |
| `Container` | Parent space chứa item instances | Định nghĩa grid size, allowed categories, nesting rules, access speed, persistence |
| `Slot` | Loadout/container position có restriction | Nêu accepted categories, required/optional status, hotkey behavior, validation blockers |
| `Stack` | Nhiều countable items trong một instance | Show current count, max count, split/merge rules, cap behavior |
| `Attachment` | Item instance gắn vào item khác | Preserve compatibility, stats delta, durability/ammo nếu relevant, parent identity |
| `OwnershipState` | Quan hệ giữa player/account và item/entitlement | Tách physical ownership, entitlement unlock, temporary grant, lost item, pending sync |
| `PlacementState` | Tính hợp lệ của item position/move | Show valid, invalid, blocked, rotate-needed, no-space, category-restricted, server-pending |
| `ItemFlag` | State modifier visible trên item instance | Gồm FIR, quest, protected, insured, contraband, locked, equipped, damaged, broken, favorited |

### Item Taxonomy

| Category | Examples | Core Rules |
| -------- | -------- | ---------- |
| Weapons | Primary, sidearm, melee | Physical combat items; không grant trực tiếp bằng premium purchase |
| Armor | Body armor, helmets, visors, armored rigs | Durability, zones, class, material, repairability, weight đều quan trọng |
| Headsets | Audio profile gear | Compare bằng audio profile và availability, không dùng armor class |
| Storage gear | Tactical rigs, backpacks, secure containers, stash cases | Định nghĩa capacity, access, mobility cost, restrictions, persistence |
| Ammunition | Loose ammo, boxed ammo | Stackable; caliber compatibility phải explicit |
| Magazines | Loaded hoặc empty mags | Giữ ammo count và caliber/weapon compatibility |
| Medical | Bandage, medkit, surgery, stim | Có thể hotkey nếu nằm trong valid accessible storage |
| Survival | Food, water, tools, utility | Có thể liên quan energy, hydration, crafting, quest requirements |
| Keys | Physical keys, cards, access devices | Quest/location relevance và secure-container rules phải visible |
| Quest items | Delivery, proof, intel, marked items | FIR và turn-in requirements ưu tiên hơn sell/discard |
| Crafting materials | Components, tools, barter items | Show recipe/trader relevance và stack/space behavior |
| Valuables | Sellable loot, rare tech, trophies | Show value-per-cell và quest/trader relevance trước bulk sell |
| Cosmetics / entitlements | Skins, charms, banners, profile items | Account unlocks; không trở thành combat-power physical gear instances |

### Ownership vs Entitlement Rules

| Concept | Meaning | Rule |
| ------- | ------- | ---- |
| Owned item instance | Physical item trong stash, loadout, world, trader transaction, reward inbox, hoặc overflow | Có thể lost, damaged, moved, insured, sold, crafted, turned in, destroyed theo item rules |
| Entitlement | Account-level unlock từ Commerce, redeem, event, support, battle pass, achievement | Unlock cosmetic/profile/service access; không tạo paid combat-power gear |
| Cosmetic application | Visual override/account presentation áp dụng lên compatible item/operator/profile | Không đổi hitbox, recoil, audio readability, visibility advantage, armor/storage stats |
| Temporary grant | Support/event/compensation item hoặc reward chưa claim | Show source, expiry, claim destination, duplicate/overflow handling |
| Pending sync | Item hoặc entitlement đang chờ backend confirmation | UI chặn duplicate claim/sell/equip cho tới khi state final |

### Item Lifecycle

```
spawned -> discovered/examined -> looted -> found-in-raid -> extracted -> stashed
   -> equipped -> insured -> damaged -> repaired
   -> traded / sold / crafted / turned-in / consumed
   -> lost / destroyed / expired / converted
```

| Lifecycle Step | Requirement |
| -------------- | ----------- |
| Spawned / discovered | Unknown items có thể show placeholder tới khi examined; reveal không phá grid layout |
| Looted / FIR | FIR state gắn với item instance và tồn tại tới khi rule tiêu thụ nó |
| Extracted / stashed | Post-raid transfer preserve flags, attachments, durability, stack count, container parent |
| Equipped | Slot validation và loadout risk summary update ngay |
| Insured | Eligible items show insured provider/rule; ineligible items show reason |
| Damaged / repaired | Current/max durability được preserve; repair preview cost và max durability loss |
| Traded / sold / crafted / turned-in | Destructive/irreversible actions show item name, flags, value, consequence |
| Lost / destroyed / expired / converted | Result state giải thích vì sao item rời ownership và support/reward inbox có áp dụng không |

### Item State Matrix

| State | Meaning | Required UI Behavior |
| ----- | ------- | -------------------- |
| Locked | Player không thể use/move/sell/equip vì rule | Show exact lock reason và unlock route |
| Protected | Player protect item khỏi bulk sell/discard | Exclude khỏi bulk destructive actions mặc định |
| Insured | Item được bảo hiểm theo rules | Show provider/rule, return window, ineligible modes |
| Uninsured | Eligible item chưa có insurance | Warn trong loadout khi value threshold cao |
| Contraband | Item có restricted trade/deploy/insurance behavior | Show readable restriction trước equip, sell, queue |
| FIR | Item found in raid và extracted hợp lệ | Badge có text support trong stash, trader, quest, AAR |
| Quest-critical | Item cần cho active/nearby quest | Sell/discard/turn-in actions explain consequence |
| Equipped | Item đang trong loadout | Bulk stash actions không move/sell nếu chưa confirm |
| Damaged | Durability dưới ideal state | Show repair route và impact lên combat/storage value |
| Broken | Dưới usable threshold | Block deploy/equip nếu rule yêu cầu |
| Stacked / split | Countable item grouped hoặc separated | Split/merge preserve caps, flags, valid containers |
| Overflow | Item nằm ngoài normal stash capacity | Require resolution path trước risky exits nếu design cần |
| Pending sync | Chờ server confirmation | Disable duplicate destructive/claim actions và show finalizing state |

### Stash IA Model

| Surface | Owns | Required Behavior |
| ------- | ---- | ----------------- |
| Persistent stash | Long-term item storage | Show capacity, value, filters, search, protected item count, overflow status |
| Equipment slots | Loadout-bound items | Mirror loadout validity và tránh accidental movement of equipped items |
| Cases / containers | Organized sub-storage | Show category restrictions, capacity, nesting/flat-storage rules, valid targets |
| Filter rail | Fast item discovery | Support category, rarity/tier, FIR, quest, protected, insured, contraband, damaged, value |
| Search | Direct retrieval | Search name, category, caliber, quest tag, trader relevance, container contents |
| Capacity summary | Stash health | Show used/total cells, incoming overflow, large-item pressure, suggested fixes |
| Overflow lane | Items waiting for resolution | Preserve reward/AAR/support source và block duplicate claim |
| Destructive action bar | Sell/discard/turn-in/craft decisions | Show protected/quest/high-value/insured/contraband warnings trước commit |

### Inventory QA Checklist

- [ ] Mọi item move có server-valid placement state: valid, invalid, blocked, rotate-needed, no-space, pending.
- [ ] Item instance state không duplicate/desync giữa stash, loadout, reward inbox, trader, post-raid transfer.
- [ ] Ownership và entitlement tách rõ; paid cosmetic entitlement không grant combat-power item instances.
- [ ] FIR, quest, protected, insured, contraband, damaged, broken, equipped, pending states có readable labels.
- [ ] Sell, discard, craft, turn-in, overwrite, bulk actions confirm protected, quest, high-value, insured, contraband items.
- [ ] Full stash, overflow, filter-empty, invalid placement, pending sync, missing capacity states show direct next actions.
- [ ] Controller/touch users có thể move, rotate, split, inspect, confirm items không cần precision-only interaction.

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
