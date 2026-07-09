---
title: "AEGIS - Sister Maria Santos"
type: docs
---

## Hồ Sơ Operator

> *"Đức tin là tấm khiên. Nhưng đôi khi, ta cần một tấm khiên thật."*

### Thông Tin Cơ Bản

| Thuộc Tính       | Giá Trị                     |
| :-------------- | :------------------------ |
| **Tên Thật**   | Sister Maria Elena Santos |
| **Codename**    | AEGIS                     |
| **Class**       | Support                   |
| **Quốc Tịch** | Filipino                  |
| **Tuổi**         | 35                        |
| **Chiều Cao**      | 165 cm (5'5")             |
| **Cân Nặng**      | 58 kg (128 lbs)           |

<!-- REF_IMAGE: AEGIS operator portrait — tactical nun habit, serene expression, golden energy shield projector active -->

### Lý Lịch

Maria Santos từng là nữ tu kiêm y tá tại một bệnh viện truyền giáo ở Manila trước khi một vụ tấn công khủng bố thay đổi mọi thứ. Khi nhóm vũ trang tràn vào bệnh viện, Maria nhặt vũ khí của một binh sĩ đã ngã xuống và cầm chân chúng suốt ba giờ cho đến khi viện binh tới, cứu được 47 bệnh nhân và nhân viên.

Sau đó Vatican âm thầm tiếp cận cô, đề nghị huấn luyện cùng các specialist của Swiss Guard. Giờ cô hoạt động như một "thiên thần hộ mệnh", bảo vệ những người không thể tự bảo vệ mình ở các nơi nguy hiểm nhất thế giới. Exclusion Zone chỉ là vùng nhiệm vụ mới nhất của cô.

### Tính Cách

- **Serene** - Bình tĩnh không lay chuyển, kể cả trong combat
- **Protective** - Sẵn sàng chết vì team mà không do dự
- **Spiritual** - Xem combat là bảo vệ, không phải bạo lực
- **Humble** - Không bao giờ nhận công về những mạng đã cứu

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

### Bộ Điều Chỉnh Khiên

| Thuộc Tính            | Giá Trị                       |
| :------------------ | :-------------------------- |
| Guardian Khiên HP  | 200                         |
| Khiên Regeneration | 20 HP/second (khi không bị trúng đòn) |
| Khiên Radius       | 5 meters                    |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 100 | Standard (Support class) |
| **Hao Stamina Khi Sprint** | 10/second | Standard |
| **Tốc Độ Hồi** | 8/second | Standard |
| **Thời Lượng Sprint Thực** | 10.0 seconds | Trung bình |
| **Âm Lượng Bước Chân** | 85% | Quiet — nun's habit of moving silently |
| **Bán Kính Audio Ability** | 30 meters | Khiên dome hum + angelic choir rất dễ nhận biết |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 0% | Đủ thời lượng |
| Slow | 10% | Kháng nhẹ (Support class) |
| Burn | 0% | Full DoT |
| EMP | 0% | Guardian Khiên bị phá hủy ngay lập tức bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 34 cm radius, 164 cm height |
| **Vùng Đầu** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette Nhìn Từ Trên Xuống** | Slim build, máy phát khiên trên lưng, dấu thập trắng trên vai |
| **Vùng Accent Theo Class** | White/Green (#22C55E) trên băng tay và dấu thập ở backpack |
| **Khiên VFX (Top-Down)** | Blue-white hemispherical dome nhìn rõ từ trên xuống, 5m radius vòng tròn trên mặt đất |
| **Khiên Audio Radius** | 30m — angelic choir hum là một tín hiệu audio |

<!-- REF_IMAGE: AEGIS top-down view — showing operator with Guardian Shield deployed, blue-white dome visible from above as 5m radius circle -->

### Guardian Khiên Stat Block

| Thuộc Tính | Giá Trị | Ghi Chú |
| :------- | :---- | :---- |
| **Khiên HP** | 200 | Absorbs damage until depleted |
| **Khiên Radius** | 5 meters | Dome — visible as circle from above |
| **Duration** | 10 seconds | Or until HP depleted |
| **Regen Rate** | 20 HP/sec | Only when not taking damage for 2s |
| **Projectile Blocking** | One-way | Đồng minh shoot out, enemies cannot shoot in |
| **Player Walk-Through** | Yes | Địch can physically enter dome |
| **Lửa Pass-Through** | No | IGNITION fire blocked by shield wall |
| **Nano Swarm Pass-Through** | Yes | PULSE swarm passes through shield |
| **EMP Vulnerability** | Destroyed instantly | Primary counterplay |

### Độ Khó

**Độ Khó: 3/5** — Khiên placement timing is critical. Deploying too early wastes duration; too late and team takes damage. Positioning within dome matters.


## Ability

### Active Ability: Guardian Shield

> *"Project a protective dome that absorbs incoming damage."*

| Thuộc Tính      | Giá Trị      |
| :------------ | :--------- |
| **Cooldown**  | 90 seconds |
| **Duration**  | 10 seconds |
| **Charges**   | 1          |
| **Khiên HP** | 200        |

#### Hiệu Ứng

| Hiệu Ứng               | Giá Trị     | Ghi Chú                                 |
| :------------------- | :-------- | :------------------------------------ |
| Khiên Radius        | 5 meters  | Dome covers allies inside             |
| Khiên HP            | 200       | Absorbs incoming damage               |
| Regen Rate           | 20 HP/sec | Only when not taking hits             |
| Đồng minh Can Shoot Out | Yes       | One-way protection                    |
| Địch Can Enter    | Yes       | Walk through, but can't shoot through |

#### Rule Tương Tác Khiên

| Interaction | Result |
| :---------- | :----- |
| **Khiên + EMP (GLITCH)** | Khiên bị phá hủy ngay lập tức — primary counter |
| **Khiên + Lửa (IGNITION)** | Lửa does NOT pass through shield wall |
| **Khiên + Nano Swarm (PULSE)** | Swarm passes through shield — does not block |
| **Khiên + TARTARUS Melee** | TARTARUS can push through shield |
| **Khiên + UAV Scan (SONAR)** | Scan does NOT reveal operators inside shield |
| **Khiên + Smoke (OBSIDIAN)** | Smoke passes through shield dome |
| **Khiên + BASTION Khiên** | Both shields stack (dome + flat shield) |

#### VFX Khiên Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Khiên deploy | Blue-white flash, dome expands outward from AEGIS |
| Khiên active | Translucent blue-white dome, 5m radius vòng tròn trên mặt đất, faint glow |
| Khiên taking damage | Khiên sparks at impact point, slight flicker |
| Khiên low HP (<50) | Khiên cracks visible, rapid flickering |
| Khiên break | Shatter effect burst outward, AEGIS staggers |


**Bản thân:**
- Golden dome effect around team
- Aegisic humming audio
- Khiên cracks as it takes damage

**Địch Perspective:**
- Obvious golden barrier
- Shots blocked (hit markers on shield)
- Khiên flickers when low

#### Cách Dùng Tactical

| Use Case              | Strategy                          |
| :-------------------- | :-------------------------------- |
| **Extraction Hold**   | Dome over extraction point        |
| **Revive Protection** | Dome while reviving ally          |
| **Advance Khiên**    | Walk forward, team shoots through |
| **Emergency Cover**   | No natural cover? Create it       |

#### Key Difference from SUTURE

| SUTURE                      | AEGIS                        |
| :----------------------- | :--------------------------- |
| Heals damage after taken | Prevents damage entirely     |
| Passive, fire-and-forget | Active, requires positioning |
| Better for sustained     | Better for burst protection  |
| Drone can be destroyed   | Khiên has HP                |

#### Slot Upgrade

**Slot 1 (Level 5):**
| Option               | Hiệu Ứng                           |
| :------------------- | :------------------------------- |
| **Reinforced Faith** | Khiên HP +50 (250 total)        |
| **Quick Prayer**     | Cooldown -20 seconds (70s total) |
| **Extended Grace**   | Duration +5 seconds (15s total)  |

**Slot 2 (Level 20):**
| Option               | Hiệu Ứng                                    |
| :------------------- | :---------------------------------------- |
| **Hồi máu Light**    | Đồng minh in dome heal 3 HP/sec              |
| **Blinding Barrier** | Địch entering dome are briefly blinded |
| **Mobile Sanctuary** | Khiên slowly moves with AEGIS (1 m/s)    |

**Slot 3 (Level 35):**
| Option              | Hiệu Ứng                                              |
| :------------------ | :-------------------------------------------------- |
| **Martyr Protocol** | When shield breaks, AEGIS gains 50 temp HP          |
| **Resurrection**    | Downed allies in dome auto-revive (once per deploy) |
| **Divine Wrath**    | Khiên breaking deals 30 damage to nearby enemies   |

---

### Passive Ability: Guardian's Watch

> *"Never abandon those in need."*

| Điều Kiện                | Hiệu Ứng                          |
| :----------------------- | :------------------------------ |
| Đồng minh below 30% HP nearby | +10% movement speed toward them |
| Reviving allies          | Take 20% less damage            |
| Đồng minh dies within 10m     | Cooldown reduced by 10 seconds  |

**Design Intent:** AEGIS should always be moving toward danger to save allies.

---

## Loadout

### Loadout Mặc Định

| Slot          | Item                | Ghi Chú                 |
| :------------ | :------------------ | :-------------------- |
| **Primary**   | P90 SMG             | Cao mag, suppressive |
| **Secondary** | G17 Pistol          | Standard sidearm      |
| **Tactical**  | Medkit ×2, Smoke ×1 | Heal + escape         |
| **Giáp**     | Light Vest          | 30 armor points       |

### Loadout Khuyến Nghị

**Defensive Aegis:**
| Slot      | Item     | Why                     |
| :-------- | :------- | :---------------------- |
| Primary   | MP5      | Reliable, accurate      |
| Secondary | G17      | Standard                |
| Tactical  | Smoke ×2 | Extra cover for revives |

**Aggressive Aegis:**
| Slot      | Item         | Why             |
| :-------- | :----------- | :-------------- |
| Primary   | Vector       | Cao fire rate  |
| Secondary | Deagle       | Finishing power |
| Tactical  | Flashbang ×2 | Entry support   |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Damage Prevention
- Khiên during critical moments
- Protect during revives
- Cover extraction

**Secondary Role:** Emergency Response
- Rush to downed allies
- Create safe zones
- Enable risky plays

### Quản Lý Khiên

**When to Deploy:**
- Before expected engagement
- During revive attempts
- Extraction countdown
- Team retreating

**When NOT to Deploy:**
- Team scattered
- Solo fight (waste of cooldown)
- Địch can easily flank around

### Vị Trí

**Ideal Position:**
- Center of team
- With clear view of allies
- Near cover (in case shield breaks)

**Bad Position:**
- Front line
- Too far from team (shield can't reach)
- Exposed to flanks

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent  | Why Favorable               | Tactic               |
| :-------- | :-------------------------- | :------------------- |
| **MAMBA** | Khiên absorbs stim damage  | Tank his burst       |
| **IGNITION** | Lửa can't penetrate shield | Protect from fire    |
| **TARTARUS** | He can't reach you in dome  | Khiên and burst him |

### Kèo Cân Bằng

| Opponent    | Ghi Chú                     | Key to Winning     |
| :---------- | :------------------------ | :----------------- |
| **SUTURE**     | Different support styles  | Team comp decides  |
| **BASTION** | Khiên vs Khiên          | Positioning battle |
| **SONAR** | Intel useless if shielded | Timing matters     |

### Kèo Bất Lợi

| Opponent    | Why Difficult                 | Counter Strategy         |
| :---------- | :---------------------------- | :----------------------- |
| **GLITCH**  | EMP destroys shield instantly | Stay out of EMP range    |
| **MIRAGE** | Traps inside dome still work  | Clear area before dome   |
| **PULSE**    | Swarm ignores shield          | Exit dome to fight swarm |

---

## Câu Thoại

### Combat

| Trigger            | Line                                 |
| :----------------- | :----------------------------------- |
| Ability Activation | "Khiên of faith, protect us!"       |
| Khiên Takes Hit   | "They cannot break our spirit!"      |
| Khiên Breaks      | "Khiên down! Find cover!"           |
| Kill               | "Forgive me."                        |
| Reviving           | "Rise, child. Your work isn't done." |
| Thấp Máu         | "I need assistance!"                 |

### Callout

| Trigger       | Line                    |
| :------------ | :---------------------- |
| Địch Spotted | "Hostiles ahead."       |
| Đồng minh Downed   | "I'm coming! Hold on!"  |
| Reloading     | "Reloading, cover me."  |
| Smoke Out     | "Concealment deployed." |

### Tính Cách

| Trigger            | Line                                       |
| :----------------- | :----------------------------------------- |
| Match Start        | "May we all return safely."                |
| Extraction Called  | "Salvation approaches. Stay vigilant."     |
| Extraction Success | "We made it. Thank the Lord."              |
| Squad Wipe         | "They were in my care, and they are safe." |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Modified nun's habit (tactical), white and blue
- **Headgear:** Modern wimple with tactical headset
- **Gloves:** White medical gloves
- **Face:** Serene expression, prayer beads around neck

### Skin Có Thể Mở Khóa

| Skin             | Rarity    | Mở Khóa         |
| :--------------- | :-------- | :------------- |
| **Sister Mercy** | Common    | Level 10       |
| **Field Nurse**  | Uncommon  | 1,000 Credits  |
| **Valkyrie**     | Rare      | Level 25       |
| **Seraphim**     | Epic      | Battle Pass S1 |
| **Archangel**    | Legendary | Season 3 Event |

### Vật Phẩm Signature

| Item              | Mô Tả                  |
| :---------------- | :--------------------------- |
| **Rosary**        | Wrapped around left wrist    |
| **Cross Pendant** | Visible on uniform           |
| **Scripture**     | Small Bible in breast pocket |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character    | Relationship                           |
| :----------- | :------------------------------------- |
| **SUTURE**      | Deep mutual respect, different methods |
| **MAMBA**    | Saved his soul, he protects her        |
| **GOLIATH** | Orthodox vs Catholic debates           |
| **SONAR**  | She finds her methods troubling        |

### Hook Câu Chuyện

- Receives coded messages from Vatican contacts
- Investigating rumors of artifacts in the Zone
- Wrestling with whether she's saving or enabling violence

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Khiên is powerful but stationary
- EMP hard-counters it completely
- Địch can walk through (not full protection)
- Long cooldown prevents spam

### Yêu Cầu Animation

- Khiên deployment: Prayer gesture + dome expansion
- Khiên active: Golden particles, angelic audio
- Khiên break: Shatter effect + AEGIS staggers
- Idle: Occasionally makes sign of the cross

### Ghi Chú Kỹ Thuật

| System           | Ghi Chú                                   |
| :--------------- | :-------------------------------------- |
| Khiên Collision | Blocks projectiles, not players         |
| Visual           | Particle-based dome, GPU intensive      |
| Audio            | Ambient choir humming, impacts distinct |
| Networking       | Khiên HP synced, visual client-side    |

### Ghi Chú Riêng Cho Top-Down

- Khiên dome from above reads as a 5m radius circle with translucent blue-white fill
- Khiên must be visible at minimum zoom — critical gameplay information
- When shield is active, allies inside should have a subtle blue tint from above (friendly indicator)
- Khiên break shatter VFX should communicate urgency — team now exposed
- One-way projectile blocking is the core mechanic — visual differentiation between inside and outside is essential
