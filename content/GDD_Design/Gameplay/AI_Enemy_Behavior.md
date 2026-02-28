---
title: "AI & Enemy Behavior"
type: docs
weight: 12
---

## Overview

AI enemies are the **primary source of non-player danger** in every raid. They create environmental pressure, punish noisy play, reward tactical movement, and generate loot that drives the economy. This document specifies enemy types, detection states, patrol behaviors, escalation, AI boss patterns, and the **Player-as-Scav** system.

> **Cross-References:** [Core Gameplay Loop](CoreLoop.md) — economy faucets (Scav Mode), phase-by-phase AI presence; [Environmental Hazards](Environmental_Hazards.md) — AI Boss spawn, Scav Raid wave event; [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) — AI detection vs LOS system; [Movement & Stamina](Movement_and_Stamina.md) — sound ranges that AI react to; [Camera System](Camera_System.md) — AI detection circles visible to player.

---

## Design Pillars

- **Pressure, not omniscience:** AI creates danger through predictable-but-punishing behaviors, not perfect aim or wallhacking. Players can learn and outmaneuver them.
- **Sound-driven detection:** AI react primarily to sound (footsteps, gunshots, looting). Matching sound ranges from [Movement & Stamina](Movement_and_Stamina.md) is mandatory.
- **Escalation, not respawn:** Killed AI do not respawn during a raid. However, AI can call reinforcements. Engagement escalates in area, not globally.
- **Top-down visibility balance:** From a top-down view, players can see AI patrol paths. AI detection must be adjusted so stealth remains viable despite the overhead perspective.
- **Loot consistency:** All AI carry contextually appropriate loot. Their gear reflects their faction and role.

---

## Enemy Faction Overview

