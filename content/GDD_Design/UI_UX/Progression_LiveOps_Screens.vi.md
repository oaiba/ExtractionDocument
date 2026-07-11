---
title: "Progression & LiveOps màn hình"
type: docs
weight: 8
---

## Mục Đích

Progression và LiveOps màn hình surface long-term goals mà không disrupting the raid loop. They should make rewards, season timing, ranked stakes, và daily activity rõ while keeping gameplay advantage và monetization trust protected.

Tham chiếu chính:

| hệ thống | source |
| :--- | :--- |
| Progression | [Progression & Monetization](../gamedesign/progression/index.html) |
| LiveOps | [Live Operations & Events](../gamedesign/liveops/index.html) |
| Ranked | [Ranked Mode & Competitive hệ thống](../gamedesign/rankedmode/index.html) |
| Economy | [Economy & Monetization Design](../gamedesign/economy/index.html) |
| Quest hệ thống | [Quest & Objective hệ thống](../gameplay/quest_objective_system/index.html) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Full UI/UX documentation hub |
| [màn hình Groups Overview](screen_groups_overview/index.html) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](global_ux_standards/index.html) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [Out-of-Raid màn hình](out_of_raid_screens/index.html) | Quest board, profile, home hub, và reward routes |
| [Pre-Raid màn hình](pre_raid_screens/index.html) | Event/ranked queue commitment và restrictions |
| [Commerce màn hình](commerce_screens/index.html) | Battle pass upgrade, event store purchase routes, currency top-up, confirmation, và receipts |
| [Settings & hệ thống màn hình](commerce_settings_system_screens/index.html) | Privacy, account, và hệ thống dialogs |

---

## Inventory Màn Hình

| màn hình | mục tiêu | primary CTA | chính trạng thái |
| :--- | :--- | :--- | :--- |
| Battle Pass | Show seasonal tier progress và claimable rewards | claim / upgrade | free, premium, unclaimed, season ended |
| Event Hub | Explain active events và objectives | Track Event | inactive, ending soon, reward ready |
| Daily / Weekly Tasks | Encourage short-term goals | Track / claim | completed, expired, rerolled |
| Reward Inbox | Collect grants, compensation, event rewards | claim | empty, expired soon, stash full |
| Ranked Overview | Explain rank, stakes, restrictions, rewards | Queue Ranked / View Rules | placement, locked, demotion risk |
| Leaderboards | Compare competitive hoặc event standings | View người chơi / Filter | not ranked, privacy hidden |
| Season Summary | Show season timing và reset rules | View Rewards | preseason, active, ending, archived |
| Patch ghi chú / News | Explain game changes và deep link to content | Open chi tiết | dismissed, updated, mandatory |

---

## Battle Pass

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Make seasonal progression và claimable rewards dễ đọc mà không implying pay-to-win |
| Layout | Tier track, selected reward chi tiết, hiện tại XP, thời gian remaining, free/premium distinction |
| primary CTA | claim Reward; upgrade Pass only khi a premium reward is selected hoặc trang context supports it |
| secondary actions | View all rewards, kiểm tra cosmetic, filter claimable, preview season |
| Monetization rule | Reward/progress context lives here; premium upgrade purchase và confirmation live in [Commerce màn hình](commerce_screens/index.html) |

### Battle Pass trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Free người chơi | Free track highlighted; premium locked với upgrade info |
| Premium người chơi | Both tracks hiển thị rõ; claimable premium rewards active |
| Reward claimable | Badge on tier và global nav notification |
| Season ended | claim grace period shown; progression disabled |
| Stash full | Non-cosmetic reward goes to inbox hoặc blocks với explanation |

---

## Event Hub

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Convert temporary content into rõ actions và rewards |
| Layout | Active event banner, objective cards, reward ladder, timer, rules/modifiers |
| primary CTA | Track Event hoặc Play Event |
| secondary actions | View lore, claim rewards, kiểm tra modifiers, patch ghi chú |
| Deep links | Event cards open exact map, mode, quest, trader, hoặc reward trạng thái |

