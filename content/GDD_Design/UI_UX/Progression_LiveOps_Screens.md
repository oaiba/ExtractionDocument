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

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |
| [Out-of-Raid Screens](Out_Of_Raid_Screens.md) | Quest board, profile, home hub, and reward routes |
| [Pre-Raid Screens](Pre_Raid_Screens.md) | Event/ranked queue commitment and restrictions |
| [Commerce, Settings & System Screens](Commerce_Settings_System_Screens.md) | Shop, wallet, purchase, privacy, and system dialogs |

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

## Designer-Ready Screen Specs

Progression and LiveOps screens should create long-term motivation without burying the path back to raid. Rewards, expiry, premium/free status, and claim blockers must always be explicit.

### Battle Pass

#### Player Intent

Check seasonal progress, understand free/premium rewards, claim earned items, and see the fastest route to progress.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| BATTLE PASS Season 1                         Level 12/50 XP 340/1000 [Upgrade] |
|--------------------------------------------------------------------------------|
| REWARD TRACK: 10  11  >12<  13  14  15                                         |
| Free:    [Claimed] [Ammo] [Title] [Locked] [Credits]                           |
| Premium: [Skin]    [Boost] [Frame] [Locked] [Case]                             |
|--------------------------------------------------------------------------------|
| SELECTED REWARD: Title | Free | Earned | [Claim] | Source: Daily/raid XP       |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Season header | season name, time remaining, level, XP, premium state |
| Reward track | free and premium lanes with earned/locked/claimed states |
| Detail panel | selected reward, source, claim state, preview |
| CTA area | claim, upgrade, view tasks |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Claimable reward | Strong label and CTA |
| 2 | Free vs premium | Text labels, not only color |
| 3 | Next level progress | Always visible |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Reward tile | level, free/premium, type, claimed/earned/locked |
| Upgrade prompt | cosmetic/value framing; never implies power advantage |
| Claim CTA | checks inventory/stash capacity where relevant |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Claimable | Promote Claim |
| Locked | Show required level and XP |
| Premium locked | Show premium requirement without hiding free rewards |
| Season ending | Show exact remaining time |
| Stash full | Block item claim and route to Reward Inbox/Stash |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse track | Wheel/drag | Bumpers/D-pad | Horizontal swipe |
| Claim | Click | A / Cross | Tap CTA |
| Preview | Hover/click | Focus tile | Tap tile |

#### Designer Notes

- Free rewards must never look like secondary leftovers.
- Avoid urgency language unless the expiry is real and visible.

#### Acceptance Checklist

- [ ] Free, premium, claimable, locked, claimed, and stash-full states are clear.

### Event Hub

#### Player Intent

Understand active event rules, objectives, rewards, expiry, and the exact playable route.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| EVENT HUB: Blackout Week                              Ends in 2d 14h [Play]    |
|--------------------------------------------------------------------------------|
| HERO / EVENT ART | Rules: Night raids, limited visibility, bonus tech loot     |
| Objectives: 2/5  | Rewards: Skin, credits, event token                         |
| Map: Sector 7    | Warnings: insurance normal, extracts modified               |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Event header | name, expiry, primary Play CTA |
| Rule panel | modifiers, restrictions, risk changes |
| Objective list | progress, rewards, tracked state |
| Route panel | mode/map/deep link |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Event rule changes | Before Play CTA |
| 2 | Expiry | Exact time remaining |
| 3 | Rewards/objectives | Clear but secondary to rules |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Event card | modifier, expiry, affected maps/modes |
| Objective row | count, condition, reward, track action |
| Play CTA | deep links to exact mode/map with rules applied |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Active | Play and track available |
| Expiring soon | Time label promoted |
| Completed | Claim rewards and show replayable status |
| Locked | Show requirement |
| Ended | Move to archive/claim grace if supported |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Track objective | Click | A / Cross | Tap |
| Play event | Click CTA | A / Cross | Sticky CTA |

#### Designer Notes

- Event hub must explain rule changes before pushing players to queue.

#### Acceptance Checklist

- [ ] Event modifiers, expiry, objectives, rewards, and route are visible.

### Daily And Weekly Tasks

#### Player Intent

Pick achievable tasks, track progress, claim rewards, and understand reset windows.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| DAILY / WEEKLY TASKS                              Reset 03:14                  |
|--------------------------------------------------------------------------------|
| Daily: Loot 5 meds  3/5  Reward 500 XP [Track]                                 |
| Daily: Extract S7   Done Reward Credits [Claim]                                |
| Weekly: Win 5 raids 2/5 Reward Case [Track]                                    |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Reset header | daily/weekly timers |
| Task rows | objective, progress, reward, track/claim |
| Detail | map/mode hints and eligibility |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Claimable tasks | Promoted |
| 2 | Reset timer | Always visible |
| 3 | Progress count | Numeric and readable |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Task row | title, progress, reset, reward, route |
| Claim CTA | checks reward capacity |
| Track action | pins objective to relevant screens |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| In progress | Track available |
| Complete | Claim promoted |
| Expired | Move to expired/removed with explanation |
| Reward blocked | route to inbox/stash |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Track/claim | Click | A / Cross | Tap |
| Filter | Click tabs | Bumpers | Tabs |

#### Designer Notes

- Tasks should feel actionable, not like a checklist wall.

