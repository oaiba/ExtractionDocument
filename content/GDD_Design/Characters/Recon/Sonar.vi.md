---
title: "SONAR - Sarah Kim"
type: docs
---

## Hồ Sơ Operator

> *"Knowledge is the deadliest weapon. They're already dead — they just don't know it yet."*

### Thông Tin Cơ Bản

| Thuộc Tính | Giá Trị |
| :-------- | :---- |
| **Tên Thật** | Sarah Ji-Young Kim |
| **Codename** | SONAR |
| **Class** | Recon |
| **Quốc Tịch** | Korean-American |
| **Tuổi** | 29 |
| **Chiều Cao** | 168 cm (5'6") |
| **Cân Nặng** | 57 kg (126 lbs) |

<!-- REF_IMAGE: SONAR operator portrait — lean build, tactical headset with holographic HUD overlay, dark clothing with subtle cyan data-stream accents -->

### Lý Lịch

Sarah Kim từng là một trong những analyst tình báo hiệu quả nhất của CIA trước khi chuyển sang field work. Khả năng dự đoán di chuyển của địch và xử lý thông tin dưới áp lực khiến cô cực kỳ giá trị trong các chiến dịch deep cover ở Triều Tiên và Trung Quốc.

Sau khi một nội gián làm lộ mạng lưới, Sarah bất lực nhìn từng asset của mình bị loại bỏ. Cô biến mất, cắt mọi liên hệ với Agency. Giờ cô hoạt động độc lập, dùng kỹ năng của mình để đi trước tất cả ba bước, dù là đồng minh hay kẻ địch.

### Tính Cách

- **Analytical** — Mọi thứ đều là dữ liệu cần xử lý
- **Paranoid** — Không hoàn toàn tin bất kỳ ai
- **Efficient** — Không lãng phí động tác hay lời nói
- **Haunted** — Mang mặc cảm vì những asset đã mất

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
| First Shot from Stealth | +10% (Ghost Protocol passive) |
| Headshot Multiplier | 2.0x |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 110 | +10% (Recon class) |
| **Hao Stamina Khi Sprint** | 9/second | -10% (Recon class) |
| **Tốc Độ Hồi** | 9.6/second | +20% (Recon class) |
| **Thời Lượng Sprint Thực** | 12.2 seconds | Best efficiency |
| **Âm Lượng Bước Chân** | 70% | -30% (Recon class trait) |
| **Bán Kính Audio Ability** | 20 meters | UAV drone buzz audible to nearby enemies |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Đủ thời lượng |
| Burn | 0% | Full DoT |
| EMP | 0% | UAV bị phá hủy ngay lập tức bởi EMP |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 34 cm radius, 170 cm height |
| **Vùng Đầu** | 13 cm radius |
| **Collision Profile** | Slim (-10% from mesh) |
| **Silhouette Nhìn Từ Trên Xuống** | Slim build, tech goggle glow nhìn rõ từ trên xuống, compact UAV pack on back |
| **Vùng Accent Theo Class** | Cyan (#06B6D4) on goggle glow and tech strips trên giáp |
| **Scan VFX (Top-Down)** | Cyan pulse rings expanding from operator, enemy outlines appear |
| **UAV Audio Radius** | 20m — drone buzz is moderate volume |

<!-- REF_IMAGE: SONAR top-down view — showing operator with UAV scan active, cyan pulse rings expanding outward, enemy silhouettes highlighted through walls -->

### UAV Stat Block

| Thuộc Tính | Giá Trị | Ghi Chú |
| :------- | :---- | :---- |
| **Scan Radius** | 30 meters | From SONAR position |
| **Duration** | 8 seconds | Continuous scan |
| **Địch Reveal** | Real-time outlines | Cyan silhouettes through geometry |
| **Team Sharing** | Yes | All allies see scanned enemies |
| **UAV Altitude** | 15 meters above | Cannot be shot by ground fire |
| **EMP Vulnerability** | Destroyed instantly (falls) | Primary counter |
| **Smoke Interaction** | Blocks scan LOS | Cannot scan through OBSIDIAN smoke |
| **Deployable Detection** | Yes | Reveals enemy deployables (sensors, drones, shields) |

### Độ Khó

**Độ Khó: 2/5** — Simple activation: press ability, see enemies. Thấp mechanical demand, but high strategic value in knowing when to scan.


## Ability

### Active Ability: UAV Scan

> *"Deploy a drone to reveal all enemies in the area."*

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Cooldown** | 100 seconds |
| **Duration** | 8 seconds |
| **Charges** | 1 |

#### Hiệu Ứng

| Hiệu Ứng | Giá Trị | Ghi Chú |
| :----- | :---- | :---- |
| Scan Radius | 30 meters | Centered on SONAR |
| Địch Reveal | Real-time | Địch visible through walls |
| Team Sharing | Yes | All allies see marked enemies |
| Update Rate | Continuous | Not just snapshot |

#### UAV Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **UAV + EMP (GLITCH)** | UAV bị phá hủy ngay lập tức, falls from sky |
| **UAV + Lửa (IGNITION)** | Not affected — UAV is airborne |
| **UAV + Nano Swarm (PULSE)** | Not affected — swarm only targets ground |
| **UAV + Smoke (OBSIDIAN)** | Scan blocked through smoke — LOS required |
| **UAV + AEGIS Khiên** | UAV cannot reveal operators inside shield dome |
| **UAV + BASTION Khiên** | Does not reveal shielded operator |

#### Top-Down Scan VFX

| State | VFX From Above |
| :---- | :------------- |
| UAV deploy | Drone rises from operator's back, ascends to scan height |
| Scan active | Cyan pulse rings expanding from operator position (30m radius) |
| Địch detected | Red outline appears on enemy model, visible through walls |
| Scan ending | Pulse rings fade, drone descends |
| UAV EMP'd | Flash burst, drone falls to ground as debris |


**Bản thân:**
- Radar pulse animation on HUD
- Địch silhouettes through walls (cyan outlines)
- Sonar ping audio loop

**Địch Perspective:**
- Faint scanner noise (audio cue at 15m range)
- "DETECTED" indicator on HUD when scanned
- Cannot see the drone or scan radius

#### Slot Upgrade

**Slot 1 (Level 5):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Extended Scan** | Duration +4 seconds (12s total) |
| **Quick Sweep** | Cooldown -20 seconds (80s total) |
| **Wide Net** | Radius +10 meters (40m total) |

**Slot 2 (Level 20):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Threat Assessment** | Shows enemy health bars during scan |
| **Silent Scan** | Địch do not know they are scanned |
| **Tracking Dart** | One enemy stays marked for 30 seconds after scan ends |

**Slot 3 (Level 35):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Predictive Analysis** | Shows enemy movement direction arrows |
| **Vũ khí Intel** | Shows enemy weapon types on HUD |
| **Counter-Intel** | Marks enemies who scanned you back |

---

### Passive Ability: Ghost Protocol

> *"Leave no trace. Remain unseen."*

| Điều Kiện | Hiệu Ứng |
| :-------- | :----- |
| Crouch walking | -30% footstep volume (stacks with class trait) |
| In cover for 3 seconds | Reduced enemy visibility (harder to spot) |
| Not firing for 5 seconds | Do not appear on enemy minimaps |

**Design Intent:** Rewards patient, information-first gameplay. SONAR should always know more than her enemies.

---

## Loadout

### Loadout Mặc Định

| Slot | Item | Ghi Chú |
| :--- | :--- | :---- |
| **Primary** | VSS Vintorez (Silenced) | Quiet kills, integrated suppressor |
| **Secondary** | Silenced Pistol | Backup stealth |
| **Tactical** | Sensor Mines x2 | Early warning traps |
| **Giáp** | Light Vest | 30 armor points |

### Loadout Khuyến Nghị

**Long-Range Intel:**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | SVD Marksman Rifle | Engage from scan range |
| Secondary | Silenced Pistol | Emergency backup |
| Tactical | Sensor Mines x2 | Watch your back |

**Aggressive Scout:**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | MP5 (Suppressed) | CQB capability with stealth |
| Secondary | Smoke Grenade x1 | Escape tool |
| Tactical | Flashbang x2 | Entry after scan reveals positions |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Information Provider
- Scan before every engagement
- Call out enemy positions, health, and weapons
- Enable team to take favorable fights

**Secondary Role:** Flanker
- Use Ghost Protocol to move undetected
- Attack from unexpected angles after scan
- Punish enemies focused on your teammates

### Vòng Lặp Combat

```
1. Move to elevated/safe position
2. Deploy UAV Scan (8 second intel window)
3. Call out enemy positions to team
4. Team engages based on intel
5. Flank or snipe from stealth
6. Relocate before scan cooldown
7. Wait for cooldown, repeat
```

### Vị Trí

**Good Positions:**
- Elevated ground with sightlines
- Behind team, feeding intel
- Near extraction zone for final scan

**Bad Positions:**
- Point of engagement (too fragile)
- Isolated without escape route
- Ground level in open terrain

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **GOLIATH** | Scan reveals position, then flank behind shield | Scan, mark, let team focus fire |
| **PULSE** | Thấp combat stats, Nano Swarm easy to avoid with intel | Maintain distance, call out swarm |
| **SUTURE** | Fragile when caught alone, drone position revealed | Snipe drone first, then SUTURE |

### Kèo Cân Bằng

| Opponent | Ghi Chú | Key to Winning |
| :------- | :---- | :------------- |
| **MIRAGE** | Both intel operators, sensor vs. scan | Scan detects sensors, destroy them |
| **IGNITION** | Lửa zones limit movement options | Avoid fire, use range advantage |
| **AEGIS** | Khiên blocks but scan reveals timing | Wait for shield down, then burst |

### Kèo Bất Lợi

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **MAMBA** | Combat Stim out-damages you in any duel | Avoid direct combat, use intel to evade |
| **OBSIDIAN** | Smoke breaks sightlines, ruins scan value | Push through or wait out smoke duration |
| **TARTARUS** | CQB monster, you are fragile | Never let TARTARUS close the gap |

---

## Câu Thoại

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Scanning. Eyes on." |
| Địch Located | "Contact. [Direction]. [Distance]." |
| Multiple Địch | "Multiple hostiles. Marking all." |
| Kill | "Target eliminated." |
| Kill (Headshot) | "Precision." |
| Thấp Máu | "I'm hit. Need cover." |
| Reviving | "Stay with me. Intel first, then we move." |

### Callout

| Trigger | Line |
| :------ | :--- |
| Địch Spotted | "Eyes on hostile, [Direction]." |
| Reloading | "Reloading. Cover me." |
| Grenade | "Grenade! Move!" |
| Scan Expired | "Scan dark. Blind for 90 seconds." |

### Tính Cách

| Trigger | Line |
| :------ | :--- |
| Match Start | "Stay quiet. Stay alive." |
| Extraction Called | "Chopper inbound. Cuối Cùng scan." |
| Extraction Success | "Objective complete. Moving out." |
| Squad Wipe | "They never knew we were here." |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Black tactical jacket with dark blue accents, lightweight plate carrier
- **Headgear:** Tactical headset with translucent holographic monocle (HUD overlay)
- **Gloves:** Gray thin operator gloves (touch-screen compatible)
- **Face:** Short black hair, focused expression, data-stream tattoo behind left ear

<!-- REF_IMAGE: SONAR default skin — top-down view showing silhouette with UAV drone in hand, dark outfit with cyan tech accents -->

### Skin Có Thể Mở Khóa

| Skin | Rarity | Mở Khóa |
| :--- | :----- | :----- |
| **Urban Shadow** | Common | Level 10 |
| **Winter Intel** | Uncommon | 1,000 Credits |
| **Neon Ghost** | Rare | Level 25 |
| **Black Site** | Epic | Battle Pass S1 |
| **Digital Obsidian** | Legendary | Season 1 Event |

### Vật Phẩm Signature

| Item | Mô Tả |
| :--- | :---------- |
| **Holographic Monocle** | Flip-down data display over right eye |
| **USB Dog Tag** | Encrypted data drive on chain |
| **Ghost Patch** | Shoulder patch — skull with circuit board pattern |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character | Relationship |
| :-------- | :----------- |
| **MAMBA** | Professional respect, different methods — he leads from the front, she leads from the shadows |
| **GLITCH** | Uneasy allies, both have secrets — share intelligence cautiously |
| **MIRAGE** | Former adversaries during Cold War-era proxy ops, now grudging respect |
| **SUTURE** | Trusts him most — he saved one of her assets years ago |

### Hook Câu Chuyện

- Hunting the mole who burned her network (major personal quest chain)
- Has intercepted Corporation communications about "Project Lazarus"
- Maintains a dead drop network across all maps — environmental storytelling
- Received an encrypted message from a supposedly dead asset

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- UAV Scan is powerful but has a 100s cooldown — longest in the game
- 95 HP makes her the second-most fragile operator (tied with all Recon)
- Ghost Protocol rewards patience but does not make her invisible
- Scan radius (30m) is intentionally shorter than engagement range to force positioning choices
- Silent Scan upgrade (Slot 2) is the strongest option — monitor pick rate

### Yêu Cầu Animation

- UAV deployment animation (0.8 seconds — pull drone from back, throw upward)
- Scanning pulse VFX (expanding cyan ring from operator position)
- Địch outline shader (cyan silhouette through geometry, 30m range)
- Ghost Protocol crouch walk (quieter, lower stance than standard crouch)
- Death animation: falls backward (defensive stance)

### Yêu Cầu Audio

| Sound | Ghi Chú |
| :---- | :---- |
| UAV deploy | Mechanical whir + ascending drone buzz |
| Scanning active | Persistent sonar ping loop (subtle) |
| Scan end | Drone recall sound + descending buzz |
| Địch detected ping | Sharp, directional chime |
| Footsteps | Light, tactical boots — quieter than all classes |

### Ghi Chú Riêng Cho Top-Down

- Scan pulse rings must be visible at minimum zoom — clearly shows scan radius to teammates
- Địch outlines should be visible through geometry from top-down camera (red silhouettes)
- UAV drone model above the battlefield should be visible as a small cyan dot from max zoom
- Ghost Protocol first-shot bonus is not visually indicated to enemies — incentivizes stealth play
- Scan does NOT show enemy health bars — only position outlines
