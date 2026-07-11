---
title: "Live Operations & Events"
type: docs
---

## Overview

Live Ops giữ game tươi mới sau launch bằng seasons, events, featured modes, balance updates, battle pass content, faction wars, và community beats.

Live Ops nên làm world có cảm giác đang sống mà không khiến base game có vẻ chưa hoàn chỉnh. Returning player cần thấy lý do mới để chơi, nhưng new player vẫn phải hiểu core raid loop mà không cần học lịch sự kiện. Seasonal content là lớp phủ trên extraction, không phải thứ thay thế nó.

Live schedule khỏe nên luân phiên cường độ. Quiet weeks hỗ trợ routine play và economy stability. Event weeks tạo spike attention. Patch weeks khôi phục trust bằng cách cho thấy balance, readability, và player feedback đang được xử lý.

## Cadence

Cadence phải đủ predictable để player plan và đủ flexible để designer phản ứng với live data. Game không nên phụ thuộc vào novelty liên tục để còn vui; live content nên refresh goal, route, reward, và social conversation.

| Cadence | Content | Purpose |
| :--- | :--- | :--- |
| Weekly | Rotating quests, small modifiers, featured shop refresh | Habit and variety |
| Monthly | Balance patch, event beat, small content drop | Meta health |
| Seasonal | Battle pass, theme, ranked reset, major event | Long-term return |
| Yearly | Major map, feature, or expansion | Reposition and re-engage |

## LiveOps System Model

LiveOps là operating layer lên lịch temporary goals mà không làm yếu core raid loop. Mỗi live beat phải định nghĩa time window, player action, reward implication, communication surface, và end behavior trước khi ship.

| Entity | Định nghĩa | Yêu cầu UI / Design |
| :--- | :--- | :--- |
| `Season` | Giai đoạn content/progression kéo dài nhiều tuần | Show theme, dates, battle pass, ranked reset, major events, recap/archive state |
| `Event` | Objective, mode, modifier, collection, hoặc community beat có thời hạn | Show rules, expiry, objective progress, reward ladder, và play route |
| `FeaturedMode` | Mode hoặc rule variant được promote tạm thời | Show exact modifier, risk, eligibility, và ranked/economy rules có khác không |
| `Objective` | Player/community task feed vào event/progression | Show count, source, progress, reward, tracking, reset/expiry |
| `RewardTrack` | Reward ladder cho event, season, battle pass, hoặc faction war | Show free/premium/event distinction, claim states, reward destinations |
| `EventCurrency` | Seasonal currency earn/spend trong event | Show cap, expiry, conversion, store destination |
| `PatchBeat` | Đơn vị communication cho balance/content/update | Show affected systems, reason, player impact, deep links |
| `CompensationGrant` | Targeted grant để phục hồi trust sau incident | Show reason, eligibility window, claim destination, support reference |
| `SeasonReset` | Transition cuối season cho rank, event, battle pass, rewards | Show retained, reset, archived, converted, claim-grace rules |

## Season Flow

Mỗi season cần arc readable: announcement, launch, mastery, disruption, final push, recap. Player phải biết cái gì mới, cái gì temporary, cái gì vẫn còn complete được, và chuyện gì xảy ra khi season kết thúc.

| Phase | Timing | Player Message | UI Destination | Reward / Backend State |
| :--- | :--- | :--- | :--- | :--- |
| Pre-season reveal | Before launch | Theme, dates, major rules, rewards preview | News, Season Summary preview | No progression; chỉ preview/wish-list |
| Season launch | Week 1 | New goals are live | Battle Pass, Event Hub, Ranked Overview | Battle pass active, ranked reset applied, launch tasks active |
| Early progression | Weeks 1-3 | Learn the season loop | Daily/Weekly Tasks, Quest Board | Normal earn rates, catch-up off hoặc nhẹ |
| Mid-season event | Middle weeks | New disruption and renewed goals | Event Hub, News, Map/Mode deep links | Event currency/reward ladder active |
| Balance patch | After live data review | What changed and why | Patch Notes, known issues, affected screens | Economy/meta values updated kèm migration note nếu cần |
| Final push | Last weeks | What can still be completed | Battle Pass, Event Hub, Reward Inbox | Claim reminders, catch-up missions, expiry labels promoted |
| End grace period | After season end | Claim remaining earned rewards | Reward Inbox, Season Summary | Progression disabled; earned claims/conversions remain |
| Recap/archive | End of grace | What was achieved and retained | Season Summary archive | Final grants delivered; archive read-only |

