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

| State | Behavior |
| :--- | :--- |
| Empty | Explain where rewards appear and offer event/quest links |
| Claimable | Show source, expiry, item/currency, and destination |
| Expiring soon | Sort to top and badge global nav |
| Stash full | Offer overflow rules, stash link, or partial claim if supported |
| Claimed | Confirm result and allow undo only if the economy supports it |

---

## Ranked Overview

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

| Spec | Requirement |
| :--- | :--- |
| Layout | Rank list, filters, player row, friend/clan tabs, reward thresholds |
| Privacy | Respect hidden profiles and streamer mode |
| Filters | Region, platform, input, season, event, friends, clan |
| Empty state | Explain no qualifying matches or hidden data |

Leaderboards must avoid implying exact hidden MMR if the ranked design does not expose it.

---

## Patch Notes And News

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
