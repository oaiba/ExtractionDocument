---
title: Environmental Hazards & Dynamic Events
type: docs
weight: 5
---


### Overview

The raid environment is not a static backdrop — it is an active participant in gameplay. Weather systems reduce visibility, zone hazards restrict movement, dynamic events create flashpoints of activity, and the raid timer imposes an ever-tightening deadline. Together, these systems ensure that no two raids play the same way.

> See [Core Gameplay Mechanics](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/CoreGameplay/README.md) for the detailed minute-by-minute match timeline. This document focuses on the design intent and mechanics of environmental systems.

***

### Weather System

Weather conditions are determined at the start of each raid and persist for the entire session. Each weather type alters gameplay in specific, predictable ways that players can plan around.

#### Weather Types

| Weather          | Visibility                                                        | Audio Impact                                                                      | Movement Impact                                                 | Tactical Effect                                                                           |
| ---------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Clear**        | Full (100m+)                                                      | Normal sound propagation                                                          | None                                                            | Baseline. Snipers and long-range players advantaged                                       |
| **Rain (Light)** | Reduced to 80m                                                    | Ambient rain masks quiet sounds. Footstep range reduced by 20%                    | Slightly louder grass/gravel                                    | Stealth players gain advantage. Snipers suffer                                            |
| **Rain (Heavy)** | Reduced to 50m                                                    | Heavy rain masks most sounds. Footstep range reduced by 40%                       | Metal surfaces become slippery (brief stumble chance on sprint) | Close-quarters combat dominant. Extraction under cover preferred                          |
| **Fog**          | Reduced to 25-30m                                                 | No change                                                                         | None                                                            | Extreme close-quarters. Shotguns and SMGs dominate. Long-range weapons useless            |
| **Overcast**     | Reduced to 70m                                                    | Slightly muffled                                                                  | None                                                            | Moderate visibility loss. Balanced conditions                                             |
| **Night**        | Dependent on light sources (flashlight: 20m, NVG: 40m green-tint) | Louder perceived sounds (heightened awareness)                                    | None                                                            | Flashlights required but reveal position. NVG is a significant advantage. Tracers visible |
| **Storm**        | Reduced to 40m                                                    | Thunder masks gunshots periodically. Lightning illuminates briefly (0.5s flashes) | Wind slows movement by 5%. Sprint stamina drain +15%            | Unpredictable visibility. Opportunistic gameplay                                          |

#### Weather Briefing

* Weather is displayed during the **matchmaking screen** before deployment
* Players can adjust loadout based on weather (e.g., bring a flashlight for night raids, switch to a shotgun for fog)
* Weather does not change mid-raid — what you see during briefing is what you get

#### Weather Distribution

| Weather      | Frequency | Time of Day Association |
| ------------ | :-------: | ----------------------- |
| Clear        |    35%    | Day                     |
| Overcast     |    20%    | Day                     |
| Rain (Light) |    15%    | Day or Dusk             |
| Rain (Heavy) |    10%    | Day or Night            |
| Fog          |    10%    | Dawn or Dusk            |
| Night        |     7%    | Night only              |
| Storm        |     3%    | Any                     |

***

### Zone Hazards

Certain map areas contain persistent environmental dangers that restrict movement, require special equipment, or deal damage over time.

#### Hazard Types

