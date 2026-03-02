---
title: "Looting & Inventory Interactions"
type: docs
weight: 4
---

## Overview

Looting is the primary reward mechanism and the source of all risk. Every interaction with a container, a dead body, or a loose item on the ground is a moment of vulnerability. The inventory system uses a grid-based "Tetris" model that forces meaningful choices about what to keep, what to drop, and what to sacrifice.

> See [Core Gameplay Mechanics](../../GameDesign/CoreGameplay/) for loot container types and dynamic loot scaling formulas. This document focuses on the physical interaction design and inventory management.

---

## Container Interaction Flow

### Search Sequence

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

### Container Types and Search Times

| Container | Search Time | Item Count | Noise Generated | Notes |
| :-------- | :---------: | :--------: | :-------------- | :---- |
| Loose Item (ground spawn) | Instant | 1 | Low (pickup sound, 5m) | No animation — grab and go |
| Wooden Crate | 2.0s | 2-4 | Medium (lid creak, 10m) | Most common container |
| Metal Locker | 3.0s | 3-5 | Medium (hinge squeak, 10m) | Buildings and offices |
| Weapon Rack | 4.0s | 1-2 weapons | Low (weapon lift, 8m) | Military areas only |
| Filing Cabinet (drawers) | 1.5s per drawer (3-4 drawers) | 1-2 per drawer | Low per drawer | Can search individual drawers. Faster per-item but noisy over time |
| Safe | 8.0s (lockpick) / Instant (key) | 4-8 high-value | High (drilling/clicking, 15m) | Lockpick animation is loud. Key use is silent |
| Dead Player Body | 3.0s | Player's full inventory | Medium (rustling, 10m) | Full Tetris grid of enemy's gear |
| Supply Drop | 5.0s | 5-10 | Very High (crate smash, 20m) | Map-wide announcement on drop |

<!-- REF_IMAGE: Container interaction UI mockup — split screen showing the player's inventory grid on the left and the container's contents on the right, with drag-and-drop indicators -->

### Search Interruption Rules

- **Taking damage** cancels the search animation. Items already revealed remain visible; items not yet revealed are hidden.
- **Sprinting away** cancels immediately. No partial penalty.
- **Being killed while looting** leaves the player's body in the looting position. Their killer can access both the player's inventory and the container.

---

## Grid Inventory System

### Grid Dimensions

| Container | Grid Size | Typical Capacity |
| :-------- | :------- | :--------------- |
| Pockets | 4 slots (1x4 strip) | Small items only: keys, cash, ammo stacks |
| Tactical Rig (Light) | 2x3 (6 slots) | Magazines, medical supplies |
| Tactical Rig (Heavy) | 3x4 (12 slots) | Full medical loadout + grenades |
| Backpack (Small) | 3x3 (9 slots) | Budget runs, light looting |
| Backpack (Medium) | 4x4 (16 slots) | Standard loadout |
| Backpack (Large) | 5x5 (25 slots) | Maximum capacity, heavy weight penalty |
| Secure Container (Standard) | 2x2 (4 slots) | Protected items — never lost on death |
| Secure Container (Upgraded) | 2x3 or 3x3 | Progression reward for quest completion |

Full rig/backpack/secure container list, slot layouts, reload rule, and in-raid secure container restrictions: [Gears — Storage Gear](../../Gears/StorageGear/) ([Storage Master Database](../../Gears/StorageGear/Storage_Master_Database.md), [Storage Slot Layouts](../../Gears/StorageGear/Storage_Slot_Layouts.md), [Storage Nesting & Folding](../../Gears/StorageGear/Storage_Nesting_Folding.md)).

### Item Sizes

| Item Category | Typical Size | Examples |
| :------------ | :----------- | :------- |
| Small (1x1) | Single slot | Ammo stack, key, bandage, pills, loose currency |
| Medium (1x2) | Two horizontal slots | Magazine, syringe, splint, small barter item |
| Large (2x2) | Four-slot square | Medkit (Salewa, IFAK), optic scope, radio |
| Long (1x3 or 1x4) | Long horizontal | Suppressor, barrel, folded weapon stock |
| Weapon (2x4 to 2x6) | Large horizontal | Full weapons vary by size. Rifles are larger than pistols |
| Bulky (2x3) | Six-slot rectangle | Grizzly medkit, fuel can, heavy barter items |

