---
title: "In-Game Communication - Voice Chat & Ping hệ thống"
type: docs
weight: 21
---

## Tổng Quan

Communication supports squad tactics mà không requiring voice chat. Pings, quick chat, map markers, và voice channels must work together.

The communication hệ thống should make silent teamwork viable. người chơi may be on mobile, in public, using different languages, avoiding voice, hoặc dealing với toxicity. The game should still let them call danger, request giúp, mark loot, confirm plans, và coordinate extraction.

Communication tools are also safety tools. Fast mute, report, ping spam control, và dễ đọc privacy settings are part of the cốt lõi design vì a bad social trải nghiệm can end a session faster than a bad death.

## Signal flow

Signal flow should preserve intent và context. A ping placed on an địch không nên look like a loot ping. A quick chat line nên được localized và short. Voice should complement pings, not replace them.

| người chơi Input | Signal Type | Output | Display / Delivery |
| :--- | :--- | :--- | :--- |
| Tap hoặc quick press | Context ping | World marker | Compass và minimap |
| Hold input | Ping wheel | Chosen intent marker | World, compass, minimap, squad feed |
| Quick chat command | Text callout | Localized phrase và optional VO | Squad feed và subtitles |
| Voice input | Voice channel | Live voice | Party, squad, proximity, hoặc clan channel |
| Mute/report action | Safety signal | Moderation action | người chơi-level communication controls |

## Communication Pillars

The pillars nên được tested in real squad play. nếu người chơi need voice to solve basic coordination, pings are underpowered. nếu pings reveal too much hoặc become spam, they are overpowering the information game.

| Pillar | Rule |
| :--- | :--- |
| Fast | One tap must communicate common intent |
| Non-verbal first | Người chơi có thể coordinate mà không microphone |
| Context-aware | Ping hệ thống should infer loot, địch, route, extraction |
| Anti-toxic | Mute, report, filters, và penalties are built in |
| Accessible | Visual alternatives for audio signals |

## Voice Channels

Voice channels should default to privacy và safety. Proximity voice can tạo memorable moments in casual modes, nhưng ranked should treat it carefully vì deception, harassment, và collusion risks are higher.

| Channel | cách dùng | Rule |
| :--- | :--- | :--- |
| Party | Friends trước matchmaking | Always private |
| Squad | Teammates in match | Default team voice |
| Proximity | Nearby người chơi nếu mode allows | disabled in ranked by default |
| Clan | Out-of-raid social | Optional |

## Ping Types

| Ping | Example | Priority |
| :--- | :--- | :--- |
| địch | Seen hoặc suspected địch | High |
| Loot | Useful item hoặc container | Medium |
| Route | Move here, rotate, avoid | Medium |
| Extraction | Extract now hoặc extraction spotted | High |
| giúp | Need revive, healing, đạn | High |
| Confirm | Yes, ready, understood | Low |

## Anti-Toxicity Rules

Anti-toxicity tools phải được reachable trong khi và sau the match. A người chơi nên được able to mute quickly mà không losing control, report from the recap, và block future communication from a profile.

| Tool | yêu cầu |
| :--- | :--- |
| Mute | Fast, per-người chơi, persistent option |
| Report | available from match và profile |
| Profanity filter | On by default |
| Voice abuse | Escalates from mute to queue restrictions |
| Ping spam | Rate limit và local mute |

## Communication Examples

A solo-fill người chơi mà không microphone should still be able to mark a route, confirm readiness, request healing, và call extraction thông qua pings và quick chat.

A squad under fire nên được able to send a danger ping với one input. The signal should appear on compass và minimap quickly, then decay so it does not clutter the màn hình forever.

A người chơi dealing với harassment nên được able to mute, report, và block from the match UI hoặc recap mà không searching thông qua settings.

## Communication Failure Cases

- nếu voice is required for basic teamwork, non-voice người chơi are disadvantaged.
- nếu ping spam hides real danger, priority và rate limits need tuning.
- nếu proximity voice enables harassment in ranked, the mode should restrict it.
- nếu quick chat is not localized, cross-language squads lose coordination.

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| Ping display | [Navigation & Map](navigationandmap.html) |
| Accessibility alternatives | [Accessibility](accessibility.html) |
| Ranked restrictions | [Ranked Mode](rankedmode.html) |
| Loadout squad voice | [Loadout Preparation](loadoutpreparation.html) |