| Hazard                   | Location                                     | Effect                                                           | Duration                         | Protection                                                                         |
| ------------------------ | -------------------------------------------- | ---------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------- |
| **Radiation Zone**       | Industrial areas, old reactors, crash sites  | 5-15 HP/sec. Screen yellows/distorts                             | Persistent                       | Gas mask + radiation filter (consumable, 120s duration)                            |
| **Chemical Spill**       | Laboratories, storage facilities             | 3 HP/sec + "Intoxication" debuff (blurred vision, -20% accuracy) | Persistent                       | Gas mask + chemical filter (consumable, 90s duration)                              |
| **Minefield**            | Perimeter zones, military checkpoints        | Instant 120 damage on trigger. Loud explosion (audible 100m+)    | Permanent until triggered        | Visual detection (partially buried, disturbed dirt). Prone movement avoids trigger |
| **Collapsed Structure**  | Earthquake-damaged buildings                 | Random debris falls dealing 20-50 damage. Navigation difficulty  | Persistent                       | Avoid standing under damaged ceilings. Move through quickly                        |
| **Flooded Area**         | Basements, low-ground terrain                | Movement speed -40%. Cannot sprint. Weapon sway increased        | Persistent, water level varies   | Wade through quickly. No mitigation                                                |
| **Dark Zone** (interior) | Underground tunnels, basements without power | Zero ambient light. Must use flashlight or NVG                   | Persistent unless power restored | Flashlight (reveals position) or NVG (expensive)                                   |

#### Hazard Design Principles

1. **Risk-Reward Balance**: The most hazardous zones must contain the highest-value loot. Radiation zones guard rare components. Minefields protect shortcut routes.
2. **Equipment Check**: Hazardous zones reward players who brought the right gear. Gas masks consume inventory space and add weight — are they worth packing?
3. **Audio Warning**: Each hazard has a distinct ambient sound (Geiger counter ticking, chemical hissing, structural groaning) that alerts attentive players before they enter the danger zone.
4. **Bypass Options**: Every hazardous zone has a safe (but longer) route around it. The hazard creates a choice: fast and dangerous, or slow and safe.

#### Performance (Cross-Platform)

