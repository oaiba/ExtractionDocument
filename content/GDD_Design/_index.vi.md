---
title: "GDD Design"
type: docs
---

Hub này sở hữu phần thiết kế sáng tạo và player-facing của Extraction: game loop, player experience, art direction, audio, worldbuilding, characters, UI/UX, và design scope. Technical implementation, architecture, code standard, và engine detail thuộc về [Technical GDD](/GDD_Technical.html).

Dùng trang này làm entry point cho design intent và navigation. Spec sâu nằm trong các section page được link.

> Bản tiếng Việt là companion translation để đọc và navigate nhanh. English vẫn là nguồn canonical khi có khác biệt về rule, number, hoặc feature contract.

## Bắt Đầu

{{< cards cols="3" >}}
{{< card link="/GDD_Design/GameDesign/Overview.html" title="Design Overview" icon="light-bulb" subtitle="Game concept, pillar, target audience, market positioning, và competitive context." >}}
{{< card link="/GDD_Design/GameDesign/CoreGameplay.html" title="Core Gameplay" icon="refresh" subtitle="Primary gameplay loop, raid phase, player psychology, và session flow." >}}
{{< card link="/GDD_Design/ProjectScope/MVP.html" title="MVP Scope" icon="flag" subtitle="Feature boundary hiện tại, launch requirement, và scope guardrail." >}}
{{< /cards >}}

## Design Domains

{{< cards cols="3" >}}
{{< card link="/GDD_Design/GameDesign" title="Game Design" icon="sparkles" subtitle="High-level system, progression, economy, ranked, live ops, controls, và onboarding." >}}
{{< card link="/GDD_Design/Gameplay" title="Gameplay Mechanics" icon="puzzle" subtitle="Luật interaction từng khoảnh khắc: movement, looting, extraction, combat feel, visibility, và hazard." >}}
{{< card link="/GDD_Design/Characters" title="Characters" icon="user-group" subtitle="Operator class, role identity, ability, synergy, progression, và cosmetic." >}}
{{< /cards >}}

{{< cards cols="3" >}}
{{< card link="/GDD_Design/Combat" title="Combat & Items" icon="adjustments" subtitle="Combat philosophy, weapon, item, inventory touchpoint, và canonical gameplay cross-reference." >}}
{{< card link="/GDD_Design/Gears" title="Gear Systems" icon="briefcase" subtitle="Armor, storage, gear tier, progression, balance, handling, và visual identity." >}}
{{< card link="/GDD_Design/Inventory_System" title="Inventory Systems" icon="cube" subtitle="Container, looting rule, medical survival, gunsmith, và inventory design reference." >}}
{{< /cards >}}

{{< cards cols="3" >}}
{{< card link="/GDD_Design/World" title="World Design" icon="map" subtitle="Map structure, loot distribution, environmental narrative, layout, và named zone design." >}}
{{< card link="/GDD_Design/Story" title="Story & Narrative" icon="book-open" subtitle="World lore, faction, backstory, quest line, và narrative delivery." >}}
{{< card link="/GDD_Design/NarrativeWorld" title="Narrative World" icon="globe-alt" subtitle="Faction territory, map bible, location lore, và environmental storytelling anchor." >}}
{{< /cards >}}

{{< cards cols="3" >}}
{{< card link="/GDD_Design/Visuals" title="Visual Design" icon="photograph" subtitle="Art direction, style guide, asset guideline, interface visual, VFX, và animation language." >}}
{{< card link="/GDD_Design/UI_UX" title="UI/UX" icon="template" subtitle="HUD, menu, loading screen, notification, UX flow, và visual style cho player-facing screen." >}}
{{< card link="/GDD_Design/Audio" title="Audio Design" icon="music-note" subtitle="Sound design, tactical audio, soundscape, voice line, và combat feedback cue." >}}
{{< /cards >}}

{{< cards cols="3" >}}
{{< card link="/GDD_Design/Social" title="Social & Multiplayer" icon="users" subtitle="Squad, matchmaking, communication, karma, clan, social hub, và post-match flow." >}}
{{< card link="/GDD_Design/AI" title="AI & Enemies" icon="chip" subtitle="Enemy behavior, faction ecology, boss design, difficulty, và AI balancing." >}}
{{< card link="/GDD_Design/ProjectScope" title="Project Scope" icon="scale" subtitle="Design pillar, MVP, non-goal, risk, competitive analysis, và planning boundary." >}}
{{< /cards >}}

## Ai Sử Dụng Trang Này

| Role | Mục Đích Chính | Bắt Đầu Với |
| --- | --- | --- |
| Game Designer | Định nghĩa mechanic, balance, progression, và player-facing system. | [Overview](/GDD_Design/GameDesign/Overview.html), [Core Gameplay](/GDD_Design/GameDesign/CoreGameplay.html) |
| Artist | Canh asset với visual style, character identity, environment, và UI tone. | [Visual Design](/GDD_Design/Visuals.html), [Characters](/GDD_Design/Characters.html), [World Design](/GDD_Design/World.html) |
| Level Designer | Xây map quanh extraction flow, loot pressure, route, và encounter pacing. | [World Design](/GDD_Design/World.html), [Core Gameplay](/GDD_Design/GameDesign/CoreGameplay.html) |
| Audio Designer | Match audio cue với tactical need, ambience, feedback, và narrative tone. | [Audio Design](/GDD_Design/Audio.html), [Core Gameplay](/GDD_Design/GameDesign/CoreGameplay.html) |
| UI/UX Designer | Định hình player flow, control, menu, HUD, accessibility, và feedback system. | [UI/UX](/GDD_Design/UI_UX.html), [Controls](/GDD_Design/GameDesign/Controls.html) |

## Design Principles

{{< cards cols="3" >}}
{{< card title="Player-First" icon="heart" subtitle="Mọi quyết định design nên cải thiện clarity, fairness, agency, hoặc emotional payoff cho người chơi." >}}
{{< card title="Mobile-Optimized" icon="device-mobile" subtitle="Session, control, readability, performance, và interaction density phải hoạt động tốt trên mobile trước." >}}
{{< card title="Depth Through Simplicity" icon="beaker" subtitle="Rule phải dễ hiểu trước, rồi mở ra mastery qua timing, positioning, risk, và tradeoff." >}}
{{< /cards >}}

## Core Terms

| Term | Meaning |
| --- | --- |
| Extraction | Rời map với loot, progress, và survival value còn nguyên. |
| Hot Zone | Khu vực high-risk, high-reward tập trung loot, enemy, và xung đột người chơi. |
| Operator | Playable character class có role identity và ability kit. |
| Stash | Kho lưu trữ persistent cho item đã extract và long-term progression. |
| MMR | Matchmaking rating dùng để tinh chỉnh competitive quality và fairness. |
| POI | Point of interest như landmark, loot site, objective, hoặc encounter area. |
| TTK | Time to kill, chỉ số chính cho combat pacing và balance. |
| DPS | Damage per second, dùng để so sánh sustained damage output. |

## Maintenance

Dùng [Project Scope](/GDD_Design/ProjectScope.html) cho boundary hiện tại, MVP decision, risk, và non-goal. Lịch sử thay đổi tài liệu được theo dõi trong [Update Log](/GDD_Design/UpdateLog.html).
