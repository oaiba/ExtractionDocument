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

## Raid System Model

Core Gameplay sở hữu contract kết quả của raid. Các trang chuyên sâu có thể tune combat, economy, inventory, map, UI, và matchmaking, nhưng không được định nghĩa lại raid là gì, player đang risk gì, hoặc outcome được resolve như thế nào.

| Entity | Định nghĩa | Design Owner |
| :--- | :--- | :--- |
| `RaidSession` | Một match instance server-authoritative từ matchmaking lock đến result reconciliation | Core Gameplay |
| `RaidPhase` | Phase hiện tại của loop: preparation, matchmaking, loading, spawn, route, execution, extraction, recovery | Core Gameplay |
| `Spawn` | Trạng thái entry ban đầu: map edge, squad position, threat gần đó, extraction options | Maps / Matchmaking |
| `Objective` | Goal do player chọn hoặc system assign để tạo hướng đi ngoài looting | Quest / Game Modes |
| `LootState` | Current value, FIR status, protected items, inventory pressure, và stash transfer result | Inventory / Economy |
| `ThreatState` | Danger có thể đọc được từ AI, players, sound, objectives, hotspots, và extraction pressure | Gameplay |
| `ExtractionPoint` | Escape route với availability, activation rule, timer, contest rule, và outcome code | Extraction |
| `RaidTimer` | Match clock điều khiển urgency, late-raid behavior, và timeout failure | Core Gameplay |
| `DeathState` | KIA, downed, revived, executed, disconnected, hoặc MIA outcome trước reconciliation | Combat / Extraction |
| `FailState` | Mọi non-extracted result, gồm death, timeout, disconnect expiry, hoặc invalid session | Core Gameplay |
| `RewardState` | XP, quest progress, loot transfer, insurance scheduling, và post-raid grants | Progression / Inventory |
| `SquadState` | Party membership, alive/downed/extracted state, partial extraction, và reconnect state | Matchmaking / Social |

## Full Raid Loop Contract

Full raid loop dài hơn in-match timer. Một run bắt đầu khi player commit risk và kết thúc khi họ hiểu outcome cũng như có next action thực tế.

| Step | Phase | Player Commitment | System Contract | Exit Condition |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Loadout commit | Gear, operator, objective, insurance, squad, và mode | Validate readiness và summarize risk | Deploy confirmed |
| 2 | Matchmaking | Time và squad readiness | Tìm pool hợp lệ mà không che giấu mode rules | Server reserved |
| 3 | Loading | Attention và anticipation | Hiển thị map, region, squad, risk tip, reconnect-safe transition | Spawn ready |
| 4 | Spawn / orientation | First route choice | Cung cấp map, extracts, objective, local threat, và squad status | Player rời spawn pocket |
| 5 | Route choice | Safety vs value | Làm route readable qua map, audio, loot density, và objective signals | Player commit direction |
| 6 | Loot / objective / combat | Exposure để lấy value | Ghép reward với danger, travel cost, hoặc noise | Player gain value hoặc mất tempo |
| 7 | Extraction decision | Bank value hoặc push sâu hơn | Giữ extract options readable và time pressure honest | Extract selected hoặc timer ép hành động |
| 8 | Extraction hold / contest | Final vulnerability | Resolve activation, interruption, squad state, và contest rules rõ ràng | Extracted, interrupted, hoặc killed |
| 9 | Outcome reconciliation | Trust in result | Resolve loot, XP, quest, FIR, insurance, death, và reconnect rules server-side | Debrief data ready |
| 10 | Debrief / recovery | Learning và next action | Giải thích chuyện gì xảy ra, state nào đổi, và làm gì tiếp | Stash, redeploy, hoặc recovery mode |

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

## Player Intent Per Phase

Mỗi phase cần một câu hỏi player rõ ràng. Nếu UI hoặc system không trả lời câu hỏi đó, player phải đoán, và đoán sai làm loss có cảm giác arbitrary.

