---
title: "Home Screen & Main Lobby Design"
type: docs
weight: 16
---

## Overview

The Home Screen is the player's out-of-raid command center. It should show identity, current goals, squad readiness, live events, and the fastest route back into a raid.

The screen should feel like a tactical staging area, not a marketing billboard. The operator, current kit, active goals, and deploy path are the primary story. Store, events, news, and social hooks can be present, but they must not compete with the player's next raid decision.

A strong Home Screen answers four questions in under five seconds: who am I playing, what can I do next, what has changed since last session, and how do I deploy?

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Primary emotion | Readiness and tension before deployment |
| Main focus | Operator showcase plus Deploy path |
| Secondary focus | Progress, events, squad, stash reminders |
| Layout standard | PC/Console landscape: operator center, navigation rail, contextual panels |

## Operator Showcase States

The operator showcase gives the player a visible identity between raids. It should react to state changes without wasting time: ready posture when the loadout is valid, restrained celebration after extraction, and grounded recovery after death. The tone is tactical confidence, not cartoon celebration.

| State | Trigger | Next State |
| :--- | :--- | :--- |
| Idle | Player rotates or taps operator | Inspect |
| Idle | Loadout becomes valid | Ready |
| Ready | Deploy pressed | Matchmaking |
| Matchmaking | Server match ready | Match Found |
| Matchmaking | Queue cancelled | Idle |
| Match Found | Player accepts or timer completes | Deploying |
| Idle | Player returns after successful extraction | Return Victory |
| Idle | Player returns after death | Return Defeat |
| Return Victory / Return Defeat | Summary animation ends | Idle |

## PC / Console Layout

PC and console layouts can show more simultaneous information, but they should still preserve one dominant action. The right panel should lead toward deploy, while the rail and supporting widgets remain stable. Avoid moving navigation between sessions because muscle memory matters for repeated raid prep.

| Region | Content | Purpose |
| :--- | :--- | :--- |
| Center | Operator showcase, stance, selected skin, weapon preview | Identity and readiness |
| Left rail | Home, Armory, Stash, Safe House, Traders, Ranked, Shop, Settings | Stable global navigation |
| Right panel | Mode card, squad status, quick deploy, queue estimate | Fast path to play |
| Top bar | Currency, notifications, profile, season timer | Account state |
| Bottom strip | Last raid, active quests, event reminder | Contextual next actions |

## Navigation Flow

Navigation should support both deliberate preparation and fast return. A player who wants to tune gear can drill into stash and loadout. A player who just wants another run should move from Home to matchmaking with only the necessary risk confirmations.

| Destination | Entry Point | Purpose |
| :--- | :--- | :--- |
| Loadout | Deploy panel or navigation rail | Prepare gear, mode, map, and squad |
| Mode and map | Loadout flow | Select raid rules and destination |
| Squad readiness | Loadout flow | Confirm party state before queue |
| Matchmaking | Deploy confirmation | Find match using selected rules |
| Stash | Navigation rail | Manage inventory |
| Safe House | Navigation rail | Upgrade modules and claim returns |
| Traders | Navigation rail | Buy, sell, and turn in tasks |
| Profile | Top bar | Review identity and stats |
| Settings | Top bar or navigation | Configure game options |

## Deploy Panel Requirements

The deploy panel is the final trust checkpoint. It should highlight invalid states, summarize risk, and explain mode modifiers before the queue begins. It should not surprise the player after matchmaking has started.

| Field | Requirement |
| :--- | :--- |
| Selected mode | Always visible |
| Squad size | Always visible |
| Gear value | Visible before deploy |
| Insurance status | Visible if eligible items are uninsured |
| Quest suggestions | Show top 1-3 relevant goals |
| Queue estimate | Update periodically during matchmaking |
| Risk warning | Trigger if player deploys with unusually high value |

## News And Events

| Surface | Rule |
| :--- | :--- |
| Event banner | One primary event at a time |
| Patch notes | Link to readable detail, not modal overload |
| Daily goals | Show progress and time remaining |
| Deep links | Event cards must open the exact target screen |
| Dismissal | Dismissed news should not reappear until updated |

## Audio And Feedback

| State | Audio Direction |
| :--- | :--- |
| Idle | Low industrial ambience |
| Queue searching | Subtle tension layer |
| Match found | Short confirmation sting |
| Post-extraction | Brief relief cue |
| Post-death | Somber recovery cue |

## Home Screen Examples

A returning player after a successful extraction should see a short loot summary, current progression gains, and a clear path to redeploy. The screen should celebrate success briefly, then return control quickly.

A player after death should see recovery actions: rebuild from preset, check insurance, open stash, or run Scavenger. The tone should be calm and practical rather than punitive.

A first-session player should see Tutorial Raid as the primary action until the basics are complete. Store, ranked, and complex live events should stay secondary until the player has context.

## Layout Failure Cases

- If the store dominates the first screen, the game feels transactional instead of tactical.
- If deploy is hidden behind too many panels, session momentum drops.
- If last-raid state is invisible, success and failure feel disconnected from the lobby.
- If the navigation rail or context panels bury common actions, regroup them into the PC/Console landscape standard.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Deploy flow | [Loadout Preparation](loadoutpreparation.html) |
| Modes | [Game Modes](gamemodes.html) |
| Progress summary | [Progression](progression.html) |
| Events feed | [Live Operations](liveops.html) |
| Safe House | [Safe House Design](safe_house_design.html) |
| Settings | [User Settings](usersettings.html) |
