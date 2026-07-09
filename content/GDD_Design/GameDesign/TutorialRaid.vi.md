---
title: "Tutorial Raid: Operation Zero"
type: docs
---

## Overview

Operation Zero là guided raid đầu tiên. Nó dạy nền tảng extraction qua một mission có kiểm soát thay vì menu tutorial.

Tutorial nên có cảm giác là mission đầu tiên của player, không phải training room tách rời. Nó giới thiệu risk, loot, combat, map reading, và extraction trong sequence được bảo vệ để player hiểu vì sao game căng thẳng trước khi đối mặt real loss.

Design goal là confidence, không phải mastery. New player nên rời Operation Zero với hiểu biết về cách move, loot, sống sót qua fight đơn giản, tìm extraction, và hiểu post-match screen. Advanced economy, ranked, market, và deep squad rules có thể để sau.

## Tutorial Goals

Mỗi goal nên được dạy qua action. Player học looting bằng cách chọn nhặt gì, không phải đọc một paragraph. Player học extraction bằng cách mang thứ có value khi timer visible, không phải xem cinematic.

| Goal | Player Learns |
| :--- | :--- |
| Move and camera | How to navigate top-down spaces |
| Loot | Why items matter and how inventory works |
| Combat | Cover, aim, abilities, and damage feedback |
| Map and pings | How to read objectives and extraction markers |
| Extraction | Why leaving alive matters |
| Debrief | How rewards, loss, stash, and next steps work |

## Mission Flow

Mission flow nên escalate pressure dần. Early steps safe và explicit. Mid steps giới thiệu enemy và inventory choice. Final extraction step thêm time pressure nhưng vẫn cho checkpoint recovery nếu player fail.

| Step | Phase | Teaches | Failure Policy | Unlocks |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Operator Selection | Class identity and ability preview | Cannot fail | Crash Site |
| 2 | Crash Site | Movement, camera, objective marker | Soft reset | Scavenger Camp |
| 3 | Scavenger Camp | Combat, cover, ability use | Retry checkpoint | Bunker |
| 4 | Bunker | Looting, inventory, item value | Guided prompts | Map and Pings |
| 5 | Map and Pings | Minimap, waypoint, squad signal | Repeat prompt | Timed Extraction |
| 6 | Timed Extraction | Timer, danger, reward | Retry checkpoint | Custom Debrief |
| 7 | Custom Debrief | Rewards, stash, and next step | Cannot fail | Safe House Onboarding |

## Starter Kit

Starter kit nên support raid thật đầu tiên mà không xóa early scarcity. Nó cho player đủ tool để thử lại, nhưng không đủ value để bỏ qua việc học economy, insurance, hoặc loadout preparation.

| Item | Purpose |
| :--- | :--- |
| Basic weapon | Enables first real raid |
| Light armor | Reduces early frustration |
| Medkit | Teaches recovery |
| Small backpack | Teaches loot capacity |
| Credits | Lets player buy a small upgrade |

## Anti-Frustration Rules

Anti-frustration rule mạnh nhất trong tutorial vì player chưa tự chọn risk. Khi player vào raid thường, loss có thể meaningful. Trong Operation Zero, failure nên dạy và reset nhanh.

| Rule | Reason |
| :--- | :--- |
| No permanent loss during tutorial | Avoid first-session punishment |
| Checkpoints after each lesson | Reduces repetition |
| Clear objective marker | Prevents navigation failure |
| Optional reminders | Helps new mobile players |
| Skip option for returning players | Respects experienced players |

## Tutorial Examples

Loot interaction đầu tiên nên cho player reward nhỏ nhưng thấy rõ, rồi show item đó xuất hiện trong inventory như thế nào. Bài học là value recognition, không phải inventory mastery.

Combat encounter đầu tiên nên dùng cover và enemy behavior readable. Player nên học rằng positioning quan trọng trước khi gặp real PvP pressure.

Extraction finale nên làm player mang thứ đáng giữ. Timer, marker, và audio cue phải dạy rằng rời đi khi còn sống là điểm chính của genre.

## Tutorial Failure Cases

- Nếu player có thể finish mà không hiểu extraction, mission dạy sai genre.
- Nếu prompt tự giải mọi step, player rời tutorial mà không có confidence.
- Nếu failure lặp lại section dài, frustration thay thế learning.
- Nếu experienced player không thể skip hoặc accelerate, replay friction tăng.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Core loop | [Core Gameplay](coregameplay.html) |
| Controls | [Controls](controls.html) |
| Loadout onboarding | [Loadout Preparation](loadoutpreparation.html) |
| Safe House | [Safe House Design](safe_house_design.html) |
| Accessibility | [Accessibility](accessibility.html) |
