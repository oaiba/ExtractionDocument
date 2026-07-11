---
title: "Thiết Kế Stash"
linkTitle: "Stash"
type: docs
weight: 25
---

## Tổng Quan

**Stash** là kho lưu trữ lâu dài ngoài raid của người chơi, dùng để giữ toàn bộ vật phẩm đã extraction thành công. Vật phẩm đã đưa vào Stash sẽ không bị mất khi người chơi chết; chỉ trang bị đã mang vào raid mới có thể bị mất. Stash là kho inventory trung tâm nối các raid với giai đoạn chuẩn bị Loadout.

> **Trạng thái tài liệu:** Tài liệu thiết kế độc lập, không thuộc section `Inventory_System`.
> **Vị trí trong game:** Stash được đặt trong **Stash Room** của [Safe House](GameDesign/Safe_House_Design.md). Người chơi có thể truy cập Stash từ Loadout Preparation và Safe House.

---

## 1. Triết Lý Thiết Kế

- **Lưu trữ lâu dài:** Loot đã extraction thành công được bảo toàn; khi chết, chỉ trang bị đã mang vào raid bị ảnh hưởng.
- **Giới hạn không gian:** Lưới kiểu Tetris tạo ra quyết định tổ chức và đánh đổi có ý nghĩa.
- **Cổng tiến trình:** Kích thước Stash tăng theo phiên bản game hoặc cấp độ Safe House.
- **Meta giá trị trên mỗi ô:** Người chơi tối ưu vật phẩm nên giữ hay bán dựa trên hiệu quả sử dụng không gian.

---

## 2. Hệ Thống Lưới

### 2.1 Kích Thước Và Sức Chứa

Sức chứa của Stash bằng **tổng số ô** trong một lưới duy nhất. Mỗi vật phẩm chiếm số ô dựa trên chiều rộng × chiều cao.

| Thuộc tính | Giá trị |
| :--- | :--- |
| **Lưới cơ bản** | 10 cột × số hàng thay đổi theo cấp độ |
| **Xoay vật phẩm** | 90° bằng phím `R` khi đang kéo vật phẩm |
| **Xếp chồng** | Đạn, tiền tệ và nguyên liệu chế tạo có thể xếp chồng; vũ khí, giáp và chìa khóa không xếp chồng |

### 2.2 Kích Thước Vật Phẩm Tham Chiếu

| Danh mục | Kích thước thường gặp | Ví dụ |
| :--- | :--- | :--- |
| Vật phẩm tiêu hao | 1×1 | Bandage, pills, đạn theo stack |
| Băng đạn | 1×2 | Băng đạn AR, băng đạn pistol |
| Lựu đạn | 1×2 | Frag, flash, smoke |
| Súng ngắn | 2×1 | Handgun |
| Súng trường | 4×1 – 5×2 | M4, AK-74 |
| Mũ bảo hộ | 2×2 | Tactical helmet |
| Áo giáp | 3×3 – 4×4 | Plate carrier |
| Ba lô | 3×3 – 7×8 | Ba lô ở trạng thái gấp hoặc mở |

Xem kích thước đầy đủ của từng vật phẩm trong [Gears — Storage Master Database](Gears/StorageGear/Storage_Master_Database.md).

### 2.3 Storage Phẳng Và Gấp Backpack

- **Không có bag-in-bag:** Mỗi container dùng một lưới phẳng; vật phẩm bên trong được quản lý ở cùng một cấp lưu trữ.
- **Gấp Backpack:** Backpack rỗng có thể được gấp lại để chiếm diện tích nhỏ hơn.
- Quy tắc chi tiết: [Storage: Flat Storage & Folding](Gears/StorageGear/Storage_Flat_Storage_Folding.md).

---

## 3. Tiến Trình Mở Rộng Stash

Sức chứa Stash tăng thông qua **phiên bản game** hoặc nâng cấp **Safe House**.