## Event Types

Event nên thay đổi hành vi player theo mục tiêu cụ thể. Boss hunt kéo squad vào hotspot. Faction war đổi objective priority. Double XP weekend đổi progression pacing. Nếu event không tạo decision khác trong raid, nó có lẽ chỉ là reward multiplier.

| Event | Duration | Objective Pattern | Reward Pattern | Risk / Expiry Rule |
| :--- | :--- | :--- | :--- | :--- |
| Double XP / Credits | Weekend | Chơi raid bình thường với eligible sources được boost | XP hoặc credits | Không được thành cách in wealth tốt nhất; boost window phải rõ |
| Limited-Time Mode | 1-2 weeks | Queue vào modified rules rõ ràng | Cosmetics, event currency, titles | Opt-in trừ khi modifier an toàn cho new player |
| Faction Wars | 2-4 weeks | Chọn faction, làm personal/clan/community objectives | Banners, titles, faction cosmetics | Faction thắng đổi presentation, không grant permanent combat power |
| Boss Hunt | 1-2 weeks | Đẩy vào hotspot, defeat boss, extract proof/reward | Unique cosmetics, trophies, event currency | Boss rewards deterministic hoặc table rõ; extraction risk visible |
| Collection Event | 2 weeks | Earn/spend event currency để hoàn tất collection | Themed cosmetics và collection reward | Collection progress, owned count, end grace explicit |
| Ranked Event | 1-2 weeks | Compete trong scoring/rule window đã announce | Titles, badges, cosmetic frames | Ranked integrity rules publish trước khi start |
| Community Challenge | 1-3 weeks | Góp global objectives qua normal play | Account-wide grants, banners, event story | Personal contribution và final grant policy visible |

## Featured Mode Rules

| Mode | Modifier | Risk |
| :--- | :--- | :--- |
| Night Ops | Low visibility, stronger audio play | Medium |
| Extraction Rush | Shorter timer, faster extracts | High |
| Hardcore | Reduced HUD, stricter loss rules | Very high |
| Solo Showdown | Solo-only matchmaking | Medium |
| Chaos Mode | Increased events and AI pressure | High |

## Faction Wars

Faction wars là community stories. Chúng nên cho solo players đóng góp meaningful trong khi clan có lý do coordinate. Winning faction có thể đổi presentation, banner, hoặc world state, nhưng không được grant permanent combat superiority.

| Contribution | Feeds Into | Reward / Outcome |
| :--- | :--- | :--- |
| Player chooses event faction | Faction alignment | Determines event identity and reward track |
| Player completes faction objectives | Personal score | Unlocks personal event rewards |
| Clan members complete objectives | Clan contribution | Moves clan leaderboard position |
| Total faction activity | Faction war outcome | Determines winning faction presentation |
| Event ends | Recap and reward grant | Delivers personal, clan, and faction rewards |

## Live Ops Guardrails

Guardrail bảo vệ trust. Player sẵn sàng engage temporary content hơn khi họ tin event không invalidate công sức, không phá ranked fairness, và không flood economy bằng reward khiến raid thường vô nghĩa.

| Guardrail | Rule |
| :--- | :--- |
| No event-only power | Event rewards cannot create permanent combat advantage |
| Avoid burnout | Weekly goals must be achievable without unhealthy playtime |
| Maintain economy health | Event rewards must respect item supply and currency sinks |
| Protect ranked integrity | Ranked rule changes must be announced and measurable |
| Keep content readable | Event modifiers must not break mobile clarity |

