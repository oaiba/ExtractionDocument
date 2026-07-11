---
title: "Loot Table Design"
type: docs
weight: 17
---

### Tổng Quan

The loot bảng hệ thống governs what items spawn in the world, at what rarity, và in which containers per map zone. It is the **most direct lever for economic balance** — loot tables set the volume of items flowing into the game each raid, directly affecting prices on the flea market và trader stock. This tài liệu specifies container types, zone loot tiers, item category weights, và spawn density rules.

> **Cross-References:** [Looting & Inventory](looting_interactions/index.html) — container interaction cơ chế, grid inventory, FIR status; [AI địch Behavior](ai_enemy_behavior/index.html) — AI corpse loot; [Environmental Hazards](environmental_hazards/index.html) — supply drop loot, boss loot tables; [Safe House Design](../gamedesign/safe_house_design/index.html) — crafting materials as loot category; [GameDesign/Economy](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Economy.md) — faucet/sink calibration.

***

### Nguyên Tắc Thiết Kế

* **Scarcity tạo giá trị.** Not every container has useful loot. empty hoặc low-giá trị containers make high-giá trị finds feel special.
* **Zone reinforces risk-reward.** Higher threat zones (military, laboratories) yield higher-tier loot. người chơi who push dangerous areas are consistently rewarded.
* **Dynamic density prevents farming.** Spawn density varies per instance — the same container does not always contain the same items. Loot feels discovered, not farmed.
* **AI carry contextual loot.** Scav corpses don't have military items; Sec-Force corpses don't carry civilian goods. Loot makes narrative sense.
* **No guaranteed cụ thể item spawns (except quest items).** Quest item containers have guaranteed spawns for the relevant quest item khi the quest is active — otherwise they spawn generic loot.

***

### Container Types

#### Physical World Containers

| Container             | Size | UI Label     | Zones Typically Found In | Loot Category                        |
| --------------------- | ---- | ------------ | ------------------------ | ------------------------------------ |
| **Wooden Crate**      | 3×3  | Crate        | All zones                | General supplies, đạn, food         |
| **Metal Locker**      | 3×4  | Locker       | Industrial, Military     | vũ khí, giáp, gear                 |
| **Desk Drawers**      | 2×2  | Drawers      | Residential, Office      | Cash, documents, keys                |
| **Filing Cabinet**    | 2×3  | Cabinet      | Office, Lab              | Documents, keycards, intel items     |
| **Safe**              | 2×2  | Safe         | Residential, Office      | Cash, jewelry, small valuables       |
| **Medical Cabinet**   | 2×3  | Med Cabinet  | Hospital, Checkpoint     | Medical items, stimulants            |
| **đạn Box**          | 2×2  | đạn Box     | Military, Checkpoint     | đạn only                            |
| **Electronics Shelf** | 3×3  | Electronics  | Lab, Office              | Electronics, GPUs, circuit boards    |
| **Tool Cabinet**      | 3×3  | Tool Cabinet | Industrial, Workshop     | Crafting parts (bolts, wires, pipes) |
| **Refrigerator**      | 2×4  | Fridge       | Residential, Break Room  | Food, water, medical crossover       |
| **Boss Stash**        | 4×4  | Boss Stash   | Boss-exclusive zone      | Boss-tier loot, unique items         |
| **Supply Drop Crate** | 4×5  | Air Drop     | Dynamic event only       | Tier 3–4 mixed loot                  |
| **Vehicle Trunk**     | 3×4  | Trunk        | Roads, Parking           | Fuel, tools, moderate gear           |

***

### Map Zones và Loot Tiers

Each map has 4-5 named zones. Zone tier determines which loot tables are used.

#### Zone Tier Definitions

| Tier                | Description                   | Zones (Example Map: "Harbortown")       | Container Density                     |
| ------------------- | ----------------------------- | --------------------------------------- | ------------------------------------- |
| **Tier 1 — Low**    | Open areas, civilian streets  | Residential District, Outer Docks       | 30–40 containers per 10,000 m²        |
| **Tier 2 — Medium** | Commercial, industrial        | Warehouses, Central Market              | 40–55 containers                      |
| **Tier 3 — High**   | Guarded hoặc dangerous areas    | Industrial Complex, Checkpoint          | 25–35 containers (fewer nhưng better)   |
| **Tier 4 — Elite**  | Boss zone, locked rooms, labs | Director's Office, The Vault, Lab Block | 10–20 containers (scarce nhưng premium) |

***

### Loot bảng — By Zone Tier

#### Tier 1 — Residential / Open Areas

