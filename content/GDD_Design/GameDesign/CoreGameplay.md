---
title: "Core Gameplay Mechanics - Deep Dive"
type: docs
---

## Overview

Core Gameplay owns the complete raid loop: preparation, deployment, looting, combat, extraction, loss, recovery, and post-match rewards. It defines the experience-level rules and links out to specialist pages for controls, loadout UI, economy, insurance, and maps.

The core fantasy is not "win every fight." It is "make a better decision than the raid is trying to force out of you." A good run should create several moments where the player stops and weighs information: the sound of gunfire, the value in the backpack, the time left, the squad's health, and the route to extraction. The system should reward discipline as much as aggression.

Every raid should tell a small story. A cautious player can survive by reading the map and leaving early. An aggressive squad can build value through combat, but must accept that every extra fight narrows the path home. A new player should understand why they died; an expert player should see three better decisions they could have made.

## Key Decisions

| Decision | Direction |
| :--- | :--- |
| Match type | PvPvE extraction raid |
| Target raid length | 10-15 minutes |
| Target session length | 25-40 minutes, usually 2-3 raids |
| Primary skill | Tactical decision making, map knowledge, risk reading |
| Primary tension | Brought gear and found loot can be lost before extraction |
| Safety net | Account progress, stash items, quest progress, and secured items persist |

## Raid System Model

Core Gameplay owns the raid outcome contract. Specialist pages can tune combat, economy, inventory, maps, UI, and matchmaking, but they should not redefine what a raid is, what the player risks, or how an outcome is resolved.

| Entity | Definition | Design Owner |
| :--- | :--- | :--- |
| `RaidSession` | One server-authoritative match instance from matchmaking lock to result reconciliation | Core Gameplay |
| `RaidPhase` | Current phase of the loop: preparation, matchmaking, loading, spawn, route, execution, extraction, recovery | Core Gameplay |
| `Spawn` | Initial player entry state: map edge, squad position, nearby threat, extraction options | Maps / Matchmaking |
| `Objective` | Player-selected or system-assigned goal that gives direction beyond looting | Quest / Game Modes |
| `LootState` | Current value, FIR status, protected items, inventory pressure, and stash transfer result | Inventory / Economy |
| `ThreatState` | Readable danger from AI, players, sound, objectives, hotspots, and extraction pressure | Gameplay |
| `ExtractionPoint` | Escape route with availability, activation rule, timer, contest rule, and outcome code | Extraction |
| `RaidTimer` | Match clock that controls urgency, late-raid behavior, and timeout failure | Core Gameplay |
| `DeathState` | KIA, downed, revived, executed, disconnected, or MIA outcome before reconciliation | Combat / Extraction |
| `FailState` | Any non-extracted result, including death, timeout, disconnect expiry, or invalid session | Core Gameplay |
| `RewardState` | XP, quest progress, loot transfer, insurance scheduling, and post-raid grants | Progression / Inventory |
| `SquadState` | Party membership, alive/downed/extracted state, partial extraction, and reconnect state | Matchmaking / Social |

## Full Raid Loop Contract

The full raid loop is longer than the in-match timer. A run starts when the player commits risk and ends when they understand the outcome and have a practical next action.

| Step | Phase | Player Commitment | System Contract | Exit Condition |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Loadout commit | Gear, operator, objective, insurance, squad, and mode | Validate readiness and summarize risk | Deploy confirmed |
| 2 | Matchmaking | Time and squad readiness | Find a valid pool without hiding mode rules | Server reserved |
| 3 | Loading | Attention and anticipation | Show map, region, squad, risk tip, reconnect-safe transition | Spawn ready |
| 4 | Spawn / orientation | First route choice | Provide map, extracts, objective, local threat, and squad status | Player leaves spawn pocket |
| 5 | Route choice | Safety vs value | Make routes readable through map, audio, loot density, and objective signals | Player commits direction |
| 6 | Loot / objective / combat | Exposure for value | Pair reward with danger, travel cost, or noise | Player gains value or loses tempo |
| 7 | Extraction decision | Bank value or push deeper | Keep extract options readable and time pressure honest | Extract selected or timer forces action |
| 8 | Extraction hold / contest | Final vulnerability | Resolve activation, interruption, squad state, and contest rules clearly | Extracted, interrupted, or killed |
| 9 | Outcome reconciliation | Trust in result | Resolve loot, XP, quest, FIR, insurance, death, and reconnect rules server-side | Debrief data ready |
| 10 | Debrief / recovery | Learning and next action | Explain what happened, what changed, and what to do next | Stash, redeploy, or recovery mode |

