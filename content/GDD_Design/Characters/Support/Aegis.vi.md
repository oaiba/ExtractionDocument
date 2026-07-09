---
title: "AEGIS - Sister Maria Santos"
type: docs
---

## Operator Profile

> *"Faith is the shield. nhưng sometimes, you need an actual shield."*

### Basic Information

| Attribute       | giá trị                     |
| :-------------- | :------------------------ |
| **Real Name**   | Sister Maria Elena Santos |
| **Codename**    | AEGIS                     |
| **Class**       | Support                   |
| **Nationality** | Filipino                  |
| **Age**         | 35                        |
| **Height**      | 165 cm (5'5")             |
| **Weight**      | 58 kg (128 lbs)           |

<!-- REF_IMAGE: AEGIS operator portrait — tactical nun habit, serene expression, golden energy shield projector active -->

### Background

Maria Santos was a nun và nurse at a missionary hospital in Manila trước a terrorist attack changed everything. khi armed men stormed the hospital, Maria picked up a fallen soldier's vũ khí và held them off for three hours until reinforcements arrived, saving 47 patients và staff.

The Vatican quietly approached her afterward, offering training với Swiss Guard specialists. Now she operates as a "guardian angel" - protecting those who cannot protect themselves in the world's most dangerous places. The Exclusion Zone is simply her newest mission field.

### Personality Traits

- **Serene** - Unshakeable calm, even in combat
- **Protective** - Will die for her team mà không hesitation
- **Spiritual** - Sees combat as protection, not violence
- **Humble** - Never takes credit for saves

---

## Combat Statistics

### Base Stats

| Stat                      | giá trị   | Class Modifier | Final     |
| :------------------------ | :------ | :------------- | :-------- |
| **máu**                | 100 HP  | -              | 100 HP    |
| **giáp**                 | 40      | -              | 40        |
| **Sprint Speed**          | 5.5 m/s | -5%            | 5.225 m/s |
| **Walk Speed**            | 3.5 m/s | -5%            | 3.325 m/s |
| **Healing Effectiveness** | 100%    | +20%           | 120%      |

### Shield Modifiers

| Property            | giá trị                       |
| :------------------ | :-------------------------- |
| Guardian Shield HP  | 200                         |
| Shield Regeneration | 20 HP/second (khi not hit) |
| Shield Radius       | 5 meters                    |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 100 | Standard (Support class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8/second | Standard |
| **Net Sprint Duration** | 10.0 seconds | Average |
| **Footstep Volume** | 85% | Quiet — nun's habit of moving silently |
| **Ability Audio Radius** | 30 meters | Shield dome hum + angelic choir is distinctive |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 10% | Slight resist (Support class) |
| Burn | 0% | Full DoT |
| EMP | 0% | Guardian Shield destroyed instantly by EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 34 cm radius, 164 cm height |
| **Head Sphere** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Slim build, shield generator on back, white cross on shoulders |
| **Class Accent Zones** | White/Green (#22C55E) on armband và backpack cross |
| **Shield VFX (Top-Down)** | Blue-white hemispherical dome hiển thị rõ from above, 5m radius circle on ground |
| **Shield Audio Radius** | 30m — angelic choir hum is a strong audio tell |

<!-- REF_IMAGE: AEGIS top-down view — showing operator với Guardian Shield deployed, blue-white dome hiển thị rõ from above as 5m radius circle -->

### Guardian Shield Stat Block

| Property | giá trị | ghi chú |
| :------- | :---- | :---- |
| **Shield HP** | 200 | Absorbs damage until depleted |
| **Shield Radius** | 5 meters | Dome — hiển thị rõ as circle from above |
| **Duration** | 10 seconds | hoặc until HP depleted |
| **Regen Rate** | 20 HP/sec | Only khi not taking damage for 2s |
| **Projectile Blocking** | One-way | Allies shoot out, địch cannot shoot in |
| **người chơi Walk-thông qua** | Yes | địch can physically enter dome |
| **Fire Pass-thông qua** | No | IGNITION fire blocked by shield wall |
| **Nano Swarm Pass-thông qua** | Yes | PULSE swarm passes thông qua shield |
| **EMP Vulnerability** | Destroyed instantly | primary counterplay |

### Difficulty Rating

**Difficulty: 3/5** — Shield placement timing is critical. Deploying too early wastes duration; too late và team takes damage. Positioning within dome matters.


## Abilities

### Active Ability: Guardian Shield

> *"Project a protective dome that absorbs incoming damage."*

| Property      | giá trị      |
| :------------ | :--------- |
| **Cooldown**  | 90 seconds |
| **Duration**  | 10 seconds |
| **Charges**   | 1          |
| **Shield HP** | 200        |

#### Effects

| Effect               | giá trị     | ghi chú                                 |
| :------------------- | :-------- | :------------------------------------ |
| Shield Radius        | 5 meters  | Dome covers allies inside             |
| Shield HP            | 200       | Absorbs incoming damage               |
| Regen Rate           | 20 HP/sec | Only khi not taking hits             |
| Allies Can Shoot Out | Yes       | One-way protection                    |
| địch Can Enter    | Yes       | Walk thông qua, nhưng can't shoot thông qua |

#### Shield Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **Shield + EMP (GLITCH)** | Shield destroyed instantly — primary counter |
| **Shield + Fire (IGNITION)** | Fire does NOT pass thông qua shield wall |
| **Shield + Nano Swarm (PULSE)** | Swarm passes thông qua shield — does not block |
| **Shield + TARTARUS Melee** | TARTARUS can push thông qua shield |
| **Shield + UAV Scan (SONAR)** | Scan does NOT reveal operators inside shield |
| **Shield + Smoke (OBSIDIAN)** | Smoke passes thông qua shield dome |
| **Shield + BASTION Shield** | Both shields stack (dome + flat shield) |

#### Top-Down Shield VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| Shield deploy | Blue-white flash, dome expands outward from AEGIS |
| Shield active | Translucent blue-white dome, 5m radius circle on ground, faint glow |
| Shield taking damage | Shield sparks at impact point, slight flicker |
| Shield low HP (<50) | Shield cracks hiển thị rõ, rapid flickering |
| Shield break | Shatter effect burst outward, AEGIS staggers |


**Self:**
- Golden dome effect around team
- Aegisic humming audio
- Shield cracks as it takes damage

**địch Perspective:**
- Obvious golden barrier
- Shots blocked (hit markers on shield)
- Shield flickers khi low

#### Tactical Uses

| cách dùng Case              | Strategy                          |
| :-------------------- | :-------------------------------- |
| **Extraction Hold**   | Dome over extraction point        |
| **Revive Protection** | Dome while reviving ally          |
| **Advance Shield**    | Walk forward, team shoots thông qua |
| **Emergency Cover**   | No natural cover? tạo it       |

#### chính Difference from SUTURE

| SUTURE                      | AEGIS                        |
| :----------------------- | :--------------------------- |
| Heals damage sau taken | Prevents damage entirely     |
| Passive, fire-và-forget | Active, requires positioning |
| Better for sustained     | Better for burst protection  |
| Drone can be destroyed   | Shield has HP                |

#### upgrade Slots

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
| **Blinding Barrier** | địch entering dome are briefly blinded |
| **Mobile Sanctuary** | Shield slowly moves với AEGIS (1 m/s)    |

**Slot 3 (Level 35):**
| Option              | Effect                                              |
| :------------------ | :-------------------------------------------------- |
| **Martyr Protocol** | khi shield breaks, AEGIS gains 50 temp HP          |
| **Resurrection**    | Downed allies in dome auto-revive (once per deploy) |
| **Divine Wrath**    | Shield breaking deals 30 damage to nearby địch   |

---

### Passive Ability: Guardian's Watch

> *"Never abandon those in need."*

| Condition                | Effect                          |
| :----------------------- | :------------------------------ |
| Ally below 30% HP nearby | +10% movement speed toward them |
| Reviving allies          | Take 20% less damage            |
| Ally dies within 10m     | Cooldown reduced by 10 seconds  |

**Design Intent:** AEGIS should always be moving toward danger to save allies.

---

## Loadout

### Default Loadout

| Slot          | Item                | ghi chú                 |
| :------------ | :------------------ | :-------------------- |
| **primary**   | P90 SMG             | High mag, suppressive |
| **secondary** | G17 Pistol          | Standard sidearm      |
| **Tactical**  | Medkit ×2, Smoke ×1 | Heal + escape         |
| **giáp**     | Light Vest          | 30 giáp points       |

### Recommended Loadouts

**Defensive Aegis:**
| Slot      | Item     | Why                     |
| :-------- | :------- | :---------------------- |
| primary   | MP5      | Reliable, accurate      |
| secondary | G17      | Standard                |
| Tactical  | Smoke ×2 | Extra cover for revives |

**Aggressive Aegis:**
| Slot      | Item         | Why             |
| :-------- | :----------- | :-------------- |
| primary   | Vector       | High fire rate  |
| secondary | Deagle       | Finishing power |
| Tactical  | Flashbang ×2 | Entry support   |

---

## Playstyle Guide

### Role in Team

**primary Role:** Damage Prevention
- Shield trong khi critical moments
- Protect trong khi revives
- Cover extraction

**secondary Role:** Emergency Response
- Rush to downed allies
- tạo safe zones
- Enable risky plays

### Shield Management

**khi to Deploy:**
- trước expected engagement
- trong khi revive attempts
- Extraction countdown
- Team retreating

**khi NOT to Deploy:**
- Team scattered
- Solo fight (waste of cooldown)
- địch can easily flank around

### Positioning

**Ideal Position:**
- Center of team
- với rõ view of allies
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
| **MAMBA** | Shield absorbs stim damage  | Tank his burst       |
| **IGNITION** | Fire can't penetrate shield | Protect from fire    |
| **TARTARUS** | He can't reach you in dome  | Shield và burst him |

### Even Matchups

| Opponent    | ghi chú                     | chính to Winning     |
| :---------- | :------------------------ | :----------------- |
| **SUTURE**     | Different support styles  | Team comp decides  |
| **BASTION** | Shield vs Shield          | Positioning battle |
| **SONAR** | Intel useless nếu shielded | Timing matters     |

### Unfavorable Matchups

| Opponent    | Why Difficult                 | Counter Strategy         |
| :---------- | :---------------------------- | :----------------------- |
| **GLITCH**  | EMP destroys shield instantly | Stay out of EMP range    |
| **MIRAGE** | Traps inside dome still work  | rõ area trước dome   |
| **PULSE**    | Swarm ignores shield          | Exit dome to fight swarm |

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
| Low máu         | "I need assistance!"                 |

### Callouts

| Trigger       | Line                    |
| :------------ | :---------------------- |
| địch Spotted | "Hostiles ahead."       |
| Ally Downed   | "I'm coming! Hold on!"  |
| Reloading     | "Reloading, cover me."  |
| Smoke Out     | "Concealment deployed." |

### Personality

| Trigger            | Line                                       |
| :----------------- | :----------------------------------------- |
| Match Start        | "May we all return safely."                |
| Extraction Called  | "Salvation approaches. Stay vigilant."     |
| Extraction success | "We made it. Thank the Lord."              |
| Squad Wipe         | "They were in my care, và they are safe." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Modified nun's habit (tactical), white và blue
- **Headgear:** Modern wimple với tactical headset
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
| **Cross Pendant** | hiển thị rõ on uniform           |
| **Scripture**     | Small Bible in breast pocket |

---

## Lore Connections

### Relationships

| nhân vật    | Relationship                           |
| :----------- | :------------------------------------- |
| **SUTURE**      | Deep mutual respect, different methods |
| **MAMBA**    | Saved his soul, he protects her        |
| **GOLIATH** | Orthodox vs Catholic debates           |
| **SONAR**  | She finds her methods troubling        |

### Story Hooks

- Receives coded messages from Vatican contacts
- Investigating rumors of artifacts in the Zone
- Wrestling với whether she's saving hoặc enabling violence

---

## Design ghi chú (For Developers)

### Balance Considerations

- Shield is powerful nhưng stationary
- EMP hard-counters it completely
- địch can walk thông qua (not full protection)
- Long cooldown prevents spam

### Animation yêu cầu

- Shield deployment: Prayer gesture + dome expansion
- Shield active: Golden particles, angelic audio
- Shield break: Shatter effect + AEGIS staggers
- Idle: Occasionally makes sign of the cross

### Ghi Chú Kỹ Thuật

| hệ thống           | ghi chú                                   |
| :--------------- | :-------------------------------------- |
| Shield Collision | Blocks projectiles, not người chơi         |
| Visual           | Particle-based dome, GPU intensive      |
| Audio            | Ambient choir humming, impacts distinct |
| Networking       | Shield HP synced, visual client-side    |

### Top-Down cụ thể ghi chú

- Shield dome from above reads as a 5m radius circle với translucent blue-white fill
- Shield phải được hiển thị rõ at minimum zoom — critical gameplay information
- khi shield is active, allies inside should have a subtle blue tint from above (friendly indicator)
- Shield break shatter VFX should communicate urgency — team now exposed
- One-way projectile blocking is the cốt lõi cơ chế — visual differentiation between inside và outside is essential