| Phiên bản / Nguồn | Lưới Stash | Tổng số ô | Chi phí mở khóa / Ghi chú |
| :--- | :--- | :---: | :--- |
| Standard Edition | 10×28 | 280 | Miễn phí |
| Safe House cấp 2 | 10×38 | 380 | 3.5M + nguyên liệu |
| Safe House cấp 3 | 10×48 | 480 | 8.5M + nguyên liệu |
| Safe House cấp 4 | 10×68 | 680 | 15M + nguyên liệu |
| Premium Edition | 10×48 | 480 | Có sẵn khi bắt đầu |
| Ultimate Edition | 10×68 | 680 | Có sẵn khi bắt đầu |

Mọi phiên bản game đều có thể đạt mức tối đa 10×68 thông qua nâng cấp Safe House. Xem lộ trình đầy đủ tại [Stash & Container Progression](Gears/StorageGear/Stash_Container_Progression.md).

---

## 4. Tiến Trình Container

### 4.1 Container Chỉ Dùng Trong Stash

Đây là các container chuyên dụng cho Stash, không thể mang vào raid:

| Giai đoạn | Container ví dụ | Cách mở khóa | Cấp độ dự kiến |
| :--- | :--- | :--- | :--- |
| Đầu game | Keytool, Docs Case | Mua từ Trader cấp 1 | 1–5 |
| Đầu – giữa game | Ammo Case, Scav Junkbox | Trader cấp 2 hoặc craft | 10–15 |
| Giữa game | Med Case, Magazine Case | Trader cấp 2 hoặc nhiệm vụ | 15–20 |
| Giữa – cuối game | Weapon Case | Trader cấp 3 hoặc chuỗi nhiệm vụ | 20–30 |
| Cuối game | Items Case | Trader cấp 3 hoặc barter | 30–40 |
| Endgame | THICC Items, THICC Weapon | Trader cấp 4 hoặc chuỗi nhiệm vụ | 40+ |

### 4.2 Lộ Trình Nâng Cấp Secure Container

**Secure Container** là container an toàn giúp giữ vật phẩm bên trong sau khi người chơi chết. Có thể nâng cấp thông qua nhiệm vụ hoặc phiên bản game:

| Container | Lưới | Số ô | Cách mở khóa |
| :--- | :---: | :---: | :--- |
| Alpha | 2×2 | 4 | Mặc định cho mọi edition |
| Beta | 2×3 | 6 | Nhiệm vụ giữa game |
| Gamma | 3×3 | 9 | Premium Edition hoặc nhiệm vụ cuối game |
| Kappa | 3×4 | 12 | Nhiệm vụ: hoàn thành toàn bộ nhiệm vụ chính ở cuối game |

**Giới hạn trong raid:** Không thể đặt vũ khí, thermal scope hoặc night vision vào Secure Container khi đang ở trong raid. Có thể đặt key, vật phẩm y tế, đạn và vật phẩm có giá trị.

---

## 5. Các Khu Vực Tổ Chức

Bố cục được khuyến nghị để quản lý Stash hiệu quả:

| Khu vực | Hàng | Mục đích |
| :--- | :--- | :--- |
| **Trên cùng — Trang bị đang dùng** | 1–10 | Vũ khí, giáp, rig sẵn sàng cho raid và các vật phẩm dùng thường xuyên |
| **Ở giữa — Container** | 11–40 | Case lưu trữ như Scav Junkbox, Ammo Case, Med Case; nhóm theo loại |
| **Bên dưới — Vật phẩm dài hạn** | 41+ | Vật phẩm nhiệm vụ, nguyên liệu nâng cấp Safe House và vật phẩm ít dùng |

**Thứ tự ưu tiên theo giá trị trên mỗi ô:** Vật phẩm nhiệm vụ → vật phẩm có giá trị trên mỗi ô cao → chìa khóa → AP ammo → meta part → barter item → vũ khí → vật phẩm có giá trị thấp cần bỏ.

---

## 6. Tích Hợp Với Stash Room

Stash nằm trong **Stash Room** của [Safe House](GameDesign/Safe_House_Design.md). Các điểm tích hợp gồm:

- **Loadout Preparation:** Panel truy cập nhanh hiển thị Stash đã lọc; người chơi có thể kéo vật phẩm vào slot trang bị.
- **Safe House:** Toàn bộ lưới Stash có thể mở từ Stash Room; logic hồi phục stamina, energy và hydration của Operator sử dụng vật phẩm từ Stash.
- **Trading Post:** Bán vật phẩm cho Trader và truy cập Flea Market.

