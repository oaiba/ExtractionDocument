---
title: "Gear Tier System"
type: docs
weight: 0
---

## Overview

This document defines the **canonical Gear Tier** for Armor Gear and Storage Gear. Progression and gating use **Tier + Rarity + player level + trader level** only. **Item level (Gear Level) is not used** — all "level" references are player level, trader level, or repair bench level.

---

## Quy ước chung (General Convention)

- **Progression:** Gear access and power are gated by **Tier**, **Rarity**, **player level**, and **trader level** (plus quest and repair bench level when relevant).
- **No item level:** There is no level attached to individual gear pieces. No "level requirement to equip", no "upgrade level" (+1, +2, etc.).
- **Tier** groups gear by power/progression band for loot tables, economy, UI, and (optionally) matchmaking or balance brackets.

---

## Armor Gear Tier (1–5)

**Source:** Armor Class (1–6, GOST) + Rarity (Common / Uncommon / Rare / Epic / Legendary).

### Mapping Table

| Tier | Class | Typical Rarity | Examples |
| :--: | :---: | :------------- | :------- |
| 1 | 1–2 | Common | PACA, Press Vest, Light Vest, Light Helmet |
| 2 | 3 | Uncommon | 6B13, Ceramic Carrier, Medium Helmet, 6B47 |
| 3 | 4 | Rare | Trooper, M1, ULACH, Heavy Helmet, 6B3TM Armored Rig |
| 4 | 5 | Epic | Redut-M, Killa, Gen4, Tactical Helmet, Altyn, Defender 2 |
| 5 | 6 | Legendary | Zabralo, Slick |

### Exceptions

- **Face shields / visors:** Assign Tier by Class (1–3); if Class is ambiguous, use Rarity band.
- **Headsets:** No armor Class; assign Tier by Rarity (Uncommon = 2, Rare = 3).
- **Armored rigs:** Use the rig's Armor Class; Tier follows the same mapping as body armor.

Every armor item in [Armor Master Database](ArmorGear/Armor_Master_Database.md) has a single Tier (1–5) per this table.

---

## Storage Gear Tier (1–4)

**Scope:** Tactical rigs (unarmored + armored), backpacks, secure containers, stash-only cases.

**Source:** Capacity band (total cells) + Rarity + Trader level.

### Mapping Table

| Tier | Capacity (cells) | Typical Rarity | Trader | Examples |
| :--: | :--------------- | :------------- | :----: | :------- |
| 1 | ≤ 9 (rig), ≤ 9 (backpack) | Common | 1 | Chest Harness, Light Rig, Sling Bag, Small Backpack |
| 2 | 10–16 (rig), 10–20 (backpack) | Uncommon | 2 | Standard Rig, Recon Vest, Berkut, Medium Backpack |
| 3 | 17–20 (rig), 21–30 (backpack) | Rare | 3 | Blackrock, Heavy Rig, Tri-Zip, Raid Backpack, Large Backpack |
| 4 | Max or special | Epic | 4 / endgame | Pilgrim, Defender 2 |

### Secure Containers

| Container | Cells | Tier |
| :-------- | :---: | :--: |
| Alpha | 4 | 1 |
| Beta | 6 | 2 |
| Gamma | 9 | 3 |
| Kappa | 12 | 4 |

### Stash-Only Cases

Assign Tier by unlock phase and capacity: early (Keytool, Docs Case) = 1; mid (Ammo, Med, Magazine Case) = 2; late (Weapon Case, Items Case) = 3; endgame (THICC cases) = 4.

Every storage item in [Storage Master Database](StorageGear/Storage_Master_Database.md) has a single Tier (1–4) per this table.

---

## Use of Tier in Systems (No Level)

| System | Usage |
| :----- | :---- |
| **Loot table** | Tier (+ Rarity) determines drop pool by zone/raid/event. |
| **Crafting** | Tier of output; recipes may require Tier/Rarity of materials. |
| **Economy / Trader** | Price, restock, availability by Tier; unlock by **player level + trader level** (see [Armor Progression](ArmorGear/Armor_Progression.md), [Stash & Container Progression](StorageGear/Stash_Container_Progression.md)). |
| **UI / Tooltip** | Display Tier consistently (icon, number, color); Rarity as today. |
| **Balance / Matchmaking** | If gear brackets exist for raids, use Tier (+ Rarity); no item level. |

---

## Game References

Similar games (Relic Hunters Legend, Project Ethos, ARC Raiders, EFT Arena, Risk of Rain 2) use tier + rarity + progression. This game uses **Tier + Rarity + player/trader level** only; no item level.

---

## Cross-References

- [Armor & Ballistics](ArmorGear/Armor.md) — Class system, zones, materials.
- [Armor Master Database](ArmorGear/Armor_Master_Database.md) — Per-item Tier column.
- [Armor Progression](ArmorGear/Armor_Progression.md) — Trader/quest/player level gates.
- [Armor Balance Framework](ArmorGear/Armor_Balance_Framework.md) — EHP, cost-efficiency.
- [Storage Master Database](StorageGear/Storage_Master_Database.md) — Per-item Tier column.
- [Stash & Container Progression](StorageGear/Stash_Container_Progression.md) — Unlock phase, secure path.
- [Progression](../GameDesign/Progression.md) — Player and trader level framework.
