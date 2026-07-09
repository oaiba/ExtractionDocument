---
title: "Insurance hệ thống Design"
type: docs
---

## Tổng Quan

Insurance softens gear loss mà không removing risk. It lets người chơi pay trước a raid for a chance to recover eligible items that were not extracted by another người chơi.

Insurance is not a refund button. It is a promise that some losses may return later nếu the raid world allows it. The delay matters vì the người chơi still feels the consequence immediately, nhưng the comeback path gives them a reason to log in, check the inbox, và rebuild instead of quitting sau a bad streak.

The người chơi-facing message phải được honest: insured gear can still be lost nếu another người chơi takes it. That uncertainty preserves gear fear và makes địch looting meaningful.

## Quyết Định Chính

| Area | Direction |
| :--- | :--- |
| primary mục đích | Reduce frustration sau death while preserving gear fear |
| purchase moment | Loadout Preparation |
| Return condition | Item must remain unlooted hoặc recoverable sau raid resolution |
| Return timing | Delayed inbox claim, not instant refund |
| Economy role | Credit sink và retention safety valve |
| Competitive rules | Ranked can restrict hoặc disable insurance |

## Insurance Lifecycle

The lifecycle nên được easy to understand at three moments: trước the raid, sau death, và khi the inbox resolves. Người chơi nên never need to guess whether an item was uninsured, looted, pending, returned, blocked by stash space, hoặc excluded by mode rules.

| Step | Event | kết quả |
| :--- | :--- | :--- |
| 1 | người chơi prepares loadout | Eligible items are shown |
| 2 | người chơi selects items và insurer | chi phí và return thời gian are previewed |
| 3 | người chơi pays insurance chi phí | Items are marked insured for the raid |
| 4 | người chơi deploys | Insurance waits for raid resolution |
| 5A | người chơi extracts với insured item | Insurance expires cleanly |
| 5B | người chơi dies và item is looted | Item is lost |
| 5C | người chơi dies và item is recoverable | Return timer starts |
| 6 | Timer completes | Item appears in Safe House inbox |
| 7 | người chơi claims item | Item returns to stash nếu space is available |

## Insurer Options

Insurers tạo a small strategic choice mà không becoming a complicated market. Budget Người chơi có thể protect common gear cheaply và wait longer. High-risk Người chơi có thể pay for faster recovery on chính vũ khí hoặc giáp. More insurers can be added later, nhưng launch should keep the comparison simple.

| Insurer | Positioning | chi phí | Return thời gian | Strength |
| :--- | :--- | :--- | :--- | :--- |
| Viktor Kozlov | Salvage Corps recovery | Lower | Slower | Good for budget và standard gear |
| Ada Chen | Tech Syndicate priority recovery | Higher | Faster | Good for rare hoặc tactical gear |

## Item Eligibility

Eligibility protects the economy from loopholes. Consumables, quest items, secure-container items, và cosmetics follow different risk rules, so they không nên be treated like normal recoverable gear. The UI must explain unavailable insurance với short reasons, not disabled controls với no context.

| Item Type | Insurable | ghi chú |
| :--- | :--- | :--- |
| vũ khí | Yes | chi phí scales với base giá trị và condition |
| giáp | Yes | Damaged gear returns damaged unless repaired separately |
| Backpack | Yes | Backpack returns empty nếu contents are not insured separately |
| Consumables | No | Used hoặc lost as part of raid risk |
| Quest items | Usually no | Prevents bypassing quest risk |
| Secure container contents | Not needed | Already protected by secure container rules |
| Cosmetics | No | Not lost in raid |

## chi phí Formula

```text
Insurance Cost = Item Base Value x Insurer Rate x Condition Modifier x Risk Modifier
```

| Modifier | mục đích |
| :--- | :--- |
| Item Base giá trị | Makes expensive gear more costly to protect |
| Insurer Rate | Differentiates recovery services |
| Condition Modifier | Reduces chi phí for heavily damaged gear |
| Risk Modifier | Allows mode hoặc event tuning |

Designers should tune chi phí around cảm xúc giá trị as well as credit giá trị. A rare vũ khí với strong attachment investment may deserve a higher chi phí band than a simple sell-giá formula suggests. Conversely, damaged hoặc low-tier gear should remain cheap enough that struggling Người chơi có thể cách dùng insurance as a recovery habit.

## UX flow

Insurance UI nên được hiển thị rõ trong khi loadout preparation, nhưng not loud enough to slow every raid. A người chơi nên được able to insure recommended items quickly, kiểm tra chi tiết khi needed, và see the total protected giá trị trước deploying.

| màn hình | người chơi Action | Feedback |
| :--- | :--- | :--- |
| Loadout Preparation | Toggle insurance per item hoặc cách dùng insure-all | chi phí preview và insurer comparison |
| Raid Recap | See insured item status | Returned, looted, pending, hoặc lost |
| Safe House Inbox | claim returned items | Timer, item condition, và storage cảnh báo |
| Economy Summary | See insurance spend | giúp người chơi learn chi phí discipline |

## Edge Case

Edge cases should favor clarity over cleverness. nếu the hệ thống cannot confidently return an item, the recap should explain why. Ambiguous trạng thái tạo support tickets và make người chơi distrust the loss model.

| Case | Rule |
| :--- | :--- |
| người chơi disconnects | Resolve based on final raid trạng thái |
| Item is looted then dropped | Counts as looted unless recovery rules explicitly allow recheck |
| Inventory full on claim | Hold in inbox until space is available |
| Seasonal wipe | Wipe rules override pending insurance unless event policy says otherwise |
| Ranked Ops | Insurance disabled hoặc restricted by season config |

## Insurance Examples

A budget người chơi insures a common rifle và light giáp trước a normal raid. They die near an edge route, the items are not looted, và the gear returns later. The loss still matters vì the người chơi lost backpack loot, thời gian, và immediate access to the kit.

A veteran insures an expensive vũ khí trước pushing a hotspot. Another squad loots the vũ khí sau the fight. The recap should show the item as looted, not mysteriously lost, so the người chơi understands that insurance did not fail.

A ranked season disables insurance. The loadout màn hình should show that rule trước queue confirmation và không nên let the người chơi spend credits on protection that cannot apply.

## Tuning ghi chú

- Insurance chi phí should rise với item giá trị nhưng stay useful for standard gear.
- Return timers should tạo anticipation mà không feeling like mobile-game punishment.
- Insure-all nên được convenient nhưng must display total chi phí clearly.
- Recovery rates nên được monitored by map, mode, gear tier, và người chơi skill.

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| Pre-raid insurance UI | [Loadout Preparation](loadoutpreparation.html) |
| Gear loss rules | [cốt lõi Gameplay](coregameplay.html) |
| Credit sinks | [Economy](economy.html) |
| Safe House inbox | [Safe House Design](safe_house_design.html) |
| Ranked restrictions | [Ranked Mode](rankedmode.html) |
