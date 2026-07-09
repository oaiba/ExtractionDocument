---
title: "Quest & Objective hệ thống"
type: docs
weight: 16
---

### Tổng Quan

Quests are the **primary structured mục tiêu layer** on top of free-form looting và extraction. They direct người chơi movement toward cụ thể map areas, reward faction reputation, unlock trader tiers, và provide narrative context for each raid. Unlike open-world quest hệ thống, all extraction shooter quests must function within the high-stakes raid context — partial completion, death, và extraction failures are built-in risk elements.

> **Cross-References:** [cốt lõi Gameplay Loop](CoreLoop.md) — Quest Turn-In in Phase 5 Recovery; [Looting & Inventory](Looting_Interactions.md) — "Found-in-Raid" status for quest items; [AI địch Behavior](AI_Enemy_Behavior.md) — AI faction affiliations; [Extraction cơ chế](Extraction_Mechanics.md) — quest-gated extraction zones; [Matchmaking & Lobby](Matchmaking_Lobby.md) — private raids disable quest completion; [GameDesign/Progression](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Progression.md) — quest chains as progression gates.

***

### Nguyên Tắc Thiết Kế

* **Quest items carry raid risk.** Most quest items require "Found-in-Raid" (FIR) status và phải được physically extracted — they can be lost to death, adding meaningful stakes.
* **No quest radar.** Objectives appear on the người chơi's map nhưng give no in-raid minimap ping to the exact spot. người chơi must navigate và search using the minimap và knowledge.
* **Quests shape route habits.** Each quest should push người chơi into an area they might avoid organically, teaching map knowledge as a side effect.
* **Multi-session design.** Most quests take 2–5 raids to complete, spreading the reward across sessions và tạo recurring motivation to log in.
* **Solo-viable.** All quests can be solo-completed. Squad bonuses are optional (efficiency, not access).

***

### Quest NPC Givers (Traders)

Each trader grants access to their quest chain, và completing their quests raises reputation (Loyalty Level), unlocking better goods và pricing.

| Trader                        | Faction Tie | Quest Theme                                     | Loyalty Caps At |
| ----------------------------- | ----------- | ----------------------------------------------- | --------------- |
| **Viktor** (Arms Dealer)      | Neutral     | vũ khí recovery, elimination                    | Loyalty 4       |
| **Mira** (Medic Supplier)     | Neutral     | Medical collection, survival challenges         | Loyalty 4       |
| **Commander Rask** (Military) | Faction A   | Intelligence gathering, strategic targets       | Loyalty 4       |
| **Shadow** (Black Market)     | Faction B   | Smuggling, contraband, extraction challenges    | Loyalty 4       |
| **Dr. Chen** (Researcher)     | Independent | Technical items, artifact recovery, exploration | Loyalty 3       |

> **Loyalty Level unlocks:** Each level unlocks better item availability và pricing. Xem [GameDesign/Progression](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Progression.md) for full Loyalty Level yêu cầu.

***

### Quest Categories

#### Category 1 — Elimination

Kill a specified number of địch (AI hoặc người chơi) of a given type, faction, hoặc location.

| Sub-type            | Example                                            | ghi chú                                                |
| ------------------- | -------------------------------------------------- | ---------------------------------------------------- |
| AI kill count       | "Kill 15 Scavengers in the Industrial Zone"        | Directs người chơi to cụ thể map area                 |
| AI faction cụ thể | "Kill 5 Sec-Force guards at the Checkpoint"        | Rewards high-risk play in guarded areas              |
| Boss kill           | "Kill the Kommandant"                              | One-off; guaranteed boss quest chain                 |
| PvP kill            | "Kill 3 địch operators"                           | PvP-aggressive quest; not forced on pacifist người chơi |
| Location kill       | "Eliminate 10 địch in the Residential District" | Area-cụ thể                                        |

**Tracking:** Kill credit requires the kill to occur in a standard hoặc ranked raid (not private). FIR status not required for kills.

***

#### Category 2 — Collection

Retrieve cụ thể items và extract với them. These are the most common quest type.

| Sub-type           | Example                                                 | ghi chú                                   |
| ------------------ | ------------------------------------------------------- | --------------------------------------- |
| Single item        | "Find 1 Golden Chip và extract với it"                | High-giá trị single item; rare spawn      |
| Multiple same item | "Extract với 3 Military Laptops"                       | Requires 3 separate raids hoặc lucky loot |
| Variety pack       | "Extract với 1 Medkit, 1 Military Case, và 1 Keycard" | Forces cụ thể loot combination        |
| Crafted item       | "Extract với 1 Purified Water (crafted)"               | Links Safe House crafting to quest      |
| Item condition     | "Extract với a vũ khí in >60% durability"              | No degraded war trophies                |

