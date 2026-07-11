---
title: "Progression & Player Growth"
type: docs
---

## Overview

Progression owns the systems that make players return: account levels, operator mastery, faction reputation, quests, battle pass advancement, achievements, and long-term goals.

Progression should make every session feel like it moved the player forward, even when the raid was lost. Extraction creates spikes of reward, but account growth, operator learning, quests, reputation, and seasonal goals keep the player from feeling that one death erased the evening.

The system should avoid mandatory chores. Daily and weekly goals are guidance, not homework. The best progression path is the one that gives the player a reason to try a different route, operator, weapon class, or squad role while still respecting the extraction fantasy.

## Progression Layers

Progression layers should be readable from the Home Screen and post-match recap. A player should know which track advanced, why it advanced, and what the next meaningful unlock is. Hidden progress is useful for achievements, but core growth should be explicit.

| Source | Progression Track | Unlocks / Result |
| :--- | :--- | :--- |
| Raid actions | Account level | Systems, rewards, and broad player growth |
| Operator usage | Operator mastery | Identity rewards and role commitment |
| Faction quests | Faction reputation | Trader access and faction-specific tasks |
| Daily / weekly goals | Quest progress | Directed goals and regular return hooks |
| Seasonal challenges | Battle pass | Seasonal cosmetics and event rewards |

## Progression System Model

Progression is the long-term memory of player effort. Each progression object must explain what moved, why it moved, what unlocked, and whether the reward is claimable now or waiting behind a capacity, season, or premium-state rule.

| Entity | Definition | UI / Design Requirement |
| :--- | :--- | :--- |
| `AccountLevel` | Broad player familiarity and system access | Unlocks systems and rewards; never grants hidden combat stats |
| `XPEvent` | Atomic reason XP was earned | Must show source category, amount, cap status, and whether it was boosted |
| `OperatorMastery` | Identity progression for a specific operator | Rewards role commitment with cosmetics/profile treatment, not mandatory stat grind |
| `FactionReputation` | Trust and access track for factions/traders | Unlocks trader access, quest chains, and faction identity |
| `QuestProgress` | Objective completion across tutorial, daily, weekly, faction, story, seasonal, repeatable quests | Must show objective, progress count, reset/expiry, reward, and route |
| `BattlePassXP` | Seasonal XP feeding battle pass tiers | Comes from raids, quests, events, and catch-up missions; purchase route lives in Commerce |
| `SeasonTier` | A tier on a free/premium seasonal reward track | Must show free/premium lane, reward type, locked/earned/claimed state |
| `RewardClaim` | Claimable grant produced by progression, event, inbox, battle pass, or compensation | Must show source, destination, expiry, blockers, and overflow behavior |

## Progression Layer Spec

| Layer | Owns | Cannot Do | Primary UI Surfaces |
| :--- | :--- | :--- | :--- |
| Account level | System access, broad rewards, onboarding milestones | Add hidden health, damage, armor, aim, audio, or matchmaking advantage | Home, AAR, Profile, Tutorial gates |
| Operator mastery | Role identity, cosmetics, tips, profile treatment | Make one operator statistically mandatory through grind | Operator Select, Profile, AAR |
| Faction reputation | Trader access, quest chains, faction status | Sell reputation directly for premium currency | Quest Board, Traders, Profile |
| Quest system | Directed goals, map learning, repeatable motivation | Depend on repetitive chores that ignore extraction decisions | Quest Board, HUD tracker, AAR |
| Battle pass | Seasonal reward track and return goals | Become the core power spine or hide free value | Battle Pass, Reward Inbox, Commerce upgrade route |
| Achievements / prestige | Long-term mastery and bragging rights | Reset meaningful player access without consent | Profile, Season Summary |

Progression can unlock access, knowledge, cosmetic identity, trader stock, and quest chains, but it must not imply premium gear power. If a progression reward grants physical gear, it is treated as an earned item instance with normal durability, insurance, loss, stash, and lifecycle rules.

## Account Levels

Account levels represent broad familiarity with the game. They can unlock systems and rewards, but they should not create a permanent combat stat gap. A level 50 player can have more options and knowledge; they should not simply have more health, damage, or hidden power.

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

Operator mastery should reward commitment without creating mandatory stat grind.

Mastery is an identity track. It should encourage players to learn an operator's rhythm, voice, abilities, and preferred squad role. Rewards should make the operator feel more personal in the lobby and profile, while keeping combat balance controlled by match rules and equipment.

## Quest System

Quests are the designer's way of teaching the map without a tutorial pop-up. A good quest asks the player to visit a place, use a system, take a risk, or notice a piece of the world. It should avoid asking for repetitive grind that ignores extraction decisions.

| Quest Type | Reset | Purpose |
| :--- | :--- | :--- |
| Tutorial | One-time | Teach survival basics |
| Daily | 24 hours | Short-term goals and return habit |
| Weekly | 7 days | Medium goals and varied play |
| Faction | Persistent | World identity, reputation, and trader unlocks |
| Story | One-time chains | Narrative and directed exploration |
| Seasonal | Season-limited | Live Ops engagement and event identity |

## Battle Pass

