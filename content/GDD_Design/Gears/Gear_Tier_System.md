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

## Tier vs Rarity vs Power

Tier, rarity, and practical power are related but not identical. UI must avoid implying that a rarer item is always strictly stronger or that gear has upgrade levels.

| Concept | Meaning | What It Controls | What It Must Not Imply |
| ------- | ------- | ---------------- | ---------------------- |
| Tier | Balance/progression bracket | Loot table bands, trader access, cost curve, optional raid brackets | A per-item level or upgrade stage |
| Rarity | Availability, presentation, and economy signal | Drop frequency, badge treatment, collection feel, trader scarcity | Automatic combat superiority |
| Practical power | The actual effect of item stats in context | Armor class, zones, durability, weight, capacity, access speed, repairability | That one item is best in every loadout |
| Player/trader level | Access gate for systems and stock | Unlock timing and shop/trader availability | Stat scaling on the gear item itself |

Armor class, durability, material, coverage zones, storage capacity, access speed, weight, and repairability define real gear value. Tier and rarity help players read progression and scarcity, but comparison UI must still explain the actual trade-off.

## Rarity Meaning Table

| Rarity | Availability Meaning | UI Meaning | Design Expectation |
| ------ | -------------------- | ---------- | ------------------ |
| Common | Early access, frequent loot, basic trader stock | Low-intensity badge, plain label | Reliable baseline, not trash by default |
| Uncommon | Slightly gated, more specialized | Clear badge and filter support | One notable advantage or better efficiency |
| Rare | Mid-progression, contested loot, reputation gates | Strong badge, comparison worth surfacing | Meaningful trade-off versus weight/cost/repair |
| Epic | Late stock, event/quest/crafting relevance | Premium-looking non-commerce badge | Strong situational role, not universally best |
| Legendary | Endgame, rare event, high-risk or prestige | Highest scarcity badge with text label | Aspirational, expensive, heavy/risky, or hard to repair |

Rarity is not a monetization promise. Paid offers may sell cosmetics that use rarity-like presentation, but paid rarity must not grant armor class, storage capacity, recoil, audio, visibility, or durability advantage.

## Gear Value Model

| Value Type | Applies To | Meaning |
| ---------- | ---------- | ------- |
| Combat value | Armor, helmets, weapons, ammo-related gear | Survival/lethality contribution under current match rules |
| Survival value | Medical, armor, storage, utility | Helps player endure, extract, or recover |
| Mobility cost | Armor, rigs, backpacks, carried loot | Weight, speed penalty, stamina, inertia, noise, silhouette |
| Economic value | All physical items | Credits, trader value, repair cost, crafting demand, insurance risk |
| Slot value | Storage and loot | Value per cell, access speed, valid container restrictions |
| Repair value | Durability gear | How much useful life remains after damage and repair loss |
| Insurance value | Insurable gear | Expected return value, return timer, mode eligibility, and loss mitigation |

## Comparison Rules

| Comparison Surface | Must Compare | Must Explain |
| ------------------ | ------------ | ------------ |
| Armor vs armor | Class, zones, current/max durability, material, weight, repairability, mobility penalty | Why heavier/higher-class gear may still be worse for stealth, stamina, or repair economy |
| Helmet/visor/headset | Protection zones, ricochet, visibility, hearing profile, weight, compatibility | What the player gains and what sensory/readability cost changes |
| Rig vs rig | Slots, hotkey access, armored/unarmored status, weight, layout, restriction | Whether reload/heal access improves and whether armor slot conflicts |
| Backpack vs backpack | Cells, layout shape, weight, speed/noise penalty, collapse behavior | Whether capacity gain is worth mobility and extraction risk |
| Secure container/case | Capacity, allowed categories, persistence, unlock route | What survives death and what is blocked by rule |
| Damaged vs repaired item | Current durability, max durability, repair cost, effective class/value | Whether repair is worth it or replacement is clearer |

Comparison UI should not rely on green/red deltas alone. It must name the trade-off in text: "more capacity, heavier", "better class, lower repairability", "faster access, less armor", or "insured but ineligible in this mode".

## Locked / Contraband / Insured Gear Rules

| State | Meaning | UI Requirement |
| ----- | ------- | -------------- |
| Trader locked | Trader/player/faction/quest requirement not met | Show requirement, progress, and unlock route |
| Quest locked | Item needed for active quest or hand-in | Warn before sell/discard/craft and route to quest |
| Contraband | Item has restricted sale, trade, insurance, deployment, or mode behavior | Badge with exact restriction and affected actions |
| Insured | Item is covered by insurance rules | Show provider/rule, return timer, and mode exceptions |
| Insurance ineligible | Item cannot be insured due to type, mode, ownership, or contraband rule | Disable insurance CTA with readable reason |
| Protected/favorited | Player marked item as safe from bulk actions | Exclude from bulk sell/discard unless explicitly included |

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
