---
title: "Game Overview & Design Foundation"
type: docs
---

## Executive Summary

**Extraction Shooter** is a mobile-first, top-down tactical extraction shooter built around short, high-pressure raids. Players prepare a loadout, enter a dangerous zone, loot under pressure, decide when to fight or flee, and must extract before the match turns against them.

**Core hook:** every raid risks something real. A successful extraction builds wealth, momentum, and story. A failed raid costs gear, teaches a lesson, and sends the player back to plan smarter.

This page defines the creative foundation. Detailed system rules live in the linked Game Design pages.

## Start Here

{{< cards cols="3" >}}
{{< card link="coregameplay/index.html" title="Core Gameplay" icon="refresh" subtitle="Raid loop, extraction rhythm, death pressure, and match flow." >}}
{{< card link="controls/index.html" title="Controls" icon="cursor-click" subtitle="Touch input, aiming, movement, camera, and mobile combat ergonomics." >}}
{{< card link="gamemodes/index.html" title="Game Modes" icon="puzzle" subtitle="Raid variants, ranked play, co-op concepts, and mode selection." >}}
{{< card link="economy/index.html" title="Economy" icon="currency-dollar" subtitle="Loot value, traders, money sinks, inflation controls, and item flow." >}}
{{< card link="progression/index.html" title="Progression" icon="chart-bar" subtitle="Account growth, operators, mastery, reputation, and long-term goals." >}}
{{< card link="mapdesign/index.html" title="Map Design" icon="location-marker" subtitle="Zone layout, extraction placement, hotspots, routes, and readability." >}}
{{< /cards >}}

## Design Snapshot

| Area | Direction |
| :--- | :--- |
| Platform | Mobile-first, with PC support as a secondary opportunity |
| Camera | Top-down tactical view with strong silhouette readability |
| Session Length | 10-15 minute raids, 25-40 minute total play sessions |
| Match Model | PvPvE extraction: loot, fight, survive, extract |
| Core Risk | Brought gear can be lost; account progress and stash remain safe |
| Monetization | Free-to-play principles, cosmetics and optional convenience only |
| Audience | Hardcore mobile players and PC extraction fans looking for shorter sessions |
| Design Bias | Tactical decisions over twitch precision, readable combat over realism |

## Core Design Pillars

{{< cards cols="2" >}}
{{< card title="Risk & Reward" icon="exclamation-circle" subtitle="Loot should feel valuable because extraction is never guaranteed." >}}
{{< card title="Mobile-First Tactics" icon="device-mobile" subtitle="Every core interaction must work under touch constraints and short sessions." >}}
{{< card title="Tactical Readability" icon="eye" subtitle="Players should understand threats, cover, loot, and squad state at a glance." >}}
{{< card title="Persistent Progression" icon="chart-bar" subtitle="Bad raids hurt, but the account, stash, reputation, and knowledge keep growing." >}}
{{< card title="Living World" icon="map" subtitle="Aethelgard should feel like a place with history, factions, and environmental clues." >}}
{{< /cards >}}

### Pillar Notes

| Pillar | Player Feeling | Design Requirement |
| :--- | :--- | :--- |
| Risk & Reward | "Should I leave now or push deeper?" | High-value areas must create visible danger and social pressure. |
| Mobile-First Tactics | "I can make smart plays on a phone." | Combat must be readable, responsive, and thumb-friendly. |
| Tactical Readability | "I lost because of a choice, not visual noise." | Silhouettes, UI states, and threat signals must be clear on small screens. |
| Persistent Progression | "Even a bad raid moves me forward." | Loss must sting without deleting long-term progress. |
| Living World | "This zone has a past." | Loot, audio, props, and faction tasks should reinforce world logic. |

## Market Position

> Market snapshot: verify competitor details before external publishing. Use this section for positioning, not final marketing claims.

| Reference | Current Relevance | Design Takeaway |
| :--- | :--- | :--- |
| Escape from Tarkov | Hardcore PC extraction benchmark | Keep meaningful gear risk, but reduce prep friction and session length. |
| ARC Raiders | Modern extraction reference on PC and console | Watch accessibility, social extraction behavior, and anti-cheat expectations. |
| Delta Force: Hazard Operations | F2P shooter with extraction mode | Differentiate through mobile-first top-down readability and shorter raids. |
| The Cycle: Frontier | Shutdown case study | Economy trust, retention, and identity must be sustainable from day one. |
| PUBG Mobile / COD Mobile | Massive mobile shooter audience | Do not copy battle royale pacing; offer higher stakes and persistent loot. |

**Positioning statement:** a tactical extraction shooter for mobile players who want higher stakes than battle royale, shorter sessions than PC extraction games, and fair progression without pay-to-win pressure.

## Player Promise

### What We Are

* A high-stakes tactical extraction shooter.
* Mobile-first, not a reduced PC port.
* Skill-based, readable, and fair.
* Built around meaningful preparation, raid decisions, and recovery after loss.

### What We Are Not

* A casual arcade shooter with no consequences.
* A pay-to-win gear economy.
* A battle royale mode with extraction branding.
* A simulation-heavy PC experience forced onto touch controls.

## Design Guardrails

| Guardrail | Rule |
| :--- | :--- |
| No Pay-to-Win | Never sell weapons, armor, stat boosts, or exclusive power. |
| Recoverable Loss | Death can cost gear, but should not erase identity, learning, or account progress. |
| Short Raid Pressure | Match pacing should support 10-15 minute raids without feeling shallow. |
| Mobile Readability | UI, camera, combat effects, and loot signals must remain clear on small screens. |
| Ethical Convenience | Paid convenience can save time only when equivalent free paths exist. |
| Fair Competition | Ranked and competitive systems must protect integrity, matchmaking quality, and anti-cheat expectations. |

## Canonical Detail Pages

| Topic | Canonical Page |
| :--- | :--- |
| Raid loop and match rhythm | [Core Gameplay](coregameplay/index.html) |
| Loadout decisions and pre-raid flow | [Loadout Preparation](loadoutpreparation/index.html) |
| Gear loss and insurance recovery | [Insurance System](insurancesystem/index.html) |
| Economy, traders, sinks, and value flow | [Economy](economy/index.html) |
| Account, operator, and reputation growth | [Progression](progression/index.html) |
| Map layout, hotspots, and extraction logic | [Map Design](mapdesign/index.html) |
| Live events, battle pass, and seasonal cadence | [Live Operations](liveops/index.html) |
| First-time user experience | [Onboarding](tutorialraid/index.html) |

## Ownership & Maintenance

| Role | Owner | Reviewer |
| :--- | :--- | :--- |
| Design Vision | Lead Game Designer | Creative Director |
| Systems Consistency | Systems Designer | Technical Director |
| Market Snapshot | Product / Publishing | Creative Director |

**Maintenance note:** keep this page short. When a section starts needing formulas, edge cases, diagrams, or balance tables, move that detail to the canonical child page and link it here.

**Recent changes:**

* **v1.2 (2026-07-06):** Refactored from mega-spec into a hub overview.
* **v1.1 (2026-02-09):** Added marketing and distribution notes.
* **v1.0 (2026-02-07):** Initial comprehensive draft.
