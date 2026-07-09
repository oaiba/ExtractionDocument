---
title: "Containers & Storage"
weight: 2
type: docs
---

### Tổng Quan

Managing space is a cốt lõi gameplay loop. Containers grant the ability to carry loot, nhưng come với movement penalties và ergonomic downsides. **Full item lists, grid layouts, và balance:** [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) và [Storage Master Database](../Gears/StorageGear/Storage_Master_Database.md).

***

### 1. Backpacks

primary method of bulk transport. Grid size và capacity scale from small (e.g. 2×3, 6 cells) to raid-sized (e.g. 5×6–6×8, 30–48 cells). Capacity = total cells; Xem [Storage Master Database](../Gears/StorageGear/Storage_Master_Database.md). Larger bags add speed penalty và noise. **Quick Drop:** Double-tap (e.g. Z) drops backpack to regain combat speed. **Flat storage:** Bags, rigs, và other items are stored as normal items in a single grid; no bag-in-bag. empty backpacks can be collapsed. Xem [Storage: Flat Storage & Folding](../Gears/StorageGear/Storage_Flat_Storage_Folding.md).

***

### 2. Tactical Rigs (Vests)

Worn on the chest. The **only** container from which vũ khí can **reload** magazines. Slot layouts vary: 1×1 (grenades, meds), 1×2 (magazines), 2×2 (drums, large meds), 1×3 (extended mags). Types: **Recon** (small, light), **Assault** (balanced), **Heavy** (high capacity), **Armored** (built-in giáp; Xem [Gears — giáp Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/ArmorGear/README.md)). Layouts và hotkey mapping: [Storage Slot Layouts](../Gears/StorageGear/Storage_Slot_Layouts.md).

***

### 3. Secure Containers

Unlootable; contents **kept sau death**. Sizes from Alpha (2×2) to Gamma/Kappa (3×3 / 3×4). **In-raid restrictions:** Cannot place guns, thermal scopes, hoặc night vision inside trong khi raid. Can place keys, meds, đạn, valuables. Can always remove items. upgrade path: [Stash & Container Progression](../Gears/StorageGear/Stash_Container_Progression.md).

***

### 4. Storage Cases (Stash Only)

Specialized containers for the global Stash (not carried in-raid): vũ khí Case, Money Case, Medcase, đạn Case, Magazine Case, Grenade Case, Keytool, Docs Case, THICC Items/vũ khí Cases. External vs internal size và item-type restrictions: [Storage Master Database — Stash-Only Containers](../Gears/StorageGear/Storage_Master_Database.md#stash-only-containers) và [Stash & Container Progression](../Gears/StorageGear/Stash_Container_Progression.md).
