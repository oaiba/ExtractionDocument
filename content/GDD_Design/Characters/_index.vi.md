---
title: "Characters & Operators"
linkTitle: Characters
type: docs
weight: 3
sidebar:
  open: false
---

### Squad Hierarchy

Trong **Extraction Shooter**, character không chỉ được định nghĩa bằng stat, mà bằng tactical utility trong squad. Mọi operator đều có thể bắn và loot, nhưng ability riêng của họ định hình nhịp combat.

> \[!NOTE] **Philosophy:** Không có "DPS" hay "Tank" theo nghĩa MMO truyền thống. Mọi viên đạn đều lethal. Role cung cấp _utility_ và _sustain_, không tạo bất tử.

#### Class Roster

{{< cards cols="3" >}}
{{< card link="Assault/" title="Assault" icon="fire" subtitle="Fragger. Breacher. Frontline engage." >}}
{{< card link="Recon/" title="Recon" icon="eye" subtitle="Thu thập intel. Sniping. Flanking." >}}
{{< card link="Support/" title="Support" icon="plus-circle" subtitle="Healing. Ammo resupply. Utility." >}}
{{< card link="Tank/" title="Tank" icon="shield-check" subtitle="Area denial. Heavy weapons. Crowd control." >}}
{{< card link="Specialist/" title="Specialist" icon="chip" subtitle="Cyberwarfare. Trap. Gadget." >}}
{{< /cards >}}

***

### Design Philosophy

#### Core Principles

| Principle | Description | Example |
| ----------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Class Identity** | Mỗi class có combat role rõ | Tank = Damage absorption |
| **Character Diversity** | Nhiều character trong mỗi class với ability khác nhau | 2 Assault operators có stim khác nhau |
| **Visual Clarity** | Nhận diện tức thì từ góc nhìn top-down | Silhouette riêng, theme màu riêng (xem [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md)) |
| **Balanced Power** | Ability bổ trợ skill, không thay thế skill | +25% damage, không phải instant kill |
| **Risk/Reward** | Lối chơi aggressive phải có trade-off | Damage cao = survivability thấp hơn |
| **Team Synergy** | Operator hoạt động tốt hơn khi phối hợp | Healer + Tank combo |

#### Reference Games

Operator design lấy cảm hứng từ:

| Game | Inspiration Element | Our Implementation |
| --------------------- | ---------------------------------------------- | ---------------------------------------------------------- |
| **Rainbow Six Siege** | Gadget riêng cho từng operator | Active ability có upgrade path |
| **Apex Legends** | Combo passive + active ability | Dual ability system |
| **The Finals** | Class-based team dynamics (Light/Medium/Heavy) | 5 core class có role riêng |
| **Valorant** | Ability cooldown, weapon-first balance | Cooldown-based ability, gunplay quan trọng hơn power |
| **Tarkov** | High-stakes tactical gameplay, gear fear | Extraction focus, mất gear khi chết |
| **Hunt Showdown** | Trait system, information warfare | Passive ability, gameplay dựa trên audio |

***

### Top-Down Viewport Design

Trong perspective top-down, readability của character khác căn bản với first-person hoặc third-person. Người chơi nhìn operator từ phía trên ở góc camera dốc khoảng 60 độ, nên **silhouette shape**, **color accent placement**, và **VFX radial clarity** là công cụ nhận diện chính.

#### Silhouette Principles

| Principle | Rule | Rationale |
| ----------------------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| **Oversized Shoulders** | Mọi operator dùng tỉ lệ shoulder/backpack phóng đại | Ở 50% zoom, shoulder shape là đặc điểm dễ thấy nhất |
| **Headgear Silhouette** | Mỗi class có headgear profile riêng nhìn được từ trên | Helmet vs hood vs cap vs visor cho class ID tức thì |
| **Weapon Readability** | Primary weapon vươn rõ khỏi character model | Người chơi phải biết enemy đang cầm loại weapon nào |
| **Color Accent Zones** | Class accent color đặt trên shoulder và backpack (top surfaces) | Top surfaces nhận nhiều exposure nhất từ camera |
| **Distinct Body Mass** | Tank = rộng nhất, Recon = hẹp nhất, class khác nằm giữa | Body width là identifier vô thức nhanh nhất |

