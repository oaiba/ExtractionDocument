---
title: "Screen Groups Overview"
type: docs
weight: 1
---

## Purpose

This page is the canonical screen inventory for the UI/UX design package. It groups screens by player lifecycle instead of widget type so designers, game designers, and engineers can reason about complete player journeys.

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Full UI/UX documentation hub |
| [Global UX Standards](global_ux_standards/index.html) | Shared navigation, focus, state, modal, and accessibility rules |
| [Out-of-Raid Screens](out_of_raid_screens/index.html) | Home, loadout, stash, traders, safe house, quests, profile |
| [Pre-Raid Screens](pre_raid_screens/index.html) | Mode, map, deploy confirmation, squad lobby, matchmaking |
| [In-Raid Screens](in_raid_screens/index.html) | HUD, tactical map, looting, inventory overlay, pause, spectator |
| [Post-Raid Screens](post_raid_screens/index.html) | AAR, death replay, loot transfer, quest progress, redeploy |

For cross-domain ownership, unresolved decisions, and MVP readiness, use [Cross-System Traceability](../projectscope/cross_system_traceability/index.html), [Design Decision Register](../projectscope/design_decision_register/index.html), and [MVP Readiness Review](../projectscope/mvp_readiness_review/index.html).

Every screen group must answer four questions:

| Question | Requirement |
| :--- | :--- |
| What is the player trying to do? | State the player intent before layout details |
| What information is required? | Expose risk, cost, progress, or failure reason at the moment it matters |
| What is the next action? | Make the primary CTA obvious and keep exits predictable |
| What can go wrong? | Define loading, empty, locked, invalid, offline, and error states |

---

## Screen Group Taxonomy

#### System Diagram

```
+----------------+     +----------------+     +----------------+
| BOOT / AUTH    | --> | OUT OF RAID    | --> | PRE RAID       |
| login, setup   |     | home, stash    |     | mode, map      |
| tutorial gate  |     | traders, quest |     | squad, deploy  |
+----------------+     +----------------+     +----------------+
                                                        |
                                                        v
+----------------+     +----------------+     +----------------+
| SYSTEM / LIVE  | <-- | POST RAID      | <-- | IN RAID        |
| shop, settings |     | AAR, replay    |     | HUD, map       |
| events, social |     | loot, redeploy |     | loot, pause    |
+----------------+     +----------------+     +----------------+
```

- Primary loop runs clockwise from account entry to raid recovery.
- Social, LiveOps, commerce, and settings can deep link into the loop but should not bury Deploy.
- Every group owns screen states, input mapping, and accessibility behavior for its surfaces.

| Phase | Screen Group | Primary Job | Key Pages |
| :--- | :--- | :--- | :--- |
| Boot and account | Onboarding / Auth | Get the player safely into a valid account and tutorial state | [Settings & System Screens](commerce_settings_system_screens/index.html), [Loading Screen Design](loadingscreen_design/index.html) |
| Out of raid | Home, profile, stash, traders, safe house, quests | Prepare, recover, progress, and manage risk | [Out-of-Raid Screens](out_of_raid_screens/index.html) |
| Pre-raid | Mode, map, squad, deploy, matchmaking | Confirm rules, risk, party readiness, and queue state | [Pre-Raid Screens](pre_raid_screens/index.html) |
| In raid | HUD, map, looting, overlays, pause, spectator | Keep survival-critical information clear during pressure | [In-Raid Screens](in_raid_screens/index.html), [HUD Design](hud_design/index.html) |
| Post-raid | AAR, death replay, loot transfer, report, redeploy | Explain outcome and route the player into the next loop | [Post-Raid Screens](post_raid_screens/index.html) |
| Social | Friends, party, clan, LFG, communication, moderation | Help players coordinate while limiting abuse | [Social Screens](social_screens/index.html) |
| Progression and LiveOps | Battle pass, events, ranked, rewards, inbox | Surface long-term goals without burying raid flow | [Progression & LiveOps Screens](progression_liveops_screens/index.html) |
| Commerce | Shop, offers, bundles, item preview, currency top-up, confirmation, receipts, redeem | Handle cosmetic purchase browsing and checkout trust states | [Commerce Screens](commerce_screens/index.html) |
| Settings and system | Settings, account, privacy, diagnostics, dialogs | Handle configuration, account, platform, and system states | [Settings & System Screens](commerce_settings_system_screens/index.html) |

---

### Commerce Coverage Checklist

Commerce screen coverage is complete only when the canonical page defines offer information architecture, offer card anatomy, checkout trust states, receipt/support routes, and platform/region restrictions.

| Coverage Area | Requirement |
| :--- | :--- |
| Offer IA | Entry points, tabs, section priority, and empty/offline fallback are explicit |
| Checkout trust | Price, currency type, ownership, balance impact, provider handoff, and confirmation are visible |
| Receipt/support | Success, pending, failed, refunded, duplicate, and missing entitlement states expose support routes |
| Platform restrictions | Region, age, account, provider, and spending-limit blocks show readable reasons |
| No wallet drift | Premium balance is a component only; no standalone Wallet destination is introduced |

---

### Progression / LiveOps Coverage Checklist

