---
title: "SUTURE - Tariq Al-Sayed"
type: docs
---

## Hồ Sơ Operator

> *"Tôi đã thề không gây hại. Tôi chưa từng nói điều đó áp dụng cho kẻ địch."*

### Thông Tin Cơ Bản

| Thuộc Tính       | Giá Trị                     |
| :-------------- | :------------------------ |
| **Tên Thật**   | Tariq Al-Sayed            |
| **Codename**    | SUTURE                    |
| **Class**       | Support                   |
| **Quốc Tịch** | Egyptian                  |
| **Tuổi**         | 42                        |
| **Chiều Cao**      | 178 cm (5'10")            |
| **Cân Nặng**      | 76 kg (168 lbs)           |

<!-- REF_IMAGE: SUTURE operator portrait — field medic gear, white cross on vest, kindly but tired expression, medical drone hovering nearby -->

### Lý Lịch

Tariq Al-Sayed từng là bác sĩ phẫu thuật chấn thương phục vụ tại các vùng xung đột khắp Trung Đông và châu Phi. Khả năng tạo ra điều kỳ diệu dưới làn đạn và cách tiếp cận chính xác, lạnh như phòng mổ giúp ông được những người lính từng chứng kiến ông kéo đồng đội khỏi bờ vực cái chết kính trọng.

Sau một cuộc extraction thù địch thất bại, Tariq bất lực nhìn binh sĩ chết trong lúc chờ cuộc sơ tán không bao giờ tới. Mất niềm tin vào bộ máy quân sự, ông rời nhiệm vụ nhưng không thoát khỏi tiếng gọi của y học nơi chiến trường. Giờ ông hoạt động trong Exclusion Zone, xem combat như một phương trình hỗn loạn cần được giải.

### Tính Cách

- **Calm Under Pressure** - Không hoảng loạn, kể cả trong hỗn loạn
- **Protective** - Xem mỗi cái chết là trách nhiệm cá nhân
- **Pragmatic** - Sẵn sàng đưa ra lựa chọn khó khăn
- **Sardonic** - Dùng hài đen để đối phó áp lực

---

## Thông Số Combat

### Chỉ Số Cơ Bản

| Stat                      | Giá Trị   | Bộ Điều Chỉnh Class | Cuối Cùng     |
| :------------------------ | :------ | :------------- | :-------- |
| **Máu**                | 100 HP  | -              | 100 HP    |
| **Giáp**                 | 40      | -              | 40        |
| **Tốc Độ Sprint**          | 5.5 m/s | -5%            | 5.225 m/s |
| **Tốc Độ Đi Bộ**            | 3.5 m/s | -5%            | 3.325 m/s |
| **Hiệu Quả Hồi Máu** | 100%    | +20%           | 120%      |

### Bộ Điều Chỉnh Hồi Máu

| Item          | Base Heal | SUTURE Bonus | Cuối Cùng    |
| :------------ | :-------- | :-------- | :------- |
| Small Medkit  | 30 HP     | +20%      | 36 HP    |
| Medkit        | 50 HP     | +20%      | 60 HP    |
| Surgery Kit   | 100 HP    | +20%      | 120 HP   |
| Hồi máu Drone | 5 HP/sec  | +20%      | 6 HP/sec |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 100 | Standard (Support class) |
| **Hao Stamina Khi Sprint** | 10/second | Standard |
| **Tốc Độ Hồi** | 8/second | Standard |
| **Thời Lượng Sprint Thực** | 10.0 seconds | Trung bình |
| **Âm Lượng Bước Chân** | 90% | Slightly quieter — designed not to alert patients |
| **Bán Kính Audio Ability** | 15 meters | Drone hum is subtle, only close-range detection |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 0% | Đủ thời lượng |
| Slow | 10% | Kháng nhẹ (Support class) — reach downed allies |
| Burn | 0% | Full DoT |
| EMP | 0% | Hồi máu Drone destroyed bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 38 cm radius, 176 cm height |
| **Vùng Đầu** | 14 cm radius |
| **Collision Profile** | Standard |
| **Silhouette Nhìn Từ Trên Xuống** | Trung bình build, large medical backpack, cross markings on shoulders |
| **Vùng Accent Theo Class** | White/Green (#22C55E) on armband cross and backpack |
| **Drone VFX (Top-Down)** | Green pulsing vòng tròn trên mặt đất (10m radius), drone model hovering at center |
| **Drone Audio Radius** | 15m — subtle hum, quietest deployable in the game |

<!-- REF_IMAGE: SUTURE top-down view — showing operator silhouette with medical gear, healing drone deployed with green radius circle visible from above -->

### Hồi máu Drone Stat Block

| Thuộc Tính | Giá Trị | Ghi Chú |
| :------- | :---- | :---- |
| **Drone HP** | 50 | Destroyable — key counterplay |
| **Heal Rate** | 6 HP/sec | With SUTURE class bonus |
| **Heal Radius** | 10 meters | Ground-plane circle |
| **Duration** | 20 seconds | Total lifetime |
| **Max Heal Total** | 120 HP/ally | Over full duration |
| **Deploy Range** | Throw (15m max) | Drone lands where thrown |
| **Can Heal Through Walls** | No | Line of sight to drone required |
| **Can Heal Through Floors** | Yes | If on adjacent floor |

### Độ Khó

**Độ Khó: 1/5** — Most beginner-friendly operator. Deploy drone, stay alive, heal team. No complex mechanics or timing required.


## Ability

### Active Ability: Healing Drone

> *"Deploy an autonomous medical drone that heals allies in radius."*

| Thuộc Tính     | Giá Trị       |
| :----------- | :---------- |
| **Cooldown** | 120 seconds |
| **Duration** | 20 seconds  |
| **Charges**  | 1           |
| **Drone HP** | 50          |

#### Hiệu Ứng

| Hiệu Ứng              | Giá Trị                | Ghi Chú                            |
| :------------------ | :------------------- | :------------------------------- |
| Heal Rate           | 5 HP/second          | +20% = 6 HP/sec with class bonus |
| Heal Radius         | 10 meters            | Centered on drone                |
| Max Heal per Deploy | 100 HP per ally      | 5 HP × 20 seconds                |
| Targets             | All allies in radius | Including SUTURE                    |

#### Rule Tương Tác Drone

| Interaction | Result |
| :---------- | :----- |
| **Drone + EMP (GLITCH)** | Drone bị phá hủy ngay lập tức |
| **Drone + Lửa (IGNITION)** | Not affected — drone hovers above fire |
| **Drone + Nano Swarm (PULSE)** | Not affected — swarm targets ground units |
| **Drone + UAV Scan (SONAR)** | Drone position revealed to scanning team |
| **Drone + BASTION Khiên** | Drone heals through shield |
| **Drone + Smoke (OBSIDIAN)** | Drone heals through smoke |

#### VFX Drone Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Drone deploy | Green flash at throw point, drone rises to hover height |
| Drone active | Green pulsing vòng tròn trên mặt đất (10m), drone model visible at center |
| Hồi máu pulse | Green particle streams from drone to allies in radius |
| Drone low HP | Sparking particles, circle flickers |
| Drone destroyed | Electrical burst, debris falls, circle disappears |


**Bản thân:**
- Drone deployment animation
- Green healing particles on allies
- Heart rate monitor beep (audio)

**Địch Perspective:**
- Drone is visible and targetable
- Green healing glow obvious
- Distinct humming sound

#### Cách Dùng Tactical

| Use Case         | Strategy                                |
| :--------------- | :-------------------------------------- |
| **Defense Hold** | Place before enemies arrive             |
| **Post-Fight**   | Deploy after combat to restore team     |
| **Extraction**   | Heal while waiting for helicopter       |
| **Bait**         | Địch may focus drone, giving opening |

#### Slot Upgrade

**Slot 1 (Level 5):**
| Option               | Hiệu Ứng                           |
| :------------------- | :------------------------------- |
| **Extended Care**    | Duration +10 seconds (30s total) |
| **Rapid Response**   | Cooldown -30 seconds (90s total) |
| **Enhanced Formula** | Heal rate +2 HP/sec (7 base)     |

**Slot 2 (Level 20):**
| Option             | Hiệu Ứng                       |
| :----------------- | :--------------------------- |
| **Armored Drone**  | Drone HP +30 (80 total)      |
| **Mobile Unit**    | Drone follows SUTURE slowly     |
| **Expanded Range** | Radius +5 meters (15m total) |

**Slot 3 (Level 35):**
| Option              | Hiệu Ứng                                  |
| :------------------ | :-------------------------------------- |
| **Revive Protocol** | Drone can revive downed allies (10 sec) |
| **Combat Stim**     | Đồng minh in range get +5% damage          |
| **Stealth Mode**    | Drone is harder to see/hear             |

---

### Passive Ability: Field Medic

> *"Faster revives and emergency self-treatment."*

| Điều Kiện          | Hiệu Ứng                             |
| :----------------- | :--------------------------------- |
| Reviving Đồng minh    | +15% faster                        |
| Bản thân Heal          | Can use healing items 20% faster   |
| Downed Đồng minh Nearby | See health bar through walls (10m) |

**Design Intent:** SUTURE should always know who needs help and get to them fast.

---

## Loadout

### Loadout Mặc Định

| Slot          | Item                     | Ghi Chú              |
| :------------ | :----------------------- | :----------------- |
| **Primary**   | MP5 SMG                  | Reliable mid-range |
| **Secondary** | G17 Pistol               | Standard sidearm   |
| **Tactical**  | Medkit ×3, Hồi máu Drone | Maximum healing    |
| **Giáp**     | Light Vest               | 30 armor points    |

### Loadout Khuyến Nghị

**Combat Medic:**
| Slot      | Item                | Why               |
| :-------- | :------------------ | :---------------- |
| Primary   | MP7                 | Better in CQB     |
| Secondary | G17                 | Reliable          |
| Tactical  | Medkit ×2, Smoke ×1 | Smoke for revives |

**Pure Support:**
| Slot      | Item                       | Why                      |
| :-------- | :------------------------- | :----------------------- |
| Primary   | P90                        | Cao mag for suppression |
| Secondary | G17                        | -                        |
| Tactical  | Medkit ×3, Surgical Kit ×1 | Maximum heal potential   |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Team Healer
- Maintain team health
- Enable extended engagements
- Revive downed teammates

**Secondary Role:** Anchor
- Hold positions with healing
- Recover team after fights
- Survive to help others

### Ma Trận Ưu Tiên Hồi Máu

| Priority | Target            | When                   |
| :------- | :---------------- | :--------------------- |
| 1        | Assault in combat | They're your damage    |
| 2        | Tank taking fire  | They're your shield    |
| 3        | Yourself          | Dead medic = dead team |
| 4        | Recon/Specialist  | Usually not in danger  |

### Đặt Drone

**Good Placement:**
- Behind cover
- Near choke points
- Extraction zones
- Not in direct fire

**Bad Placement:**
- Open areas
- Far from team
- Where enemies can easily destroy

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent     | Why Favorable                   | Tactic                 |
| :----------- | :------------------------------ | :--------------------- |
| **MIRAGE**  | Traps can't kill if you heal    | Out-sustain the damage |
| **PULSE**     | Nano swarm is slow damage       | Heal through it        |
| **GOLIATH** | Thấp offense, you sustain better | Attrition warfare      |

### Kèo Cân Bằng

| Opponent    | Ghi Chú                       | Key to Winning          |
| :---------- | :-------------------------- | :---------------------- |
| **AEGIS**   | Both Support, comes to team | Your team's DPS matters |
| **SONAR** | Intel vs healing            | Stay hidden, heal safe  |
| **OBSIDIAN**  | Smoke disrupts drone        | Place drone carefully   |

### Kèo Bất Lợi

| Opponent    | Why Difficult               | Counter Strategy         |
| :---------- | :-------------------------- | :----------------------- |
| **MAMBA**   | Burst exceeds healing       | Focus fire him first     |
| **TARTARUS**   | Kills before heal matters   | Stay far from engagement |
| **BASTION** | Protected DPS behind shield | Wait for push to end     |

---

## Câu Thoại

### Combat

| Trigger            | Line                                |
| :----------------- | :---------------------------------- |
| Ability Activation | "Drone deployed! Stay in the zone!" |
| Hồi máu Đồng minh       | "Hold still, I've got you."         |
| Kill               | "Apologies. No hard feelings."      |
| Reviving           | "You're not dying on my watch!"     |
| Thấp Máu         | "I'm hit! Need cover!"              |
| Đồng minh Downed        | "Man down! Moving to assist!"       |

### Callout

| Trigger         | Line                             |
| :-------------- | :------------------------------- |
| Địch Spotted   | "Contact spotted."               |
| Drone Destroyed | "Drone's down! Cooldown needed." |
| Thấp on Meds     | "Running low on supplies."       |
| Reloading       | "Changing mag."                  |

### Tính Cách

| Trigger            | Line                                         |
| :----------------- | :------------------------------------------- |
| Match Start        | "Right then. Let's keep everyone breathing." |
| Extraction Called  | "Evac inbound. No heroics, just survive."    |
| Extraction Success | "Job's done. Drinks are on me."              |
| Squad Wipe         | "Remarkable. We actually stayed alive."      |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** White tactical vest with red cross, khaki pants
- **Headgear:** Medical cap with tactical goggles
- **Gloves:** Blue surgical gloves
- **Face:** Graying beard, kind but tired eyes

### Skin Có Thể Mở Khóa

| Skin                  | Rarity    | Mở Khóa          |
| :-------------------- | :-------- | :-------------- |
| **Field Surgeon**     | Common    | Level 10        |
| **Desert Medic**      | Uncommon  | 1,000 Credits   |
| **Trauma Team**       | Rare      | Level 25        |
| **Battlefield Aegis** | Epic      | Battle Pass S1  |
| **Plague Suturetor**     | Legendary | Halloween Event |

### Vật Phẩm Signature

| Item             | Mô Tả           |
| :--------------- | :-------------------- |
| **Medical Bag**  | Always visible on hip |
| **Stethoscope**  | Hanging around neck   |
| **Wedding Ring** | Never removed         |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character   | Relationship                          |
| :---------- | :------------------------------------ |
| **MAMBA**   | Served together, saved his life twice |
| **IGNITION**   | Treated her burns, protective of her  |
| **AEGIS**   | Respects her dedication               |
| **BASTION** | Old friends, philosophical opposites  |

### Hook Câu Chuyện

- Wife and daughter back home, his reason to extract
- Looking for a missing medical convoy
- Has a terminal diagnosis, operates on borrowed time

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Drone is destroyable = counterplay
- Long cooldown prevents spam healing
- Thấp combat stats = relies on team
- Passive helps team coordination

### Yêu Cầu Animation

- Drone throw/deploy animation
- Green healing particle effects
- Revive animation (faster than standard)
- Death: Falls protecting medical bag

### Yêu Cầu Audio

| Sound           | Ghi Chú                           |
| :-------------- | :------------------------------ |
| Drone deploy    | Mechanical launch + hover start |
| Drone active    | Soft humming loop               |
| Hồi máu pulse   | Gentle heartbeat rhythm         |
| Drone destroyed | Electrical fizzle + crash       |

### Ghi Chú Riêng Cho Top-Down

- Hồi máu drone green circle must be visible at minimum zoom — key gameplay information for both teams
- Drone model should be slightly larger than realistic to ensure visibility from above
- Green healing particles from drone to allies must be visible but not obscure combat (thin streams)
- Drone destruction VFX should be dramatic enough to communicate to the team that healing is gone
- Drone position revealed by SONAR UAV — this is a deliberate counterplay vector