---

## 7. UI/UX

### 7.1 Bố Cục Màn Hình Stash

```
+------------------------------------------------------------------+
|  < QUAY LẠI       STASH       [Tìm kiếm] [Bộ lọc ▼] [Sắp xếp ▼]   |
|------------------------------------------------------------------|
|  LƯỚI STASH (12 cột x N hàng)                                    |
|  SỨC CHỨA: 145 / 200 ô       TỔNG GIÁ TRỊ: 2,450,000 Credits     |
|  THAO TÁC: [Tự động sắp xếp] [Bán đồ đánh dấu] [Chuyển vào Loadout]|
|           [Bỏ vật phẩm]                                         |
+------------------------------------------------------------------+
```

### 7.2 Cơ Chế Lưới

| Cơ chế | Mô tả | Input theo nền tảng |
| :--- | :--- | :--- |
| Đặt vật phẩm | Vật phẩm chiếm các ô theo kích thước của nó | PC: kéo và thả. Console: di chuyển con trỏ và nhấn `A`. Mobile: chạm để chọn rồi chạm vị trí đặt |
| Xoay vật phẩm | Xoay vật phẩm 90° để tối ưu không gian | PC: nhấn `R`. Console: nhấn `Y` khi đang giữ vật phẩm. Mobile: dùng nút xoay |
| Xếp chồng | Đạn và vật phẩm tiêu hao cùng loại được xếp chồng | Tự động khi đặt lên chồng vật phẩm tương ứng |
| Chuyển nhanh | Chuyển vật phẩm vào slot Loadout đang trang bị | PC: `Ctrl+Click`. Console: giữ `A`. Mobile: chạm hai lần |
| Tìm kiếm | Lọc theo chữ và làm nổi bật vật phẩm phù hợp | PC: `Ctrl+F`. Console: nhấn `Y` để mở bàn phím ảo |
| Tự động sắp xếp | Tổ chức lại vật phẩm để tối ưu không gian | Nhấn một lần; vẫn giữ nhóm danh mục |
| Bán nhanh | Đánh dấu vật phẩm để bán theo lô | PC: nhấn chuột giữa. Console: `X`. Mobile: vuốt sang trái |

### 7.3 Keybind Tham Chiếu

| Hành động | Keybind | Cách dùng |
| :--- | :--- | :--- |
| Chuyển nhanh | `Ctrl + Click` | Chuyển vào vị trí trống đầu tiên |
| Trang bị nhanh | `Alt + Click` | Chuyển vào slot phù hợp |
| Bỏ vật phẩm | `Del` | Đưa vật phẩm ra khỏi Stash |
| Xoay vật phẩm | `R` | Xoay 90° khi đang kéo vật phẩm |

---

## 8. Economy

- **Giá trị trên mỗi ô** = `Price / (W × H)`. Chỉ số này cho biết vật phẩm nào đáng ưu tiên khi không gian Stash bị giới hạn.
- **Bán hay giữ:** Giữ vũ khí nếu đang thuộc meta hoặc cần cho nhiệm vụ; giữ giáp nếu thuộc Class 5+ và độ bền trên 60%; giữ vật phẩm barter nếu cần cho Safe House hoặc chế tạo.
- **Sức chứa theo phiên bản và Safe House:** Standard Edition bắt đầu với 280 ô; mọi phiên bản game đều có thể đạt tối đa 680 ô thông qua nâng cấp Safe House.

---

## 9. Tham Chiếu Chéo

- [Stash & Container Progression](Gears/StorageGear/Stash_Container_Progression.md) — Bảng đầy đủ và chi phí mở khóa.
- [Safe House Design](GameDesign/Safe_House_Design.md) — Stash Room và trạng thái hồi phục của Operator.
- [Storage Master Database](Gears/StorageGear/Storage_Master_Database.md) — Thông số container và các case chỉ dùng trong Stash.
- [Menus — Stash / Inventory Management](UI_UX/Menus.md) — Chi tiết bố cục UI.
- [Loadout Preparation](GameDesign/LoadoutPreparation.md) — Panel truy cập nhanh Stash.
- [Inventory System](Inventory_System/_index.md) — Paper doll, slot trang bị và trải nghiệm looting.
