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
| Project Scope | Needs Engineering Decision | [MVP](MVP.vi.md), [Risks](Risks.vi.md) | Chốt launch và Season 3 | Production |
| Core Gameplay | Needs Balancing | [Core Gameplay](../GameDesign/CoreGameplay.vi.md), [Extraction](../Gameplay/Extraction_Mechanics.vi.md) | Validate raid length, extraction rate, recovery | Game Design |
| AI | Needs Balancing | [AI & Enemy Behavior](../Gameplay/AI_Enemy_Behavior.vi.md) | Validate threat band, reinforcement, frustration | AI / Combat |
| Combat / Weapons | Needs Balancing | [Weapons](../Combat/Weapons.vi.md), [Weapon Balance](../Weapons/Weapon_Balance_Framework.vi.md) | Chốt TTK band và outlier threshold | Combat |
| Inventory / Gear / Loadout | Needs UX Validation | [Inventory](../Inventory_System/_index.vi.md), [Loadout](../GameDesign/LoadoutPreparation.vi.md) | Validate stash pressure, comparison, blocker | Inventory / UX |
| Economy | Needs Balancing | [Economy](../GameDesign/Economy.vi.md), [Commerce](../UI_UX/Commerce_Screens.vi.md) | Chốt kit cost, repair và recovery | Economy |
| Progression / LiveOps | Needs Engineering Decision | [Progression](../GameDesign/Progression.vi.md), [LiveOps](../GameDesign/LiveOps.vi.md) | Chốt reset, expiry và reward service | Progression / LiveOps |
| Commerce | Needs Engineering Decision | [Commerce Screens](../UI_UX/Commerce_Screens.vi.md) | Chốt provider, region, refund, entitlement | Commerce |
| UI/UX | Needs UX Validation | [Global UX Standards](../UI_UX/Global_UX_Standards.vi.md), screen groups | Validate focus, mobile và offline | UX |
| Social / Multiplayer | Needs Engineering Decision | [Matchmaking](../Gameplay/Matchmaking_Lobby.vi.md), [Social Screens](../UI_UX/Social_Screens.vi.md) | Chốt party, reconnect, moderation, voice | Multiplayer |
| Characters / Abilities | Placeholder | [Hero Abilities](../Gameplay/Hero_Abilities.vi.md) | Approve ability numbers và counterplay | Characters / Combat |
| World / Maps | Placeholder | [World](../World/_index.vi.md), [Project Scope](_index.vi.md) | Chốt zone và Season 3 content | World |
| Narrative | Needs UX Validation | [Story](../Story/_index.vi.md), [Narrative World](../NarrativeWorld/_index.vi.md) | Validate delivery với onboarding/LiveOps | Narrative |
| Audio / Visuals | Needs UX Validation | [Audio](../Audio/_index.vi.md), [Visuals](../Visuals/_index.vi.md) | Validate cue/readability cross-platform | Audio / Visuals |
| Accessibility | Needs UX Validation | [Accessibility](../GameDesign/Accessibility.vi.md) | Hoàn thiện input, contrast, caption, motion | UX |
| Anti-Cheat / Fair Play | Needs Engineering Decision | [Anti-Cheat](../Gameplay/Anti_Cheat_Fair_Play.vi.md) | Chốt provider và enforcement operation | Engineering |

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

Review trang này sau mỗi design wave lớn, trước external playtest, content lock và MVP sign-off. Mọi item `Blocked` hoặc `Needs Engineering Decision` phải link tới [Design Decision Register](Design_Decision_Register.vi.md).

## Tham Chiếu Chéo

- [Design Decision Register](Design_Decision_Register.vi.md)
- [Cross-System Traceability](Cross_System_Traceability.vi.md)
- [MVP](MVP.vi.md)
