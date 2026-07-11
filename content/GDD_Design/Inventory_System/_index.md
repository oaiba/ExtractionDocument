---
title: Inventory System — Core Mechanics
linkTitle: Inventory System
type: docs
weight: 60
version: 2.1
last_updated: 2026-03-04T00:00:00.000Z
---


> **Document Status**: Living Document - Updated Regularly\
> **Target Platform**: PC (Primary), Console (Secondary)\
> **Reference Games**: Escape from Tarkov, Arena Breakout: Infinite, Delta Force, Hunt: Showdown 1896, Gray Zone Warfare

***

### Scope: Inventory vs Gears

**Gears** ([../gears/](https://github.com/oaiba/extractiondocument/blob/main/content/gdd_design/gears/readme/index.html)) = physical equipment the Operator **wears or carries** in-raid: body armor, helmets, tactical rigs, backpacks, secure containers. All armor and storage **specs** (classes, materials, slot layouts, balance) live under **Gears/ArmorGear** and **Gears/StorageGear**.

**Inventory\_System** (this section) = **general inventory system**: grid mechanics, paper doll, equipment slots, encumbrance overview, looting UX. Later expansion may add: Vehicle\_Inventory, Global\_Stash\_System, Crate\_System, etc.

***

### Executive Summary

Inventory & Gear design centers on **meaningful choices**, **spatial puzzle-solving**, and **risk-reward balance**. Key differentiators: Tetris-style grid with rotation, weight-based movement penalties, zone-based armor (see Gears), tactical accessibility (rig = reload source), and economic risk (lose gear on death).

***

### Inventory System Model

The inventory model defines how physical items exist across world loot, stash, loadout, containers, traders, rewards, and post-raid transfer. It is intentionally separate from Commerce entitlements: paid cosmetic ownership can unlock presentation, but combat gear power remains physical, earned, found, crafted, traded, or quest-granted.

| Entity | Definition | UI / Design Requirement |
| ------ | ---------- | ----------------------- |
| `Item` | Any player-visible object that can be inspected, moved, equipped, consumed, sold, turned in, or granted | Always has a category, display name, footprint or slot rule, value context, and allowed actions |
| `ItemTemplate` | Static data shared by all copies of an item | Defines category, base weight, footprint, max durability, rarity, tier, tags, valid containers, valid slots |
| `ItemInstance` | A specific owned or world-spawned copy of an item | Carries durability, ammo count, FIR, insurance, ownership, lock, attachment, and location state |
| `Container` | A parent space that can hold item instances | Defines grid size, allowed categories, nesting rules, access speed, and persistence |
| `Slot` | A loadout or container position with restrictions | Names accepted item categories, required/optional status, hotkey behavior, and validation blockers |
| `Stack` | Multiple countable items represented by one instance | Shows current count, max count, split/merge rules, and cap behavior |
| `Attachment` | Item instance mounted to another item | Must preserve compatibility, stats delta, durability/ammo where relevant, and parent item identity |
| `OwnershipState` | Relationship between player/account and an item/entitlement | Distinguishes physical ownership, entitlement unlock, temporary grant, lost item, and pending sync |
| `PlacementState` | Validity of an item position or move | Shows valid, invalid, blocked, rotate-needed, no-space, category-restricted, or server-pending |
| `ItemFlag` | A visible state modifier on an item instance | Includes FIR, quest, protected, insured, contraband, locked, equipped, damaged, broken, favorited |

### Item Taxonomy

| Category | Examples | Core Rules |
| -------- | -------- | ---------- |
| Weapons | Primary, sidearm, melee | Physical combat items; never granted directly by premium purchase |
| Armor | Body armor, helmets, visors, armored rigs | Durability, zones, class, material, repairability, weight all matter |
| Headsets | Audio profile gear | Compared by audio profile and availability, not armor class |
| Storage gear | Tactical rigs, backpacks, secure containers, stash cases | Defines capacity, access, mobility cost, restrictions, and persistence |
| Ammunition | Loose ammo and boxed ammo | Stackable; caliber compatibility must be explicit |
| Magazines | Loaded or empty mags | Holds ammo count and caliber/weapon compatibility |
| Medical | Bandage, medkit, surgery, stim | Can be hotkeyed if in valid accessible storage |
| Survival | Food, water, tools, utility | May interact with energy, hydration, crafting, or quest requirements |
| Keys | Physical keys, cards, access devices | Quest/location relevance and secure-container rules must be visible |
| Quest items | Delivery, proof, intel, marked items | FIR and turn-in requirements take priority over sell/discard actions |
| Crafting materials | Components, tools, barter items | Show recipe/trader relevance and stack/space behavior |
| Valuables | Sellable loot, rare tech, trophies | Show value-per-cell and quest/trader relevance before bulk sell |
| Cosmetics / entitlements | Skins, charms, banners, profile items | Account unlocks; do not become combat-power physical gear instances |

### Ownership vs Entitlement Rules

| Concept | Meaning | Rule |
| ------- | ------- | ---- |
| Owned item instance | A physical item in stash, loadout, world, trader transaction, reward inbox, or overflow | Can be lost, damaged, moved, insured, sold, crafted, turned in, or destroyed according to item rules |
| Entitlement | Account-level unlock from Commerce, redeem, event, support, battle pass, or achievement | Unlocks cosmetic/profile/service access; does not create paid combat-power gear |
| Cosmetic application | Visual override or account presentation applied to a compatible item/operator/profile | Must not change hitbox, recoil, audio readability, visibility advantage, or armor/storage stats |
| Temporary grant | Support/event/compensation item or reward not yet claimed | Must show source, expiry, claim destination, and duplicate/overflow handling |
| Pending sync | Item or entitlement waiting for backend confirmation | UI must prevent duplicate claim/sell/equip actions until state is final |

### Item Lifecycle

```
spawned -> discovered/examined -> looted -> found-in-raid -> extracted -> stashed
   -> equipped -> insured -> damaged -> repaired
   -> traded / sold / crafted / turned-in / consumed
   -> lost / destroyed / expired / converted
```

| Lifecycle Step | Requirement |
| -------------- | ----------- |
| Spawned / discovered | Unknown items may show placeholder until examined; reveal must not break grid layout |
| Looted / FIR | FIR state is attached to the item instance and must survive transfer until consumed by a rule |
| Extracted / stashed | Post-raid transfer must preserve item flags, attachments, durability, stack count, and container parent |
| Equipped | Slot validation and loadout risk summary update immediately |
| Insured | Eligible items show insured provider/rule; ineligible items show reason |
| Damaged / repaired | Current and max durability are preserved; repair previews cost and max durability loss |
| Traded / sold / crafted / turned-in | Destructive or irreversible actions show item name, flags, value, and consequence |
| Lost / destroyed / expired / converted | Result state must explain why the item left ownership and whether support/reward inbox applies |

### Item State Matrix

| State | Meaning | Required UI Behavior |
| ----- | ------- | -------------------- |
| Locked | Player cannot use/move/sell/equip due to rule | Show exact lock reason and unlock route |
| Protected | Player intentionally protected the item from bulk sell/discard | Exclude from bulk destructive actions by default |
| Insured | Item is covered by insurance rules | Show provider/rule, return window, and ineligible modes |
| Uninsured | Eligible item has no insurance | Warn in loadout when value threshold is high |
| Contraband | Item has restricted trade/deploy/insurance behavior | Show readable restriction before equip, sell, or queue |
| FIR | Item was found in raid and extracted under valid rules | Badge must be text-supported and visible in stash, trader, quest, and AAR |
| Quest-critical | Item is required by an active/nearby quest | Sell/discard/turn-in actions must explain consequence |
| Equipped | Item is currently in loadout | Bulk stash actions must not move/sell without confirmation |
| Damaged | Durability below ideal state | Show repair route and effect on combat/storage value |
| Broken | Below usable threshold | Block deploy/equip if required by loadout rule |
| Stacked / split | Countable item grouped or separated | Split/merge must preserve caps, flags, and valid containers |
| Overflow | Item exists outside normal stash capacity | Require resolution path before risky exits if design requires |
| Pending sync | Awaiting server confirmation | Disable duplicate destructive/claim actions and show finalizing state |

### Stash IA Model

| Surface | Owns | Required Behavior |
| ------- | ---- | ----------------- |
| Persistent stash | Long-term item storage | Shows capacity, value, filters, search, protected item count, and overflow status |
| Equipment slots | Loadout-bound items | Mirrors loadout validity and prevents accidental movement of equipped items |
| Cases / containers | Organized sub-storage | Shows category restrictions, capacity, nesting/flat-storage rules, and valid targets |
| Filter rail | Fast item discovery | Supports category, rarity/tier, FIR, quest, protected, insured, contraband, damaged, value |
| Search | Direct retrieval | Searches name, category, caliber, quest tag, trader relevance, and container contents |
| Capacity summary | Stash health | Shows used/total cells, incoming overflow, large-item pressure, and suggested fixes |
| Overflow lane | Items waiting for player resolution | Preserves reward/AAR/support source and blocks duplicate claim |
| Destructive action bar | Sell/discard/turn-in/craft decisions | Shows protected/quest/high-value/insured/contraband warnings before commit |

### Inventory QA Checklist

- [ ] Every item move has a server-valid placement state: valid, invalid, blocked, rotate-needed, no-space, or pending.
- [ ] Item instance state cannot duplicate or desync across stash, loadout, reward inbox, trader, and post-raid transfer.
- [ ] Ownership and entitlement are visibly separate; paid cosmetic entitlement never grants combat-power item instances.
- [ ] FIR, quest, protected, insured, contraband, damaged, broken, equipped, and pending states have readable labels.
- [ ] Sell, discard, craft, turn-in, overwrite, and bulk actions confirm protected, quest, high-value, insured, or contraband items.
- [ ] Full stash, overflow, filter-empty, invalid placement, pending sync, and missing capacity states show direct next actions.
- [ ] Controller and touch users can move, rotate, split, inspect, and confirm items without precision-only interaction.

***

### 1. Design Philosophy & Core Pillars

#### 1.1 Core Design Pillars

**Pillar 1: Spatial Puzzle Management** — Inventory space is a physical constraint; items have dimensions (1×1 bandage vs 4×2 rifle); rotation (90°) enables creative packing. Goal: satisfying "Tetris moments."

**Pillar 2: Weight Has Consequences** — Every item has mass; overburdening causes stamina, speed, and inertia penalties. Goal: armor vs mobility, loot vs escape trade-offs.

**Pillar 3: Risk-Reward Economics** — High-tier gear increases survival but amplifies loss on death; insurance and secure container soften the loop. Goal: "gearing fear" and "loot excitement."

**Pillar 4: Tactical Ergonomics** — Where items are stored matters: magazines in rig = quick reload; in backpack = must open inventory. Goal: reward preparation, punish poor loadout planning.

#### 1.2 Player Experience Goals

* **New players:** Gradual introduction, simple starter loadouts, clear feedback for weight/space.
* **Veterans:** Min-max space/weight, value-per-slot meta, speed-looting keybinds.
* **Emotional beats:** Tension (limited space), satisfaction (perfect pack), fear (overweight extract), loss (death), triumph (full inventory extract).

***

### 2. The Character Loadout System (Paper Doll)

#### 2.1 Primary Interface

Pre-raid screen: 3D character model (rotatable), equipment slots around model, real-time stats (armor rating, weight, movement speed), durability indicators.

#### 2.2 Equipment Slots

| Slot Name            | Grid Size | Hotkey        | Durability | Notes                                                                                                                                                                                                          |
| -------------------- | --------- | ------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Headset**          | 1×1       | No            | N/A        | Audio mix (compress gunfire, amplify footsteps). EQ varies by model. See [Gears — Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md#headsets).                                                |
| **Helmet**           | 2×2       | No            | Yes        | Zone protection (Top, Nape, Ears, Eyes, Jaws). Class 1–6. See [Gears/ArmorGear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/ArmorGear/README.md).                           |
| **Face Cover**       | 1×1       | No            | Some       | Concealment + optional Class 1–2.                                                                                                                                                                              |
| **Body Armor**       | Variable  | No            | Yes        | Only when not using Armored Rig. Thorax/Stomach. Class 1–6. [Gears — Armor](../gears/armorgear/armor/index.html).                                                                                                      |
| **Tactical Rig**     | Variable  | **YES**       | Varies     | **Reload source.** Unarmored or Armored (replaces body armor). 12–24 slots typical. [Gears/StorageGear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md). |
| **Primary 1 / 2**    | Weapon    | **1** / **2** | Yes        | Chest / back.                                                                                                                                                                                                  |
| **Sidearm**          | Weapon    | **3**         | Yes        | Holster, fastest swap.                                                                                                                                                                                         |
| **Scabbard**         | Weapon    | **V**         | N/A        | Melee.                                                                                                                                                                                                         |
| **Pockets**          | 4×1       | **4–0**       | N/A        | Built-in; hotkeyable; keys, meds, nades.                                                                                                                                                                       |
| **Backpack**         | Variable  | No            | N/A        | Main loot; no hotkey; lost on death. [Gears/StorageGear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md).                                                |
| **Secure Container** | Variable  | No            | N/A        | **Survives death.** 2×2 to 3×4. In-raid: no weapons/thermal/NVG/helmets in. [Storage Gear](../Gears/StorageGear/Storage_Master_Database.md#secure-containers).                                                 |
| **Armband**          | 1×1       | No            | N/A        | Cosmetic / team ID.                                                                                                                                                                                            |

#### 2.3 UI/UX

Grid drag-drop, color coding (green/red/yellow), tooltips (name, weight, size, value, durability), keybind remapping, optional auto-sort. Accessibility: colorblind mode, scalable UI.

***

### 3. Equipment Overview (Armor & Storage)

**Armor & ballistics** — Class 1–6, zones, materials, penetration, blunt, ricochet: [Gears — Armor & Ballistics](../gears/armorgear/armor/index.html). Full item list: [Armor Master Database](../gears/armorgear/armor_master_database/index.html).

**Tactical rigs vs armored rigs** — Unarmored rig = more slots, no protection; armored rig = fewer slots + Class 3–5. Decision matrix and loadout examples: [Gears — Storage Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) and [Gear Mechanics](../gameplay/gear_mechanics/index.html).

**Headsets** — ANC/ASA, EQ profiles (ComTac, GSSH, Peltor, Sordin, MSA). Listed in [Armor Master Database — Headsets](../Gears/ArmorGear/Armor_Master_Database.md#headsets).

***

### 4. Grid System Overview

#### 4.1 Item Dimensions & Rotation

All items: Width × Height in 1×1 cells. Rotation: 90° (R while dragging). **Weapon grid size is fixed per weapon type;** adding or removing attachments does not change the weapon's inventory size.

| Category    | Typical Size | Examples                                                                                                                                     |
| ----------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Consumables | 1×1          | Bandage, pills, ammo stack                                                                                                                   |
| Magazines   | 1×2          | AR mags, pistol mags                                                                                                                         |
| Grenades    | 1×2          | Frag, flash, smoke                                                                                                                           |
| Pistols     | 2×1          | Handguns                                                                                                                                     |
| SMGs        | 2×2 – 3×2    | MP5, Vector                                                                                                                                  |
| Rifles      | 4×1 – 5×2    | M4, AK-74                                                                                                                                    |
| Sniper      | 5×2 – 6×2    | SVD, M700                                                                                                                                    |
| Helmets     | 2×2          | Tactical helmets                                                                                                                             |
| Armor Vests | 3×3 – 4×4    | Plate carriers                                                                                                                               |
| Backpacks   | 3×3 – 7×8    | Collapsed vs deployed; capacity = total cells per container (see [Storage Master Database](../gears/storagegear/storage_master_database/index.html)) |

#### 4.2 Stacking

Stackable: ammo (e.g. 60/stack), currency, crafting materials. Non-stackable: weapons, armor, attachments, keys, quest items. Consolidate partial stacks before raid.

#### 4.3 Flat Storage & Folding

**No bag-in-bag:** Each Storage Gear has a single Storage; all items in it are at the same level (flat). Bags, rigs, armor, weapons, and attachments placed in a container are normal items (footprint only). **Backpack collapse:** Empty backpacks can collapse to smaller size. Full rules: [Gears — Flat Storage & Folding](../gears/storagegear/storage_flat_storage_folding/index.html).

***

### 5. Encumbrance & Movement

Total weight = equipped gear + inventory (all items in all Storage Gears and slots). Weight tiers (Light → Medium → Heavy → Critical → Overweight) affect movement speed, sprint, inertia, jump, noise. Full formula, thresholds, inertia, stamina regen: [Gear Mechanics](../gameplay/gear_mechanics/index.html) and [Movement & Stamina](../gameplay/movement_and_stamina/index.html).

***

### 6. In-Raid Interactions & UX

#### 6.1 Looting

**Open inventory (e.g. Tab):** Split view — left: vicinity/containers, right: your inventory. Time does not freeze; audio muffled but audible.

**Container search:** Progress bar (1–5 s by container type and Perception skill). Items reveal progressively; can cancel. Examination: unknown items "?" until examined (0.5–2 s).

#### 6.2 Keybinds (examples)

| Action      | Keybind      | Use                |
| ----------- | ------------ | ------------------ |
| Quick Move  | Ctrl + Click | First free space   |
| Quick Equip | Alt + Click  | Correct slot       |
| Discard     | Del          | Drop               |
| Rotate      | R            | 90° while dragging |
| Examine     | Middle Click | Identify           |

#### 6.3 Value & Priority

Value/slot = Price ÷ (W×H). Priority: quest items → high value/slot → keys → AP ammo → meta parts → barter → weapons → low value (drop).

***

### 7. Weapon Modding (Gunsmith)

Weapons are platforms with 40–100+ attachments per family. Node-based build (receiver, barrel, handguard, optics, stock, etc.); live stat comparison; presets and sharing. Full UI and compatibility: [Gunsmith System](gunsmith_system/index.html). Weapon specs: [Weapon Arsenal](../gameplay/weaponarsenal/index.html) and [Weapons](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Weapons/README.md) section.

***

### 8. Stash & Containers

See [**Stash Design**](../stash_design/index.html) for the full Stash specification (grid, containers, progression, UI/UX). Stash size by edition and Safe House level; container unlock path (Scav Junkbox, Ammo/Med/Weapon Case, Items Case, THICC); secure container upgrade (Alpha → Beta → Gamma/Kappa). Full tables: [Gears — Stash & Container Progression](../gears/storagegear/stash_container_progression/index.html).

***

### 9. Implementation Notes

* **Data:** Item placement uses grid coordinates, rotation, parentId (container), slotId. Server validates overlap, weight, placement rules.
* **Anti-cheat:** Server-side grid and weight checks; no client trust for capacity or duplicates.
* **UX:** Drag state, valid/invalid placement feedback, snap-to-grid, SFX. See existing technical notes in repo.

***

### Appendix A: Glossary

**ADS** Aim Down Sights · **EOD** Edge of Darkness (premium) · **FiR** Found in Raid · **Rig** Tactical vest (reload source) · **Stash** Persistent out-of-raid storage · **Tetris** Spatial grid inventory

***

### Appendix B: Related Docs

* [**Stash Design**](../stash_design/index.html) — Full Stash specification (independent document).
* [**Gears**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/README.md) — Armor & Storage gear specs (ArmorGear, StorageGear).
* [**Gameplay — Gear Mechanics**](../gameplay/gear_mechanics/index.html) — Weight tiers, loadout philosophy, extraction.
* [**Gameplay — Looting & Inventory**](../gameplay/looting_interactions/index.html) — Container search times, grid dimensions.
* [**Container Mechanics**](container_mechanics/index.html) — High-level container types and mechanics (secure containers, nesting).
* [**Looting & FIR Rules**](looting_and_fir_rules/index.html) — Loot loop, FIR status, corpse looting.
* [**Medical & Survival Systems**](medical_and_survival_systems/index.html) — Injury types, meds, stimulants, hydration/energy.
* [**Gunsmith System**](gunsmith_system/index.html) — Weapon modding, ergonomics, malfunctions, overheating.