#### VFX Readability from Above

Ability VFX phải đọc rõ từ camera top-down. Mọi area-effect ability dùng **radial indicator** chiếu lên ground plane.

| VFX Type | Design Rule | Example |
| ------------------ | --------------------------------------------------- | ------------------------------------------------ |
| **Area of Effect** | Ground decal hình tròn với edge ring màu class | PULSE Nano Swarm = vòng bạc/xanh trên mặt đất |
| **Directional** | Cone hoặc line chiếu về phía trước operator | BASTION Shield = arc indicator 120 độ |
| **Self-Buff** | Glow nhẹ trên operator model + đổi minimap icon | MAMBA Combat Stim = body glow cam |
| **Deployable** | World-space model với pulsing radius indicator | SUTURE Healing Drone = vòng xanh pulse |
| **Status Applied** | Icon màu phía trên đầu character bị ảnh hưởng | Burn = flame icon, Slow = chain icon |

> \[!NOTE] Tất cả VFX phải đọc được ở **minimum zoom** (khoảng cách camera xa nhất). Nếu effect chỉ thấy ở maximum zoom, nó fail yêu cầu readability. Xem [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) cho particle budget và performance tier của VFX.

#### Class Color Identification (Top-Down)

| Class | Accent Color | Hex | Top-Surface Placement | Visibility Distance |
| ---------- | ------------ | ------- | --------------------------- | ------------------- |
| Assault | Orange | #F97316 | Shoulder patches, ammo belt | 80+ units |
| Support | White/Green | #22C55E | Cross armband, backpack | 80+ units |
| Recon | Cyan | #06B6D4 | Goggle glow, tech strips | 60+ units |
| Tank | Steel Blue | #3B82F6 | Shoulder plates, visor | 100+ units |
| Specialist | Amber | #F59E0B | Utility markings, goggles | 60+ units |

Xem [Style Guide](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/StyleGuide/README.md) cho full color coding specification.

***

### Hitbox & Collision

Mọi operator dùng **capsule-based collision** với một head hitbox sphere riêng. Kích thước hitbox thay đổi theo class để phản ánh body mass khác nhau nhìn thấy từ trên.

#### Hitbox Dimensions

| Operator | Capsule Radius | Capsule Height | Head Sphere Radius | Collision Profile |
| -------- | -------------- | -------------- | ------------------ | ----------------- |
| MAMBA | 40 cm | 180 cm | 14 cm | Standard |
| IGNITION | 36 cm | 168 cm | 13 cm | Standard |
| TARTARUS | 44 cm | 190 cm | 15 cm | Standard |
| SUTURE | 38 cm | 176 cm | 14 cm | Standard |
| AEGIS | 34 cm | 164 cm | 13 cm | Standard |
| SONAR | 34 cm | 170 cm | 13 cm | Slim |
| MIRAGE | 40 cm | 182 cm | 14 cm | Slim |
| OBSIDIAN | 32 cm | 160 cm | 12 cm | Slim |
| BASTION | 48 cm | 188 cm | 15 cm | Heavy |
| GOLIATH | 46 cm | 186 cm | 15 cm | Heavy |
| GLITCH | 36 cm | 175 cm | 13 cm | Standard |
| PULSE | 38 cm | 172 cm | 13 cm | Standard |

**Collision Profiles:**

* **Slim** - hitbox nhỏ hơn body mesh 10% cho lợi thế Recon
* **Standard** - hitbox khớp body mesh 1:1
* **Heavy** - hitbox lớn hơn body mesh 5% (trade-off cho Tank armor)

**Head Hitbox Rules:**

* Headshot multiplier: 2.0x (xem [Combat](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Combat/README.md) cho damage formula)
* Head sphere luôn nằm ở đỉnh capsule, bất kể animation state
* Từ top-down view, head hitbox là target visible chính; đây là chủ ý thiết kế

***

### Status Effect System

Ability có thể apply status effect lên operator. Mỗi effect có base duration được modified bởi class resistance.

#### Status Effects

