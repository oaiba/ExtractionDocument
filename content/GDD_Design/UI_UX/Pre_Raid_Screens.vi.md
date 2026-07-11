---
title: "Pre-Raid màn hình"
type: docs
weight: 4
---

## Mục Đích

Pre-raid màn hình convert preparation into commitment. They must communicate selected rules, map risk, squad readiness, gear giá trị, insurance status, và matchmaking trạng thái trước the người chơi loses control.

Tham chiếu chính:

| hệ thống | source |
| :--- | :--- |
| Matchmaking | [Matchmaking & Lobby hệ thống](../gameplay/matchmaking_lobby/index.html) |
| Loadout | [Loadout Preparation](../gamedesign/loadoutpreparation/index.html) |
| Modes | [Game Modes Design](../gamedesign/gamemodes/index.html) |
| Maps | [Map Design](../gamedesign/mapdesign/index.html) |
| Insurance | [Insurance hệ thống Design](../gamedesign/insurancesystem/index.html) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Full UI/UX documentation hub |
| [màn hình Groups Overview](screen_groups_overview/index.html) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](global_ux_standards/index.html) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [Out-of-Raid màn hình](out_of_raid_screens/index.html) | Loadout, stash, quests, traders, safe house |
| [In-Raid màn hình](in_raid_screens/index.html) | HUD, tactical map, looting, pause, reconnect |
| [loading màn hình Design](loadingscreen_design/index.html) | L4 lobby-to-match loading và reconnect transitions |

---

## Inventory Màn Hình

| màn hình | mục tiêu | primary CTA | Critical trạng thái |
| :--- | :--- | :--- | :--- |
| Mode Select | Choose raid rules và squad size | Select Mode | locked, ranked restrictions, event modifier |
| Map Select | Choose điểm đến và understand extracts/difficulty | Select Map | locked map, high risk, unavailable region |
| Deploy Confirmation | Summarize risk trước queue | Deploy | invalid loadout, high uninsured giá trị, squad not ready |
| Squad Lobby | Coordinate party readiness | Ready / Deploy | member not ready, missing kit, voice muted, leader only |
| Matchmaking | Communicate queue progress và cancel rules | Cancel Queue | match found, timeout, server error, party changed |
| Match Found | Final accept hoặc countdown | Accept / Deploying | người chơi declined, party member failed, reconnecting |

---

## Mode Select

Layout (PC/Console)

```
+------------------------------------------------------------------+
| < Back                         MODE SELECT                       |
|------------------------------------------------------------------|
| +----------------+ +----------------+ +----------------+         |
| | SOLO           | | DUO            | | SQUAD          |         |
| | Mixed lobbies  | | 2 players      | | 3-4 players    |         |
| | Low comms risk | | Team bonus     | | High reward    |         |
| | [SELECTED]     | | [SELECT]       | | [SELECT]       |         |
| +----------------+ +----------------+ +----------------+         |
| +----------------+ +----------------+                            |
| | RANKED         | | EVENT RAID     | Rules, losses, rewards     |
| | Locked Lv15    | | Modifier active| shown for selected card    |
| +----------------+ +----------------+                            |
+------------------------------------------------------------------+
```

| Spec | yêu cầu |
| :--- | :--- |
| User intent | Pick the ruleset that matches desired risk, squad size, và reward |
| Entry points | Home deploy card, Loadout mission tab, event deep link |
| Layout | Mode cards với rules, losses, rewards, matchmaking pool, và availability |
| primary CTA | Select Mode |
| secondary actions | View rules, compare rewards, toggle squad fill, view ranked restrictions |
| Accessibility | Rule changes phải được text labels, not only badges hoặc colors |

### Mode trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| available | Normal card với reward/risk summary |
| Locked | Show yêu cầu và unlock path |
| Event | Show modifier badge và expiry thời gian |
| Ranked | Show rank impact, party restrictions, và locked settings |
| disabled | Explain server, region, hoặc maintenance reason |

---

