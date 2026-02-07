# Operators - Character System Overview

**[← Previous: Core Gameplay](../GameDesign/CoreGameplay.md)** | **[Index](../README.md)** | **[Next: Map Design →](../World/MapDesign.md)**

---

## Introduction

**Operators** are playable characters in **Extraction Protocol**. Each Operator belongs to a specific class that defines their role in combat, but has unique abilities, visual design, backstory, and playstyle that sets them apart.

This document serves as an **index and overview** for all Operators. For detailed information on each individual character, please refer to the linked character documents within their respective class folders.

---

## Design Philosophy

### Core Principles

| Principle               | Description                                            | Example                                  |
| :---------------------- | :----------------------------------------------------- | :--------------------------------------- |
| **Class Identity**      | Each class has a defined role                          | Tank = Damage absorption                 |
| **Character Diversity** | Multiple characters per class with different abilities | 2 Assault operators with different stims |
| **Visual Clarity**      | Instant recognition from top-down view                 | Unique silhouettes, color themes         |
| **Balanced Power**      | Abilities complement skill, not replace it             | +25% damage, not instant kill            |
| **Risk/Reward**         | Aggressive play has trade-offs                         | High damage = lower survivability        |
| **Team Synergy**        | Operators work better together                         | Healer + Tank combo                      |

### Reference Games

Our Operator design draws inspiration from:

| Game                  | Inspiration Element              | Our Implementation       |
| :-------------------- | :------------------------------- | :----------------------- |
| **Rainbow Six Siege** | Unique gadgets per operator      | Active abilities         |
| **Apex Legends**      | Passive + Active ability combo   | Dual ability system      |
| **The Finals**        | Class-based team dynamics        | 5 core classes           |
| **Valorant**          | Ability cooldowns, not resources | Cooldown-based abilities |
| **Tarkov**            | High-stakes, tactical gameplay   | Extraction focus         |

---

## Operator Classes

### Class Overview Matrix

| Class                           | Role                | Primary Stat  | Team Value | Solo Viability | Operators |
| :------------------------------ | :------------------ | :------------ | :--------- | :------------- | :-------- |
| [**ASSAULT**](./Assault/)       | Frontline Aggressor | Damage        | ★★★☆☆      | ★★★★☆          | 3         |
| [**SUPPORT**](./Support/)       | Team Healer         | Healing       | ★★★★★      | ★★☆☆☆          | 2         |
| [**RECON**](./Recon/)           | Intel Specialist    | Information   | ★★★★☆      | ★★★★★          | 3         |
| [**TANK**](./Tank/)             | Damage Sponge       | Survivability | ★★★★☆      | ★★★☆☆          | 2         |
| [**SPECIALIST**](./Specialist/) | Tech Disruptor      | Utility       | ★★★★☆      | ★★★★☆          | 2         |

### Unlock Progression

```
ACCOUNT LEVEL 1  → Assault (VIPER) - Free starter
ACCOUNT LEVEL 1  → Support (DOC) - Free starter
ACCOUNT LEVEL 5  → Assault (BLAZE) - 5,000 Credits or Quest
ACCOUNT LEVEL 8  → Recon (PHANTOM) - 5,000 Credits or Quest
ACCOUNT LEVEL 10 → Tank (BULWARK) - 7,500 Credits or Quest
ACCOUNT LEVEL 12 → Recon (SPECTER) - 7,500 Credits or Quest
ACCOUNT LEVEL 15 → Specialist (CIPHER) - 10,000 Credits or Quest
ACCOUNT LEVEL 18 → Support (ANGEL) - 10,000 Credits or Quest
ACCOUNT LEVEL 20 → Tank (FORTRESS) - 12,000 Credits or Quest
ACCOUNT LEVEL 22 → Assault (HAVOC) - 12,000 Credits or Quest
ACCOUNT LEVEL 25 → Recon (WRAITH) - 15,000 Credits or Quest
ACCOUNT LEVEL 28 → Specialist (FLUX) - 15,000 Credits or Quest
```

---

## Class Details

### 1. ASSAULT CLASS - "Frontline Aggressors"

**Role:** High damage dealers who lead the charge into combat.

**Class Traits:**
- +10% Base Sprint Speed
- +5% Weapon Damage
- -10% Maximum Armor

