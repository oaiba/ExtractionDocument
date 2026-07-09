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

## Presets

Presets should accelerate common intentions mà không removing người chơi authorship. A budget kit giúp sau losses, a standard kit supports reliable raids, và objective presets reduce forgetfulness. Presets nên được editable sau selection so người chơi learn rather than blindly accept.

| Preset Type | mục đích |
| :--- | :--- |
| Budget | Low-risk recovery và practice |
| Standard | Balanced raid kit |
| Objective | Quest-cụ thể gear |
| Squad Role | Team role kit such as scout, medic, anchor |
| Custom | người chơi-defined saved loadout |

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
| cốt lõi raid loop | [cốt lõi Gameplay](coregameplay.html) |
| Insurance | [Insurance hệ thống](insurancesystem.html) |
| Economy và gear giá trị | [Economy](economy.html) |
| Controls và mobile input | [Controls](controls.html) |
| Map và mode choice | [Map Design](mapdesign.html), [Game Modes](gamemodes.html) |
