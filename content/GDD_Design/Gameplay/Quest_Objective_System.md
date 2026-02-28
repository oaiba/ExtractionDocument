---
title: "Quest & Objective System"
type: docs
weight: 16
---

## Overview

Quests are the **primary structured goal layer** on top of free-form looting and extraction. They direct player movement toward specific map areas, reward faction reputation, unlock trader tiers, and provide narrative context for each raid. Unlike open-world quest systems, all extraction shooter quests must function within the high-stakes raid context — partial completion, death, and extraction failures are built-in risk elements.

> **Cross-References:** [Core Gameplay Loop](CoreLoop.md) — Quest Turn-In in Phase 5 Recovery; [Looting & Inventory](Looting_Interactions.md) — "Found-in-Raid" status for quest items; [AI Enemy Behavior](AI_Enemy_Behavior.md) — AI faction affiliations; [Extraction Mechanics](Extraction_Mechanics.md) — quest-gated extraction zones; [Matchmaking & Lobby](Matchmaking_Lobby.md) — private raids disable quest completion; [GameDesign/Progression](../../GameDesign/Progression.md) — quest chains as progression gates.

---

## Design Principles

- **Quest items carry raid risk.** Most quest items require "Found-in-Raid" (FIR) status and must be physically extracted — they can be lost to death, adding meaningful stakes.
- **No quest radar.** Objectives appear on the player's map but give no in-raid minimap ping to the exact spot. Players must navigate and search using the minimap and knowledge.
- **Quests shape route habits.** Each quest should push players into an area they might avoid organically, teaching map knowledge as a side effect.
- **Multi-session design.** Most quests take 2–5 raids to complete, spreading the reward across sessions and creating recurring motivation to log in.
- **Solo-viable.** All quests can be solo-completed. Squad bonuses are optional (efficiency, not access).

---

## Quest NPC Givers (Traders)

Each trader grants access to their quest chain, and completing their quests raises reputation (Loyalty Level), unlocking better goods and pricing.

| Trader | Faction Tie | Quest Theme | Loyalty Caps At |
| :----- | :---------- | :---------- | :-------------- |
| **Viktor** (Arms Dealer) | Neutral | Weapon recovery, elimination | Loyalty 4 |
| **Mira** (Medic Supplier) | Neutral | Medical collection, survival challenges | Loyalty 4 |
| **Commander Rask** (Military) | Faction A | Intelligence gathering, strategic targets | Loyalty 4 |
| **Shadow** (Black Market) | Faction B | Smuggling, contraband, extraction challenges | Loyalty 4 |
| **Dr. Chen** (Researcher) | Independent | Technical items, artifact recovery, exploration | Loyalty 3 |

> **Loyalty Level unlocks:** Each level unlocks better item availability and pricing. See [GameDesign/Progression](../../GameDesign/Progression.md) for full Loyalty Level requirements.

---

## Quest Categories

### Category 1 — Elimination

Kill a specified number of enemies (AI or players) of a given type, faction, or location.

| Sub-type | Example | Notes |
| :------- | :------ | :---- |
| AI kill count | "Kill 15 Scavengers in the Industrial Zone" | Directs players to specific map area |
| AI faction specific | "Kill 5 Sec-Force guards at the Checkpoint" | Rewards high-risk play in guarded areas |
| Boss kill | "Kill the Kommandant" | One-off; guaranteed boss quest chain |
| PvP kill | "Kill 3 enemy operators" | PvP-aggressive quest; not forced on pacifist players |
| Location kill | "Eliminate 10 enemies in the Residential District" | Area-specific |

**Tracking:** Kill credit requires the kill to occur in a standard or ranked raid (not private). FIR status not required for kills.

---

### Category 2 — Collection

Retrieve specific items and extract with them. These are the most common quest type.

| Sub-type | Example | Notes |
| :------- | :------ | :---- |
| Single item | "Find 1 Golden Chip and extract with it" | High-value single item; rare spawn |
| Multiple same item | "Extract with 3 Military Laptops" | Requires 3 separate raids or lucky loot |
| Variety pack | "Extract with 1 Medkit, 1 Military Case, and 1 Keycard" | Forces specific loot combination |
| Crafted item | "Extract with 1 Purified Water (crafted)" | Links hideout crafting to quest |
| Item condition | "Extract with a weapon in >60% durability" | No degraded war trophies |

**FIR requirement:** All collection quests require items to have "Found-in-Raid" status per [Looting & Inventory](Looting_Interactions.md). Items purchased from traders or the flea market cannot be used.

---

### Category 3 — Mark / Investigate

Interact with a specific world object at a location to "mark" or scan it. No item required.

| Sub-type | Example | Notes |
| :------- | :------ | :---- |
| Mark objective | "Place a tracker on the Cargo Container in West Dock" | 3-second interaction, very loud, creates ambush opportunity |
| Photograph | "Photograph the server room in the Lab facility" | Uses in-raid camera item (consumable) |
| Scan (tech item) | "Use the Signal Scanner at the broadcast tower" | Requires carrying a bulky quest item |
| Document pickup | "Retrieve the encrypted drive from the Director's Office" | FIR required; item spawns only in specific container |

**Design intent:** Mark quests direct players to specific locations without requiring them to carry heavy items. The interaction time and noise creates a vulnerability window — an organic PvP hotspot.

---

### Category 4 — Survive & Reach