**Operators:**

| Operator                                       | Codename | Ability         | Specialty            |
| :--------------------------------------------- | :------- | :-------------- | :------------------- |
| [**Marcus "Viper" Chen**](./Assault/Viper.md)  | VIPER    | Combat Stim     | Damage Amplification |
| [**Elena "Blaze" Reyes**](./Assault/Blaze.md)  | BLAZE    | Incendiary Rush | Area Denial          |
| [**Anton "Havoc" Petrov**](./Assault/Havoc.md) | HAVOC    | Berserker Rage  | Close Combat         |

📁 **[View All Assault Operators →](./Assault/)**

---

### 2. SUPPORT CLASS - "Team Lifelines"

**Role:** Keep teammates alive and enable sustained combat.

**Class Traits:**
- +20% Healing Item Effectiveness
- +15% Revive Speed
- -5% Movement Speed

**Operators:**

| Operator                                              | Codename | Ability         | Specialty         |
| :---------------------------------------------------- | :------- | :-------------- | :---------------- |
| [**Dr. James "Doc" Morrison**](./Support/Doc.md)      | DOC      | Healing Drone   | Area Healing      |
| [**Sister Maria "Angel" Santos**](./Support/Angel.md) | ANGEL    | Guardian Shield | Damage Prevention |

📁 **[View All Support Operators →](./Support/)**

---

### 3. RECON CLASS - "Information Specialists"

**Role:** Gather intel, scout enemy positions, and enable ambushes.

**Class Traits:**
- +15% Crouch Movement Speed
- -30% Footstep Volume
- -5% Maximum Health

**Operators:**

| Operator                                          | Codename | Ability        | Specialty      |
| :------------------------------------------------ | :------- | :------------- | :------------- |
| [**Sarah "Phantom" Kim**](./Recon/Phantom.md)     | PHANTOM  | UAV Scan       | Area Reveal    |
| [**Viktor "Specter" Volkov**](./Recon/Specter.md) | SPECTER  | Motion Sensors | Trap Detection |
| [**Yuki "Wraith" Tanaka**](./Recon/Wraith.md)     | WRAITH   | Smoke Screen   | Visual Denial  |

📁 **[View All Recon Operators →](./Recon/)**

---

### 4. TANK CLASS - "Frontline Defenders"

**Role:** Absorb damage, hold positions, and protect teammates.

**Class Traits:**
- +25% Maximum Armor Capacity
- +10% Armor Damage Reduction
- -15% Sprint Speed

**Operators:**

| Operator                                           | Codename | Ability          | Specialty          |
| :------------------------------------------------- | :------- | :--------------- | :----------------- |
| [**Hans "Bulwark" Richter**](./Tank/Bulwark.md)    | BULWARK  | Riot Shield      | Frontal Protection |
| [**Dmitri "Fortress" Kozlov**](./Tank/Fortress.md) | FORTRESS | Armor Overcharge | Team Defense       |

📁 **[View All Tank Operators →](./Tank/)**

---

### 5. SPECIALIST CLASS - "Tech Disruptors"

**Role:** Utility, control, counter enemy abilities.

**Class Traits:**
- +2 Inventory Slots
- +20% Gadget Interaction Speed
- -10% Weapon Accuracy

**Operators:**

| Operator                                             | Codename | Ability    | Specialty      |
| :--------------------------------------------------- | :------- | :--------- | :------------- |
| [**Alex "Cipher" Nakamura**](./Specialist/Cipher.md) | CIPHER   | EMP Blast  | Ability Denial |
| [**Maya "Flux" Okonkwo**](./Specialist/Flux.md)      | FLUX     | Nano Swarm | Area Control   |

📁 **[View All Specialist Operators →](./Specialist/)**

---

## Operator Balance Matrix

### Combat Statistics