### Rotation and Placement

- Items can be **rotated 90 degrees** (press R while dragging) to fit differently shaped gaps
- **Auto-placement**: Quick-transfer (Ctrl+Click) automatically finds the best-fit slot
- **Manual placement**: Dragging allows precise control for optimal packing

**Design Intent**: The Tetris inventory is deliberately friction-heavy. Every second spent organizing items in-raid is a second of vulnerability. Players who pre-plan their loadout and pack efficiently gain a survival advantage.

<!-- REF_IMAGE: Inventory grid example — a well-packed backpack (5x5) showing rotated items, different sizes fitting together, with color-coded item rarity borders -->

---

## Secure Container

The Secure Container is the single most important item in the game. Everything placed inside is **permanently protected** — even if the player dies.

### Container Progression

| Stage | Size | How to Obtain |
| :---- | :--- | :------------ |
| Starting | 2x2 (4 slots) | Given at account creation |
| Upgraded (Tier 1) | 2x3 (6 slots) | Complete early quest chain + $50,000 |
| Upgraded (Tier 2) | 3x3 (9 slots) | Complete mid-game quest chain + $200,000 |
| Premium (Max) | 3x4 (12 slots) | Complete end-game quest chain (very difficult) |

### Secure Container Rules

- **Can store**: Quest items, keys, found-in-raid barter items, small medical supplies, ammo
- **Cannot store**: Full weapons, body armor, helmets, backpacks, large items
- **In-raid placement**: Items placed in the Secure Container during a raid retain "found-in-raid" status ONLY if the player successfully extracts. If the player dies, items in the container are kept but lose "found-in-raid" status (cannot be sold on flea market)
- **Pre-raid placement**: Players can pre-load the container with keys, extra ammo, or emergency medical supplies before deploying

**Design Intent**: The Secure Container reduces the total loss on death. It ensures that even the worst possible outcome (death with zero loot) is not a complete wipe — the player still retains pre-loaded container items. This prevents rage-quitting while preserving the fear of loss.

---

## Quick Transfer System

| Shortcut | Action | Context |
| :------- | :----- | :------ |
| Ctrl+Click | Quick-move item to/from container | Fastest looting method. Item goes to first available slot |
| Alt+Click | Equip item instantly | Only works if a matching equipment slot is empty (e.g., alt-click a weapon equips it) |
| Double-click | Inspect item details | Shows stats, durability, attached modifications |
| Drag + R | Rotate item 90 degrees | Manual placement optimization |
| Discard (Del key) | Drop item on ground | Drops at player's feet. Other players can pick it up |

### Cross-Platform

Grid rules, search times, and container behavior are identical on PC, console, and mobile. **Input:** PC uses drag-and-drop and shortcuts (Ctrl+Click, Alt+Click); mobile uses tap-to-transfer and optional auto-sort; console uses cursor or d-pad selection. Same vulnerability window and noise rules apply. See [Controls](../../GameDesign/Controls.md) and [Gear Mechanics](Gear_Mechanics.md) for platform input and inventory UX.

---

## Looting Risk Design

### Vulnerability Window Analysis

Every looting action has a cost measured in seconds of vulnerability:

| Action | Time Exposed | Risk Level | Mitigation |
| :----- | :----------: | :--------- | :--------- |
| Pick up loose item | 0.3s | Very Low | Can do while moving |
| Search wooden crate | 2.0s | Low | Crouch behind crate for cover |
| Loot a dead player | 3.0s + browsing time | High | Full inventory browsing. Extended exposure |
| Lockpick a safe | 8.0s | Very High | Loud, stationary, confined room. Bring a teammate |
| Organize inventory mid-raid | Variable | Medium | Only do behind solid cover or in a locked room |

### Sound Generation While Looting

