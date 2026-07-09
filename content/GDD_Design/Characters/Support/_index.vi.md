---
title: Support
linkTitle: Support
type: docs
weight: 2
---

### Tổng Quan Class

Operator class **Support** là xương sống của mọi team, giữ đồng đội sống sót và cho phép engagement kéo dài. Họ hy sinh combat power cá nhân để đổi lấy team utility.

#### Class Identity

| Attribute | Value | Notes |
| ------------------- | --------------------- | -------------------- |
| **Role** | Team Healer / Sustain | Giữ team sống |
| **Difficulty** | Low | Thân thiện beginner |
| **Team Dependency** | High | Tốt nhất khi có teammate |
| **Skill Ceiling** | Medium | Positioning + timing |

#### Class Traits (All Support Operators)

| Trait | Effect | Gameplay Impact |
| --------------------- | ------------------------------- | ----------------------------- |
| **Medical Expertise** | +20% Healing Item Effectiveness | Medkit heal 60 thay vì 50 |
| **Quick Revive** | +15% Revive Speed | Dựng teammate nhanh hơn |
| **Slow Movement** | -5% Movement Speed | Penalty positioning nhẹ |

***

### Operators

| Operator | Codename | Specialty | Unlock |
| -------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------------- | ------------------------ |
| [Tariq Al-Sayed](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Suture/README.md) | SUTURE | Area Healing | Free Starter |
| [Victoria Sterling](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Aegis/README.md) | AEGIS | Damage Prevention | Level 18, 10,000 Credits |

***

### Playstyle Guide

#### Khi Nào Chọn Support

**Chọn Support khi:**

* Team có người chơi aggressive
* Map yêu cầu giữ vị trí
* Dự kiến engagement kéo dài
* Bạn muốn enable teammate

**Tránh Support khi:**

* Chơi solo
* Team đã có Support
* Map quá mở (không có cover)
* Địch có burst damage nặng

#### Positioning Guidelines

**Quy Tắc Vàng:** Đứng phía sau damage dealer của bạn.

| Position | Priority |
| ----------- | --------------------------- |
| Behind Tank | Cao nhất; được bảo vệ |
| Mid-team | Tốt; chạm tới mọi người |
| Flank | Nguy hiểm; chỉ dùng để ambush |
| Front | Không bao giờ; bạn sẽ chết đầu tiên |

#### Healing Priority

```
1. Teammate low HP đang trong combat
2. Bản thân (nếu thấp)
3. Pre-healing trước khi push
4. Topping off đồng đội gần full HP (low priority)
```

***

### Counter Strategies

#### Cách Counter Support Operators

| Operator | Counter Strategy |
| ---------- | ------------------------------------ |
| **SUTURE** | Giết drone trước, rồi focus SUTURE |
| **AEGIS** | Chờ shield hết duration, rồi burst |

#### Best Counters to Support

| Counter Pick | Why |
| ------------ | -------------------------------- |
| **MAMBA** | Burst damage vượt healing |
| **TARTARUS** | CQB giết trước khi healing có giá trị |
| **GLITCH** | EMP disable support ability |

***

### Synergies

#### Best Support Duos

| Partner | Synergy | Notes |
| ----------- | ----------------- | ------------------------------- |
| **MAMBA** | Assault + Sustain | Push mạnh hơn, heal sau đó |
| **BASTION** | Tank + Healer | Defensive combo kinh điển |
| **SONAR** | Intel + Safety | Biết khi nào heal, khi nào hide |

***

### Top-Down Visual Identity

Support operators có **medium silhouette** với medical/utility pack trên lưng là identifier chính từ phía trên.

| Feature | Design Rule | Visibility |
| ------------------ | ------------------------------------------------------- | ---------- |
| **Shoulder Width** | Standard; giữa Recon và Assault | 60+ units |
| **Headgear** | Medical cap hoặc visor có cross marking | 60+ units |
| **Color Accent** | White/Green (#22C55E) trên cross armband và backpack | 80+ units |
| **Back Profile** | Medical pack lớn (SUTURE) hoặc shield generator (AEGIS) | 80+ units |
| **Movement Anim** | Nhịp di chuyển standard, posture hơi cẩn trọng | 50+ units |

#### Operator-Specific Top-Down Tells

| Operator | Unique Visual From Above |
| -------- | ------------------------------------------------------------------- |
| SUTURE | Vòng xanh pulse quanh Healing Drone khi deployed |
| AEGIS | Dome shield xanh-trắng bán cầu nhìn rõ từ trên khi active |

***

### Class Stamina Profile

| Parameter | Support Value | Comparison |
| ----------------------- | -------------- | ---------- |
| **Stamina Pool** | 100 (Standard) | Average |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8/second | Standard |
| **Net Sprint Duration** | 10.0 seconds | Average |

**Design Intent:** Support có stamina standard. Họ không cần sprint để engage (như Assault) hoặc reposition (như Recon). Trait -5% movement speed mới là giới hạn thật, không phải stamina.

***

### Status Effect Modifiers

| Effect | Support Resistance | Notes |
| ------ | ------------------ | -------------------------------------------------- |
| Stun | 0% | Full stun duration |
| Slow | 10% | Slight slow resist để tới được đồng đội downed |
| Burn | 0% | Full burn damage |
| EMP | 0% | Healing Drone và Guardian Shield bị EMP phá |

**Design Intent:** Support gần như không có resistance. Giá trị của họ đến từ sustain teammate, không phải personal survivability. Slow resist nhẹ đảm bảo họ vẫn có thể tới được đồng đội bị thương trong combat.

***

### Map Suitability

| Map Archetype | Suitability | Recommended Operator | Why |
| -------------------- | ----------- | -------------------- | --------------------------------------------------------- |
| **Extraction Zones** | Highest | AEGIS | Guardian Shield bảo vệ team trong extraction countdown |
| **Tight Corridors** | High | SUTURE | Healing Drone radius bao phủ chiều rộng corridor |
| **Multi-Floor** | Medium | SUTURE | Drone heal xuyên floor nếu đặt đúng level |
| **Open Fields** | Low | AEGIS | Shield cung cấp cover trên địa hình mở |
| **Dense Urban** | Medium | Either | Nhiều engagement point cần mobile healing |

Xem [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) để biết layout map chi tiết.