| Item Category       | Chance (per container) | Typical Items                         |
| ------------------- | :--------------------: | ------------------------------------- |
| **empty**           |           25%          | Nothing                               |
| **Food/Water**      |           30%          | Water bottle, juice, MRE, canned food |
| **Basic Medical**   |           15%          | Bandage x2, AI-2 medkit               |
| **Cash ($)**        |           15%          | $200–$1,500                           |
| **Barter (common)** |           10%          | Wires, bolts, cloth, matches          |
| **vũ khí (Tier 1)** |           3%           | Pistol, basic shotgun                 |
| **chính**             |           2%           | Common area chính                       |

> **Expected loot giá trị per container (average):** \~$1,200

***

#### Tier 2 — Industrial / Commercial

| Item Category            | Chance | Typical Items                               |
| ------------------------ | :----: | ------------------------------------------- |
| **empty**                |   15%  | Nothing                                     |
| **Crafting Materials**   |   25%  | Metal pipes, wires, cơ chế parts, bolts |
| **đạn (Tier 1–2)**      |   20%  | FMJ rounds, buckshot (20–100 rounds)        |
| **vũ khí (Tier 2)**      |   12%  | AR, SMG, shotgun (lightly degraded)         |
| **giáp (Class 2–3)**    |   8%   | Soft vest, light helmet                     |
| **Medical (Standard)**   |   8%   | IFAK, painkillers                           |
| **Electronics (common)** |   6%   | Wires, circuit board basic                  |
| **Cash ($)**             |   4%   | $1,000–$4,000                               |
| **chính**                  |   2%   | Industrial chính                              |

> **Expected loot giá trị per container:** \~$4,500

***

#### Tier 3 — Military / Checkpoint

| Item Category           | Chance | Typical Items                                |
| ----------------------- | :----: | -------------------------------------------- |
| **empty**               |   8%   | Nothing                                      |
| **vũ khí (Tier 3)**     |   18%  | Modded AR, DMR, LMG                          |
| **đạn (AP/special)**   |   20%  | giáp-piercing, hollow-point (50–100 rounds) |
| **giáp (Class 3–4)**   |   14%  | Plate carrier, military helmet               |
| **Medical (Advanced)**  |   12%  | Grizzly kit, IFAK, stims                     |
| **Electronics**         |   10%  | Circuit boards, GPUs (5% chance)             |
| **Crafting (Military)** |   8%   | Spark plugs, bearings, precision parts       |
| **Cash ($)**            |   6%   | $3,000–$10,000                               |
| **Keycard (common)**    |   3%   | Bronze/Silver keycard                        |
| **Intel Item**          |   1%   | Encrypted drive, military documents          |

> **Expected loot giá trị per container:** \~$12,000

***

#### Tier 4 — Elite (Vault / Lab / Boss Zone)

| Item Category         | Chance | Typical Items                               |
| --------------------- | :----: | ------------------------------------------- |
| **empty**             |   5%   | Nothing                                     |
| **vũ khí (Tier 4)**   |   15%  | Rare sniper, LMG, fully-modded AR           |
| **giáp (Class 5–6)** |   10%  | Heavy plate carrier, ballistic helmet       |
| **GPU**               |   20%  | GPU ×1–3 (Bitcoin Farm fuel)                |
| **Rare Electronics**  |   15%  | Server blade, rare circuit board, processor |
| **Stimulants**        |   10%  | Adrenaline, Propital, SJ6                   |
| **Cash ($)**          |   10%  | $8,000–$25,000                              |
| **Keycard (rare)**    |   8%   | Gold keycard, Lab card                      |
| **Unique Quest Item** |   5%   | Intel artifact, boss chính, mission files     |
| **vũ khí Blueprint**  |   2%   | Safe House crafting recipe (unique)         |

> **Expected loot giá trị per container:** \~$40,000

***

### AI Corpse Loot Tables

#### By địch Tier

| địch Type                  | vũ khí (kept on body)             | giáp (degraded)   | Special Loot                                        |
| --------------------------- | --------------------------------- | ------------------ | --------------------------------------------------- |
| **Scav (Tier 1)**           | Tier 1 vũ khí (50–70% durability) | Class 0–2 (30–60%) | Food ×1, $200–$600, occasional chính                  |
| **Militia Raider (Tier 2)** | Tier 2 vũ khí (50–80%)            | Class 2–3 (40–70%) | đạn ×20–50, $500–$2,000, rig (15% chance)          |
| **Sec-Force (Tier 3)**      | Tier 3 vũ khí (60–90%)            | Class 3–4 (50–80%) | AP đạn ×30–80, $1,500–$5,000, keycard (10% chance) |
| **Rogue PMC (Tier 4)**      | Tier 4 vũ khí (70–95%)            | Class 4–5 (60–90%) | Stim ×1–2, $3,000–$10,000, rare item (20% chance)   |

