---
title: "Core Gameplay Systems"
linkTitle: "Game Design"
type: docs
weight: 5
---

## Tổng Quan

Section này sở hữu các luật player-facing của Extraction Shooter: raid bắt đầu như thế nào, người chơi di chuyển và chiến đấu ra sao, loot và loss vận hành thế nào, progression kéo người chơi quay lại ra sao, và UX xung quanh hỗ trợ loop như thế nào.

Dùng trang này như bản đồ Game Design. Chi tiết implementation sâu nằm trong các page được link.

## Foundations

{{< cards cols="3" >}}
{{< card link="overview.html" title="High-Level Vision" icon="light-bulb" subtitle="Player promise, design pillar, market position, và guardrail." >}}
{{< card link="coregameplay.html" title="Core Gameplay" icon="refresh" subtitle="Pre-match, raid, extraction, post-match, và balance target." >}}
{{< card link="gamemodes.html" title="Game Modes" icon="puzzle" subtitle="Raid, Scav Run, Blitz, Ranked Ops, co-op, và featured mode." >}}
{{< /cards >}}

## Raid Flow

{{< cards cols="3" >}}
{{< card link="loadoutpreparation.html" title="Loadout Preparation" icon="adjustments" subtitle="Pre-raid ritual, saved preset, insurance, squad readiness, và deploy flow." >}}
{{< card link="controls.html" title="Controls" icon="cursor-click" subtitle="Touch, gamepad, keyboard, aiming, camera, và input switching." >}}
{{< card link="mapdesign.html" title="Map Design" icon="location-marker" subtitle="Zone layout, extraction placement, hotspot, và top-down readability." >}}
{{< card link="navigationandmap.html" title="Navigation & Map" icon="map" subtitle="Compass, minimap, tactical map, world marker, và ping visibility." >}}
{{< card link="insurancesystem.html" title="Insurance System" icon="shield-check" subtitle="Pre-raid insurance, return rule, claim flow, và economy constraint." >}}
{{< card link="tutorialraid.html" title="Tutorial Raid" icon="academic-cap" subtitle="Operation Zero onboarding, guided raid phase, và starter kit." >}}
{{< /cards >}}

## Meta, Progression, Và Live Ops

{{< cards cols="3" >}}
{{< card link="economy.html" title="Economy" icon="currency-dollar" subtitle="Currency, monetization ethics, marketplace rule, và economy health." >}}
{{< card link="progression.html" title="Progression" icon="chart-bar" subtitle="Account level, operator mastery, quest, battle pass, và retention loop." >}}
{{< card link="liveops.html" title="Live Operations" icon="calendar" subtitle="Season cadence, event, featured mode, faction war, và content update." >}}
{{< card link="safe_house_design.html" title="Safe House" icon="home" subtitle="Out-of-raid hub, stash, workbench, upgrade, và module dependency." >}}
{{< card link="rankedmode.html" title="Ranked Mode" icon="star" subtitle="RP, tier, matchmaking, season reset, reward, và competitive integrity." >}}
{{< card link="clansystem.html" title="Clan System" icon="user-group" subtitle="Clan creation, rank, mission, clan bank, và faction war support." >}}
{{< /cards >}}

## UX, Social, Và Accessibility

{{< cards cols="3" >}}
{{< card link="homescreen_design.html" title="Home Screen & Lobby" icon="home" subtitle="Operator showcase, navigation model, deploy panel, event, và return state." >}}
{{< card link="playerprofile.html" title="Player Profile" icon="identification" subtitle="Career stat, achievement, match history, privacy, và social action." >}}
{{< card link="communication.html" title="Communication" icon="chat" subtitle="Voice, ping, quick chat, minimap signal, và anti-toxicity rule." >}}
{{< card link="usersettings.html" title="User Settings" icon="cog" subtitle="Settings UX, category, preset, platform rule, và matrix reference." >}}
{{< card link="accessibility.html" title="Accessibility" icon="hand" subtitle="Yêu cầu accessibility cho visual, audio, motor, cognitive, và platform." >}}
{{< card link="localization.html" title="Localization" icon="translate" subtitle="Language tier, text rule, voice strategy, cultural review, và QA." >}}
{{< /cards >}}

## Quy Tắc Source-Of-Truth

| Topic | Trang Canonical |
| :--- | :--- |
| Raid loop và match pacing | [Core Gameplay](coregameplay.html) |
| Input, camera, và controls | [Controls](controls.html) |
| Economy và monetization ethics | [Economy](economy.html) |
| Player growth và retention | [Progression](progression.html) |
| Season cadence và events | [Live Operations](liveops.html) |
| Settings option và tag | [User Settings](usersettings.html), [Settings Matrix](usersettings_matrix.html), [Settings Tags](usersettings_tags.html) |
