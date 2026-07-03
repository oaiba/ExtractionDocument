---
title: "Storage Master Database"
type: docs
weight: 1
---

## Overview

This document is the **canonical list** of all storage gear: tactical rigs (unarmored and armored), backpacks, secure containers, and stash-only cases. For slot layouts and reload rule see [Storage Slot Layouts](Storage_Slot_Layouts.md); for flat storage (no bag-in-bag) and backpack collapse see [Storage: Flat Storage & Folding](Storage_Flat_Storage_Folding.md); for balance see [Storage Balance Framework](Storage_Balance_Framework.md) and [Stash & Container Progression](Stash_Container_Progression.md).

### Grid Inventory & Subgrid Model

Storage is **grid inventory** but a container can have **one or more subgrids** inside. Each **subgrid** has dimensions (W×H), optional slot-type constraints (e.g. 1×1 only, or allows 1×2), optional hotkey (quick-access), and a role/name (e.g. mag pouch, utility, main compartment).

- **Total capacity** = **sum of all cells in all subgrids**. This is the primary capacity number for balance, cost-per-slot, and capacity checks — not "width × height" of a single rectangle.
- **Tactical depth:** Where the player places items (which subgrid) matters: subgrids with hotkey = quick access and reload source; other subgrids require opening inventory. Rigs with distinct mag vs utility subgrids create meaningful loadout choices.

---

## Tactical Rigs

Rigs are worn on the chest. **Weapons can only reload from the tactical rig (or pockets);** backpack does not count. Each rig is defined by **total capacity (cells)** and **subgrids**; exact layout in [Storage Slot Layouts](Storage_Slot_Layouts.md). **Tier** per [Gear Tier System](../Gear_Tier_System.md).

### Unarmored Rigs


| Code          | Display Name  | Tier | Total capacity (cells) | Subgrids                                     | Hotkey slots | Weight (kg) | Value ($) | Trader | Rarity   | Notes                  |
| ------------- | ------------- | :--: | ---------------------- | -------------------------------------------- | ------------ | ----------- | --------- | ------ | -------- | ---------------------- |
| RIG_HARNESS   | Chest Harness | 1    | 4                      | Main 2×2 (4)                                 | 2            | 0.3         | 2,000     | 1      | Common   | Minimal; scav default  |
| RIG_LIGHT     | Light Rig     | 1    | 6                      | Main 2×3 (6)                                 | 3            | 0.4         | 5,000     | 1      | Common   | Scout/rat              |
| RIG_RECON     | Recon Vest    | 2    | 8                      | Main 2×3 (6) + Util 1×2 (2)                  | 4            | 0.45        | 8,000     | 2      | Uncommon | High ergo              |
| RIG_STANDARD  | Standard Rig  | 2    | 9                      | Main 3×2 (6) + Mag 1×3 (3)                   | 4            | 0.6         | 12,000    | 2      | Uncommon | Balanced               |
| RIG_ASSAULT   | Assault Vest  | 2    | 14                     | Main 3×3 (9) + Mag 2×1×2 (4) + Util 1×1 (1)  | 5            | 0.7         | 20,000    | 2      | Uncommon | Mag subgrid = reload   |
| RIG_HEAVY     | Heavy Rig     | 3    | 12                     | Main 3×4 (12)                                | 6            | 0.8         | 25,000    | 3      | Rare     | Chad preferred         |
| RIG_BLACKROCK | Blackrock     | 3    | 20                     | Main 3×4 (12) + Mag 2×1×2 (4) + Util 2×2 (4) | 6            | 0.9         | 35,000    | 3      | Rare     | Max capacity unarmored |


### Armored Rigs

