---
title: "Narrative & World"
linkTitle: Narrative World
type: docs
weight: 5
sidebar:
  open: false
---

### Story Và World Không Thể Tách Rời

Trong extraction shooter, **map CHÍNH LÀ câu chuyện**. Neo-Asia Industrial Corridor không chỉ cung cấp terrain; nó là một nhân vật có lịch sử, bi kịch, và những bí mật đáng để chết vì chúng. Mỗi location người chơi raid từng là nơi con người thật đã làm việc, yêu thương, và chết.

Section này chứa toàn bộ tài liệu narrative và world design cho game. Story writer, level designer, và narrative artist nên xem đây là **một reference thống nhất** chứ không phải các discipline tách rời.

> **Cross-References:** Với quest mechanics và systems, xem [Gameplay/Quest & Objectives](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/Quest_Objective_System/README.md). Với map balance metric và extraction zone spec, xem [Gameplay/Loot Table Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gameplay/Loot_Table_Design/README.md). Với operator character profile, xem [Characters](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/README.md).

***

### Tài Liệu Narrative

{{< cards cols="2" >}}
{{< card link="Narrative" title="Narrative Design Bible" icon="pencil" subtitle="Tone guide, thematic pillar, storytelling hierarchy, dialogue guideline, và pacing." >}}
{{< card link="Backstory" title="World History & Backstory" icon="book-open" subtitle="Timeline đầy đủ 2020-2036, The Collapse, Project Prometheus, lịch sử khu vực, mystery." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Factions" title="Factions" icon="user-group" subtitle="4 faction profile, NPC detail, reputation system, double-agent mechanic, territory influence." >}}
{{< card link="QuestLines" title="Quest Lines" icon="clipboard-list" subtitle="Main story chapter, faction quest, daily/weekly system, hidden quest, branching design." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="Lore_Delivery" title="Lore Delivery Systems" icon="document-text" subtitle="Audio log, epistolary framework, codex system, item description, và lore gating." >}}
{{< card link="FactionTerritories" title="Faction Territories" icon="map" subtitle="Ai kiểm soát khu nào; faction zone ownership theo map, territorial conflict, và seasonal shift." >}}
{{< /cards >}}

***

### Tài Liệu World & Map

{{< cards cols="2" >}}
{{< card link="MapBible" title="Map Design Bible" icon="globe-alt" subtitle="Map philosophy, zone type, design principle, environmental storytelling, cover, verticality." >}}
{{< card link="MapLayouts" title="Map Layouts & Tactical Data" icon="puzzle" subtitle="POI tier, hotspot, choke point, extraction point, traffic flow analysis." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="LootDistribution" title="Loot Distribution & Heatmaps" icon="chart-bar" subtitle="Zone loot heatmap, skill-based route, spawn timing, balance KPI." >}}
{{< /cards >}}

***

### Tài Liệu Lore Theo Map

Mỗi map có một tài liệu lore + layout thống nhất, nối lịch sử, atmosphere, audio log, câu chuyện POI, và tactical data.

{{< cards cols="2" >}}
{{< card link="MapLore_Industrial" title="Industrial Decay (Sector 7)" icon="cog" subtitle="The Origin Zone. Reactor Tower, Prometheus Labs, Corporate Collapse; toàn bộ lore và layout được thống nhất." >}}
{{< card link="MapLore_Urban" title="Urban Ruins (District 14)" icon="office-building" subtitle="Nơi dân thường sống sót, chết, và đưa ra lựa chọn khó. Mall, Subway, Hotel; lore + tactical spec." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="MapLore_Military" title="Firebase Delta (Future - S3)" icon="shield-check" subtitle="Last stand của quân đội. Classified intel, prototype weapon, Nuclear Option debate." >}}
{{< /cards >}}

***

### Integration Notes

> Thư mục này thay thế và hợp nhất hai thư mục cũ **Story/** và **World/**. Cả hai hiện đã deprecated bằng redirect notice trỏ về đây. Không mất nội dung nào; toàn bộ content đã được tổ chức lại và cross-link.

| Vị Trí Cũ | Hiện Nằm Trong |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Story/Narrative.md` | [Narrative Design Bible](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Narrative/README.md) |
| `Story/Backstory.md` | [World History & Backstory](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Backstory/README.md) |
| `Story/Factions.md` | [Factions](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Factions/README.md) |
| `Story/QuestLines.md` | [Quest Lines](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/QuestLines/README.md) |
| `Story/Lore_Delivery.md` | [Lore Delivery Systems](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Lore_Delivery/README.md) |
| `World/MapDesign.md` + `World/EnvironmentalNarrative_Guidelines.md` | [Map Design Bible](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapBible/README.md) |
| `World/MapLayouts.md` | [Map Layouts & Tactical Data](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLayouts/README.md) |
| `World/LootDistribution.md` | [Loot Distribution](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/LootDistribution/README.md) |
| `World/EnvironmentalNarrative.md` | [Industrial Decay Map Lore](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLore_Industrial/README.md) + [Lore Delivery](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/Lore_Delivery/README.md) |
| `World/MapDesign_IndustrialZone.md` | [Industrial Decay Map Lore](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLore_Industrial/README.md) |
| `World/MapDesign_NeonSlums.md` | [Urban Ruins Map Lore](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLore_Urban/README.md) |
