---
title: "Combat, Weapons & Gear"
linkTitle: Combat
type: docs
weight: 4
---

### Nghệ Thuật Bạo Lực

Combat trong **Extraction Shooter** có stakes cao và không khoan nhượng. Với **TTK thấp (Time to Kill)** và mất gear vĩnh viễn khi chết, mỗi cuộc chạm trán đều là một rủi ro phải tính toán.

{{< callout type="warning" >}} **Quy Tắc Vàng:** Gear không chỉ là progression; nó là _tài nguyên tiêu hao_. Mất một khẩu rifle tier cao sẽ đau, nhưng chính điều đó vận hành economy.
{{< /callout >}}

{{< callout type="info" >}} **Thông Báo Di Chuyển Tài Liệu:** Toàn bộ spec Weapon Arsenal và Item Catalogue đã được hợp nhất vào section **Gameplay/** làm GDD canonical. Dùng các link bên dưới cho weapon stat, attachment table, armor spec, item value, và combat mechanics mới nhất.
{{< /callout >}}

#### Core Mechanics

* **Ballistics:** Bullet drop và travel time đáng tin.
* **Recoil:** Theo pattern, có random deviation.
* **Suppression:** Hỏa lực nặng làm giảm accuracy và làm mờ tầm nhìn.
* **Armor System:** Protection dựa trên durability. AP ammo phá armor; HP ammo phá flesh.

{{< cards cols="2" >}}
{{< card link="../Gameplay/WeaponArsenal" title="Weapon Arsenal (Canonical)" icon="adjustments" subtitle="Weapon bible đầy đủ: category, bảng ammo caliber, attachment reference, damage model, recoil, TTK. [-> Gameplay/]" >}}
{{< card link="../Gameplay/ItemsAndGear" title="Items & Gear Catalogue (Canonical)" icon="archive" subtitle="Armor, medical supplies, throwable, key, crafting material; toàn bộ item spec, value, grid size. [-> Gameplay/]" >}}
{{< /cards >}}

***

### Quản Lý Inventory

Combat bắt đầu trước khi raid diễn ra.

* **Weight System:** Gear nặng làm giảm movement speed và stamina recovery.
* **Grid Inventory:** Inventory kiểu "Tetris" buộc người chơi quyết định khó về thứ nên giữ.
* **Hotbar Limits:** Mỗi raid chỉ có 2 weapon và 4 utility slot. Chọn kỹ.

Với chi tiết grid inventory, secure container rule, và marketplace, xem [Looting & Inventory](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/Looting_Interactions/README.md).
