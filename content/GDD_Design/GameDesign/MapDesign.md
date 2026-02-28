---
title: "Map Design — Level & Zone Design Rules"
type: docs
weight: 19
---

## Overview

This document consolidates **all map design rules, level design philosophy, and zone layout principles** for Aethelgard maps. Currently, map information is scattered across `CoreGameplay.md` (loot zones, match timeline), `NavigationAndMap.md` (HUD/minimap), and `Overview.md` (competitive positioning). This GDD is the **single source of truth** for how maps are designed and why.

> **Cross-References:** [Core Gameplay](CoreGameplay.md) — match timeline and zone events; [Navigation & HUD](NavigationAndMap.md) — minimap, compass, floor switching, ping system; [Loot Table Design](../Gameplay/Loot_Table_Design.md) — per-zone loot spawn tables; [Environmental Hazards](../Gameplay/Environmental_Hazards.md) — contamination zone mechanics; [Camera System](../Gameplay/Camera_System.md) — top-down view constraints and readability requirements; [GameModes](GameModes.md) — mode-specific map rules.

---

## 1. Design Philosophy

### Extraction Map vs. Battle Royale Map

Our maps are **extraction maps**, not battle royale maps. The distinction is critical:

| Attribute | Battle Royale Map | Extraction Map |
| :-------- | :--------------- | :------------- |
| Size | Massive (few km²) | Medium (300×300m – 600×600m) |
| Goal | Survive to last | Extract with loot |
| Zone design | 1 ring shrinking | Multiple zones with distinct identities |
| Traversal | Vehicle-focused | Foot travel with strategic positioning |
| Pacing | Slow opening, frantic ending | Constant tension, multiple intensity spikes |
| Player density | Low-density (large map) | High-density (small map, many encounters) |
| Replayability | Map knowledge less critical | Map mastery is a core skill |

### Top-Down Perspective Design Constraints

Because our game uses a **top-down camera** (see [Camera System](../Gameplay/Camera_System.md)), map design has specific readability requirements that differ from FPS extraction:

| Concern | FPS Design | Our Top-Down Design |
| :------ | :--------- | :------------------ |
| Height difference | Cover behind walls | Cover requires objects player can hide *under* the camera's view |
| Line of sight | Eye-level corridors | Overhead LOS — players can see further but can also be seen |
| Building interiors | Enter and clear room-by-room | Buildings are multi-floor; floors are switched via UI (see NavigationAndMap) |
| Skybox | Fully rendered | Simplified (performance); building roofs become tactical positions |
| Readability at range | FoV limits distant info | Top-down exposes more of the map — more information = more tactical decisions |
| Cover design | Walls, doorways | Containers, vehicles, low walls, floor-height variations |

---

## 2. Map Size & Scale Standards

| Map Tier | Playable Area | Player Count | Match Duration | Description |
| :------- | :------------ | :----------- | :------------- | :---------- |
| **Standard** | 400×400m | 8–16 players | 15–20 min | Core raid maps — most common |
| **Blitz** | 150×150m | 6–10 players | 8 min | Small subset of standard map, extreme density |
| **Co-op** | 250×250m | 1–3 players | 15 min | Enclosed, defensible — PvE optimized |

**Scale rule:** 1 map unit = 1 real-world meter. All movement speeds, audio ranges, and sniper ranges are calibrated to this scale.

### Minimum Room Sizes

| Room Type | Min Width | Min Height (clearance) | Purpose |
| :-------- | :-------- | :--------------------- | :------ |
| Corridor | 3m | 3.5m | Single-file movement; tight tension |
| Fight room | 6m × 6m | 4m | 2v2 close-quarters; cover needed |
| Large interior | 12m × 8m | 5m | Multi-squad encounters possible |
| Open courtyard | 20m × 20m | Open sky | Long-range engagement; sniper viable |
| Extraction zone | 8m × 8m | Open | Enough room for trio + fight while waiting |

---

## 3. Zone Anatomy — Every Map Must Have

Each standard raid map is divided into **three concentric zone types** and a **transition zone** between each. No map launches without all three.

