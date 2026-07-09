---
title: "Environmental Hazards & Dynamic Events"
type: docs
weight: 5
---

### Tổng Quan

The raid environment is not a static backdrop — it is an active participant in gameplay. Weather hệ thống reduce visibility, zone hazards restrict movement, dynamic events tạo flashpoints of activity, và the raid timer imposes an ever-tightening deadline. Together, these hệ thống ensure that no two raids play the same way.

> Xem [cốt lõi Gameplay cơ chế](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/CoreGameplay/README.md) để xem chi tiết minute-by-minute match timeline. This tài liệu focuses on the design intent và cơ chế of environmental hệ thống.

***

### Weather hệ thống

Weather conditions are determined at the start of each raid và persist for the entire session. Each weather type alters gameplay in cụ thể, predictable ways that Người chơi có thể plan around.

#### Weather Types

| Weather          | Visibility                                                        | Audio Impact                                                                      | Movement Impact                                                 | Tactical Effect                                                                           |
| ---------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **rõ**        | Full (100m+)                                                      | Normal sound propagation                                                          | None                                                            | Baseline. Snipers và long-range người chơi advantaged                                       |
| **Rain (Light)** | Reduced to 80m                                                    | Ambient rain masks quiet sounds. Footstep range reduced by 20%                    | Slightly louder grass/gravel                                    | Stealth người chơi gain advantage. Snipers suffer                                            |
| **Rain (Heavy)** | Reduced to 50m                                                    | Heavy rain masks most sounds. Footstep range reduced by 40%                       | Metal surfaces become slippery (brief stumble chance on sprint) | Close-quarters combat dominant. Extraction under cover preferred                          |
| **Fog**          | Reduced to 25-30m                                                 | No change                                                                         | None                                                            | Extreme close-quarters. Shotguns và SMGs dominate. Long-range vũ khí useless            |
| **Overcast**     | Reduced to 70m                                                    | Slightly muffled                                                                  | None                                                            | Moderate visibility loss. Balanced conditions                                             |
| **Night**        | Dependent on light sources (flashlight: 20m, NVG: 40m green-tint) | Louder perceived sounds (heightened awareness)                                    | None                                                            | Flashlights required nhưng reveal position. NVG is a significant advantage. Tracers hiển thị rõ |
| **Storm**        | Reduced to 40m                                                    | Thunder masks gunshots periodically. Lightning illuminates briefly (0.5s flashes) | Wind slows movement by 5%. Sprint stamina drain +15%            | Unpredictable visibility. Opportunistic gameplay                                          |

#### Weather Briefing

* Weather is displayed trong khi the **matchmaking màn hình** trước deployment
* Người chơi có thể adjust loadout based on weather (e.g., bring a flashlight for night raids, switch to a shotgun for fog)
* Weather does not change mid-raid — what you see trong khi briefing is what you get

#### Weather Distribution

| Weather      | Frequency | thời gian of Day Association |
| ------------ | :-------: | ----------------------- |
| rõ        |    35%    | Day                     |
| Overcast     |    20%    | Day                     |
| Rain (Light) |    15%    | Day hoặc Dusk             |
| Rain (Heavy) |    10%    | Day hoặc Night            |
| Fog          |    10%    | Dawn hoặc Dusk            |
| Night        |     7%    | Night only              |
| Storm        |     3%    | Any                     |

***

### Zone Hazards

Certain map areas contain persistent environmental dangers that restrict movement, require special equipment, hoặc deal damage over thời gian.

#### Hazard Types