Armored rigs provide built-in body armor and **replace** a separate vest. Armor stats: [Armor Master Database — Armored Rigs](../ArmorGear/Armor_Master_Database.md#armored-rigs). **Tier** per [Gear Tier System](../Gear_Tier_System.md).


| Code         | Display Name          | Tier | Total capacity (cells) | Subgrids                                     | Hotkey | Weight (kg) | Armor class | Value ($) | Rarity   |
| ------------ | --------------------- | :--: | ---------------------- | -------------------------------------------- | ------ | ----------- | ----------- | --------- | -------- |
| RIG_ARMORED  | Armored Rig (Generic) | 2    | 12                     | Main 3×4 (12)                                | 6      | 3.5         | 3           | 45,000    | Uncommon |
| RIG_6B3TM    | 6B3TM Armored Rig     | 3    | 16                     | Main 3×4 (12) + Mag 2×2 (4)                  | 6      | 9.5         | 4           | 45,000    | Rare     |
| RIG_TV110    | Wartech TV-110        | 3    | 20                     | Main 3×4 (12) + Mag 2×1×2 (4) + Util 2×2 (4) | 6      | 8.0         | 4           | 55,000    | Rare     |
| RIG_DEFENDER | Defender 2            | 4    | 14                     | Main 3×4 (12) + Util 1×2 (2)                 | 6      | 11.0        | 5           | 95,000    | Epic     |


---

## Backpacks

Backpacks provide grid storage only; no hotkey. Contents lost on death (except as insured). **Capacity** = total cells (sum of subgrids). Grid (external) = footprint when worn or collapsed size reference; see [Storage: Flat Storage & Folding](Storage_Flat_Storage_Folding.md) (flat storage, collapse). **Tier** per [Gear Tier System](../Gear_Tier_System.md).


| Code         | Display Name      | Tier | Grid (external) | Capacity (cells) | Subgrids                      | Weight (empty) | Speed penalty | Noise radius | Collapsed size | Value ($) | Trader | Rarity           |
| ------------ | ----------------- | :--: | --------------- | ---------------- | ----------------------------- | -------------- | ------------- | ------------ | -------------- | --------- | ------ | ---------------- |
| BAG_SLING    | Sling Bag         | 1    | 2×3             | 6                | Single 2×3 (6)                | 0.3 kg         | 0%            | —            | 1×2            | 1,500     | 1      | Common           |
| BAG_SMALL    | Small Backpack    | 1    | 3×3             | 9                | Single 3×3 (9)                | 0.5 kg         | 0%            | —            | 2×2            | 4,000     | 1      | Common           |
| BAG_BERKUT   | Berkut / Scav BP  | 2    | 4×5             | 20               | Main 4×4 (16) + Front 2×2 (4) | 0.8 kg         | −3%           | 5 m          | 3×3            | 12,000    | 2      | Uncommon         |
| BAG_MEDIUM   | Medium Backpack   | 2    | 4×4             | 16               | Single 4×4 (16)               | 1.0 kg         | −2%           | 8 m          | 3×2            | 10,000    | 2      | Uncommon         |
| BAG_LARGE    | Large Backpack    | 3    | 5×5             | 25               | Single 5×5 (25)               | 2.0 kg         | −5%           | 12 m         | 3×3            | 22,000    | 3      | Rare             |
| BAG_TRIZIP   | Tri-Zip           | 3    | 5×6             | 30               | Single 5×6 (30)               | 2.2 kg         | −10%          | 12 m         | 4×3            | 35,000    | 3      | Rare             |
| BAG_TACTICAL | Tactical Backpack | 4    | 5×6             | 30               | Single 5×6 (30)               | 2.0 kg         | −5%           | 10 m         | 3×3            | 10,000    | 2      | Epic (catalogue) |
| BAG_RAID     | Raid Backpack     | 3    | 5×6             | 30               | Single 5×6 (30)               | 2.5 kg         | −8%           | 15 m         | 4×3            | 40,000    | 3      | Rare             |
| BAG_PILGRIM  | Pilgrim           | 4    | 6×7             | 42               | Single 6×7 (42)               | 3.0 kg         | −12%          | 18 m         | 4×4            | 55,000    | 4      | Epic             |


---

## Secure Containers

Unlootable; contents **kept after death**. **Cells** = total capacity (primary number). In-raid placement restrictions apply: see [Storage Slot Layouts](Storage_Slot_Layouts.md) and below. Unlock path: [Stash & Container Progression](Stash_Container_Progression.md#secure-container-upgrade-path). **Tier** per [Gear Tier System](../Gear_Tier_System.md).


| Code         | Display Name | Tier | Grid | Cells (total capacity) | Subgrids           | Unlock method                                 | Value (if buyable) |
| ------------ | ------------ | :--: | ---- | ---------------------- | ------------------ | --------------------------------------------- | ------------------ |
| SECURE_ALPHA | Alpha        | 1    | 2×2  | 4                      | Single compartment | Default (all editions)                        | —                  |
| SECURE_BETA  | Beta         | 2    | 2×3  | 6                      | Single compartment | Quest (e.g. Punisher line)                    | —                  |
| SECURE_GAMMA | Gamma        | 3    | 3×3  | 9                      | Single compartment | Premium edition OR quest (e.g. The Collector) | —                  |
| SECURE_KAPPA | Kappa        | 4    | 3×4  | 12                     | Single compartment | Quest: complete all main quests               | —                  |


### Secure container restrictions


| Action                            | In-raid | In-stash |
| --------------------------------- | ------- | -------- |
| Place keys, ammo, meds, valuables | Yes     | Yes      |
| Place weapons                     | **No**  | Yes      |
| Place thermal / NVG               | **No**  | Yes      |
| Place armor / helmets             | **No**  | Yes      |
| Remove any item                   | Yes     | Yes      |


---

## Stash-Only Containers

Used only in the global Stash (not carried in-raid). **External size** = cells taken in stash; **Internal capacity (cells)** = total cells inside the container (sum of subgrids; stash-only cases are typically one internal grid). Efficiency = internal capacity ÷ external cells. **Tier** per [Gear Tier System](../Gear_Tier_System.md) (by unlock phase).


| Code              | Display Name       | Tier | External size | Internal capacity (cells) | Internal grid (ref) | Efficiency | Item restriction           | Value ($)  | Unlock           |
| ----------------- | ------------------ | :--: | ------------- | ------------------------- | ------------------- | ---------- | -------------------------- | ---------- | ---------------- |
| CASE_WEAPON       | Weapon Case        | 3    | 5×5 (25)      | 50                        | 10×5 (50)           | 2:1        | Weapons, attachments       | 600,000    | Trader 3 / quest |
| CASE_AMMO         | Ammo Case          | 2    | 2×2 (4)       | 49                        | 7×7 (49)            | 12:1       | Ammo, mags                 | 350,000    | Trader 2         |
| CASE_MED          | Medicine Case      | 2    | 2×2 (4)       | 35                        | 7×5 (35)            | 8.75:1     | Medical                    | 280,000    | Trader 2         |
| CASE_MAG          | Magazine Case      | 2    | 2×2 (4)       | 36                        | 6×6 (36)            | 9:1        | Magazines                  | 180,000    | Trader 2         |
| CASE_GRENADE      | Grenade Case       | 2    | 2×2 (4)       | 49                        | 7×7 (49)            | 12:1       | Grenades                   | 350,000    | Trader 2         |
| CASE_KEYTOOL      | Keytool            | 1    | 1×1 (1)       | 16                        | 4×4 (16)            | 16:1       | Keys, keycards             | 250,000    | Trader 1         |
| CASE_DOCS         | Docs Case          | 1    | 1×2 (2)       | 16                        | 4×4 (16)            | 8:1        | Keys, money, maps          | 350,000    | Trader 1         |
| CASE_ITEMS        | Items Case         | 3    | 2×2 (4)       | 64                        | 8×8 (64)            | 16:1       | Any                        | 2,500,000  | Trader 3         |
| CASE_JUNKBOX      | Lucky Scav Junkbox | 2    | 4×4 (16)      | 256                       | 16×16 (256)         | 16:1       | Barter/crafting only       | 1,200,000  | Trader 2 / craft |
| CASE_MONEY        | Money Case         | 2    | 2×2 (4)       | —                         | —                   | —          | Cash stacks (500k–50M cap) | 500,000    | Trader 2         |
| CASE_THICC_ITEMS  | THICC Items Case   | 4    | 3×3 (9)       | 196                       | 14×14 (196)         | 21.8:1     | Any                        | 18,000,000 | Trader 4 / quest |
| CASE_THICC_WEAPON | THICC Weapon Case  | 4    | 5×5 (25)      | 120                       | 15×8 (120)          | 4.8:1      | Weapons                    | 11,000,000 | Trader 4 / quest |


---

## Cross-References

- [Gear Tier System](../Gear_Tier_System.md) — Storage Tier (1–4) definition; progression = Tier + Rarity + player/trader level.
- [Storage Slot Layouts](Storage_Slot_Layouts.md) — Per-rig grid diagrams, reload rule, hotkey mapping.
- [Storage: Flat Storage & Folding](Storage_Flat_Storage_Folding.md) — Flat storage, backpack collapse.
- [Storage Balance Framework](Storage_Balance_Framework.md) — Capacity vs mobility, cost per slot.
- [Stash & Container Progression](Stash_Container_Progression.md) — Stash size, unlock order, secure path.
- [Armor Master Database — Armored Rigs](../ArmorGear/Armor_Master_Database.md#armored-rigs) — Armor class and zones for armored rigs.

