---
title: "TARTARUS - Carlos Mendes"
type: docs
---

## Hồ Sơ Operator

> *"Do dự là chết. Tôi chọn bạo lực."*

### Thông Tin Cơ Bản

| Thuộc Tính       | Giá Trị                     |
| :-------------- | :------------------------ |
| **Tên Thật**   | Carlos Mendes             |
| **Codename**    | TARTARUS                  |
| **Class**       | Assault                   |
| **Quốc Tịch** | Brazilian                 |
| **Tuổi**         | 38                        |
| **Chiều Cao**      | 191 cm (6'3")             |
| **Cân Nặng**      | 98 kg (216 lbs)           |

<!-- REF_IMAGE: TARTARUS operator portrait — massive scar on face, thick spetsnaz armor, heavy shotgun, berserker rage visible in eyes -->

### Lý Lịch

Carlos Mendes từng là huyền thoại của BOPE Brazil trước khi một chiến dịch thất bại khiến anh trở thành người sống sót duy nhất của đơn vị. Bị cấp trên tham nhũng đổ lỗi cho thảm họa, anh bị tước danh dự và xóa khỏi hồ sơ chính thức.

Trong nhiều năm, Carlos lang bạt như một lính đánh thuê, danh tiếng lớn dần như một đội phá hủy chỉ có một người. Anh không tìm đồng đội, anh tìm mục tiêu. Exclusion Zone chỉ là một chiến trường khác, và Carlos chưa từng thua một trận đánh do chính anh khơi mào.

### Tính Cách

- **Brutal** - Không khoan nhượng, không do dự
- **Solitary** - Thích hành động một mình
- **Haunted** - Mất toàn bộ squad và mang mặc cảm của người sống sót
- **Respectful** - Tôn trọng đối thủ xứng đáng

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

| Điều Kiện                | Bộ Điều Chỉnh                |
| :----------------------- | :---------------------- |
| Damage Vũ Khí Cơ Bản       | +5% (Class)             |
| Berserker Active         | +35% melee, +15% weapon |
| Berserker + Kill         | Refreshes duration      |
| Melee Damage (Base)      | 50                      |
| Melee Damage (Berserker) | 67                      |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 120 | +20% (Assault class) |
| **Hao Stamina Khi Sprint** | 10/second | Standard |
| **Tốc Độ Hồi** | 8.8/second | +10% (Assault class) |
| **Thời Lượng Sprint Thực** | 12.0 seconds | Longest sprint tier |
| **Âm Lượng Bước Chân** | 110% | Slightly louder — heavy build |
| **Bán Kính Audio Ability** | 50 meters | Rage roar is the loudest activation in the game |
| **Melee Lunge Range** | 3.5 meters | Extended melee lunge during Berserker Rage |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 0% | Đủ thời lượng — critical vulnerability |
| Slow | 0% | Đủ thời lượng — devastating during Rage |
| Burn | 0% | Full DoT |
| EMP | 0% | Rage bị hủy ngay lập tức bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 44 cm radius, 190 cm height |
| **Vùng Đầu** | 15 cm radius |
| **Collision Profile** | Standard (largest among Assault) |
| **Silhouette Nhìn Từ Trên Xuống** | Broad-shouldered, aggressive stance, largest Assault operator |
| **Vùng Accent Theo Class** | Orange (#F97316) + Red (#DC2626) during Rage |
| **Rage Active VFX (Top-Down)** | Red pulsing glow on body, wider aggressive stance, ground crack effects on melee |
| **Melee VFX (Top-Down)** | Red arc slash visible on ground plane, 3.5m range |
| **Rage Audio Radius** | 50m — loudest ability activation in roster |

<!-- REF_IMAGE: TARTARUS top-down view — showing operator in normal vs Berserker Rage stance from above, red glow and melee range arc visible -->

### Độ Khó

**Độ Khó: 4/5** — Cao risk/reward. Must close distance without dying, manage kill chain timer, and accept +10% incoming damage. Requires aggressive confidence.


## Ability

### Active Ability: Berserker Rage

> *"Enter a frenzy state. Each kill extends the rage."*

| Thuộc Tính         | Giá Trị               |
| :--------------- | :------------------ |
| **Cooldown**     | 100 seconds         |
| **Duration**     | 8 seconds (base)    |
| **Extension**    | +3 seconds per kill |
| **Max Duration** | 20 seconds          |

#### Hiệu Ứng

| Hiệu Ứng         | Giá Trị  | Ghi Chú                 |
| :------------- | :----- | :-------------------- |
| Melee Damage   | +35%   | Makes melee viable    |
| Vũ khí Damage  | +15%   | Less than MAMBA stim  |
| Movement Speed | +15%   | All movement types    |
| Damage Taken   | +10%   | Trade-off             |
| Kill Extension | +3 sec | Encourages aggression |

#### Tương Tác Ability

| Interaction | Result |
| :---------- | :----- |
| **Rage + EMP** | Rage bị hủy ngay lập tức, kill chain timer lost |
| **Rage + Stun** | Full stun duration — wastes precious Rage seconds |
| **Rage + AEGIS Khiên** | TARTARUS melee CAN push through Guardian Khiên |
| **Rage + BASTION Khiên** | Melee bash staggers shield (1s), does not break through |
| **Rage + Burn** | Burn damage stacks with +10% incoming damage modifier |
| **Rage + Kill (SONAR scanned target)** | Kill still extends duration even if target was scanned |

#### VFX Cuồng Nộ Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Rage activation | Red flash burst from operator, ground cracks radiate outward (1m) |
| Rage active | Persistent red body glow, widened stance animation |
| Melee swing | Red arc slash on ground (3.5m forward cone) |
| Kill chain (kill during rage) | Brief bright flash + timer refresh indicator |
| Rage ending | Glow dims, operator visibly exhales (hunched posture) |


**Bản thân:**
- Screen pulses red
- Heavy breathing audio
- Blood splatter on screen edges

**Địch Perspective:**
- Red glow around Tartarus
- Audible roar on activation
- Movements appear more aggressive

#### Cơ Chế Chuỗi Hạ Gục

The unique aspect of Berserker Rage is the **kill extension**:

```
Base activation: 8 seconds
Kill 1: 8 + 3 = 11 seconds remaining
Kill 2: 11 + 3 = 14 seconds remaining
Kill 3: 14 + 3 = 17 seconds remaining
Kill 4+: Capped at 20 seconds
```

**Design Intent:** Cao risk, potentially infinite uptime if you're skilled enough.

#### Slot Upgrade

**Slot 1 (Level 5):**
| Option           | Hiệu Ứng                                       |
| :--------------- | :------------------------------------------- |
| **Blood Frenzy** | Kill extension +2 seconds (5 total per kill) |
| **Quick Rage**   | Cooldown -20 seconds (80s total)             |
| **Iron Will**    | Damage taken penalty removed                 |

**Slot 2 (Level 20):**
| Option                | Hiệu Ứng                                        |
| :-------------------- | :-------------------------------------------- |
| **Executioner**       | Melee kills heal 20 HP                        |
| **Unstoppable Force** | Immune to knockback/stun                      |
| **Terror**            | Nearby enemies hear heartbeat (psychological) |

**Slot 3 (Level 35):**
| Option         | Hiệu Ứng                                            |
| :------------- | :------------------------------------------------ |
| **Last Stand** | If killed during rage, explode for 50 area damage |
| **Rampage**    | Each kill also reduces cooldown by 5 seconds      |
| **Predator**   | Damaged enemies are marked for 5 seconds          |

---

### Passive Ability: Bloodlust

> *"The closer to death, the stronger he becomes."*

| Máu Threshold | Hiệu Ứng                            |
| :--------------- | :-------------------------------- |
| Below 50%        | +10% weapon damage                |
| Below 30%        | +15% weapon damage, +5% movement  |
| Below 15%        | +20% weapon damage, +10% movement |

**Synergy with Berserker:** Combined with rage mode at low health = devastating damage output.

**Design Intent:** Makes TARTARUS terrifying when cornered. Never assume a low-health TARTARUS is easy.

---

## Loadout

### Loadout Mặc Định

| Slot          | Item            | Ghi Chú               |
| :------------ | :-------------- | :------------------ |
| **Primary**   | SPAS-12 Shotgun | CQB dominance       |
| **Secondary** | Desert Eagle    | Cao damage backup  |
| **Tactical**  | Flashbang ×2    | Entry tool          |
| **Giáp**     | Trung bình Vest     | 50 armor points     |
| **Melee**     | Combat Knife    | Enhanced by passive |

### Loadout Khuyến Nghị

**Full Berserker:**
| Slot      | Item               | Why                |
| :-------- | :----------------- | :----------------- |
| Primary   | AA-12 Auto Shotgun | Spray and pray     |
| Secondary | Revolver           | One-shot potential |
| Tactical  | Stun Grenade ×2    | Close the gap      |
| Melee     | Machete            | Higher base damage |

**Controlled Aggression:**
| Slot      | Item                   | Why                     |
| :-------- | :--------------------- | :---------------------- |
| Primary   | UMP-45 SMG             | More range than shotgun |
| Secondary | G17                    | Reliable backup         |
| Tactical  | Flashbang ×1, Smoke ×1 | Entry + escape          |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** CQB Specialist
- Dominates close quarters
- Clears rooms aggressively
- Terrifies enemies in tight spaces

**Secondary Role:** Finisher
- Chase down wounded enemies
- Capitalize on team damage
- Execute distracted targets

### Vòng Lặp Combat

```
1. Get close (use cover, flanks, smoke)
2. Activate Berserker Rage
3. Engage closest enemy
4. Secure kill -> Duration extends
5. Immediately move to next target
6. Chain kills to maintain rage
7. If no kills in 8 seconds, retreat
```

### Áp Đảo Cự Ly Gần

**Best Engagement Range:** 0-10 meters

| Range  | Tactic                              |
| :----- | :---------------------------------- |
| 0-3m   | Melee or shotgun                    |
| 3-10m  | Shotgun or SMG                      |
| 10-20m | SMG only, don't engage if avoidable |
| 20m+   | Disengage, reposition               |

### Khi KHÔNG Nên Chọn TARTARUS

- Long-range maps (open areas)
- Địch team has multiple Tanks
- Your team has no healer
- You're not confident in CQB

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent    | Why Favorable           | Tactic                    |
| :---------- | :---------------------- | :------------------------ |
| **SUTURE**     | Fragile up close        | Rush before drone deploys |
| **SONAR** | No combat advantage     | Close distance fast       |
| **GLITCH**  | Thấp combat stats        | Overwhelm with aggression |
| **AEGIS**   | Can't escape your speed | Push through shield       |

### Kèo Cân Bằng

| Opponent    | Ghi Chú                         | Key to Winning           |
| :---------- | :---------------------------- | :----------------------- |
| **MAMBA**   | Both aggressive, comes to aim | Land first shot          |
| **IGNITION**   | Lửa vs Rage                  | Avoid fire while closing |
| **MIRAGE** | Traps slow you down           | Clear traps, then push   |

### Kèo Bất Lợi

| Opponent     | Why Difficult                 | Counter Strategy        |
| :----------- | :---------------------------- | :---------------------- |
| **BASTION**  | Khiên completely blocks you  | Flank only, never front |
| **GOLIATH** | Team armor absorbs your burst | Focus teammates first   |
| **PULSE**     | Nano swarm slows you          | Wait for swarm to end   |

---

## Câu Thoại

### Combat

| Trigger                  | Line                       |
| :----------------------- | :------------------------- |
| Ability Activation       | *War cry in Russian*       |
| Ability Activation (Alt) | "Now you die!"             |
| Kill                     | "Pathetic."                |
| Kill (Melee)             | "Too slow."                |
| Kill Chain (3+)          | "Who's next?!"             |
| Thấp Máu               | "You think this stops me?" |
| Reviving                 | "Get up. We're not done."  |

### Callout

| Trigger       | Line                |
| :------------ | :------------------ |
| Địch Spotted | "Contact."          |
| Pushing       | "Moving in."        |
| Taking Lửa   | "They are nothing." |
| Reloading     | "Reloading."        |
| Grenade       | "Grenade."          |

### Tính Cách

| Trigger            | Line                           |
| :----------------- | :----------------------------- |
| Match Start        | "Let's finish this quickly."   |
| Extraction Called  | "Cover me. We leave now."      |
| Extraction Success | "Another day survived."        |
| Squad Wipe         | "That was almost challenging." |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Dark gray tactical sweater, black vest
- **Headgear:** Black balaclava
- **Gloves:** Worn leather combat gloves
- **Face:** Heavy scarring, cold blue eyes

### Skin Có Thể Mở Khóa

| Skin            | Rarity    | Mở Khóa               |
| :-------------- | :-------- | :------------------- |
| **Winter Wolf** | Common    | Level 10             |
| **Blood Red**   | Uncommon  | 1,000 Credits        |
| **Spetsnaz**    | Rare      | Level 25             |
| **Executioner** | Epic      | Battle Pass S2       |
| **Reaper**      | Legendary | Ranked Season Reward |

### Vật Phẩm Signature

| Item                | Mô Tả                           |
| :------------------ | :------------------------------------ |
| **Dog Tags**        | Collection from fallen squad (hidden) |
| **Scar Pattern**    | Distinctive slash marks on face       |
| **Knuckle Tattoos** | Cyrillic letters spelling "DEATH"     |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character    | Relationship                         |
| :----------- | :----------------------------------- |
| **MAMBA**    | Mutual respect between soldiers      |
| **GOLIATH** | Former comrade from Russian military |
| **BASTION**  | Considers him a worthy opponent      |
| **IGNITION**    | Kindred spirit in chaos              |

### Hook Câu Chuyện

- Seeking the general who ordered his squad's sacrifice
- Has bounty on his head from Russian intelligence
- Protects new operators from making his mistakes

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Extremely high risk, high reward
- Damage taken penalty balances damage output
- Kill chain mechanic rewards skill
- CQB focus limits map versatility

### Yêu Cầu Animation

- Rage activation: Shoulder roll + crack neck
- Movement during rage: More aggressive posture
- Melee attacks: Heavy, brutal swings
- Death: Falls to knees first, then forward

### Ghi Chú Kỹ Thuật

| System          | Ghi Chú                                  |
| :-------------- | :------------------------------------- |
| Kill Extension  | Server calculates, syncs to client     |
| Duration Timer  | Visible to player, hidden from enemies |
| Damage Bộ Điều Chỉnh | Applies before armor calculation       |
| Sounds          | Rage growl synced to all players       |

### Ghi Chú Riêng Cho Top-Down

- Rage red glow must be visible at minimum zoom — brightest self-buff VFX in the game
- Melee lunge animation from top-down should show clear forward movement (3.5m)
- Melee arc VFX on ground plane helps teammates and enemies judge range
- Kill chain timer is intentionally hidden from enemies to prevent them timing disengagements
- +10% incoming damage during Rage means TARTARUS drops faster — encourage burst or kiting counterplay
