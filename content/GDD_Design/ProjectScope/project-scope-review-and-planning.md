---
title: "Project Scope – Review, Benchmarks & Planning"
linkTitle: "Scope Review & Planning"
type: docs
weight: 8
version: 1.0
last_updated: 2026-02-12
---

# Project Scope: Review, Thinking & Planning

**Document Type:** Strategic Planning & Benchmarking  
**Purpose:** Review group tài liệu ProjectScope, tham chiếu roadmap/GDD các tựa game multiplayer hero shooter looter extraction top-down, và lập planning tối ưu.  
**Audience:** Lead Producer, Creative Director, GDD maintainers.

---

## 1. Executive Summary

| Mục | Kết luận |
|:----|:---------|
| **Hiện trạng** | Design Pillars, MVP, Non-Goals, Risks, Competitive Analysis đã rõ; thiếu link rõ ràng giữa scope ↔ roadmap theo phase (theo chuẩn genre). |
| **Tham chiếu genre** | HAWKED, Engines of Fury, Everstorm, Tarkov, Arena Breakout, Delta Force cho thấy: session 15–25 phút, cross-platform, F2P fair, roadmap theo quý (Q1–Q4), hero/operator + extraction + looter. |
| **Planning đề xuất** | Ưu tiên: (1) Đồng bộ MVP milestones với roadmap theo quý; (2) Bổ sung “Hero/Looter/Top-down” vào positioning; (3) Hoàn thiện các GDD còn thiếu (Combat, Character, Map, Economy, …); (4) Review risk D4 và B3 định kỳ. |

---

## 2. Review Hiện Trạng Nhóm ProjectScope

### 2.1 Cấu trúc hiện có

| Document | Mục đích | Độ đầy đủ | Ghi chú |
|:---------|:---------|:----------|:--------|
| **_index.md** | Hub Scope & Vision |  | Đã có link Competitive Analysis, Scope Review & Planning. |
| **design-pillars-enhanced.md** | 5 Pillars + Genre Pillars |  100% | Chuẩn extraction shooter; có thể bổ sung “top-down / hero” positioning. |
| **MVP.md** | Milestones M1–M6, Alpha/Beta scope |  ~85% | Có bảng so sánh feature; chưa map rõ theo quý (Q1–Q4) như HAWKED/Tarkov. |
| **NonGoals.md** | Explicit exclusions |  ~95% | Rõ BR/MMO/Esport/Vehicles/Base/P2W/Loot box; ổn. |
| **Risks.md** | Design, Tech, Business, Ops |  ~90% | D4 cross-platform, B3 economy đã có; nên gắn owner + review cadence. |
| **competitive-analysis-extraction-shooters.md** | Inventory + market |  100% | Tốt cho scope quyết định (Tetris, weight, F2P, cross-platform). |
| *(GDD gap roadmap)* | — | — | Character/Combat/Map/Economy/Monetization/Technical/Art/Narrative/Social chưa có doc riêng. |

### 2.2 Điểm mạnh

- **Pillars rõ ràng:** Risk of Loss, Tactical Fluidity, Environmental Narrative, Task-Driven Agency, Persistent Progression — khớp genre extraction shooter.
- **MVP có số cụ thể:** 1 map ~500×500m, 3 operators (Alpha) → 5 (Beta), 5 weapons (Alpha) → 15+ (Beta), session 15–20 phút.
- **Non-Goals và Risks:** Giới hạn scope tốt (không BR, không MMO, không P2W, không loot box).
- **Competitive Analysis:** So sánh Tarkov, Arena Breakout, Delta Force, Hunt, Gray Zone, Marauders — hỗ trợ quyết định scope (inventory, F2P, cross-platform).

### 2.3 Khoảng trống (Gaps)

