---
title: "GOLIATH - Wei Chen"
type: docs
---

## Operator Profile

> *"Together we are unbreakable. Divided, we are nothing."*

### Basic Information

| Attribute | giá trị |
| :-------- | :---- |
| **Real Name** | Wei Chen |
| **Codename** | GOLIATH |
| **Class** | Tank |
| **Nationality** | Chinese |
| **Age** | 48 |
| **Height** | 188 cm (6'2") |
| **Weight** | 105 kg (231 lbs) |

<!-- REF_IMAGE: GOLIATH operator portrait — broad-shouldered, heavy LMG, worn body giáp với team insignia patches, cyberpunk power cells on belt -->

### Background

Wei Chen commanded Russia's elite VDV (Airborne Troops) for 15 years, known for his unbreakable defensive tactics và unwavering loyalty to his men. His philosophy: a unit that protects each other can survive anything.

sau refusing orders that would have sacrificed his men for political optics, Dmitri was quietly discharged. Now he brings his protective leadership to the Exclusion Zone, where his team-focused abilities keep squads alive against impossible odds.

### Personality Traits

- **Paternal** — Treats team like family
- **Tactical** — Always thinking of the unit
- **Orthodox** — Deep religious faith
- **Unbreakable** — Will never abandon comrades

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
| Ally within 5m (Brotherhood) | +5% damage resistance (both) |
| giáp Overcharge active (self) | +15% damage resistance |
| Headshot Multiplier | 2.0x |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 80 | -20% (Tank class) |
| **Sprint Drain** | 12/second | +20% (Tank class) |
| **Recovery Rate** | 7.2/second | -10% (Tank class) |
| **Net Sprint Duration** | 6.7 seconds | Shortest in roster |
| **Footstep Volume** | 115% | Very loud — armored boots |
| **Ability Audio Radius** | 30 meters | Overcharge power-up hum is distinctive |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 25% | Tank class resist |
| Slow | 25% + immunity trong khi Overcharge | Tank resist + ability grants full immunity |
| Burn | 10% | Minor fire resist from giáp |
| EMP | 0% | Overcharge bonus giáp stripped instantly |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 46 cm radius, 186 cm height |
| **Head Sphere** | 15 cm radius |
| **Collision Profile** | Heavy (+5% from mesh) |
| **Silhouette From Above** | Wide build, heavy giáp pack hiển thị rõ, LMG barrel extends forward |
| **Class Accent Zones** | Steel Blue (#3B82F6) on shoulder plates và giáp pack |
| **Overcharge VFX (Top-Down)** | Blue energy glow on giáp plates, 8m radius pulse circle on ground for ally buff range |
| **Overcharge Audio** | 30m — deep power-up hum |

<!-- REF_IMAGE: GOLIATH top-down view — showing operator với giáp Overcharge active, blue glow on giáp plates, 8m buff radius circle hiển thị rõ from above -->

### Difficulty Rating

**Difficulty: 3/5** — Must manage Brotherhood positioning (5m ally proximity) và Overcharge timing. Simple cơ chế nhưng requires team coordination.


## Abilities

### Active Ability: giáp Overcharge

> *"Overcharge your giáp hệ thống, tạo a protective field for nearby allies."*

| Property | giá trị |
| :------- | :---- |
| **Cooldown** | 100 seconds |
| **Duration** | 12 seconds |
| **Range** | 8 meters |

#### Effects

| Effect | giá trị | ghi chú |
| :----- | :---- | :---- |
| Self giáp Boost | +50 temporary giáp | On top of hiện tại giáp |
| Ally giáp Boost | +25 temporary giáp | All allies within range |
| Damage Resistance | +15% (self only) | trong khi ability |
| Slow Immunity | Yes | Cannot be slowed trong khi overcharge |

#### Overcharge Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **Overcharge + EMP (GLITCH)** | Bonus giáp stripped instantly, ability cancelled |
| **Overcharge + Fire (IGNITION)** | Overcharge does not protect against fire DoT — extra giáp absorbs it |
| **Overcharge + TARTARUS Rage** | Both buffs active simultaneously — neither cancels the other |
| **Overcharge + AEGIS Shield** | Stack — overcharge giáp + shield HP for maximum defense |
| **Overcharge + UAV Scan (SONAR)** | Overcharge does not interact với scans |

#### Top-Down Overcharge VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| Overcharge activation | Blue energy burst from GOLIATH, pulse wave expands to 8m |
| Overcharge active | Blue glow on giáp plates, faint 8m radius circle on ground |
| Ally receiving buff | Blue giáp particle stream from GOLIATH to ally |
| Overcharge ending | Glow dims, energy dissipates |
| Overcharge EMP'd | Blue static burst, giáp plates go dark |


**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extended Field** | Duration +4 seconds (16s total) |
| **Rapid Response** | Cooldown -25 seconds (75s total) |
| **Wide Protection** | Range +4 meters (12m total) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **shared Resistance** | Allies also get +10% damage resistance |
| **giáp Regen** | Allies regenerate 5 giáp/sec in range |
| **Fortified** | Duration extends 2 seconds per kill |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Last Stand** | nếu downed trong khi ability, allies keep buff for remaining duration |
| **Iron Curtain** | Allies within range take 30% less headshot damage |
| **Reactive giáp** | 20% chance to completely negate a hit |

---

### Passive Ability: Brotherhood

> *"No man left behind."*

| Condition | Effect |
| :-------- | :----- |
| Ally within 5 meters | Both gain +5% damage resistance |
| Ally downed within 10 meters | +20% movement speed toward them |
| Reviving | Take 25% less damage trong khi revive |

**Design Intent:** GOLIATH is the team Tank. While BASTION blocks damage for one direction, GOLIATH buffs the entire team. His power scales với team proximity — solo GOLIATH is weak, nhưng a GOLIATH team is nearly unkillable.

---

## Loadout

### Default Loadout

| Slot | Item | ghi chú |
| :--- | :--- | :---- |
| **primary** | PKM LMG | Suppressive fire, large magazine |
| **secondary** | Makarov Pistol | Russian standard sidearm |
| **Tactical** | giáp Plates x2 | Team durability |
| **giáp** | Heavy Vest | 75 giáp points |

### Recommended Loadouts

**Suppressive Wall (Defensive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | M249 SAW | Maximum suppression, 150-round belt |
| secondary | Makarov Pistol | Backup |
| Tactical | giáp Plates x3 | Maximum team giáp distribution |

**Mobile Goliath (Aggressive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | AK-47 | Reliable damage, controllable |
| secondary | Stun Grenades x2 | Entry support |
| Tactical | giáp Plates x1, Medkit x1 | Self-sustain + team armoring |

---

## Playstyle Guide

### Role in Team

**primary Role:** Team Protector
- Stay near teammates to share Brotherhood passive
- Activate giáp Overcharge trước team engagements
- Absorb damage for fragile teammates

**secondary Role:** Revive Specialist
- Brotherhood gives +20% sprint speed toward downed allies
- 25% damage resistance trong khi revive makes pickups safer
- GOLIATH + SUTURE revive combo is the strongest in the game

### Combat Loop

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

### Positioning

**Good Positions:**
- Center of team formation (Brotherhood range)
- Near chokepoints với team around
- Behind BASTION (stack both Tank passives)
- At extraction zone với full team

**Bad Positions:**
- Solo (all abilities require teammates)
- Point position (too slow to retreat, draws focus mà không shield)
- Far from teammates (Brotherhood wasted)
- On the move between objectives (slow rotations)

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **IGNITION** | Overcharge giáp absorbs incendiary damage, team stays alive | Overcharge, push thông qua fire zone as a group |
| **MIRAGE** | Sensors reveal position nhưng overcharge negates trap damage | Accept detection, push với giáp advantage |
| **AEGIS** | Guardian Shield is short duration — Overcharge outlasts it | Wait for shield to drop, then push với armored team |

### Even Matchups

| Opponent | ghi chú | chính to Winning |
| :------- | :---- | :------------- |
| **BASTION** | Fellow Tank — neither kills the other fast | Whoever has better team support wins the attrition |
| **SUTURE** | Healing vs giáp — both extend team fights | Focus fire single targets to overwhelm healing |
| **OBSIDIAN** | Smoke disrupts formation nhưng giáp persists | Maintain team proximity in smoke, Brotherhood still active |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **SONAR** | Scan reveals entire team position, enabling flanks that split formation | Push as group trước scan intel can be acted on |
| **PULSE** | Nano Swarm damages thông qua giáp, DoT bypasses flat resistance | Move team out of swarm — do not try to tank it |
| **GLITCH** | EMP does not destroy Overcharge nhưng strips temporary giáp from allies | Activate Overcharge sau EMP, not trước |

---

## Voice Lines

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "giáp engaged! Stay close, brothers!" |
| Ally Takes Damage | "They're hitting my people!" |
| Kill | "For the squad." |
| Kill (While Protecting Ally) | "Nobody touches them." |
| Ally Downed | "Man down! I'm coming!" |
| Reviving | "I won't leave you. Get up!" |
| Low máu | "giáp failing... hold the line..." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| địch Spotted | "Contact, [Direction]. Form up." |
| Overcharge Ready | "giáp ready. Say khi." |
| Overcharge Expired | "Overcharge down. Stay in cover." |
| Reloading | "Reloading. Cover each other." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "We move as one. No one dies alone." |
| Extraction Called | "Stay together. We leave as a unit." |
| Extraction success | "Family survives. Always." |
| Squad Wipe | "They chose the wrong unit to fight." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Worn heavy plate carrier over dark olive fatigues, VDV insignia on shoulder
- **Headgear:** Russian military beanie (ushanka liner), tactical earpiece
- **Gloves:** Heavy leather field gloves
- **Face:** Thick salt-và-pepper beard, deep-set eyes với crow's feet, small orthodox cross tattoo on neck

<!-- REF_IMAGE: GOLIATH default skin — top-down view showing broad silhouette, LMG hiển thị rõ, heavy vest với giáp plates, team-focused posture -->

### Unlockable Skins

| Skin | Rarity | Unlock |
| :--- | :----- | :----- |
| **Steel Curtain** | Common | Level 10 |
| **Arctic Patrol** | Uncommon | 1,000 Credits |
| **Red Star** | Rare | Level 25 |
| **VDV Commander** | Epic | Battle Pass S1 |
| **The Colonel** | Legendary | Season 1 Event |

### Signature Items

| Item | Description |
| :--- | :---------- |
| **Orthodox Cross** | Small steel cross on chain, hiển thị rõ at collar |
| **Unit Photo** | Faded photo of VDV squad tucked in vest pocket |
| **Command Badge** | Colonel rank insignia on right breast |

---

## Lore Connections

### Relationships

| nhân vật | Relationship |
| :-------- | :----------- |
| **TARTARUS** | Fellow Russian — GOLIATH worries about TARTARUS's self-destructive tendencies, tries to mentor him |
| **MIRAGE** | Old military contacts from overlapping operations — share tactical intelligence |
| **AEGIS** | Debates faith — both deeply religious, different traditions, mutual respect |
| **BASTION** | Mentorship — BASTION teaches shield work, GOLIATH teaches squad leadership |

### Story Hooks

- Searching for a way to formally rõ his discharged soldiers' records
- Maintains contact với former VDV unit members scattered as mercenaries
- Receives coded messages from someone inside Russian military intelligence
- Personal quest chain involves protecting a safehouse full of displaced civilians in the Zone

---

## Design ghi chú (For Developers)

### Balance Considerations

- giáp Overcharge is team-dependent — solo activation is wasteful
- +25 temporary giáp for allies is strong nhưng requires 5m proximity — positioning is the skill expression
- Brotherhood passive không được stack với multiple GOLIATH operators — cap at one instance
- Reactive giáp upgrade (20% negate chance) không nên apply to headshots
- Last Stand upgrade is emotionally powerful nhưng mechanically niche — buff remaining duration gives team 4-6 seconds post-down
- GOLIATH + SUTURE combo is intentionally the strongest duo in the game — counter với GLITCH EMP

### Animation yêu cầu

- Overcharge activation (0.6 seconds — fist clench, giáp plates glow orange)
- Overcharge VFX (expanding orange pulse from GOLIATH, team giáp plates glow)
- Brotherhood proximity indicator (subtle UI pulse khi allies are in range)
- Revive animation (faster/more stable than standard due to damage resistance)
- Death animation: falls slowly, reaches toward nearest ally (dramatic, team-focused)

### Audio yêu cầu

| Sound | ghi chú |
| :---- | :---- |
| Overcharge activate | Deep power-up hum + giáp plate rattle |
| Overcharge active | Low ambient energy pulse (team hears it as reassuring) |
| Overcharge end | Power-down descending tone |
| Brotherhood proximity | Subtle heartbeat sync (both người chơi hear it) |
| Footsteps | Heavy, authoritative — military boots, giáp clink |
| LMG fire | Deep, sustained — signature sound in combat |

### Top-Down cụ thể ghi chú

- Overcharge 8m radius circle phải được hiển thị rõ to teammates at minimum zoom — shows buff zone
- Blue giáp glow nên được clearly distinct from AEGIS shield's blue-white — cách dùng deeper steel blue
- Brotherhood passive proximity (5m) should show a subtle connecting line between GOLIATH và nearby ally
- LMG barrel extending forward from the model makes GOLIATH identifiable by vũ khí type from above
- Overcharge giáp stripping by EMP should have dramatic VFX — communicate vulnerability to both teams
