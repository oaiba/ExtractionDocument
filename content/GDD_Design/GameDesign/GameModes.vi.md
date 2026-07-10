---
title: "Game Modes Design"
type: docs
---

## Overview

Game modes định nghĩa vì sao player bước vào extraction loop và rule nào định hình mỗi run. Raid là core experience; mọi mode khác phải hỗ trợ onboarding, recovery, competition, hoặc live operations mà không làm loãng extraction identity.

Mỗi mode nên trả lời một nhu cầu player. Raid là identity chính. Scavenger Run giúp recovery. Blitz hỗ trợ short session. Ranked đưa mastery lên competitive stage. Co-op Training cho player practice system không bị PvP pressure. Featured modes tạo novelty mà không rewrite core economy mỗi tuần.

Mode design phải tránh chia audience thành các game không tương thích. Player học route, sound, extraction timing, và inventory risk ở một mode phải dùng được knowledge đó ở mode khác. Rule change có thể chỉnh pressure, nhưng không nên dạy habit fail trong core raid.

## Mode Selection Flow

Selection flow phải show risk trước matchmaking. Player không nên load xong mới biết insurance disabled, gear loss nặng hơn, squad fill đang bật, hoặc event có extraction rule đặc biệt. Confirmation step là contract giữa mode và player.

| Step | Screen / Action | Result |
| :--- | :--- | :--- |
| 1 | Home Screen | Player chooses to deploy |
| 2 | Loadout Preparation | Player reviews gear and squad state |
| 3 | Choose Mode | Player selects Raid, Scav, Blitz, Ranked, Co-op, or Featured |
| 4 | Choose Map or Event | Player commits to zone rules and event modifiers |
| 5 | Choose Squad Size | Player confirms Solo, Duo, Trio, or fill |
| 6 | Confirm Risk | UI summarizes gear loss, insurance, and rewards |
| 7 | Matchmaking | Queue begins with selected rules |

## Mode Catalogue

| Mode | Purpose | Risk | Squad Size | Notes |
| :--- | :--- | :--- | :--- | :--- |
| The Raid | Core extraction experience | Normal | Solo, Duo, Trio | Full loot, full progression, insurance supported |
| Scavenger Run | Recovery and practice | Low | Solo, Duo | Free temporary kit, limited rewards, no insurance |
| Blitz | Short session quick play | Medium | Solo, Duo, Trio | Faster timer, reduced map size, faster extraction pressure |
| Ranked Operations | Competitive extraction | High | Solo, Duo, Trio | RP enabled, stricter matchmaking, limited rule changes |
| Co-op Training | Low-pressure mastery | Low | Solo, Duo, Trio | PvE learning, no premium rewards |
| Featured Mode | Live Ops variety | Variable | Event-defined | Rotates through seasonal rules |

## Mode Rule Contract

Mỗi mode card và deploy confirmation phải show rule contract trước khi matchmaking starts. Nếu mode thay đổi loss, insurance, quest progress, extraction timing, hoặc rewards, player phải thấy trước khi bấm Deploy.

| Mode | Timer | Squad Size | Player Density | AI Density | Gear Loss | Insurance | Quest Progress | Reward Cap | Extraction Modifier | Matchmaking Pool |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| The Raid | 10-15 min target run | Solo/Duo/Trio | Standard | Standard | Enabled | Enabled | Full | None | Standard extraction rules | Casual regional |
| Scavenger Run | Standard hoặc ngắn hơn | Solo/Duo | Standard hoặc lower | Standard | Temporary scav kit only | Disabled | Limited | Lower loot ceiling | Standard, nhưng lower-value extracts allowed | Recovery-weighted casual |
| Blitz | Short | Solo/Duo/Trio | Medium-high | Reduced hoặc focused | Enabled | Enabled trừ khi event nói khác | Limited hoặc full theo map | Lower raid value ceiling | Faster late pressure và shorter extract windows | Casual quick-play |
| Ranked Operations | Season-defined | Solo/Duo/Trio | Competitive target | Standard | Enabled | Restricted hoặc disabled | Ranked-safe only | Ranked rewards và cosmetics | Standard trừ khi season rule explicit | Ranked pool |
| Co-op Training | Flexible | Solo/Duo/Trio | None PvP | Tutorial/training | Disabled hoặc restored | Not needed | Tutorial/training only | No premium/economy farming | Guided extraction và retry support | PvE training |
| Featured Mode | Event-defined | Event-defined | Event-defined | Event-defined | Must be disclosed | Must be disclosed | Must be disclosed | Event-defined | Modifier nào cũng phải disclosed | LiveOps event pool |

## Mode Compatibility Matrix

Mode variants có thể adjust pressure, nhưng không được dạy thói quen làm hỏng core raid loop.

