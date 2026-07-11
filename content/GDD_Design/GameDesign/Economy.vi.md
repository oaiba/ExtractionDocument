---
title: "Economy & Monetization Design"
type: docs
---

## Overview

Economy sở hữu currencies, value flow, monetization ethics, marketplace health, và economic safety systems. Progression sở hữu XP, level, quest, và battle pass advancement.

Economy phải làm extracted items có giá trị mà không biến game thành bài tập kế toán. Player cần hiểu vì sao item quan trọng, nên bán, equip, craft, insure, hay giữ cho quest. Economy tốt làm raid decision tiếp tục có ý nghĩa sau khi match kết thúc.

Rule thương mại rất đơn giản: revenue có thể hỗ trợ identity, convenience, và seasonal engagement, nhưng không được bán combat certainty. Player có thể mua skin, battle pass, hoặc convenience unlock kiếm được bằng chơi. Họ không được mua một gunfight.

## Philosophy

Economy philosophy phải visible trong UI language. Khi player thấy price, insurance cost, trader lock, hoặc premium offer, interface phải reinforce fairness: thứ gì earned through play, thứ gì cosmetic, thứ gì convenience, và thứ gì không bao giờ grant combat power.

| Principle | Rule |
| :--- | :--- |
| No pay-to-win | Never sell weapons, armor, stats, or exclusive combat power |
| Loss must matter | Gear risk supports extraction tension |
| Recovery must exist | Players need comeback paths after bad streaks |
| Prices teach value | Item values should guide what players choose to extract |
| Economy must be monitored | Inflation, hoarding, and poverty spirals need live dashboards |

## Currency Flow

Currency flow nên tạo friction lành mạnh. Credits rời economy qua gear, repairs, insurance, crafting, và upgrades. Value vào economy qua risk: raids, quests, events, trading. Nếu player có thể giàu lên mà không bước vào danger, extraction loop yếu đi.

| Source | Becomes | Main Sinks | Design Role |
| :--- | :--- | :--- | :--- |
| Raid loot | Extracted stash items | Sell, equip, craft, trade | Converts risk into value |
| Sold loot | Credits | Gear, insurance, repairs, Safe House upgrades | Main soft-currency loop |
| Premium purchase | Tokens | Cosmetics, battle pass, fair convenience | Revenue without combat power |
| Faction quests | Reputation | Trader access and quest unlocks | Long-term specialization |
| Events | Event currency | Event cosmetics and limited rewards | Seasonal engagement |

## Economy System Model

Economy model tạo vocabulary chung cho designer và engineer về cách value di chuyển. Mọi reward, purchase, repair, insurance fee, event grant, và compensation package nên map vào một object rõ ràng để UI copy và telemetry cùng giải thích một sự thật.

| Entity | Định nghĩa | Yêu cầu UI / Design |
| :--- | :--- | :--- |
| `Currency` | Giá trị đếm được dùng cho purchase, upgrade, claim, hoặc event exchange | Luôn hiển thị tên, số lượng, source, và loại earnable/premium/seasonal/reputation-like |
| `Source` | System thêm value vào account hoặc stash | Phải giải thích vì sao player nhận value và value đi tới đâu |
| `Sink` | System lấy value khỏi account hoặc stash | Phải giải thích cost, consequence, và spend có reversible không |
| `Reward` | Value được grant từ raid, quest, event, battle pass, compensation, hoặc purchase | Phải khai báo type, destination, claim state, expiry, và gameplay impact |
| `TraderPrice` | Giá gear, service, repair, crafting input, hoặc trade offer | Phải show reputation requirement, stock state, và lý do đổi giá nếu dynamic |
| `RepairCost` | Cost để restore durability/readiness của item | Phải preview trước commit và show durability before/after |
| `InsuranceCost` | Cost bảo hiểm loadout item theo insurance rules | Phải show return chance/rule, return window, và blocked conditions |
| `EventCurrency` | Seasonal value kiếm trong limited window | Phải show expiry, cap, conversion, và event store destination |
| `PremiumToken` | Premium currency mua hoặc grant qua non-power route | Không bao giờ dùng để mua combat certainty; purchase UX thuộc Commerce |
| `InflationSignal` | Telemetry báo value growth không lành mạnh | Phải segment theo account age, skill, mode, platform, và season phase |

