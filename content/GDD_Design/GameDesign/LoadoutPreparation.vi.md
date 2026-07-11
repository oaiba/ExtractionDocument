---
title: "Pre-Raid Loadout & Preparation màn hình"
type: docs
---

## Tổng Quan

Loadout Preparation is the ritual trước risk. It must giúp người chơi understand what they are bringing, what they can lose, which objective they are chasing, và whether the squad is ready.

Màn hình này nên make gear fear productive. Người chơi nên feel the weight of the quyết định mà không feeling trapped in inventory management. A good prep flow lets experts optimize quickly và lets newer người chơi trust recommended cảnh báo, presets, và objective hints.

The màn hình is also a communication surface for the squad. It should show who is ready, who lacks đạn hoặc healing, who is over weight, và whether the selected mode changes insurance hoặc loss rules.

## Quyết Định Chính

| Area | Direction |
| :--- | :--- |
| primary job | Make risk legible trước khi deploy |
| cốt lõi surfaces | Operator, gear, stash, insurance, mode, map, squad |
| Layout standard | PC/Console multi-column workbench |
| Deploy gate | Block only critical invalid trạng thái |

## Loadout System Model

Loadout preparation biến inventory state thành quyết định bước vào raid. Màn hình này phải validate physical kit, giải thích risk, giữ player intent, và ngăn việc deploy nhầm với critical gear bị thiếu.

| Entity | Định nghĩa | Yêu cầu UI / Design |
| :--- | :--- | :--- |
| `Loadout` | Bộ đầy đủ gồm operator, gear, accessible items, storage, mission context, squad readiness | Show readiness, value, weight, blockers, warnings, deployment consequence |
| `GearSlot` | Equipment position nhận item instances | Nêu accepted categories, current item, durability/ammo nếu relevant, lock reason |
| `RequiredSlot` | Slot hoặc requirement có thể block deploy | Phải show missing/invalid reason và direct fix route |
| `OptionalSlot` | Slot cải thiện readiness nhưng không luôn block deploy | Dùng advisory/warning language, không tạo false blocker |
| `ValidationRule` | Deploy readiness check | Có severity, first blocker copy, direct fix, platform-safe focus target |
| `RiskSummary` | Persistent summary của loadout value, weight, insurance, ammo, meds, quest items, mode rules | Luôn visible khi browsing stash hoặc presets |
| `Preset` | Saved hoặc suggested kit configuration | Show missing items, substitutions, cost, capacity result, overwrite/delete confirmation |
| `InsuranceSelection` | Player chọn protect eligible item instances | Show eligible/ineligible counts, cost, provider/rule, return timer, mode restrictions |

## Loadout flow

The flow is ordered from identity to commitment. Operator comes first vì it shapes role và abilities. Gear và stash come next vì they define risk. Mode, map, insurance, và squad readiness come last vì they decide the context where that risk will be spent.

| Step | Action | kết quả |
| :--- | :--- | :--- |
| 1 | Choose operator | Ability, role, và nhân vật identity are set |
| 2 | Equip vũ khí và giáp | Combat readiness và gear giá trị update |
| 3 | Pack meds, tools, và backpack | Survival tools và carry capacity update |
| 4 | Select mode và map | Rules, extracts, và risk profile are set |
| 5 | Review insurance | Eligible items are protected hoặc intentionally left uninsured |
| 6 | Squad ready check | Party voice, fill, và ready status are confirmed |
| 7 | Deploy | Matchmaking starts |

## PC / Console Layout

The PC/console layout can operate like a workbench: kiểm tra the kit, manipulate inventory, và review mission context at the same thời gian. The layout should reduce back-và-forth by keeping giá trị, weight, và readiness hiển thị rõ while the người chơi edits gear.

| Region | Content | mục đích |
| :--- | :--- | :--- |
| Left column | Operator, gear slots, weight, insurance status | Read loadout trong một nhịp nhìn |
| Center column | Stash grid, filters, item chi tiết | Equip và manage items |
| Right column | Mode, map, quests, squad, deploy button | Commit to raid |
| Footer | Loadout giá trị, risk cảnh báo, preset controls | Keep risk hiển thị rõ |

## Loadout Summary

cảnh báo nên được educational, not scolding. "No compatible đạn" is more useful than "invalid loadout." "High uninsured giá trị" teaches risk. "Quest item missing" prevents wasted raids. Each cảnh báo should point to a cách sửa trực tiếp.

| Signal | Display Rule |
| :--- | :--- |
| Gear giá trị | Always hiển thị rõ trước khi deploy |
| Weight | Show hiện tại và max carry weight |
| đạn readiness | Warn nếu vũ khí has no compatible đạn |
| Healing readiness | Warn nếu no healing item is equipped |
| Insurance | Show insured, uninsured, và ineligible counts |
| Quest items | Highlight required equipment hoặc objectives |

## Readiness Severity

| Severity | Deploy Behavior | Copy Rule | Examples |
| :--- | :--- | :--- | :--- |
| Blocker | Không thể deploy tới khi fix | Name first blocker và focus fix target | Missing primary weapon, invalid container item, squad/mode restriction |
| Warning | Có thể deploy sau acknowledgement/confirmation | Explain risk và consequence, không scold | Missing meds, high uninsured value, low weapon durability |
| Advisory | Không block và không cần confirmation | Teach optimization và suggest một action | Sidearm empty, low value-per-slot, recommended armor upgrade |

## Loadout Validation Matrix

