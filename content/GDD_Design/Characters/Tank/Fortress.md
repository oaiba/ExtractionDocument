---
title: "FORTRESS - Dmitri Kozlov"
type: docs
---

## Operator Profile

> *"Together we are unbreakable. Divided, we are nothing."*

### Basic Information

| Attribute | Value |
| :-------- | :---- |
| **Real Name** | Dmitri Ivanovich Kozlov |
| **Codename** | FORTRESS |
| **Class** | Tank |
| **Nationality** | Russian |
| **Age** | 48 |
| **Height** | 188 cm (6'2") |
| **Weight** | 105 kg (231 lbs) |

<!-- REF_IMAGE: FORTRESS operator portrait — broad-shouldered, heavy LMG, worn body armor with team insignia patches, cyberpunk power cells on belt -->

### Background

Colonel Dmitri Kozlov commanded Russia's elite VDV (Airborne Troops) for 15 years, known for his unbreakable defensive tactics and unwavering loyalty to his men. His philosophy: a unit that protects each other can survive anything.

After refusing orders that would have sacrificed his men for political optics, Dmitri was quietly discharged. Now he brings his protective leadership to the Exclusion Zone, where his team-focused abilities keep squads alive against impossible odds.

### Personality Traits

- **Paternal** — Treats team like family
- **Tactical** — Always thinking of the unit
- **Orthodox** — Deep religious faith
- **Unbreakable** — Will never abandon comrades

---

## Combat Statistics

### Base Stats

| Stat | Value | Class Modifier | Final |
| :--- | :---- | :------------- | :---- |
| **Health** | 100 HP | - | 100 HP |
| **Armor** | 75 | +25% cap | 75 (max 125) |
| **Sprint Speed** | 5.5 m/s | -15% | 4.675 m/s |
| **Walk Speed** | 3.5 m/s | - | 3.5 m/s |
| **Crouch Speed** | 2.0 m/s | - | 2.0 m/s |

### Damage Modifiers

| Condition | Modifier |
| :-------- | :------- |
| Base Weapon Damage | +0% (no class bonus) |
| Ally within 5m (Brotherhood) | +5% damage resistance (both) |
| Armor Overcharge active (self) | +15% damage resistance |
| Headshot Multiplier | 2.0x |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 80 | -20% (Tank class) |
| **Sprint Drain** | 12/second | +20% (Tank class) |
| **Recovery Rate** | 7.2/second | -10% (Tank class) |
| **Net Sprint Duration** | 6.7 seconds | Shortest in roster |
| **Footstep Volume** | 115% | Very loud — armored boots |
| **Ability Audio Radius** | 30 meters | Overcharge power-up hum is distinctive |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 25% | Tank class resist |
| Slow | 25% + immunity during Overcharge | Tank resist + ability grants full immunity |
| Burn | 10% | Minor fire resist from armor |
| EMP | 0% | Overcharge bonus armor stripped instantly |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 46 cm radius, 186 cm height |
| **Head Sphere** | 15 cm radius |
| **Collision Profile** | Heavy (+5% from mesh) |
| **Silhouette From Above** | Wide build, heavy armor pack visible, LMG barrel extends forward |
| **Class Accent Zones** | Steel Blue (#3B82F6) on shoulder plates and armor pack |
| **Overcharge VFX (Top-Down)** | Blue energy glow on armor plates, 8m radius pulse circle on ground for ally buff range |
| **Overcharge Audio** | 30m — deep power-up hum |

<!-- REF_IMAGE: FORTRESS top-down view — showing operator with Armor Overcharge active, blue glow on armor plates, 8m buff radius circle visible from above -->

### Difficulty Rating

**Difficulty: 3/5** — Must manage Brotherhood positioning (5m ally proximity) and Overcharge timing. Simple mechanics but requires team coordination.


## Abilities

### Active Ability: Armor Overcharge

> *"Overcharge your armor systems, creating a protective field for nearby allies."*

| Property | Value |
| :------- | :---- |
| **Cooldown** | 100 seconds |
| **Duration** | 12 seconds |
| **Range** | 8 meters |

#### Effects

| Effect | Value | Notes |
| :----- | :---- | :---- |
| Self Armor Boost | +50 temporary armor | On top of current armor |
| Ally Armor Boost | +25 temporary armor | All allies within range |
| Damage Resistance | +15% (self only) | During ability |
| Slow Immunity | Yes | Cannot be slowed during overcharge |

#### Overcharge Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **Overcharge + EMP (CIPHER)** | Bonus armor stripped instantly, ability cancelled |
| **Overcharge + Fire (BLAZE)** | Overcharge does not protect against fire DoT — extra armor absorbs it |
| **Overcharge + HAVOC Rage** | Both buffs active simultaneously — neither cancels the other |
| **Overcharge + ANGEL Shield** | Stack — overcharge armor + shield HP for maximum defense |
| **Overcharge + UAV Scan (PHANTOM)** | Overcharge does not interact with scans |

#### Top-Down Overcharge VFX

| State | VFX From Above |
| :---- | :------------- |
| Overcharge activation | Blue energy burst from FORTRESS, pulse wave expands to 8m |
| Overcharge active | Blue glow on armor plates, faint 8m radius circle on ground |
| Ally receiving buff | Blue armor particle stream from FORTRESS to ally |
| Overcharge ending | Glow dims, energy dissipates |
| Overcharge EMP'd | Blue static burst, armor plates go dark |


**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extended Field** | Duration +4 seconds (16s total) |
| **Rapid Response** | Cooldown -25 seconds (75s total) |
| **Wide Protection** | Range +4 meters (12m total) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **Shared Resistance** | Allies also get +10% damage resistance |
| **Armor Regen** | Allies regenerate 5 armor/sec in range |
| **Fortified** | Duration extends 2 seconds per kill |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Last Stand** | If downed during ability, allies keep buff for remaining duration |
| **Iron Curtain** | Allies within range take 30% less headshot damage |
| **Reactive Armor** | 20% chance to completely negate a hit |

---

### Passive Ability: Brotherhood

> *"No man left behind."*

| Condition | Effect |
| :-------- | :----- |
| Ally within 5 meters | Both gain +5% damage resistance |
| Ally downed within 10 meters | +20% movement speed toward them |
| Reviving | Take 25% less damage during revive |

**Design Intent:** FORTRESS is the team Tank. While BULWARK blocks damage for one direction, FORTRESS buffs the entire team. His power scales with team proximity — solo FORTRESS is weak, but a FORTRESS team is nearly unkillable.

---

## Loadout

### Default Loadout

| Slot | Item | Notes |
| :--- | :--- | :---- |
| **Primary** | PKM LMG | Suppressive fire, large magazine |
| **Secondary** | Makarov Pistol | Russian standard sidearm |
| **Tactical** | Armor Plates x2 | Team durability |
| **Armor** | Heavy Vest | 75 armor points |

### Recommended Loadouts

**Suppressive Wall (Defensive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | M249 SAW | Maximum suppression, 150-round belt |
| Secondary | Makarov Pistol | Backup |
| Tactical | Armor Plates x3 | Maximum team armor distribution |

**Mobile Fortress (Aggressive):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | AK-47 | Reliable damage, controllable |
| Secondary | Stun Grenades x2 | Entry support |
| Tactical | Armor Plates x1, Medkit x1 | Self-sustain + team armoring |

---

## Playstyle Guide

### Role in Team

**Primary Role:** Team Protector
- Stay near teammates to share Brotherhood passive
- Activate Armor Overcharge before team engagements
- Absorb damage for fragile teammates

**Secondary Role:** Revive Specialist
- Brotherhood gives +20% sprint speed toward downed allies
- 25% damage resistance during revive makes pickups safer
- FORTRESS + DOC revive combo is the strongest in the game

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
- Near chokepoints with team around
- Behind BULWARK (stack both Tank passives)
- At extraction zone with full team

**Bad Positions:**
- Solo (all abilities require teammates)
- Point position (too slow to retreat, draws focus without shield)
- Far from teammates (Brotherhood wasted)
- On the move between objectives (slow rotations)

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **BLAZE** | Overcharge armor absorbs incendiary damage, team stays alive | Overcharge, push through fire zone as a group |
| **SPECTER** | Sensors reveal position but overcharge negates trap damage | Accept detection, push with armor advantage |
| **ANGEL** | Guardian Shield is short duration — Overcharge outlasts it | Wait for shield to drop, then push with armored team |

### Even Matchups

| Opponent | Notes | Key to Winning |
| :------- | :---- | :------------- |
| **BULWARK** | Fellow Tank — neither kills the other fast | Whoever has better team support wins the attrition |
| **DOC** | Healing vs Armor — both extend team fights | Focus fire single targets to overwhelm healing |
| **WRAITH** | Smoke disrupts formation but armor persists | Maintain team proximity in smoke, Brotherhood still active |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **PHANTOM** | Scan reveals entire team position, enabling flanks that split formation | Push as group before scan intel can be acted on |
| **FLUX** | Nano Swarm damages through armor, DoT bypasses flat resistance | Move team out of swarm — do not try to tank it |
| **CIPHER** | EMP does not destroy Overcharge but strips temporary armor from allies | Activate Overcharge AFTER EMP, not before |

---

## Voice Lines

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Armor engaged! Stay close, brothers!" |
| Ally Takes Damage | "They're hitting my people!" |
| Kill | "For the squad." |
| Kill (While Protecting Ally) | "Nobody touches them." |
| Ally Downed | "Man down! I'm coming!" |
| Reviving | "I won't leave you. Get up!" |
| Low Health | "Armor failing... hold the line..." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| Enemy Spotted | "Contact, [Direction]. Form up." |
| Overcharge Ready | "Armor ready. Say when." |
| Overcharge Expired | "Overcharge down. Stay in cover." |
| Reloading | "Reloading. Cover each other." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "We move as one. No one dies alone." |
| Extraction Called | "Stay together. We leave as a unit." |
| Extraction Success | "Family survives. Always." |
| Squad Wipe | "They chose the wrong unit to fight." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Worn heavy plate carrier over dark olive fatigues, VDV insignia on shoulder
- **Headgear:** Russian military beanie (ushanka liner), tactical earpiece
- **Gloves:** Heavy leather field gloves
- **Face:** Thick salt-and-pepper beard, deep-set eyes with crow's feet, small orthodox cross tattoo on neck

<!-- REF_IMAGE: FORTRESS default skin — top-down view showing broad silhouette, LMG visible, heavy vest with armor plates, team-focused posture -->

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
| **Orthodox Cross** | Small steel cross on chain, visible at collar |
| **Unit Photo** | Faded photo of VDV squad tucked in vest pocket |
| **Command Badge** | Colonel rank insignia on right breast |

---

## Lore Connections

### Relationships

| Character | Relationship |
| :-------- | :----------- |
| **HAVOC** | Fellow Russian — FORTRESS worries about HAVOC's self-destructive tendencies, tries to mentor him |
| **SPECTER** | Old military contacts from overlapping operations — share tactical intelligence |
| **ANGEL** | Debates faith — both deeply religious, different traditions, mutual respect |
| **BULWARK** | Mentorship — BULWARK teaches shield work, FORTRESS teaches squad leadership |

### Story Hooks

- Searching for a way to formally clear his discharged soldiers' records
- Maintains contact with former VDV unit members scattered as mercenaries
- Receives coded messages from someone inside Russian military intelligence
- Personal quest chain involves protecting a safehouse full of displaced civilians in the Zone

---

## Design Notes (For Developers)

### Balance Considerations

- Armor Overcharge is team-dependent — solo activation is wasteful
- +25 temporary armor for allies is strong but requires 5m proximity — positioning is the skill expression
- Brotherhood passive must NOT stack with multiple FORTRESS operators — cap at one instance
- Reactive Armor upgrade (20% negate chance) should not apply to headshots
- Last Stand upgrade is emotionally powerful but mechanically niche — buff remaining duration gives team 4-6 seconds post-down
- FORTRESS + DOC combo is intentionally the strongest duo in the game — counter with CIPHER EMP

### Animation Requirements

- Overcharge activation (0.6 seconds — fist clench, armor plates glow orange)
- Overcharge VFX (expanding orange pulse from FORTRESS, team armor plates glow)
- Brotherhood proximity indicator (subtle UI pulse when allies are in range)
- Revive animation (faster/more stable than standard due to damage resistance)
- Death animation: falls slowly, reaches toward nearest ally (dramatic, team-focused)

### Audio Requirements

| Sound | Notes |
| :---- | :---- |
| Overcharge activate | Deep power-up hum + armor plate rattle |
| Overcharge active | Low ambient energy pulse (team hears it as reassuring) |
| Overcharge end | Power-down descending tone |
| Brotherhood proximity | Subtle heartbeat sync (both players hear it) |
| Footsteps | Heavy, authoritative — military boots, armor clink |
| LMG fire | Deep, sustained — signature sound in combat |

### Top-Down Specific Notes

- Overcharge 8m radius circle must be visible to teammates at minimum zoom — shows buff zone
- Blue armor glow should be clearly distinct from ANGEL shield's blue-white — use deeper steel blue
- Brotherhood passive proximity (5m) should show a subtle connecting line between FORTRESS and nearby ally
- LMG barrel extending forward from the model makes FORTRESS identifiable by weapon type from above
- Overcharge armor stripping by EMP should have dramatic VFX — communicate vulnerability to both teams

