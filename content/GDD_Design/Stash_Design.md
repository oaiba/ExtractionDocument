---
title: "Stash Design"
linkTitle: "Stash"
type: docs
weight: 25
---

## Overview

The **Stash** is the player's permanent out-of-raid storage for all items extracted from Raid Extraction. Items in the Stash are never lost on death — only gear brought into raid can be lost. The Stash is the central inventory repository that bridges raids and enables the preparation phase.

> **Document Status:** Independent design document — not part of Inventory_System section.  
> **Location:** Stash is physically housed in the **Stash Room** within the [Safe House](gamedesign/safe_house_design/index.html). Access from Loadout Preparation and Safe House.

---

## 1. Design Philosophy

- **Permanent storage:** Extracted loot is safe; death only affects gear brought into raid
- **Spatial constraint:** Grid-based Tetris-style management creates meaningful organization decisions
- **Progression gate:** Stash size scales with edition and Safe House level
- **Value-per-slot meta:** Players optimize what to keep vs. sell based on space efficiency

---

## 2. Grid System

### 2.1 Dimensions & Capacity

Stash capacity = **total cells** in a single grid. All items occupy cells based on width × height.

| Property | Value |
| :------- | :---- |
| **Base grid** | 10 columns × variable rows |
| **Rotation** | 90° (R key while dragging) |
| **Stacking** | Ammo, currency, crafting materials stack; weapons, armor, keys do not |

### 2.2 Item Dimensions (Reference)

| Category | Typical Size | Examples |
| :------- | :----------- | :------- |
| Consumables | 1×1 | Bandage, pills, ammo stack |
| Magazines | 1×2 | AR mags, pistol mags |
| Grenades | 1×2 | Frag, flash, smoke |
| Pistols | 2×1 | Handguns |
| Rifles | 4×1 – 5×2 | M4, AK-74 |
| Helmets | 2×2 | Tactical helmets |
| Armor Vests | 3×3 – 4×4 | Plate carriers |
| Backpacks | 3×3 – 7×8 | Collapsed vs deployed |

Full item dimensions: [Gears — Storage Master Database](gears/storagegear/storage_master_database/index.html).

### 2.3 Flat Storage & Folding

- **No bag-in-bag:** Each container has a single flat grid; items inside are at the same level
- **Backpack collapse:** Empty backpacks can collapse to smaller footprint
- Rules: [Storage: Flat Storage & Folding](gears/storagegear/storage_flat_storage_folding/index.html)

---

## 3. Stash Size Progression

Stash capacity increases with **edition** or **Safe House level** upgrades.

| Edition / Source | Stash Grid | Total Cells | Unlock Cost / Note |
| :--------------- | :--------- | :---------: | :----------------- |
| Standard Edition | 10×28 | 280 | Free |
| Safe House Lvl 2 | 10×38 | 380 | 3.5M + materials |
| Safe House Lvl 3 | 10×48 | 480 | 8.5M + materials |
| Safe House Lvl 4 | 10×68 | 680 | 15M + materials |
| Premium Edition | 10×48 | 480 | Free (start) |
| Ultimate Edition | 10×68 | 680 | Free (start) |

All editions can reach the same maximum (10×68) via Safe House upgrades. Full progression: [Stash & Container Progression](gears/storagegear/stash_container_progression/index.html).

---

## 4. Container Progression

### 4.1 Stash-Only Containers

Specialized containers for the global Stash (not carried in-raid):

| Phase | Container (Examples) | How to Unlock | Estimated Level |
| :---- | :------------------- | :------------- | :-------------- |
| Early | Keytool, Docs Case | Trader Lvl 1 purchase | 1–5 |
| Early–Mid | Ammo Case, Scav Junkbox | Trader Lvl 2 or craft | 10–15 |
| Mid | Med Case, Magazine Case | Trader Lvl 2 / quest | 15–20 |
| Mid–Late | Weapon Case | Trader Lvl 3 / quest chain | 20–30 |
| Late | Items Case | Trader Lvl 3 / barter | 30–40 |
| Endgame | THICC Items, THICC Weapon | Trader Lvl 4 / quest chain | 40+ |

### 4.2 Secure Container Upgrade Path

Secure containers survive death. Upgrade via quests or edition:

| Container | Grid | Cells | Unlock Method |
| :-------- | :--: | :---: | :------------ |
| Alpha | 2×2 | 4 | Default (all editions) |
| Beta | 2×3 | 6 | Quest (mid-game) |
| Gamma | 3×3 | 9 | Premium Edition OR quest (late-game) |
| Kappa | 3×4 | 12 | Quest: complete all main quests (endgame) |

**In-raid restrictions:** Cannot place guns, thermal scopes, or night vision inside during raid. Can place keys, meds, ammo, valuables.

---

## 5. Organization Zones

Recommended layout for efficient stash management:

| Zone | Rows | Purpose |
| :--- | :--- | :------ |
| **Top (Active Gear)** | 1–10 | Ready-to-raid weapons, armor, rigs; frequently used items |
| **Middle (Containers)** | 11–40 | Storage cases (Scav Junkbox, Ammo Case, Med Case, etc.); grouped by type |
| **Bottom (Long-term)** | 41+ | Quest items, Safe House upgrade materials, rarely used items |

**Value-per-slot priority:** Quest items → high value/slot → keys → AP ammo → meta parts → barter → weapons → low value (drop).

---

## 6. Stash Room Integration

The Stash is located in the **Stash Room** within the [Safe House](gamedesign/safe_house_design/index.html). Integration points:

- **Loadout Preparation:** Quick-access panel shows filtered stash; drag items to equip
- **Safe House:** Full stash grid accessible from Stash Room; Operator stamina/energy/hydration recovery logic uses items from stash
- **Trading Post:** Sell items to traders; Flea Market access

---

## 7. UI/UX

### 7.1 Layout (Full Stash Screen)

```
+------------------------------------------------------------------+
|  < BACK          STASH            [Search] [Filter ▼] [Sort ▼]   |
|------------------------------------------------------------------|
|  GRID VIEW (12 columns x N rows)                                  |
|  CAPACITY: 145 / 200 slots       TOTAL VALUE: 2,450,000 credits  |
|  ACTIONS: [Auto-Sort] [Sell Junk] [Move to Loadout] [Discard]     |
+------------------------------------------------------------------+
```

### 7.2 Grid Mechanics

| Mechanic | Description | Platform Input |
| :------- | :---------- | :------------- |
| Item placement | Items occupy grid cells based on size | PC: drag-drop. Console: cursor + A. Mobile: tap-to-select then tap-to-place |
| Rotation | Rotate items 90° to optimize space | PC: R. Console: Y while holding. Mobile: rotate button |
| Stacking | Same ammo/consumables stack | Automatic when placed on matching stack |
| Quick transfer | Move to equipped loadout slot | PC: Ctrl+Click. Console: hold A. Mobile: double-tap |
| Search | Text filter highlights matching items | PC: Ctrl+F. Console: Y → virtual keyboard |
| Auto-Sort | Reorganize for optimal space | Single button press. Maintains category grouping |
| Quick-Sell | Mark items for sale, batch sell | PC: middle-click. Console: X. Mobile: swipe-left |

### 7.3 Keybinds (Examples)

| Action | Keybind | Use |
| :----- | :------ | :-- |
| Quick Move | Ctrl + Click | First free space |
| Quick Equip | Alt + Click | Correct slot |
| Discard | Del | Drop |
| Rotate | R | 90° while dragging |

---

## 8. Economy

- **Value-per-slot** = Price ÷ (W×H). High value-per-slot items prioritized for limited space
- **Sell vs. Keep:** Weapons (keep if meta/quest), armor (keep if Class 5+ >60%), barter (keep if Safe House/craft needed)
- **Capacity vs edition/Safe House level:** Standard starts 280 cells; max 680 cells for all editions

---

## 9. Cross-References

- [Stash & Container Progression](gears/storagegear/stash_container_progression/index.html) — Full tables, unlock costs
- [Safe House Design](gamedesign/safe_house_design/index.html) — Stash Room, Operator state recovery
- [Storage Master Database](gears/storagegear/storage_master_database/index.html) — Container specs, stash-only cases
- [Menus — Stash / Inventory Management](ui_ux/menus/index.html) — UI layout details
- [Loadout Preparation](gamedesign/loadoutpreparation/index.html) — Quick Stash Access panel
- [Inventory System](inventory_system/_index/index.html) — Paper doll, equipment slots, looting UX
