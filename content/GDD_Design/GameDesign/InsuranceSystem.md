---
title: "Insurance System Design"
type: docs
---

## Overview

Insurance softens gear loss without removing risk. It lets players pay before a raid for a chance to recover eligible items that were not extracted by another player.

Insurance is not a refund button. It is a promise that some losses may return later if the raid world allows it. The delay matters because the player still feels the consequence immediately, but the comeback path gives them a reason to log in, check the inbox, and rebuild instead of quitting after a bad streak.

The player-facing message must be honest: insured gear can still be lost if another player takes it. That uncertainty preserves gear fear and makes enemy looting meaningful.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Primary purpose | Reduce frustration after death while preserving gear fear |
| Purchase moment | Loadout Preparation |
| Return condition | Item must remain unlooted or recoverable after raid resolution |
| Return timing | Delayed inbox claim, not instant refund |
| Economy role | Credit sink and retention safety valve |
| Competitive rules | Ranked can restrict or disable insurance |

## Insurance Lifecycle

The lifecycle should be easy to understand at three moments: before the raid, after death, and when the inbox resolves. The player should never need to guess whether an item was uninsured, looted, pending, returned, blocked by stash space, or excluded by mode rules.

| Step | Event | Result |
| :--- | :--- | :--- |
| 1 | Player prepares loadout | Eligible items are shown |
| 2 | Player selects items and insurer | Cost and return time are previewed |
| 3 | Player pays insurance cost | Items are marked insured for the raid |
| 4 | Player deploys | Insurance waits for raid resolution |
| 5A | Player extracts with insured item | Insurance expires cleanly |
| 5B | Player dies and item is looted | Item is lost |
| 5C | Player dies and item is recoverable | Return timer starts |
| 6 | Timer completes | Item appears in Safe House inbox |
| 7 | Player claims item | Item returns to stash if space is available |

## Insurer Options

Insurers create a small strategic choice without becoming a complicated market. Budget players can protect common gear cheaply and wait longer. High-risk players can pay for faster recovery on key weapons or armor. More insurers can be added later, but launch should keep the comparison simple.

| Insurer | Positioning | Cost | Return Time | Strength |
| :--- | :--- | :--- | :--- | :--- |
| Viktor Kozlov | Salvage Corps recovery | Lower | Slower | Good for budget and standard gear |
| Ada Chen | Tech Syndicate priority recovery | Higher | Faster | Good for rare or tactical gear |

## Item Eligibility

Eligibility protects the economy from loopholes. Consumables, quest items, secure-container items, and cosmetics follow different risk rules, so they should not be treated like normal recoverable gear. The UI must explain unavailable insurance with short reasons, not disabled controls with no context.

| Item Type | Insurable | Notes |
| :--- | :--- | :--- |
| Weapons | Yes | Cost scales with base value and condition |
| Armor | Yes | Damaged gear returns damaged unless repaired separately |
| Backpack | Yes | Backpack returns empty if contents are not insured separately |
| Consumables | No | Used or lost as part of raid risk |
| Quest items | Usually no | Prevents bypassing quest risk |
| Secure container contents | Not needed | Already protected by secure container rules |
| Cosmetics | No | Not lost in raid |

## Cost Formula

```text
Insurance Cost = Item Base Value x Insurer Rate x Condition Modifier x Risk Modifier
```

| Modifier | Purpose |
| :--- | :--- |
| Item Base Value | Makes expensive gear more costly to protect |
| Insurer Rate | Differentiates recovery services |
| Condition Modifier | Reduces cost for heavily damaged gear |
| Risk Modifier | Allows mode or event tuning |

Designers should tune cost around emotional value as well as credit value. A rare weapon with strong attachment investment may deserve a higher cost band than a simple sell-price formula suggests. Conversely, damaged or low-tier gear should remain cheap enough that struggling players can use insurance as a recovery habit.

## UX Flow

Insurance UI should be visible during loadout preparation, but not loud enough to slow every raid. A player should be able to insure recommended items quickly, inspect details when needed, and see the total protected value before deploying.

| Screen | Player Action | Feedback |
| :--- | :--- | :--- |
| Loadout Preparation | Toggle insurance per item or use insure-all | Cost preview and insurer comparison |
| Raid Recap | See insured item status | Returned, looted, pending, or lost |
| Safe House Inbox | Claim returned items | Timer, item condition, and storage warning |
| Economy Summary | See insurance spend | Helps players learn cost discipline |

## Edge Cases

Edge cases should favor clarity over cleverness. If the system cannot confidently return an item, the recap should explain why. Ambiguous states create support tickets and make players distrust the loss model.

| Case | Rule |
| :--- | :--- |
| Player disconnects | Resolve based on final raid state |
| Item is looted then dropped | Counts as looted unless recovery rules explicitly allow recheck |
| Inventory full on claim | Hold in inbox until space is available |
| Seasonal wipe | Wipe rules override pending insurance unless event policy says otherwise |
| Ranked Ops | Insurance disabled or restricted by season config |

## Insurance Examples

A budget player insures a common rifle and light armor before a normal raid. They die near an edge route, the items are not looted, and the gear returns later. The loss still matters because the player lost backpack loot, time, and immediate access to the kit.

A veteran insures an expensive weapon before pushing a hotspot. Another squad loots the weapon after the fight. The recap should show the item as looted, not mysteriously lost, so the player understands that insurance did not fail.

A ranked season disables insurance. The loadout screen should show that rule before queue confirmation and should not let the player spend credits on protection that cannot apply.

## Tuning Notes

- Insurance cost should rise with item value but stay useful for standard gear.
- Return timers should create anticipation without feeling like mobile-game punishment.
- Insure-all should be convenient but must display total cost clearly.
- Recovery rates should be monitored by map, mode, gear tier, and player skill.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Pre-raid insurance UI | [Loadout Preparation](loadoutpreparation.html) |
| Gear loss rules | [Core Gameplay](coregameplay.html) |
| Credit sinks | [Economy](economy.html) |
| Safe House inbox | [Safe House Design](safe_house_design.html) |
| Ranked restrictions | [Ranked Mode](rankedmode.html) |
