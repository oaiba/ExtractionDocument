---
title: "Faction Territories & Map Control"
type: docs
weight: 6
---

## Overview

This document bridges **Factions** and **Maps** — defining which factions operate where, how territory control affects gameplay, and how seasonal community events shift the power balance.

> **Cross-References:** [Factions](Factions.md) — full faction profiles, reputation systems; [MapBible](MapBible.md) — zone type definitions; [MapLore_Industrial](MapLore_Industrial.md) and [MapLore_Urban](MapLore_Urban.md) — per-map lore and spatial detail; [Quest Lines](QuestLines.md) — quests are faction-gated by territory.

---

## Design Philosophy

### Why Territory Matters in Extraction

Faction territory is not cosmetic — it directly changes the gameplay experience for players in that zone:

| Territory Effect | Gameplay Impact |
| :--------------- | :-------------- |
| **Faction AI spawns** | Faction patrol NPCs appear as non-hostile allies (if rep ≥ 2) or neutral (if rep 0) |
| **Vendor presence** | Field vendor kiosk available at zone entry point |
| **Quest objective markers** | Zone quests from controlling faction appear on map |
| **Environmental signs** | Faction-specific graffiti, barricades, radio frequencies, and lighting |
| **Loot type skew** | Controlling faction's signature items spawn at slightly higher rate |

### "No Permanent Owner" Principle

No faction permanently owns any zone. Territory is a **seasonal state** that reflects:
1. Community quest completion rates (which faction got more tasks done this season?)
2. Live Op events (Faction War events can temporarily flip control)
3. Dev-authored season narrative (some shifts are scripted for story purposes)

---

## Map 1: Industrial Decay (Sector 7)

```
┌─────────────────────────────────────────────────────┐
│                     NORTH                           │
│     [Forest Edge Zone — Unclaimed, Neutral]         │
│                                                     │
│  [WAREHOUSES]     [REACTOR TOWER]     [TECH LABS]   │
│  🟠 Salvage       🔴 Contested!       🔵 Tech Syn   │
│  Corps Primary    (No faction holds   Syndicate     │
│                   the center)         Primary        │
│                                                     │
│  [OFFICES]        [WORKSHOPS]         [Storage]     │
│  🔵 Tech Syn      🟠 Salvage          ⚪ Contested   │
│  Secondary        Corps Secondary                   │
│                                                     │
│     [Forest Edge Zone — Unclaimed, Neutral]         │
│                     SOUTH                           │
└─────────────────────────────────────────────────────┘

🟠 = Salvage Corps   🔵 = Tech Syndicate
🔴 = Actively Contested (high PvP)   ⚪ = Disputed
```

### Industrial Decay — Zone Control Table

| Zone | Controlling Faction | AI Spawns | Vendor | Notes |
| :--- | :------------------ | :-------- | :----- | :---- |
| **Reactor Tower** | ❌ Contested — None | Prometheus Enhanced Subjects (AI Bosses) | None | No faction controls the center — AI Bosses are the deterrent |
| **Tech Labs (Alpha, Beta, Gamma)** | 🔵 Tech Syndicate (Primary) | Tech Syndicate field operatives | Signal Scanner, Data Drives, Keycards | Syndicate guards the Prometheus data here |
| **Warehouse District** | 🟠 Salvage Corps (Primary) | Salvage work crews | Industrial parts, repair tools, weapons | Salvage established first claim post-Collapse |
| **Office Complex** | 🔵 Tech Syndicate (Secondary) | Tech Syndicate data agents | Electronic components, intel items | Corporate network nodes still active here |
| **Workshops** | 🟠 Salvage Corps (Secondary) | Salvage mechanics | Crafting materials, basic weapons | Salvage maintains the only working machinery |
| **Storage Area** | ⚪ Disputed (Underground / Salvage) | Rotating patrols | None — underground dead drops only | Underground runs smuggling routes through here |
| **Forest Perimeter** | ⚪ Unclaimed — Neutral | Random wandering scavs, wildlife | None | No faction worth fighting for at the edges |

