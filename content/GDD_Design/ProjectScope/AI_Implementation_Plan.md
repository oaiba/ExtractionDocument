---
title: "AI Agent Implementation Plan & Research Gaps"
type: docs
---

# 🤖 Agent Directives: Project Expansion Plan

**Status:** Active
**Last Updated:** 2026-02-11
**Objective:** This document serves as a "Job Board" for AI Agents to systematically flesh out the Game Design Document.

All Agents working on this project must consult this file to identify high-priority research and content generation tasks.

---

## 🏗️ Priority 1: Core Combat & Systems (Immediate)

### 1.1 Ballistics & Armor Data
**Target File:** `content/GDD_Design/Combat/Ballistics_Master_Table.md`
**Status:** ✅ Complete
**Directives for Agent:**
*   **Research:** Analyze Tarkov and Gray Zone calibers (5.56x45, 7.62x39, 9x19, etc.).
*   **Create:** A Markdown table defining:
    *   Ammo Name (e.g., M855, AP 6.3)
    *   Damage vs Flesh
    *   Penetration Value (Tier 1-6)
    *   Armor Damage %
    *   Velocity & Frag Chance

### 1.2 Medical System Specifics
**Target File:** `content/GDD_Design/Gameplay/Medical_System.md`
**Status:** ✅ Complete
**Directives for Agent:**
*   **Task:** Define specific items and their mechanical effects.
*   **Fill Data:**
    *   **Light Bleed:** Bandage (2s cast), Army Bandage (1s cast).
    *   **Heavy Bleed:** Esmarch Tourniquet (5s), CAT (3s).
    *   **Fracture:** Splint (Alu vs Grizzly).
    *   **Pain:** Analgesics (Ibuprofen, Vaseline) - define duration & hydration costs.

### 1.3 Weapon Master List (Alpha)
**Target File:** `content/GDD_Design/Weapons/Alpha_Weapon_List.md`
**Status:** ✅ Complete
**Directives for Agent:**
*   **Task:** Detail statistics for the 5 Alpha weapons (AK-47, M4A1, MP5, Glock 17, M870).
*   **Define:** vertical_recoil, horizontal_recoil, ergo, fire_rate, effective_range, mod_slots_available.

---

## 🗺️ Priority 2: World & Map Design

### 2.1 "Industrial Zone" POI Detail
**Target File:** `content/GDD_Design/Maps/Industrial_Zone_Design.md`
**Status:** ✅ Complete
**Directives for Agent:**
*   **Task:** Flesh out the "Industrial Zone" map.
*   **Create Sections:**
    *   **Points of Interest (POIs):** (e.g., The Crackhouse, Train Depot, Silo 4).
    *   **Loot Tiering:** High Value (Safe Room) vs Low Value (Civilian Housing).
    *   **Choke Points:** Where players are forced to fight.
    *   **Extraction Logic:** Specific conditions for the 3 Extracts (e.g., "Must carry Paracord", "Pay 3000 Credits").

### 2.2 Key & Door System
**Target File:** `content/GDD_Design/Maps/Key_Registry.md`
**Status:** ⭕ To Be Created
**Directives for Agent:**
*   **Task:** Create a list of keys for the Industrial Zone.
*   **Define:** Key Name, Spawn Location (approx), Room Loot Value, Durability (1/1 to 25/25).

---

## 💰 Priority 3: Economy & Progression

### 3.1 Loot Tables (Distribution)
**Target File:** `content/GDD_Design/Economy/Loot_Distribution.md`
**Status:** ⭕ To Be Created
**Directives for Agent:**
*   **Task:** Categorize loot items.
*   **Categories:**
    *   **Barter Items:** Bolts, Screw Nuts, Duct Tape (Used for crafting/trading).
    *   **Info Intel:** SSDs, Folders, Diaries (High value to traders).
    *   **Provisions:** Tushonka, Water, Milk.
    *   **Valuables:** Bitcoins, Golden Chains, Rolexes (Rare spawns).

### 3.2 Trader Assortment (Tier 1)
**Target File:** `content/GDD_Design/Economy/Traders/The_Fixer.md`
**Status:** ⭕ To Be Created
**Directives for Agent:**
*   **Task:** Define the inventory for the starting trader "The Fixer".
*   **Define:**
    *   Items for Sale (Level 1).
    *   Barter Trades (e.g., 2x Duct Tape -> 1x IFAK).
    *   Buy Orders (What he pays best price for).

---

## 🧠 Priority 4: AI & NPC Logic

### 4.1 Scavenger Behavior Tree
**Target File:** `content/GDD_Design/AI/Scav_Behavior_Patterns.md`
**Status:** ⭕ To Be Created
**Directives for Agent:**
*   **Research:** Utility AI vs Behavior Trees for Extraction Shooters.
*   **Define States:**
    *   **Idle/Patrol:** Route randomization.
    *   **Suspicion:** Hearing a noise -> "Mumbling" -> Investigating.
    *   **Combat:** Cover usage, suppressing fire, "Cheeki Breeki" voice lines.

---

## 📂 Implementation Protocol for Agents

1.  **Read this file first.**
2.  **Pick a Priority Task.**
3.  **Search/Research** the topic (e.g., "Tarkov medical animation times").
4.  **Create/Edit** the target file using the path provided.
5.  **Mark Status** in this file as `✅ Complete` when done.
