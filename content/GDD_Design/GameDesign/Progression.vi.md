---
title: "Progression & Player Growth"
type: docs
---

## Overview

Progression sở hữu các system khiến player quay lại: account levels, operator mastery, faction reputation, quests, battle pass advancement, achievements, và long-term goals.

Progression phải làm mọi session có cảm giác đẩy player tiến lên, kể cả khi raid thua. Extraction tạo spike reward, nhưng account growth, operator learning, quest, reputation, và seasonal goal giúp player không cảm thấy một death đã xóa cả buổi tối.

System nên tránh mandatory chores. Daily và weekly goal là guidance, không phải homework. Progression path tốt nhất là path cho player lý do thử route, operator, weapon class, hoặc squad role khác mà vẫn tôn trọng extraction fantasy.

## Progression Layers

Progression layer phải readable từ Home Screen và post-match recap. Player phải biết track nào tăng, vì sao tăng, và unlock meaningful tiếp theo là gì. Hidden progress hữu ích cho achievement, nhưng core growth phải explicit.

| Source | Progression Track | Unlocks / Result |
| :--- | :--- | :--- |
| Raid actions | Account level | Systems, rewards, and broad player growth |
| Operator usage | Operator mastery | Identity rewards and role commitment |
| Faction quests | Faction reputation | Trader access and faction-specific tasks |
| Daily / weekly goals | Quest progress | Directed goals and regular return hooks |
| Seasonal challenges | Battle pass | Seasonal cosmetics and event rewards |

## Progression System Model

Progression là long-term memory của nỗ lực player. Mỗi progression object phải giải thích track nào tăng, vì sao tăng, unlock gì, và reward có claim được ngay hay đang bị chặn bởi capacity, season, hoặc premium-state rule.

| Entity | Định nghĩa | Yêu cầu UI / Design |
| :--- | :--- | :--- |
| `AccountLevel` | Mức familiarity rộng và system access | Unlock system và reward; không grant hidden combat stats |
| `XPEvent` | Lý do atomic khiến XP được earned | Phải show source category, amount, cap status, và boost state |
| `OperatorMastery` | Identity progression cho một operator cụ thể | Reward role commitment bằng cosmetics/profile treatment, không tạo mandatory stat grind |
| `FactionReputation` | Trust/access track cho faction/trader | Unlock trader access, quest chains, và faction identity |
| `QuestProgress` | Objective completion cho tutorial, daily, weekly, faction, story, seasonal, repeatable quests | Phải show objective, progress count, reset/expiry, reward, và route |
| `BattlePassXP` | Seasonal XP đưa vào battle pass tiers | Đến từ raids, quests, events, catch-up missions; purchase route thuộc Commerce |
| `SeasonTier` | Tier trong free/premium seasonal reward track | Phải show free/premium lane, reward type, locked/earned/claimed state |
| `RewardClaim` | Claimable grant từ progression, event, inbox, battle pass, hoặc compensation | Phải show source, destination, expiry, blockers, và overflow behavior |

## Progression Layer Spec

| Layer | Owns | Cannot Do | Primary UI Surfaces |
| :--- | :--- | :--- | :--- |
| Account level | System access, broad rewards, onboarding milestones | Add hidden health, damage, armor, aim, audio, hoặc matchmaking advantage | Home, AAR, Profile, Tutorial gates |
| Operator mastery | Role identity, cosmetics, tips, profile treatment | Khiến một operator statistically mandatory thông qua grind | Operator Select, Profile, AAR |
| Faction reputation | Trader access, quest chains, faction status | Bán reputation trực tiếp bằng premium currency | Quest Board, Traders, Profile |
| Quest system | Directed goals, map learning, repeatable motivation | Dựa vào repetitive chores bỏ qua extraction decisions | Quest Board, HUD tracker, AAR |
| Battle pass | Seasonal reward track và return goals | Trở thành core power spine hoặc che free value | Battle Pass, Reward Inbox, Commerce upgrade route |
| Achievements / prestige | Long-term mastery và bragging rights | Reset meaningful player access mà không có consent | Profile, Season Summary |

Progression có thể unlock access, knowledge, cosmetic identity, trader stock, và quest chains, nhưng không được imply premium gear power. Nếu progression reward grant physical gear, nó là earned item instance với durability, insurance, loss, stash, và lifecycle rules bình thường.

## Account Levels

