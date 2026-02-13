---
title: "Characters & Operators"
linkTitle: "Characters"
type: docs
weight: 3
sidebar:
  open: true
---

## The Squad Hierarchy

In **Extraction Shooter**, characters are defined not just by stats, but by their tactical utility in a squad. While every operator can shoot and loot, their unique abilities define the flow of combat.

> [!NOTE]
> **Philosophy:** No "DPS" or "Tank" in the traditional MMO sense. Every bullet is lethal. Roles provide *utility* and *sustain*, not invincibility.

### Class Roster

{{< cards cols="3" >}}
  {{< card link="Assault/" title="Assault" icon="fire" subtitle="Fraggers. Breachers. Frontline engage." >}}
  {{< card link="Recon/" title="Recon" icon="eye" subtitle="Intel gathering. Sniping. Flanking." >}}
  {{< card link="Support/" title="Support" icon="plus-circle" subtitle="Healing. Ammo resupply. Utility." >}}
  {{< card link="Tank/" title="Tank" icon="shield-check" subtitle="Area denial. Heavy weapons. Crowd control." >}}
  {{< card link="Specialist/" title="Specialist" icon="chip" subtitle="Cyberwarfare. Traps. Gadgets." >}}
{{< /cards >}}

---

## Design Philosophy

### Core Principles

| Principle | Description | Example |
| :-------- | :---------- | :------ |
| **Class Identity** | Each class has a defined combat role | Tank = Damage absorption |
| **Character Diversity** | Multiple characters per class with different abilities | 2 Assault operators with different stims |
| **Visual Clarity** | Instant recognition from top-down view | Unique silhouettes, color themes (see [Art Direction](../Visuals/ArtDirection/)) |
| **Balanced Power** | Abilities complement skill, not replace it | +25% damage, not instant kill |
| **Risk/Reward** | Aggressive play has trade-offs | High damage = lower survivability |
| **Team Synergy** | Operators work better together | Healer + Tank combo |

### Reference Games

Our Operator design draws inspiration from:

| Game | Inspiration Element | Our Implementation |
| :--- | :------------------ | :----------------- |
| **Rainbow Six Siege** | Unique gadgets per operator | Active abilities with upgrade paths |
| **Apex Legends** | Passive + Active ability combo | Dual ability system |
| **The Finals** | Class-based team dynamics (Light/Medium/Heavy) | 5 core classes with distinct roles |
| **Valorant** | Ability cooldowns, weapon-first balance | Cooldown-based abilities, gunplay matters more than powers |
| **Tarkov** | High-stakes, tactical gameplay, gear fear | Extraction focus, gear loss on death |
| **Hunt Showdown** | Trait system, information warfare | Passive abilities, audio-driven gameplay |

<!-- REF_IMAGE: Operator roster silhouette lineup — all 12 operators arranged by class with color-coded backgrounds matching faction/class identity -->

---

## Operator Classes

### Class Overview Matrix

| Class | Role | Primary Stat | Team Value | Solo Viability | Operators |
| :---- | :--- | :----------- | :--------- | :------------- | :-------- |
| [**ASSAULT**](./Assault/) | Frontline Aggressor | Damage | Medium | High | 3 |
| [**SUPPORT**](./Support/) | Team Healer | Healing | Very High | Low | 2 |
| [**RECON**](./Recon/) | Intel Specialist | Information | High | Very High | 3 |
| [**TANK**](./Tank/) | Damage Sponge | Survivability | High | Medium | 2 |
| [**SPECIALIST**](./Specialist/) | Tech Disruptor | Utility | High | High | 2 |

### Unlock Progression

```
ACCOUNT LEVEL 1  -> Assault (VIPER) - Free starter
ACCOUNT LEVEL 1  -> Support (DOC) - Free starter
ACCOUNT LEVEL 5  -> Assault (BLAZE) - 5,000 Credits or Quest
ACCOUNT LEVEL 8  -> Recon (PHANTOM) - 5,000 Credits or Quest
ACCOUNT LEVEL 10 -> Tank (BULWARK) - 7,500 Credits or Quest
ACCOUNT LEVEL 12 -> Recon (SPECTER) - 7,500 Credits or Quest
ACCOUNT LEVEL 15 -> Specialist (CIPHER) - 10,000 Credits or Quest
ACCOUNT LEVEL 18 -> Support (ANGEL) - 10,000 Credits or Quest
ACCOUNT LEVEL 20 -> Tank (FORTRESS) - 12,000 Credits or Quest
ACCOUNT LEVEL 22 -> Assault (HAVOC) - 12,000 Credits or Quest
ACCOUNT LEVEL 25 -> Recon (WRAITH) - 15,000 Credits or Quest
ACCOUNT LEVEL 28 -> Specialist (FLUX) - 15,000 Credits or Quest
```

