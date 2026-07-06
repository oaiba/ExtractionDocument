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

## Cross-References

| Topic | Page |
| :--- | :--- |
| Loadout UI | [Loadout Preparation](loadoutpreparation.html) |
| Input and camera | [Controls](controls.html) |
| Map routes and extraction placement | [Map Design](mapdesign.html) |
| Insurance rules | [Insurance System](insurancesystem.html) |
| Economy impact | [Economy](economy.html) |
| Onboarding | [Tutorial Raid](tutorialraid.html) |