## Currency Types

| Currency | Source | Sink | Can Be Bought? | Design Notes |
| :--- | :--- | :--- | :--- | :--- |
| Credits | Loot sales, quests, tasks, compensation, trader payouts | Gear, repair, insurance, crafting, Safe House upgrades, trader fees | No direct premium purchase | Core soft economy; không bypass mastery hoặc reputation locks |
| Tokens | Premium purchase, battle pass grants, event grants, compensation | Cosmetics, battle pass, capped non-power convenience | Yes | Không mua weapon, armor, stat advantage, protected combat slot, hoặc matchmaking advantage |
| Reputation | Faction quests, event alignment, trader tasks | Trader unlocks, quest access, faction identity | No | Không là spendable power currency; mất reputation phải hiếm và rõ |
| Event Currency | Limited-time events and seasonal objectives | Event cosmetics, deterministic rewards, event collection progress | Event-defined | Expire hoặc convert theo policy; không silently disappear nếu reward đã claimable |

## Sources And Sinks Matrix

| Value Source | Grants | Required Context | Primary Sink / Follow-Up |
| :--- | :--- | :--- | :--- |
| Extracted loot | Items, credits sau khi bán, crafting inputs | Found-in-raid state, rarity, trader value | Sell, equip, craft, quest turn-in, stash |
| Quest reward | Credits, XP, reputation, items, unlocks | Quest source, completion reason, claim state | Progression tracks, traders, loadout recovery |
| Daily / weekly task | XP, credits, items, rep, battle pass XP | Reset timer, progress, reward destination | Short-term return loop |
| Event objective | Event currency, cosmetics, XP, credits | Event name, expiry, conversion policy | Event store, reward ladder, inbox |
| Battle pass free track | Cosmetics, currency, materials | Tier, free/premium lane, claim state | Identity, progression, economy support nhẹ |
| Battle pass premium track | Cosmetics, premium tokens, non-power boosts | Premium state, Commerce upgrade route | Identity và seasonal value |
| Compensation grant | Items, credits, tokens, inbox entries | Reason, affected window, support reference | Recovery và trust repair |
| Gear purchase | Gear item | Trader, stock, reputation, price | Raid loadout và risk |
| Repair / insurance | Restored durability hoặc protected item | Item state, cost, rules, timer | Loss mitigation |
| Crafting / Safe House | Crafted items, module upgrades | Inputs, time, unlock requirement | Long-term sinks và planning |
| Cosmetic purchase | Cosmetic entitlement | Offer, ownership, confirmation, receipt | Purchase UX thuộc Commerce |

## Monetization Structure

Monetization phải "boring" ở đúng chỗ. Store có thể exciting về visual, nhưng rule phía sau phải predictable và audit dễ. Bất kỳ thứ gì đổi visibility, recoil, hitbox, sound readability, hoặc inventory survival đều được xem là power và không bán.

| Product | Allowed | Guardrail |
| :--- | :--- | :--- |
| Battle Pass | Yes | Rewards cosmetics, currency, and fair progression boosts |
| Operator cosmetics | Yes | No stat advantage |
| Weapon skins | Yes | No visibility or recoil advantage |
| Stash expansion | Yes, if earnable | Must have free progression path |
| Loadout slots | Yes, if earnable | Convenience only |
| Loot boxes | No | Avoid paid RNG power perception |
| Better weapons or armor | No | Violates no pay-to-win |

Commerce UI, offer taxonomy, purchase confirmation, provider handoff, receipt, refund, và entitlement states nằm ở [Commerce Screens](../ui_ux/commerce_screens/index.html). Economy quyết định thứ gì được bán và vì sao; Commerce quyết định cách trình bày offer, checkout trust, và các state nhạy cảm với support.