| Operator | Class      | Combat Power | Survivability | Utility | Team Value | Solo Viability |
| :------- | :--------- | :----------: | :-----------: | :-----: | :--------: | :------------: |
| VIPER    | Assault    |     9/10     |     6/10      |  4/10   |    6/10    |      8/10      |
| BLAZE    | Assault    |     8/10     |     5/10      |  6/10   |    7/10    |      7/10      |
| HAVOC    | Assault    |    10/10     |     4/10      |  3/10   |    5/10    |      9/10      |
| DOC      | Support    |     5/10     |     7/10      |  8/10   |   10/10    |      4/10      |
| ANGEL    | Support    |     4/10     |     8/10      |  9/10   |   10/10    |      3/10      |
| PHANTOM  | Recon      |     6/10     |     5/10      |  9/10   |    8/10    |      9/10      |
| SPECTER  | Recon      |     7/10     |     5/10      |  8/10   |    7/10    |      8/10      |
| WRAITH   | Recon      |     5/10     |     6/10      |  10/10  |    8/10    |      7/10      |
| BULWARK  | Tank       |     7/10     |     10/10     |  5/10   |    8/10    |      5/10      |
| FORTRESS | Tank       |     6/10     |     9/10      |  7/10   |    9/10    |      4/10      |
| CIPHER   | Specialist |     5/10     |     6/10      |  10/10  |    7/10    |      7/10      |
| FLUX     | Specialist |     6/10     |     5/10      |  9/10   |    8/10    |      6/10      |

### Counter Matrix

| Operator | Strong Against   | Weak Against    |
| :------- | :--------------- | :-------------- |
| VIPER    | PHANTOM, DOC     | BULWARK, CIPHER |
| BLAZE    | WRAITH, FORTRESS | SPECTER, FLUX   |
| HAVOC    | ANGEL, CIPHER    | BULWARK, DOC    |
| DOC      | All (Sustain)    | VIPER, HAVOC    |
| ANGEL    | BLAZE, HAVOC     | CIPHER, SPECTER |
| PHANTOM  | FORTRESS, FLUX   | VIPER, WRAITH   |
| SPECTER  | BLAZE, HAVOC     | CIPHER, ANGEL   |
| WRAITH   | BULWARK, VIPER   | PHANTOM, FLUX   |
| BULWARK  | VIPER, HAVOC     | WRAITH, CIPHER  |
| FORTRESS | BLAZE, SPECTER   | PHANTOM, FLUX   |
| CIPHER   | ANGEL, BULWARK   | VIPER, HAVOC    |
| FLUX     | PHANTOM, SPECTER | BLAZE, WRAITH   |

---

## Team Compositions

### Recommended Squad Compositions (3-Player)

| Comp Name           | Composition                | Playstyle             | Strength               |
| :------------------ | :------------------------- | :-------------------- | :--------------------- |
| **Rush Meta**       | VIPER + HAVOC + DOC        | Aggressive push       | High damage, sustained |
| **Intel Control**   | PHANTOM + SPECTER + CIPHER | Information dominance | Never surprised        |
| **Fortress Hold**   | BULWARK + DOC + BLAZE      | Defensive extraction  | Hard to push           |
| **Balanced**        | VIPER + DOC + PHANTOM      | All-around            | Flexible               |
| **Stealth Extract** | WRAITH + SPECTER + FLUX    | Avoid combat          | Maximum loot           |

### Duo Synergies

| Duo              | Synergy                     | Strategy                |
| :--------------- | :-------------------------- | :---------------------- |
| VIPER + DOC      | Assault heals               | Aggressive with sustain |
| BULWARK + HAVOC  | Tank leads, Assault follows | Overwhelming push       |
| PHANTOM + CIPHER | Intel + Disable             | Information control     |
| FORTRESS + ANGEL | Double defense              | Extraction fortress     |
| WRAITH + SPECTER | Stealth duo                 | Avoid all combat        |

---

## Operator Progression

### Individual Leveling

**Max Level per Operator:** 50

| Level | Unlock                          |
| :---- | :------------------------------ |
| 1     | Base operator unlocked          |
| 5     | Ability Upgrade Slot 1          |
| 10    | Cosmetic Skin 1                 |
| 15    | Stat Boost 1 (+5% Health)       |
| 20    | Ability Upgrade Slot 2          |
| 25    | Cosmetic Skin 2                 |
| 30    | Stat Boost 2 (+5% Stamina)      |
| 35    | Ability Upgrade Slot 3          |
| 40    | Elite Cosmetic Skin             |
| 45    | Stat Boost 3 (+5% Sprint Speed) |
| 50    | Prestige Cosmetics + Title      |

### Prestige System

