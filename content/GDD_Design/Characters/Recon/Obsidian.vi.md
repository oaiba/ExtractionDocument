---
title: "OBSIDIAN - Unit N-7 \"Nero\""
type: docs
---

## Hồ Sơ Operator

> *"Anh không thể đánh thứ mình không nhìn thấy."*

### Thông Tin Cơ Bản

| Thuộc Tính | Giá Trị |
| :-------- | :---- |
| **Tên Thật** | Unit N-7 "Nero" |
| **Codename** | OBSIDIAN |
| **Class** | Recon |
| **Quốc Tịch** | Unknown (Machine) |
| **Tuổi** | 26 |
| **Chiều Cao** | 162 cm (5'4") |
| **Cân Nặng** | 52 kg (115 lbs) |

<!-- REF_IMAGE: OBSIDIAN operator portrait — small, agile frame, face half-obscured by tactical mask, smoke grenades on belt, dark stealth suit with faint cyan circuitry -->

### Lý Lịch

Yuki Tanaka là thần đồng trong Japan Special Forces Group, chuyên về xâm nhập và thoát ly. Thân hình nhỏ và khả năng biến mất gần như siêu nhiên khiến cô hoàn hảo cho các chiến dịch bí mật, nơi bị phát hiện đồng nghĩa với cái chết.

Một nhiệm vụ thất bại ở Đài Loan khiến squad của cô thiệt mạng, còn Yuki bị cấp trên biến thành vật tế thần. Cô biến mất vào thế giới ngầm tội phạm trước khi xuất hiện trong Exclusion Zone, nơi tài biến mất của cô được trọng dụng thay vì bị trừng phạt.

### Tính Cách

- **Elusive** — Không bao giờ ở nơi bạn nghĩ cô ấy sẽ ở
- **Quiet** — Hành động có giá trị hơn lời nói
- **Survivor** — Thoát được quan trọng hơn chiến thắng
- **Loyal** — Một khi đã có niềm tin thì không phản bội

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
| First attack from smoke (Shadow Step) | +15% |
| Toxic Smoke tick (upgrade) | 3 HP/sec |
| Headshot Multiplier | 2.0x |

### Thông Số Combat Mở Rộng

| Tham Số | Giá Trị | Ghi Chú |
| :-------- | :---- | :---- |
| **Quỹ Stamina** | 110 | +10% (Recon class) |
| **Hao Stamina Khi Sprint** | 9/second | -10% (Recon class) |
| **Tốc Độ Hồi** | 9.6/second | +20% (Recon class) |
| **Thời Lượng Sprint Thực** | 12.2 seconds | Best efficiency |
| **Âm Lượng Bước Chân** | 60% | -30% (class) + additional -10% (Shadow Step passive) |
| **Bán Kính Audio Ability** | 20 meters | Smoke canister hiss audible |

### Kháng Hiệu Ứng Trạng Thái

| Hiệu Ứng | Kháng | Ghi Chú |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Đủ thời lượng |
| Burn | 0% | Full DoT |
| EMP | 0% | No tech-based abilities to disable |

### Spec Hình Ảnh Top-Down

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Hitbox Capsule** | 32 cm radius, 160 cm height |
| **Vùng Đầu** | 12 cm radius |
| **Collision Profile** | Slim (-10% from mesh) — smallest operator |
| **Silhouette Nhìn Từ Trên Xuống** | Smallest operator, hooded head, no visible backpack |
| **Vùng Accent Theo Class** | Cyan (#06B6D4) on goggle glow, subtle strips on hood |
| **Smoke VFX (Top-Down)** | Dense gray cloud on ground (8m radius), character fades to near-invisibility inside |
| **Smoke Audio Radius** | 20m — canister hiss on deploy, atmospheric whoosh during duration |

<!-- REF_IMAGE: OBSIDIAN top-down view — showing operator with smoke cloud deployed, 8m radius gray cloud on ground, character partially faded inside -->

### Độ Khó

**Độ Khó: 5/5** — Hardest operator to master. Requires perfect smoke placement timing, in-smoke awareness, and exploiting Shadow Step first-attack bonus. Maximum game sense required.


## Ability

### Active Ability: Smoke Screen

> *"Deploy a large smoke cloud that blocks vision for all."*

| Thuộc Tính | Giá Trị |
| :------- | :---- |
| **Cooldown** | 70 seconds |
| **Duration** | 15 seconds |
| **Charges** | 1 |

#### Hiệu Ứng

| Hiệu Ứng | Giá Trị | Ghi Chú |
| :----- | :---- | :---- |
| Smoke Radius | 8 meters | Large area denial |
| Vision Block | 100% | Cannot see through |
| OBSIDIAN Bonus | Can see enemy outlines in own smoke | 10m range |
| Firing Reveals | Muzzle flash briefly visible | 1 second duration |

#### Rule Tương Tác Khói

| Interaction | Result |
| :---------- | :----- |
| **Smoke + SONAR UAV** | Smoke blocks scan LOS — enemies in smoke not revealed |
| **Smoke + Lửa (IGNITION)** | Lửa burns through smoke — smoke does not extinguish fire |
| **Smoke + Nano Swarm (PULSE)** | Smoke does not interact with swarm |
| **Smoke + AEGIS Khiên** | Smoke passes through shield dome |
| **Smoke + BASTION Khiên** | Smoke blocks vision through shield |
| **Smoke + MIRAGE Sensors** | Sensors still detect through smoke |

#### VFX Khói Top-Down

| State | VFX From Above |
| :---- | :------------- |
| Smoke deploy | Canister lands, gray cloud expands rapidly to 8m radius |
| Smoke active | Dense gray cloud on ground plane, opaque from above |
| OBSIDIAN inside (ally view) | Faint outline visible to teammates only |
| Địch inside (enemy view) | Completely hidden, no outline |
| Smoke clearing (last 3s) | Cloud thins, visibility gradually returns |


#### Cách Dùng Tactical

| Use Case | Strategy |
| :------- | :------- |
| **Escape** | Cover retreat when overwhelmed |
| **Entry** | Confuse enemy positions, push through |
| **Revive** | Block enemy sightlines during teammate pickup |
| **Extraction** | Cover helicopter arrival zone |
| **Loot** | Safely loot high-value containers in contested areas |

#### Slot Upgrade

**Slot 1 (Level 5):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Extended Fog** | Duration +8 seconds (23s total) |
| **Quick Fade** | Cooldown -15 seconds (55s total) |
| **Larger Cloud** | Radius +4 meters (12m total) |

**Slot 2 (Level 20):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Toxic Smoke** | Địch in smoke take 3 HP/sec |
| **Thermal Block** | Also blocks thermal/scan vision |
| **Mobile Cloud** | Smoke slowly follows OBSIDIAN |

**Slot 3 (Level 35):**

| Option | Hiệu Ứng |
| :----- | :----- |
| **Ghost Walk** | OBSIDIAN is invisible in own smoke |
| **Disorienting** | Địch exiting smoke are briefly confused (1.5s sway) |
| **Double Screen** | 2 smoke charges |

---

### Passive Ability: Shadow Step

> *"Move like the wind. Strike like the storm."*

| Điều Kiện | Hiệu Ứng |
| :-------- | :----- |
| In smoke (any) | +20% movement speed |
| Exit smoke | 3-second speed boost (+10%) |
| First attack from smoke | +15% damage |

**Design Intent:** OBSIDIAN is the only operator who thrives in zero-visibility conditions. Smoke is not just a tool — it is her natural habitat. The first-strike bonus incentivizes aggressive plays from concealment, not just passive running.

---

## Loadout

### Loadout Mặc Định

| Slot | Item | Ghi Chú |
| :--- | :--- | :---- |
| **Primary** | MP7 (Suppressed) | Small, quiet |
| **Secondary** | Karambit Knife | Silent kills |
| **Tactical** | Smoke Grenades x2 | Additional smoke coverage |
| **Giáp** | Light Vest | 30 armor points |

### Loadout Khuyến Nghị

**Ghost Assassin (Stealth):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | Vector SMG (Suppressed) | Fastest close-range TTK with suppressor |
| Secondary | Karambit Knife | Silent melee for unaware enemies |
| Tactical | Smoke Grenades x3 | Maximum visual denial |

**Smoke Support (Team Play):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | MP5 (Suppressed) | Reliable mid-range |
| Secondary | Silenced Pistol | Backup |
| Tactical | Smoke x2, Flashbang x1 | Cover + entry |

---

## Hướng Dẫn Playstyle

### Vai Trò Trong Team

**Primary Role:** Visual Denial / Stealth Flanker
- Smoke key sightlines before team pushes
- Flank through smoke to attack from unexpected angles
- Cover revives and extractions with smoke

**Secondary Role:** Escape Artist
- Create escape routes for retreating team
- Disengage losing fights with smoke
- Extract with loot when extraction zone is contested

### Vòng Lặp Combat

```
1. Identify key engagement area sightlines
2. Deploy Smoke Screen on enemy overwatch position
3. Enter smoke (Shadow Step activates — +20% speed)
4. Use smoke vision to locate enemy outlines
5. First attack from smoke (+15% damage)
6. Eliminate or reposition before smoke clears
7. Exit smoke with speed boost
8. Fall back and wait for cooldown
```

### Vị Trí

**Good Positions:**
- Near chokepoints where smoke has maximum impact
- Close to team for smoke-supported revives
- Flanking routes that connect to smoke-covered areas

**Bad Positions:**
- Open ground with no cover (smoke is not enough alone)
- Alone without team to capitalize on smoke chaos
- Against enemies with thermal/scan capabilities (countered before upgrade)

---

## Kèo Đấu

### Kèo Có Lợi

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **BASTION** | Khiên is useless when he cannot see — smoke negates his entire kit | Smoke, flank behind shield, melee |
| **MAMBA** | Combat Stim is wasted if he cannot find a target in smoke | Deploy smoke when stim activates, wait it out |
| **GOLIATH** | Slow rotations make him vulnerable to smoke flanks | Smoke his position, attack from behind |

### Kèo Cân Bằng

| Opponent | Ghi Chú | Key to Winning |
| :------- | :---- | :------------- |
| **IGNITION** | Lửa vs. smoke — fire reveals you, smoke hides you | Avoid fire zones, use smoke to block fire sightlines |
| **AEGIS** | Guardian Khiên works in smoke | Wait for shield down, then push through smoke |
| **SUTURE** | Hồi máu extends fights — smoke delays but does not prevent healing | Rush SUTURE in smoke before drone can reposition |

### Kèo Bất Lợi

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **SONAR** | UAV Scan sees through smoke (unless Thermal Block upgrade) | Prioritize Thermal Block upgrade, or avoid SONAR scan zones |
| **PULSE** | Nano Swarm targets area, not vision — works in smoke | Exit smoke away from swarm, reposition to fresh cover |
| **MIRAGE** | Motion sensors trigger regardless of smoke — reveals your position | Destroy sensors before deploying smoke |

---

## Câu Thoại

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Shikai wo ubau." (Stealing their vision) |
| Kill (From Smoke) | "You never saw it coming." |
| Kill (Melee) | "Silent." |
| Thấp Máu | "Need cover. Deploying smoke." |
| Reviving | "Rise. We disappear together." |

### Callout

| Trigger | Line |
| :------ | :--- |
| Địch Spotted | "Contact. [Direction]." |
| Smoke Deploying | "Smoke out. Push or fall back." |
| Reloading | "Reloading." |
| Smoke Ending | "Clear in three..." |

### Tính Cách

| Trigger | Line |
| :------ | :--- |
| Match Start | "Stay close. Disappear with me." |
| Extraction Called | "Smoke the landing zone." |
| Extraction Success | "Like ghosts. Never there." |
| Squad Wipe | "They were already dead. They just had not realized." |

---

## Cosmetic

### Ngoại Hình Mặc Định

- **Outfit:** Matte black tactical suit, lightweight silhouette, smoke grenades on hip harness
- **Headgear:** Half-face tactical mask (lower face), short dark hair with single white streak
- **Gloves:** Thin black stealth gloves
- **Face:** Sharp features, focused eyes, faint scar along jawline

<!-- REF_IMAGE: OBSIDIAN default skin — top-down view showing smallest silhouette in roster, smoke grenades visible, dark outfit with minimal reflective surfaces -->

### Skin Có Thể Mở Khóa

| Skin | Rarity | Mở Khóa |
| :--- | :----- | :----- |
| **Mist Walker** | Common | Level 10 |
| **Sakura Shadow** | Uncommon | 1,000 Credits |
| **Neon Sonar** | Rare | Level 25 |
| **Kunoichi** | Epic | Battle Pass S1 |
| **Yuurei** | Legendary | Season 1 Event |

### Vật Phẩm Signature

| Item | Mô Tả |
| :--- | :---------- |
| **White Streak** | Single white stripe in hair (unique identifier) |
| **Karambit Sheath** | Custom carbon-fiber knife holster on thigh |
| **Origami Crane** | Paper crane tucked into vest strap (memorial for lost squad) |

---

## Liên Kết Lore

### Mối Quan Hệ

| Character | Relationship |
| :-------- | :----------- |
| **SONAR** | Respects her intel capabilities but dislikes being tracked — friendly rivalry |
| **IGNITION** | Lửa burns smoke — natural enemy on the battlefield, no personal grudge |
| **GLITCH** | Mutual understanding of being outcasts from their own governments |
| **MIRAGE** | He hunted her once during a covert operation — she escaped, earning his respect |

### Hook Câu Chuyện

- Seeking evidence to clear her name for the failed Taiwan operation
- Has contacts in Japanese criminal underground who provide black market items
- Memorial ritual — places origami cranes at teammate death locations (environmental detail)
- Intercepted a Corporation dossier with her real identity — someone knows who she is

---

## Ghi Chú Thiết Kế (Cho Developer)

### Cân Nhắc Balance

- Smoke Screen is unique as the only full vision-block ability in the game
- OBSIDIAN's in-smoke vision is her most powerful mechanic — 10m outline range keeps it fair
- First-strike +15% damage from Shadow Step should only apply to the very first attack, not sustained fire from smoke
- Ghost Walk upgrade makes her invisible but NOT invulnerable — damage still hits, audio still present
- Thermal Block upgrade (Slot 2) is the primary counter to SONAR — this is an intentional rock-paper-scissors dynamic
- Mobile Cloud should move at 50% of OBSIDIAN's movement speed — too fast makes it oppressive

### Yêu Cầu Animation

- Smoke grenade throw animation (0.6 seconds — quick wrist flick)
- Smoke deployment VFX (rapid expansion from canister, volumetric cloud)
- In-smoke enemy outline shader (orange silhouettes, 10m range)
- Shadow Step speed boost (subtle body lean forward on exit)
- Death animation: crumples silently (no dramatic fall — she goes quiet)

### Yêu Cầu Audio

| Sound | Ghi Chú |
| :---- | :---- |
| Smoke deploy | Sharp hiss of canister + rapid gas expansion |
| Smoke active | Gentle ambient whoosh (quiet, atmospheric) |
| Smoke clearing | Gradual fade-out hiss |
| Shadow Step activate | Soft footstep acceleration (barely audible) |
| Footsteps | Lightest in roster — bare minimum contact sounds |
| Melee kill | Swift blade draw + single cut impact |

### Ghi Chú Riêng Cho Top-Down

- Smoke cloud must be opaque from above — top-down camera sees dense gray vòng tròn trên mặt đất
- OBSIDIAN inside own smoke is nearly invisible from top-down (faint shimmer for teammates only)
- Smoke must NOT block friendly minimap detection — allies can still see teammate dots through smoke
- Smoke edge should be well-defined from above (clear boundary between vision/no vision)
- First attack from smoke (+15% damage) applies only to the first bullet/hit, not sustained fire
