---
title: "Menus & Screens"
type: docs
weight: 30
---

## Status

This page is kept as a compatibility entry for older links. The UI/UX documentation has been reorganized into screen groups by player lifecycle so each surface has clearer ownership, states, platform behavior, and cross-references.

For the canonical screen inventory, start with [Screen Groups Overview](Screen_Groups_Overview.md).

The lifecycle screen group pages now contain designer-ready detail specs: expanded ASCII wireframes, layout anatomy, visual hierarchy, component requirements, state behavior, platform input, designer notes, and acceptance checklists. Use this page only to resolve old links.

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
| Settings / Shop      | Commerce, Settings, System  |
+----------------------+-----------------------------+
```

| Group | Covers |
| :--- | :--- |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Full taxonomy, spec template, navigation model, coverage checklist |
| [Global UX Standards](Global_UX_Standards.md) | Navigation, focus, responsive layout, modals, empty/error/loading states, accessibility |
| [Out-of-Raid Screens](Out_Of_Raid_Screens.md) | Home, operator select, loadout, stash, traders, safe house, quests, profile |
| [Pre-Raid Screens](Pre_Raid_Screens.md) | Mode select, map select, deploy confirmation, squad lobby, matchmaking |
| [In-Raid Screens](In_Raid_Screens.md) | HUD, tactical map, looting, inventory overlay, pause, spectator, reconnect |
| [Post-Raid Screens](Post_Raid_Screens.md) | AAR, death replay, loot transfer, quest progress, report/commend, redeploy |
| [Social Screens](Social_Screens.md) | Friends, party, invites, LFG, clans, chat, voice, block/report |
| [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) | Battle pass, events, daily/weekly tasks, ranked, leaderboards, reward inbox |
| [Commerce, Settings & System Screens](Commerce_Settings_System_Screens.md) | Auth, first-time setup, shop, wallet, settings, privacy, diagnostics, system dialogs |

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
| Settings Menu | [Commerce, Settings & System Screens](Commerce_Settings_System_Screens.md), [User Settings](../GameDesign/UserSettings.md) |
| Pause Menu | [In-Raid Screens](In_Raid_Screens.md) |

---

## Migration Rule

New UI screen specs should not be added to this page. Add them to the owning screen group and link back to the relevant game design or technical system page.

When migrating old menu content, preserve intent and state requirements, but rewrite layout detail using the designer-ready section set defined in [Screen Groups Overview](Screen_Groups_Overview.md).