After reaching Level 50, operators can be **Prestiged**:
- Reset to Level 1
- Gain Prestige Badge (visible to other players)
- Unlock exclusive Prestige cosmetics
- +5% XP bonus for that operator
- Max Prestige: 5

---

## Cosmetic System

### Customization Options

| Type             | Description                   | Acquisition                  |
| :--------------- | :---------------------------- | :--------------------------- |
| **Skins**        | Full operator visual change   | Credits, Battle Pass, Events |
| **Headgear**     | Helmets, hats, masks          | Credits, Battle Pass         |
| **Gloves**       | Hand cosmetics                | Credits only                 |
| **Weapon Skins** | Applied to equipped weapons   | Credits, Battle Pass         |
| **Emotes**       | Victory poses, taunts         | Battle Pass, Events          |
| **Kill Effects** | Visual effect on eliminations | Premium Currency only        |
| **Voice Packs**  | Alternate voice lines         | Premium Currency only        |

### Rarity Tiers

| Tier      | Color  | Drop Rate | Purchase Price       |
| :-------- | :----- | :-------- | :------------------- |
| Common    | White  | 60%       | 500 Credits          |
| Uncommon  | Green  | 25%       | 1,000 Credits        |
| Rare      | Blue   | 10%       | 2,500 Credits        |
| Epic      | Purple | 4%        | Premium only         |
| Legendary | Gold   | 1%        | Battle Pass / Events |

---

## Future Operators (Roadmap)

### Season 1 (Launch + 3 months)

| Operator     | Class      | Ability Preview    |
| :----------- | :--------- | :----------------- |
| **SHADOW**   | Recon      | Invisibility cloak |
| **ENGINEER** | Specialist | Deployable turret  |

### Season 2 (6 months)

| Operator  | Class   | Ability Preview        |
| :-------- | :------ | :--------------------- |
| **PYRO**  | Assault | Fire damage specialist |
| **MERCY** | Support | Mass revive            |

### Season 3+ (9 months+)

- New class consideration: **COMMANDER** (tactical calldowns)
- Community-voted operator concepts
- Crossover event operators (licensed characters)

---

## Document Index

### Assault Class

| File                           | Operator             | Status     |
| :----------------------------- | :------------------- | :--------- |
| [Viper.md](./Assault/Viper.md) | Marcus "Viper" Chen  | ✅ Complete |
| [Blaze.md](./Assault/Blaze.md) | Elena "Blaze" Reyes  | ✅ Complete |
| [Havoc.md](./Assault/Havoc.md) | Anton "Havoc" Petrov | ✅ Complete |

### Support Class

| File                           | Operator                    | Status     |
| :----------------------------- | :-------------------------- | :--------- |
| [Doc.md](./Support/Doc.md)     | Dr. James "Doc" Morrison    | ✅ Complete |
| [Angel.md](./Support/Angel.md) | Sister Maria "Angel" Santos | ✅ Complete |

### Recon Class

| File                             | Operator                | Status     |
| :------------------------------- | :---------------------- | :--------- |
| [Phantom.md](./Recon/Phantom.md) | Sarah "Phantom" Kim     | ✅ Complete |
| [Specter.md](./Recon/Specter.md) | Viktor "Specter" Volkov | ✅ Complete |
| [Wraith.md](./Recon/Wraith.md)   | Yuki "Wraith" Tanaka    | ✅ Complete |

### Tank Class

| File                              | Operator                 | Status     |
| :-------------------------------- | :----------------------- | :--------- |
| [Bulwark.md](./Tank/Bulwark.md)   | Hans "Bulwark" Richter   | ✅ Complete |
| [Fortress.md](./Tank/Fortress.md) | Dmitri "Fortress" Kozlov | ✅ Complete |

### Specialist Class

| File                                | Operator               | Status     |
| :---------------------------------- | :--------------------- | :--------- |
| [Cipher.md](./Specialist/Cipher.md) | Alex "Cipher" Nakamura | ✅ Complete |
| [Flux.md](./Specialist/Flux.md)     | Maya "Flux" Okonkwo    | ✅ Complete |

---

**[← Previous: Core Gameplay](../GameDesign/CoreGameplay.md)** | **[Index](../README.md)** | **[Next: Map Design →](../World/MapDesign.md)**
