---
title: Characters & Operators
linkTitle: Characters
type: docs
weight: 3
sidebar:
  open: false
---

### Thứ Bậc Squad

Trong **Extraction Shooter**, nhân vật không chỉ được định nghĩa bằng chỉ số, mà bằng tactical utility trong squad. Mọi operator đều có thể bắn và loot, nhưng ability riêng của họ định hình nhịp combat.

> \[!NOTE] **Philosophy:** Không có "DPS" hay "Tank" theo nghĩa MMO truyền thống. Mọi viên đạn đều nguy hiểm. Role cung cấp _utility_ và _sustain_, không phải bất tử.

#### Danh Sách Class

{{< cards cols="3" >}}
{{< card link="Assault/" title="Assault" icon="fire" subtitle="Fragger. Breacher. Mở giao tranh tuyến đầu." >}}
{{< card link="Recon/" title="Recon" icon="eye" subtitle="Thu thập intel. Sniping. Flanking." >}}
{{< card link="Support/" title="Support" icon="plus-circle" subtitle="Hồi máu. Đạn resupply. Utility." >}}
{{< card link="Tank/" title="Tank" icon="shield-check" subtitle="Khóa khu vực. Vũ khí hạng nặng. Crowd control." >}}
{{< card link="Specialist/" title="Specialist" icon="chip" subtitle="Cyberwarfare. Trap. Gadget." >}}
{{< /cards >}}

***

### Triết Lý Thiết Kế

#### Nguyên Tắc Cốt Lõi

| Nguyên Tắc               | Mô Tả                                            | Ví Dụ                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Class Identity**      | Mỗi class có combat role rõ ràng                   | Tank = Damage absorption                                                                                                                                        |
| **Character Diversity** | Mỗi class có nhiều nhân vật với ability khác nhau | 2 operator Assault có stim khác nhau                                                                                                                        |
| **Visual Clarity**      | Nhận diện tức thì từ góc nhìn top-down                 | Silhouette và theme màu riêng (xem [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md)) |
| **Balanced Power**      | Ability bổ trợ skill, không thay thế skill             | +25% damage, không phải instant kill                                                                                                                                   |
| **Risk/Reward**         | Lối chơi hổ báo phải có trade-off                         | Damage cao = survivability thấp hơn                                                                                                                               |
| **Team Synergy**        | Operator mạnh hơn khi phối hợp                         | Combo Healer + Tank                                                                                                                                             |

#### Game Tham Chiếu

Thiết kế operator lấy cảm hứng từ:

| Game                  | Inspiration Element                            | Our Implementation                                         |
| --------------------- | ---------------------------------------------- | ---------------------------------------------------------- |
| **Rainbow Six Siege** | Gadget riêng cho từng operator                    | Active ability có upgrade path                        |
| **Apex Legends**      | Combo passive + active ability                 | Hệ thống ability kép                                        |
| **The Finals**        | Team dynamic dựa trên class (Light/Trung bình/Heavy) | 5 class lõi với role riêng                         |
| **Valorant**          | Cooldown ability, balance ưu tiên vũ khí        | Ability dựa trên cooldown, gunplay quan trọng hơn power |
| **Tarkov**            | Gameplay tactical stakes cao, có gear fear      | Tập trung extraction, chết là mất gear                       |
| **Hunt Showdown**     | Hệ thống trait, chiến tranh thông tin              | Passive ability, gameplay dẫn dắt bằng audio                   |

***

### Thiết Kế Viewport Top-Down

Trong góc nhìn top-down, độ dễ đọc của nhân vật khác căn bản so với game first-person hoặc third-person. Người chơi nhìn operator từ trên xuống ở góc camera dốc (\~60 degrees), vì vậy **hình silhouette**, **vị trí color accent** và **độ rõ radial của VFX** là công cụ nhận diện chính.

#### Nguyên Tắc Silhouette