- **Container opening**: Audible squeak/creak (8-15m depending on type)
- **Item pickup**: Soft sound (5m)
- **Inventory movement**: Gear rustling (3m)
- **Backpack zipping**: When closing the inventory screen (8m)

**Design Intent**: Looting is inherently noisy. A player searching a room is broadcasting their position to anyone nearby. This creates natural ambush opportunities and encourages buddy-system play.

<!-- REF_IMAGE: Looting scenario illustration — isometric view of a player crouching behind a crate while searching it, with sound radius circles showing the range enemies could hear -->

---

## Key and Keycard System

### Key Types

| Key Type | Durability | Use Case | Acquisition |
| :------- | :--------: | :------- | :---------- |
| Standard Key | 20-50 uses | Common locked rooms (offices, storage) | Loot from jackets, drawers, scavs |
| Military Key | 10-25 uses | Military-grade rooms (armories, server rooms) | Rare loot spawn, quest reward |
| Keycard | 5-10 uses | High-security areas (labs, vaults, restricted zones) | Boss drop, barter trade, quest chain |
| Master Key | 1 use | One-time access to extreme-value rooms | Legendary drop only |

### Locked Room Design Philosophy

- **Every locked room must justify its key cost**: The expected loot value behind the door should exceed the key's market value divided by its remaining uses.
- **Risk escalation**: Higher-tier rooms are deeper inside dangerous zones. The best loot requires traversing the most hostile territory.
- **Key sharing**: A player can open a door for their squad. Only the key-holder consumes a use. This makes keys valuable team assets.

---

## Found-in-Raid Status

### Definition

An item has "Found-in-Raid" (FIR) status if:
1. It was picked up from a world spawn (container, loose loot, AI corpse)
2. It was crafted in the hideout
3. It was received as a quest reward

An item does **not** have FIR status if:
1. It was purchased from a trader
2. It was bought on the flea market
3. It was found in-raid but the player died (items in secure container lose FIR status on death)

### Why FIR Matters

| System | FIR Required? | Reason |
| :----- | :-----------: | :----- |
| Flea Market selling | Yes | Prevents buy-low-sell-high market manipulation |
| Quest turn-ins | Most require FIR | Forces players to find items through gameplay, not purchase |
| Trader barters | Some require FIR | Encourages actual scavenging over market shortcuts |
| Personal use (equip, consume) | No | Players can always use purchased items themselves |

**Design Intent**: The FIR system ensures that progression requires actual raid participation. Players cannot simply buy their way through the quest line — they must engage with the core loop.

---


## Barter Items

### Categories

| Category | Examples | Primary Use |
| :------- | :------- | :---------- |
| Electronics | GPU, CPU, Circuit Board, Flash Drive | Hideout upgrades, high-value trader barters |
| Medical Supplies | Saline, Surgical Instruments, Blood Set | Medical station crafting, quest turn-ins |
| Mechanical Parts | Bolts, Nuts, Screws, Springs | Weapon crafting, hideout construction |
| Valuables | Gold Chain, Rollex, Bitcoins | Direct sale for high credit value |
| Provisions | Canned food, MREs, Water bottles | Sustain Hydration/Energy in-raid, hideout fuel |
| Functional Items | Fuel, Car Battery, Wires | Hideout power, generator fuel |

### Item Identification

- **Known items**: Players who have previously examined an item can identify it on sight (name and icon shown)
- **Unknown items**: First encounter shows "Unidentified [category]" until examined (takes 2 seconds). This rewards players who study the loot pool.

<!-- REF_IMAGE: Barter item reference grid — a visual catalog of 20-30 common barter items with their icons, names, approximate values, and primary uses listed -->

---

## Marketplace & Player Trading

> **Item Catalogue:** For all item specs, values, and grid sizes, see [Items & Gear](ItemsAndGear.md). This section covers the *trading mechanics* — how items move between players.

### Face-to-Face Trading (Lobby)

Direct trades between players without marketplace fees.

