---
title: "SONAR - Sarah Kim"
type: docs
---

## Operator Profile

> *"Knowledge is the deadliest weapon. They're already dead — they just don't know it yet."*

### Basic Information

| Attribute | Value |
| :-------- | :---- |
| **Real Name** | Sarah Ji-Young Kim |
| **Codename** | SONAR |
| **Class** | Recon |
| **Nationality** | Korean-American |
| **Age** | 29 |
| **Height** | 168 cm (5'6") |
| **Weight** | 57 kg (126 lbs) |

<!-- REF_IMAGE: SONAR operator portrait — lean build, tactical headset with holographic HUD overlay, dark clothing with subtle cyan data-stream accents -->

### Background

Sarah Kim was one of the CIA's most effective intelligence analysts before transitioning to field work. Her ability to predict enemy movements and process information under pressure made her invaluable for deep cover operations in North Korea and China.

After a mole compromised her network, Sarah watched helplessly as her assets were eliminated one by one. She went dark, cutting all ties with the Agency. Now she operates independently, using her skills to stay three steps ahead of everyone — allies and enemies alike.

### Personality Traits

- **Analytical** — Everything is data to process
- **Paranoid** — Trusts no one completely
- **Efficient** — No wasted movements or words
- **Haunted** — Carries guilt for lost assets

---

## Combat Statistics

### Base Stats

| Stat | Value | Class Modifier | Final |
| :--- | :---- | :------------- | :---- |
| **Health** | 100 HP | -5% | 95 HP |
| **Armor** | 30 | - | 30 |
| **Sprint Speed** | 5.5 m/s | - | 5.5 m/s |
| **Crouch Speed** | 2.0 m/s | +15% | 2.3 m/s |
| **Footstep Volume** | 100% | -30% | 70% |

### Damage Modifiers

| Condition | Modifier |
| :-------- | :------- |
| Base Weapon Damage | +0% (no class bonus) |
| First Shot from Stealth | +10% (Ghost Protocol passive) |
| Headshot Multiplier | 2.0x |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 110 | +10% (Recon class) |
| **Sprint Drain** | 9/second | -10% (Recon class) |
| **Recovery Rate** | 9.6/second | +20% (Recon class) |
| **Net Sprint Duration** | 12.2 seconds | Best efficiency |
| **Footstep Volume** | 70% | -30% (Recon class trait) |
| **Ability Audio Radius** | 20 meters | UAV drone buzz audible to nearby enemies |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT |
| EMP | 0% | UAV destroyed instantly by EMP |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 34 cm radius, 170 cm height |
| **Head Sphere** | 13 cm radius |
| **Collision Profile** | Slim (-10% from mesh) |
| **Silhouette From Above** | Slim build, tech goggle glow visible from above, compact UAV pack on back |
| **Class Accent Zones** | Cyan (#06B6D4) on goggle glow and tech strips on armor |
| **Scan VFX (Top-Down)** | Cyan pulse rings expanding from operator, enemy outlines appear |
| **UAV Audio Radius** | 20m — drone buzz is moderate volume |

<!-- REF_IMAGE: SONAR top-down view — showing operator with UAV scan active, cyan pulse rings expanding outward, enemy silhouettes highlighted through walls -->

### UAV Stat Block

| Property | Value | Notes |
| :------- | :---- | :---- |
| **Scan Radius** | 30 meters | From SONAR position |
| **Duration** | 8 seconds | Continuous scan |
| **Enemy Reveal** | Real-time outlines | Cyan silhouettes through geometry |
| **Team Sharing** | Yes | All allies see scanned enemies |
| **UAV Altitude** | 15 meters above | Cannot be shot by ground fire |
| **EMP Vulnerability** | Destroyed instantly (falls) | Primary counter |
| **Smoke Interaction** | Blocks scan LOS | Cannot scan through OBSIDIAN smoke |
| **Deployable Detection** | Yes | Reveals enemy deployables (sensors, drones, shields) |

### Difficulty Rating

**Difficulty: 2/5** — Simple activation: press ability, see enemies. Low mechanical demand, but high strategic value in knowing when to scan.


## Abilities

### Active Ability: UAV Scan

> *"Deploy a drone to reveal all enemies in the area."*

| Property | Value |
| :------- | :---- |
| **Cooldown** | 100 seconds |
| **Duration** | 8 seconds |
| **Charges** | 1 |

#### Effects

| Effect | Value | Notes |
| :----- | :---- | :---- |
| Scan Radius | 30 meters | Centered on SONAR |
| Enemy Reveal | Real-time | Enemies visible through walls |
| Team Sharing | Yes | All allies see marked enemies |
| Update Rate | Continuous | Not just snapshot |

#### UAV Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **UAV + EMP (GLITCH)** | UAV destroyed instantly, falls from sky |
| **UAV + Fire (IGNITION)** | Not affected — UAV is airborne |
| **UAV + Nano Swarm (PULSE)** | Not affected — swarm only targets ground |
| **UAV + Smoke (OBSIDIAN)** | Scan blocked through smoke — LOS required |
| **UAV + AEGIS Shield** | UAV cannot reveal operators inside shield dome |
| **UAV + BASTION Shield** | Does not reveal shielded operator |

#### Top-Down Scan VFX

| State | VFX From Above |
| :---- | :------------- |
| UAV deploy | Drone rises from operator's back, ascends to scan height |
| Scan active | Cyan pulse rings expanding from operator position (30m radius) |
| Enemy detected | Red outline appears on enemy model, visible through walls |
| Scan ending | Pulse rings fade, drone descends |
| UAV EMP'd | Flash burst, drone falls to ground as debris |


**Self:**
- Radar pulse animation on HUD
- Enemy silhouettes through walls (cyan outlines)
- Sonar ping audio loop

**Enemy Perspective:**
- Faint scanner noise (audio cue at 15m range)
- "DETECTED" indicator on HUD when scanned
- Cannot see the drone or scan radius

#### Upgrade Slots

**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extended Scan** | Duration +4 seconds (12s total) |
| **Quick Sweep** | Cooldown -20 seconds (80s total) |
| **Wide Net** | Radius +10 meters (40m total) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **Threat Assessment** | Shows enemy health bars during scan |
| **Silent Scan** | Enemies do not know they are scanned |
| **Tracking Dart** | One enemy stays marked for 30 seconds after scan ends |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Predictive Analysis** | Shows enemy movement direction arrows |
| **Weapon Intel** | Shows enemy weapon types on HUD |
| **Counter-Intel** | Marks enemies who scanned you back |

---

### Passive Ability: Ghost Protocol

> *"Leave no trace. Remain unseen."*

| Condition | Effect |
| :-------- | :----- |
| Crouch walking | -30% footstep volume (stacks with class trait) |
| In cover for 3 seconds | Reduced enemy visibility (harder to spot) |
| Not firing for 5 seconds | Do not appear on enemy minimaps |

**Design Intent:** Rewards patient, information-first gameplay. SONAR should always know more than her enemies.

---

## Loadout

### Default Loadout

| Slot | Item | Notes |
| :--- | :--- | :---- |
| **Primary** | VSS Vintorez (Silenced) | Quiet kills, integrated suppressor |
| **Secondary** | Silenced Pistol | Backup stealth |
| **Tactical** | Sensor Mines x2 | Early warning traps |
| **Armor** | Light Vest | 30 armor points |

### Recommended Loadouts

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

## Playstyle Guide

### Role in Team

**Primary Role:** Information Provider
- Scan before every engagement
- Call out enemy positions, health, and weapons
- Enable team to take favorable fights

**Secondary Role:** Flanker
- Use Ghost Protocol to move undetected
- Attack from unexpected angles after scan
- Punish enemies focused on your teammates

### Combat Loop

```
1. Move to elevated/safe position
2. Deploy UAV Scan (8 second intel window)
3. Call out enemy positions to team
4. Team engages based on intel
5. Flank or snipe from stealth
6. Relocate before scan cooldown
7. Wait for cooldown, repeat
```

### Positioning

**Good Positions:**
- Elevated ground with sightlines
- Behind team, feeding intel
- Near extraction zone for final scan

**Bad Positions:**
- Point of engagement (too fragile)
- Isolated without escape route
- Ground level in open terrain

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **GOLIATH** | Scan reveals position, then flank behind shield | Scan, mark, let team focus fire |
| **PULSE** | Low combat stats, Nano Swarm easy to avoid with intel | Maintain distance, call out swarm |
| **SUTURE** | Fragile when caught alone, drone position revealed | Snipe drone first, then SUTURE |

### Even Matchups

| Opponent | Notes | Key to Winning |
| :------- | :---- | :------------- |
| **MIRAGE** | Both intel operators, sensor vs. scan | Scan detects sensors, destroy them |
| **IGNITION** | Fire zones limit movement options | Avoid fire, use range advantage |
| **AEGIS** | Shield blocks but scan reveals timing | Wait for shield down, then burst |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **MAMBA** | Combat Stim out-damages you in any duel | Avoid direct combat, use intel to evade |
| **OBSIDIAN** | Smoke breaks sightlines, ruins scan value | Push through or wait out smoke duration |
| **TARTARUS** | CQB monster, you are fragile | Never let TARTARUS close the gap |

---

## Voice Lines

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Scanning. Eyes on." |
| Enemy Located | "Contact. [Direction]. [Distance]." |
| Multiple Enemies | "Multiple hostiles. Marking all." |
| Kill | "Target eliminated." |
| Kill (Headshot) | "Precision." |
| Low Health | "I'm hit. Need cover." |
| Reviving | "Stay with me. Intel first, then we move." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| Enemy Spotted | "Eyes on hostile, [Direction]." |
| Reloading | "Reloading. Cover me." |
| Grenade | "Grenade! Move!" |
| Scan Expired | "Scan dark. Blind for 90 seconds." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "Stay quiet. Stay alive." |
| Extraction Called | "Chopper inbound. Final scan." |
| Extraction Success | "Objective complete. Moving out." |
| Squad Wipe | "They never knew we were here." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Black tactical jacket with dark blue accents, lightweight plate carrier
- **Headgear:** Tactical headset with translucent holographic monocle (HUD overlay)
- **Gloves:** Gray thin operator gloves (touch-screen compatible)
- **Face:** Short black hair, focused expression, data-stream tattoo behind left ear

<!-- REF_IMAGE: SONAR default skin — top-down view showing silhouette with UAV drone in hand, dark outfit with cyan tech accents -->

### Unlockable Skins

| Skin | Rarity | Unlock |
| :--- | :----- | :----- |
| **Urban Shadow** | Common | Level 10 |
| **Winter Intel** | Uncommon | 1,000 Credits |
| **Neon Ghost** | Rare | Level 25 |
| **Black Site** | Epic | Battle Pass S1 |
| **Digital Obsidian** | Legendary | Season 1 Event |

### Signature Items

| Item | Description |
| :--- | :---------- |
| **Holographic Monocle** | Flip-down data display over right eye |
| **USB Dog Tag** | Encrypted data drive on chain |
| **Ghost Patch** | Shoulder patch — skull with circuit board pattern |

---

## Lore Connections

### Relationships

| Character | Relationship |
| :-------- | :----------- |
| **MAMBA** | Professional respect, different methods — he leads from the front, she leads from the shadows |
| **GLITCH** | Uneasy allies, both have secrets — share intelligence cautiously |
| **MIRAGE** | Former adversaries during Cold War-era proxy ops, now grudging respect |
| **SUTURE** | Trusts him most — he saved one of her assets years ago |

### Story Hooks

- Hunting the mole who burned her network (major personal quest chain)
- Has intercepted Corporation communications about "Project Lazarus"
- Maintains a dead drop network across all maps — environmental storytelling
- Received an encrypted message from a supposedly dead asset

---

## Design Notes (For Developers)

### Balance Considerations

- UAV Scan is powerful but has a 100s cooldown — longest in the game
- 95 HP makes her the second-most fragile operator (tied with all Recon)
- Ghost Protocol rewards patience but does not make her invisible
- Scan radius (30m) is intentionally shorter than engagement range to force positioning choices
- Silent Scan upgrade (Slot 2) is the strongest option — monitor pick rate

### Animation Requirements

- UAV deployment animation (0.8 seconds — pull drone from back, throw upward)
- Scanning pulse VFX (expanding cyan ring from operator position)
- Enemy outline shader (cyan silhouette through geometry, 30m range)
- Ghost Protocol crouch walk (quieter, lower stance than standard crouch)
- Death animation: falls backward (defensive stance)

### Audio Requirements

| Sound | Notes |
| :---- | :---- |
| UAV deploy | Mechanical whir + ascending drone buzz |
| Scanning active | Persistent sonar ping loop (subtle) |
| Scan end | Drone recall sound + descending buzz |
| Enemy detected ping | Sharp, directional chime |
| Footsteps | Light, tactical boots — quieter than all classes |

### Top-Down Specific Notes

- Scan pulse rings must be visible at minimum zoom — clearly shows scan radius to teammates
- Enemy outlines should be visible through geometry from top-down camera (red silhouettes)
- UAV drone model above the battlefield should be visible as a small cyan dot from max zoom
- Ghost Protocol first-shot bonus is not visually indicated to enemies — incentivizes stealth play
- Scan does NOT show enemy health bars — only position outlines