> AI gear condition varies vì AI takes damage trong khi combat. Condition is randomized within the range above at AI spawn, và further reduced by any hits they actually take trong khi the raid.

***

### Boss Loot Tables

| Boss           | Guaranteed                                       | Random Drop (50% each)                 | Unique Drop (15%)                                   |
| -------------- | ------------------------------------------------ | -------------------------------------- | --------------------------------------------------- |
| **Kommandant** | Tier 4 vũ khí, Class 5 giáp, Vault Room keycard | Stim ×2, $15,000–$30,000, blueprint    | "Kommandant's Sidearm" unique pistol                |
| **Obsidian**   | Suppressed Tier 3–4 vũ khí, Intel item           | Light rig, $10,000–$20,000             | "Obsidian's Cloak Module" — unique gadget component |
| **Iron Wall**  | LMG (Tier 4), Military keycard                   | Class 5 giáp (heavy), $20,000–$40,000 | "Iron Wall's cốt lõi" — quest-chain-only barter item   |

***

### Dynamic Loot Events

#### Supply Drop

| Property           | giá trị                                                                              |
| ------------------ | ---------------------------------------------------------------------------------- |
| **Trigger**        | Dynamic event per [Environmental Hazards](environmental_hazards/index.html)                |
| **Container**      | One 4×5 Super Crate                                                                |
| **Loot bảng**     | Tier 3 only — guaranteed at least 1 Tier 4 item, 3–5 Tier 3 items, $10,000–$20,000 |
| **AI guard**       | 4 Militia Raiders spawn at crate on landing                                        |
| **Contested thời gian** | Crate accessible 90s sau landing (AI spawn delay); becomes permanently lootable  |

#### Quest Container

| Property               | giá trị                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| **Spawn condition**    | Spawns only for cụ thể người chơi với active quest                                                 |
| **Server instancing**  | Different người chơi on same server see different quest item spawns                                   |
| **nếu looted by địch** | Item still counts as "found" — nhưng địch can extract it, denying the quest item to original người chơi |
| **Fallback**           | Quest item respawns in new location sau 5 minutes nếu not yet taken                               |

***

### Spawn Density Rules

#### Per-Instance Variation

To prevent farming predictability, each server instance shuffles loot:

| Rule                       | chi tiết                                                                                                                       |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **60% fill rate**          | On average, 60% of containers in a zone have loot. 40% are empty.                                                            |
| **±15% randomization**     | Each instance rolls ±15% density deviation (45–75% containers filled).                                                       |
| **Hot zone boost**         | nếu fewer than 8 người chơi remain alive at raid mid-point, loot density increases +10% for remaining người chơi (survival reward). |
| **người chơi proximity reset** | A container that was looted by người chơi A will appear empty to người chơi B — no ghost-items remain in containers.                 |
| **chính-gated rooms**        | Always 100% container fill rate behind locked doors (rewarding chính investment).                                              |

#### Loot Balance Target

| Zone Tier                  | Target average loot giá trị per người chơi per raid | Basis                                |
| -------------------------- | :-------------------------------------------: | ------------------------------------ |
| Tier 1 zones only          |                 $8,000–12,000                 | Rat-playstyle baseline               |
| Tier 2 + some Tier 3       |                 $20,000–40,000                | Standard run                         |
| Tier 3 + Tier 4            |                $50,000–120,000                | High-risk play                       |
| Full Chad run (all Tier 4) |                $80,000–200,000                | Peak; requires surviving boss fights |

***

### Seasonal & Event Loot Modifiers

| Event                   | Effect                                                                   | Duration    |
| ----------------------- | ------------------------------------------------------------------------ | ----------- |
| **Double Loot Weekend** | Container fill rate +25%; item quality tier +1                           | 48h live-op |
| **Scarcity Week**       | Container fill rate −30%; prices rise on flea market                     | 7 days      |
| **Contamination Event** | New hazardous item category spawns: Contamination Samples (quest-only)   | Live-op     |
| **Faction War**         | cụ thể AI faction loot bảng enriched (±30% of faction-cụ thể items) | 7 days      |

***

### Tham Chiếu Chéo

