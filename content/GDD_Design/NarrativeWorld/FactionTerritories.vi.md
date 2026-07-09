---
title: "Faction Territories & Map Control"
type: docs
weight: 6
---

### Tổng Quan

This tài liệu bridges **Factions** và **Maps** — defining which factions operate where, how territory control affects gameplay, và how seasonal community events shift the power balance.

> **Cross-References:** [Factions](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Factions.md) — full faction profiles, reputation hệ thống; [MapBible](MapBible.md) — zone type definitions; [MapLore\_Industrial](MapLore_Industrial.md) và [MapLore\_Urban](MapLore_Urban.md) — per-map lore và spatial chi tiết; [Quest Lines](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/QuestLines.md) — quests are faction-gated by territory.

***

### Design Philosophy

#### Why Territory Matters in Extraction

Faction territory is not cosmetic — it directly changes the gameplay trải nghiệm for người chơi in that zone:

| Territory Effect            | Gameplay Impact                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------- |
| **Faction AI spawns**       | Faction patrol NPCs appear as non-hostile allies (nếu rep ≥ 2) hoặc neutral (nếu rep 0) |
| **Vendor presence**         | Field vendor kiosk available at zone entry point                                    |
| **Quest objective markers** | Zone quests from controlling faction appear on map                                  |
| **Environmental signs**     | Faction-cụ thể graffiti, barricades, radio frequencies, và lighting              |
| **Loot type skew**          | Controlling faction's signature items spawn at slightly higher rate                 |

#### "No Permanent Owner" Principle

No faction permanently owns any zone. Territory is a **seasonal trạng thái** that reflects:

1. Community quest completion rates (which faction got more tasks done this season?)
2. Live Op events (Faction War events can temporarily flip control)
3. Dev-authored season narrative (some shifts are scripted for story purposes)

***

### Map 1: Industrial Decay (Sector 7)

```
┌─────────────────────────────────────────────────────┐
│                     NORTH                           │
│     [Forest Edge Zone — Unclaimed, Neutral]         │
│                                                     │
│  [WAREHOUSES]     [REACTOR TOWER]     [TECH LABS]   │
│   Salvage        Contested!        Tech Syn   │
│  Corps Primary    (No faction holds   Syndicate     │
│                   the center)         Primary        │
│                                                     │
│  [OFFICES]        [WORKSHOPS]         [Storage]     │
│   Tech Syn       Salvage           Contested   │
│  Secondary        Corps Secondary                   │
│                                                     │
│     [Forest Edge Zone — Unclaimed, Neutral]         │
│                     SOUTH                           │
└─────────────────────────────────────────────────────┘

 = Salvage Corps    = Tech Syndicate
 = Actively Contested (high PvP)    = Disputed
```

#### Industrial Decay — Zone Control bảng

| Zone                               | Controlling Faction                | AI Spawns                                | Vendor                                  | ghi chú                                                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------------- | --------------------------------------- | ------------------------------------------------------------ |
| **Reactor Tower**                  |  Contested — None                 | Prometheus Enhanced Subjects (AI Bosses) | None                                    | No faction controls the center — AI Bosses are the deterrent |
| **Tech Labs (Alpha, Beta, Gamma)** |  Tech Syndicate (primary)        | Tech Syndicate field operatives          | Signal Scanner, Data Drives, Keycards   | Syndicate guards the Prometheus data here                    |
| **Warehouse District**             |  Salvage Corps (primary)         | Salvage work crews                       | Industrial parts, repair tools, vũ khí | Salvage established first claim post-Collapse                |
| **Office Complex**                 |  Tech Syndicate (secondary)      | Tech Syndicate data agents               | Electronic components, intel items      | Corporate network nodes still active here                    |
| **Workshops**                      |  Salvage Corps (secondary)       | Salvage cơ chế                        | Crafting materials, basic vũ khí       | Salvage maintains the only working machinery                 |
| **Storage Area**                   |  Disputed (Underground / Salvage) | Rotating patrols                         | None — underground dead drops only      | Underground runs smuggling routes thông qua here               |
| **Forest Perimeter**               |  Unclaimed — Neutral              | Random wandering scavs, wildlife         | None                                    | No faction worth fighting for at the edges                   |

#### Sector 7 Territorial Conflict Points

