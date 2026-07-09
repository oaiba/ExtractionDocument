---
title: "Core Gameplay Mechanics - Deep Dive"
type: docs
---

## Overview

Core Gameplay sở hữu toàn bộ raid loop: preparation, deployment, looting, combat, extraction, loss, recovery, và post-match rewards. Trang này định nghĩa rule ở cấp experience và link sang các page chuyên sâu cho controls, loadout UI, economy, insurance, và maps.

Core fantasy không phải là "win every fight." Nó là "đưa ra quyết định tốt hơn điều mà raid đang ép bạn làm." Một run tốt nên tạo nhiều khoảnh khắc người chơi dừng lại và cân thông tin: tiếng súng, giá trị trong backpack, thời gian còn lại, health của squad, và route tới extraction. System nên thưởng cho discipline ngang với aggression.

Mỗi raid nên kể một câu chuyện nhỏ. Người chơi cẩn trọng có thể sống sót bằng cách đọc map và rời sớm. Squad aggressive có thể tạo value qua combat, nhưng phải chấp nhận mỗi fight thêm sẽ làm đường về hẹp hơn. New player nên hiểu vì sao họ chết; expert player nên thấy ba quyết định tốt hơn họ đã có thể làm.

## Key Decisions

| Decision | Direction |
| :--- | :--- |
| Match type | PvPvE extraction raid |
| Target raid length | 10-15 minutes |
| Target session length | 25-40 minutes, thường 2-3 raids |
| Primary skill | Tactical decision making, map knowledge, risk reading |
| Primary tension | Gear mang vào và loot tìm được có thể mất trước extraction |
| Safety net | Account progress, stash items, quest progress, và secured items persist |

## Raid Loop

Raid loop đủ ngắn cho mobile session nhưng đủ dày để có mastery. Preparation tạo commitment, match tạo tension, post-match chuyển kết quả thành learning và progression. Loop không được có cảm giác arcade disposable vì người chơi luôn mang thứ gì đó vào raid và luôn mang consequence ra ngoài.

| Step | Action | Result |
| :--- | :--- | :--- |
| 1 | Prepare loadout | Player commit gear, operator, objective, map, và risk level |
| 2 | Deploy to zone | Squad vào raid với extraction options đã assign |
| 3 | Scout and choose route | Player đọc map, audio, squad ping, và loot gần đó |
| 4 | Loot, fight, or avoid | Player chọn value, safety, hoặc pressure |
| 5 | Decide whether to extract | Lựa chọn an toàn bank current value; lựa chọn risky tìm thêm value |
| 6 | Resolve extraction | Extract thành công bank loot và XP; thất bại mất raid inventory |
| 7 | Rebuild or upgrade | Player repair, sell, upgrade, re-equip, và queue lại |

## Pre-Match Phase

Pre-match phase là một ritual có chủ ý. Người chơi phải hiểu risk họ đang chọn trước khi bấm Deploy.

Phase này nên có cảm giác như nạp đạn trước khi mở một cánh cửa nguy hiểm. UI phải surface nhanh các câu hỏi thực dụng: objective là gì, thứ gì đang risk, thứ gì được protect, và escape plan là gì. Tránh spreadsheet fatigue bằng cách summarize risk rõ và đẩy inventory work sâu vào loadout screen.

| Step | Player Question | Canonical Detail |
| :--- | :--- | :--- |
| Select objective | Raid này tôi đang cố làm gì? | [Game Modes](gamemodes.html) |
| Select operator | Ability và role nào khớp goal? | Character docs |
| Build loadout | Tôi sẵn sàng risk bao nhiêu? | [Loadout Preparation](loadoutpreparation.html) |
| Choose insurance | Item nào đáng recovery protection? | [Insurance System](insurancesystem.html) |
| Choose map and squad | Đi đâu, với ai? | [Map Design](mapdesign.html), [Communication](communication.html) |
| Confirm deploy | Expected reward có đáng risk không? | This page |

## In-Match Phase