| Nguyên Tắc               | Rule                                                               | Lý Do                                                |
| ----------------------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| **Oversized Shoulders** | Mọi operator dùng tỉ lệ shoulder/backpack được phóng đại        | Ở 50% zoom, hình vai là đặc điểm dễ thấy nhất  |
| **Headgear Silhouette** | Mỗi class có profile headgear riêng đọc được từ trên xuống      | Helmet, hood, cap và visor giúp nhận diện class tức thì  |
| **Vũ khí Readability**  | Primary weapon phải vươn rõ khỏi model nhân vật                | Người chơi phải đọc được địch đang cầm loại vũ khí nào       |
| **Color Accent Zones**  | Màu accent class đặt trên vai và backpack, tức các bề mặt hướng lên camera | Bề mặt phía trên nhận nhiều camera exposure nhất |
| **Distinct Body Mass**  | Tank rộng nhất, Recon hẹp nhất, các class khác nằm giữa            | Độ rộng cơ thể là tín hiệu nhận diện class nhanh nhất trong vô thức  |

#### Độ Đọc VFX Từ Trên Xuống

VFX ability phải đọc rõ từ camera top-down. Mọi ability dạng area-effect dùng **radial indicator** chiếu lên mặt đất.

| VFX Type           | Design Rule                                         | Ví Dụ                                          |
| ------------------ | --------------------------------------------------- | ------------------------------------------------ |
| **Area of Hiệu Ứng** | Ground decal hình tròn với viền màu theo class  | PULSE Nano Swarm = silver/green vòng tròn trên mặt đất |
| **Directional**    | Cone hoặc line chiếu về phía trước operator        | BASTION Khiên = 120-degree arc indicator        |
| **Bản thân-Buff**      | Glow nhẹ trên model operator kèm đổi icon minimap | MAMBA Combat Stim = orange body glow             |
| **Deployable**     | Model trong world-space kèm indicator bán kính dạng pulse     | SUTURE Hồi máu Drone = green pulsing circle      |
| **Status Applied** | Icon màu phía trên đầu nhân vật bị ảnh hưởng        | Burn = flame icon, Slow = chain icon             |

> \[!NOTE] Tất cả VFX phải đọc được ở **minimum zoom** (khoảng cách camera xa nhất). Nếu VFX chỉ thấy rõ ở maximum zoom, nó không đạt yêu cầu readability. See [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) để xem particle budget và performance tier của VFX.

#### Nhận Diện Màu Class (Top-Down)

| Class      | Accent Color | Hex     | Top-Surface Placement       | Visibility Distance |
| ---------- | ------------ | ------- | --------------------------- | ------------------- |
| Assault    | Orange       | #F97316 | Shoulder patches, ammo belt | 80+ units           |
| Support    | White/Green  | #22C55E | Cross armband, backpack     | 80+ units           |
| Recon      | Cyan         | #06B6D4 | Goggle glow, tech strips    | 60+ units           |
| Tank       | Steel Blue   | #3B82F6 | Shoulder plates, visor      | 100+ units          |
| Specialist | Amber        | #F59E0B | Utility markings, goggles   | 60+ units           |

See [Style Guide](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/StyleGuide/README.md) for full color coding specifications.

***

### Hitbox & Collision

All operators use **capsule-based collision** with a separate head hitbox sphere. Hitbox dimensions vary by class to reflect body mass differences nhìn rõ từ trên xuống.

#### Kích Thước Hitbox

| Operator | Capsule Radius | Capsule Chiều Cao | Vùng Đầu Radius | Collision Profile |
| -------- | -------------- | -------------- | ------------------ | ----------------- |
| MAMBA    | 40 cm          | 180 cm         | 14 cm              | Standard          |
| IGNITION | 36 cm          | 168 cm         | 13 cm              | Standard          |
| TARTARUS | 44 cm          | 190 cm         | 15 cm              | Standard          |
| SUTURE   | 38 cm          | 176 cm         | 14 cm              | Standard          |
| AEGIS    | 34 cm          | 164 cm         | 13 cm              | Standard          |
| SONAR    | 34 cm          | 170 cm         | 13 cm              | Slim              |
| MIRAGE   | 40 cm          | 182 cm         | 14 cm              | Slim              |
| OBSIDIAN | 32 cm          | 160 cm         | 12 cm              | Slim              |
| BASTION  | 48 cm          | 188 cm         | 15 cm              | Heavy             |
| GOLIATH  | 46 cm          | 186 cm         | 15 cm              | Heavy             |
| GLITCH   | 36 cm          | 175 cm         | 13 cm              | Standard          |
| PULSE    | 38 cm          | 172 cm         | 13 cm              | Standard          |

