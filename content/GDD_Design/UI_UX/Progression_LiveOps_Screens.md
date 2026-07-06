---
title: "Progression & LiveOps Screens"
type: docs
weight: 8
---

## Purpose

Progression and LiveOps screens surface long-term goals without disrupting the raid loop. They should make rewards, season timing, ranked stakes, and daily activity clear while keeping gameplay advantage and monetization trust protected.

Primary references:

| System | Source |
| :--- | :--- |
| Progression | [Progression & Monetization](../GameDesign/Progression.md) |
| LiveOps | [Live Operations & Events](../GameDesign/LiveOps.md) |
| Ranked | [Ranked Mode & Competitive Systems](../GameDesign/RankedMode.md) |
| Economy | [Economy & Monetization Design](../GameDesign/Economy.md) |
| Quest system | [Quest & Objective System](../Gameplay/Quest_Objective_System.md) |

---

## Screen Inventory

| Screen | Goal | Primary CTA | Key States |
| :--- | :--- | :--- | :--- |
| Battle Pass | Show seasonal tier progress and claimable rewards | Claim / Upgrade | free, premium, unclaimed, season ended |
| Event Hub | Explain active events and objectives | Track Event | inactive, ending soon, reward ready |
| Daily / Weekly Tasks | Encourage short-term goals | Track / Claim | completed, expired, rerolled |
| Reward Inbox | Collect grants, compensation, event rewards | Claim | empty, expired soon, stash full |
| Ranked Overview | Explain rank, stakes, restrictions, rewards | Queue Ranked / View Rules | placement, locked, demotion risk |
| Leaderboards | Compare competitive or event standings | View Player / Filter | not ranked, privacy hidden |
| Season Summary | Show season timing and reset rules | View Rewards | preseason, active, ending, archived |
| Patch Notes / News | Explain game changes and deep link to content | Open Details | dismissed, updated, mandatory |

---

## Battle Pass

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| SEASON 1: SHADOWS OF PROMETHEUS              Time left 47 days   |
|------------------------------------------------------------------|
| Current Tier 12 / 50     XP 2,400 / 5,000                        |
| [10] [11] [12 YOU] [13] [14] [15] [16] ... [50 LEGEND]           |
|------------------------------------------------------------------|
| SELECTED TIER 12                  | PREVIEW / CLAIM              |
| Free: Title "Zone Runner"         | [Cosmetic Preview]           |
| Premium: Operator Skin "Ghost"    | Owned pass: No               |
|                                   | [Claim Free] [Upgrade Pass]  |
|------------------------------------------------------------------|
| [Filter Claimable] [View All Rewards] [Season Rules]             |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Make seasonal progression and claimable rewards readable without implying pay-to-win |
| Layout | Tier track, selected reward detail, current XP, time remaining, free/premium distinction |
| Primary CTA | Claim Reward; Upgrade Pass only when a premium reward is selected or page context supports it |
| Secondary actions | View all rewards, inspect cosmetic, filter claimable, preview season |
| Monetization rule | Premium purchase must clearly state cosmetic/non-power nature |

### Battle Pass States

| State | Behavior |
| :--- | :--- |
| Free player | Free track highlighted; premium locked with upgrade info |
| Premium player | Both tracks visible; claimable premium rewards active |
| Reward claimable | Badge on tier and global nav notification |
| Season ended | Claim grace period shown; progression disabled |
| Stash full | Non-cosmetic reward goes to inbox or blocks with explanation |

---

## Event Hub

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| EVENT HUB: BLACKOUT WEEK                         Ends in 3d 12h  |
|------------------------------------------------------------------|
| EVENT BANNER / ART                                               |
|------------------------------------------------------------------|
| OBJECTIVES                         | REWARD LADDER               |
| [ ] Extract from Sector 7 at night | 1: Banner                   |
| [x] Loot 3 power cells             | 2: 5,000 credits [CLAIM]    |
| [ ] Survive without flashlight     | 3: Skin                     |
|------------------------------------------------------------------|
| Modifier: Reduced lights, more AI patrols   [Track Event] [Play] |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Convert temporary content into clear actions and rewards |
| Layout | Active event banner, objective cards, reward ladder, timer, rules/modifiers |
| Primary CTA | Track Event or Play Event |
| Secondary actions | View lore, claim rewards, inspect modifiers, patch notes |
| Deep links | Event cards open exact map, mode, quest, trader, or reward state |

### Event States

| State | Behavior |
| :--- | :--- |
| Active | Objectives and rewards visible |
| Ending soon | Timer and unclaimed rewards emphasized |
| Inactive | Archive or "next event" placeholder |
| Locked | Show level/tutorial requirement |
| Reward ready | Claim CTA and inbox fallback |

---

