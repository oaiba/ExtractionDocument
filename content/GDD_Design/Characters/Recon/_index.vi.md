---
title: Recon
linkTitle: Recon
type: docs
weight: 3
---

### Tổng Quan Class

Operator class **Recon** mạnh ở thu thập intelligence và kiểm soát luồng thông tin. Họ mở đường cho ambush, ngăn bất ngờ, và thống trị bằng kiến thức.

#### Class Identity

| Attribute | Value | Notes |
| ------------------- | --------------- | -------------------------------------- |
| **Role** | Intel & Stealth | Information is power |
| **Difficulty** | High | Cần game sense và map knowledge |
| **Team Dependency** | Medium | Intel giúp team, vẫn solo hiệu quả |
| **Skill Ceiling** | Very High | Map knowledge cực kỳ quan trọng |

#### Class Traits (All Recon Operators)

| Trait | Effect | Gameplay Impact |
| ------------------- | -------------------- | ----------------------- |
| **Sneaky Movement** | +15% Crouch Speed | Stealth movement nhanh hơn |
| **Silent Steps** | -30% Footstep Volume | Khó nghe thấy khi tiếp cận |
| **Fragile Frame** | -5% Maximum Health | Glass cannon |

***

### Operators

| Operator | Codename | Specialty | Unlock |
| ------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------- | ------------------------ |
| [Kaito Nakamura](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Sonar/README.md) | SONAR | Area Reveal | Level 8, 5,000 Credits |
| [Ananya Patel](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Mirage/README.md) | MIRAGE | Trap Detection | Level 12, 7,500 Credits |
| [Unit N-7 "Nero"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Obsidian/README.md) | OBSIDIAN | Visual Denial | Level 25, 15,000 Credits |

***

### Playstyle Guide

#### Khi Nào Chọn Recon

**Chọn Recon khi:**

* Solo hoặc team nhỏ
* Map có nhiều flank route
* Bạn biết map rõ
* Team địch có khả năng ambush

**Tránh Recon khi:**

* Map mở và đơn giản
* Team cần healing
* Bạn chưa quen route
* Địch có area denial nặng

#### Information Priority

```
1. Vị trí địch (trước fight)
2. Độ an toàn của extraction zone
3. Khu loot đã clear hay chưa
4. Canh flank
```

***

### Counter Strategies

#### Cách Counter Recon Operators

| Operator | Counter Strategy |
| ------------ | ---------------------------------------- |
| **SONAR** | Luôn di chuyển, đừng đứng yên để bị scan |
| **MIRAGE** | Không trigger trap, kiểm tra góc |
| **OBSIDIAN** | Push xuyên smoke, đừng chờ |

#### Best Counters to Recon

| Counter Pick | Why |
| ------------ | --------------------------------------- |
| **MAMBA** | Burst damage giết trước khi intel có giá trị |
| **TARTARUS** | CQB áp đảo Recon operators mỏng |
| **PULSE** | Nano Swarm chặn escape route |

***

### Synergies

#### Best Recon Duos

| Partner | Synergy | Notes |
| ----------- | --------------- | ----------------------------------------------------- |
| **SUTURE** | Intel + Sustain | Biết threat, heal xuyên encounter |
| **GLITCH** | Scan + EMP | Full information control; scan reveal, EMP disable |
| **MAMBA** | Intel + Damage | Scan position, burst down |
| **GOLIATH** | Intel + Tank | Reveal flanker, GOLIATH giữ vị trí |

***

### Top-Down Visual Identity

Recon operators có **silhouette mảnh nhất** trong roster. Từ camera top-down, họ được phân biệt bằng compact tech gear và movement low-profile.

| Feature | Design Rule | Visibility |
| ------------------ | ---------------------------------------------------------- | ---------- |
| **Shoulder Width** | Hẹp nhất roster; 0.7x standard | 50+ units |
| **Headgear** | Tech goggle hoặc slim hood (không bulky helmet) | 60+ units |
| **Color Accent** | Cyan (#06B6D4) trên goggle glow và tech strip | 60+ units |
| **Back Profile** | Compact tech pack (drone, sensor kit) | 40+ units |
| **Movement Anim** | Low crouch-walk, transition mượt; movement stealth nhất | 40+ units |

#### Operator-Specific Top-Down Tells

| Operator | Unique Visual From Above |
| -------- | --------------------------------------------------------------------- |
| SONAR | Vòng pulse scan màu cyan mở rộng từ operator trong UAV scan |
| MIRAGE | Sensor device nhỏ nhìn thấy trên mặt đất, indicator nhấp nháy |
| OBSIDIAN | Smoke cloud mở rộng từ vị trí, character model giảm opacity |

***

### Class Stamina Profile

| Parameter | Recon Value | Comparison |
| ----------------------- | ----------------- | ------------------- |
| **Stamina Pool** | 110 (+10%) | Trên trung bình |
| **Sprint Drain** | 9/second (-10%) | Sprint hiệu quả |
| **Recovery Rate** | 9.6/second (+20%) | Recovery nhanh nhất |
| **Net Sprint Duration** | 12.2 seconds | Best efficiency |

**Design Intent:** Recon operators reposition thường xuyên. Họ sprint tới vantage point mới, recover nhanh, rồi sprint tiếp. Stamina usage hiệu quả phản ánh playstyle cơ động.

***

### Status Effect Modifiers

| Effect | Recon Resistance | Notes |
| ------ | ---------------- | ------------------------------------------------- |
| Stun | 15% | Partial stun resist; hướng về evasion |
| Slow | 0% | Full slow duration; cực nguy hiểm cho class cơ động |
| Burn | 0% | Full burn damage; operator mỏng |
| EMP | 0% | UAV và sensor bị EMP phá hoàn toàn |

**Design Intent:** Recon operators có stun resistance nhẹ để hỗ trợ playstyle né tránh, nhưng ngoài ra vẫn hoàn toàn vulnerable. Slow effect đặc biệt nguy hiểm vì mobility là core defense của họ.

***

### Map Suitability

| Map Archetype | Suitability | Recommended Operator | Why |
| -------------------- | ----------- | -------------------- | --------------------------------------------------- |
| **Dense Urban** | Highest | MIRAGE | Nhiều góc và flank route để đặt trap |
| **Multi-Floor** | High | SONAR | UAV scan xuyên floor cho vertical intel |
| **Large Industrial** | High | OBSIDIAN | Smoke cắt sightline dài, giúp reposition |
| **Tight Corridors** | Medium | SONAR | Scan range bao phủ toàn corridor |
| **Open Fields** | Low | OBSIDIAN | Chỉ smoke có utility, cover hạn chế |

Xem [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) để biết layout map chi tiết.
