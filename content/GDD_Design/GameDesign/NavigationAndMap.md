---
title: "Navigation & Map System Design"
type: docs
---
# Navigation & Map System Design

**[← Back to Index](../README.md)** | **[Next: Controls & Combat →](./Controls.md)**

---

## 🧭 System Overview

The **Navigation & Map System** is the player's primary tool for situational awareness in the Extraction zone. Unlike traditional shooters where red dots reveal enemies, Extraction Shooters rely on **Intel-based Navigation**. The system prioritizes sound, line-of-sight, and tactical markings over "god-mode" radar.

**Key Design Pillars:**
1.  **Intel over Omniscience:** The map shows *known* info, not *all* info.
2.  **Communication Focus:** Pings and Markers replace voice chat for rapid tactical coordination.
3.  **Diegetic Integration:** UI elements should feel like tactical augmented reality (AR) gear.
4.  **Audio-Visual Synergy:** Visualizing sound (footsteps/gunfire) for mobile accessibility.

---

## 🧭 HUD Compass Ring

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

## 🗺️ Minimap (HUD Radar)

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
| **Player**         | Arrow           | 🟡 Yellow        | Fixed Up (Player-Up) or Rotates (North-Up).                                 |
| **Teammate**       | Circle + Number | 🔵 Blue          | Shows directional arrow if off-map on the Compass Ring.                     |
| **Enemy (Visual)** | Solid Dot       | 🔴 Red           | Only appears if scanned by UAV/Ability or team LOS (Line of Sight).         |
| **Enemy (Audio)**  | Pulsing Wave    | 🔴 Red / ⚪ White | Shows *direction* of sound (footsteps/shots). See [Sound Visualization](#). |
| **Gunfire**        | Bullet Icon     | 🔴 Red           | Fades after 2s. Size indicates caliber/threat.                              |
| **Extraction**     | Door/Heli       | 🟢 Green         | Always visible if active.                                                   |
| **Loot**           | Diamond         | ⚪ White         | Only special high-tier loot marked by teammates.                            |

---

## 📍 Tactical Map (BigMap)

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

## 🎯 3D World Markers (AR Pointers)

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

## 📢 Ping System (Smart Comms)

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
*   ⬆️ **Attack / Push** ("Attacking!")
*   ⬇️ **Defend / Hold** ("Hold this position.")
*   ⬅️ **Watching** ("Watching this angle.")
*   ➡️ **Looting** ("I'm looting.")
*   ↗️ **Enemy Missing** ("Enemy gone?")
*   ↖️ **Group Up** ("Regroup here!")

### 3. Danger Ping (Double Tap)
Double-tapping the ping button *immediately* places a high-priority **RED DANGER** marker at the crosshair location with a distinct alert sound ("Enemy contact!").

### 4. Intel Sharing
*   Pings from teammates appear on **both** the HUD (3D Marker) and the Compass/Minimap.
*   Pings last **15 seconds** (Loot/Move) or **5 seconds** (Enemy/Danger).

---

## 🧭 Compass Ring (Top-Down Optimized)

---

## 🚧 Implementation & Tech Constraints

### Network Optimization
*   **Minimap Updates:** Player positions update @ 10Hz. Enemy sound markers update @ 20Hz (priority).
*   **Fog of War:** Calculated client-side based on server-sent visibility radius to save bandwidth.

### Performance (Mobile)
*   **3D Markers:** Use **Screen Space UI** (not World Space Canvas) where possible for batching.
*   **Occlusion:** Markers for loot deep within buildings should handle occlusion intelligently (e.g., show "Through Wall" icon style).

---

## 🔍 Reference Inspirations
*   **Apex Legends:** Contextual Ping system and Ping Wheel.
*   **Arena Breakout / Lost Light:** Sound visualization on Minimap (footstep waves).
*   **Call of Duty Mobile:** Map grid system and footprint indicators.
*   **The Division:** 3D AR lines floating in the world (for pathfinding integration).

---

**[← Back to Index](../README.md)** | **[Next: Controls & Combat →](./Controls.md)**