| Phase | Player Intent | Required Information | Primary Decision | Common Failure |
| :--- | :--- | :--- | :--- | :--- |
| Preparation | Build một plan đáng để risk | Loadout validity, mode rules, insurance, objective, squad readiness | Mang bao nhiêu value vào raid | Deploy khi thiếu ammo, durability thấp, hoặc objective không rõ |
| Matchmaking | Tin rằng queue đủ công bằng | Queue type, region, cancel state, squad ready state | Chờ, cancel, hoặc chỉnh party | Hidden rule mismatch hoặc long queue không rõ lý do |
| Loading | Hiểu mình đang đi đâu và vì sao | Map, weather, squad, tip, server region | Chuẩn bị route trong đầu | Loading không có tactical context |
| Spawn | Định hướng mà không bị phạt tức thì | Spawn location, extracts, objective marker, nearby cover | Move, scout, hoặc regroup | Spawn confusion hoặc death sớm không readable |
| Route | Chọn safety, value, hoặc objective speed | Loot density, sound, timer, squad health, route risk | Avoid, flank, push, hoặc loot | Đi theo route mà không đọc risk |
| Execution | Chuyển opportunity thành value | Enemy cues, container value, objective status, ammo/health | Fight, loot, disengage, hoặc reposition | Greed sau khi mất tempo |
| Extraction | Bank value trước khi risk vượt reward | Extract distance, timer, noise, contest risk, squad state | Leave now hoặc tiếp tục | Đợi quá lâu hoặc hiểu sai extract rules |
| Recovery | Learn và quay lại loop | Lost/kept items, XP, quest, insurance, death cause | Rebuild, sell, claim, hoặc redeploy | Debrief không giải thích consequence |

## Risk / Reward Rules

Risk nên có cảm giác do player tự chọn. Game có thể tạo pressure, nhưng hiếm khi được gây consequence mà player không thể đọc trước.

| Risk Driver | Tăng Khi | Player-Facing Tell | Reward Pairing |
| :--- | :--- | :--- | :--- |
| Time in raid | Raid timer chạy và safe routes đóng dần | Timer color, ambient pressure, late-raid VO, extract distance | Loot contested tốt hơn và late objective windows |
| Loot value | Backpack value tăng hoặc player mang rare item | Value summary, rarity/FIR badges, weight changes | Sell, quest, craft, hoặc progression value cao hơn |
| Noise | Gunfire, sprinting, alarm, extraction call, heavy gear | Audio falloff, ping, map notification khi phù hợp | Loot nhanh hơn, combat opportunity, hoặc extraction progress |
| Weight | Inventory và armor vượt threshold | Movement penalty, stamina drain, weight warning | Mang được nhiều value về hơn |
| Distance to extract | Route đi qua hotspot hoặc sightline mở | Extract marker, route danger, known sound zones | Thêm thời gian lấy value trước khi rời |
| Squad health | Teammate downed, split, ít meds, hoặc disconnected | Squad status, revive timer, reconnect state | Team survival, revive XP, shared extraction |
| Objective commitment | Player mang quest item hoặc vào objective zone | Objective badge, extraction requirement, loss warning | Quest progress, reputation, unlocks |

Reward không được miễn phí khỏi exposure. Nếu reward không có travel cost, sound cost, time cost, resource cost, hoặc combat risk, reward đó phải low value, tutorial-only, hoặc bị cap rõ ràng.

## Pre-Match Phase

Pre-match phase là một ritual có chủ ý. Người chơi phải hiểu risk họ đang chọn trước khi bấm Deploy.

Phase này nên có cảm giác như nạp đạn trước khi mở một cánh cửa nguy hiểm. UI phải surface nhanh các câu hỏi thực dụng: objective là gì, thứ gì đang risk, thứ gì được protect, và escape plan là gì. Tránh spreadsheet fatigue bằng cách summarize risk rõ và đẩy inventory work sâu vào loadout screen.

| Step | Player Question | Canonical Detail |
| :--- | :--- | :--- |
| Select objective | Raid này tôi đang cố làm gì? | [Game Modes](gamemodes/index.html) |
| Select operator | Ability và role nào khớp goal? | Character docs |
| Build loadout | Tôi sẵn sàng risk bao nhiêu? | [Loadout Preparation](loadoutpreparation/index.html) |
| Choose insurance | Item nào đáng recovery protection? | [Insurance System](insurancesystem/index.html) |
| Choose map and squad | Đi đâu, với ai? | [Map Design](mapdesign/index.html), [Communication](communication/index.html) |
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

## Raid Outcome Matrix

Outcome reconciliation phải deterministic và server-authoritative. Debrief có thể trình bày đơn giản hơn, nhưng vocabulary state phía backend phải ổn định.