### Sector 7 Territorial Conflict Points

| Conflict | Factions | Why | Season Dynamic |
| :------- | :------- | :-- | :------------- |
| **Workshop Dispute** | Salvage vs. Tech | Tech wants the industrial machinery for data terminal manufacturing. Salvage won't give it up | Season 2 Resource War — players must choose sides. Winner gains control |
| **Lab Access** | Tech vs. Peacekeepers | Peacekeepers want Firebase Delta access codes stored in Lab Beta. Tech is blocking them | Peacekeeper quest: "Seize the Data" — if completed faction-wide, gains zone access |
| **Warehouse Smuggling** | Underground vs. Salvage | Underground runs contraband through Salvage-held warehouses without Salvage knowledge | Underground quest: "Keep Viktor in the Dark" — if exposed, Underground loses access |

---

## Map 2: Urban Ruins (District 14)

```
┌─────────────────────────────────────────────────────┐
│                     NORTH                           │
│  [Subway NORTH]  [MALL]      [Subway SOUTH]         │
│  🟣 Underground  🔴 Contested 🟣 Underground         │
│                                                     │
│  [PARK]          [CENTRAL    [HOTEL]                │
│  🛡️ Peacekeepers  PLAZA]      🛡️ Peacekeepers        │
│  Patrol Zone     🔴 Contested Medical Post          │
│                                                     │
│  [Apartments]    [Streets]   [Streets]              │
│  ⚪ Civilian      🟣/🛡️       🟣/🛡️                  │
│  Communities     Mixed       Mixed                  │
│                                                     │
│     [Extraction Perimeter — Open/Neutral]           │
│                     SOUTH                           │
└─────────────────────────────────────────────────────┘

🟣 = Underground Network   🛡️ = Peacekeepers
🔴 = Hotly Contested   ⚪ = Civilian communities (neither faction)
```

### Urban Ruins — Zone Control Table

| Zone | Controlling Faction | AI Spawns | Vendor | Notes |
| :--- | :------------------ | :-------- | :----- | :---- |
| **Shopping Mall** | ❌ Contested | Hostile scavengers + occasional faction NPCs | None (too dangerous) | Highest value loot draws all factions. PvP hotspot |
| **Central Plaza** | ❌ Contested | Supply drop event draws all factions | None | Control shifts by match — whoever holds it mid-match controls the supply drop |
| **Subway System** | 🟣 Underground Network (Primary) | Underground runners, Rat King's lieutenants | Black market items, forged IDs, smuggled gear | Underground controls the tunnels — fastest travel routes in the map |
| **Hotel** | 🛡️ Peacekeepers (Primary) | Peacekeeper patrol units, Dr. Wells' medics | Medical supplies, armor, Commander's radio | Peacekeepers use the hotel as their District 14 command post |
| **City Park** | 🛡️ Peacekeepers (Secondary) | Peacekeeper patrol | None | Open patrol routes; extraction zone proximity |
| **Apartment Buildings** | ⚪ Civilian Communities | Friendly civilian NPCs (non-hostile), occasional lone scavs | None — barter only from civilians | Autonomous survivor communities. Neither faction controls them |
| **Streets** | Mixed — shifts by time | Faction patrols (early match = PK, late match = Underground) | None | Early game: Peacekeeper sweeps. Late game: Underground emerges from tunnels |

### District 14 Territorial Conflict Points

| Conflict | Factions | Why | Season Dynamic |
| :------- | :------- | :-- | :------------- |
| **Subway Control** | Underground vs. Peacekeepers | Peacekeepers want to shut down the Underground smuggling route. Underground says tunnels are their sovereign territory | Season 2 "Peacekeepers Overreach" — if PK completes the crackdown quest, Underground loses Subway; gains new safehouse elsewhere |
| **Apartment Neutrality** | PK vs. Underground vs. Civilians | Both factions want civilian support. Underground protects them transactionally; Peacekeepers protect them ideologically | Community quest: civilians vote their allegiance based on player quest choices — gives winner +faction-aligned quest objectives in this zone |
| **Mall Loot Exclusivity** | All Factions | Whoever gets the most kills in the Mall gets first access to the supply drop zone | Rotating seasonal "Turf War" event — winner faction gets bonus loot here for the week |

