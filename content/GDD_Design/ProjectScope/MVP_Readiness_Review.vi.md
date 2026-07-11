---
title: Review Mức Độ Sẵn Sàng MVP
linkTitle: MVP Readiness
type: docs
weight: 10
---

## Mục Đích

Trang này là góc nhìn readiness của bộ design docs cho MVP. Nó ghi nhận domain nào đủ sẵn sàng để review và trỏ tới evidence hoặc decision còn thiếu. Đây không phải bản thay thế cho tài liệu canonical của từng system.

## Từ Vựng Trạng Thái

| Trạng thái | Ý nghĩa |
| :--- | :--- |
| Complete | Rule và hành vi hướng người chơi đã rõ; còn bước validate implementation |
| Needs Balancing | Rule có nhưng thiếu tuning hoặc playtest evidence |
| Needs Engineering Decision | Phụ thuộc service, platform hoặc technical constraint chưa chốt |
| Needs UX Validation | Hành vi có nhưng layout, accessibility hoặc platform validation chưa đủ |
| Placeholder | Intent có nhưng content hoặc value quan trọng chưa final |
| Out of MVP Scope | Được loại khỏi launch hiện tại |
| Blocked | Chưa thể tiếp tục nếu dependency chưa được giải quyết |

## Readiness Theo Domain

| Domain | Trạng thái | Evidence | Decision/risk còn thiếu | Owner |
| :--- | :--- | :--- | :--- | :--- |
| Project Scope | Needs Engineering Decision | [MVP](mvp.vi/index.html), [Risks](risks.vi/index.html) | Chốt launch và Season 3 | Production |
| Core Gameplay | Needs Balancing | [Core Gameplay](../gamedesign/coregameplay.vi/index.html), [Extraction](../gameplay/extraction_mechanics.vi/index.html) | Validate raid length, extraction rate, recovery | Game Design |
| AI | Needs Balancing | [AI & Enemy Behavior](../gameplay/ai_enemy_behavior.vi/index.html) | Validate threat band, reinforcement, frustration | AI / Combat |
| Combat / Weapons | Needs Balancing | [Weapons](../combat/weapons.vi/index.html), [Weapon Balance](../weapons/weapon_balance_framework.vi/index.html) | Chốt TTK band và outlier threshold | Combat |
| Inventory / Gear / Loadout | Needs UX Validation | [Inventory](../inventory_system/_index.vi/index.html), [Loadout](../gamedesign/loadoutpreparation.vi/index.html) | Validate stash pressure, comparison, blocker | Inventory / UX |
| Economy | Needs Balancing | [Economy](../gamedesign/economy.vi/index.html), [Commerce](../ui_ux/commerce_screens.vi/index.html) | Chốt kit cost, repair và recovery | Economy |
| Progression / LiveOps | Needs Engineering Decision | [Progression](../gamedesign/progression.vi/index.html), [LiveOps](../gamedesign/liveops.vi/index.html) | Chốt reset, expiry và reward service | Progression / LiveOps |
| Commerce | Needs Engineering Decision | [Commerce Screens](../ui_ux/commerce_screens.vi/index.html) | Chốt provider, region, refund, entitlement | Commerce |
| UI/UX | Needs UX Validation | [Global UX Standards](../ui_ux/global_ux_standards.vi/index.html), screen groups | Validate focus, mobile và offline | UX |
| Social / Multiplayer | Needs Engineering Decision | [Matchmaking](../gameplay/matchmaking_lobby.vi/index.html), [Social Screens](../ui_ux/social_screens.vi/index.html) | Chốt party, reconnect, moderation, voice | Multiplayer |
| Characters / Abilities | Placeholder | [Hero Abilities](../gameplay/hero_abilities.vi/index.html) | Approve ability numbers và counterplay | Characters / Combat |
| World / Maps | Placeholder | [World](../world/_index.vi/index.html), [Project Scope](_index.vi/index.html) | Chốt zone và Season 3 content | World |
| Narrative | Needs UX Validation | [Story](../story/_index.vi/index.html), [Narrative World](../narrativeworld/_index.vi/index.html) | Validate delivery với onboarding/LiveOps | Narrative |
| Audio / Visuals | Needs UX Validation | [Audio](../audio/_index.vi/index.html), [Visuals](../visuals/_index.vi/index.html) | Validate cue/readability cross-platform | Audio / Visuals |
| Accessibility | Needs UX Validation | [Accessibility](../gamedesign/accessibility.vi/index.html) | Hoàn thiện input, contrast, caption, motion | UX |
| Anti-Cheat / Fair Play | Needs Engineering Decision | [Anti-Cheat](../gameplay/anti_cheat_fair_play.vi/index.html) | Chốt provider và enforcement operation | Engineering |

## Điều Kiện MVP Gate

- [ ] Người chơi mới hoàn thành tutorial và hiểu extraction, death, loss, redeploy.
- [ ] Loadout validation nêu mọi blocker và next action.
- [ ] Raid outcome, reward, insurance, item lifecycle reconcile deterministic.
- [ ] Combat feedback giải thích armor, damage, suppression và death cause.
- [ ] AI có tell, counterplay và reinforcement có giới hạn.
- [ ] Economy không tạo bankruptcy không kiểm soát hoặc pay-to-win power.
- [ ] UI error, offline, reconnecting và pending đều có recovery action.
- [ ] Route English/Vietnamese build được, không broken link hoặc lỗi encoding.
- [ ] Decision critical `Under Review` đã được approve hoặc defer rõ ràng.

## Nhịp Review

Review trang này sau mỗi design wave lớn, trước external playtest, content lock và MVP sign-off. Mọi item `Blocked` hoặc `Needs Engineering Decision` phải link tới [Design Decision Register](design_decision_register.vi/index.html).

## Tham Chiếu Chéo

- [Design Decision Register](design_decision_register.vi/index.html)
- [Cross-System Traceability](cross_system_traceability.vi/index.html)
- [MVP](mvp.vi/index.html)
