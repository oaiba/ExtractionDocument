---
title: Specialist
linkTitle: Specialist
type: docs
weight: 5
---

### Tổng Quan Class

The **Specialist** class operators bring utility and disruption to the battlefield. They excel at countering enemy abilities and controlling the flow of combat through tech-based tools. In an extraction shooter, information denial and area control can be worth more than raw damage.

#### Bản Sắc Class

| Thuộc Tính           | Giá Trị                | Ghi Chú                                            |
| ------------------- | -------------------- | ------------------------------------------------ |
| **Role**            | Utility / Disruption | Control specialists                              |
| **Độ Khó**      | Rất cao            | Requires timing, game sense, and enemy knowledge |
| **Phụ Thuộc Team** | Trung bình               | Enables team, can solo with game knowledge       |
| **Trần Kỹ Năng**   | Rất cao            | Knowledge-based mastery, not aim-dependent       |

#### Trait Class (Tất Cả Operator Specialist)

| Trait                  | Hiệu Ứng                        | Tác Động Gameplay                                 |
| ---------------------- | ----------------------------- | ----------------------------------------------- |
| **Expanded Inventory** | +2 Inventory Slots            | More loot capacity per raid                     |
| **Tech Savvy**         | +20% Gadget Interaction Speed | Faster hacking, door opening, terminal use      |
| **Distracted**         | -10% Độ Chính Xác Vũ Khí          | Combat penalty — compensate with ability timing |

***

### Operator

| Operator                                                                                                                       | Codename | Chuyên Môn      | Mở Khóa                   |
| ------------------------------------------------------------------------------------------------------------------------------ | -------- | -------------- | ------------------------ |
| [Maya Torres](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Glitch/README.md) | GLITCH   | Ability Denial | Level 15, 10,000 Credits |
| [D-84 "Ohm"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Pulse/README.md)   | PULSE    | Area Control   | Level 28, 15,000 Credits |

***

### Hướng Dẫn Playstyle

#### Khi Nên Chọn Specialist

**Chọn Specialist khi:**

* Địch team relies heavily on abilities (Support healers, Tank shields)
* Map has hackable doors, terminals, or environmental traps
* You want maximum loot extraction (+2 slots is huge for economy)
* Your team needs a counter to a specific enemy composition

**Tránh Specialist khi:**

* You prefer direct combat (accuracy penalty hurts aim-dependent players)
* Map is open with few interactive objects
* Địch team is running pure Assault (nothing to counter)
* Your team needs direct healing or damage

#### Tactic Dùng Gadget

**Priority Order:**

```
1. Hack enemy equipment (destroy traps, disable turrets)
2. Use ability to counter enemy push (EMP / Nano Swarm)
3. Interact with environmental objects (terminals, locked doors)
4. Loot efficiently (extra inventory slots for high-value items)
```

**Positioning:**

* Stay mid-range — too far and abilities miss, too close and accuracy penalty kills you
* Use corners and cover to deploy abilities safely
* Position near interactive objects (terminals, locked rooms) for fastest access
* Never be the entry fragger — let Assault lead, follow with denial

#### Tactic Combat

**The Counter-Play:**

1. Identify enemy abilities in use (shields, heals, scans)
2. Wait for optimal timing (ability midway through duration)
3. Deploy counter (EMP or Swarm)
4. Call out disabled enemies for team to push
5. Fall back to cover while ability recharges

**The Loot Run:**

1. Use extra inventory to carry high-value items others cannot fit
2. Hack locked containers for exclusive loot
3. Speed-interact with terminals to reveal hidden stashes
4. Prioritize extraction — your loot count is your score

***

### Chiến Lược Counter

#### Cách Counter Operator Specialist

| Operator   | Counter Strategy                                                                              |
| ---------- | --------------------------------------------------------------------------------------------- |
| **GLITCH** | Bait EMP before using abilities, rush during 90s cooldown window                              |
| **PULSE**  | Stay mobile, don't cluster — swarm targets grouped enemies. Push through or around swarm zone |

#### Counter Tốt Nhất Với Specialist

