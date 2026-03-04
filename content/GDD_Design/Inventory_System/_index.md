---
title: "Inventory System — Core Mechanics"
linkTitle: "Inventory System"
type: docs
weight: 60
version: 2.1
last_updated: 2026-03-04
---

> **Document Status**: Living Document - Updated Regularly  
> **Target Platform**: PC (Primary), Console (Secondary)  
> **Reference Games**: Escape from Tarkov, Arena Breakout: Infinite, Delta Force, Hunt: Showdown 1896, Gray Zone Warfare

---

## Scope: Inventory vs Gears

**Gears** ([../Gears/](../Gears/)) = physical equipment the Operator **wears or carries** in-raid: body armor, helmets, tactical rigs, backpacks, secure containers. All armor and storage **specs** (classes, materials, slot layouts, balance) live under **Gears/ArmorGear** and **Gears/StorageGear**.

**Inventory_System** (this section) = **general inventory system**: grid mechanics, paper doll, equipment slots, encumbrance overview, looting UX. Later expansion may add: Vehicle_Inventory, Global_Stash_System, Crate_System, etc.

---

## Executive Summary

Inventory & Gear design centers on **meaningful choices**, **spatial puzzle-solving**, and **risk-reward balance**. Key differentiators: Tetris-style grid with rotation, weight-based movement penalties, zone-based armor (see Gears), tactical accessibility (rig = reload source), and economic risk (lose gear on death).

---

## 1. Design Philosophy & Core Pillars

### 1.1 Core Design Pillars

**Pillar 1: Spatial Puzzle Management** — Inventory space is a physical constraint; items have dimensions (1×1 bandage vs 4×2 rifle); rotation (90°) enables creative packing. Goal: satisfying "Tetris moments."

**Pillar 2: Weight Has Consequences** — Every item has mass; overburdening causes stamina, speed, and inertia penalties. Goal: armor vs mobility, loot vs escape trade-offs.

**Pillar 3: Risk-Reward Economics** — High-tier gear increases survival but amplifies loss on death; insurance and secure container soften the loop. Goal: "gearing fear" and "loot excitement."

**Pillar 4: Tactical Ergonomics** — Where items are stored matters: magazines in rig = quick reload; in backpack = must open inventory. Goal: reward preparation, punish poor loadout planning.

### 1.2 Player Experience Goals

- **New players:** Gradual introduction, simple starter loadouts, clear feedback for weight/space.
- **Veterans:** Min-max space/weight, value-per-slot meta, speed-looting keybinds.
- **Emotional beats:** Tension (limited space), satisfaction (perfect pack), fear (overweight extract), loss (death), triumph (full inventory extract).

---

## 2. The Character Loadout System (Paper Doll)

### 2.1 Primary Interface

Pre-raid screen: 3D character model (rotatable), equipment slots around model, real-time stats (armor rating, weight, movement speed), durability indicators.

### 2.2 Equipment Slots