| Hazard                   | Location                                     | Effect                                                           | Duration                         | Protection                                                                         |
| ------------------------ | -------------------------------------------- | ---------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------- |
| **Radiation Zone**       | Industrial areas, old reactors, crash sites  | 5-15 HP/sec. màn hình yellows/distorts                             | Persistent                       | Gas mask + radiation filter (consumable, 120s duration)                            |
| **Chemical Spill**       | Laboratories, storage facilities             | 3 HP/sec + "Intoxication" debuff (blurred vision, -20% accuracy) | Persistent                       | Gas mask + chemical filter (consumable, 90s duration)                              |
| **Minefield**            | Perimeter zones, military checkpoints        | Instant 120 damage on trigger. Loud explosion (audible 100m+)    | Permanent until triggered        | Visual detection (partially buried, disturbed dirt). Prone movement avoids trigger |
| **Collapsed Structure**  | Earthquake-damaged buildings                 | Random debris falls dealing 20-50 damage. Navigation difficulty  | Persistent                       | Avoid standing under damaged ceilings. Move thông qua quickly                        |
| **Flooded Area**         | Basements, low-ground terrain                | Movement speed -40%. Cannot sprint. vũ khí sway increased        | Persistent, water level varies   | Wade thông qua quickly. No mitigation                                                |
| **Dark Zone** (interior) | Underground tunnels, basements mà không power | Zero ambient light. Must cách dùng flashlight hoặc NVG                   | Persistent unless power restored | Flashlight (reveals position) hoặc NVG (expensive)                                   |

#### Hazard Design Principles

1. **Risk-Reward Balance**: The most hazardous zones must contain the highest-giá trị loot. Radiation zones guard rare components. Minefields protect shortcut routes.
2. **Equipment Check**: Hazardous zones reward người chơi who brought the right gear. Gas masks consume inventory space và add weight — are they worth packing?
3. **Audio cảnh báo**: Each hazard has a distinct ambient sound (Geiger counter ticking, chemical hissing, structural groaning) that alerts attentive người chơi trước they enter the danger zone.
4. **Bypass Options**: Every hazardous zone has a safe (nhưng longer) route around it. The hazard tạo a choice: fast và dangerous, hoặc slow và safe.

#### Performance (Cross-Platform)

