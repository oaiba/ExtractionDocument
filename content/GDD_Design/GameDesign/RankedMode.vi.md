---
title: "Ranked Mode & Competitive Systems"
type: docs
---

## Overview

Ranked Mode thêm competitive stakes vào extraction mà không biến game thành pure deathmatch. Thành công nên reward extraction discipline, objective play, combat skill, và survival.

Ranked nên có cảm giác là phiên bản chặt hơn của cùng một game, không phải esport tách biệt với instinct khác. Player climb vì họ liên tục ra quyết định raid tốt hơn: chọn risk có lợi, sống sót dưới pressure, hoàn thành objective, và rời đi trước khi greed phá run.

System phải tránh reward kill-chasing như đường duy nhất để lên rank. Combat quan trọng, nhất là khi bảo vệ objective hoặc extraction, nhưng final score vẫn phải nhận ra extraction shooter nói về value secured, không chỉ bodies dropped.

## Rank Ladder

Rank ladder cho player seasonal identity. Mỗi tier cần emotional meaning rõ, nhưng UI nên tránh gợi ý lower-ranked players vô giá trị. Bronze/Silver là learning space; Gold/Platinum là consistency; Diamond/Champion là high-pressure mastery.

| Order | Rank | Meaning |
| :--- | :--- | :--- |
| 1 | Bronze | Entry ranked tier |
| 2 | Silver | Basic consistency |
| 3 | Gold | Solid extraction discipline |
| 4 | Platinum | Strong tactical and economy skill |
| 5 | Diamond | High-level competitive play |
| 6 | Champion | Top seasonal prestige |

## RP Inputs

RP inputs phải hiểu được từ post-match screen. Player phải thấy vì sao run gain/lost points và decision nào quan trọng nhất. Hidden formula có thể tồn tại để anti-abuse tuning, nhưng scoring category visible phải stable.

| Input | Direction |
| :--- | :--- |
| Extraction | Primary positive RP source |
| Objective completion | Strong positive modifier |
| Combat performance | Positive, capped to avoid kill farming |
| Loot value extracted | Positive, capped by rank/mode |
| Death | Negative |
| Early disconnect | Strong negative unless protected by reconnect rules |

## Queue Rules

Queue rules là một phần của competitive integrity. Ranked không nên mở trước khi player hiểu extraction basics, có đủ gear context, và hoàn thành tutorial requirement. Matchmaking nên ưu tiên fair/stable game hơn instant queue.

| Rule | Direction |
| :--- | :--- |
| Account requirement | Minimum level and tutorial completion |
| Squad rank spread | Limit rank gap for fairness |
| Map rotation | Seasonal and announced |
| Insurance | Disabled or restricted |
| Matchmaking | Rank, latency, party size, and integrity signals |

## Season Structure

| Phase | Purpose |
| :--- | :--- |
| Placement | Establish starting rank |
| Climb | Core ranked season |
| Mid-season patch | Balance and integrity update |
| Final push | Increased visibility and rewards |
| Reset | Soft reset plus reward distribution |

## Competitive Integrity

Integrity issue gây hại hơn trong ranked vì nó ảnh hưởng trust vào ladder. Anti-cheat, disconnect policy, party restriction, và suspicious pattern review phải communicate đủ rõ để honest players hiểu vì sao rule tồn tại.

| Risk | Mitigation |
| :--- | :--- |
| Cheating | Anti-cheat, telemetry, review pipeline |
| Boosting | Party rank limits, suspicious pattern detection |
| Collusion | Match history and proximity analysis |
| Smurfing | Account age, performance spikes, phone/platform signals |
| Disconnect abuse | Reconnect window and escalating penalties |

## Rewards

Reward nên làm ranked status visible mà không tăng combat power. Reward language an toàn nhất là identity: badge, banner, title, profile treatment, cosmetic, và end-of-season recognition.

| Reward | Rule |
| :--- | :--- |
| Rank badge | Seasonal, profile-visible |
| Cosmetic | No gameplay advantage |
| Banner/title | Prestige only |
| Leaderboard | Top players and squads |
| Clan contribution | Optional clan leaderboard points |

## Ranked Match Examples

Player extract với loot vừa phải, hoàn thành objective, và tránh combat không cần thiết. Đây nên là ranked outcome positive vì player execute extraction goal sạch.

Squad thắng nhiều fight nhưng chết vì timeout khi mang high-value loot. Combat performance có thể làm nhẹ loss, nhưng kết quả vẫn phải dạy rằng ranked extraction yêu cầu rời đi với value.

Player disconnect trong fight đang thua và không reconnect. System nên áp escalating penalty trong khi vẫn bảo vệ reconnect window hợp lý cho network instability thật.

## Tuning Notes

- RP nên reward extraction trước, sau đó objective quality, rồi capped combat contribution.
- Placement matches nên giảm volatility cho new ranked players.
- Party rank limit nên ngăn boosting mà không chặn friend group bình thường quá sớm.
- Leaderboard nên tách solo, duo, trio, và clan contribution nếu có thể.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Core ranked mode rules | [Game Modes](gamemodes/index.html) |
| Profile display | [Player Profile](playerprofile/index.html) |
| Communication restrictions | [Communication](communication/index.html) |
| Economy guardrails | [Economy](economy/index.html) |