| Effect | Icon | Base Duration | Source Abilities | Visual Cue (Top-Down) |
| --------- | -------------- | -------------------- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| **Stun** | Lightning bolt | 1.5 seconds | BASTION Shield Bash, Flashbang grenade | Character đứng khựng, spark particle trên đầu |
| **Slow** | Chain links | 3.0 seconds | PULSE Nano Swarm (Napalm Stick upgrade), IGNITION fire exit | Movement trail chuyển xanh, character model bị kéo nặng |
| **Burn** | Flame | 5.0 seconds (15 DPS) | IGNITION Incendiary Rush, Molotov | Flame particle cam trên character, smoke trail |
| **EMP** | Circuit break | 4.0 seconds | GLITCH EMP Blast | Blue static particle, HUD distortion (self view) |
| **Blind** | Eye cross | 2.0 seconds | Flashbang grenade, IGNITION Flashpoint upgrade | White flash trên operator model (top-down: glow trắng sáng) |
| **Mark** | Crosshair | 5.0 seconds | SONAR UAV Scan, MIRAGE Motion Sensor, TARTARUS Predator upgrade | Red outline thấy xuyên tường và từ trên |

#### Class Resistances

| Class | Stun Resist | Slow Resist | Burn Resist | EMP Resist | Notes |
| ---------- | ----------- | ----------- | ----------- | ---------- | --------------------------------------------- |
| Assault | 0% | 0% | 0% | 0% | Không resistance; pure offense |
| Support | 0% | 10% | 0% | 0% | Slow resist nhẹ để tới đồng đội downed |
| Recon | 15% | 0% | 0% | 0% | Stun resist cho evasion |
| Tank | 25% | 25% | 10% | 0% | Physical resistance rộng |
| Specialist | 0% | 0% | 0% | 50% | Half EMP duration; họ xây công nghệ |

> \[!NOTE] Passive riêng của từng operator có thể modify resistance thêm. Xem section "Expanded Combat Statistics" của từng operator cho modifier cụ thể.

***

### Stamina System

Sprint tiêu hao stamina. Khi stamina cạn, operator không thể sprint cho đến khi hồi một phần.

#### Base Stamina

| Parameter | Value | Notes |
| ------------------------ | ----------- | -------------------------------------------- |
| **Stamina Pool** | 100 | Universal base |
| **Sprint Drain** | 10/second | 10 giây sprint liên tục |
| **Recovery Rate** | 8/second | Hồi khi walk hoặc idle |
| **Recovery Delay** | 1.5 seconds | Delay sau sprint trước khi hồi |
| **Exhaustion Threshold** | 0 | Không thể sprint ở 0 stamina |
| **Minimum to Sprint** | 20 | Cần 20+ stamina để bắt đầu sprint |

#### Class Stamina Modifiers

| Class | Pool Modifier | Drain Modifier | Recovery Modifier | Net Sprint Duration |
| ---------- | -------------- | --------------- | ----------------- | ------------------- |
| Assault | +20% (120) | Standard (10/s) | +10% (8.8/s) | 12.0 seconds |
| Support | Standard (100) | Standard (10/s) | Standard (8/s) | 10.0 seconds |
| Recon | +10% (110) | -10% (9/s) | +20% (9.6/s) | 12.2 seconds |
| Tank | -20% (80) | +20% (12/s) | -10% (7.2/s) | 6.7 seconds |
| Specialist | Standard (100) | Standard (10/s) | Standard (8/s) | 10.0 seconds |

**Design Intent:** Tank operators commit vào vị trí. Họ không thể sprint xa; chọn nơi giao tranh là quyết định critical. Recon operators có thể reposition thường xuyên. Assault operators có sprint dài nhất để aggressive entry.

***

### Ability Interaction Matrix

Khi ability va chạm, các rule sau được áp dụng. Matrix này định nghĩa **điều gì xảy ra khi một ability gặp ability khác**; rất quan trọng cho balance và counterplay.

#### Deployable vs. Ability Interactions

