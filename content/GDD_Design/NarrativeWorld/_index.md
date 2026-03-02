---
title: "Narrative & World"
linkTitle: "Narrative World"
type: docs
weight: 5
sidebar:
  open: true
---

## Story and World Are Inseparable

In an extraction shooter, the **map IS the story**. The Neo-Asia Industrial Corridor doesn't just provide terrain — it is a character with a history, a tragedy, and secrets worth dying for. Every location players raid was once a place where real people worked, loved, and died.

This section contains all narrative and world design documentation for the game. Story writers, level designers, and narrative artists should treat this as a **single unified reference** — not separate disciplines.

> **Cross-References:** For quest mechanics and systems, see [Gameplay/Quest & Objectives](../Gameplay/Quest_Objective_System). For map balance metrics and extraction zone specs, see [Gameplay/Loot Table Design](../Gameplay/Loot_Table_Design). For operator character profiles, see [Characters](../Characters/).

---

## 📖 Narrative Documents

{{< cards cols="2" >}}
  {{< card link="Narrative" title="Narrative Design Bible" icon="pencil" subtitle="Tone guide, thematic pillars, storytelling hierarchy, dialogue guidelines, and pacing." >}}
  {{< card link="Backstory" title="World History & Backstory" icon="book-open" subtitle="Full timeline 2020–2036, The Collapse, Project Prometheus, regional history, mysteries." >}}
{{< /cards >}}

{{< cards cols="2" >}}
  {{< card link="Factions" title="Factions" icon="user-group" subtitle="4 faction profiles, NPC details, reputation systems, double-agent mechanics, territory influence." >}}
  {{< card link="QuestLines" title="Quest Lines" icon="clipboard-list" subtitle="Main story chapters, faction quests, daily/weekly system, hidden quests, branching design." >}}
{{< /cards >}}

{{< cards cols="2" >}}
  {{< card link="Lore_Delivery" title="Lore Delivery Systems" icon="document-text" subtitle="Audio logs, epistolary framework, codex system, item descriptions, and lore gating." >}}
  {{< card link="FactionTerritories" title="Faction Territories" icon="map" subtitle="Who controls what — faction zone ownership per map, territorial conflict, and seasonal shifts." >}}
{{< /cards >}}

---

## 🗺️ World & Map Documents

{{< cards cols="2" >}}
  {{< card link="MapBible" title="Map Design Bible" icon="globe-alt" subtitle="Map philosophy, zone types, design principles, environmental storytelling, cover, verticality." >}}
  {{< card link="MapLayouts" title="Map Layouts & Tactical Data" icon="puzzle" subtitle="POI tiers, hotspots, choke points, extraction points, traffic flow analysis." >}}
{{< /cards >}}

{{< cards cols="2" >}}
  {{< card link="LootDistribution" title="Loot Distribution & Heatmaps" icon="chart-bar" subtitle="Zone loot heatmaps, skill-based routes, spawn timing, balance KPIs." >}}
{{< /cards >}}

---

## 🏭 Per-Map Lore Documents

Each map has a unified lore + layout document tying together history, atmosphere, audio logs, POI stories, and tactical data.

{{< cards cols="2" >}}
  {{< card link="MapLore_Industrial" title="Industrial Decay (Sector 7)" icon="cog" subtitle="The Origin Zone. Reactor Tower, Prometheus Labs, the Corporate Collapse — all lore and layout unified." >}}
  {{< card link="MapLore_Urban" title="Urban Ruins (District 14)" icon="office-building" subtitle="Where civilians survived, died, and made hard choices. Mall, Subway, Hotel — lore + tactical spec." >}}
{{< /cards >}}

{{< cards cols="2" >}}
  {{< card link="MapLore_Military" title="Firebase Delta (Future — S3)" icon="shield-check" subtitle="The military's last stand. Classified intel, prototype weapons, the Nuclear Option debate." >}}
{{< /cards >}}

---

## Integration Notes

> This directory replaces and unifies the former **Story/** and **World/** directories. Both are now deprecated with redirect notices pointing here. No content was lost — all content has been reorganized and cross-linked.

| Former Location | Now In |
| :-------------- | :----- |
| `Story/Narrative.md` | [Narrative Design Bible](Narrative) |
| `Story/Backstory.md` | [World History & Backstory](Backstory) |
| `Story/Factions.md` | [Factions](Factions) |
| `Story/QuestLines.md` | [Quest Lines](QuestLines) |
| `Story/Lore_Delivery.md` | [Lore Delivery Systems](Lore_Delivery) |
| `World/MapDesign.md` + `World/EnvironmentalNarrative_Guidelines.md` | [Map Design Bible](MapBible) |
| `World/MapLayouts.md` | [Map Layouts & Tactical Data](MapLayouts) |
| `World/LootDistribution.md` | [Loot Distribution](LootDistribution) |
| `World/EnvironmentalNarrative.md` | [Industrial Decay Map Lore](MapLore_Industrial) + [Lore Delivery](Lore_Delivery) |
| `World/MapDesign_IndustrialZone.md` | [Industrial Decay Map Lore](MapLore_Industrial) |
| `World/MapDesign_NeonSlums.md` | [Urban Ruins Map Lore](MapLore_Urban) |
