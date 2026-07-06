---
title: GDD Design
type: docs
aliases:
  - /gdd_design.html
  - /GDD_Design.html
  - /gdd_design/
  - /gdd_design/index.html
  - /GDD_Design/
  - /GDD_Design/index.html
---

This hub owns the creative and player-facing design of Extraction: game loops, player experience, art direction, audio, worldbuilding, characters, UI/UX, and design scope. Technical implementation, architecture, code standards, and engine details belong in [Technical GDD](/GDD_Technical.html).

Use this page as the entry point for design intent and navigation. Deep specifications live in the linked section pages.

## Start Here

{{< cards cols="3" >}}
{{< card link="/GDD_Design/GameDesign/Overview.html" title="Design Overview" icon="light-bulb" subtitle="Game concept, pillars, target audience, market positioning, and competitive context." >}}
{{< card link="/GDD_Design/GameDesign/CoreGameplay.html" title="Core Gameplay" icon="refresh" subtitle="Primary gameplay loop, raid phases, player psychology, and session flow." >}}
{{< card link="/GDD_Design/ProjectScope/MVP.html" title="MVP Scope" icon="flag" subtitle="Current feature boundaries, launch requirements, and scope guardrails." >}}
{{< /cards >}}

## Design Domains

{{< cards cols="3" >}}
{{< card link="/GDD_Design/GameDesign" title="Game Design" icon="sparkles" subtitle="High-level systems, progression, economy, ranked, live ops, controls, and onboarding." >}}
{{< card link="/GDD_Design/Gameplay" title="Gameplay Mechanics" icon="puzzle" subtitle="Moment-to-moment interaction rules: movement, looting, extraction, combat feel, visibility, and hazards." >}}
{{< card link="/GDD_Design/Characters" title="Characters" icon="user-group" subtitle="Operator classes, role identities, abilities, synergies, progression, and cosmetics." >}}
{{< /cards >}}

{{< cards cols="3" >}}
{{< card link="/GDD_Design/Combat" title="Combat & Items" icon="adjustments" subtitle="Combat philosophy, weapons, items, inventory touchpoints, and canonical gameplay cross-references." >}}
{{< card link="/GDD_Design/Gears" title="Gear Systems" icon="briefcase" subtitle="Armor, storage, gear tiers, progression, balance, handling, and visual identity." >}}
{{< card link="/GDD_Design/Inventory_System" title="Inventory Systems" icon="cube" subtitle="Containers, looting rules, medical survival, gunsmith, and inventory design references." >}}
{{< /cards >}}

{{< cards cols="3" >}}
{{< card link="/GDD_Design/World" title="World Design" icon="map" subtitle="Map structure, loot distribution, environmental narrative, layouts, and named zone design." >}}
{{< card link="/GDD_Design/Story" title="Story & Narrative" icon="book-open" subtitle="World lore, factions, backstory, quest lines, and narrative delivery." >}}
{{< card link="/GDD_Design/NarrativeWorld" title="Narrative World" icon="globe-alt" subtitle="Faction territories, map bible, location lore, and environmental storytelling anchors." >}}
{{< /cards >}}

{{< cards cols="3" >}}
{{< card link="/GDD_Design/Visuals" title="Visual Design" icon="photograph" subtitle="Art direction, style guide, asset guidelines, interface visuals, VFX, and animation language." >}}
{{< card link="/GDD_Design/UI_UX" title="UI/UX" icon="template" subtitle="HUD, menus, loading screens, notifications, UX flows, and visual style for player-facing screens." >}}
{{< card link="/GDD_Design/Audio" title="Audio Design" icon="music-note" subtitle="Sound design, tactical audio, soundscape, voice lines, and combat feedback cues." >}}
{{< /cards >}}

{{< cards cols="3" >}}
{{< card link="/GDD_Design/Social" title="Social & Multiplayer" icon="users" subtitle="Squads, matchmaking, communication, karma, clans, social hub, and post-match flow." >}}
{{< card link="/GDD_Design/AI" title="AI & Enemies" icon="chip" subtitle="Enemy behavior, faction ecology, boss design, difficulty, and AI balancing." >}}
{{< card link="/GDD_Design/ProjectScope" title="Project Scope" icon="scale" subtitle="Design pillars, MVP, non-goals, risks, competitive analysis, and planning boundaries." >}}
{{< /cards >}}

## Who Uses This

| Role | Primary Use | Start With |
| --- | --- | --- |
| Game Designer | Define mechanics, balance, progression, and player-facing systems. | [Overview](/GDD_Design/GameDesign/Overview.html), [Core Gameplay](/GDD_Design/GameDesign/CoreGameplay.html) |
| Artist | Align assets with visual style, character identity, environments, and UI tone. | [Visual Design](/GDD_Design/Visuals.html), [Characters](/GDD_Design/Characters.html), [World Design](/GDD_Design/World.html) |
| Level Designer | Build maps around extraction flow, loot pressure, routes, and encounter pacing. | [World Design](/GDD_Design/World.html), [Core Gameplay](/GDD_Design/GameDesign/CoreGameplay.html) |
| Audio Designer | Match audio cues to tactical needs, ambience, feedback, and narrative tone. | [Audio Design](/GDD_Design/Audio.html), [Core Gameplay](/GDD_Design/GameDesign/CoreGameplay.html) |
| UI/UX Designer | Shape player flows, controls, menus, HUD, accessibility, and feedback systems. | [UI/UX](/GDD_Design/UI_UX.html), [Controls](/GDD_Design/GameDesign/Controls.html) |

## Design Principles

{{< cards cols="3" >}}
{{< card title="Player-First" icon="heart" subtitle="Every design decision should improve clarity, fairness, agency, or emotional payoff for the player." >}}
{{< card title="Mobile-Optimized" icon="device-mobile" subtitle="Sessions, controls, readability, performance, and interaction density must work on mobile first." >}}
{{< card title="Depth Through Simplicity" icon="beaker" subtitle="Rules should be easy to understand, then reveal mastery through timing, positioning, risk, and tradeoffs." >}}
{{< /cards >}}

## Core Terms

| Term | Meaning |
| --- | --- |
| Extraction | Leaving the map with loot, progress, and survival value intact. |
| Hot Zone | High-risk, high-reward area that concentrates loot, enemies, and player conflict. |
| Operator | Playable character class with a role identity and ability kit. |
| Stash | Persistent storage for extracted items and long-term progression. |
| MMR | Matchmaking rating used to tune competitive quality and fairness. |
| POI | Point of interest such as a landmark, loot site, objective, or encounter area. |
| TTK | Time to kill, a key combat pacing and balance measure. |
| DPS | Damage per second, used to compare sustained damage output. |

## Maintenance

Use [Project Scope](/GDD_Design/ProjectScope.html) for current boundaries, MVP decisions, risks, and non-goals. Historical documentation changes are tracked in [Update Log](/GDD_Design/UpdateLog.html).
