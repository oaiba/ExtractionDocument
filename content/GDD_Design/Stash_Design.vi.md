---
title: "Stash Design"
linkTitle: "Stash"
type: docs
weight: 25
---

## Tổng Quan

The **Stash** is the người chơi's permanent out-of-raid storage for all items extracted from Raid Extraction. Items in the Stash are never lost on death — only gear brought into raid can be lost. The Stash is the central inventory repository that bridges raids và enables the preparation phase.

> **tài liệu Status:** Independent design tài liệu — not part of Inventory_System section.  
> **Location:** Stash is physically housed in the **Stash Room** within the [Safe House](GameDesign/Safe_House_Design.md). Access from Loadout Preparation và Safe House.

---

## 1. Design Philosophy

- **Permanent storage:** Extracted loot is safe; death only affects gear brought into raid
- **Spatial constraint:** Grid-based Tetris-style management tạo meaningful organization quyết định
- **Progression gate:** Stash size scales với edition và Safe House level
- **giá trị-per-slot meta:** người chơi optimize what to keep vs. sell based on space efficiency

---

## 2. Grid hệ thống

### 2.1 Dimensions & Capacity

Stash capacity = **total cells** in a single grid. All items occupy cells based on width × height.

| Property | giá trị |
| :------- | :---- |
| **Base grid** | 10 columns × variable rows |
| **Rotation** | 90° (R chính while dragging) |
| **Stacking** | đạn, currency, crafting materials stack; vũ khí, giáp, keys do not |

### 2.2 Item Dimensions (Reference)

| Category | Typical Size | Examples |
| :------- | :----------- | :------- |
| Consumables | 1×1 | Bandage, pills, đạn stack |
| Magazines | 1×2 | AR mags, pistol mags |
| Grenades | 1×2 | Frag, flash, smoke |
| Pistols | 2×1 | Handguns |
| Rifles | 4×1 – 5×2 | M4, AK-74 |
| Helmets | 2×2 | Tactical helmets |
| giáp Vests | 3×3 – 4×4 | Plate carriers |
| Backpacks | 3×3 – 7×8 | Collapsed vs deployed |

Full item dimensions: [Gears — Storage Master Database](Gears/StorageGear/Storage_Master_Database.md).

### 2.3 Flat Storage & Folding

- **No bag-in-bag:** Each container has a single flat grid; items inside are at the same level
- **Backpack collapse:** empty backpacks can collapse to smaller footprint
- Rules: [Storage: Flat Storage & Folding](Gears/StorageGear/Storage_Flat_Storage_Folding.md)

---

## 3. Stash Size Progression

Stash capacity increases với **edition** hoặc **Safe House level** upgrades.

| Edition / source | Stash Grid | Total Cells | Unlock chi phí / Note |
| :--------------- | :--------- | :---------: | :----------------- |
| Standard Edition | 10×28 | 280 | Free |
| Safe House Lvl 2 | 10×38 | 380 | 3.5M + materials |
| Safe House Lvl 3 | 10×48 | 480 | 8.5M + materials |
| Safe House Lvl 4 | 10×68 | 680 | 15M + materials |
| Premium Edition | 10×48 | 480 | Free (start) |
| Ultimate Edition | 10×68 | 680 | Free (start) |

All editions can reach the same maximum (10×68) via Safe House upgrades. Full progression: [Stash & Container Progression](Gears/StorageGear/Stash_Container_Progression.md).

---

## 4. Container Progression

### 4.1 Stash-Only Containers

Specialized containers for the global Stash (not carried in-raid):

| Phase | Container (Examples) | How to Unlock | Estimated Level |
| :---- | :------------------- | :------------- | :-------------- |
| Early | Keytool, Docs Case | Trader Lvl 1 purchase | 1–5 |
| Early–Mid | đạn Case, Scav Junkbox | Trader Lvl 2 hoặc craft | 10–15 |
| Mid | Med Case, Magazine Case | Trader Lvl 2 / quest | 15–20 |
| Mid–Late | vũ khí Case | Trader Lvl 3 / quest chain | 20–30 |
| Late | Items Case | Trader Lvl 3 / barter | 30–40 |
| Endgame | THICC Items, THICC vũ khí | Trader Lvl 4 / quest chain | 40+ |

### 4.2 Secure Container upgrade Path

Secure containers survive death. upgrade via quests hoặc edition:

| Container | Grid | Cells | Unlock Method |
| :-------- | :--: | :---: | :------------ |
| Alpha | 2×2 | 4 | Default (all editions) |
| Beta | 2×3 | 6 | Quest (mid-game) |
| Gamma | 3×3 | 9 | Premium Edition hoặc quest (late-game) |
| Kappa | 3×4 | 12 | Quest: complete all main quests (endgame) |

**In-raid restrictions:** Cannot place guns, thermal scopes, hoặc night vision inside trong khi raid. Can place keys, meds, đạn, valuables.

---

## 5. Organization Zones

Recommended layout for efficient stash management:

| Zone | Rows | mục đích |
| :--- | :--- | :------ |
| **Top (Active Gear)** | 1–10 | Ready-to-raid vũ khí, giáp, rigs; frequently used items |
| **Middle (Containers)** | 11–40 | Storage cases (Scav Junkbox, đạn Case, Med Case, etc.); grouped by type |
| **Bottom (Long-term)** | 41+ | Quest items, Safe House upgrade materials, rarely used items |

**giá trị-per-slot priority:** Quest items → high giá trị/slot → keys → AP đạn → meta parts → barter → vũ khí → low giá trị (drop).

---

## 6. Stash Room Integration

The Stash is located in the **Stash Room** within the [Safe House](GameDesign/Safe_House_Design.md). Integration points:

- **Loadout Preparation:** Quick-access panel shows filtered stash; drag items to equip
- **Safe House:** Full stash grid accessible from Stash Room; Operator stamina/energy/hydration recovery logic uses items from stash
- **Trading Post:** Sell items to traders; Flea Market access

---

## 7. UI/UX

### 7.1 Layout (Full Stash màn hình)

```
+------------------------------------------------------------------+
|  < BACK          STASH            [Search] [Filter ▼] [Sort ▼]   |
|------------------------------------------------------------------|
|  GRID VIEW (12 columns x N rows)                                  |
|  CAPACITY: 145 / 200 slots       TOTAL VALUE: 2,450,000 credits  |
|  ACTIONS: [Auto-Sort] [Sell Junk] [Move to Loadout] [Discard]     |
+------------------------------------------------------------------+
```

### 7.2 Grid cơ chế

| cơ chế | Description | Platform Input |
| :------- | :---------- | :------------- |
| Item placement | Items occupy grid cells based on size | PC: drag-drop. Console: cursor + A. Mobile: tap-to-select then tap-to-place |
| Rotation | Rotate items 90° to optimize space | PC: R. Console: Y while holding. Mobile: rotate button |
| Stacking | Same đạn/consumables stack | Automatic khi placed on matching stack |
| Quick transfer | Move to equipped loadout slot | PC: Ctrl+Click. Console: hold A. Mobile: double-tap |
| Search | Text filter highlights matching items | PC: Ctrl+F. Console: Y → virtual keyboard |
| Auto-Sort | Reorganize for optimal space | Single button press. Maintains category grouping |
| Quick-Sell | Mark items for sale, batch sell | PC: middle-click. Console: X. Mobile: swipe-left |

### 7.3 Keybinds (Examples)

| Action | Keybind | cách dùng |
| :----- | :------ | :-- |
| Quick Move | Ctrl + Click | First free space |
| Quick Equip | Alt + Click | Correct slot |
| Discard | Del | Drop |
| Rotate | R | 90° while dragging |

---

## 8. Economy

- **giá trị-per-slot** = giá ÷ (W×H). High giá trị-per-slot items prioritized for limited space
- **Sell vs. Keep:** vũ khí (keep nếu meta/quest), giáp (keep nếu Class 5+ >60%), barter (keep nếu Safe House/craft needed)
- **Capacity vs edition/Safe House level:** Standard starts 280 cells; max 680 cells for all editions

---

## 9. Cross-References

- [Stash & Container Progression](Gears/StorageGear/Stash_Container_Progression.md) — Full tables, unlock costs
- [Safe House Design](GameDesign/Safe_House_Design.md) — Stash Room, Operator trạng thái recovery
- [Storage Master Database](Gears/StorageGear/Storage_Master_Database.md) — Container specs, stash-only cases
- [Menus — Stash / Inventory Management](UI_UX/Menus.md) — UI layout chi tiết
- [Loadout Preparation](GameDesign/LoadoutPreparation.md) — Quick Stash Access panel
- [Inventory hệ thống](Inventory_System/_index.md) — Paper doll, equipment slots, looting UX
