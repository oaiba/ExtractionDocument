---
title: "Menus & Screens"
type: docs
weight: 30
---

## Status

Trang này được giữ như compatibility entry cho các link cũ. Tài liệu UI/UX đã được tổ chức lại thành screen group theo player lifecycle để mỗi surface có ownership, states, platform behavior, và cross-reference rõ hơn.

Với screen inventory canonical, bắt đầu từ [Screen Groups Overview](screen_groups_overview/index.html).

Các lifecycle screen group pages hiện chứa designer-ready detail specs: expanded ASCII wireframes, layout anatomy, visual hierarchy, component requirements, state behavior, platform input, designer notes, và acceptance checklists. Chỉ dùng trang này để resolve old links.

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Hub tài liệu UI/UX đầy đủ |
| [Screen Groups Overview](screen_groups_overview/index.html) | Taxonomy canonical và migration target |
| [Global UX Standards](global_ux_standards/index.html) | Rule chung cho navigation, focus, state, modal, accessibility |
| [Out-of-Raid Screens](out_of_raid_screens/index.html) | Main menu, home, loadout, stash, traders |
| [Pre-Raid Screens](pre_raid_screens/index.html) | Map, squad, deploy, queue |
| [In-Raid Screens](in_raid_screens/index.html) | Pause, looting, inventory overlay, reconnect |

---

## New Screen Group Pages

#### System Diagram

```
Legacy Menus.md
      |
      v
+----------------------+-----------------------------+
| Old Section          | New Owner                   |
+----------------------+-----------------------------+
| Main Menu / Home     | Out-of-Raid Screens         |
| Loadout / Stash      | Out-of-Raid Screens         |
| Map / Squad / Queue  | Pre-Raid Screens            |
| Pause / Looting      | In-Raid Screens             |
| AAR / Death Replay   | Post-Raid Screens           |
| Battle Pass / Events | Progression & LiveOps       |
| Shop                 | Commerce Screens            |
| Settings             | Settings & System Screens   |
+----------------------+-----------------------------+
```

| Group | Covers |
| :--- | :--- |
| [Screen Groups Overview](screen_groups_overview/index.html) | Full taxonomy, spec template, navigation model, coverage checklist |
| [Global UX Standards](global_ux_standards/index.html) | Navigation, focus, responsive layout, modal, empty/error/loading states, accessibility |
| [Out-of-Raid Screens](out_of_raid_screens/index.html) | Home, operator select, loadout, stash, traders, safe house, quests, profile |
| [Pre-Raid Screens](pre_raid_screens/index.html) | Mode select, map select, deploy confirmation, squad lobby, matchmaking |
| [In-Raid Screens](in_raid_screens/index.html) | HUD, tactical map, looting, inventory overlay, pause, spectator, reconnect |
| [Post-Raid Screens](post_raid_screens/index.html) | AAR, death replay, loot transfer, quest progress, report/commend, redeploy |
| [Social Screens](social_screens/index.html) | Friends, party, invites, LFG, clans, chat, voice, block/report |
| [Progression & LiveOps Screens](progression_liveops_screens/index.html) | Battle pass, events, daily/weekly tasks, ranked, leaderboards, reward inbox |
| [Commerce Screens](commerce_screens/index.html) | Shop, offers, bundles, item preview, currency top-up, purchase confirmation, receipts, redeem |
| [Settings & System Screens](commerce_settings_system_screens/index.html) | Auth, first-time setup, settings, privacy, diagnostics, system dialogs |

---

## Legacy Content Mapping

| Former Section | New Owner |
| :--- | :--- |
| Main Menu / Safe House | [Out-of-Raid Screens](out_of_raid_screens/index.html), [Home Screen & Main Lobby Design](../gamedesign/homescreen_design/index.html) |
| Loadout Screen | [Out-of-Raid Screens](out_of_raid_screens/index.html), [Loadout Preparation](../gamedesign/loadoutpreparation/index.html) |
| Trader / Market Screen | [Out-of-Raid Screens](out_of_raid_screens/index.html) |
| Stash / Inventory Management | [Out-of-Raid Screens](out_of_raid_screens/index.html), [Stash Design](../stash_design/index.html) |
| Map Selection Screen | [Pre-Raid Screens](pre_raid_screens/index.html) |
| Squad / Lobby Screen | [Pre-Raid Screens](pre_raid_screens/index.html), [Social Screens](social_screens/index.html) |
| After Action Report | [Post-Raid Screens](post_raid_screens/index.html), [Post-Game Debrief & Replay](../gameplay/post_game_debrief/index.html) |
| Battle Pass / Seasonal Screen | [Progression & LiveOps Screens](progression_liveops_screens/index.html) |
| Settings Menu | [Settings & System Screens](commerce_settings_system_screens/index.html), [User Settings](../gamedesign/usersettings/index.html) |
| Pause Menu | [In-Raid Screens](in_raid_screens/index.html) |

---

## Migration Rule

Không thêm screen spec UI mới vào trang này. Hãy thêm vào screen group sở hữu nó và link ngược về game design hoặc technical system page liên quan.

Khi migrate old menu content, giữ intent và state requirement, nhưng viết lại layout detail bằng designer-ready section set được định nghĩa trong [Screen Groups Overview](screen_groups_overview/index.html).
