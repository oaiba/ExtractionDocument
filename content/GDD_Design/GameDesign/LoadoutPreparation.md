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
| PC layout | Multi-column workbench |
| Mobile layout | Tabbed flow with persistent summary |
| Deploy gate | Block only critical invalid states |

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

## Mobile Layout

Mobile uses tabs because a full stash workbench cannot remain readable on small screens. The persistent summary is critical: even while editing a weapon or moving items, the player should still see total value, weight, and deploy readiness.

| Tab | Content | Persistent Element |
| :--- | :--- | :--- |
| Operator | Character, ability, armor slots | Loadout value |
| Gear | Weapons, ammo, meds, backpack | Weight and warning |
| Stash | Inventory grid and filters | Quick equip actions |
| Mission | Mode, map, quests | Deploy readiness |
| Squad | Party, voice, ready state | Deploy button |

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

## Presets

Presets should accelerate common intentions without removing player authorship. A budget kit helps after losses, a standard kit supports reliable raids, and objective presets reduce forgetfulness. Presets should be editable after selection so players learn rather than blindly accept.

| Preset Type | Purpose |
| :--- | :--- |
| Budget | Low-risk recovery and practice |
| Standard | Balanced raid kit |
| Objective | Quest-specific gear |
| Squad Role | Team role kit such as scout, medic, anchor |
| Custom | Player-defined saved loadout |

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
| Core raid loop | [Core Gameplay](coregameplay.html) |
| Insurance | [Insurance System](insurancesystem.html) |
| Economy and gear value | [Economy](economy.html) |
| Controls and mobile input | [Controls](controls.html) |
| Map and mode choice | [Map Design](mapdesign.html), [Game Modes](gamemodes.html) |
