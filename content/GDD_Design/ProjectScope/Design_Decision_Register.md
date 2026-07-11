---
title: Design Decision Register
linkTitle: Decision Register
type: docs
weight: 8
---

## Purpose

This register tracks design decisions that affect more than one system or are not yet ready to be treated as canonical. It does not replace the source-of-truth document for a system. English is canonical; the Vietnamese companion is a translation for navigation and review.

## Decision Status

| Status | Meaning | Required next action |
| :--- | :--- | :--- |
| Proposed | A candidate direction exists but has not been reviewed | Capture alternatives and owner |
| Under Review | Design, product, or engineering review is active | Record evidence and review date |
| Approved | The decision is authoritative for dependent docs | Update source-of-truth pages and links |
| Rejected | The option is explicitly closed | Record reason to prevent reopening by accident |
| Deferred | Deliberately postponed without blocking current scope | Add trigger and review milestone |

## Decision Contract

Every entry must include a stable ID, decision statement, owner, affected systems, evidence, MVP impact, and review date. A number that has not been approved must remain a placeholder in gameplay documentation and must be listed here instead of being presented as final balance.

## Active Register

| ID | Decision | Status | Owner | Affected systems | MVP impact | Next action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DR-001 | Season 3 map/content opening scope | Under Review | Design / Production | World, LiveOps, Progression, Economy | Defines post-launch content boundary | Confirm launch vs Season 3 content split |
| DR-002 | Hero ability numerical tuning | Under Review | Combat / Characters | Combat, Weapons, Accessibility, UI feedback | Blocks final balance and telemetry thresholds | Approve test bands, not just point values |
| DR-003 | Armor, gear, and weapon tuning bands | Under Review | Combat / Economy | Gear, Weapons, Inventory, Economy | Blocks reliable TTK and kit-cost validation | Run representative loadout simulations |
| DR-004 | Stash and container unlock pacing | Under Review | Progression / Inventory | Inventory, Progression, Economy, UI/UX | Affects onboarding and stash pressure | Approve unlock milestones and overflow policy |
| DR-005 | Economy tuning targets | Under Review | Economy / Production | Economy, Commerce, Loot, Progression | Blocks inflation and new-player recovery review | Set target raid value, kit cost, and repair ratios |
| DR-006 | Extraction, death, insurance, and reward edge cases | Under Review | Core Gameplay / Engineering | Raid, Inventory, Economy, Post-Raid | Blocks deterministic reconciliation | Approve outcome matrix and rollback behavior |
| DR-007 | AI difficulty and reinforcement limits | Under Review | AI / Combat | AI, Raid Loop, Loot, Matchmaking | Blocks encounter pacing and frustration review | Validate threat bands by raid phase |
| DR-008 | Matchmaking fallback and reconnect window | Under Review | Multiplayer / Production | Matchmaking, Raid, Social, Loading | Blocks queue and recovery acceptance | Approve region, low-pop, and crash fallback |
| DR-009 | Ranked and event rule modifiers | Under Review | Progression / LiveOps | Modes, Ranked, Rewards, UI/UX | Blocks seasonal QA scenarios | Publish mode contracts and reset behavior |
| DR-010 | Platform and accessibility baseline | Under Review | UX / Engineering | UI/UX, Controls, Settings, QA | Blocks cross-platform sign-off | Confirm minimum targets and input parity |

## Review Rules

- An `Approved` decision must link to the canonical implementation/design pages.
- A deferred decision must state what remains valid while it is deferred.
- Conflicting documents must link here and be marked as pending reconciliation.
- Product, design, and engineering owners should review active decisions before an MVP gate.

## Cross-References

- [Project Scope](_index/index.html)
- [MVP](mvp/index.html)
- [Cross-System Traceability](cross_system_traceability/index.html)
- [MVP Readiness Review](mvp_readiness_review/index.html)
