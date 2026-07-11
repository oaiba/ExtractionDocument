---
title: "Weapon Progression & Mastery"
type: docs
weight: 5
---

## Overview

Weapon progression gives players long-term goals per weapon model: proficiency levels, attachment unlocks, mastery challenges, and seasonal weapon pass integration. Design reference: Delta Force per-weapon attachment unlock progression, Arena Breakout weapon mastery.

> **Cross-References:** [Weapon Arsenal](../gameplay/weaponarsenal/index.html) — weapon list; [Weapon Attachment System](../gameplay/weapon_attachment_system/index.html) — attachment unlocks; [Safe House Design](../gamedesign/safe_house_design/index.html) — Workbench and crafting; [Quest & Objective System](../gameplay/quest_objective_system/index.html) — quest-gated unlocks.

---

## Weapon Proficiency Levels

Each **weapon model** (e.g. M4A1, AK-47, MP5) has its own proficiency track. Levels 1–10 are earned by using that weapon in raids.

| Level | Cumulative XP (example) | Unlocks / Rewards |
| :---- | :--------------------- | :---------------- |
| 1 | 0 (base) | Weapon available; base attachments per vendor |
| 2 | 500 | Cosmetic: weapon charm slot; minor skin variant |
| 3 | 1,500 | Cosmetic: second skin option |
| 4 | 3,000 | Attachment blueprint: first tier (e.g. Red Dot, Comp) |
| 5 | 5,000 | Attachment blueprint: second tier |
| 6 | 8,000 | Attachment blueprint: third tier (e.g. ACOG, Suppressor) |
| 7 | 12,000 | Attachment blueprint: fourth tier |
| 8 | 18,000 | Mastery challenge unlocked |
| 9 | 25,000 | Mastery challenge reward (badge) |
| 10 | 35,000 | Mastery skin; badge; optional stat flair (e.g. "M4A1 Master") |

Proficiency is **per weapon**, not per category. Using M4A1 does not level HK416.

---

## Weapon XP Formula

XP is awarded at end of raid (or on kill, then confirmed on extract) for actions performed with that weapon.

**Base values (per action):**

| Action | Base XP | Notes |
| :----- | :-----: | :---- |
| Kill (any) | 50 | With this weapon |
| Headshot kill | +25 | Stacked on kill XP |
| Kill &gt; 30 m | +15 | Distance bonus |
| Kill &gt; 50 m | +25 | Long range |
| Damage dealt (per 100 dmg) | 10 | Assists, non-kills |
| Raid completed (extract) | 20 | Weapon in loadout at extract |
| Raid completed (weapon used in kill) | 40 | At least one kill with this weapon |

**Modifiers:**  
- First kill of raid with this weapon: ×1.5.  
- Multi-kill in same life (2+): ×1.2 for each kill after the first.  
- Double weapon XP events (seasonal or weekend): ×2.

**Formula (example):**  
`XP = (KillXP + HeadshotBonus + DistanceBonus) × Multipliers + DamageXP + ExtractBonus`

---

## Proficiency Rewards Summary

| Level Band | Reward Type | Examples |
| :--------- | :---------- | :------- |
| 1–3 | Cosmetic | Charms, basic skins, no gameplay impact |
| 4–7 | Attachment blueprints | Unlock crafting or purchase of attachments for this weapon |
| 8–10 | Mastery | Challenge unlock, badge, unique skin, title flair |

Attachment blueprints unlocked via proficiency are **additive** to Workbench level and quest unlocks. A player can get Red Dot for M4A1 via M4A1 Level 4, or via Workbench Level 2—whichever is reached first.

---

## Weapon Unlock Gating

Not all weapons are available at account level 1. Gating ensures progression and reduces early overwhelm.

**Trader level (example):**

| Trader Level | Weapon Availability |
| :----------- | :------------------ |
| 1 | Pistols (Glock, M1911), MP5, Remington 870, AK-47 |
| 2 | M4A1, UMP-45, Mossberg 590, SVD, P226, USP-S |
| 3 | SCAR-H, HK416, AUG, Vector, P90, MP7, SPAS-12, Saiga-12, M24, PKM, RPK |
| 4 | AA-12, AWP, VSS, M249, MG42, M107, Deagle, Revolver, melee (Axe, Machete, Baton) |

**Quest-gated weapons:** Certain weapons or variants unlock only after completing specific quests (e.g. Viktor quest chain for a mod blueprint or a named weapon). See [Quest & Objective System](../gameplay/quest_objective_system/index.html).

---

## Mastery Challenges

At **Proficiency Level 8**, the player unlocks the mastery challenge for that weapon. Completing it awards the Level 9–10 rewards (badge, mastery skin).

**Example challenges (per weapon):**

| Challenge Type | Example (M4A1) | Reward |
| :------------- | :------------- | :----- |
| Headshots | Get 50 headshot kills with M4A1 in raids | Mastery badge |
| Distance | Get 20 kills at 40 m+ with M4A1 | Mastery skin |
| Consistency | Extract 15 times with M4A1 and at least 2 kills each | Title flair |
| Efficiency | Get 5 kills in a single raid with M4A1 (no other weapon kills) | Bonus charm |

Challenges are **per weapon** and one-time (or repeatable for cosmetic-only rewards, as designed). Progress is saved across raids.

---

## Seasonal Weapon Pass

The battle pass includes weapon-related rewards to align with [Weapon Balance Framework](weapon_balance_framework/index.html) seasonal rotation.

**Typical seasonal weapon pass content:**

| Reward Type | Description |
| :---------- | :---------- |
| Weapon skins | Themed skins for 3–5 weapons |
| Attachment variants | Cosmetic or slight stat variant (e.g. "Tactical Red Dot") |
| Charm / sticker | Seasonal theme |
| XP boost | Double weapon XP for a weekend or per-raid boost |
| Exclusive weapon (optional) | Time-limited weapon or variant for the season |

Seasonal weapons or variants do not replace base weapons; they add choice or flair. No core weapon is removed from the game for balance.

---

## Cross-References

- [Weapon Arsenal](../gameplay/weaponarsenal/index.html) — Weapon list and categories.
- [Weapon Attachment System](../gameplay/weapon_attachment_system/index.html) — Attachment slots and crafting.
- [Safe House Design](../gamedesign/safe_house_design/index.html) — Workbench levels and recipes.
- [Quest & Objective System](../gameplay/quest_objective_system/index.html) — Quest-gated weapon and blueprint unlocks.
- [Weapon Balance Framework](weapon_balance_framework/index.html) — Seasonal rotation and meta.
