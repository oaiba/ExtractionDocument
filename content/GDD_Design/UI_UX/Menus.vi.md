---
title: "Menus & Screens"
type: docs
weight: 30
---

## Status

Trang này được giữ như compatibility entry cho các link cũ. Tài liệu UI/UX đã được tổ chức lại thành screen group theo player lifecycle để mỗi surface có ownership, states, platform behavior, và cross-reference rõ hơn.

Với screen inventory canonical, bắt đầu từ [Screen Groups Overview](Screen_Groups_Overview.md).

Các lifecycle screen group pages hiện chứa designer-ready detail specs: expanded ASCII wireframes, layout anatomy, visual hierarchy, component requirements, state behavior, platform input, designer notes, và acceptance checklists. Chỉ dùng trang này để resolve old links.

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Hub tài liệu UI/UX đầy đủ |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Taxonomy canonical và migration target |
| [Global UX Standards](Global_UX_Standards.md) | Rule chung cho navigation, focus, state, modal, accessibility |
| [Out-of-Raid Screens](Out_Of_Raid_Screens.md) | Main menu, home, loadout, stash, traders |
| [Pre-Raid Screens](Pre_Raid_Screens.md) | Map, squad, deploy, queue |
| [In-Raid Screens](In_Raid_Screens.md) | Pause, looting, inventory overlay, reconnect |

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
| [Screen Groups Overview](Screen_Groups_Overview.md) | Full taxonomy, spec template, navigation model, coverage checklist |
| [Global UX Standards](Global_UX_Standards.md) | Navigation, focus, responsive layout, modal, empty/error/loading states, accessibility |
| [Out-of-Raid Screens](Out_Of_Raid_Screens.md) | Home, operator select, loadout, stash, traders, safe house, quests, profile |
| [Pre-Raid Screens](Pre_Raid_Screens.md) | Mode select, map select, deploy confirmation, squad lobby, matchmaking |
| [In-Raid Screens](In_Raid_Screens.md) | HUD, tactical map, looting, inventory overlay, pause, spectator, reconnect |
| [Post-Raid Screens](Post_Raid_Screens.md) | AAR, death replay, loot transfer, quest progress, report/commend, redeploy |
| [Social Screens](Social_Screens.md) | Friends, party, invites, LFG, clans, chat, voice, block/report |
| [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) | Battle pass, events, daily/weekly tasks, ranked, leaderboards, reward inbox |
| [Commerce Screens](Commerce_Screens.md) | Shop, offers, bundles, item preview, currency top-up, purchase confirmation, receipts, redeem |
| [Settings & System Screens](Commerce_Settings_System_Screens.md) | Auth, first-time setup, settings, privacy, diagnostics, system dialogs |

---

## Legacy Content Mapping

| Former Section | New Owner |
| :--- | :--- |
| Main Menu / Safe House | [Out-of-Raid Screens](Out_Of_Raid_Screens.md), [Home Screen & Main Lobby Design](../GameDesign/HomeScreen_Design.md) |
| Loadout Screen | [Out-of-Raid Screens](Out_Of_Raid_Screens.md), [Loadout Preparation](../GameDesign/LoadoutPreparation.md) |
| Trader / Market Screen | [Out-of-Raid Screens](Out_Of_Raid_Screens.md) |
| Stash / Inventory Management | [Out-of-Raid Screens](Out_Of_Raid_Screens.md), [Stash Design](../Stash_Design.md) |
| Map Selection Screen | [Pre-Raid Screens](Pre_Raid_Screens.md) |
| Squad / Lobby Screen | [Pre-Raid Screens](Pre_Raid_Screens.md), [Social Screens](Social_Screens.md) |
| After Action Report | [Post-Raid Screens](Post_Raid_Screens.md), [Post-Game Debrief & Replay](../Gameplay/Post_Game_Debrief.md) |
| Battle Pass / Seasonal Screen | [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) |
| Settings Menu | [Settings & System Screens](Commerce_Settings_System_Screens.md), [User Settings](../GameDesign/UserSettings.md) |
| Pause Menu | [In-Raid Screens](In_Raid_Screens.md) |

---

## Migration Rule

Không thêm screen spec UI mới vào trang này. Hãy thêm vào screen group sở hữu nó và link ngược về game design hoặc technical system page liên quan.

Khi migrate old menu content, giữ intent và state requirement, nhưng viết lại layout detail bằng designer-ready section set được định nghĩa trong [Screen Groups Overview](Screen_Groups_Overview.md).
