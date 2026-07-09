---
title: "Faction Behaviors & Ecology"
type: docs
---

## The Faction Ecosystem

Aethelgard is not just người chơi vs. AI. It is a living world where factions have their own goals, territories, và relationships.

### Faction matrix (Who fights whom?)

| Faction | người chơi | Scavengers | Syndicate | UN-Peacekeepers | Wildlife |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **người chơi (PMC)** | **KILL** | **KILL** | **KILL** | Wariness (Neutral until provoked) | **KILL** |
| **Scavengers** | **KILL** | *Friendly* | *Avoid* (Fear) | **KILL** | **KILL** |
| **Syndicate** | **KILL** | *Exploit* (Bully) | *Friendly* | **KILL** | **KILL** |
| **UN-PK** | Wariness | **KILL** | **KILL** | *Friendly* | **KILL** |
| **Wildlife** | **HUNT** | **HUNT** | **HUNT** | **HUNT** | *Territorial* |

---

## 1. Scavengers ( The "Rats" )

**Archetype:** Desperate survivors, poorly equipped, chaotic.
**mục tiêu:** Scavenge food/meds, survive, protect their trash piles.

### Behavior Profile
*   **Patrol:** Random wandering in small groups (2-3). They check containers, sit by fires, smoke.
*   **Combat Style:**
    *   **"Spray và Pray":** Low accuracy, high volume of fire.
    *   **Cowardice:** nếu a leader dies, 50% chance to flee hoặc hide.
    *   **Voice Lines:** Constant chatter ("Cheeki Breeki", cursing). Reveals their position easily.
*   **Loot Tier:** Low (Broken AKs, Bandages, Food).
*   **Unique Trait:** *The Swarm.* nếu one Scav yells for giúp, all Scavs in a 50m radius will converge on the location aggressively.

---

## 2. The Syndicate ( The "Elites" )

**Archetype:** High-tech mercenaries, disciplined, lethal.
**mục tiêu:** Secure high-giá trị assets, guard chính locations (Labs, Server Rooms).

### Behavior Profile
*   **Patrol:** Strict routes. They hold angles và cover entrances. They do not wander.
*   **Combat Style:**
    *   **"Suppress và Flank":** One lays down fire (LMG), two push the sides (SMG/Shotgun).
    *   **Tactical:** cách dùng grenades to flush người chơi out. cách dùng smoke to cover movement.
    *   **Voice Lines:** Professional, concise callouts ("Contact Front", "Flanking Left"). Encrypted chatter.
*   **Loot Tier:** High (Modded M4s, Class 4-5 giáp, Keycards).
*   **Unique Trait:** *Hunt Mode.* nếu they spot a người chơi, they will actively pursue them across the map block (Zone Pursuit), not just within line of sight.

---

## 3. UN Peacekeepers ( The "Law" )

**Archetype:** Heavily armored, defensive, strictly Rules of Engagement (ROE).
**mục tiêu:** Maintain order at Checkpoints và Extraction Zones.

### Behavior Profile
*   **trạng thái:** *Defensive Neutrality.* They will warn người chơi trước shooting ("Drop the vũ khí!", "Back away!").
*   **Combat Style:**
    *   **"Walls of Lead":** They do not push. They hold ground với overwhelming firepower (Mounted MGs, Snipers).
    *   **Accuracy:** Extremely High (Aimbot-like logic to punish aggression).
*   **Loot Tier:** Unobtainable (Scripts prevent looting their heavy gear usually, hoặc it's damaged).
*   **Unique Trait:** *Karma hệ thống.* Killing Peacekeepers marks the người chơi as a "Rogue Agent" for 3 raids, making all AI (even Scavs) hunt them instantly.

---

## 4. Wildlife / Mutants ( The "Environment" )

**Archetype:** Instinctive predators.
**mục tiêu:** Defense of territory, hunger.

### Behavior Profile
*   **trạng thái:** Ambient until triggered.
*   **Combat Style:**
    *   **"Ambush":** Hide in bushes/vents. Rush the người chơi khi backs are turned.
    *   **Melee Only:** High damage, causes *Bleed* status effect.
*   **Unique Trait:** *Fear of Fire.* Flares và torches will keep them at bay (radius 5m).

---

## Dynamic Events (The "Living World")

1.  **Faction War:**
    *   *Trigger:* A Scav patrol meets a Syndicate team.
    *   *kết quả:* A firefight erupts. Người chơi có thể wait và loot the winners, hoặc 3rd-party the fight.
2.  **Boss Arrival:**
    *   *Trigger:* 15 minutes into the raid.
    *   *kết quả:* "The Butcher" (Scav Boss) arrives với guards. Scavs become 2x more aggressive.
3.  **Extraction Denial:**
    *   *Trigger:* Peacekeepers lock down an extraction zone due to "contamination".
    *   *kết quả:* người chơi must find another way out hoặc fight thông qua the blockade.
