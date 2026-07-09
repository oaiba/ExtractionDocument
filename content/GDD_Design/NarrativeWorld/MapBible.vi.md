---
title: "Map Design Bible"
type: docs
weight: 7
---

### Tổng Quan

This tài liệu is the single authoritative reference for level design principles, environmental storytelling standards, và world feel. It merges **map design hệ thống** với **narrative art direction** — vì in extraction shooters, the two cannot be separated.

> **Cross-References:** [MapLayouts](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLayouts.md) — choke points, extraction points, POI combat data; [LootDistribution](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/LootDistribution.md) — heatmaps và container tables; Per-map lore in [MapLore\_Industrial](MapLore_Industrial.md) và [MapLore\_Urban](MapLore_Urban.md).

***

### Map Design Philosophy

**cốt lõi Principles:**

1. **Readability** — Top-down perspective requires rõ visual hierarchy. người chơi must understand zone type within 5 seconds of entering.
2. **Tactical Depth** — Multiple routes, cover options, và vertical elements at every scale.
3. **Risk vs. Reward** — Loot quality scales precisely với danger level. No good loot is ever safely accessible.
4. **Memorable Landmarks** — Distinct visual anchors so người chơi call out locations by name, not coordinates.

***

### Extraction-Shooter Design Factors

#### primary Factors

**1. Verticality**

* **định nghĩa:** How height và layers affect visibility, flanking, và position advantage.
* **Hot Zones:** 3+ floors, catwalks, multi-angle ambush positions
* **Mid Zones:** 2 floors, accessible rooftops for vantage
* **Edge Zones:** Ground level với natural elevation changes only

**2. Size**

* **định nghĩa:** Horizontal scale relative to match duration (travel thời gian vs. looting thời gian).
* **Hot Zones:** Condensed footprint, high asset density — forces encounters
* **Edge Zones:** Expansive — allows safe spawning và initial movement mà không being shot immediately

**3. Population**

* **định nghĩa:** người chơi và AI entity density per square meter.
* **Hot Zones:** Maximum density — peak người chơi convergence + Elite AI squads
* **Mid Zones:** Medium density — roaming AI patrols, transiting người chơi
* **Edge Zones:** Low density — scattered AI, spawning/extracting người chơi

#### secondary Factors

| Factor                   | Rule                                                                                                                 |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Spawn/Exit Points**    | Primarily Edge Zones. Conditional hot exits (rooftop helipads) exist nhưng are always high-risk                        |
| **Event Pockets (POIs)** | Supply drops và Contamination temporarily transform Mid Zones into combat-heavy Hot Zones                           |
| **Line of Sight**        | Hot Zones: frequent blind spots và LOS breaks for tactical movement. Edge Zones: longer sightlines, less hard cover |
| **Navigator Elements**   | Ziplines, jump pads, ladders bridge Mid Zone gaps hoặc provide rapid access to Hot Zone verticality                    |

***

### Zone Type Definitions

#### Hot Zones (Center Areas)

**Characteristics:**

* 60% loot spawn rate — Rare và Epic items
* Heavy AI presence (10–15 địch + Boss opportunities)
* Multiple entry points (5–7)
* Multi-floor vertical gameplay

**Design Goals:**

* Focal points for conflict và quyết định-making
* Reward người chơi who engage với risk
* Dynamic combat spaces that feel different each raid

#### Mid Zones (Transition Areas)

**Characteristics:**

* 40% loot spawn rate — Uncommon và Rare items
* Moderate AI (5–8 địch)
* 3–4 entry points
* Mixed indoor/outdoor environments

**Design Goals:**

* Provide safer nhưng still meaningful looting
* Connect Hot Zones to map edges
* offer tactical choices mà không forcing death

#### Edge Zones (Perimeter)

**Characteristics:**

* 20% loot spawn rate — Common items, basic supplies
* Minimal AI (0–3 địch)
* Open areas near extraction points

**Design Goals:**

* Safe spawn areas với protection window
* Quick escape routes và extraction defense positions
* "Breath" areas that give người chơi thời gian to assess trước committing inward

***

### Cover hệ thống Design

#### Cover Types

| Type           | Protection | Examples                                                             |
| -------------- | :--------: | -------------------------------------------------------------------- |
| **Full Cover** |    100%    | Concrete walls, thick pillars, armored vehicles, metal containers    |
| **Half Cover** |     60%    | Wooden crates, low walls, cars, machinery                            |
| **Soft Cover** |     30%    | Bushes (visual only), chain fences, thin walls, destructible objects |

**Design Rules:**

* Never leave large open areas mà không cover every 5–10m
* Mix cover heights — a field of same-height crates is boring và unrealistic
* Consider top-down sightlines specifically — horizontal cover that feels great in FPS may be invisible from above
* Destructible soft cover tạo dynamic mid-match terrain changes

