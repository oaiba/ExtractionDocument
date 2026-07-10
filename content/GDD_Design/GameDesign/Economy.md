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

## Economy System Model

The economy model gives designers and engineers a shared vocabulary for value movement. Every reward, purchase, repair, insurance fee, event grant, and compensation package should map to one of these objects so UI copy and telemetry can explain the same truth.

| Entity | Definition | UI / Design Requirement |
| :--- | :--- | :--- |
| `Currency` | A countable value used for purchases, upgrades, claims, or event exchange | Always show name, amount, source, and whether it is earnable, premium, seasonal, or reputation-like |
| `Source` | A system that adds value to the player account or stash | Must explain why the player received value and where it landed |
| `Sink` | A system that removes value from the player account or stash | Must explain cost, consequence, and whether the spend is reversible |
| `Reward` | Any value granted by raid, quest, event, battle pass, compensation, or purchase | Must declare type, destination, claim state, expiry, and gameplay impact |
| `TraderPrice` | Price for gear, services, repairs, crafting inputs, or trade offers | Must show reputation requirement, stock state, and price change reason when dynamic |
| `RepairCost` | Cost to restore item durability or readiness | Must preview before commit and show before/after durability |
| `InsuranceCost` | Cost paid to protect a loadout item from permanent loss under insurance rules | Must show return chance/rule, return window, and blocked conditions |
| `EventCurrency` | Seasonal value earned during a limited window | Must show expiry, cap, conversion, and event store destination |
| `PremiumToken` | Premium currency bought or granted through non-power routes | Must never be required for combat certainty; purchase UX lives in Commerce |
| `InflationSignal` | Telemetry that indicates value growth is unhealthy | Must be segmented by account age, skill, mode, platform, and season phase |

## Currency Types

| Currency | Source | Sink | Can Be Bought? | Design Notes |
| :--- | :--- | :--- | :--- | :--- |
| Credits | Loot sales, quests, tasks, compensation, trader payouts | Gear, repair, insurance, crafting, Safe House upgrades, trader fees | No direct premium purchase | Core soft economy; cannot bypass mastery or reputation locks |
| Tokens | Premium purchase, battle pass grants, event grants, compensation | Cosmetics, battle pass, capped non-power convenience | Yes | Must not buy weapons, armor, stat advantage, protected combat slots, or matchmaking advantage |
| Reputation | Faction quests, event alignment, trader tasks | Trader unlocks, quest access, faction identity | No | Not a spendable power currency; losing reputation should be rare and explicit |
| Event Currency | Limited-time events and seasonal objectives | Event cosmetics, deterministic rewards, event collection progress | Event-defined | Expires or converts by policy; never silently disappears if reward was claimable |

## Sources And Sinks Matrix

| Value Source | Grants | Required Context | Primary Sink / Follow-Up |
| :--- | :--- | :--- | :--- |
| Extracted loot | Items, credits after sale, crafting inputs | Found-in-raid state, rarity, trader value | Sell, equip, craft, quest turn-in, stash |
| Quest reward | Credits, XP, reputation, items, unlocks | Quest source, completion reason, claim state | Progression tracks, traders, loadout recovery |
| Daily / weekly task | XP, credits, items, rep, battle pass XP | Reset timer, progress, reward destination | Short-term return loop |
| Event objective | Event currency, cosmetics, XP, credits | Event name, expiry, conversion policy | Event store, reward ladder, inbox |
| Battle pass free track | Cosmetics, currency, materials | Tier, free/premium lane, claim state | Identity, progression, light economy support |
| Battle pass premium track | Cosmetics, premium tokens, non-power boosts | Premium state, Commerce upgrade route | Identity and seasonal value |
| Compensation grant | Items, credits, tokens, inbox entries | Reason, affected window, support reference | Recovery and trust repair |
| Gear purchase | Gear item | Trader, stock, reputation, price | Raid loadout and risk |
| Repair / insurance | Restored durability or protected item | Item state, cost, rules, timer | Loss mitigation |
| Crafting / Safe House | Crafted items, module upgrades | Inputs, time, unlock requirement | Long-term sinks and planning |
| Cosmetic purchase | Cosmetic entitlement | Offer, ownership, confirmation, receipt | Commerce-owned purchase UX |

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

## Inflation / Poverty / Hoarding Guardrails