| Deployable | EMP Blast | Incendiary Rush | Nano Swarm | Smoke Screen | Berserker Rage | UAV Scan |
| --------------------------- | ----------------- | -------------------------------------------------------------- | ------------------------------------- | --------------------------------- | -------------- | ----------------------------------- |
| **Healing Drone** (SUTURE) | Destroyed | Not affected | Not affected | Not affected | N/A | Revealed |
| **Guardian Shield** (AEGIS) | Destroyed | Fire does NOT pass through | Swarm ignores shield (passes through) | Smoke passes through | N/A | Does not reveal shield users inside |
| **Motion Sensors** (MIRAGE) | Destroyed | Destroyed by fire | Not affected | Not affected | N/A | N/A |
| **UAV** (SONAR) | Destroyed (falls) | Not affected (airborne) | Not affected (airborne) | Blocks scan LOS to ground targets | N/A | N/A |
| **Nano Swarm** (PULSE) | Destroyed | Fire burns through swarm (both damage stack on enemies inside) | N/A | Smoke does not interact | N/A | Revealed |
| **Riot Shield** (BASTION) | Disabled (5 sec) | Fire does NOT pass through | Swarm ignores shield | Smoke passes through | N/A | Does not reveal shielded operator |

#### Buff vs. Debuff Interactions

| Buff/Ability | Can be EMP'd? | Cleansed by Stim? | Blocked by Shield? | Affected by Smoke? |
| ------------------------------ | --------------------------- | ----------------- | ----------------------------------------------------- | --------------------------------------------------------- |
| **Combat Stim** (MAMBA) | Yes - cancelled immediately | N/A (is the stim) | N/A | No |
| **Berserker Rage** (TARTARUS) | Yes - cancelled immediately | No | N/A | No |
| **Armor Overcharge** (GOLIATH) | Yes - bonus armor stripped | No | N/A | No |
| **Burn** (IGNITION) | No - not tech-based | No | Guardian Shield blocks fire source, not existing burn | No |
| **Mark** (SONAR/MIRAGE) | No - already applied | No | No | Smoke blocks NEW scans but does not remove existing marks |

***

### Operator Classes

#### Class Overview Matrix

| Class | Role | Primary Stat | Team Value | Solo Viability | Operators |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- | ---------- | -------------- | --------- |
| [**ASSAULT**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/README.md) | Frontline Aggressor | Damage | Medium | High | 3 |
| [**SUPPORT**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/README.md) | Team Healer | Healing | Very High | Low | 2 |
| [**RECON**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/README.md) | Intel Specialist | Information | High | Very High | 3 |
| [**TANK**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/README.md) | Damage Sponge | Survivability | High | Medium | 2 |
| [**SPECIALIST**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/README.md) | Tech Disruptor | Utility | High | High | 2 |

#### Unlock Progression

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

**Design Intent:** Starter operators (MAMBA, SUTURE) đại diện hai core loop: giết và sống sót. Class mới unlock đều đặn để giới thiệu complexity mà không làm người chơi mới quá tải.

***

### Class Details

#### 1. ASSAULT CLASS - Frontline Aggressors

**Role:** Damage dealer cao dẫn đầu charge vào combat.

**Class Traits:**

* +10% Base Sprint Speed
* +5% Weapon Damage
* -10% Maximum Armor

| Operator | Codename | Ability | Specialty |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------- | --------------- | -------------------- |
| [Thuy "Mamba" Nguyen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Mamba/README.md) | MAMBA | Combat Stim | Damage Amplification |
| [Ji-yoon "Ignition" Kwon](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Ignition/README.md) | IGNITION | Incendiary Rush | Area Denial |
| [Carlos "Tartarus" Mendes](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/Tartarus/README.md) | TARTARUS | Berserker Rage | Close Combat |

[View All Assault Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Assault/README.md)

#### 2. SUPPORT CLASS - Team Lifelines

**Role:** Giữ teammate sống và enable sustained combat.

**Class Traits:**

* +20% Healing Item Effectiveness
* +15% Revive Speed
* -5% Movement Speed

| Operator | Codename | Ability | Specialty |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------- | ----------------- |
| [Tariq "Suture" Al-Sayed](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Suture/README.md) | SUTURE | Healing Drone | Area Healing |
| [Victoria "Aegis" Sterling](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Aegis/README.md) | AEGIS | Guardian Shield | Damage Prevention |

[View All Support Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/README.md)

#### 3. RECON CLASS - Information Specialists

