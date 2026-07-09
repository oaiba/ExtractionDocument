---
title: "Gear Tier hệ thống"
type: docs
weight: 0
---

## Tổng Quan

Tài liệu này định nghĩa the **canonical Gear Tier** for giáp Gear và Storage Gear. Progression và gating cách dùng **Tier + Rarity + người chơi level + trader level** only. **Item level (Gear Level) is not used** — all "level" references are người chơi level, trader level, hoặc repair bench level.

---

## Quy ước chung (General Convention)

- **Progression:** Gear access và power are gated by **Tier**, **Rarity**, **người chơi level**, và **trader level** (plus quest và repair bench level khi relevant).
- **No item level:** There is no level attached to individual gear pieces. No "level yêu cầu to equip", no "upgrade level" (+1, +2, etc.).
- **Tier** groups gear by power/progression band for loot tables, economy, UI, và (optionally) matchmaking hoặc balance brackets.

---

## giáp Gear Tier (1–5)

**source:** giáp Class (1–6, GOST) + Rarity (Common / Uncommon / Rare / Epic / Legendary).

### Mapping bảng

| Tier | Class | Typical Rarity | Examples |
| :--: | :---: | :------------- | :------- |
| 1 | 1–2 | Common | PACA, Press Vest, Light Vest, Light Helmet |
| 2 | 3 | Uncommon | 6B13, Ceramic Carrier, Medium Helmet, 6B47 |
| 3 | 4 | Rare | Trooper, M1, ULACH, Heavy Helmet, 6B3TM Armored Rig |
| 4 | 5 | Epic | Redut-M, Killa, Gen4, Tactical Helmet, Altyn, Defender 2 |
| 5 | 6 | Legendary | Zabralo, Slick |

### Exceptions

- **Face shields / visors:** Assign Tier by Class (1–3); nếu Class is ambiguous, cách dùng Rarity band.
- **Headsets:** No giáp Class; assign Tier by Rarity (Uncommon = 2, Rare = 3).
- **Armored rigs:** cách dùng the rig's giáp Class; Tier follows the same mapping as body giáp.

Every giáp item in [giáp Master Database](ArmorGear/Armor_Master_Database.md) has a single Tier (1–5) per this bảng.

---

## Storage Gear Tier (1–4)

**Scope:** Tactical rigs (unarmored + armored), backpacks, secure containers, stash-only cases.

**source:** Capacity band (total cells) + Rarity + Trader level.

### Mapping bảng

| Tier | Capacity (cells) | Typical Rarity | Trader | Examples |
| :--: | :--------------- | :------------- | :----: | :------- |
| 1 | ≤ 9 (rig), ≤ 9 (backpack) | Common | 1 | Chest Harness, Light Rig, Sling Bag, Small Backpack |
| 2 | 10–16 (rig), 10–20 (backpack) | Uncommon | 2 | Standard Rig, Recon Vest, Berkut, Medium Backpack |
| 3 | 17–20 (rig), 21–30 (backpack) | Rare | 3 | Blackrock, Heavy Rig, Tri-Zip, Raid Backpack, Large Backpack |
| 4 | Max hoặc special | Epic | 4 / endgame | Pilgrim, Defender 2 |

### Secure Containers

| Container | Cells | Tier |
| :-------- | :---: | :--: |
| Alpha | 4 | 1 |
| Beta | 6 | 2 |
| Gamma | 9 | 3 |
| Kappa | 12 | 4 |

### Stash-Only Cases

Assign Tier by unlock phase và capacity: early (Keytool, Docs Case) = 1; mid (đạn, Med, Magazine Case) = 2; late (vũ khí Case, Items Case) = 3; endgame (THICC cases) = 4.

Every storage item in [Storage Master Database](StorageGear/Storage_Master_Database.md) has a single Tier (1–4) per this bảng.

---

## cách dùng of Tier in hệ thống (No Level)

| hệ thống | Usage |
| :----- | :---- |
| **Loot bảng** | Tier (+ Rarity) determines drop pool by zone/raid/event. |
| **Crafting** | Tier of output; recipes may require Tier/Rarity of materials. |
| **Economy / Trader** | giá, restock, availability by Tier; unlock by **người chơi level + trader level** (Xem [giáp Progression](ArmorGear/Armor_Progression.md), [Stash & Container Progression](StorageGear/Stash_Container_Progression.md)). |
| **UI / Tooltip** | Display Tier consistently (icon, number, color); Rarity as today. |
| **Balance / Matchmaking** | nếu gear brackets exist for raids, cách dùng Tier (+ Rarity); no item level. |

---

## Game References

Similar games (Relic Hunters Legend, Project Ethos, ARC Raiders, EFT Arena, Risk of Rain 2) cách dùng tier + rarity + progression. This game uses **Tier + Rarity + người chơi/trader level** only; no item level.

---

## Tham Chiếu Chéo

- [giáp & Ballistics](ArmorGear/giáp.md) — Class hệ thống, zones, materials.
- [giáp Master Database](ArmorGear/Armor_Master_Database.md) — Per-item Tier column.
- [giáp Progression](ArmorGear/Armor_Progression.md) — Trader/quest/người chơi level gates.
- [giáp Balance Framework](ArmorGear/Armor_Balance_Framework.md) — EHP, chi phí-efficiency.
- [Storage Master Database](StorageGear/Storage_Master_Database.md) — Per-item Tier column.
- [Stash & Container Progression](StorageGear/Stash_Container_Progression.md) — Unlock phase, secure path.
- [Progression](../GameDesign/Progression.md) — người chơi và trader level framework.