| Outcome | Result Code | Loot Result | Progress Result | Player Message |
| :--- | :--- | :--- | :--- | :--- |
| Successful extraction | `EXTRACTED` | Extracted items chuyển vào stash; consumables vẫn đã dùng | XP, quest, FIR, và reward rules áp dụng bình thường | "Extracted. Loot secured." |
| Killed in raid | `KIA` | Equipped và backpack items mất trừ khi protected hoặc insured về sau | Account XP và allowed quest progress áp dụng | "Killed in action. Review how you died." |
| Timer expired | `MIA_TIMEOUT` | Treat như failed extraction; secure/protected rules vẫn áp dụng | Limited progress chỉ khi rule cho phép | "Missing in action. You did not extract before time expired." |
| Disconnect unresolved | `MIA_DISCONNECT` | Slot được giữ trong reconnect window, sau đó failed extraction nếu không reconnect | Không thêm penalty ngoài MIA rules | "Connection lost. Reconnect window expired." |
| Server rollback | `SERVER_ROLLBACK` | Trả về pre-raid loadout snapshot | Không có raid rewards; compensation có thể grant riêng | "Raid could not be validated. Gear restored." |
| Squad partial extraction | `PARTIAL_EXTRACT` | Member đã extract bank loot; member còn lại tiếp tục risk | Mỗi player resolve độc lập | "Squadmate extracted. Your raid continues." |
| Objective complete, failed extract | `OBJECTIVE_UNSECURED` | Objective item mất trừ khi protected; progress phụ thuộc objective rule | Non-extraction objectives có thể persist nếu mark rõ | "Objective progress requires extraction." |

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
| Squad coordination | Cho team shared information mà không xóa tension | [Communication](communication/index.html) |
| Information warfare | Làm sensor, ping, và sound có ý nghĩa | [Navigation & Map](navigationandmap/index.html) |
| Insurance | Giảm loss frustration mà không xóa risk | [Insurance System](insurancesystem/index.html) |
| Ranked rule changes | Bảo vệ competitive integrity | [Ranked Mode](rankedmode/index.html) |
| Scavenger runs | Low-stakes recovery và practice | [Game Modes](gamemodes/index.html) |

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

## Raid Telemetry

Telemetry nên giải thích loop có readable không, không chỉ đo player thắng hay thua.

| Signal | Question Answered |
| :--- | :--- |
| Phase duration by skill bracket | Player đang kẹt, rush, hoặc disengage ở đâu? |
| Spawn-to-first-contact time | Spawn có fair và readable không? |
| Hotspot collision rate | Valuable zones có tạo conflict đúng ý không? |
| Loot value carried vs extracted | Greed pressure có hiệu quả mà không vô vọng không? |
| Extraction activation / interruption / success rate | Extraction contest có dramatic nhưng không bất khả thi không? |
| Death reason clarity rating | Player có hiểu vì sao họ mất không? |
| Disconnect reconnect success rate | Technical failure có được tách khỏi gameplay loss không? |
| Tutorial completion to first standard raid | Onboarding có chuyển hóa thành real play không? |

## Core Gameplay QA Checklist

- New player có thể giải thích raid goal sau một tutorial và một debrief.
- Mọi deploy path hiển thị mode rules, gear loss, insurance, squad, map, và objective trước queue start.
- Mọi extraction outcome có result code ổn định và player-facing message rõ ràng.
- Death, MIA, disconnect, partial extraction, và server rollback không dùng copy mơ hồ giống nhau.
- Reward giá trị cao cần exposure qua time, sound, travel, resources, hoặc combat risk.
- Quest và loot progress nói rõ extraction có bắt buộc không.
- Reconnect được thử trước khi unresolved disconnect thành MIA.
- Debrief luôn có ít nhất một next action thực tế: redeploy, rebuild, claim, sell, repair, hoặc learn.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Loadout UI | [Loadout Preparation](loadoutpreparation/index.html) |
| Input and camera | [Controls](controls/index.html) |
| Map routes and extraction placement | [Map Design](mapdesign/index.html) |
| Insurance rules | [Insurance System](insurancesystem/index.html) |
| Economy impact | [Economy](economy/index.html) |
| Onboarding | [Tutorial Raid](tutorialraid/index.html) |