## Event Reward And Currency Rules

| Rule | Requirement |
| :--- | :--- |
| Event currency cap | Nếu currency earn lặp lại, show cap, reset, và overflow bị lost/blocked/converted |
| Conversion policy | Event currency expiry phải show exact conversion hoặc deletion rule trước khi event kết thúc |
| Claim grace | Earned but unclaimed rewards nên move tới inbox hoặc grace period, không silently disappear |
| Deterministic clarity | Purchasable/claimable event rewards phải show exact contents; no paid RNG |
| No event-only permanent power | Event reward có thể đổi identity/story/cosmetic/temporary opt-in rules, không tạo permanent combat superiority |
| Store split | Event progress/rewards nằm ở LiveOps; event purchases và checkout nằm ở Commerce |
| Ranked protection | Ranked events phải giữ matchmaking, input, exploit, và eligibility rules |

## Patch / Communication Rules

| Communication Type | Requirement |
| :--- | :--- |
| Balance patch | Nói rõ affected systems, reason, player impact, và loadouts/economy values có đổi không |
| Economy adjustment | Explain vì sao values đổi và existing inventory có bị ảnh hưởng không |
| Event announcement | Show start/end dates, rules, rewards, restrictions, playable route |
| Known issue | Có severity, affected platforms, workaround, next update expectation |
| Compensation | Show reason, eligibility window, grant contents, claim route, support reference |
| Mandatory update | Chỉ dùng system modal cho version/security blockers; còn lại dùng News/Patch Notes |

## LiveOps QA Checklist

- [ ] Season reveal, launch, final push, end grace, recap, và archive states được định nghĩa.
- [ ] Event end behavior cover objectives, unclaimed rewards, event currency, store access, và archive copy.
- [ ] Reward claims route qua Battle Pass, Event Hub, hoặc Reward Inbox, không silently disappear.
- [ ] Expired objectives giải thích progress bị lost, converted, hoặc moved to inbox.
- [ ] Ranked reset và ranked event rules visible trước khi queue.
- [ ] Compensation grants targeted, auditable, và duplicate-safe.
- [ ] Offline/cached news không show stale playable CTAs.
- [ ] Event modifiers không phá accessibility, mobile readability, hoặc new-player comprehension.
- [ ] Economy-affecting events có caps, sinks, hoặc conversion policies.
- [ ] Commerce purchase routes được link nhưng không duplicate trong LiveOps specs.

## Event Design Examples

Night Ops event nên đổi cách đọc route, giá trị audio, và extraction tension, không chỉ làm màn hình tối hơn. Event cần silhouette mạnh hơn, accessibility fallback rõ, và reward khớp theme.

Faction War nên cho solo players personal progress trong khi clan đóng góp vào public result lớn hơn. Result có thể đổi banner, recap presentation, và world flavor mà không grant combat advantage vĩnh viễn.

Boss Hunt nên tạo hotspot với danger readable. Player phải biết vì sao squad hội tụ, boss reward là gì, và extraction khó hơn thế nào sau khi objective hoàn thành.

## Live Ops Failure Cases

- Nếu weekly goal cần số giờ không lành mạnh, giảm objective count hoặc thêm alternate path.
- Nếu event currency flood economy, thêm capped sink hoặc conversion rule.
- Nếu modifier làm new player confused, giới hạn trong opt-in modes hoặc cải thiện rule cards.
- Nếu ranked đổi giữa season, communicate timing, reason, expected impact.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Battle pass progression | [Progression](progression/index.html) |
| Economy rewards | [Economy](economy/index.html) |
| Featured modes | [Game Modes](gamemodes/index.html) |
| Ranked seasons | [Ranked Mode](rankedmode/index.html) |
| Clan competition | [Clan System](clansystem/index.html) |