| Core Skill | The Raid | Scavenger Run | Blitz | Ranked | Co-op Training | Featured |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Route reading | Primary | Practice | Compressed | Primary | Guided | Depends on event |
| Loot risk | Primary | Low-stakes | Faster decisions | High-stakes | Tutorial only | Event-defined |
| Combat judgment | Primary | Practice | Frequent | Competitive | AI-focused | Event-defined |
| Extraction timing | Primary | Practice | Faster | Primary | Guided | Must be explicit |
| Gear fear | Primary | Reduced | Medium | High | Disabled | Event-defined |
| Economy impact | Full | Capped | Reduced hoặc full | Full với ranked rules | Minimal | Explicitly capped |
| Tutorial value | Moderate | High for recovery | Low | Low | Primary | Contextual |

Nếu một mode bỏ cả gear risk và extraction pressure, nó phải được frame là training hoặc event novelty, không phải recommendation chính.

## Core Mode Rules

### The Raid

The Raid là reference mode. Balance, economy, onboarding, và map design phải được đánh giá trước tiên theo mode này.

The Raid phải tự hoàn chỉnh về cảm xúc: preparation, fear, opportunity, conflict, extraction, recovery. Nếu một feature chỉ hoạt động ở mode khác nhưng làm hại The Raid, nó nên là variant rule thay vì core design.

| Parameter | Target |
| :--- | :--- |
| Match length | 10-15 minutes |
| Player count | Tuned per map size |
| AI threat | Present around loot and objectives |
| Gear loss | Enabled |
| Insurance | Enabled |
| Quest progress | Enabled |

### Scavenger Run

Scavenger Run ngăn poverty spiral và cho player practice route mà không risk stash.

Mode này nên hữu ích nhưng không tối ưu nhất. Nó là pressure release valve sau khi mất gear, learning tool cho route mới, và cách re-enter loop mà không giveaway premium rewards. Nó không được trở thành farming path tốt nhất.

| Rule | Direction |
| :--- | :--- |
| Starting kit | Randomized low-value kit |
| Cooldown | Required to prevent farming |
| Rewards | Extracted loot allowed, but lower ceiling than The Raid |
| Progression | Limited account XP, no ranked progress |

### Ranked Operations

Ranked Operations dùng core extraction loop với competitive rules chặt hơn. Full RP design nằm trong [Ranked Mode](rankedmode.html).

Ranked phải test extraction mastery, không chỉ elimination skill. Ranked player giỏi nhất phải biết khi nào tránh fight, khi nào secure value, khi nào pressure squad khác, và khi nào leave. Reward nên tôn vinh consistency, discipline, và clutch decision.

| Rule | Direction |
| :--- | :--- |
| Matchmaking | Rank-aware, latency-aware, anti-smurf monitored |
| Insurance | Disabled or restricted per season rules |
| Rewards | Rank points, cosmetics, leaderboard position |
| Integrity | Stronger penalties for disconnects, boosting, and collusion |

## Mode Card Requirements

Mode card phải truyền đạt emotional contract của mỗi queue. Player phải biết đây là stash-risk raid nghiêm túc, recovery run, warm-up nhanh, competitive match, hay seasonal experiment trước khi confirm.

| Field | Required |
| :--- | :--- |
| Mode name | Yes |
| Risk level | Yes |
| Estimated raid length | Yes |
| Gear loss rules | Yes |
| Insurance rules | Yes |
| Squad sizes | Yes |
| Reward type | Yes |

## Mode Design Examples

The Raid nên là default recommendation cho player có valid kit và không có recovery state cấp bách. Đây là nơi balance economy, quest, map, và insurance đầu tiên.

Scavenger Run nên được recommend sau repeated losses hoặc stash value thấp. UI nên frame mode này là recovery và practice, không phải shame state.

Blitz hữu ích khi player ít thời gian. Nó có thể giảm map size và timer length, nhưng vẫn cần loot, danger, và extraction decision.

Featured Mode nên distinct về visual nhưng transparent về rule. Nếu event sửa insurance, extraction timing, AI density, hoặc reward cap, rule đó phải show trước matchmaking.

## Mode Failure Cases

- Nếu player farm Scavenger Run thay raid thường, reward ceiling quá cao.
- Nếu Blitz dạy habit reckless fail trong The Raid, pressure tuning quá arcade-like.
- Nếu Ranked thành kill-only, RP weights cần reinforce extraction và objective.
- Nếu Featured Mode cần giải thích dài, modifier có thể quá phức tạp.
| Event timer | Only for featured modes |

## Cross-References

| Topic | Page |
| :--- | :--- |
| Prep screen integration | [Loadout Preparation](loadoutpreparation.html) |
| Ranked rules | [Ranked Mode](rankedmode.html) |
| Event rotations | [Live Operations](liveops.html) |
| Map rules | [Map Design](mapdesign.html) |
| Insurance mode differences | [Insurance System](insurancesystem.html) |
