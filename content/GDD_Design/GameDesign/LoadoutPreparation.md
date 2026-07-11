---
title: "Pre-Raid Loadout & Preparation Screen"
type: docs
---

## Overview

Loadout Preparation is the ritual before risk. It must help players understand what they are bringing, what they can lose, which objective they are chasing, and whether the squad is ready.

This screen should make gear fear productive. The player should feel the weight of the decision without feeling trapped in inventory management. A good prep flow lets experts optimize quickly and lets newer players trust recommended warnings, presets, and objective hints.

The screen is also a communication surface for the squad. It should show who is ready, who lacks ammo or healing, who is over weight, and whether the selected mode changes insurance or loss rules.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Primary job | Make risk legible before deploy |
| Core surfaces | Operator, gear, stash, insurance, mode, map, squad |
| Layout standard | PC/Console multi-column workbench |
| Deploy gate | Block only critical invalid states |

## Loadout System Model

Loadout preparation turns inventory state into raid commitment. It must validate the physical kit, explain risk, and preserve player intent while preventing accidental deployment with missing critical gear.

| Entity | Definition | UI / Design Requirement |
| :--- | :--- | :--- |
| `Loadout` | The complete set of equipped operator, gear, accessible items, storage, mission context, and squad readiness | Shows readiness, value, weight, blockers, warnings, and deployment consequence |
| `GearSlot` | Any equipment position that accepts item instances | Names accepted categories, current item, durability/ammo where relevant, and lock reason |
| `RequiredSlot` | Slot or requirement that can block deploy | Must show missing/invalid reason and direct fix route |
| `OptionalSlot` | Slot that improves readiness but does not always block deploy | Uses advisory/warning language, not false blockers |
| `ValidationRule` | A deploy readiness check | Has severity, first blocker copy, direct fix, and platform-safe focus target |
| `RiskSummary` | Persistent summary of loadout value, weight, insurance, ammo, meds, quest items, and mode rules | Stays visible while browsing stash or presets |
| `Preset` | Saved or suggested kit configuration | Shows missing items, substitutions, cost, capacity result, and overwrite/delete confirmation |
| `InsuranceSelection` | Player choice to protect eligible item instances | Shows eligible/ineligible counts, cost, provider/rule, return timer, and mode restrictions |

## Loadout Flow

The flow is ordered from identity to commitment. Operator comes first because it shapes role and abilities. Gear and stash come next because they define risk. Mode, map, insurance, and squad readiness come last because they decide the context where that risk will be spent.

| Step | Action | Result |
| :--- | :--- | :--- |
| 1 | Choose operator | Ability, role, and character identity are set |
| 2 | Equip weapons and armor | Combat readiness and gear value update |
| 3 | Pack meds, tools, and backpack | Survival tools and carry capacity update |
| 4 | Select mode and map | Rules, extracts, and risk profile are set |
| 5 | Review insurance | Eligible items are protected or intentionally left uninsured |
| 6 | Squad ready check | Party voice, fill, and ready status are confirmed |
| 7 | Deploy | Matchmaking starts |

## PC / Console Layout

The PC/console layout can operate like a workbench: inspect the kit, manipulate inventory, and review mission context at the same time. The layout should reduce back-and-forth by keeping value, weight, and readiness visible while the player edits gear.

| Region | Content | Purpose |
| :--- | :--- | :--- |
| Left column | Operator, gear slots, weight, insurance status | Read loadout at a glance |
| Center column | Stash grid, filters, item details | Equip and manage items |
| Right column | Mode, map, quests, squad, deploy button | Commit to raid |
| Footer | Loadout value, risk warnings, preset controls | Keep risk visible |

## Loadout Summary

Warnings should be educational, not scolding. "No compatible ammo" is more useful than "invalid loadout." "High uninsured value" teaches risk. "Quest item missing" prevents wasted raids. Each warning should point to a direct fix.

| Signal | Display Rule |
| :--- | :--- |
| Gear value | Always visible before deploy |
| Weight | Show current and max carry weight |
| Ammo readiness | Warn if weapon has no compatible ammo |
| Healing readiness | Warn if no healing item is equipped |
| Insurance | Show insured, uninsured, and ineligible counts |
| Quest items | Highlight required equipment or objectives |

## Readiness Severity

| Severity | Deploy Behavior | Copy Rule | Examples |
| :--- | :--- | :--- | :--- |
| Blocker | Cannot deploy until fixed | Name the first blocker and focus the fix target | Missing primary weapon, invalid container item, squad/mode restriction |
| Warning | Can deploy after acknowledgement or confirmation | Explain risk and consequence without shaming | Missing meds, high uninsured value, low weapon durability |
| Advisory | Does not block or require confirmation | Teach optimization and suggest one action | Sidearm empty, low value-per-slot, recommended armor upgrade |

## Loadout Validation Matrix