The battle pass is a seasonal checklist, not the core progression spine. It should reward regular play across modes and provide catch-up paths for late-season players. Premium rewards should be desirable, but free-track rewards must prove that the season is not locked behind spending.

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
| Extraction and objectives matter most | Extraction, quest completion, squad support, and meaningful objective play should outweigh raw kill volume |
| Failed raids can still teach | Failed raids may grant limited account/operator/quest learning when the player made meaningful progress |
| Raw kill farming is capped | Repeated trivial AI kills, spawn camping, or low-risk loops hit diminishing returns |
| Catch-up respects early players | Catch-up accelerates late players without invalidating early-season participation or paid/free fairness |
| Boosts are non-power | XP boosts cannot create combat certainty and must disclose duration/source |
| Reward destination is explicit | Rewards state whether they go to stash, inbox, profile, currency balance, battle pass, trader, or claim screen |
| Claim blockers are named | Stash full, premium locked, expired, capped, duplicate, and offline states must show a direct next action |

## Reward Taxonomy

| Reward Type | Player-Facing? | Gameplay-Affecting? | Seasonal? | Claim Behavior |
| :--- | :--- | :--- | :--- | :--- |
| Cosmetic | Yes | No | Optional | Claim/equip/view; preview supported |
| Profile item | Yes | No | Optional | Claim to profile inventory |
| Credits | Yes | Economy-affecting, not power by itself | Optional | Add to balance or inbox if capped |
| Premium token grant | Yes | No combat power | Optional | Add to balance with source/receipt |
| Material / crafting input | Yes | Indirect economy value | Optional | Requires stash/capacity handling |
| Convenience unlock | Yes | Conditional non-power | Usually persistent | Must be earnable/capped and never combat certainty |
| Access unlock | Yes | System access, not stat power | Persistent | Shows requirement and unlocked destination |
| Title / badge | Yes | No | Optional | Profile destination |
| Account service | Yes | No | Persistent or limited | Must describe consequence and reversibility |

## Progression State Matrix

| State | Meaning | Required UI Behavior |
| :--- | :--- | :--- |
| Locked | Requirement not met | Show exact requirement, progress, and route |
| In progress | Player has partial progress | Show count, percentage, next step, and reset/expiry if any |
| Claimable | Reward is earned but not claimed | Promote claim action and show destination |
| Claimed | Reward already granted | Mark complete and avoid duplicate CTA |
| Expired | Time window ended | Explain what happened, whether claim grace exists, and whether value converted |
| Converted | Expired/seasonal value changed into another value | Show conversion amount and policy |
| Capped | Progress or reward hit a limit | Explain cap and when it resets |
| Overflow | Reward cannot fit destination | Route to inbox/stash/capacity fix and preserve reward |
| Retroactive grant | Player qualifies after purchase, fix, or rule change | Show source, receipt/support context, and claim destination |

## Retention Loops

Retention should come from confidence and aspiration, not fear of missing out alone. The player should return because they have a plan: finish a trader chain, master an operator, recover from a failed raid, push ranked, or unlock a cosmetic that reflects how they play.

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

A day-one player completes Operation Zero, extracts once, and unlocks a starter faction task. The goal is to convert tutorial confidence into a short real objective without overwhelming them with all systems at once.

A week-one player starts favoring one operator. Operator mastery rewards should recognize that identity through cosmetics, voice, profile treatment, and tips, while avoiding stat bonuses that make switching roles feel bad.

A seasonal player returns for an event. Battle pass, faction objectives, and live quests should point toward the same seasonal activity so progress feels coordinated rather than scattered across unrelated checklists.

## Tuning Notes

- XP should reward extraction and objective completion more reliably than raw kill volume.
- Catch-up should reduce late-season pressure without invalidating early participation.
- Quest chains should vary route, item, and behavior requirements to avoid grind fatigue.
- Prestige should be cosmetic-first until long-term balance is proven.

## Progression Analytics

| Signal | Use |
| :--- | :--- |
| XP source distribution | Detect kill farming, objective under-rewarding, or event over-rewarding |
| Quest abandon and reroll rate | Identify unclear, tedious, or poorly routed objectives |
| Reward claim latency | Reveal hidden claim surfaces or unclear reward destinations |
| Battle pass tier velocity | Tune season length, catch-up missions, and reward cadence |
| Catch-up use and completion | Check whether late-season support is helpful without becoming mandatory |
| Operator mastery concentration | Detect role imbalance or rewards that over-pull one operator |
| Faction reputation pace | Tune trader access and quest chain length |
| Overflow/blocked claim rate | Improve stash, inbox, or reward routing UX |

## Cross-References

| Topic | Page |
| :--- | :--- |
| Economy and monetization ethics | [Economy](economy/index.html) |
| Event cadence | [Live Operations](liveops/index.html) |
| Player stats and achievements | [Player Profile](playerprofile/index.html) |
| Tutorial goals | [Tutorial Raid](tutorialraid/index.html) |
| Clan missions | [Clan System](clansystem/index.html) |
| Inventory item lifecycle | [Inventory System](../Inventory_System/) |
| Gear tier and rarity rules | [Gear Tier System](../gears/gear_tier_system/index.html) |