| Slot Name            | Grid Size | Hotkey  | Durability | Notes |
| :------------------- | :-------- | :------ | :--------- | :---- |
| **Headset**          | 1×1       | No      | N/A        | Audio mix (compress gunfire, amplify footsteps). EQ varies by model. See [Gears — Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md#headsets). |
| **Helmet**           | 2×2       | No      | Yes        | Zone protection (Top, Nape, Ears, Eyes, Jaws). Class 1–6. See [Gears/ArmorGear](../Gears/ArmorGear/). |
| **Face Cover**       | 1×1       | No      | Some       | Concealment + optional Class 1–2. |
| **Body Armor**       | Variable  | No      | Yes        | Only when not using Armored Rig. Thorax/Stomach. Class 1–6. [Gears — Armor](../Gears/ArmorGear/Armor.md). |
| **Tactical Rig**     | Variable  | **YES** | Varies     | **Reload source.** Unarmored or Armored (replaces body armor). 12–24 slots typical. [Gears/StorageGear](../Gears/StorageGear/). |
| **Primary 1 / 2**    | Weapon    | **1** / **2** | Yes | Chest / back. |
| **Sidearm**          | Weapon    | **3**   | Yes        | Holster, fastest swap. |
| **Scabbard**         | Weapon    | **V**   | N/A        | Melee. |
| **Pockets**          | 4×1       | **4–0** | N/A        | Built-in; hotkeyable; keys, meds, nades. |
| **Backpack**         | Variable  | No      | N/A        | Main loot; no hotkey; lost on death. [Gears/StorageGear](../Gears/StorageGear/). |
| **Secure Container** | Variable  | No      | N/A        | **Survives death.** 2×2 to 3×4. In-raid: no weapons/thermal/NVG/helmets in. [Storage Gear](../Gears/StorageGear/Storage_Master_Database.md#secure-containers). |
| **Armband**          | 1×1       | No      | N/A        | Cosmetic / team ID. |

### 2.3 UI/UX

Grid drag-drop, color coding (green/red/yellow), tooltips (name, weight, size, value, durability), keybind remapping, optional auto-sort. Accessibility: colorblind mode, scalable UI.

---

## 3. Equipment Overview (Armor & Storage)

**Armor & ballistics** — Class 1–6, zones, materials, penetration, blunt, ricochet: [Gears — Armor & Ballistics](../Gears/ArmorGear/Armor.md). Full item list: [Armor Master Database](../Gears/ArmorGear/Armor_Master_Database.md).

**Tactical rigs vs armored rigs** — Unarmored rig = more slots, no protection; armored rig = fewer slots + Class 3–5. Decision matrix and loadout examples: [Gears — Storage Gear](../Gears/StorageGear/) and [Gear Mechanics](../Gameplay/Gear_Mechanics.md).

**Headsets** — ANC/ASA, EQ profiles (ComTac, GSSH, Peltor, Sordin, MSA). Listed in [Armor Master Database — Headsets](../Gears/ArmorGear/Armor_Master_Database.md#headsets).

---

## 4. Grid System Overview

### 4.1 Item Dimensions & Rotation

All items: Width × Height in 1×1 cells. Rotation: 90° (R while dragging). **Weapon grid size is fixed per weapon type;** adding or removing attachments does not change the weapon's inventory size.

| Category     | Typical Size | Examples |
| :----------- | :----------- | :------- |
| Consumables  | 1×1          | Bandage, pills, ammo stack |
| Magazines    | 1×2          | AR mags, pistol mags |
| Grenades     | 1×2          | Frag, flash, smoke |
| Pistols      | 2×1          | Handguns |
| SMGs         | 2×2 – 3×2    | MP5, Vector |
| Rifles       | 4×1 – 5×2    | M4, AK-74 |
| Sniper       | 5×2 – 6×2    | SVD, M700 |
| Helmets      | 2×2          | Tactical helmets |
| Armor Vests  | 3×3 – 4×4    | Plate carriers |
| Backpacks    | 3×3 – 7×8    | Collapsed vs deployed; capacity = total cells per container (see [Storage Master Database](../Gears/StorageGear/Storage_Master_Database.md)) |

### 4.2 Stacking

Stackable: ammo (e.g. 60/stack), currency, crafting materials. Non-stackable: weapons, armor, attachments, keys, quest items. Consolidate partial stacks before raid.

### 4.3 Flat Storage & Folding

**No bag-in-bag:** Each Storage Gear has a single Storage; all items in it are at the same level (flat). Bags, rigs, armor, weapons, and attachments placed in a container are normal items (footprint only). **Backpack collapse:** Empty backpacks can collapse to smaller size. Full rules: [Gears — Flat Storage & Folding](../Gears/StorageGear/Storage_Flat_Storage_Folding.md).

---

## 5. Encumbrance & Movement

Total weight = equipped gear + inventory (all items in all Storage Gears and slots). Weight tiers (Light → Medium → Heavy → Critical → Overweight) affect movement speed, sprint, inertia, jump, noise. Full formula, thresholds, inertia, stamina regen: [Gear Mechanics](../Gameplay/Gear_Mechanics.md) and [Movement & Stamina](../Gameplay/Movement_and_Stamina.md).

---

## 6. In-Raid Interactions & UX

### 6.1 Looting

**Open inventory (e.g. Tab):** Split view — left: vicinity/containers, right: your inventory. Time does not freeze; audio muffled but audible.

**Container search:** Progress bar (1–5 s by container type and Perception skill). Items reveal progressively; can cancel. Examination: unknown items "?" until examined (0.5–2 s).

### 6.2 Keybinds (examples)

| Action           | Keybind              | Use |
| :--------------- | :------------------- | :--- |
| Quick Move       | Ctrl + Click         | First free space |
| Quick Equip      | Alt + Click          | Correct slot |
| Discard          | Del                  | Drop |
| Rotate           | R                    | 90° while dragging |
| Examine          | Middle Click         | Identify |

### 6.3 Value & Priority

Value/slot = Price ÷ (W×H). Priority: quest items → high value/slot → keys → AP ammo → meta parts → barter → weapons → low value (drop).

---

## 7. Weapon Modding (Gunsmith)

Weapons are platforms with 40–100+ attachments per family. Node-based build (receiver, barrel, handguard, optics, stock, etc.); live stat comparison; presets and sharing. Full UI and compatibility: [Gunsmith System](Gunsmith_System.md). Weapon specs: [Weapon Arsenal](../Gameplay/WeaponArsenal.md) and [Weapons](../Weapons/) section.

---

## 8. Stash & Containers

See **[Stash Design](../Stash_Design.md)** for the full Stash specification (grid, containers, progression, UI/UX). Stash size by edition and Safe House level; container unlock path (Scav Junkbox, Ammo/Med/Weapon Case, Items Case, THICC); secure container upgrade (Alpha → Beta → Gamma/Kappa). Full tables: [Gears — Stash & Container Progression](../Gears/StorageGear/Stash_Container_Progression.md).

---

## 9. Implementation Notes

- **Data:** Item placement uses grid coordinates, rotation, parentId (container), slotId. Server validates overlap, weight, placement rules.
- **Anti-cheat:** Server-side grid and weight checks; no client trust for capacity or duplicates.
- **UX:** Drag state, valid/invalid placement feedback, snap-to-grid, SFX. See existing technical notes in repo.

---

## Appendix A: Glossary

**ADS** Aim Down Sights · **EOD** Edge of Darkness (premium) · **FiR** Found in Raid · **Rig** Tactical vest (reload source) · **Stash** Persistent out-of-raid storage · **Tetris** Spatial grid inventory

---

## Appendix B: Related Docs

- **[Stash Design](../Stash_Design.md)** — Full Stash specification (independent document).
- **[Gears](../Gears/)** — Armor & Storage gear specs (ArmorGear, StorageGear).
- **[Gameplay — Gear Mechanics](../Gameplay/Gear_Mechanics.md)** — Weight tiers, loadout philosophy, extraction.
- **[Gameplay — Looting & Inventory](../Gameplay/Looting_Interactions.md)** — Container search times, grid dimensions.
- **[Container Mechanics](Container_Mechanics.md)** — High-level container types and mechanics (secure containers, nesting).
- **[Looting & FIR Rules](Looting_And_FIR_Rules.md)** — Loot loop, FIR status, corpse looting.
- **[Medical & Survival Systems](Medical_And_Survival_Systems.md)** — Injury types, meds, stimulants, hydration/energy.
- **[Gunsmith System](Gunsmith_System.md)** — Weapon modding, ergonomics, malfunctions, overheating.
