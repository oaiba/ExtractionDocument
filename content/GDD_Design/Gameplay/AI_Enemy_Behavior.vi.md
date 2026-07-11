---
title: "AI & địch Behavior"
type: docs
weight: 12
---

### Tổng Quan

AI địch are the **primary source of non-người chơi danger** in every raid. They tạo environmental pressure, punish noisy play, reward tactical movement, và generate loot that drives the economy. This tài liệu specifies địch types, detection trạng thái, patrol behaviors, escalation, AI boss patterns, và the **người chơi-as-Scav** hệ thống.

> **Cross-References:** [cốt lõi Gameplay Loop](CoreLoop.md) — economy faucets (Scav Mode), phase-by-phase AI presence; [Environmental Hazards](Environmental_Hazards.md) — AI Boss spawn, Scav Raid wave event; [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) — AI detection vs LOS hệ thống; [Movement & Stamina](Movement_and_Stamina.md) — sound ranges that AI react to; [Camera hệ thống](Camera_System.md) — AI detection circles hiển thị rõ to người chơi.

***

### Design Pillars

* **Pressure, not omniscience:** AI tạo danger thông qua predictable-nhưng-punishing behaviors, not perfect aim hoặc wallhacking. Người chơi có thể learn và outmaneuver them.
* **Sound-driven detection:** AI react primarily to sound (footsteps, gunshots, looting). Matching sound ranges from [Movement & Stamina](Movement_and_Stamina.md) is mandatory.
* **Escalation, not respawn:** Killed AI do not respawn trong khi a raid. However, AI can call reinforcements. Engagement escalates in area, not globally.
* **Top-down visibility balance:** From a top-down view, Người chơi có thể see AI patrol paths. AI detection phải được adjusted so stealth remains viable despite the overhead perspective.
* **Loot consistency:** All AI carry contextually appropriate loot. Their gear reflects their faction và role.

***

### địch Faction Overview

