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
| Project Scope | Needs Engineering Decision | [MVP](MVP.md), [Risks](Risks.md) | Confirm launch vs Season 3 boundaries | Production |
| Core Gameplay | Needs Balancing | [Core Gameplay](../GameDesign/CoreGameplay.md), [Extraction](../Gameplay/Extraction_Mechanics.md) | Validate raid length, extraction rate, and outcome recovery | Game Design |
| AI | Needs Balancing | [AI & Enemy Behavior](../Gameplay/AI_Enemy_Behavior.md) | Validate threat bands, reinforcement, and frustration limits | AI / Combat |
| Combat / Weapons | Needs Balancing | [Weapons](../Combat/Weapons.md), [Weapon Balance](../Weapons/Weapon_Balance_Framework.md) | Confirm TTK bands and outlier thresholds | Combat |
| Inventory / Gear / Loadout | Needs UX Validation | [Inventory](../Inventory_System/_index.md), [Loadout](../GameDesign/LoadoutPreparation.md) | Validate stash pressure, comparison, and loadout blockers | Inventory / UX |
| Economy | Needs Balancing | [Economy](../GameDesign/Economy.md), [Commerce](../UI_UX/Commerce_Screens.md) | Set target kit cost, repair, and recovery bands | Economy |
| Progression / LiveOps | Needs Engineering Decision | [Progression](../GameDesign/Progression.md), [LiveOps](../GameDesign/LiveOps.md) | Confirm reset, expiry, and reward delivery services | Progression / LiveOps |
| Commerce | Needs Engineering Decision | [Commerce Screens](../UI_UX/Commerce_Screens.md) | Confirm provider, region, refund, and entitlement behavior | Commerce |
| UI/UX | Needs UX Validation | [Global UX Standards](../UI_UX/Global_UX_Standards.md), screen groups | Validate platform focus, mobile layout, and offline states | UX |
| Social / Multiplayer | Needs Engineering Decision | [Matchmaking](../Gameplay/Matchmaking_Lobby.md), [Social Screens](../UI_UX/Social_Screens.md) | Confirm party, reconnect, moderation, and voice services | Multiplayer |
| Characters / Abilities | Placeholder | [Hero Abilities](../Gameplay/Hero_Abilities.md) | Approve ability numbers and counterplay | Characters / Combat |
| World / Maps | Placeholder | [World](../World/_index.md), [Project Scope](_index.md) | Confirm named zones and Season 3 content | World |
| Narrative | Needs UX Validation | [Story](../Story/_index.md), [Narrative World](../NarrativeWorld/_index.md) | Validate delivery beats against onboarding and LiveOps | Narrative |
| Audio / Visuals | Needs UX Validation | [Audio](../Audio/_index.md), [Visuals](../Visuals/_index.md) | Validate combat/readability cues across platforms | Audio / Visuals |
| Accessibility | Needs UX Validation | [Accessibility](../GameDesign/Accessibility.md) | Complete input, contrast, captions, and motion review | UX |
| Anti-Cheat / Fair Play | Needs Engineering Decision | [Anti-Cheat](../Gameplay/Anti_Cheat_Fair_Play.md) | Confirm service provider and enforcement operations | Engineering |

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

Review this page at the end of each major design wave, before external playtest, before content lock, and before MVP sign-off. Any `Blocked` or `Needs Engineering Decision` item must link to the [Design Decision Register](Design_Decision_Register.md).

## Cross-References

- [Design Decision Register](Design_Decision_Register.md)
- [Cross-System Traceability](Cross_System_Traceability.md)
- [MVP](MVP.md)