**Collision Profiles:**

* **Slim** — 10% smaller hitbox than body mesh for Recon class advantage
* **Standard** — Hitbox matches body mesh 1:1
* **Heavy** — 5% larger hitbox than body mesh (trade-off for Tank armor)

**Head Hitbox Rules:**

* Headshot multiplier: 2.0x (see [Combat](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Combat/README.md) for damage formulas)
* Head sphere is always at the top of the capsule, regardless of animation state
* From top-down view, head hitbox is the primary visible target — this is intentional

***

### Hệ Thống Hiệu Ứng Trạng Thái

Abilities can apply status effects to operators. Each effect has a base duration modified by class resistances.

#### Hiệu Ứng Trạng Thái

| Hiệu Ứng    | Icon           | Base Duration        | Source Abilities                                                | Visual Cue (Top-Down)                                       |
| --------- | -------------- | -------------------- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| **Stun**  | Lightning bolt | 1.5 seconds          | BASTION Khiên Bash, Flashbang grenade                          | Character freezes, spark particles above head               |
| **Slow**  | Chain links    | 3.0 seconds          | PULSE Nano Swarm (Napalm Stick upgrade), IGNITION fire exit     | Movement trail turns blue, character model drags            |
| **Burn**  | Flame          | 5.0 seconds (15 DPS) | IGNITION Incendiary Rush, Molotov                               | Orange flame particles on character, smoke trail            |
| **EMP**   | Circuit break  | 4.0 seconds          | GLITCH EMP Blast                                                | Blue static particles, HUD distortion (self view)           |
| **Blind** | Eye cross      | 2.0 seconds          | Flashbang grenade, IGNITION Flashpoint upgrade                  | White flash on operator model (top-down: bright white glow) |
| **Mark**  | Crosshair      | 5.0 seconds          | SONAR UAV Scan, MIRAGE Motion Sensor, TARTARUS Predator upgrade | Red outline visible through walls and from above            |

#### Kháng Theo Class

| Class      | Stun Resist | Slow Resist | Burn Resist | EMP Resist | Ghi Chú                                         |
| ---------- | ----------- | ----------- | ----------- | ---------- | --------------------------------------------- |
| Assault    | 0%          | 0%          | 0%          | 0%         | No resistances — pure offense                 |
| Support    | 0%          | 10%         | 0%          | 0%         | Slight slow resist for reaching downed allies |
| Recon      | 15%         | 0%          | 0%          | 0%         | Stun resist for evasion                       |
| Tank       | 25%         | 25%         | 10%         | 0%         | Broad physical resistance                     |
| Specialist | 0%          | 0%          | 0%          | 50%        | Half EMP duration — they build the tech       |

> \[!NOTE] Individual operator passives may further modify resistances. See each operator's "Expanded Combat Statistics" section for operator-specific modifiers.

***

### Hệ Thống Stamina

Sprinting consumes stamina. When stamina is depleted, operators cannot sprint until partial recovery.

#### Stamina Cơ Bản

| Tham Số                | Giá Trị       | Ghi Chú                                        |
| ------------------------ | ----------- | -------------------------------------------- |
| **Quỹ Stamina**         | 100         | Universal base                               |
| **Hao Stamina Khi Sprint**         | 10/second   | 10 seconds of continuous sprint              |
| **Tốc Độ Hồi**        | 8/second    | Recovers while walking or idle               |
| **Recovery Delay**       | 1.5 seconds | Delay after sprinting before recovery starts |
| **Exhaustion Threshold** | 0           | Cannot sprint at 0 stamina                   |
| **Minimum to Sprint**    | 20          | Must have 20+ stamina to start sprinting     |

#### Bộ Điều Chỉnh Stamina Theo Class

