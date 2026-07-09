---
title: "BASTION - Mikhail Ivanov"
type: docs
---

## Operator Profile

> *"Behind me. Nothing gets thông qua."*

### Basic Information

| Attribute | giá trị |
| :-------- | :---- |
| **Real Name** | Mikhail Ivanov |
| **Codename** | BASTION |
| **Class** | Tank |
| **Nationality** | Russian |
| **Age** | 41 |
| **Height** | 195 cm (6'5") |
| **Weight** | 110 kg (243 lbs) |

<!-- REF_IMAGE: BASTION operator portrait — massive frame, riot shield on back, heavy tactical vest, cyberpunk-style reinforced plating với orange accent strips -->

### Background

Hans Richter was the immovable object of GSG 9, Germany's elite counter-terrorism unit. His ability to hold positions under overwhelming fire became legendary sau a 2019 embassy siege where he protected 30 hostages for 8 hours với only a riot shield và his determination.

sau a political scandal forced budget cuts that disbanded his unit, Hans could not return to civilian life. The Exclusion Zone offer what he needs: a rõ mission, địch to stop, và people to protect.

### Personality Traits

- **Stoic** — Rarely shows emotion
- **Protective** — Lives for defending others
- **Stubborn** — Will not retreat
- **Honorable** — Respects worthy opponents

---

## Combat Statistics

### Base Stats

| Stat | giá trị | Class Modifier | Final |
| :--- | :---- | :------------- | :---- |
| **máu** | 100 HP | - | 100 HP |
| **giáp** | 75 | +25% cap | 75 (max 125) |
| **Sprint Speed** | 5.5 m/s | -15% | 4.675 m/s |
| **Walk Speed** | 3.5 m/s | - | 3.5 m/s |
| **Crouch Speed** | 2.0 m/s | - | 2.0 m/s |

### Damage Modifiers

| Condition | Modifier |
| :-------- | :------- |
| Base vũ khí Damage | +0% (no class bonus) |
| Shield Bash | 30 flat damage + 1.5s stun |
| Standing still (Living Wall) | +15% damage resistance |
| In cover (Living Wall) | +20% damage resistance |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 80 | -20% (Tank class) |
| **Sprint Drain** | 12/second | +20% (Tank class) |
| **Recovery Rate** | 7.2/second | -10% (Tank class) |
| **Net Sprint Duration** | 6.7 seconds | Shortest in roster |
| **Footstep Volume** | 120% | Loudest operator — armored boots |
| **Ability Audio Radius** | 35 meters | Shield deploy slam is very loud |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 25% | Tank class resist |
| Slow | 25% | Tank class resist |
| Burn | 10% | Minor fire resist from giáp |
| EMP | 0% | Shield disabled for 5 seconds by EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 48 cm radius, 188 cm height |
| **Head Sphere** | 15 cm radius |
| **Collision Profile** | Heavy (+5% from mesh) |
| **Silhouette From Above** | Widest operator, shield hiển thị rõ on back khi stowed, massive shoulder plates |
| **Class Accent Zones** | Steel Blue (#3B82F6) on shoulder plates và visor edge |
| **Shield VFX (Top-Down)** | 120-degree arc indicator on ground khi deployed, metallic surface hiển thị rõ |
| **Shield Audio** | 35m — deploy slam + constant metallic scraping khi walking |

<!-- REF_IMAGE: BASTION top-down view — showing operator với riot shield deployed, 120-degree arc hiển thị rõ from above, widest operator silhouette -->

### Riot Shield Stat Block

| Property | giá trị | ghi chú |
| :------- | :---- | :---- |
| **Shield Coverage** | 180-degree frontal arc | Indestructible |
| **Duration** | 15 seconds | Active thời gian |
| **Movement Penalty** | -40% | Very slow while deployed |
| **vũ khí Access** | secondary only | Pistol only |
| **Shield Bash Damage** | 30 | + 1.5s stun |
| **Shield Bash Range** | 2 meters | Close range only |
| **Shield Bash Cooldown** | 5 seconds | Internal cooldown |
| **EMP Vulnerability** | disabled 5s | Not destroyed, temporarily disabled |
| **Fire Pass-thông qua** | No | Blocks IGNITION fire trail |
| **Smoke Pass-thông qua** | Yes | Smoke passes thông qua shield |

### Difficulty Rating

**Difficulty: 2/5** — Simple concept: deploy shield, push forward. Low cơ chế complexity nhưng requires positional awareness to avoid flanks.


## Abilities

### Active Ability: Riot Shield Deploy

> *"Deploy an indestructible riot shield. Cannot fire while active."*

| Property | giá trị |
| :------- | :---- |
| **Cooldown** | 80 seconds |
| **Duration** | 15 seconds |
| **Shield Coverage** | 180 degree frontal arc |

#### Effects

| Effect | giá trị | ghi chú |
| :----- | :---- | :---- |
| Damage Block | 100% frontal | Cannot be broken by any vũ khí |
| Movement Penalty | -40% | Very slow — commit to direction |
| vũ khí cách dùng | secondary only | Pistol while shield deployed |
| Melee | Yes | Shield bash causes stun |

#### Shield Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **Shield + EMP (GLITCH)** | Shield disabled for 5 seconds (not destroyed) |
| **Shield + Fire (IGNITION)** | Fire does NOT pass thông qua riot shield |
| **Shield + Nano Swarm (PULSE)** | Swarm ignores shield — passes thông qua |
| **Shield + TARTARUS Melee** | Melee bash staggers shield (1s), does not break |
| **Shield + UAV Scan (SONAR)** | Does not reveal shielded operator |
| **Shield + Smoke (OBSIDIAN)** | Smoke blocks vision around/thông qua shield |

#### Top-Down Shield VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| Shield deploy | Flash + 120-degree arc indicator appears on ground |
| Shield active | Metallic surface hiển thị rõ from above, arc indicator persistent |
| Shield taking fire | Spark particles on shield surface |
| Shield bash | Forward thrust VFX, stun spark on target |
| Shield EMP'd | Blue static flash, arc indicator flickers off for 5s |
| Shield stow | Arc indicator fades |


| Property | giá trị |
| :------- | :---- |
| Damage | 30 |
| Stun Duration | 1.5 seconds |
| Range | 2 meters |
| Cooldown | 5 seconds (trong khi shield) |

#### upgrade Slots

**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extended Guard** | Duration +5 seconds (20s total) |
| **Quick Deploy** | Cooldown -20 seconds (60s total) |
| **Mobile Wall** | Movement penalty -15% (only -25%) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **Shield Bash+** | Bash damage +20, stun +0.5 sec |
| **Reflective Surface** | 10% damage reflected back to shooter |
| **Steadfast** | Immune to stagger/knockback |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Forward Unto Dawn** | Gain 50 temporary HP khi deploying |
| **Team Aura** | Allies behind shield gain +10% damage |
| **Explosive Resistance** | Block 50% grenade damage |

---

### Passive Ability: Living Wall

> *"The bigger they are, the harder they stand."*

| Condition | Effect |
| :-------- | :----- |
| Standing still | +15% damage resistance |
| In cover | +20% damage resistance |
| Taking fire | Generate Aggro (địch more likely to target you in PvE) |

**Design Intent:** BASTION is the anchor. His shield is the most powerful single defensive ability in the game, nhưng the trade-off is severe: almost no offensive capability while deployed. He tạo space — teammates cách dùng it.

---

## Loadout

### Default Loadout

| Slot | Item | ghi chú |
| :--- | :--- | :---- |
| **primary** | SPAS-12 Shotgun | CQB power |
| **secondary** | .44 Magnum | High damage pistol (usable behind shield) |
| **Tactical** | Flashbang x1, Extra giáp Plate x1 | Entry + durability |
| **giáp** | Heavy Vest | 75 giáp points |

### Recommended Loadouts

**The Juggernaut (Aggressive Push):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | AA-12 Auto Shotgun | Devastating CQB khi shield drops |
| secondary | Deagle | Maximum damage behind shield |
| Tactical | Flashbang x2 | Disorient trước shield push |

**Extraction Anchor (Defensive Hold):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | SPAS-12 Shotgun | Doorway control |
| secondary | .44 Magnum | Range option behind shield |
| Tactical | Extra giáp Plate x2 | Maximum durability for extraction hold |

---

## Playstyle Guide

### Role in Team

**primary Role:** Point Leader
- Be first into contested areas với shield up
- Draw địch fire và attention
- tạo safe space for team to operate

**secondary Role:** Extraction Anchor
- Hold extraction zone với shield
- Block doorways và chokepoints
- Protect teammates trong khi helicopter arrival

### Combat Loop

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

### Positioning

**Good Positions:**
- Narrow corridors (shield covers entire width)
- Doorways (one direction of threat)
- Extraction zones với walls behind you
- In front of Support operators

**Bad Positions:**
- Open ground (flanked easily around shield)
- Multiple doorways (cannot block all)
- Elevated positions (shield does not block grenades from below)
- Far from team (shield wasted mà không shooters behind)

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **MAMBA** | Shield blocks all Combat Stim damage | Face him, let stim timer expire |
| **TARTARUS** | Shield stops Berserker Rush completely | Shield up khi he charges, bash stun |
| **IGNITION** | Shield blocks incendiary rounds | Walk thông qua fire zones protected |

### Even Matchups

| Opponent | ghi chú | chính to Winning |
| :------- | :---- | :------------- |
| **GOLIATH** | Both Tanks, neither can kill the other quickly | Whoever has team support wins |
| **SUTURE** | Cannot damage him faster than drone heals | Focus drone với bash, then SUTURE |
| **AEGIS** | Guardian Shield vs Riot Shield — stalemate | Wait for her shield duration, then push |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **OBSIDIAN** | Smoke negates shield — cannot see targets | Drop shield in smoke, cách dùng primary vũ khí với audio |
| **GLITCH** | EMP instantly disables Riot Shield | Bait EMP trước deploying, hoặc pre-deploy và absorb EMP |
| **SONAR** | UAV reveals flanking teammates — shield becomes useless mà không team pressure | Coordinate push timing với team, rush trong khi scan cooldown |

---

## Voice Lines

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Shield up! I'll cover you!" |
| Shield Bash | "Back!" |
| Taking Heavy Fire | "I can take it. Keep moving!" |
| Shield Down | "Shield dropping. Need a moment." |
| Kill | "Cleared." |
| Kill (Shield Bash) | "Stay down." |
| Low máu | "giáp failing. Fall back!" |
| Reviving | "Not today, friend. Get up." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| địch Spotted | "Contact front." |
| Pushing | "Moving up. Stay behind me." |
| Reloading | "Reloading. Cover." |
| Shield Ready | "Shield ready. Say the word." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "I go first. Stay behind me." |
| Extraction Called | "Hold here. Nothing gets past." |
| Extraction success | "Mission complete. All secure." |
| Squad Wipe | "Nobody touches my team." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Heavy tactical plate carrier, reinforced arm guards, riot shield on back
- **Headgear:** Open-face tactical helmet với visor, rõ face hiển thị rõ
- **Gloves:** Reinforced knuckle gloves
- **Face:** Clean-shaven, square jaw, small scar above right eyebrow, focused eyes

<!-- REF_IMAGE: BASTION default skin — top-down view showing largest silhouette in roster, shield hiển thị rõ on back, heavy giáp profile -->

### Unlockable Skins

| Skin | Rarity | Unlock |
| :--- | :----- | :----- |
| **Iron Wall** | Common | Level 10 |
| **Winter Guard** | Uncommon | 1,000 Credits |
| **Crimson Goliath** | Rare | Level 25 |
| **GSG 9 Classic** | Epic | Battle Pass S1 |
| **Siegebreaker** | Legendary | Season 1 Event |

### Signature Items

| Item | Description |
| :--- | :---------- |
| **Shield Markings** | Tally marks scratched into riot shield surface |
| **GSG 9 Unit Patch** | Original unit insignia on left shoulder |
| **Cross Pendant** | Steel cross hiển thị rõ at collar (from grandmother) |

---

## Lore Connections

### Relationships

| nhân vật | Relationship |
| :-------- | :----------- |
| **MAMBA** | Rival philosophies — MAMBA attacks, BASTION defends. Mutual respect despite constant arguments |
| **SUTURE** | Old friends from joint NATO training. Saved each other's lives. Closest bond in the roster |
| **TARTARUS** | Professional animosity — BASTION considers TARTARUS too reckless, a danger to teammates |
| **GOLIATH** | Fellow Tank. Paternal bond — BASTION mentors the younger GOLIATH in shield work |

### Story Hooks

- Searching for former GSG 9 teammates scattered sau unit disbandment
- Has evidence that the political scandal was engineered by Corporation interests
- Maintains a personal code of honor — will not extract mà không confirming all teammates are safe
- Receives anonymous letters from someone claiming to be his former commander

---

## Design ghi chú (For Developers)

### Balance Considerations

- Riot Shield is indestructible by design — counterplay is flanking, EMP, hoặc waiting it out
- 180-degree coverage means back và sides are always vulnerable
- -40% movement penalty is critical — BASTION cannot chase hoặc flee effectively
- Shield Bash stun (1.5s) is strong nhưng has 5s internal cooldown to prevent stunlock
- Team Aura upgrade (Slot 3) must require strict positioning — allies phải được within 3m of BASTION's back arc
- Living Wall passive không nên stack với Shield — choose one hoặc the other

### Animation yêu cầu

- Shield deploy animation (0.7 seconds — pull from back mount, forward snap)
- Shield walk cycle (heavy, feet planted, slower than normal walk)
- Shield bash animation (shield thrust forward, 0.3 second impact)
- Shield stow animation (0.5 seconds — return to back mount)
- Death animation: falls to one knee, then forward (shield clatters)

### Audio yêu cầu

| Sound | ghi chú |
| :---- | :---- |
| Shield deploy | Heavy metallic slam + pneumatic lock |
| Shield walk | Heavy metal drag, boot impacts |
| Shield impact (bullets) | Metallic ping per hit (satisfying) |
| Shield bash | Heavy slam + địch stagger grunt |
| Shield stow | Metallic slide + lock click |
| Footsteps | Heaviest in roster — armored boots on floor |

### Top-Down cụ thể ghi chú

- Shield arc indicator (120-degree) phải được hiển thị rõ at minimum zoom — shows teammates và địch the protected zone
- Shield is visually distinct from AEGIS's dome: flat metallic surface vs translucent dome
- Shield walking animation from top-down should show heavy foot plants với dust/ground disturbance
- khi EMP disabled, shield visually flickers (communicates vulnerability window to both teams)
- BASTION is the widest silhouette in the game — easily identifiable even at max zoom