1. **Positioning “hero shooter looter extraction top-down”** chưa được ghi thành mục riêng trong scope/vision (game là top-down, có operator/class, có looter loop).
2. **Roadmap theo quý** chưa map trực tiếp: MVP.md có M1–M6 theo tháng nhưng chưa có bảng Q1–Q4 công bố được (cho stakeholder/investor).
3. **Link GDD ↔ MVP:** Các doc còn thiếu (Combat, Character, Map, Economy, v.v.) chưa được đặt trong timeline “sau M2” hay “trước M4”.
4. **_index** đã dẫn tới Competitive Analysis và Scope Review & Planning.

---

## 3. Tham Khảo Roadmap & GDD Cùng Thể Loại

### 3.1 HAWKED (PvPvE extraction, cross-platform, F2P)

| Nguồn | Nội dung chính |
|:------|:----------------|
| Roadmap 2024 | **Q1:** Global cross-platform (PC, PS4/5, Xbox), UI rework. **Q2:** Ranked PvP, Codex, Steam Deck/EGS. **Q3:** New locations, story, weapons, enemies, Crafting, Black Market. **Q4:** Final story chapter, limited-time event. |
| GDD / Design | “Expedition” (A→B + collect), accessible-casual, flashy/fun; competitive treasure hunting; puzzles + traps + environment; comic style; hideout + storyline quest trong session. |
| Áp dụng cho scope | Roadmap theo quý rõ ràng; “accessible nhưng có depth”; narrative + session quest; cross-platform từ Q1. |

### 3.2 Engines of Fury (Top-down extraction, Diablo-like)

| Nguồn | Nội dung chính |
|:------|:----------------|
| Positioning | Diablo meets extraction shooter; infiltrate → scavenge → extract to hideout; 3–5 bosses per location; infinite gear mods; crafting; player trading. |
| Áp dụng cho scope | Top-down + extraction + looter + hideout rất gần với game của chúng ta; có thể tham chiếu “boss per zone”, “crafting tại hideout”, “trading”. |

### 3.3 Everstorm (MOBA controls, top-down extraction)

| Nguồn | Nội dung chính |
|:------|:----------------|
| Design | 6 classes, 5 base abilities + passive; “storm spells” mua trong raid; professions (Alchemy, Blacksmithing) giữa các raid. |
| Áp dụng cho scope | Hero/class + extraction; progression giữa raid (professions) tương tự Hideout/Trader; có thể tham khảo số lượng class/ability. |

### 3.4 Escape from Tarkov (Roadmap 2024)

| Nguồn | Nội dung chính |
|:------|:----------------|
| Technical | Unity 2022, FSR 3/DLSS 3; QoL: stash/hideout while queuing, lock items. |
| Content | Seasonal weather; Ground Zero rework; new weapons; endgame scenario. Arena: Overrun (5p), Shootout Tournament, battle pass, sync với main game. |
| Áp dụng cho scope | QoL stash/hideout khi queue; seasonal content; optional “arena” mode (có thể defer như Non-Goals). |

### 3.5 Arena Breakout: Infinite & Delta Force

| Game | Điểm chính cho scope |
|:-----|:--------------------|
| **Arena Breakout** | F2P, mobile+PC; simplified grid + auto-organize; retention cao nhờ accessibility; session ~45 phút (mobile). |
| **Delta Force** | Cross-platform (PC, console, mobile); operator + extraction; vehicle storage; Battle Pass; tránh P2W và grind quá nặng. |

### 3.6 Bảng tổng hợp tham chiếu

| Tiêu chí | HAWKED | Engines of Fury | Everstorm | Tarkov | Arena Breakout | Delta Force | **Our game (target)** |
|:---------|:-------|:----------------|:----------|:------|:----------------|:------------|:----------------------|
| Session length | ~20–25 min | — | — | 25–45 min | ~45 min (mobile) | ~1h | **15–20 min** (MVP) |
| Perspective | Third-person | **Top-down** | **Top-down** | FPS | FPS | FPS/TPP | **Top-down** |
| Hero/Operator | Characters | Customization | **6 classes** | — | Light classes | **Operators** | **Operators (3→5→8+)** |
| Looter depth | Treasure + puzzles | Infinite mods | Professions | Deep inventory | Tetris medium | Medium | **Tetris + weight + containers** |
| Roadmap cadence | Q1–Q4 | — | — | Patches + Arena | Weekly updates | Seasons | **M1–M6 + nên thêm Q1–Q4** |
| Cross-platform |  Q1 | — | — | PC |  |  | **Crossplatform (scope)** |
| Monetization | F2P, BP | — | — | B2P | F2P fair | F2P + BP | **F2P, no P2W** |

