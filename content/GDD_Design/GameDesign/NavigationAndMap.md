---
title: "Navigation & Map System Design"
type: docs
---

##  System Overview

The **Navigation & Map System** is the player's primary tool for situational awareness in the Extraction zone. Unlike traditional shooters where red dots reveal enemies, Extraction Shooters rely on **Intel-based Navigation**. The system prioritizes sound, line-of-sight, and tactical markings over "god-mode" radar.

**Key Design Pillars:**
1.  **Intel over Omniscience:** The map shows *known* info, not *all* info.
2.  **Communication Focus:** Pings and Markers replace voice chat for rapid tactical coordination.
3.  **Diegetic Integration:** UI elements should feel like tactical augmented reality (AR) gear.
4.  **Audio-Visual Synergy:** Visualizing sound (footsteps/gunfire) for mobile accessibility.

---

##  HUD Compass Ring

Instead of a First-Person Shooter (FPS) style horizontal "Compass Tape", the compass is **integrated directly into the Minimap border**.

### Design & Behavior
The compass is a **Ring** surrounding the square/circular Minimap at the top-right corner.

*   **Visual Style:** A calibrated ring with Cardinal Directions (N, E, S, W) and degree ticks.
*   **Rotation Logic:** Depends on Minimap settings (see below).
    *   *If Map Rotates (Player-Up):* The **Compass Ring rotates** so "North" always points to the true North of the map.
    *   *If Map Static (North-Up):* The **Compass Ring is fixed** with "North" at the top. The player arrow inside rotates.
*   **Indicators on Ring:**
    *   **Red Arcs:** Incoming fire direction (Audio/Hit).
    *   **Blue Chevrons:** Off-screen teammates.
    *   **Gold Arrow:** Main Objective / Extraction direction.

---

##  Minimap (HUD Radar)

### Core Mechanics
The Minimap is a constant HUD element located at the **Top-Right** (default).

*   **Shape:** Option for **Circle** (Default) or **Square** (Settings).
*   **Orientation Settings:**
    1.  **Option A: Player-Up (Default)**
        *   **Behavior:** The Map rotates. The Player Arrow is fixed pointing UP.
        *   **Compass:** The border ring rotates to show direction.
        *   *Best for:* Tactical navigation and immediate combat awareness.
    2.  **Option B: North-Up (Static)**
        *   **Behavior:** The Map is fixed (North is Up). The Player Arrow rotates.
        *   **Compass:** The border ring is static.
        *   *Best for:* Coordinate communication and map reading experts.

### Visual Indicators

