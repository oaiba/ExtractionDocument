---
title: "Economy & Monetization Design"
type: docs
---

## Overview

Economy owns currencies, value flow, monetization ethics, marketplace health, and economic safety systems. Progression owns XP, levels, quests, and battle pass advancement.

The economy should make extracted items feel valuable without turning the game into accounting homework. Players need to understand why an item matters, whether it should be sold, equipped, crafted, insured, or saved for a quest. Good economy design gives meaning to raid decisions after the match ends.

The commercial rule is simple: revenue can support identity, convenience, and seasonal engagement, but it cannot sell combat certainty. A player may buy a skin, a battle pass, or an earnable convenience unlock. They must not buy a gunfight.

## Philosophy

Economy philosophy should be visible in UI language. When a player sees a price, insurance cost, trader lock, or premium offer, the interface should reinforce fairness: what is earned through play, what is cosmetic, what is convenience, and what never grants combat power.

| Principle | Rule |
| :--- | :--- |
| No pay-to-win | Never sell weapons, armor, stats, or exclusive combat power |
| Loss must matter | Gear risk supports extraction tension |
| Recovery must exist | Players need comeback paths after bad streaks |
| Prices teach value | Item values should guide what players choose to extract |
| Economy must be monitored | Inflation, hoarding, and poverty spirals need live dashboards |

## Currency Flow

Currency flow should create healthy friction. Credits leave the economy through gear, repairs, insurance, crafting, and upgrades. Value enters the economy through risk: raids, quests, events, and trading. If players can grow wealth without entering danger, the extraction loop weakens.

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

Monetization must be boring in the right places. The store can be visually exciting, but the rules behind it should be predictable and easy to audit. Anything that changes visibility, recoil, hitboxes, sound readability, or inventory survival is treated as power and is not sold.

| Product | Allowed | Guardrail |
| :--- | :--- | :--- |
| Battle Pass | Yes | Rewards cosmetics, currency, and fair progression boosts |
| Operator cosmetics | Yes | No stat advantage |
| Weapon skins | Yes | No visibility or recoil advantage |
| Stash expansion | Yes, if earnable | Must have free progression path |
| Loadout slots | Yes, if earnable | Convenience only |
| Loot boxes | No | Avoid paid RNG power perception |
| Better weapons or armor | No | Violates no pay-to-win |

Commerce UI, offer taxonomy, purchase confirmation, provider handoff, receipt, refund, and entitlement states live in [Commerce Screens](../UI_UX/Commerce_Screens.md). Economy owns what can be sold and why; Commerce owns how offers, checkout trust, and support-sensitive states are presented.

## Marketplace Rules

Marketplace design should support player agency without letting the market become the main game. Trading is useful when it helps players convert unwanted value into useful value. It becomes harmful when bots, price manipulation, or real-money trading make normal raid rewards feel irrelevant.

| Rule | Purpose |
| :--- | :--- |
| Price bands | Prevent extreme manipulation |
| Listing fees | Create credit sink |
| Trade limits | Reduce real-money trading and bots |
| Item provenance | Track found-in-raid, crafted, traded, and insured status |
| Suspicious trade detection | Protect economy health |

## Economy Health Metrics

Economy telemetry should be segmented by account age, skill bracket, mode, and platform. A healthy median can hide a new-player bankruptcy problem or a veteran inflation problem. Designers should review economy health alongside extraction rate, insurance use, and average loadout value.

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

A cautious player extracts common industrial loot and sells it for enough credits to repair armor and buy ammunition. This is a healthy low-risk loop because it rewards survival without flooding the player with high-tier gear.

A veteran extracts rare tech from a hot zone and chooses between selling it, crafting with it, or saving it for a faction task. This is the desired high-value decision: the item has multiple legitimate uses, not just one obvious vendor price.

A player on a loss streak uses Scavenger Run, budget presets, and low-cost insurance to rebuild. The economy should support this recovery path without making failure more profitable than normal success.

## Economy Failure Cases

- If players hoard everything, stash pressure and sell value may be unclear.
- If players sell everything instantly, crafting, quests, and upgrade demand may be too weak.
- If premium convenience feels mandatory, monetization has crossed into pressure.
- If new players cannot afford basic kits, recovery rewards or budget gear need adjustment.
- If veteran wealth trivializes risk, sinks and high-tier availability need review.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Progression and battle pass XP | [Progression](progression.html) |
| Seasonal economy events | [Live Operations](liveops.html) |
| Shop UX and purchase states | [Commerce Screens](../UI_UX/Commerce_Screens.md) |
| Insurance costs | [Insurance System](insurancesystem.html) |
| Safe House upgrade sinks | [Safe House Design](safe_house_design.html) |
| Loadout value display | [Loadout Preparation](loadoutpreparation.html) |
