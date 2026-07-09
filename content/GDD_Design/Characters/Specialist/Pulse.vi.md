---
title: "PULSE - D-84 \"Ohm\""
type: docs
---

## Hồ Sơ Operator

> *"Nanobot của tôi thấy mọi thứ. Cảm nhận mọi thứ. Kiểm soát mọi thứ."*

### Thông Tin Cơ Bản

| Thuộc Tính       | Giá Trị               |
| :-------------- | :------------------ |
| **Tên Thật**   | D-84 "Ohm" |
| **Codename**    | PULSE |
| **Class**       | Specialist          |
| **Quốc Tịch** | German |
| **Tuổi**         | 31                  |
| **Chiều Cao**      | 173 cm (5'8")       |
| **Cân Nặng**      | 65 kg (143 lbs)     |

### Lý Lịch

D-84 "Ohm" từng là nhà nghiên cứu nanotechnology hàng đầu tại Cambridge University, tiên phong ứng dụng nanobot trong y học. Đột phá của cô về nano-swarm lập trình được lẽ ra có thể cách mạng hóa y học, cho đến khi một tập đoàn dược phẩm đánh cắp nghiên cứu và vũ khí hóa nó.

Khi mọi nỗ lực vạch trần chúng qua kênh pháp lý thất bại, Maya tự mình hành động. Cô tái tạo công nghệ từ trí nhớ và giờ dùng nó trong Exclusion Zone, chứng minh rằng tạo vật của cô có thể cứu mạng người và kết liễu những kẻ lạm dụng quyền lực.

### Tính Cách

- **Brilliant** - Trí tuệ cấp thiên tài
- **Driven** - Ám ảnh với việc chứng minh giá trị bản thân
- **Compassionate** - Dùng công nghệ để giúp người khác, không chỉ để gây hại
- **Vindictive** - Không bao giờ quên điều sai trái đã chịu

---

## Thông Số Combat

### Chỉ Số Cơ Bản

| Stat                | Giá Trị   | Bộ Điều Chỉnh Class | Cuối Cùng   |
| :------------------ | :------ | :------------- | :------ |
| **Máu**          | 100 HP  | -              | 100 HP  |
| **Giáp**           | 50      | -              | 50      |
| **Tốc Độ Sprint**    | 5.5 m/s | -              | 5.5 m/s |
| **Tốc Độ Đi Bộ**      | 3.5 m/s | -              | 3.5 m/s |
| **Độ Chính Xác Vũ Khí** | 100%    | -10%           | 90%     |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 100 | Standard (Specialist class) |
| **Hao Stamina Khi Sprint** | 10/second | Standard |
| **Tốc Độ Hồi** | 8/second | Standard |
| **Thời Lượng Sprint Thực** | 10.0 seconds | Trung bình |
| **Âm Lượng Bước Chân** | 95% | Standard — tactical sneakers |
| **Bán Kính Audio Ability** | 25 meters | Swarm buzzing is moderate volume |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 0% | Đủ thời lượng |
| Slow | 0% | Đủ thời lượng |
| Burn | 0% | Full DoT |
| EMP | 0% | Nano Swarm destroyed bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 36 cm radius, 168 cm height |
| **Vùng Đầu** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette Nhìn Từ Trên Xuống** | Slim build, nano-canister harness on chest, tech goggles |
| **Vùng Accent Theo Class** | Yellow (#EAB308) on harness strips and goggle glow |
| **Swarm VFX (Top-Down)** | Silver particle cloud on ground (6m radius), shimmering/pulsing |
| **Swarm Audio Radius** | 25m — persistent insect-like buzzing |

<!-- REF_IMAGE: PULSE top-down view — showing operator with Nano Swarm deployed, silver particle cloud visible from above as 6m radius shimmer -->

### Nano Swarm Stat Block

| Thuộc Tính | Giá Trị | Ghi Chú |
| :------- | :---- | :---- |
| **Swarm Radius** | 6 meters | Stationary (can be redirected) |
| **Swarm Chiều Cao** | 3 meters | Covers ground to upper floor |
| **Địch Damage** | 8 HP/second | Tick every 0.5s |
| **Đồng minh Hồi máu** | 4 HP/second | Half of damage rate |
| **Địch Slow** | -20% movement | While in swarm |
| **Duration** | 12 seconds | Full lifetime |
| **EMP Vulnerability** | Dispersed instantly | Primary counter |
| **Lửa Interaction** | Not affected | Lửa does not destroy nanobots |

### Độ Khó

**Độ Khó: 4/5** — Swarm placement and redirection require spatial awareness. Dual-purpose (damage + heal) means constant decision-making about positioning.


## Ability

### Active Ability: Nano Swarm

> *"Deploy a cloud of nanobots that damages enemies and heals allies in the area."*

| Thuộc Tính     | Giá Trị      |
| :----------- | :--------- |
| **Cooldown** | 90 seconds |
| **Duration** | 12 seconds |
| **Charges**  | 1          |

#### Hiệu Ứng

| Hiệu Ứng  | Target           | Giá Trị              |
| :------ | :--------------- | :----------------- |
| Damage  | Địch in swarm | 8 HP/second        |
| Hồi máu | Đồng minh in swarm  | 4 HP/second        |
| Slow    | Địch          | -20% movement      |
| Vision  | Địch          | Reduced visibility |

#### Rule Tương Tác Swarm

| Interaction | Result |
| :---------- | :----- |
| **Swarm + EMP (GLITCH)** | Swarm dispersed instantly — primary counter |
| **Swarm + Lửa (IGNITION)** | Both effects stack on enemies in overlap zone |
| **Swarm + Smoke (OBSIDIAN)** | Swarm operates through smoke normally |
| **Swarm + AEGIS Khiên** | Swarm passes through Guardian Khiên |
| **Swarm + BASTION Khiên** | Swarm ignores Riot Khiên — passes through |
| **Swarm + MIRAGE Sensors** | Swarm does not affect sensors |
| **Swarm + SUTURE Drone** | Swarm heal + drone heal stack on allies |

#### VFX Swarm Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Swarm deploy | Canister crack, silver particles expand to 6m radius |
| Swarm active | Shimmering silver cloud on ground, semi-transparent |
| Địch in swarm | Red damage particles trail toward enemy |
| Đồng minh in swarm | Green healing particles trail toward ally |
| Swarm redirected | Cloud moves toward new target position |
| Swarm ending | Particles settle downward, shimmer fades |
| Swarm EMP'd | Brief blue flash, all particles scatter and vanish |


| Thuộc Tính   | Giá Trị                          |
| :--------- | :----------------------------- |
| Radius     | 6 meters                       |
| Chiều Cao     | 3 meters                       |
| Mobility   | Stationary (can be redirected) |
| Visibility | Cloud of silver particles      |

#### Cách Dùng Tactical

| Use Case             | Strategy                          |
| :------------------- | :-------------------------------- |
| **Area Denial**      | Block chokepoint                  |
| **Combat Support**   | Heal team while damaging enemies  |
| **Extraction Hold**  | Place over extraction zone        |
| **Chase Prevention** | Swarm behind you while retreating |

#### Slot Upgrade

**Slot 1 (Level 5):**
| Option                | Hiệu Ứng                           |
| :-------------------- | :------------------------------- |
| **Extended Swarm**    | Duration +6 seconds (18s total)  |
| **Quick Replication** | Cooldown -20 seconds (70s total) |
| **Dense Cloud**       | Damage +3 HP/sec (11 total)      |

**Slot 2 (Level 20):**
| Option               | Hiệu Ứng                            |
| :------------------- | :-------------------------------- |
| **Medical Protocol** | Hồi máu +3 HP/sec (7 total)       |
| **Corrosive Bots**   | Địch in swarm take +10% damage |
| **Mobile Swarm**     | Swarm slowly follows PULSE (1 m/s) |

**Slot 3 (Level 35):**
| Option                | Hiệu Ứng                           |
| :-------------------- | :------------------------------- |
| **Symbiosis**         | PULSE heals double in own swarm   |
| **Giáp Dissolution** | Swarm reduces enemy armor by 20% |
| **Dual Deployment**   | 2 smaller swarms instead of 1    |

---

### Passive Ability: Nano-Infused

> *"The nanobots in her blood work constantly."*

| Điều Kiện               | Hiệu Ứng                            |
| :---------------------- | :-------------------------------- |
| Out of combat 5 seconds | Regenerate 2 HP/second            |
| In own swarm            | +10% movement speed               |
| Damaged by enemy swarm  | Take 50% less damage (resistance) |

**Design Intent:** Bản thân-sustaining operator who excels in attrition warfare.

---

## Loadout

### Loadout Mặc Định

| Slot          | Item                        | Ghi Chú                         |
| :------------ | :-------------------------- | :---------------------------- |
| **Primary**   | P90                         | Cao capacity                 |
| **Secondary** | G17 Pistol                  | Standard                      |
| **Tactical**  | Nano Grenades ×2, Medkit ×1 | Extra swarms + backup healing |
| **Giáp**     | Trung bình Vest                 | 50 armor                      |

### Loadout Khuyến Nghị

**Full Nano:**
| Slot      | Item            | Why               |
| :-------- | :-------------- | :---------------- |
| Primary   | MP7             | Compact, accurate |
| Secondary | Machine Pistol  | CQB backup        |
| Tactical  | Nano Grenade ×3 | Maximum coverage  |

**Survival Focus:**
| Slot      | Item               | Why                      |
| :-------- | :----------------- | :----------------------- |
| Primary   | Vector             | Fast TTK                 |
| Secondary | G17                | Reliable                 |
| Tactical  | Medkit ×2, Nano ×1 | Passive + active healing |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Area Control
- Place swarms at key locations
- Zone enemies away from objectives
- Provide ambient healing

**Secondary Role:** Hybrid Support
- Not a full healer, but supplements SUTURE/AEGIS
- Bản thân-sustaining flanker
- Extended presence in combat

### Đặt Swarm

**Good Placement:**
- Chokepoints
- Objectives (extraction, loot)
- Behind cover for healing
- Entry points to slow enemies

**Bad Placement:**
- Wide open areas (easy to avoid)
- Where team won't benefit
- Before enemies arrive (waste duration)

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent    | Why Favorable                | Tactic                 |
| :---------- | :--------------------------- | :--------------------- |
| **MAMBA**   | Swarm slows his rush         | Fight in swarm         |
| **TARTARUS**   | Slows his CQB approach       | Keep distance in swarm |
| **BASTION** | Swarm damages through shield | Surround with nano     |

### Kèo Cân Bằng

| Opponent     | Ghi Chú               | Key to Winning             |
| :----------- | :------------------ | :------------------------- |
| **SUTURE**      | Both sustain        | Your damage vs his healing |
| **GOLIATH** | Giáp vs nano       | Focus single target        |
| **MIRAGE**  | Control specialists | Map control battle         |

### Kèo Bất Lợi

| Opponent    | Why Difficult         | Counter Strategy   |
| :---------- | :-------------------- | :----------------- |
| **GLITCH**  | EMP destroys swarm    | Deploy after EMP   |
| **IGNITION**   | Lửa damages you back | Avoid fire zones   |
| **SONAR** | Can see you in swarm  | Move unpredictably |

---

## Câu Thoại

### Combat

| Trigger                 | Line                                |
| :---------------------- | :---------------------------------- |
| Ability Activation      | "Swarm deployed. They're learning." |
| Địch in Swarm          | "They're feeling it now."           |
| Đồng minh in Swarm (Hồi máu) | "Let the nanobots work."            |
| Kill                    | "Science wins."                     |
| Reviving                | "The bots will stabilize you."      |

### Tính Cách

| Trigger            | Line                               |
| :----------------- | :--------------------------------- |
| Match Start        | "Nanobots online. Let's begin."    |
| Extraction Success | "Research successful. Extracting." |
| Thấp Máu         | "Bots are working on it."          |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** White lab coat over lightweight tactical vest, nanobot canisters on belt
- **Headgear:** Cao-tech visor / AR glasses with data readouts
- **Gloves:** White latex gloves (medical/scientific aesthetic)
- **Features:** Short natural hair, confident stance, silver nano-trace patterns on forearms

<!-- REF_IMAGE: PULSE default skin — top-down view showing lab coat over vest silhouette, AR glasses, nano canisters visible on belt, silver-particle aura effect -->

### Skin Có Thể Mở Khóa

| Skin | Rarity | Mở Khóa |
| :--- | :----- | :----- |
| **Lab Technician** | Common | Level 10 |
| **Biohazard** | Uncommon | 1,000 Credits |
| **Nanosuit** | Rare | Level 25 |
| **Synthwave** | Epic | Battle Pass S2 |
| **Singularity** | Legendary | Season 4 Event |

### Vật Phẩm Signature

| Item | Mô Tả |
| :--- | :---------- |
| **Nano Canisters** | Glowing silver canisters on belt harness |
| **Cambridge Pin** | University crest pin on lab coat lapel |
| **Silver Trace** | Faint silver nano-patterns visible on forearms (the bots in her blood) |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character | Relationship |
| :-------- | :----------- |
| **GLITCH** | Fellow outcasts, share tech knowledge — closest friend/collaborator |
| **SUTURE** | Medical debate partners — SUTURE uses traditional medicine, PULSE uses nanotech. Mutual professional respect |
| **AEGIS** | Faith vs Science discussions — AEGIS prays, PULSE programs. Surprisingly good friends |
| **MAMBA** | MAMBA finds her nanobots unsettling — "Keep those things away from me" |

### Hook Câu Chuyện

- Hunting the executives who stole her research at the pharmaceutical conglomerate
- Developing new nanobot applications in the field (quest chain: test prototypes for rewards)
- Secretly working on a cure for SUTURE's chronic condition using nano-medicine
- Discovered that Corporation is mass-producing her stolen nano-swarm tech for military use

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Swarm is the only dual-purpose ability (damage + heal) — monitor effective healing per match
- Stationary deployment is the primary weakness — enemies can simply walk away
- Mobile Swarm upgrade (Slot 2) should cap at 1 m/s movement — too fast makes it oppressive
- Dual Deployment (Slot 3) splits radius — 2x 4m swarms instead of 1x 6m, total area is less
- EMP hard-counters Nano Swarm — this is intentional and should NOT be changed
- Bản thân-healing passive (2 HP/sec out of combat) prevents chip-damage attrition — 5 second delay is critical
- Symbiosis upgrade (double heal in own swarm) makes PULSE nearly unkillable in swarm — she must sacrifice other Slot 3 options

### Ghi Chú Kỹ Thuật

| System | Ghi Chú |
| :----- | :---- |
| Swarm Particles | GPU particle system, limit 5000 particles per swarm |
| Damage Tick | Every 0.5 seconds (8 x 2 = 16 ticks per 12s duration) |
| Đồng minh/Địch Detection | Server-side detection, client-side visual feedback |
| Dual Swarm | Each swarm is independent particle system |

### Yêu Cầu Animation

- Swarm deploy animation (0.7 seconds — throw canister, nanobots emerge)
- Swarm active VFX (silver particle cloud, shimmering, semi-transparent)
- Hồi máu VFX (green particle trails toward allies in swarm)
- Damage VFX (red particle trails targeting enemies in swarm)
- Death animation: nanobots visibly scatter from body (dramatic tech failure)

### Yêu Cầu Audio

| Sound | Ghi Chú |
| :---- | :---- |
| Swarm deploy | Canister crack + rising electronic buzz |
| Swarm active | Persistent insect-like buzzing (louder near center) |
| Swarm healing | Soft harmonic hum overlay (ally feedback) |
| Swarm damage | Aggressive buzz + crackling (enemy perspective) |
| Swarm end | Descending buzz, particles settle |
| Footsteps | Standard weight — tactical sneakers |

### Ghi Chú Riêng Cho Top-Down

- Swarm silver cloud must be visible at minimum zoom — area denial information for both teams
- Red (enemy damage) and green (ally heal) particle streams provide instant team understanding from above
- Swarm cloud should be clearly distinct from OBSIDIAN smoke: silver/shimmering vs gray/opaque
- Dual Deployment upgrade splits into 2x 4m swarms — each should be independently visible
- Swarm redirection animation should show cloud flowing toward new position (1-2 second travel time)
- -10% weapon accuracy (Specialist class) means PULSE should avoid straight gunfights