### Event trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Active | Objectives và rewards hiển thị rõ |
| Ending soon | Timer và unclaimed rewards emphasized |
| Inactive | Archive hoặc "next event" placeholder |
| Locked | Show level/tutorial yêu cầu |
| Reward ready | claim CTA và inbox fallback |

---

## Daily và Weekly Tasks

Layout (PC/Console)

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

| Field | yêu cầu |
| :--- | :--- |
| Objective | rõ action, location, và progress |
| thời gian remaining | Always hiển thị rõ |
| Reward | XP, currency, items, rep, hoặc cosmetic |
| Track action | Pins to Home, HUD objective tracker, hoặc map |
| Reroll | Shows chi phí, limit, và changed categories trước confirm |

Expired tasks không được silently disappear nếu a reward was claimable; move claimable rewards to inbox hoặc show final claim trạng thái based on LiveOps policy.

---

## Reward Inbox

Layout (PC/Console)

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

| trạng thái | Behavior |
| :--- | :--- |
| empty | Explain where rewards appear và offer event/quest links |
| Claimable | Show source, expiry, item/currency, và điểm đến |
| Expiring soon | Sort to top và badge global nav |
| Stash full | offer overflow rules, stash link, hoặc partial claim nếu supported |
| Claimed | Confirm kết quả và allow undo only nếu the economy supports it |

---

## Ranked Overview

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Explain competitive status, yêu cầu, party rules, và rank consequences |
| primary CTA | Queue Ranked nếu eligible |
| secondary actions | View rules, rewards, leaderboard, match history |
| Locked trạng thái | Show unlock yêu cầu và progress |
| Integrity | Explain settings/input locks và party restrictions plainly |

### Ranked trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Placement | Show matches remaining và provisional messaging |
| Active rank | Show rank, points, next threshold, protection |
| Demotion risk | Warn trước queue với rank impact |
| Party ineligible | Show which member/rule blocks queue |
| Season ending | Show reset date và reward eligibility |

---

## Leaderboards

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| Layout | Rank list, filters, người chơi row, friend/clan tabs, reward thresholds |
| Privacy | Respect hidden profiles và streamer mode |
| Filters | Region, platform, input, season, event, friends, clan |
| empty trạng thái | Explain no qualifying matches hoặc hidden data |

Leaderboards must avoid implying exact hidden MMR nếu the ranked design does not expose it.

---

## Patch ghi chú và News

Layout (PC/Console)

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

Layout (PC/Console)

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

| Rule | yêu cầu |
| :--- | :--- |
| One primary news item | Home không nên become an ad wall |
| Dismissal | Dismissed item stays dismissed until content changes |
| Mandatory updates | hệ thống modal only for required version/security issues |
| Deep links | Patch entries link to relevant settings, event, map, hoặc known issue |
| Readability | cách dùng summary first, chi tiết ghi chú second |

---

## Progression / LiveOps Information Architecture

Progression và LiveOps navigation phải tách rõ long-term progress, temporary events, competitive status, và reward claims nhưng vẫn giữ deep link có đường quay lại. Player đi vào từ Home, AAR, Quest Board, Battle Pass, Event Hub, News, hoặc Reward Inbox luôn phải hiểu họ đến từ đâu và next playable action là gì.

| Destination | Owns | Entry Points | Exit / Return Behavior |
| :--- | :--- | :--- | :--- |
| Battle Pass | Season tier progress, free/premium rewards, claimable tiers | Home notification, Season Summary, Reward Inbox, Commerce upgrade return | Quay về màn trước hoặc mở Commerce chỉ cho upgrade/checkout |
| Event Hub | Event rules, objectives, reward ladder, playable route | Home event strip, News, Map Select, Tasks, Reward Inbox | Quay lại exact event route hoặc mở playable map/mode |
| Daily / Weekly Tasks | Short-term objectives, tracking, reset, reroll | Home, Quest Board, AAR, HUD tracker | Track objective tới Home/HUD/map; claim route tới Inbox nếu blocked |
| Reward Inbox | Grants, compensation, overflow, claim-all leftovers | Global notification, AAR, Battle Pass, Event Hub, support grant | Quay về source screen hoặc destination inventory/profile |
| Ranked Overview | Competitive rules, eligibility, season reward, queue | Home, Mode Select, Leaderboards, Season Summary | Chỉ queue ranked khi mọi blocker pass |
| Leaderboards | Competitive/event comparison và privacy-safe profiles | Ranked Overview, Event Hub, Profile | Giữ filters khi quay lại |
| Season Summary | Season timing, reset, retained rewards, archive | Home, News, Battle Pass, Ranked | Link tới claimable rewards, recap, archive |
| Patch Notes / News | Live communication, known issues, deep links | Home, mandatory update, settings/help | Chỉ dismiss khi noncritical; deep links show disabled reason nếu unavailable |

