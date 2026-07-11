---
title: Sổ Đăng Ký Quyết Định Thiết Kế
linkTitle: Decision Register
type: docs
weight: 8
---

## Mục Đích

Tài liệu này theo dõi các quyết định thiết kế ảnh hưởng tới nhiều hệ thống hoặc chưa đủ điều kiện để xem là canonical. Tài liệu không thay thế source-of-truth của từng system. English vẫn là bản canonical; bản tiếng Việt phục vụ đọc và review.

## Trạng Thái Quyết Định

| Trạng thái | Ý nghĩa | Hành động tiếp theo |
| :--- | :--- | :--- |
| Proposed | Đã có hướng đề xuất nhưng chưa review | Ghi lại phương án và owner |
| Under Review | Đang review bởi design, product hoặc engineering | Ghi evidence và ngày review |
| Approved | Đã là quyết định chính thức cho các tài liệu liên quan | Cập nhật source-of-truth và link |
| Rejected | Phương án bị loại rõ ràng | Ghi lý do để tránh mở lại nhầm |
| Deferred | Chủ động hoãn và chưa chặn scope hiện tại | Ghi điều kiện và mốc review |

## Quy Ước Ghi Quyết Định

Mỗi entry phải có ID ổn định, nội dung quyết định, owner, system bị ảnh hưởng, evidence, tác động MVP và ngày review. Số liệu chưa được approve phải tiếp tục được đánh dấu là placeholder trong tài liệu gameplay và phải xuất hiện ở đây thay vì được trình bày như balance cuối cùng.

## Danh Sách Đang Theo Dõi

| ID | Quyết định | Trạng thái | Owner | System bị ảnh hưởng | Tác động MVP | Hành động tiếp theo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DR-001 | Phạm vi map/content mở ở Season 3 | Under Review | Design / Production | World, LiveOps, Progression, Economy | Xác định ranh giới content sau launch | Chốt phần launch và Season 3 |
| DR-002 | Tuning số liệu Hero Ability | Under Review | Combat / Characters | Combat, Weapons, Accessibility, UI feedback | Chặn balance và telemetry cuối | Chốt test band thay vì chỉ một giá trị |
| DR-003 | Band tuning armor, gear và weapon | Under Review | Combat / Economy | Gear, Weapons, Inventory, Economy | Chặn kiểm tra TTK và cost kit | Chạy mô phỏng loadout đại diện |
| DR-004 | Nhịp unlock stash và container | Under Review | Progression / Inventory | Inventory, Progression, Economy, UI/UX | Ảnh hưởng onboarding và stash pressure | Chốt milestone và overflow policy |
| DR-005 | Mục tiêu tuning economy | Under Review | Economy / Production | Economy, Commerce, Loot, Progression | Chặn review inflation và recovery người mới | Chốt raid value, kit cost và repair ratio |
| DR-006 | Edge case extraction, death, insurance và reward | Under Review | Core Gameplay / Engineering | Raid, Inventory, Economy, Post-Raid | Chặn reconciliation deterministic | Chốt outcome matrix và rollback |
| DR-007 | Difficulty AI và giới hạn reinforcement | Under Review | AI / Combat | AI, Raid Loop, Loot, Matchmaking | Chặn review pacing và frustration | Validate threat band theo phase |
| DR-008 | Matchmaking fallback và reconnect window | Under Review | Multiplayer / Production | Matchmaking, Raid, Social, Loading | Chặn acceptance queue và recovery | Chốt region, low-pop và crash fallback |
| DR-009 | Modifier của Ranked và event | Under Review | Progression / LiveOps | Modes, Ranked, Rewards, UI/UX | Chặn QA theo season | Công bố mode contract và reset |
| DR-010 | Baseline platform và accessibility | Under Review | UX / Engineering | UI/UX, Controls, Settings, QA | Chặn sign-off cross-platform | Chốt target tối thiểu và parity |

## Quy Tắc Review

- Decision `Approved` phải link tới tài liệu canonical liên quan.
- Decision `Deferred` phải nói rõ phần nào vẫn có hiệu lực.
- Tài liệu mâu thuẫn nhau phải link về register và được đánh dấu cần reconcile.
- Product, design và engineering nên review các decision active trước MVP gate.

## Tham Chiếu Chéo

- [Project Scope](_index.vi/index.html)
- [MVP](mvp.vi/index.html)
- [Cross-System Traceability](cross_system_traceability.vi/index.html)
- [MVP Readiness Review](mvp_readiness_review.vi/index.html)
