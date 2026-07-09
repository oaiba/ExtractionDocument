---
title: "MAMBA - Thuy Nguyen"
type: docs
---

## Operator Profile

> *"First in, last standing."*

### Basic Information

| Attribute       | giá trị                       |
| :-------------- | :-------------------------- |
| **Real Name**   | Thuy Nguyen                 |
| **Codename**    | MAMBA                       |
| **Class**       | Assault                     |
| **Nationality** | Vietnamese                  |
| **Age**         | 26                          |
| **Height**      | 168 cm (5'6")               |
| **Weight**      | 60 kg (132 lbs)             |

<!-- REF_IMAGE: MAMBA operator portrait — athletic build, tactical cap, green eyes, holding combat knife, aggressive stance -->

### Background

Thuy Nguyen served in the Dac Cong (Vietnamese Special Forces) trước transitioning to underground mercenary work. Known for her calculated aggression và lethal, fast-striking tactics, she earned the callsign "Mamba" for striking mà không cảnh báo và leaving no survivors.

sau a classified operation went sideways, she was left for dead by her handlers. Surviving against all odds, she now operates as a freelance contractor in the Exclusion Zone, using her skills to extract valuable assets và occasionally settle old scores.

### Personality Traits

- **Confident** - Never doubts his abilities
- **Direct** - Says what he means, no BS
- **Protective** - Watches out for teammates
- **Vengeful** - Never forgets betrayal

---

## Combat Statistics

### Base Stats

| Stat             | giá trị   | Class Modifier | Final    |
| :--------------- | :------ | :------------- | :------- |
| **máu**       | 100 HP  | -              | 100 HP   |
| **giáp**        | 50      | -10%           | 45       |
| **Sprint Speed** | 5.5 m/s | +10%           | 6.05 m/s |
| **Walk Speed**   | 3.5 m/s | -              | 3.5 m/s  |
| **Crouch Speed** | 2.0 m/s | -              | 2.0 m/s  |

### Damage Modifiers

| Condition           | Modifier    |
| :------------------ | :---------- |
| Base vũ khí Damage  | +5% (Class) |
| Combat Stim Active  | +25%        |
| Combat Stim + Class | +30% total  |
| Headshot Multiplier | 2.0x        |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 120 | +20% (Assault class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8.8/second | +10% (Assault class) |
| **Net Sprint Duration** | 12.0 seconds | Longest sprint tier |
| **Footstep Volume** | 100% | Standard — no stealth bonus |
| **Ability Audio Radius** | 25 meters | Stim inject hiss audible to nearby địch |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 0% | Full duration — devastating trong khi stim |
| Burn | 0% | Full DoT |
| EMP | 0% | Stim cancelled immediately by EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 40 cm radius, 180 cm height |
| **Head Sphere** | 14 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Medium athletic build, cross-chest đạn belt hiển thị rõ, medium helmet |
| **Class Accent Zones** | Orange (#F97316) on shoulder patches và đạn belt |
| **Stim Active VFX (Top-Down)** | Orange body glow, subtle particle trail khi moving |
| **Stim Audio Radius** | 25m — địch within range hear injection hiss |

<!-- REF_IMAGE: MAMBA top-down view — showing operator silhouette from 60-degree camera với orange accent zones highlighted, stim active vs inactive comparison -->

### Difficulty Rating

**Difficulty: 2/5** — Straightforward kit. Press stim, shoot better. Low cơ chế complexity, rewards good aim timing.


## Abilities

### Active Ability: Combat Stim

> *"Inject experimental combat stimulant for temporary enhanced performance."*

| Property     | giá trị      |
| :----------- | :--------- |
| **Cooldown** | 90 seconds |
| **Duration** | 10 seconds |
| **Charges**  | 1          |

#### Effects

| Effect         | giá trị | ghi chú                    |
| :------------- | :---- | :----------------------- |
| Damage Boost   | +25%  | Stacks với class bonus  |
| Movement Speed | +10%  | All movement types       |
| Reload Speed   | +15%  | Faster reload animations |

#### Ability Interactions

| Interaction | kết quả |
| :---------- | :----- |
| **Stim + EMP** | Stim cancelled immediately, remaining duration lost |
| **Stim + Burn** | Stim does NOT cleanse burn — damage stacks |
| **Stim + Slow** | Stim movement boost partially counters slow (net +0% to -5% depending on slow source) |
| **Stim + Mark** | Stim does not remove mark status |

#### Top-Down VFX Description

| trạng thái | VFX From Above |
| :---- | :------------- |
| Stim inject | Brief orange flash on operator model (0.5s) |
| Stim active | Persistent orange glow on body, subtle particle trail on ground behind movement |
| Stim ending (last 2s) | Glow flickers, particles diminish |
| Stim expired | Glow fades, brief gray exhale particle |


#### Visual & Audio Cues

**Self:**
- màn hình edge orange vignette
- Heartbeat audio intensifies
- Hands shake slightly (cosmetic)

**địch Perspective:**
- Operator glows orange
- Distinct injection sound (audio cue)
- Faster movement hiển thị rõ

#### upgrade Slots

**Slot 1 (Level 5):**
| Option              | Effect                           |
| :------------------ | :------------------------------- |
| **Extended Rush**   | Duration +5 seconds (15s total)  |
| **Quick Reload**    | Cooldown -20 seconds (70s total) |
| **Adrenaline Heal** | Heal 10 HP on activation         |

**Slot 2 (Level 20):**
| Option              | Effect                              |
| :------------------ | :---------------------------------- |
| **Overdrive**       | Damage boost +30% (instead of +25%) |
| **Iron Skin**       | +20% damage resistance trong khi stim  |
| **Lightning Hands** | +50% reload speed (instead of +15%) |

**Slot 3 (Level 35):**
| Option          | Effect                                                   |
| :-------------- | :------------------------------------------------------- |
| **Rally Cry**   | Nearby allies get +10% damage                            |
| **Second Wind** | nếu killed trong khi stim, survive với 1 HP (once per life) |
| **Unstoppable** | Immune to stun/slow trong khi stim                          |

---

### Passive Ability: Adrenaline Surge

> *"Near-death experiences fuel his combat performance."*

| Condition        | Effect                           |
| :--------------- | :------------------------------- |
| máu below 30% | +15% reload speed                |
| máu below 20% | +20% reload speed, +5% movement  |
| máu below 10% | +25% reload speed, +10% movement |

**Design Intent:** Rewards aggressive play và tạo clutch moments.

---

## Loadout

### Default Loadout

| Slot          | Item               | ghi chú                       |
| :------------ | :----------------- | :-------------------------- |
| **primary**   | M4A1 Assault Rifle | Mid-tier AR, balanced stats |
| **secondary** | G17 Pistol         | Standard sidearm            |
| **Tactical**  | Frag Grenade ×2    | Area damage                 |
| **giáp**     | Medium Vest        | 50 giáp points             |

### Recommended Loadouts

**Aggressive Entry:**
| Slot      | Item         | Why                  |
| :-------- | :----------- | :------------------- |
| primary   | AK-47        | High damage per shot |
| secondary | Deagle       | Backup punch         |
| Tactical  | Flashbang ×2 | Entry assistance     |

**Sustained Combat:**
| Slot      | Item              | Why                       |
| :-------- | :---------------- | :------------------------ |
| primary   | M4A1              | Controllable, fast reload |
| secondary | SMG (MP7)         | CQB backup                |
| Tactical  | Smoke ×1, Frag ×1 | Versatility               |

---

## Playstyle Guide

### Role in Team

**primary Role:** Entry Fragger
- Be first into contested areas
- Trade kills aggressively
- tạo space for team

**secondary Role:** Cleanup
- Finish wounded địch
- Chase down runners
- Secure kills

### Combat Loop

```
1. Wait for intel (Recon scan)
2. Pre-aim angles
3. Activate Combat Stim
4. Entry push (10 second window)
5. Eliminate or call out enemies
6. Retreat if stim expires without kills
7. Wait for cooldown, repeat
```

### Positioning

**Good Positions:**
- Near entry points
- với rõ sightlines
- Close to Support for healing

**Bad Positions:**
- Isolated mà không backup
- Long rotations from team
- Exposed flanks

---

## Matchups

### Favorable Matchups

| Opponent    | Why Favorable                | Tactic                        |
| :---------- | :--------------------------- | :---------------------------- |
| **SUTURE**     | Cannot outheal your damage   | Rush trước drone deploys     |
| **SONAR** | Fragile, no combat advantage | Win aim duel                  |
| **PULSE**    | Low combat power             | Aggressive push thông qua swarm |

### Even Matchups

| Opponent    | ghi chú                      | chính to Winning                    |
| :---------- | :------------------------- | :-------------------------------- |
| **IGNITION**   | Similar role, fire vs stim | Avoid fire zones, cách dùng range       |
| **MIRAGE** | Traps are annoying         | Check corners, don't rush blindly |
| **AEGIS**   | Shield is strong           | Wait for shield to drop           |

### Unfavorable Matchups

| Opponent    | Why Difficult            | Counter Strategy              |
| :---------- | :----------------------- | :---------------------------- |
| **BASTION** | Shield blocks all damage | Flank hoặc wait for shield down |
| **GLITCH**  | EMP cancels your stim    | Bait EMP, then engage         |
| **TARTARUS**   | Out-damages you in CQB   | Keep range, cách dùng cover         |

---

## Voice Lines

### Combat

| Trigger            | Line                                             |
| :----------------- | :----------------------------------------------- |
| Ability Activation | "Stim active! Let's go!"                         |
| Kill               | "Hostile down!"                                  |
| Kill (Headshot)    | "Clean shot."                                    |
| Downed địch       | "They're already dead, they just don't know it." |
| Low máu         | "Taking hits, need backup!"                      |
| Reviving           | "Stay với me, soldier!"                         |

### Callouts

| Trigger          | Line                           |
| :--------------- | :----------------------------- |
| địch Spotted    | "Contact! Eyes on hostile!"    |
| Multiple địch | "Multiple contacts, heads up!" |
| Reloading        | "Mag out!"                     |
| Grenade          | "Frag out!"                    |

### Personality

| Trigger            | Line                                             |
| :----------------- | :----------------------------------------------- |
| Match Start        | "Let's get this done. Stay sharp."               |
| Extraction Called  | "Bird's coming. Hold the line."                  |
| Extraction success | "Mission complete. Another day, another dollar." |
| Squad Wipe         | "This is what we trained for."                   |

---

## Cosmetics

### Default Appearance

- **Outfit:** OD Green tactical vest, black pants
- **Headgear:** Black baseball cap
- **Gloves:** Black fingerless tactical gloves
- **Face:** Clean-shaven, slight scar on left cheek

### Unlockable Skins

| Skin             | Rarity    | Unlock         |
| :--------------- | :-------- | :------------- |
| **Desert Storm** | Common    | Level 10       |
| **Urban Gray**   | Uncommon  | 1,000 Credits  |
| **Blood Orange** | Rare      | Level 25       |
| **Black Ops**    | Epic      | Battle Pass S1 |
| **Phoenix**      | Legendary | Season 1 Event |

### Signature Items

| Item           | Description                   |
| :------------- | :---------------------------- |
| **Dog Tags**   | Dangling from vest (cosmetic) |
| **Ranger Tab** | Shoulder patch                |
| **Bite Marks** | Scar pattern on left arm      |

---

## Lore Connections

### Relationships

| nhân vật   | Relationship                    |
| :---------- | :------------------------------ |
| **SUTURE**     | Served together, mutual respect |
| **BASTION** | Rival, different philosophies   |
| **GLITCH**  | Distrusts - "Too many secrets"  |
| **SONAR** | Professional admiration         |

### Story Hooks

- Looking for the handler who betrayed him
- Has intel on Corporation black sites
- Owes a favor to unknown benefactor

---

## Design ghi chú (For Developers)

### Balance Considerations

- Combat Stim is strong nhưng predictable (audio cue)
- Low giáp punishes poor timing
- Cooldown prevents ability spam
- Passive encourages aggressive play

### Animation yêu cầu

- Stim injection animation (1 second)
- Orange glow VFX trong khi stim
- Heartbeat audio loop
- Death animation: Falls forward (aggressive stance)

### Audio yêu cầu

| Sound       | ghi chú                        |
| :---------- | :--------------------------- |
| Stim inject | Sharp hiss + heartbeat start |
| Stim active | Persistent heartbeat loop    |
| Stim end    | Heartbeat slowdown + exhale  |
| Footsteps   | Heavy, military boots        |

### Top-Down cụ thể ghi chú

- Stim orange glow must remain hiển thị rõ at minimum zoom (furthest camera distance)
- Stim audio cue phải được directional — địch nên được able to locate MAMBA by sound
- Particle trail trong khi stim nên được subtle enough not to obscure ground loot nhưng hiển thị rõ enough for địch awareness
- khi viewed from top-down, stim injection animation should show arm movement clearly (not hidden by body)
