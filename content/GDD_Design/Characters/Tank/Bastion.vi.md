---
title: "BASTION - Mikhail Ivanov"
type: docs
---

## Hồ Sơ Operator

> *"Sau lưng tôi. Không thứ gì lọt qua."*

### Thông Tin Cơ Bản

| Thuộc Tính | Giá Trị |
| :-------- | :---- |
| **Tên Thật** | Mikhail Ivanov |
| **Codename** | BASTION |
| **Class** | Tank |
| **Quốc Tịch** | Russian |
| **Tuổi** | 41 |
| **Chiều Cao** | 195 cm (6'5") |
| **Cân Nặng** | 110 kg (243 lbs) |

<!-- REF_IMAGE: BASTION operator portrait — massive frame, riot shield on back, heavy tactical vest, cyberpunk-style reinforced plating with orange accent strips -->

### Lý Lịch

Hans Richter từng là bức tường bất động của GSG 9, đơn vị chống khủng bố tinh nhuệ của Đức. Khả năng giữ vị trí dưới hỏa lực áp đảo của anh trở thành huyền thoại sau vụ bao vây đại sứ quán năm 2019, nơi anh bảo vệ 30 con tin trong 8 giờ chỉ với một riot shield và ý chí của mình.

Sau một bê bối chính trị khiến ngân sách bị cắt và đơn vị của anh bị giải tán, Hans không thể quay lại đời sống dân sự. Exclusion Zone cho anh thứ anh cần: một nhiệm vụ rõ ràng, kẻ địch để chặn lại, và người cần bảo vệ.

### Tính Cách

- **Stoic** — Hiếm khi bộc lộ cảm xúc
- **Protective** — Sống để bảo vệ người khác
- **Stubborn** — Không rút lui
- **Honorable** — Tôn trọng đối thủ xứng đáng

---

## Thông Số Combat

### Chỉ Số Cơ Bản

| Stat | Giá Trị | Bộ Điều Chỉnh Class | Cuối Cùng |
| :--- | :---- | :------------- | :---- |
| **Máu** | 100 HP | - | 100 HP |
| **Giáp** | 75 | +25% cap | 75 (max 125) |
| **Tốc Độ Sprint** | 5.5 m/s | -15% | 4.675 m/s |
| **Tốc Độ Đi Bộ** | 3.5 m/s | - | 3.5 m/s |
| **Tốc Độ Crouch** | 2.0 m/s | - | 2.0 m/s |

### Bộ Điều Chỉnh Damage

| Điều Kiện | Bộ Điều Chỉnh |
| :-------- | :------- |
| Damage Vũ Khí Cơ Bản | +0% (no class bonus) |
| Khiên Bash | 30 flat damage + 1.5s stun |
| Standing still (Living Wall) | +15% damage resistance |
| In cover (Living Wall) | +20% damage resistance |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 80 | -20% (Tank class) |
| **Hao Stamina Khi Sprint** | 12/second | +20% (Tank class) |
| **Tốc Độ Hồi** | 7.2/second | -10% (Tank class) |
| **Thời Lượng Sprint Thực** | 6.7 seconds | Shortest in roster |
| **Âm Lượng Bước Chân** | 120% | Loudest operator — armored boots |
| **Bán Kính Audio Ability** | 35 meters | Khiên deploy slam is very loud |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 25% | Tank class resist |
| Slow | 25% | Tank class resist |
| Burn | 10% | Minor fire resist from armor |
| EMP | 0% | Khiên disabled for 5 seconds bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 48 cm radius, 188 cm height |
| **Vùng Đầu** | 15 cm radius |
| **Collision Profile** | Heavy (+5% from mesh) |
| **Silhouette Nhìn Từ Trên Xuống** | Widest operator, shield visible on back when stowed, massive shoulder plates |
| **Vùng Accent Theo Class** | Steel Blue (#3B82F6) on shoulder plates and visor edge |
| **Khiên VFX (Top-Down)** | 120-degree arc indicator on ground when deployed, metallic surface visible |
| **Khiên Audio** | 35m — deploy slam + constant metallic scraping when walking |

<!-- REF_IMAGE: BASTION top-down view — showing operator with riot shield deployed, 120-degree arc visible from above, widest operator silhouette -->

### Riot Khiên Stat Block

| Thuộc Tính | Giá Trị | Ghi Chú |
| :------- | :---- | :---- |
| **Khiên Coverage** | 180-degree frontal arc | Indestructible |
| **Duration** | 15 seconds | Active time |
| **Movement Penalty** | -40% | Very slow while deployed |
| **Vũ khí Access** | Secondary only | Pistol only |
| **Khiên Bash Damage** | 30 | + 1.5s stun |
| **Khiên Bash Range** | 2 meters | Close range only |
| **Khiên Bash Cooldown** | 5 seconds | Internal cooldown |
| **EMP Vulnerability** | Disabled 5s | Not destroyed, temporarily disabled |
| **Lửa Pass-Through** | No | Blocks IGNITION fire trail |
| **Smoke Pass-Through** | Yes | Smoke passes through shield |

### Độ Khó

**Độ Khó: 2/5** — Simple concept: deploy shield, push forward. Thấp mechanical complexity but requires positional awareness to avoid flanks.


## Ability

### Active Ability: Riot Shield Deploy

> *"Deploy an indestructible riot shield. Cannot fire while active."*

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Cooldown** | 80 seconds |
| **Duration** | 15 seconds |
| **Khiên Coverage** | 180 degree frontal arc |

#### Hiệu Ứng

| Hiệu Ứng | Giá Trị | Ghi Chú |
| :----- | :---- | :---- |
| Damage Block | 100% frontal | Cannot be broken by any weapon |
| Movement Penalty | -40% | Very slow — commit to direction |
| Vũ khí Use | Secondary only | Pistol while shield deployed |
| Melee | Yes | Khiên bash causes stun |

#### Rule Tương Tác Khiên

| Interaction | Result |
| :---------- | :----- |
| **Khiên + EMP (GLITCH)** | Khiên disabled for 5 seconds (not destroyed) |
| **Khiên + Lửa (IGNITION)** | Lửa does NOT pass through riot shield |
| **Khiên + Nano Swarm (PULSE)** | Swarm ignores shield — passes through |
| **Khiên + TARTARUS Melee** | Melee bash staggers shield (1s), does not break |
| **Khiên + UAV Scan (SONAR)** | Does not reveal shielded operator |
| **Khiên + Smoke (OBSIDIAN)** | Smoke blocks vision around/through shield |

#### VFX Khiên Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Khiên deploy | Flash + 120-degree arc indicator appears on ground |
| Khiên active | Metallic surface nhìn rõ từ trên xuống, arc indicator persistent |
| Khiên taking fire | Spark particles on shield surface |
| Khiên bash | Forward thrust VFX, stun spark on target |
| Khiên EMP'd | Blue static flash, arc indicator flickers off for 5s |
| Khiên stow | Arc indicator fades |


| Thuộc Tính | Giá Trị |
| :------- | :---- |
| Damage | 30 |
| Stun Duration | 1.5 seconds |
| Range | 2 meters |
| Cooldown | 5 seconds (during shield) |

#### Slot Upgrade

**Slot 1 (Level 5):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Extended Guard** | Duration +5 seconds (20s total) |
| **Quick Deploy** | Cooldown -20 seconds (60s total) |
| **Mobile Wall** | Movement penalty -15% (only -25%) |

**Slot 2 (Level 20):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Khiên Bash+** | Bash damage +20, stun +0.5 sec |
| **Reflective Surface** | 10% damage reflected back to shooter |
| **Steadfast** | Immune to stagger/knockback |

**Slot 3 (Level 35):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Forward Unto Dawn** | Gain 50 temporary HP when deploying |
| **Team Aura** | Đồng minh behind shield gain +10% damage |
| **Explosive Kháng** | Block 50% grenade damage |

---

### Passive Ability: Living Wall

> *"The bigger they are, the harder they stand."*

| Điều Kiện | Hiệu Ứng |
| :-------- | :----- |
| Standing still | +15% damage resistance |
| In cover | +20% damage resistance |
| Taking fire | Generate Aggro (enemies more likely to target you in PvE) |

**Design Intent:** BASTION is the anchor. His shield is the most powerful single defensive ability in the game, but the trade-off is severe: almost no offensive capability while deployed. He creates space — teammates use it.

---

## Loadout

### Loadout Mặc Định

| Slot | Item | Ghi Chú |
| :--- | :--- | :---- |
| **Primary** | SPAS-12 Shotgun | CQB power |
| **Secondary** | .44 Magnum | Cao damage pistol (usable behind shield) |
| **Tactical** | Flashbang x1, Extra Giáp Plate x1 | Entry + durability |
| **Giáp** | Heavy Vest | 75 armor points |

### Loadout Khuyến Nghị

**The Juggernaut (Aggressive Push):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | AA-12 Auto Shotgun | Devastating CQB when shield drops |
| Secondary | Deagle | Maximum damage behind shield |
| Tactical | Flashbang x2 | Disorient before shield push |

**Extraction Anchor (Defensive Hold):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | SPAS-12 Shotgun | Doorway control |
| Secondary | .44 Magnum | Range option behind shield |
| Tactical | Extra Giáp Plate x2 | Maximum durability for extraction hold |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Point Leader
- Be first into contested areas with shield up
- Draw enemy fire and attention
- Create safe space for team to operate

**Secondary Role:** Extraction Anchor
- Hold extraction zone with shield
- Block doorways and chokepoints
- Protect teammates during helicopter arrival

### Vòng Lặp Combat

```
1. Communicate plan ("Shield pushing left side")
2. Deploy Riot Shield
3. Walk forward — draw fire (15 second window)
4. Shield Bash if enemies close (30 damage + 1.5s stun)
5. Team pushes around flanks during enemy focus on you
6. Drop shield when enemies are distracted
7. Switch to primary weapon for cleanup
8. Retreat and wait for 80s cooldown
```

### Vị Trí

**Good Positions:**
- Narrow corridors (shield covers entire width)
- Doorways (one direction of threat)
- Extraction zones with walls behind you
- In front of Support operators

**Bad Positions:**
- Open ground (flanked easily around shield)
- Multiple doorways (cannot block all)
- Elevated positions (shield does not block grenades from below)
- Far from team (shield wasted without shooters behind)

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **MAMBA** | Khiên blocks all Combat Stim damage | Face him, let stim timer expire |
| **TARTARUS** | Khiên stops Berserker Rush completely | Khiên up when he charges, bash stun |
| **IGNITION** | Khiên blocks incendiary rounds | Walk through fire zones protected |

### Kèo Cân Bằng

| Opponent | Ghi Chú | Key to Winning |
| :------- | :---- | :------------- |
| **GOLIATH** | Both Tanks, neither can kill the other quickly | Whoever has team support wins |
| **SUTURE** | Cannot damage him faster than drone heals | Focus drone with bash, then SUTURE |
| **AEGIS** | Guardian Khiên vs Riot Khiên — stalemate | Wait for her shield duration, then push |

### Kèo Bất Lợi

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **OBSIDIAN** | Smoke negates shield — cannot see targets | Drop shield in smoke, use primary weapon with audio |
| **GLITCH** | EMP instantly disables Riot Khiên | Bait EMP before deploying, or pre-deploy and absorb EMP |
| **SONAR** | UAV reveals flanking teammates — shield becomes useless without team pressure | Coordinate push timing with team, rush during scan cooldown |

---

## Câu Thoại

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Khiên up! I'll cover you!" |
| Khiên Bash | "Back!" |
| Taking Heavy Lửa | "I can take it. Keep moving!" |
| Khiên Down | "Khiên dropping. Need a moment." |
| Kill | "Cleared." |
| Kill (Khiên Bash) | "Stay down." |
| Thấp Máu | "Giáp failing. Fall back!" |
| Reviving | "Not today, friend. Get up." |

### Callout

| Trigger | Line |
| :------ | :--- |
| Địch Spotted | "Contact front." |
| Pushing | "Moving up. Stay behind me." |
| Reloading | "Reloading. Cover." |
| Khiên Ready | "Khiên ready. Say the word." |

### Tính Cách

| Trigger | Line |
| :------ | :--- |
| Match Start | "I go first. Stay behind me." |
| Extraction Called | "Hold here. Nothing gets past." |
| Extraction Success | "Mission complete. All secure." |
| Squad Wipe | "Nobody touches my team." |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Heavy tactical plate carrier, reinforced arm guards, riot shield on back
- **Headgear:** Open-face tactical helmet with visor, clear face visible
- **Gloves:** Reinforced knuckle gloves
- **Face:** Clean-shaven, square jaw, small scar above right eyebrow, focused eyes

<!-- REF_IMAGE: BASTION default skin — top-down view showing largest silhouette in roster, shield visible on back, heavy armor profile -->

### Skin Có Thể Mở Khóa

| Skin | Rarity | Mở Khóa |
| :--- | :----- | :----- |
| **Iron Wall** | Common | Level 10 |
| **Winter Guard** | Uncommon | 1,000 Credits |
| **Crimson Goliath** | Rare | Level 25 |
| **GSG 9 Classic** | Epic | Battle Pass S1 |
| **Siegebreaker** | Legendary | Season 1 Event |

### Vật Phẩm Signature

| Item | Mô Tả |
| :--- | :---------- |
| **Khiên Markings** | Tally marks scratched into riot shield surface |
| **GSG 9 Unit Patch** | Original unit insignia on left shoulder |
| **Cross Pendant** | Steel cross visible at collar (from grandmother) |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character | Relationship |
| :-------- | :----------- |
| **MAMBA** | Rival philosophies — MAMBA attacks, BASTION defends. Mutual respect despite constant arguments |
| **SUTURE** | Old friends from joint NATO training. Saved each other's lives. Closest bond in the roster |
| **TARTARUS** | Professional animosity — BASTION considers TARTARUS too reckless, a danger to teammates |
| **GOLIATH** | Fellow Tank. Paternal bond — BASTION mentors the younger GOLIATH in shield work |

### Hook Câu Chuyện

- Searching for former GSG 9 teammates scattered after unit disbandment
- Has evidence that the political scandal was engineered by Corporation interests
- Maintains a personal code of honor — will not extract without confirming all teammates are safe
- Receives anonymous letters from someone claiming to be his former commander

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Riot Khiên is indestructible by design — counterplay is flanking, EMP, or waiting it out
- 180-degree coverage means back and sides are always vulnerable
- -40% movement penalty is critical — BASTION cannot chase or flee effectively
- Khiên Bash stun (1.5s) is strong but has 5s internal cooldown to prevent stunlock
- Team Aura upgrade (Slot 3) must require strict positioning — allies must be within 3m of BASTION's back arc
- Living Wall passive should NOT stack with Khiên — choose one or the other

### Yêu Cầu Animation

- Khiên deploy animation (0.7 seconds — pull from back mount, forward snap)
- Khiên walk cycle (heavy, feet planted, slower than normal walk)
- Khiên bash animation (shield thrust forward, 0.3 second impact)
- Khiên stow animation (0.5 seconds — return to back mount)
- Death animation: falls to one knee, then forward (shield clatters)

### Yêu Cầu Audio

| Sound | Ghi Chú |
| :---- | :---- |
| Khiên deploy | Heavy metallic slam + pneumatic lock |
| Khiên walk | Heavy metal drag, boot impacts |
| Khiên impact (bullets) | Metallic ping per hit (satisfying) |
| Khiên bash | Heavy slam + enemy stagger grunt |
| Khiên stow | Metallic slide + lock click |
| Footsteps | Heaviest in roster — armored boots on floor |

### Ghi Chú Riêng Cho Top-Down

- Khiên arc indicator (120-degree) must be visible at minimum zoom — shows teammates and enemies the protected zone
- Khiên is visually distinct from AEGIS's dome: flat metallic surface vs translucent dome
- Khiên walking animation from top-down should show heavy foot plants with dust/ground disturbance
- When EMP disabled, shield visually flickers (communicates vulnerability window to both teams)
- BASTION is the widest silhouette in the game — easily identifiable even at max zoom
