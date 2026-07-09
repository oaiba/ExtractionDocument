---
title: "SONAR - Sarah Kim"
type: docs
---

## Operator Profile

> *"Knowledge is the deadliest vũ khí. They're already dead — they just don't know it yet."*

### Basic Information

| Attribute | giá trị |
| :-------- | :---- |
| **Real Name** | Sarah Ji-Young Kim |
| **Codename** | SONAR |
| **Class** | Recon |
| **Nationality** | Korean-American |
| **Age** | 29 |
| **Height** | 168 cm (5'6") |
| **Weight** | 57 kg (126 lbs) |

<!-- REF_IMAGE: SONAR operator portrait — lean build, tactical headset với holographic HUD overlay, dark clothing với subtle cyan data-stream accents -->

### Background

Sarah Kim was one of the CIA's most effective intelligence analysts trước transitioning to field work. Her ability to predict địch movements và process information under pressure made her invaluable for deep cover operations in North Korea và China.

sau a mole compromised her network, Sarah watched helplessly as her assets were eliminated one by one. She went dark, cutting all ties với the Agency. Now she operates independently, using her skills to stay three steps ahead of everyone — allies và địch alike.

### Personality Traits

- **Analytical** — Everything is data to process
- **Paranoid** — Trusts no one completely
- **Efficient** — No wasted movements hoặc words
- **Haunted** — Carries guilt for lost assets

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
| First Shot from Stealth | +10% (Ghost Protocol passive) |
| Headshot Multiplier | 2.0x |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 110 | +10% (Recon class) |
| **Sprint Drain** | 9/second | -10% (Recon class) |
| **Recovery Rate** | 9.6/second | +20% (Recon class) |
| **Net Sprint Duration** | 12.2 seconds | Best efficiency |
| **Footstep Volume** | 70% | -30% (Recon class trait) |
| **Ability Audio Radius** | 20 meters | UAV drone buzz audible to nearby địch |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT |
| EMP | 0% | UAV destroyed instantly by EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 34 cm radius, 170 cm height |
| **Head Sphere** | 13 cm radius |
| **Collision Profile** | Slim (-10% from mesh) |
| **Silhouette From Above** | Slim build, tech goggle glow hiển thị rõ from above, compact UAV pack on back |
| **Class Accent Zones** | Cyan (#06B6D4) on goggle glow và tech strips on giáp |
| **Scan VFX (Top-Down)** | Cyan pulse rings expanding from operator, địch outlines appear |
| **UAV Audio Radius** | 20m — drone buzz is moderate volume |

<!-- REF_IMAGE: SONAR top-down view — showing operator với UAV scan active, cyan pulse rings expanding outward, địch silhouettes highlighted thông qua walls -->

### UAV Stat Block

| Property | giá trị | ghi chú |
| :------- | :---- | :---- |
| **Scan Radius** | 30 meters | From SONAR position |
| **Duration** | 8 seconds | Continuous scan |
| **địch Reveal** | Real-thời gian outlines | Cyan silhouettes thông qua geometry |
| **Team Sharing** | Yes | All allies see scanned địch |
| **UAV Altitude** | 15 meters above | Cannot be shot by ground fire |
| **EMP Vulnerability** | Destroyed instantly (falls) | primary counter |
| **Smoke Interaction** | Blocks scan LOS | Cannot scan thông qua OBSIDIAN smoke |
| **Deployable Detection** | Yes | Reveals địch deployables (sensors, drones, shields) |

### Difficulty Rating

**Difficulty: 2/5** — Simple activation: press ability, Xem địch. Low cơ chế demand, nhưng high strategic giá trị in knowing khi to scan.


## Abilities

### Active Ability: UAV Scan

> *"Deploy a drone to reveal all địch in the area."*

| Property | giá trị |
| :------- | :---- |
| **Cooldown** | 100 seconds |
| **Duration** | 8 seconds |
| **Charges** | 1 |

#### Effects

| Effect | giá trị | ghi chú |
| :----- | :---- | :---- |
| Scan Radius | 30 meters | Centered on SONAR |
| địch Reveal | Real-thời gian | địch hiển thị rõ thông qua walls |
| Team Sharing | Yes | All allies see marked địch |
| Update Rate | Continuous | Not just snapshot |

#### UAV Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **UAV + EMP (GLITCH)** | UAV destroyed instantly, falls from sky |
| **UAV + Fire (IGNITION)** | Not affected — UAV is airborne |
| **UAV + Nano Swarm (PULSE)** | Not affected — swarm only targets ground |
| **UAV + Smoke (OBSIDIAN)** | Scan blocked thông qua smoke — LOS required |
| **UAV + AEGIS Shield** | UAV cannot reveal operators inside shield dome |
| **UAV + BASTION Shield** | Does not reveal shielded operator |

#### Top-Down Scan VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| UAV deploy | Drone rises from operator's back, ascends to scan height |
| Scan active | Cyan pulse rings expanding from operator position (30m radius) |
| địch detected | Red outline appears on địch model, hiển thị rõ thông qua walls |
| Scan ending | Pulse rings fade, drone descends |
| UAV EMP'd | Flash burst, drone falls to ground as debris |


**Self:**
- Radar pulse animation on HUD
- địch silhouettes thông qua walls (cyan outlines)
- Sonar ping audio loop

**địch Perspective:**
- Faint scanner noise (audio cue at 15m range)
- "DETECTED" indicator on HUD khi scanned
- Cannot see the drone hoặc scan radius

#### upgrade Slots

**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extended Scan** | Duration +4 seconds (12s total) |
| **Quick Sweep** | Cooldown -20 seconds (80s total) |
| **Wide Net** | Radius +10 meters (40m total) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **Threat Assessment** | Shows địch máu bars trong khi scan |
| **Silent Scan** | địch do not know they are scanned |
| **Tracking Dart** | One địch stays marked for 30 seconds sau scan ends |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Predictive Analysis** | Shows địch movement direction arrows |
| **vũ khí Intel** | Shows địch vũ khí types on HUD |
| **Counter-Intel** | Marks địch who scanned you back |

---

### Passive Ability: Ghost Protocol

> *"Leave no trace. Remain unseen."*

| Condition | Effect |
| :-------- | :----- |
| Crouch walking | -30% footstep volume (stacks với class trait) |
| In cover for 3 seconds | Reduced địch visibility (harder to spot) |
| Not firing for 5 seconds | Do not appear on địch minimaps |

**Design Intent:** Rewards patient, information-first gameplay. SONAR should always know more than her địch.

---

## Loadout

### Default Loadout

| Slot | Item | ghi chú |
| :--- | :--- | :---- |
| **primary** | VSS Vintorez (Silenced) | Quiet kills, integrated suppressor |
| **secondary** | Silenced Pistol | Backup stealth |
| **Tactical** | Sensor Mines x2 | Early cảnh báo traps |
| **giáp** | Light Vest | 30 giáp points |

### Recommended Loadouts

**Long-Range Intel:**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | SVD Marksman Rifle | Engage from scan range |
| secondary | Silenced Pistol | Emergency backup |
| Tactical | Sensor Mines x2 | Watch your back |

**Aggressive Scout:**

| Slot | Item | Why |
| :--- | :--- | :-- |
| primary | MP5 (Suppressed) | CQB capability với stealth |
| secondary | Smoke Grenade x1 | Escape tool |
| Tactical | Flashbang x2 | Entry sau scan reveals positions |

---

## Playstyle Guide

### Role in Team

**primary Role:** Information Provider
- Scan trước every engagement
- Call out địch positions, máu, và vũ khí
- Enable team to take favorable fights

**secondary Role:** Flanker
- cách dùng Ghost Protocol to move undetected
- Attack from unexpected angles sau scan
- Punish địch focused on your teammates

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
- Elevated ground với sightlines
- Behind team, feeding intel
- Near extraction zone for final scan

**Bad Positions:**
- Point of engagement (too fragile)
- Isolated mà không escape route
- Ground level in open terrain

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **GOLIATH** | Scan reveals position, then flank behind shield | Scan, mark, let team focus fire |
| **PULSE** | Low combat stats, Nano Swarm easy to avoid với intel | Maintain distance, call out swarm |
| **SUTURE** | Fragile khi caught alone, drone position revealed | Snipe drone first, then SUTURE |

### Even Matchups

| Opponent | ghi chú | chính to Winning |
| :------- | :---- | :------------- |
| **MIRAGE** | Both intel operators, sensor vs. scan | Scan detects sensors, destroy them |
| **IGNITION** | Fire zones limit movement options | Avoid fire, cách dùng range advantage |
| **AEGIS** | Shield blocks nhưng scan reveals timing | Wait for shield down, then burst |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **MAMBA** | Combat Stim out-damages you in any duel | Avoid direct combat, cách dùng intel to evade |
| **OBSIDIAN** | Smoke breaks sightlines, ruins scan giá trị | Push thông qua hoặc wait out smoke duration |
| **TARTARUS** | CQB monster, you are fragile | Never let TARTARUS close the gap |

---

## Voice Lines

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Scanning. Eyes on." |
| địch Located | "Contact. [Direction]. [Distance]." |
| Multiple địch | "Multiple hostiles. Marking all." |
| Kill | "Target eliminated." |
| Kill (Headshot) | "Precision." |
| Low máu | "I'm hit. Need cover." |
| Reviving | "Stay với me. Intel first, then we move." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| địch Spotted | "Eyes on hostile, [Direction]." |
| Reloading | "Reloading. Cover me." |
| Grenade | "Grenade! Move!" |
| Scan Expired | "Scan dark. Blind for 90 seconds." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "Stay quiet. Stay alive." |
| Extraction Called | "Chopper inbound. Final scan." |
| Extraction success | "Objective complete. Moving out." |
| Squad Wipe | "They never knew we were here." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Black tactical jacket với dark blue accents, lightweight plate carrier
- **Headgear:** Tactical headset với translucent holographic monocle (HUD overlay)
- **Gloves:** Gray thin operator gloves (touch-màn hình compatible)
- **Face:** Short black hair, focused expression, data-stream tattoo behind left ear

<!-- REF_IMAGE: SONAR default skin — top-down view showing silhouette với UAV drone in hand, dark outfit với cyan tech accents -->

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
| **Ghost Patch** | Shoulder patch — skull với circuit board pattern |

---

## Lore Connections

### Relationships

| nhân vật | Relationship |
| :-------- | :----------- |
| **MAMBA** | Professional respect, different methods — he leads from the front, she leads from the shadows |
| **GLITCH** | Uneasy allies, both have secrets — share intelligence cautiously |
| **MIRAGE** | Former adversaries trong khi Cold War-era proxy ops, now grudging respect |
| **SUTURE** | Trusts him most — he saved one of her assets years ago |

### Story Hooks

- Hunting the mole who burned her network (major personal quest chain)
- Has intercepted Corporation communications about "Project Lazarus"
- Maintains a dead drop network across all maps — environmental storytelling
- Received an encrypted message from a supposedly dead asset

---

## Design ghi chú (For Developers)

### Balance Considerations

- UAV Scan is powerful nhưng has a 100s cooldown — longest in the game
- 95 HP makes her the second-most fragile operator (tied với all Recon)
- Ghost Protocol rewards patience nhưng does not make her invisible
- Scan radius (30m) is intentionally shorter than engagement range to force positioning choices
- Silent Scan upgrade (Slot 2) is the strongest option — monitor pick rate

### Animation yêu cầu

- UAV deployment animation (0.8 seconds — pull drone from back, throw upward)
- Scanning pulse VFX (expanding cyan ring from operator position)
- địch outline shader (cyan silhouette thông qua geometry, 30m range)
- Ghost Protocol crouch walk (quieter, lower stance than standard crouch)
- Death animation: falls backward (defensive stance)

### Audio yêu cầu

| Sound | ghi chú |
| :---- | :---- |
| UAV deploy | cơ chế whir + ascending drone buzz |
| Scanning active | Persistent sonar ping loop (subtle) |
| Scan end | Drone recall sound + descending buzz |
| địch detected ping | Sharp, directional chime |
| Footsteps | Light, tactical boots — quieter than all classes |

### Top-Down cụ thể ghi chú

- Scan pulse rings phải được hiển thị rõ at minimum zoom — clearly shows scan radius to teammates
- địch outlines nên được hiển thị rõ thông qua geometry from top-down camera (red silhouettes)
- UAV drone model above the battlefield nên được hiển thị rõ as a small cyan dot from max zoom
- Ghost Protocol first-shot bonus is not visually indicated to địch — incentivizes stealth play
- Scan does NOT show địch máu bars — only position outlines
