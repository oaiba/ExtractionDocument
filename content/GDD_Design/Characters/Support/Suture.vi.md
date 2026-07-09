---
title: "SUTURE - Tariq Al-Sayed"
type: docs
---

## Operator Profile

> *"I swore an oath to do no harm. I never said anything about my địch."*

### Basic Information

| Attribute       | giá trị                     |
| :-------------- | :------------------------ |
| **Real Name**   | Tariq Al-Sayed            |
| **Codename**    | SUTURE                    |
| **Class**       | Support                   |
| **Nationality** | Egyptian                  |
| **Age**         | 42                        |
| **Height**      | 178 cm (5'10")            |
| **Weight**      | 76 kg (168 lbs)           |

<!-- REF_IMAGE: SUTURE operator portrait — field medic gear, white cross on vest, kindly nhưng tired expression, medical drone hovering nearby -->

### Background

Tariq Al-Sayed was a trauma surgeon serving in conflict zones across the Middle East và Africa. His ability to perform miracles under fire và his clinical, precise approach earned him the respect of soldiers who'd seen him pull men back from the brink of death.

sau a hostile extraction went wrong, Tariq watched helplessly as soldiers died waiting for evacuation that never came. Disillusioned với military bureaucracy, he retired from dịch vụ nhưng couldn't escape the call of medicine in war zones. Now he operates in the Exclusion Zone, treating combat as a messy equation to be solved.

### Personality Traits

- **Calm Under Pressure** - Never panics, even in chaos
- **Protective** - Takes every death personally
- **Pragmatic** - Will make hard choices
- **Sardonic** - Dark humor coping mechanism

---

## Combat Statistics

### Base Stats

| Stat                      | giá trị   | Class Modifier | Final     |
| :------------------------ | :------ | :------------- | :-------- |
| **máu**                | 100 HP  | -              | 100 HP    |
| **giáp**                 | 40      | -              | 40        |
| **Sprint Speed**          | 5.5 m/s | -5%            | 5.225 m/s |
| **Walk Speed**            | 3.5 m/s | -5%            | 3.325 m/s |
| **Healing Effectiveness** | 100%    | +20%           | 120%      |

### Healing Modifiers

| Item          | Base Heal | SUTURE Bonus | Final    |
| :------------ | :-------- | :-------- | :------- |
| Small Medkit  | 30 HP     | +20%      | 36 HP    |
| Medkit        | 50 HP     | +20%      | 60 HP    |
| Surgery Kit   | 100 HP    | +20%      | 120 HP   |
| Healing Drone | 5 HP/sec  | +20%      | 6 HP/sec |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 100 | Standard (Support class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8/second | Standard |
| **Net Sprint Duration** | 10.0 seconds | Average |
| **Footstep Volume** | 90% | Slightly quieter — designed not to alert patients |
| **Ability Audio Radius** | 15 meters | Drone hum is subtle, only close-range detection |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 10% | Slight resist (Support class) — reach downed allies |
| Burn | 0% | Full DoT |
| EMP | 0% | Healing Drone destroyed by EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 38 cm radius, 176 cm height |
| **Head Sphere** | 14 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Medium build, large medical backpack, cross markings on shoulders |
| **Class Accent Zones** | White/Green (#22C55E) on armband cross và backpack |
| **Drone VFX (Top-Down)** | Green pulsing circle on ground (10m radius), drone model hovering at center |
| **Drone Audio Radius** | 15m — subtle hum, quietest deployable in the game |

<!-- REF_IMAGE: SUTURE top-down view — showing operator silhouette với medical gear, healing drone deployed với green radius circle hiển thị rõ from above -->

### Healing Drone Stat Block

| Property | giá trị | ghi chú |
| :------- | :---- | :---- |
| **Drone HP** | 50 | Destroyable — chính counterplay |
| **Heal Rate** | 6 HP/sec | với SUTURE class bonus |
| **Heal Radius** | 10 meters | Ground-plane circle |
| **Duration** | 20 seconds | Total lifetime |
| **Max Heal Total** | 120 HP/ally | Over full duration |
| **Deploy Range** | Throw (15m max) | Drone lands where thrown |
| **Can Heal thông qua Walls** | No | Line of sight to drone required |
| **Can Heal thông qua Floors** | Yes | nếu on adjacent floor |

### Difficulty Rating

**Difficulty: 1/5** — Most beginner-friendly operator. Deploy drone, stay alive, heal team. No complex cơ chế hoặc timing required.


## Abilities

### Active Ability: Healing Drone

> *"Deploy an autonomous medical drone that heals allies in radius."*

| Property     | giá trị       |
| :----------- | :---------- |
| **Cooldown** | 120 seconds |
| **Duration** | 20 seconds  |
| **Charges**  | 1           |
| **Drone HP** | 50          |

#### Effects

| Effect              | giá trị                | ghi chú                            |
| :------------------ | :------------------- | :------------------------------- |
| Heal Rate           | 5 HP/second          | +20% = 6 HP/sec với class bonus |
| Heal Radius         | 10 meters            | Centered on drone                |
| Max Heal per Deploy | 100 HP per ally      | 5 HP × 20 seconds                |
| Targets             | All allies in radius | Including SUTURE                    |

#### Drone Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **Drone + EMP (GLITCH)** | Drone destroyed instantly |
| **Drone + Fire (IGNITION)** | Not affected — drone hovers above fire |
| **Drone + Nano Swarm (PULSE)** | Not affected — swarm targets ground units |
| **Drone + UAV Scan (SONAR)** | Drone position revealed to scanning team |
| **Drone + BASTION Shield** | Drone heals thông qua shield |
| **Drone + Smoke (OBSIDIAN)** | Drone heals thông qua smoke |

#### Top-Down Drone VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| Drone deploy | Green flash at throw point, drone rises to hover height |
| Drone active | Green pulsing circle on ground (10m), drone model hiển thị rõ at center |
| Healing pulse | Green particle streams from drone to allies in radius |
| Drone low HP | Sparking particles, circle flickers |
| Drone destroyed | Electrical burst, debris falls, circle disappears |


**Self:**
- Drone deployment animation
- Green healing particles on allies
- Heart rate monitor beep (audio)

**địch Perspective:**
- Drone is hiển thị rõ và targetable
- Green healing glow obvious
- Distinct humming sound

#### Tactical Uses

| cách dùng Case         | Strategy                                |
| :--------------- | :-------------------------------------- |
| **Defense Hold** | Place trước địch arrive             |
| **Post-Fight**   | Deploy sau combat to restore team     |
| **Extraction**   | Heal while waiting for helicopter       |
| **Bait**         | địch may focus drone, giving opening |

#### upgrade Slots

**Slot 1 (Level 5):**
| Option               | Effect                           |
| :------------------- | :------------------------------- |
| **Extended Care**    | Duration +10 seconds (30s total) |
| **Rapid Response**   | Cooldown -30 seconds (90s total) |
| **Enhanced Formula** | Heal rate +2 HP/sec (7 base)     |

**Slot 2 (Level 20):**
| Option             | Effect                       |
| :----------------- | :--------------------------- |
| **Armored Drone**  | Drone HP +30 (80 total)      |
| **Mobile Unit**    | Drone follows SUTURE slowly     |
| **Expanded Range** | Radius +5 meters (15m total) |

**Slot 3 (Level 35):**
| Option              | Effect                                  |
| :------------------ | :-------------------------------------- |
| **Revive Protocol** | Drone can revive downed allies (10 sec) |
| **Combat Stim**     | Allies in range get +5% damage          |
| **Stealth Mode**    | Drone is harder to see/hear             |

---

### Passive Ability: Field Medic

> *"Faster revives và emergency self-treatment."*

| Condition          | Effect                             |
| :----------------- | :--------------------------------- |
| Reviving Allies    | +15% faster                        |
| Self Heal          | Can cách dùng healing items 20% faster   |
| Downed Ally Nearby | See máu bar thông qua walls (10m) |

**Design Intent:** SUTURE should always know who needs giúp và get to them fast.

---

## Loadout

### Default Loadout

| Slot          | Item                     | ghi chú              |
| :------------ | :----------------------- | :----------------- |
| **primary**   | MP5 SMG                  | Reliable mid-range |
| **secondary** | G17 Pistol               | Standard sidearm   |
| **Tactical**  | Medkit ×3, Healing Drone | Maximum healing    |
| **giáp**     | Light Vest               | 30 giáp points    |

### Recommended Loadouts

**Combat Medic:**
| Slot      | Item                | Why               |
| :-------- | :------------------ | :---------------- |
| primary   | MP7                 | Better in CQB     |
| secondary | G17                 | Reliable          |
| Tactical  | Medkit ×2, Smoke ×1 | Smoke for revives |

**Pure Support:**
| Slot      | Item                       | Why                      |
| :-------- | :------------------------- | :----------------------- |
| primary   | P90                        | High mag for suppression |
| secondary | G17                        | -                        |
| Tactical  | Medkit ×3, Surgical Kit ×1 | Maximum heal potential   |

---

## Playstyle Guide

### Role in Team

**primary Role:** Team Healer
- Maintain team máu
- Enable extended engagements
- Revive downed teammates

**secondary Role:** Anchor
- Hold positions với healing
- Recover team sau fights
- Survive to giúp others

### Healing Priority matrix

| Priority | Target            | khi                   |
| :------- | :---------------- | :--------------------- |
| 1        | Assault in combat | They're your damage    |
| 2        | Tank taking fire  | They're your shield    |
| 3        | Yourself          | Dead medic = dead team |
| 4        | Recon/Specialist  | Usually not in danger  |

### Drone Placement

**Good Placement:**
- Behind cover
- Near choke points
- Extraction zones
- Not in direct fire

**Bad Placement:**
- Open areas
- Far from team
- Where địch can easily destroy

---

## Matchups

### Favorable Matchups

| Opponent     | Why Favorable                   | Tactic                 |
| :----------- | :------------------------------ | :--------------------- |
| **MIRAGE**  | Traps can't kill nếu you heal    | Out-sustain the damage |
| **PULSE**     | Nano swarm is slow damage       | Heal thông qua it        |
| **GOLIATH** | Low offense, you sustain better | Attrition warfare      |

### Even Matchups

| Opponent    | ghi chú                       | chính to Winning          |
| :---------- | :-------------------------- | :---------------------- |
| **AEGIS**   | Both Support, comes to team | Your team's DPS matters |
| **SONAR** | Intel vs healing            | Stay hidden, heal safe  |
| **OBSIDIAN**  | Smoke disrupts drone        | Place drone carefully   |

### Unfavorable Matchups

| Opponent    | Why Difficult               | Counter Strategy         |
| :---------- | :-------------------------- | :----------------------- |
| **MAMBA**   | Burst exceeds healing       | Focus fire him first     |
| **TARTARUS**   | Kills trước heal matters   | Stay far from engagement |
| **BASTION** | Protected DPS behind shield | Wait for push to end     |

---

## Voice Lines

### Combat

| Trigger            | Line                                |
| :----------------- | :---------------------------------- |
| Ability Activation | "Drone deployed! Stay in the zone!" |
| Healing Ally       | "Hold still, I've got you."         |
| Kill               | "Apologies. No hard feelings."      |
| Reviving           | "You're not dying on my watch!"     |
| Low máu         | "I'm hit! Need cover!"              |
| Ally Downed        | "Man down! Moving to assist!"       |

### Callouts

| Trigger         | Line                             |
| :-------------- | :------------------------------- |
| địch Spotted   | "Contact spotted."               |
| Drone Destroyed | "Drone's down! Cooldown needed." |
| Low on Meds     | "Running low on supplies."       |
| Reloading       | "Changing mag."                  |

### Personality

| Trigger            | Line                                         |
| :----------------- | :------------------------------------------- |
| Match Start        | "Right then. Let's keep everyone breathing." |
| Extraction Called  | "Evac inbound. No heroics, just survive."    |
| Extraction success | "Job's done. Drinks are on me."              |
| Squad Wipe         | "Remarkable. We actually stayed alive."      |

---

## Cosmetics

### Default Appearance

- **Outfit:** White tactical vest với red cross, khaki pants
- **Headgear:** Medical cap với tactical goggles
- **Gloves:** Blue surgical gloves
- **Face:** Graying beard, kind nhưng tired eyes

### Unlockable Skins

| Skin                  | Rarity    | Unlock          |
| :-------------------- | :-------- | :-------------- |
| **Field Surgeon**     | Common    | Level 10        |
| **Desert Medic**      | Uncommon  | 1,000 Credits   |
| **Trauma Team**       | Rare      | Level 25        |
| **Battlefield Aegis** | Epic      | Battle Pass S1  |
| **Plague Suturetor**     | Legendary | Halloween Event |

### Signature Items

| Item             | Description           |
| :--------------- | :-------------------- |
| **Medical Bag**  | Always hiển thị rõ on hip |
| **Stethoscope**  | Hanging around neck   |
| **Wedding Ring** | Never removed         |

---

## Lore Connections

### Relationships

| nhân vật   | Relationship                          |
| :---------- | :------------------------------------ |
| **MAMBA**   | Served together, saved his life twice |
| **IGNITION**   | Treated her burns, protective of her  |
| **AEGIS**   | Respects her dedication               |
| **BASTION** | Old friends, philosophical opposites  |

### Story Hooks

- Wife và daughter back home, his reason to extract
- Looking for a missing medical convoy
- Has a terminal diagnosis, operates on borrowed thời gian

---

## Design ghi chú (For Developers)

### Balance Considerations

- Drone is destroyable = counterplay
- Long cooldown prevents spam healing
- Low combat stats = relies on team
- Passive giúp team coordination

### Animation yêu cầu

- Drone throw/deploy animation
- Green healing particle effects
- Revive animation (faster than standard)
- Death: Falls protecting medical bag

### Audio yêu cầu

| Sound           | ghi chú                           |
| :-------------- | :------------------------------ |
| Drone deploy    | cơ chế launch + hover start |
| Drone active    | Soft humming loop               |
| Healing pulse   | Gentle heartbeat rhythm         |
| Drone destroyed | Electrical fizzle + crash       |

### Top-Down cụ thể ghi chú

- Healing drone green circle phải được hiển thị rõ at minimum zoom — chính gameplay information for both teams
- Drone model nên được slightly larger than realistic to ensure visibility from above
- Green healing particles from drone to allies phải được hiển thị rõ nhưng not obscure combat (thin streams)
- Drone destruction VFX nên được dramatic enough to communicate to the team that healing is gone
- Drone position revealed by SONAR UAV — this is a deliberate counterplay vector