---

## Map 3: Firebase Delta (Future — Season 3)

> **Content Status:** This zone will open in Season 3. Territory control is placeholder design.

```
Projected Territory (Season 3 Opening):

[Airfield]           → Contested — no faction control at launch
[Command Bunker]     → Peacekeepers objective (Helena's main S3 quest)
[Weapons Lab]        → Tech Syndicate objective (Prometheus tech recovery)
[Barracks]           → Salvage Corps objective (military equipment salvage)
[Underground Armory] → Contested (all factions want this)
```

The Firebase Delta narrative revolves around the **Peacekeepers' legitimate claim** to reclaim this military installation as a new HQ — contested by Tech Syndicate's mission to retrieve Prometheus prototype data before it falls under "law enforcement" jurisdiction.

---

## Seasonal Territory Mechanics

### Community Quest Completion

At the end of each season, the system tallies **quest completions by faction** across all players:

| Outcome | Effect |
| :------ | :----- |
| Faction A completes 20% more quests than Faction B in a contested zone | Faction A gains control of that zone next season |
| Tie (within 5%) | Zone remains contested |
| Faction loses a Loyalty Test quest chain server-wide | Zone is lost immediately, regardless of quest count |

### Faction War Live Events (3x per Season)

Timed 48-hour events where the community completes specific high-value objectives:

| Event Type | Trigger | Stakes |
| :--------- | :------ | :----- |
| **Supply Surge** | Deliver X items to faction HQ | Winning faction gets +20% loot rate in their zone for 1 week |
| **Zone Push** | Eliminate X enemies in a contested zone under faction flag | Winner claims the zone for the remainder of the season |
| **Intelligence Race** | Extract X intel items for a faction | Winner gets a new vendor item unlocked for all faction members |

### Territory Loss Consequences

When a faction loses a zone:
- Their vendor booth disappears from that zone (vendor moves to nearest controlled zone)
- Their patrol NPCs become rare encounters rather than common
- Their quest objectives in that zone become inaccessible until control is regained
- New faction's environmental elements (graffiti, barricades, radio) appear within 2 days (via server update patch)

---

## Player Rep × Territory Interaction

How individual player reputation interacts with faction territory:

| Player Rep with Controlling Faction | In-Zone Experience |
| :---------------------------------- | :----------------- |
| Rep Level 0 (no rep) | Faction NPCs are neutral — they don't help or attack |
| Rep Level 1–2 | Faction patrol NPCs are friendly — will not attack, may warn of enemies |
| Rep Level 3+ | Faction NPCs actively assist — will attack enemy players targeting you (within 50m) |
| Rep Level 5 (max) | Exclusive quest markers appear at vendor in this zone |
| Negative Rep (Hostile) | Faction NPCs will attack the player on sight in their controlled zone |

**Design Note:** This creates powerful in-raid incentives. A player with high Salvage rep moving through the Warehouse District has allied AI support. A player with negative Salvage rep must avoid the Warehouses or fight through friendly AI. Territory and reputation combine into a dynamic social contract.

---

## Cross-References

- [Factions](Factions.md) — Full faction profiles, NPC details, reputation progression system.
- [MapBible](MapBible.md) — Zone type definitions, how Hot/Mid/Edge zones are designed.
- [MapLore_Industrial](MapLore_Industrial.md) — Industrial Decay detailed lore + POI-level faction presence.
- [MapLore_Urban](MapLore_Urban.md) — Urban Ruins detailed lore + faction presence per location.
- [Quest Lines](QuestLines.md) — How faction territory controls which quest types are available.
- [Backstory](Backstory.md) — Historical reasons why each faction controls the zones they do.
