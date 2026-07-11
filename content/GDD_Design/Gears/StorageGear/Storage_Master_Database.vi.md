---
title: "Storage Master Database"
type: docs
weight: 1
---

## Tổng Quan

This tài liệu is the **canonical list** of all storage gear: tactical rigs (unarmored và armored), backpacks, secure containers, và stash-only cases. For slot layouts và reload rule Xem [Storage Slot Layouts](storage_slot_layouts/index.html); for flat storage (no bag-in-bag) và backpack collapse Xem [Storage: Flat Storage & Folding](storage_flat_storage_folding/index.html); for balance Xem [Storage Balance Framework](storage_balance_framework/index.html) và [Stash & Container Progression](stash_container_progression/index.html).

### Grid Inventory & Subgrid Model

Storage is **grid inventory** nhưng a container can have **one hoặc more subgrids** inside. Each **subgrid** has dimensions (W×H), optional slot-type constraints (e.g. 1×1 only, hoặc allows 1×2), optional hotkey (quick-access), và a role/name (e.g. mag pouch, utility, main compartment).

- **Total capacity** = **sum of all cells in all subgrids**. This is the primary capacity number for balance, chi phí-per-slot, và capacity checks — not "width × height" of a single rectangle.
- **Tactical depth:** Where the người chơi places items (which subgrid) matters: subgrids với hotkey = quick access và reload source; other subgrids require opening inventory. Rigs với distinct mag vs utility subgrids tạo meaningful loadout choices.

---

## Tactical Rigs

Rigs are worn on the chest. **vũ khí can only reload from the tactical rig (hoặc pockets);** backpack does not count. Each rig is defined by **total capacity (cells)** và **subgrids**; exact layout in [Storage Slot Layouts](storage_slot_layouts/index.html). **Tier** per [Gear Tier hệ thống](../gear_tier_system/index.html).

### Unarmored Rigs


| Code          | Display Name  | Tier | Total capacity (cells) | Subgrids                                     | Hotkey slots | Weight (kg) | giá trị ($) | Trader | Rarity   | ghi chú                  |
| ------------- | ------------- | :--: | ---------------------- | -------------------------------------------- | ------------ | ----------- | --------- | ------ | -------- | ---------------------- |
| RIG_HARNESS   | Chest Harness | 1    | 4                      | Main 2×2 (4)                                 | 2            | 0.3         | 2,000     | 1      | Common   | Minimal; scav default  |
| RIG_LIGHT     | Light Rig     | 1    | 6                      | Main 2×3 (6)                                 | 3            | 0.4         | 5,000     | 1      | Common   | Scout/rat              |
| RIG_RECON     | Recon Vest    | 2    | 8                      | Main 2×3 (6) + Util 1×2 (2)                  | 4            | 0.45        | 8,000     | 2      | Uncommon | High ergo              |
| RIG_STANDARD  | Standard Rig  | 2    | 9                      | Main 3×2 (6) + Mag 1×3 (3)                   | 4            | 0.6         | 12,000    | 2      | Uncommon | Balanced               |
| RIG_ASSAULT   | Assault Vest  | 2    | 14                     | Main 3×3 (9) + Mag 2×1×2 (4) + Util 1×1 (1)  | 5            | 0.7         | 20,000    | 2      | Uncommon | Mag subgrid = reload   |
| RIG_HEAVY     | Heavy Rig     | 3    | 12                     | Main 3×4 (12)                                | 6            | 0.8         | 25,000    | 3      | Rare     | Chad preferred         |
| RIG_BLACKROCK | Blackrock     | 3    | 20                     | Main 3×4 (12) + Mag 2×1×2 (4) + Util 2×2 (4) | 6            | 0.9         | 35,000    | 3      | Rare     | Max capacity unarmored |


### Armored Rigs