In-match phase được xây quanh pressure tăng dần, không phải vòng bo battle royale thu hẹp. Người chơi nên cảm thấy ở lại map ngày càng "đắt": loot tốt hơn, safe path ít hơn, thông tin ồn hơn, exit bị tranh chấp hơn. Timer là design tool cho commitment, không phải punishment cho exploration.

| Time Window | Phase | Design Intent | Pressure |
| :--- | :--- | :--- | :--- |
| 0-3 min | Spawn and orientation | Cho squad đọc map, objective, extraction options | Low |
| 3-7 min | Edge loot and route choice | Cung cấp safe value và decision sớm | Rising |
| 7-11 min | Hotspot pressure | Tạo player collision quanh value | High |
| 11-14 min | Extraction contest | Ép commitment và route discipline | Very high |
| 15 min | Match end | Ngăn endless looting và camping | Extreme |

## Combat And Looting Rules

Combat và looting là hai system đi cùng nhau. Loot tạo lý do di chuyển, sound tạo bằng chứng rằng ai đó đã di chuyển, và combat quyết định player có giữ được thứ tìm thấy hay không. Fight tốt nhất nên bắt đầu trước viên đạn đầu tiên, qua route choice, sound discipline, cover selection, và timing.

| System | Rule | Why It Matters |
| :--- | :--- | :--- |
| Combat | Positioning và cover quan trọng hơn raw aim speed | Support top-down mobile tactics |
| TTK | Đủ nhanh để phạt mistake, đủ chậm để counterplay | Tránh sponge arcade lẫn instant frustration |
| Loot value | Value tăng theo danger và travel cost | Làm route planning có ý nghĩa |
| Sound | Gunfire, footstep, alarm, extraction cue tạo risk information | Biến audio thành tactical data |
| AI | AI bảo vệ value, reveal player position, tạo pressure | Tránh loot run trống rỗng |
| Extraction | Extraction phải readable, interruptible, risky | Làm final choice đáng nhớ |

## Greed Loop

Greed loop là trung tâm cảm xúc của extraction play. Game phải liên tục hỏi "đủ chưa?" mà không ép một đáp án đúng. Nếu player extract sớm, kết quả nên thấy smart chứ không boring. Nếu họ push sâu hơn, reward phải đủ visible để risk có cảm giác tự chọn.

| Current State | Player Temptation | Safe Choice | Risk Choice | Outcome |
| :--- | :--- | :--- | :--- | :--- |
| Player có loot giá trị | Extract ngay hay push sâu hơn | Leave và bank value | Đi tiếp tìm loot | Safe value vs increased pressure |
| Extraction ở gần | "One more container" | Commit extraction | Delay extraction | Relief vs possible regret |
| Rare opportunity xuất hiện | Fight, loot, hoặc avoid | Avoid và giữ kit | Contest value | Memorable win hoặc meaningful loss |
| Player chết | Blame hay learn | Review death recap | Rebuild without learning | Better next decision hoặc repeated mistake |

## Death, Extraction, And Recovery

Loss được phép đau, nhưng không được opaque. Raid thất bại phải giải thích rõ mất gì, giữ gì, có thể recover gì qua insurance, và player nên làm gì tiếp. Mục tiêu là regret có dạy học, không phải frustration khiến kết thúc session.

| Outcome | Lost | Preserved | Follow-Up |
| :--- | :--- | :--- | :--- |
| Successful extraction | Consumables dùng trong raid | Found loot, XP, quest progress, insured item status | Sell, stash, upgrade, queue next raid |
| Death in raid | Brought gear, backpack loot, unprotected items | Account XP, stash at home, secure container contents, quest knowledge | Death recap, insurance wait, rebuild |
| Timeout | Treated as failed extraction | Account progress và protected systems | Clear warning và recap |

## Post-Match Flow

| Step | Extracted Run | Failed Run |
| :--- | :--- | :--- |
| 1 | Show loot summary | Show death recap |
| 2 | Apply XP và quest updates | Apply XP, quest, và lesson feedback |
| 3 | Move extracted loot to stash | Mark lost, protected, và insured items |
| 4 | Suggest sell, upgrade, hoặc redeploy | Suggest rebuild, claim insurance later, hoặc recovery mode |

## Advanced Mechanics

