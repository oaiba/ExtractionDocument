---
title: "Faction Behaviors & Ecology"
type: docs
---

##  The Faction Ecosystem

Aethelgard is not just Player vs. AI. It is a living world where factions have their own goals, territories, and relationships.

### Faction Matrix (Who fights whom?)

| Faction | Player | Scavengers | Syndicate | UN-Peacekeepers | Wildlife |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Player (PMC)** | **KILL** | **KILL** | **KILL** | Wariness (Neutral until provoked) | **KILL** |
| **Scavengers** | **KILL** | *Friendly* | *Avoid* (Fear) | **KILL** | **KILL** |
| **Syndicate** | **KILL** | *Exploit* (Bully) | *Friendly* | **KILL** | **KILL** |
| **UN-PK** | Wariness | **KILL** | **KILL** | *Friendly* | **KILL** |
| **Wildlife** | **HUNT** | **HUNT** | **HUNT** | **HUNT** | *Territorial* |

---

##  1. Scavengers ( The "Rats" )

**Archetype:** Desperate survivors, poorly equipped, chaotic.
**Goal:** Scavenge food/meds, survive, protect their trash piles.

### Behavior Profile
*   **Patrol:** Random wandering in small groups (2-3). They check containers, sit by fires, smoke.
*   **Combat Style:**
    *   **"Spray and Pray":** Low accuracy, high volume of fire.
    *   **Cowardice:** If a leader dies, 50% chance to flee or hide.
    *   **Voice Lines:** Constant chatter ("Cheeki Breeki", cursing). Reveals their position easily.
*   **Loot Tier:** Low (Broken AKs, Bandages, Food).
*   **Unique Trait:** *The Swarm.* If one Scav yells for help, all Scavs in a 50m radius will converge on the location aggressively.

---

##  2. The Syndicate ( The "Elites" )

**Archetype:** High-tech mercenaries, disciplined, lethal.
**Goal:** Secure high-value assets, guard key locations (Labs, Server Rooms).

### Behavior Profile
*   **Patrol:** Strict routes. They hold angles and cover entrances. They do not wander.
*   **Combat Style:**
    *   **"Suppress and Flank":** One lays down fire (LMG), two push the sides (SMG/Shotgun).
    *   **Tactical:** Use grenades to flush players out. Use smoke to cover movement.
    *   **Voice Lines:** Professional, concise callouts ("Contact Front", "Flanking Left"). Encrypted chatter.
*   **Loot Tier:** High (Modded M4s, Class 4-5 Armor, Keycards).
*   **Unique Trait:** *Hunt Mode.* If they spot a player, they will actively pursue them across the map block (Zone Pursuit), not just within line of sight.

---

##  3. UN Peacekeepers ( The "Law" )

**Archetype:** Heavily armored, defensive, strictly Rules of Engagement (ROE).
**Goal:** Maintain order at Checkpoints and Extraction Zones.

### Behavior Profile
*   **State:** *Defensive Neutrality.* They will warn players before shooting ("Drop the weapon!", "Back away!").
*   **Combat Style:**
    *   **"Walls of Lead":** They do not push. They hold ground with overwhelming firepower (Mounted MGs, Snipers).
    *   **Accuracy:** Extremely High (Aimbot-like logic to punish aggression).
*   **Loot Tier:** Unobtainable (Scripts prevent looting their heavy gear usually, or it's damaged).
*   **Unique Trait:** *Karma System.* Killing Peacekeepers marks the player as a "Rogue Agent" for 3 raids, making all AI (even Scavs) hunt them instantly.

---

##  4. Wildlife / Mutants ( The "Environment" )

**Archetype:** Instinctive predators.
**Goal:** Defense of territory, hunger.

### Behavior Profile
*   **State:** Ambient until triggered.
*   **Combat Style:**
    *   **"Ambush":** Hide in bushes/vents. Rush the player when backs are turned.
    *   **Melee Only:** High damage, causes *Bleed* status effect.
*   **Unique Trait:** *Fear of Fire.* Flares and torches will keep them at bay (radius 5m).

---

##  Dynamic Events (The "Living World")

1.  **Faction War:**
    *   *Trigger:* A Scav patrol meets a Syndicate team.
    *   *Result:* A firefight erupts. Players can wait and loot the winners, or 3rd-party the fight.
2.  **Boss Arrival:**
    *   *Trigger:* 15 minutes into the raid.
    *   *Result:* "The Butcher" (Scav Boss) arrives with guards. Scavs become 2x more aggressive.
3.  **Extraction Denial:**
    *   *Trigger:* Peacekeepers lock down an extraction zone due to "contamination".
    *   *Result:* Players must find another way out or fight through the blockade.


