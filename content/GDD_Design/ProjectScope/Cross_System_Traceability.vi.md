---
title: Ma Trận Truy Vết Liên Hệ Thống
linkTitle: Traceability Matrix
type: docs
weight: 9
---

## Mục Đích

Ma trận này map hành trình chính của người chơi với owner gameplay, trạng thái UI, hành vi khi lỗi, telemetry và tài liệu canonical. Đây là công cụ kiểm tra tính nhất quán, không thay thế đặc tả chi tiết của từng system.

## Ranh Giới Ownership

| Domain | Sở hữu | Không sở hữu |
| :--- | :--- | :--- |
| Core Gameplay | Phase raid, risk, extraction và outcome | Storage item hoặc layout UI |
| AI | Detection, threat, reinforcement, AI loot profile | Reconciliation reward người chơi |
| Combat / Weapons | Damage, armor, TTK và weapon feedback | Commerce entitlement |
| Inventory | Item instance, ownership, placement, lifecycle | Tuning currency |
| Economy | Source, sink, price, inflation, recovery | Cách trình bày màn hình |
| Progression | XP, unlock, reward track, claim state | Platform checkout |
| Commerce | Offer, entitlement, checkout, receipt, support | Gear combat power |
| UI/UX | Layout, input, focus, state communication, accessibility | Server authority hoặc balance |
| Technical GDD | Event name, data contract, service constraint | Design intent hướng người chơi |

## Ma Trận Hành Trình Người Chơi

| Hành động | Owner | UI surface | State bắt buộc | Hành vi lỗi | Telemetry | Tài liệu canonical |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Vào account | Settings/System | Login, setup, tutorial gate | loading, linked, blocked, offline | Hiện lý do và route recovery | auth success/failure | [Settings/System](../ui_ux/commerce_settings_system_screens.vi/index.html) |
| Tutorial | Core Gameplay | Tutorial HUD và debrief | checkpoint, hint, pass, retry | Reset checkpoint, không mất vĩnh viễn | tutorial conversion | [Tutorial Raid](../gamedesign/tutorialraid.vi/index.html) |
| Home / chuẩn bị | Core Gameplay | Home, loadout, stash | valid, pending sync, blocked | Giữ Deploy disabled kèm lý do | home impression, deploy intent | [Out-of-Raid](../ui_ux/out_of_raid_screens.vi/index.html) |
| Commit loadout | Inventory / Economy | Loadout Workbench | ready, warning, blocker | Hiện item thiếu hoặc không tương thích | blocker frequency | [Loadout](../gamedesign/loadoutpreparation.vi/index.html) |
| Matchmaking | Matchmaking | Lobby, queue, loading | queued, found, reconnecting | Retry, rời queue hoặc fallback | queue time, cancel, reconnect | [Matchmaking](../gameplay/matchmaking_lobby.vi/index.html) |
| Spawn / orientation | Core Gameplay / AI | HUD, loading | protected spawn, active | Recovery hoặc rollback spawn lỗi | spawn-to-action time | [Core Gameplay](../gamedesign/coregameplay.vi/index.html) |
| Loot | Inventory / Economy | Looting overlay, item detail | available, protected, FIR, full | Overflow hoặc decline với lý do | loot interaction, pickup failure | [Looting](../gameplay/looting_interactions.vi/index.html) |
| Combat | Combat / AI | HUD, hit feedback | damage, armor hit, suppression, downed | Hiện cause và lựa chọn tiếp theo | hit, death reason, TTK | [Weapons](../combat/weapons.vi/index.html) |
| Objective | Progression / Core Gameplay | Objective tracker | active, complete, extraction-required | Giữ hoặc mất progress theo rule | objective completion | [Quest](../gameplay/quest_objective_system.vi/index.html) |
| Extraction | Core Gameplay | Extraction UI | available, holding, contested, blocked | Hiện cancel/contest/outcome rõ ràng | extraction attempt/result | [Extraction](../gameplay/extraction_mechanics.vi/index.html) |
| Death / success | Core Gameplay / Inventory | Debrief, death replay | extracted, KIA, MIA, rollback | Reconcile deterministic | outcome reason | [Debrief](../gameplay/post_game_debrief.vi/index.html) |
| Loot transfer | Inventory / Economy | Loot transfer, stash, inbox | accepted, overflow, pending | Retry hoặc support, không duplicate | transfer success/failure | [Inventory](../inventory_system/_index.vi/index.html) |
| Claim reward | Progression / LiveOps | Inbox, battle pass, event | claimable, claimed, expired, converted | Giữ source và support path | claim funnel | [Progression](../gamedesign/progression.vi/index.html) |
| Mua Commerce | Commerce | Shop, confirmation, receipt | confirm, provider pending, success | Không charge hai lần; support route | purchase funnel | [Commerce](../ui_ux/commerce_screens.vi/index.html) |
| Redeploy | Core Gameplay / Inventory | Home, loadout | ready, blocked, recovery | Trả về blocker đầu tiên | redeploy conversion | [Pre-Raid](../ui_ux/pre_raid_screens.vi/index.html) |

## Quy Tắc Review

- Mọi blocker phải có owner, lý do dễ đọc và next action.
- Mọi item/reward state persistent phải có một owner lifecycle duy nhất.
- Mọi analytics event phải gắn với player action hoặc system transition.
- Rule liên domain phải link tới ma trận này và hai source document sở hữu nó.
- Route chỉ được xem là hoàn tất khi đã map success, failure, offline, reconnecting và pending.

## Checklist Review

- [ ] Không có gameplay rule chỉ được định nghĩa ở UI page.
- [ ] Không có UI state thiếu gameplay, economy, inventory hoặc service source.
- [ ] Raid outcome, reward, item và progression reconcile deterministic.
- [ ] Commerce không grant combat-power item instance.
- [ ] English và Vietnamese dùng cùng ownership boundary.

## Tham Chiếu Chéo

- [Design Decision Register](design_decision_register.vi/index.html)
- [MVP Readiness Review](mvp_readiness_review.vi/index.html)
- [Screen Groups Overview](../ui_ux/screen_groups_overview.vi/index.html)
