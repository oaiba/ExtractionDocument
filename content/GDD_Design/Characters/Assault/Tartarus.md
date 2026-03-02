---
title: "TARTARUS - Carlos Mendes"
type: docs
---

## Operator Profile

> *"Hesitation is death. I choose violence."*

### Basic Information

| Attribute       | Value                     |
| :-------------- | :------------------------ |
| **Real Name**   | Carlos Mendes             |
| **Codename**    | TARTARUS                  |
| **Class**       | Assault                   |
| **Nationality** | Brazilian                 |
| **Age**         | 38                        |
| **Height**      | 191 cm (6'3")             |
| **Weight**      | 98 kg (216 lbs)           |

<!-- REF_IMAGE: TARTARUS operator portrait — massive scar on face, thick spetsnaz armor, heavy shotgun, berserker rage visible in eyes -->

### Background

Carlos Mendes was a legendary figure in Brazil's BOPE before a failed operation left him the sole survivor of his unit. Blamed for the disaster by corrupt superiors, he was dishonorably discharged and erased from official records.

For years, Carlos wandered as a mercenary, his reputation growing as a one-man wrecking crew. He doesn't seek teammates - he seeks targets. The Exclusion Zone is just another battlefield, and Carlos has never lost a fight he started.

### Personality Traits

- **Brutal** - No mercy, no hesitation
- **Solitary** - Prefers working alone
- **Haunted** - Lost his whole squad, carries survivor's guilt
- **Respectful** - Honors worthy opponents

---

## Combat Statistics

### Base Stats

| Stat             | Value   | Class Modifier | Final    |
| :--------------- | :------ | :------------- | :------- |
| **Health**       | 100 HP  | -              | 100 HP   |
| **Armor**        | 50      | -10%           | 45       |
| **Sprint Speed** | 5.5 m/s | +10%           | 6.05 m/s |
| **Walk Speed**   | 3.5 m/s | -              | 3.5 m/s  |
| **Crouch Speed** | 2.0 m/s | -              | 2.0 m/s  |

### Damage Modifiers

| Condition                | Modifier                |
| :----------------------- | :---------------------- |
| Base Weapon Damage       | +5% (Class)             |
| Berserker Active         | +35% melee, +15% weapon |
| Berserker + Kill         | Refreshes duration      |
| Melee Damage (Base)      | 50                      |
| Melee Damage (Berserker) | 67                      |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 120 | +20% (Assault class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8.8/second | +10% (Assault class) |
| **Net Sprint Duration** | 12.0 seconds | Longest sprint tier |
| **Footstep Volume** | 110% | Slightly louder — heavy build |
| **Ability Audio Radius** | 50 meters | Rage roar is the loudest activation in the game |
| **Melee Lunge Range** | 3.5 meters | Extended melee lunge during Berserker Rage |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration — critical vulnerability |
| Slow | 0% | Full duration — devastating during Rage |
| Burn | 0% | Full DoT |
| EMP | 0% | Rage cancelled immediately by EMP |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 44 cm radius, 190 cm height |
| **Head Sphere** | 15 cm radius |
| **Collision Profile** | Standard (largest among Assault) |
| **Silhouette From Above** | Broad-shouldered, aggressive stance, largest Assault operator |
| **Class Accent Zones** | Orange (#F97316) + Red (#DC2626) during Rage |
| **Rage Active VFX (Top-Down)** | Red pulsing glow on body, wider aggressive stance, ground crack effects on melee |
| **Melee VFX (Top-Down)** | Red arc slash visible on ground plane, 3.5m range |
| **Rage Audio Radius** | 50m — loudest ability activation in roster |

<!-- REF_IMAGE: TARTARUS top-down view — showing operator in normal vs Berserker Rage stance from above, red glow and melee range arc visible -->

### Difficulty Rating

**Difficulty: 4/5** — High risk/reward. Must close distance without dying, manage kill chain timer, and accept +10% incoming damage. Requires aggressive confidence.


## Abilities

### Active Ability: Berserker Rage

> *"Enter a frenzy state. Each kill extends the rage."*

| Property         | Value               |
| :--------------- | :------------------ |
| **Cooldown**     | 100 seconds         |
| **Duration**     | 8 seconds (base)    |
| **Extension**    | +3 seconds per kill |
| **Max Duration** | 20 seconds          |

#### Effects

| Effect         | Value  | Notes                 |
| :------------- | :----- | :-------------------- |
| Melee Damage   | +35%   | Makes melee viable    |
| Weapon Damage  | +15%   | Less than MAMBA stim  |
| Movement Speed | +15%   | All movement types    |
| Damage Taken   | +10%   | Trade-off             |
| Kill Extension | +3 sec | Encourages aggression |

#### Ability Interactions

| Interaction | Result |
| :---------- | :----- |
| **Rage + EMP** | Rage cancelled immediately, kill chain timer lost |
| **Rage + Stun** | Full stun duration — wastes precious Rage seconds |
| **Rage + AEGIS Shield** | TARTARUS melee CAN push through Guardian Shield |
| **Rage + BASTION Shield** | Melee bash staggers shield (1s), does not break through |
| **Rage + Burn** | Burn damage stacks with +10% incoming damage modifier |
| **Rage + Kill (SONAR scanned target)** | Kill still extends duration even if target was scanned |

#### Top-Down Rage VFX

| State | VFX From Above |
| :---- | :------------- |
| Rage activation | Red flash burst from operator, ground cracks radiate outward (1m) |
| Rage active | Persistent red body glow, widened stance animation |
| Melee swing | Red arc slash on ground (3.5m forward cone) |
| Kill chain (kill during rage) | Brief bright flash + timer refresh indicator |
| Rage ending | Glow dims, operator visibly exhales (hunched posture) |


**Self:**
- Screen pulses red
- Heavy breathing audio
- Blood splatter on screen edges

**Enemy Perspective:**
- Red glow around Tartarus
- Audible roar on activation
- Movements appear more aggressive

#### Kill Chain Mechanic

The unique aspect of Berserker Rage is the **kill extension**:

```
Base activation: 8 seconds
Kill 1: 8 + 3 = 11 seconds remaining
Kill 2: 11 + 3 = 14 seconds remaining
Kill 3: 14 + 3 = 17 seconds remaining
Kill 4+: Capped at 20 seconds
```

**Design Intent:** High risk, potentially infinite uptime if you're skilled enough.

#### Upgrade Slots

**Slot 1 (Level 5):**
| Option           | Effect                                       |
| :--------------- | :------------------------------------------- |
| **Blood Frenzy** | Kill extension +2 seconds (5 total per kill) |
| **Quick Rage**   | Cooldown -20 seconds (80s total)             |
| **Iron Will**    | Damage taken penalty removed                 |

**Slot 2 (Level 20):**
| Option                | Effect                                        |
| :-------------------- | :-------------------------------------------- |
| **Executioner**       | Melee kills heal 20 HP                        |
| **Unstoppable Force** | Immune to knockback/stun                      |
| **Terror**            | Nearby enemies hear heartbeat (psychological) |

**Slot 3 (Level 35):**
| Option         | Effect                                            |
| :------------- | :------------------------------------------------ |
| **Last Stand** | If killed during rage, explode for 50 area damage |
| **Rampage**    | Each kill also reduces cooldown by 5 seconds      |
| **Predator**   | Damaged enemies are marked for 5 seconds          |

---

### Passive Ability: Bloodlust

> *"The closer to death, the stronger he becomes."*

| Health Threshold | Effect                            |
| :--------------- | :-------------------------------- |
| Below 50%        | +10% weapon damage                |
| Below 30%        | +15% weapon damage, +5% movement  |
| Below 15%        | +20% weapon damage, +10% movement |

**Synergy with Berserker:** Combined with rage mode at low health = devastating damage output.

**Design Intent:** Makes TARTARUS terrifying when cornered. Never assume a low-health TARTARUS is easy.

---

## Loadout

### Default Loadout

| Slot          | Item            | Notes               |
| :------------ | :-------------- | :------------------ |
| **Primary**   | SPAS-12 Shotgun | CQB dominance       |
| **Secondary** | Desert Eagle    | High damage backup  |
| **Tactical**  | Flashbang ×2    | Entry tool          |
| **Armor**     | Medium Vest     | 50 armor points     |
| **Melee**     | Combat Knife    | Enhanced by passive |

### Recommended Loadouts

**Full Berserker:**
| Slot      | Item               | Why                |
| :-------- | :----------------- | :----------------- |
| Primary   | AA-12 Auto Shotgun | Spray and pray     |
| Secondary | Revolver           | One-shot potential |
| Tactical  | Stun Grenade ×2    | Close the gap      |
| Melee     | Machete            | Higher base damage |

**Controlled Aggression:**
| Slot      | Item                   | Why                     |
| :-------- | :--------------------- | :---------------------- |
| Primary   | UMP-45 SMG             | More range than shotgun |
| Secondary | G17                    | Reliable backup         |
| Tactical  | Flashbang ×1, Smoke ×1 | Entry + escape          |

---

## Playstyle Guide

### Role in Team

**Primary Role:** CQB Specialist
- Dominates close quarters
- Clears rooms aggressively
- Terrifies enemies in tight spaces

**Secondary Role:** Finisher
- Chase down wounded enemies
- Capitalize on team damage
- Execute distracted targets

### Combat Loop

```
1. Get close (use cover, flanks, smoke)
2. Activate Berserker Rage
3. Engage closest enemy
4. Secure kill -> Duration extends
5. Immediately move to next target
6. Chain kills to maintain rage
7. If no kills in 8 seconds, retreat
```

### Close Quarters Dominance

**Best Engagement Range:** 0-10 meters

| Range  | Tactic                              |
| :----- | :---------------------------------- |
| 0-3m   | Melee or shotgun                    |
| 3-10m  | Shotgun or SMG                      |
| 10-20m | SMG only, don't engage if avoidable |
| 20m+   | Disengage, reposition               |

### When NOT to Pick TARTARUS

- Long-range maps (open areas)
- Enemy team has multiple Tanks
- Your team has no healer
- You're not confident in CQB

---

## Matchups

### Favorable Matchups

| Opponent    | Why Favorable           | Tactic                    |
| :---------- | :---------------------- | :------------------------ |
| **SUTURE**     | Fragile up close        | Rush before drone deploys |
| **SONAR** | No combat advantage     | Close distance fast       |
| **GLITCH**  | Low combat stats        | Overwhelm with aggression |
| **AEGIS**   | Can't escape your speed | Push through shield       |

### Even Matchups

| Opponent    | Notes                         | Key to Winning           |
| :---------- | :---------------------------- | :----------------------- |
| **MAMBA**   | Both aggressive, comes to aim | Land first shot          |
| **IGNITION**   | Fire vs Rage                  | Avoid fire while closing |
| **MIRAGE** | Traps slow you down           | Clear traps, then push   |

### Unfavorable Matchups

| Opponent     | Why Difficult                 | Counter Strategy        |
| :----------- | :---------------------------- | :---------------------- |
| **BASTION**  | Shield completely blocks you  | Flank only, never front |
| **GOLIATH** | Team armor absorbs your burst | Focus teammates first   |
| **PULSE**     | Nano swarm slows you          | Wait for swarm to end   |

---

## Voice Lines

### Combat

| Trigger                  | Line                       |
| :----------------------- | :------------------------- |
| Ability Activation       | *War cry in Russian*       |
| Ability Activation (Alt) | "Now you die!"             |
| Kill                     | "Pathetic."                |
| Kill (Melee)             | "Too slow."                |
| Kill Chain (3+)          | "Who's next?!"             |
| Low Health               | "You think this stops me?" |
| Reviving                 | "Get up. We're not done."  |

### Callouts

| Trigger       | Line                |
| :------------ | :------------------ |
| Enemy Spotted | "Contact."          |
| Pushing       | "Moving in."        |
| Taking Fire   | "They are nothing." |
| Reloading     | "Reloading."        |
| Grenade       | "Grenade."          |

### Personality

| Trigger            | Line                           |
| :----------------- | :----------------------------- |
| Match Start        | "Let's finish this quickly."   |
| Extraction Called  | "Cover me. We leave now."      |
| Extraction Success | "Another day survived."        |
| Squad Wipe         | "That was almost challenging." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Dark gray tactical sweater, black vest
- **Headgear:** Black balaclava
- **Gloves:** Worn leather combat gloves
- **Face:** Heavy scarring, cold blue eyes

### Unlockable Skins

| Skin            | Rarity    | Unlock               |
| :-------------- | :-------- | :------------------- |
| **Winter Wolf** | Common    | Level 10             |
| **Blood Red**   | Uncommon  | 1,000 Credits        |
| **Spetsnaz**    | Rare      | Level 25             |
| **Executioner** | Epic      | Battle Pass S2       |
| **Reaper**      | Legendary | Ranked Season Reward |

### Signature Items

| Item                | Description                           |
| :------------------ | :------------------------------------ |
| **Dog Tags**        | Collection from fallen squad (hidden) |
| **Scar Pattern**    | Distinctive slash marks on face       |
| **Knuckle Tattoos** | Cyrillic letters spelling "DEATH"     |

---

## Lore Connections

### Relationships

| Character    | Relationship                         |
| :----------- | :----------------------------------- |
| **MAMBA**    | Mutual respect between soldiers      |
| **GOLIATH** | Former comrade from Russian military |
| **BASTION**  | Considers him a worthy opponent      |
| **IGNITION**    | Kindred spirit in chaos              |

### Story Hooks

- Seeking the general who ordered his squad's sacrifice
- Has bounty on his head from Russian intelligence
- Protects new operators from making his mistakes

---

## Design Notes (For Developers)

### Balance Considerations

- Extremely high risk, high reward
- Damage taken penalty balances damage output
- Kill chain mechanic rewards skill
- CQB focus limits map versatility

### Animation Requirements

- Rage activation: Shoulder roll + crack neck
- Movement during rage: More aggressive posture
- Melee attacks: Heavy, brutal swings
- Death: Falls to knees first, then forward

### Technical Notes

| System          | Notes                                  |
| :-------------- | :------------------------------------- |
| Kill Extension  | Server calculates, syncs to client     |
| Duration Timer  | Visible to player, hidden from enemies |
| Damage Modifier | Applies before armor calculation       |
| Sounds          | Rage growl synced to all players       |

### Top-Down Specific Notes

- Rage red glow must be visible at minimum zoom — brightest self-buff VFX in the game
- Melee lunge animation from top-down should show clear forward movement (3.5m)
- Melee arc VFX on ground plane helps teammates and enemies judge range
- Kill chain timer is intentionally hidden from enemies to prevent them timing disengagements
- +10% incoming damage during Rage means TARTARUS drops faster — encourage burst or kiting counterplay
