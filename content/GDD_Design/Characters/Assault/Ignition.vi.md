---
title: "IGNITION - Ji-yoon Kwon"
type: docs
---

## Hồ Sơ Operator

> *"Họ có thể chạy, nhưng không thể trốn khỏi ngọn lửa."*

### Thông Tin Cơ Bản

| Thuộc Tính       | Giá Trị             |
| :-------------- | :---------------- |
| **Tên Thật**   | Ji-yoon Kwon      |
| **Codename**    | IGNITION          |
| **Class**       | Assault           |
| **Quốc Tịch** | South Korean      |
| **Tuổi**         | 28                |
| **Chiều Cao**      | 170 cm (5'7")     |
| **Cân Nặng**      | 62 kg (137 lbs)   |

<!-- REF_IMAGE: IGNITION operator portrait — firefighter gear modified for combat, red bandana, intense eyes, holding Molotov or flamethrower nozzle -->

### Lý Lịch

Ji-yoon Kwon lớn lên ở Seoul, nơi cô gây dựng danh tiếng là một kỹ sư hỏa thuật thất thường nhưng cực kỳ tài năng. Khả năng điều khiển lửa và làm việc trong điều kiện khắc nghiệt của cô nhanh chóng thu hút sự chú ý của các nhà tuyển mộ quân sự.

Sau thời gian phục vụ như một combat engineer chuyên về vũ khí gây cháy, Ji-yoon mất niềm tin vào hệ thống chỉ huy. Cô đào ngũ và hiện hoạt động trong Exclusion Zone, dùng chuyên môn hỏa thuật để dọn phòng, khóa vị trí địch và tạo hỗn loạn có chủ đích.

### Tính Cách

- **Intense** - Làm gì cũng đầy lửa và tận lực
- **Reckless** - Đôi khi vượt qua ranh giới mà người khác không dám vượt
- **Fiercely Independent** - Không bao giờ mù quáng tuân lệnh nữa
- **Protective** - Thiêu cháy bất kỳ ai đe dọa team của mình

---

## Thông Số Combat

### Chỉ Số Cơ Bản

| Stat             | Giá Trị   | Bộ Điều Chỉnh Class | Cuối Cùng    |
| :--------------- | :------ | :------------- | :------- |
| **Máu**       | 100 HP  | -              | 100 HP   |
| **Giáp**        | 50      | -10%           | 45       |
| **Tốc Độ Sprint** | 5.5 m/s | +10%           | 6.05 m/s |
| **Tốc Độ Đi Bộ**   | 3.5 m/s | -              | 3.5 m/s  |
| **Tốc Độ Crouch** | 2.0 m/s | -              | 2.0 m/s  |

### Bộ Điều Chỉnh Damage

| Điều Kiện              | Bộ Điều Chỉnh                       |
| :--------------------- | :----------------------------- |
| Damage Vũ Khí Cơ Bản     | +5% (Class)                    |
| Damage Lửa (Ability)  | 15 DPS for 5 seconds           |
| Lửa + Trúng Trực Tiếp      | 75 total (nếu đứng trong lửa) |
| Kháng Lửa (Bản thân) | Miễn nhiễm với lửa của chính mình             |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 120 | +20% (Assault class) |
| **Hao Stamina Khi Sprint** | 10/second | Standard |
| **Tốc Độ Hồi** | 8.8/second | +10% (Assault class) |
| **Thời Lượng Sprint Thực** | 12.0 seconds | Longest sprint tier |
| **Âm Lượng Bước Chân** | 100% | Standard |
| **Bán Kính Audio Ability** | 40 meters | Lửa crackle lớn và có hướng |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 0% | Đủ thời lượng |
| Slow | 0% | Đủ thời lượng |
| Burn | 100% (self only) | Miễn nhiễm với lửa của chính mình, nhận đủ damage từ lửa của địch |
| EMP | 0% | Incendiary Rush bị hủy ngay lập tức bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 36 cm radius, 168 cm height |
| **Vùng Đầu** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette Nhìn Từ Trên Xuống** | Compact athletic build, lighter gear, dây grenade nhìn rõ |
| **Vùng Accent Theo Class** | Orange (#F97316) trên patch vai, flame decals trên giáp |
| **Lửa Trail VFX (Top-Down)** | Bright orange line on ground, 2m wide, flickering flame particles |
| **Lửa Audio Radius** | 40m — crackling fire nghe được từ xa |

<!-- REF_IMAGE: IGNITION top-down view — showing fire trail behind operator as seen from above during Incendiary Rush, 2m trail width visible -->

### Độ Khó

**Độ Khó: 3/5** — Requires spatial awareness for fire placement. Trail creation during sprint demands good map knowledge to create effective area denial.


## Ability

### Active Ability: Incendiary Rush

> *"Deploy a trail of fire behind you while sprinting, creating area denial."*

| Thuộc Tính          | Giá Trị                      |
| :---------------- | :------------------------- |
| **Cooldown**      | 75 seconds                 |
| **Duration**      | 6 seconds (trail creation) |
| **Lửa Duration** | 8 seconds (fire persists)  |
| **Charges**       | 1                          |

#### Hiệu Ứng

| Hiệu Ứng           | Giá Trị           | Ghi Chú                      |
| :--------------- | :-------------- | :------------------------- |
| Lửa Trail Width | 2 meters        | Creates wall behind you    |
| Damage Lửa      | 15 HP/second    | Standing in fire           |
| Sprint Bonus     | +20%            | While ability active       |
| Trail Length     | Up to 30 meters | Depends on sprint distance |

#### Rule Tương Tác Lửa

| Interaction | Result |
| :---------- | :----- |
| **Lửa + MIRAGE Sensors** | Sensors destroyed by fire contact |
| **Lửa + PULSE Nano Swarm** | Both damage effects stack on enemies caught in overlap zone |
| **Lửa + AEGIS Khiên** | Lửa does NOT pass through Guardian Khiên |
| **Lửa + BASTION Khiên** | Lửa does NOT pass through Riot Khiên |
| **Lửa + Smoke (OBSIDIAN)** | Lửa burns through smoke — smoke does not extinguish |
| **Lửa + EMP (GLITCH)** | EMP cancels Incendiary Rush immediately, existing fire persists |

#### VFX Vệt Lửa Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Trail creation | Bright orange line on ground behind sprinting operator |
| Lửa active | Flickering flame particles, 2m wide, orange-yellow glow on ground |
| Lửa fading (last 2s) | Flames shrink, glow dims, smoke wisps rise |
| Lửa expired | Dark scorch mark on ground (fades after 5s) |

#### Tín Hiệu Hình Ảnh & Audio

**Bản thân:**
- Feet leave fire footprints
- Screen edges glow orange
- Lửa crackling audio

**Địch Perspective:**
- Visible fire trail
- Smoke particles rising
- Distinct ignition sound

#### Cách Dùng Tactical

| Use Case             | Strategy                                 |
| :------------------- | :--------------------------------------- |
| **Entry Denial**     | Run across doorway to block entrance     |
| **Escape Route**     | Create fire between you and pursuers     |
| **Flank Prevention** | Seal off one angle while pushing another |
| **Zone Control**     | Cut off extraction point access          |
| **Chase Prevention** | Injured? Run and leave fire              |

#### Slot Upgrade

**Slot 1 (Level 5):**
| Option             | Hiệu Ứng                               |
| :----------------- | :----------------------------------- |
| **Scorched Earth** | Lửa duration +4 seconds (12s total) |
| **Rapid Ignition** | Cooldown -15 seconds (60s total)     |
| **Thermal Surge**  | Lửa damage +5 DPS (20 total)        |

**Slot 2 (Level 20):**
| Option            | Hiệu Ứng                                     |
| :---------------- | :----------------------------------------- |
| **Inferno Width** | Lửa trail width +1 meter (3m total)       |
| **Smoke Screen**  | Lửa creates vision-blocking smoke         |
| **Napalm Stick**  | Lửa applies slow effect (-30% move speed) |

**Slot 3 (Level 35):**
| Option               | Hiệu Ứng                                   |
| :------------------- | :--------------------------------------- |
| **Phoenix Protocol** | Walking through own fire heals 5 HP/sec  |
| **Wildfire**         | Lửa spreads 1m outward over duration    |
| **Flashpoint**       | Địch exiting fire are briefly blinded |

---

### Passive Ability: Pyromaniac

> *"Lửa damage dealt to enemies restores health."*

| Điều Kiện                        | Hiệu Ứng                         |
| :------------------------------- | :----------------------------- |
| Địch takes fire damage from you | Heal 2 HP per second they burn |
| Multiple enemies burning         | Heal for each enemy            |
| Maximum heal per ability         | 30 HP                          |

**Design Intent:** Rewards aggressive area denial and creating chaos.

---

## Loadout

### Loadout Mặc Định

| Slot          | Item            | Ghi Chú                   |
| :------------ | :-------------- | :---------------------- |
| **Primary**   | PP-19 Bizon SMG | Cao mag, medium damage |
| **Secondary** | G17 Pistol      | Standard sidearm        |
| **Tactical**  | Molotov ×2      | Extra fire damage       |
| **Giáp**     | Trung bình Vest     | 50 armor points         |

### Loadout Khuyến Nghị

**Full Pyro:**
| Slot      | Item       | Why                          |
| :-------- | :--------- | :--------------------------- |
| Primary   | MP5K       | Fast fire rate for finishing |
| Secondary | Flare Gun  | Extra fire (meme but fun)    |
| Tactical  | Molotov ×2 | Maximum fire coverage        |

**Balanced Ignition:**
| Slot      | Item                 | Why                  |
| :-------- | :------------------- | :------------------- |
| Primary   | AK-74u               | Good damage at range |
| Secondary | G17                  | Reliable backup      |
| Tactical  | Molotov ×1, Smoke ×1 | Lửa + escape        |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Area Denial
- Block chokepoints with fire
- Control enemy movement
- Create chaos in fights

**Secondary Role:** Entry Fragger
- Push through your own fire (immune)
- Surprise enemies expecting you to avoid fire
- Flank while fire distracts

### Vòng Lặp Combat

```
1. Identify key chokepoint
2. Activate Incendiary Rush
3. Sprint across to create fire wall
4. Push through fire to surprise enemies
5. Use conventional weapons while fire does work
6. Heal from passive as enemies burn
7. Reposition for cooldown, repeat
```

### Mẹo Đặt Lửa

**Good Lửa Placement:**
- Doorways and windows
- Extraction point approaches
- Behind you while retreating
- Between enemy and teammate

**Bad Lửa Placement:**
- Your team's planned route
- Near friendly healing zones
- In open areas (easy to avoid)

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent     | Why Favorable                 | Tactic                     |
| :----------- | :---------------------------- | :------------------------- |
| **GOLIATH** | Slow, can't escape fire       | Trap in fire zones         |
| **BASTION**  | Khiên doesn't stop fire      | Circle around, create fire |
| **AEGIS**    | Khiên can't heal fire damage | Burn through shield value  |

### Kèo Cân Bằng

| Opponent    | Ghi Chú                             | Key to Winning            |
| :---------- | :-------------------------------- | :------------------------ |
| **MAMBA**   | Stim vs Lửa, different strengths | Avoid direct gunfight     |
| **SUTURE**     | Can heal through fire             | Kill drone first          |
| **SONAR** | Intel vs area denial              | Lửa blocks common routes |

### Kèo Bất Lợi

| Opponent    | Why Difficult                 | Counter Strategy                     |
| :---------- | :---------------------------- | :----------------------------------- |
| **MIRAGE** | Traps counter your aggression | Clear traps carefully                |
| **PULSE**    | Nano swarm can zone you back  | Trade zones, don't engage in swarm   |
| **OBSIDIAN**  | Smoke negates fire visibility | Use fire for area denial, not vision |

---

## Câu Thoại

### Combat

| Trigger                  | Line                                   |
| :----------------------- | :------------------------------------- |
| Ability Activation       | "Light 'em up!"                        |
| Ability Activation (Alt) | "Burn, baby, burn!"                    |
| Kill                     | "Toasted."                             |
| Kill (Lửa)              | "How's the heat?"                      |
| Kill (Lửa, Alt)         | "Should've stayed out of the kitchen." |
| Thấp Máu               | "Running hot over here!"               |
| Reviving                 | "Don't fade on me!"                    |

### Callout

| Trigger          | Line                                    |
| :--------------- | :-------------------------------------- |
| Địch Spotted    | "Got eyes on a target!"                 |
| Lửa Placed      | "Area's hot!"                           |
| Multiple Địch | "Got a crowd - perfect for a barbecue!" |
| Reloading        | "Swapping!"                             |
| Molotov Throw    | "Lửa in the hole!"                     |

### Tính Cách

| Trigger            | Line                                       |
| :----------------- | :----------------------------------------- |
| Match Start        | "Time to turn up the heat."                |
| Extraction Called  | "Almost done. Let's not get burned now."   |
| Extraction Success | "Another successful job. Time for drinks." |
| Squad Wipe         | "Nobody escapes the flames."               |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Dark red tactical jacket, black cargo pants
- **Headgear:** Red bandana covering lower face
- **Gloves:** Heat-resistant black gloves
- **Face:** Light scarring from old burns, intense eyes

### Skin Có Thể Mở Khóa

| Skin            | Rarity    | Mở Khóa         |
| :-------------- | :-------- | :------------- |
| **Wildfire**    | Common    | Level 10       |
| **Ash Gray**    | Uncommon  | 1,000 Credits  |
| **Inferno**     | Rare      | Level 25       |
| **Firefighter** | Epic      | Battle Pass S1 |
| **Hellfire**    | Legendary | Season 2 Event |

### Vật Phẩm Signature

| Item            | Mô Tả                             |
| :-------------- | :-------------------------------------- |
| **Lighter**     | Zippo always in hand during idle        |
| **Burn Scars**  | Arms have healed burn marks             |
| **Lửa Tattoo** | Phoenix on back (visible on some skins) |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character  | Relationship                              |
| :--------- | :---------------------------------------- |
| **MAMBA**  | Friendly rivalry, respects his directness |
| **SUTURE**    | Treated her burns, she owes him           |
| **OBSIDIAN** | Dislikes smoke interfering with fire      |
| **TARTARUS**  | Kindred spirits, both reckless            |

### Hook Câu Chuyện

- Looking for the officer who ordered the village burning
- Has contacts in the cartel underworld
- Hides guilt behind bravado and flames

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Lửa is powerful but telegraphed
- Miễn nhiễm với lửa của chính mình = unique gameplay
- Cooldown prevents constant fire spam
- Lửa damage over time allows counterplay

### Yêu Cầu Animation

- Lửa trail VFX (procedural along sprint path)
- Foot ignition particles while sprinting
- Molotov throw animation
- Death animation: Covers face (protecting from flames)

### Ghi Chú Kỹ Thuật

| System      | Ghi Chú                                                |
| :---------- | :--------------------------------------------------- |
| Lửa Trail  | Spawns every 0.5m along sprint path                  |
| Performance | Max 3 active fire zones at once                      |
| Collision   | Lửa is non-physical, just damage zone               |
| Networking  | Lửa positions synced, damage calculated server-side |

### Ghi Chú Riêng Cho Top-Down

- Lửa trail must be clearly visible at minimum zoom — bright orange on ground plane
- Lửa trail width (2m) should read as a meaningful barrier from above, not a thin line
- Scorch marks after fire expires provide temporary intel on where IGNITION has been
- Lửa particle effects must not obscure loot items on ground within fire zone
- Sprint path prediction: server calculates fire spawn points every 0.5m along the actual path taken
