---
title: Tank
linkTitle: Tank
type: docs
weight: 4
---

### Tổng Quan Class

Operator class **Tank** hứng damage và bảo vệ đồng đội. They excel at holding positions and leading pushes with their superior survivability. In an extraction shooter where every bullet matters, a Tank buys time — and time means loot.

#### Bản Sắc Class

| Thuộc Tính           | Giá Trị         | Ghi Chú                                              |
| ------------------- | ------------- | -------------------------------------------------- |
| **Role**            | Damage Sponge | Absorb and protect                                 |
| **Độ Khó**      | Trung bình        | Thân thiện với người mới mechanics, positioning matters   |
| **Phụ Thuộc Team** | Trung bình        | Better with team, can anchor solo extractions      |
| **Trần Kỹ Năng**   | Trung bình        | Positioning and cooldown management define mastery |

#### Trait Class (Tất Cả Operator Tank)

| Trait                | Hiệu Ứng                | Tác Động Gameplay                     |
| -------------------- | --------------------- | ----------------------------------- |
| **Reinforced Giáp** | +25% Maximum Giáp    | 125 armor cap (vs 100 standard)     |
| **Damage Reduction** | +10% Giáp Absorption | Take less damage through armor      |
| **Heavy Frame**      | -15% Tốc Độ Sprint     | Slow rotations, commit to positions |

***

### Operator

| Operator                                                                                                                     | Codename | Chuyên Môn          | Mở Khóa                   |
| ---------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------ | ------------------------ |
| [Mikhail Ivanov](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Bastion/README.md) | BASTION  | Frontal Protection | Level 10, 7,500 Credits  |
| [Wei Chen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Goliath/README.md)       | GOLIATH  | Team Defense       | Level 20, 12,000 Credits |

***

### Hướng Dẫn Playstyle

#### Khi Nên Chọn Tank

**Chọn Tank khi:**

* Your team needs a point leader for pushes
* Map has narrow chokepoints to hold
* Địch team has aggressive Assault operators
* You need to anchor an extraction zone

**Tránh Tank khi:**

* Map requires fast rotations between objectives
* Địch team has multiple flankers (OBSIDIAN, MIRAGE)
* Your team already has a Tank
* You are playing solo and need to cover ground quickly

#### Guideline Vị Trí

**Golden Rule:** Control space. You decide where fights happen.

| Position                      | Priority  | Why                                        |
| ----------------------------- | --------- | ------------------------------------------ |
| Chokepoint                    | Highest   | Force enemies through your kill zone       |
| Extraction Zone               | Cao      | Anchor the exit, protect looting teammates |
| Behind cover, facing approach | Good      | Reduce flanking exposure                   |
| Open ground                   | Dangerous | Even Tanks die to focus fire in the open   |

#### Tactic Combat

**The Push:**

1. Communicate intent ("Pushing left, follow me")
2. Deploy defensive ability (Khiên or Giáp Overcharge)
3. Move forward at walk speed — do not sprint
4. Draw enemy fire while teammates engage from sides
5. Hold position once you reach cover
6. Wait for cooldowns before pushing again

**The Hold:**

1. Position at extraction zone or objective
2. Deploy ability when enemy appears
3. Call out enemy positions
4. Let DPS teammates handle kills
5. Only retreat if ability is on cooldown AND health is critical

**Critical Mistake to Avoid:** Tanks often overcommit. Your job is to absorb damage, not chase kills. If your ability ends and enemies are still fighting, **fall back** and wait for cooldown. A dead Tank helps nobody.

***

### Chiến Lược Counter

#### Cách Counter Operator Tank

| Operator    | Counter Strategy                                                                     |
| ----------- | ------------------------------------------------------------------------------------ |
| **BASTION** | Flank behind the shield, use grenades around corners, wait out shield duration (15s) |
| **GOLIATH** | Focus fire before armor overcharge completes, use EMP to strip bonus armor           |

#### Counter Tốt Nhất Với Tank

| Counter Pick | Why                                                  |
| ------------ | ---------------------------------------------------- |
| **OBSIDIAN** | Smoke flanks around shield, attacks from blind angle |
| **GLITCH**   | EMP disables Khiên and strips Overcharge armor      |
| **SONAR**    | Intel reveals Tank position for flanking setup       |

