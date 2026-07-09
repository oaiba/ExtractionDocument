---
title: Tank
linkTitle: Tank
type: docs
weight: 4
---

### Tổng Quan Class

Operator class **Tank** hấp thụ damage và bảo vệ teammate. Họ mạnh ở việc giữ vị trí và dẫn đầu push nhờ survivability vượt trội. Trong extraction shooter nơi mỗi viên đạn đều quan trọng, Tank mua thời gian; và thời gian nghĩa là loot.

#### Class Identity

| Attribute | Value | Notes |
| ------------------- | ------------- | -------------------------------------------------- |
| **Role** | Damage Sponge | Hấp thụ và bảo vệ |
| **Difficulty** | Medium | Mechanic thân thiện beginner, positioning quan trọng |
| **Team Dependency** | Medium | Tốt hơn khi có team, vẫn anchor solo extraction được |
| **Skill Ceiling** | Medium | Mastery nằm ở positioning và cooldown management |

#### Class Traits (All Tank Operators)

| Trait | Effect | Gameplay Impact |
| -------------------- | --------------------- | ----------------------------------- |
| **Reinforced Armor** | +25% Maximum Armor | 125 armor cap (so với 100 standard) |
| **Damage Reduction** | +10% Armor Absorption | Nhận ít damage hơn qua armor |
| **Heavy Frame** | -15% Sprint Speed | Rotate chậm, commit vào vị trí |

***

### Operators

| Operator | Codename | Specialty | Unlock |
| ---------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------ | ------------------------ |
| [Mikhail Ivanov](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Bastion/README.md) | BASTION | Frontal Protection | Level 10, 7,500 Credits |
| [Wei Chen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Goliath/README.md) | GOLIATH | Team Defense | Level 20, 12,000 Credits |

***

### Playstyle Guide

#### Khi Nào Chọn Tank

**Chọn Tank khi:**

* Team cần point leader cho push
* Map có chokepoint hẹp để giữ
* Team địch có Assault operators aggressive
* Bạn cần anchor một extraction zone

**Tránh Tank khi:**

* Map yêu cầu rotate nhanh giữa objective
* Team địch có nhiều flanker (OBSIDIAN, MIRAGE)
* Team đã có Tank
* Bạn chơi solo và cần di chuyển phủ map nhanh

#### Positioning Guidelines

**Quy Tắc Vàng:** Kiểm soát space. Bạn quyết định fight diễn ra ở đâu.

| Position | Priority | Why |
| ----------------------------- | --------- | ------------------------------------------ |
| Chokepoint | Highest | Ép địch đi qua kill zone của bạn |
| Extraction Zone | High | Anchor exit, bảo vệ teammate đang loot |
| Behind cover, facing approach | Good | Giảm exposure từ flank |
| Open ground | Dangerous | Tank vẫn chết vì focus fire ngoài open |

#### Combat Tactics

**The Push:**

1. Communicate intent ("Pushing left, follow me")
2. Deploy defensive ability (Shield hoặc Armor Overcharge)
3. Tiến lên bằng walk speed; không sprint
4. Hút enemy fire trong khi teammate engage từ hai bên
5. Giữ vị trí khi tới cover
6. Chờ cooldown trước khi push tiếp

**The Hold:**

1. Đứng tại extraction zone hoặc objective
2. Deploy ability khi địch xuất hiện
3. Call out vị trí địch
4. Để DPS teammate xử lý kill
5. Chỉ retreat nếu ability đang cooldown VÀ health critical

**Critical Mistake to Avoid:** Tank thường overcommit. Nhiệm vụ của bạn là hấp thụ damage, không phải đuổi kill. Nếu ability hết và địch vẫn fight, **fall back** và chờ cooldown. Tank chết không giúp được ai.

***

### Counter Strategies

#### Cách Counter Tank Operators

| Operator | Counter Strategy |
| ----------- | ------------------------------------------------------------------------------------ |
| **BASTION** | Flank sau shield, dùng grenade quanh góc, chờ shield hết duration (15s) |
| **GOLIATH** | Focus fire trước khi armor overcharge hoàn tất, dùng EMP để strip bonus armor |

