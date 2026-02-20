---
title: "VIPER - Marcus Chen"
type: docs
---

## Operator Profile

> *"First in, last standing."*

### Basic Information

| Attribute       | Value                       |
| :-------------- | :-------------------------- |
| **Real Name**   | Marcus Chen                 |
| **Codename**    | VIPER                       |
| **Class**       | Assault                     |
| **Nationality** | American (Chinese heritage) |
| **Age**         | 32                          |
| **Height**      | 183 cm (6'0")               |
| **Weight**      | 85 kg (187 lbs)             |

<!-- REF_IMAGE: VIPER operator portrait — athletic build, tactical cap, green eyes, holding combat knife, aggressive stance -->

### Background

Marcus Chen served 10 years in the US Army's 75th Ranger Regiment before joining the private military contractor sphere. Known for his calculated aggression and ability to remain calm under fire, he earned the callsign "Viper" for his quick-strike tactics and deadly precision.

After a classified operation in Eastern Europe went sideways, Marcus was left for dead by his handlers. Surviving against all odds, he now operates as a freelance contractor in the Exclusion Zone, using his skills to extract valuable assets and occasionally settle old scores.

### Personality Traits

- **Confident** - Never doubts his abilities
- **Direct** - Says what he means, no BS
- **Protective** - Watches out for teammates
- **Vengeful** - Never forgets betrayal

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

| Condition           | Modifier    |
| :------------------ | :---------- |
| Base Weapon Damage  | +5% (Class) |
| Combat Stim Active  | +25%        |
| Combat Stim + Class | +30% total  |
| Headshot Multiplier | 2.0x        |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 120 | +20% (Assault class) |
| **Sprint Drain** | 10/second | Standard |
| **Recovery Rate** | 8.8/second | +10% (Assault class) |
| **Net Sprint Duration** | 12.0 seconds | Longest sprint tier |
| **Footstep Volume** | 100% | Standard — no stealth bonus |
| **Ability Audio Radius** | 25 meters | Stim inject hiss audible to nearby enemies |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 0% | Full duration |
| Slow | 0% | Full duration — devastating during stim |
| Burn | 0% | Full DoT |
| EMP | 0% | Stim cancelled immediately by EMP |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 40 cm radius, 180 cm height |
| **Head Sphere** | 14 cm radius |
| **Collision Profile** | Standard |
| **Silhouette From Above** | Medium athletic build, cross-chest ammo belt visible, medium helmet |
| **Class Accent Zones** | Orange (#F97316) on shoulder patches and ammo belt |
| **Stim Active VFX (Top-Down)** | Orange body glow, subtle particle trail when moving |
| **Stim Audio Radius** | 25m — enemies within range hear injection hiss |

<!-- REF_IMAGE: VIPER top-down view — showing operator silhouette from 60-degree camera with orange accent zones highlighted, stim active vs inactive comparison -->

### Difficulty Rating

**Difficulty: 2/5** — Straightforward kit. Press stim, shoot better. Low mechanical complexity, rewards good aim timing.


## Abilities

### Active Ability: Combat Stim

> *"Inject experimental combat stimulant for temporary enhanced performance."*

| Property     | Value      |
| :----------- | :--------- |
| **Cooldown** | 90 seconds |
| **Duration** | 10 seconds |
| **Charges**  | 1          |

#### Effects

| Effect         | Value | Notes                    |
| :------------- | :---- | :----------------------- |
| Damage Boost   | +25%  | Stacks with class bonus  |
| Movement Speed | +10%  | All movement types       |
| Reload Speed   | +15%  | Faster reload animations |

#### Ability Interactions

| Interaction | Result |
| :---------- | :----- |
| **Stim + EMP** | Stim cancelled immediately, remaining duration lost |
| **Stim + Burn** | Stim does NOT cleanse burn — damage stacks |
| **Stim + Slow** | Stim movement boost partially counters slow (net +0% to -5% depending on slow source) |
| **Stim + Mark** | Stim does not remove mark status |

#### Top-Down VFX Description

| State | VFX From Above |
| :---- | :------------- |
| Stim inject | Brief orange flash on operator model (0.5s) |
| Stim active | Persistent orange glow on body, subtle particle trail on ground behind movement |
| Stim ending (last 2s) | Glow flickers, particles diminish |
| Stim expired | Glow fades, brief gray exhale particle |


#### Visual & Audio Cues

**Self:**
- Screen edge orange vignette
- Heartbeat audio intensifies
- Hands shake slightly (cosmetic)

**Enemy Perspective:**
- Operator glows orange
- Distinct injection sound (audio cue)
- Faster movement visible

#### Upgrade Slots

**Slot 1 (Level 5):**
| Option              | Effect                           |
| :------------------ | :------------------------------- |
| **Extended Rush**   | Duration +5 seconds (15s total)  |
| **Quick Reload**    | Cooldown -20 seconds (70s total) |
| **Adrenaline Heal** | Heal 10 HP on activation         |

**Slot 2 (Level 20):**
| Option              | Effect                              |
| :------------------ | :---------------------------------- |
| **Overdrive**       | Damage boost +30% (instead of +25%) |
| **Iron Skin**       | +20% damage resistance during stim  |
| **Lightning Hands** | +50% reload speed (instead of +15%) |

**Slot 3 (Level 35):**
| Option          | Effect                                                   |
| :-------------- | :------------------------------------------------------- |
| **Rally Cry**   | Nearby allies get +10% damage                            |
| **Second Wind** | If killed during stim, survive with 1 HP (once per life) |
| **Unstoppable** | Immune to stun/slow during stim                          |

---

### Passive Ability: Adrenaline Surge

> *"Near-death experiences fuel his combat performance."*

| Condition        | Effect                           |
| :--------------- | :------------------------------- |
| Health below 30% | +15% reload speed                |
| Health below 20% | +20% reload speed, +5% movement  |
| Health below 10% | +25% reload speed, +10% movement |

**Design Intent:** Rewards aggressive play and creates clutch moments.

---

## Loadout

### Default Loadout

| Slot          | Item               | Notes                       |
| :------------ | :----------------- | :-------------------------- |
| **Primary**   | M4A1 Assault Rifle | Mid-tier AR, balanced stats |
| **Secondary** | G17 Pistol         | Standard sidearm            |
| **Tactical**  | Frag Grenade ×2    | Area damage                 |
| **Armor**     | Medium Vest        | 50 armor points             |

### Recommended Loadouts

**Aggressive Entry:**
| Slot      | Item         | Why                  |
| :-------- | :----------- | :------------------- |
| Primary   | AK-47        | High damage per shot |
| Secondary | Deagle       | Backup punch         |
| Tactical  | Flashbang ×2 | Entry assistance     |

**Sustained Combat:**
| Slot      | Item              | Why                       |
| :-------- | :---------------- | :------------------------ |
| Primary   | M4A1              | Controllable, fast reload |
| Secondary | SMG (MP7)         | CQB backup                |
| Tactical  | Smoke ×1, Frag ×1 | Versatility               |

---

## Playstyle Guide

### Role in Team

**Primary Role:** Entry Fragger
- Be first into contested areas
- Trade kills aggressively
- Create space for team

**Secondary Role:** Cleanup
- Finish wounded enemies
- Chase down runners
- Secure kills

### Combat Loop

```
1. Wait for intel (Recon scan)
2. Pre-aim angles
3. Activate Combat Stim
4. Entry push (10 second window)
5. Eliminate or call out enemies
6. Retreat if stim expires without kills
7. Wait for cooldown, repeat
```

### Positioning

**Good Positions:**
- Near entry points
- With clear sightlines
- Close to Support for healing

**Bad Positions:**
- Isolated without backup
- Long rotations from team
- Exposed flanks

---

## Matchups

### Favorable Matchups

| Opponent    | Why Favorable                | Tactic                        |
| :---------- | :--------------------------- | :---------------------------- |
| **DOC**     | Cannot outheal your damage   | Rush before drone deploys     |
| **PHANTOM** | Fragile, no combat advantage | Win aim duel                  |
| **FLUX**    | Low combat power             | Aggressive push through swarm |

### Even Matchups

| Opponent    | Notes                      | Key to Winning                    |
| :---------- | :------------------------- | :-------------------------------- |
| **BLAZE**   | Similar role, fire vs stim | Avoid fire zones, use range       |
| **SPECTER** | Traps are annoying         | Check corners, don't rush blindly |
| **ANGEL**   | Shield is strong           | Wait for shield to drop           |

### Unfavorable Matchups

| Opponent    | Why Difficult            | Counter Strategy              |
| :---------- | :----------------------- | :---------------------------- |
| **BULWARK** | Shield blocks all damage | Flank or wait for shield down |
| **CIPHER**  | EMP cancels your stim    | Bait EMP, then engage         |
| **HAVOC**   | Out-damages you in CQB   | Keep range, use cover         |

---

## Voice Lines

### Combat

| Trigger            | Line                                             |
| :----------------- | :----------------------------------------------- |
| Ability Activation | "Stim active! Let's go!"                         |
| Kill               | "Hostile down!"                                  |
| Kill (Headshot)    | "Clean shot."                                    |
| Downed Enemy       | "They're already dead, they just don't know it." |
| Low Health         | "Taking hits, need backup!"                      |
| Reviving           | "Stay with me, soldier!"                         |

### Callouts

| Trigger          | Line                           |
| :--------------- | :----------------------------- |
| Enemy Spotted    | "Contact! Eyes on hostile!"    |
| Multiple Enemies | "Multiple contacts, heads up!" |
| Reloading        | "Mag out!"                     |
| Grenade          | "Frag out!"                    |

### Personality

| Trigger            | Line                                             |
| :----------------- | :----------------------------------------------- |
| Match Start        | "Let's get this done. Stay sharp."               |
| Extraction Called  | "Bird's coming. Hold the line."                  |
| Extraction Success | "Mission complete. Another day, another dollar." |
| Squad Wipe         | "This is what we trained for."                   |

---

## Cosmetics

### Default Appearance

- **Outfit:** OD Green tactical vest, black pants
- **Headgear:** Black baseball cap
- **Gloves:** Black fingerless tactical gloves
- **Face:** Clean-shaven, slight scar on left cheek

### Unlockable Skins

| Skin             | Rarity    | Unlock         |
| :--------------- | :-------- | :------------- |
| **Desert Storm** | Common    | Level 10       |
| **Urban Gray**   | Uncommon  | 1,000 Credits  |
| **Blood Orange** | Rare      | Level 25       |
| **Black Ops**    | Epic      | Battle Pass S1 |
| **Phoenix**      | Legendary | Season 1 Event |

### Signature Items

| Item           | Description                   |
| :------------- | :---------------------------- |
| **Dog Tags**   | Dangling from vest (cosmetic) |
| **Ranger Tab** | Shoulder patch                |
| **Bite Marks** | Scar pattern on left arm      |

---

## Lore Connections

### Relationships

| Character   | Relationship                    |
| :---------- | :------------------------------ |
| **DOC**     | Served together, mutual respect |
| **BULWARK** | Rival, different philosophies   |
| **CIPHER**  | Distrusts - "Too many secrets"  |
| **PHANTOM** | Professional admiration         |

### Story Hooks

- Looking for the handler who betrayed him
- Has intel on Corporation black sites
- Owes a favor to unknown benefactor

---

## Design Notes (For Developers)

### Balance Considerations

- Combat Stim is strong but predictable (audio cue)
- Low armor punishes poor timing
- Cooldown prevents ability spam
- Passive encourages aggressive play

### Animation Requirements

- Stim injection animation (1 second)
- Orange glow VFX during stim
- Heartbeat audio loop
- Death animation: Falls forward (aggressive stance)

### Audio Requirements

| Sound       | Notes                        |
| :---------- | :--------------------------- |
| Stim inject | Sharp hiss + heartbeat start |
| Stim active | Persistent heartbeat loop    |
| Stim end    | Heartbeat slowdown + exhale  |
| Footsteps   | Heavy, military boots        |

### Top-Down Specific Notes

- Stim orange glow must remain visible at minimum zoom (furthest camera distance)
- Stim audio cue must be directional — enemies should be able to locate VIPER by sound
- Particle trail during stim should be subtle enough not to obscure ground loot but visible enough for enemy awareness
- When viewed from top-down, stim injection animation should show arm movement clearly (not hidden by body)
