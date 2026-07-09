---
title: "Game Overview & Design Foundation"
type: docs
---

## Executive Summary

**Extraction Shooter** là tactical extraction shooter mobile-first, top-down, xoay quanh các raid ngắn nhưng áp lực cao. Người chơi chuẩn bị loadout, vào một zone nguy hiểm, loot dưới áp lực, quyết định khi nào fight hoặc flee, và phải extract trước khi trận đấu quay lưng lại với họ.

**Core hook:** mỗi raid đều đặt cược thứ gì đó thật. Extract thành công tạo wealth, momentum, và story. Raid thất bại tốn gear, dạy một bài học, và đưa người chơi về để plan thông minh hơn.

Trang này định nghĩa creative foundation. Rule chi tiết của từng system nằm trong các Game Design page được link.

## Start Here

{{< cards cols="3" >}}
{{< card link="coregameplay.html" title="Core Gameplay" icon="refresh" subtitle="Raid loop, extraction rhythm, death pressure, và match flow." >}}
{{< card link="controls.html" title="Controls" icon="cursor-click" subtitle="Touch input, aiming, movement, camera, và mobile combat ergonomics." >}}
{{< card link="gamemodes.html" title="Game Modes" icon="puzzle" subtitle="Raid variant, ranked play, co-op concept, và mode selection." >}}
{{< card link="economy.html" title="Economy" icon="currency-dollar" subtitle="Loot value, trader, money sink, inflation control, và item flow." >}}
{{< card link="progression.html" title="Progression" icon="chart-bar" subtitle="Account growth, operator, mastery, reputation, và long-term goal." >}}
{{< card link="mapdesign.html" title="Map Design" icon="location-marker" subtitle="Zone layout, extraction placement, hotspot, route, và readability." >}}
{{< /cards >}}

## Design Snapshot

| Area | Direction |
| :--- | :--- |
| Platform | Mobile-first, PC support là secondary opportunity |
| Camera | Top-down tactical view với silhouette readability mạnh |
| Session Length | Raid 10-15 phút, tổng play session 25-40 phút |
| Match Model | PvPvE extraction: loot, fight, survive, extract |
| Core Risk | Gear mang vào có thể mất; account progress và stash vẫn an toàn |
| Monetization | Free-to-play principles, chỉ cosmetics và optional convenience |
| Audience | Hardcore mobile players và PC extraction fans muốn session ngắn hơn |
| Design Bias | Tactical decision hơn twitch precision, readable combat hơn realism |

## Core Design Pillars

{{< cards cols="2" >}}
{{< card title="Risk & Reward" icon="exclamation-circle" subtitle="Loot chỉ thấy có giá trị khi extraction không bao giờ được đảm bảo." >}}
{{< card title="Mobile-First Tactics" icon="device-mobile" subtitle="Mọi core interaction phải hoạt động trong giới hạn touch và session ngắn." >}}
{{< card title="Tactical Readability" icon="eye" subtitle="Người chơi phải đọc được threat, cover, loot, và squad state trong nháy mắt." >}}
{{< card title="Persistent Progression" icon="chart-bar" subtitle="Raid xấu gây đau, nhưng account, stash, reputation, và knowledge vẫn tăng." >}}
{{< card title="Living World" icon="map" subtitle="Aethelgard phải có cảm giác là nơi có lịch sử, faction, và environmental clue." >}}
{{< /cards >}}

### Pillar Notes

| Pillar | Player Feeling | Design Requirement |
| :--- | :--- | :--- |
| Risk & Reward | "Nên rời ngay hay đẩy sâu hơn?" | High-value area phải tạo danger và social pressure nhìn thấy được. |
| Mobile-First Tactics | "Tôi có thể play thông minh trên điện thoại." | Combat phải readable, responsive, thumb-friendly. |
| Tactical Readability | "Tôi thua vì lựa chọn, không phải visual noise." | Silhouette, UI state, và threat signal phải rõ trên màn hình nhỏ. |
| Persistent Progression | "Ngay cả raid tệ vẫn đẩy tôi tiến lên." | Loss phải đau nhưng không xóa long-term progress. |
| Living World | "Zone này từng có quá khứ." | Loot, audio, prop, và faction task nên củng cố world logic. |