| Faction                | Name            | Allegiance                  | Threat Level | primary Role                               |
| ---------------------- | --------------- | --------------------------- | ------------ | ------------------------------------------ |
| **Scavengers**         | Scavs           | Neutral/Hostile             | Low–Medium   | Map filler, loot source, noise generators  |
| **Militia**            | Raiders         | Hostile to all người chơi      | Medium–High  | Mid-map control, high-giá trị room guards    |
| **Corporate Security** | Sec-Force       | Hostile (Faction B's địch) | High         | Objective zone guards, keys, military loot |
| **Boss Crew**          | varies per boss | Hostile                     | Very High    | Boss bodyguards                            |
| **Rogue PMC**          | Rogues          | Hostile to everyone         | High         | Roaming elite AI; best loot                |

> **Faction lore integration:** Full faction backstory in [Story](https://github.com/oaiba/ExtractionDocument/blob/main/content/Story/README.md). For gameplay purposes, faction only determines patrol zone, loot bảng, và aggro range. Faction AI do not attack each other (prevents AI-on-AI noise drowning out người chơi activity).

***

### địch Types & Base Stats

#### Tier 1 — Scavengers (Common)

Standard map-filling địch. Low threat individually; dangerous in groups hoặc khi triggering others.

| Property              | giá trị                                                   |
| --------------------- | ------------------------------------------------------- |
| **HP**                | 60–90 (varies by gear)                                  |
| **giáp Class**       | 0–2 (no giáp to light vest)                            |
| **vũ khí Tier**       | Tier 1 only (pistols, basic SMGs, occasional shotgun)   |
| **Aim Accuracy**      | Low (±15–20° spread at 15m)                             |
| **Patrol behavior**   | Wander within 30m zone; stop to examine sounds          |
| **Alert range**       | Hearing: 20m (walk), 35m (sprint), 50m (gunshot nearby) |
| **Aggro radius**      | 12m visual, 25m alert → visual required                 |
| **Group size**        | 1–4 (solo hoặc small pack)                                |
| **Retreat threshold** | 20% HP — runs to cover, calls for ally                  |
| **Loot**              | Tier 1 gear, basic meds, food/water, small barter items |

#### Tier 2 — Militia Raiders (Uncommon)

Mid-raid threat. Guard cụ thể buildings hoặc patrol contested zones. Tactical positioning.

| Property              | giá trị                                                 |
| --------------------- | ----------------------------------------------------- |
| **HP**                | 100–150                                               |
| **giáp Class**       | 2–3 (light-medium vest)                               |
| **vũ khí Tier**       | Tier 2 (ARs, shotguns, SMGs với basic mods)          |
| **Aim Accuracy**      | Medium (±8–12° spread at 20m)                         |
| **Patrol behavior**   | Fixed patrol route within 50m zone với partner       |
| **Alert range**       | Hearing: 25m (walk), 40m (sprint), 60m (gunshot)      |
| **Suppression fire**  | Yes — fires toward detected sound even mà không visual |
| **Group size**        | 2–6 (pairs minimum; small squads at objectives)       |
| **Retreat threshold** | 30% HP — moves to new cover, does not flee            |
| **Communication**     | Alerts patrol partner within 30m on aggro             |
| **Loot**              | Tier 2 vũ khí, Class 2–3 giáp, standard meds        |

#### Tier 3 — Sec-Force (Rare)

High-threat guards for high-giá trị objectives. Tactical, coordinated, suppress-và-flank capable.

| Property              | giá trị                                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------- |
| **HP**                | 150–200                                                                                  |
| **giáp Class**       | 3–4 (military vest + helmet)                                                             |
| **vũ khí Tier**       | Tier 3–4 (modded ARs, DMRs, LMGs at objective posts)                                     |
| **Aim Accuracy**      | High (±4–6° spread at 25m)                                                               |
| **Patrol behavior**   | Fixed post hoặc two-man patrol within 80m; does not leave objective zone                   |
| **Group size**        | 2–8 (minimum 2, up to 8 at major objectives)                                             |
| **Flanking**          | Yes — one unit suppresses, partner flanks                                                |
| **Retreat threshold** | Never retreats from zone — holds position to death                                       |
| **Radio call**        | Has a 10s radio activation on aggro — calls +2 reinforcement Sec-Force from nearest post |
| **Loot**              | Tier 3–4 vũ khí, Class 3–4 giáp, military-tier meds, rare keycards                     |

#### Tier 4 — Rogue PMC (Very Rare)

Elite roaming AI. Highest threat. Spawn in 1–2 locations per raid, not at objectives.

| Property              | giá trị                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------- |
| **HP**                | 200–300                                                                               |
| **giáp Class**       | 4–5 (heavy plate carrier + ballistic helmet)                                          |
| **vũ khí Tier**       | Tier 4 exclusively (best-in-slot configurations)                                      |
| **Aim Accuracy**      | Very High (±2–4° at 30m)                                                              |
| **Patrol area**       | Roams 150m radius; no fixed route                                                     |
| **Group size**        | 2–3 (never solo)                                                                      |
| **Tactics**           | Suppression + flank + grenade usage                                                   |
| **Grenade usage**     | Yes — throws frag grenades into cover positions                                       |
| **Retreat threshold** | 40% HP — tactical withdraw to better position, not flight                             |
| **Loot**              | Elite vũ khí, Class 4–5 giáp, rare barter items, keycard                            |
| **Spawn chance**      | 25% per raid (Xem [Environmental Hazards](Environmental_Hazards.md) — dynamic events) |

***

### AI Detection hệ thống

#### Detection Layers

AI uses two primary detection channels: **hearing** và **sight**. Detection is never instant.

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

#### AI Vision Cone (Top-Down)

By design, top-down camera gives người chơi awareness of AI positions. To maintain stealth viability, AI vision is limited:

| AI Type   | Vision cone width | Vision range      | Turns to investigate sounds? |
| --------- | ----------------- | ----------------- | ---------------------------- |
| Scav      | 120° forward arc  | 15m line-of-sight | Yes (immediately)            |
| Militia   | 90° forward arc   | 20m LOS           | Yes (với 2s delay)          |
| Sec-Force | 100° forward arc  | 25m LOS           | Yes (immediately)            |
| Rogue PMC | 120° forward arc  | 30m LOS           | Yes (immediately)            |

**Top-down visual aid:** The camera-hiển thị rõ "detection arc" is shown to the người chơi as a subtle UI indicator (faint cone emanating from địch in direction they face). This is a deliberate game design choice — Người chơi có thể see the cone, reducing frustration. The cone reflects accurate detection logic, not a false display.

#### Hearing Multipliers

AI hearing is directly coupled to [Movement & Stamina](Movement_and_Stamina.md) sound ranges:

| người chơi Action        | Sound Range | AI Reaction nếu in Range          |
| -------------------- | ----------- | -------------------------------- |
| Crouch-walk concrete | 4m          | Alert trạng thái only nếu in cone      |
| Walking concrete     | 10m         | Suspicious (turn toward sound)   |
| Sprint concrete      | 25m         | Aggressive alert                 |
| Sprint metal         | 35m         | Immediate aggro nếu nearby        |
| Gunshot (any)        | 50–100m     | Moves toward sound origin        |
| Grenade explosion    | 100m        | All AI in area move toward event |
| Container open       | 8–15m       | Suspicious (moves toward)        |

***

### Alert trạng thái Machine

AI exists in one of four trạng thái. Transitions between trạng thái tạo the escalation arc:

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

#### trạng thái Definitions

| trạng thái          | Behavior                                                                                   | Duration                                            | Visual Indicator to người chơi                     |
| -------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------- | ---------------------------------------------- |
| **Unaware**    | Normal patrol, no người chơi awareness                                                         | Indefinite                                          | No indicator                                   |
| **Suspicious** | Stops patrol, faces sound direction, moves to investigate slowly (crouch-walk speed)       | Until confirmed hoặc 20s timeout                      | Yellow exclamation mark (!) above head at 25m+ |
| **Alerted**    | Actively searches last-known position. Calls patrol partner. Increased vision cone (180°). | Until người chơi found hoặc 30s timeout from last contact | Orange alert arc; spoken audio cue             |
| **Hostile**    | Active combat. Full AI capability unlocked: suppression, flanking, grenades.               | Until người chơi dead, escaped 50m for 20s, hoặc AI dead  | Red aggressive indicator; audio shout          |

#### Communication Between AI Units

AI units within a faction communicate khi alert trạng thái changes:

| Trigger                 | Communication                      | Range                      | Effect                                                                     |
| ----------------------- | ---------------------------------- | -------------------------- | -------------------------------------------------------------------------- |
| One Scav detects người chơi | Informs nearby Scavs within 20m    | 20m radius call            | All Scavs in range enter Alerted trạng thái                                     |
| Militia aggro           | Radio call to squad                | Whole patrol group (\~50m) | Full squad enters Hostile                                                  |
| Sec-Force aggro         | Radio call + reinforcement request | 80m + trigger post radio   | +2 Sec-Force arrive from nearest post within 30s                           |
| Rogue PMC aggro         | Tactical radio; all Rogues in area | 100m                       | Unit repositions to flanking positions trước engaging                     |
| AI hears gunshot        | Moves toward sound                 | 100m                       | All AI in range move toward gunshot location (not aggro, just investigate) |

***

### AI Patrol Behavior

#### Patrol Types

| Type            | Description                                                                               | AI Types                              |
| --------------- | ----------------------------------------------------------------------------------------- | ------------------------------------- |
| **Zone Wander** | Moves randomly within a defined zone (30–80m radius). No fixed route.                     | Scavs                                 |
| **Fixed Route** | Walks a pre-set path (hiển thị rõ to designer, not published to người chơi). Loops indefinitely. | Militia, Sec-Force                    |
| **Post Guard**  | Stationary at chính point. Rotates facing direction every 15–30s.                           | Sec-Force at objectives               |
| **Roam**        | Moves freely across a large map area (150m+). No fixed path. High threat.                 | Rogue PMC                             |
| **Area Search** | Triggered by alert — moves to sound origin và searches 15m radius                        | All types in Suspicious/Alerted trạng thái |

#### Patrol Schedules

* Fixed route AI never leave their designated zone, even khi alerted. They alert local units và hold.
* Zone wander AI may drift near other zones nhưng are pushed back by zone boundary logic.
* Dead AI **do not respawn** trong khi a raid. Cleared areas remain cleared.
* Killed AI persist as lootable corpses for the entire raid duration.

***

### Combat Behavior

#### General Engagement Rules

| Rule                           | chi tiết                                                                                                               |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Cover usage**                | All Tier 2–4 AI move to cover immediately on taking fire. Never strafe in the open beyond 3 steps.                   |
| **Suppression fire**           | Tier 2+ AI fire in direction of sound/muzzle flash even mà không visual (±20° spread). người chơi must change position.   |
| **Flanking**                   | Militia và higher — one unit suppresses, another moves to flanking angle (triggered at 2+ AI vs 1 người chơi position). |
| **Grenade usage**              | Rogue PMC only. Throws frag grenade into confirmed người chơi cover position sau 4+ seconds of no visual.              |
| **Shooting accuracy**          | Increases at closer range. Ranges: 5m = base×1.5 accuracy; 30m = base accuracy; 50m = base×0.6                       |
| **Limb targeting**             | AI does not specifically target weak limbs. Randomized hit distribution by body area (weighted toward torso).        |
| **Bleed/Fracture application** | AI can cause bleeds và fractures via the same rules as người chơi vũ khí. Status effects apply normally.               |
| **Ammunition type**            | AI cách dùng contextually appropriate đạn (Scavs: FMJ/ball; Militia: Hollowpoint; Sec-Force/PMC: AP rounds).              |

#### Retreat & Self-Preservation

| AI Type   | Retreat Threshold | Behavior                                                         |
| --------- | ----------------- | ---------------------------------------------------------------- |
| Scav      | 20% HP            | Runs to nearest cover, shouts for giúp, breaks LoS               |
| Militia   | 30% HP            | Tactical withdrawal to secondary position, still shooting        |
| Sec-Force | Never retreats    | Holds position until death                                       |
| Rogue PMC | 40% HP            | Pulls back to better tactical position, reengages from new angle |

#### AI vs AI

* Factional AI do **not** attack each other. Two different faction AI occupying the same zone will ignore one another.
* Exception: Boss-type AI has a 10% chance to aggro all nearby non-boss AI nếu boss fight lasts >60s (chaos mode).
* người chơi-as-Scav AI (see below) CAN be attacked by Hostile Sec-Force hoặc PMC AI.

***

### AI Boss hệ thống

Bosses are unique high-difficulty spawns that award the best loot in the game. Each map has 1–2 associated boss types.

#### Boss Spawn Rules (per Environmental Hazards integration)

* **Spawn chance:** 30% per standard raid; 100% trong khi "Boss Hunt" live event.
* **Spawn timing:** 3–8 minutes into raid (gives initial người chơi thời gian to spread trước boss spawns).
* **Spawn announcement:** Distant unique audio cue audible at 100m+ (each boss has a distinct sound).
* **Spawn location:** Boss spawns at their zone's anchor point; does not switch zones.

#### Boss Types (Launch Roster — 3 Maps)

**Boss Type 1 — "Kommandant" (Industrial Zone)**

> _A former security contractor gone rogue. Commands a disciplined 4-man squad._

| Property              | giá trị                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| **HP**                | 450                                                                                              |
| **giáp**             | Class 5 plate carrier                                                                            |
| **vũ khí**            | Modded AR (Tier 4) + pistol backup                                                               |
| **Bodyguards**        | 4 × Militia-class AI (150 HP each)                                                               |
| **Ability**           | At 50% HP, calls in 2 additional Militia reinforcements (one thời gian)                               |
| **Unique behavior**   | Kommandant never leaves his office room. Bodyguards patrol outer rooms và phải được cleared first |
| **Loot on kill**      | Guaranteed Tier 4 vũ khí, Class 5 giáp (worn, degraded), unique keycard to vault room           |
| **Recommended squad** | 3-người chơi squad; solo possible nhưng not recommended                                                |

**Engagement pattern:**

1. Reach inner office → door is reinforced (breach takes 3s, is very loud, alerts bodyguards immediately)
2. Bodyguards spread out in adjacent rooms — suppress-và-flank pattern
3. At 50% HP, Kommandant activates radio for reinforcements (30s delay for arrivals)
4. Killing Kommandant does not despawn bodyguards; they continue fighting

**Boss Type 2 — "Obsidian" (Residential District)**

> _A former scout-class operative. Unpredictable, fast, cloaks briefly._

| Property            | giá trị                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------- |
| **HP**              | 280                                                                                                 |
| **giáp**           | Class 3 vest, no helmet                                                                             |
| **vũ khí**          | DMR (Tier 3) + suppressed pistol                                                                    |
| **Bodyguards**      | 2 × light Scav-class với SMGs                                                                      |
| **Ability**         | Every 45s, uses a 3s cloak (semi-invisible in top-down, shimmer hiển thị rõ). Repositions trong khi cloak. |
| **Unique behavior** | Does not stay still. Constantly repositioning every 8–12s. Never in same position for >12s.         |
| **Loot on kill**    | Guaranteed suppressed vũ khí (Tier 3–4), light rig, rare intel item (quest objective)               |
| **Audio tell**      | Distinct quiet footstep pattern (faster than Scav). Electronic crackle khi cloaking.               |
| **Counterplay**     | AoE abilities (Flashbang, Frag) reveal cloak position. Motion Sensor tracks movement.               |

**Boss Type 3 — "Iron Wall" (Military Checkpoint)**

> _A heavily armored ex-military enforcer. Slow nhưng near-unkillable in frontal assault._

| Property            | giá trị                                                                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HP**              | 700                                                                                                                                                             |
| **giáp**           | Class 6 full torso (like Zabralo Mk.2)                                                                                                                          |
| **vũ khí**          | LMG (Tier 4, suppression-focused)                                                                                                                               |
| **Bodyguards**      | 6 × Sec-Force guards spread across checkpoint                                                                                                                   |
| **Ability**         | Every 60s, enters "Goliath" stance for 10s (-70% incoming damage; cannot move)                                                                                  |
| **Unique behavior** | Holds checkpoint entrance. Flanking required — frontal attack wastes đạn against Class 6.                                                                      |
| **Loot on kill**    | Guaranteed Class 5–6 giáp (heavily degraded), LMG, military keycard tier                                                                                       |
| **Counterplay**     | Attack trong khi non-Goliath window. EMP Drone disrupts Goliath stance (gadget disruption). Flank from three sides to force reorientation. High-AP đạn mandatory. |

***

### người chơi-as-Scav (Scav Mode)

Scav Mode allows người chơi to run zero-chi phí raids using randomized AI-grade gear. This is documented in [cốt lõi Gameplay Loop](CoreLoop.md) (economy faucet) nhưng behavior specifics are defined here.

#### Scav Spawn Rules

| Property                       | giá trị                                                                  |
| ------------------------------ | ---------------------------------------------------------------------- |
| **Cooldown between Scav runs** | 20 minutes real thời gian                                                   |
| **Spawn timing**               | 5–10 minutes into an active raid (not at raid start)                   |
| **Gear provided**              | Randomized: Tier 1–2 vũ khí, 0–2 class giáp, basic meds, partial đạn |
| **Inventory at spawn**         | Random loot pre-loaded (người chơi has a "head start" on looting)          |
| **Spawn zone**                 | Perimeter of map, not near high-traffic zones                          |
| **Extraction**                 | Same extraction zones as PMC, same timer rules                         |

#### Scav-vs-Scav Rules

| Scenario                     | Behavior                                                                                                         |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| người chơi-Scav vs AI-Scav       | AI Scavs treat người chơi-Scav as **friendly by default**. No aggro unless người chơi-Scav fires first.                  |
| người chơi-Scav fires on AI-Scav | All AI Scavs in 40m radius turn hostile. Reputation penalty.                                                     |
| người chơi-Scav vs PMC người chơi    | Normal PvP — no restriction                                                                                      |
| người chơi-Scav reputation       | Shooting allied AI Scavs reduces Scav faction reputation. Low reputation = AI Scavs attack người chơi-Scav on sight. |

#### Karma / Scav Reputation hệ thống

| Action                                   | Reputation Change | Consequence                                         |
| ---------------------------------------- | ----------------- | --------------------------------------------------- |
| Extract successfully as Scav             | +0.1              | Positive spiral                                     |
| Kill AI Scav                             | −0.5              | AI Scavs become suspicious of người chơi                |
| Kill người chơi-Scav (team kill)             | −1.0              | AI Scavs go hostile at −1.5 reputation              |
| Kill PMC người chơi                          | +0.2              | Rewarded for PvP                                    |
| Complete Cooperative Extraction với PMC | +0.5              | Xem [Extraction cơ chế](Extraction_Mechanics.md) |

**Reputation floor:** At −2.0 reputation, ALL AI Scavs (even Tier 1 wanderers) attack người chơi-Scav on sight. Recovery requires 10 clean Scav runs mà không incident.

***

### AI Scav Raid Event

Distinct from người chơi-as-Scav. Referenced in [Environmental Hazards](Environmental_Hazards.md) và expanded here:

| Property                 | giá trị                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| **Trigger**              | 25% random chance per raid; fires between 6:00 và 10:00 of raid timer                         |
| **Wave composition**     | 6–10 Tier 1 Scavs spawning at map edge, moving toward map center                               |
| **Patrol path**          | Moves along main routes toward high-loot zones                                                 |
| **Duration**             | Until all AI Scavs are killed hoặc raid timer ends                                               |
| **Impact**               | Generates significant gunshot audio; other người chơi hear the wave moving                        |
| **Loot from wave scavs** | Standard Tier 1 loot; occasionally a Tier 2 item on the group "leader" (randomly designated)   |
| **Alert propagation**    | Wave AI alert each other nhưng do not alert static map AI (Militia, Sec-Force) — contained event |

***

### AI Audio Design Brief

All AI sounds nên được directional (3D spatialized) và nhất quán với the distances in [Movement & Stamina](Movement_and_Stamina.md). chính SFX yêu cầu:

| Sound                                        |                            Audible at                           | Priority                                   |
| -------------------------------------------- | :-------------------------------------------------------------: | ------------------------------------------ |
| Scav chatter (idle talk, mumbling)           |                               20m                               | Medium — ambient immersion                 |
| Suspicious exclamation ("What was that?")    |                               30m                               | High — người chơi cảnh báo signal               |
| Aggro shout (voice line)                     |                               40m                               | Critical — alert người chơi to AI seeing them |
| AI gunfire                                   |                               80m+                              | Critical — phải được directional             |
| Radio crackle (Sec-Force reinforcement call) |                               25m                               | High — warns người chơi of incoming            |
| Boss audio tell (unique per boss)            |                              100m+                              | Critical — announces boss presence         |
| Grenade pin-pull (Rogue PMC)                 |                               15m                               | High — survival critical signal            |
| AI movement sounds (footsteps)               | per [Movement & Stamina](Movement_and_Stamina.md) surface bảng | High                                       |

***

### Anti-Frustration Rules

To prevent AI from feeling unfair hoặc cheap, the following design limits apply:

| Rule                               | chi tiết                                                      | Reason                                       |
| ---------------------------------- | ----------------------------------------------------------- | -------------------------------------------- |
| No perfect aim thông qua smoke       | AI accuracy drops 80% inside smoke                          | Smoke is a valid counter                     |
| No instant headshots               | AI requires 1 frame of target acquisition trước first shot | Prevents instant one-shot on first detection |
| No shooting thông qua walls          | AI only shoot at confirmed LOS targets                      | Same LOS rules as người chơi                    |
| 10-second invulnerability at spawn | người chơi-as-Scav gets 10s                                     | Matches PMC spawn protection                 |
| Dead AI stay dead                  | No respawn within same raid                                 | Rewards area clearing                        |
| Alert trạng thái thời gian out (20–30s)     | AI return to Unaware nếu người chơi hides                        | Stealth remains viable recovery option       |
| Boss areas pre-announced           | Boss audio cue at 100m trước người chơi enters zone            | Người chơi có thể prepare, not blindly stumble     |

***

### Summary of chính quyết định

| Topic                | quyết định                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| **AI respawn**       | No respawn within a raid. Dead AI stay dead.                                                      |
| **AI detection**     | Sound-primary, vision-secondary. Vision cone limited by design for stealth viability in top-down. |
| **AI communication** | Zone-local communication. Not global alerts.                                                      |
| **Boss count**       | 1–2 boss spawns per map. 3 boss types at launch.                                                  |
| **người chơi-as-Scav**   | Separate zero-chi phí mode với karma hệ thống. 20-min cooldown.                                       |
| **Faction AI**       | Do not fight each other. Aggro only người chơi of any faction.                                       |
| **Grenade usage**    | Rogue PMC only at launch. Future expansion may add Militia grenades.                              |

***

### AI Production Contract

Các bảng enemy hiện có mô tả roster. Section này định nghĩa contract chung mà mọi enemy, boss hoặc event AI mới phải đáp ứng trước khi đưa vào raid.

#### AI System Model

| Entity | Trách nhiệm bắt buộc |
| :--- | :--- |
| `EnemyAgent` | Actor runtime có health, equipment, faction, threat tier và intent hiện tại |
| `Faction` | Quyết định patrol territory, visual/audio identity, loot profile và ally rule |
| `ThreatTier` | Giới hạn accuracy, armor, coordination, reinforcement và reward |
| `DetectionState` | Unknown, suspicious, alerted, visual contact, searching hoặc de-escalating |
| `AlertState` | Lan truyền alert theo local với source, age, confidence và expiry |
| `PatrolRoute` | Vùng di chuyển và anchor bị giới hạn, không search toàn map |
| `CombatIntent` | Hold, advance, suppress, flank, retreat, investigate, heal hoặc call support |
| `ReinforcementRequest` | Request theo faction có cooldown, distance, cap và reason |
| `BossEncounter` | Owner, phase rule, arena boundary, reward profile và reset policy |
| `AIRewardProfile` | Loot source, tier, economy value và anti-farming limit |
| `PlayerAsScavState` | Spawn context, objective, extraction rule và reputation impact |

#### Enemy Role Và Counterplay Contract

Mỗi role phải có gameplay purpose, range/threat profile, detection, movement/cover behavior, combat behavior, counterplay, loot contribution và audio/visual tell. Basic scavenger, patrol guard, objective guard, elite/rogue, boss crew, event AI và Player-as-Scav đều phải đáp ứng contract này.

Không role nào được tạo độ khó chỉ bằng hidden accuracy hoặc damage cao hơn. Difficulty phải đến từ positioning, timing, coordination, resource pressure hoặc route control có thể đọc được.

#### Detection Và Alert Rules

- Detection dùng sight, hearing và contextual evidence; AI không biết vị trí player nếu không có source hợp lệ.
- Sound event phải có source type, vị trí không chắc chắn, age và intensity; AI điều tra một vùng hợp lý thay vì snap thẳng tới player.
- Alert propagation có giới hạn theo faction, distance và expiry.
- Mất line of sight chuyển AI sang search có thời lượng giới hạn, không tracking vĩnh viễn.
- Reinforcement có cooldown, local cap, travel time và audio/visual signal.
- Spawn protection, reconnect recovery và safe interaction không bị ngắt bởi hidden aggro tức thời.

#### Combat Readability Contract

Player phải nhận biết được vì sao pressure tăng. AI phải có feedback cho detection, search, reinforcement, suppression, flank, retreat, heal, boss phase change và mất target bằng ít nhất hai trong audio, animation, VFX, world-space message hoặc HUD. Hidden difficulty modifier không thay thế tell.

#### AI Loot Và Economy Rules

- Faction và role chọn loot profile có giới hạn; AI không tạo item ngoài faucet đã cấu hình.
- Boss và event reward phải có risk, exposure hoặc objective cost rõ ràng và không tạo paid combat power.
- AI reward farming bị giới hạn bằng spawn, repeat-kill hoặc session cap khi cần.
- Loot tuân theo item lifecycle canonical và được server reconcile khi death, extraction, rollback hoặc disconnect.

#### Anti-Frustration Và Exploit Rules

- Không spawn enemy trong active interaction, extraction hold hoặc protected reconnect state.
- Giới hạn cross-zone aggro, reinforcement chain và số threat tier cao đồng thời.
- Có cooldown cho repeated pressure và recovery route sau khi squad disengage.
- Movement, damage, loot và reward của AI phải được validate server-side.

#### AI Telemetry Và QA

Theo dõi time to first threat, detection false positive/negative, reinforcement frequency/chain length, player death reason, boss completion/escape, AI loot value, repeat-kill farming và frustration report. Mỗi AI feature mới phải có role, counterplay, detection tell, reward profile, failure behavior và telemetry owner.

### Tham Chiếu Chéo

* [cốt lõi Gameplay Loop](CoreLoop.md) — Scav Mode economy faucet, AI in infiltration phase.
* [Environmental Hazards](Environmental_Hazards.md) — Boss spawn conditions, Scav Raid wave event.
* [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) — AI detect using same LOS rules as người chơi.
* [Movement & Stamina](Movement_and_Stamina.md) — Sound ranges that AI hearing reacts to.
* [Camera hệ thống](Camera_System.md) — AI detection arc hiển thị rõ to người chơi in top-down view.
* [Extraction cơ chế](Extraction_Mechanics.md) — Scav cooperative extraction và trust cơ chế.
* [Hero Abilities](Hero_Abilities.md) — Motion Sensor và Drone interact với AI alert trạng thái.
* [Story](https://github.com/oaiba/ExtractionDocument/blob/main/content/Story/README.md) — Faction lore và world context for AI địch factions.
