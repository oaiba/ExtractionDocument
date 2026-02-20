---
title: "ANGEL - Sister Maria Santos"
type: docs
---

## Operator Profile

> *"Faith is the shield. But sometimes, you need an actual shield."*

### Basic Information

| Attribute       | Value                     |
| :-------------- | :------------------------ |
| **Real Name**   | Sister Maria Elena Santos |
| **Codename**    | ANGEL                     |
| **Class**       | Support                   |
| **Nationality** | Filipino                  |
| **Age**         | 35                        |
| **Height**      | 165 cm (5'5")             |
| **Weight**      | 58 kg (128 lbs)           |

<!-- REF_IMAGE: ANGEL operator portrait — tactical nun habit, serene expression, golden energy shield projector active -->

### Background

Maria Santos was a nun and nurse at a missionary hospital in Manila before a terrorist attack changed everything. When armed men stormed the hospital, Maria picked up a fallen soldier's weapon and held them off for three hours until reinforcements arrived, saving 47 patients and staff.

The Vatican quietly approached her afterward, offering training with Swiss Guard specialists. Now she operates as a "guardian angel" - protecting those who cannot protect themselves in the world's most dangerous places. The Exclusion Zone is simply her newest mission field.

### Personality Traits

- **Serene** - Unshakeable calm, even in combat
- **Protective** - Will die for her team without hesitation
- **Spiritual** - Sees combat as protection, not violence
- **Humble** - Never takes credit for saves

---

## Combat Statistics

### Base Stats

| Stat                      | Value   | Class Modifier | Final     |
| :------------------------ | :------ | :------------- | :-------- |
| **Health**                | 100 HP  | -              | 100 HP    |
| **Armor**                 | 40      | -              | 40        |
| **Sprint Speed**          | 5.5 m/s | -5%            | 5.225 m/s |
| **Walk Speed**            | 3.5 m/s | -5%            | 3.325 m/s |
| **Healing Effectiveness** | 100%    | +20%           | 120%      |

### Shield Modifiers

| Property            | Value                       |
| :------------------ | :-------------------------- |
| Guardian Shield HP  | 200                         |
| Shield Regeneration | 20 HP/second (when not hit) |
| Shield Radius       | 5 meters                    |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 100 | Standard (Support class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8/second | Standard |
| **Net Sprint Duration** | 10.0 seconds | Average |
| **Footstep Volume** | 85% | Quiet — nun's habit of moving silently |
| **Ability Audio Radius** | 30 meters | Shield dome hum + angelic choir is distinctive |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 10% | Slight resist (Support class) |
| Burn | 0% | Full DoT |
| EMP | 0% | Guardian Shield destroyed instantly by EMP |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 34 cm radius, 164 cm height |
| **Head Sphere** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Slim build, shield generator on back, white cross on shoulders |
| **Class Accent Zones** | White/Green (#22C55E) on armband and backpack cross |
| **Shield VFX (Top-Down)** | Blue-white hemispherical dome visible from above, 5m radius circle on ground |
| **Shield Audio Radius** | 30m — angelic choir hum is a strong audio tell |

<!-- REF_IMAGE: ANGEL top-down view — showing operator with Guardian Shield deployed, blue-white dome visible from above as 5m radius circle -->

### Guardian Shield Stat Block

| Property | Value | Notes |
| :------- | :---- | :---- |
| **Shield HP** | 200 | Absorbs damage until depleted |
| **Shield Radius** | 5 meters | Dome — visible as circle from above |
| **Duration** | 10 seconds | Or until HP depleted |
| **Regen Rate** | 20 HP/sec | Only when not taking damage for 2s |
| **Projectile Blocking** | One-way | Allies shoot out, enemies cannot shoot in |
| **Player Walk-Through** | Yes | Enemies can physically enter dome |
| **Fire Pass-Through** | No | BLAZE fire blocked by shield wall |
| **Nano Swarm Pass-Through** | Yes | FLUX swarm passes through shield |
| **EMP Vulnerability** | Destroyed instantly | Primary counterplay |

### Difficulty Rating

**Difficulty: 3/5** — Shield placement timing is critical. Deploying too early wastes duration; too late and team takes damage. Positioning within dome matters.


## Abilities

### Active Ability: Guardian Shield

> *"Project a protective dome that absorbs incoming damage."*

| Property      | Value      |
| :------------ | :--------- |
| **Cooldown**  | 90 seconds |
| **Duration**  | 10 seconds |
| **Charges**   | 1          |
| **Shield HP** | 200        |

#### Effects

| Effect               | Value     | Notes                                 |
| :------------------- | :-------- | :------------------------------------ |
| Shield Radius        | 5 meters  | Dome covers allies inside             |
| Shield HP            | 200       | Absorbs incoming damage               |
| Regen Rate           | 20 HP/sec | Only when not taking hits             |
| Allies Can Shoot Out | Yes       | One-way protection                    |
| Enemies Can Enter    | Yes       | Walk through, but can't shoot through |

#### Shield Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **Shield + EMP (CIPHER)** | Shield destroyed instantly — primary counter |
| **Shield + Fire (BLAZE)** | Fire does NOT pass through shield wall |
| **Shield + Nano Swarm (FLUX)** | Swarm passes through shield — does not block |
| **Shield + HAVOC Melee** | HAVOC can push through shield |
| **Shield + UAV Scan (PHANTOM)** | Scan does NOT reveal operators inside shield |
| **Shield + Smoke (WRAITH)** | Smoke passes through shield dome |
| **Shield + BULWARK Shield** | Both shields stack (dome + flat shield) |

#### Top-Down Shield VFX

| State | VFX From Above |
| :---- | :------------- |
| Shield deploy | Blue-white flash, dome expands outward from ANGEL |
| Shield active | Translucent blue-white dome, 5m radius circle on ground, faint glow |
| Shield taking damage | Shield sparks at impact point, slight flicker |
| Shield low HP (<50) | Shield cracks visible, rapid flickering |
| Shield break | Shatter effect burst outward, ANGEL staggers |


**Self:**
- Golden dome effect around team
- Angelic humming audio
- Shield cracks as it takes damage

**Enemy Perspective:**
- Obvious golden barrier
- Shots blocked (hit markers on shield)
- Shield flickers when low

#### Tactical Uses

| Use Case              | Strategy                          |
| :-------------------- | :-------------------------------- |
| **Extraction Hold**   | Dome over extraction point        |
| **Revive Protection** | Dome while reviving ally          |
| **Advance Shield**    | Walk forward, team shoots through |
| **Emergency Cover**   | No natural cover? Create it       |

#### Key Difference from DOC

| DOC                      | ANGEL                        |
| :----------------------- | :--------------------------- |
| Heals damage after taken | Prevents damage entirely     |
| Passive, fire-and-forget | Active, requires positioning |
| Better for sustained     | Better for burst protection  |
| Drone can be destroyed   | Shield has HP                |

#### Upgrade Slots

**Slot 1 (Level 5):**
| Option               | Effect                           |
| :------------------- | :------------------------------- |
| **Reinforced Faith** | Shield HP +50 (250 total)        |
| **Quick Prayer**     | Cooldown -20 seconds (70s total) |
| **Extended Grace**   | Duration +5 seconds (15s total)  |

**Slot 2 (Level 20):**
| Option               | Effect                                    |
| :------------------- | :---------------------------------------- |
| **Healing Light**    | Allies in dome heal 3 HP/sec              |
| **Blinding Barrier** | Enemies entering dome are briefly blinded |
| **Mobile Sanctuary** | Shield slowly moves with ANGEL (1 m/s)    |

**Slot 3 (Level 35):**
| Option              | Effect                                              |
| :------------------ | :-------------------------------------------------- |
| **Martyr Protocol** | When shield breaks, ANGEL gains 50 temp HP          |
| **Resurrection**    | Downed allies in dome auto-revive (once per deploy) |
| **Divine Wrath**    | Shield breaking deals 30 damage to nearby enemies   |

---

### Passive Ability: Guardian's Watch

> *"Never abandon those in need."*

| Condition                | Effect                          |
| :----------------------- | :------------------------------ |
| Ally below 30% HP nearby | +10% movement speed toward them |
| Reviving allies          | Take 20% less damage            |
| Ally dies within 10m     | Cooldown reduced by 10 seconds  |

**Design Intent:** ANGEL should always be moving toward danger to save allies.

---

## Loadout

### Default Loadout

| Slot          | Item                | Notes                 |
| :------------ | :------------------ | :-------------------- |
| **Primary**   | P90 SMG             | High mag, suppressive |
| **Secondary** | G17 Pistol          | Standard sidearm      |
| **Tactical**  | Medkit ×2, Smoke ×1 | Heal + escape         |
| **Armor**     | Light Vest          | 30 armor points       |

### Recommended Loadouts

**Defensive Angel:**
| Slot      | Item     | Why                     |
| :-------- | :------- | :---------------------- |
| Primary   | MP5      | Reliable, accurate      |
| Secondary | G17      | Standard                |
| Tactical  | Smoke ×2 | Extra cover for revives |

**Aggressive Angel:**
| Slot      | Item         | Why             |
| :-------- | :----------- | :-------------- |
| Primary   | Vector       | High fire rate  |
| Secondary | Deagle       | Finishing power |
| Tactical  | Flashbang ×2 | Entry support   |

---

## Playstyle Guide

### Role in Team

**Primary Role:** Damage Prevention
- Shield during critical moments
- Protect during revives
- Cover extraction

**Secondary Role:** Emergency Response
- Rush to downed allies
- Create safe zones
- Enable risky plays

### Shield Management

**When to Deploy:**
- Before expected engagement
- During revive attempts
- Extraction countdown
- Team retreating

**When NOT to Deploy:**
- Team scattered
- Solo fight (waste of cooldown)
- Enemies can easily flank around

### Positioning

**Ideal Position:**
- Center of team
- With clear view of allies
- Near cover (in case shield breaks)

**Bad Position:**
- Front line
- Too far from team (shield can't reach)
- Exposed to flanks

---

## Matchups

### Favorable Matchups

| Opponent  | Why Favorable               | Tactic               |
| :-------- | :-------------------------- | :------------------- |
| **VIPER** | Shield absorbs stim damage  | Tank his burst       |
| **BLAZE** | Fire can't penetrate shield | Protect from fire    |
| **HAVOC** | He can't reach you in dome  | Shield and burst him |

### Even Matchups

| Opponent    | Notes                     | Key to Winning     |
| :---------- | :------------------------ | :----------------- |
| **DOC**     | Different support styles  | Team comp decides  |
| **BULWARK** | Shield vs Shield          | Positioning battle |
| **PHANTOM** | Intel useless if shielded | Timing matters     |

### Unfavorable Matchups

| Opponent    | Why Difficult                 | Counter Strategy         |
| :---------- | :---------------------------- | :----------------------- |
| **CIPHER**  | EMP destroys shield instantly | Stay out of EMP range    |
| **SPECTER** | Traps inside dome still work  | Clear area before dome   |
| **FLUX**    | Swarm ignores shield          | Exit dome to fight swarm |

---

## Voice Lines

### Combat

| Trigger            | Line                                 |
| :----------------- | :----------------------------------- |
| Ability Activation | "Shield of faith, protect us!"       |
| Shield Takes Hit   | "They cannot break our spirit!"      |
| Shield Breaks      | "Shield down! Find cover!"           |
| Kill               | "Forgive me."                        |
| Reviving           | "Rise, child. Your work isn't done." |
| Low Health         | "I need assistance!"                 |

### Callouts

| Trigger       | Line                    |
| :------------ | :---------------------- |
| Enemy Spotted | "Hostiles ahead."       |
| Ally Downed   | "I'm coming! Hold on!"  |
| Reloading     | "Reloading, cover me."  |
| Smoke Out     | "Concealment deployed." |

### Personality

| Trigger            | Line                                       |
| :----------------- | :----------------------------------------- |
| Match Start        | "May we all return safely."                |
| Extraction Called  | "Salvation approaches. Stay vigilant."     |
| Extraction Success | "We made it. Thank the Lord."              |
| Squad Wipe         | "They were in my care, and they are safe." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Modified nun's habit (tactical), white and blue
- **Headgear:** Modern wimple with tactical headset
- **Gloves:** White medical gloves
- **Face:** Serene expression, prayer beads around neck

### Unlockable Skins

| Skin             | Rarity    | Unlock         |
| :--------------- | :-------- | :------------- |
| **Sister Mercy** | Common    | Level 10       |
| **Field Nurse**  | Uncommon  | 1,000 Credits  |
| **Valkyrie**     | Rare      | Level 25       |
| **Seraphim**     | Epic      | Battle Pass S1 |
| **Archangel**    | Legendary | Season 3 Event |

### Signature Items

| Item              | Description                  |
| :---------------- | :--------------------------- |
| **Rosary**        | Wrapped around left wrist    |
| **Cross Pendant** | Visible on uniform           |
| **Scripture**     | Small Bible in breast pocket |

---

## Lore Connections

### Relationships

| Character    | Relationship                           |
| :----------- | :------------------------------------- |
| **DOC**      | Deep mutual respect, different methods |
| **VIPER**    | Saved his soul, he protects her        |
| **FORTRESS** | Orthodox vs Catholic debates           |
| **PHANTOM**  | She finds her methods troubling        |

### Story Hooks

- Receives coded messages from Vatican contacts
- Investigating rumors of artifacts in the Zone
- Wrestling with whether she's saving or enabling violence

---

## Design Notes (For Developers)

### Balance Considerations

- Shield is powerful but stationary
- EMP hard-counters it completely
- Enemies can walk through (not full protection)
- Long cooldown prevents spam

### Animation Requirements

- Shield deployment: Prayer gesture + dome expansion
- Shield active: Golden particles, angelic audio
- Shield break: Shatter effect + ANGEL staggers
- Idle: Occasionally makes sign of the cross

### Technical Notes

| System           | Notes                                   |
| :--------------- | :-------------------------------------- |
| Shield Collision | Blocks projectiles, not players         |
| Visual           | Particle-based dome, GPU intensive      |
| Audio            | Ambient choir humming, impacts distinct |
| Networking       | Shield HP synced, visual client-side    |

### Top-Down Specific Notes

- Shield dome from above reads as a 5m radius circle with translucent blue-white fill
- Shield must be visible at minimum zoom — critical gameplay information
- When shield is active, allies inside should have a subtle blue tint from above (friendly indicator)
- Shield break shatter VFX should communicate urgency — team now exposed
- One-way projectile blocking is the core mechanic — visual differentiation between inside and outside is essential
