---
title: Specialist
linkTitle: Specialist
type: docs
weight: 5
---

### Tổng Quan Class

Operator class **Specialist** mang utility và disruption vào chiến trường. Họ mạnh ở việc counter ability của địch và kiểm soát flow combat bằng tool dựa trên công nghệ. Trong extraction shooter, information denial và area control có thể đáng giá hơn raw damage.

#### Class Identity

| Attribute | Value | Notes |
| ------------------- | -------------------- | ------------------------------------------------ |
| **Role** | Utility / Disruption | Control specialists |
| **Difficulty** | Very High | Cần timing, game sense, và hiểu enemy |
| **Team Dependency** | Medium | Enable team, solo được nếu có game knowledge |
| **Skill Ceiling** | Very High | Mastery dựa trên knowledge, không phụ thuộc aim |

#### Class Traits (All Specialist Operators)

| Trait | Effect | Gameplay Impact |
| ---------------------- | ----------------------------- | ----------------------------------------------- |
| **Expanded Inventory** | +2 Inventory Slots | Thêm loot capacity mỗi raid |
| **Tech Savvy** | +20% Gadget Interaction Speed | Hack, mở cửa, dùng terminal nhanh hơn |
| **Distracted** | -10% Weapon Accuracy | Combat penalty; bù bằng ability timing |

***

### Operators

| Operator | Codename | Specialty | Unlock |
| ------------------------------------------------------------------------------------------------------------------------------ | -------- | -------------- | ------------------------ |
| [Maya Torres](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Glitch/README.md) | GLITCH | Ability Denial | Level 15, 10,000 Credits |
| [D-84 "Ohm"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Pulse/README.md) | PULSE | Area Control | Level 28, 15,000 Credits |

***

### Playstyle Guide

#### Khi Nào Chọn Specialist

**Chọn Specialist khi:**

* Team địch dựa nhiều vào ability (Support healer, Tank shield)
* Map có cửa, terminal, hoặc environmental trap hack được
* Bạn muốn tối đa hóa loot extraction (+2 slot rất lớn cho economy)
* Team cần counter một enemy composition cụ thể

**Tránh Specialist khi:**

* Bạn thích direct combat (accuracy penalty đau với player phụ thuộc aim)
* Map mở và ít interactive object
* Team địch chơi pure Assault (không có nhiều thứ để counter)
* Team cần healing hoặc damage trực tiếp

#### Gadget Usage Tactics

**Priority Order:**

```
1. Hack equipment địch (phá trap, disable turret)
2. Dùng ability để counter enemy push (EMP / Nano Swarm)
3. Tương tác environmental object (terminal, locked door)
4. Loot hiệu quả (extra inventory slot cho item giá trị cao)
```

**Positioning:**

* Giữ mid-range; quá xa ability dễ miss, quá gần accuracy penalty khiến bạn chết
* Dùng corner và cover để deploy ability an toàn
* Đứng gần interactive object (terminal, locked room) để access nhanh nhất
* Không bao giờ làm entry fragger; để Assault dẫn đầu, bạn theo sau với denial

#### Combat Tactics

**The Counter-Play:**

1. Nhận diện enemy ability đang được dùng (shield, heal, scan)
2. Chờ timing tối ưu (ability đang ở giữa duration)
3. Deploy counter (EMP hoặc Swarm)
4. Call out enemy bị disable để team push
5. Fall back về cover trong khi ability recharge

**The Loot Run:**

1. Dùng extra inventory để mang item giá trị cao mà người khác không chứa được
2. Hack locked container để lấy exclusive loot
3. Speed-interact với terminal để reveal hidden stash
4. Ưu tiên extraction; số loot của bạn là điểm số của bạn

***

### Counter Strategies

#### Cách Counter Specialist Operators

| Operator | Counter Strategy |
| ---------- | --------------------------------------------------------------------------------------------- |
| **GLITCH** | Bait EMP trước khi dùng ability, rush trong cửa sổ cooldown 90s |
| **PULSE** | Luôn di chuyển, đừng cluster; swarm target enemy tụ nhóm. Push xuyên qua hoặc vòng quanh swarm zone |