| Conflict                | Factions                | Why                                                                                           | Season Dynamic                                                                      |
| ----------------------- | ----------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Workshop Dispute**    | Salvage vs. Tech        | Tech wants the industrial machinery for data terminal manufacturing. Salvage won't give it up | Season 2 Resource War — người chơi must choose sides. Winner gains control             |
| **Lab Access**          | Tech vs. Peacekeepers   | Peacekeepers want Firebase Delta access codes stored in Lab Beta. Tech is blocking them       | Peacekeeper quest: "Seize the Data" — nếu completed faction-wide, gains zone access  |
| **Warehouse Smuggling** | Underground vs. Salvage | Underground runs contraband thông qua Salvage-held warehouses mà không Salvage knowledge         | Underground quest: "Keep Viktor in the Dark" — nếu exposed, Underground loses access |

***

### Map 2: Urban Ruins (District 14)

```
┌─────────────────────────────────────────────────────┐
│                     NORTH                           │
│  [Subway NORTH]  [MALL]      [Subway SOUTH]         │
│   Underground   Contested  Underground         │
│                                                     │
│  [PARK]          [CENTRAL    [HOTEL]                │
│   Peacekeepers  PLAZA]       Peacekeepers        │
│  Patrol Zone      Contested Medical Post          │
│                                                     │
│  [Apartments]    [Streets]   [Streets]              │
│   Civilian      /       /                  │
│  Communities     Mixed       Mixed                  │
│                                                     │
│     [Extraction Perimeter — Open/Neutral]           │
│                     SOUTH                           │
└─────────────────────────────────────────────────────┘

 = Underground Network    = Peacekeepers
 = Hotly Contested    = Civilian communities (neither faction)
```

#### Urban Ruins — Zone Control bảng

| Zone                    | Controlling Faction              | AI Spawns                                                    | Vendor                                        | ghi chú                                                                         |
| ----------------------- | -------------------------------- | ------------------------------------------------------------ | --------------------------------------------- | ----------------------------------------------------------------------------- |
| **Shopping Mall**       |  Contested                      | Hostile scavengers + occasional faction NPCs                 | None (too dangerous)                          | Highest giá trị loot draws all factions. PvP hotspot                            |
| **Central Plaza**       |  Contested                      | Supply drop event draws all factions                         | None                                          | Control shifts by match — whoever holds it mid-match controls the supply drop |
| **Subway hệ thống**       |  Underground Network (primary) | Underground runners, Rat King's lieutenants                  | Black market items, forged IDs, smuggled gear | Underground controls the tunnels — fastest travel routes in the map           |
| **Hotel**               |  Peacekeepers (primary)       | Peacekeeper patrol units, Dr. Wells' medics                  | Medical supplies, giáp, Commander's radio    | Peacekeepers cách dùng the hotel as their District 14 command post                  |
| **City Park**           |  Peacekeepers (secondary)     | Peacekeeper patrol                                           | None                                          | Open patrol routes; extraction zone proximity                                 |
| **Apartment Buildings** |  Civilian Communities           | Friendly civilian NPCs (non-hostile), occasional lone scavs  | None — barter only from civilians             | Autonomous survivor communities. Neither faction controls them                |
| **Streets**             | Mixed — shifts by thời gian           | Faction patrols (early match = PK, late match = Underground) | None                                          | Early game: Peacekeeper sweeps. Late game: Underground emerges from tunnels   |

#### District 14 Territorial Conflict Points

| Conflict                  | Factions                         | Why                                                                                                                     | Season Dynamic                                                                                                                               |
| ------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Subway Control**        | Underground vs. Peacekeepers     | Peacekeepers want to shut down the Underground smuggling route. Underground says tunnels are their sovereign territory  | Season 2 "Peacekeepers Overreach" — nếu PK completes the crackdown quest, Underground loses Subway; gains new safehouse elsewhere             |
| **Apartment Neutrality**  | PK vs. Underground vs. Civilians | Both factions want civilian support. Underground protects them transactionally; Peacekeepers protect them ideologically | Community quest: civilians vote their allegiance based on người chơi quest choices — gives winner +faction-aligned quest objectives in this zone |
| **Mall Loot Exclusivity** | All Factions                     | Whoever gets the most kills in the Mall gets first access to the supply drop zone                                       | Rotating seasonal "Turf War" event — winner faction gets bonus loot here for the week                                                        |

