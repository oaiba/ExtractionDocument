---
title: Containers & Storage
weight: 2
type: docs
---


### Overview

Managing space is a core gameplay loop. Containers grant the ability to carry loot, but come with movement penalties and ergonomic downsides. **Full item lists, grid layouts, and balance:** [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) and [Storage Master Database](../gears/storagegear/storage_master_database/index.html).

***

### 1. Backpacks

Primary method of bulk transport. Grid size and capacity scale from small (e.g. 2×3, 6 cells) to raid-sized (e.g. 5×6–6×8, 30–48 cells). Capacity = total cells; see [Storage Master Database](../gears/storagegear/storage_master_database/index.html). Larger bags add speed penalty and noise. **Quick Drop:** Double-tap (e.g. Z) drops backpack to regain combat speed. **Flat storage:** Bags, rigs, and other items are stored as normal items in a single grid; no bag-in-bag. Empty backpacks can be collapsed. See [Storage: Flat Storage & Folding](../gears/storagegear/storage_flat_storage_folding/index.html).

***

### 2. Tactical Rigs (Vests)

Worn on the chest. The **only** container from which weapons can **reload** magazines. Slot layouts vary: 1×1 (grenades, meds), 1×2 (magazines), 2×2 (drums, large meds), 1×3 (extended mags). Types: **Recon** (small, light), **Assault** (balanced), **Heavy** (high capacity), **Armored** (built-in armor; see [Gears — Armor Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/ArmorGear/README.md)). Layouts and hotkey mapping: [Storage Slot Layouts](../gears/storagegear/storage_slot_layouts/index.html).

***

### 3. Secure Containers

Unlootable; contents **kept after death**. Sizes from Alpha (2×2) to Gamma/Kappa (3×3 / 3×4). **In-raid restrictions:** Cannot place guns, thermal scopes, or night vision inside during raid. Can place keys, meds, ammo, valuables. Can always remove items. Upgrade path: [Stash & Container Progression](../gears/storagegear/stash_container_progression/index.html).

***

### 4. Storage Cases (Stash Only)

Specialized containers for the global Stash (not carried in-raid): Weapon Case, Money Case, Medcase, Ammo Case, Magazine Case, Grenade Case, Keytool, Docs Case, THICC Items/Weapon Cases. External vs internal size and item-type restrictions: [Storage Master Database — Stash-Only Containers](../Gears/StorageGear/Storage_Master_Database.md#stash-only-containers) and [Stash & Container Progression](../gears/storagegear/stash_container_progression/index.html).