## Reward Claim Model

Mọi reward UI dùng cùng claim vocabulary để player không phải học rule riêng cho battle pass, events, tasks, compensation, và ranked rewards.

| Claim State | Meaning | Required UI Behavior |
| :--- | :--- | :--- |
| Locked | Requirement chưa đạt | Show exact requirement, progress, và route |
| Earned | Player qualify nhưng reward chưa claim | Promote Claim và show destination |
| Claimed | Reward delivered | Mark complete và remove duplicate CTA |
| Blocked | Reward chưa deliver được | Name blocker: stash full, cap reached, offline, premium locked, account restriction |
| Overflow | Reward không fit destination | Preserve reward trong inbox và show required capacity/action |
| Expiring | Reward hoặc claim window sắp hết hạn | Sort/promote và show exact time remaining |
| Expired | Claim window ended | Show reward lost, converted, archived, hoặc support-eligible |
| Converted | Seasonal value đổi thành value khác | Show conversion amount và policy |
| Retroactive | Player qualify sau purchase, fix, hoặc rule change | Show source, grant reason, và support-safe reference |

## Season And Event State Model

| State | Battle Pass | Event Hub | Tasks | Reward Inbox | News / Summary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Preseason | Preview rewards/rules, no XP | Tease event nếu announced | Normal tasks | Normal grants | Season preview |
| Active | XP, claim, upgrade route active | Play/track/claim active | Track/claim active | Claim active | Featured live update |
| Ending soon | Exact timer, claim reminders | Timer và unclaimed rewards promoted | Reset warning | Expiring sort | Final push copy |
| Grace period | XP disabled, earned claim active | Play disabled, claim/conversion active | Expired tasks resolved | Earned claims preserved | Ended copy |
| Archived | Read-only recap | Read-only rules/rewards | Hidden hoặc history only | Claimed/history only | Archive/recap |
| Offline/cached | Show cached state và disable risky claims | Disable play/purchase links | Track local only if safe | Disable claim hoặc queue sync | Cached news with timestamp |

## Cross-Screen Deep Link Rules

| Source | Target | Rule |
| :--- | :--- | :--- |
| AAR reward row | Reward Inbox hoặc exact source screen | Preserve source context và show why reward claimable/blocked |
| Battle Pass upgrade CTA | Commerce Battle Pass Upgrade | Commerce owns purchase, confirmation, receipt, và return |
| Event store CTA | Commerce Event / Collection Store | Event Hub owns progress; Commerce owns purchase |
| Insufficient balance | Commerce Currency Top-Up | Return tới exact offer hoặc reward context sau checkout |
| Task track | Home, HUD tracker, map, hoặc Quest Board | Track state phải visible trên ít nhất một pre-raid và in-raid surface |
| Ranked reward | Ranked Overview hoặc Reward Inbox | Show season eligibility và reset timing trước claim |
| Patch note item | Affected setting, event, map, mode, hoặc known issue | Disable với reason nếu target unavailable hoặc offline |

---

## Designer-Ready màn hình Specs

Progression và LiveOps màn hình should tạo long-term motivation mà không burying the path back to raid. Rewards, expiry, premium/free status, và claim blockers must always be explicit.

### Battle Pass

**người chơi Intent**

