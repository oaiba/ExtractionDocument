---
title: "WRAITH - Yuki Tanaka"
type: docs
---

## Operator Profile

> *"You can't fight what you can't see."*

### Basic Information

| Attribute | Value |
| :-------- | :---- |
| **Real Name** | Yuki Tanaka |
| **Codename** | WRAITH |
| **Class** | Recon |
| **Nationality** | Japanese |
| **Age** | 26 |
| **Height** | 162 cm (5'4") |
| **Weight** | 52 kg (115 lbs) |

<!-- REF_IMAGE: WRAITH operator portrait — small, agile frame, face half-obscured by tactical mask, smoke grenades on belt, dark stealth suit with faint cyan circuitry -->

### Background

Yuki Tanaka was a prodigy in Japan's Special Forces Group, specializing in infiltration and evasion. Her small stature and uncanny ability to vanish made her perfect for covert operations where detection meant death.

A failed mission in Taiwan left her squad dead and Yuki blamed by superiors looking for a scapegoat. She vanished into the criminal underworld before emerging in the Exclusion Zone, where her talents for disappearing are appreciated rather than punished.

### Personality Traits

- **Elusive** — Never where you expect her
- **Quiet** — Actions speak, words waste energy
- **Survivor** — Escape trumps victory
- **Loyal** — Once trust is earned, never broken

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
| First attack from smoke (Shadow Step) | +15% |
| Toxic Smoke tick (upgrade) | 3 HP/sec |
| Headshot Multiplier | 2.0x |

### Expanded Combat Statistics

| Parameter | Value | Notes |
| :-------- | :---- | :---- |
| **Stamina Pool** | 110 | +10% (Recon class) |
| **Sprint Drain** | 9/second | -10% (Recon class) |
| **Recovery Rate** | 9.6/second | +20% (Recon class) |
| **Net Sprint Duration** | 12.2 seconds | Best efficiency |
| **Footstep Volume** | 60% | -30% (class) + additional -10% (Shadow Step passive) |
| **Ability Audio Radius** | 20 meters | Smoke canister hiss audible |

### Status Effect Resistances

| Effect | Resistance | Notes |
| :----- | :--------- | :---- |
| Stun | 15% | Partial resist (Recon class) |
| Slow | 0% | Full duration |
| Burn | 0% | Full DoT |
| EMP | 0% | No tech-based abilities to disable |

### Top-Down Visual Spec

| Property | Value |
| :------- | :---- |
| **Hitbox Capsule** | 32 cm radius, 160 cm height |
| **Head Sphere** | 12 cm radius |
| **Collision Profile** | Slim (-10% from mesh) — smallest operator |
| **Silhouette From Above** | Smallest operator, hooded head, no visible backpack |
| **Class Accent Zones** | Cyan (#06B6D4) on goggle glow, subtle strips on hood |
| **Smoke VFX (Top-Down)** | Dense gray cloud on ground (8m radius), character fades to near-invisibility inside |
| **Smoke Audio Radius** | 20m — canister hiss on deploy, atmospheric whoosh during duration |

<!-- REF_IMAGE: WRAITH top-down view — showing operator with smoke cloud deployed, 8m radius gray cloud on ground, character partially faded inside -->

### Difficulty Rating

**Difficulty: 5/5** — Hardest operator to master. Requires perfect smoke placement timing, in-smoke awareness, and exploiting Shadow Step first-attack bonus. Maximum game sense required.


## Abilities

### Active Ability: Smoke Screen

> *"Deploy a large smoke cloud that blocks vision for all."*

| Property | Value |
| :------- | :---- |
| **Cooldown** | 70 seconds |
| **Duration** | 15 seconds |
| **Charges** | 1 |

#### Effects

| Effect | Value | Notes |
| :----- | :---- | :---- |
| Smoke Radius | 8 meters | Large area denial |
| Vision Block | 100% | Cannot see through |
| WRAITH Bonus | Can see enemy outlines in own smoke | 10m range |
| Firing Reveals | Muzzle flash briefly visible | 1 second duration |

#### Smoke Interaction Rules

| Interaction | Result |
| :---------- | :----- |
| **Smoke + PHANTOM UAV** | Smoke blocks scan LOS — enemies in smoke not revealed |
| **Smoke + Fire (BLAZE)** | Fire burns through smoke — smoke does not extinguish fire |
| **Smoke + Nano Swarm (FLUX)** | Smoke does not interact with swarm |
| **Smoke + ANGEL Shield** | Smoke passes through shield dome |
| **Smoke + BULWARK Shield** | Smoke blocks vision through shield |
| **Smoke + SPECTER Sensors** | Sensors still detect through smoke |

#### Top-Down Smoke VFX

| State | VFX From Above |
| :---- | :------------- |
| Smoke deploy | Canister lands, gray cloud expands rapidly to 8m radius |
| Smoke active | Dense gray cloud on ground plane, opaque from above |
| WRAITH inside (ally view) | Faint outline visible to teammates only |
| Enemy inside (enemy view) | Completely hidden, no outline |
| Smoke clearing (last 3s) | Cloud thins, visibility gradually returns |


#### Tactical Uses

| Use Case | Strategy |
| :------- | :------- |
| **Escape** | Cover retreat when overwhelmed |
| **Entry** | Confuse enemy positions, push through |
| **Revive** | Block enemy sightlines during teammate pickup |
| **Extraction** | Cover helicopter arrival zone |
| **Loot** | Safely loot high-value containers in contested areas |

#### Upgrade Slots

**Slot 1 (Level 5):**

| Option | Effect |
| :----- | :----- |
| **Extended Fog** | Duration +8 seconds (23s total) |
| **Quick Fade** | Cooldown -15 seconds (55s total) |
| **Larger Cloud** | Radius +4 meters (12m total) |

**Slot 2 (Level 20):**

| Option | Effect |
| :----- | :----- |
| **Toxic Smoke** | Enemies in smoke take 3 HP/sec |
| **Thermal Block** | Also blocks thermal/scan vision |
| **Mobile Cloud** | Smoke slowly follows WRAITH |

**Slot 3 (Level 35):**

| Option | Effect |
| :----- | :----- |
| **Ghost Walk** | WRAITH is invisible in own smoke |
| **Disorienting** | Enemies exiting smoke are briefly confused (1.5s sway) |
| **Double Screen** | 2 smoke charges |

---

### Passive Ability: Shadow Step

> *"Move like the wind. Strike like the storm."*

| Condition | Effect |
| :-------- | :----- |
| In smoke (any) | +20% movement speed |
| Exit smoke | 3-second speed boost (+10%) |
| First attack from smoke | +15% damage |

**Design Intent:** WRAITH is the only operator who thrives in zero-visibility conditions. Smoke is not just a tool — it is her natural habitat. The first-strike bonus incentivizes aggressive plays from concealment, not just passive running.

---

## Loadout

### Default Loadout

| Slot | Item | Notes |
| :--- | :--- | :---- |
| **Primary** | MP7 (Suppressed) | Small, quiet |
| **Secondary** | Karambit Knife | Silent kills |
| **Tactical** | Smoke Grenades x2 | Additional smoke coverage |
| **Armor** | Light Vest | 30 armor points |

### Recommended Loadouts

**Ghost Assassin (Stealth):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | Vector SMG (Suppressed) | Fastest close-range TTK with suppressor |
| Secondary | Karambit Knife | Silent melee for unaware enemies |
| Tactical | Smoke Grenades x3 | Maximum visual denial |

**Smoke Support (Team Play):**

| Slot | Item | Why |
| :--- | :--- | :-- |
| Primary | MP5 (Suppressed) | Reliable mid-range |
| Secondary | Silenced Pistol | Backup |
| Tactical | Smoke x2, Flashbang x1 | Cover + entry |

---

## Playstyle Guide

### Role in Team

**Primary Role:** Visual Denial / Stealth Flanker
- Smoke key sightlines before team pushes
- Flank through smoke to attack from unexpected angles
- Cover revives and extractions with smoke

**Secondary Role:** Escape Artist
- Create escape routes for retreating team
- Disengage losing fights with smoke
- Extract with loot when extraction zone is contested

### Combat Loop

```
1. Identify key engagement area sightlines
2. Deploy Smoke Screen on enemy overwatch position
3. Enter smoke (Shadow Step activates — +20% speed)
4. Use smoke vision to locate enemy outlines
5. First attack from smoke (+15% damage)
6. Eliminate or reposition before smoke clears
7. Exit smoke with speed boost
8. Fall back and wait for cooldown
```

### Positioning

**Good Positions:**
- Near chokepoints where smoke has maximum impact
- Close to team for smoke-supported revives
- Flanking routes that connect to smoke-covered areas

**Bad Positions:**
- Open ground with no cover (smoke is not enough alone)
- Alone without team to capitalize on smoke chaos
- Against enemies with thermal/scan capabilities (countered before upgrade)

---

## Matchups

### Favorable Matchups

| Opponent | Why Favorable | Tactic |
| :------- | :------------ | :----- |
| **BULWARK** | Shield is useless when he cannot see — smoke negates his entire kit | Smoke, flank behind shield, melee |
| **VIPER** | Combat Stim is wasted if he cannot find a target in smoke | Deploy smoke when stim activates, wait it out |
| **FORTRESS** | Slow rotations make him vulnerable to smoke flanks | Smoke his position, attack from behind |

### Even Matchups

| Opponent | Notes | Key to Winning |
| :------- | :---- | :------------- |
| **BLAZE** | Fire vs. smoke — fire reveals you, smoke hides you | Avoid fire zones, use smoke to block fire sightlines |
| **ANGEL** | Guardian Shield works in smoke | Wait for shield down, then push through smoke |
| **DOC** | Healing extends fights — smoke delays but does not prevent healing | Rush DOC in smoke before drone can reposition |

### Unfavorable Matchups

| Opponent | Why Difficult | Counter Strategy |
| :------- | :------------ | :--------------- |
| **PHANTOM** | UAV Scan sees through smoke (unless Thermal Block upgrade) | Prioritize Thermal Block upgrade, or avoid PHANTOM scan zones |
| **FLUX** | Nano Swarm targets area, not vision — works in smoke | Exit smoke away from swarm, reposition to fresh cover |
| **SPECTER** | Motion sensors trigger regardless of smoke — reveals your position | Destroy sensors before deploying smoke |

---

## Voice Lines

### Combat

| Trigger | Line |
| :------ | :--- |
| Ability Activation | "Shikai wo ubau." (Stealing their vision) |
| Kill (From Smoke) | "You never saw it coming." |
| Kill (Melee) | "Silent." |
| Low Health | "Need cover. Deploying smoke." |
| Reviving | "Rise. We disappear together." |

### Callouts

| Trigger | Line |
| :------ | :--- |
| Enemy Spotted | "Contact. [Direction]." |
| Smoke Deploying | "Smoke out. Push or fall back." |
| Reloading | "Reloading." |
| Smoke Ending | "Clear in three..." |

### Personality

| Trigger | Line |
| :------ | :--- |
| Match Start | "Stay close. Disappear with me." |
| Extraction Called | "Smoke the landing zone." |
| Extraction Success | "Like ghosts. Never there." |
| Squad Wipe | "They were already dead. They just had not realized." |

---

## Cosmetics

### Default Appearance

- **Outfit:** Matte black tactical suit, lightweight silhouette, smoke grenades on hip harness
- **Headgear:** Half-face tactical mask (lower face), short dark hair with single white streak
- **Gloves:** Thin black stealth gloves
- **Face:** Sharp features, focused eyes, faint scar along jawline

<!-- REF_IMAGE: WRAITH default skin — top-down view showing smallest silhouette in roster, smoke grenades visible, dark outfit with minimal reflective surfaces -->

### Unlockable Skins

| Skin | Rarity | Unlock |
| :--- | :----- | :----- |
| **Mist Walker** | Common | Level 10 |
| **Sakura Shadow** | Uncommon | 1,000 Credits |
| **Neon Phantom** | Rare | Level 25 |
| **Kunoichi** | Epic | Battle Pass S1 |
| **Yuurei** | Legendary | Season 1 Event |

### Signature Items

| Item | Description |
| :--- | :---------- |
| **White Streak** | Single white stripe in hair (unique identifier) |
| **Karambit Sheath** | Custom carbon-fiber knife holster on thigh |
| **Origami Crane** | Paper crane tucked into vest strap (memorial for lost squad) |

---

## Lore Connections

### Relationships

| Character | Relationship |
| :-------- | :----------- |
| **PHANTOM** | Respects her intel capabilities but dislikes being tracked — friendly rivalry |
| **BLAZE** | Fire burns smoke — natural enemy on the battlefield, no personal grudge |
| **CIPHER** | Mutual understanding of being outcasts from their own governments |
| **SPECTER** | He hunted her once during a covert operation — she escaped, earning his respect |

### Story Hooks

- Seeking evidence to clear her name for the failed Taiwan operation
- Has contacts in Japanese criminal underground who provide black market items
- Memorial ritual — places origami cranes at teammate death locations (environmental detail)
- Intercepted a Corporation dossier with her real identity — someone knows who she is

---

## Design Notes (For Developers)

### Balance Considerations

- Smoke Screen is unique as the only full vision-block ability in the game
- WRAITH's in-smoke vision is her most powerful mechanic — 10m outline range keeps it fair
- First-strike +15% damage from Shadow Step should only apply to the very first attack, not sustained fire from smoke
- Ghost Walk upgrade makes her invisible but NOT invulnerable — damage still hits, audio still present
- Thermal Block upgrade (Slot 2) is the primary counter to PHANTOM — this is an intentional rock-paper-scissors dynamic
- Mobile Cloud should move at 50% of WRAITH's movement speed — too fast makes it oppressive

### Animation Requirements

- Smoke grenade throw animation (0.6 seconds — quick wrist flick)
- Smoke deployment VFX (rapid expansion from canister, volumetric cloud)
- In-smoke enemy outline shader (orange silhouettes, 10m range)
- Shadow Step speed boost (subtle body lean forward on exit)
- Death animation: crumples silently (no dramatic fall — she goes quiet)

### Audio Requirements

| Sound | Notes |
| :---- | :---- |
| Smoke deploy | Sharp hiss of canister + rapid gas expansion |
| Smoke active | Gentle ambient whoosh (quiet, atmospheric) |
| Smoke clearing | Gradual fade-out hiss |
| Shadow Step activate | Soft footstep acceleration (barely audible) |
| Footsteps | Lightest in roster — bare minimum contact sounds |
| Melee kill | Swift blade draw + single cut impact |

### Top-Down Specific Notes

- Smoke cloud must be opaque from above — top-down camera sees dense gray circle on ground
- WRAITH inside own smoke is nearly invisible from top-down (faint shimmer for teammates only)
- Smoke must NOT block friendly minimap detection — allies can still see teammate dots through smoke
- Smoke edge should be well-defined from above (clear boundary between vision/no vision)
- First attack from smoke (+15% damage) applies only to the first bullet/hit, not sustained fire

