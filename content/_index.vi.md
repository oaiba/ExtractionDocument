---
title: "Extraction Document"
type: docs
sidebar:
  hide: true
---

<img class="extraction-ascii-banner" src="/ExtractionDocument/assets/extraction-banner.svg" alt="EXTRACTION">

Đây là cổng tài liệu trung tâm cho toàn bộ dự án **Extraction Shooter**. Trang này đóng vai trò là nguồn tham chiếu chính cho tầm nhìn sáng tạo, thiết kế gameplay, và định hướng triển khai kỹ thuật của trải nghiệm tactical top-down có nhịp độ căng thẳng.

> Bản tiếng Việt là bản dịch song song để đọc nhanh. Khi có khác biệt, bản tiếng Anh vẫn là nguồn canonical.

## Tổng Quan Dự Án

{{< cards cols="3" >}}
{{< card title="Engine" icon="server" subtitle="Unreal Engine 5 (C++)" >}}
{{< card title="Nền tảng" icon="device-mobile" subtitle="Mobile (iOS/Android) + PC" >}}
{{< card title="Thể loại" icon="fire" subtitle="Top-down Extraction Shooter" >}}
{{< /cards >}}

**Giai đoạn hiện tại:** Tiền sản xuất / Prototype core gameplay

## Bắt Đầu Từ Đây

Dùng các lối vào nhanh này khi cần chuyển giữa kế hoạch, ý đồ thiết kế, và chi tiết triển khai.

{{< cards cols="3" >}}
{{< card link="/tracker/index.html" title="Project Tracker" icon="clipboard-list" subtitle="Milestone, kế hoạch phase, ghi chú sprint, và điều phối dự án." >}}
{{< card link="/tracker/tasks/index.html" title="Tasks & Milestones" icon="flag" subtitle="Roadmap theo từng phase từ core prototype đến launch." >}}
{{< card link="/gdd_design/projectscope/mvp/index.html" title="MVP Scope" icon="sparkles" subtitle="Ranh giới launch, feature bắt buộc, non-goal, và rủi ro chính." >}}
{{< /cards >}}

## Cổng Tài Liệu

Truy cập các hub tài liệu chuyên biệt theo vai trò và công việc hiện tại.

{{< cards cols="2" >}}
{{< card link="/gdd_design/index.html" title="Design & Creative Hub" icon="sparkles" subtitle="Trải nghiệm người chơi, world-building, visual/audio, và narrative." >}}
{{< card link="/gdd_technical/index.html" title="Technical & Engineering Hub" icon="terminal" subtitle="Spec triển khai, kiến trúc hệ thống, networking, và performance." >}}
{{< /cards >}}

{{< cards cols="2" >}}
{{< card link="/tracker/index.html" title="Project Tracker" icon="clipboard-list" subtitle="Milestone, task, delivery phase, và production planning." >}}
{{< card link="/gdd_agents/index.html" title="AI Agent Guidelines" icon="chip" subtitle="Rule, workflow, và skill dành cho AI coding agents." >}}
{{< /cards >}}

## Phạm Vi & Tiến Độ

{{< cards cols="3" >}}
{{< card link="/gdd_design/projectscope/mvp/index.html" title="MVP Definition" icon="flag" subtitle="Feature tối thiểu và ranh giới scope của sản phẩm." >}}
{{< card link="/gdd_design/projectscope/nongoals/index.html" title="Non-Goals" icon="x-circle" subtitle="Những feature chủ động loại khỏi scope hiện tại." >}}
{{< card link="/gdd_design/projectscope/risks/index.html" title="Risk Assessment" icon="exclamation-circle" subtitle="Rủi ro đã biết và hướng giảm thiểu." >}}
{{< /cards >}}

### Milestone Gần Đây

{{< cards cols="3" >}}
{{< card title="Audio Architecture" icon="volume-up" subtitle="Đã hoàn thiện định nghĩa soundscape và tactical audio." >}}
{{< card title="Visual Direction" icon="photograph" subtitle="Đã chốt art bible và budget hiệu năng cho mobile." >}}
{{< card title="Map System" icon="map" subtitle="Đã mở rộng hotspot khu công nghiệp và loot heatmap." >}}
{{< /cards >}}

## Quick Start Theo Vai Trò

### Cho Design & Art Teams

* **Nguồn tham chiếu chính**: Bắt đầu từ [Design Hub](/GDD_Design) trước khi làm creative work.
* **Visual Consistency**: Theo [Style Guide](/gdd_design/visuals/styleguide/index.html) để giữ chất lượng cross-platform.
* **Core Loop**: Giữ [Core Gameplay](/gdd_design/gamedesign/coregameplay/index.html) đồng bộ với mọi thay đổi cơ chế.
* **Asset Submission**: Dùng [Asset Guidelines](/gdd_design/visuals/assetguidelines/index.html) cho spec asset sẵn sàng đưa vào UE5.

### Cho Technical & Dev Teams

* **Implementation Specs**: System architecture và engineering notes nằm trong [Technical Hub](/GDD_Technical).
* **Performance First**: Bám theo [Performance Budgets](/gdd_technical/performance/budgets/index.html).
* **Task Management**: Theo [Development Roadmap](/gdd_technical/core/developmentroadmap/index.html) và [Tasks & Milestones](/tracker/tasks/index.html).
* **Code Standards**: Giữ modularity theo [Architecture](/gdd_technical/core/architecture/index.html).

## Điều Hướng Nhanh

### Mới Tham Gia Dự Án?

1. **Đọc** [**MVP Scope**](/gdd_design/projectscope/mvp/index.html) để hiểu trọng tâm hiện tại.
2. **Xem** [**Core Gameplay**](/gdd_design/gamedesign/coregameplay/index.html) để nắm nhịp gameplay chính.
3. **Review** [**Tasks & Milestones**](/tracker/tasks/index.html) để hiểu kế hoạch delivery hiện tại.

### Tài Liệu Hệ Thống Chính

* **Task Tracker** -> [Tasks & Milestones](/tracker/tasks/index.html)
* **World & Maps** -> [Map Design](/gdd_design/world/mapdesign/index.html)
* **Combat & Weapons** -> [Weapon System](/gdd_technical/gameplay/weaponsystem/index.html)
* **Inventory & Loot** -> [Inventory System](/gdd_technical/gameplay/inventorysystem/index.html)
* **Networking** -> [Networking System](/gdd_technical/core/networkingsystem/index.html)
* **AI Behavior** -> [AI System](/gdd_technical/systems/aisystem/index.html)

_Cập nhật lần cuối: February 13, 2026_
