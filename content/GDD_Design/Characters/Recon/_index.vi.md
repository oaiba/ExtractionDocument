---
title: Recon
linkTitle: Recon
type: docs
weight: 3
---

### Tổng Quan Class

Operator class **Recon** mạnh về thu thập intel và kiểm soát luồng thông tin. They enable ambushes, prevent surprises, and dominate through knowledge.

#### Bản Sắc Class

| Thuộc Tính           | Giá Trị           | Ghi Chú                                  |
| ------------------- | --------------- | -------------------------------------- |
| **Role**            | Intel & Stealth | Information is power                   |
| **Độ Khó**      | Cao            | Requires game sense and map knowledge  |
| **Phụ Thuộc Team** | Trung bình          | Intel helps team, can solo effectively |
| **Trần Kỹ Năng**   | Rất cao       | Map knowledge crucial                  |

#### Trait Class (Tất Cả Operator Recon)

| Trait               | Hiệu Ứng               | Tác Động Gameplay         |
| ------------------- | -------------------- | ----------------------- |
| **Sneaky Movement** | +15% Tốc Độ Crouch    | Faster stealth movement |
| **Silent Steps**    | -30% Âm Lượng Bước Chân | Harder to hear coming   |
| **Fragile Frame**   | -5% Maximum Máu   | Glass cannon            |

***

### Operator

| Operator                                                                                                                        | Codename | Chuyên Môn      | Mở Khóa                   |
| ------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------- | ------------------------ |
| [Kaito Nakamura](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Sonar/README.md)     | SONAR    | Area Reveal    | Level 8, 5,000 Credits   |
| [Ananya Patel](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Mirage/README.md)      | MIRAGE   | Trap Detection | Level 12, 7,500 Credits  |
| [Unit N-7 "Nero"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Obsidian/README.md) | OBSIDIAN | Visual Denial  | Level 25, 15,000 Credits |

***

### Hướng Dẫn Playstyle

#### Khi Nên Chọn Recon

**Chọn Recon khi:**

* Solo or small team
* Map has lots of flank routes
* You know the map well
* Địch team has ambush potential

**Tránh Recon khi:**

* Open, simple maps
* Your team needs healing
* You are unfamiliar with routes
* Địch has heavy area denial

#### Ưu Tiên Thông Tin

```
1. Enemy positions (before fight)
2. Extraction zone safety
3. Loot area clearance
4. Flank watch
```

***

### Chiến Lược Counter

#### Cách Counter Operator Recon

| Operator     | Counter Strategy                         |
| ------------ | ---------------------------------------- |
| **SONAR**    | Stay moving, do not get scanned in place |
| **MIRAGE**   | Do not trigger traps, check corners      |
| **OBSIDIAN** | Push through smoke, do not wait          |

#### Counter Tốt Nhất Với Recon

| Counter Pick | Why                                     |
| ------------ | --------------------------------------- |
| **MAMBA**    | Burst damage kills before intel matters |
| **TARTARUS** | CQB overwhelms fragile Recon operators  |
| **PULSE**    | Nano Swarm blocks escape routes         |

***

### Synergy

#### Duo Recon Tốt Nhất

| Partner     | Synergy         | Ghi Chú                                                 |
| ----------- | --------------- | ----------------------------------------------------- |
| **SUTURE**  | Intel + Sustain | Know threats, heal through encounters                 |
| **GLITCH**  | Scan + EMP      | Full information control — scan reveals, EMP disables |
| **MAMBA**   | Intel + Damage  | Scan position, burst down                             |
| **GOLIATH** | Intel + Tank    | Reveal flankers, GOLIATH anchors position             |

***

### Nhận Diện Hình Ảnh Top-Down

Recon operators have the **slimmest silhouette** in the roster. From the top-down camera, they are distinguished by compact tech gear and low-profile movement.

| Feature            | Design Rule                                                | Visibility |
| ------------------ | ---------------------------------------------------------- | ---------- |
| **Shoulder Width** | Narrowest in roster — 0.7x standard                        | 50+ units  |
| **Headgear**       | Tech goggles or slim hood (no bulky helmet)                | 60+ units  |
| **Color Accent**   | Cyan (#06B6D4) on goggle glow and tech strips              | 60+ units  |
| **Back Profile**   | Compact tech pack (drone, sensor kit)                      | 40+ units  |
| **Movement Anim**  | Thấp crouch-walk, smooth transitions — stealthiest movement | 40+ units  |

#### Dấu Hiệu Top-Down Riêng Của Operator

| Operator | Unique Visual From Above                                              |
| -------- | --------------------------------------------------------------------- |
| SONAR    | Cyan scanning pulse rings expanding from operator during UAV scan     |
| MIRAGE   | Small sensor device visible when placed on ground, blinking indicator |
| OBSIDIAN | Smoke cloud expanding from position, character model fades in opacity |

***

### Hồ Sơ Stamina Theo Class

| Tham Số               | Recon Giá Trị       | Comparison          |
| ----------------------- | ----------------- | ------------------- |
| **Quỹ Stamina**        | 110 (+10%)        | Above average       |
| **Hao Stamina Khi Sprint**        | 9/second (-10%)   | Efficient sprinting |
| **Tốc Độ Hồi**       | 9.6/second (+20%) | Fastest recovery    |
| **Thời Lượng Sprint Thực** | 12.2 seconds      | Best efficiency     |

**Design Intent:** Recon operators reposition frequently. They sprint to new vantage points, recover quickly, and sprint again. Efficient stamina usage reflects their mobile playstyle.

***

### Bộ Điều Chỉnh Hiệu Ứng Trạng Thái

| Hiệu Ứng | Recon Kháng | Ghi Chú                                             |
| ------ | ---------------- | ------------------------------------------------- |
| Stun   | 15%              | Partial stun resist — evasion-oriented            |
| Slow   | 0%               | Full slow duration — devastating for mobile class |
| Burn   | 0%               | Full burn damage — fragile operators              |
| EMP    | 0%               | UAV and sensors fully destroyed bởi EMP            |

**Design Intent:** Recon operators have slight stun resistance to support their evasive playstyle, but are otherwise fully vulnerable. Slow effects are especially dangerous since mobility is their core defense.

***

### Độ Phù Hợp Theo Map

| Map Archetype        | Suitability | Recommended Operator | Why                                                 |
| -------------------- | ----------- | -------------------- | --------------------------------------------------- |
| **Dense Urban**      | Highest     | MIRAGE               | Many corners and flank routes to trap               |
| **Multi-Floor**      | Cao        | SONAR                | UAV scans through floors for vertical intel         |
| **Large Industrial** | Cao        | OBSIDIAN             | Smoke breaks long sightlines, enables repositioning |
| **Tight Corridors**  | Trung bình      | SONAR                | Scan range covers entire corridor                   |
| **Open Fields**      | Thấp         | OBSIDIAN             | Only smoke provides utility, limited cover          |

See [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) for detailed map layouts.
