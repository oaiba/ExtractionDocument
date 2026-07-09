---
title: "GLITCH - Maya Torres"
type: docs
---

## Hồ Sơ Operator

> *"Gadget, ability, kế hoạch của anh đều vô nghĩa. Tôi chỉ cần tắt công tắc."*

### Thông Tin Cơ Bản

| Thuộc Tính       | Giá Trị                     |
| :-------------- | :------------------------ |
| **Tên Thật**   | Maya Torres |
| **Codename**    | GLITCH                    |
| **Class**       | Specialist                |
| **Quốc Tịch** | American |
| **Tuổi**         | 27                        |
| **Chiều Cao**      | 175 cm (5'9")             |
| **Cân Nặng**      | 68 kg (150 lbs)           |

### Lý Lịch

Maya Torres từng là thần đồng tại MIT trước khi bỏ học để gia nhập đơn vị cyber warfare tinh nhuệ của NSA. Khả năng tìm exploit trong mọi hệ thống khiến cô trở nên vô giá, cho đến khi cô phát hiện cơ quan này dùng công cụ của mình để giám sát hàng loạt công dân Mỹ.

Cô rò rỉ những gì có thể rồi biến mất, dùng kỹ năng của mình để cân bằng sân chơi cho những người không có lợi thế công nghệ. Trong Exclusion Zone, nơi công nghệ có thể quyết định sống chết, GLITCH đảm bảo không ai có lợi thế bất công.

### Tính Cách

- **Anti-authority** - Không tin các tổ chức quyền lực
- **Clever** - Luôn đi trước ba nước
- **Sardonic** - Dùng hài hước để né tránh cảm xúc
- **Ethical** - Có những ranh giới không bao giờ vượt qua

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
| **Âm Lượng Bước Chân** | 95% | Slightly quieter than average — sneakers |
| **Bán Kính Audio Ability** | 40 meters | EMP pulse is very loud — tín hiệu audio lớn |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 0% | Đủ thời lượng |
| Slow | 0% | Đủ thời lượng |
| Burn | 0% | Full DoT |
| EMP | 100% | Immune to enemy GLITCH EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 38 cm radius, 175 cm height |
| **Vùng Đầu** | 14 cm radius |
| **Collision Profile** | Standard |
| **Silhouette Nhìn Từ Trên Xuống** | Trung bình build, antenna array on backpack, arm-mounted hacking interface visible |
| **Vùng Accent Theo Class** | Yellow (#EAB308) on tech strips and backpack antenna |
| **EMP VFX (Top-Down)** | Blue-white expanding ring from operator (15m radius), static distortion on affected units |
| **EMP Audio Radius** | 40m — loud pulse crack audible at extreme range |

<!-- REF_IMAGE: GLITCH top-down view — showing operator with EMP blast active, blue-white expanding ring visible from above, static effects on enemies in radius -->

### Độ Khó

**Độ Khó: 4/5** — EMP timing is everything. Using it too early wastes it; too late and shields/drones already did their job. Reading enemy tech usage is critical.


## Ability

### Active Ability: EMP Blast

> *"Release an electromagnetic pulse that disables all technology in the area."*

| Thuộc Tính     | Giá Trị                         |
| :----------- | :---------------------------- |
| **Cooldown** | 110 seconds                   |
| **Duration** | Instant (effects last 10 sec) |
| **Charges**  | 1                             |

#### Hiệu Ứng

| Hiệu Ứng             | Target                 | Duration   |
| :----------------- | :--------------------- | :--------- |
| Ability Disable    | Địch operators        | 10 seconds |
| Gadget Destruction | All gadgets in range   | Permanent  |
| HUD Disruption     | Địch                | 5 seconds  |
| Khiên Destruction | AEGIS, BASTION shields | Instant    |

#### Ma Trận Tương Tác EMP

| Target | Hiệu Ứng | Duration |
| :----- | :----- | :------- |
| **AEGIS Guardian Khiên** | Destroyed instantly | Permanent (until redeployed) |
| **BASTION Riot Khiên** | Disabled (not destroyed) | 5 seconds |
| **SUTURE Hồi máu Drone** | Destroyed instantly | Permanent |
| **SONAR UAV** | Destroyed, falls from sky | Permanent |
| **MIRAGE Sensors** | All in radius destroyed | Permanent |
| **PULSE Nano Swarm** | Dispersed instantly | Permanent |
| **MAMBA Combat Stim** | Cancelled | Immediate |
| **TARTARUS Berserker Rage** | Cancelled | Immediate |
| **OBSIDIAN Smoke Screen** | Not affected | N/A — smoke is chemical, not tech |
| **GOLIATH Overcharge** | Bonus armor stripped | Immediate |
| **Địch HUD** | Static distortion | 5 seconds |

#### VFX EMP Top-Down

| State | VFX From Above |
| :---- | :------------- |
| EMP charging | Blue-white glow building on GLITCH's arm device |
| EMP blast | Blue-white ring expanding outward from operator (15m radius) |
| EMP on enemy | Blue static sparks on affected operator, HUD disruption VFX |
| Gadget destroyed | Blue flash + debris scatter from gadget position |
| Khiên broken | Dramatic shatter VFX on AEGIS dome / BASTION arc flicker |


| Thuộc Tính       | Giá Trị                  |
| :------------- | :--------------------- |
| Radius         | 15 meters              |
| Vertical Range | Full height            |
| Line of Sight  | Not required           |
| Friendly Lửa  | No (allies unaffected) |

#### What Gets Disabled

| Category | Affected |
| :------- | :------- |
| **Destroys** | AEGIS Khiên, Hồi máu Drone, Motion Sensors, Turrets |
| **Disables** | Combat Stim, Berserker, UAV Scan, Smoke Emitters |
| **Immune** | Passive abilities, Vũ khí, Giáp |

#### Slot Upgrade

**Slot 1 (Level 5):**
| Option              | Hiệu Ứng                                  |
| :------------------ | :-------------------------------------- |
| **Longer Blackout** | Disable duration +5 seconds (15s total) |
| **Quick Hack**      | Cooldown -25 seconds (85s total)        |
| **Wide Signal**     | Radius +5 meters (20m total)            |

**Slot 2 (Level 20):**
| Option              | Hiệu Ứng                                  |
| :------------------ | :-------------------------------------- |
| **System Shock**    | Disabled enemies take 10 damage         |
| **Sensor Overload** | Disabled enemies are also slowed 20%    |
| **Cascade Failure** | Destroyed gadgets explode for 15 damage |

**Slot 3 (Level 35):**
| Option             | Hiệu Ứng                                           |
| :----------------- | :----------------------------------------------- |
| **Total Blackout** | Also disables enemy minimap for 20 seconds       |
| **Power Drain**    | Killing a disabled enemy reduces cooldown by 20s |
| **Counter-Tech**   | Immune to being EMP'd/disabled yourself          |

---

### Passive Ability: Hacker's Toolkit

> *"Every system has a backdoor. I just know where to look."*

| Điều Kiện             | Hiệu Ứng                                    |
| :-------------------- | :---------------------------------------- |
| Interacting with tech | +20% speed                                |
| Near enemy gadget     | See outline through walls (5m)            |
| Destroying gadget     | Reveal player who placed it for 3 seconds |

**Interactions Affected:**
- Hacking terminals
- Opening locked containers
- Disarming traps
- Accessing intel points

---

## Loadout

### Loadout Mặc Định

| Slot          | Item                      | Ghi Chú            |
| :------------ | :------------------------ | :--------------- |
| **Primary**   | MAC-10 SMG                | Compact, fast    |
| **Secondary** | G17 Pistol                | Standard         |
| **Tactical**  | EMP Grenades ×2, Lockpick | Extra disruption |
| **Giáp**     | Trung bình Vest               | 50 armor         |

### Loadout Khuyến Nghị

**Hard Counter:**
| Slot      | Item        | Why                |
| :-------- | :---------- | :----------------- |
| Primary   | UMP-45      | Stable, accurate   |
| Secondary | G17         | -                  |
| Tactical  | EMP Nade ×3 | Maximum disruption |

**Loot Focused:**
| Slot      | Item                | Why             |
| :-------- | :------------------ | :-------------- |
| Primary   | VSS                 | Quiet looting   |
| Secondary | Silenced Pistol     | Stay quiet      |
| Tactical  | Lockpick ×2, EMP ×1 | Access + safety |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Counter-Tech
- Disable enemy abilities before fight
- Destroy defensive gadgets
- Enable team pushes

**Secondary Role:** Objective Specialist
- Fast hacking/interaction
- First to locked areas
- Intel gathering

### Thời Điểm Dùng EMP

**Perfect Timing:**
- Right before team push
- When enemy activates ability (cancel it)
- Against defensive setup

**Bad Timing:**
- When no enemy tech nearby
- While solo (wasted potential)
- On cooldown before key fight

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent    | Why Favorable              | Tactic               |
| :---------- | :------------------------- | :------------------- |
| **AEGIS**   | Khiên bị phá hủy ngay lập tức | EMP > Push           |
| **SUTURE**     | Drone destroyed            | Kill drone first     |
| **BASTION** | Khiên disabled            | EMP ends his defense |
| **MIRAGE** | Sensors destroyed          | Clear his traps      |

### Kèo Cân Bằng

| Opponent     | Ghi Chú                   | Key to Winning    |
| :----------- | :---------------------- | :---------------- |
| **SONAR**  | Both tech-focused       | Timing war        |
| **PULSE**     | Both disable            | Who EMPs first    |
| **GOLIATH** | Giáp buff not disabled | Focus fire anyway |

### Kèo Bất Lợi

| Opponent  | Why Difficult                           | Counter Strategy |
| :-------- | :-------------------------------------- | :--------------- |
| **MAMBA** | After EMP, he still out-guns you        | Team support     |
| **TARTARUS** | Berserker can activate before/after EMP | Keep range       |
| **IGNITION** | Lửa isn't tech                         | Avoid fire zones |

---

## Câu Thoại

### Combat

| Trigger               | Line                            |
| :-------------------- | :------------------------------ |
| Ability Activation    | "EMP out! Systems down!"        |
| Gadget Destroyed      | "Nice toy. Had a nice toy."     |
| Kill (Disabled Địch) | "Should've gone analog."        |
| Hacking               | "I'm in."                       |
| Reviving              | "Stay with me, got work to do." |

### Tính Cách

| Trigger            | Line                                |
| :----------------- | :---------------------------------- |
| Match Start        | "Let's see what toys they brought." |
| Extraction Success | "Data secured. We're out."          |
| Detecting Gadget   | "I see you... hackable."            |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Black hoodie under lightweight tactical vest, multiple USB drives on belt
- **Headgear:** Black beanie with tech goggles pushed up on forehead
- **Gloves:** Fingerless gloves (hacker aesthetic, touch-screen compatible)
- **Face:** Youthful, slight stubble, always watching screens

<!-- REF_IMAGE: GLITCH default skin — top-down view showing lean silhouette, hoodie under vest, tech goggles on forehead, utility belt with EMP device -->

### Skin Có Thể Mở Khóa

| Skin | Rarity | Mở Khóa |
| :--- | :----- | :----- |
| **White Hat** | Common | Level 10 |
| **Darknet** | Uncommon | 1,000 Credits |
| **Anonymous** | Rare | Level 25 |
| **Mainframe** | Epic | Battle Pass S2 |
| **Ghost in the Shell** | Legendary | Crossover Event |

### Vật Phẩm Signature

| Item | Mô Tả |
| :--- | :---------- |
| **USB Bandolier** | Row of encrypted USB drives on chest harness |
| **Binary Tattoo** | Circuit-pattern tattoo on left forearm |
| **Laptop Stickers** | Hacker collective logos on laptop (visible in lobby) |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character | Relationship |
| :-------- | :----------- |
| **SONAR** | Complicated — she hunted leakers like him at the CIA, now forced allies |
| **PULSE** | Fellow outcasts, share tech knowledge — closest friend in the roster |
| **AEGIS** | She represents the institutions he hates — philosophical tension |
| **MAMBA** | MAMBA distrusts him — "Too many secrets." GLITCH finds the suspicion amusing |

### Hook Câu Chuyện

- Leaked NSA surveillance tools are now being used by Corporation — feels responsible
- Maintains a dark web presence under the alias "Z3R0_DAY"
- Seeking the pharmaceutical exec who weaponized PULSE's nano research
- Dead drop quest chain — encrypted messages hidden across all maps

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- EMP Blast is the strongest counter-ability in the game — 110s cooldown is justified
- EMP should NOT cancel passive abilities or deactivate weapons — only active abilities and deployables
- Khiên Destruction is instant and permanent — AEGIS and BASTION players should hear a distinct "shield broken" audio cue
- -10% weapon accuracy class trait ensures GLITCH loses straight gunfights — his power is in disruption timing
- Cascade Failure upgrade (Slot 2) explosive damage should have a minimum range to prevent self-harm from nearby gadget destruction

### Yêu Cầu Animation

- EMP activation (0.8 seconds — pull device from vest, slam button)
- EMP pulse VFX (expanding blue-white ring from operator)
- Hacking animation (fast typing gesture on arm-mounted interface)
- Gadget detection HUD (blue outline through walls at 5m)
- Death animation: collapses backward, device sparks (tech failure)

### Yêu Cầu Audio

| Sound | Ghi Chú |
| :---- | :---- |
| EMP activate | Rising electronic whine + sharp pulse crack |
| EMP effect (enemy perspective) | Static burst + HUD distortion noise |
| Hacking interaction | Rapid keyboard clicks + data transfer chirps |
| Gadget detected | Soft electronic ping (only GLITCH hears) |
| Footsteps | Standard weight — sneakers on concrete |

### Ghi Chú Riêng Cho Top-Down

- EMP expanding ring must be visible at minimum zoom — largest VFX radius in the game (15m)
- Static distortion on affected enemies should be visible from top-down (blue sparking particles)
- Gadget destruction VFX must clearly communicate which gadgets were destroyed
- GLITCH is immune to enemy EMP — this is a critical balance point in mirror matchups
- -10% weapon accuracy penalty means GLITCH should lose aim duels — his power is in EMP timing
- Tech Scavenge passive (hack enemy gadgets) should show a clear interaction prompt from above
