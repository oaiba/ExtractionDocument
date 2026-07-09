---
title: "GOLIATH - Wei Chen"
type: docs
---

## Hồ Sơ Operator

> *"Ở cạnh nhau, chúng ta không thể bị bẻ gãy. Chia rẽ ra, chúng ta chẳng là gì."*

### Thông Tin Cơ Bản

| Thuộc Tính | Giá Trị |
| :-------- | :---- |
| **Tên Thật** | Wei Chen |
| **Codename** | GOLIATH |
| **Class** | Tank |
| **Quốc Tịch** | Chinese |
| **Tuổi** | 48 |
| **Chiều Cao** | 188 cm (6'2") |
| **Cân Nặng** | 105 kg (231 lbs) |

<!-- REF_IMAGE: GOLIATH operator portrait — broad-shouldered, heavy LMG, worn body armor with team insignia patches, cyberpunk power cells on belt -->

### Lý Lịch

Wei Chen chỉ huy lực lượng VDV tinh nhuệ của Nga trong 15 năm, nổi tiếng với chiến thuật phòng thủ không thể bẻ gãy và lòng trung thành tuyệt đối với binh sĩ. Triết lý của ông: một đơn vị biết bảo vệ lẫn nhau có thể sống sót trước mọi thứ.

Sau khi từ chối mệnh lệnh có thể hy sinh binh sĩ của mình vì hình ảnh chính trị, Dmitri bị cho giải ngũ trong im lặng. Giờ ông mang phong cách lãnh đạo bảo hộ vào Exclusion Zone, nơi ability xoay quanh team của ông giữ squad sống sót trước những tình huống tưởng như không thể.

### Tính Cách

- **Paternal** — Xem team như gia đình
- **Tactical** — Luôn nghĩ cho đơn vị
- **Orthodox** — Đức tin tôn giáo sâu sắc
- **Unbreakable** — Không bao giờ bỏ rơi đồng đội

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
| Đồng minh within 5m (Brotherhood) | +5% damage resistance (both) |
| Giáp Overcharge active (self) | +15% damage resistance |
| Headshot Multiplier | 2.0x |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 80 | -20% (Tank class) |
| **Hao Stamina Khi Sprint** | 12/second | +20% (Tank class) |
| **Tốc Độ Hồi** | 7.2/second | -10% (Tank class) |
| **Thời Lượng Sprint Thực** | 6.7 seconds | Shortest in roster |
| **Âm Lượng Bước Chân** | 115% | Very loud — armored boots |
| **Bán Kính Audio Ability** | 30 meters | Overcharge power-up hum rất dễ nhận biết |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 25% | Tank class resist |
| Slow | 25% + immunity during Overcharge | Tank resist + ability grants full immunity |
| Burn | 10% | Minor fire resist from armor |
| EMP | 0% | Overcharge bonus armor stripped instantly |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 46 cm radius, 186 cm height |
| **Vùng Đầu** | 15 cm radius |
| **Collision Profile** | Heavy (+5% from mesh) |
| **Silhouette Nhìn Từ Trên Xuống** | Wide build, heavy armor pack visible, LMG barrel extends forward |
| **Vùng Accent Theo Class** | Steel Blue (#3B82F6) on shoulder plates and armor pack |
| **Overcharge VFX (Top-Down)** | Blue energy glow trên giáp plates, 8m radius pulse vòng tròn trên mặt đất for ally buff range |
| **Overcharge Audio** | 30m — deep power-up hum |

<!-- REF_IMAGE: GOLIATH top-down view — showing operator with Armor Overcharge active, blue glow on armor plates, 8m buff radius circle visible from above -->

### Độ Khó

**Độ Khó: 3/5** — Must manage Brotherhood positioning (5m ally proximity) and Overcharge timing. Simple mechanics but requires team coordination.


## Ability

### Active Ability: Armor Overcharge

> *"Overcharge your armor systems, creating a protective field for nearby allies."*

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Cooldown** | 100 seconds |
| **Duration** | 12 seconds |
| **Range** | 8 meters |

#### Hiệu Ứng

| Hiệu Ứng | Giá Trị | Ghi Chú |
| :----- | :---- | :---- |
| Bản thân Giáp Boost | +50 temporary armor | On top of current armor |
| Đồng minh Giáp Boost | +25 temporary armor | All allies within range |
| Damage Kháng | +15% (self only) | During ability |
| Slow Immunity | Yes | Cannot be slowed during overcharge |

#### Rule Tương Tác Overcharge

| Interaction | Result |
| :---------- | :----- |
| **Overcharge + EMP (GLITCH)** | Bonus armor stripped instantly, ability cancelled |
| **Overcharge + Lửa (IGNITION)** | Overcharge does not protect against fire DoT — extra armor absorbs it |
| **Overcharge + TARTARUS Rage** | Both buffs active simultaneously — neither cancels the other |
| **Overcharge + AEGIS Khiên** | Stack — overcharge armor + shield HP for maximum defense |
| **Overcharge + UAV Scan (SONAR)** | Overcharge does not interact with scans |

#### VFX Overcharge Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Overcharge activation | Blue energy burst from GOLIATH, pulse wave expands to 8m |
| Overcharge active | Blue glow trên giáp plates, faint 8m radius vòng tròn trên mặt đất |
| Đồng minh receiving buff | Blue armor particle stream from GOLIATH to ally |
| Overcharge ending | Glow dims, energy dissipates |
| Overcharge EMP'd | Blue static burst, armor plates go dark |


**Slot 1 (Level 5):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Extended Field** | Duration +4 seconds (16s total) |
| **Rapid Response** | Cooldown -25 seconds (75s total) |
| **Wide Protection** | Range +4 meters (12m total) |

**Slot 2 (Level 20):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Shared Kháng** | Đồng minh also get +10% damage resistance |
| **Giáp Regen** | Đồng minh regenerate 5 armor/sec in range |
| **Fortified** | Duration extends 2 seconds per kill |

**Slot 3 (Level 35):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Last Stand** | If downed during ability, allies keep buff for remaining duration |
| **Iron Curtain** | Đồng minh within range take 30% less headshot damage |
| **Reactive Giáp** | 20% chance to completely negate a hit |

---

### Passive Ability: Brotherhood

> *"No man left behind."*

| Điều Kiện | Hiệu Ứng |
| :-------- | :----- |
| Đồng minh within 5 meters | Both gain +5% damage resistance |
| Đồng minh downed within 10 meters | +20% movement speed toward them |
| Reviving | Take 25% less damage during revive |

**Design Intent:** GOLIATH is the team Tank. While BASTION blocks damage for one direction, GOLIATH buffs the entire team. His power scales with team proximity — solo GOLIATH is weak, but a GOLIATH team is nearly unkillable.

---

## Loadout

### Loadout Mặc Định

| Slot | Item | Ghi Chú |
| :--- | :--- | :---- |
| **Primary** | PKM LMG | Suppressive fire, large magazine |
| **Secondary** | Makarov Pistol | Russian standard sidearm |
| **Tactical** | Giáp Plates x2 | Team durability |
| **Giáp** | Heavy Vest | 75 armor points |

### Loadout Khuyến Nghị

**Suppressive Wall (Defensive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | M249 SAW | Maximum suppression, 150-round belt |
| Secondary | Makarov Pistol | Backup |
| Tactical | Giáp Plates x3 | Maximum team armor distribution |

**Mobile Goliath (Aggressive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | AK-47 | Reliable damage, controllable |
| Secondary | Stun Grenades x2 | Entry support |
| Tactical | Giáp Plates x1, Medkit x1 | Bản thân-sustain + team armoring |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Team Protector
- Stay near teammates to share Brotherhood passive
- Activate Giáp Overcharge before team engagements
- Absorb damage for fragile teammates

**Secondary Role:** Revive Specialist
- Brotherhood gives +20% sprint speed toward downed allies
- 25% damage resistance during revive makes pickups safer
- GOLIATH + SUTURE revive combo is the strongest in the game

### Vòng Lặp Combat

```
1. Position near team (within 5m for Brotherhood)
2. Identify incoming engagement
3. Activate Armor Overcharge (12 second team buff)
4. Lay suppressive fire to pin enemies
5. Prioritize reviving downed teammates (Brotherhood movement boost)
6. Hold position until overcharge expires
7. Reposition to cover while on cooldown
8. Redistribute armor plates to damaged teammates
```

### Vị Trí

**Good Positions:**
- Center of team formation (Brotherhood range)
- Near chokepoints with team around
- Behind BASTION (stack both Tank passives)
- At extraction zone with full team

**Bad Positions:**
- Solo (all abilities require teammates)
- Point position (too slow to retreat, draws focus without shield)
- Far from teammates (Brotherhood wasted)
- On the move between objectives (slow rotations)

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **IGNITION** | Overcharge armor absorbs incendiary damage, team stays alive | Overcharge, push through fire zone as a group |
| **MIRAGE** | Sensors reveal position but overcharge negates trap damage | Accept detection, push with armor advantage |
| **AEGIS** | Guardian Khiên is short duration — Overcharge outlasts it | Wait for shield to drop, then push with armored team |

### Kèo Cân Bằng

| Opponent | Ghi Chú | Key to Winning |
| :------- | :---- | :------------- |
| **BASTION** | Fellow Tank — neither kills the other fast | Whoever has better team support wins the attrition |
| **SUTURE** | Hồi máu vs Giáp — both extend team fights | Focus fire single targets to overwhelm healing |
| **OBSIDIAN** | Smoke disrupts formation but armor persists | Maintain team proximity in smoke, Brotherhood still active |

### Kèo Bất Lợi

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **SONAR** | Scan reveals entire team position, enabling flanks that split formation | Push as group before scan intel can be acted on |
| **PULSE** | Nano Swarm damages through armor, DoT bypasses flat resistance | Move team out of swarm — do not try to tank it |
| **GLITCH** | EMP does not destroy Overcharge but strips temporary armor from allies | Activate Overcharge AFTER EMP, not before |

---

## Câu Thoại

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Giáp engaged! Stay close, brothers!" |
| Đồng minh Takes Damage | "They're hitting my people!" |
| Kill | "For the squad." |
| Kill (While Protecting Đồng minh) | "Nobody touches them." |
| Đồng minh Downed | "Man down! I'm coming!" |
| Reviving | "I won't leave you. Get up!" |
| Thấp Máu | "Giáp failing... hold the line..." |

### Callout

| Trigger | Line |
| :------ | :--- |
| Địch Spotted | "Contact, [Direction]. Form up." |
| Overcharge Ready | "Giáp ready. Say when." |
| Overcharge Expired | "Overcharge down. Stay in cover." |
| Reloading | "Reloading. Cover each other." |

### Tính Cách

| Trigger | Line |
| :------ | :--- |
| Match Start | "We move as one. No one dies alone." |
| Extraction Called | "Stay together. We leave as a unit." |
| Extraction Success | "Family survives. Always." |
| Squad Wipe | "They chose the wrong unit to fight." |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Worn heavy plate carrier over dark olive fatigues, VDV insignia on shoulder
- **Headgear:** Russian military beanie (ushanka liner), tactical earpiece
- **Gloves:** Heavy leather field gloves
- **Face:** Thick salt-and-pepper beard, deep-set eyes with crow's feet, small orthodox cross tattoo on neck

<!-- REF_IMAGE: GOLIATH default skin — top-down view showing broad silhouette, LMG visible, heavy vest with armor plates, team-focused posture -->

### Skin Có Thể Mở Khóa

| Skin | Rarity | Mở Khóa |
| :--- | :----- | :----- |
| **Steel Curtain** | Common | Level 10 |
| **Arctic Patrol** | Uncommon | 1,000 Credits |
| **Red Star** | Rare | Level 25 |
| **VDV Commander** | Epic | Battle Pass S1 |
| **The Colonel** | Legendary | Season 1 Event |

### Vật Phẩm Signature

| Item | Mô Tả |
| :--- | :---------- |
| **Orthodox Cross** | Small steel cross on chain, visible at collar |
| **Unit Photo** | Faded photo of VDV squad tucked in vest pocket |
| **Command Badge** | Colonel rank insignia on right breast |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character | Relationship |
| :-------- | :----------- |
| **TARTARUS** | Fellow Russian — GOLIATH worries about TARTARUS's self-destructive tendencies, tries to mentor him |
| **MIRAGE** | Old military contacts from overlapping operations — share tactical intelligence |
| **AEGIS** | Debates faith — both deeply religious, different traditions, mutual respect |
| **BASTION** | Mentorship — BASTION teaches shield work, GOLIATH teaches squad leadership |

### Hook Câu Chuyện

- Searching for a way to formally clear his discharged soldiers' records
- Maintains contact with former VDV unit members scattered as mercenaries
- Receives coded messages from someone inside Russian military intelligence
- Personal quest chain involves protecting a safehouse full of displaced civilians in the Zone

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Giáp Overcharge is team-dependent — solo activation is wasteful
- +25 temporary armor for allies is strong but requires 5m proximity — positioning is the skill expression
- Brotherhood passive must NOT stack with multiple GOLIATH operators — cap at one instance
- Reactive Giáp upgrade (20% negate chance) should not apply to headshots
- Last Stand upgrade is emotionally powerful but mechanically niche — buff remaining duration gives team 4-6 seconds post-down
- GOLIATH + SUTURE combo is intentionally the strongest duo in the game — counter with GLITCH EMP

### Yêu Cầu Animation

- Overcharge activation (0.6 seconds — fist clench, armor plates glow orange)
- Overcharge VFX (expanding orange pulse from GOLIATH, team armor plates glow)
- Brotherhood proximity indicator (subtle UI pulse when allies are in range)
- Revive animation (faster/more stable than standard due to damage resistance)
- Death animation: falls slowly, reaches toward nearest ally (dramatic, team-focused)

### Yêu Cầu Audio

| Sound | Ghi Chú |
| :---- | :---- |
| Overcharge activate | Deep power-up hum + armor plate rattle |
| Overcharge active | Thấp ambient energy pulse (team hears it as reassuring) |
| Overcharge end | Power-down descending tone |
| Brotherhood proximity | Subtle heartbeat sync (both players hear it) |
| Footsteps | Heavy, authoritative — military boots, armor clink |
| LMG fire | Deep, sustained — signature sound in combat |

### Ghi Chú Riêng Cho Top-Down

- Overcharge 8m radius circle must be visible to teammates at minimum zoom — shows buff zone
- Blue armor glow should be clearly distinct from AEGIS shield's blue-white — use deeper steel blue
- Brotherhood passive proximity (5m) should show a subtle connecting line between GOLIATH and nearby ally
- LMG barrel extending forward from the model makes GOLIATH identifiable by weapon type from above
- Overcharge armor stripping bởi EMP should have dramatic VFX — communicate vulnerability to both teams
