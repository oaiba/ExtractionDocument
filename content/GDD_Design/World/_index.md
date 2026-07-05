---
title: World & Level Design
linkTitle: World
type: docs
weight: 12
---

# World & Level Design

> \[!IMPORTANT] **📋 Directory Migration Notice:** The Story & World documentation has been merged into a unified [**NarrativeWorld/**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/README.md) section. The map design and environmental narrative files below are preserved for reference, but the **canonical, up-to-date GDDs** are in `NarrativeWorld/`. New work should be done there.
>
> **New canonical documents:** [Map Design Bible](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapBible/README.md) (merges `MapDesign.md` + `EnvironmentalNarrative_Guidelines.md`), [Industrial Decay Map Lore](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLore_Industrial/README.md), [Urban Ruins Map Lore](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLore_Urban/README.md), [Faction Territories](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/FactionTerritories/README.md).

### 🌍 The Map is the Main Character

In an extraction shooter, map knowledge is the highest skill ceiling. Our levels are designed with specific **choke points**, **sniping lanes**, and **flank routes** to force player interaction.

#### Level Design Principles

* **The Swiss Cheese:** No dead ends. Every room has at least two exits.
* **Verticality:** Power positions exist but always have counters.
* **Landmarks:** Distinct visual anchors so players never need a compass to know where they are.

***

#### Core Maps & Zones

{{< cards cols="3" >}}
{{< card link="mapdesign_industrialzone.html" title="Industrial Zone" icon="cog" subtitle="CQC focus. Vertical factories. High loot density." >}}
{{< card link="mapdesign_neonslums.html" title="Neon Slums" icon="office-building" subtitle="Urban warfare. Tight alleys and rooftops." >}}
{{< card link="mapdesign_wilderness.html" title="The Wilderness" icon="cloud" subtitle="Long range. Forests and open fields." >}}
{{< /cards >}}

***

#### Systems & Mechanics

{{< cards cols="2" >}}
{{< card link="lootdistribution.html" title="Loot Economy" icon="gift" subtitle="Spawning logic, container types, and heatmaps." >}}
{{< card link="maplayouts.html" title="Blueprints" icon="map" subtitle="Top-down views and tactical overlays." >}}
{{< card link="environmentalnarrative.html" title="Storytelling" icon="book-open" subtitle="Telling stories without words." >}}
{{< card link="environmentalnarrative_guidelines.html" title="Level Art Rules" icon="pencil" subtitle="Placement rules for props and decals." >}}
{{< /cards >}}