***

### Verticality in Top-Down Perspective

#### Multi-Floor Building Design

| Challenge                      | Solution                                                                            |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| Floor distinction              | rõ visual differentiators per floor (color palette shift, ceiling height change) |
| Floor transparency             | khi người chơi is above, floors below become semi-transparent                          |
| Navigation clarity             | Minimap floor-indicator (F1/F2/F3/ROOF labels on minimap)                           |
| Height advantage communication | Shadow effects showing entities above/below người chơi level                            |

**Gameplay Impact of Verticality:**

* Rooftop sniping positions that reward map knowledge
* Ambush setups from above (pre-position on floor above trước target enters)
* Escape routes via ledge drop (take fall damage vs. fight thông qua stairwell)

***

### Extraction Zone Design

#### Per Map: 4–6 Extraction Points

**Placement Rules:**

* Edge Zones primarily, 300–400m from Hot Zones
* Cover available nearby for defensive setup
* Multiple approach routes (no single choke to campable spot)

#### Extraction Types

| Type                      | Visual Cue                        | Capacity | Wait       | Risk                          |
| ------------------------- | --------------------------------- | :------: | ---------- | ----------------------------- |
| **Helicopter Extract**    | Helicopter landing + visual flare |     4    | 30s        | High — sound audible map-wide |
| **Vehicle Extract**       | Armored truck approach            |     6    | 30s        | Medium                        |
| **Underground Tunnel**    | Manhole entrance                  |     2    | 45s (slow) | Low — hidden location         |
| **Paid Extract (Convoy)** | Signal + credits required         |     8    | 30s        | Medium — chi phí is the barrier  |
| **Late-Game Boat**        | Appears only at <3:00 remaining   |     3    | 20s        | High — only accessible late   |

**Activation Rules:**

* 2–3 extraction points active per match (random selection)
* Announced at 3-minute mark (người chơi plan extraction trước announcement)
* Protection timer prevents camping from spawn (extractions locked for first 3 minutes of match)

***

### Dynamic Map Elements

#### Supply Drops

| Property      | giá trị                                                               |
| ------------- | ------------------------------------------------------------------- |
| Timing        | 5:00 và 10:00 into match                                           |
| Landing Zone  | Random Mid-to-Hot zones                                             |
| Visual Signal | Map-wide: Plane flyover → cảnh báo siren → signal flare → parachute  |
| Contents      | High-tier vũ khí, giáp, stims, occasional quest items             |
| Effect        | tạo an instant high-heat PvP zone for 2–3 minutes sau landing |

#### Contamination Zone

| Property       | giá trị                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| Start          | 12:00 remaining                                                                                      |
| Visual         | Red fog expanding from center outward (inverse of battle royale — starts from center, works way out) |
| Damage         | 10 HP/sec → 50 HP/sec as match nears end                                                             |
| Mitigation     | Hazmat gear reduces damage by 60%. Gas Mask reduces by 40%                                           |
| Design mục đích | Forces movement, prevents camping, tạo late-match urgency                                        |

#### Environmental Hazards

| Hazard                                                  |   Damage  | ghi chú                                                           |
| ------------------------------------------------------- | :-------: | --------------------------------------------------------------- |
| Electrical Hazards (exposed wiring, sparking machinery) |  5 HP/sec | Map-persistent, always present                                  |
| Radiation Zones (map-cụ thể)                          | 10 HP/sec | Best loot located inside — risk/reward                          |
| Fire (dynamic, explosion-triggered)                     | 15 HP/sec | Spreads slowly; blocks paths; tạo dynamic cover destruction |

***

### Spawn hệ thống

**Spawn Point Rules:**

* 8–12 spawn locations per map
* Located near map edges only — never within 200m of Hot Zones
* Equidistant from Hot Zones (fairness across spawn positions)
* Random assignment với minimum 100m distance from other người chơi
* 10-second protection shield (prevents instant spawn killing)

**Anti-Spawn-Camp Rules:**

* No spawn points in direct sightlines from any POI
* Spawn points deactivated nếu an địch is within 150m
* Last 2 người chơi may not share spawn quadrant

***

### Navigation Design

#### Visual Landmarks

Each map requires **5–7 map-wide recognizable anchors** that người chơi cách dùng for callouts:

| Landmark Type                         | Why It Works                     | Design Rule                                                            |
| ------------------------------------- | -------------------------------- | ---------------------------------------------------------------------- |
| Tall structures (towers, smokestacks) | hiển thị rõ from anywhere on map     | phải được the tallest object in their zone by at least 20m               |
| Unique color schemes per area         | Zone instant identification      | Each major zone has a dominant hue that differs from neighbors         |
| Distinct lighting signatures          | Works even in darkness/fog       | Reactor = red emergency; Labs = clinical white; Forest = natural green |
| Architectural variety                 | Prevents "it all looks the same" | No two major POIs can share architectural style                        |