Check seasonal progress, understand free/premium rewards, claim earned items, và see the fastest route to progress.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Season header | season name, thời gian remaining, level, XP, premium trạng thái |
| Reward track | free và premium lanes với earned/locked/claimed trạng thái |
| chi tiết panel | selected reward, source, claim trạng thái, preview |
| CTA area | claim, upgrade, view tasks |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Claimable reward | Strong label và CTA |
| 2 | Free vs premium | Text labels, not only color |
| 3 | Next level progress | Always hiển thị rõ |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Reward tile | level, free/premium, type, claimed/earned/locked |
| upgrade prompt | cosmetic/giá trị framing; never implies power advantage |
| claim CTA | checks inventory/stash capacity where relevant |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Claimable | Promote claim |
| Locked | Show required level và XP |
| Premium locked | Show premium yêu cầu mà không hiding free rewards |
| Season ending | Show exact remaining thời gian |
| Stash full | Block item claim và route to Reward Inbox/Stash |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse track | Wheel/drag | Bumpers/D-pad | Horizontal swipe |
| claim | Click | A / Cross | Tap CTA |
| preview | Hover/click | Focus tile | Tap tile |

**Designer ghi chú**

- Free rewards must never look like secondary leftovers.
- Avoid urgency language unless the expiry is real và hiển thị rõ.

**Acceptance checklist**

- [ ] Free, premium, claimable, locked, claimed, và stash-full trạng thái are rõ.

### Event Hub

**người chơi Intent**

Understand active event rules, objectives, rewards, expiry, và the exact playable route.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| EVENT HUB: Blackout Week                              Ends in 2d 14h [Play]    |
|--------------------------------------------------------------------------------|
| HERO / EVENT ART | Rules: Night raids, limited visibility, bonus tech loot     |
| Objectives: 2/5  | Rewards: Skin, credits, event token                         |
| Map: Sector 7    | Warnings: insurance normal, extracts modified               |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Event header | name, expiry, primary Play CTA |
| Rule panel | modifiers, restrictions, risk changes |
| Objective list | progress, rewards, tracked trạng thái |
| Route panel | mode/map/deep link |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Event rule changes | trước Play CTA |
| 2 | Expiry | Exact thời gian remaining |
| 3 | Rewards/objectives | rõ nhưng secondary to rules |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Event card | modifier, expiry, affected maps/modes |
| Objective row | count, condition, reward, track action |
| Play CTA | deep links to exact mode/map với rules applied |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Active | Play và track available |
| Expiring soon | thời gian label promoted |
| Completed | claim rewards và show replayable status |
| Locked | Show yêu cầu |
| Ended | Move to archive/claim grace nếu supported |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Track objective | Click | A / Cross | Tap |
| Play event | Click CTA | A / Cross | Sticky CTA |

**Designer ghi chú**

- Event hub must explain rule changes trước pushing người chơi to queue.

**Acceptance checklist**

- [ ] Event modifiers, expiry, objectives, rewards, và route are hiển thị rõ.

### Daily và Weekly Tasks

**người chơi Intent**

Pick achievable tasks, track progress, claim rewards, và understand reset windows.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| DAILY / WEEKLY TASKS                              Reset 03:14                  |
|--------------------------------------------------------------------------------|
| Daily: Loot 5 meds  3/5  Reward 500 XP [Track]                                 |
| Daily: Extract S7   Done Reward Credits [Claim]                                |
| Weekly: Win 5 raids 2/5 Reward Case [Track]                                    |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Reset header | daily/weekly timers |
| Task rows | objective, progress, reward, track/claim |
| chi tiết | map/mode hints và eligibility |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Claimable tasks | Promoted |
| 2 | Reset timer | Always hiển thị rõ |
| 3 | Progress count | Numeric và dễ đọc |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Task row | title, progress, reset, reward, route |
| claim CTA | checks reward capacity |
| Track action | pins objective to relevant màn hình |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| In progress | Track available |
| Complete | claim promoted |
| Expired | Move to expired/removed với explanation |
| Reward blocked | route to inbox/stash |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Track/claim | Click | A / Cross | Tap |
| Filter | Click tabs | Bumpers | Tabs |

**Designer ghi chú**

- Tasks should feel actionable, not like a checklist wall.

