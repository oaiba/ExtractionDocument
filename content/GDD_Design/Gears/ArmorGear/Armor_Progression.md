---
title: "Armor Progression"
type: docs
weight: 5
---

## Overview

This document covers **trader unlock gating**, **Safe House repair bench progression**, **armor crafting**, and **Found-in-Raid (FIR) armor** rules. For item list see [Armor Master Database](Armor_Master_Database.md); for balance see [Armor Balance Framework](Armor_Balance_Framework.md).

---

## Trader Unlock Gating

Armor tier (per [Gear Tier System](../Gear_Tier_System.md)) is gated by trader level, quests, and player level so that early game is not dominated by top-tier armor.

| Armor tier | Trader level required | Quest gate | Level gate |
| :--------- | :-------------------: | :--------- | :--------: |
| Class 1–2 | Trader Lvl 1 | None | 1 |
| Class 3 | Trader Lvl 2 | e.g. "Proving Ground" | 10 |
| Class 4 | Trader Lvl 3 | e.g. "Armored Up" | 20 |
| Class 5 | Trader Lvl 4 | e.g. "Forged in Fire" | 35 |
| Class 6 | Trader Lvl 4 (Exalted) | e.g. Boss kill / endgame quest | 45 |

Exact quest names and level numbers are placeholders; adjust to match [Progression](../../GameDesign/Progression.md) and quest design.

---

## Safe House Repair Bench Progression

Repair bench level determines which armor classes and materials can be repaired in-raid or in Safe House, and repair efficiency.

| Bench level | Repairable class | Repairable materials | Notes |
| :---------- | :--------------- | :------------------- | :---- |
| 1 | Class 1–3 | Aramid, Steel | Basic repairs only |
| 2 | Class 1–4 | All materials | Full material set |
| 3 | Class 1–6 | All materials | Reduced repair max loss (−2% per repair) |

Trader repair remains available for all classes and materials but uses standard material repair loss; Safe House Lvl 3 bench is the best long-term option for high-tier armor.

---

## Armor Crafting (Safe House)

Selected armor pieces can be crafted at the Safe House. Recipes consume materials and time; output is one armor item at fixed durability (e.g. 80–100%).

**Example recipes (placeholder):**

- **Class 3 vest:** 5× Polymer + 3× Rare Components + 2 h → 1× Ceramic Carrier (80% durability).
- **Class 2 vest:** 3× Aramid + 2× Scrap Metal + 30 min → 1× Press Vest (90% durability).

Crafting provides an alternative to trader purchase and FIR loot, and consumes barter/crafting materials. Full recipe list should live in [Safe House Design](../../GameDesign/Safe_House_Design.md) with references here.

---

## Found-in-Raid (FIR) Armor

- **FIR armor** spawns in-raid with **durability in a range** (e.g. 60–100% of max). This avoids “free” full-durability top-tier armor from loot only.
- FIR armor is often the **only way** to obtain certain rare or high-class pieces before unlocking the corresponding trader level or quest.
- FIR status is lost if the item is brought into raid by the player (e.g. re-equipped). Marketplace and FIR rules: see [Looting & Inventory](../../Gameplay/Looting_Interactions.md) and economy docs.

---

## Cross-References

- [Gear Tier System](../Gear_Tier_System.md) — Armor Tier (1–5) definition; progression = Tier + Rarity + player/trader level.
- [Armor Master Database](Armor_Master_Database.md) — Trader column per item.
- [Safe House Design](../../GameDesign/Safe_House_Design.md) — Crafting recipes, bench requirements.
- [Progression](../../GameDesign/Progression.md) — Player and trader progression framework.
- [Quest Objective System](../../Gameplay/Quest_Objective_System.md) — Quest gates for armor unlocks.
