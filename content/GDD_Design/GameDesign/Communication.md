---
title: "In-Game Communication - Voice Chat & Ping System"
type: docs
weight: 21
---

## Overview

Communication supports squad tactics without requiring voice chat. Pings, quick chat, map markers, and voice channels must work together.

The communication system should make silent teamwork viable. Players may be on mobile, in public, using different languages, avoiding voice, or dealing with toxicity. The game should still let them call danger, request help, mark loot, confirm plans, and coordinate extraction.

Communication tools are also safety tools. Fast mute, report, ping spam control, and readable privacy settings are part of the core design because a bad social experience can end a session faster than a bad death.

## Signal Flow

Signal flow should preserve intent and context. A ping placed on an enemy should not look like a loot ping. A quick chat line should be localized and short. Voice should complement pings, not replace them.

| Player Input | Signal Type | Output | Display / Delivery |
| :--- | :--- | :--- | :--- |
| Tap or quick press | Context ping | World marker | Compass and minimap |
| Hold input | Ping wheel | Chosen intent marker | World, compass, minimap, squad feed |
| Quick chat command | Text callout | Localized phrase and optional VO | Squad feed and subtitles |
| Voice input | Voice channel | Live voice | Party, squad, proximity, or clan channel |
| Mute/report action | Safety signal | Moderation action | Player-level communication controls |

## Communication Pillars

The pillars should be tested in real squad play. If players need voice to solve basic coordination, pings are underpowered. If pings reveal too much or become spam, they are overpowering the information game.

| Pillar | Rule |
| :--- | :--- |
| Fast | One tap must communicate common intent |
| Non-verbal first | Players can coordinate without microphone |
| Context-aware | Ping system should infer loot, enemy, route, extraction |
| Anti-toxic | Mute, report, filters, and penalties are built in |
| Accessible | Visual alternatives for audio signals |

## Voice Channels

Voice channels should default to privacy and safety. Proximity voice can create memorable moments in casual modes, but ranked should treat it carefully because deception, harassment, and collusion risks are higher.

| Channel | Use | Rule |
| :--- | :--- | :--- |
| Party | Friends before matchmaking | Always private |
| Squad | Teammates in match | Default team voice |
| Proximity | Nearby players if mode allows | Disabled in ranked by default |
| Clan | Out-of-raid social | Optional |

## Ping Types

| Ping | Example | Priority |
| :--- | :--- | :--- |
| Enemy | Seen or suspected enemy | High |
| Loot | Useful item or container | Medium |
| Route | Move here, rotate, avoid | Medium |
| Extraction | Extract now or extraction spotted | High |
| Help | Need revive, healing, ammo | High |
| Confirm | Yes, ready, understood | Low |

## Anti-Toxicity Rules

Anti-toxicity tools must be reachable during and after the match. A player should be able to mute quickly without losing control, report from the recap, and block future communication from a profile.

| Tool | Requirement |
| :--- | :--- |
| Mute | Fast, per-player, persistent option |
| Report | Available from match and profile |
| Profanity filter | On by default |
| Voice abuse | Escalates from mute to queue restrictions |
| Ping spam | Rate limit and local mute |

## Communication Examples

A solo-fill player without microphone should still be able to mark a route, confirm readiness, request healing, and call extraction through pings and quick chat.

A squad under fire should be able to send a danger ping with one input. The signal should appear on compass and minimap quickly, then decay so it does not clutter the screen forever.

A player dealing with harassment should be able to mute, report, and block from the match UI or recap without searching through settings.

## Communication Failure Cases

- If voice is required for basic teamwork, non-voice players are disadvantaged.
- If ping spam hides real danger, priority and rate limits need tuning.
- If proximity voice enables harassment in ranked, the mode should restrict it.
- If quick chat is not localized, cross-language squads lose coordination.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Ping display | [Navigation & Map](navigationandmap.html) |
| Accessibility alternatives | [Accessibility](accessibility.html) |
| Ranked restrictions | [Ranked Mode](rankedmode.html) |
| Loadout squad voice | [Loadout Preparation](loadoutpreparation.html) |