***

### Map 3: Firebase Delta (Future — Season 3)

> **Content Status:** This zone will open in Season 3. Territory control is placeholder design.

```
Projected Territory (Season 3 Opening):

[Airfield]           → Contested — no faction control at launch
[Command Bunker]     → Peacekeepers objective (Helena's main S3 quest)
[Weapons Lab]        → Tech Syndicate objective (Prometheus tech recovery)
[Barracks]           → Salvage Corps objective (military equipment salvage)
[Underground Armory] → Contested (all factions want this)
```

The Firebase Delta narrative revolves around the **Peacekeepers' legitimate claim** to reclaim this military installation as a new HQ — contested by Tech Syndicate's mission to retrieve Prometheus prototype data trước it falls under "law enforcement" jurisdiction.

***

### Seasonal Territory cơ chế

#### Community Quest Completion

At the end of each season, the hệ thống tallies **quest completions by faction** across all người chơi:

| Outcome                                                                | Effect                                              |
| ---------------------------------------------------------------------- | --------------------------------------------------- |
| Faction A completes 20% more quests than Faction B in a contested zone | Faction A gains control of that zone next season    |
| Tie (within 5%)                                                        | Zone remains contested                              |
| Faction loses a Loyalty Test quest chain server-wide                   | Zone is lost immediately, regardless of quest count |

#### Faction War Live Events (3x per Season)

Timed 48-hour events where the community completes cụ thể high-giá trị objectives:

| Event Type            | Trigger                                                    | Stakes                                                         |
| --------------------- | ---------------------------------------------------------- | -------------------------------------------------------------- |
| **Supply Surge**      | Deliver X items to faction HQ                              | Winning faction gets +20% loot rate in their zone for 1 week   |
| **Zone Push**         | Eliminate X địch in a contested zone under faction flag | Winner claims the zone for the remainder of the season         |
| **Intelligence Race** | Extract X intel items for a faction                        | Winner gets a new vendor item unlocked for all faction members |

#### Territory Loss Consequences

khi a faction loses a zone:

* Their vendor booth disappears from that zone (vendor moves to nearest controlled zone)
* Their patrol NPCs become rare encounters rather than common
* Their quest objectives in that zone become inaccessible until control is regained
* New faction's environmental elements (graffiti, barricades, radio) appear within 2 days (via server update patch)

***

### người chơi Rep × Territory Interaction

How individual người chơi reputation interacts với faction territory:

| người chơi Rep với Controlling Faction | In-Zone trải nghiệm                                                                  |
| ----------------------------------- | ----------------------------------------------------------------------------------- |
| Rep Level 0 (no rep)                | Faction NPCs are neutral — they don't giúp hoặc attack                                |
| Rep Level 1–2                       | Faction patrol NPCs are friendly — will not attack, may warn of địch             |
| Rep Level 3+                        | Faction NPCs actively assist — will attack địch người chơi targeting you (within 50m) |
| Rep Level 5 (max)                   | Exclusive quest markers appear at vendor in this zone                               |
| Negative Rep (Hostile)              | Faction NPCs will attack the người chơi on sight in their controlled zone               |

**Design Note:** This tạo powerful in-raid incentives. A người chơi với high Salvage rep moving thông qua the Warehouse District has allied AI support. A người chơi với negative Salvage rep must avoid the Warehouses hoặc fight thông qua friendly AI. Territory và reputation combine into a dynamic social contract.

***

### Tham Chiếu Chéo

* [Factions](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Factions.md) — Full faction profiles, NPC chi tiết, reputation progression hệ thống.
* [MapBible](MapBible.md) — Zone type definitions, how Hot/Mid/Edge zones are designed.
* [MapLore\_Industrial](MapLore_Industrial.md) — Industrial Decay chi tiết lore + POI-level faction presence.
* [MapLore\_Urban](MapLore_Urban.md) — Urban Ruins chi tiết lore + faction presence per location.
* [Quest Lines](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/QuestLines.md) — How faction territory controls which quest types are available.
* [Backstory](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Backstory.md) — Historical reasons why each faction controls the zones they do.