**FIR yêu cầu:** All collection quests require items to have "Found-in-Raid" status per [Looting & Inventory](Looting_Interactions.md). Items purchased from traders hoặc the flea market cannot be used.

***

#### Category 3 — Mark / Investigate

Interact với a cụ thể world object at a location to "mark" hoặc scan it. No item required.

| Sub-type         | Example                                                   | ghi chú                                                       |
| ---------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Mark objective   | "Place a tracker on the Cargo Container in West Dock"     | 3-second interaction, very loud, tạo ambush opportunity |
| Photograph       | "Photograph the server room in the Lab facility"          | Uses in-raid camera item (consumable)                       |
| Scan (tech item) | "cách dùng the Signal Scanner at the broadcast tower"           | Requires carrying a bulky quest item                        |
| tài liệu pickup  | "Retrieve the encrypted drive from the Director's Office" | FIR required; item spawns only in cụ thể container        |

**Design intent:** Mark quests direct người chơi to cụ thể locations mà không requiring them to carry heavy items. The interaction thời gian và noise tạo a vulnerability window — an organic PvP hotspot.

***

#### Category 4 — Survive & Reach

Reach a location và extract from a cụ thể zone. No item required.

| Sub-type         | Example                                              | ghi chú                                              |
| ---------------- | ---------------------------------------------------- | -------------------------------------------------- |
| Reach & extract  | "Extract from the Northern Checkpoint 2 times"       | Teaches uncommon extraction routes                 |
| Survive duration | "Survive for at least 15 minutes in a standard raid" | Anti-skirter/early quitter challenge               |
| Timed run        | "Extract within 8 minutes of raid start"             | Speed-run challenge; contradicts looting playstyle |
| Wounded extract  | "Extract với less than 35 HP remaining"             | Fringe challenge for experienced người chơi           |
| Injure & extract | "Extract while actively bleeding"                    | Dark; teaches that bleeding is manageable          |

***

#### Category 5 — Escort / Cooperative (Future — Post-Beta)

Work với allies hoặc other người chơi (even from different factions) to complete a shared mục tiêu.

| Sub-type               | Example                                           | ghi chú                                                                                |
| ---------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Squad extraction       | "Extract với your full 3-người chơi squad intact"    | All members must extract to count                                                    |
| Revive quest           | "Successfully revive a downed teammate 3 times"   | Links to [Downstate & Revive](Downstate_Revive.md)                                   |
| Cooperative extraction | "Extract với a người chơi from the opposing faction" | Uses Cooperative Extraction zone per [Extraction cơ chế](Extraction_Mechanics.md) |

> **Post-Beta:** Escort/cooperative quests introduce social trust cơ chế và are intentionally held back from early access to let the community establish playstyle norms.

***

### Quest Lifecycle

#### Quest trạng thái

```
LOCKED
  (prerequisite quest not completed, trader loyalty too low)
    ↓
AVAILABLE
  (visible in trader screen; player can accept)
    ↓
ACTIVE
  (accepted; tracked in UI; objectives visible on map)
    ↓
  ┌──── PARTIAL (some objectives met; raid ended in death)
  │         ↓ Progress is SAVED for most objective types
  └──────────────────────────────────────────────────────┐
READY TO TURN IN                                         │
  (all objectives complete; must visit trader)           │
    ↓                                                    │
COMPLETED ←──────────────────────────────────────────────┘
  (permanent; rewards granted)
```

#### Progress Persistence

| Objective type    | Progress kept on death? | ghi chú                                                     |
| ----------------- | ----------------------- | --------------------------------------------------------- |
| Kill count        |  Yes                   | Kills accumulate across multiple raids                    |
| Item collection   |  No (FIR items lost)   | Item phải được physically extracted; losing it loses credit |
| Mark / scan       |  Yes                   | Interaction registers on server immediately               |
| Survive duration  |  Partial               | thời gian survived in this raid counts; resets next raid       |
| Reach location    |  Yes                   | "Visited" flag set server-side on arrival                 |
| Extract from zone |  No                    | Must complete extraction                                  |

***

### Quest Chain Design

#### Chain Structure

Quests form chains per trader. Each chain has 3–5 quests gating into the next trust level.

**Example: Viktor's Chain (Alpha test, 5 quests)**