Progression and LiveOps coverage is complete only when the canonical page defines reward claim states, season/event timing, deep links, expiry/conversion behavior, and Commerce handoff boundaries.

| Coverage Area | Requirement |
| :--- | :--- |
| Reward model | Locked, earned, claimable, claimed, blocked, overflow, expired, converted, and retroactive grants are explicit |
| Season state | Preseason, active, ending, grace, archived, and offline/cached states have UI behavior |
| Event clarity | Event rules, modifiers, objectives, reward ladder, event currency, expiry, and playable route are visible |
| Claim trust | Rewards show source, destination, expiry, blocker, claim-all leftovers, and support route when needed |
| Commerce boundary | Battle pass/event purchase CTAs route to Commerce; reward/progress context stays in Progression/LiveOps |

---

## Screen Spec Template

Use this template for every new screen spec. Keep it short enough to update, but complete enough for designer layout, UX review, and implementation planning. [Out-of-Raid Screens](out_of_raid_screens/index.html) is the baseline example for the full designer-ready format.

#### Spec Template Layout

```
+------------------------------------------------------------------+
| SCREEN NAME                                      [Primary CTA]   |
| Entry: Home / Deep Link / Event                 Exit: Back / X   |
|------------------------------------------------------------------|
| Goal: One sentence                                               |
| Intent: What the player came here to do                          |
|                                                                  |
| +----------------------+  +------------------------------------+ |
| | Main Content         |  | Context / Detail Panel             | |
| | selected item/state  |  | rules, cost, risk, requirement     | |
| +----------------------+  +------------------------------------+ |
|                                                                  |
| States: Default | Loading | Empty | Locked | Error | Success     |
| Input: Mouse/KB | Controller | Touch | Accessibility notes       |
+------------------------------------------------------------------+
```

| Section | Required Content |
| :--- | :--- |
| Player Intent | Why the player opened it, what success means, and what risk/cost must be understood |
| Expanded ASCII Wireframe | PC/console landscape layout with header, primary area, detail panel, warning lane, and action bar |
| Layout Anatomy | Named regions and exact content each region must hold |
| Visual Hierarchy | Priority order for what must read first, second, and third |
| Component Requirements | Low-level requirements for rows, cards, panels, CTAs, warnings, badges, and dialogs |
| States & Edge Cases | Default, loading, empty, invalid, blocked, locked, offline, error, success, and destructive confirmation states |
| Input / Focus / Touch | Mouse/keyboard, controller, mobile touch, focus order, and hold/tap alternatives |
| Designer Notes | Short actionable constraints about density, copy, responsiveness, and non-color state meaning |
| Acceptance Checklist | Review checklist for layout handoff and implementation QA |

### Designer-Ready Handoff Rules

| Rule | Requirement |
| :--- | :--- |
| Summary is not enough | Critical requirements must live inside the owning screen section, not only in inventory tables |
| Disabled means explained | Every disabled CTA must name the first blocker and provide a route when possible |
| Color is never alone | State, rarity, danger, lock, and success meaning must have text or icon-shape support |
| Action bars stay stable | Primary CTAs should not jump when warning text appears |
| Mobile is not an afterthought | Every screen needs a touch layout note and a sticky or reachable primary CTA |
| Destructive actions confirm | Sell, discard, abandon, unlink, delete, spend, and report/block flows state consequence before commit |

---

## Global Navigation Model

#### Screen Ownership Map

```
+--------------------+       +-----------------------+
| SCREEN GROUP DOC   | ----> | GAME DESIGN DOC       |
| layout, states     |       | rules, economy, flow  |
+--------------------+       +-----------------------+
          |                              |
          v                              v
+--------------------+       +-----------------------+
| TECHNICAL SYSTEM   | <---- | UX FLOWS / STANDARDS  |
| code names, events |       | journey, input, QA    |
+--------------------+       +-----------------------+
```

- Screen group pages own the player-facing layout contract.
- Game design pages own gameplay rules and economy outcomes.
- Technical pages own code names, events, data contracts, and implementation constraints.

| Surface | Navigation Rule |
| :--- | :--- |
| Home hub | Horizontal global navigation bar using the PC/Console landscape standard |
| Preparation flow | Linear enough for new players, jumpable for experts |
| In-raid overlays | Never fully pause online raid state; preserve audio and threat awareness |
| Modal dialogs | One decision per modal; destructive actions require hold or second confirmation |
| Back behavior | `ESC` / `B` always closes the deepest layer first |
| Deep links | Event, quest, reward, and trader cards must open the exact destination screen |
| Vertical rails | Secondary/local navigation only: stash filters, roster filters, trader list, quest list, settings categories, social/LFG lists |

---

## Coverage Checklist

- [ ] Every player lifecycle phase has a screen group.
- [ ] Every group follows the PC/Console landscape standard.
- [ ] Primary navigation uses the horizontal global nav; vertical rails are secondary/local only.
- [ ] Every group defines blocked, empty, locked, loading, offline, and error states.
- [ ] Every major game system has a UI owner or cross-reference.
- [ ] No single document owns unrelated screens that should live in separate groups.
- [ ] Technical terms match [UI System](../../gdd_technical/systems/uisystem/index.html) where code-facing names are needed.