## Map Select

Layout (PC/Console)

```
+------------------------------------------------------------------+
| < Back                         MAP SELECT              [Ready]   |
|------------------------------------------------------------------|
| MAP LIST            | MAP PREVIEW / INTEL              | DETAILS |
| [Selected] Sector 7 | +------------------------------+ | Hard    |
| District 14         | | Industrial map art           | | 8-12    |
| Firebase Delta      | | Extract markers + landmarks  | | Boss 1  |
| [Locked] The Mire   | +------------------------------+ | Night v |
|                     | Extracts: Crossroads, Boat       | Quest 2 |
|                     | Queue estimate: 45s              | Squad 1 |
|------------------------------------------------------------------|
| [Show Quests] [Compare Risk] [Change Time] [READY]               |
+------------------------------------------------------------------+
```

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Make điểm đến choice dễ đọc: difficulty, extracts, người chơi count, thời gian of day, quest relevance |
| Layout | PC/Console landscape standard: map list left, preview/map art center, extracts và squad context right |
| primary CTA | Select Map / Ready |
| secondary actions | preview extracts, show quests, change thời gian of day, compare difficulty |

### Required Map Fields

| Field | mục đích |
| :--- | :--- |
| Difficulty | Sets expectation for combat và survival |
| người chơi count | Communicates PvP density |
| Boss / high-giá trị target | Flags high-risk opportunities |
| Extraction rules | Prevents surprise loss conditions |
| Quest relevance | giúp choose useful điểm đến |
| thời gian of day | Communicates visibility và AI behavior changes |
| Queue estimate | Sets wait expectation trước commit |

---

## Deploy Confirmation

Deploy confirmation is the final trust checkpoint. It nên được quick for valid kits và explicit for risky kits.

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         DEPLOY CONFIRMATION                      |
|------------------------------------------------------------------|
| Mission: Solo / Sector 7 / Night       Queue estimate: 45s       |
| Squad: You READY                       Fill: Off                 |
|------------------------------------------------------------------|
| Gear value: 125,000        Weight: 24 / 40kg        Ammo: OK     |
| Insurance: 4 insured / 2 uninsured eligible                      |
| Quests: Supply Run, Lab Rat                                      |
| Warnings: [!] High uninsured value                               |
|------------------------------------------------------------------|
| [Back to Loadout]        [Insure All]        [HOLD TO DEPLOY]    |
+------------------------------------------------------------------+
```

| Field | yêu cầu |
| :--- | :--- |
| Selected mode và map | Always hiển thị rõ |
| Squad size và fill | Always hiển thị rõ |
| Gear giá trị | Always hiển thị rõ |
| Insurance | Show insured, uninsured, và ineligible counts |
| Quest suggestions | Show top 1-3 relevant objectives |
| Loadout blockers | Inline, actionable, và focusable |
| Queue estimate | Update trước matchmaking starts |

### Confirmation Rules

| Condition | Behavior |
| :--- | :--- |
| Valid normal kit | Single Deploy CTA |
| Missing vũ khí | Block; focus missing slot |
| Missing đạn | Warn; allow explicit confirmation only nếu design permits |
| Overweight | Block; offer quick stash filter |
| High giá trị | Confirm risk với gear giá trị shown |
| Uninsured eligible items | offer Insure All hoặc Deploy Uninsured |
| Ranked mode | Show rank impact và locked settings summary |

---

## Squad Lobby

Layout (PC/Console)

```
+------------------------------------------------------------------+
| < Back                         SQUAD LOBBY       [Invite] [Leave]|
|------------------------------------------------------------------|
| +----------------+ +----------------+ +----------------+         |
| | You Leader     | | Player2        | | Empty Slot     |         |
| | READY          | | NOT READY      | | [Invite]       |         |
| | Value 125K     | | Missing meds   | | [Match Fill]   |         |
| | Voice OK       | | Voice muted    | |                |         |
| +----------------+ +----------------+ +----------------+         |
| Mission: Sector 7 / Night / Squad                                |
| Chat [__________________________] [Send]  Voice: Squad ON        |
|------------------------------------------------------------------|
| [Change Map] [Change Loadout]        [DEPLOY LOCKED: P2 blocker] |
+------------------------------------------------------------------+
```

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Let squads coordinate readiness mà không hiding blockers |
| Layout | người chơi cards, selected mission, voice/chat, readiness, leader controls |
| primary CTA | Ready for member; Deploy for leader khi all ready |
| secondary actions | Invite, kiểm tra loadout summary, change map, change loadout, leave |
| Destructive actions | Kick, leave party, cancel matchmaking require confirmation depending context |

### Squad Card Fields

| Field | mục đích |
| :--- | :--- |
| người chơi name và platform | Identity và cross-play clarity |
| Operator và role | Team composition |
| Ready trạng thái | Blocking status |
| Loadout cảnh báo | Shows why deploy is blocked |
| Voice status | Confirms communication readiness |
| Gear giá trị range | Communicates risk mà không exposing exact inventory chi tiết |

### Squad trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| empty slot | Invite, match fill, hoặc close slot |
| Member not ready | Show reason nếu shared by hệ thống |
| Leader only action | disabled for members với reason |
| Voice muted | Badge và settings shortcut |
| Party mismatch | Explain platform, ranked, hoặc level restriction |

---

## Matchmaking

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         MATCHMAKING                              |
|------------------------------------------------------------------|
| Sector 7 / Solo / Night                                          |
| Searching... 00:42                         Region: SEA  Ping 38  |
| [======================----------]                               |
|                                                                  |
| Squad: Kai READY                                                 |
| Estimated wait: 45s       Search range: Normal                   |
| Tip: Heavy bags make heavy noise.                                |
|------------------------------------------------------------------|
| [Cancel Queue]                         Status: can cancel        |
+------------------------------------------------------------------+
```