| Validation | Severity | Required Behavior |
| :--- | :--- | :--- |
| Missing primary weapon | Blocker | Focus primary weapon slot và filter compatible weapons |
| Missing compatible ammo | Warning hoặc blocker theo mode | Show ammo caliber, required magazine/ammo count, compatible filter |
| No meds | Warning | Suggest medical filter và budget med source |
| No extraction objective item | Warning hoặc blocker theo quest | Show quest, source, stash/trader/map route |
| Overweight / critical weight | Blocker hoặc warning theo tuning | Show weight source, suggested removals, movement penalty |
| Incompatible attachment | Blocker | Show incompatible node và valid replacements |
| Broken armor | Blocker nếu protection rule yêu cầu | Route tới repair, replacement, hoặc remove item |
| Low durability weapon | Warning | Show malfunction/durability risk và repair route |
| Uninsured high value | Warning | Show uninsured value, eligible count, Insure All, ineligible reasons |
| Invalid container item | Blocker | Show container rule: category, size, secure-container, contraband, hoặc mode restriction |
| Quest item missing | Warning hoặc blocker theo selected objective | Show objective consequence và direct stash/quest route |
| Squad not ready | Blocker | Show member nào đang block và lý do |
| Mode restriction | Blocker | Show mode rule: gear tier cap, insured disabled, contraband forbidden, hoặc ranked rule |

## Gear Comparison / Equip Decision

| Compare Input | Requirement |
| :--- | :--- |
| Slot compatibility | Show valid slots, conflicts, required unequip/move actions |
| Stats delta | Compare class, durability, armor zones, ammo count, storage cells, access speed, weight, mobility impact |
| Value impact | Show item value, loadout total value, sell/trader relevance, insurance cost impact |
| Durability / repair | Show current/max durability, repair route, effective performance impact |
| Risk flags | Show FIR, quest, protected, insured, contraband, locked, equipped, high-value flags |
| Recommended action | Explain vì sao nên Equip, Keep, Repair, Insure, Sell, hoặc Do Not Deploy |

## Presets

Presets should accelerate common intentions mà không removing người chơi authorship. A budget kit giúp sau losses, a standard kit supports reliable raids, và objective presets reduce forgetfulness. Presets nên được editable sau selection so người chơi learn rather than blindly accept.

| Preset Type | mục đích |
| :--- | :--- |
| Budget | Low-risk recovery và practice |
| Standard | Balanced raid kit |
| Objective | Quest-cụ thể gear |
| Squad Role | Team role kit such as scout, medic, anchor |
| Custom | người chơi-defined saved loadout |

### Preset Rules

| Rule | Requirement |
| :--- | :--- |
| Apply preview | Show mọi item sẽ equip, move, buy, substitute, hoặc còn missing |
| Missing items | List missing items với source routes: stash, trader, craft, quest, budget substitute |
| Substitutions | Name substitute và explain thay đổi: ammo, armor class, storage capacity, weight, value |
| Cost | Show credits, trader requirements, insurance delta, stash capacity result trước commit |
| Overwrite/delete | Require confirmation và show preset name |
| Squad role preset | Show intended role và minimum required items để squad hiểu readiness |
| Objective preset | Show quest objective, required items, FIR requirements, extraction/map constraints |

## Insurance And Risk Rules

| Rule | Requirement |
| :--- | :--- |
| Eligible items | Show eligible count, cost, provider/rule, return timer |
| Ineligible items | Show exact reason: item type, contraband, mode, ownership, account rule, already insured |
| High-value threshold | Warn khi uninsured eligible value vượt tuning threshold |
| Mode-specific insurance | Nếu selected mode đổi insurance, show rule trước Ready CTA |
| Insure All | Chỉ áp dụng eligible selected/current loadout items và summarize skipped items |
| Remove insured item | Require confirmation nếu removal đổi risk summary hoặc insurance plan |
| Return expectation | Không imply guaranteed return nếu insurance design probabilistic/conditional |

## Deploy Validation

| trạng thái | Behavior |
| :--- | :--- |
| Missing vũ khí | Block deploy |
| Missing đạn | Warn, allow only với explicit confirmation |
| Overweight | Block hoặc force item removal |
| High gear giá trị | Warn |
| No insurance | Warn nếu eligible items are present |
| Squad not ready | Wait until all required người chơi ready |

## Preparation Examples

A người chơi selects a budget preset sau several failed raids. The màn hình should keep risk low, warn about missing healing, và suggest a route hoặc mode that supports recovery.

A squad prepares for a high-giá trị objective. The màn hình should show each member's readiness, squad size, selected map, uninsured giá trị, và any mode rules that change extraction hoặc insurance.

A người chơi equips a quest item nhưng forgets compatible đạn. The deploy gate should block hoặc warn clearly và provide a direct path to the missing item filter.

## Preparation Failure Cases

- nếu người chơi deploy mà không đạn by accident, validation is too weak.
- nếu người chơi cannot tell why deploy is blocked, error messaging is too vague.
- nếu mobile stash editing requires too many màn hình changes, persistent summary và quick equip need improvement.
- nếu squads wait on one người chơi mà không knowing why, readiness chi tiết nên được more hiển thị rõ.

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| cốt lõi raid loop | [cốt lõi Gameplay](coregameplay/index.html) |
| Insurance | [Insurance hệ thống](insurancesystem/index.html) |
| Economy và gear giá trị | [Economy](economy/index.html) |
| Controls và mobile input | [Controls](controls/index.html) |
| Map và mode choice | [Map Design](mapdesign/index.html), [Game Modes](gamemodes/index.html) |
