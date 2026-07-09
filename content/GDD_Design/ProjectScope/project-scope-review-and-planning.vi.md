---
title: "Project Scope - Review, Benchmarks & Planning"
linkTitle: "Scope Review & Planning"
type: docs
weight: 8
version: 1.0
last_updated: 2026-02-12
---

# Project Scope: Review, Thinking & Planning

**Document Type:** Strategic Planning & Benchmarking  
**Purpose:** Review nhóm tài liệu ProjectScope, tham chiếu roadmap/GDD của các game multiplayer hero shooter looter extraction top-down, và lập planning tối ưu.  
**Audience:** Lead Producer, Creative Director, GDD maintainers.

---

## 1. Executive Summary

| Mục | Kết luận |
|:----|:---------|
| **Hiện trạng** | Design Pillars, MVP, Non-Goals, Risks, Competitive Analysis đã rõ; cần giữ link chặt giữa scope và roadmap theo phase. |
| **Tham chiếu genre** | HAWKED, Engines of Fury, Everstorm, Tarkov, Arena Breakout, Delta Force cho thấy các pattern quan trọng: session 15-25 phút, cross-platform, F2P fair, roadmap theo quý, hero/operator + extraction + looter. |
| **Planning đề xuất** | Ưu tiên: đồng bộ MVP milestone với quarterly roadmap; nhấn rõ positioning "hero/looter/top-down"; hoàn thiện GDD còn thiếu; review định kỳ risk D4 và B3. |

---

## 2. Review Hiện Trạng Nhóm ProjectScope

### 2.1 Cấu trúc hiện có

| Document | Mục đích | Độ đầy đủ | Ghi chú |
|:---------|:---------|:----------|:--------|
| **_index.md** | Hub Scope & Vision | Good | Đã có link Competitive Analysis, Scope Review & Planning. |
| **design-pillars-enhanced.md** | 5 Pillars + Genre Pillars | 100% | Chuẩn extraction shooter; nên nhấn thêm top-down/hero positioning. |
| **MVP.md** | Milestones M1-M6, Alpha/Beta scope | ~85% | Có bảng feature comparison và roadmap Q1-Q4. |
| **NonGoals.md** | Explicit exclusions | ~95% | Rõ BR/MMO/Esport/Vehicles/Base/P2W/Loot box. |
| **Risks.md** | Design, Tech, Business, Ops | ~90% | D4 cross-platform và B3 economy cần owner + review cadence. |
| **competitive-analysis-extraction-shooters.md** | Inventory + market benchmark | 100% | Hỗ trợ quyết định scope về inventory, F2P, cross-platform. |

### 2.2 Điểm mạnh

- **Pillars rõ ràng:** Risk of Loss, Tactical Fluidity, Environmental Narrative, Task-Driven Agency, Persistent Progression khớp genre extraction shooter.
- **MVP có số cụ thể:** 1 map khoảng 500x500m, 3 operators ở Alpha, 5 ở Beta, 5 weapons ở Alpha, 15+ ở Beta, session 15-20 phút.
- **Non-Goals và Risks:** Giới hạn scope tốt: không BR, không MMO, không P2W, không loot box.
- **Competitive Analysis:** So sánh Tarkov, Arena Breakout, Delta Force, Hunt, Gray Zone, Marauders để hỗ trợ quyết định scope.

### 2.3 Khoảng trống

1. **Positioning "hero shooter looter extraction top-down"** phải xuất hiện nhất quán trong scope/vision.
2. **Roadmap theo quý** cần dùng được cho stakeholder/investor, không chỉ milestone theo tháng.
3. **Link GDD <-> MVP** cần chỉ rõ doc nào phải xong trước M2, M3, M4.
4. **Risk owner/review cadence** phải rõ với các risk trọng yếu.

---

## 3. Tham Khảo Roadmap & GDD Cùng Thể Loại

| Game | Bài học áp dụng cho scope |
|:-----|:--------------------------|
| **HAWKED** | Roadmap theo quý rõ ràng, accessible extraction, cross-platform sớm, narrative + session quest. |
| **Engines of Fury** | Top-down + extraction + looter + hideout gần với hướng game; tham chiếu boss per zone, crafting tại hideout, trading. |
| **Everstorm** | Hero/class + extraction; progression giữa raid tương tự Hideout/Trader; tham khảo số lượng class/ability. |
| **Escape from Tarkov** | QoL stash/hideout khi queue, seasonal content, optional arena mode có thể defer. |
| **Arena Breakout / Delta Force** | F2P, cross-platform, accessibility, battle pass không P2W, inventory vừa đủ sâu. |

### Bảng tổng hợp tham chiếu