**Design Intent:** Starter operators (VIPER, DOC) represent the two core loops — killing and surviving. New classes unlock steadily to introduce complexity without overwhelming new players.

---

## Class Details

### 1. ASSAULT CLASS — Frontline Aggressors

**Role:** High damage dealers who lead the charge into combat.

**Class Traits:**
- +10% Base Sprint Speed
- +5% Weapon Damage
- -10% Maximum Armor

**Operators:**

| Operator | Codename | Ability | Specialty |
| :------- | :------- | :------ | :-------- |
| [Marcus "Viper" Chen](./Assault/Viper/) | VIPER | Combat Stim | Damage Amplification |
| [Elena "Blaze" Reyes](./Assault/Blaze/) | BLAZE | Incendiary Rush | Area Denial |
| [Anton "Havoc" Petrov](./Assault/Havoc/) | HAVOC | Berserker Rage | Close Combat |

[View All Assault Operators](./Assault/)

---

### 2. SUPPORT CLASS — Team Lifelines

**Role:** Keep teammates alive and enable sustained combat.

**Class Traits:**
- +20% Healing Item Effectiveness
- +15% Revive Speed
- -5% Movement Speed

**Operators:**

| Operator | Codename | Ability | Specialty |
| :------- | :------- | :------ | :-------- |
| [Dr. James "Doc" Morrison](./Support/Doc/) | DOC | Healing Drone | Area Healing |
| [Sister Maria "Angel" Santos](./Support/Angel/) | ANGEL | Guardian Shield | Damage Prevention |

[View All Support Operators](./Support/)

---

### 3. RECON CLASS — Information Specialists

**Role:** Gather intel, scout enemy positions, and enable ambushes.

**Class Traits:**
- +15% Crouch Movement Speed
- -30% Footstep Volume
- -5% Maximum Health

**Operators:**

| Operator | Codename | Ability | Specialty |
| :------- | :------- | :------ | :-------- |
| [Sarah "Phantom" Kim](./Recon/Phantom/) | PHANTOM | UAV Scan | Area Reveal |
| [Viktor "Specter" Volkov](./Recon/Specter/) | SPECTER | Motion Sensors | Trap Detection |
| [Yuki "Wraith" Tanaka](./Recon/Wraith/) | WRAITH | Smoke Screen | Visual Denial |

[View All Recon Operators](./Recon/)

---

### 4. TANK CLASS — Frontline Defenders

**Role:** Absorb damage, hold positions, and protect teammates.

**Class Traits:**
- +25% Maximum Armor Capacity
- +10% Armor Damage Reduction
- -15% Sprint Speed

**Operators:**

| Operator | Codename | Ability | Specialty |
| :------- | :------- | :------ | :-------- |
| [Hans "Bulwark" Richter](./Tank/Bulwark/) | BULWARK | Riot Shield | Frontal Protection |
| [Dmitri "Fortress" Kozlov](./Tank/Fortress/) | FORTRESS | Armor Overcharge | Team Defense |

[View All Tank Operators](./Tank/)

---

### 5. SPECIALIST CLASS — Tech Disruptors

**Role:** Utility, control, counter enemy abilities.

**Class Traits:**
- +2 Inventory Slots
- +20% Gadget Interaction Speed
- -10% Weapon Accuracy

**Operators:**

| Operator | Codename | Ability | Specialty |
| :------- | :------- | :------ | :-------- |
| [Alex "Cipher" Nakamura](./Specialist/Cipher/) | CIPHER | EMP Blast | Ability Denial |
| [Maya "Flux" Okonkwo](./Specialist/Flux/) | FLUX | Nano Swarm | Area Control |

[View All Specialist Operators](./Specialist/)

---

## Operator Balance Matrix

### Combat Statistics

