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

## Currency Types

| Currency | Source | Sink | Can Be Bought? | Design Notes |
| :--- | :--- | :--- | :--- | :--- |
| Credits | Loot sales, quests, events | Gear, insurance, repairs, upgrades | No direct power purchase | Core soft economy |
| Tokens | Purchases, battle pass rewards | Cosmetics, battle pass, convenience | Yes | Must not buy combat power |
| Reputation | Faction quests and events | Trader unlocks, quest access | No | Long-term trust and specialization |
| Event Currency | Limited-time events | Event cosmetics and rewards | Event-defined | Expires or converts by policy |

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

Commerce UI, offer taxonomy, purchase confirmation, provider handoff, receipt, refund, và entitlement states nằm ở [Commerce Screens](../UI_UX/Commerce_Screens.md). Economy quyết định thứ gì được bán và vì sao; Commerce quyết định cách trình bày offer, checkout trust, và các state nhạy cảm với support.

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

## Ethical Monetization Rules

| Promise | Implementation |
| :--- | :--- |
| Spend to express identity | Cosmetics, banners, skins, emotes |
| Spend to save time carefully | Convenience must be earnable and capped |
| Never sell power | No paid stat advantage |
| Be clear about value | Show contents, duration, and refund rules |
| Protect minors | Spending controls and platform compliance |

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
| Progression and battle pass XP | [Progression](progression.html) |
| Seasonal economy events | [Live Operations](liveops.html) |
| Shop UX và purchase states | [Commerce Screens](../UI_UX/Commerce_Screens.md) |
| Insurance costs | [Insurance System](insurancesystem.html) |
| Safe House upgrade sinks | [Safe House Design](safe_house_design.html) |
| Loadout value display | [Loadout Preparation](loadoutpreparation.html) |