| Tiêu chí | HAWKED | Engines of Fury | Everstorm | Tarkov | Arena Breakout | Delta Force | **Our game (target)** |
|:---------|:-------|:----------------|:----------|:------|:----------------|:------------|:----------------------|
| Session length | ~20-25 min | - | - | 25-45 min | ~45 min mobile | ~1h | **15-20 min** |
| Perspective | Third-person | **Top-down** | **Top-down** | FPS | FPS | FPS/TPP | **Top-down** |
| Hero/Operator | Characters | Customization | **6 classes** | - | Light classes | **Operators** | **Operators (3->5->8+)** |
| Looter depth | Treasure + puzzles | Infinite mods | Professions | Deep inventory | Tetris medium | Medium | **Tetris + weight + containers** |
| Roadmap cadence | Q1-Q4 | - | - | Patches + Arena | Weekly updates | Seasons | **M1-M6 + Q1-Q4** |
| Monetization | F2P, BP | - | - | B2P | F2P fair | F2P + BP | **F2P, no P2W** |

---

## 4. Định Vị Thể Loại

Để scope nhất quán với "multiplayer hero shooter looter extraction top-down":

- **Multiplayer:** 15-20 players/raid; squad 2-3 ở Beta; server-authoritative.
- **Hero shooter:** Operators theo class, passive/active ability, progression theo operator.
- **Looter:** Grid inventory, weight, container, secure container, loot table theo zone.
- **Extraction:** Spawn -> loot/combat -> extract; mất đồ khi chết; insurance.
- **Top-down:** Camera/control/map design khác FPS extraction, cần được nhấn rõ trong scope và MVP.

---

## 5. Planning Đề Xuất Cho ProjectScope

### 5.1 Phase 1: Đồng bộ & bổ sung (0-2 tuần)

| # | Hành động | Owner | Deliverable |
|:--|:---------|:------|:------------|
| 1 | Map M1-M6 sang Q1-Q4. | Lead Producer | Bảng "MVP <-> Quarterly roadmap". |
| 2 | Thêm subsection genre positioning. | Creative Director | 1 paragraph trong scope/vision. |
| 3 | Cập nhật index link Competitive Analysis và Scope Review. | Doc maintainer | `_index.md` với cards/links. |
| 4 | Gắn owner + review cadence cho D4/B3. | Producer | `Risks.md` updated. |

### 5.2 Phase 2: Hoàn thiện GDD theo Master Plan (4-6 tuần)

| # | Hành động | Deliverable |
|:--|:---------|:------------|
| 1 | Combat & Weapons | combat-weapons-database.md + ballistics-system.md |
| 2 | Character & Operators | character-operators.md |
| 3 | Map & Level | map-industrial-zone.md + loot-tables |
| 4 | Economy & Progression | economy-model.md, trader-system, hideout-upgrades |
| 5 | Monetization & Live Ops | monetization-strategy.md, battle-pass-design, seasonal-roadmap |
| 6 | Technical | technical-requirements.md |

### 5.3 Phase 3: Duy trì & review định kỳ

| Tần suất | Nội dung |
|:---------|:---------|
| Hàng tuần | Risk owner cập nhật status trong `Risks.md`. |
| Hàng tháng | So sánh tiến độ thực tế với MVP roadmap; cập nhật Non-Goals nếu có quyết định defer/new. |
| Theo quý | Review competitive roadmap và Design Pillars. |

---

## 6. Roadmap Gợi Ý (Quarterly View)

| Quarter | Milestones từ MVP.md | Nội dung công bố được |
|:--------|:----------------------|:----------------------|
| **Q1** | M1 Prototype, M2 Vertical Slice | Playable greybox, 1 zone polished, combat loop; server/auth validated. |
| **Q2** | M3 Alpha (Internal) | Map 1 full, 3 operators, Scav AI, inventory, stash, vendor. |
| **Q3** | M4 Beta (Closed), M5 Soft Launch | Economy, quests, 5 operators, gunsmith, squad; store + live ops pipeline. |
| **Q4** | M6 Global Launch | Marketing, events, platform cert done. |

---

## 7. Recommendations Tóm Tắt

1. Giữ Design Pillars, MVP, Non-Goals, Risks; bổ sung/duy trì genre positioning và quarterly roadmap.
2. Dùng HAWKED, Engines of Fury, Everstorm, Tarkov, Arena Breakout/Delta Force làm benchmark liên tục.
3. Ưu tiên hoàn thiện Combat, Character, Map, Economy, Monetization, Technical trước; Art/Audio, Narrative, Social sau.
4. D4 (cross-platform balance) và B3 (economy inflation) cần owner rõ và review định kỳ.
5. Giữ link tới Competitive Analysis và Scope Review & Planning để team tìm nhanh.

---

## 8. Tài Liệu Tham Khảo

- HAWKED 2024 roadmap.
- HAWKED design: extraction shooter evolution.
- Engines of Fury: Diablo meets top-down extraction shooter.
- Everstorm: MOBA controls, 6 classes, professions.
- Escape from Tarkov 2024 roadmap.
- Extraction shooter GDD/scope references.
- Competitive Analysis nội bộ.

---

## 9. Changelog & Ownership

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| 1.1 | 2026-02-12 | - | Applied planning: genre positioning, MVP <-> Q1-Q4, owner/review cho D4/B3. |
| 1.0 | 2026-02-12 | - | Initial review ProjectScope, benchmark roadmaps/GDD, planning phases. |

**Owner:** Lead Producer / Doc maintainer.  
**Review:** Quarterly hoặc khi có thay đổi lớn về scope/roadmap.
