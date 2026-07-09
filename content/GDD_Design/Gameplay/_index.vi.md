---
title: "Gameplay Mechanics"
linkTitle: Gameplay
type: docs
weight: 6
---

# Cỗ Máy Tương Tác

Section này mô tả chi tiết các **interaction mechanics** cụ thể: người chơi tương tác vật lý với thế giới và hệ thống như thế nào. Trong khi [Game Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/GameDesign/README.md) bao phủ spec hệ thống cấp cao với số liệu cụ thể, và [Combat](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Combat/README.md) bao phủ weapon và armor, section này tập trung vào _feel_, _flow_, và _design intent_ phía sau từng mechanic.

> **Cross-Reference**: Với timeline trận theo phút, layout control scheme, và raw balance number, xem [Core Gameplay Mechanics](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/GameDesign/CoreGameplay/README.md). Với weapon arsenal và item catalogue, xem GDD [Weapon Arsenal](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/WeaponArsenal/README.md) và [Items & Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/ItemsAndGear/README.md) trong section này.

{{< cards cols="2" >}}
{{< card link="CoreLoop" title="Core Gameplay Loop" icon="refresh" subtitle="Chu kỳ extraction năm phase, psychological hook, và economy design." >}}
{{< card link="Movement_and_Stamina" title="Movement & Stamina" icon="pencil" subtitle="Movement state, dual stamina system, weight encumbrance, và surface noise." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Gear_Mechanics" title="Gear Mechanics" icon="briefcase" subtitle="Loadout (weight, rig, armor) ảnh hưởng mobility, stamina, và extraction flow như thế nào." >}}
{{< card link="Medical_System" title="Medical System" icon="heart" subtitle="Body part health, injury type, healing triage, toxicity, và overdose." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Looting_Interactions" title="Looting & Inventory" icon="collection" subtitle="Container interaction, grid inventory, secure container, key, và barter item." >}}
{{< card link="Hero_Abilities" title="Hero Abilities" icon="user" subtitle="Operator class, passive/active/signature ability, và Operator Mastery." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Environmental_Hazards" title="Environmental Hazards" icon="cloud" subtitle="Weather, zone hazard, contamination, dynamic event, và raid timer." >}}
{{< card link="Extraction_Mechanics" title="Extraction Mechanics" icon="logout" subtitle="Zone type, extraction process, interruption rule, và counter-play." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="LOS_Fog_Visibility" title="LOS & Fog of War" icon="eye" subtitle="Line of sight, visibility layer, shared team vision, và minimap fog." >}}
{{< card link="Camera_System" title="Camera System" icon="camera" subtitle="Top-down camera: altitude state, zoom, indoor geometry, và mobile control." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="AI_Enemy_Behavior" title="AI & Enemy Behavior" icon="chip" subtitle="Enemy type, alert state, boss, Player-as-Scav, và karma system." >}}
{{< card link="Matchmaking_Lobby" title="Matchmaking & Lobby" icon="server" subtitle="Queue system, squad config, ABMM, cross-platform pool, và reconnect rule." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Hydration_Energy" title="Hydration & Energy" icon="beaker" subtitle="Survival bar, food/water item, threshold effect, và stomach damage link." >}}
{{< card link="../GameDesign/Safe_House_Design" title="Safe House" icon="home" subtitle="Operator base, Stash Room, Trophy Vault, Workbench, crafting, và seasonal wipe. Xem GameDesign." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Quest_Objective_System" title="Quest & Objectives" icon="flag" subtitle="5 quest category, 5 NPC trader, quest chain, daily/weekly task, và HUD integration." >}}
{{< card link="Loot_Table_Design" title="Loot Table Design" icon="archive" subtitle="Zone-tier loot table, AI/boss loot, dynamic density, seasonal modifier." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Downstate_Revive" title="Downstate & Revive" icon="heart" subtitle="Downed HP pool, revive process, operator interaction, và escalating bleedout." >}}
{{< card link="Combat_Feel_Topdown" title="Combat Feel (Top-Down)" icon="cursor-click" subtitle="Aim cone recoil, cover footprint system, suppression, range degradation." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Anti_Cheat_Fair_Play" title="Anti-Cheat & Fair Play" icon="lock-closed" subtitle="Server-authoritative architecture, cheat vector prevention, reporting, soft isolation." >}}
{{< card link="Post_Game_Debrief" title="Post-Game Debrief" icon="chart-bar" subtitle="Outcome screen, XP breakdown, loot summary, combat stat, death replay." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Operator_Synergy_Guide" title="Operator Synergy Guide" icon="puzzle" subtitle="4 Tier 1 combo, counter matrix, meta composition theo playstyle, và balance guardrail." >}}
{{< card link="Weapon_Attachment_System" title="Weapon Attachment System" icon="cog" subtitle="8 slot type, stat trade-off, in-raid swap, preset system, và Workbench crafting gate." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Gameplay_Review_Checklist" title="Review Checklist & Benchmark" icon="check" subtitle="Pillar alignment, competitor benchmark, cross-platform review, và consistency fix." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="WeaponArsenal" title="Weapon Arsenal" icon="adjustments" subtitle="Weapon bible đầy đủ: 5 primary category, ammo caliber table, attachment reference, damage/recoil/TTK mechanic." >}}
{{< card link="ItemsAndGear" title="Items & Gear Catalogue" icon="archive" subtitle="Armor, medical, consumable, tactical gear, key, crafting material; toàn bộ item spec, value, và grid size." >}}
{{< /cards >}}
