---
title: "Hệ Thống Gear"
linkTitle: Gears
type: docs
weight: 7
---

# Tài Liệu Gears

**Gears** là trang bị vật lý Operator mặc hoặc mang vào raid: body armor, helmet, tactical rig, backpack, và secure container. Section này là hub canonical cho thiết kế armor và storage gear: spec, handling, balance, progression, và master database.

Nó khác với [**Inventory & Gear**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Inventory_System/README.md) (`Inventory_System`), nơi bao phủ hệ inventory tổng quát: grid mechanics, paper doll, looting flow, và các loại container tương lai (stash, vehicle inventory, crate inventory). Gears = _Operator mặc/mang gì_. Inventory_System = _inventory vận hành như thế nào_.

## Trụ Cột Thiết Kế

* **Protection Has Weight** - Armor tốt hơn phải trả giá bằng mobility; mỗi class có penalty về movement và ergonomics.
* **Tactical Ergonomics** - Vị trí cất item (rig hay backpack) quyết định hotkey access và khả năng reload.
* **Visual Readability** - Ở góc nhìn top-down, armor tier và silhouette phải đọc được ở khoảng cách combat.

## Cây Tài Liệu

| Section | Mô Tả |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Gear Tier System](gear_tier_system/index.html) | Gear Tier canonical cho Armor (1-5) và Storage (1-4). Progression = Tier + Rarity + player/trader level; không có item level. Dùng cho loot, craft, economy, UI. |
| [Armor Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/ArmorGear/README.md) | Body armor, helmet, face shield, headset: class, zone, material, penetration, blunt damage, ricochet. Master database, handling, balance, progression, visual identity. |
| [Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) | Tactical rig, backpack, secure container, stash-only case: grid layout, reload rule, flat storage và backpack collapse, balance, stash progression. |

## Section Liên Quan

* [**Inventory & Gear**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Inventory_System/README.md) - Grid system, paper doll, equipment slot, encumbrance overview, looting UX.
* [**Gameplay - Gear Mechanics**](../gameplay/gear_mechanics/index.html) - Gear ảnh hưởng raid như thế nào: weight tier, inertia, rig/backpack gameplay, loadout philosophy.
* [**Gameplay - Looting & Inventory**](../gameplay/looting_interactions/index.html) - Container interaction flow, search time, grid dimension.
* [**Weapons - Caliber & Ballistics**](../weapons/caliber_ballistics_system/index.html) - Penetration vs armor class, blunt damage formula, armor degradation.