Advanced mechanics nên thêm decision expressive mà không đổi promise cơ bản của raid. Squad tools, insurance, ranked rules, và information systems đều là support layer quanh cùng một câu hỏi: player đọc, mang, và thoát với bao nhiêu risk?

| Mechanic | Purpose | Detail Owner |
| :--- | :--- | :--- |
| Squad coordination | Cho team shared information mà không xóa tension | [Communication](communication.html) |
| Information warfare | Làm sensor, ping, và sound có ý nghĩa | [Navigation & Map](navigationandmap.html) |
| Insurance | Giảm loss frustration mà không xóa risk | [Insurance System](insurancesystem.html) |
| Ranked rule changes | Bảo vệ competitive integrity | [Ranked Mode](rankedmode.html) |
| Scavenger runs | Low-stakes recovery và practice | [Game Modes](gamemodes.html) |

## Player Experience Examples

Một solo player vào với budget rifle và một objective item. Họ tránh hotspot đầu tiên, loot edge containers, nghe gunfire gần mid-map, và quyết định extract sớm với value vừa phải. Đây là low-risk story thành công: player có discipline và học route.

Một trio vào với armor mạnh và rare key. Họ tranh hot zone, thắng fight, nhưng mất healing và time. Quyết định tiếp theo không phải "tiếp tục fight vì đang thắng"; mà là key room reward có đáng để băng qua map với gear hỏng và footprint ồn không.

Một new player chết sau khi mở container gần sightline rõ. Recap nên nối death với cause đọc được: enemy angle, sound cue, exposed looting position, hoặc missing extraction timing. Next action nên practical, như thử safe route hơn hoặc equip smoke.

## Edge Cases And Anti-Frustration

- Nếu player disconnect trong raid, reconnect phải ưu tiên trước loss resolution.
- Nếu player chết vì timeout, recap phải show timer warning và last known extraction distance.
- Nếu squadmate extract một mình, squad member còn lại tiếp tục theo risk rule bình thường.
- Nếu player chết khi đang interact với extraction, UI phải show rõ extraction đã complete hay chưa.
- Nếu quest objective complete nhưng player chết, quest rule phải nói rõ progress có cần extraction không.
- Nếu matchmaking đưa new player vào lobby quá harsh, onboarding protection nên giảm extreme early failure.

## Core Tuning Knobs

- Raid timer kiểm soát urgency; chỉ shorten nếu route và extract vẫn readable.
- Loot value kiểm soát greed; chỉ tăng hotspot value khi danger và exit pressure tăng tương ứng.
- AI density kiểm soát pacing; dùng AI để guard value và tạo sound, không thay thế PvP tension.
- Extraction timer kiểm soát final commitment; tune cùng cover, sightline, và audio tell.
- Secure container size kiểm soát loss pain; protection lớn hơn giảm gear fear và economy risk.
- Death recap detail kiểm soát learning; clarity cao hơn có thể giảm frustration mà không giảm stakes.

## Metrics

Metric là design health signal, không phải truth cố định. Nếu extraction rate tăng nhưng player nói chán, map có thể quá safe. Nếu death rate tăng và player không giải thích được vì sao, readability đang fail. Balance work phải kết hợp telemetry với death recap feedback và session survey.

| Metric | Target | Notes |
| :--- | :--- | :--- |
| Overall extraction rate | 30-40% | Tune theo skill bracket và mode |
| Beginner extraction rate | 20-30% | Tutorial và protected queue hỗ trợ learning |
| Average raid length | 10-15 minutes | Tránh PC-scale session bloat |
| Menu time per session | Under 20% | Loadout prep phải meaningful, không slow |
| Death recap usefulness | High qualitative score | Player phải biết nên cải thiện gì |

## Cross-References

| Topic | Page |
| :--- | :--- |
| Loadout UI | [Loadout Preparation](loadoutpreparation.html) |
| Input and camera | [Controls](controls.html) |
| Map routes and extraction placement | [Map Design](mapdesign.html) |
| Insurance rules | [Insurance System](insurancesystem.html) |
| Economy impact | [Economy](economy.html) |
| Onboarding | [Tutorial Raid](tutorialraid.html) |