| Operator | Class | Combat Power | Survivability | Utility | Team Value | Solo Viability |
| :------- | :---- | :----------: | :-----------: | :-----: | :--------: | :------------: |
| VIPER | Assault | 9/10 | 6/10 | 4/10 | 6/10 | 8/10 |
| BLAZE | Assault | 8/10 | 5/10 | 6/10 | 7/10 | 7/10 |
| HAVOC | Assault | 10/10 | 4/10 | 3/10 | 5/10 | 9/10 |
| DOC | Support | 5/10 | 7/10 | 8/10 | 10/10 | 4/10 |
| ANGEL | Support | 4/10 | 8/10 | 9/10 | 10/10 | 3/10 |
| PHANTOM | Recon | 6/10 | 5/10 | 9/10 | 8/10 | 9/10 |
| SPECTER | Recon | 7/10 | 5/10 | 8/10 | 7/10 | 8/10 |
| WRAITH | Recon | 5/10 | 6/10 | 10/10 | 8/10 | 7/10 |
| BULWARK | Tank | 7/10 | 10/10 | 5/10 | 8/10 | 5/10 |
| FORTRESS | Tank | 6/10 | 9/10 | 7/10 | 9/10 | 4/10 |
| CIPHER | Specialist | 5/10 | 6/10 | 10/10 | 7/10 | 7/10 |
| FLUX | Specialist | 6/10 | 5/10 | 9/10 | 8/10 | 6/10 |

**Balance Philosophy:** No operator should exceed 8/10 in more than two categories. Total score across all categories should fall within 32-36 points to maintain parity. See [Gameplay Balance](../Gameplay/) for detailed tuning rules.

### Counter Matrix

| Operator | Strong Against | Weak Against |
| :------- | :------------- | :----------- |
| VIPER | PHANTOM, DOC | BULWARK, CIPHER |
| BLAZE | WRAITH, FORTRESS | SPECTER, FLUX |
| HAVOC | ANGEL, CIPHER | BULWARK, DOC |
| DOC | All (Sustain) | VIPER, HAVOC |
| ANGEL | BLAZE, HAVOC | CIPHER, SPECTER |
| PHANTOM | FORTRESS, FLUX | VIPER, WRAITH |
| SPECTER | BLAZE, HAVOC | CIPHER, ANGEL |
| WRAITH | BULWARK, VIPER | PHANTOM, FLUX |
| BULWARK | VIPER, HAVOC | WRAITH, CIPHER |
| FORTRESS | BLAZE, SPECTER | PHANTOM, FLUX |
| CIPHER | ANGEL, BULWARK | VIPER, HAVOC |
| FLUX | PHANTOM, SPECTER | BLAZE, WRAITH |

**Reading the Counter Matrix:** "Strong Against" means the operator has an inherent advantage in a 1v1 scenario due to ability matchups. Skill always matters more than counters — a skilled BULWARK can beat a WRAITH.

<!-- REF_IMAGE: Counter matrix diagram — visual web showing counter relationships with arrows, color-coded by class -->

---

## Team Compositions

### Recommended Squad Compositions (3-Player)

| Comp Name | Composition | Playstyle | Strength | Weakness |
| :-------- | :---------- | :-------- | :------- | :------- |
| **Rush Meta** | VIPER + HAVOC + DOC | Aggressive push | High damage, sustained | No intel, no area control |
| **Intel Control** | PHANTOM + SPECTER + CIPHER | Information dominance | Never surprised | Low damage output |
| **Fortress Hold** | BULWARK + DOC + BLAZE | Defensive extraction | Hard to push | Slow rotations |
| **Balanced** | VIPER + DOC + PHANTOM | All-around | Flexible | No hard counter to Tanks |
| **Stealth Extract** | WRAITH + SPECTER + FLUX | Avoid combat | Maximum loot, low risk | Loses direct fights |

### Duo Synergies

| Duo | Synergy | Strategy |
| :-- | :------ | :------- |
| VIPER + DOC | Assault heals | Aggressive pushing with sustain backup |
| BULWARK + HAVOC | Tank leads, Assault follows | Shield creates opening, HAVOC closes |
| PHANTOM + CIPHER | Intel + Disable | Full information control of engagement |
| FORTRESS + ANGEL | Double defense | Nearly unkillable extraction fortress |
| WRAITH + SPECTER | Stealth duo | Silent map traversal, avoid all combat |

---

## Operator Progression

### Individual Leveling

