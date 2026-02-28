---
title: "Loot Table Design"
type: docs
weight: 17
---

## Overview

The loot table system governs what items spawn in the world, at what rarity, and in which containers per map zone. It is the **most direct lever for economic balance** — loot tables set the volume of items flowing into the game each raid, directly affecting prices on the flea market and trader stock. This document specifies container types, zone loot tiers, item category weights, and spawn density rules.

> **Cross-References:** [Looting & Inventory](Looting_Interactions.md) — container interaction mechanic, grid inventory, FIR status; [AI Enemy Behavior](AI_Enemy_Behavior.md) — AI corpse loot; [Environmental Hazards](Environmental_Hazards.md) — supply drop loot, boss loot tables; [Hideout & Crafting](Hideout_Crafting.md) — crafting materials as loot category; [GameDesign/Economy](../../GameDesign/Economy.md) — faucet/sink calibration.

---

## Design Principles

- **Scarcity creates value.** Not every container has useful loot. Empty or low-value containers make high-value finds feel special.
- **Zone reinforces risk-reward.** Higher threat zones (military, laboratories) yield higher-tier loot. Players who push dangerous areas are consistently rewarded.
- **Dynamic density prevents farming.** Spawn density varies per instance — the same container does not always contain the same items. Loot feels discovered, not farmed.
- **AI carry contextual loot.** Scav corpses don't have military items; Sec-Force corpses don't carry civilian goods. Loot makes narrative sense.
- **No guaranteed specific item spawns (except quest items).** Quest item containers have guaranteed spawns for the relevant quest item when the quest is active — otherwise they spawn generic loot.

---

## Container Types

### Physical World Containers

| Container | Size | UI Label | Zones Typically Found In | Loot Category |
| :-------- | :--- | :------- | :----------------------- | :------------ |
| **Wooden Crate** | 3×3 | Crate | All zones | General supplies, ammo, food |
| **Metal Locker** | 3×4 | Locker | Industrial, Military | Weapons, armor, gear |
| **Desk Drawers** | 2×2 | Drawers | Residential, Office | Cash, documents, keys |
| **Filing Cabinet** | 2×3 | Cabinet | Office, Lab | Documents, keycards, intel items |
| **Safe** | 2×2 | Safe | Residential, Office | Cash, jewelry, small valuables |
| **Medical Cabinet** | 2×3 | Med Cabinet | Hospital, Checkpoint | Medical items, stimulants |
| **Ammo Box** | 2×2 | Ammo Box | Military, Checkpoint | Ammo only |
| **Electronics Shelf** | 3×3 | Electronics | Lab, Office | Electronics, GPUs, circuit boards |
| **Tool Cabinet** | 3×3 | Tool Cabinet | Industrial, Workshop | Crafting parts (bolts, wires, pipes) |
| **Refrigerator** | 2×4 | Fridge | Residential, Break Room | Food, water, medical crossover |
| **Boss Stash** | 4×4 | Boss Stash | Boss-exclusive zone | Boss-tier loot, unique items |
| **Supply Drop Crate** | 4×5 | Air Drop | Dynamic event only | Tier 3–4 mixed loot |
| **Vehicle Trunk** | 3×4 | Trunk | Roads, Parking | Fuel, tools, moderate gear |

---

## Map Zones and Loot Tiers

Each map has 4-5 named zones. Zone tier determines which loot tables are used.

### Zone Tier Definitions

| Tier | Description | Zones (Example Map: "Harbortown") | Container Density |
| :--- | :---------- | :-------------------------------- | :---------------- |
| **Tier 1 — Low** | Open areas, civilian streets | Residential District, Outer Docks | 30–40 containers per 10,000 m² |
| **Tier 2 — Medium** | Commercial, industrial | Warehouses, Central Market | 40–55 containers |
| **Tier 3 — High** | Guarded or dangerous areas | Industrial Complex, Checkpoint | 25–35 containers (fewer but better) |
| **Tier 4 — Elite** | Boss zone, locked rooms, labs | Director's Office, The Vault, Lab Block | 10–20 containers (scarce but premium) |

---

## Loot Table — By Zone Tier

### Tier 1 — Residential / Open Areas