**Acceptance checklist**

- [ ] Reset, progress, claim, expired, và blocked reward trạng thái are covered.

### Reward Inbox

**người chơi Intent**

claim pending rewards safely while understanding expiry, source, capacity, và duplicate/overflow rules.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Inbox list | source, reward, expiry, trạng thái |
| chi tiết | selected reward contents và điểm đến |
| Capacity summary | stash/wallet limits |
| Actions | claim, claim all, route to stash |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Expiring rewards | Promoted |
| 2 | claim blockers | Exact reason |
| 3 | source | Traceable for trust |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Reward row | source, item, expiry, điểm đến, trạng thái |
| claim all | excludes blocked rewards và explains leftovers |
| Capacity cảnh báo | needed cells hoặc currency cap |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Claimable | claim active |
| Expiring soon | expiry label promoted |
| Stash full | block item claim và route to stash |
| Already claimed | remove hoặc show history |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| claim row | Click | A / Cross | Tap |
| claim all | Click | Y / Triangle | Button |

**Designer ghi chú**

- claim điểm đến phải được rõ trước the click.

**Acceptance checklist**

- [ ] Expiry, source, capacity, claim all, và blocked claim trạng thái are covered.

### Ranked Overview

**người chơi Intent**

Understand rank, progress, rules, restrictions, rewards, và consequences trước queueing ranked.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| RANKED OVERVIEW                         Silver II  340/500 RP [Queue Ranked]   |
|--------------------------------------------------------------------------------|
| Rank card | Placement/Promotion | Rules: squad restrictions, loss, MMR         |
| Requirements: Lv15, verified account, no penalty cooldown                      |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Rank card | hiện tại tier, RP, promotion/demotion |
| Rules | party restrictions, gear rules, penalties |
| Rewards | season rewards và milestones |
| Queue CTA | enabled only khi yêu cầu pass |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Queue eligibility | rõ pass/block |
| 2 | Rank progress | Numeric và visual |
| 3 | Consequences | hiển thị rõ trước queue |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| yêu cầu row | pass/fail label và fix route |
| RP bar | hiện tại, next, demotion threshold |
| Queue CTA | names first blocker khi disabled |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Eligible | Queue CTA active |
| Level locked | show level yêu cầu |
| Penalty cooldown | show exact timer |
| Party mismatch | show member blocker |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Queue | Click | A / Cross | Sticky CTA |
| kiểm tra rules | Click | Focus | Tap |

**Designer ghi chú**

- Ranked màn hình must trạng thái consequences trước queue.

**Acceptance checklist**

- [ ] Eligibility, cooldown, party mismatch, và rank progress trạng thái are covered.

### Leaderboards

**người chơi Intent**

Compare rank safely by season, region, friends, và platform while respecting privacy.

**Expanded ASCII Wireframe**