| Class      | Pool Bộ Điều Chỉnh  | Drain Bộ Điều Chỉnh  | Recovery Bộ Điều Chỉnh | Thời Lượng Sprint Thực |
| ---------- | -------------- | --------------- | ----------------- | ------------------- |
| Assault    | +20% (120)     | Standard (10/s) | +10% (8.8/s)      | 12.0 seconds        |
| Support    | Standard (100) | Standard (10/s) | Standard (8/s)    | 10.0 seconds        |
| Recon      | +10% (110)     | -10% (9/s)      | +20% (9.6/s)      | 12.2 seconds        |
| Tank       | -20% (80)      | +20% (12/s)     | -10% (7.2/s)      | 6.7 seconds         |
| Specialist | Standard (100) | Standard (10/s) | Standard (8/s)    | 10.0 seconds        |

**Design Intent:** Tank operators commit to positions. They cannot sprint long distances — choosing where to fight is critical. Recon operators can reposition frequently. Assault operators have the longest sprint for aggressive entry.

***

### Ma Trận Tương Tác Ability

When abilities collide, the following rules apply. This matrix defines **what happens when one ability meets another** — critical for balance and counterplay.

#### Tương Tác Deployable vs. Ability

| Deployable                  | EMP Blast         | Incendiary Rush                                                | Nano Swarm                            | Smoke Screen                      | Berserker Rage | UAV Scan                            |
| --------------------------- | ----------------- | -------------------------------------------------------------- | ------------------------------------- | --------------------------------- | -------------- | ----------------------------------- |
| **Hồi máu Drone** (SUTURE)  | Destroyed         | Not affected                                                   | Not affected                          | Not affected                      | N/A            | Revealed                            |
| **Guardian Khiên** (AEGIS) | Destroyed         | Lửa does NOT pass through                                     | Swarm ignores shield (passes through) | Smoke passes through              | N/A            | Does not reveal shield users inside |
| **Motion Sensors** (MIRAGE) | Destroyed         | Destroyed by fire                                              | Not affected                          | Not affected                      | N/A            | N/A                                 |
| **UAV** (SONAR)             | Destroyed (falls) | Not affected (airborne)                                        | Not affected (airborne)               | Blocks scan LOS to ground targets | N/A            | N/A                                 |
| **Nano Swarm** (PULSE)      | Destroyed         | Lửa burns through swarm (both damage stack on enemies inside) | N/A                                   | Smoke does not interact           | N/A            | Revealed                            |
| **Riot Khiên** (BASTION)   | Disabled (5 sec)  | Lửa does NOT pass through                                     | Swarm ignores shield                  | Smoke passes through              | N/A            | Does not reveal shielded operator   |

#### Tương Tác Buff vs. Debuff

| Buff/Ability                   | Can be EMP'd?               | Cleansed by Stim? | Blocked by Khiên?                                    | Affected by Smoke?                                        |
| ------------------------------ | --------------------------- | ----------------- | ----------------------------------------------------- | --------------------------------------------------------- |
| **Combat Stim** (MAMBA)        | Yes — bị hủy ngay lập tức | N/A (is the stim) | N/A                                                   | No                                                        |
| **Berserker Rage** (TARTARUS)  | Yes — bị hủy ngay lập tức | No                | N/A                                                   | No                                                        |
| **Giáp Overcharge** (GOLIATH) | Yes — bonus armor stripped  | No                | N/A                                                   | No                                                        |
| **Burn** (IGNITION)            | No — not tech-based         | No                | Guardian Khiên blocks fire source, not existing burn | No                                                        |
| **Mark** (SONAR/MIRAGE)        | No — already applied        | No                | No                                                    | Smoke blocks NEW scans but does not remove existing marks |

***

### Class Operator

#### Ma Trận Tổng Quan Class

| Class                                                                                                                      | Role                | Primary Stat  | Team Giá Trị | Solo Viability | Operators |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- | ---------- | -------------- | --------- |
| [**ASSAULT**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/README.md)       | Frontline Aggressor | Damage        | Trung bình     | Cao           | 3         |
| [**SUPPORT**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/README.md)       | Team Healer         | Hồi máu       | Rất cao  | Thấp            | 2         |
| [**RECON**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/README.md)           | Intel Specialist    | Information   | Cao       | Rất cao      | 3         |
| [**TANK**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/README.md)             | Damage Sponge       | Survivability | Cao       | Trung bình         | 2         |
| [**SPECIALIST**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/README.md) | Tech Disruptor      | Utility       | Cao       | Cao           | 2         |