| Item Category | Chance (per container) | Typical Items |
| :------------ | :--------------------: | :------------ |
| **Empty** | 25% | Nothing |
| **Food/Water** | 30% | Water bottle, juice, MRE, canned food |
| **Basic Medical** | 15% | Bandage x2, AI-2 medkit |
| **Cash ($)** | 15% | $200–$1,500 |
| **Barter (common)** | 10% | Wires, bolts, cloth, matches |
| **Weapon (Tier 1)** | 3% | Pistol, basic shotgun |
| **Key** | 2% | Common area key |

> **Expected loot value per container (average):** ~$1,200

---

### Tier 2 — Industrial / Commercial

| Item Category | Chance | Typical Items |
| :------------ | :----: | :------------ |
| **Empty** | 15% | Nothing |
| **Crafting Materials** | 25% | Metal pipes, wires, mechanical parts, bolts |
| **Ammo (Tier 1–2)** | 20% | FMJ rounds, buckshot (20–100 rounds) |
| **Weapon (Tier 2)** | 12% | AR, SMG, shotgun (lightly degraded) |
| **Armor (Class 2–3)** | 8% | Soft vest, light helmet |
| **Medical (Standard)** | 8% | IFAK, painkillers |
| **Electronics (common)** | 6% | Wires, circuit board basic |
| **Cash ($)** | 4% | $1,000–$4,000 |
| **Key** | 2% | Industrial key |

> **Expected loot value per container:** ~$4,500

---

### Tier 3 — Military / Checkpoint

| Item Category | Chance | Typical Items |
| :------------ | :----: | :------------ |
| **Empty** | 8% | Nothing |
| **Weapon (Tier 3)** | 18% | Modded AR, DMR, LMG |
| **Ammo (AP/special)** | 20% | Armor-piercing, hollow-point (50–100 rounds) |
| **Armor (Class 3–4)** | 14% | Plate carrier, military helmet |
| **Medical (Advanced)** | 12% | Grizzly kit, IFAK, stims |
| **Electronics** | 10% | Circuit boards, GPUs (5% chance) |
| **Crafting (Military)** | 8% | Spark plugs, bearings, precision parts |
| **Cash ($)** | 6% | $3,000–$10,000 |
| **Keycard (common)** | 3% | Bronze/Silver keycard |
| **Intel Item** | 1% | Encrypted drive, military documents |

> **Expected loot value per container:** ~$12,000

---

### Tier 4 — Elite (Vault / Lab / Boss Zone)

| Item Category | Chance | Typical Items |
| :------------ | :----: | :------------ |
| **Empty** | 5% | Nothing |
| **Weapon (Tier 4)** | 15% | Rare sniper, LMG, fully-modded AR |
| **Armor (Class 5–6)** | 10% | Heavy plate carrier, ballistic helmet |
| **GPU** | 20% | GPU ×1–3 (Bitcoin Farm fuel) |
| **Rare Electronics** | 15% | Server blade, rare circuit board, processor |
| **Stimulants** | 10% | Adrenaline, Propital, SJ6 |
| **Cash ($)** | 10% | $8,000–$25,000 |
| **Keycard (rare)** | 8% | Gold keycard, Lab card |
| **Unique Quest Item** | 5% | Intel artifact, boss key, mission files |
| **Weapon Blueprint** | 2% | Hideout crafting recipe (unique) |

> **Expected loot value per container:** ~$40,000

---

## AI Corpse Loot Tables

### By Enemy Tier

| Enemy Type | Weapon (kept on body) | Armor (degraded) | Special Loot |
| :--------- | :-------------------- | :--------------- | :----------- |
| **Scav (Tier 1)** | Tier 1 weapon (50–70% durability) | Class 0–2 (30–60%) | Food ×1, $200–$600, occasional key |
| **Militia Raider (Tier 2)** | Tier 2 weapon (50–80%) | Class 2–3 (40–70%) | Ammo ×20–50, $500–$2,000, rig (15% chance) |
| **Sec-Force (Tier 3)** | Tier 3 weapon (60–90%) | Class 3–4 (50–80%) | AP ammo ×30–80, $1,500–$5,000, keycard (10% chance) |
| **Rogue PMC (Tier 4)** | Tier 4 weapon (70–95%) | Class 4–5 (60–90%) | Stim ×1–2, $3,000–$10,000, rare item (20% chance) |

