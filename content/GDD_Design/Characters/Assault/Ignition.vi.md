---
title: "IGNITION - Ji-yoon Kwon"
type: docs
---

## Operator Profile

> *"They can run, nhưng they can't hide from the flames."*

### Basic Information

| Attribute       | giá trị             |
| :-------------- | :---------------- |
| **Real Name**   | Ji-yoon Kwon      |
| **Codename**    | IGNITION          |
| **Class**       | Assault           |
| **Nationality** | South Korean      |
| **Age**         | 28                |
| **Height**      | 170 cm (5'7")     |
| **Weight**      | 62 kg (137 lbs)   |

<!-- REF_IMAGE: IGNITION operator portrait — firefighter gear modified for combat, red bandana, intense eyes, holding Molotov hoặc flamethrower nozzle -->

### Background

Ji-yoon Kwon grew up in Seoul, where she developed a reputation as a volatile pyrotechnics engineer of exceptional skill. Her ability to mold fire và work under extreme conditions caught the attention of military recruiters.

sau serving as a combat engineer specializing in incendiary vũ khí, Ji-yoon became disillusioned với the chain of command. She went AWOL và now operates in the Exclusion Zone, using her pyrotechnic expertise to rõ rooms và deny địch positions với chaotic glee.

### Personality Traits

- **Intense** - Everything she does, she does với passion
- **Reckless** - Sometimes crosses lines others won't
- **Fiercely Independent** - Never follows orders blindly again
- **Protective** - Burns anyone who threatens her team

---

## Combat Statistics

### Base Stats

| Stat             | giá trị   | Class Modifier | Final    |
| :--------------- | :------ | :------------- | :------- |
| **máu**       | 100 HP  | -              | 100 HP   |
| **giáp**        | 50      | -10%           | 45       |
| **Sprint Speed** | 5.5 m/s | +10%           | 6.05 m/s |
| **Walk Speed**   | 3.5 m/s | -              | 3.5 m/s  |
| **Crouch Speed** | 2.0 m/s | -              | 2.0 m/s  |

### Damage Modifiers

| Condition              | Modifier                       |
| :--------------------- | :----------------------------- |
| Base vũ khí Damage     | +5% (Class)                    |
| Fire Damage (Ability)  | 15 DPS for 5 seconds           |
| Fire + Direct Hit      | 75 total (nếu standing in fire) |
| Fire Resistance (Self) | Immune to own fire             |

### Expanded Combat Statistics

| Parameter | giá trị | ghi chú |
| :-------- | :---- | :---- |
| **Stamina Pool** | 120 | +20% (Assault class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8.8/second | +10% (Assault class) |
| **Net Sprint Duration** | 12.0 seconds | Longest sprint tier |
| **Footstep Volume** | 100% | Standard |
| **Ability Audio Radius** | 40 meters | Fire crackle is loud và directional |

### Status Effect Resistances

| Effect | Resistance | ghi chú |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 0% | Full duration |
| Burn | 100% (self only) | Immune to own fire, full damage from địch fire |
| EMP | 0% | Incendiary Rush cancelled immediately by EMP |

### Top-Down Visual Spec

| Property | giá trị |
| :------- | :---- |
| **Hitbox Capsule** | 36 cm radius, 168 cm height |
| **Head Sphere** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Compact athletic build, lighter gear, hiển thị rõ grenade belt |
| **Class Accent Zones** | Orange (#F97316) on shoulder patches, flame decals on giáp |
| **Fire Trail VFX (Top-Down)** | Bright orange line on ground, 2m wide, flickering flame particles |
| **Fire Audio Radius** | 40m — crackling fire audible from distance |

<!-- REF_IMAGE: IGNITION top-down view — showing fire trail behind operator as seen from above trong khi Incendiary Rush, 2m trail width hiển thị rõ -->

### Difficulty Rating

**Difficulty: 3/5** — Requires spatial awareness for fire placement. Trail creation trong khi sprint demands good map knowledge to tạo effective area denial.


## Abilities

### Active Ability: Incendiary Rush

> *"Deploy a trail of fire behind you while sprinting, tạo area denial."*

| Property          | giá trị                      |
| :---------------- | :------------------------- |
| **Cooldown**      | 75 seconds                 |
| **Duration**      | 6 seconds (trail creation) |
| **Fire Duration** | 8 seconds (fire persists)  |
| **Charges**       | 1                          |

#### Effects

| Effect           | giá trị           | ghi chú                      |
| :--------------- | :-------------- | :------------------------- |
| Fire Trail Width | 2 meters        | tạo wall behind you    |
| Fire Damage      | 15 HP/second    | Standing in fire           |
| Sprint Bonus     | +20%            | While ability active       |
| Trail Length     | Up to 30 meters | Depends on sprint distance |

#### Fire Interaction Rules

| Interaction | kết quả |
| :---------- | :----- |
| **Fire + MIRAGE Sensors** | Sensors destroyed by fire contact |
| **Fire + PULSE Nano Swarm** | Both damage effects stack on địch caught in overlap zone |
| **Fire + AEGIS Shield** | Fire does NOT pass thông qua Guardian Shield |
| **Fire + BASTION Shield** | Fire does NOT pass thông qua Riot Shield |
| **Fire + Smoke (OBSIDIAN)** | Fire burns thông qua smoke — smoke does not extinguish |
| **Fire + EMP (GLITCH)** | EMP cancels Incendiary Rush immediately, existing fire persists |

#### Top-Down Fire Trail VFX

| trạng thái | VFX From Above |
| :---- | :------------- |
| Trail creation | Bright orange line on ground behind sprinting operator |
| Fire active | Flickering flame particles, 2m wide, orange-yellow glow on ground |
| Fire fading (last 2s) | Flames shrink, glow dims, smoke wisps rise |
| Fire expired | Dark scorch mark on ground (fades sau 5s) |

#### Visual & Audio Cues

**Self:**
- Feet leave fire footprints
- màn hình edges glow orange
- Fire crackling audio

**địch Perspective:**
- hiển thị rõ fire trail
- Smoke particles rising
- Distinct ignition sound

#### Tactical Uses

| cách dùng Case             | Strategy                                 |
| :------------------- | :--------------------------------------- |
| **Entry Denial**     | Run across doorway to block entrance     |
| **Escape Route**     | tạo fire between you và pursuers     |
| **Flank Prevention** | Seal off one angle while pushing another |
| **Zone Control**     | Cut off extraction point access          |
| **Chase Prevention** | Injured? Run và leave fire              |

#### upgrade Slots

**Slot 1 (Level 5):**
| Option             | Effect                               |
| :----------------- | :----------------------------------- |
| **Scorched Earth** | Fire duration +4 seconds (12s total) |
| **Rapid Ignition** | Cooldown -15 seconds (60s total)     |
| **Thermal Surge**  | Fire damage +5 DPS (20 total)        |

**Slot 2 (Level 20):**
| Option            | Effect                                     |
| :---------------- | :----------------------------------------- |
| **Inferno Width** | Fire trail width +1 meter (3m total)       |
| **Smoke màn hình**  | Fire tạo vision-blocking smoke         |
| **Napalm Stick**  | Fire applies slow effect (-30% move speed) |

**Slot 3 (Level 35):**
| Option               | Effect                                   |
| :------------------- | :--------------------------------------- |
| **Phoenix Protocol** | Walking thông qua own fire heals 5 HP/sec  |
| **Wildfire**         | Fire spreads 1m outward over duration    |
| **Flashpoint**       | địch exiting fire are briefly blinded |

---

### Passive Ability: Pyromaniac

> *"Fire damage dealt to địch restores máu."*

| Condition                        | Effect                         |
| :------------------------------- | :----------------------------- |
| địch takes fire damage from you | Heal 2 HP per second they burn |
| Multiple địch burning         | Heal for each địch            |
| Maximum heal per ability         | 30 HP                          |

**Design Intent:** Rewards aggressive area denial và tạo chaos.

---

## Loadout

### Default Loadout

| Slot          | Item            | ghi chú                   |
| :------------ | :-------------- | :---------------------- |
| **primary**   | PP-19 Bizon SMG | High mag, medium damage |
| **secondary** | G17 Pistol      | Standard sidearm        |
| **Tactical**  | Molotov ×2      | Extra fire damage       |
| **giáp**     | Medium Vest     | 50 giáp points         |

### Recommended Loadouts

**Full Pyro:**
| Slot      | Item       | Why                          |
| :-------- | :--------- | :--------------------------- |
| primary   | MP5K       | Fast fire rate for finishing |
| secondary | Flare Gun  | Extra fire (meme nhưng fun)    |
| Tactical  | Molotov ×2 | Maximum fire coverage        |

**Balanced Ignition:**
| Slot      | Item                 | Why                  |
| :-------- | :------------------- | :------------------- |
| primary   | AK-74u               | Good damage at range |
| secondary | G17                  | Reliable backup      |
| Tactical  | Molotov ×1, Smoke ×1 | Fire + escape        |

---

## Playstyle Guide

### Role in Team

**primary Role:** Area Denial
- Block chokepoints với fire
- Control địch movement
- tạo chaos in fights

**secondary Role:** Entry Fragger
- Push thông qua your own fire (immune)
- Surprise địch expecting you to avoid fire
- Flank while fire distracts

### Combat Loop

```
1. Identify key chokepoint
2. Activate Incendiary Rush
3. Sprint across to create fire wall
4. Push through fire to surprise enemies
5. Use conventional weapons while fire does work
6. Heal from passive as enemies burn
7. Reposition for cooldown, repeat
```

### Fire Placement Tips

**Good Fire Placement:**
- Doorways và windows
- Extraction point approaches
- Behind you while retreating
- Between địch và teammate

**Bad Fire Placement:**
- Your team's planned route
- Near friendly healing zones
- In open areas (easy to avoid)

---

## Matchups

### Favorable Matchups

| Opponent     | Why Favorable                 | Tactic                     |
| :----------- | :---------------------------- | :------------------------- |
| **GOLIATH** | Slow, can't escape fire       | Trap in fire zones         |
| **BASTION**  | Shield doesn't stop fire      | Circle around, tạo fire |
| **AEGIS**    | Shield can't heal fire damage | Burn thông qua shield giá trị  |

### Even Matchups

| Opponent    | ghi chú                             | chính to Winning            |
| :---------- | :-------------------------------- | :------------------------ |
| **MAMBA**   | Stim vs Fire, different strengths | Avoid direct gunfight     |
| **SUTURE**     | Can heal thông qua fire             | Kill drone first          |
| **SONAR** | Intel vs area denial              | Fire blocks common routes |

### Unfavorable Matchups

| Opponent    | Why Difficult                 | Counter Strategy                     |
| :---------- | :---------------------------- | :----------------------------------- |
| **MIRAGE** | Traps counter your aggression | rõ traps carefully                |
| **PULSE**    | Nano swarm can zone you back  | Trade zones, don't engage in swarm   |
| **OBSIDIAN**  | Smoke negates fire visibility | cách dùng fire for area denial, not vision |

---

## Voice Lines

### Combat

| Trigger                  | Line                                   |
| :----------------------- | :------------------------------------- |
| Ability Activation       | "Light 'em up!"                        |
| Ability Activation (Alt) | "Burn, baby, burn!"                    |
| Kill                     | "Toasted."                             |
| Kill (Fire)              | "How's the heat?"                      |
| Kill (Fire, Alt)         | "Should've stayed out of the kitchen." |
| Low máu               | "Running hot over here!"               |
| Reviving                 | "Don't fade on me!"                    |

### Callouts

| Trigger          | Line                                    |
| :--------------- | :-------------------------------------- |
| địch Spotted    | "Got eyes on a target!"                 |
| Fire Placed      | "Area's hot!"                           |
| Multiple địch | "Got a crowd - perfect for a barbecue!" |
| Reloading        | "Swapping!"                             |
| Molotov Throw    | "Fire in the hole!"                     |

### Personality

| Trigger            | Line                                       |
| :----------------- | :----------------------------------------- |
| Match Start        | "thời gian to turn up the heat."                |
| Extraction Called  | "Almost done. Let's not get burned now."   |
| Extraction success | "Another successful job. thời gian for drinks." |
| Squad Wipe         | "Nobody escapes the flames."               |

---

## Cosmetics

### Default Appearance

- **Outfit:** Dark red tactical jacket, black cargo pants
- **Headgear:** Red bandana covering lower face
- **Gloves:** Heat-resistant black gloves
- **Face:** Light scarring from old burns, intense eyes

### Unlockable Skins

| Skin            | Rarity    | Unlock         |
| :-------------- | :-------- | :------------- |
| **Wildfire**    | Common    | Level 10       |
| **Ash Gray**    | Uncommon  | 1,000 Credits  |
| **Inferno**     | Rare      | Level 25       |
| **Firefighter** | Epic      | Battle Pass S1 |
| **Hellfire**    | Legendary | Season 2 Event |

### Signature Items

| Item            | Description                             |
| :-------------- | :-------------------------------------- |
| **Lighter**     | Zippo always in hand trong khi idle        |
| **Burn Scars**  | Arms have healed burn marks             |
| **Fire Tattoo** | Phoenix on back (hiển thị rõ on some skins) |

---

## Lore Connections

### Relationships

| nhân vật  | Relationship                              |
| :--------- | :---------------------------------------- |
| **MAMBA**  | Friendly rivalry, respects his directness |
| **SUTURE**    | Treated her burns, she owes him           |
| **OBSIDIAN** | Dislikes smoke interfering với fire      |
| **TARTARUS**  | Kindred spirits, both reckless            |

### Story Hooks

- Looking for the officer who ordered the village burning
- Has contacts in the cartel underworld
- Hides guilt behind bravado và flames

---

## Design ghi chú (For Developers)

### Balance Considerations

- Fire is powerful nhưng telegraphed
- Immune to own fire = unique gameplay
- Cooldown prevents constant fire spam
- Fire damage over thời gian allows counterplay

### Animation yêu cầu

- Fire trail VFX (procedural along sprint path)
- Foot ignition particles while sprinting
- Molotov throw animation
- Death animation: Covers face (protecting from flames)

### Ghi Chú Kỹ Thuật

| hệ thống      | ghi chú                                                |
| :---------- | :--------------------------------------------------- |
| Fire Trail  | Spawns every 0.5m along sprint path                  |
| Performance | Max 3 active fire zones at once                      |
| Collision   | Fire is non-physical, just damage zone               |
| Networking  | Fire positions synced, damage calculated server-side |

### Top-Down cụ thể ghi chú

- Fire trail phải được clearly hiển thị rõ at minimum zoom — bright orange on ground plane
- Fire trail width (2m) should read as a meaningful barrier from above, not a thin line
- Scorch marks sau fire expires provide temporary intel on where IGNITION has been
- Fire particle effects không được obscure loot items on ground within fire zone
- Sprint path prediction: server calculates fire spawn points every 0.5m along the actual path taken
