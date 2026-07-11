---
title: MVP Readiness Review
linkTitle: MVP Readiness
type: docs
weight: 10
---

## Purpose

This page is the release-readiness view of the design package. It records whether each domain is complete enough for MVP review and points to the evidence or missing decision. It is not a replacement for the canonical design documents.

## Status Vocabulary

| Status | Meaning |
| :--- | :--- |
| Complete | Rules and player-facing behavior are specified; only implementation validation remains |
| Needs Balancing | Rules exist but numeric tuning or playtest evidence is missing |
| Needs Engineering Decision | Design depends on an unresolved service, platform, or technical constraint |
| Needs UX Validation | Behavior exists but layout, accessibility, or platform validation is incomplete |
| Placeholder | Intent is documented but important content or values are not final |
| Out of MVP Scope | Explicitly excluded from the current launch target |
| Blocked | Cannot proceed until a dependency is resolved |

## Domain Readiness

| Domain | Status | Evidence | Missing decision / risk | Owner |
| :--- | :--- | :--- | :--- | :--- |
| Project Scope | Needs Engineering Decision | [MVP](mvp/index.html), [Risks](risks/index.html) | Confirm launch vs Season 3 boundaries | Production |
| Core Gameplay | Needs Balancing | [Core Gameplay](../gamedesign/coregameplay/index.html), [Extraction](../gameplay/extraction_mechanics/index.html) | Validate raid length, extraction rate, and outcome recovery | Game Design |
| AI | Needs Balancing | [AI & Enemy Behavior](../gameplay/ai_enemy_behavior/index.html) | Validate threat bands, reinforcement, and frustration limits | AI / Combat |
| Combat / Weapons | Needs Balancing | [Weapons](../combat/weapons/index.html), [Weapon Balance](../weapons/weapon_balance_framework/index.html) | Confirm TTK bands and outlier thresholds | Combat |
| Inventory / Gear / Loadout | Needs UX Validation | [Inventory](../inventory_system/_index/index.html), [Loadout](../gamedesign/loadoutpreparation/index.html) | Validate stash pressure, comparison, and loadout blockers | Inventory / UX |
| Economy | Needs Balancing | [Economy](../gamedesign/economy/index.html), [Commerce](../ui_ux/commerce_screens/index.html) | Set target kit cost, repair, and recovery bands | Economy |
| Progression / LiveOps | Needs Engineering Decision | [Progression](../gamedesign/progression/index.html), [LiveOps](../gamedesign/liveops/index.html) | Confirm reset, expiry, and reward delivery services | Progression / LiveOps |
| Commerce | Needs Engineering Decision | [Commerce Screens](../ui_ux/commerce_screens/index.html) | Confirm provider, region, refund, and entitlement behavior | Commerce |
| UI/UX | Needs UX Validation | [Global UX Standards](../ui_ux/global_ux_standards/index.html), screen groups | Validate platform focus, mobile layout, and offline states | UX |
| Social / Multiplayer | Needs Engineering Decision | [Matchmaking](../gameplay/matchmaking_lobby/index.html), [Social Screens](../ui_ux/social_screens/index.html) | Confirm party, reconnect, moderation, and voice services | Multiplayer |
| Characters / Abilities | Placeholder | [Hero Abilities](../gameplay/hero_abilities/index.html) | Approve ability numbers and counterplay | Characters / Combat |
| World / Maps | Placeholder | [World](../world/_index/index.html), [Project Scope](_index/index.html) | Confirm named zones and Season 3 content | World |
| Narrative | Needs UX Validation | [Story](../story/_index/index.html), [Narrative World](../narrativeworld/_index/index.html) | Validate delivery beats against onboarding and LiveOps | Narrative |
| Audio / Visuals | Needs UX Validation | [Audio](../audio/_index/index.html), [Visuals](../visuals/_index/index.html) | Validate combat/readability cues across platforms | Audio / Visuals |
| Accessibility | Needs UX Validation | [Accessibility](../gamedesign/accessibility/index.html) | Complete input, contrast, captions, and motion review | UX |
| Anti-Cheat / Fair Play | Needs Engineering Decision | [Anti-Cheat](../gameplay/anti_cheat_fair_play/index.html) | Confirm service provider and enforcement operations | Engineering |

## MVP Gate Criteria

- [ ] A new player can complete the tutorial and explain extraction, death, loss, and redeploy.
- [ ] Loadout validation exposes every deployment blocker with a direct next action.
- [ ] Raid outcomes, rewards, insurance, and item lifecycle reconcile deterministically.
- [ ] Combat feedback explains armor, damage, suppression, and death causes.
- [ ] AI threats have predictable tells, counterplay, and bounded reinforcement.
- [ ] Economy does not create uncontrolled new-player bankruptcy or pay-to-win power.
- [ ] UI error, offline, reconnecting, and pending states provide recovery actions.
- [ ] English and Vietnamese routes build without broken links or encoding corruption.
- [ ] Critical `Under Review` decisions are approved or explicitly deferred.

## Review Cadence

Review this page at the end of each major design wave, before external playtest, before content lock, and before MVP sign-off. Any `Blocked` or `Needs Engineering Decision` item must link to the [Design Decision Register](design_decision_register/index.html).

## Cross-References

- [Design Decision Register](design_decision_register/index.html)
- [Cross-System Traceability](cross_system_traceability/index.html)
- [MVP](mvp/index.html)
