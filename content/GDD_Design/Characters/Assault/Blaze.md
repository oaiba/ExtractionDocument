---
title: "BLAZE - Elena Reyes"
type: docs
---

## Operator Profile

> *"They can run, but they can't hide from the flames."*

### Basic Information

| Attribute       | Value             |
| :-------------- | :---------------- |
| **Real Name**   | Elena Maria Reyes |
| **Codename**    | BLAZE             |
| **Class**       | Assault           |
| **Nationality** | Mexican-American  |
| **Age**         | 28                |
| **Height**      | 170 cm (5'7")     |
| **Weight**      | 62 kg (137 lbs)   |

<!-- REF_IMAGE: BLAZE operator portrait — firefighter gear modified for combat, red bandana, intense eyes, holding Molotov or flamethrower nozzle -->

### Background

Elena Reyes grew up in the borderlands of Arizona, where she developed a reputation as a wildfire fighter of exceptional skill. Her ability to predict fire behavior and work under extreme conditions caught the attention of military recruiters.

After serving as a combat engineer specializing in incendiary weapons, Elena became disillusioned with chain of command after her unit was ordered to destroy a civilian village. She went AWOL and now operates in the Exclusion Zone, using her pyrotechnic expertise to clear rooms and deny enemy positions.

### Personality Traits

- **Intense** - Everything she does, she does with passion
- **Reckless** - Sometimes crosses lines others won't
- **Fiercely Independent** - Never follows orders blindly again
- **Protective** - Burns anyone who threatens her team

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

| Condition              | Modifier                       |
| :--------------------- | :----------------------------- |
| Base Weapon Damage     | +5% (Class)                    |
| Fire Damage (Ability)  | 15 DPS for 5 seconds           |
| Fire + Direct Hit      | 75 total (if standing in fire) |
| Fire Resistance (Self) | Immune to own fire             |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 120 | +20% (Assault class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8.8/second | +10% (Assault class) |
| **Net Sprint Duration** | 12.0 seconds | Longest sprint tier |
| **Footstep Volume** | 100% | Standard |
| **Ability Audio Radius** | 40 meters | Fire crackle is loud and directional |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 0% | Full duration |
| Burn | 100% (self only) | Immune to own fire, full damage from enemy fire |
| EMP | 0% | Incendiary Rush cancelled immediately by EMP |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 36 cm radius, 168 cm height |
| **Head Sphere** | 13 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Compact athletic build, lighter gear, visible grenade belt |
| **Class Accent Zones** | Orange (#F97316) on shoulder patches, flame decals on armor |
| **Fire Trail VFX (Top-Down)** | Bright orange line on ground, 2m wide, flickering flame particles |
| **Fire Audio Radius** | 40m — crackling fire audible from distance |

<!-- REF_IMAGE: BLAZE top-down view — showing fire trail behind operator as seen from above during Incendiary Rush, 2m trail width visible -->

### Difficulty Rating

**Difficulty: 3/5** — Requires spatial awareness for fire placement. Trail creation during sprint demands good map knowledge to create effective area denial.


## Abilities

### Active Ability: Incendiary Rush

> *"Deploy a trail of fire behind you while sprinting, creating area denial."*

| Property          | Value                      |
| :---------------- | :------------------------- |
| **Cooldown**      | 75 seconds                 |
| **Duration**      | 6 seconds (trail creation) |
| **Fire Duration** | 8 seconds (fire persists)  |
| **Charges**       | 1                          |

#### Effects

| Effect           | Value           | Notes                      |
| :--------------- | :-------------- | :------------------------- |
| Fire Trail Width | 2 meters        | Creates wall behind you    |
| Fire Damage      | 15 HP/second    | Standing in fire           |
| Sprint Bonus     | +20%            | While ability active       |
| Trail Length     | Up to 30 meters | Depends on sprint distance |

#### Fire Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **Fire + SPECTER Sensors** | Sensors destroyed by fire contact |
| **Fire + FLUX Nano Swarm** | Both damage effects stack on enemies caught in overlap zone |
| **Fire + ANGEL Shield** | Fire does NOT pass through Guardian Shield |
| **Fire + BULWARK Shield** | Fire does NOT pass through Riot Shield |
| **Fire + Smoke (WRAITH)** | Fire burns through smoke — smoke does not extinguish |
| **Fire + EMP (CIPHER)** | EMP cancels Incendiary Rush immediately, existing fire persists |

#### Top-Down Fire Trail VFX

| State | VFX From Above |
| :---- | :------------- |
| Trail creation | Bright orange line on ground behind sprinting operator |
| Fire active | Flickering flame particles, 2m wide, orange-yellow glow on ground |
| Fire fading (last 2s) | Flames shrink, glow dims, smoke wisps rise |
| Fire expired | Dark scorch mark on ground (fades after 5s) |

#### Visual & Audio Cues

**Self:**
- Feet leave fire footprints
- Screen edges glow orange
- Fire crackling audio

**Enemy Perspective:**
- Visible fire trail
- Smoke particles rising
- Distinct ignition sound

#### Tactical Uses

| Use Case             | Strategy                                 |
| :------------------- | :--------------------------------------- |
| **Entry Denial**     | Run across doorway to block entrance     |
| **Escape Route**     | Create fire between you and pursuers     |
| **Flank Prevention** | Seal off one angle while pushing another |
| **Zone Control**     | Cut off extraction point access          |
| **Chase Prevention** | Injured? Run and leave fire              |

#### Upgrade Slots

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
| **Smoke Screen**  | Fire creates vision-blocking smoke         |
| **Napalm Stick**  | Fire applies slow effect (-30% move speed) |

**Slot 3 (Level 35):**
| Option               | Effect                                   |
| :------------------- | :--------------------------------------- |
| **Phoenix Protocol** | Walking through own fire heals 5 HP/sec  |
| **Wildfire**         | Fire spreads 1m outward over duration    |
| **Flashpoint**       | Enemies exiting fire are briefly blinded |

---

### Passive Ability: Pyromaniac

> *"Fire damage dealt to enemies restores health."*

| Condition                        | Effect                         |
| :------------------------------- | :----------------------------- |
| Enemy takes fire damage from you | Heal 2 HP per second they burn |
| Multiple enemies burning         | Heal for each enemy            |
| Maximum heal per ability         | 30 HP                          |

**Design Intent:** Rewards aggressive area denial and creating chaos.

---

## Loadout

### Default Loadout

| Slot          | Item            | Notes                   |
| :------------ | :-------------- | :---------------------- |
| **Primary**   | PP-19 Bizon SMG | High mag, medium damage |
| **Secondary** | G17 Pistol      | Standard sidearm        |
| **Tactical**  | Molotov ×2      | Extra fire damage       |
| **Armor**     | Medium Vest     | 50 armor points         |

### Recommended Loadouts

**Full Pyro:**
| Slot      | Item       | Why                          |
| :-------- | :--------- | :--------------------------- |
| Primary   | MP5K       | Fast fire rate for finishing |
| Secondary | Flare Gun  | Extra fire (meme but fun)    |
| Tactical  | Molotov ×2 | Maximum fire coverage        |

**Balanced Blaze:**
| Slot      | Item                 | Why                  |
| :-------- | :------------------- | :------------------- |
| Primary   | AK-74u               | Good damage at range |
| Secondary | G17                  | Reliable backup      |
| Tactical  | Molotov ×1, Smoke ×1 | Fire + escape        |

---

## Playstyle Guide

### Role in Team

**Primary Role:** Area Denial
- Block chokepoints with fire
- Control enemy movement
- Create chaos in fights

**Secondary Role:** Entry Fragger
- Push through your own fire (immune)
- Surprise enemies expecting you to avoid fire
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
- Doorways and windows
- Extraction point approaches
- Behind you while retreating
- Between enemy and teammate

**Bad Fire Placement:**
- Your team's planned route
- Near friendly healing zones
- In open areas (easy to avoid)

---

## Matchups

### Favorable Matchups

| Opponent     | Why Favorable                 | Tactic                     |
| :----------- | :---------------------------- | :------------------------- |
| **FORTRESS** | Slow, can't escape fire       | Trap in fire zones         |
| **BULWARK**  | Shield doesn't stop fire      | Circle around, create fire |
| **ANGEL**    | Shield can't heal fire damage | Burn through shield value  |

### Even Matchups

| Opponent    | Notes                             | Key to Winning            |
| :---------- | :-------------------------------- | :------------------------ |
| **VIPER**   | Stim vs Fire, different strengths | Avoid direct gunfight     |
| **DOC**     | Can heal through fire             | Kill drone first          |
| **PHANTOM** | Intel vs area denial              | Fire blocks common routes |

### Unfavorable Matchups

| Opponent    | Why Difficult                 | Counter Strategy                     |
| :---------- | :---------------------------- | :----------------------------------- |
| **SPECTER** | Traps counter your aggression | Clear traps carefully                |
| **FLUX**    | Nano swarm can zone you back  | Trade zones, don't engage in swarm   |
| **WRAITH**  | Smoke negates fire visibility | Use fire for area denial, not vision |

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
| Low Health               | "Running hot over here!"               |
| Reviving                 | "Don't fade on me!"                    |

### Callouts

| Trigger          | Line                                    |
| :--------------- | :-------------------------------------- |
| Enemy Spotted    | "Got eyes on a target!"                 |
| Fire Placed      | "Area's hot!"                           |
| Multiple Enemies | "Got a crowd - perfect for a barbecue!" |
| Reloading        | "Swapping!"                             |
| Molotov Throw    | "Fire in the hole!"                     |

### Personality

| Trigger            | Line                                       |
| :----------------- | :----------------------------------------- |
| Match Start        | "Time to turn up the heat."                |
| Extraction Called  | "Almost done. Let's not get burned now."   |
| Extraction Success | "Another successful job. Time for drinks." |
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
| **Lighter**     | Zippo always in hand during idle        |
| **Burn Scars**  | Arms have healed burn marks             |
| **Fire Tattoo** | Phoenix on back (visible on some skins) |

---

## Lore Connections

### Relationships

| Character  | Relationship                              |
| :--------- | :---------------------------------------- |
| **VIPER**  | Friendly rivalry, respects his directness |
| **DOC**    | Treated her burns, she owes him           |
| **WRAITH** | Dislikes smoke interfering with fire      |
| **HAVOC**  | Kindred spirits, both reckless            |

### Story Hooks

- Looking for the officer who ordered the village burning
- Has contacts in the cartel underworld
- Hides guilt behind bravado and flames

---

## Design Notes (For Developers)

### Balance Considerations

- Fire is powerful but telegraphed
- Immune to own fire = unique gameplay
- Cooldown prevents constant fire spam
- Fire damage over time allows counterplay

### Animation Requirements

- Fire trail VFX (procedural along sprint path)
- Foot ignition particles while sprinting
- Molotov throw animation
- Death animation: Covers face (protecting from flames)

### Technical Notes

| System      | Notes                                                |
| :---------- | :--------------------------------------------------- |
| Fire Trail  | Spawns every 0.5m along sprint path                  |
| Performance | Max 3 active fire zones at once                      |
| Collision   | Fire is non-physical, just damage zone               |
| Networking  | Fire positions synced, damage calculated server-side |

### Top-Down Specific Notes

- Fire trail must be clearly visible at minimum zoom — bright orange on ground plane
- Fire trail width (2m) should read as a meaningful barrier from above, not a thin line
- Scorch marks after fire expires provide temporary intel on where BLAZE has been
- Fire particle effects must not obscure loot items on ground within fire zone
- Sprint path prediction: server calculates fire spawn points every 0.5m along the actual path taken