```
+-------------------------------------------------------------------------------+
| LEADERBOARDS                         Season v Region v Friends v              |
|-------------------------------------------------------------------------------|
| Rank | Player | Tier | Extract Rate | Raids | Privacy-safe profile action     |
+-------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Filters | season, region, friends/global, platform |
| Rows | rank, người chơi, tier, chính stat, profile |
| Self row | sticky/hiện tại người chơi highlight |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | người chơi's own position | Easy to find |
| 2 | Rank/tier | First columns |
| 3 | Privacy trạng thái | Hidden names respected |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Leaderboard row | rank, alias, tier, stats, privacy-safe action |
| Filter | rõ hiện tại scope |
| empty trạng thái | no data explanation |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Private/streamer | anonymize names |
| No ranking | explain placement yêu cầu |
| loading trang | skeleton rows |
| Filter empty | broaden filters action |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Filter | Click | Bumpers/focus | Filter sheet |
| Open profile | Click row | A / Cross | Tap row |

**Designer ghi chú**

- Do not reveal hidden identity thông qua profile links hoặc invite codes.

**Acceptance checklist**

- [ ] Privacy, empty, loading, và no-ranking trạng thái are covered.

### Patch ghi chú và News

**người chơi Intent**

See the one most quan trọng update, learn what changed, dismiss noncritical news, và deep link to relevant content.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| NEWS / PATCH NOTES                                                [Dismiss]    |
|--------------------------------------------------------------------------------|
| FEATURED: Blackout Week is live                  [Play Event] [Read Details]   |
| Patch 1.0.4: extraction timer tuning, stash sorting fixes, subtitles option    |
| [Known Issues] [Open Event Hub]                                                |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Featured item | one primary update |
| Patch summary | short bullets first |
| Actions | dismiss, read, deep link |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Required/featured update | One primary item |
| 2 | Dismiss và deep link | rõ |
| 3 | chi tiết ghi chú | secondary |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| News card | title, category, date, hành động chính |
| Patch row | version, summary, known issues |
| Dismiss | persists until content changes |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Mandatory update | hệ thống modal, not dismissible |
| Dismissed | stays hidden until changed |
| Offline | cached ghi chú hoặc unavailable message |
| Deep link unavailable | disable với reason |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Dismiss | Click | X / Square | Swipe/button |
| Open | Click | A / Cross | Tap |

**Designer ghi chú**

- News không được compete với Deploy as the main Home action.

**Acceptance checklist**

- [ ] Featured, dismissed, mandatory, offline, và deep-link unavailable trạng thái are covered.

---

## Analytics

| Metric | cách dùng |
| :--- | :--- |
| Battle pass viewed | Đo reach của season surface |
| Reward selected | Xác định reward clarity và preview interest |
| Reward claim attempted / succeeded / blocked | Tìm capacity, premium, expiry, và routing blockers |
| Battle pass upgrade CTA opened | Đảm bảo monetization prompt contextual và không quá áp lực |
| Event objective tracked | Đo event clarity và route usefulness |
| Event CTA used | Detect event có convert thành playable activity không |
| Event reward claimed | Tune reward visibility và completion pacing |
| Daily/weekly task tracked | Xác định objective relevance |
| Daily/weekly task claimed / expired / rerolled | Tune difficulty, reset timing, và anti-frustration |
| Reward inbox claim all leftovers | Reveal capacity hoặc duplicate grant confusion |
| Ranked queue eligibility failure | Improve restriction messaging |
| Leaderboard filter changed | Hiểu competitive comparison behavior |
| Season recap viewed | Đo season closure comprehension |
| News dismissal and click-through | Tune Home surface priority |

---

## Progression / LiveOps QA Checklist

- [ ] Battle Pass free, premium, claimable, locked, claimed, retroactive, season-ended, và grace-period states are visible.
- [ ] Battle Pass upgrade và tier-skip actions route tới Commerce cho purchase, confirmation, receipt, và return.
- [ ] Event Hub giải thích modifiers, expiry, objectives, deterministic rewards, event currency, và playable route trước queue.
- [ ] Event end behavior cover play disabled, claim grace, event currency conversion, archive, và owned rewards.
- [ ] Daily/weekly tasks show reset, reroll cost/limit, claimable-at-reset behavior, và objective route.
- [ ] Reward Inbox preserve blocked/overflow rewards và explain claim-all leftovers.
- [ ] Ranked Overview show eligibility, demotion risk, season reset, reward eligibility, và party blockers trước queue.
- [ ] Leaderboards respect privacy, platform/input filters, archived seasons, và reward thresholds.
- [ ] Patch Notes / News disable stale play/claim CTAs khi offline hoặc cached.
- [ ] All reward claims show source, destination, expiry, blocker, và support route khi cần.

---

## checklist Nghiệm Thu

- [ ] Premium, free, và gameplay-affecting rewards are clearly distinguished.
- [ ] Event và task cards deep link to exact playable context.
- [ ] Ranked màn hình show yêu cầu và consequences trước queue.
- [ ] Reward inbox handles stash-full và expiry trạng thái.
- [ ] News does not compete với deploy as the main Home action.
- [ ] Privacy settings are honored in leaderboards và profiles.
- [ ] Season reset, claim grace, reward conversion, và archive states are covered.
- [ ] Commerce purchase routes are linked without duplicating checkout UX.
