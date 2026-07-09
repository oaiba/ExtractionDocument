---
title: Support
linkTitle: Support
type: docs
weight: 2
---

### Tổng Quan Class

Operator class **Support** là xương sống của team, giữ đồng đội sống sót và cho phép giao tranh kéo dài. They sacrifice personal combat power for team utility.

#### Bản Sắc Class

| Thuộc Tính           | Giá Trị                 | Ghi Chú                |
| ------------------- | --------------------- | -------------------- |
| **Role**            | Team Healer / Sustain | Keep team alive      |
| **Độ Khó**      | Thấp                   | Thân thiện với người mới    |
| **Phụ Thuộc Team** | Cao                  | Best with teammates  |
| **Trần Kỹ Năng**   | Trung bình                | Positioning + timing |

#### Trait Class (Tất Cả Operator Support)

| Trait                 | Hiệu Ứng                          | Tác Động Gameplay               |
| --------------------- | ------------------------------- | ----------------------------- |
| **Medical Expertise** | +20% Hồi máu Item Effectiveness | Medkits heal 60 instead of 50 |
| **Quick Revive**      | +15% Revive Speed               | Faster teammate pickup        |
| **Slow Movement**     | -5% Movement Speed              | Slight positioning penalty    |

***

### Operator

| Operator                                                                                                                         | Codename | Chuyên Môn         | Mở Khóa                   |
| -------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------------- | ------------------------ |
| [Tariq Al-Sayed](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Suture/README.md)   | SUTURE   | Area Hồi máu      | Free Starter             |
| [Victoria Sterling](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Aegis/README.md) | AEGIS    | Damage Prevention | Level 18, 10,000 Credits |

***

### Hướng Dẫn Playstyle

#### Khi Nên Chọn Support

**Chọn Support khi:**

* Your team has aggressive players
* Map requires holding positions
* Extended engagements expected
* You want to enable teammates

**Tránh Support khi:**

* Playing solo
* Team already has a Support
* Map is wide open (no cover)
* Địch has heavy burst damage

#### Guideline Vị Trí

**Golden Rule:** Stay behind your damage dealers.

| Position    | Priority                    |
| ----------- | --------------------------- |
| Behind Tank | Highest — Protected         |
| Mid-team    | Good — Can reach everyone   |
| Flank       | Dangerous — Only for ambush |
| Front       | Never — You will die first  |

#### Ưu Tiên Hồi Máu

```
1. Low HP teammate in combat
2. Yourself (if low)
3. Pre-healing before push
4. Topping off full HP allies (low priority)
```

***

### Chiến Lược Counter

#### Cách Counter Operator Support

| Operator   | Counter Strategy                     |
| ---------- | ------------------------------------ |
| **SUTURE** | Kill drone first, then focus SUTURE  |
| **AEGIS**  | Wait for shield duration, then burst |

#### Counter Tốt Nhất Với Support

| Counter Pick | Why                              |
| ------------ | -------------------------------- |
| **MAMBA**    | Burst damage exceeds healing     |
| **TARTARUS** | CQB kills before healing matters |
| **GLITCH**   | EMP disables support abilities   |

***

### Synergy

#### Duo Support Tốt Nhất

| Partner     | Synergy           | Ghi Chú                           |
| ----------- | ----------------- | ------------------------------- |
| **MAMBA**   | Assault + Sustain | Push harder, heal after         |
| **BASTION** | Tank + Healer     | Classic defensive combo         |
| **SONAR**   | Intel + Safety    | Know when to heal, when to hide |

***

### Nhận Diện Hình Ảnh Top-Down

Support operators have a **medium silhouette** with medical/utility pack on their back as the primary identifier from above.

| Feature            | Design Rule                                             | Visibility |
| ------------------ | ------------------------------------------------------- | ---------- |
| **Shoulder Width** | Standard — between Recon and Assault                    | 60+ units  |
| **Headgear**       | Medical cap or visor with cross markings                | 60+ units  |
| **Color Accent**   | White/Green (#22C55E) on cross armband and backpack     | 80+ units  |
| **Back Profile**   | Large medical pack (SUTURE) or shield generator (AEGIS) | 80+ units  |
| **Movement Anim**  | Standard pace, slightly cautious posture                | 50+ units  |

#### Dấu Hiệu Top-Down Riêng Của Operator

| Operator | Unique Visual From Above                                            |
| -------- | ------------------------------------------------------------------- |
| SUTURE   | Green pulsing circle around Hồi máu Drone when deployed             |
| AEGIS    | Blue-white hemispherical shield dome nhìn rõ từ trên xuống when active |

***

### Hồ Sơ Stamina Theo Class

| Tham Số               | Support Giá Trị  | Comparison |
| ----------------------- | -------------- | ---------- |
| **Quỹ Stamina**        | 100 (Standard) | Trung bình    |
| **Hao Stamina Khi Sprint**        | 10/second      | Standard   |
| **Tốc Độ Hồi**       | 8/second       | Standard   |
| **Thời Lượng Sprint Thực** | 10.0 seconds   | Trung bình    |

**Design Intent:** Support has standard stamina. They do not need to sprint to engage (like Assault) or reposition (like Recon). Their -5% movement speed class trait is the real limitation, not stamina.

***

### Bộ Điều Chỉnh Hiệu Ứng Trạng Thái

| Hiệu Ứng | Support Kháng | Ghi Chú                                              |
| ------ | ------------------ | -------------------------------------------------- |
| Stun   | 0%                 | Full stun duration                                 |
| Slow   | 10%                | Slight slow resist for reaching downed allies      |
| Burn   | 0%                 | Full burn damage                                   |
| EMP    | 0%                 | Hồi máu Drone and Guardian Khiên destroyed bởi EMP |

**Design Intent:** Support has minimal resistances. Their value comes from sustaining teammates, not from personal survivability. The slight slow resist ensures they can still reach wounded allies during combat.

***

### Độ Phù Hợp Theo Map

| Map Archetype        | Suitability | Recommended Operator | Why                                                       |
| -------------------- | ----------- | -------------------- | --------------------------------------------------------- |
| **Extraction Zones** | Highest     | AEGIS                | Guardian Khiên protects team during extraction countdown |
| **Tight Corridors**  | Cao        | SUTURE               | Hồi máu Drone radius covers corridor width                |
| **Multi-Floor**      | Trung bình      | SUTURE               | Drone heals through floors if placed on correct level     |
| **Open Fields**      | Thấp         | AEGIS                | Khiên provides cover in open terrain                     |
| **Dense Urban**      | Trung bình      | Either               | Multiple engagement points require mobile healing         |

See [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) for detailed map layouts.