| Counter Pick | Why                                                            |
| ------------ | -------------------------------------------------------------- |
| **MAMBA**    | Raw damage overwhelms low combat power before abilities matter |
| **TARTARUS** | CQB kills Specialist before gadgets deploy                     |
| **OBSIDIAN** | Smoke blocks line of sight for EMP targeting                   |

***

### Synergy

#### Duo Specialist Tốt Nhất

| Partner     | Synergy           | Ghi Chú                                                           |
| ----------- | ----------------- | --------------------------------------------------------------- |
| **SONAR**   | Intel + Denial    | Scan reveals, GLITCH disables — full information control        |
| **GOLIATH** | Tank + Disruption | GOLIATH absorbs, GLITCH strips enemy buffs                      |
| **MIRAGE**  | Traps + Swarm     | MIRAGE sensors detect, PULSE swarm punishes approach            |
| **SUTURE**  | Sustain + Utility | SUTURE keeps Specialist alive long enough for gadgets to matter |

***

### Nhận Diện Hình Ảnh Top-Down

Specialist operators have a **standard silhouette** with visible tool pockets and utility belts. From the top-down camera, they are identified by amber utility markings and compact gadget profiles.

| Feature            | Design Rule                                              | Visibility |
| ------------------ | -------------------------------------------------------- | ---------- |
| **Shoulder Width** | Standard — utility vest slightly wider than Recon        | 60+ units  |
| **Headgear**       | Work goggles pushed up or side-mounted hacking visor     | 60+ units  |
| **Color Accent**   | Amber (#F59E0B) utility markings and caution tape strips | 60+ units  |
| **Back Profile**   | Tool pack with visible cables and gadget holsters        | 60+ units  |
| **Movement Anim**  | Standard pace, occasional gadget-checking idle animation | 50+ units  |

#### Dấu Hiệu Top-Down Riêng Của Operator

| Operator | Unique Visual From Above                                               |
| -------- | ---------------------------------------------------------------------- |
| GLITCH   | Blue EMP pulse ring expanding rapidly from operator position           |
| PULSE    | Swirling silver/green nano cloud visible as area-denial zone on ground |

***

### Hồ Sơ Stamina Theo Class

| Tham Số               | Specialist Giá Trị | Comparison |
| ----------------------- | ---------------- | ---------- |
| **Quỹ Stamina**        | 100 (Standard)   | Trung bình    |
| **Hao Stamina Khi Sprint**        | 10/second        | Standard   |
| **Tốc Độ Hồi**       | 8/second         | Standard   |
| **Thời Lượng Sprint Thực** | 10.0 seconds     | Trung bình    |

**Design Intent:** Specialist stamina is standard. Their strength comes from gadget timing and knowledge, not from movement. The +20% gadget interaction speed class trait is their unique mobility advantage (faster door hacking, terminal access).

***

### Bộ Điều Chỉnh Hiệu Ứng Trạng Thái

| Hiệu Ứng | Specialist Kháng | Ghi Chú                                                   |
| ------ | --------------------- | ------------------------------------------------------- |
| Stun   | 0%                    | Full stun duration                                      |
| Slow   | 0%                    | Full slow duration                                      |
| Burn   | 0%                    | Full burn damage                                        |
| EMP    | 50%                   | Half EMP duration — they build the tech, they resist it |

**Design Intent:** Specialist operators are the tech experts. They designed EMP technology, so they have built-in shielding. This creates an important counter dynamic: GLITCH's EMP is less effective against enemy GLITCH or PULSE than against other classes.

***

### Độ Phù Hợp Theo Map

| Map Archetype        | Suitability | Recommended Operator | Why                                                           |
| -------------------- | ----------- | -------------------- | ------------------------------------------------------------- |
| **Dense Urban**      | Highest     | GLITCH               | Many hackable doors and terminals, lots of deployables to EMP |
| **Multi-Floor**      | Cao        | PULSE                | Nano Swarm blocks stairwells and vertical access              |
| **Large Industrial** | Cao        | GLITCH               | Hackable containers and terminals throughout                  |
| **Tight Corridors**  | Trung bình      | PULSE                | Swarm covers corridor width for area denial                   |
| **Open Fields**      | Thấp         | Neither              | Few gadgets to interact with, EMP range limits utility        |

See [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) for detailed map layouts.
