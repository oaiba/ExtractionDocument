---
title: "MIRAGE - Ananya Patel"
type: docs
---

## Hồ Sơ Operator

> *"Anh nghĩ mình là thợ săn? Anh đã ở trong bẫy của tôi rồi."*

### Thông Tin Cơ Bản

| Thuộc Tính | Giá Trị |
| :-------- | :---- |
| **Tên Thật** | Ananya Patel |
| **Codename** | MIRAGE |
| **Class** | Recon |
| **Quốc Tịch** | Indian |
| **Tuổi** | 44 |
| **Chiều Cao** | 175 cm (5'9") |
| **Cân Nặng** | 72 kg (159 lbs) |

<!-- REF_IMAGE: MIRAGE operator portrait — stocky build, tactical vest with sensor nodes, cold expression, cyberpunk utility belt with motion sensors -->

### Lý Lịch

Viktor Volkov có 20 năm trong phản gián FSB, chuyên săn gián điệp nước ngoài trên đất Nga. Mạng lưới bẫy tinh vi và phong cách săn mồi kiên nhẫn khiến những kẻ sợ hắn gọi hắn là "The Spider".

Sau khi mất niềm tin vào sự mục ruỗng đang ăn mòn nước Nga từ bên trong, Viktor biến mất cùng một số hồ sơ mật. Giờ hắn dùng chuyên môn của mình trong Exclusion Zone, đặt bẫy những kẻ đủ dại để bước vào mạng nhện của hắn.

### Tính Cách

- **Patient** — Có thể chờ hàng giờ cho khoảnh khắc hoàn hảo
- **Methodical** — Mọi thứ đều theo kế hoạch
- **Cynical** — Tin rằng ai cũng có thể bị tha hóa
- **Protective** — Xem đồng đội như asset cần được bảo toàn

---

## Thông Số Combat

### Chỉ Số Cơ Bản

| Stat | Giá Trị | Bộ Điều Chỉnh Class | Cuối Cùng |
| :--- | :---- | :------------- | :---- |
| **Máu** | 100 HP | -5% | 95 HP |
| **Giáp** | 30 | - | 30 |
| **Tốc Độ Sprint** | 5.5 m/s | - | 5.5 m/s |
| **Tốc Độ Crouch** | 2.0 m/s | +15% | 2.3 m/s |
| **Âm Lượng Bước Chân** | 100% | -30% | 70% |

### Bộ Điều Chỉnh Damage

| Điều Kiện | Bộ Điều Chỉnh |
| :-------- | :------- |
| Damage Vũ Khí Cơ Bản | +0% (no class bonus) |
| Trap-assisted kill | +15 bonus damage from Shock Trap (upgrade) |
| Headshot Multiplier | 2.0x |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 110 | +10% (Recon class) |
| **Hao Stamina Khi Sprint** | 9/second | -10% (Recon class) |
| **Tốc Độ Hồi** | 9.6/second | +20% (Recon class) |
| **Thời Lượng Sprint Thực** | 12.2 seconds | Best efficiency |
| **Âm Lượng Bước Chân** | 70% | -30% (Recon class trait) |
| **Bán Kính Audio Ability** | 5 meters | Sensors are nearly silent when deployed |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Đủ thời lượng |
| Burn | 0% | Full DoT — sensors destroyed by fire |
| EMP | 0% | All sensors bị phá hủy ngay lập tức bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 40 cm radius, 182 cm height |
| **Vùng Đầu** | 14 cm radius |
| **Collision Profile** | Slim (-10% from mesh) |
| **Silhouette Nhìn Từ Trên Xuống** | Trung bình-slim build, tech harness visible, sensor pouches on belt |
| **Vùng Accent Theo Class** | Cyan (#06B6D4) on goggle glow and harness strips |
| **Sensor VFX (Top-Down)** | Small blinking devices on ground, 8m detection radius shown as faint circle when ally walks near |
| **Sensor Audio** | Nearly silent — <5m detection range for enemies |

<!-- REF_IMAGE: MIRAGE top-down view — showing operator with 3 motion sensors deployed, detection radius circles visible from above -->

### Motion Sensor Stat Block

| Thuộc Tính | Giá Trị | Ghi Chú |
| :------- | :---- | :---- |
| **Sensors Per Activation** | 3 | Deploy individually |
| **Detection Range** | 8 meters each | Overlapping for full coverage |
| **Sensor HP** | 20 | One-shot destroyable |
| **Duration** | Permanent | Until destroyed or match end |
| **Mark Duration** | 4 seconds | After detection |
| **EMP Vulnerability** | Destroyed instantly | Primary counter |
| **Lửa Vulnerability** | Destroyed on contact | Secondary counter |
| **Visibility** | Subtle blinking light | Camo Sensors upgrade removes this |

### Độ Khó

**Độ Khó: 4/5** — Sensor placement and coverage optimization require deep map knowledge. Trap Sense passive demands awareness of enemy Recon setups.


## Ability

### Active Ability: Motion Sensor Network

> *"Deploy interconnected sensors that detect and mark enemies."*

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Cooldown** | 60 seconds |
| **Duration** | Until destroyed or match end |
| **Charges** | 3 sensors per activation |

#### Hiệu Ứng

| Hiệu Ứng | Giá Trị | Ghi Chú |
| :----- | :---- | :---- |
| Detection Range | 8 meters per sensor | Overlapping coverage best |
| Sensor HP | 20 | Destroyable by gunfire or EMP |
| Alert Type | Audio + Visual ping | Directional indicator on HUD |
| Mark Duration | 4 seconds after detection | Địch visible through walls |

#### Sensor Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **Sensor + EMP (GLITCH)** | All sensors in EMP radius bị phá hủy ngay lập tức |
| **Sensor + Lửa (IGNITION)** | Sensors destroyed by fire contact |
| **Sensor + Nano Swarm (PULSE)** | Sensors not affected by swarm |
| **Sensor + UAV Scan (SONAR)** | N/A — both are intel abilities |
| **Sensor + Smoke (OBSIDIAN)** | Sensors still detect through smoke |
| **Sensor + TARTARUS Rage** | Sensors detect raging TARTARUS (louder footsteps trigger faster) |

#### Top-Down Sensor VFX

| State | VFX From Above |
| :---- | :------------- |
| Sensor deploy | Brief cyan flash on landing point |
| Sensor active | Small blinking device on ground (friendly: green glow, enemy: not visible unless detected) |
| Sensor triggered | Red pulse expanding from sensor (8m radius flash), alarm chime |
| Sensor destroyed | Brief electrical spark + pop |


| Location | Effectiveness |
| :------- | :------------ |
| Doorways | Cao — Catches entries |
| Corners | Cao — Catches flanks |
| Behind cover | Trung bình — Late warning |
| Open areas | Thấp — Easy to spot/avoid |

#### Slot Upgrade

**Slot 1 (Level 5):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Extra Sensors** | 5 sensors per activation |
| **Hardened** | Sensor HP +15 (35 total) |
| **Wide Angle** | Detection range +3 meters (11m total) |

**Slot 2 (Level 20):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Slow Field** | Detected enemies slowed 15% for 2 seconds |
| **Silent Alarm** | Địch do not know they triggered sensor |
| **Networked** | If one sees enemy, all mark them |

**Slot 3 (Level 35):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Shock Trap** | Detected enemies take 15 damage |
| **Camo Sensors** | Sensors are nearly invisible |
| **Recall** | Can pick up sensors to redeploy |

---

### Passive Ability: Trap Sense

> *"Experience makes you recognize danger."*

| Điều Kiện | Hiệu Ứng |
| :-------- | :----- |
| Near enemy trap/sensor | HUD warning (10m range) |
| Crouch detecting | Can see trap outline through walls |
| Destroy enemy trap | Gain 5-second enemy position reveal |

**Design Intent:** MIRAGE is the anti-trap specialist. While SONAR provides active intel through scanning, MIRAGE provides persistent, passive territorial control. He is the defensive Recon.

---

## Loadout

### Loadout Mặc Định

| Slot | Item | Ghi Chú |
| :--- | :--- | :---- |
| **Primary** | AK-74u (Suppressed) | Russian reliability |
| **Secondary** | Makarov Pistol | Soviet classic |
| **Tactical** | Motion Sensors x3, Claymore x1 | Layered traps |
| **Giáp** | Light Vest | 30 armor points |

### Loadout Khuyến Nghị

**The Spider's Web (Defensive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | Saiga-12 Shotgun | Close range punishment for trapped enemies |
| Secondary | Makarov Pistol | Backup |
| Tactical | Motion Sensors x3, Trip Mine x1 | Maximum area denial |

**Active Hunter (Aggressive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | AS Val (Suppressed) | Accurate, suppressed, mid-range |
| Secondary | Stun Grenades x2 | Disable after sensor trigger |
| Tactical | Motion Sensors x3 | Early warning while pushing |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Area Denial / Early Warning
- Set sensor perimeters around objectives
- Alert team to incoming flanks
- Control chokepoints with trap + weapon combos

**Secondary Role:** Counter-Intel
- Detect and destroy enemy traps
- Deny SONAR scans by detecting sensors
- Clear buildings ahead of team push

### Vòng Lặp Combat

```
1. Arrive at objective / extraction zone
2. Deploy 3 sensors at key entry points
3. Hold position and wait for triggers
4. When sensor trips — pre-aim the marked location
5. Engage with positional advantage (you know, they do not)
6. Redeploy sensors as they are destroyed
7. Repeat trap cycle
```

### Vị Trí

**Good Positions:**
- Behind his own sensor network
- In rooms with single entry points
- Near extraction zones (sensor perimeter)

**Bad Positions:**
- On the move without deployed sensors
- Open ground (sensors become useless)
- Same building as another Recon (redundant)

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **IGNITION** | Incendiary Rush is loud and predictable — sensors detect approach easily | Trap doorways, pre-aim fire paths |
| **TARTARUS** | Berserker Rush is linear — sensors give warning for easy kiting | Place sensors at CQB approach, backpedal and shoot |
| **GOLIATH** | Slow rotations, easy to track with sensor network | Surround with sensors, never let him close |

### Kèo Cân Bằng

| Opponent | Ghi Chú | Key to Winning |
| :------- | :---- | :------------- |
| **SONAR** | Both intel operators — scan vs. traps | Pre-place sensors before scan, maintain awareness |
| **AEGIS** | Guardian Khiên protects pushes through traps | Stack sensors to overwhelm shield timing |
| **MAMBA** | Combat Stim rushes can outrun sensor alerts | Layer sensors deeper, not just at entry |

### Kèo Bất Lợi

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **GLITCH** | EMP destroys all deployed sensors instantly | Space sensors apart, keep reserves |
| **OBSIDIAN** | Smoke blocks sensor engagement value | Push through smoke to trigger sensors manually |
| **SUTURE** | Hồi máu drone sustains through trap damage | Focus fire SUTURE directly, ignore drone |

---

## Câu Thoại

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Sensors deployed. The web is set." |
| Sensor Triggered | "Movement detected. [Direction]." |
| Multiple Triggers | "Multiple contacts on sensors." |
| Kill | "Predictable." |
| Kill (Trap Assisted) | "Caught in my web." |
| Thấp Máu | "Falling back. Sensors still active." |
| Reviving | "On your feet, comrade." |

### Callout

| Trigger | Line |
| :------ | :--- |
| Địch Trap Detected | "Địch trap. [Direction]." |
| Sensor Destroyed | "Sensor down. Blind spot at [Direction]." |
| Reloading | "Reloading. Watch the sensors." |

### Tính Cách

| Trigger | Line |
| :------ | :--- |
| Match Start | "Patience. The prey will come to us." |
| Extraction Called | "Pull the web tight. They will try to stop us." |
| Extraction Success | "Another successful hunt." |
| Squad Wipe | "The spider always wins." |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Olive drab tactical vest over black base layer, utility harness with sensor modules
- **Headgear:** Black beret (Russian military style), tactical earpiece
- **Gloves:** Dark leather field gloves
- **Face:** Short graying beard, scar across bridge of nose, calculating eyes

<!-- REF_IMAGE: MIRAGE default skin — top-down view showing stocky silhouette with sensor equipment visible on belt, muted military color scheme -->

### Skin Có Thể Mở Khóa

| Skin | Rarity | Mở Khóa |
| :--- | :----- | :----- |
| **Snow Web** | Common | Level 10 |
| **Night Watch** | Uncommon | 1,000 Credits |
| **Crimson Spider** | Rare | Level 25 |
| **FSB Classified** | Epic | Battle Pass S1 |
| **The Weaver** | Legendary | Season 1 Event |

### Vật Phẩm Signature

| Item | Mô Tả |
| :--- | :---------- |
| **Spider Brooch** | Small metal spider pin on collar |
| **Sensor Bandolier** | Belt of sensor modules across chest |
| **Old Dog Tags** | FSB unit tags, scratched and worn |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character | Relationship |
| :-------- | :----------- |
| **SONAR** | Former adversaries during Cold War-era proxy ops — uneasy respect born from mutual competence |
| **TARTARUS** | Both Russian, but different ideology — MIRAGE despises TARTARUS's recklessness |
| **GOLIATH** | Old military connection — served in same regional command, share tactical language |
| **OBSIDIAN** | Hunted her once during a covert operation in Japan — failed, respects her evasion |

### Hook Câu Chuyện

- Stole classified FSB files detailing Corporation connections to Russian government
- Maintains a network of informants across the Exclusion Zone (quest givers)
- Searching for his former handler who sold agent identities
- Hidden sensor caches in every map — environmental easter eggs

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Sensors are persistent but fragile (20 HP) — a single shot destroys them
- 3 sensors per activation with 60s cooldown gives steady but not overwhelming coverage
- Trap Sense passive is strong against mirror matchups — monitor Recon vs Recon win rates
- Shock Trap upgrade (15 damage) is the highest-impact Slot 3 option — consider 12 damage if overperforming
- Camo Sensors upgrade should still show a faint shimmer — truly invisible sensors are not fun to play against

### Yêu Cầu Animation

- Sensor throw animation (0.5 seconds — quick underhand toss)
- Sensor deployment VFX (small pulse on landing, then ambient glow)
- Sensor trigger VFX (red pulse expanding from triggered sensor)
- Trap detection HUD (pulsing orange marker for enemy traps)
- Death animation: collapses methodically (controlled, not dramatic)

### Yêu Cầu Audio

| Sound | Ghi Chú |
| :---- | :---- |
| Sensor deploy | Soft thud on surface + electronic chirp |
| Sensor active | Minimal ambient hum (nearly silent) |
| Sensor triggered | Sharp alarm chime (team-wide) |
| Sensor destroyed | Electric crackle + pop |
| Footsteps | Standard Recon — quiet tactical boots |
| Trap Sense alert | Thấp warning buzz when near enemy trap |

### Ghi Chú Riêng Cho Top-Down

- Sensors on the ground should be visible to the owning team as small green dots from minimum zoom
- Địch sensors should only appear if within detection range of friendly teams or revealed by Trap Sense
- Sensor trigger red pulse must be visible at minimum zoom — critical audio/visual alert
- Sensor placement animation should be quick (0.5s) and not interrupt movement flow
- Camo Sensors upgrade visual shimmer should be subtle but discoverable by attentive players at max zoom
