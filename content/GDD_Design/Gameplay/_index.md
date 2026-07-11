---
title: Gameplay Mechanics
linkTitle: Gameplay
type: docs
weight: 6
---

# The Engine of Interaction

This section details the specific **interaction mechanics** — how players physically interact with the world and its systems. While [Game Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/GameDesign/README.md) covers high-level system specifications with concrete numbers, and [Combat](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Combat/README.md) covers weapons and armor, this section focuses on the _feel_, _flow_, and _design intent_ behind each mechanic.

> **Cross-Reference**: For per-minute match timelines, control scheme layouts, and raw balance numbers, see [Core Gameplay Mechanics](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/GameDesign/CoreGameplay/README.md). For weapon arsenals and item catalogue, see the [Weapon Arsenal](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/WeaponArsenal/README.md) and [Items & Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/ItemsAndGear/README.md) GDDs in this section.

{{< cards cols="2" >}}
{{< card link="CoreLoop" title="Core Gameplay Loop" icon="refresh" subtitle="The five-phase extraction cycle, psychological hooks, and economy design." >}}
{{< card link="Movement_and_Stamina" title="Movement & Stamina" icon="pencil" subtitle="Movement states, dual stamina system, weight encumbrance, and surface noise." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Gear_Mechanics" title="Gear Mechanics" icon="briefcase" subtitle="How loadout (weight, rig, armor) affects mobility, stamina, and extraction flow." >}}
{{< card link="Medical_System" title="Medical System" icon="heart" subtitle="Body part health, injury types, healing triage, toxicity, and overdose." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Looting_Interactions" title="Looting & Inventory" icon="collection" subtitle="Container interaction, grid inventory, secure container, keys, and barter items." >}}
{{< card link="Hero_Abilities" title="Hero Abilities" icon="user" subtitle="Operator classes, passive/active/signature abilities, and Operator Mastery." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Environmental_Hazards" title="Environmental Hazards" icon="cloud" subtitle="Weather, zone hazards, contamination, dynamic events, and raid timer." >}}
{{< card link="Extraction_Mechanics" title="Extraction Mechanics" icon="logout" subtitle="Zone types, extraction process, interruption rules, and counter-play." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="LOS_Fog_Visibility" title="LOS & Fog of War" icon="eye" subtitle="Line of sight, visibility layers, shared team vision, and minimap fog." >}}
{{< card link="Camera_System" title="Camera System" icon="camera" subtitle="Top-down camera: altitude states, zoom, indoor geometry, and mobile controls." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="AI_Enemy_Behavior" title="AI & Enemy Behavior" icon="chip" subtitle="Enemy types, alert states, bosses, Player-as-Scav, and karma system." >}}
{{< card link="Matchmaking_Lobby" title="Matchmaking & Lobby" icon="server" subtitle="Queue system, squad config, ABMM, cross-platform pools, and reconnect rules." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Hydration_Energy" title="Hydration & Energy" icon="beaker" subtitle="Survival bars, food/water items, threshold effects, and stomach damage link." >}}
{{< card link="../GameDesign/Safe_House_Design" title="Safe House" icon="home" subtitle="Operator base, Stash Room, Trophy Vault, Workbench, crafting, and seasonal wipe. See GameDesign." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Quest_Objective_System" title="Quest & Objectives" icon="flag" subtitle="5 quest categories, 5 NPC traders, quest chains, daily/weekly tasks, and HUD integration." >}}
{{< card link="Loot_Table_Design" title="Loot Table Design" icon="archive" subtitle="Zone-tier loot tables, AI/boss loot, dynamic density, seasonal modifiers." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Downstate_Revive" title="Downstate & Revive" icon="heart" subtitle="Downed HP pool, revive process, operator interactions, and escalating bleedout." >}}
{{< card link="Combat_Feel_Topdown" title="Combat Feel (Top-Down)" icon="cursor-click" subtitle="Aim cone recoil, cover footprint system, suppression, range degradation." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Anti_Cheat_Fair_Play" title="Anti-Cheat & Fair Play" icon="lock-closed" subtitle="Server-authoritative architecture, cheat vector prevention, reporting, soft isolation." >}}
{{< card link="Post_Game_Debrief" title="Post-Game Debrief" icon="chart-bar" subtitle="Outcome screen, XP breakdown, loot summary, combat stats, death replay." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Operator_Synergy_Guide" title="Operator Synergy Guide" icon="puzzle" subtitle="4 Tier 1 combos, counter matrix, meta compositions by playstyle, and balance guardrails." >}}
{{< card link="Weapon_Attachment_System" title="Weapon Attachment System" icon="cog" subtitle="8 slot types, stat trade-offs, in-raid swap, preset system, and Workbench crafting gates." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Gameplay_Review_Checklist" title="Review Checklist & Benchmark" icon="check" subtitle="Pillar alignment, competitor benchmark, cross-platform review, and consistency fixes." >}}
{{< /cards >}}

## Production Readiness References

{{< cards cols="2" >}}
{{< card link="AI_Enemy_Behavior" title="AI Production Contract" icon="chip" subtitle="Enemy roles, counterplay, detection tells, anti-frustration, loot, and telemetry." >}}
{{< card link="Anti_Cheat_Fair_Play" title="Fair Play Production Contract" icon="lock-closed" subtitle="Server authority, evidence, enforcement, recovery, privacy, and QA." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="WeaponArsenal" title="Weapon Arsenal" icon="adjustments" subtitle="Full weapon bible: 5 primary categories, ammo caliber tables, attachment reference, damage/recoil/TTK mechanics." >}}
{{< card link="ItemsAndGear" title="Items & Gear Catalogue" icon="archive" subtitle="Armor, medical, consumables, tactical gear, keys, crafting materials — all item specs, values, and grid sizes." >}}
{{< /cards >}}