| Validation | Severity | Required Behavior |
| :--- | :--- | :--- |
| Missing primary weapon | Blocker | Focus primary weapon slot and filter compatible weapons |
| Missing compatible ammo | Warning or blocker by mode | Show ammo caliber, required magazine/ammo count, and compatible filter |
| No meds | Warning | Suggest medical filter and budget med source |
| No extraction objective item | Warning or blocker by quest | Show quest, source, and stash/trader/map route |
| Overweight / critical weight | Blocker or warning by tuning | Show weight source, suggested removals, and movement penalty |
| Incompatible attachment | Blocker | Show incompatible node and valid replacements |
| Broken armor | Blocker if required protection rule applies | Route to repair, replacement, or remove item |
| Low durability weapon | Warning | Show malfunction/durability risk and repair route |
| Uninsured high value | Warning | Show uninsured value, eligible count, Insure All, and ineligible reasons |
| Invalid container item | Blocker | Show container rule: category, size, secure-container, contraband, or mode restriction |
| Quest item missing | Warning or blocker by selected objective | Show objective consequence and direct stash/quest route |
| Squad not ready | Blocker | Show which member is blocking and why |
| Mode restriction | Blocker | Show mode rule: gear tier cap, insured disabled, contraband forbidden, or ranked rule |

## Gear Comparison / Equip Decision

| Compare Input | Requirement |
| :--- | :--- |
| Slot compatibility | Show valid slots, conflicts, and required unequip/move actions |
| Stats delta | Compare class, durability, armor zones, ammo count, storage cells, access speed, weight, and mobility impact |
| Value impact | Show item value, loadout total value, sell/trader relevance, and insurance cost impact |
| Durability / repair | Show current/max durability, repair route, and effective performance impact |
| Risk flags | Show FIR, quest, protected, insured, contraband, locked, equipped, and high-value flags |
| Recommended action | Explain why Equip, Keep, Repair, Insure, Sell, or Do Not Deploy is recommended |

## Presets

Presets should accelerate common intentions without removing player authorship. A budget kit helps after losses, a standard kit supports reliable raids, and objective presets reduce forgetfulness. Presets should be editable after selection so players learn rather than blindly accept.

| Preset Type | Purpose |
| :--- | :--- |
| Budget | Low-risk recovery and practice |
| Standard | Balanced raid kit |
| Objective | Quest-specific gear |
| Squad Role | Team role kit such as scout, medic, anchor |
| Custom | Player-defined saved loadout |

### Preset Rules

| Rule | Requirement |
| :--- | :--- |
| Apply preview | Show all items that will be equipped, moved, bought, substituted, or left missing |
| Missing items | List missing items with source routes: stash, trader, craft, quest, or budget substitute |
| Substitutions | Name the substitute and explain what changed: ammo, armor class, storage capacity, weight, or value |
| Cost | Show credits, trader requirements, insurance delta, and stash capacity result before commit |
| Overwrite/delete | Require confirmation and show preset name |
| Squad role preset | Show intended role and minimum required items so squads understand readiness |
| Objective preset | Show quest objective, required items, FIR requirements, and extraction/map constraints |

## Insurance And Risk Rules

| Rule | Requirement |
| :--- | :--- |
| Eligible items | Show eligible count, cost, provider/rule, and return timer |
| Ineligible items | Show exact reason: item type, contraband, mode, equipped state, account rule, or already insured |
| High-value threshold | Warn when uninsured eligible value crosses tuning threshold |
| Mode-specific insurance | If selected mode changes insurance, show rule before Ready CTA |
| Insure All | Applies only to eligible selected/current loadout items and summarizes skipped items |
| Remove insured item | Requires confirmation if removing would change risk summary or insurance plan |
| Return expectation | Never imply guaranteed return if insurance design is probabilistic or conditional |

## Deploy Validation

| State | Behavior |
| :--- | :--- |
| Missing weapon | Block deploy |
| Missing ammo | Warn, allow only with explicit confirmation |
| Overweight | Block or force item removal |
| High gear value | Warn |
| No insurance | Warn if eligible items are present |
| Squad not ready | Wait until all required players ready |

## Preparation Examples

A player selects a budget preset after several failed raids. The screen should keep risk low, warn about missing healing, and suggest a route or mode that supports recovery.

A squad prepares for a high-value objective. The screen should show each member's readiness, squad size, selected map, uninsured value, and any mode rules that change extraction or insurance.

A player equips a quest item but forgets compatible ammo. The deploy gate should block or warn clearly and provide a direct path to the missing item filter.

## Preparation Failure Cases

- If players deploy without ammo by accident, validation is too weak.
- If players cannot tell why deploy is blocked, error messaging is too vague.
- If mobile stash editing requires too many screen changes, persistent summary and quick equip need improvement.
- If squads wait on one player without knowing why, readiness details should be more visible.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Core raid loop | [Core Gameplay](coregameplay/index.html) |
| Insurance | [Insurance System](insurancesystem/index.html) |
| Economy and gear value | [Economy](economy/index.html) |
| Controls and mobile input | [Controls](controls/index.html) |
| Map and mode choice | [Map Design](mapdesign/index.html), [Game Modes](gamemodes/index.html) |