Weather và hazard effects cách dùng the same gameplay rules on all platforms. On mobile và low-end devices, particle density, fog resolution, và distant weather LOD may be reduced for performance; damage, visibility ranges, và audio cues remain unchanged. Xem [Asset Guidelines](https://github.com/oaiba/ExtractionDocument/blob/main/content/Visuals/AssetGuidelines.md) for cross-platform LOD và effect budgets.

***

### Contamination cơ chế

Contamination is the primary end-of-raid pressure hệ thống. It replaces a traditional battle-royale-style shrinking circle với a thematic in-world event.

#### Timeline

| thời gian                   | Event                                                                   | người chơi Impact                                                          |
| ---------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 12:00 (of 15:00 total) | **cảnh báo**: "Contamination incoming" alert. Red zone appears on map    | 30 seconds to plan. Most người chơi begin moving toward extraction        |
| 12:30                  | **Contamination Active (Phase 1)**: Outer edges of map become hazardous | 10 HP/sec in contaminated zone. Playable area shrinks inward           |
| 13:30                  | **Contamination Escalation (Phase 2)**: Zone shrinks further            | 25 HP/sec. Only central zones remain safe. Extraction becomes critical |
| 14:30                  | **Final Push (Phase 3)**: Almost entire map is contaminated             | 50 HP/sec. Only extraction zone interiors are safe                     |
| 15:00                  | **Match Ends**: All remaining người chơi die                               | Total loss of gear. No extraction possible                             |

For **standard raids** (25–30 min, Xem [cốt lõi Gameplay Loop](CoreLoop.md)), contamination triggers in the final third of the raid; phases scale proportionally. The bảng above is for a **15-min Quick Raid** hoặc reference scale.

#### Contamination Visual và Audio Design

* **Visual**: Green/yellow toxic fog rolling in from the map edges. Affected areas have particle effects và color desaturation.
* **Audio**: Deep rumbling horn at cảnh báo phase. Escalating alarm tones at each phase. Within contamination: muffled audio, heavy breathing, coughing.
* **HUD**: Timer prominently displayed. Contamination zone boundary shown on minimap in pulsing red.

#### Why Contamination Instead of a Shrinking Circle?

* **Thematic Fit**: Contamination feels organic in an extraction world (chemical leak, radiation event, gas attack) rather than an arbitrary game cơ chế.
* **Pacing Control**: The 3-minute cảnh báo gives người chơi thời gian to make deliberate quyết định rather than panic.
* **Extraction Integration**: Contamination drives người chơi toward extraction zones, tạo natural hotspots for final encounters.

***

### Dynamic Events

Dynamic events inject unpredictability into each raid. They are randomized, với each raid featuring 2-3 events from the pool.

#### Event Types

**Supply Drop**

| Property     | chi tiết                                                                                   |
| ------------ | ---------------------------------------------------------------------------------------- |
| Trigger      | Scheduled at 5:00 và 10:00 into the raid                                                |
| Notification | Map-wide announcement: location marked, cargo plane audio                                |
| Loot Quality | Epic-Legendary (70/30 split)                                                             |
| Container    | 5-10 high-giá trị items in an armored crate                                                |
| Risk         | Bright smoke signal hiển thị rõ at 100m+. Multiple squads converge. Highest PvP density zone |

**AI Boss Spawn**

| Property     | chi tiết                                                                                                               |
| ------------ | -------------------------------------------------------------------------------------------------------------------- |
| Trigger      | Random, 30% chance per raid. Spawns between 3:00 và 8:00                                                            |
| Notification | Distant unique audio cue (e.g., heavy machinery, distinct boss roar/call sign)                                       |
| Boss Type    | Heavily armored AI với unique behavior (patrol route, retreat, call reinforcements)                                 |
| Loot         | Boss drops a guaranteed Rare+ vũ khí và a unique chính/keycard to a high-giá trị room                                   |
| Risk         | Boss is extremely dangerous. Can alert nearby người chơi to the fight. Fighting the boss is a loud, extended engagement |

**Power Outage**

| Property | chi tiết                                                                                                                                        |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Trigger  | Random, 20% chance per raid. Occurs at any point sau 2:00                                                                                   |
| Effect   | All electric lights on the map turn off. Powered doors lock/unlock. Security cameras deactivate                                               |
| Duration | Permanent for the remainder of the raid (power cannot be restored)                                                                            |
| Impact   | Interior areas become Dark Zones. người chơi mà không flashlights/NVGs are severely disadvantaged. Some previously locked areas become accessible |

**Helicopter Crash Site**

| Property     | chi tiết                                                                                                    |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Trigger      | Random, 15% chance per raid. Occurs between 4:00 và 7:00                                                 |
| Notification | Helicopter flying overhead, followed by crash explosion (audible map-wide). Smoke column hiển thị rõ at 200m+ |
| Loot         | Military-grade vũ khí, rare attachments, đạn crates. 8-12 high-giá trị items                              |
| Hazard       | Fire around crash site deals 10 HP/sec. Smoke reduces visibility to 10m in immediate area                 |

**Scav Raid (AI Wave)**

| Property | chi tiết                                                                                                                 |
| -------- | ---------------------------------------------------------------------------------------------------------------------- |
| Trigger  | Random, 25% chance per raid. Occurs between 6:00 và 10:00                                                             |
| Effect   | A wave of 6-10 AI scavengers spawns at a random point on the map và patrols aggressively                              |
| Impact   | Increased PvE danger. Gunfire from AI engagements draws người chơi attention. Scav corpses can be looted for mid-tier gear |

#### Event Design Principles

1. **Information Asymmetry**: Events provide information to all người chơi simultaneously. Those who react faster gain an advantage.
2. **Optional Engagement**: No event forces người chơi participation. A người chơi can always choose to ignore the supply drop và extract quietly.
3. **Risk Escalation**: Events tạo concentrated danger. Multiple người chơi converging on the same location increases PvP encounter rate.
4. **Narrative Context**: Every event has an in-world explanation (supply convoy, rogue AI patrol, failed evacuation). This reinforces immersion.

***

### Raid Timer Design

#### Why 10-15 Minutes?

The raid duration is one of the most critical design parameters:

| Duration  | người chơi Behavior                                                                        | Session Fit                  | Tension Curve                                 |
| --------- | -------------------------------------------------------------------------------------- | ---------------------------- | --------------------------------------------- |
| < 8 min   | Too rushed. người chơi sprint to nearest loot và extract. Little exploration hoặc PvP      | Good for mobile sessions     | Flat — constant rush, no build-up             |
| 10-15 min | Balanced. Người chơi có thể explore, fight, và extract. Natural arc from cautious to urgent | Ideal for mobile và desktop | Rising arc — tension builds as thời gian decreases |
| > 20 min  | Too long. Mid-game becomes boring. người chơi camp và wait. Matches feel dragged out     | Poor for mobile              | Flat in the middle, spike at the end          |

#### Timer Visibility

* Timer is **always hiển thị rõ** on the HUD (top-right corner)
* Color changes: White (0-8 min), Yellow (8-12 min), Red (12-15 min)
* At 12:00: Timer font size increases và pulses
* At 14:00: Timer becomes fully red với alarm audio

#### What Happens khi thời gian Runs Out

* **14:30**: "FINAL cảnh báo" — màn hình edges flash red
* **15:00**: All người chơi still in the raid are killed instantly
* **Death by timeout** results in full gear loss (same as combat death)
* **No exceptions** — even người chơi in an extraction zone who have not completed the timer die

**Design Intent**: The absolute hard deadline ensures that no người chơi can wait indefinitely. The contamination hệ thống pushes người chơi toward extraction zones, và the hard timer ensures those who stall at extraction are punished.

***

### Environmental Interaction

#### Destructible và Interactive Objects

| Object          | Interaction                                                   | Sound                                      | Tactical cách dùng                                                                              |
| --------------- | ------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Wooden Door     | Open (quiet), Breach (sprint thông qua), Lock (với chính)        | Open: Low (5m), Breach: Very High (25m)    | Breach for surprise entry. Lock behind you for protection                                 |
| Metal Door      | Open only (cannot breach)                                     | Medium (10m hinge squeak)                  | Blocks certain paths. Some require keys                                                   |
| Breakable Glass | Shoot, melee, hoặc explosion                                    | High (20m shatter)                         | tạo surprise entry. Risk: alerts everyone nearby                                       |
| Windows         | Open (quiet, 1.5s), break (loud, instant)                     | Open: Low (5m), Break: High (20m)          | cách dùng opened windows for silent entry. Breaking is faster nhưng reveals position              |
| Light Switch    | Toggle room lights                                            | Low (3m click)                             | Turn off lights trước entering to gain dark advantage. Turn on lights to blind NVG users |
| Alarm hệ thống    | Triggered by opening certain doors/containers mà không the chính | Very High (40m siren, runs for 15 seconds) | Avoid by using the correct chính. Can be used as a distraction                              |
| Barricade       | Deploy from inventory item (wooden plank, wire)               | Medium (8m hammering/wiring)               | Block doorways to tạo safe rooms hoặc slow pursuer routes                                |

***

### Seasonal và Live Events

#### Seasonal Weather Rotation

| Season (Real-World Calendar) | Dominant Weather                                            | Special Hazard                                   | Thematic Loot            |
| ---------------------------- | ----------------------------------------------------------- | ------------------------------------------------ | ------------------------ |
| Spring (Mar-May)             | Rain, Fog                                                   | Flooded basements more common                    | Survival-themed items    |
| Summer (Jun-Aug)             | rõ, Storm                                                | Heat haze (visual distortion at range)           | Military surplus events  |
| Autumn (Sep-Nov)             | Overcast, Wind                                              | Reduced foliage cover (less natural concealment) | Harvest festival items   |
| Winter (Dec-Feb)             | Night priority, Snow (reduced traction, hiển thị rõ footprints) | Hypothermia risk mà không warm clothing           | Holiday-themed cosmetics |

#### Limited-thời gian Events

Examples of potential event types for live dịch vụ operation:

* **"Containment Breach"**: Radiation zones expand to cover 50% of the map. Gas masks become essential. Loot quality in radiated areas increases by 2x.
* **"Arms Race"**: Only vũ khí found in-raid can be used (no pre-equipped vũ khí). All vũ khí spawn rates doubled.
* **"Blackout"**: All raids are Night weather. Flashlight và NVG spawn rates tripled. Extraction zones are unlit.
* **"Boss Hunt"**: AI Boss spawn rate increased to 100%. Boss drops exclusive seasonal loot.

**Design Intent**: Seasonal và live events keep the meta fresh và give người chơi a reason to return trong khi cụ thể windows. Limited-thời gian events tạo urgency và community discussion.
