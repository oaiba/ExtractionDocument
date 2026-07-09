---
title: "MAMBA - Thuy Nguyen"
type: docs
---

## Hồ Sơ Operator

> *"Vào đầu tiên, trụ lại cuối cùng."*

### Thông Tin Cơ Bản

| Thuộc Tính       | Giá Trị                       |
| :-------------- | :-------------------------- |
| **Tên Thật**   | Thuy Nguyen                 |
| **Codename**    | MAMBA                       |
| **Class**       | Assault                     |
| **Quốc Tịch** | Vietnamese                  |
| **Tuổi**         | 26                          |
| **Chiều Cao**      | 168 cm (5'6")               |
| **Cân Nặng**      | 60 kg (132 lbs)             |

<!-- REF_IMAGE: MAMBA operator portrait — athletic build, tactical cap, green eyes, holding combat knife, aggressive stance -->

### Lý Lịch

Thuy Nguyen từng phục vụ trong Đặc Công Việt Nam trước khi chuyển sang hoạt động lính đánh thuê ngầm. Nổi tiếng với sự hổ báo có tính toán và chiến thuật ra đòn nhanh, chí mạng, cô nhận callsign "Mamba" vì luôn tấn công không báo trước và không để lại người sống sót.

Sau một chiến dịch mật đổ vỡ, cô bị chính handler bỏ mặc cho chết. Sống sót gần như không tưởng, cô hiện là contractor tự do trong Exclusion Zone, dùng kỹ năng của mình để extract tài sản giá trị và đôi khi thanh toán những món nợ cũ.

### Tính Cách

- **Confident** - Không bao giờ nghi ngờ khả năng của mình
- **Direct** - Nói thẳng điều mình nghĩ, không vòng vo
- **Protective** - Luôn để mắt bảo vệ đồng đội
- **Vengeful** - Không bao giờ quên sự phản bội

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

| Điều Kiện           | Bộ Điều Chỉnh    |
| :------------------ | :---------- |
| Damage Vũ Khí Cơ Bản  | +5% (Class) |
| Combat Stim Active  | +25%        |
| Combat Stim + Class | +30% total  |
| Headshot Multiplier | 2.0x        |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 120 | +20% (Assault class) |
| **Hao Stamina Khi Sprint** | 10/second | Standard |
| **Tốc Độ Hồi** | 8.8/second | +10% (Assault class) |
| **Thời Lượng Sprint Thực** | 12.0 seconds | Longest sprint tier |
| **Âm Lượng Bước Chân** | 100% | Standard — no stealth bonus |
| **Bán Kính Audio Ability** | 25 meters | Stim inject hiss audible to nearby enemies |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 0% | Đủ thời lượng |
| Slow | 0% | Đủ thời lượng — devastating during stim |
| Burn | 0% | Full DoT |
| EMP | 0% | Stim bị hủy ngay lập tức bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 40 cm radius, 180 cm height |
| **Vùng Đầu** | 14 cm radius |
| **Collision Profile** | Standard |
| **Silhouette Nhìn Từ Trên Xuống** | Trung bình athletic build, cross-chest ammo belt visible, medium helmet |
| **Vùng Accent Theo Class** | Orange (#F97316) trên patch vai and ammo belt |
| **Stim Active VFX (Top-Down)** | Orange body glow, subtle particle trail when moving |
| **Stim Audio Radius** | 25m — enemies within range hear injection hiss |

<!-- REF_IMAGE: MAMBA top-down view — showing operator silhouette from 60-degree camera with orange accent zones highlighted, stim active vs inactive comparison -->

### Độ Khó

**Độ Khó: 2/5** — Straightforward kit. Press stim, shoot better. Thấp mechanical complexity, rewards good aim timing.


## Ability

### Active Ability: Combat Stim

> *"Inject experimental combat stimulant for temporary enhanced performance."*

| Thuộc Tính     | Giá Trị      |
| :----------- | :--------- |
| **Cooldown** | 90 seconds |
| **Duration** | 10 seconds |
| **Charges**  | 1          |

#### Hiệu Ứng

| Hiệu Ứng         | Giá Trị | Ghi Chú                    |
| :------------- | :---- | :----------------------- |
| Damage Boost   | +25%  | Stacks with class bonus  |
| Movement Speed | +10%  | All movement types       |
| Reload Speed   | +15%  | Faster reload animations |

#### Tương Tác Ability

| Interaction | Result |
| :---------- | :----- |
| **Stim + EMP** | Stim bị hủy ngay lập tức, remaining duration lost |
| **Stim + Burn** | Stim does NOT cleanse burn — damage stacks |
| **Stim + Slow** | Stim movement boost partially counters slow (net +0% to -5% depending on slow source) |
| **Stim + Mark** | Stim does not remove mark status |

#### Mô Tả VFX Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Stim inject | Brief orange flash on operator model (0.5s) |
| Stim active | Persistent orange glow on body, subtle particle trail on ground behind movement |
| Stim ending (last 2s) | Glow flickers, particles diminish |
| Stim expired | Glow fades, brief gray exhale particle |


#### Tín Hiệu Hình Ảnh & Audio

**Bản thân:**
- Screen edge orange vignette
- Heartbeat audio intensifies
- Hands shake slightly (cosmetic)

**Địch Perspective:**
- Operator glows orange
- Distinct injection sound (audio cue)
- Faster movement visible

#### Slot Upgrade

**Slot 1 (Level 5):**
| Option              | Hiệu Ứng                           |
| :------------------ | :------------------------------- |
| **Extended Rush**   | Duration +5 seconds (15s total)  |
| **Quick Reload**    | Cooldown -20 seconds (70s total) |
| **Adrenaline Heal** | Heal 10 HP on activation         |

**Slot 2 (Level 20):**
| Option              | Hiệu Ứng                              |
| :------------------ | :---------------------------------- |
| **Overdrive**       | Damage boost +30% (instead of +25%) |
| **Iron Skin**       | +20% damage resistance during stim  |
| **Lightning Hands** | +50% reload speed (instead of +15%) |

**Slot 3 (Level 35):**
| Option          | Hiệu Ứng                                                   |
| :-------------- | :------------------------------------------------------- |
| **Rally Cry**   | Nearby allies get +10% damage                            |
| **Second Wind** | If killed during stim, survive with 1 HP (once per life) |
| **Unstoppable** | Immune to stun/slow during stim                          |

---

### Passive Ability: Adrenaline Surge

> *"Near-death experiences fuel his combat performance."*

| Điều Kiện        | Hiệu Ứng                           |
| :--------------- | :------------------------------- |
| Máu below 30% | +15% reload speed                |
| Máu below 20% | +20% reload speed, +5% movement  |
| Máu below 10% | +25% reload speed, +10% movement |

**Design Intent:** Rewards aggressive play and creates clutch moments.

---

## Loadout

### Loadout Mặc Định

| Slot          | Item               | Ghi Chú                       |
| :------------ | :----------------- | :-------------------------- |
| **Primary**   | M4A1 Assault Rifle | Mid-tier AR, balanced stats |
| **Secondary** | G17 Pistol         | Standard sidearm            |
| **Tactical**  | Frag Grenade ×2    | Area damage                 |
| **Giáp**     | Trung bình Vest        | 50 armor points             |

### Loadout Khuyến Nghị

**Aggressive Entry:**
| Slot      | Item         | Why                  |
| :-------- | :----------- | :------------------- |
| Primary   | AK-47        | Cao damage per shot |
| Secondary | Deagle       | Backup punch         |
| Tactical  | Flashbang ×2 | Entry assistance     |

**Sustained Combat:**
| Slot      | Item              | Why                       |
| :-------- | :---------------- | :------------------------ |
| Primary   | M4A1              | Controllable, fast reload |
| Secondary | SMG (MP7)         | CQB backup                |
| Tactical  | Smoke ×1, Frag ×1 | Versatility               |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Entry Fragger
- Be first into contested areas
- Trade kills aggressively
- Create space for team

**Secondary Role:** Cleanup
- Finish wounded enemies
- Chase down runners
- Secure kills

### Vòng Lặp Combat

```
1. Wait for intel (Recon scan)
2. Pre-aim angles
3. Activate Combat Stim
4. Entry push (10 second window)
5. Eliminate or call out enemies
6. Retreat if stim expires without kills
7. Wait for cooldown, repeat
```

### Vị Trí

**Good Positions:**
- Near entry points
- With clear sightlines
- Close to Support for healing

**Bad Positions:**
- Isolated without backup
- Long rotations from team
- Exposed flanks

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent    | Why Favorable                | Tactic                        |
| :---------- | :--------------------------- | :---------------------------- |
| **SUTURE**     | Cannot outheal your damage   | Rush before drone deploys     |
| **SONAR** | Fragile, no combat advantage | Win aim duel                  |
| **PULSE**    | Thấp combat power             | Aggressive push through swarm |

### Kèo Cân Bằng

| Opponent    | Ghi Chú                      | Key to Winning                    |
| :---------- | :------------------------- | :-------------------------------- |
| **IGNITION**   | Similar role, fire vs stim | Avoid fire zones, use range       |
| **MIRAGE** | Traps are annoying         | Check corners, don't rush blindly |
| **AEGIS**   | Khiên is strong           | Wait for shield to drop           |

### Kèo Bất Lợi

| Opponent    | Why Difficult            | Counter Strategy              |
| :---------- | :----------------------- | :---------------------------- |
| **BASTION** | Khiên blocks all damage | Flank or wait for shield down |
| **GLITCH**  | EMP cancels your stim    | Bait EMP, then engage         |
| **TARTARUS**   | Out-damages you in CQB   | Keep range, use cover         |

---

## Câu Thoại

### Combat

| Trigger            | Line                                             |
| :----------------- | :----------------------------------------------- |
| Ability Activation | "Stim active! Let's go!"                         |
| Kill               | "Hostile down!"                                  |
| Kill (Headshot)    | "Clean shot."                                    |
| Downed Địch       | "They're already dead, they just don't know it." |
| Thấp Máu         | "Taking hits, need backup!"                      |
| Reviving           | "Stay with me, soldier!"                         |

### Callout

| Trigger          | Line                           |
| :--------------- | :----------------------------- |
| Địch Spotted    | "Contact! Eyes on hostile!"    |
| Multiple Địch | "Multiple contacts, heads up!" |
| Reloading        | "Mag out!"                     |
| Grenade          | "Frag out!"                    |

### Tính Cách

| Trigger            | Line                                             |
| :----------------- | :----------------------------------------------- |
| Match Start        | "Let's get this done. Stay sharp."               |
| Extraction Called  | "Bird's coming. Hold the line."                  |
| Extraction Success | "Mission complete. Another day, another dollar." |
| Squad Wipe         | "This is what we trained for."                   |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** OD Green tactical vest, black pants
- **Headgear:** Black baseball cap
- **Gloves:** Black fingerless tactical gloves
- **Face:** Clean-shaven, slight scar on left cheek

### Skin Có Thể Mở Khóa

| Skin             | Rarity    | Mở Khóa         |
| :--------------- | :-------- | :------------- |
| **Desert Storm** | Common    | Level 10       |
| **Urban Gray**   | Uncommon  | 1,000 Credits  |
| **Blood Orange** | Rare      | Level 25       |
| **Black Ops**    | Epic      | Battle Pass S1 |
| **Phoenix**      | Legendary | Season 1 Event |

### Vật Phẩm Signature

| Item           | Mô Tả                   |
| :------------- | :---------------------------- |
| **Dog Tags**   | Dangling from vest (cosmetic) |
| **Ranger Tab** | Shoulder patch                |
| **Bite Marks** | Scar pattern on left arm      |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character   | Relationship                    |
| :---------- | :------------------------------ |
| **SUTURE**     | Served together, mutual respect |
| **BASTION** | Rival, different philosophies   |
| **GLITCH**  | Distrusts - "Too many secrets"  |
| **SONAR** | Professional admiration         |

### Hook Câu Chuyện

- Looking for the handler who betrayed him
- Has intel on Corporation black sites
- Owes a favor to unknown benefactor

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Combat Stim is strong but predictable (audio cue)
- Thấp armor punishes poor timing
- Cooldown prevents ability spam
- Passive encourages aggressive play

### Yêu Cầu Animation

- Stim injection animation (1 second)
- Orange glow VFX during stim
- Heartbeat audio loop
- Death animation: Falls forward (aggressive stance)

### Yêu Cầu Audio

| Sound       | Ghi Chú                        |
| :---------- | :--------------------------- |
| Stim inject | Sharp hiss + heartbeat start |
| Stim active | Persistent heartbeat loop    |
| Stim end    | Heartbeat slowdown + exhale  |
| Footsteps   | Heavy, military boots        |

### Ghi Chú Riêng Cho Top-Down

- Stim orange glow must remain visible at minimum zoom (khoảng cách camera xa nhất)
- Stim audio cue must be directional — enemies should be able to locate MAMBA by sound
- Particle trail during stim should be subtle enough not to obscure ground loot but visible enough for enemy awareness
- When viewed from top-down, stim injection animation should show arm movement clearly (not hidden by body)