---

## 4. Định Vị Thể Loại: Hero Shooter Looter Extraction Top-Down

Để scope nhất quán với mô tả “multiplayer hero shooter looter extraction top-down”:

- **Multiplayer:** 15–20 players/raid; squad 2–3 (Beta); server-authoritative.  Đã có trong MVP/Risks.
- **Hero shooter:** Operators với class (Assault, Scout, Support, Tank, Specialist), passive/active abilities, progression per operator.  Có trong MVP; đã ghi rõ trong _index và design-pillars.
- **Looter:** Grid inventory, weight, containers, secure container, loot tables theo zone.  Có trong Inventory/Gear và Competitive Analysis.
- **Extraction:** Spawn → loot/combat → extract; mất đồ khi chết; insurance.  Có trong Pillars + MVP.
- **Top-down:** Camera và control scheme top-down (khác Tarkov/Arena FPS).  Nên nêu rõ trong Project Scope / MVP (view, control, map design cho top-down).

**Đề xuất:** Thêm một đoạn ngắn vào **Project Scope (_index hoặc MVP)** khẳng định: “Multiplayer hero shooter looter extraction, top-down perspective, cross-platform, session 15–20 phút, F2P fair.”

---

## 5. Planning Đề Xuất Cho Nhóm ProjectScope

### 5.1 Phase 1: Đồng bộ & bổ sung (0–2 tuần)

| # | Hành động | Owner | Deliverable |
|:--|:---------|:------|:------------|
| 1 | Map MVP milestones (M1–M6) sang roadmap Q1–Q4 (ví dụ M1–M2 = Q1, M3 = Q2, M4–M5 = Q3, M6 = Q4). | Lead Producer | Bảng “MVP ↔ Quarterly roadmap” trong MVP.md hoặc doc riêng. |
| 2 | Thêm subsection “Genre positioning” (hero shooter looter extraction top-down) vào _index hoặc design-pillars. | Creative Director | 1 paragraph trong scope/vision. |
| 3 | Cập nhật _index: link Competitive Analysis, Scope Review & Planning. | Suture maintainer | _index.md với cards/links. |
| 4 | Gắn Risk owner + review cadence rõ (ví dụ D4, B3 review hàng tháng). | Producer | Risks.md updated. |

### 5.2 Phase 2: Hoàn thiện GDD theo Master Plan (4–6 tuần)

| # | Hành động | Tham chiếu | Deliverable |
|:--|:---------|:-----------|:------------|
| 1 | Combat & Weapons (weapon DB, ballistics, TTK). | — | combat-weapons-database.md + ballistics-system.md. |
| 2 | Character & Operators (5–8 operators, progression). | — | character-operators.md. |
| 3 | Map & Level (Industrial Zone, loot tables, extracts). | — | map-industrial-zone.md + loot-tables. |
| 4 | Economy & Progression (currency, traders, hideout). | — | economy-model.md, trader-system, hideout-upgrades. |
| 5 | Monetization & Live Ops (BP, seasons, no P2W). | — | monetization-strategy.md, battle-pass-design, seasonal-roadmap. |
| 6 | Technical (device specs, server, anti-cheat). | — | technical-requirements.md. |

Các mảng Art/Audio, Narrative, Social ưu tiên sau.

### 5.3 Phase 3: Duy trì & review (định kỳ)

