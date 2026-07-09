---
title: Assault
linkTitle: Assault
type: docs
weight: 1
---

### Tổng Quan Class

Operator class **Assault** dành cho người chơi thích gameplay hổ báo, chủ động và risk/reward cao. They excel at leading charges, dealing damage, and eliminating threats quickly.

#### Bản Sắc Class

| Thuộc Tính           | Giá Trị               | Ghi Chú                        |
| ------------------- | ------------------- | ---------------------------- |
| **Role**            | Frontline Aggressor | First into combat            |
| **Độ Khó**      | Trung bình              | Good for learning aggression |
| **Phụ Thuộc Team** | Thấp                 | Can solo effectively         |
| **Trần Kỹ Năng**   | Cao                | Rewards mechanical skill     |

#### Trait Class (Tất Cả Operator Assault)

| Trait             | Hiệu Ứng             | Tác Động Gameplay                   |
| ----------------- | ------------------ | --------------------------------- |
| **Sprint Boost**  | +10% Tốc Độ Sprint  | Faster rotations, chase potential |
| **Damage Boost**  | +5% Vũ khí Damage  | Slightly faster TTK               |
| **Giáp Penalty** | -10% Maximum Giáp | Punishes poor positioning         |

***

### Operator

| Operator                                                                                                                        | Codename | Chuyên Môn            | Mở Khóa                   |
| ------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------------- | ------------------------ |
| [Thuy Nguyen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Mamba/README.md)      | MAMBA    | Damage Amplification | Free Starter             |
| [Ji-yoon Kwon](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Ignition/README.md)  | IGNITION | Area Denial          | Level 5, 5,000 Credits   |
| [Carlos Mendes](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Tartarus/README.md) | TARTARUS | Close Combat         | Level 22, 12,000 Credits |

***

### Hướng Dẫn Playstyle

#### Khi Nên Chọn Assault

**Chọn Assault khi:**

* You have strong mechanical aim
* Your team needs a damage dealer
* The map has open sightlines
* Địch team is squishy (no Tank)

**Tránh Assault khi:**

* Địch team has multiple Tanks
* Map is CQC-focused (favor Recon)
* Your team lacks healing
* You are new to the game

#### Tactic Combat

**Entry Fragging:**

1. Wait for intel from Recon
2. Pre-aim common angles
3. Use ability before engagement
4. Push with aggression
5. Call out enemy positions

**Trading:**

* Always push with a teammate
* If first player dies, trade the kill
* Do not ego peek without backup

**Ability Timing:**

* Save ability for key fights
* Do not waste on cleanup kills
* Coordinate with team pushes

***

### Chiến Lược Counter

#### Cách Counter Operator Assault

| Operator     | Counter Strategy                        |
| ------------ | --------------------------------------- |
| **MAMBA**    | Wait out Combat Stim (10s), then engage |
| **IGNITION** | Avoid fire zones, use long-range        |
| **TARTARUS** | Kite at range, do not let close         |

#### Counter Tốt Nhất Với Assault

| Counter Pick | Why                               |
| ------------ | --------------------------------- |
| **BASTION**  | Khiên blocks all frontal damage  |
| **GLITCH**   | EMP cancels all Assault abilities |
| **SONAR**    | Intel prevents ambush             |

***

### Synergy

#### Duo Assault Tốt Nhất

| Partner     | Synergy         | Ghi Chú                       |
| ----------- | --------------- | --------------------------- |
| **SUTURE**  | Hồi máu sustain | Push harder, heal after     |
| **SONAR**   | Intel + Damage  | Know where to push          |
| **BASTION** | Khiên + Damage | Tank leads, Assault follows |

#### Triple Assault Cheese

> \[!WARNING] **Not Recommended** but can work: MAMBA + IGNITION + TARTARUS. Overwhelming damage, no sustain. Win fast or lose fast.

***

### Nhận Diện Hình Ảnh Top-Down

Assault operators share a **medium-athletic silhouette** with prominent cross-chest ammo belts. From the top-down camera, the key distinguishing features are:

| Feature            | Design Rule                                                                      | Visibility |
| ------------------ | -------------------------------------------------------------------------------- | ---------- |
| **Shoulder Width** | Trung bình (between Recon and Tank)                                                  | 60+ units  |
| **Headgear**       | Trung bình tactical helmet with visor glow                                           | 60+ units  |
| **Color Accent**   | Orange (#F97316) trên patch vai and ammo belt                               | 80+ units  |
| **Vũ khí Profile** | Primary weapon extends forward from model, visible barrel                        | 50+ units  |
| **Movement Anim**  | Fast, forward-leaning sprint — distinguishable from Tank trudge and Recon crouch | 40+ units  |

#### Dấu Hiệu Top-Down Riêng Của Operator

| Operator | Unique Visual From Above                                   |
| -------- | ---------------------------------------------------------- |
| MAMBA    | Orange glow on hands/arms when stim is active              |
| IGNITION | Lửa trail visible behind character during Incendiary Rush |
| TARTARUS | Red pulsing body glow during Berserker Rage, larger stance |

***

### Hồ Sơ Stamina Theo Class

| Tham Số               | Assault Giá Trị     | Comparison                   |
| ----------------------- | ----------------- | ---------------------------- |
| **Quỹ Stamina**        | 120 (+20%)        | Longest sprint duration      |
| **Hao Stamina Khi Sprint**        | 10/second         | Standard                     |
| **Tốc Độ Hồi**       | 8.8/second (+10%) | Fast recovery between pushes |
| **Thời Lượng Sprint Thực** | 12.0 seconds      | Best in class                |

**Design Intent:** Assault operators can sprint to engagement distance and have stamina remaining for repositioning during combat.

***

### Bộ Điều Chỉnh Hiệu Ứng Trạng Thái

| Hiệu Ứng | Assault Kháng | Ghi Chú                                        |
| ------ | ------------------ | -------------------------------------------- |
| Stun   | 0%                 | Full stun duration — punishes reckless entry |
| Slow   | 0%                 | Full slow duration — devastating if caught   |
| Burn   | 0%                 | Full burn damage — avoid friendly fire       |
| EMP    | 0%                 | Stim and Rage cancelled bởi EMP               |

**Design Intent:** Assault has zero resistances. Their strength is raw damage output, not damage mitigation. Being caught by CC abilities is a hard punishment for bad positioning.

***

### Độ Phù Hợp Theo Map

| Map Archetype        | Suitability | Recommended Operator | Why                                             |
| -------------------- | ----------- | -------------------- | ----------------------------------------------- |
| **Open Fields**      | Cao        | MAMBA                | Long sightlines favor stim-boosted accuracy     |
| **Tight Corridors**  | Cao        | TARTARUS             | Berserker Rage excels in close quarters         |
| **Multi-Floor**      | Trung bình      | IGNITION             | Lửa denies vertical access routes              |
| **Large Industrial** | Trung bình      | MAMBA or IGNITION    | Depends on engagement distance                  |
| **Dense Urban**      | Thấp         | Any                  | Too many flanking routes, hard to control space |

See [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) for detailed map layouts.