Armored rigs provide built-in body giáp và **replace** a separate vest. giáp stats: [giáp Master Database — Armored Rigs](../ArmorGear/Armor_Master_Database.md#armored-rigs). **Tier** per [Gear Tier hệ thống](../gear_tier_system/index.html).


| Code         | Display Name          | Tier | Total capacity (cells) | Subgrids                                     | Hotkey | Weight (kg) | giáp class | giá trị ($) | Rarity   |
| ------------ | --------------------- | :--: | ---------------------- | -------------------------------------------- | ------ | ----------- | ----------- | --------- | -------- |
| RIG_ARMORED  | Armored Rig (Generic) | 2    | 12                     | Main 3×4 (12)                                | 6      | 3.5         | 3           | 45,000    | Uncommon |
| RIG_6B3TM    | 6B3TM Armored Rig     | 3    | 16                     | Main 3×4 (12) + Mag 2×2 (4)                  | 6      | 9.5         | 4           | 45,000    | Rare     |
| RIG_TV110    | Wartech TV-110        | 3    | 20                     | Main 3×4 (12) + Mag 2×1×2 (4) + Util 2×2 (4) | 6      | 8.0         | 4           | 55,000    | Rare     |
| RIG_DEFENDER | Defender 2            | 4    | 14                     | Main 3×4 (12) + Util 1×2 (2)                 | 6      | 11.0        | 5           | 95,000    | Epic     |


---

## Backpacks

Backpacks provide grid storage only; no hotkey. Contents lost on death (except as insured). **Capacity** = total cells (sum of subgrids). Grid (external) = footprint khi worn hoặc collapsed size reference; Xem [Storage: Flat Storage & Folding](storage_flat_storage_folding/index.html) (flat storage, collapse). **Tier** per [Gear Tier hệ thống](../gear_tier_system/index.html).


| Code         | Display Name      | Tier | Grid (external) | Capacity (cells) | Subgrids                      | Weight (empty) | Speed penalty | Noise radius | Collapsed size | giá trị ($) | Trader | Rarity           |
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

Unlootable; contents **kept sau death**. **Cells** = total capacity (primary number). In-raid placement restrictions apply: Xem [Storage Slot Layouts](storage_slot_layouts/index.html) và below. Unlock path: [Stash & Container Progression](Stash_Container_Progression.md#secure-container-upgrade-path). **Tier** per [Gear Tier hệ thống](../gear_tier_system/index.html).


| Code         | Display Name | Tier | Grid | Cells (total capacity) | Subgrids           | Unlock method                                 | giá trị (nếu buyable) |
| ------------ | ------------ | :--: | ---- | ---------------------- | ------------------ | --------------------------------------------- | ------------------ |
| SECURE_ALPHA | Alpha        | 1    | 2×2  | 4                      | Single compartment | Default (all editions)                        | —                  |
| SECURE_BETA  | Beta         | 2    | 2×3  | 6                      | Single compartment | Quest (e.g. Punisher line)                    | —                  |
| SECURE_GAMMA | Gamma        | 3    | 3×3  | 9                      | Single compartment | Premium edition hoặc quest (e.g. The Collector) | —                  |
| SECURE_KAPPA | Kappa        | 4    | 3×4  | 12                     | Single compartment | Quest: complete all main quests               | —                  |


### Secure container restrictions


| Action                            | In-raid | In-stash |
| --------------------------------- | ------- | -------- |
| Place keys, đạn, meds, valuables | Yes     | Yes      |
| Place vũ khí                     | **No**  | Yes      |
| Place thermal / NVG               | **No**  | Yes      |
| Place giáp / helmets             | **No**  | Yes      |
| Remove any item                   | Yes     | Yes      |


---

## Stash-Only Containers

Used only in the global Stash (not carried in-raid). **External size** = cells taken in stash; **Internal capacity (cells)** = total cells inside the container (sum of subgrids; stash-only cases are typically one internal grid). Efficiency = internal capacity ÷ external cells. **Tier** per [Gear Tier hệ thống](../gear_tier_system/index.html) (by unlock phase).


| Code              | Display Name       | Tier | External size | Internal capacity (cells) | Internal grid (ref) | Efficiency | Item restriction           | giá trị ($)  | Unlock           |
| ----------------- | ------------------ | :--: | ------------- | ------------------------- | ------------------- | ---------- | -------------------------- | ---------- | ---------------- |
| CASE_WEAPON       | vũ khí Case        | 3    | 5×5 (25)      | 50                        | 10×5 (50)           | 2:1        | vũ khí, attachments       | 600,000    | Trader 3 / quest |
| CASE_AMMO         | đạn Case          | 2    | 2×2 (4)       | 49                        | 7×7 (49)            | 12:1       | đạn, mags                 | 350,000    | Trader 2         |
| CASE_MED          | Medicine Case      | 2    | 2×2 (4)       | 35                        | 7×5 (35)            | 8.75:1     | Medical                    | 280,000    | Trader 2         |
| CASE_MAG          | Magazine Case      | 2    | 2×2 (4)       | 36                        | 6×6 (36)            | 9:1        | Magazines                  | 180,000    | Trader 2         |
| CASE_GRENADE      | Grenade Case       | 2    | 2×2 (4)       | 49                        | 7×7 (49)            | 12:1       | Grenades                   | 350,000    | Trader 2         |
| CASE_KEYTOOL      | Keytool            | 1    | 1×1 (1)       | 16                        | 4×4 (16)            | 16:1       | Keys, keycards             | 250,000    | Trader 1         |
| CASE_DOCS         | Docs Case          | 1    | 1×2 (2)       | 16                        | 4×4 (16)            | 8:1        | Keys, money, maps          | 350,000    | Trader 1         |
| CASE_ITEMS        | Items Case         | 3    | 2×2 (4)       | 64                        | 8×8 (64)            | 16:1       | Any                        | 2,500,000  | Trader 3         |
| CASE_JUNKBOX      | Lucky Scav Junkbox | 2    | 4×4 (16)      | 256                       | 16×16 (256)         | 16:1       | Barter/crafting only       | 1,200,000  | Trader 2 / craft |
| CASE_MONEY        | Money Case         | 2    | 2×2 (4)       | —                         | —                   | —          | Cash stacks (500k–50M cap) | 500,000    | Trader 2         |
| CASE_THICC_ITEMS  | THICC Items Case   | 4    | 3×3 (9)       | 196                       | 14×14 (196)         | 21.8:1     | Any                        | 18,000,000 | Trader 4 / quest |
| CASE_THICC_WEAPON | THICC vũ khí Case  | 4    | 5×5 (25)      | 120                       | 15×8 (120)          | 4.8:1      | vũ khí                    | 11,000,000 | Trader 4 / quest |


---

## Tham Chiếu Chéo

- [Gear Tier hệ thống](../gear_tier_system/index.html) — Storage Tier (1–4) định nghĩa; progression = Tier + Rarity + người chơi/trader level.
- [Storage Slot Layouts](storage_slot_layouts/index.html) — Per-rig grid diagrams, reload rule, hotkey mapping.
- [Storage: Flat Storage & Folding](storage_flat_storage_folding/index.html) — Flat storage, backpack collapse.
- [Storage Balance Framework](storage_balance_framework/index.html) — Capacity vs mobility, chi phí per slot.
- [Stash & Container Progression](stash_container_progression/index.html) — Stash size, unlock order, secure path.
- [giáp Master Database — Armored Rigs](../ArmorGear/Armor_Master_Database.md#armored-rigs) — giáp class và zones for armored rigs.