| Feature | Detail |
| :------ | :----- |
| **When** | Post-raid lobby, Home Screen — not in-raid |
| **Initiation** | Right-click player nameplate → "Trade" |
| **Interface** | Split-panel — your offer left / their offer right |
| **Completion** | Both players must "Accept" simultaneously |
| **Safety** | No fee; trade window shows both sides before confirmation |
| **Scam prevention** | Each player sees the full trade contents; last-second changes reset both accepted states |
| **Audit log** | Trade recorded in both players' trade history (view in profile) |

---

### Auction House (Flea Market)

The player-driven market — the primary economic hub outside of NPC traders.

#### Listing Items

| Parameter | Rule |
| :-------- | :--- |
| **FIR required** | Yes — only Found-in-Raid items eligible for listing |
| **Starting bid** | Set by seller |
| **Buyout price** | Optional — instant-purchase price |
| **Listing fee** | 5% of starting bid (non-refundable, even if unsold) |
| **Duration options** | 24h / 48h / 72h |
| **Max active listings** | 5 (increases with Hideout upgrade) |

#### Bidding

| Feature | Detail |
| :------ | :----- |
| **Bid increment** | Minimum +5% over current bid |
| **Auto-outbid notifications** | Push notification when outbid |
| **Anti-snipe extension** | Bids in last 60 seconds extend auction by 5 minutes |
| **Instant buyout** | Ends auction immediately at listed buyout price |

#### Fees

| Fee | Amount | Paid By | Purpose |
| :-- | :----: | :------ | :------ |
| Listing fee | 5% of starting bid | Seller (upfront) | Discourages spam listings |
| Sale tax | 10% of final sale price | Seller (on sale) | Credit sink |
| **Total seller cost** | ~15% of sale | — | Stabilizes economy |

#### Market Dynamics

| Mechanism | Detail |
| :-------- | :----- |
| **Price floors** | Each item has a minimum vendor-buyback value — prevents complete price crashes |
| **Price cap** | Max 50% price change per day (server-enforced) — prevents artificial spikes |
| **Whale detection** | Bulk purchases above 10× average volume flagged for review |
| **Price history** | 7-day price chart visible on each item listing — lets players assess fair market value |
| **Weekend events affect prices** | Double Loot weekends increase supply, driving prices down; Scarcity Events increase prices |

---

### Black Market (In-Raid AI Trader)

A high-risk premium vendor concept — an AI trader that spawns in the contaminated zone during late-game.

| Property | Detail |
| :------- | :----- |
| **Activation** | Spawns at 10:00 minute mark in contamination zone (map-wide announcement: "Vendor is open") |
| **Location** | Rotates between 3 preset spots per map — players must find him |
| **Payment** | Cash only — in-raid currency looted during that raid (cannot use Credits from stash) |
| **Inventory** | Rotating — 4–6 items: always at least 1 Epic+ item; mix of weapons, armor, stims |
| **Risk** | Players must enter contamination zone → receive damage; also known PvP hotspot |
| **Design intent** | Creates late-game decision point: extract with what you have, or gamble on Black Market item |

---

## Cross-References

- [Items & Gear](ItemsAndGear.md) — Full item catalogue with values, grid sizes, weights, and use descriptions.
- [Gears — Storage Gear](../../Gears/StorageGear/) — Storage Master Database, Slot Layouts (reload rule, hotkeys), Nesting & Folding, Secure Container restrictions.
- [Loot Table Design](Loot_Table_Design.md) — What spawns in each container type and zone; supply drop loot.
- [Gear Mechanics](Gear_Mechanics.md) — Weight encumbrance, item condition, and armor repair.
- [Hideout & Crafting](Hideout_Crafting.md) — Crafting recipes; Hideout upgrades that expand marketplace listing slots.
- [Quest & Objectives](Quest_Objective_System.md) — Quest items require FIR; some quests require buying from traders.
- [GameDesign/Economy](../../GameDesign/Economy.md) — Macro economy design: trader tiers, credit sinks, inflation control.
- [GameDesign/Insurance System](../../GameDesign/InsuranceSystem.md) — Insurance pre-checkout as part of pre-raid loadout flow.

