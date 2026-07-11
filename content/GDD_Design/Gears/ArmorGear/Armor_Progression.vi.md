---
title: "giáp Progression"
type: docs
weight: 5
---

## Tổng Quan

This tài liệu covers **trader unlock gating**, **Safe House repair bench progression**, **giáp crafting**, và **Found-in-Raid (FIR) giáp** rules. For item list Xem [giáp Master Database](armor_master_database/index.html); for balance Xem [giáp Balance Framework](armor_balance_framework/index.html).

---

## Trader Unlock Gating

giáp tier (per [Gear Tier hệ thống](../gear_tier_system/index.html)) is gated by trader level, quests, và người chơi level so that early game is not dominated by top-tier giáp.

| giáp tier | Trader level required | Quest gate | Level gate |
| :--------- | :-------------------: | :--------- | :--------: |
| Class 1–2 | Trader Lvl 1 | None | 1 |
| Class 3 | Trader Lvl 2 | e.g. "Proving Ground" | 10 |
| Class 4 | Trader Lvl 3 | e.g. "Armored Up" | 20 |
| Class 5 | Trader Lvl 4 | e.g. "Forged in Fire" | 35 |
| Class 6 | Trader Lvl 4 (Exalted) | e.g. Boss kill / endgame quest | 45 |

Exact quest names và level thông số are placeholders; adjust to match [Progression](../../gamedesign/progression/index.html) và quest design.

---

## Safe House Repair Bench Progression

Repair bench level determines which giáp classes và materials can be repaired in-raid hoặc in Safe House, và repair efficiency.

| Bench level | Repairable class | Repairable materials | ghi chú |
| :---------- | :--------------- | :------------------- | :---- |
| 1 | Class 1–3 | Aramid, Steel | Basic repairs only |
| 2 | Class 1–4 | All materials | Full material set |
| 3 | Class 1–6 | All materials | Reduced repair max loss (−2% per repair) |

Trader repair remains available for all classes và materials nhưng uses standard material repair loss; Safe House Lvl 3 bench is the best long-term option for high-tier giáp.

---

## giáp Crafting (Safe House)

Selected giáp pieces can be crafted at the Safe House. Recipes consume materials và thời gian; output is one giáp item at fixed durability (e.g. 80–100%).

**Example recipes (placeholder):**

- **Class 3 vest:** 5× Polymer + 3× Rare Components + 2 h → 1× Ceramic Carrier (80% durability).
- **Class 2 vest:** 3× Aramid + 2× Scrap Metal + 30 min → 1× Press Vest (90% durability).

Crafting provides an alternative to trader purchase và FIR loot, và consumes barter/crafting materials. Full recipe list should live in [Safe House Design](../../gamedesign/safe_house_design/index.html) với references here.

---

## Found-in-Raid (FIR) giáp

- **FIR giáp** spawns in-raid với **durability in a range** (e.g. 60–100% of max). This avoids “free” full-durability top-tier giáp from loot only.
- FIR giáp is often the **only way** to obtain certain rare hoặc high-class pieces trước unlocking the corresponding trader level hoặc quest.
- FIR status is lost nếu the item is brought into raid by the người chơi (e.g. re-equipped). Marketplace và FIR rules: Xem [Looting & Inventory](../../gameplay/looting_interactions/index.html) và economy docs.

---

## Tham Chiếu Chéo

- [Gear Tier hệ thống](../gear_tier_system/index.html) — giáp Tier (1–5) định nghĩa; progression = Tier + Rarity + người chơi/trader level.
- [giáp Master Database](armor_master_database/index.html) — Trader column per item.
- [Safe House Design](../../gamedesign/safe_house_design/index.html) — Crafting recipes, bench yêu cầu.
- [Progression](../../gamedesign/progression/index.html) — người chơi và trader progression framework.
- [Quest Objective hệ thống](../../gameplay/quest_objective_system/index.html) — Quest gates for giáp unlocks.