| Indicator          | Icon            | Color           | Behavior                                                                    |
| :----------------- | :-------------- | :-------------- | :-------------------------------------------------------------------------- |
| **Player**         | Arrow           |  Yellow        | Fixed Up (Player-Up) or Rotates (North-Up).                                 |
| **Teammate**       | Circle + Number |  Blue          | Shows directional arrow if off-map on the Compass Ring.                     |
| **Enemy (Visual)** | Solid Dot       |  Red           | Only appears if scanned by UAV/Ability or team LOS (Line of Sight).         |
| **Enemy (Audio)**  | Pulsing Wave    |  Red /  White | Shows *direction* of sound (footsteps/shots). See [Sound Visualization](#). |
| **Gunfire**        | Bullet Icon     |  Red           | Fades after 2s. Size indicates caliber/threat.                              |
| **Extraction**     | Door/Heli       |  Green         | Always visible if active.                                                   |
| **Loot**           | Diamond         |  White         | Only special high-tier loot marked by teammates.                            |

---

##  Tactical Map (BigMap)

### Access & Layout
Accessed by **tapping the Minimap**. Overlays the screen (80% opacity) or slides in.

*   **Orientation:** **ALWAYS North-Up**.
    *   *Why?* To ensure consistent "Grid Callouts" (e.g., "Enemy in B4") regardless of individual player facing.
*   **Grid System:** The map is divided into `A-H` (Horizontal) and `1-8` (Vertical) grids.
*   **Fog of War:** Unexplored areas are *not* hidden, BUT dynamic contents (loot/enemies) are not shown unless revealed by intel. Terrain is always known.

### Interactive Features
1.  **Custom Waypoints:**
    *   **Tap:** Places a personal "Move" marker (White).
    *   **Double Tap:** Places a "Danger" marker (Red).
    *   **Tap Teammate:** Context menu (Follow / Trade).
2.  **Zoom & Pan:** Pinch to zoom, drag to pan.
3.  **Extraction Status:**
    *   Extraction Zones are marked with clear icons.
    *   *Status:* **Open** (Green), **Closed** (Red), **Requires Item** (Yellow Lock icon).
    *   Tap an Extraction Zone to see requirements (e.g., "Needs $3000" or "No Backpack").

### Zone Info Panel
A slide-out panel on the Tactical Map showing:
*   **Raid Timer:** Remaining time.
*   **Radiation/Gas Zone:** Current spread and safe zones.
*   **Active Events:** E.g., "Boss detected in Hotel".

---

##  3D World Markers (AR Pointers)

Markers that exist in the 3D game world to guide players without looking at the map.

### Behavior
*   **On-Screen:** Floating icon clamped to the object's position. Scales down with distance.
*   **Off-Screen:** If a marker is behind the player, the icon clamps to the *edge of the screen* pointing towards the target.
*   **Distance Label:** Always shows distance (e.g., "45m") below the icon.
*   **Fade:** Icons turn transparent (30% opacity) when aiming down sights (ADS) or when directly over the crosshair to prevent visual obstruction.

### Marker Types
1.  **Objective Pointers:** Main Quest / Extraction (Gold/Green).
2.  **Teammate Overhead:** Name + Health Bar + Equipment Icon (e.g., Class).
3.  **Loot Beams:**
    *   *Visual:* Vertical light beam from the ground for high-tier loot (Legendary = Gold, Epic = Purple).
    *   *Only visible within short range or via perks.*

---

##  Ping System (Smart Comms)

A robust "Apex-style" ping system is critical for non-verbal communication.

### 1. Contextual Ping (Single Tap)
Pressing the **Ping Button** performs different actions based on what the crosshair is aiming at:

| Target Object       | Ping Result | Voice Line             | Icon              |
| :------------------ | :---------- | :--------------------- | :---------------- |
| **Terrain / Empty** | "Go Here"   | "Moving to location."  | White Arrow       |
| **Enemy**           | "Hostile"   | "Enemy spotted!"       | Red Diamond       |
| **Loot (Item)**     | "Loot"      | "Level 3 Armor here."  | Item Rarity Color |
| **Open Container**  | "Search"    | "Someone's been here." | Grey Magnifier    |
| **Teammate**        | "Group"     | "On me."               | Blue Flag         |

### 2. Ping Wheel (Hold & Drag)
Holding the Ping Button opens a radial menu for specific commands:
*   ⬆ **Attack / Push** ("Attacking!")
*   ⬇ **Defend / Hold** ("Hold this position.")
*   ⬅ **Watching** ("Watching this angle.")
*    **Looting** ("I'm looting.")
*   ↗ **Enemy Missing** ("Enemy gone?")
*   ↖ **Group Up** ("Regroup here!")

### 3. Danger Ping (Double Tap)
Double-tapping the ping button *immediately* places a high-priority **RED DANGER** marker at the crosshair location with a distinct alert sound ("Enemy contact!").

### 4. Intel Sharing
*   Pings from teammates appear on **both** the HUD (3D Marker) and the Compass/Minimap.
*   Pings last **15 seconds** (Loot/Move) or **5 seconds** (Enemy/Danger).

---

##  Multi-Floor Building Navigation (Top-Down Specific)

Top-down perspective requires unique handling of vertical space. When indoors, the camera cuts away the roof to reveal the layout per [Camera System](../Gameplay/Camera_System.md). Multi-story buildings need additional map affordances.

### Floor Layer System

| Floor | How Player Switches | Camera Behavior | Minimap Behavior |
| :---- | :------------------ | :-------------- | :--------------- |
| Ground (Floor 0) | Starting floor | Standard altitude (18m) | Full floor footprint shown |
| Floor 1 (upper) | Walk up stairs / climb ladder | Altitude lowers to show Floor 1 layout (12m) | Only Floor 1 rooms visible; Floor 0 grayed |
| Floor 2+ | Continue up | Altitude lowers further (8m) | Only current floor visible |
| Basement (below ground) | Descend stairs / hatch | Altitude 6m; roof removed | Basement layout renders; surface grayed |

**Floor indicator:** HUD shows a small floor icon and number (e.g., `[F2]`) in the corner of the minimap. Changes when crossing a floor threshold (staircase reach).

**Invisible floors:** When on Floor 2, Floor 0 and 1 are rendered at 20% opacity (silhouettes) so the player can see through to navigate — but Floor 2 is solid and fully lit.

### Minimap Floor Behavior

- **Minimap always shows current floor only** — switching floors transitions with a 0.3s cross-fade.
- **Staircase icons** (↑↓ arrow) on minimap mark staircase/ladder locations between floors — visible on all floors.
- **Teammate floor indicator**: teammate icon on minimap has a small `↑` or `↓` badge if they are on a different floor than local player.

### Inter-Floor Audio

Being on Floor 2 above a floor-1 firefight:
- **Footsteps:** Heard at −40% normal volume through the floor.
- **Gunfire:** Heard at full volume (not attenuated by floors).
- **Explosions:** Full volume + screen shake regardless of floor.

> Design intent: players above enemies can hear them and prepare — but cannot see through the floor. Information asymmetry creates vertical tactical play.

---

##  Sound Visualization System

Extraction shooters use audio as primary information. For players with sound disabilities, and for mobile players in public spaces, the minimap visualizes sound sources:

### Sound Rings on Minimap

| Sound Event | Minimap Effect | Duration | Range Rule |
| :---------- | :------------- | :------- | :--------- |
| **Enemy footsteps** | Ripple wave ring at sound location | 1.5s fade | Only if within actual hearing range per [Movement & Stamina](../Gameplay/Movement_and_Stamina.md) |
| **Enemy gunfire** | Burst flash icon + direction arc | 3s fade | Audible range per weapon (20–80m) |
| **Explosion** | Large ring (radius = explosion range) | 2s | Always shown if within 120m |
| **Door break/open** | Brief pulse at door location | 1s | Within 15m |
| **Enemy voice/call-out** | Humanoid icon pulse | 2s | Within 25m |
| **Item pickup noise** | Small dot flash | 0.5s | Within 5m |

**Accuracy caveat:** Sound visualization shows *direction and approximate distance* only. It does NOT pinpoint the exact grid position. This maintains the game's intel-over-omniscience principle.

**Mobile accessibility:** Sound rings are enabled by default on mobile. PC/Console: off by default, opt-in in Accessibility settings.

---

##  Extraction Zone Discovery System

Extraction zones are not all visible at raid start. This creates exploration incentive and prevents immediate camping.

### Zone Visibility States

| State | Minimap Display | How Reached |
| :---- | :-------------- | :---------- |
| **Unknown** | Greyed area, no icon | Has never been physically visited this raid |
| **Discovered** | Icon visible, status shown | Player or teammate walked within 30m of zone entrance |
| **Active** | Pulsing green icon | Extraction window open; can attempt extract |
| **Closed** | Red X icon | Extraction window has closed (timed or conditional) |
| **Conditional** | Yellow lock icon | Available but requires item/payment |

**Shared discovery:** When one squad member discovers an extraction zone, it reveals on **all teammates' minimaps** simultaneously.

**Map screen — extraction tab:** Tactical map has a dedicated extraction tab showing all zones, their current state, estimated remaining availability window, and conditions (if any). Zones remain greyed if undiscovered (not shown in tab either — must be physically found).

### Zone Types on Map

| Icon | Type | Notes |
| :--- | :--- | :---- |
|  Door | Standard | Walk-in, hold timer |
|  Helicopter | Vehicle | Must be activated; leaves when full |
|   | Conditional (paid/item) | Lock icon with cost shown on hover |
|  Dual | Cooperative | Two players required per [Extraction Mechanics](../Gameplay/Extraction_Mechanics.md) |
|  Emergency | Expensive | Always available; flare cost shown |

---

##  Top-Down Specific Design Notes

### Why This Map System Differs from FPS Maps

In a first-person game, the player sees the world from the character's eye level. In top-down, the player sees a live aerial view. This creates unique opportunities and constraints:

| Design Question | FPS Solution | Top-Down Solution |
| :-------------- | :----------- | :---------------- |
| "Where am I on the map?" | Minimap as supplement | Minimap matches exactly what player sees in camera |
| "Where is the enemy relative to me?" | Audio + compass arc | Sound visualization rings + camera shows visible enemies directly |
| "Which floor am I on?" | Not a concern (FPS is single-plane mostly) | Floor indicator + minimap floor layers |
| "Is this area safe?" | FPS uses cover and wall lean | Top-down uses overhead camera + LOS blocking |
| "How do I call out a position?" | "At the corner" descriptions | Grid callout system (A4, C7) always North-Up on BigMap |

### Camera-Map Integration

Because the in-game camera IS a top-down view, the minimap is essentially a zoomed-out version of what the player already sees: 

- **Minimap FOV ~80m radius** vs. camera's 26m visible radius — minimap shows further area than camera.
- **Minimap is always lit** (no fog of render distance). Camera is fog-affected.
- **Enemy dots on minimap only appear via LOS or ability scan** — they don't appear just from camera range.

---

##  Cross-References

- [Camera System](../Gameplay/Camera_System.md) — Camera altitude per floor, indoor building handling, and compass offset.
- [LOS, Fog & Visibility](../Gameplay/LOS_Fog_Visibility.md) — Fog of War rules; when enemies appear on minimap; ability LOS reveals.
- [Movement & Stamina](../Gameplay/Movement_and_Stamina.md) — Surface sound ranges; stairs/ladder traversal affecting sound emission.
- [Hero Abilities](../Gameplay/Hero_Abilities.md) — Hawk's motion sensor and drone adding minimap pings; Glitch's tactical overlay.
- [Extraction Mechanics](../Gameplay/Extraction_Mechanics.md) — Extraction zone types, timers, conditional requirements.
- [AI Enemy Behavior](../Gameplay/AI_Enemy_Behavior.md) — AI alert states that trigger audio visualization events.
- [GameDesign/Controls](Controls.md) — Ping button input mapping (single tap, hold, double tap) per platform.




