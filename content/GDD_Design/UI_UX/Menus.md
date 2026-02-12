---
title: "Menus & Screens"
type: docs
---

## ⏸️ Pause Menu

## ⏸️ Pause Menu (System Overlay)

**Context:** Accessed during gameplay by pressing `ESC` (PC) or `Start/Menu` (Console).
**Design Philosophy:**
In an Extraction Shooter, the game **does not pause** (in online raids). The menu acts as an overlay. It must allow the player to maintain **situational awareness** (visuals visible through blur, audio unmuted) while accessing critical system functions.

**Visual Style:**
*   **Background:** Heavy "Frosted Glass" blur (Gaussian Blur radius 15px). De-saturates the game world but keeps motion visible (e.g., if an enemy walks by, you see the shadow/shape).
*   **Layout:**
    *   **Left Column:** Interaction Buttons (Resume, Settings, Leave).
    *   **Right Column:** Raid Status Panel (Timer, Raid ID, Connectivity).
    *   **Center/Bottom:** Contextual Squad Info (optional).
*   **Typography:** *Oxanium* (Headers), *Inter* (Body). High contrast.

![Pause Menu Reference](https://www.gameuidatabase.com/uploads/Alien-Isolation12152020-025857-62996.jpg)
*Figure 1: conceptual reference. Note the "Tech" aesthetic and background visibility. Our design will use a similar layout but with more specific data.*

### Menu Structure

| Section | Elements | Functionality |
| :--- | :--- | :--- |
| **Main Actions** | **Resume** | Closes menu immediately. |
| | **Options** | Opens [Settings Menu](file:///d:/UE_Project/ExtractionDocument/content/GDD_Design/GameDesign/UserSettings.md) (Graphics, Keybinds). |
| | **Statistics** | Shows current session stats (Kills, Damage Dealt, XP gained *so far*). |
| | **Abandon Raid** | **[CRITICAL RED]** Leaves session. Triggers "Confirm Disconnect" popup warning that gear will be lost. |
| **Raid Status** | **Raid Timer** | Countdown content (e.g., `25:43`). Color turns red at <10 mins. |
| | **Extraction Points** | List of available exits (e.g., "Crossroads - Open", "Boat - 30s Wait"). Similar to *Tarkov* 'O' double-tap but persistent here. |
| | **Network Info** | Ping (ms), Packet Loss (%), Raid Hash ID (bottom right). |
| **Squad Info** | **Teammate Cards** | Small widgets showing Squadmate Name, HP Bar, and Status (Alive/Dead/Extracting). *Inspired by Hunt: Showdown.* |

### UX Interaction & Safeguards
*   **"Hold to Abandon":** The "Abandon Raid" button requires a **0.5s hold** to activate, preventing accidental clicks during panic.
*   **Audio Pass-through:** Game audio is **NOT** muted. Footsteps and gunshots remain at 100% volume.
*   **Cursor:** Frees mouse cursor for UI interaction. Camera movement locked.
*   **Input Override:** Pressing `Tab` (Inventory) or `M` (Map) while in this menu immediately switches to those views.