## Market Position

> Market snapshot: verify competitor detail trước khi publish bên ngoài. Dùng section này cho positioning, không phải final marketing claim.

| Reference | Current Relevance | Design Takeaway |
| :--- | :--- | :--- |
| Escape from Tarkov | Hardcore PC extraction benchmark | Giữ gear risk có ý nghĩa, nhưng giảm prep friction và session length. |
| ARC Raiders | Modern extraction reference trên PC/console | Theo dõi accessibility, social extraction behavior, anti-cheat expectation. |
| Delta Force: Hazard Operations | F2P shooter có extraction mode | Khác biệt bằng mobile-first top-down readability và raid ngắn hơn. |
| The Cycle: Frontier | Shutdown case study | Economy trust, retention, và identity phải bền từ day one. |
| PUBG Mobile / COD Mobile | Mobile shooter audience cực lớn | Không copy battle royale pacing; cung cấp stakes cao hơn và persistent loot. |

**Positioning statement:** tactical extraction shooter cho mobile players muốn stakes cao hơn battle royale, session ngắn hơn PC extraction games, và progression công bằng không pay-to-win.

## Player Promise

### What We Are

* High-stakes tactical extraction shooter.
* Mobile-first, không phải PC port bị cắt giảm.
* Skill-based, readable, và fair.
* Xây quanh preparation có ý nghĩa, raid decision, và recovery sau loss.

### What We Are Not

* Casual arcade shooter không hậu quả.
* Pay-to-win gear economy.
* Battle royale mode khoác nhãn extraction.
* Simulation-heavy PC experience bị ép lên touch controls.

## Design Guardrails

| Guardrail | Rule |
| :--- | :--- |
| No Pay-to-Win | Không bao giờ bán weapon, armor, stat boost, hoặc power độc quyền. |
| Recoverable Loss | Death có thể tốn gear, nhưng không xóa identity, learning, hoặc account progress. |
| Short Raid Pressure | Match pacing phải support raid 10-15 phút mà không nông. |
| Mobile Readability | UI, camera, combat effect, và loot signal phải rõ trên màn hình nhỏ. |
| Ethical Convenience | Paid convenience chỉ tiết kiệm thời gian khi có path free tương đương. |
| Fair Competition | Ranked và competitive system phải bảo vệ integrity, matchmaking quality, và anti-cheat expectation. |

## Canonical Detail Pages

| Topic | Canonical Page |
| :--- | :--- |
| Raid loop and match rhythm | [Core Gameplay](coregameplay.html) |
| Loadout decisions and pre-raid flow | [Loadout Preparation](loadoutpreparation.html) |
| Gear loss and insurance recovery | [Insurance System](insurancesystem.html) |
| Economy, traders, sinks, and value flow | [Economy](economy.html) |
| Account, operator, and reputation growth | [Progression](progression.html) |
| Map layout, hotspots, and extraction logic | [Map Design](mapdesign.html) |
| Live events, battle pass, and seasonal cadence | [Live Operations](liveops.html) |
| First-time user experience | [Onboarding](tutorialraid.html) |

## Ownership & Maintenance

| Role | Owner | Reviewer |
| :--- | :--- | :--- |
| Design Vision | Lead Game Designer | Creative Director |
| Systems Consistency | Systems Designer | Technical Director |
| Market Snapshot | Product / Publishing | Creative Director |

**Maintenance note:** giữ trang này ngắn. Khi section bắt đầu cần formula, edge case, diagram, hoặc balance table, chuyển detail sang child page canonical và link lại đây.

**Recent changes:**

* **v1.2 (2026-07-06):** Refactor từ mega-spec thành hub overview.
* **v1.1 (2026-02-09):** Thêm marketing và distribution notes.
* **v1.0 (2026-02-07):** Draft toàn diện ban đầu.