## Daily And Weekly Tasks

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| DAILY / WEEKLY TASKS                         Reset in 08:14:22   |
|------------------------------------------------------------------|
| DAILY                              | WEEKLY                      |
| [x] Extract once       [Claim]     | [ ] Kill 20 AI      12/20   |
| [ ] Heal 300 HP        180/300     | [ ] Turn in tools    1/5    |
| [ ] Loot meds          2/5         | [x] Squad revive     Claim  |
|------------------------------------------------------------------|
| Selected: Heal 300 HP   Reward: 1,000 XP + Medkit                |
| [Track] [Reroll 2,000] [Show Suggested Map]                      |
+------------------------------------------------------------------+
```

| Field | Requirement |
| :--- | :--- |
| Objective | Clear action, location, and progress |
| Time remaining | Always visible |
| Reward | XP, currency, items, rep, or cosmetic |
| Track action | Pins to Home, HUD objective tracker, or map |
| Reroll | Shows cost, limit, and changed categories before confirm |

Expired tasks must not silently disappear if a reward was claimable; move claimable rewards to inbox or show final claim state based on LiveOps policy.

---

## Reward Inbox

#### Layout (PC/Console)

```
+-------------------------------------------------------------------+
| REWARD INBOX                                      Expiring first  |
|-------------------------------------------------------------------|
| SOURCE              REWARD                EXPIRES       ACTION    |
| Event Blackout      5,000 credits         3d            [Claim]   |
| Compensation        Medkit x3             12d           [Claim]   |
| Battle Pass         Banner                Never         [Claim]   |
|-------------------------------------------------------------------|
| Stash: 178 / 200       [Claim All] [Open Stash] [Inbox Rules]     |
+-------------------------------------------------------------------+
```

| State | Behavior |
| :--- | :--- |
| Empty | Explain where rewards appear and offer event/quest links |
| Claimable | Show source, expiry, item/currency, and destination |
| Expiring soon | Sort to top and badge global nav |
| Stash full | Offer overflow rules, stash link, or partial claim if supported |
| Claimed | Confirm result and allow undo only if the economy supports it |

---

## Ranked Overview

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| RANKED OVERVIEW                                  Season ends 21d |
|------------------------------------------------------------------|
| Rank: Silver II       Points: 1,420 / 1,600       Protection ON  |
| [========================----------------]                       |
|------------------------------------------------------------------|
| RULES / LOCKS                    | PARTY ELIGIBILITY             |
| FOV locked in ranked             | You: OK                       |
| Input matchmaking: Controller    | Player2: Rank gap [!]         |
| Friendly fire penalty active     |                               |
|------------------------------------------------------------------|
| [View Rewards] [Leaderboard]              [Queue Ranked Locked]  |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Explain competitive status, requirements, party rules, and rank consequences |
| Primary CTA | Queue Ranked if eligible |
| Secondary actions | View rules, rewards, leaderboard, match history |
| Locked state | Show unlock requirements and progress |
| Integrity | Explain settings/input locks and party restrictions plainly |

### Ranked States

| State | Behavior |
| :--- | :--- |
| Placement | Show matches remaining and provisional messaging |
| Active rank | Show rank, points, next threshold, protection |
| Demotion risk | Warn before queue with rank impact |
| Party ineligible | Show which member/rule blocks queue |
| Season ending | Show reset date and reward eligibility |

---

## Leaderboards

#### Layout (PC/Console)

```
+-------------------------------------------------------------------+
| LEADERBOARDS                       Season 1  Region SEA Friends v |
|-------------------------------------------------------------------|
| Rank   Player           Rating      Extract %     Platform        |
| 01     GhostLine        2,840       61%           PC              |
| 02     Mira             2,790       58%           Mobile          |
| 03     Kai              2,610       54%           PC              |
|-------------------------------------------------------------------|
| Your Rank: 124   Reward threshold: Top 500                        |
| [View Profile] [Filter] [Privacy Settings]                        |
+-------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Layout | Rank list, filters, player row, friend/clan tabs, reward thresholds |
| Privacy | Respect hidden profiles and streamer mode |
| Filters | Region, platform, input, season, event, friends, clan |
| Empty state | Explain no qualifying matches or hidden data |

Leaderboards must avoid implying exact hidden MMR if the ranked design does not expose it.

---

## Patch Notes And News

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| SEASON SUMMARY: SEASON 1                                         |
|------------------------------------------------------------------|
| Status: Active                         Ends in 21 days           |
| Rank reward eligibility: Silver II achieved                      |
| Battle Pass: Tier 12 / 50                                        |
| Unclaimed rewards: 3                                             |
| Reset policy: rank soft reset, cosmetics retained                |
|------------------------------------------------------------------|
| [View Rewards] [Claim Inbox] [Season Rules]                      |
+------------------------------------------------------------------+
```

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| NEWS / PATCH NOTES                                               |
|------------------------------------------------------------------|
| FEATURED: Blackout Week is live                                  |
| [Play Event] [Read Details]                                      |
|------------------------------------------------------------------|
| Patch 1.0.4                                                      |
| - Map extraction timer tuning                                    |
| - Fixed stash sorting edge cases                                 |
| - New accessibility subtitle option                              |
|------------------------------------------------------------------|
| [Dismiss] [Known Issues] [Open Event Hub]                        |
+------------------------------------------------------------------+
```

| Rule | Requirement |
| :--- | :--- |
| One primary news item | Home should not become an ad wall |
| Dismissal | Dismissed item stays dismissed until content changes |
| Mandatory updates | System modal only for required version/security issues |
| Deep links | Patch entries link to relevant settings, event, map, or known issue |
| Readability | Use summary first, detailed notes second |

---

## Analytics

| Metric | Use |
| :--- | :--- |
| Reward claim latency | Identify hidden rewards |
| Event objective tracking | Measure event clarity |
| Battle pass upgrade context | Ensure monetization prompts are not overbearing |
| Ranked queue eligibility failures | Improve restriction messaging |
| News dismissal and click-through | Tune Home surface priority |
| Daily task completion | Tune task difficulty and time windows |

---

## Acceptance Checklist

- [ ] Premium, free, and gameplay-affecting rewards are clearly distinguished.
- [ ] Event and task cards deep link to exact playable context.
- [ ] Ranked screens show requirements and consequences before queue.
- [ ] Reward inbox handles stash-full and expiry states.
- [ ] News does not compete with deploy as the main Home action.
- [ ] Privacy settings are honored in leaderboards and profiles.
