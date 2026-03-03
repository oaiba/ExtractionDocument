---
title: "Game Modes Design"
type: docs
---

## 🎮 Core Philosophy

Our game modes are designed to cater to different player intensities and time commitments, all revolving around the core loop: **Deploy → Loot → Extract**.

**Design Pillars:**
1.  **High Stakes:** Gear fear is real. Death has consequences.
2.  **Variability:** No two raids feel the same (Dynamic weather, spawn points).
3.  **Progression:** Every mode feeds into the main progression (Safe House/Trader).

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
*   **Cooldown:** 20 Minutes (Reducible with Safe House upgrades).

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

## 🎛️ Mode Selection Screen Design

The Mode Selection UI is embedded in the [Loadout Preparation Screen](LoadoutPreparation.md) — players select their mode as part of the pre-raid ritual, not as a separate lobby screen.

### Mode Summary Cards

Each mode is represented as a **pill-style button** in the loadout prep screen. When selected, a **mode detail card** expands below showing:

| Card Element | Description |
| :----------- | :---------- |
| **Mode Name & Icon** | Bold name + distinctive icon (⚔ Raid, ⚡ Blitz, 👻 Scav, ♦ Ranked, 🛡 Co-op) |
| **Map thumbnail** | Top-down miniature of the currently selected map |
| **Duration range** | e.g., "15–30 min" / "8 min" |
| **Player count** | e.g., "8–16 Players" / "3 Players max" |
| **Risk badge** | ⚠ HIGH / ⚡ MEDIUM / ✅ ZERO / ♦ EXTREME / 🛡 MEDIUM |
| **Queue estimate** | Live-updated estimated wait time from matchmaking |
| **Special rules** | Any mode-specific rule deviations (e.g., "No insurance in Ranked") |

### Mode Pill Row

```
[● THE RAID ⚔]  [ BLITZ ⚡]  [ SCAV RUN 👻]  [ RANKED ♦]  [ CO-OP 🛡]  [ FEATURED ★]
```

- Only one mode active at a time (radio select)
- Unavailable modes (level-locked) shown greyed with lock icon + unlock tooltip
- "Featured ★" pill only visible during active LiveOps events

### Mode Quick Reference Table

| Mode | Type | Duration | Players | Risk | Insurance | Unlocked At |
| :--- | :--- | :------- | :------ | :--- | :-------- | :---------- |
| **The Raid** | PvPvE | 15–30 min | 8–16 | ⚠ High | ✅ Yes | Level 1 |
| **Blitz** | PvPvE | 8 min | 6–10 | ⚡ Medium | ✅ Yes | Level 1 |
| **Scav Run** | PvPvE (Scav) | 10–20 min | joins live raid | ✅ Zero | ❌ N/A | Level 1 |
| **Ranked Ops** | PvPvE Competitive | 15–20 min | 8–12 | ♦ Extreme | ❌ **No** | Level 15, 20+ matches |
| **Blackout (Co-op)** | PvE | 15 min | 1–3 | 🛡 Medium | ✅ Yes | Level 5 |
| **Training Grounds** | PvE Only | No limit | Solo | ✅ Zero | ❌ N/A | Level 1 |
| **Featured ★** | Varies | Varies | Varies | Varies | Varies | Event active |

### Queue Size Selector (within Mode Card)

Below the mode card, players select squad configuration:

```
SQUAD:  ○ Solo    ○ Duo    ● Trio    [ ] Auto-fill (LFG)
Estimated wait: ~40 seconds
```

- **Duo and Trio** require squad slots filled (or Auto-fill enabled)
- **Scav Run** does not show squad selector — Scavs always deploy solo into live raids
- **Training Grounds** always Solo, selector hidden

---

## 📊 Cross-References

- [Loadout Preparation](LoadoutPreparation.md) — Mode selection UI embedded in prep screen; full wireframe and interaction design.
- [Map Design](MapDesign.md) — Map zone rules and how weather/loot bias varies by map; affects mode card info shown.
- [Ranked Mode](RankedMode.md) — Full Ranked Ops RP system, season structure, rank tiers, and competitive integrity rules.
- [Live Ops](LiveOps.md) — Dynamic Events and Featured modes defined here; Limited-Time Mode design and rotation schedule.
- [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — Queue parameters, SBMM, team formation rules per mode.
- [Insurance System](InsuranceSystem.md) — Ranked Ops disables insurance; Scav Run has no insurance; all other modes support it.