#### Tiến Trình Mở Khóa

```
ACCOUNT LEVEL 1  -> Assault (MAMBA) - Free starter
ACCOUNT LEVEL 1  -> Support (SUTURE) - Free starter
ACCOUNT LEVEL 5  -> Assault (IGNITION) - 5,000 Credits or Quest
ACCOUNT LEVEL 8  -> Recon (SONAR) - 5,000 Credits or Quest
ACCOUNT LEVEL 10 -> Tank (BASTION) - 7,500 Credits or Quest
ACCOUNT LEVEL 12 -> Recon (MIRAGE) - 7,500 Credits or Quest
ACCOUNT LEVEL 15 -> Specialist (GLITCH) - 10,000 Credits or Quest
ACCOUNT LEVEL 18 -> Support (AEGIS) - 10,000 Credits or Quest
ACCOUNT LEVEL 20 -> Tank (GOLIATH) - 12,000 Credits or Quest
ACCOUNT LEVEL 22 -> Assault (TARTARUS) - 12,000 Credits or Quest
ACCOUNT LEVEL 25 -> Recon (OBSIDIAN) - 15,000 Credits or Quest
ACCOUNT LEVEL 28 -> Specialist (PULSE) - 15,000 Credits or Quest
```

**Design Intent:** Starter operators (MAMBA, SUTURE) represent the two core loops — killing and surviving. New classes unlock steadily to introduce complexity without overwhelming new players.

***

### Chi Tiết Class

#### 1. ASSAULT CLASS — Frontline Aggressors

**Role:** Cao damage dealers who lead the charge into combat.

**Class Traits:**

* +10% Base Tốc Độ Sprint
* +5% Vũ khí Damage
* -10% Maximum Giáp

**Operators:**

| Operator                                                                                                                                   | Codename | Ability         | Chuyên Môn            |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------- | --------------- | -------------------- |
| [Thuy "Mamba" Nguyen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Mamba/README.md)         | MAMBA    | Combat Stim     | Damage Amplification |
| [Ji-yoon "Ignition" Kwon](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Ignition/README.md)  | IGNITION | Incendiary Rush | Area Denial          |
| [Carlos "Tartarus" Mendes](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Tartarus/README.md) | TARTARUS | Berserker Rage  | Close Combat         |

[View All Assault Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/README.md)

***

#### 2. SUPPORT CLASS — Team Lifelines

**Role:** Keep teammates alive and enable sustained combat.

**Class Traits:**

* +20% Hồi máu Item Effectiveness
* +15% Revive Speed
* -5% Movement Speed

**Operators:**

| Operator                                                                                                                                 | Codename | Ability         | Chuyên Môn         |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------- | ----------------- |
| [Tariq "Suture" Al-Sayed](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Suture/README.md)  | SUTURE   | Hồi máu Drone   | Area Hồi máu      |
| [Victoria "Aegis" Sterling](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Aegis/README.md) | AEGIS    | Guardian Khiên | Damage Prevention |

[View All Support Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/README.md)

***

#### 3. RECON CLASS — Information Specialists

**Role:** Gather intel, scout enemy positions, and enable ambushes.

**Class Traits:**

* +15% Crouch Movement Speed
* -30% Âm Lượng Bước Chân
* -5% Maximum Máu

**Operators:**

| Operator                                                                                                                                   | Codename | Ability        | Chuyên Môn      |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------- | -------------- | -------------- |
| [Kaito "Sonar" Nakamura](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Sonar/README.md)        | SONAR    | UAV Scan       | Area Reveal    |
| [Ananya "Mirage" Patel](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Mirage/README.md)        | MIRAGE   | Motion Sensors | Trap Detection |
| [Unit N-7 "Obsidian" "Nero"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Obsidian/README.md) | OBSIDIAN | Smoke Screen   | Visual Denial  |

[View All Recon Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/README.md)

***

#### 4. TANK CLASS — Frontline Defenders