Reach a location and extract from a specific zone. No item required.

| Sub-type | Example | Notes |
| :------- | :------ | :---- |
| Reach & extract | "Extract from the Northern Checkpoint 2 times" | Teaches uncommon extraction routes |
| Survive duration | "Survive for at least 15 minutes in a standard raid" | Anti-skirter/early quitter challenge |
| Timed run | "Extract within 8 minutes of raid start" | Speed-run challenge; contradicts looting playstyle |
| Wounded extract | "Extract with less than 35 HP remaining" | Fringe challenge for experienced players |
| Injure & extract | "Extract while actively bleeding" | Dark; teaches that bleeding is manageable |

---

### Category 5 — Escort / Cooperative (Future — Post-Beta)

Work with allies or other players (even from different factions) to complete a shared goal.

| Sub-type | Example | Notes |
| :------- | :------ | :---- |
| Squad extraction | "Extract with your full 3-player squad intact" | All members must extract to count |
| Revive quest | "Successfully revive a downed teammate 3 times" | Links to [Downstate & Revive](Downstate_Revive.md) |
| Cooperative extraction | "Extract with a player from the opposing faction" | Uses Cooperative Extraction zone per [Extraction Mechanics](Extraction_Mechanics.md) |

> **Post-Beta:** Escort/cooperative quests introduce social trust mechanics and are intentionally held back from early access to let the community establish playstyle norms.

---

## Quest Lifecycle

### Quest States

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

### Progress Persistence

| Objective type | Progress kept on death? | Notes |
| :------------- | :---------------------- | :---- |
| Kill count | ✅ Yes | Kills accumulate across multiple raids |
| Item collection | ❌ No (FIR items lost) | Item must be physically extracted; losing it loses credit |
| Mark / scan | ✅ Yes | Interaction registers on server immediately |
| Survive duration | ✅ Partial | Time survived in this raid counts; resets next raid |
| Reach location | ✅ Yes | "Visited" flag set server-side on arrival |
| Extract from zone | ❌ No | Must complete extraction |

---

## Quest Chain Design

### Chain Structure

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

### Cross-Trader Chains

Some quests require completion of a chain from *another* trader first — creating natural decision points:

> "Shadow's 'Inside Contact' quest chain requires Viktor Loyalty Level 2 — players must first arm themselves well enough to navigate black-market supply lines."

---

## Quest Rewards

| Reward Type | Range | Frequency |
| :---------- | :---- | :-------- |
| **Currency ($)** | 5,000–100,000 | Every quest |
| **Trader Loyalty XP** | +0.1 to +0.5 per quest | Every quest |
| **Items (weapons, armor, meds)** | Tier 2–4 depending on chain stage | ~70% of quests |
| **Unique blueprint (crafting recipe)** | Rare/unique items | ~20% — chain finale rewards |
| **Operator XP** | +500–2,000 XP flat bonus | ~40% |
| **Trader level unlock** | Unlocks new Loyalty Level | Chain milestone quests |
| **Cosmetic** | Operator skin, weapon charm | Special/limited quests only |
| **Stash expansion** | +1 row added to stash | Specific milestone quests (non-repeatable) |

---

## Daily & Weekly Quests

In addition to main chains, dynamic quests refresh on a timer:

| Type | Refresh | Count | Example |
| :--- | :------ | :---- | :------ |
| **Daily Task** | 24h | 3 active at once | "Extract with 2 energy drinks" |
| **Weekly Challenge** | 7 days | 1 active | "Kill 30 enemies in the Lab zone this week" |
| **Limited Event Quest** | Live-ops schedule | 1–3 | "Find 5 Contaminated Samples during Hazard Week" |

**Daily Task reward range:** $3,000–8,000 + small item bundle.  
**Weekly Challenge reward:** $20,000–60,000 + Loyalty bonus.

---

## Quest HUD Integration

### In-Raid Quest Tracker

| Element | Display | Location |
| :------ | :------ | :------- |
| Active quest name | Always visible (small text) | Top-right HUD |
| Objective progress | "Scavs: 3/5" counter | Below quest name |
| Map marker | Colored zone boundary on minimap | Minimap only (no compass icon) |
| Interaction prompt | On-screen when near markable object | contextual pop-up |
| Quest item spawn | Highlighted container outline when within 3m | World-space indicator |

**Quest item glow:** Quest-relevant containers glow with a faint gold outline when within 3m and the relevant quest is active. This is QoL without removing exploration.

---

## Cross-References

- [Core Gameplay Loop](CoreLoop.md) — Quest turn-in in Phase 5; Quest XP as non-extraction reward.
- [Looting & Inventory](Looting_Interactions.md) — "Found-in-Raid" status gate for collection quests.
- [AI Enemy Behavior](AI_Enemy_Behavior.md) — AI faction affiliations; boss kill quests.
- [Extraction Mechanics](Extraction_Mechanics.md) — Cooperative extraction zone quest; zone-specific extraction quests.
- [Matchmaking & Lobby](Matchmaking_Lobby.md) — Private raid disables quest completion.
- [Hideout & Crafting](Hideout_Crafting.md) — Hideout upgrades gated behind trader quest chain completion.
- [GameDesign/Progression](../../GameDesign/Progression.md) — Loyalty Level system; quest XP integration.
- [GameDesign/Economy](../../GameDesign/Economy.md) — Quest cash rewards as economy faucet.
