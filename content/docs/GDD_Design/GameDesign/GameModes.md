# Game Modes Design

**[← Back to Index](../README.md)** | **[Next: Audio Design →](../Audio/SoundDesign.md)**

---

## 🎮 Core Philosophy

Our game modes are designed to cater to different player intensities and time commitments, all revolving around the core loop: **Deploy → Loot → Extract**.

**Design Pillars:**
1.  **High Stakes:** Gear fear is real. Death has consequences.
2.  **Variability:** No two raids feel the same (Dynamic weather, spawn points).
3.  **Progression:** Every mode feeds into the main progression (Hideout/Trader).

---

## 🎲 1. The Raid (Core Experience)

The primary "Extraction Shooter" mode. This is the heart of the game.

*   **Player Count:** 8-16 Players (Map dependent).
*   **Team Size:** Solo, Duo, Trio (Separate matchmaking queues).
*   **Duration:** 15-30 Minutes.
*   **Goal:** Scavenge loot, complete quests, and extract alive.
*   **Consequence:** Death = Loss of all carried gear (except Secure Container).

**Match Flow:**
1.  **Deployment:** Random spawn at map edge.
2.  **Phase 1 (Scouting):** Players move inward, AI Scavs are passive.
3.  **Phase 2 (Conflict):** High-tier loot zones contested. Boss spawns.
4.  **Phase 3 (Extraction):** Timer counts down. Exits open/close. Player Scavs spawn.
5.  **Overtime:** Radiation/Gas pushes everyone to final exits.

---

## 👻 2. Scavenger Run ("Scav Mode")

A risk-free mode to recover from losses or learn maps.

*   **Character:** Random loadout (low-tier gear). Stats do not progress.
*   **AI Relationship:** Friendly to AI (unless you shoot first). 
*   **Goal:** Loot "leftovers" from a live PMC raid and extract.
*   **Risk:** Zero. Death costs nothing.
*   **Reward:** You keep everything you extract with.
*   **Cooldown:** 20 Minutes (Reducible with Hideout upgrades).

**Design Purpose:** 
*   Prevents "bankruptcy" (players losing everything).
*   Adds unpredictable human elements to the end of PMC raids.

---

## ⚔️ 3. Ranked Operations (Competitive)

A high-stakes version of The Raid for veteran players.

*   **Entry Fee:** High (In-game currency or Keycards).
*   **Modifiers:**
    *   No Insurance (Gear is lost forever).
    *   No HUD (Hardcore UI).
    *   Friendly Fire ON.
    *   Better Loot tables (S-Tier guaranteed).
*   **Ranking:** Elo-based matchmaking. See [Ranked System](../Technical/Systems/RankedSystem.md).

---

## ⚡ 4. Blitz (Quick Play)

A faster, condensed experience for mobile play sessions.

*   **Map:** Small sections of main maps (e.g., just "The Factory" interior).
*   **Duration:** 8 Minutes.
*   **Loot:** Focused on PvP gear and Consumables (No quest items).
*   **Extraction:** Only 1 Exit opens at the end. King of the Hill style.

---

## 🛡️ PvE / Co-op Modes

### "Blackout" (Horde Mode)
*   **Premise:** Defend a fortified position against waves of infected/AI.
*   **Goal:** Hold out until the extraction heli arrives.
*   **Reward:** XP and Crafting Materials (No weapons/armor).

### "Training Grounds" (Solo PvE)
*   **Premise:** Offline raid against AI.
*   **Risk/Reward:** Zero. No gear lost, no loot kept. Purely for practice.

---

## 🔄 Dynamic Events (Live Ops)

Special limited-time modes that mutate the core rules.

| Event Name      | Modifier        | Description                                         |
| :-------------- | :-------------- | :-------------------------------------------------- |
| **Nightmare**   | Permanent Night | Flashlights required. Cultist AI enemies spawn.     |
| **Golden Rush** | 500% Cash Loot  | Everyone spawns with pistols only. Loot cash & run. |
| **No Fly Zone** | No Air Drops    | Extractions are ground-only. Snipers dominate.      |

---

**[← Back to Index](../README.md)** | **[Next: Audio Design →](../Audio/SoundDesign.md)**