**Role:** Absorb damage, hold positions, and protect teammates.

**Class Traits:**

* +25% Maximum Giáp Capacity
* +10% Giáp Damage Reduction
* -15% Tốc Độ Sprint

**Operators:**

| Operator                                                                                                                               | Codename | Ability          | Chuyên Môn          |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------- | ------------------ |
| [Mikhail "Bastion" Ivanov](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Bastion/README.md) | BASTION  | Riot Khiên      | Frontal Protection |
| [Wei "Goliath" Chen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Goliath/README.md)       | GOLIATH  | Giáp Overcharge | Team Defense       |

[View All Tank Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/README.md)

***

#### 5. SPECIALIST CLASS — Tech Disruptors

**Role:** Utility, control, counter enemy abilities.

**Class Traits:**

* +2 Inventory Slots
* +20% Gadget Interaction Speed
* -10% Độ Chính Xác Vũ Khí

**Operators:**

| Operator                                                                                                                                | Codename | Ability    | Chuyên Môn      |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------- | -------------- |
| [Maya "Glitch" Torres](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Glitch/README.md) | GLITCH   | EMP Blast  | Ability Denial |
| [D-84 "Pulse" "Ohm"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Pulse/README.md)    | PULSE    | Nano Swarm | Area Control   |

[View All Specialist Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/README.md)

***

### Ma Trận Balance Operator

#### Thông Số Combat

| Operator | Class      | Độ Khó | Combat Power | Survivability | Utility | Team Giá Trị | Solo Viability | Total |
| -------- | ---------- | :--------: | :----------: | :-----------: | :-----: | :--------: | :------------: | :---: |
| MAMBA    | Assault    |     2/5    |     9/10     |      6/10     |   4/10  |    6/10    |      8/10      |   33  |
| IGNITION | Assault    |     3/5    |     8/10     |      5/10     |   6/10  |    7/10    |      7/10      |   33  |
| TARTARUS | Assault    |     4/5    |     10/10    |      4/10     |   3/10  |    5/10    |      9/10      |   31  |
| SUTURE   | Support    |     1/5    |     5/10     |      7/10     |   8/10  |    10/10   |      4/10      |   34  |
| AEGIS    | Support    |     3/5    |     4/10     |      8/10     |   9/10  |    10/10   |      3/10      |   34  |
| SONAR    | Recon      |     2/5    |     6/10     |      5/10     |   9/10  |    8/10    |      9/10      |   37  |
| MIRAGE   | Recon      |     4/5    |     7/10     |      5/10     |   8/10  |    7/10    |      8/10      |   35  |
| OBSIDIAN | Recon      |     5/5    |     5/10     |      6/10     |  10/10  |    8/10    |      7/10      |   36  |
| BASTION  | Tank       |     2/5    |     7/10     |     10/10     |   5/10  |    8/10    |      5/10      |   35  |
| GOLIATH  | Tank       |     3/5    |     6/10     |      9/10     |   7/10  |    9/10    |      4/10      |   35  |
| GLITCH   | Specialist |     4/5    |     5/10     |      6/10     |  10/10  |    7/10    |      7/10      |   35  |
| PULSE    | Specialist |     5/5    |     6/10     |      5/10     |   9/10  |    8/10    |      6/10      |   34  |

**Độ Khó Key:** 1/5 = Thân thiện với người mới, 5/5 = Requires deep game knowledge and precise ability timing.

**Balance Philosophy:** No operator should exceed 8/10 in more than two categories. Total score across all categories should fall within 31-37 points to maintain parity. See [Gameplay Balance](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/README.md) for detailed tuning rules.

#### Counter Matrix

