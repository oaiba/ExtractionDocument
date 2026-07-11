---
title: "Core Gameplay Systems"
linkTitle: "Game Design"
type: docs
weight: 5
---

## Overview

This section owns the player-facing rules of Extraction Shooter: how a raid starts, how players move and fight, how loot and loss work, how progression pulls players back, and how the surrounding UX supports the loop.

Use this page as the Game Design map. Deep implementation details belong in the linked pages.

## Foundations

{{< cards cols="3" >}}
{{< card link="overview/index.html" title="High-Level Vision" icon="light-bulb" subtitle="Player promise, design pillars, market position, and guardrails." >}}
{{< card link="coregameplay/index.html" title="Core Gameplay" icon="refresh" subtitle="Pre-match, raid, extraction, post-match, and balance targets." >}}
{{< card link="gamemodes/index.html" title="Game Modes" icon="puzzle" subtitle="Raid, Scav Run, Blitz, Ranked Ops, co-op, and featured modes." >}}
{{< /cards >}}

## Raid Flow

{{< cards cols="3" >}}
{{< card link="loadoutpreparation/index.html" title="Loadout Preparation" icon="adjustments" subtitle="Pre-raid ritual, saved presets, insurance, squad readiness, and deploy flow." >}}
{{< card link="controls/index.html" title="Controls" icon="cursor-click" subtitle="Touch, gamepad, keyboard, aiming, camera, and input switching." >}}
{{< card link="mapdesign/index.html" title="Map Design" icon="location-marker" subtitle="Zone layout, extraction placement, hotspots, and top-down readability." >}}
{{< card link="navigationandmap/index.html" title="Navigation & Map" icon="map" subtitle="Compass, minimap, tactical map, world markers, and ping visibility." >}}
{{< card link="insurancesystem/index.html" title="Insurance System" icon="shield-check" subtitle="Pre-raid insurance, return rules, claim flow, and economy constraints." >}}
{{< card link="tutorialraid/index.html" title="Tutorial Raid" icon="academic-cap" subtitle="Operation Zero onboarding, guided raid phases, and starter kit." >}}
{{< /cards >}}

## Meta, Progression, And Live Ops

{{< cards cols="3" >}}
{{< card link="economy/index.html" title="Economy" icon="currency-dollar" subtitle="Currencies, monetization ethics, marketplace rules, and economy health." >}}
{{< card link="progression/index.html" title="Progression" icon="chart-bar" subtitle="Account levels, operator mastery, quests, battle pass, and retention loops." >}}
{{< card link="liveops/index.html" title="Live Operations" icon="calendar" subtitle="Season cadence, events, featured modes, faction wars, and content updates." >}}
{{< card link="safe_house_design/index.html" title="Safe House" icon="home" subtitle="Out-of-raid hub, stash, workbench, upgrades, and module dependencies." >}}
{{< card link="rankedmode/index.html" title="Ranked Mode" icon="star" subtitle="RP, tiers, matchmaking, season resets, rewards, and competitive integrity." >}}
{{< card link="clansystem/index.html" title="Clan System" icon="user-group" subtitle="Clan creation, ranks, missions, clan bank, and faction war support." >}}
{{< /cards >}}

## UX, Social, And Accessibility

{{< cards cols="3" >}}
{{< card link="homescreen_design/index.html" title="Home Screen & Lobby" icon="home" subtitle="Operator showcase, navigation model, deploy panel, events, and return states." >}}
{{< card link="playerprofile/index.html" title="Player Profile" icon="identification" subtitle="Career stats, achievements, match history, privacy, and social actions." >}}
{{< card link="communication/index.html" title="Communication" icon="chat" subtitle="Voice, ping, quick chat, minimap signals, and anti-toxicity rules." >}}
{{< card link="usersettings/index.html" title="User Settings" icon="cog" subtitle="Settings UX, categories, presets, platform rules, and matrix reference." >}}
{{< card link="accessibility/index.html" title="Accessibility" icon="hand" subtitle="Visual, audio, motor, cognitive, and platform accessibility requirements." >}}
{{< card link="localization/index.html" title="Localization" icon="translate" subtitle="Language tiers, text rules, voice strategy, cultural review, and QA." >}}
{{< /cards >}}

## Source-Of-Truth Rules

| Topic | Canonical Page |
| :--- | :--- |
| Raid loop and match pacing | [Core Gameplay](coregameplay/index.html) |
| Input, camera, and controls | [Controls](controls/index.html) |
| Economy and monetization ethics | [Economy](economy/index.html) |
| Player growth and retention | [Progression](progression/index.html) |
| Season cadence and events | [Live Operations](liveops/index.html) |
| Settings options and tags | [User Settings](usersettings/index.html), [Settings Matrix](usersettings_matrix/index.html), [Settings Tags](usersettings_tags/index.html) |