**Role:** Thu thập intel, scout vị trí địch, và enable ambush.

**Class Traits:**

* +15% Crouch Movement Speed
* -30% Footstep Volume
* -5% Maximum Health

| Operator | Codename | Ability | Specialty |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------- | -------------- | -------------- |
| [Kaito "Sonar" Nakamura](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Sonar/README.md) | SONAR | UAV Scan | Area Reveal |
| [Ananya "Mirage" Patel](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Mirage/README.md) | MIRAGE | Motion Sensors | Trap Detection |
| [Unit N-7 "Obsidian" "Nero"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/Obsidian/README.md) | OBSIDIAN | Smoke Screen | Visual Denial |

[View All Recon Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Recon/README.md)

#### 4. TANK CLASS - Frontline Defenders

**Role:** Hấp thụ damage, giữ vị trí, và bảo vệ teammate.

**Class Traits:**

* +25% Maximum Armor Capacity
* +10% Armor Damage Reduction
* -15% Sprint Speed

| Operator | Codename | Ability | Specialty |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------- | ------------------ |
| [Mikhail "Bastion" Ivanov](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Bastion/README.md) | BASTION | Riot Shield | Frontal Protection |
| [Wei "Goliath" Chen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Goliath/README.md) | GOLIATH | Armor Overcharge | Team Defense |

[View All Tank Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/README.md)

#### 5. SPECIALIST CLASS - Tech Disruptors

**Role:** Utility, control, counter enemy ability.

**Class Traits:**

* +2 Inventory Slots
* +20% Gadget Interaction Speed
* -10% Weapon Accuracy

| Operator | Codename | Ability | Specialty |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------- | -------------- |
| [Maya "Glitch" Torres](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Glitch/README.md) | GLITCH | EMP Blast | Ability Denial |
| [D-84 "Pulse" "Ohm"](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/Pulse/README.md) | PULSE | Nano Swarm | Area Control |

[View All Specialist Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Specialist/README.md)

***

### Operator Balance Matrix

#### Combat Statistics

| Operator | Class | Difficulty | Combat Power | Survivability | Utility | Team Value | Solo Viability | Total |
| -------- | ---------- | :--------: | :----------: | :-----------: | :-----: | :--------: | :------------: | :---: |
| MAMBA | Assault | 2/5 | 9/10 | 6/10 | 4/10 | 6/10 | 8/10 | 33 |
| IGNITION | Assault | 3/5 | 8/10 | 5/10 | 6/10 | 7/10 | 7/10 | 33 |
| TARTARUS | Assault | 4/5 | 10/10 | 4/10 | 3/10 | 5/10 | 9/10 | 31 |
| SUTURE | Support | 1/5 | 5/10 | 7/10 | 8/10 | 10/10 | 4/10 | 34 |
| AEGIS | Support | 3/5 | 4/10 | 8/10 | 9/10 | 10/10 | 3/10 | 34 |
| SONAR | Recon | 2/5 | 6/10 | 5/10 | 9/10 | 8/10 | 9/10 | 37 |
| MIRAGE | Recon | 4/5 | 7/10 | 5/10 | 8/10 | 7/10 | 8/10 | 35 |
| OBSIDIAN | Recon | 5/5 | 5/10 | 6/10 | 10/10 | 8/10 | 7/10 | 36 |
| BASTION | Tank | 2/5 | 7/10 | 10/10 | 5/10 | 8/10 | 5/10 | 35 |
| GOLIATH | Tank | 3/5 | 6/10 | 9/10 | 7/10 | 9/10 | 4/10 | 35 |
| GLITCH | Specialist | 4/5 | 5/10 | 6/10 | 10/10 | 7/10 | 7/10 | 35 |
| PULSE | Specialist | 5/5 | 6/10 | 5/10 | 9/10 | 8/10 | 6/10 | 34 |

**Difficulty Key:** 1/5 = thân thiện beginner, 5/5 = cần game knowledge sâu và ability timing chính xác.

**Balance Philosophy:** Không operator nào nên vượt 8/10 ở hơn hai category. Total score trên mọi category nên nằm trong 31-37 điểm để giữ parity. Xem [Gameplay Balance](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/README.md) cho tuning rule chi tiết.

