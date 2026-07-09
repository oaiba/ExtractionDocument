---
title: "Special & Exotic vũ khí"
type: docs
weight: 6
---

## Tổng Quan

Special và exotic vũ khí are variants hoặc unique models obtained thông qua bosses, quests, seasons, hoặc crafting. They offer distinct traits, cosmetics, hoặc stat tweaks mà không replacing the cốt lõi vũ khí roster. For base vũ khí stats Xem [vũ khí Arsenal](../Gameplay/WeaponArsenal.md) và [vũ khí Master Database](Weapon_Master_Database.md).

> **Cross-References:** [Loot bảng Design](../Gameplay/Loot_Table_Design.md) — boss và zone loot; [Quest & Objective hệ thống](../Gameplay/Quest_Objective_System.md) — quest rewards; [Safe House Design](../GameDesign/Safe_House_Design.md) — Workbench crafting.

---

## Boss Drop vũ khí

Unique hoặc named vũ khí that drop from cụ thể AI bosses. They have fixed traits và cannot be fully replicated by modding a base vũ khí.

| Boss (example) | vũ khí | Trait / Difference | Rarity |
| :------------- | :----- | :----------------- | :----- |
| Juggernaut | "Nemesis" LMG | Built-in incendiary rounds (DoT on hit); 5% fire rate increase | Epic |
| Warden | "Warden's M4" | Pre-modded suppressor + ACOG; unique skin; +5% ergonomics | Rare |
| Scav Commander | "Commander's AK" | High durability spawn (90–100%); no unique stat | Uncommon |

**Design rules:** Boss vũ khí are not strictly better than a fully modded base. They offer convenience (pre-built), flair (skin, name), hoặc a single unique trait. They are insurable và lootable like normal vũ khí.

---

## Quest Reward vũ khí

Named vũ khí earned by completing quest lines. Typically pre-configured và sometimes với a small stat hoặc cosmetic bonus.

| Quest (example) | vũ khí | Condition |
| :-------------- | :----- | :-------- |
| Viktor Quest Chain (final) | "Viktor's M4" | Pre-modded; unique skin; Found-in-Raid for turn-in hoặc cách dùng |
| Ada Tech Syndicate (mid) | "Ada's HK416" | Suppressed, red dot; quest-only skin |
| Faction Reputation (high) | Faction-cụ thể sidearm | Skin + minor stat (e.g. +1 mag capacity) |

Quest vũ khí are often **Found-in-Raid** khi awarded và can be used in raid, sold, hoặc turned in for follow-up quests per design. They do not break the economy; they are one-thời gian hoặc limited rewards.

---

## Seasonal Limited vũ khí

vũ khí hoặc variants introduced for a limited thời gian (e.g. one season). They may rotate out of the loot pool hoặc become permanently available later.

| Type | Description | Example |
| :--- | :----------- | :------ |
| Seasonal variant | Reskin of existing vũ khí với same stats | "Frost" M4A1 skin (Winter season) |
| Limited vũ khí | New model hoặc caliber available only trong khi season | "Icebreaker" DMR (Winter); removed hoặc readded in later season |
| Event vũ khí | Short-duration availability (e.g. 2 weeks) | Themed shotgun hoặc pistol for community event |

**Design rules:** No cốt lõi balance is locked behind seasonal exclusivity. Seasonal vũ khí are either cosmetic hoặc balanced với existing options. nếu a seasonal vũ khí is removed, người chơi who obtained it keep it (hoặc a replacement skin) per policy.

---

## Crafted vũ khí

vũ khí variants hoặc base models that can be crafted at the Safe House Workbench. Xem [Safe House Design](../GameDesign/Safe_House_Design.md) for Workbench levels và recipes.

| Workbench Level | Craftable vũ khí (example) | Materials |
| :-------------- | :------------------------- | :-------- |
| 1 | — | vũ khí not crafted at Lvl 1 |
| 2 | Base pistol (e.g. Glock 19) | Metal parts, springs, receiver component |
| 3 | Base SMG (e.g. MP5), base shotgun (e.g. 870) | Higher-tier parts, vũ khí parts |
| 4 (nếu exists) | Base AR (e.g. M4A1), rare receiver | Rare materials, quest-unlocked recipe |

Crafted vũ khí have **no inherent stat bonus** over vendor hoặc loot versions; they offer an alternative source for economy và progression. Crafting thời gian và chi phí are tuned so that crafting is not always cheaper than buying.

---

## vũ khí Condition (Found-in-Raid)

vũ khí found in raid (loot, AI, bosses) spawn với a **durability range**. This affects performance (Xem [vũ khí Modding](../Inventory_System/Gunsmith_System.md) — MOA degrades at low durability) và giá trị.

| source | Durability Range (typical) | ghi chú |
| :----- | :------------------------- | :---- |
| Containers (crates, vũ khí boxes) | 50–100% | Random roll |
| AI scavs | 40–85% | Often lower |
| AI bosses | 75–100% | Higher average |
| người chơi loot (dropped on death) | As left by người chơi | Can be 0% nếu destroyed |
| Vendor / purchase | 100% | New |
| Crafted | 100% | New |
| Quest reward | 90–100% | Often full |

**FIR (Found-in-Raid) status:** vũ khí (và attachments) that are found in raid và extracted carry FIR status. FIR is required for some quest turn-ins và affects flea market listing rules. Using the vũ khí in raid does not remove FIR until it is sold hoặc turned in; durability loss does not remove FIR.

---

## Tham Chiếu Chéo

- [vũ khí Arsenal](../Gameplay/WeaponArsenal.md) — Base vũ khí list và stats.
- [vũ khí Master Database](Weapon_Master_Database.md) — Per-vũ khí base và modded stats.
- [Loot bảng Design](../Gameplay/Loot_Table_Design.md) — Boss và zone loot tables.
- [Quest & Objective hệ thống](../Gameplay/Quest_Objective_System.md) — Quest rewards và FIR.
- [Safe House Design](../GameDesign/Safe_House_Design.md) — Workbench và crafting recipes.
- [Inventory & Gear — vũ khí Modding](../Inventory_System/Gunsmith_System.md) — Durability và MOA.
