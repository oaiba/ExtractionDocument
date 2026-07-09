---
title: "OBSIDIAN - Unit N-7 \"Nero\""
type: docs
---

## Operator Profile

> *"You can't fight what you can't see."*

### Basic Information

| Attribute | giá trị |
| :-------- | :---- |
| **Real Name** | Unit N-7 "Nero" |
| **Codename** | OBSIDIAN |
| **Class** | Recon |
| **Nationality** | Unknown (Machine) |
| **Age** | 26 |
| **Height** | 162 cm (5'4") |
| **Weight** | 52 kg (115 lbs) |

<!-- REF_IMAGE: OBSIDIAN operator portrait — small, agile frame, face half-obscured by tactical mask, smoke grenades on belt, dark stealth suit với faint cyan circuitry -->

### Background

Yuki Tanaka was a prodigy in Japan's Special Forces Group, specializing in infiltration và evasion. Her small stature và uncanny ability to vanish made her perfect for covert operations where detection meant death.

A failed mission in Taiwan left her squad dead và Yuki blamed by superiors looking for a scapegoat. She vanished into the criminal underworld trước emerging in the Exclusion Zone, where her talents for disappearing are appreciated rather than punished.

### Personality Traits

- **Elusive** — Never where you expect her
- **Quiet** — Actions speak, words waste energy
- **Survivor** — Escape trumps victory
- **Loyal** — Once trust is earned, never broken

---

## Combat Statistics

### Base Stats

| Stat | giá trị | Class Modifier | Final |
| :--- | :---- | :------------- | :---- |
| **máu** | 100 HP | -5% | 95 HP |
| **giáp** | 30 | - | 30 |
| **Sprint Speed** | 5.5 m/s | - | 5.5 m/s |
| **Crouch Speed** | 2.0 m/s | +15% | 2.3 m/s |
| **Footstep Volume** | 100% | -30% | 70% |

### Damage Modifiers

| Condition | Modifier |
| :-------- | :------- |
| Base vũ khí Damage | +0% (no class bonus) |
| First attack from smoke (Shadow Step) | +15% |
| Toxic Smoke tick (upgrade) | 3 HP/sec |
| Headshot Multiplier | 2.0x |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 110 | +10% (Recon class) |
| **Sprint Drain** | 9/second | -10% (Recon class) |
| **Recovery Rate** | 9.6/second | +20% (Recon class) |
| **Net Sprint Duration** | 12.2 seconds | Best efficiency |
| **Footstep Volume** | 60% | -30% (class) + additional -10% (Shadow Step passive) |
| **Ability Audio Radius** | 20 meters | Smoke canister hiss audible |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT |
| EMP | 0% | No tech-based abilities to disable |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 32 cm radius, 160 cm height |
| **Head Sphere** | 12 cm radius |
| **Collision Profile** | Slim (-10% from mesh) — smallest operator |
| **Silhouette From Above** | Smallest operator, hooded head, no hiển thị rõ backpack |
| **Class Accent Zones** | Cyan (#06B6D4) on goggle glow, subtle strips on hood |
| **Smoke VFX (Top-Down)** | Dense gray cloud on ground (8m radius), nhân vật fades to near-invisibility inside |
| **Smoke Audio Radius** | 20m — canister hiss on deploy, atmospheric whoosh trong khi duration |

<!-- REF_IMAGE: OBSIDIAN top-down view — showing operator với smoke cloud deployed, 8m radius gray cloud on ground, nhân vật partially faded inside -->

### Difficulty Rating

**Difficulty: 5/5** — Hardest operator to master. Requires perfect smoke placement timing, in-smoke awareness, và exploiting Shadow Step first-attack bonus. Maximum game sense required.


## Abilities

### Active Ability: Smoke màn hình

> *"Deploy a large smoke cloud that blocks vision for all."*

| Property | giá trị |
| :------- | :---- |
| **Cooldown** | 70 seconds |
| **Duration** | 15 seconds |
| **Charges** | 1 |

#### Effects

| Effect | giá trị | ghi chú |
| :----- | :---- | :---- |
| Smoke Radius | 8 meters | Large area denial |
| Vision Block | 100% | Cannot see thông qua |
| OBSIDIAN Bonus | Can Xem địch outlines in own smoke | 10m range |
| Firing Reveals | Muzzle flash briefly hiển thị rõ | 1 second duration |

#### Smoke Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **Smoke + SONAR UAV** | Smoke blocks scan LOS — địch in smoke not revealed |
| **Smoke + Fire (IGNITION)** | Fire burns thông qua smoke — smoke does not extinguish fire |
| **Smoke + Nano Swarm (PULSE)** | Smoke does not interact với swarm |
| **Smoke + AEGIS Shield** | Smoke passes thông qua shield dome |
| **Smoke + BASTION Shield** | Smoke blocks vision thông qua shield |
| **Smoke + MIRAGE Sensors** | Sensors still detect thông qua smoke |

#### Top-Down Smoke VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| Smoke deploy | Canister lands, gray cloud expands rapidly to 8m radius |
| Smoke active | Dense gray cloud on ground plane, opaque from above |
| OBSIDIAN inside (ally view) | Faint outline hiển thị rõ to teammates only |
| địch inside (địch view) | Completely hidden, no outline |
| Smoke clearing (last 3s) | Cloud thins, visibility gradually returns |


#### Tactical Uses

| cách dùng Case | Strategy |
| :------- | :------- |
| **Escape** | Cover retreat khi overwhelmed |
| **Entry** | Confuse địch positions, push thông qua |
| **Revive** | Block địch sightlines trong khi teammate pickup |
| **Extraction** | Cover helicopter arrival zone |
| **Loot** | Safely loot high-giá trị containers in contested areas |

#### upgrade Slots

**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extended Fog** | Duration +8 seconds (23s total) |
| **Quick Fade** | Cooldown -15 seconds (55s total) |
| **Larger Cloud** | Radius +4 meters (12m total) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **Toxic Smoke** | địch in smoke take 3 HP/sec |
| **Thermal Block** | Also blocks thermal/scan vision |
| **Mobile Cloud** | Smoke slowly follows OBSIDIAN |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Ghost Walk** | OBSIDIAN is invisible in own smoke |
| **Disorienting** | địch exiting smoke are briefly confused (1.5s sway) |
| **Double màn hình** | 2 smoke charges |

---

### Passive Ability: Shadow Step

> *"Move like the wind. Strike like the storm."*

| Condition | Effect |
| :-------- | :----- |
| In smoke (any) | +20% movement speed |
| Exit smoke | 3-second speed boost (+10%) |
| First attack from smoke | +15% damage |

**Design Intent:** OBSIDIAN is the only operator who thrives in zero-visibility conditions. Smoke is not just a tool — it is her natural habitat. The first-strike bonus incentivizes aggressive plays from concealment, not just passive running.

---

## Loadout

### Default Loadout

| Slot | Item | ghi chú |
| :--- | :--- | :---- |
| **primary** | MP7 (Suppressed) | Small, quiet |
| **secondary** | Karambit Knife | Silent kills |
| **Tactical** | Smoke Grenades x2 | Additional smoke coverage |
| **giáp** | Light Vest | 30 giáp points |

### Recommended Loadouts

**Ghost Assassin (Stealth):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | Vector SMG (Suppressed) | Fastest close-range TTK với suppressor |
| secondary | Karambit Knife | Silent melee for unaware địch |
| Tactical | Smoke Grenades x3 | Maximum visual denial |

**Smoke Support (Team Play):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | MP5 (Suppressed) | Reliable mid-range |
| secondary | Silenced Pistol | Backup |
| Tactical | Smoke x2, Flashbang x1 | Cover + entry |

---

## Playstyle Guide

### Role in Team

**primary Role:** Visual Denial / Stealth Flanker
- Smoke chính sightlines trước team pushes
- Flank thông qua smoke to attack from unexpected angles
- Cover revives và extractions với smoke

**secondary Role:** Escape Artist
- tạo escape routes for retreating team
- Disengage losing fights với smoke
- Extract với loot khi extraction zone is contested

### Combat Loop

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

### Positioning

**Good Positions:**
- Near chokepoints where smoke has maximum impact
- Close to team for smoke-supported revives
- Flanking routes that connect to smoke-covered areas

**Bad Positions:**
- Open ground với no cover (smoke is not enough alone)
- Alone mà không team to capitalize on smoke chaos
- Against địch với thermal/scan capabilities (countered trước upgrade)

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **BASTION** | Shield is useless khi he cannot Xem — smoke negates his entire kit | Smoke, flank behind shield, melee |
| **MAMBA** | Combat Stim is wasted nếu he cannot find a target in smoke | Deploy smoke khi stim activates, wait it out |
| **GOLIATH** | Slow rotations make him vulnerable to smoke flanks | Smoke his position, attack from behind |

### Even Matchups

| Opponent | ghi chú | chính to Winning |
| :------- | :---- | :------------- |
| **IGNITION** | Fire vs. smoke — fire reveals you, smoke hides you | Avoid fire zones, cách dùng smoke to block fire sightlines |
| **AEGIS** | Guardian Shield works in smoke | Wait for shield down, then push thông qua smoke |
| **SUTURE** | Healing extends fights — smoke delays nhưng does not prevent healing | Rush SUTURE in smoke trước drone can reposition |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **SONAR** | UAV Scan sees thông qua smoke (unless Thermal Block upgrade) | Prioritize Thermal Block upgrade, hoặc avoid SONAR scan zones |
| **PULSE** | Nano Swarm targets area, not vision — works in smoke | Exit smoke away from swarm, reposition to fresh cover |
| **MIRAGE** | Motion sensors trigger regardless of smoke — reveals your position | Destroy sensors trước deploying smoke |

---

## Voice Lines

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Shikai wo ubau." (Stealing their vision) |
| Kill (From Smoke) | "You never saw it coming." |
| Kill (Melee) | "Silent." |
| Low máu | "Need cover. Deploying smoke." |
| Reviving | "Rise. We disappear together." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| địch Spotted | "Contact. [Direction]." |
| Smoke Deploying | "Smoke out. Push hoặc fall back." |
| Reloading | "Reloading." |
| Smoke Ending | "rõ in three..." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "Stay close. Disappear với me." |
| Extraction Called | "Smoke the landing zone." |
| Extraction success | "Like ghosts. Never there." |
| Squad Wipe | "They were already dead. They just had not realized." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Matte black tactical suit, lightweight silhouette, smoke grenades on hip harness
- **Headgear:** Half-face tactical mask (lower face), short dark hair với single white streak
- **Gloves:** Thin black stealth gloves
- **Face:** Sharp tính năng, focused eyes, faint scar along jawline

<!-- REF_IMAGE: OBSIDIAN default skin — top-down view showing smallest silhouette in roster, smoke grenades hiển thị rõ, dark outfit với minimal reflective surfaces -->

### Unlockable Skins

| Skin | Rarity | Unlock |
| :--- | :----- | :----- |
| **Mist Walker** | Common | Level 10 |
| **Sakura Shadow** | Uncommon | 1,000 Credits |
| **Neon Sonar** | Rare | Level 25 |
| **Kunoichi** | Epic | Battle Pass S1 |
| **Yuurei** | Legendary | Season 1 Event |

### Signature Items

| Item | Description |
| :--- | :---------- |
| **White Streak** | Single white stripe in hair (unique identifier) |
| **Karambit Sheath** | Custom carbon-fiber knife holster on thigh |
| **Origami Crane** | Paper crane tucked into vest strap (memorial for lost squad) |

---

## Lore Connections

### Relationships

| nhân vật | Relationship |
| :-------- | :----------- |
| **SONAR** | Respects her intel capabilities nhưng dislikes being tracked — friendly rivalry |
| **IGNITION** | Fire burns smoke — natural địch on the battlefield, no personal grudge |
| **GLITCH** | Mutual understanding of being outcasts from their own governments |
| **MIRAGE** | He hunted her once trong khi a covert operation — she escaped, earning his respect |

### Story Hooks

- Seeking evidence to rõ her name for the failed Taiwan operation
- Has contacts in Japanese criminal underground who provide black market items
- Memorial ritual — places origami cranes at teammate death locations (environmental chi tiết)
- Intercepted a Corporation dossier với her real identity — someone knows who she is

---

## Design ghi chú (For Developers)

### Balance Considerations

- Smoke màn hình is unique as the only full vision-block ability in the game
- OBSIDIAN's in-smoke vision is her most powerful cơ chế — 10m outline range keeps it fair
- First-strike +15% damage from Shadow Step should only apply to the very first attack, not sustained fire from smoke
- Ghost Walk upgrade makes her invisible nhưng NOT invulnerable — damage still hits, audio still present
- Thermal Block upgrade (Slot 2) is the primary counter to SONAR — this is an intentional rock-paper-scissors dynamic
- Mobile Cloud should move at 50% of OBSIDIAN's movement speed — too fast makes it oppressive

### Animation yêu cầu

- Smoke grenade throw animation (0.6 seconds — quick wrist flick)
- Smoke deployment VFX (rapid expansion from canister, volumetric cloud)
- In-smoke địch outline shader (orange silhouettes, 10m range)
- Shadow Step speed boost (subtle body lean forward on exit)
- Death animation: crumples silently (no dramatic fall — she goes quiet)

### Audio yêu cầu

| Sound | ghi chú |
| :---- | :---- |
| Smoke deploy | Sharp hiss of canister + rapid gas expansion |
| Smoke active | Gentle ambient whoosh (quiet, atmospheric) |
| Smoke clearing | Gradual fade-out hiss |
| Shadow Step activate | Soft footstep acceleration (barely audible) |
| Footsteps | Lightest in roster — bare minimum contact sounds |
| Melee kill | Swift blade draw + single cut impact |

### Top-Down cụ thể ghi chú

- Smoke cloud phải được opaque from above — top-down camera sees dense gray circle on ground
- OBSIDIAN inside own smoke is nearly invisible from top-down (faint shimmer for teammates only)
- Smoke không được block friendly minimap detection — allies can still see teammate dots thông qua smoke
- Smoke edge nên được well-defined from above (rõ boundary between vision/no vision)
- First attack from smoke (+15% damage) applies only to the first bullet/hit, not sustained fire