Account level đại diện familiarity rộng với game. Nó có thể unlock system và reward, nhưng không được tạo permanent combat stat gap. Player level 50 có nhiều option và knowledge hơn; họ không nên đơn giản có nhiều health, damage, hoặc hidden power hơn.

| Area | Direction |
| :--- | :--- |
| Level range | Launch target: 1-50 |
| Primary source | Raid XP, quest completion, event objectives |
| Unlock cadence | Meaningful unlock or reward every 5 levels |
| Prestige | Post-launch system, cosmetic-first |
| Loss rules | Account XP is never lost on death |

## Operator Mastery

| Tier | Player Meaning | Reward Type |
| :--- | :--- | :--- |
| 0-2 | Learning the role | Starter cosmetics, tips, basic mastery badges |
| 3-5 | Comfortable play | Voice lines, skins, minor convenience unlocks |
| 6-8 | Specialist identity | Advanced cosmetics, profile badges |
| 9-10 | Dedicated mastery | Prestige cosmetics, title, showcase treatment |

Operator mastery nên reward commitment mà không tạo mandatory stat grind.

Mastery là identity track. Nó nên khuyến khích player học rhythm, voice, ability, và squad role của operator. Reward nên làm operator cá nhân hơn trong lobby/profile, trong khi combat balance vẫn do match rules và equipment kiểm soát.

## Quest System

Quest là cách designer dạy map mà không dùng tutorial pop-up. Quest tốt yêu cầu player tới một nơi, dùng một system, nhận một risk, hoặc chú ý một mảnh world. Nó nên tránh grind lặp lại bỏ qua extraction decisions.

| Quest Type | Reset | Purpose |
| :--- | :--- | :--- |
| Tutorial | One-time | Teach survival basics |
| Daily | 24 hours | Short-term goals and return habit |
| Weekly | 7 days | Medium goals and varied play |
| Faction | Persistent | World identity, reputation, and trader unlocks |
| Story | One-time chains | Narrative and directed exploration |
| Seasonal | Season-limited | Live Ops engagement and event identity |

## Battle Pass

Battle pass là seasonal checklist, không phải core progression spine. Nó nên reward regular play across modes và cung cấp catch-up path cho late-season players. Premium reward nên desirable, nhưng free-track reward phải chứng minh season không bị khóa sau spending.

| Component | Direction |
| :--- | :--- |
| Tracks | Free and premium |
| Reward type | Cosmetics, currency, materials, boosts that do not sell combat power |
| Progress sources | Raid XP, quests, event challenges |
| Catch-up | Late-season missions or boosted objectives |
| Integrity | No paid combat advantage |

## XP And Reward Rules

| Rule | Requirement |
| :--- | :--- |
| Extraction and objectives matter most | Extraction, quest completion, squad support, và meaningful objective play nên nặng hơn raw kill volume |
| Failed raids can still teach | Failed raid có thể grant limited account/operator/quest learning nếu player có meaningful progress |
| Raw kill farming is capped | Repeated trivial AI kills, spawn camping, hoặc low-risk loops bị diminishing returns |
| Catch-up respects early players | Catch-up tăng tốc late player mà không phủ nhận early-season participation hoặc paid/free fairness |
| Boosts are non-power | XP boosts không tạo combat certainty và phải disclose duration/source |
| Reward destination is explicit | Reward nói rõ đi tới stash, inbox, profile, currency balance, battle pass, trader, hoặc claim screen |
| Claim blockers are named | Stash full, premium locked, expired, capped, duplicate, và offline states phải có direct next action |

## Reward Taxonomy

| Reward Type | Player-Facing? | Gameplay-Affecting? | Seasonal? | Claim Behavior |
| :--- | :--- | :--- | :--- | :--- |
| Cosmetic | Yes | No | Optional | Claim/equip/view; có preview |
| Profile item | Yes | No | Optional | Claim vào profile inventory |
| Credits | Yes | Economy-affecting, không tự nó là power | Optional | Add vào balance hoặc inbox nếu capped |
| Premium token grant | Yes | No combat power | Optional | Add vào balance kèm source/receipt |
| Material / crafting input | Yes | Indirect economy value | Optional | Cần xử lý stash/capacity |
| Convenience unlock | Yes | Conditional non-power | Usually persistent | Phải earnable/capped và không tạo combat certainty |
| Access unlock | Yes | System access, không stat power | Persistent | Show requirement và unlocked destination |
| Title / badge | Yes | No | Optional | Profile destination |
| Account service | Yes | No | Persistent hoặc limited | Mô tả consequence và reversibility |