## Marketplace Rules

Marketplace design nên support player agency mà không để market thành main game. Trading hữu ích khi giúp player chuyển unwanted value thành useful value. Nó harmful khi bot, price manipulation, hoặc real-money trading làm raid reward bình thường trở nên irrelevant.

| Rule | Purpose |
| :--- | :--- |
| Price bands | Prevent extreme manipulation |
| Listing fees | Create credit sink |
| Trade limits | Reduce real-money trading and bots |
| Item provenance | Track found-in-raid, crafted, traded, and insured status |
| Suspicious trade detection | Protect economy health |

## Economy Health Metrics

Economy telemetry phải segmented theo account age, skill bracket, mode, và platform. Median khỏe có thể che new-player bankruptcy hoặc veteran inflation. Designer nên review economy health cùng extraction rate, insurance use, và average loadout value.

| Metric | Watch For | Possible Action |
| :--- | :--- | :--- |
| Median player credits | Poverty spiral or inflation | Adjust loot value, sinks, quest rewards |
| Item price volatility | Manipulation or scarcity | Adjust drop rates and price bands |
| Insurance usage | Too much loss pain or too much safety | Tune cost and return timer |
| Gear tier distribution | Overpowered meta or stagnant progression | Tune trader unlocks and item availability |
| New player bankruptcy | Onboarding failure | Increase tutorial rewards or recovery quests |

## Inflation / Poverty / Hoarding Guardrails

| Risk | Trigger Signal | Guardrail |
| :--- | :--- | :--- |
| New-player bankruptcy | Account mới không afford basic kit sau nhiều raid thất bại | Tăng tutorial/recovery rewards, surface budget presets, giảm early repair pressure |
| Veteran hoarding | Player lâu năm giữ quá nhiều credits/items nhưng ít dùng sink | Thêm prestige cosmetics, crafting sinks, Safe House goals, hoặc vanity sinks không tạo power |
| High-tier saturation | Quá nhiều raid có top-tier kits so với extraction risk | Tune trader stock, repair cost, insurance return, rarity, và high-tier loot spawn |
| Event currency flood | Event currency nhiều hơn nhu cầu event store hoặc conversion policy | Thêm caps, deterministic sinks, conversion limits, và end-of-event messaging rõ |
| Compensation abuse | Grant lặp lại tạo farming incentive hoặc market distortion | Dùng targeted grants, eligibility windows, và receipt IDs audit được |
| Market manipulation | Price volatility vượt scarcity bình thường | Dùng listing fees, price bands, trade limits, provenance checks, suspicious trade detection |

## Economy Tuning Inputs

| Input | Vì sao quan trọng | Cadence review |
| :--- | :--- | :--- |
| Extraction rate | Xác định value raid sống sót thường xuyên thế nào | Daily khi launch, weekly khi ổn |
| Average raid value | Cho biết risk có tạo reward đủ ý nghĩa không | Weekly theo map/mode/skill |
| Average kit cost | Đo normal play có affordable không | Weekly theo account age và rank |
| Repair cost ratio | Đo durability có fair hay punitive không | Weekly sau balance patch |
| Insurance use and return rate | Đo loss mitigation có trusted hoặc quá mạnh không | Weekly theo item tier |
| Stash pressure | Reveal hoarding, confusion, hoặc thiếu item sinks | Weekly theo account age |
| Trader unlock pace | Validate reputation và quest economy pacing | Mỗi season và major quest update |
| Premium token earn rate | Bảo vệ perceived fairness quanh premium currency grants | Mỗi season và event |
| Event currency earn/spend ratio | Tránh event store thiếu demand hoặc impossible completion | Daily trong active events |

## Gear Value And Item Sinks

