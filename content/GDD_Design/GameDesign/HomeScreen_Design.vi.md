---
title: "Home màn hình & Main Lobby Design"
type: docs
weight: 16
---

## Tổng Quan

The Home màn hình is the người chơi's out-of-raid command center. It should show identity, hiện tại goals, squad readiness, live events, và the fastest route back into a raid.

The màn hình should feel like a tactical staging area, not a marketing billboard. The operator, hiện tại kit, active goals, và deploy path are the primary story. Store, events, news, và social hooks can be present, nhưng they không được compete với the người chơi's next raid quyết định.

A strong Home màn hình answers four questions in under five seconds: who am I playing, what can I do next, what has changed since last session, và how do I deploy?

## Quyết Định Chính

| Area | Direction |
| :--- | :--- |
| primary emotion | Readiness và tension trước deployment |
| Main focus | Operator showcase plus Deploy path |
| secondary focus | Progress, events, squad, stash reminders |
| Layout standard | PC/Console landscape: operator center, navigation rail, contextual panels |

## Operator Showcase trạng thái

The operator showcase gives the người chơi a hiển thị rõ identity between raids. It should react to trạng thái changes mà không wasting thời gian: ready posture khi the loadout is valid, restrained celebration sau extraction, và grounded recovery sau death. The tone is tactical confidence, not cartoon celebration.

| trạng thái | Trigger | Next trạng thái |
| :--- | :--- | :--- |
| Idle | người chơi rotates hoặc taps operator | kiểm tra |
| Idle | Loadout becomes valid | Ready |
| Ready | Deploy pressed | Matchmaking |
| Matchmaking | Server match ready | Match Found |
| Matchmaking | Queue cancelled | Idle |
| Match Found | người chơi accepts hoặc timer completes | Deploying |
| Idle | người chơi returns sau successful extraction | Return Victory |
| Idle | người chơi returns sau death | Return Defeat |
| Return Victory / Return Defeat | Summary animation ends | Idle |

## PC / Console Layout

PC và console layouts can show more simultaneous information, nhưng they should still preserve one dominant action. The right panel should lead toward deploy, while the rail và supporting widgets remain stable. Avoid moving navigation between sessions vì muscle memory matters for repeated raid prep.

| Region | Content | mục đích |
| :--- | :--- | :--- |
| Center | Operator showcase, stance, selected skin, vũ khí preview | Identity và readiness |
| Horizontal global nav | Home, Armory, Stash, Safe House, Traders, Ranked, Shop, Settings | Stable primary navigation |
| Local/secondary rail | Contextual shortcuts only when a hub needs local categories | Secondary navigation, never primary Shop access |
| Right panel | Mode card, squad status, quick deploy, queue estimate | Fast path to play |
| Top bar | Currency, notifications, profile, season timer | Account trạng thái |
| Bottom strip | Last raid, active quests, event reminder | Contextual next actions |

## Navigation flow

Navigation should support both deliberate preparation và fast return. A người chơi who wants to tune gear can drill into stash và loadout. A người chơi who just wants another run should move from Home to matchmaking với only the necessary risk confirmations.

| điểm đến | Entry Point | mục đích |
| :--- | :--- | :--- |
| Loadout | Deploy panel hoặc navigation rail | Prepare gear, mode, map, và squad |
| Mode và map | Loadout flow | Select raid rules và điểm đến |
| Squad readiness | Loadout flow | Confirm party trạng thái trước queue |
| Matchmaking | Deploy confirmation | Find match using selected rules |
| Stash | Navigation rail | Manage inventory |
| Safe House | Navigation rail | upgrade modules và claim returns |
| Traders | Navigation rail | mua, sell, và turn in tasks |
| Profile | Top bar | Review identity và stats |
| Settings | Top bar hoặc navigation | Configure game options |

## Deploy Panel yêu cầu

The deploy panel is the final trust checkpoint. It should highlight invalid trạng thái, summarize risk, và explain mode modifiers trước the queue begins. It không nên surprise the người chơi sau matchmaking has started.

| Field | yêu cầu |
| :--- | :--- |
| Selected mode | Always hiển thị rõ |
| Squad size | Always hiển thị rõ |
| Gear giá trị | hiển thị rõ trước khi deploy |
| Insurance status | hiển thị rõ nếu eligible items are uninsured |
| Quest suggestions | Show top 1-3 relevant goals |
| Queue estimate | Update periodically trong khi matchmaking |
| Risk cảnh báo | Trigger nếu người chơi deploys với unusually high giá trị |

## News và Events

| Surface | Rule |
| :--- | :--- |
| Event banner | One primary event at a thời gian |
| Patch ghi chú | Link to dễ đọc chi tiết, not modal overload |
| Daily goals | Show progress và thời gian remaining |
| Deep links | Event cards must open the exact target màn hình |
| Dismissal | Dismissed news không nên reappear until updated |

## Audio và Feedback

| trạng thái | Audio Direction |
| :--- | :--- |
| Idle | Low industrial ambience |
| Queue searching | Subtle tension layer |
| Match found | Short confirmation sting |
| Post-extraction | Brief relief cue |
| Post-death | Somber recovery cue |

## Home màn hình Examples

A returning người chơi sau a successful extraction should see a short loot summary, hiện tại progression gains, và a rõ path to redeploy. The màn hình should celebrate success briefly, then return control quickly.

A người chơi sau death should see recovery actions: rebuild from preset, check insurance, open stash, hoặc run Scavenger. The tone nên được calm và practical rather than punitive.

A first-session người chơi should see Tutorial Raid as the hành động chính until the basics are complete. Store, ranked, và complex live events should stay secondary until the người chơi has context.

## Layout Failure Cases

- nếu the store dominates the first màn hình, the game feels transactional instead of tactical.
- nếu deploy is hidden behind too many panels, session momentum drops.
- nếu last-raid trạng thái is invisible, success và failure feel disconnected from the lobby.
- nếu the navigation rail hoặc context panels bury common actions, regroup them into the PC/Console landscape standard.

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| Deploy flow | [Loadout Preparation](loadoutpreparation/index.html) |
| Modes | [Game Modes](gamemodes/index.html) |
| Progress summary | [Progression](progression/index.html) |
| Events feed | [Live Operations](liveops/index.html) |
| Safe House | [Safe House Design](safe_house_design/index.html) |
| Settings | [User Settings](usersettings/index.html) |