## Raid Loop

The raid loop is intentionally short enough for mobile sessions but dense enough to support mastery. Preparation creates commitment, the match creates tension, and the post-match phase converts the result into learning and progression. The loop should never feel like a disposable arcade match because the player always brings something into the raid and always carries a consequence out.

| Step | Action | Result |
| :--- | :--- | :--- |
| 1 | Prepare loadout | Player commits gear, operator, objective, map, and risk level |
| 2 | Deploy to zone | Squad enters the raid with assigned extraction options |
| 3 | Scout and choose route | Player reads map, audio, squad pings, and nearby loot |
| 4 | Loot, fight, or avoid | Player chooses value, safety, or pressure |
| 5 | Decide whether to extract | Safe choice banks current value; risky choice seeks more value |
| 6 | Resolve extraction | Successful extraction banks loot and XP; failure causes raid inventory loss |
| 7 | Rebuild or upgrade | Player repairs, sells, upgrades, re-equips, and queues again |

## Player Intent Per Phase

Every phase needs a clear player question. If the UI or systems do not answer that question, players must guess, and guesswork makes loss feel arbitrary.

| Phase | Player Intent | Required Information | Primary Decision | Common Failure |
| :--- | :--- | :--- | :--- | :--- |
| Preparation | Build a plan worth risking | Loadout validity, mode rules, insurance, objective, squad readiness | How much value to bring | Deploying with missing ammo, low durability, or unclear objective |
| Matchmaking | Trust that the queue is fair enough | Queue type, region, cancel state, squad ready state | Wait, cancel, or adjust party | Hidden rule mismatch or unclear long queue |
| Loading | Understand where and why they are going | Map, weather, squad, tip, server region | Mentally prepare route | Loading with no tactical context |
| Spawn | Get oriented without instant punishment | Spawn location, extracts, objective marker, nearby cover | Move, scout, or regroup | Spawn confusion or early unfair death |
| Route | Choose safety, value, or objective speed | Loot density, sound, timer, squad health, route risk | Avoid, flank, push, or loot | Following a route with no risk read |
| Execution | Convert opportunity into value | Enemy cues, container value, objective status, ammo/health | Fight, loot, disengage, or reposition | Greed after tempo is lost |
| Extraction | Bank value before risk exceeds reward | Extract distance, timer, noise, contest risk, squad state | Leave now or continue | Waiting too long or misreading extract rules |
| Recovery | Learn and re-enter the loop | Lost/kept items, XP, quest, insurance, death cause | Rebuild, sell, claim, or redeploy | Debrief does not explain the consequence |

## Risk / Reward Rules

Risk should feel self-chosen. The game can pressure players, but it should rarely surprise them with a consequence that was impossible to read.

| Risk Driver | Increases When | Player-Facing Tell | Reward Pairing |
| :--- | :--- | :--- | :--- |
| Time in raid | Raid timer advances and safe routes close | Timer color, ambient pressure, late-raid VO, extract distance | Better contested loot and late objective windows |
| Loot value | Backpack value rises or rare items are carried | Value summary, rarity/FIR badges, weight changes | Higher sell, quest, craft, or progression value |
| Noise | Gunfire, sprinting, alarms, extraction calls, heavy gear | Audio falloff, ping, map notification where applicable | Faster looting, combat opportunity, or extraction progress |
| Weight | Inventory and armor exceed thresholds | Movement penalty, stamina drain, weight warning | More value carried home |
| Distance to extract | Route crosses hotspots or open sightlines | Extract marker, route danger, known sound zones | More time to gather value before leaving |
| Squad health | Teammates are downed, split, low on meds, or disconnected | Squad status, revive timer, reconnect state | Team survival, revive XP, shared extraction |
| Objective commitment | Player carries quest item or enters objective zone | Objective badge, extraction requirement, loss warning | Quest progress, reputation, unlocks |

