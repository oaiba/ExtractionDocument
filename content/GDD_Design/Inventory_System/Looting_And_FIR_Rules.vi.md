---
title: "Looting Mechanics"
weight: 5
type: docs
---

### The Looting Loop

Looting is tactical. It requires looking down (loss of situational awareness) và making noise.

### 1. Interaction Logic

#### Container Types

* **Static:** vũ khí Boxes, Safes, Jackets, PCs. (Fixed positions).
* **Dynamic:** Loose items on tables/shelves. (Randomized positions).
* **Airdrops:** Random events. Smoke signal attracts all người chơi. High-tier loot.

#### The Search Process (UX)

1. **Initiate:** Press `F` on container.
2. **Searching:** A progress bar appears.
   * _Perception Skill:_ Reduces search thời gian.
   * _Experience:_ Revealed items stay revealed.
3. **Visual Feedback:** Items appear one-by-one in the UI grid.
4. **Sound Cue:** Zipper/Lid noise is broadcasted to \~30m radius. **Sound is chính.**

***

### 2. Advanced Loot Concepts

#### Locked Rooms (chính hệ thống)

Keys are physical items với durability (e.g., 25/25 uses).

* **Marked Rooms:** Cultist rooms với extremely high-giá trị loot (Keycards, Documents).
* **chính Cards:** Color-coded electronic access (Red, Blue, Green, Violet, Yellow) for high-security labs. Rare và expensive.

#### "Found In Raid" (FIR) Status

To combat Real Money Trading (RMT) và market flipping:

* **Status:** Items spawned in the raid have a generic checkmark (FIR).
* **Loss of Status:** nếu a người chơi brings an item _into_ a raid, hoặc dies với it in their Secure Container (depending on server settings), it loses FIR status.
* **Market:** Only FIR items can be sold on the Flea Market (người chơi Auction House). Non-FIR items can only be sold to NPC Traders for less money.

***

### 3. Corpse Looting & Dogtags

Looting a người chơi is the ultimate reward.

* **Dogtag:** A specialized 1-slot item on the body.
  * _Contains:_ Level, Killer Name, vũ khí Used, Distance.
  * _Value:_ Higher Level = Higher Sell giá. Can be bartered for end-game gear.
* **Weight Management:** You cannot carry everything. Choosing to take a dead địch's heavy Class 6 giáp means dropping your own hoặc moving at snail's pace. For container types, rig/backpack capacities, và secure container rules, Xem [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) và [Containers](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Inventory_System/Containers.md).

***
