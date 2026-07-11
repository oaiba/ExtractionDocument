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

## Tutorial Onboarding Model

Operation Zero nên dạy raid loop theo đúng thứ tự player sẽ dùng trong normal play. Tutorial có thể bảo vệ player khỏi permanent loss, nhưng không được giấu sự tồn tại của risk.

| Teaching Goal | Player Action | UI Support | Fail-Safe | Pass Condition | Next Unlock |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Movement and camera | Di chuyển qua crash site, xoay/aim camera, dùng cover path | Objective marker, soft boundary, camera hint | Reset về checkpoint nếu stuck | Reach first marker | Loot container |
| Looting and value | Search container, compare item, đặt vào backpack | Loot panel, value badge, capacity hint | Pause threat khi first loot panel mở | Take required item hoặc skip có confirm | Inventory lesson |
| Inventory basics | Move, rotate, equip, consume, và protect một item | Highlight valid slots, show blocked placement reason | Auto-place tutorial item sau repeated failure | Inventory có required item ở valid location | Combat encounter |
| Combat and cover | Fight simple AI bằng cover, reload, ability | Enemy intent cue, hit feedback, health/armor HUD | Enemy accuracy giảm sau repeated deaths | Enemy defeated hoặc bypass qua taught route | Healing lesson |
| Healing and status | Dùng medkit sau scripted damage | Status icon, quick-slot hint, safe cover | Damage dừng đến khi healed | Health stabilized | Map/objective lesson |
| Map and objective | Mở map, đọc extraction/objective marker, set waypoint | Pulsing objective, extract marker, route hint | Re-ping objective sau delay | Player follow route | Timed extraction |
| Extraction timer | Activate extraction, hold zone, defend hoặc wait | Countdown, zone boundary, audio cue | Retry từ checkpoint gần đó nếu interrupted | Extraction completes | Debrief |
| Debrief and stash | Đọc outcome, move reward vào stash, thấy next deploy CTA | Guided debrief, stash highlight, deploy path | No permanent loss, no blocking overflow | Player tới Safe House onboarding | Standard queue |

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

## Tutorial Failure And Recovery Rules

Tutorial failure chỉ được phép khi nó dạy lần thử tiếp theo. Nó không được tạo account loss, lock player trong đoạn lặp dài, hoặc che mờ lý do fail.

| Failure | Recovery | Copy Requirement |
| :--- | :--- | :--- |
| Player dies in combat | Restart tại combat checkpoint với ammo/health restored | Explain cover, healing, hoặc reload lesson |
| Player runs out of ammo | Spawn tutorial ammo và highlight reload | "Pick up ammo and reload before pushing." |
| Player cannot solve inventory placement | Offer auto-place sau hai lần fail | "Auto-place item" phải optional |
| Player misses extraction timer | Restart gần extraction với route hint | "Stay inside the zone until timer completes." |
| Player disconnects | Resume tutorial checkpoint, không MIA | "Tutorial progress restored." |
| Player skips tutorial | Chỉ allowed cho returning accounts hoặc explicit skip path | Show system nào có thể vẫn unfamiliar |

## First Real Raid Handoff

Sau Operation Zero, first standard raid nên quen thuộc nhưng không còn protected. Handoff phải show những gì thay đổi:

| System | Tutorial | First Standard Raid |
| :--- | :--- | :--- |
| Gear loss | No permanent loss | Loadout can be lost |
| Enemy pressure | Scripted AI only | PvPvE với real players |
| Extraction | Guided route và retry | Multiple extracts, no checkpoint retry |
| Loot | Curated items | Full loot table và FIR rules |
| Death | Checkpoint recovery | KIA/MIA debrief và rebuild |
| Matchmaking | Training pool | Soft protected standard pool cho early raids |

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

## Tutorial QA Checklist

- Player có thể move, aim, loot, heal, open map, activate extraction, và read debrief mà không cần external instruction.
- Player thấy ít nhất một valuable item trước extraction để genre promise rõ.
- Player hiểu tutorial loss protection không áp dụng cho normal raids.
- Tutorial có thể resume sau disconnect mà không MIA hoặc gear loss.
- Skip/replay rules visible và không block returning players.
- First standard raid deploy screen nhắc lại gear loss, insurance, và extraction stakes.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Core loop | [Core Gameplay](coregameplay/index.html) |
| Controls | [Controls](controls/index.html) |
| Loadout onboarding | [Loadout Preparation](loadoutpreparation/index.html) |
| Safe House | [Safe House Design](safe_house_design/index.html) |
| Accessibility | [Accessibility](accessibility/index.html) |