Rewards must not be free of exposure. If a reward has no travel cost, sound cost, time cost, resource cost, or combat risk, it should be low value, tutorial-only, or explicitly capped.

## Pre-Match Phase

The pre-match phase is a deliberate ritual. The player should understand the risk they are choosing before pressing Deploy.

This phase should feel like loading a weapon before opening a dangerous door. The UI must surface the practical questions quickly: what is the objective, what is at risk, what can be protected, and what is the escape plan. It should avoid spreadsheet fatigue by summarizing risk clearly and pushing deep inventory work into the loadout screen.

| Step | Player Question | Canonical Detail |
| :--- | :--- | :--- |
| Select objective | What am I trying to accomplish this raid? | [Game Modes](gamemodes.html) |
| Select operator | Which ability and role fits the goal? | Character docs |
| Build loadout | How much am I willing to risk? | [Loadout Preparation](loadoutpreparation.html) |
| Choose insurance | Which items deserve recovery protection? | [Insurance System](insurancesystem.html) |
| Choose map and squad | Where are we going, and with whom? | [Map Design](mapdesign.html), [Communication](communication.html) |
| Confirm deploy | Does the expected reward justify the risk? | This page |

## In-Match Phase

The in-match phase is built around rising pressure rather than a shrinking battle royale circle. Players should feel that the map is becoming more expensive to stay in: better loot, fewer safe paths, louder information, and more contested exits. The timer is a design tool for commitment, not a punishment for exploration.

| Time Window | Phase | Design Intent | Pressure |
| :--- | :--- | :--- | :--- |
| 0-3 min | Spawn and orientation | Let squads read map, objective, extraction options | Low |
| 3-7 min | Edge loot and route choice | Offer safe value and early decisions | Rising |
| 7-11 min | Hotspot pressure | Create player collision around value | High |
| 11-14 min | Extraction contest | Force commitment and route discipline | Very high |
| 15 min | Match end | Prevent endless looting and camping | Extreme |

## Combat And Looting Rules

Combat and looting are paired systems. Loot creates the reason to move, sound creates the evidence that someone moved, and combat decides whether the player can keep what they found. The best fights should begin before bullets are fired, through route choice, sound discipline, cover selection, and timing.

| System | Rule | Why It Matters |
| :--- | :--- | :--- |
| Combat | Positioning and cover should matter more than raw aim speed | Supports top-down mobile tactics |
| TTK | Fast enough to punish mistakes, slow enough for counterplay | Avoids both arcade sponge combat and instant frustration |
| Loot value | Value increases with danger and travel cost | Makes route planning meaningful |
| Sound | Gunfire, footsteps, alarms, and extraction cues create risk information | Turns audio into tactical data |
| AI | AI protects value, reveals player position, and creates pressure | Avoids empty loot runs |
| Extraction | Extraction must be readable, interruptible, and risky | Makes the final choice memorable |

## Greed Loop

The greed loop is the emotional center of extraction play. The game should keep asking "is this enough?" without forcing one correct answer. If the player extracts early, the result should feel smart rather than boring. If they push deeper, the reward should be visible enough that the risk feels self-chosen.

| Current State | Player Temptation | Safe Choice | Risk Choice | Outcome |
| :--- | :--- | :--- | :--- | :--- |
| Player has valuable loot | Extract now or push deeper | Leave and bank value | Continue toward more loot | Safe value vs. increased pressure |
| Extraction is nearby | "One more container" | Commit to extraction | Delay extraction | Relief vs. possible regret |
| Rare opportunity appears | Fight, loot, or avoid | Avoid and preserve kit | Contest value | Memorable win or meaningful loss |
| Player dies | Blame or learn | Review death recap | Rebuild without learning | Better next decision or repeated mistake |

