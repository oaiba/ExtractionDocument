---
title: "Safe House Design"
linkTitle: "Safe House"
type: docs
weight: 16
---

## Tổng Quan

The Safe House is the người chơi's persistent out-of-raid base. It gives context to stash growth, crafting, upgrades, insurance claims, và long-term identity.

The Safe House should make out-of-raid progress feel grounded. Instead of presenting stash, crafting, traders, và insurance as disconnected menus, it frames them as parts of a base the người chơi improves over thời gian. This gives economic sinks a fiction và gives the người chơi a place to return sau success hoặc failure.

The hệ thống should support long-term goals mà không blocking normal play. Upgrades can tạo efficiency, identity, và new options, nhưng a người chơi không nên feel unable to raid vì a module is incomplete.

## Module Dependency

Dependencies should teach the base gradually. Early modules support basic storage và claims. Powered modules introduce crafting và repairs. Radio-linked modules connect the người chơi to factions, traders, và world events.

| Parent / yêu cầu | Module | mục đích |
| :--- | :--- | :--- |
| Safe House | Stash Room | Storage, sorting, và inventory expansion |
| Safe House | Generator | Powers advanced modules |
| Generator | Workbench | Crafting, repair, và modification support |
| Generator | Medical Station | Recovery và medical crafting support |
| Safe House | Radio | Faction contact và world updates |
| Radio | Trading Post | Trader access và insurance inbox context |
| Stash Room | Workbench | Supplies materials for crafting và upgrades |

## Functional Areas

Each area should have one obvious job. nếu a người chơi wants to claim insurance, the Trading Post nên được the answer. nếu they want to repair gear, the Workbench nên được the answer. Avoid scattering the same action across multiple rooms unless there is a rõ shortcut.

| Area | mục đích | người chơi Action |
| :--- | :--- | :--- |
| Stash Room | Inventory storage và sorting | Store, filter, expand |
| Trophy Vault | Identity và achievement display | View trophies, kiểm tra milestones |
| Workbench | Crafting và repairs | Build, modify, repair |
| Radio | Faction contact và event briefing | Accept tasks, hear world updates |
| Trading Post | Traders và insurance inbox | mua, sell, claim returns |
| Operator Lounge | Home màn hình context | Select operator, view status |

## upgrade Rules

upgrade rules protect motivation. Người chơi nên know what an upgrade changes trước spending resources, và locked modules should show a hiển thị rõ path forward. Seasonal wipe policy phải được announced early vì base progression can represent significant người chơi investment.

| Rule | yêu cầu |
| :--- | :--- |
| rõ benefit | Every module upgrade must trạng thái what changes |
| Economy sink | Upgrades consume credits, items, hoặc reputation |
| No paid-only power | upgrade materials phải được earnable |
| dễ đọc dependency | Locked modules show prerequisite path |
| Seasonal policy | Wipe behavior phải được explicit trước season launch |

## Out-Of-Raid Operator trạng thái

Operator trạng thái can add texture to recovery, nhưng it không nên become a punishment stack. máu, cooldown, và readiness hệ thống should encourage planning và varied operators, not force người chơi to wait instead of playing.

| trạng thái | mục đích | ghi chú |
| :--- | :--- | :--- |
| máu | Recovery pacing | Avoid excessive downtime |
| Energy / hydration | Light planning pressure | Optional depending on hardcore tuning |
| Cooldown | Prevent instant reuse sau severe failure | không nên block all play |
| Morale / readiness | Future flavor hệ thống | cosmetic hoặc narrative first |

## Safe House Examples

sau a failed raid, the người chơi returns to claim insurance, repair damaged gear, và rebuild from stash. The Safe House should make that recovery loop feel intentional instead of like menu cleanup.

sau a successful raid, the người chơi sorts loot, starts a craft, upgrades a module, và chooses what to risk next. This converts extraction giá trị into long-term identity và planning.

trong khi a season event, the Radio can surface faction updates và event objectives while the Trading Post handles reward claims. Người chơi nên understand where seasonal actions live.

## Safe House Failure Cases

- nếu upgrades feel mandatory trước normal raids, progression pressure is too high.
- nếu the same action appears in too many rooms, navigation becomes confusing.
- nếu stash expansion feels paid-only, monetization trust is damaged.
- nếu seasonal wipe policy is unclear, người chơi may avoid investing in upgrades.

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| Economy sinks | [Economy](economy.html) |
| Insurance inbox | [Insurance hệ thống](insurancesystem.html) |
| Home màn hình relation | [Home màn hình & Lobby](homescreen_design.html) |
| Progression unlocks | [Progression](progression.html) |