***

### Synergy

#### Duo Tank Tốt Nhất

| Partner      | Synergy            | Ghi Chú                                                        |
| ------------ | ------------------ | ------------------------------------------------------------ |
| **SUTURE**   | Tank + Healer      | Sustain through any fight, classic combo                     |
| **TARTARUS** | Khiên + CQB       | BASTION leads, TARTARUS flanks behind shield chaos           |
| **IGNITION** | Tank + Area Denial | Hold chokepoint, set fire to flanking routes                 |
| **AEGIS**    | Double Defense     | Guardian Khiên + Riot Khiên = near-invulnerable extraction |

***

### Nhận Diện Hình Ảnh Top-Down

Tank operators have the **widest silhouette** in the roster. From the top-down camera, they are immediately recognizable by their broad shoulder plates and heavy armor profile.

| Feature            | Design Rule                                                 | Visibility |
| ------------------ | ----------------------------------------------------------- | ---------- |
| **Shoulder Width** | Widest in roster — 1.5x standard                            | 100+ units |
| **Headgear**       | Heavy riot visor or full-face helmet                        | 80+ units  |
| **Color Accent**   | Steel Blue (#3B82F6) on shoulder plates and visor edge      | 100+ units |
| **Back Profile**   | Khiên (BASTION) or armor pack (GOLIATH) nhìn rõ từ trên xuống | 80+ units  |
| **Movement Anim**  | Slow, deliberate trudge — heaviest footfalls in roster      | 60+ units  |

#### Dấu Hiệu Top-Down Riêng Của Operator

| Operator | Unique Visual From Above                                                        |
| -------- | ------------------------------------------------------------------------------- |
| BASTION  | Riot shield visible on back when stowed; 120-degree arc indicator when deployed |
| GOLIATH  | Glowing armor plates when Overcharge is active, blue energy pulse effect        |

***

### Hồ Sơ Stamina Theo Class

| Tham Số               | Tank Giá Trị        | Comparison             |
| ----------------------- | ----------------- | ---------------------- |
| **Quỹ Stamina**        | 80 (-20%)         | Lowest sprint duration |
| **Hao Stamina Khi Sprint**        | 12/second (+20%)  | Drains fast            |
| **Tốc Độ Hồi**       | 7.2/second (-10%) | Slow recovery          |
| **Thời Lượng Sprint Thực** | 6.7 seconds       | Shortest in roster     |

**Design Intent:** Tanks commit to positions. Sprinting to cover is a short burst, not a sustained run. This forces deliberate positioning decisions and prevents Tanks from excessively rotating.

***

### Bộ Điều Chỉnh Hiệu Ứng Trạng Thái

| Hiệu Ứng | Tank Kháng | Ghi Chú                                                         |
| ------ | --------------- | ------------------------------------------------------------- |
| Stun   | 25%             | Reduced stun duration — harder to lock down                   |
| Slow   | 25%             | Partial slow resist — already slow, further slow is punishing |
| Burn   | 10%             | Minor fire resistance from heavy armor                        |
| EMP    | 0%              | Khiên and Overcharge fully disabled bởi EMP                   |

**Design Intent:** Tanks resist physical CC effects (stun, slow) but are fully vulnerable to tech disruption (EMP). This creates the core Tank vs Specialist counterplay dynamic.

***

### Độ Phù Hợp Theo Map

| Map Archetype        | Suitability | Recommended Operator | Why                                              |
| -------------------- | ----------- | -------------------- | ------------------------------------------------ |
| **Tight Corridors**  | Highest     | BASTION              | Khiên covers entire corridor width              |
| **Extraction Zones** | Cao        | GOLIATH              | Giáp Overcharge protects team during extraction |
| **Multi-Floor**      | Trung bình      | BASTION              | Khiên protects against single-direction threats |
| **Open Fields**      | Thấp         | Neither              | Easy to flank around shield, no cover advantage  |
| **Dense Urban**      | Thấp         | Neither              | Too many angles to protect against               |

See [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) for detailed map layouts.