**Max Level per Operator:** 50

| Level | Unlock |
| :---- | :----- |
| 1 | Base operator unlocked |
| 5 | Ability Upgrade Slot 1 (choose 1 of 3 options) |
| 10 | Cosmetic Skin 1 |
| 15 | Stat Boost 1 (+5% Health) |
| 20 | Ability Upgrade Slot 2 (choose 1 of 3 options) |
| 25 | Cosmetic Skin 2 |
| 30 | Stat Boost 2 (+5% Stamina) |
| 35 | Ability Upgrade Slot 3 (choose 1 of 3 options) |
| 40 | Elite Cosmetic Skin |
| 45 | Stat Boost 3 (+5% Sprint Speed) |
| 50 | Prestige Cosmetics + Title |

### Prestige System

After reaching Level 50, operators can be **Prestiged**:
- Reset to Level 1
- Gain Prestige Badge (visible to other players in lobby and kill feed)
- Unlock exclusive Prestige cosmetics per prestige level
- +5% XP bonus for that operator (stacks per prestige)
- Max Prestige: 5

**Prestige Rewards:**

| Prestige | Reward |
| :------- | :----- |
| 1 | Bronze badge + weapon charm |
| 2 | Silver badge + unique skin |
| 3 | Gold badge + voice line pack |
| 4 | Diamond badge + animated banner |
| 5 | Obsidian badge + legendary title + unique kill effect |

---

## Cosmetic System

### Customization Options

| Type | Description | Acquisition |
| :--- | :---------- | :---------- |
| **Skins** | Full operator visual change | Credits, Battle Pass, Events |
| **Headgear** | Helmets, hats, masks | Credits, Battle Pass |
| **Gloves** | Hand cosmetics | Credits only |
| **Weapon Skins** | Applied to equipped weapons | Credits, Battle Pass |
| **Emotes** | Victory poses, taunts | Battle Pass, Events |
| **Kill Effects** | Visual effect on eliminations | Premium Currency only |
| **Voice Packs** | Alternate voice lines | Premium Currency only |

All cosmetics are purely visual — no gameplay advantage. See [Art Direction](../Visuals/ArtDirection/) for character model specifications and visual guidelines.

### Rarity Tiers

| Tier | Color | Drop Rate | Purchase Price |
| :--- | :---- | :-------- | :------------- |
| Common | Gray #9CA3AF | 60% | 500 Credits |
| Uncommon | Green #22C55E | 25% | 1,000 Credits |
| Rare | Blue #3B82F6 | 10% | 2,500 Credits |
| Epic | Purple #A855F7 | 4% | Premium only |
| Legendary | Gold #EAB308 | 1% | Battle Pass / Events |

---

## Future Operators (Roadmap)

### Season 1 (Launch + 3 months)

| Operator | Class | Ability Preview | Design Status |
| :------- | :---- | :-------------- | :------------ |
| **SHADOW** | Recon | Invisibility cloak (limited duration, breaks on fire) | Concept |
| **ENGINEER** | Specialist | Deployable turret (limited ammo, hackable by CIPHER) | Concept |

### Season 2 (6 months)

| Operator | Class | Ability Preview | Design Status |
| :------- | :---- | :-------------- | :------------ |
| **PYRO** | Assault | Fire damage specialist (upgraded Molotov, heat vision) | Concept |
| **MERCY** | Support | Mass revive (long cooldown, partial health restore) | Concept |

### Season 3+ (9 months+)

- New class consideration: **COMMANDER** (tactical calldowns — artillery markers, supply drops)
- Community-voted operator concepts (seasonal votes)
- Crossover event operators (licensed characters with unique abilities)

---

## Cross-References

| Topic | Document | What It Covers |
| :---- | :------- | :------------- |
| Character visuals | [Art Direction](../Visuals/ArtDirection/) | Operator model specs, silhouette guide, poly budgets, cyberpunk elements |
| Character style | [Style Guide](../Visuals/StyleGuide/) | Class color coding, gear layering system, top-down readability |
| Audio design | [Audio Design](../Audio/) | Voice line recording specs, combat callout systems |
| Gameplay balance | [Gameplay](../Gameplay/) | TTK, damage formulas, ability cooldown framework |
| UI representation | [HUD Design](../UI_UX/HUD_Design/) | How operators display on HUD, teammate status panels |