> AI gear condition varies because AI takes damage during combat. Condition is randomized within the range above at AI spawn, and further reduced by any hits they actually take during the raid.

---

## Boss Loot Tables

| Boss | Guaranteed | Random Drop (50% each) | Unique Drop (15%) |
| :--- | :--------- | :--------------------- | :---------------- |
| **Kommandant** | Tier 4 weapon, Class 5 armor, Vault Room keycard | Stim ×2, $15,000–$30,000, blueprint | "Kommandant's Sidearm" unique pistol |
| **Wraith** | Suppressed Tier 3–4 weapon, Intel item | Light rig, $10,000–$20,000 | "Wraith's Cloak Module" — unique gadget component |
| **Iron Wall** | LMG (Tier 4), Military keycard | Class 5 armor (heavy), $20,000–$40,000 | "Iron Wall's Core" — quest-chain-only barter item |

---

## Dynamic Loot Events

### Supply Drop

| Property | Value |
| :------- | :---- |
| **Trigger** | Dynamic event per [Environmental Hazards](Environmental_Hazards.md) |
| **Container** | One 4×5 Super Crate |
| **Loot table** | Tier 3 only — guaranteed at least 1 Tier 4 item, 3–5 Tier 3 items, $10,000–$20,000 |
| **AI guard** | 4 Militia Raiders spawn at crate on landing |
| **Contested time** | Crate accessible 90s after landing (AI spawn delay); becomes permanently lootable |

### Quest Container

| Property | Value |
| :------- | :---- |
| **Spawn condition** | Spawns only for specific players with active quest |
| **Server instancing** | Different players on same server see different quest item spawns |
| **If looted by enemy** | Item still counts as "found" — but enemy can extract it, denying the quest item to original player |
| **Fallback** | Quest item respawns in new location after 5 minutes if not yet taken |

---

## Spawn Density Rules

### Per-Instance Variation

To prevent farming predictability, each server instance shuffles loot:

| Rule | Detail |
| :--- | :----- |
| **60% fill rate** | On average, 60% of containers in a zone have loot. 40% are empty. |
| **±15% randomization** | Each instance rolls ±15% density deviation (45–75% containers filled). |
| **Hot zone boost** | If fewer than 8 players remain alive at raid mid-point, loot density increases +10% for remaining players (survival reward). |
| **Player proximity reset** | A container that was looted by Player A will appear empty to Player B — no ghost-items remain in containers. |
| **Key-gated rooms** | Always 100% container fill rate behind locked doors (rewarding key investment). |

### Loot Balance Target

| Zone Tier | Target average loot value per player per raid | Basis |
| :-------- | :-------------------------------------------: | :---- |
| Tier 1 zones only | $8,000–12,000 | Rat-playstyle baseline |
| Tier 2 + some Tier 3 | $20,000–40,000 | Standard run |
| Tier 3 + Tier 4 | $50,000–120,000 | High-risk play |
| Full Chad run (all Tier 4) | $80,000–200,000 | Peak; requires surviving boss fights |

---

## Seasonal & Event Loot Modifiers

| Event | Effect | Duration |
| :---- | :----- | :------- |
| **Double Loot Weekend** | Container fill rate +25%; item quality tier +1 | 48h live-op |
| **Scarcity Week** | Container fill rate −30%; prices rise on flea market | 7 days |
| **Contamination Event** | New hazardous item category spawns: Contamination Samples (quest-only) | Live-op |
| **Faction War** | Specific AI faction loot table enriched (±30% of faction-specific items) | 7 days |

---

## Cross-References

- [Looting & Inventory](Looting_Interactions.md) — Container interaction, FIR status, grid inventory.
- [AI Enemy Behavior](AI_Enemy_Behavior.md) — AI corpse loot tables; boss loot.
- [Environmental Hazards](Environmental_Hazards.md) — Supply drop event and Scav Raid wave loot.
- [Quest & Objective System](Quest_Objective_System.md) — Quest items and their container spawn rules.
- [Hideout & Crafting](Hideout_Crafting.md) — Crafting materials as primary Tier 2 loot category.
- [GameDesign/Economy](../../GameDesign/Economy.md) — Macro economy calibration; loot as primary faucet.