## Death, Extraction, And Recovery

Loss is allowed to hurt, but it should not feel opaque. A failed raid must clearly explain what was lost, what was preserved, what can be recovered through insurance, and what the player can do next. The goal is regret that teaches, not frustration that ends the session.

| Outcome | Lost | Preserved | Follow-Up |
| :--- | :--- | :--- | :--- |
| Successful extraction | Consumables used during raid | Found loot, XP, quest progress, insured item status | Sell, stash, upgrade, queue next raid |
| Death in raid | Brought gear, backpack loot, unprotected items | Account XP, stash at home, secure container contents, quest knowledge | Death recap, insurance wait, rebuild |
| Timeout | Treated as failed extraction | Account progress and protected systems | Clear warning and recap |

## Raid Outcome Matrix

Outcome reconciliation must be deterministic and server-authoritative. The debrief can simplify presentation, but the backend state vocabulary should remain stable.

| Outcome | Result Code | Loot Result | Progress Result | Player Message |
| :--- | :--- | :--- | :--- | :--- |
| Successful extraction | `EXTRACTED` | Extracted items transfer to stash; consumables remain consumed | XP, quest, FIR, and reward rules apply normally | "Extracted. Loot secured." |
| Killed in raid | `KIA` | Equipped and backpack items lost unless protected or later insured | Account XP and allowed quest progress apply | "Killed in action. Review how you died." |
| Timer expired | `MIA_TIMEOUT` | Treated as failed extraction; secure/protected rules still apply | Limited progress only where rules allow | "Missing in action. You did not extract before time expired." |
| Disconnect unresolved | `MIA_DISCONNECT` | Slot held during reconnect window, then failed extraction if unresolved | No extra penalty beyond normal MIA rules | "Connection lost. Reconnect window expired." |
| Server rollback | `SERVER_ROLLBACK` | Return to pre-raid loadout snapshot | No raid rewards; compensation may be granted separately | "Raid could not be validated. Gear restored." |
| Squad partial extraction | `PARTIAL_EXTRACT` | Extracted members bank loot; remaining members continue risk | Each player resolves independently | "Squadmate extracted. Your raid continues." |
| Objective complete, failed extract | `OBJECTIVE_UNSECURED` | Objective item lost unless protected; progress depends on objective rule | Non-extraction objectives may persist if explicitly marked | "Objective progress requires extraction." |

## Post-Match Flow

| Step | Extracted Run | Failed Run |
| :--- | :--- | :--- |
| 1 | Show loot summary | Show death recap |
| 2 | Apply XP and quest updates | Apply XP, quest, and lesson feedback |
| 3 | Move extracted loot to stash | Mark lost, protected, and insured items |
| 4 | Suggest sell, upgrade, or redeploy | Suggest rebuild, claim insurance later, or recovery mode |

## Advanced Mechanics

Advanced mechanics should add expressive decisions without changing the basic promise of the raid. Squad tools, insurance, ranked rules, and information systems are all support layers around the same question: how much risk can the player read, carry, and escape with?

| Mechanic | Purpose | Detail Owner |
| :--- | :--- | :--- |
| Squad coordination | Give teams shared information without removing tension | [Communication](communication.html) |
| Information warfare | Make sensors, pings, and sound meaningful | [Navigation & Map](navigationandmap.html) |
| Insurance | Reduce loss frustration without deleting risk | [Insurance System](insurancesystem.html) |
| Ranked rule changes | Preserve competitive integrity | [Ranked Mode](rankedmode.html) |
| Scavenger runs | Provide low-stakes recovery and practice | [Game Modes](gamemodes.html) |

## Player Experience Examples

A solo player enters with a budget rifle and one objective item. They avoid the first hotspot, loot edge containers, hear gunfire near mid-map, and decide to extract early with moderate value. This is a successful low-risk story: the player exercised discipline and learned a route.