Weather and hazard effects use the same gameplay rules on all platforms. On mobile and low-end devices, particle density, fog resolution, and distant weather LOD may be reduced for performance; damage, visibility ranges, and audio cues remain unchanged. See [Asset Guidelines](https://github.com/oaiba/ExtractionDocument/blob/main/content/Visuals/AssetGuidelines.md) for cross-platform LOD and effect budgets.

***

### Contamination Mechanic

Contamination is the primary end-of-raid pressure system. It replaces a traditional battle-royale-style shrinking circle with a thematic in-world event.

#### Timeline

| Time                   | Event                                                                   | Player Impact                                                          |
| ---------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 12:00 (of 15:00 total) | **Warning**: "Contamination incoming" alert. Red zone appears on map    | 30 seconds to plan. Most players begin moving toward extraction        |
| 12:30                  | **Contamination Active (Phase 1)**: Outer edges of map become hazardous | 10 HP/sec in contaminated zone. Playable area shrinks inward           |
| 13:30                  | **Contamination Escalation (Phase 2)**: Zone shrinks further            | 25 HP/sec. Only central zones remain safe. Extraction becomes critical |
| 14:30                  | **Final Push (Phase 3)**: Almost entire map is contaminated             | 50 HP/sec. Only extraction zone interiors are safe                     |
| 15:00                  | **Match Ends**: All remaining players die                               | Total loss of gear. No extraction possible                             |

For **standard raids** (25–30 min, see [Core Gameplay Loop](coreloop/index.html)), contamination triggers in the final third of the raid; phases scale proportionally. The table above is for a **15-min Quick Raid** or reference scale.

#### Contamination Visual and Audio Design

* **Visual**: Green/yellow toxic fog rolling in from the map edges. Affected areas have particle effects and color desaturation.
* **Audio**: Deep rumbling horn at warning phase. Escalating alarm tones at each phase. Within contamination: muffled audio, heavy breathing, coughing.
* **HUD**: Timer prominently displayed. Contamination zone boundary shown on minimap in pulsing red.

#### Why Contamination Instead of a Shrinking Circle?

* **Thematic Fit**: Contamination feels organic in an extraction world (chemical leak, radiation event, gas attack) rather than an arbitrary game mechanic.
* **Pacing Control**: The 3-minute warning gives players time to make deliberate decisions rather than panic.
* **Extraction Integration**: Contamination drives players toward extraction zones, creating natural hotspots for final encounters.

***

### Dynamic Events

Dynamic events inject unpredictability into each raid. They are randomized, with each raid featuring 2-3 events from the pool.

#### Event Types

**Supply Drop**

| Property     | Detail                                                                                   |
| ------------ | ---------------------------------------------------------------------------------------- |
| Trigger      | Scheduled at 5:00 and 10:00 into the raid                                                |
| Notification | Map-wide announcement: location marked, cargo plane audio                                |
| Loot Quality | Epic-Legendary (70/30 split)                                                             |
| Container    | 5-10 high-value items in an armored crate                                                |
| Risk         | Bright smoke signal visible at 100m+. Multiple squads converge. Highest PvP density zone |

**AI Boss Spawn**

| Property     | Detail                                                                                                               |
| ------------ | -------------------------------------------------------------------------------------------------------------------- |
| Trigger      | Random, 30% chance per raid. Spawns between 3:00 and 8:00                                                            |
| Notification | Distant unique audio cue (e.g., heavy machinery, distinct boss roar/call sign)                                       |
| Boss Type    | Heavily armored AI with unique behavior (patrol route, retreat, call reinforcements)                                 |
| Loot         | Boss drops a guaranteed Rare+ weapon and a unique key/keycard to a high-value room                                   |
| Risk         | Boss is extremely dangerous. Can alert nearby players to the fight. Fighting the boss is a loud, extended engagement |

**Power Outage**

| Property | Detail                                                                                                                                        |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Trigger  | Random, 20% chance per raid. Occurs at any point after 2:00                                                                                   |
| Effect   | All electric lights on the map turn off. Powered doors lock/unlock. Security cameras deactivate                                               |
| Duration | Permanent for the remainder of the raid (power cannot be restored)                                                                            |
| Impact   | Interior areas become Dark Zones. Players without flashlights/NVGs are severely disadvantaged. Some previously locked areas become accessible |

**Helicopter Crash Site**

| Property     | Detail                                                                                                    |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Trigger      | Random, 15% chance per raid. Occurs between 4:00 and 7:00                                                 |
| Notification | Helicopter flying overhead, followed by crash explosion (audible map-wide). Smoke column visible at 200m+ |
| Loot         | Military-grade weapons, rare attachments, ammo crates. 8-12 high-value items                              |
| Hazard       | Fire around crash site deals 10 HP/sec. Smoke reduces visibility to 10m in immediate area                 |

**Scav Raid (AI Wave)**

| Property | Detail                                                                                                                 |
| -------- | ---------------------------------------------------------------------------------------------------------------------- |
| Trigger  | Random, 25% chance per raid. Occurs between 6:00 and 10:00                                                             |
| Effect   | A wave of 6-10 AI scavengers spawns at a random point on the map and patrols aggressively                              |
| Impact   | Increased PvE danger. Gunfire from AI engagements draws player attention. Scav corpses can be looted for mid-tier gear |

#### Event Design Principles

1. **Information Asymmetry**: Events provide information to all players simultaneously. Those who react faster gain an advantage.
2. **Optional Engagement**: No event forces player participation. A player can always choose to ignore the supply drop and extract quietly.
3. **Risk Escalation**: Events create concentrated danger. Multiple players converging on the same location increases PvP encounter rate.
4. **Narrative Context**: Every event has an in-world explanation (supply convoy, rogue AI patrol, failed evacuation). This reinforces immersion.

***

### Raid Timer Design

#### Why 10-15 Minutes?

The raid duration is one of the most critical design parameters:

| Duration  | Player Behavior                                                                        | Session Fit                  | Tension Curve                                 |
| --------- | -------------------------------------------------------------------------------------- | ---------------------------- | --------------------------------------------- |
| < 8 min   | Too rushed. Players sprint to nearest loot and extract. Little exploration or PvP      | Good for mobile sessions     | Flat — constant rush, no build-up             |
| 10-15 min | Balanced. Players can explore, fight, and extract. Natural arc from cautious to urgent | Ideal for mobile and desktop | Rising arc — tension builds as time decreases |
| > 20 min  | Too long. Mid-game becomes boring. Players camp and wait. Matches feel dragged out     | Poor for mobile              | Flat in the middle, spike at the end          |

#### Timer Visibility

* Timer is **always visible** on the HUD (top-right corner)
* Color changes: White (0-8 min), Yellow (8-12 min), Red (12-15 min)
* At 12:00: Timer font size increases and pulses
* At 14:00: Timer becomes fully red with alarm audio

#### What Happens When Time Runs Out

* **14:30**: "FINAL WARNING" — screen edges flash red
* **15:00**: All players still in the raid are killed instantly
* **Death by timeout** results in full gear loss (same as combat death)
* **No exceptions** — even players in an extraction zone who have not completed the timer die

**Design Intent**: The absolute hard deadline ensures that no player can wait indefinitely. The contamination system pushes players toward extraction zones, and the hard timer ensures those who stall at extraction are punished.

***

### Environmental Interaction

#### Destructible and Interactive Objects

| Object          | Interaction                                                   | Sound                                      | Tactical Use                                                                              |
| --------------- | ------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Wooden Door     | Open (quiet), Breach (sprint through), Lock (with key)        | Open: Low (5m), Breach: Very High (25m)    | Breach for surprise entry. Lock behind you for protection                                 |
| Metal Door      | Open only (cannot breach)                                     | Medium (10m hinge squeak)                  | Blocks certain paths. Some require keys                                                   |
| Breakable Glass | Shoot, melee, or explosion                                    | High (20m shatter)                         | Create surprise entry. Risk: alerts everyone nearby                                       |
| Windows         | Open (quiet, 1.5s), break (loud, instant)                     | Open: Low (5m), Break: High (20m)          | Use opened windows for silent entry. Breaking is faster but reveals position              |
| Light Switch    | Toggle room lights                                            | Low (3m click)                             | Turn off lights before entering to gain dark advantage. Turn on lights to blind NVG users |
| Alarm System    | Triggered by opening certain doors/containers without the key | Very High (40m siren, runs for 15 seconds) | Avoid by using the correct key. Can be used as a distraction                              |
| Barricade       | Deploy from inventory item (wooden plank, wire)               | Medium (8m hammering/wiring)               | Block doorways to create safe rooms or slow pursuer routes                                |

***

### Seasonal and Live Events

#### Seasonal Weather Rotation

| Season (Real-World Calendar) | Dominant Weather                                            | Special Hazard                                   | Thematic Loot            |
| ---------------------------- | ----------------------------------------------------------- | ------------------------------------------------ | ------------------------ |
| Spring (Mar-May)             | Rain, Fog                                                   | Flooded basements more common                    | Survival-themed items    |
| Summer (Jun-Aug)             | Clear, Storm                                                | Heat haze (visual distortion at range)           | Military surplus events  |
| Autumn (Sep-Nov)             | Overcast, Wind                                              | Reduced foliage cover (less natural concealment) | Harvest festival items   |
| Winter (Dec-Feb)             | Night priority, Snow (reduced traction, visible footprints) | Hypothermia risk without warm clothing           | Holiday-themed cosmetics |

#### Limited-Time Events

Examples of potential event types for live service operation:

* **"Containment Breach"**: Radiation zones expand to cover 50% of the map. Gas masks become essential. Loot quality in radiated areas increases by 2x.
* **"Arms Race"**: Only weapons found in-raid can be used (no pre-equipped weapons). All weapon spawn rates doubled.
* **"Blackout"**: All raids are Night weather. Flashlight and NVG spawn rates tripled. Extraction zones are unlit.
* **"Boss Hunt"**: AI Boss spawn rate increased to 100%. Boss drops exclusive seasonal loot.

**Design Intent**: Seasonal and live events keep the meta fresh and give players a reason to return during specific windows. Limited-time events create urgency and community discussion.