Physical gear value được tạo và bị lấy khỏi economy thông qua play. Gear vào hệ thống qua raids, traders, crafting, quests, events, và compensation; gear rời hệ thống qua death, sale, crafting, repair loss, quest turn-in, discard, wipe/reset rules. Commerce có thể bán cosmetic entitlements hoặc non-power services, nhưng không tạo paid combat-power item instances.

| Gear Economy Concept | Requirement |
| :--- | :--- |
| Gear value | UI nên giải thích value qua combat role, durability, weight, rarity/tier, repair cost, insurance cost, trader/quest relevance |
| Item sink | Sell, repair, craft, quest turn-in, discard, death loss, và durability degradation phải visible và auditable |
| Premium boundary | Premium purchases có thể unlock cosmetics hoặc capped convenience, không unlock weapons, armor, ammo, stat power, hoặc protected combat slots |
| Contraband/restricted gear | Restricted sale, trade, insurance, hoặc deploy behavior phải show readable reason |

## Ethical Monetization Rules

| Promise | Implementation |
| :--- | :--- |
| Spend to express identity | Cosmetics, banners, skins, emotes |
| Spend to save time carefully | Convenience must be earnable and capped |
| Never sell power | No paid stat advantage |
| Be clear about value | Show contents, duration, and refund rules |
| Protect minors | Spending controls and platform compliance |

## Economy QA Checklist

- [ ] Không paid product nào grant weapon, armor, stat, protected combat slot, visibility advantage, recoil advantage, hoặc matchmaking advantage.
- [ ] Credits không bypass mastery, reputation, tutorial gates, ranked eligibility, hoặc quest knowledge checks.
- [ ] Event reward không flood core market supply hoặc làm raid reward bình thường mất giá trị.
- [ ] Premium tokens chỉ dùng cho cosmetics, battle pass, và capped non-power convenience.
- [ ] Mọi source giải thích vì sao value được grant và đi tới đâu.
- [ ] Mọi sink preview cost, consequence, và blocked state trước commit.
- [ ] New-player recovery tồn tại nhưng không khiến failure profitable hơn success.
- [ ] Veteran sinks tạo aspiration mà không ép unhealthy grind.
- [ ] Compensation grants audit được và không khuyến khích retry/spam.
- [ ] UI text phân biệt earned, premium, seasonal, reputation, claimable, expired, và converted value.

## Economy Examples

Player cẩn trọng extract common industrial loot và bán đủ credits để repair armor, mua ammunition. Đây là low-risk loop khỏe vì nó thưởng survival mà không flood player bằng gear tier cao.

Veteran extract rare tech từ hot zone và chọn giữa selling, crafting, hoặc giữ cho faction task. Đây là high-value decision mong muốn: item có nhiều use hợp lý, không chỉ một vendor price obvious.

Player đang loss streak dùng Scavenger Run, budget preset, và low-cost insurance để rebuild. Economy nên support recovery path này mà không khiến failure profitable hơn normal success.

## Economy Failure Cases

- Nếu player hoard mọi thứ, stash pressure và sell value có thể chưa rõ.
- Nếu player bán mọi thứ ngay, crafting/quest/upgrade demand quá yếu.
- Nếu premium convenience thấy mandatory, monetization đã vượt thành pressure.
- Nếu new player không mua nổi basic kit, recovery reward hoặc budget gear cần chỉnh.
- Nếu veteran wealth làm risk trivial, sink và high-tier availability cần review.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Progression and battle pass XP | [Progression](progression/index.html) |
| Seasonal economy events | [Live Operations](liveops/index.html) |
| Shop UX và purchase states | [Commerce Screens](../ui_ux/commerce_screens/index.html) |
| Insurance costs | [Insurance System](insurancesystem/index.html) |
| Safe House upgrade sinks | [Safe House Design](safe_house_design/index.html) |
| Loadout value display | [Loadout Preparation](loadoutpreparation/index.html) |
| Inventory item lifecycle | [Inventory System](../Inventory_System/) |
| Gear tier and rarity | [Gear Tier System](../gears/gear_tier_system/index.html) |