| Faction | Name | Allegiance | Threat Level | Primary Role |
| :------ | :--- | :--------- | :----------- | :----------- |
| **Scavengers** | Scavs | Neutral/Hostile | Low–Medium | Map filler, loot source, noise generators |
| **Militia** | Raiders | Hostile to all players | Medium–High | Mid-map control, high-value room guards |
| **Corporate Security** | Sec-Force | Hostile (Faction B's enemy) | High | Objective zone guards, keys, military loot |
| **Boss Crew** | varies per boss | Hostile | Very High | Boss bodyguards |
| **Rogue PMC** | Rogues | Hostile to everyone | High | Roaming elite AI; best loot |

> **Faction lore integration:** Full faction backstory in [Story](../../Story/). For gameplay purposes, faction only determines patrol zone, loot table, and aggro range. Faction AI do not attack each other (prevents AI-on-AI noise drowning out player activity).

---

## Enemy Types & Base Stats

### Tier 1 — Scavengers (Common)

Standard map-filling enemies. Low threat individually; dangerous in groups or when triggering others.

| Property | Value |
| :------- | :---- |
| **HP** | 60–90 (varies by gear) |
| **Armor Class** | 0–2 (no armor to light vest) |
| **Weapon Tier** | Tier 1 only (pistols, basic SMGs, occasional shotgun) |
| **Aim Accuracy** | Low (±15–20° spread at 15m) |
| **Patrol behavior** | Wander within 30m zone; stop to examine sounds |
| **Alert range** | Hearing: 20m (walk), 35m (sprint), 50m (gunshot nearby) |
| **Aggro radius** | 12m visual, 25m alert → visual required |
| **Group size** | 1–4 (solo or small pack) |
| **Retreat threshold** | 20% HP — runs to cover, calls for ally |
| **Loot** | Tier 1 gear, basic meds, food/water, small barter items |

### Tier 2 — Militia Raiders (Uncommon)

Mid-raid threat. Guard specific buildings or patrol contested zones. Tactical positioning.

| Property | Value |
| :------- | :---- |
| **HP** | 100–150 |
| **Armor Class** | 2–3 (light-medium vest) |
| **Weapon Tier** | Tier 2 (ARs, shotguns, SMGs with basic mods) |
| **Aim Accuracy** | Medium (±8–12° spread at 20m) |
| **Patrol behavior** | Fixed patrol route within 50m zone with partner |
| **Alert range** | Hearing: 25m (walk), 40m (sprint), 60m (gunshot) |
| **Suppression fire** | Yes — fires toward detected sound even without visual |
| **Group size** | 2–6 (pairs minimum; small squads at objectives) |
| **Retreat threshold** | 30% HP — moves to new cover, does not flee |
| **Communication** | Alerts patrol partner within 30m on aggro |
| **Loot** | Tier 2 weapons, Class 2–3 armor, standard meds |

### Tier 3 — Sec-Force (Rare)

High-threat guards for high-value objectives. Tactical, coordinated, suppress-and-flank capable.

| Property | Value |
| :------- | :---- |
| **HP** | 150–200 |
| **Armor Class** | 3–4 (military vest + helmet) |
| **Weapon Tier** | Tier 3–4 (modded ARs, DMRs, LMGs at objective posts) |
| **Aim Accuracy** | High (±4–6° spread at 25m) |
| **Patrol behavior** | Fixed post or two-man patrol within 80m; does not leave objective zone |
| **Group size** | 2–8 (minimum 2, up to 8 at major objectives) |
| **Flanking** | Yes — one unit suppresses, partner flanks |
| **Retreat threshold** | Never retreats from zone — holds position to death |
| **Radio call** | Has a 10s radio activation on aggro — calls +2 reinforcement Sec-Force from nearest post |
| **Loot** | Tier 3–4 weapons, Class 3–4 armor, military-tier meds, rare keycards |

### Tier 4 — Rogue PMC (Very Rare)

Elite roaming AI. Highest threat. Spawn in 1–2 locations per raid, not at objectives.

| Property | Value |
| :------- | :---- |
| **HP** | 200–300 |
| **Armor Class** | 4–5 (heavy plate carrier + ballistic helmet) |
| **Weapon Tier** | Tier 4 exclusively (best-in-slot configurations) |
| **Aim Accuracy** | Very High (±2–4° at 30m) |
| **Patrol area** | Roams 150m radius; no fixed route |
| **Group size** | 2–3 (never solo) |
| **Tactics** | Suppression + flank + grenade usage |
| **Grenade usage** | Yes — throws frag grenades into cover positions |
| **Retreat threshold** | 40% HP — tactical withdraw to better position, not flight |
| **Loot** | Elite weapons, Class 4–5 armor, rare barter items, keycard |
| **Spawn chance** | 25% per raid (see [Environmental Hazards](Environmental_Hazards.md) — dynamic events) |

---

## AI Detection System

### Detection Layers

AI uses two primary detection channels: **hearing** and **sight**. Detection is never instant.

```
DETECTION FLOW
    
 Sound generated by player
    |
 Sound range check (from Movement & Stamina)
    |
 Is AI within sound range AND in "aware" state?
    |── YES → Alert state transition (see alert states below)
    |── NO  → Ignore
    
 Visual (requires AI to look at area)
    |
 Is player within AI sight range AND in AI vision cone?
    |── YES → Visual confirmation
    |          ↓
    |── Is player in concealment?
    |     Crouch/Prone: 30% detection reduction
    |     Smoke: 80% detection reduction  
    |── Confirmed → Aggro
    |── NO  → Ignore
```

### AI Vision Cone (Top-Down)

By design, top-down camera gives players awareness of AI positions. To maintain stealth viability, AI vision is limited:

| AI Type | Vision cone width | Vision range | Turns to investigate sounds? |
| :------ | :---------------- | :----------- | :--------------------------- |
| Scav | 120° forward arc | 15m line-of-sight | Yes (immediately) |
| Militia | 90° forward arc | 20m LOS | Yes (with 2s delay) |
| Sec-Force | 100° forward arc | 25m LOS | Yes (immediately) |
| Rogue PMC | 120° forward arc | 30m LOS | Yes (immediately) |

**Top-down visual aid:** The camera-visible "detection arc" is shown to the player as a subtle UI indicator (faint cone emanating from enemy in direction they face). This is a deliberate game design choice — players CAN see the cone, reducing frustration. The cone reflects accurate detection logic, not a false display.

### Hearing Multipliers

AI hearing is directly coupled to [Movement & Stamina](Movement_and_Stamina.md) sound ranges:

| Player Action | Sound Range | AI Reaction if in Range |
| :------------ | :---------- | :---------------------- |
| Crouch-walk concrete | 4m | Alert state only if in cone |
| Walking concrete | 10m | Suspicious (turn toward sound) |
| Sprint concrete | 25m | Aggressive alert |
| Sprint metal | 35m | Immediate aggro if nearby |
| Gunshot (any) | 50–100m | Moves toward sound origin |
| Grenade explosion | 100m | All AI in area move toward event |
| Container open | 8–15m | Suspicious (moves toward) |

---

## Alert State Machine

AI exists in one of four states. Transitions between states create the escalation arc:

```
┌─────────────────────────────────────────────────────────────────┐
│                        AI ALERT STATES                           │
│                                                                   │
│  UNAWARE ──────────→ SUSPICIOUS ──────────→ ALERTED             │
│  (patrol)           (investigating)        (searching area)      │
│     ↑                    │                      │                 │
│     │    player leaves   │  timeout (20s)       │  loses contact  │
│     │    area quietly    │  nothing found       │  (30s timeout)  │
│     └────────────────────┴──────────────────────┘                │
│                                                                   │
│  ALERTED ─────────→ HOSTILE                                      │
│  (searching)       (active combat)                               │
│     ↑                    │                                        │
│     │    player hides    │  visual confirmed, active fire         │
│     └────────────────────┘                                        │
└─────────────────────────────────────────────────────────────────┘
```

### State Definitions

| State | Behavior | Duration | Visual Indicator to Player |
| :---- | :------- | :------- | :------------------------- |
| **Unaware** | Normal patrol, no player awareness | Indefinite | No indicator |
| **Suspicious** | Stops patrol, faces sound direction, moves to investigate slowly (crouch-walk speed) | Until confirmed or 20s timeout | Yellow exclamation mark (!) above head at 25m+ |
| **Alerted** | Actively searches last-known position. Calls patrol partner. Increased vision cone (180°). | Until player found or 30s timeout from last contact | Orange alert arc; spoken audio cue |
| **Hostile** | Active combat. Full AI capability unlocked: suppression, flanking, grenades. | Until player dead, escaped 50m for 20s, or AI dead | Red aggressive indicator; audio shout |

### Communication Between AI Units

AI units within a faction communicate when alert state changes:

| Trigger | Communication | Range | Effect |
| :------ | :------------ | :---- | :----- |
| One Scav detects player | Informs nearby Scavs within 20m | 20m radius call | All Scavs in range enter Alerted state |
| Militia aggro | Radio call to squad | Whole patrol group (~50m) | Full squad enters Hostile |
| Sec-Force aggro | Radio call + reinforcement request | 80m + trigger post radio | +2 Sec-Force arrive from nearest post within 30s |
| Rogue PMC aggro | Tactical radio; all Rogues in area | 100m | Unit repositions to flanking positions before engaging |
| AI hears gunshot | Moves toward sound | 100m | All AI in range move toward gunshot location (not aggro, just investigate) |

---

## AI Patrol Behavior

### Patrol Types

| Type | Description | AI Types |
| :--- | :---------- | :------- |
| **Zone Wander** | Moves randomly within a defined zone (30–80m radius). No fixed route. | Scavs |
| **Fixed Route** | Walks a pre-set path (visible to designer, not published to players). Loops indefinitely. | Militia, Sec-Force |
| **Post Guard** | Stationary at key point. Rotates facing direction every 15–30s. | Sec-Force at objectives |
| **Roam** | Moves freely across a large map area (150m+). No fixed path. High threat. | Rogue PMC |
| **Area Search** | Triggered by alert — moves to sound origin and searches 15m radius | All types in Suspicious/Alerted state |

### Patrol Schedules

- Fixed route AI never leave their designated zone, even when alerted. They alert local units and hold.
- Zone wander AI may drift near other zones but are pushed back by zone boundary logic.
- Dead AI **do not respawn** during a raid. Cleared areas remain cleared.
- Killed AI persist as lootable corpses for the entire raid duration.

---

## Combat Behavior

### General Engagement Rules

| Rule | Detail |
| :--- | :----- |
| **Cover usage** | All Tier 2–4 AI move to cover immediately on taking fire. Never strafe in the open beyond 3 steps. |
| **Suppression fire** | Tier 2+ AI fire in direction of sound/muzzle flash even without visual (±20° spread). Player must change position. |
| **Flanking** | Militia and higher — one unit suppresses, another moves to flanking angle (triggered at 2+ AI vs 1 player position). |
| **Grenade usage** | Rogue PMC only. Throws frag grenade into confirmed player cover position after 4+ seconds of no visual. |
| **Shooting accuracy** | Increases at closer range. Ranges: 5m = base×1.5 accuracy; 30m = base accuracy; 50m = base×0.6 |
| **Limb targeting** | AI does not specifically target weak limbs. Randomized hit distribution by body area (weighted toward torso). |
| **Bleed/Fracture application** | AI can cause bleeds and fractures via the same rules as player weapons. Status effects apply normally. |
| **Ammunition type** | AI use contextually appropriate ammo (Scavs: FMJ/ball; Militia: Hollowpoint; Sec-Force/PMC: AP rounds). |

### Retreat & Self-Preservation

| AI Type | Retreat Threshold | Behavior |
| :------ | :---------------- | :------- |
| Scav | 20% HP | Runs to nearest cover, shouts for help, breaks LoS |
| Militia | 30% HP | Tactical withdrawal to secondary position, still shooting |
| Sec-Force | Never retreats | Holds position until death |
| Rogue PMC | 40% HP | Pulls back to better tactical position, reengages from new angle |

### AI vs AI

- Factional AI do **not** attack each other. Two different faction AI occupying the same zone will ignore one another.
- Exception: Boss-type AI has a 10% chance to aggro all nearby non-boss AI if boss fight lasts >60s (chaos mode).
- Player-as-Scav AI (see below) CAN be attacked by Hostile Sec-Force or PMC AI.

---

## AI Boss System

Bosses are unique high-difficulty spawns that award the best loot in the game. Each map has 1–2 associated boss types.

### Boss Spawn Rules (per Environmental Hazards integration)

- **Spawn chance:** 30% per standard raid; 100% during "Boss Hunt" live event.
- **Spawn timing:** 3–8 minutes into raid (gives initial players time to spread before boss spawns).
- **Spawn announcement:** Distant unique audio cue audible at 100m+ (each boss has a distinct sound).
- **Spawn location:** Boss spawns at their zone's anchor point; does not switch zones.

### Boss Types (Launch Roster — 3 Maps)

#### Boss Type 1 — "Kommandant" (Industrial Zone)

> *A former security contractor gone rogue. Commands a disciplined 4-man squad.*

| Property | Value |
| :------- | :---- |
| **HP** | 450 |
| **Armor** | Class 5 plate carrier |
| **Weapon** | Modded AR (Tier 4) + pistol backup |
| **Bodyguards** | 4 × Militia-class AI (150 HP each) |
| **Ability** | At 50% HP, calls in 2 additional Militia reinforcements (one time) |
| **Unique behavior** | Kommandant never leaves his office room. Bodyguards patrol outer rooms and must be cleared first |
| **Loot on kill** | Guaranteed Tier 4 weapon, Class 5 armor (worn, degraded), unique keycard to vault room |
| **Recommended squad** | 3-player squad; solo possible but not recommended |

**Engagement pattern:**
1. Reach inner office → door is reinforced (breach takes 3s, is very loud, alerts bodyguards immediately)
2. Bodyguards spread out in adjacent rooms — suppress-and-flank pattern
3. At 50% HP, Kommandant activates radio for reinforcements (30s delay for arrivals)
4. Killing Kommandant does not despawn bodyguards; they continue fighting

#### Boss Type 2 — "Wraith" (Residential District)

> *A former scout-class operative. Unpredictable, fast, cloaks briefly.*

| Property | Value |
| :------- | :---- |
| **HP** | 280 |
| **Armor** | Class 3 vest, no helmet |
| **Weapon** | DMR (Tier 3) + suppressed pistol |
| **Bodyguards** | 2 × light Scav-class with SMGs |
| **Ability** | Every 45s, uses a 3s cloak (semi-invisible in top-down, shimmer visible). Repositions during cloak. |
| **Unique behavior** | Does not stay still. Constantly repositioning every 8–12s. Never in same position for >12s. |
| **Loot on kill** | Guaranteed suppressed weapon (Tier 3–4), light rig, rare intel item (quest objective) |
| **Audio tell** | Distinct quiet footstep pattern (faster than Scav). Electronic crackle when cloaking. |
| **Counterplay** | AoE abilities (Flashbang, Frag) reveal cloak position. Motion Sensor tracks movement. |

#### Boss Type 3 — "Iron Wall" (Military Checkpoint)

> *A heavily armored ex-military enforcer. Slow but near-unkillable in frontal assault.*

| Property | Value |
| :------- | :---- |
| **HP** | 700 |
| **Armor** | Class 6 full torso (like Zabralo Mk.2) |
| **Weapon** | LMG (Tier 4, suppression-focused) |
| **Bodyguards** | 6 × Sec-Force guards spread across checkpoint |
| **Ability** | Every 60s, enters "Fortress" stance for 10s (-70% incoming damage; cannot move) |
| **Unique behavior** | Holds checkpoint entrance. Flanking required — frontal attack wastes ammo against Class 6. |
| **Loot on kill** | Guaranteed Class 5–6 armor (heavily degraded), LMG, military keycard tier |
| **Counterplay** | Attack during non-Fortress window. EMP Drone disrupts Fortress stance (gadget disruption). Flank from three sides to force reorientation. High-AP ammo mandatory. |

---

## Player-as-Scav (Scav Mode)

Scav Mode allows players to run zero-cost raids using randomized AI-grade gear. This is documented in [Core Gameplay Loop](CoreLoop.md) (economy faucet) but behavior specifics are defined here.

### Scav Spawn Rules

| Property | Value |
| :------- | :---- |
| **Cooldown between Scav runs** | 20 minutes real time |
| **Spawn timing** | 5–10 minutes into an active raid (not at raid start) |
| **Gear provided** | Randomized: Tier 1–2 weapon, 0–2 class armor, basic meds, partial ammo |
| **Inventory at spawn** | Random loot pre-loaded (player has a "head start" on looting) |
| **Spawn zone** | Perimeter of map, not near high-traffic zones |
| **Extraction** | Same extraction zones as PMC, same timer rules |

### Scav-vs-Scav Rules

| Scenario | Behavior |
| :------- | :------- |
| Player-Scav vs AI-Scav | AI Scavs treat Player-Scav as **friendly by default**. No aggro unless Player-Scav fires first. |
| Player-Scav fires on AI-Scav | All AI Scavs in 40m radius turn hostile. Reputation penalty. |
| Player-Scav vs PMC player | Normal PvP — no restriction |
| Player-Scav reputation | Shooting allied AI Scavs reduces Scav faction reputation. Low reputation = AI Scavs attack Player-Scav on sight. |

### Karma / Scav Reputation System

| Action | Reputation Change | Consequence |
| :----- | :---------------- | :---------- |
| Extract successfully as Scav | +0.1 | Positive spiral |
| Kill AI Scav | −0.5 | AI Scavs become suspicious of player |
| Kill Player-Scav (team kill) | −1.0 | AI Scavs go hostile at −1.5 reputation |
| Kill PMC player | +0.2 | Rewarded for PvP |
| Complete Cooperative Extraction with PMC | +0.5 | See [Extraction Mechanics](Extraction_Mechanics.md) |

**Reputation floor:** At −2.0 reputation, ALL AI Scavs (even Tier 1 wanderers) attack Player-Scav on sight. Recovery requires 10 clean Scav runs without incident.

---

## AI Scav Raid Event

Distinct from Player-as-Scav. Referenced in [Environmental Hazards](Environmental_Hazards.md) and expanded here:

| Property | Value |
| :------- | :---- |
| **Trigger** | 25% random chance per raid; fires between 6:00 and 10:00 of raid timer |
| **Wave composition** | 6–10 Tier 1 Scavs spawning at map edge, moving toward map center |
| **Patrol path** | Moves along main routes toward high-loot zones |
| **Duration** | Until all AI Scavs are killed or raid timer ends |
| **Impact** | Generates significant gunshot audio; other players hear the wave moving |
| **Loot from wave scavs** | Standard Tier 1 loot; occasionally a Tier 2 item on the group "leader" (randomly designated) |
| **Alert propagation** | Wave AI alert each other but do not alert static map AI (Militia, Sec-Force) — contained event |

---

## AI Audio Design Brief

All AI sounds should be directional (3D spatialized) and consistent with the distances in [Movement & Stamina](Movement_and_Stamina.md). Key SFX requirements:

| Sound | Audible at | Priority |
| :---- | :--------: | :------- |
| Scav chatter (idle talk, mumbling) | 20m | Medium — ambient immersion |
| Suspicious exclamation ("What was that?") | 30m | High — player warning signal |
| Aggro shout (voice line) | 40m | Critical — alert players to AI seeing them |
| AI gunfire | 80m+ | Critical — must be directional |
| Radio crackle (Sec-Force reinforcement call) | 25m | High — warns player of incoming |
| Boss audio tell (unique per boss) | 100m+ | Critical — announces boss presence |
| Grenade pin-pull (Rogue PMC) | 15m | High — survival critical signal |
| AI movement sounds (footsteps) | per [Movement & Stamina](Movement_and_Stamina.md) surface table | High |

---

## Anti-Frustration Rules

To prevent AI from feeling unfair or cheap, the following design limits apply:

| Rule | Detail | Reason |
| :--- | :----- | :----- |
| No perfect aim through smoke | AI accuracy drops 80% inside smoke | Smoke is a valid counter |
| No instant headshots | AI requires 1 frame of target acquisition before first shot | Prevents instant one-shot on first detection |
| No shooting through walls | AI only shoot at confirmed LOS targets | Same LOS rules as players |
| 10-second invulnerability at spawn | Player-as-Scav gets 10s | Matches PMC spawn protection |
| Dead AI stay dead | No respawn within same raid | Rewards area clearing |
| Alert states time out (20–30s) | AI return to Unaware if player hides | Stealth remains viable recovery option |
| Boss areas pre-announced | Boss audio cue at 100m before player enters zone | Players can prepare, not blindly stumble |

---

## Summary of Key Decisions

| Topic | Decision |
| :---- | :------- |
| **AI respawn** | No respawn within a raid. Dead AI stay dead. |
| **AI detection** | Sound-primary, vision-secondary. Vision cone limited by design for stealth viability in top-down. |
| **AI communication** | Zone-local communication. Not global alerts. |
| **Boss count** | 1–2 boss spawns per map. 3 boss types at launch. |
| **Player-as-Scav** | Separate zero-cost mode with karma system. 20-min cooldown. |
| **Faction AI** | Do not fight each other. Aggro only players of any faction. |
| **Grenade usage** | Rogue PMC only at launch. Future expansion may add Militia grenades. |

---

## Cross-References

- [Core Gameplay Loop](CoreLoop.md) — Scav Mode economy faucet, AI in infiltration phase.
- [Environmental Hazards](Environmental_Hazards.md) — Boss spawn conditions, Scav Raid wave event.
- [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) — AI detect using same LOS rules as players.
- [Movement & Stamina](Movement_and_Stamina.md) — Sound ranges that AI hearing reacts to.
- [Camera System](Camera_System.md) — AI detection arc visible to player in top-down view.
- [Extraction Mechanics](Extraction_Mechanics.md) — Scav cooperative extraction and trust mechanics.
- [Hero Abilities](Hero_Abilities.md) — Motion Sensor and Drone interact with AI alert states.
- [Story](../../Story/) — Faction lore and world context for AI enemy factions.