#### Acceptance Checklist

- [ ] Reset, progress, claim, expired, and blocked reward states are covered.

### Reward Inbox

#### Player Intent

Claim pending rewards safely while understanding expiry, source, capacity, and duplicate/overflow rules.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| REWARD INBOX                                      Stash 190/200 [Claim All]    |
|--------------------------------------------------------------------------------|
| Source          Reward            Expires       State                          |
| Battle Pass     Frame             Never         Claim                          |
| Insurance       AK-74M            22h           Stash needs 4x2                |
| Event           Token x5          2d            Claim                          |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Inbox list | source, reward, expiry, state |
| Detail | selected reward contents and destination |
| Capacity summary | stash/wallet limits |
| Actions | claim, claim all, route to stash |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Expiring rewards | Promoted |
| 2 | Claim blockers | Exact reason |
| 3 | Source | Traceable for trust |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Reward row | source, item, expiry, destination, state |
| Claim all | excludes blocked rewards and explains leftovers |
| Capacity warning | needed cells or currency cap |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Claimable | Claim active |
| Expiring soon | expiry label promoted |
| Stash full | block item claim and route to stash |
| Already claimed | remove or show history |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Claim row | Click | A / Cross | Tap |
| Claim all | Click | Y / Triangle | Button |

#### Designer Notes

- Claim destination must be clear before the click.

#### Acceptance Checklist

- [ ] Expiry, source, capacity, claim all, and blocked claim states are covered.

### Ranked Overview

#### Player Intent

Understand rank, progress, rules, restrictions, rewards, and consequences before queueing ranked.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| RANKED OVERVIEW                         Silver II  340/500 RP [Queue Ranked]   |
|--------------------------------------------------------------------------------|
| Rank card | Placement/Promotion | Rules: squad restrictions, loss, MMR         |
| Requirements: Lv15, verified account, no penalty cooldown                      |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Rank card | current tier, RP, promotion/demotion |
| Rules | party restrictions, gear rules, penalties |
| Rewards | season rewards and milestones |
| Queue CTA | enabled only when requirements pass |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Queue eligibility | Clear pass/block |
| 2 | Rank progress | Numeric and visual |
| 3 | Consequences | Visible before queue |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Requirement row | pass/fail label and fix route |
| RP bar | current, next, demotion threshold |
| Queue CTA | names first blocker when disabled |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Eligible | Queue CTA active |
| Level locked | show level requirement |
| Penalty cooldown | show exact timer |
| Party mismatch | show member blocker |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Queue | Click | A / Cross | Sticky CTA |
| Inspect rules | Click | Focus | Tap |

#### Designer Notes

- Ranked screens must state consequences before queue.

#### Acceptance Checklist

- [ ] Eligibility, cooldown, party mismatch, and rank progress states are covered.

### Leaderboards

#### Player Intent

Compare rank safely by season, region, friends, and platform while respecting privacy.

#### Expanded ASCII Wireframe

```
+-------------------------------------------------------------------------------+
| LEADERBOARDS                         Season v Region v Friends v              |
|-------------------------------------------------------------------------------|
| Rank | Player | Tier | Extract Rate | Raids | Privacy-safe profile action     |
+-------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Filters | season, region, friends/global, platform |
| Rows | rank, player, tier, key stat, profile |
| Self row | sticky/current player highlight |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Player's own position | Easy to find |
| 2 | Rank/tier | First columns |
| 3 | Privacy state | Hidden names respected |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Leaderboard row | rank, alias, tier, stats, privacy-safe action |
| Filter | clear current scope |
| Empty state | no data explanation |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Private/streamer | anonymize names |
| No ranking | explain placement requirement |
| Loading page | skeleton rows |
| Filter empty | broaden filters action |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Filter | Click | Bumpers/focus | Filter sheet |
| Open profile | Click row | A / Cross | Tap row |

#### Designer Notes

- Do not reveal hidden identity through profile links or invite codes.

#### Acceptance Checklist

- [ ] Privacy, empty, loading, and no-ranking states are covered.

### Patch Notes And News

#### Player Intent

See the one most important update, learn what changed, dismiss noncritical news, and deep link to relevant content.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| NEWS / PATCH NOTES                                                [Dismiss]    |
|--------------------------------------------------------------------------------|
| FEATURED: Blackout Week is live                  [Play Event] [Read Details]   |
| Patch 1.0.4: extraction timer tuning, stash sorting fixes, subtitles option    |
| [Known Issues] [Open Event Hub]                                                |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Featured item | one primary update |
| Patch summary | short bullets first |
| Actions | dismiss, read, deep link |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Required/featured update | One primary item |
| 2 | Dismiss and deep link | Clear |
| 3 | Detailed notes | Secondary |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| News card | title, category, date, primary action |
| Patch row | version, summary, known issues |
| Dismiss | persists until content changes |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Mandatory update | system modal, not dismissible |
| Dismissed | stays hidden until changed |
| Offline | cached notes or unavailable message |
| Deep link unavailable | disable with reason |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Dismiss | Click | X / Square | Swipe/button |
| Open | Click | A / Cross | Tap |

#### Designer Notes

- News must not compete with Deploy as the main Home action.

#### Acceptance Checklist

- [ ] Featured, dismissed, mandatory, offline, and deep-link unavailable states are covered.

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