#### Counter Matrix

| Operator | Strong Against | Weak Against | Key Ability Interaction |
| -------- | ------------------ | ------------------ | ------------------------------------------------------------------------- |
| MAMBA | SONAR, SUTURE | BASTION, GLITCH | Stim bị EMP hủy; stim vượt heal rate của SUTURE |
| IGNITION | OBSIDIAN, GOLIATH | MIRAGE, PULSE | Fire phá Motion Sensors; fire + swarm stack damage trên target chung |
| TARTARUS | AEGIS, GLITCH | BASTION, SUTURE | Rage bị EMP hủy; có thể push xuyên Guardian Shield |
| SUTURE | All (Sustain) | MAMBA, TARTARUS | Drone bị EMP phá; stim burst vượt heal rate |
| AEGIS | IGNITION, TARTARUS | GLITCH, MIRAGE | Shield bị EMP phá ngay; fire không xuyên shield |
| SONAR | GOLIATH, PULSE | MAMBA, OBSIDIAN | Scan bị smoke chặn; scan reveal mọi deployable |
| MIRAGE | IGNITION, TARTARUS | GLITCH, AEGIS | Sensor bị EMP và fire phá; sensor detect Berserker approach |
| OBSIDIAN | BASTION, MAMBA | SONAR, PULSE | Smoke chặn shield vision; smoke chặn UAV scan LOS |
| BASTION | MAMBA, TARTARUS | OBSIDIAN, GLITCH | Shield bị EMP disable (5s); shield chặn fire và bullet |
| GOLIATH | IGNITION, MIRAGE | SONAR, PULSE | Overcharge armor bị EMP strip; hấp thụ fire DoT |
| GLITCH | AEGIS, BASTION | MAMBA, TARTARUS | EMP phá mọi deployable và disable active buff |
| PULSE | SONAR, MIRAGE | IGNITION, OBSIDIAN | Swarm bị EMP phá; swarm ignore shield (đi xuyên) |

**Reading the Counter Matrix:** "Strong Against" nghĩa là operator có lợi thế tự nhiên trong 1v1 nhờ ability matchup. Cột "Key Ability Interaction" giải thích TẠI SAO; rất quan trọng cho balance discussion. Skill luôn quan trọng hơn counter.

***

### Team Compositions

#### Recommended Squad Compositions (3-Player)

| Comp Name | Composition | Playstyle | Strength | Weakness |
| ------------------- | --------------------------- | --------------------- | ---------------------- | ------------------------- |
| **Rush Meta** | MAMBA + TARTARUS + SUTURE | Aggressive push | High damage, sustained | Không intel, không area control |
| **Intel Control** | SONAR + MIRAGE + GLITCH | Information dominance | Không bị bất ngờ | Damage output thấp |
| **Goliath Hold** | BASTION + SUTURE + IGNITION | Defensive extraction | Khó push | Rotate chậm |
| **Balanced** | MAMBA + SUTURE + SONAR | All-around | Flexible | Không hard counter Tank |
| **Stealth Extract** | OBSIDIAN + MIRAGE + PULSE | Tránh combat | Loot tối đa, risk thấp | Thua direct fight |

#### Duo Synergies

| Duo | Synergy | Strategy |
| ------------------ | --------------------------- | --------------------------------------- |
| MAMBA + SUTURE | Assault heals | Aggressive push với sustain backup |
| BASTION + TARTARUS | Tank leads, Assault follows | Shield tạo opening, TARTARUS close |
| SONAR + GLITCH | Intel + Disable | Full information control của engagement |
| GOLIATH + AEGIS | Double defense | Extraction fortress gần như không thể giết |
| OBSIDIAN + MIRAGE | Stealth duo | Di chuyển im lặng qua map, tránh combat |

***

### Operator Progression

#### Individual Leveling

**Max Level per Operator:** 50