#### trạng thái Diagram

```
Searching -> Expanding Search -> Match Found -> L4 Loading -> In Raid
     |              |                |
     v              v                v
 Cancelled      Server Error     Player Declined
```

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                           MATCH FOUND                            |
|------------------------------------------------------------------|
| Sector 7 / Night / Squad                                         |
| Accept countdown: 00:12                                          |
|                                                                  |
| You        [ACCEPTED]                                            |
| Player2    [PENDING]                                             |
| Player3    [ACCEPTED]                                            |
|                                                                  |
| Loadout locked. Cancelling now returns to Squad Lobby.           |
|------------------------------------------------------------------|
| [Decline]                                      [Accept]          |
+------------------------------------------------------------------+
```

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Make waiting understandable và cancellable where rules allow |
| Layout | Selected mission summary, squad status, queue timer, region/ping, tips |
| primary CTA | Cancel Queue until match lock |
| secondary actions | Voice/chat, kiểm tra mission rules, settings shortcut |
| loading link | Uses `LT_LobbyToMatch` khi match begins; Xem [loading màn hình Design](loadingscreen_design/index.html) |

### Matchmaking trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Searching | Queue thời gian, estimate, region, squad cards |
| Expanding search | Explain MMR/region expansion nếu used |
| Match found | Countdown và readiness lock |
| người chơi declined | Return to lobby với explanation |
| Server error | Retry, change region, hoặc cancel |
| Cancel locked | Explain why cancellation is disabled sau match allocation |

---

## Platform Input Mapping

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Change tab | Click / number keys | LB/RB | Swipe hoặc tab row |
| Ready toggle | Click / Space | A / Cross | Tap CTA |
| Hold deploy | Hold mouse / chính | Hold A / Cross | Hold CTA với accessible tap alternative |
| Invite | Click Invite | Y / Triangle | Tap Invite |
| Open chat | Enter | Focus chat / virtual keyboard | Chat button |
| Cancel queue | ESC / click | B / Circle | Cancel button với confirm |

---

## Designer-Ready màn hình Specs

The sections below are the canonical low-level handoff for pre-raid layout work. Summary tables above remain useful for navigation, nhưng interaction, trạng thái, và visual yêu cầu nên được taken from these màn hình-level specs.

### Mode Select

**người chơi Intent**

Choose the ruleset that matches desired risk, squad size, reward, và thời gian commitment trước any gear is put at risk.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| < Back                              MODE SELECT                  Rules [i]     |
|--------------------------------------------------------------------------------|
| MODE CARDS                                                                     |
| +----------------+ +----------------+ +----------------+ +----------------+    |
| | SOLO           | | DUO            | | SQUAD          | | RANKED         |    |
| | 1 player       | | 2 players      | | 3-4 players    | | Lv15 required  |    |
| | Loss: Normal   | | Shared extracts| | High reward    | | Rank impact    |    |
| | [SELECTED]     | | [SELECT]       | | [SELECT]       | | LOCKED         |    |
| +----------------+ +----------------+ +----------------+ +----------------+    |
|--------------------------------------------------------------------------------|
| DETAIL: Solo | Risk Low | PvP Medium | Insurance Allowed | Queue 45s           |
| Rules: no revive, no shared quest progress, normal extraction rules            |
|--------------------------------------------------------------------------------|
| [Compare Rewards] [View Rules]                                      [SELECT]   |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Mode cards | Show squad size, loss rule, reward/risk summary, queue pool, selected/locked trạng thái |
| chi tiết panel | Explain selected mode rule changes trước CTA |
| Action bar | Keep Select Mode stable; compare và rules are secondary |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Selected mode | rõ by border, label, và chi tiết panel title |
| 2 | Rule/loss differences | Text labels required; never color-only badges |
| 3 | Locked/restricted modes | Show exact yêu cầu và route to unlock |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Mode card | mode name, party size, risk, loss rule, reward modifier, queue estimate |
| Ranked card | rank impact, party restrictions, locked settings, unlock yêu cầu |
| Event card | modifier, expiry, special extraction/loss changes |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| available | Select CTA active và chi tiết panel populated |
| Locked | CTA disabled; yêu cầu và unlock path hiển thị rõ |
| Event active | Badge includes thời gian remaining và rule modifier |
| disabled | Explain maintenance, region, hoặc server pool issue |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse modes | Click card / arrows | D-pad grid | Horizontal card swipe |
| View rules | Click info | Focus + Y / Triangle | Tap info chip |
| Select | Click CTA / Enter | A / Cross | Sticky CTA |

**Designer ghi chú**

- Cards phải được comparable trong một nhịp nhìn; keep fields aligned.
- Do not hide loss rules in tooltips.
- Locked cards stay hiển thị rõ so người chơi understand progression.

**Acceptance checklist**

- [ ] Every mode shows squad size, loss rule, risk/reward, và queue expectation.
- [ ] Locked và disabled modes explain the exact reason.
- [ ] Selected trạng thái is hiển thị rõ mà không relying on color.

### Map Select

**người chơi Intent**

Pick a điểm đến while understanding difficulty, extracts, người chơi density, quest relevance, thời gian of day, và queue impact.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| < Back                               MAP SELECT                       [Ready]  |
|--------------------------------------------------------------------------------|
| MAP LIST            | MAP PREVIEW / INTEL                       | DETAILS      |
| > Sector 7          | +---------------------------------------+ | Difficulty H |
|   District 14       | | map art, extracts, landmarks          | | Players 8-12 |
|   Firebase Delta    | | selected quest zone highlights        | | Boss: 1      |
|   The Mire LOCKED   | | danger zones and extracts             | | Time: Night v|
|---------------------| +---------------------------------------+ | Extracts 3   |
| Region Best Ping    | Extracts: Crossroads, Boat, Elevator      | Quests: 2    |
| Quest Relevant Only | Queue estimate: 45s                       | [SELECT MAP] |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Map list | Shows selected, locked, quest-relevant, event-modified, và unavailable maps |
| preview | Uses map art/intel với extract markers, quest highlights, và risk zones |
| chi tiết panel | Fixed summary: difficulty, người chơi count, boss, thời gian, extracts, quests, queue |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Selected map và Select/Ready CTA | Always hiển thị rõ |
| 2 | Extraction và risk rules | Must appear trước commit |
| 3 | Quest relevance | Highlight useful maps mà không hiding others |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Map row | name, difficulty, availability, quest badge, event badge |
| Extract marker | name, rule type, availability, special yêu cầu |
| thời gian selector | communicates visibility, AI, và queue differences |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Locked map | Show unlock source và preview permission |
| unavailable region | Disable CTA và explain server/latency reason |
| High risk | Warn nhưng allow selection unless mode blocks it |
| Quest mismatch | Show no relevant quests và a route to Quest Board |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse maps | Click list / arrows | D-pad list | Swipe list |
| kiểm tra extract | Hover/click marker | Focus marker | Tap marker |
| Change thời gian | Dropdown | Focus selector | Bottom sheet |

**Designer ghi chú**

- Extract names và rules phải được text-dễ đọc; marker icons are not enough.
- Keep map preview inspectable mà không becoming a tactical map replacement.

**Acceptance checklist**

- [ ] Difficulty, extracts, người chơi count, thời gian of day, quests, và queue estimate are hiển thị rõ.
- [ ] Locked/unavailable maps provide a rõ reason.

### Deploy Confirmation

**người chơi Intent**

Make one final informed commitment sau seeing mode, map, squad, loadout blockers, gear giá trị, insurance, quests, và queue estimate.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
|                                DEPLOY CONFIRMATION                             |
|--------------------------------------------------------------------------------|
| MISSION: Solo / Sector 7 / Night            Queue estimate: 45s                |
| SQUAD: You READY                            Fill: Off                          |
|--------------------------------------------------------------------------------|
| Gear value 125,000 | Weight 24/40kg | Ammo OK | Insurance 4/6 insured          |
| Quests: Supply Run, Lab Rat                                                    |
| WARNING: [!] 2 eligible items uninsured. [Insure All] [Review Items]           |
|--------------------------------------------------------------------------------|
| [Back to Loadout]                    [Insure All]             [HOLD TO DEPLOY] |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Mission summary | mode, map, thời gian, queue, squad/fill |
| Loadout risk | gear giá trị, weight, đạn, insurance, quests |
| cảnh báo lane | blockers và cảnh báo với direct fixes |
| CTA row | back, fix/insure, hold-to-deploy |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Hold to Deploy | Only primary khi no blockers exist |
| 2 | Blocking cảnh báo | Must sit directly above CTA row |
| 3 | Gear giá trị và insurance | Always hiển thị rõ for risk trust |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Hold CTA | Requires hold hoặc equivalent accessible confirmation |
| cảnh báo chip | Severity, item count, direct route |
| Quest summary | Top 1-3 relevant quests với extraction/FIR cảnh báo nếu needed |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Valid kit | Single hold-to-deploy action |
| Missing vũ khí | Block và focus vũ khí slot |
| Missing đạn | Warn hoặc block per tuning với đạn filter action |
| Overweight | Block và route to loadout removal |
| High giá trị | Require explicit risk acknowledgement |
| Ranked | Show rank impact và locked settings |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Deploy | Hold click / keyboard hold | Hold A / Cross | Hold sticky CTA |
| Fix blocker | Click cảnh báo | Focus cảnh báo + A | Tap cảnh báo |
| Back | Esc / click | B / Circle | Back button |

**Designer ghi chú**

- This màn hình is a trust checkpoint, not a dashboard.
- disabled deploy must name the exact first blocker.

**Acceptance checklist**

- [ ] Deploy never hides gear giá trị, insurance, mode, map, và squad status.
- [ ] Every blocker has a cách sửa trực tiếp action.

### Squad Lobby

**người chơi Intent**

Coordinate readiness, identify teammate blockers, manage invites, và let the leader deploy only khi the party is valid.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| < Back                              SQUAD LOBBY              [Invite] [Leave]  |
|--------------------------------------------------------------------------------|
| +----------------+ +----------------+ +----------------+ +----------------+    |
| | You Leader     | | Player2        | | Empty Slot     | | Match Fill Off |    |
| | READY          | | NOT READY      | | [Invite]       | | Toggle         |    |
| | Sonar / Recon  | | Missing meds   | |                | |                |    |
| | Voice OK       | | Voice muted    | |                | |                |    |
| +----------------+ +----------------+ +----------------+ +----------------+    |
| Mission: Sector 7 / Night / Squad        Chat [______________________] [Send]  |
| WARNING: Deploy locked because Player2 has a blocker.                          |
|--------------------------------------------------------------------------------|
| [Change Map] [Change Loadout] [Voice Settings]              [DEPLOY LOCKED]    |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| người chơi cards | identity, role, ready, blocker, voice, platform |
| Mission strip | selected map/mode/thời gian và leader controls |
| Communication | chat và voice status mà không burying readiness |
| Action bar | invite, change map/loadout, deploy/ready |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Ready/blocker trạng thái | rõ per member |
| 2 | Leader deploy lock reason | Directly tied to CTA |
| 3 | Voice/chat | secondary nhưng hiển thị rõ |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Member card | người chơi name, platform, operator, role, readiness, blocker reason |
| empty slot | invite, match fill, close slot nếu supported |
| Leader controls | hiển thị rõ nhưng disabled for non-leaders với reason |
| Voice trạng thái | muted/disconnected/push-to-talk labels |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Member not ready | Show reason nếu hệ thống knows it |
| Party mismatch | Explain platform, level, ranked, hoặc region restriction |
| Leader only action | disabled for members với text reason |
| Invite pending | Slot shows recipient và timeout/cancel |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Focus member | Click card | D-pad cards | Tap card |
| Invite | Click Invite | Focus empty slot | Invite sheet |
| Ready | Click CTA | A / Cross | Sticky CTA |

**Designer ghi chú**

- Squad readiness should read as operational status cards, not social profile cards.
- Do not expose exact teammate inventory; cách dùng blocker summaries.

**Acceptance checklist**

- [ ] Leader và member views both show correct disabled trạng thái.
- [ ] Member blockers explain deploy lock.

### Matchmaking / Match Found

**người chơi Intent**

Understand queue progress, cancel rules, match found countdown, và reconnect/decline outcomes mà không mơ hồ.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
|                                MATCHMAKING                                     |
|--------------------------------------------------------------------------------|
| Searching Sector 7 / Solo / Night                                              |
| [====================        ] 45s elapsed     Estimate 70s                    |
| Server region: Best Ping  Squad: 1/1  Loadout locked                           |
| Status: Finding compatible raid                                                |
|--------------------------------------------------------------------------------|
| MATCH FOUND: Accept within 15s                                                 |
| You: Accepted | Player2: Waiting | Player3: Declined                           |
|--------------------------------------------------------------------------------|
| [Cancel Queue]                                            [ACCEPT / DEPLOYING] |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Queue status | selected mission, elapsed, estimate, region, party trạng thái |
| Progress message | truthful hiện tại phase, not fake precision |
| Match found panel | countdown, accept trạng thái, failure outcome |
| Action bar | cancel trước lock; accept khi found |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | hiện tại queue/match trạng thái | Large status text |
| 2 | Countdown/cancel consequence | Always hiển thị rõ |
| 3 | Party accept status | hiển thị rõ trong khi match found |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Progress indicator | Can be indeterminate; must name hiện tại phase |
| Cancel CTA | disabled sau deployment lock với reason |
| Accept panel | Per-người chơi accept status và timeout |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Searching | Show elapsed, estimate, và cancel |
| Timeout | Explain no match và offer retry/change region |
| Server error | Show retry và support code |
| Match found | Show accept countdown và party statuses |
| người chơi declined | Explain return path và whether queue restarts |
| Reconnecting | Show preserved slot và timeout |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Cancel | Click / Esc confirm | B / Circle confirm | Cancel button |
| Accept | Click / Enter | A / Cross | Large CTA |
| View chi tiết | Click mission | Focus mission | Tap mission |

**Designer ghi chú**

- Avoid fake progress percentages; cách dùng phase labels và elapsed thời gian.
- Cancel copy must trạng thái nếu gear is still safe.

**Acceptance checklist**

- [ ] Searching, timeout, error, match found, declined, và reconnecting trạng thái are covered.
- [ ] người chơi always knows whether cancel is safe.

---

## Production State Matrix

| Screen | Loading / Pending | Disabled / Locked | Invalid / Error | Offline / Reconnect | Success |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Mode Select | mode cards skeleton, rule chips delayed | ranked/event locked với visible requirement | unavailable mode nêu service reason | offline chỉ cho training nếu cached | selected mode persist sang map step |
| Map Select | thumbnails và loot/weather placeholders | map locked bởi level/quest/event | missing map data có retry | region outage disable affected maps | selected map summary đi tiếp |
| Deploy Confirmation | loadout validation pending | deploy disabled với first blocker focused | missing weapon/ammo/durability/insurance warning | reconnecting squad member state shown | deploy starts matchmaking |
| Squad Lobby | member cards pending | ready disabled cho invalid member state | invite fail, privacy block, party mismatch | disconnected member grace timer | all ready hoặc leader deploy partial nếu allowed |
| Matchmaking / Match Found | queue timer, phase, region | cancel disabled chỉ trong final lock | timeout, declined, server reserve fail | reconnect/resume route visible | match locks và chuyển loading |

## Platform Behavior And Input

| Platform | Rule |
| :--- | :--- |
| PC | Mouse jump giữa cards; keyboard focus order theo mode -> map -> loadout blockers -> primary CTA. |
| Console | Shoulder tabs đổi major step; D-pad/left stick move card focus; destructive/cancel actions cần confirmation. |
| Mobile | Single-column stepper, bottom pinned CTA, long tables collapse thành expandable rows, blockers scroll into view. |

## Analytics Funnel

| Event | Required Properties |
| :--- | :--- |
| `pre_raid_screen_viewed` | screen, mode, platform, party_size |
| `pre_raid_primary_cta_selected` | screen, cta, selected_mode, selected_map |
| `pre_raid_blocker_shown` | blocker_type, slot, severity, resolved |
| `matchmaking_started` | mode, map, region, party_size, fill_enabled |
| `match_found_result` | accepted, declined, timeout, server_error, reconnect |

## Pre-Raid QA Checklist

- Mọi disabled Deploy/Ready state nêu blocker và direct next action.
- Console focus không bao giờ land đầu tiên trên cancel/leave/destructive actions.
- Mobile layout giữ selected mode, queue status, và primary CTA visible không horizontal scroll.
- Offline/reconnect states không silently discard selected loadout hoặc squad state.

## Analytics

| Metric | cách dùng |
| :--- | :--- |
| Mode select conversion | Identify confusing rules hoặc reward tuning |
| Map select dwell thời gian | Detect unreadable map risk |
| Deploy blocked reason | Improve validation và defaults |
| Queue cancel reason | Tune matchmaking estimates |
| Squad not-ready duration | Improve readiness visibility |
| Match found decline rate | Detect queue mismatch hoặc unclear commitment |

---

## checklist Nghiệm Thu

- [ ] Mode và map rules are hiển thị rõ trước queue.
- [ ] Deploy cannot be blocked mà không an actionable reason.
- [ ] Squad lobby clearly shows who is blocking deploy và why.
- [ ] Matchmaking communicates cancel availability và queue trạng thái.
- [ ] Mobile has a persistent selected mission summary.
- [ ] Ranked/event restrictions are explained trước commitment.