#### Minimap Standards

| Element                 | Standard                                                                         |
| ----------------------- | -------------------------------------------------------------------------------- |
| Zone color-coding       | Hot Zones = red tint, Mid = yellow tint, Edge = green tint                       |
| POI icons               | Permanent icons với name label on first discovery                               |
| Extraction markers      | Appear at 3-minute mark khi activated                                           |
| người chơi/địch indicators | người chơi = blue dot, squad = smaller blue; địch = red (conditional on visibility) |
| Floor indicator         | Small "F1/F2/F3" label attached to người chơi icon                                   |

***

### Map Balance Metrics

#### Target Distribution KPIs

| Metric          |      Target     | Alert Threshold                              |
| --------------- | :-------------: | -------------------------------------------- |
| Common items    | 60% of all loot | >70% = map feels punishingly empty           |
| Uncommon items  |       25%       | —                                            |
| Rare items      |       10%       | <8% = high-rep người chơi leave map prematurely |
| Epic items      |        4%       | —                                            |
| Legendary items |        1%       | >2% = economy inflation risk                 |

#### Combat Density Targets

| Zone       | % of All Deaths | Design Intent                            |
| ---------- | :-------------: | ---------------------------------------- |
| Hot Zones  |       40%       | Conflict magnet                          |
| Mid Zones  |       45%       | Where most mid-skill engagements occur   |
| Edge Zones |       15%       | Occasional ambushes near extraction only |

#### Extraction success

* Each extraction zone: 20–30% usage rate
* No single zone dominates (>40% = người chơi camping it; redesign access)

#### Heatmap Tracking (Live dịch vụ)

* người chơi death locations (identify camping spots và balance issues)
* Loot pickup locations (validate distribution is felt)
* thời gian-in-zone (confirm người chơi explore all zones, not just one)
* Path travel frequency (validate multiple routes are used, not just one optimal path)

***

### Weather & thời gian of Day

#### Launch

Static daytime lighting on all maps.

#### Post-Launch tính năng

| hệ thống          | Variants                                                                                                                               |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Weather**     | rõ (default), Rain (reduced visibility + louder footsteps), Fog (favors CQC + suppresses callouts), Sandstorm (Desert map cụ thể) |
| **thời gian of Day** | Day (launch), Dusk (S2 addition — different aesthetics), Night (S3 — introduces flashlight cơ chế, NVG gear advantage)              |

***

### Environmental Storytelling Principles

> These principles govern how **level art direction và prop placement** deliver narrative. For full per-map implementations, Xem [MapLore\_Industrial](MapLore_Industrial.md) và [MapLore\_Urban](MapLore_Urban.md). For lore delivery channels (audio logs, codex, etc.), Xem [Lore Delivery hệ thống](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Lore_Delivery.md).

#### cốt lõi Principle: "The Aftermath"

Every location must look like **something happened here right trước the người chơi arrived**. There are no static, pristine presets. The world decays, struggles, và changes — và every prop tells that story.

#### Three Narrative Layers

| Layer                                   | What It Shows                     | Example Assets                                                                         |
| --------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------- |
| **Layer 1: The Panic** (Immediate Past) | The moment society collapsed      | Suitcases spilled on highways; half-eaten meals; cars crashed into barricades          |
| **Layer 2: The Struggle** (Recent Past) | Survivors trying to live in ruins | Mattress in a bank vault; rain collectors from tarps; makeshift graves in a playground |
| **Layer 3: The Decay** (Present)        | Nature reclaiming the world       | Trees thông qua office floors; rust dripping down concrete; animals nesting in engines   |

#### Micro-Story Vignettes

Self-contained environmental scenes (dioramas) that tell a complete story mà không any text:

**The Last Stand:** Bathroom stall, subway station. Skeleton + revolver + one spent casing + door barricaded from inside. _Story: A survivor heard the threats coming, realized escape was impossible, và made a final choice. No log needed._

**The Deal Gone Wrong:** Alleyway behind a pharmacy. Two skeletons facing each other. Duffel bag of meds between them. Both have knives in their chests. _Story: A trade turned violent. The loot — the meds — is still there for the người chơi who finds this._

**The Hopeless Signal:** Rooftop generator + radio tower + "SOS" painted in white. Generator out of fuel. Skeleton sits by the radio, headphones on. _Story: Someone waited for rescue that never came._

#### Diegetic Loot Placement

Loot must make logical sense in its physical context. người chơi who **read the environment** find more loot:

| Loot Type        | DO Place In                                                 | DO NOT Place In                          |
| ---------------- | ----------------------------------------------------------- | ---------------------------------------- |
| Medical supplies | Ambulances, bathrooms, triage tents, office first aid boxes | Random wooden crates in industrial areas |
| vũ khí parts     | Workbenches, gun store ruins, police vehicle trunks         | Hospital supply closets                  |
| Food/Water       | Kitchens, supermarkets, vending machines (broken)           | Reactor cooling rooms                    |
| Electronics      | Server rooms, offices, labs                                 | Warehouses built for cơ chế parts    |

#### Lighting as Narrative

| Light Color  | Meaning                                            | người chơi Reaction                                                          |
| ------------ | -------------------------------------------------- | ------------------------------------------------------------------------ |
|  Red       | Danger, emergency, "Do Not Enter"                  | Curiosity — người chơi investigate; risk implied                            |
|  Green     | Safety, medical, "Exit"                            | Relief — người chơi cách dùng green-lit paths to feel safer                       |
|  Flickering | Instability, recent damage, something still active | Tension — flickering vent light implies something moved thông qua recently |
|  Cold Blue | Technology, data, Nexus Corp presence              | Unease — clinical và inhuman; Tech Syndicate aesthetic                  |

#### Bloodstain Storytelling Rules

| Bloodstain Type     | Reads As                                | Usage Rule                                  |
| ------------------- | --------------------------------------- | ------------------------------------------- |
| Radial splatter     | Violence, gunfire — death happened here | Place at combat scenes only                 |
| Large static pool   | Body rested here a long thời gian            | cách dùng với a nearby skeleton hoặc drag marks    |
| Drag marks (linear) | Body was moved                          | Always lead somewhere — never end at a wall |
| Handprints on wall  | Wounded person crawling                 | Connect to a medical item cache nearby      |

#### Narrative Anti-Patterns (DO NOT)

1. **Diary ghi chú everywhere** — Avoid "My Dearest Diary..." trang in illogical locations. Environmental clues first, text last.
2. **Blood mà không điểm đến** — nếu there's a blood trail, it must lead somewhere. Never let it end at a wall.
3. **Halloween prop skeletons** — Skeletons nên được disarticulated, scavenged, hoặc crushed. No perfect poses.
4. **Graffiti mà không voice** — Every piece of graffiti must have an implied author. "WHO IS THE BROKER?" feels human; random symbols don't.

***

### Level Design checklist

For each new map, verify:

**Layout:**

* [ ] Balanced hot/mid/edge zone ratio (\~15% Hot, \~40% Mid, \~45% Edge by area)
* [ ] Multiple routes between all major POIs (minimum 3 paths to each Hot Zone)
* [ ] No dead-end areas anywhere on the map
* [ ] Extraction zone placement (edge-only, 300m+ from Hot Zones)
* [ ] Spawn point placement (edge-only, equidistant, 100m min distance)

**Loot:**

* [ ] Container placement (200–300 total)
* [ ] Rarity distribution balanced per targets above
* [ ] Quest item locations documented
* [ ] Supply drop landing zones rõ of permanent obstacles

**Combat:**

* [ ] Cover density appropriate per zone type
* [ ] Sightline variety (no single line of sight that dominates entire zone)
* [ ] Flanking routes available for every major position
* [ ] Vertical elements confirmed in all Hot Zone buildings

**Navigation:**

* [ ] 5–7 map-wide visual landmarks
* [ ] Minimap dễ đọc at 1:1 design scale
* [ ] Wayfinding rõ from ground level (no "maze" feeling)
* [ ] Zone transitions smooth và visually distinct

**Environmental Storytelling:**

* [ ] 3 narrative layers present in each major POI
* [ ] At least 3 micro-story vignettes per map
* [ ] Diegetic loot placement reviewed (no illogical containers)
* [ ] Lighting language nhất quán với zone tone

**Performance:**

* [ ] Occlusion volumes configured
* [ ] LOD configured for all assets
* [ ] Draw calls within budget
* [ ] Collision geometry simplified

**Playtesting:**

* [ ] 10+ internal playtests completed
* [ ] Heatmap analysis reviewed (death locations, loot pickup)
* [ ] Balance adjustments made
* [ ] Bug report rõ

***

### Map Rotation & Voting

**Launch:**

* 2 maps in active rotation
* Random selection per session

**Post-Launch:**

* Map voting from 3 options (weighted random prevents repeats)
* Featured map trong khi live events

### Future Map Concepts

| Map                    | Theme                       | chính tính năng                                     |
| ---------------------- | --------------------------- | ----------------------------------------------- |
| **Flooded City**       | Water + urban post-disaster | Boat navigation; underwater passages            |
| **Mountain Facility**  | Snowy, remote               | Cable cars; avalanche hazard events             |
| **Abandoned Airport**  | Huge open tarmac            | Long-range specialist map; plane wreck Hot Zone |
| **Underground Bunker** | Cold War facility           | No natural light; flashlight required           |
