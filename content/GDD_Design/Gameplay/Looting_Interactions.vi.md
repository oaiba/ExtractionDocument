---
title: "Looting & Inventory Interactions"
type: docs
weight: 4
---

### Tổng Quan

Looting is the primary reward mechanism và the source of all risk. Every interaction với a container, a dead body, hoặc a loose item on the ground is a moment of vulnerability. The inventory hệ thống uses a grid-based "Tetris" model that forces meaningful choices about what to keep, what to drop, và what to sacrifice.

> Xem [cốt lõi Gameplay cơ chế](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/CoreGameplay/README.md) for loot container types và dynamic loot scaling formulas. This tài liệu focuses on the physical interaction design và inventory management.

***

### Container Interaction flow

#### Search Sequence

```
APPROACH CONTAINER
    |
  [Interaction Prompt Appears — "Search" / "Open"]
    |
  Activate Search
    |
  Character Animation: Kneeling, opening container
    |
  VULNERABILITY WINDOW BEGINS
  (Cannot sprint, reduced awareness, healing canceled)
    |
  Items Revealed One by One (0.5s interval per item)
    |
  Player Selects Items to Take (drag to inventory or quick-transfer)
    |
  Close Container / Walk Away
    |
  VULNERABILITY WINDOW ENDS
```

#### Container Types và Search Times

| Container                 |           Search thời gian           |        Item Count       | Noise Generated               | ghi chú                                                              |
| ------------------------- | :-----------------------------: | :---------------------: | ----------------------------- | ------------------------------------------------------------------ |
| Loose Item (ground spawn) |             Instant             |            1            | Low (pickup sound, 5m)        | No animation — grab và go                                         |
| Wooden Crate              |               2.0s              |           2-4           | Medium (lid creak, 10m)       | Most common container                                              |
| Metal Locker              |               3.0s              |           3-5           | Medium (hinge squeak, 10m)    | Buildings và offices                                              |
| vũ khí Rack               |               4.0s              |       1-2 vũ khí       | Low (vũ khí lift, 8m)         | Military areas only                                                |
| Filing Cabinet (drawers)  |  1.5s per drawer (3-4 drawers)  |      1-2 per drawer     | Low per drawer                | Can search individual drawers. Faster per-item nhưng noisy over thời gian |
| Safe                      | 8.0s (lockpick) / Instant (chính) |      4-8 high-giá trị     | High (drilling/clicking, 15m) | Lockpick animation is loud. chính cách dùng is silent                      |
| Dead người chơi Body          |               3.0s              | người chơi's full inventory | Medium (rustling, 10m)        | Full Tetris grid of địch's gear                                   |
| Supply Drop               |               5.0s              |           5-10          | Very High (crate smash, 20m)  | Map-wide announcement on drop                                      |

#### Search Interruption Rules

* **Taking damage** cancels the search animation. Items already revealed remain hiển thị rõ; items not yet revealed are hidden.
* **Sprinting away** cancels immediately. No partial penalty.
* **Being killed while looting** leaves the người chơi's body in the looting position. Their killer can access both the người chơi's inventory và the container.

***

### Grid Inventory hệ thống

#### Grid Dimensions