A trio enters with strong armor and a rare key. They contest a hot zone, win the fight, but lose healing and time. Their next decision is not "keep fighting because we are winning"; it is whether the key room reward is worth crossing the map with damaged gear and a loud footprint.

A new player dies after opening a container near an obvious sightline. The recap should connect the death to a readable cause: enemy angle, sound cue, exposed looting position, or missing extraction timing. The next action should be practical, such as trying a safer route or equipping smoke.

## Edge Cases And Anti-Frustration

- If a player disconnects during a raid, reconnect should be prioritized over immediate loss resolution.
- If a player dies to timeout, the recap should show timer warnings and last known extraction distance.
- If a squadmate extracts alone, remaining squad members continue under normal risk rules.
- If a player dies while interacting with extraction, the UI should clearly show whether the extraction completed.
- If a quest objective is completed but the player dies, quest rules must state whether progress requires extraction.
- If matchmaking places a new player into a harsh lobby, onboarding protection should reduce extreme early failures.

## Core Tuning Knobs

- Raid timer controls urgency; shorten it only if routes and extracts remain readable.
- Loot value controls greed; increase hotspot value only with matching danger and exit pressure.
- AI density controls pacing; use AI to guard value and create sound, not to replace PvP tension.
- Extraction timer controls final commitment; tune it alongside cover, sightlines, and audio tells.
- Secure container size controls loss pain; larger protection reduces gear fear and economy risk.
- Death recap detail controls learning; more clarity can reduce frustration without reducing stakes.

## Metrics

Metrics should be read as design health signals, not fixed truths. If extraction rate rises but players report boredom, the maps may be too safe. If death rate rises and players cannot explain why, readability is failing. Balance work should combine telemetry with death recap feedback and session surveys.

| Metric | Target | Notes |
| :--- | :--- | :--- |
| Overall extraction rate | 30-40% | Tune by skill bracket and mode |
| Beginner extraction rate | 20-30% | Tutorial and protected queues should support learning |
| Average raid length | 10-15 minutes | Avoid PC-scale session bloat |
| Menu time per session | Under 20% | Loadout prep should feel meaningful, not slow |
| Death recap usefulness | High qualitative score | Players should know what to improve |

## Raid Telemetry

Telemetry should explain whether the loop is readable, not just whether players win or lose.

| Signal | Question Answered |
| :--- | :--- |
| Phase duration by skill bracket | Where do players stall, rush, or disengage? |
| Spawn-to-first-contact time | Are spawns fair and readable? |
| Hotspot collision rate | Are valuable zones creating the intended conflict? |
| Loot value carried vs extracted | Is greed pressure working without feeling futile? |
| Extraction activation / interruption / success rate | Are extraction contests dramatic but not impossible? |
| Death reason clarity rating | Do players understand why they lost? |
| Disconnect reconnect success rate | Are technical failures separated from gameplay loss? |
| Tutorial completion to first standard raid | Does onboarding convert into real play? |

## Core Gameplay QA Checklist

- A new player can explain the raid goal after one tutorial and one debrief.
- Every deploy path shows mode rules, gear loss, insurance, squad, map, and objective before queue start.
- Every extraction outcome has a stable result code and a clear player-facing message.
- Death, MIA, disconnect, partial extraction, and server rollback never share ambiguous copy.
- Valuable rewards require exposure through time, sound, travel, resources, or combat risk.
- Quest and loot progress clearly state whether extraction is required.
- Reconnect is attempted before unresolved disconnects become MIA.
- Debrief always gives at least one practical next action: redeploy, rebuild, claim, sell, repair, or learn.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Loadout UI | [Loadout Preparation](loadoutpreparation.html) |
| Input and camera | [Controls](controls.html) |
| Map routes and extraction placement | [Map Design](mapdesign.html) |
| Insurance rules | [Insurance System](insurancesystem.html) |
| Economy impact | [Economy](economy.html) |
| Onboarding | [Tutorial Raid](tutorialraid.html) |