#### Best Counters to Tank

| Counter Pick | Why |
| ------------ | ---------------------------------------------------- |
| **OBSIDIAN** | Smoke flank quanh shield, tấn công từ blind angle |
| **GLITCH** | EMP disable Shield và strip Overcharge armor |
| **SONAR** | Intel reveal vị trí Tank để setup flank |

***

### Synergies

#### Best Tank Duos

| Partner | Synergy | Notes |
| ------------ | ------------------ | ------------------------------------------------------------ |
| **SUTURE** | Tank + Healer | Sustain qua mọi fight, classic combo |
| **TARTARUS** | Shield + CQB | BASTION dẫn đầu, TARTARUS flank sau chaos của shield |
| **IGNITION** | Tank + Area Denial | Giữ chokepoint, đốt route flank |
| **AEGIS** | Double Defense | Guardian Shield + Riot Shield = extraction gần bất khả xâm phạm |

***

### Top-Down Visual Identity

Tank operators có **silhouette rộng nhất** trong roster. Từ camera top-down, họ được nhận ra ngay bằng shoulder plate rộng và profile armor nặng.

| Feature | Design Rule | Visibility |
| ------------------ | ----------------------------------------------------------- | ---------- |
| **Shoulder Width** | Rộng nhất roster; 1.5x standard | 100+ units |
| **Headgear** | Heavy riot visor hoặc full-face helmet | 80+ units |
| **Color Accent** | Steel Blue (#3B82F6) trên shoulder plate và viền visor | 100+ units |
| **Back Profile** | Shield (BASTION) hoặc armor pack (GOLIATH) nhìn rõ từ trên | 80+ units |
| **Movement Anim** | Bước nặng, chậm, deliberate; footfall nặng nhất roster | 60+ units |

#### Operator-Specific Top-Down Tells

| Operator | Unique Visual From Above |
| -------- | ------------------------------------------------------------------------------- |
| BASTION | Riot shield nhìn thấy trên lưng khi stowed; indicator arc 120 độ khi deployed |
| GOLIATH | Armor plate glow khi Overcharge active, blue energy pulse effect |

***

### Class Stamina Profile

| Parameter | Tank Value | Comparison |
| ----------------------- | ----------------- | ---------------------- |
| **Stamina Pool** | 80 (-20%) | Sprint duration thấp nhất |
| **Sprint Drain** | 12/second (+20%) | Drain nhanh |
| **Recovery Rate** | 7.2/second (-10%) | Recovery chậm |
| **Net Sprint Duration** | 6.7 seconds | Ngắn nhất roster |

**Design Intent:** Tank commit vào vị trí. Sprint tới cover là burst ngắn, không phải sustained run. Điều này buộc quyết định positioning có chủ đích và ngăn Tank rotate quá mức.

***

### Status Effect Modifiers

| Effect | Tank Resistance | Notes |
| ------ | --------------- | ------------------------------------------------------------- |
| Stun | 25% | Giảm stun duration; khó lock down hơn |
| Slow | 25% | Partial slow resist; vốn đã chậm, slow thêm rất nặng |
| Burn | 10% | Fire resistance nhẹ từ heavy armor |
| EMP | 0% | Shield và Overcharge bị EMP disable hoàn toàn |

**Design Intent:** Tank chống lại physical CC (stun, slow) nhưng vulnerable hoàn toàn trước tech disruption (EMP). Đây là dynamic counterplay cốt lõi giữa Tank và Specialist.

***

### Map Suitability

| Map Archetype | Suitability | Recommended Operator | Why |
| -------------------- | ----------- | -------------------- | ------------------------------------------------ |
| **Tight Corridors** | Highest | BASTION | Shield che toàn bộ chiều rộng corridor |
| **Extraction Zones** | High | GOLIATH | Armor Overcharge bảo vệ team trong extraction |
| **Multi-Floor** | Medium | BASTION | Shield bảo vệ trước threat một hướng |
| **Open Fields** | Low | Neither | Dễ bị flank quanh shield, không có lợi thế cover |
| **Dense Urban** | Low | Neither | Quá nhiều angle cần bảo vệ |

Xem [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) để biết layout map chi tiết.