| Operator | Strong Against     | Weak Against       | Key Ability Interaction                                                   |
| -------- | ------------------ | ------------------ | ------------------------------------------------------------------------- |
| MAMBA    | SONAR, SUTURE      | BASTION, GLITCH    | Stim cancelled bởi EMP; stim out-damages SUTURE heal rate                  |
| IGNITION | OBSIDIAN, GOLIATH  | MIRAGE, PULSE      | Lửa destroys Motion Sensors; fire + swarm stack damage on shared targets |
| TARTARUS | AEGIS, GLITCH      | BASTION, SUTURE    | Rage cancelled bởi EMP; can push through Guardian Khiên                   |
| SUTURE   | All (Sustain)      | MAMBA, TARTARUS    | Drone destroyed bởi EMP; stim burst exceeds heal rate                      |
| AEGIS    | IGNITION, TARTARUS | GLITCH, MIRAGE     | Khiên bị phá hủy ngay lập tức bởi EMP; fire cannot pass through shield        |
| SONAR    | GOLIATH, PULSE     | MAMBA, OBSIDIAN    | Scan blocked by smoke; scan reveals all deployables                       |
| MIRAGE   | IGNITION, TARTARUS | GLITCH, AEGIS      | Sensors destroyed bởi EMP and fire; sensors detect Berserker approach      |
| OBSIDIAN | BASTION, MAMBA     | SONAR, PULSE       | Smoke blocks shield vision; smoke blocks UAV scan LOS                     |
| BASTION  | MAMBA, TARTARUS    | OBSIDIAN, GLITCH   | Khiên disabled bởi EMP (5s); shield blocks fire and bullets               |
| GOLIATH  | IGNITION, MIRAGE   | SONAR, PULSE       | Overcharge armor stripped bởi EMP; absorbs fire DoT                        |
| GLITCH   | AEGIS, BASTION     | MAMBA, TARTARUS    | EMP destroys all deployables and disables active buffs                    |
| PULSE    | SONAR, MIRAGE      | IGNITION, OBSIDIAN | Swarm destroyed bởi EMP; swarm ignores shields (passes through)            |

**Reading the Counter Matrix:** "Strong Against" means the operator has an inherent advantage in a 1v1 scenario due to ability matchups. The "Key Ability Interaction" column explains WHY — this is critical for balance discussions. Skill always matters more than counters.

***

### Đội Hình Team

#### Đội Hình Squad Khuyến Nghị (3 Người)

| Comp Name           | Composition                 | Playstyle             | Strength               | Weakness                  |
| ------------------- | --------------------------- | --------------------- | ---------------------- | ------------------------- |
| **Rush Meta**       | MAMBA + TARTARUS + SUTURE   | Aggressive push       | Cao damage, sustained | No intel, no area control |
| **Intel Control**   | SONAR + MIRAGE + GLITCH     | Information dominance | Never surprised        | Thấp damage output         |
| **Goliath Hold**    | BASTION + SUTURE + IGNITION | Defensive extraction  | Hard to push           | Slow rotations            |
| **Balanced**        | MAMBA + SUTURE + SONAR      | All-around            | Flexible               | No hard counter to Tanks  |
| **Stealth Extract** | OBSIDIAN + MIRAGE + PULSE   | Avoid combat          | Maximum loot, low risk | Loses direct fights       |

#### Synergy Duo

| Duo                | Synergy                     | Strategy                                |
| ------------------ | --------------------------- | --------------------------------------- |
| MAMBA + SUTURE     | Assault heals               | Aggressive pushing with sustain backup  |
| BASTION + TARTARUS | Tank leads, Assault follows | Khiên creates opening, TARTARUS closes |
| SONAR + GLITCH     | Intel + Disable             | Full information control of engagement  |
| GOLIATH + AEGIS    | Double defense              | Nearly unkillable extraction fortress   |
| OBSIDIAN + MIRAGE  | Stealth duo                 | Silent map traversal, avoid all combat  |

***

### Tiến Trình Operator

#### Level Riêng Từng Operator

**Max Level per Operator:** 50

| Level | Mở Khóa                                         |
| ----- | ---------------------------------------------- |
| 1     | Base operator unlocked                         |
| 5     | Ability Upgrade Slot 1 (choose 1 of 3 options) |
| 10    | Cosmetic Skin 1                                |
| 15    | Stat Boost 1 (+5% Máu)                      |
| 20    | Ability Upgrade Slot 2 (choose 1 of 3 options) |
| 25    | Cosmetic Skin 2                                |
| 30    | Stat Boost 2 (+5% Stamina)                     |
| 35    | Ability Upgrade Slot 3 (choose 1 of 3 options) |
| 40    | Elite Cosmetic Skin                            |
| 45    | Stat Boost 3 (+5% Tốc Độ Sprint)                |
| 50    | Prestige Cosmetics + Title                     |

