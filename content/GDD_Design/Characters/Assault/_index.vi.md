---
title: Assault
linkTitle: Assault
type: docs
weight: 1
---

### Tổng Quan Class

Operator class **Assault** được thiết kế cho người chơi thích gameplay chủ động, aggressive, high-risk/high-reward. Họ mạnh ở việc mở giao tranh, gây damage, và loại bỏ threat nhanh.

#### Class Identity

| Attribute | Value | Notes |
| ------------------- | ------------------- | ---------------------------- |
| **Role** | Frontline Aggressor | Người đầu tiên vào combat |
| **Difficulty** | Medium | Tốt để học aggression |
| **Team Dependency** | Low | Solo hiệu quả |
| **Skill Ceiling** | High | Thưởng cho mechanical skill |

#### Class Traits (All Assault Operators)

| Trait | Effect | Gameplay Impact |
| ----------------- | ------------------ | --------------------------------- |
| **Sprint Boost** | +10% Sprint Speed | Rotate nhanh hơn, đuổi bắt tốt hơn |
| **Damage Boost** | +5% Weapon Damage | TTK nhanh hơn một chút |
| **Armor Penalty** | -10% Maximum Armor | Phạt positioning kém |

***

### Operators

| Operator | Codename | Specialty | Unlock |
| ------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------------- | ------------------------ |
| [Thuy Nguyen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Mamba/README.md) | MAMBA | Damage Amplification | Free Starter |
| [Ji-yoon Kwon](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Ignition/README.md) | IGNITION | Area Denial | Level 5, 5,000 Credits |
| [Carlos Mendes](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Tartarus/README.md) | TARTARUS | Close Combat | Level 22, 12,000 Credits |

***

### Playstyle Guide

#### Khi Nào Chọn Assault

**Chọn Assault khi:**

* Bạn có mechanical aim mạnh
* Team cần damage dealer
* Map có sightline mở
* Team địch mềm (không có Tank)

**Tránh Assault khi:**

* Team địch có nhiều Tank
* Map tập trung CQC (ưu tiên Recon)
* Team thiếu healing
* Bạn mới chơi game

#### Combat Tactics

**Entry Fragging:**

1. Chờ intel từ Recon
2. Pre-aim các góc phổ biến
3. Dùng ability trước engagement
4. Push chủ động
5. Call out vị trí địch

**Trading:**

* Luôn push cùng teammate
* Nếu người đầu tiên chết, trade kill
* Không ego peek khi không có backup

**Ability Timing:**

* Giữ ability cho fight quan trọng
* Không phí ability cho cleanup kill
* Coordinate với team push

***

### Counter Strategies

#### Cách Counter Assault Operators

| Operator | Counter Strategy |
| ------------ | --------------------------------------- |
| **MAMBA** | Chờ Combat Stim hết (10s), rồi engage |
| **IGNITION** | Tránh fire zone, dùng long-range |
| **TARTARUS** | Kite ở range, không để áp sát |

#### Best Counters to Assault

| Counter Pick | Why |
| ------------ | --------------------------------- |
| **BASTION** | Shield chặn toàn bộ frontal damage |
| **GLITCH** | EMP hủy tất cả Assault ability |
| **SONAR** | Intel ngăn ambush |

***

### Synergies

#### Best Assault Duos

| Partner | Synergy | Notes |
| ----------- | --------------- | --------------------------- |
| **SUTURE** | Healing sustain | Push mạnh hơn, heal sau đó |
| **SONAR** | Intel + Damage | Biết nên push đâu |
| **BASTION** | Shield + Damage | Tank dẫn trước, Assault theo sau |

#### Triple Assault Cheese

> \[!WARNING] **Không khuyến nghị** nhưng có thể hiệu quả: MAMBA + IGNITION + TARTARUS. Damage áp đảo, không có sustain. Thắng nhanh hoặc thua nhanh.

***

### Top-Down Visual Identity

Assault operators dùng **silhouette medium-athletic** với dây đạn chéo ngực nổi bật. Từ camera top-down, các đặc điểm phân biệt chính là:

| Feature | Design Rule | Visibility |
| ------------------ | -------------------------------------------------------------------------------- | ---------- |
| **Shoulder Width** | Medium (giữa Recon và Tank) | 60+ units |
| **Headgear** | Medium tactical helmet với visor glow | 60+ units |
| **Color Accent** | Orange (#F97316) trên shoulder patch và ammo belt | 80+ units |
| **Weapon Profile** | Primary weapon vươn rõ về phía trước model, barrel nhìn thấy được | 50+ units |
| **Movement Anim** | Sprint nhanh, nghiêng về trước; phân biệt với Tank trudge và Recon crouch | 40+ units |

#### Operator-Specific Top-Down Tells

| Operator | Unique Visual From Above |
| -------- | ---------------------------------------------------------- |
| MAMBA | Glow cam trên tay/cánh tay khi stim active |
| IGNITION | Fire trail phía sau nhân vật trong Incendiary Rush |
| TARTARUS | Body glow đỏ nhịp pulse trong Berserker Rage, stance lớn hơn |

***

### Class Stamina Profile

| Parameter | Assault Value | Comparison |
| ----------------------- | ----------------- | ---------------------------- |
| **Stamina Pool** | 120 (+20%) | Sprint duration dài nhất |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8.8/second (+10%) | Recovery nhanh giữa các push |
| **Net Sprint Duration** | 12.0 seconds | Best in class |

**Design Intent:** Assault operators có thể sprint tới engagement distance và vẫn còn stamina để reposition trong combat.

***

### Status Effect Modifiers

| Effect | Assault Resistance | Notes |
| ------ | ------------------ | -------------------------------------------- |
| Stun | 0% | Full stun duration; phạt reckless entry |
| Slow | 0% | Full slow duration; cực nguy hiểm nếu bị bắt |
| Burn | 0% | Full burn damage; tránh friendly fire |
| EMP | 0% | Stim và Rage bị EMP hủy |

**Design Intent:** Assault không có resistance. Sức mạnh của họ là raw damage output, không phải damage mitigation. Bị CC ability bắt trúng là punishment nặng cho positioning kém.

***

### Map Suitability

| Map Archetype | Suitability | Recommended Operator | Why |
| -------------------- | ----------- | -------------------- | ----------------------------------------------- |
| **Open Fields** | High | MAMBA | Sightline dài ưu tiên accuracy được stim boost |
| **Tight Corridors** | High | TARTARUS | Berserker Rage mạnh trong close quarters |
| **Multi-Floor** | Medium | IGNITION | Fire chặn vertical access route |
| **Large Industrial** | Medium | MAMBA or IGNITION | Tùy engagement distance |
| **Dense Urban** | Low | Any | Quá nhiều flank route, khó kiểm soát space |

Xem [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) để biết layout map chi tiết.