## Progression State Matrix

| State | Meaning | Required UI Behavior |
| :--- | :--- | :--- |
| Locked | Chưa đạt requirement | Show exact requirement, progress, và route |
| In progress | Player có partial progress | Show count, percentage, next step, và reset/expiry nếu có |
| Claimable | Reward earned nhưng chưa claim | Promote claim action và show destination |
| Claimed | Reward đã grant | Mark complete và tránh duplicate CTA |
| Expired | Time window kết thúc | Explain claim grace, conversion, hoặc lost state |
| Converted | Seasonal/expired value đổi thành value khác | Show conversion amount và policy |
| Capped | Progress/reward chạm limit | Explain cap và khi nào reset |
| Overflow | Reward không fit destination | Route tới inbox/stash/capacity fix và preserve reward |
| Retroactive grant | Player qualify sau purchase, fix, hoặc rule change | Show source, receipt/support context, và claim destination |

## Retention Loops

Retention nên đến từ confidence và aspiration, không chỉ fear of missing out. Player nên quay lại vì họ có plan: hoàn thành trader chain, master operator, recover sau raid thất bại, push ranked, hoặc unlock cosmetic phản ánh cách họ chơi.

| Timeframe | Player Goal | System Support |
| :--- | :--- | :--- |
| Day 1 | Learn extraction and bank first win | Tutorial Raid, starter quests |
| Week 1 | Build stash and choose favorite operator | Daily quests, operator mastery |
| Month 1 | Unlock traders and understand economy | Faction reputation, Safe House upgrades |
| Season | Complete battle pass and event goals | Live Ops, ranked, clan missions |
| Long term | Master roles and build identity | Achievements, cosmetics, profile, prestige |

## Anti-Frustration Rules

| Risk | Mitigation |
| :--- | :--- |
| New player loses everything | Starter kits, Scavenger Run, protected onboarding |
| Player has no goal | Daily/weekly/faction quest surfacing |
| Progress feels paywalled | Earnable paths for convenience and cosmetics |
| Meta becomes stale | Live Ops events, balance patches, rotating objectives |

## Progression Examples

Day-one player hoàn thành Operation Zero, extract một lần, và unlock starter faction task. Mục tiêu là chuyển tutorial confidence thành objective thật ngắn mà không overwhelm họ bằng mọi system cùng lúc.

Week-one player bắt đầu thích một operator. Operator mastery reward nên nhận diện identity đó bằng cosmetic, voice, profile treatment, và tips, nhưng tránh stat bonus khiến switching role tệ đi.

Seasonal player quay lại vì event. Battle pass, faction objective, và live quest nên cùng trỏ về seasonal activity để progress có cảm giác phối hợp, không tản mạn.

## Tuning Notes

- XP nên reward extraction và objective completion ổn định hơn raw kill volume.
- Catch-up nên giảm late-season pressure mà không phủ nhận early participation.
- Quest chain nên đổi route, item, behavior requirement để tránh grind fatigue.
- Prestige nên cosmetic-first cho đến khi long-term balance được chứng minh.

## Progression Analytics

| Signal | Use |
| :--- | :--- |
| XP source distribution | Detect kill farming, objective under-rewarding, hoặc event over-rewarding |
| Quest abandon and reroll rate | Tìm objective không rõ, tẻ nhạt, hoặc routing kém |
| Reward claim latency | Reveal claim surfaces ẩn hoặc reward destination không rõ |
| Battle pass tier velocity | Tune season length, catch-up missions, và reward cadence |
| Catch-up use and completion | Kiểm tra late-season support có hữu ích mà không thành mandatory |
| Operator mastery concentration | Detect role imbalance hoặc reward kéo quá mạnh về một operator |
| Faction reputation pace | Tune trader access và quest chain length |
| Overflow/blocked claim rate | Improve stash, inbox, hoặc reward routing UX |

## Cross-References

| Topic | Page |
| :--- | :--- |
| Economy and monetization ethics | [Economy](economy.html) |
| Event cadence | [Live Operations](liveops.html) |
| Player stats and achievements | [Player Profile](playerprofile.html) |
| Tutorial goals | [Tutorial Raid](tutorialraid.html) |
| Clan missions | [Clan System](clansystem.html) |
| Inventory item lifecycle | [Inventory System](../Inventory_System/) |
| Gear tier and rarity rules | [Gear Tier System](../Gears/Gear_Tier_System.md) |