```
MAP ZONE LAYOUT — SCHEMATIC VIEW (400×400m)
┌─────────────────────────────────────────────────────────┐
│░░░░░░░░░░░░░  PERIMETER SAFE ZONE  ░░░░░░░░░░░░░░░░░░░░│  ← Spawn ring (first 60s)
│░░                                                    ░░░│
│░░  ┌───────────────────────────────────────────────┐ ░░│
│░░  │▒▒▒▒▒▒▒▒▒▒▒  MID ZONE  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│ ░░│  ← Primary loot, PvP starts here
│░░  │▒▒                                         ▒▒▒│ ░░│
│░░  │▒▒  ┌──────────────────────────────────┐  ▒▒▒│ ░░│
│░░  │▒▒  │████████  HOT ZONE  ████████████│  ▒▒▒│ ░░│  ← High loot, Boss, Supply Drop
│░░  │▒▒  │████         [BOSS]         ████│  ▒▒▒│ ░░│
│░░  │▒▒  │████     [OBJECTIVE]        ████│  ▒▒▒│ ░░│
│░░  │▒▒  └──────────────────────────────────┘  ▒▒▒│ ░░│
│░░  │▒▒                                         ▒▒▒│ ░░│
│░░  └───────────────────────────────────────────────┘ ░░│
│░░                                                    ░░░│
│░░ [EXTRACT A]    [EXTRACT B]    [EXTRACT C]  [EXTRACT D]│  ← 3–4 extractions, spaced
└─────────────────────────────────────────────────────────┘
```

### Zone Definitions

| Zone | Coverage of Map | Loot Tier | AI Density | PvP Intensity | Design Role |
| :--- | :-------------- | :-------- | :--------- | :------------ | :---------- |
| **Safe Zone** (perimeter) | 40% area | Common–Uncommon | Low | Very low | Spawn safety; entry/exit routing |
| **Mid Zone** | 40% area | Uncommon–Rare | Medium | Medium | Core loot loop; player pathing convergence |
| **Hot Zone** (center) | 20% area | Rare–Legendary | High | Very high | High-risk decisions; boss room; supply drops |

**Design rule:** No player should ever need to go to the Hot Zone to extract. Extractions are placed in the Safe Zone and on the perimeter of Mid Zone. The decision to enter the Hot Zone is always **voluntary and rewarded**.

---

## 4. Extraction Point Placement Rules

### Count Per Map

| Map Size | Min Extractions | Max Extractions | Notes |
| :------- | :-------------- | :-------------- | :---- |
| Standard (400×400m) | 3 | 5 | 3 always active; 1–2 conditional |
| Blitz (150×150m) | 1 | 2 | 1 final extract, 1 optional mid-map |
| Co-op (250×250m) | 2 | 3 | At least 1 always open |

### Placement Rules

1. **Never place an extraction in the Hot Zone** — extractions must never be inside the highest-risk area.
2. **Spread extractions across all 4 map quadrants** — no two adjacent extractions within 150m of each other (standard map).
3. **Extraction zones must have 2+ approach angles** — no extraction that can only be reached from one direction (removes camping viability).
4. **At least 1 extraction per map must be reachable without crossing a contested high-traffic corridor** — for looting/avoidance playstyles.
5. **Conditional extractions (e.g., vehicle, keycard) are always optional** — standard extractions always exist as fallback.

### Extraction Zone Types (Per Map)

| Type | Count per Map | Condition | Timer | Capacity |
| :--- | :------------ | :-------- | :---- | :------- |
| **Standard Extract** | 3 | Always open | 30s | Unlimited |
| **Vehicle Extract** | 1 | First-come (4 max) | 45s countdown, then leaves | 4 players |
| **Hidden Extract** | 1–2 | Requires specific Area Key or quest completion | 15s | Unlimited |

---

## 5. Building & Interior Design Rules

### Multi-Floor Buildings

Buildings in top-down extraction maps are the **primary tactical complexity driver**. Rules:

| Rule | Detail |
| :--- | :----- |
| **Max floors:** 3 | Ground (G), First Floor (1F), Roof (R). More than 3 floors creates camera confusion. |
| **Floor legibility** | Every floor must be navigable with top-down camera showing interior from above |
| **Staircase placement** | At least 2 staircase/ladder entries per floor (avoid single-entry chokepoint floors) |
| **Roof access** | Roof level is a sniper/overwatch position — requires dedicated access staircase or ladder, never automatic |
| **Door density** | Every interior room must have minimum 2 doors OR 1 door + 1 window (no dead-end rooms without window escape) |

### Readability Standards (Top-Down)

| Requirement | Rule |
| :---------- | :--- |
| **Wall color contrast** | Walls must contrast with floor color — no grey-on-grey environments |
| **Cover object silhouettes** | All driveable/walkable cover objects must read clearly from overhead |
| **Loot container visibility** | Containers always visible from top-down without needing to change camera zoom below 90% |
| **Shadow indicators** | Multi-floor shadows indicate elevated terrain; consistent north-light rule |
| **Minimap accuracy** | Minimap faithfully represents actual traversable geometry. No "tunnel" spaces invisible on minimap |

---

## 6. Loot Zone Design

### Hot Zone: Mandatory Elements

Every Hot Zone must contain:
- [ ] At least **1 boss spawn point** (see [AI Enemy Behavior](../Gameplay/AI_Enemy_Behavior.md))
- [ ] At least **2 Safes** or equivalent high-tier containers
- [ ] At least **1 weapon rack**
- [ ] **Supply Drop landing zone** (cleared flat area, supplies drop at match event timer)
- [ ] **At least 2 AI Scav patrol paths** crossing through

### Mid Zone: Mandatory Elements

- [ ] Mix of **Metal Lockers, crates, and barrels** — medium loot density
- [ ] **Quest marker triggers** (most quest objectives in Mid Zone)
- [ ] **Scav patrol routes** that enter and exit (not stationary)
- [ ] **At least 4 pieces of destructible cover** (breakable crates, doors)
- [ ] **1 named location** (landmark name for callouts — e.g., "The Mill", "East Garage")

### Safe Zone: Mandatory Elements

- [ ] **Player spawn points** — at least 8 per zone on standard maps, spread with 30m separation minimum
- [ ] Low-tier loot (crates, barrels) — enough for budget loadout players to be useful
- [ ] **Camouflage terrain** — dense foliage, rubble, or vehicles for new-player protection
- [ ] Clear **visual path indicators** toward the Mid Zone

---

## 7. Traffic Flow & Bottleneck Design

Extraction maps thrive on **controlled player convergence** — players should naturally funnel toward conflict hotspots without feeling forced.

### Funnel Hierarchy

```
SAFE ZONE (spawn)
    │
    ├── 2-3 wide routes into Mid Zone (choice)
    │
MID ZONE
    │
    ├── 1-2 narrow choke routes into Hot Zone (risk decision point)
    │
HOT ZONE
    │
    └── 1 centralized boss/objective room (ultimate focal point)
```

### Choke Point Rules

| Choke Type | Width | Design Use | Max Count Per Map |
| :--------- | :---- | :--------- | :---------------- |
| **Hard choke** (bridges, doorways) | 2–3m | High-tension ambush point | 2 |
| **Soft choke** (open corridors between buildings) | 5–8m | Contested but escapable | 4 |
| **Wide approach** (open streets or fields) | 15m+ | Low-speed rotation; snipers viable | No limit |

**Anti-campability rule:** Every hard choke point must have at least one flanking route within 30m that lets players bypass it. Camping should be strong but not impenetrable.

---

## 8. Named Locations & Callout Design

Every map must have **named locations** for player callouts — critical for:
- Ping system ("Enemy spotted near [Mill]")
- Death log ("Killed by [Player] in [East Garage]")
- Quest objectives ("Retrieve item from [Generator Room]")

### Naming Rules

| Rule | Detail |
| :--- | :----- |
| **Names must be intuitive** | Based on visual identity of the area (Sawmill, Crane Yard, Generator Room) |
| **Max 12 named locations per standard map** | Too many names overwhelms new players |
| **At least 1 name per zone tier** | Safe Zone: 2 names, Mid Zone: 6 names, Hot Zone: 4 names |
| **No directional names alone** | "North" or "East" alone as a name is not sufficient — must be descriptive |
| **Names visible on minimap** | All named locations appear as text labels on the tactical map |

