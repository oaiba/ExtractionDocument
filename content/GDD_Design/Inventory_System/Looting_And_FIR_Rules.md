---
title: "Looting Mechanics"
weight: 5
type: docs
---

## The Looting Loop

Looting is tactical. It requires looking down (loss of situational awareness) and making noise.

## 1. Interaction Logic

### Container Types
*   **Static:** Weapon Boxes, Safes, Jackets, PCs. (Fixed positions).
*   **Dynamic:** Loose items on tables/shelves. (Randomized positions).
*   **Airdrops:** Random events. Smoke signal attracts all players. High-tier loot.

### The Search Process (UX)
1.  **Initiate:** Press `F` on container.
2.  **Searching:** A progress bar appears.
    *   *Perception Skill:* Reduces search time.
    *   *Experience:* Revealed items stay revealed.
3.  **Visual Feedback:** Items appear one-by-one in the UI grid.
4.  **Sound Cue:** Zipper/Lid noise is broadcasted to ~30m radius. **Sound is key.**

---

## 2. Advanced Loot Concepts

### Locked Rooms (Key System)
Keys are physical items with durability (e.g., 25/25 uses).
*   **Marked Rooms:** Cultist rooms with extremely high-value loot (Keycards, Documents).
*   **Key Cards:** Color-coded electronic access (Red, Blue, Green, Violet, Yellow) for high-security labs. Rare and expensive.

### "Found In Raid" (FIR) Status
To combat Real Money Trading (RMT) and market flipping:
*   **Status:** Items spawned in the raid have a generic checkmark (FIR).
*   **Loss of Status:** If a player brings an item *into* a raid, or dies with it in their Secure Container (depending on server settings), it loses FIR status.
*   **Market:** Only FIR items can be sold on the Flea Market (Player Auction House). Non-FIR items can only be sold to NPC Traders for less money.

---

## 3. Corpse Looting & Dogtags

Looting a player is the ultimate reward.
*   **Dogtag:** A specialized 1-slot item on the body.
    *   *Contains:* Level, Killer Name, Weapon Used, Distance.
    *   *Value:* Higher Level = Higher Sell Price. Can be bartered for end-game gear.
*   **Weight Management:** You cannot carry everything. Choosing to take a dead enemy's heavy Class 6 Armor means dropping your own or moving at snail's pace. For container types, rig/backpack capacities, and secure container rules, see [Gears — Storage Gear](../Gears/StorageGear/) and [Containers](Containers.md).

---