| Tần suất | Nội dung |
|:---------|:---------|
| Hàng tuần | Risk owners cập nhật status (risks/index.html). |
| Hàng tháng | So sánh tiến độ thực tế với MVP roadmap; cập nhật Non-Goals nếu có quyết định defer/new. |
| Theo quý | Review competitive (roadmap HAWKED, Arena Breakout, Delta Force); cập nhật Competitive Analysis nếu cần; review Design Pillars (đã có quarterly trong design-pillars-enhanced). |

---

## 6. Roadmap Gợi Ý (Quarterly View)

Để dễ đối chiếu với HAWKED/Tarkov và báo cáo stakeholder:

| Quarter | Milestones (từ MVP.md) | Nội dung công bố được (high-level) |
|:--------|:----------------------|:-----------------------------------|
| **Q1** | M1 Prototype, M2 Vertical Slice | Playable greybox, 1 zone polished, combat loop; server/auth validated. |
| **Q2** | M3 Alpha (Internal) | Map 1 full, 3 operators, Scav AI, inventory, stash, vendor. |
| **Q3** | M4 Beta (Closed), M5 Soft Launch | Economy, quests, 5 operators, gunsmith, squad; store + live ops pipeline. |
| **Q4** | M6 Global Launch | Marketing, events, platform cert done. |

Có thể thêm cột “Content themes” (ví dụ Q3 = “Economy & Quests”, Q4 = “Launch & Events”) để gần với cách HAWKED/Tarkov trình bày roadmap.

---

## 7. Recommendations Tóm Tắt

1. **Scope doc:** Giữ nguyên Design Pillars, MVP, Non-Goals, Risks; bổ sung **genre positioning** (hero shooter looter extraction top-down) và **quarterly roadmap** (map từ M1–M6).  
2. **Competitive:** Dùng HAWKED (roadmap Q1–Q4, accessible extraction), Engines of Fury (top-down + looter), Everstorm (class/ability), Tarkov (QoL, seasonal), Arena Breakout/Delta Force (F2P, cross-platform) làm benchmark liên tục.  
3. **GDD:** Ưu tiên hoàn thiện Combat, Character, Map, Economy, Monetization, Technical trước; Art/Audio, Narrative, Social sau (Phase 2 trong doc này).  
4. **Risks:** D4 (cross-platform balance) và B3 (economy inflation) cần owner rõ ràng và review định kỳ.  
5. **_index:** Giữ link tới Competitive Analysis và **Scope Review & Planning** để nhóm tìm nhanh.

---

## 8. Tài Liệu Tham Khảo (Đã dùng)

- HAWKED 2024 roadmap (Q1–Q4 launch, ranked, crafting, story) — MassivelyOP, MMOs.com, PlayHawked.  
- HAWKED design: “How HAWKED Evolves Extraction Shooters…” — Game Developer.  
- Engines of Fury: “Diablo Meets a Top-Down Extraction Shooter” — Immutable Blog.  
- Everstorm: MOBA controls, 6 classes, professions — Gamerant.  
- Escape from Tarkov 2024 roadmap (Unity, QoL, Arena, seasonal) — PCGamesN, Ginx, Fandom.  
- Extraction shooter GDD/scope (map design, core pillars, session length) — Medium (Critical Design Issues), Game Developer.  
- Competitive Analysis nội bộ: Tarkov, Arena Breakout, Delta Force, Hunt, Gray Zone, Marauders.

---

## 9. Changelog & Ownership

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| 1.1 | 2026-02-12 | — | Applied planning to group: genre positioning (_index), MVP↔Q1–Q4 (mvp/index.html), Owner+Review for D4/B3 (risks/index.html), top-down/hero in Design Pillars. |
| 1.0 | 2026-02-12 | — | Initial: review ProjectScope, benchmark roadmaps/GDD, planning phases, recommendations. |

**Owner:** Lead Producer / Suture maintainer.  
**Review:** Quarterly hoặc khi có thay đổi lớn scope/roadmap.