#### Hệ Thống Prestige

After reaching Level 50, operators can be **Prestiged**:

* Reset to Level 1
* Gain Prestige Badge (visible to other players in lobby and kill feed)
* Mở Khóa exclusive Prestige cosmetics per prestige level
* +5% XP bonus for that operator (stacks per prestige)
* Max Prestige: 5

**Prestige Rewards:**

| Prestige | Reward                                                |
| -------- | ----------------------------------------------------- |
| 1        | Bronze badge + weapon charm                           |
| 2        | Silver badge + unique skin                            |
| 3        | Gold badge + voice line pack                          |
| 4        | Diamond badge + animated banner                       |
| 5        | Obsidian badge + legendary title + unique kill effect |

***

### Hệ Thống Cosmetic

#### Tùy Chọn Customization

| Type             | Mô Tả                   | Acquisition                  |
| ---------------- | ----------------------------- | ---------------------------- |
| **Skins**        | Full operator visual change   | Credits, Battle Pass, Events |
| **Headgear**     | Helmets, hats, masks          | Credits, Battle Pass         |
| **Gloves**       | Hand cosmetics                | Credits only                 |
| **Vũ khí Skins** | Applied to equipped weapons   | Credits, Battle Pass         |
| **Emotes**       | Victory poses, taunts         | Battle Pass, Events          |
| **Kill Effects** | Visual effect on eliminations | Premium Currency only        |
| **Voice Packs**  | Alternate voice lines         | Premium Currency only        |

All cosmetics are purely visual — no gameplay advantage. See [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) for character model specifications and visual guidelines.

#### Tier Độ Hiếm

| Tier      | Color          | Drop Rate | Purchase Price       |
| --------- | -------------- | --------- | -------------------- |
| Common    | Gray #9CA3AF   | 60%       | 500 Credits          |
| Uncommon  | Green #22C55E  | 25%       | 1,000 Credits        |
| Rare      | Blue #3B82F6   | 10%       | 2,500 Credits        |
| Epic      | Purple #A855F7 | 4%        | Premium only         |
| Legendary | Gold #EAB308   | 1%        | Battle Pass / Events |

***

### Operator Tương Lai (Roadmap)

#### Season 1 (Launch + 3 tháng)

| Operator     | Class      | Ability Preview                                       | Design Status |
| ------------ | ---------- | ----------------------------------------------------- | ------------- |
| **SHADOW**   | Recon      | Invisibility cloak (limited duration, breaks on fire) | Concept       |
| **ENGINEER** | Specialist | Deployable turret (limited ammo, hackable by GLITCH)  | Concept       |

#### Season 2 (6 tháng)

| Operator  | Class   | Ability Preview                                        | Design Status |
| --------- | ------- | ------------------------------------------------------ | ------------- |
| **PYRO**  | Assault | Lửa damage specialist (upgraded Molotov, heat vision) | Concept       |
| **MERCY** | Support | Mass revive (long cooldown, partial health restore)    | Concept       |

#### Season 3+ (9 tháng+)

* New class consideration: **COMMANDER** (tactical calldowns — artillery markers, supply drops)
* Community-voted operator concepts (seasonal votes)
* Crossover event operators (licensed characters with unique abilities)

***

### Tham Chiếu Chéo

| Topic             | Sutureument                                                                                                              | What It Covers                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Character visuals | [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) | Operator model specs, silhouette guide, poly budgets, cyberpunk elements |
| Character style   | [Style Guide](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/StyleGuide/README.md)     | Class color coding, gear layering system, top-down readability           |
| Audio design      | [Audio Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Audio/README.md)                 | Voice line recording specs, combat callout systems                       |
| Gameplay balance  | [Gameplay](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/README.md)                  | TTK, damage formulas, ability cooldown framework                         |
| UI representation | [HUD Design](../UI_UX/HUD_Design.md)        | How operators display on HUD, teammate status panels                     |