| Level | Unlock |
| ----- | ---------------------------------------------- |
| 1 | Base operator unlocked |
| 5 | Ability Upgrade Slot 1 (chọn 1 trong 3 option) |
| 10 | Cosmetic Skin 1 |
| 15 | Stat Boost 1 (+5% Health) |
| 20 | Ability Upgrade Slot 2 (chọn 1 trong 3 option) |
| 25 | Cosmetic Skin 2 |
| 30 | Stat Boost 2 (+5% Stamina) |
| 35 | Ability Upgrade Slot 3 (chọn 1 trong 3 option) |
| 40 | Elite Cosmetic Skin |
| 45 | Stat Boost 3 (+5% Sprint Speed) |
| 50 | Prestige Cosmetics + Title |

#### Prestige System

Sau khi đạt Level 50, operator có thể **Prestige**:

* Reset về Level 1
* Nhận Prestige Badge (hiển thị cho người chơi khác trong lobby và kill feed)
* Unlock cosmetic Prestige độc quyền theo prestige level
* +5% XP bonus cho operator đó (stack theo prestige)
* Max Prestige: 5

**Prestige Rewards:**

| Prestige | Reward |
| -------- | ----------------------------------------------------- |
| 1 | Bronze badge + weapon charm |
| 2 | Silver badge + unique skin |
| 3 | Gold badge + voice line pack |
| 4 | Diamond badge + animated banner |
| 5 | Obsidian badge + legendary title + unique kill effect |

***

### Cosmetic System

#### Customization Options

| Type | Description | Acquisition |
| ---------------- | ----------------------------- | ---------------------------- |
| **Skins** | Thay đổi visual operator toàn thân | Credits, Battle Pass, Events |
| **Headgear** | Helmet, hat, mask | Credits, Battle Pass |
| **Gloves** | Cosmetic tay | Credits only |
| **Weapon Skins** | Áp dụng lên weapon được equip | Credits, Battle Pass |
| **Emotes** | Victory pose, taunt | Battle Pass, Events |
| **Kill Effects** | Visual effect khi elimination | Premium Currency only |
| **Voice Packs** | Voice line thay thế | Premium Currency only |

Tất cả cosmetic chỉ mang tính visual; không tạo gameplay advantage. Xem [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) cho character model specification và visual guideline.

#### Rarity Tiers

| Tier | Color | Drop Rate | Purchase Price |
| --------- | -------------- | --------- | -------------------- |
| Common | Gray #9CA3AF | 60% | 500 Credits |
| Uncommon | Green #22C55E | 25% | 1,000 Credits |
| Rare | Blue #3B82F6 | 10% | 2,500 Credits |
| Epic | Purple #A855F7 | 4% | Premium only |
| Legendary | Gold #EAB308 | 1% | Battle Pass / Events |

***

### Future Operators (Roadmap)

#### Season 1 (Launch + 3 months)

| Operator | Class | Ability Preview | Design Status |
| ------------ | ---------- | ----------------------------------------------------- | ------------- |
| **SHADOW** | Recon | Invisibility cloak (limited duration, breaks on fire) | Concept |
| **ENGINEER** | Specialist | Deployable turret (limited ammo, hackable by GLITCH) | Concept |

#### Season 2 (6 months)

| Operator | Class | Ability Preview | Design Status |
| --------- | ------- | ------------------------------------------------------ | ------------- |
| **PYRO** | Assault | Fire damage specialist (upgraded Molotov, heat vision) | Concept |
| **MERCY** | Support | Mass revive (long cooldown, partial health restore) | Concept |

#### Season 3+ (9 months+)

* Cân nhắc class mới: **COMMANDER** (tactical calldowns; artillery marker, supply drop)
* Concept operator do community vote (seasonal vote)
* Crossover event operator (licensed character với unique ability)

***

### Cross-References

| Topic | Document | What It Covers |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Character visuals | [Art Direction](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/ArtDirection/README.md) | Operator model spec, silhouette guide, poly budget, cyberpunk element |
| Character style | [Style Guide](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Visuals/StyleGuide/README.md) | Class color coding, gear layering system, top-down readability |
| Audio design | [Audio Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Audio/README.md) | Voice line recording spec, combat callout system |
| Gameplay balance | [Gameplay](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/README.md) | TTK, damage formula, ability cooldown framework |
| UI representation | [HUD Design](../UI_UX/HUD_Design.md) | Operator hiển thị trên HUD, teammate status panel |