| Risk | Trigger Signal | Guardrail |
| :--- | :--- | :--- |
| New-player bankruptcy | New accounts cannot afford a basic kit after repeated failed raids | Increase tutorial/recovery rewards, surface budget presets, reduce early repair pressure |
| Veteran hoarding | High-account-age players hold excessive credits/items with low sink usage | Add prestige cosmetics, crafting sinks, Safe House goals, or limited non-power vanity sinks |
| High-tier saturation | Too many raids contain top-tier kits compared with extraction risk | Tune trader stock, repair cost, insurance return, rarity, and high-tier loot spawn |
| Event currency flood | Event currency outpaces event store demand or conversion policy | Add caps, deterministic sinks, conversion limits, and clear end-of-event messaging |
| Compensation abuse | Repeated grants create farming incentives or market distortion | Use targeted grants, account eligibility windows, and support-auditable receipt IDs |
| Market manipulation | Price volatility exceeds normal scarcity patterns | Apply listing fees, price bands, trade limits, provenance checks, and suspicious trade detection |

## Economy Tuning Inputs

| Input | Why It Matters | Review Cadence |
| :--- | :--- | :--- |
| Extraction rate | Defines how often raid value survives | Daily during launch, weekly once stable |
| Average raid value | Shows whether risk produces meaningful reward | Weekly by map/mode/skill |
| Average kit cost | Measures whether normal play is affordable | Weekly by account age and rank |
| Repair cost ratio | Indicates whether durability feels fair or punitive | Weekly after balance patches |
| Insurance use and return rate | Shows whether loss mitigation is trusted or too strong | Weekly by item tier |
| Stash pressure | Reveals hoarding, confusion, or insufficient item sinks | Weekly by account age |
| Trader unlock pace | Validates reputation and quest economy pacing | Per season and major quest update |
| Premium token earn rate | Protects perceived fairness around premium currency grants | Per season and event |
| Event currency earn/spend ratio | Prevents event store under-demand or impossible completion | Daily during active events |

## Gear Value And Item Sinks

Physical gear value is created and removed through play. Gear enters through raids, traders, crafting, quests, events, and compensation; it leaves through death, sale, crafting, repair loss, quest turn-in, discard, and wipe/reset rules. Commerce may sell cosmetic entitlements or non-power services, but it does not create paid combat-power item instances.

| Gear Economy Concept | Requirement |
| :--- | :--- |
| Gear value | UI should explain value through combat role, durability, weight, rarity/tier, repair cost, insurance cost, and trader/quest relevance |
| Item sink | Sell, repair, craft, quest turn-in, discard, death loss, and durability degradation must be visible and auditable |
| Premium boundary | Premium purchases may unlock cosmetics or capped convenience, not weapons, armor, ammo, stat power, or protected combat slots |
| Contraband/restricted gear | Restricted sale, trade, insurance, or deploy behavior must show a readable reason |

## Ethical Monetization Rules

| Promise | Implementation |
| :--- | :--- |
| Spend to express identity | Cosmetics, banners, skins, emotes |
| Spend to save time carefully | Convenience must be earnable and capped |
| Never sell power | No paid stat advantage |
| Be clear about value | Show contents, duration, and refund rules |
| Protect minors | Spending controls and platform compliance |

## Economy QA Checklist

- [ ] No paid product grants weapons, armor, stats, protected combat slots, visibility advantage, recoil advantage, or matchmaking advantage.
- [ ] Credits cannot bypass mastery, reputation, tutorial gates, ranked eligibility, or quest knowledge checks.
- [ ] Event rewards do not flood core market supply or make normal raid rewards feel irrelevant.
- [ ] Premium tokens are used only for cosmetics, battle pass, and capped non-power convenience.
- [ ] Every source explains why value was granted and where it landed.
- [ ] Every sink previews cost, consequence, and blocked state before commit.
- [ ] New-player recovery exists without making failure more profitable than success.
- [ ] Veteran sinks create aspiration without forcing unhealthy grind.
- [ ] Compensation grants are auditable and do not encourage repeated retry/spam behavior.
- [ ] UI text distinguishes earned, premium, seasonal, reputation, claimable, expired, and converted value.

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
| Inventory item lifecycle | [Inventory System](../Inventory_System/) |
| Gear tier and rarity | [Gear Tier System](../Gears/Gear_Tier_System.md) |