Capacity = **total cells** (sum of subgrids); Xem [Storage Master Database](https://github.com/oaiba/ExtractionDocument/blob/main/content/Gears/StorageGear/Storage_Master_Database.md).

| Container                   | Grid Size           | Capacity (cells)                                 |
| --------------------------- | ------------------- | ------------------------------------------------ |
| Pockets                     | 4 slots (1×4 strip) | Small items only: keys, cash, đạn stacks        |
| Tactical Rig (Light)        | 2×3                 | 6 — Magazines, medical supplies                  |
| Tactical Rig (Heavy)        | 3×4                 | 12 — Full medical loadout + grenades             |
| Backpack (Small)            | 3×3                 | 9 — Budget runs, light looting                   |
| Backpack (Medium)           | 4×4                 | 16 — Standard loadout                            |
| Backpack (Large)            | 5×5                 | 25 — Maximum capacity, heavy weight penalty      |
| Secure Container (Standard) | 2×2                 | 4 — Protected items; never lost on death         |
| Secure Container (Upgraded) | 2×3 hoặc 3×3          | 6 hoặc 9 — Progression reward for quest completion |

Full rig/backpack/secure container list, slot layouts, reload rule, và in-raid secure container restrictions: [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/Gears/StorageGear/README.md) ([Storage Master Database](https://github.com/oaiba/ExtractionDocument/blob/main/content/Gears/StorageGear/Storage_Master_Database.md), [Storage Slot Layouts](https://github.com/oaiba/ExtractionDocument/blob/main/content/Gears/StorageGear/Storage_Slot_Layouts.md), [Storage: Flat Storage & Folding](https://github.com/oaiba/ExtractionDocument/blob/main/content/Gears/StorageGear/Storage_Flat_Storage_Folding.md)).

#### Item Sizes

| Item Category       | Typical Size         | Examples                                                  |
| ------------------- | -------------------- | --------------------------------------------------------- |
| Small (1x1)         | Single slot          | đạn stack, chính, bandage, pills, loose currency           |
| Medium (1x2)        | Two horizontal slots | Magazine, syringe, splint, small barter item              |
| Large (2x2)         | Four-slot square     | Medkit (Salewa, IFAK), optic scope, radio                 |
| Long (1x3 hoặc 1x4)   | Long horizontal      | Suppressor, barrel, folded vũ khí stock                   |
| vũ khí (2x4 to 2x6) | Large horizontal     | Full vũ khí vary by size. Rifles are larger than pistols |
| Bulky (2x3)         | Six-slot rectangle   | Grizzly medkit, fuel can, heavy barter items              |

#### Rotation và Placement

* Items can be **rotated 90 degrees** (press R while dragging) to fit differently shaped gaps
* **Auto-placement**: Quick-transfer (Ctrl+Click) automatically finds the best-fit slot
* **Manual placement**: Dragging allows precise control for optimal packing

**Design Intent**: The Tetris inventory is deliberately friction-heavy. Every second spent organizing items in-raid is a second of vulnerability. người chơi who pre-plan their loadout và pack efficiently gain a survival advantage.

***

### Secure Container

The Secure Container is the single most quan trọng item in the game. Everything placed inside is **permanently protected** — even nếu the người chơi dies.

#### Container Progression

| Stage             | Size           | How to Obtain                                  |
| ----------------- | -------------- | ---------------------------------------------- |
| Starting          | 2x2 (4 slots)  | Given at account creation                      |
| Upgraded (Tier 1) | 2x3 (6 slots)  | Complete early quest chain + $50,000           |
| Upgraded (Tier 2) | 3x3 (9 slots)  | Complete mid-game quest chain + $200,000       |
| Premium (Max)     | 3x4 (12 slots) | Complete end-game quest chain (very difficult) |

#### Secure Container Rules

* **Can store**: Quest items, keys, found-in-raid barter items, small medical supplies, đạn
* **Cannot store**: Full vũ khí, body giáp, helmets, backpacks, large items
* **In-raid placement**: Items placed in the Secure Container trong khi a raid retain "found-in-raid" status ONLY nếu the người chơi successfully extracts. nếu the người chơi dies, items in the container are kept nhưng lose "found-in-raid" status (cannot be sold on flea market)
* **Pre-raid placement**: Người chơi có thể pre-load the container với keys, extra đạn, hoặc emergency medical supplies trước deploying

**Design Intent**: The Secure Container reduces the total loss on death. It ensures that even the worst possible outcome (death với zero loot) is not a complete wipe — the người chơi still retains pre-loaded container items. This prevents rage-quitting while preserving the fear of loss.

***

### Quick Transfer hệ thống

| Shortcut          | Action                            | Context                                                                               |
| ----------------- | --------------------------------- | ------------------------------------------------------------------------------------- |
| Ctrl+Click        | Quick-move item to/from container | Fastest looting method. Item goes to first available slot                             |
| Alt+Click         | Equip item instantly              | Only works nếu a matching equipment slot is empty (e.g., alt-click a vũ khí equips it) |
| Double-click      | kiểm tra item chi tiết              | Shows stats, durability, attached modifications                                       |
| Drag + R          | Rotate item 90 degrees            | Manual placement optimization                                                         |
| Discard (Del chính) | Drop item on ground               | Drops at người chơi's feet. Other Người chơi có thể pick it up                                  |

#### Cross-Platform

Grid rules, search times, và container behavior are identical on PC, console, và mobile. **Input:** PC uses drag-và-drop và shortcuts (Ctrl+Click, Alt+Click); mobile uses tap-to-transfer và optional auto-sort; console uses cursor hoặc d-pad selection. Same vulnerability window và noise rules apply. Xem [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) và [Gear cơ chế](Gear_Mechanics.md) for platform input và inventory UX.

***

### Looting Risk Design

#### Vulnerability Window Analysis

Every looting action has a chi phí measured in seconds of vulnerability:

| Action                      |     thời gian Exposed     | Risk Level | Mitigation                                        |
| --------------------------- | :------------------: | ---------- | ------------------------------------------------- |
| Pick up loose item          |         0.3s         | Very Low   | Can do while moving                               |
| Search wooden crate         |         2.0s         | Low        | Crouch behind crate for cover                     |
| Loot a dead người chơi          | 3.0s + duyệt thời gian | High       | Full inventory duyệt. Extended exposure        |
| Lockpick a safe             |         8.0s         | Very High  | Loud, stationary, confined room. Bring a teammate |
| Organize inventory mid-raid |       Variable       | Medium     | Only do behind solid cover hoặc in a locked room    |

#### Sound Generation While Looting

* **Container opening**: Audible squeak/creak (8-15m depending on type)
* **Item pickup**: Soft sound (5m)
* **Inventory movement**: Gear rustling (3m)
* **Backpack zipping**: khi closing the inventory màn hình (8m)

**Design Intent**: Looting is inherently noisy. A người chơi searching a room is broadcasting their position to anyone nearby. This tạo natural ambush opportunities và encourages buddy-hệ thống play.

***

### chính và Keycard hệ thống

#### chính Types

| chính Type     | Durability | cách dùng Case                                             | Acquisition                          |
| ------------ | :--------: | ---------------------------------------------------- | ------------------------------------ |
| Standard chính | 20-50 uses | Common locked rooms (offices, storage)               | Loot from jackets, drawers, scavs    |
| Military chính | 10-25 uses | Military-grade rooms (armories, server rooms)        | Rare loot spawn, quest reward        |
| Keycard      |  5-10 uses | High-security areas (labs, vaults, restricted zones) | Boss drop, barter trade, quest chain |
| Master chính   |    1 cách dùng   | One-thời gian access to extreme-giá trị rooms               | Legendary drop only                  |

#### Locked Room Design Philosophy

* **Every locked room must justify its chính chi phí**: The expected loot giá trị behind the door should exceed the chính's market giá trị divided by its remaining uses.
* **Risk escalation**: Higher-tier rooms are deeper inside dangerous zones. The best loot requires traversing the most hostile territory.
* **chính sharing**: A người chơi can open a door for their squad. Only the chính-holder consumes a cách dùng. This makes keys valuable team assets.

***

### Found-in-Raid Status

#### định nghĩa

An item has "Found-in-Raid" (FIR) status nếu:

1. It was picked up from a world spawn (container, loose loot, AI corpse)
2. It was crafted in the Safe House
3. It was received as a quest reward

An item does **not** have FIR status nếu:

1. It was purchased from a trader
2. It was bought on the flea market
3. It was found in-raid nhưng the người chơi died (items in secure container lose FIR status on death)

#### Why FIR Matters

| hệ thống                        |   FIR Required?  | Reason                                                      |
| ----------------------------- | :--------------: | ----------------------------------------------------------- |
| Flea Market selling           |        Yes       | Prevents mua-low-sell-high market manipulation              |
| Quest turn-ins                | Most require FIR | Forces người chơi to find items thông qua gameplay, not purchase |
| Trader barters                | Some require FIR | Encourages actual scavenging over market shortcuts          |
| Personal cách dùng (equip, consume) |        No        | Người chơi có thể always cách dùng purchased items themselves           |

**Design Intent**: The FIR hệ thống ensures that progression requires actual raid participation. người chơi cannot simply mua their way thông qua the quest line — they must engage với the cốt lõi loop.

***

### Barter Items

#### Categories

| Category         | Examples                                | primary cách dùng                                       |
| ---------------- | --------------------------------------- | ------------------------------------------------- |
| Electronics      | GPU, CPU, Circuit Board, Flash Drive    | Safe House upgrades, high-giá trị trader barters    |
| Medical Supplies | Saline, Surgical Instruments, Blood Set | Medical station crafting, quest turn-ins          |
| cơ chế Parts | Bolts, Nuts, Screws, Springs            | vũ khí crafting, Safe House construction          |
| Valuables        | Gold Chain, Rollex, Bitcoins            | Direct sale for high credit giá trị                 |
| Provisions       | Canned food, MREs, Water bottles        | Sustain Hydration/Energy in-raid, Safe House fuel |
| Functional Items | Fuel, Car Battery, Wires                | Safe House power, generator fuel                  |

#### Item Identification

* **Known items**: người chơi who have previously examined an item can identify it on sight (name và icon shown)
* **Unknown items**: First encounter shows "Unidentified \[category]" until examined (takes 2 seconds). This rewards người chơi who study the loot pool.

***

### Marketplace & người chơi Trading

> **Item Catalogue:** For all item specs, values, và grid sizes, Xem [Items & Gear](ItemsAndGear.md). This section covers the _trading mechanics_ — how items move between người chơi.

#### Face-to-Face Trading (Lobby)

Direct trades between người chơi mà không marketplace fees.

| tính năng             | chi tiết                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **khi**            | Post-raid lobby, Home màn hình — not in-raid                                               |
| **Initiation**      | Right-click người chơi nameplate → "Trade"                                                   |
| **Interface**       | Split-panel — your offer left / their offer right                                        |
| **Completion**      | Both người chơi must "Accept" simultaneously                                                |
| **Safety**          | No fee; trade window shows both sides trước confirmation                                |
| **Scam prevention** | Each người chơi sees the full trade contents; last-second changes reset both accepted trạng thái |
| **Audit log**       | Trade recorded in both người chơi' trade history (view in profile)                          |

***

#### Auction House (Flea Market)

The người chơi-driven market — the primary economic hub outside of NPC traders.

**Listing Items**

| Parameter               | Rule                                                |
| ----------------------- | --------------------------------------------------- |
| **FIR required**        | Yes — only Found-in-Raid items eligible for listing |
| **Starting bid**        | Set by seller                                       |
| **Buyout giá**        | Optional — instant-purchase giá                   |
| **Listing fee**         | 5% of starting bid (non-refundable, even nếu unsold) |
| **Duration options**    | 24h / 48h / 72h                                     |
| **Max active listings** | 5 (increases với Safe House upgrade)               |

**Bidding**

| tính năng                       | chi tiết                                              |
| ----------------------------- | --------------------------------------------------- |
| **Bid increment**             | Minimum +5% over hiện tại bid                        |
| **Auto-outbid notifications** | Push notification khi outbid                       |
| **Anti-snipe extension**      | Bids in last 60 seconds extend auction by 5 minutes |
| **Instant buyout**            | Ends auction immediately at listed buyout giá     |

**Fees**

| Fee                   |          Amount         | Paid By          | mục đích                   |
| --------------------- | :---------------------: | ---------------- | ------------------------- |
| Listing fee           |    5% of starting bid   | Seller (upfront) | Discourages spam listings |
| Sale tax              | 10% of final sale giá | Seller (on sale) | Credit sink               |
| **Total seller chi phí** |      \~15% of sale      | —                | Stabilizes economy        |

**Market Dynamics**

| Mechanism                        | chi tiết                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| **giá floors**                 | Each item has a minimum vendor-buyback giá trị — prevents complete giá crashes             |
| **giá cap**                    | Max 50% giá change per day (server-enforced) — prevents artificial spikes                |
| **Whale detection**              | Bulk purchases above 10× average volume flagged for review                                 |
| **giá history**                | 7-day giá chart hiển thị rõ on each item listing — lets người chơi assess fair market giá trị     |
| **Weekend events affect prices** | Double Loot weekends increase supply, driving prices down; Scarcity Events increase prices |

***

#### Black Market (In-Raid AI Trader)

A high-risk premium vendor concept — an AI trader that spawns in the contaminated zone trong khi late-game.

| Property          | chi tiết                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------- |
| **Activation**    | Spawns at 10:00 minute mark in contamination zone (map-wide announcement: "Vendor is open")  |
| **Location**      | Rotates between 3 preset spots per map — người chơi must find him                               |
| **Payment**       | Cash only — in-raid currency looted trong khi that raid (cannot cách dùng Credits from stash)         |
| **Inventory**     | Rotating — 4–6 items: always at least 1 Epic+ item; mix of vũ khí, giáp, stims             |
| **Risk**          | người chơi must enter contamination zone → receive damage; also known PvP hotspot               |
| **Design intent** | tạo late-game quyết định point: extract với what you have, hoặc gamble on Black Market item |

***

### Tham Chiếu Chéo

* [Items & Gear](ItemsAndGear.md) — Full item catalogue với values, grid sizes, weights, và cách dùng descriptions.
* [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/Gears/StorageGear/README.md) — Storage Master Database, Slot Layouts (reload rule, hotkeys), Flat Storage & Folding, Secure Container restrictions.
* [Loot bảng Design](Loot_Table_Design.md) — What spawns in each container type và zone; supply drop loot.
* [Gear cơ chế](Gear_Mechanics.md) — Weight encumbrance, item condition, và giáp repair.
* [Safe House Design](../GameDesign/Safe_House_Design.md) — Crafting recipes; Safe House upgrades that expand marketplace listing slots.
* [Quest & Objectives](Quest_Objective_System.md) — Quest items require FIR; some quests require buying from traders.
* [GameDesign/Economy](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Economy.md) — Macro economy design: trader tiers, credit sinks, inflation control.
* [GameDesign/Insurance hệ thống](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/InsuranceSystem.md) — Insurance pre-checkout as part of pre-raid loadout flow.