```
[VK-01] "First Blood"
   Kill 5 Scavs anywhere
   Reward: $5,000 + Viktor Loyalty +0.2
     ↓
[VK-02] "Recovery Operation"
   Find and extract with 1 Viktor's Crate (marked container)
   Reward: 2× M4A1 (Tier 2) + $8,000 + Loyalty +0.3
     ↓
[VK-03] "Armed and Ready"
   Kill 10 Militia Raiders + extract with any AR at <50% durability
   Reward: Weapon mod kit + Viktor Loyalty Level 2 unlock
     ↓
[VK-04] "Black Site"
   Enter the Vault Room (keycard required) + photograph the server
   Reward: $25,000 + rare weapon skin + Loyalty +0.4
     ↓
[VK-05] "The Kommandant's End"
   Kill the Kommandant boss
   Reward: Viktor Loyalty Level 3 unlock + unique weapon blueprint
```

#### Cross-Trader Chains

Some quests require completion of a chain from _another_ trader first — tạo natural quyết định points:

> "Shadow's 'Inside Contact' quest chain requires Viktor Loyalty Level 2 — người chơi must first arm themselves well enough to navigate black-market supply lines."

***

### Quest Rewards

| Reward Type                            | Range                             | Frequency                                  |
| -------------------------------------- | --------------------------------- | ------------------------------------------ |
| **Currency ($)**                       | 5,000–100,000                     | Every quest                                |
| **Trader Loyalty XP**                  | +0.1 to +0.5 per quest            | Every quest                                |
| **Items (vũ khí, giáp, meds)**       | Tier 2–4 depending on chain stage | \~70% of quests                            |
| **Unique blueprint (crafting recipe)** | Rare/unique items                 | \~20% — chain finale rewards               |
| **Operator XP**                        | +500–2,000 XP flat bonus          | \~40%                                      |
| **Trader level unlock**                | Unlocks new Loyalty Level         | Chain milestone quests                     |
| **cosmetic**                           | Operator skin, vũ khí charm       | Special/limited quests only                |
| **Stash expansion**                    | +1 row added to stash             | cụ thể milestone quests (non-repeatable) |

***

### Daily & Weekly Quests

In addition to main chains, dynamic quests refresh on a timer:

| Type                    | Refresh           | Count            | Example                                          |
| ----------------------- | ----------------- | ---------------- | ------------------------------------------------ |
| **Daily Task**          | 24h               | 3 active at once | "Extract với 2 energy drinks"                   |
| **Weekly Challenge**    | 7 days            | 1 active         | "Kill 30 địch in the Lab zone this week"      |
| **Limited Event Quest** | Live-ops schedule | 1–3              | "Find 5 Contaminated Samples trong khi Hazard Week" |

**Daily Task reward range:** $3,000–8,000 + small item bundle.\
**Weekly Challenge reward:** $20,000–60,000 + Loyalty bonus.

***

### Quest HUD Integration

#### In-Raid Quest Tracker

| Element            | Display                                      | Location                       |
| ------------------ | -------------------------------------------- | ------------------------------ |
| Active quest name  | Always hiển thị rõ (small text)                  | Top-right HUD                  |
| Objective progress | "Scavs: 3/5" counter                         | Below quest name               |
| Map marker         | Colored zone boundary on minimap             | Minimap only (no compass icon) |
| Interaction prompt | On-màn hình khi near markable object          | contextual pop-up              |
| Quest item spawn   | Highlighted container outline khi within 3m | World-space indicator          |

**Quest item glow:** Quest-relevant containers glow với a faint gold outline khi within 3m và the relevant quest is active. This is QoL mà không removing exploration.

***

### Tham Chiếu Chéo

* [cốt lõi Gameplay Loop](CoreLoop.md) — Quest turn-in in Phase 5; Quest XP as non-extraction reward.
* [Looting & Inventory](Looting_Interactions.md) — "Found-in-Raid" status gate for collection quests.
* [AI địch Behavior](AI_Enemy_Behavior.md) — AI faction affiliations; boss kill quests.
* [Extraction cơ chế](Extraction_Mechanics.md) — Cooperative extraction zone quest; zone-cụ thể extraction quests.
* [Matchmaking & Lobby](Matchmaking_Lobby.md) — Private raid disables quest completion.
* [Safe House Design](../GameDesign/Safe_House_Design.md) — Safe House upgrades gated behind trader quest chain completion.
* [GameDesign/Progression](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Progression.md) — Loyalty Level hệ thống; quest XP integration.
* [GameDesign/Economy](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Economy.md) — Quest cash rewards as economy faucet.
