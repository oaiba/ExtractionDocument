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

## Tier vs Rarity vs Power

Tier, rarity, và practical power có liên quan nhưng không giống nhau. UI không được khiến player hiểu rằng item hiếm hơn luôn mạnh hơn tuyệt đối hoặc gear có upgrade level.

| Concept | Meaning | What It Controls | What It Must Not Imply |
| ------- | ------- | ---------------- | ---------------------- |
| Tier | Balance/progression bracket | Loot table bands, trader access, cost curve, optional raid brackets | Per-item level hoặc upgrade stage |
| Rarity | Availability, presentation, economy signal | Drop frequency, badge treatment, collection feel, trader scarcity | Automatic combat superiority |
| Practical power | Tác động thực tế của stats trong context | Armor class, zones, durability, weight, capacity, access speed, repairability | Một item best trong mọi loadout |
| Player/trader level | Access gate cho system và stock | Unlock timing và shop/trader availability | Stat scaling trên gear item |

Armor class, durability, material, coverage zones, storage capacity, access speed, weight, và repairability mới định nghĩa real gear value. Tier và rarity giúp đọc progression/scarcity, nhưng comparison UI vẫn phải giải thích trade-off thực tế.

## Rarity Meaning Table

| Rarity | Availability Meaning | UI Meaning | Design Expectation |
| ------ | -------------------- | ---------- | ------------------ |
| Common | Early access, frequent loot, basic trader stock | Low-intensity badge, plain label | Baseline đáng tin, không mặc định là rác |
| Uncommon | Slightly gated, specialized hơn | Clear badge và filter support | Có một lợi thế đáng chú ý hoặc efficiency tốt hơn |
| Rare | Mid-progression, contested loot, reputation gates | Strong badge, đáng compare | Trade-off rõ với weight/cost/repair |
| Epic | Late stock, event/quest/crafting relevance | Premium-looking non-commerce badge | Strong situational role, không universally best |
| Legendary | Endgame, rare event, high-risk hoặc prestige | Highest scarcity badge với text label | Aspirational, expensive, heavy/risky, hoặc khó repair |

Rarity không phải monetization promise. Paid offers có thể bán cosmetic có presentation giống rarity, nhưng paid rarity không được grant armor class, storage capacity, recoil, audio, visibility, hoặc durability advantage.

## Gear Value Model

| Value Type | Applies To | Meaning |
| ---------- | ---------- | ------- |
| Combat value | Armor, helmets, weapons, ammo-related gear | Survival/lethality contribution trong match rules hiện tại |
| Survival value | Medical, armor, storage, utility | Giúp player endure, extract, hoặc recover |
| Mobility cost | Armor, rigs, backpacks, carried loot | Weight, speed penalty, stamina, inertia, noise, silhouette |
| Economic value | All physical items | Credits, trader value, repair cost, crafting demand, insurance risk |
| Slot value | Storage and loot | Value per cell, access speed, valid container restrictions |
| Repair value | Durability gear | Useful life còn lại sau damage và repair loss |
| Insurance value | Insurable gear | Expected return value, return timer, mode eligibility, loss mitigation |

## Comparison Rules

| Comparison Surface | Must Compare | Must Explain |
| ------------------ | ------------ | ------------ |
| Armor vs armor | Class, zones, current/max durability, material, weight, repairability, mobility penalty | Vì sao gear class cao/nặng hơn vẫn có thể tệ hơn cho stealth, stamina, repair economy |
| Helmet/visor/headset | Protection zones, ricochet, visibility, hearing profile, weight, compatibility | Player được gì và sensory/readability cost đổi ra sao |
| Rig vs rig | Slots, hotkey access, armored/unarmored status, weight, layout, restriction | Reload/heal access có tốt hơn không và armor slot có conflict không |
| Backpack vs backpack | Cells, layout shape, weight, speed/noise penalty, collapse behavior | Capacity gain có đáng mobility/extraction risk không |
| Secure container/case | Capacity, allowed categories, persistence, unlock route | Cái gì survives death và cái gì bị rule block |
| Damaged vs repaired item | Current durability, max durability, repair cost, effective class/value | Repair có đáng không hay replacement rõ hơn |

Comparison UI không chỉ dựa vào green/red deltas. Nó phải gọi tên trade-off bằng text: "more capacity, heavier", "better class, lower repairability", "faster access, less armor", hoặc "insured but ineligible in this mode".

## Locked / Contraband / Insured Gear Rules

| State | Meaning | UI Requirement |
| ----- | ------- | -------------- |
| Trader locked | Trader/player/faction/quest requirement chưa đạt | Show requirement, progress, unlock route |
| Quest locked | Item cần cho active quest hoặc hand-in | Warn trước sell/discard/craft và route tới quest |
| Contraband | Item bị restricted sale, trade, insurance, deployment, hoặc mode behavior | Badge với exact restriction và affected actions |
| Insured | Item được bảo hiểm theo rules | Show provider/rule, return timer, mode exceptions |
| Insurance ineligible | Item không thể insure vì type, mode, ownership, hoặc contraband rule | Disable insurance CTA với readable reason |
| Protected/favorited | Player đánh dấu item an toàn khỏi bulk actions | Exclude khỏi bulk sell/discard trừ khi explicitly included |

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