#### Best Counters to Specialist

| Counter Pick | Why |
| ------------ | -------------------------------------------------------------- |
| **MAMBA** | Raw damage áp đảo combat power thấp trước khi ability có giá trị |
| **TARTARUS** | CQB giết Specialist trước khi gadget deploy |
| **OBSIDIAN** | Smoke chặn line of sight cho EMP targeting |

***

### Synergies

#### Best Specialist Duos

| Partner | Synergy | Notes |
| ----------- | ----------------- | --------------------------------------------------------------- |
| **SONAR** | Intel + Denial | Scan reveal, GLITCH disable; full information control |
| **GOLIATH** | Tank + Disruption | GOLIATH hấp thụ, GLITCH strip buff của địch |
| **MIRAGE** | Traps + Swarm | MIRAGE sensor detect, PULSE swarm phạt approach |
| **SUTURE** | Sustain + Utility | SUTURE giữ Specialist sống đủ lâu để gadget có giá trị |

***

### Top-Down Visual Identity

Specialist operators có **standard silhouette** với tool pocket và utility belt nhìn thấy rõ. Từ camera top-down, họ được nhận diện bằng marking amber utility và compact gadget profile.

| Feature | Design Rule | Visibility |
| ------------------ | -------------------------------------------------------- | ---------- |
| **Shoulder Width** | Standard; utility vest hơi rộng hơn Recon | 60+ units |
| **Headgear** | Work goggle đẩy lên hoặc side-mounted hacking visor | 60+ units |
| **Color Accent** | Amber (#F59E0B) utility marking và caution tape strip | 60+ units |
| **Back Profile** | Tool pack với cable và gadget holster nhìn thấy rõ | 60+ units |
| **Movement Anim** | Nhịp di chuyển standard, thỉnh thoảng có idle animation kiểm tra gadget | 50+ units |

#### Operator-Specific Top-Down Tells

| Operator | Unique Visual From Above |
| -------- | ---------------------------------------------------------------------- |
| GLITCH | Blue EMP pulse ring mở rộng rất nhanh từ vị trí operator |
| PULSE | Nano cloud bạc/xanh xoáy, nhìn như area-denial zone trên mặt đất |

***

### Class Stamina Profile

| Parameter | Specialist Value | Comparison |
| ----------------------- | ---------------- | ---------- |
| **Stamina Pool** | 100 (Standard) | Average |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8/second | Standard |
| **Net Sprint Duration** | 10.0 seconds | Average |

**Design Intent:** Specialist có stamina standard. Sức mạnh của họ đến từ gadget timing và knowledge, không phải movement. Trait +20% gadget interaction speed là lợi thế mobility riêng (hack cửa nhanh hơn, access terminal nhanh hơn).

***

### Status Effect Modifiers

| Effect | Specialist Resistance | Notes |
| ------ | --------------------- | ------------------------------------------------------- |
| Stun | 0% | Full stun duration |
| Slow | 0% | Full slow duration |
| Burn | 0% | Full burn damage |
| EMP | 50% | Half EMP duration; họ tạo ra công nghệ, nên họ chống lại nó |

**Design Intent:** Specialist operators là tech expert. Họ thiết kế EMP technology, nên có built-in shielding. Điều này tạo counter dynamic quan trọng: EMP của GLITCH kém hiệu quả hơn trước GLITCH hoặc PULSE địch so với các class khác.

***

### Map Suitability

| Map Archetype | Suitability | Recommended Operator | Why |
| -------------------- | ----------- | -------------------- | ------------------------------------------------------------- |
| **Dense Urban** | Highest | GLITCH | Nhiều cửa và terminal hack được, nhiều deployable để EMP |
| **Multi-Floor** | High | PULSE | Nano Swarm chặn stairwell và vertical access |
| **Large Industrial** | High | GLITCH | Hackable container và terminal rải khắp map |
| **Tight Corridors** | Medium | PULSE | Swarm bao phủ chiều rộng corridor để area denial |
| **Open Fields** | Low | Neither | Ít gadget để tương tác, EMP range hạn chế utility |

Xem [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) để biết layout map chi tiết.
