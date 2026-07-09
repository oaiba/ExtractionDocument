---
title: "Map Design - Level & Zone Design Rules"
type: docs
---

## Tổng Quan

Map Design defines how extraction zones are built for top-down tactical play. Maps must tạo dễ đọc routes, meaningful risk gradients, rõ extraction choices, và strong landmarks mà không becoming battle royale arenas.

Each map should behave like a pressure machine. Spawns give người chơi enough room to form a plan, mid-zones tempt them với better giá trị, hotspots tạo collision, và extraction routes ask whether the hiện tại haul is worth protecting. The map is successful khi Người chơi có thể explain their route sau the raid: where they went, why they turned, where they heard danger, và why extraction felt possible hoặc impossible.

Top-down readability is the governing constraint. A beautiful space that hides threats, blocks touch movement, hoặc makes floor levels ambiguous is not ready for production. Landmarks, silhouettes, lighting, sound, và minimap language must all reinforce the same route quyết định.

## Quyết Định Chính

| Area | Direction |
| :--- | :--- |
| primary map role | Support extraction quyết định, not last-người chơi-standing collapse |
| Camera assumption | Top-down tactical view với occlusion handling |
| Raid duration | 10-15 minutes |
| cốt lõi tension | High-giá trị loot pulls người chơi inward; extraction pulls them outward |
| Readability target | Threat, cover, path, floor level, và extraction trạng thái dễ đọc on mobile |

## Zone Model

Zones are not just loot bands. They are pacing tools. Edge zones teach the map và give low-pressure giá trị, mid-zones tạo branching quyết định, và hot zones tạo stories người chơi remember. Người chơi nên understand khi they are moving into danger trước the first shot is fired.

| Zone | Loot | AI Threat | người chơi Pressure | Design mục đích |
| :--- | :--- | :--- | :--- | :--- |
| Edge / Spawn | Common | Light | Low | Let người chơi orient và build confidence |
| Mid Zone | Common to Rare | Medium | Medium | tạo route quyết định và first contact |
| Hot Zone | Rare to Legendary | Heavy | High | tạo major risk/reward quyết định |
| Event Zone | Event-defined | Variable | Very high | Pull người chơi together for timed opportunities |
| Extraction Zone | Reward-neutral | Variable | High near end | Force commitment và route discipline |

## Raid Movement Logic

Routes should support different người chơi personalities. A cautious solo needs a survivable edge path. A confident squad needs a contestable route thông qua giá trị. A quest-focused người chơi needs a dễ đọc way to reach an objective và leave. These routes can intersect, nhưng they không nên collapse into one mandatory lane.

| quyết định Point | Safe Route | Balanced Route | High-Risk Route |
| :--- | :--- | :--- | :--- |
| Spawn on edge | Read nearby extraction và edge loot | Move toward mid-zone objective | Rush hotspot hoặc event zone |
| First loot choice | Common giá trị, low contact | Mixed loot, moderate contact | Rare loot, high contact |
| Rotation | Early extraction path | Mid-map flank to extraction | Contest center then rotate late |
| Final choice | Extract và bank loot | Extract hoặc re-enter based on squad trạng thái | Push final giá trị hoặc risk timeout |

## Extraction Placement Rules

Extraction placement is where the map cashes out its promises. nếu extraction is too safe, looting has no tension. nếu extraction is too random hoặc too campable, losses feel cheap. The best extraction point tạo a short, dễ đọc final test: commit, defend, và leave.

| Rule | yêu cầu |
| :--- | :--- |
| Minimum options | Each người chơi should have multiple plausible extraction routes |
| Distance | At least one extraction must require route planning, not immediate safety |
| Contestability | High-giá trị extracts should have dễ đọc risk và counterplay |
| Signaling | Extraction trạng thái phải được hiển thị rõ và audible trước commitment |
| Anti-camping | Cover, sightlines, alternate routes, và timers must limit hard camping |
| Mode support | Ranked, Scav, và events can modify extraction rules nhưng not clarity |

## Top-Down Readability

Readability issues phải được solved in level design trước UI tries to patch them. nếu roofs, props, fog, hoặc vertical floors hide critical combat information, the map should cách dùng cutaways, fade rules, simplified collision, hoặc stronger silhouettes. The HUD should confirm information, not rescue a confusing layout.

