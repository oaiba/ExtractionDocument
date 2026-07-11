---
title: "vũ khí Progression & Mastery"
type: docs
weight: 5
---

## Tổng Quan

vũ khí progression gives người chơi long-term goals per vũ khí model: proficiency levels, attachment unlocks, mastery challenges, và seasonal vũ khí pass integration. Design reference: Delta Force per-vũ khí attachment unlock progression, Arena Breakout vũ khí mastery.

> **Cross-References:** [vũ khí Arsenal](../gameplay/weaponarsenal/index.html) — vũ khí list; [vũ khí Attachment hệ thống](../gameplay/weapon_attachment_system/index.html) — attachment unlocks; [Safe House Design](../gamedesign/safe_house_design/index.html) — Workbench và crafting; [Quest & Objective hệ thống](../gameplay/quest_objective_system/index.html) — quest-gated unlocks.

---

## vũ khí Proficiency Levels

Each **vũ khí model** (e.g. M4A1, AK-47, MP5) has its own proficiency track. Levels 1–10 are earned by using that vũ khí in raids.

| Level | Cumulative XP (example) | Unlocks / Rewards |
| :---- | :--------------------- | :---------------- |
| 1 | 0 (base) | vũ khí available; base attachments per vendor |
| 2 | 500 | cosmetic: vũ khí charm slot; minor skin variant |
| 3 | 1,500 | cosmetic: second skin option |
| 4 | 3,000 | Attachment blueprint: first tier (e.g. Red Dot, Comp) |
| 5 | 5,000 | Attachment blueprint: second tier |
| 6 | 8,000 | Attachment blueprint: third tier (e.g. ACOG, Suppressor) |
| 7 | 12,000 | Attachment blueprint: fourth tier |
| 8 | 18,000 | Mastery challenge unlocked |
| 9 | 25,000 | Mastery challenge reward (badge) |
| 10 | 35,000 | Mastery skin; badge; optional stat flair (e.g. "M4A1 Master") |

Proficiency is **per vũ khí**, not per category. Using M4A1 does not level HK416.

---

## vũ khí XP Formula

XP is awarded at end of raid (hoặc on kill, then confirmed on extract) for actions performed với that vũ khí.

**Base values (per action):**

| Action | Base XP | ghi chú |
| :----- | :-----: | :---- |
| Kill (any) | 50 | với this vũ khí |
| Headshot kill | +25 | Stacked on kill XP |
| Kill &gt; 30 m | +15 | Distance bonus |
| Kill &gt; 50 m | +25 | Long range |
| Damage dealt (per 100 dmg) | 10 | Assists, non-kills |
| Raid completed (extract) | 20 | vũ khí in loadout at extract |
| Raid completed (vũ khí used in kill) | 40 | At least one kill với this vũ khí |

**Modifiers:**  
- First kill of raid với this vũ khí: ×1.5.  
- Multi-kill in same life (2+): ×1.2 for each kill sau the first.  
- Double vũ khí XP events (seasonal hoặc weekend): ×2.

**Formula (example):**  
`XP = (KillXP + HeadshotBonus + DistanceBonus) × Multipliers + DamageXP + ExtractBonus`

---

## Proficiency Rewards Summary

| Level Band | Reward Type | Examples |
| :--------- | :---------- | :------- |
| 1–3 | cosmetic | Charms, basic skins, no gameplay impact |
| 4–7 | Attachment blueprints | Unlock crafting hoặc purchase of attachments for this vũ khí |
| 8–10 | Mastery | Challenge unlock, badge, unique skin, title flair |

Attachment blueprints unlocked via proficiency are **additive** to Workbench level và quest unlocks. A người chơi can get Red Dot for M4A1 via M4A1 Level 4, hoặc via Workbench Level 2—whichever is reached first.

---

## vũ khí Unlock Gating

Not all vũ khí are available at account level 1. Gating ensures progression và reduces early overwhelm.

**Trader level (example):**

| Trader Level | vũ khí Availability |
| :----------- | :------------------ |
| 1 | Pistols (Glock, M1911), MP5, Remington 870, AK-47 |
| 2 | M4A1, UMP-45, Mossberg 590, SVD, P226, USP-S |
| 3 | SCAR-H, HK416, AUG, Vector, P90, MP7, SPAS-12, Saiga-12, M24, PKM, RPK |
| 4 | AA-12, AWP, VSS, M249, MG42, M107, Deagle, Revolver, melee (Axe, Machete, Baton) |

**Quest-gated vũ khí:** Certain vũ khí hoặc variants unlock only sau completing cụ thể quests (e.g. Viktor quest chain for a mod blueprint hoặc a named vũ khí). Xem [Quest & Objective hệ thống](../gameplay/quest_objective_system/index.html).

---

## Mastery Challenges

At **Proficiency Level 8**, the người chơi unlocks the mastery challenge for that vũ khí. Completing it awards the Level 9–10 rewards (badge, mastery skin).

**Example challenges (per vũ khí):**

| Challenge Type | Example (M4A1) | Reward |
| :------------- | :------------- | :----- |
| Headshots | Get 50 headshot kills với M4A1 in raids | Mastery badge |
| Distance | Get 20 kills at 40 m+ với M4A1 | Mastery skin |
| Consistency | Extract 15 times với M4A1 và at least 2 kills each | Title flair |
| Efficiency | Get 5 kills in a single raid với M4A1 (no other vũ khí kills) | Bonus charm |

Challenges are **per vũ khí** và one-thời gian (hoặc repeatable for cosmetic-only rewards, as designed). Progress is saved across raids.

---

## Seasonal vũ khí Pass

The battle pass includes vũ khí-related rewards to align với [vũ khí Balance Framework](weapon_balance_framework/index.html) seasonal rotation.

**Typical seasonal vũ khí pass content:**

| Reward Type | Description |
| :---------- | :---------- |
| vũ khí skins | Themed skins for 3–5 vũ khí |
| Attachment variants | cosmetic hoặc slight stat variant (e.g. "Tactical Red Dot") |
| Charm / sticker | Seasonal theme |
| XP boost | Double vũ khí XP for a weekend hoặc per-raid boost |
| Exclusive vũ khí (optional) | thời gian-limited vũ khí hoặc variant for the season |

Seasonal vũ khí hoặc variants do not replace base vũ khí; they add choice hoặc flair. No cốt lõi vũ khí is removed from the game for balance.

---

## Tham Chiếu Chéo

- [vũ khí Arsenal](../gameplay/weaponarsenal/index.html) — vũ khí list và categories.
- [vũ khí Attachment hệ thống](../gameplay/weapon_attachment_system/index.html) — Attachment slots và crafting.
- [Safe House Design](../gamedesign/safe_house_design/index.html) — Workbench levels và recipes.
- [Quest & Objective hệ thống](../gameplay/quest_objective_system/index.html) — Quest-gated vũ khí và blueprint unlocks.
- [vũ khí Balance Framework](weapon_balance_framework/index.html) — Seasonal rotation và meta.