### Aethelgard Industrial Zone — Named Locations (Launch Map Example)

| Zone | Location Name | Description |
| :--- | :------------ | :---------- |
| Safe | **East Gate** | Primary spawn zone east side |
| Safe | **The Rail Yard** | Abandoned rail cars; western spawn area |
| Mid | **The Mill** | Central building complex; heavy cover |
| Mid | **Fuel Depot** | Explosive barrels; flanking route |
| Mid | **East Garage** | 2-floor building; contested loot |
| Mid | **Underground Passage** | Below-ground shortcut; dark |
| Mid | **Worker Barracks** | Dense indoor close-quarters |
| Mid | **Crane Yard** | Open area; snipers viable |
| Hot | **Generator Room** | Boss spawn room; basement level |
| Hot | **The Vault** | Safe room cluster; high loot |
| Hot | **Rooftop A** | 3F roof; long-range vantage |
| Hot | **Inner Courtyard** | Supply drop landing zone |

---

## 9. Weather Systems & Map State Variants

Each map has **4 weather variants** that rotate each match:

| Weather | Visibility | Audio Impact | Loot Impact | Frequency |
| :------ | :--------- | :----------- | :---------- | :-------- |
| **Clear** | Full (100m+ sightlines) | No change | Standard | 40% |
| **Overcast** | Good (reduced contrast, harder to spot at range) | Slight wind noise | +Medical supplies 10% | 30% |
| **Rain** | Moderate (fog of war reduces to 60m) | Rain masks footsteps | No loot change | 20% |
| **Heavy Fog** | Low (20m visibility cap) | Complete footstep masking | -Rare items 10%; +Common +20% | 10% |

**Design intent:** Weather variants incentivize different operator and playstyle selections. Heavy Fog is a powerful Recon/Scout advantage. Clear weather favors Sniper-equipped assault builds.

Weather is **shown as a badge on the Map Card** in the Loadout Preparation screen (see [Loadout Preparation](LoadoutPreparation.md)) so players can adjust their kit accordingly.

---

## 10. Cross-Map Design Consistency Rules

All maps must pass these checks before shipping:

| Check | Requirement |
| :---- | :---------- |
| **3-zone coverage** | Safe / Mid / Hot zones clearly defined and balanced by area |
| **Extraction spread** | Min 3 standard extractions, in different quadrants |
| **Anti-camping** | Every hard choke has a flank within 30m |
| **Readability** | Top-down camera at default zoom shows all navigable paths |
| **Audio zones** | Gunshots audible across Mid→Mid; not guaranteed across Safe→Hot |
| **AI patrol coverage** | At least 2 AI patrol routes that cross all three zone tiers |
| **Named locations** | 10–12 named locations, visible on minimap |
| **Boss room** | 1 boss spawn in Hot Zone; accessible from 2+ directions |
| **Quest hooks** | At least 3 quest objective trigger locations |
| **Performance** | Target 60fps on mid-range device at peak player count |

---

## Cross-References

- [Core Gameplay](CoreGameplay.md) — Match timeline events (supply drops at 5:00, contamination at 12:00) calibrated to standard map size.
- [Navigation & HUD](NavigationAndMap.md) — Minimap, compass, multi-floor layer system, ping points all derived from map named locations.
- [Loot Table Design](../Gameplay/Loot_Table_Design.md) — Per-zone spawn tables; loot tier thresholds per zone type.
- [Environmental Hazards](../Gameplay/Environmental_Hazards.md) — Contamination zone emergence from map edges inward; weather impact rules.
- [Camera System](../Gameplay/Camera_System.md) — Top-down perspective constraints; readability requirements; LOS implementation.
- [AI Enemy Behavior](../Gameplay/AI_Enemy_Behavior.md) — AI patrol routes; boss spawn rooms; Scav density per zone.
- [GameModes](GameModes.md) — Blitz uses subset of standard map; Co-op uses dedicated enclosed map variant.
- [Loadout Preparation](LoadoutPreparation.md) — Map card displays weather, loot bias, and risk rating sourced from map variant data.
