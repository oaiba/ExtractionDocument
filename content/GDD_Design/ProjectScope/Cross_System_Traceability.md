---
title: Cross-System Traceability
linkTitle: Traceability Matrix
type: docs
weight: 9
---

## Purpose

This matrix maps the primary player journey to its gameplay owner, state presentation, failure behavior, telemetry, and canonical references. It is a consistency tool, not a replacement for detailed system specifications.

## Ownership Boundaries

| Domain | Owns | Does not own |
| :--- | :--- | :--- |
| Core Gameplay | Raid phases, risk, extraction, and outcome | Item storage implementation or UI layout |
| AI | Detection, threat, reinforcement, AI loot profile | Player reward reconciliation |
| Combat / Weapons | Damage, armor, TTK, weapon feedback | Commerce entitlement rules |
| Inventory | Item instances, ownership, placement, lifecycle | Currency balance tuning |
| Economy | Sources, sinks, prices, inflation, recovery | Screen presentation |
| Progression | XP, unlocks, reward tracks, claim states | Platform checkout |
| Commerce | Offers, entitlement, checkout, receipt, support route | Combat-power gear progression |
| UI/UX | Layout, input, focus, state communication, accessibility | Server authority or balance values |
| Technical GDD | Event names, data contracts, service constraints | Player-facing design intent |

## Player Journey Matrix

| Player Action | Gameplay Owner | UI Surface | Required State | Failure Behavior | Telemetry | Canonical References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Account entry | Settings/System | Login, setup, tutorial gate | loading, linked, blocked, offline | show reason and recovery route | auth success/failure | [Settings/System](../UI_UX/Commerce_Settings_System_Screens.md) |
| Tutorial | Core Gameplay | Tutorial HUD and debrief | checkpoint, hint, pass, retry | reset checkpoint without permanent loss | tutorial conversion | [Tutorial Raid](../GameDesign/TutorialRaid.md) |
| Home / preparation | Core Gameplay | Home, loadout, stash | valid, pending sync, blocked | keep deploy unavailable with reason | home impression, deploy intent | [Out-of-Raid](../UI_UX/Out_Of_Raid_Screens.md) |
| Loadout commit | Inventory / Economy | Loadout Workbench | ready, warning, blocker | explain missing/incompatible item | blocker frequency | [Loadout Preparation](../GameDesign/LoadoutPreparation.md) |
| Matchmaking | Matchmaking | Lobby, queue, loading | queued, found, reconnecting | retry, leave queue, fallback | queue time, cancel, reconnect | [Matchmaking](../Gameplay/Matchmaking_Lobby.md) |
| Spawn / orientation | Core Gameplay / AI | HUD, loading | spawn protected, active | recover or rollback invalid spawn | spawn-to-action time | [Core Gameplay](../GameDesign/CoreGameplay.md) |
| Loot | Inventory / Economy | Looting overlay, item detail | available, protected, FIR, full | overflow or decline with clear reason | loot interaction, pickup failure | [Looting](../Gameplay/Looting_Interactions.md) |
| Combat | Combat / AI | HUD, hit feedback | damage, armor hit, suppression, downed | show readable cause and next option | hit, death reason, TTK | [Weapons](../Combat/Weapons.md) |
| Objective | Progression / Core Gameplay | Objective tracker | active, complete, extraction-required | preserve or remove progress by rule | objective completion | [Quest Objectives](../Gameplay/Quest_Objective_System.md) |
| Extraction | Core Gameplay | Extraction UI | available, holding, contested, blocked | clear cancel/contest/outcome state | extraction attempt/result | [Extraction](../Gameplay/Extraction_Mechanics.md) |
| Death / success | Core Gameplay / Inventory | Debrief, death replay | extracted, KIA, MIA, rollback | deterministic reconciliation | outcome reason | [Post-Game Debrief](../Gameplay/Post_Game_Debrief.md) |
| Loot transfer | Inventory / Economy | Loot transfer, stash, inbox | accepted, overflow, pending | retry or support without duplication | transfer success/failure | [Inventory System](../Inventory_System/_index.md) |
| Reward claim | Progression / LiveOps | Reward inbox, battle pass, event | claimable, claimed, expired, converted | preserve source and support path | claim funnel | [Progression/LiveOps](../GameDesign/Progression.md) |
| Commerce purchase | Commerce | Shop, confirmation, receipt | confirm, provider pending, success | do not double charge; support route | purchase funnel | [Commerce Screens](../UI_UX/Commerce_Screens.md) |
| Redeploy | Core Gameplay / Inventory | Home, loadout | ready, blocked, recovery | return to first actionable blocker | redeploy conversion | [Pre-Raid](../UI_UX/Pre_Raid_Screens.md) |

## Traceability Review Rules

- Every player-facing blocker must have an owner, readable reason, and next action.
- Every persistent item or reward state must have one authoritative lifecycle owner.
- Every analytics event must correspond to a player action or system transition.
- Any cross-domain rule must link to this matrix and both owning source documents.
- A route is not complete until success, failure, offline, reconnecting, and pending states are mapped.

## Review Checklist

- [ ] No gameplay rule is owned only by a UI page.
- [ ] No UI state lacks a gameplay, economy, inventory, or service source.
- [ ] Raid outcome, reward, item, and progression states reconcile deterministically.
- [ ] Commerce never grants combat-power item instances.
- [ ] English and Vietnamese pages use the same ownership boundaries.

## Cross-References

- [Design Decision Register](Design_Decision_Register.md)
- [MVP Readiness Review](MVP_Readiness_Review.md)
- [Screen Groups Overview](../UI_UX/Screen_Groups_Overview.md)
