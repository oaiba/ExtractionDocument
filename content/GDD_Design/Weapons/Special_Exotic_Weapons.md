---
title: "Special & Exotic Weapons"
type: docs
weight: 6
---

## Overview

Special and exotic weapons are variants or unique models obtained through bosses, quests, seasons, or crafting. They offer distinct traits, cosmetics, or stat tweaks without replacing the core weapon roster. For base weapon stats see [Weapon Arsenal](../gameplay/weaponarsenal/index.html) and [Weapon Master Database](weapon_master_database/index.html).

> **Cross-References:** [Loot Table Design](../gameplay/loot_table_design/index.html) — boss and zone loot; [Quest & Objective System](../gameplay/quest_objective_system/index.html) — quest rewards; [Safe House Design](../gamedesign/safe_house_design/index.html) — Workbench crafting.

---

## Boss Drop Weapons

Unique or named weapons that drop from specific AI bosses. They have fixed traits and cannot be fully replicated by modding a base weapon.

| Boss (example) | Weapon | Trait / Difference | Rarity |
| :------------- | :----- | :----------------- | :----- |
| Juggernaut | "Nemesis" LMG | Built-in incendiary rounds (DoT on hit); 5% fire rate increase | Epic |
| Warden | "Warden's M4" | Pre-modded suppressor + ACOG; unique skin; +5% ergonomics | Rare |
| Scav Commander | "Commander's AK" | High durability spawn (90–100%); no unique stat | Uncommon |

**Design rules:** Boss weapons are not strictly better than a fully modded base. They offer convenience (pre-built), flair (skin, name), or a single unique trait. They are insurable and lootable like normal weapons.

---

## Quest Reward Weapons

Named weapons earned by completing quest lines. Typically pre-configured and sometimes with a small stat or cosmetic bonus.

| Quest (example) | Weapon | Condition |
| :-------------- | :----- | :-------- |
| Viktor Quest Chain (final) | "Viktor's M4" | Pre-modded; unique skin; Found-in-Raid for turn-in or use |
| Ada Tech Syndicate (mid) | "Ada's HK416" | Suppressed, red dot; quest-only skin |
| Faction Reputation (high) | Faction-specific sidearm | Skin + minor stat (e.g. +1 mag capacity) |

Quest weapons are often **Found-in-Raid** when awarded and can be used in raid, sold, or turned in for follow-up quests per design. They do not break the economy; they are one-time or limited rewards.

---

## Seasonal Limited Weapons

Weapons or variants introduced for a limited time (e.g. one season). They may rotate out of the loot pool or become permanently available later.

| Type | Description | Example |
| :--- | :----------- | :------ |
| Seasonal variant | Reskin of existing weapon with same stats | "Frost" M4A1 skin (Winter season) |
| Limited weapon | New model or caliber available only during season | "Icebreaker" DMR (Winter); removed or readded in later season |
| Event weapon | Short-duration availability (e.g. 2 weeks) | Themed shotgun or pistol for community event |

**Design rules:** No core balance is locked behind seasonal exclusivity. Seasonal weapons are either cosmetic or balanced with existing options. If a seasonal weapon is removed, players who obtained it keep it (or a replacement skin) per policy.

---

## Crafted Weapons

Weapon variants or base models that can be crafted at the Safe House Workbench. See [Safe House Design](../gamedesign/safe_house_design/index.html) for Workbench levels and recipes.

| Workbench Level | Craftable Weapon (example) | Materials |
| :-------------- | :------------------------- | :-------- |
| 1 | — | Weapons not crafted at Lvl 1 |
| 2 | Base pistol (e.g. Glock 19) | Metal parts, springs, receiver component |
| 3 | Base SMG (e.g. MP5), base shotgun (e.g. 870) | Higher-tier parts, weapon parts |
| 4 (if exists) | Base AR (e.g. M4A1), rare receiver | Rare materials, quest-unlocked recipe |

Crafted weapons have **no inherent stat bonus** over vendor or loot versions; they offer an alternative source for economy and progression. Crafting time and cost are tuned so that crafting is not always cheaper than buying.

---

## Weapon Condition (Found-in-Raid)

Weapons found in raid (loot, AI, bosses) spawn with a **durability range**. This affects performance (see [Weapon Modding](../inventory_system/gunsmith_system/index.html) — MOA degrades at low durability) and value.

| Source | Durability Range (typical) | Notes |
| :----- | :------------------------- | :---- |
| Containers (crates, weapon boxes) | 50–100% | Random roll |
| AI scavs | 40–85% | Often lower |
| AI bosses | 75–100% | Higher average |
| Player loot (dropped on death) | As left by player | Can be 0% if destroyed |
| Vendor / purchase | 100% | New |
| Crafted | 100% | New |
| Quest reward | 90–100% | Often full |

**FIR (Found-in-Raid) status:** Weapons (and attachments) that are found in raid and extracted carry FIR status. FIR is required for some quest turn-ins and affects flea market listing rules. Using the weapon in raid does not remove FIR until it is sold or turned in; durability loss does not remove FIR.

---

## Cross-References

- [Weapon Arsenal](../gameplay/weaponarsenal/index.html) — Base weapon list and stats.
- [Weapon Master Database](weapon_master_database/index.html) — Per-weapon base and modded stats.
- [Loot Table Design](../gameplay/loot_table_design/index.html) — Boss and zone loot tables.
- [Quest & Objective System](../gameplay/quest_objective_system/index.html) — Quest rewards and FIR.
- [Safe House Design](../gamedesign/safe_house_design/index.html) — Workbench and crafting recipes.
- [Inventory & Gear — Weapon Modding](../inventory_system/gunsmith_system/index.html) — Durability and MOA.