* [Looting & Inventory](looting_interactions/index.html) — Container interaction, FIR status, grid inventory.
* [AI địch Behavior](ai_enemy_behavior/index.html) — AI corpse loot tables; boss loot.
* [Environmental Hazards](environmental_hazards/index.html) — Supply drop event và Scav Raid wave loot.
* [Quest & Objective hệ thống](quest_objective_system/index.html) — Quest items và their container spawn rules.
* [Safe House Design](../gamedesign/safe_house_design/index.html) — Crafting materials as primary Tier 2 loot category.
* [GameDesign/Economy](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Economy.md) — Macro economy calibration; loot as primary faucet.
* [Items & Gear](itemsandgear/index.html) — Full item catalogue với values, weights, và drop categories.

***

### Dynamic Loot Scaling

The loot hệ thống adjusts dynamically based on in-raid conditions to maintain meaningful play throughout each session.

#### người chơi Count Adjustment

| Trigger                          | Effect                                          | mục đích                                                 |
| -------------------------------- | ----------------------------------------------- | ------------------------------------------------------- |
| More người chơi alive →             | More loot containers activated                  | Prevents loot drought in high-population sessions       |
| người chơi eliminated →             | Small loot quality increase globally            | Compensates surviving người chơi; rewards skilled survival |
| Fewer than 4 người chơi remaining → | Tier +1 upgrade applied to remaining containers | Incentivizes holding out vs early extract               |

#### thời gian-Based Scaling

| thời gian Range                | Loot Quality trạng thái                              |
| ------------------------- | ----------------------------------------------- |
| 0–5 min                   | Base bảng — Common/Uncommon dominant           |
| 5–10 min                  | Mid-tier push — Rare rate +20% globally         |
| 10+ min                   | Late quality — Elite containers enter hot zones |
| Contamination Zone active | Peak quality — best loot trước match end       |

#### Death-Based Scaling

Each confirmed người chơi kill in the match triggers a +2% loot quality modifier globally (stacks up to +20%). This tạo a positive feedback loop for survivors — the longer you live, the better the loot becomes.

***

### Seasonal Economy Events

Seasonal events temporarily shift the loot economy to tạo predictable spikes in supply hoặc demand that fuel the marketplace.

| Event                      | Duration   | Loot Effect                                                | Market Effect                                                    |
| -------------------------- | ---------- | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| **Double Loot Weekend**    | 48h        | Container fill rate +25%; quality tier +1                  | Prices drop due to supply surge; good thời gian to stock up           |
| **Scarcity Week**          | 7 days     | Container fill rate −30%                                   | Prices rise 20–50% — good thời gian to sell stockpiles                |
| **Rare Item Event**        | 3–5 days   | cụ thể vũ khí type spawn rate ×3 (e.g., "Sniper Week")   | Target item giá crashes; other categories less affected        |
| **Trader Special**         | 3 days     | NPC vendors 20–30% discount on selected categories         | mua from traders instead of marketplace; drives market balance   |
| **Faction War Loot Boost** | 7 days     | Faction-cụ thể AI loot enriched ±30%                     | Encourages fighting over zone control — affects zone competition |
| **Contamination Surge**    | Live event | New Contamination Sample items spawn (quest-only category) | No market impact (cannot sell) — affects quest progress speed    |

**Design intent:** Seasonal events give media coverage angles ("Scarcity Week forces market panic"), tạo predictable planning opportunities for veteran người chơi, và generate community discussion on forums và social channels.

***

### Economic Balance Goals

#### máu Indicators

The loot hệ thống is the primary economic faucet. These metrics indicate a balanced economy:

| Indicator             |        Healthy Range       | Problem Threshold                                       |
| --------------------- | :------------------------: | ------------------------------------------------------- |
| Average người chơi wealth |      $50,000–$150,000      | < $20,000 (poverty loop) hoặc > $500,000 (hyperinflation) |
| Inflation rate        |         < 5%/month         | > 15%/month = emergency intervention                    |
| Market activity       | 60%+ người chơi trade monthly | < 30% = dead market                                     |
| giá stability       |   < 20% fluctuation/week   | > 50% weekly swing = market manipulation                |

#### Developer Interventions

| Problem              | Lever                                                   |
| -------------------- | ------------------------------------------------------- |
| Hyperinflation       | Reduce loot fill rates, increase placeholder taxes      |
| Item scarcity        | Increase spawn rate via targeted Rare Item Event        |
| Wealth concentration | Adjust trader pricing for mid-tier items downward       |
| Dead market          | Run Double Loot Weekend + Trader Special simultaneously |
| Bot farming detected | Emergency fill-rate reduction + item sink event         |