| Problem | Design Response |
| :--- | :--- |
| Tall buildings hide người chơi | cách dùng cutaways, fade roofs, outlines, hoặc floor indicators |
| Visual clutter hides loot | cách dùng rarity shapes, glow limits, và contextual labels |
| Verticality becomes confusing | Keep floor transitions explicit và minimize hidden sightlines |
| Cover is unclear | cách dùng nhất quán silhouettes và dễ đọc edge highlights |
| người chơi lose extraction direction | Compass, minimap, world marker, và audio cues reinforce each other |

## Building và Interior Rules

| Element | Guideline |
| :--- | :--- |
| Rooms | Large enough for touch movement, cover, và squad visibility |
| Corridors | Avoid long invisible kill tunnels; add side exits và dễ đọc cover |
| Doors | cách dùng as tactical information, not cheap surprise blockers |
| Windows | Support scouting và risk, nhưng avoid unreadable one-way shots |
| Stairs / elevators | Mark floor changes clearly in HUD và map |

## Loot Placement Rules

Loot placement should tell người chơi what kind of place they are entering. A clinic implies medical giá trị và quiet risk; an armory implies conflict; a server room implies tech rewards và flank routes. Repeated loot language giúp người chơi plan mà không memorizing every container spawn.

| Loot Type | Best Location | Risk yêu cầu |
| :--- | :--- | :--- |
| Medical | Clinics, ambulances, checkpoints | Low to medium |
| Industrial | Factories, warehouses, maintenance rooms | Medium |
| Military | Checkpoints, armories, command rooms | High |
| Tech | Labs, offices, server rooms | Medium to high |
| Legendary | Hot zones, bosses, events, locked rooms | Very high |

## Encounter Examples

A safe edge route might contain low-giá trị containers, one light AI patrol, và a rõ extraction branch. It teaches the map và lets a cautious người chơi bank giá trị mà không becoming the best farming option.

A mid-zone route might split between a clinic, a warehouse, và a noisy shortcut. Người chơi có thể choose healing security, industrial giá trị, hoặc speed. Each option tạo different sound và sightline risks.

A hot zone should tạo a dễ đọc promise: rare giá trị is present, nhưng the route in và out is exposed, loud, hoặc AI-defended. Người chơi nên know they are entering a contested space trước the first fight begins.

## Map Failure Cases

- nếu người chơi repeatedly die mà không seeing the attacker, sightlines hoặc occlusion are failing.
- nếu extraction camping dominates, exits need alternate approaches, audio tells, hoặc timer changes.
- nếu all squads take the same route, loot và objective distribution are too centralized.
- nếu người chơi ignore interiors, room scale, entry risk, hoặc rewards may be wrong.
- nếu mobile người chơi miss stairs hoặc doors, floor markers và silhouettes need stronger treatment.

## Map Tuning Knobs

- Spawn spacing controls early safety; crowded spawns tạo cheap deaths trước planning begins.
- Loot density controls route pressure; dense hotspots need multiple dễ đọc exits.
- Landmark strength controls memory; every major route should have a nameable reference point.
- Extraction distance controls commitment; short routes reduce tension và long routes punish slow người chơi.
- AI placement controls information; AI can reveal routes, protect giá trị, và tạo sound pressure.
- Cover spacing controls combat rhythm; too little cover tạo aim checks, too much tạo stalemates.

## Map Readiness checklist

| Check | Pass Criteria |
| :--- | :--- |
| Route clarity | New người chơi can identify at least two plausible paths |
| Hotspot clarity | High-giá trị areas are visually và mechanically obvious |
| Extraction fairness | Extracts are contestable nhưng not impossible |
| Mobile readability | Threats và cover remain dễ đọc on 5 inch màn hình |
| Spawn fairness | Spawn positions avoid immediate unavoidable deaths |
| Audio support | chính threats và extraction events have rõ sound cues |

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| Raid pacing | [cốt lõi Gameplay](coregameplay.html) |
| Map UI và pings | [Navigation & Map](navigationandmap.html) |
| Mode variations | [Game Modes](gamemodes.html) |
| Loadout map selection | [Loadout Preparation](loadoutpreparation.html) |
