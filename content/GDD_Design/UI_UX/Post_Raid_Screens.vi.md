---
title: "Post-Raid màn hình"
type: docs
weight: 6
---

## Mục Đích

Post-raid màn hình convert raid outcome into learning, reward, recovery, và the next run. They must explain what happened, what changed, what was gained hoặc lost, và how Người chơi có thể act next.

Tham chiếu chính:

| hệ thống | source |
| :--- | :--- |
| Debrief | [Post-Game Debrief & Replay](../Gameplay/Post_Game_Debrief.md) |
| Extraction outcomes | [Extraction cơ chế](../Gameplay/Extraction_Mechanics.md) |
| Progression | [Progression & Monetization](../GameDesign/Progression.md) |
| Quest objectives | [Quest & Objective hệ thống](../Gameplay/Quest_Objective_System.md) |
| Fair play | [Anti-Cheat & Fair Play](../Gameplay/Anti_Cheat_Fair_Play.md) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [màn hình Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](Global_UX_Standards.md) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [In-Raid màn hình](In_Raid_Screens.md) | Raid overlays và reconnect trước results |
| [Out-of-Raid màn hình](Out_Of_Raid_Screens.md) | Stash, quests, profile, và recovery actions sau results |
| [Social màn hình](Social_Screens.md) | Commend, report, add friend, và squad continuation |

---

## Inventory Màn Hình

| màn hình | mục tiêu | primary CTA | Critical trạng thái |
| :--- | :--- | :--- | :--- |
| Outcome Transition | Bridge raid end into results | Continue | extracted, KIA, MIA, disconnected |
| sau Action Report | Explain rewards, losses, XP, stats, quests | Continue / Deploy Again | success, death, partial rewards, server issue |
| Death Replay | Teach cause of death | Watch / Skip | unavailable, saved clip, report |
| Loot Transfer | Confirm extracted items are stored | Continue to Stash | stash full, quest turn-in available |
| Quest Progress | Show objective changes | Track Next / Turn In | completed, failed, item lost |
| Squad Summary | Compare squad outcomes | Commend / Continue | solo, party stayed, member disconnected |
| Report / Commend | Positive và negative social actions | Submit | clip attached, category missing, cooldown |
| Redeploy flow | Return to next run với valid setup | Deploy Again | missing kit, preset rebuild, party not ready |

---

## sau Action Report

The AAR is the most quan trọng post-raid màn hình. It nên được calm, dễ đọc, và fast to exit.

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         EXTRACTION SUCCESSFUL                    |
| Sector 7 - Industrial Decay                  Duration 18:42      |
|------------------------------------------------------------------|
| LOOT ACQUIRED                    | XP BREAKDOWN                  |
| AK-74M (FIR)          45,000     | Kills        +450             |
| Armor Lv4             38,000     | Looting      +320             |
| Quest Data            QUEST      | Quest        +500             |
| Total Value           93,800     | Extraction   +200             |
|----------------------------------+-------------------------------|
| Quest: Supply Run completed | Combat: 5 kills, 34% accuracy  |
|------------------------------------------------------------------|
| [Continue to Stash] [Deploy Again] [View Replay] [Main Menu]     |
+------------------------------------------------------------------+
```

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                              KIA                                 |
| Sector 7 - Industrial Decay                  Survived 12:08      |
|------------------------------------------------------------------|
| Cause: Headshot by PlayerName - SVD                              |
| LOST ITEMS                       | KEPT / SECURE                 |
| AK-74M              -45,000      | Quest Key              SAFE   |
| Armor Lv4           -38,000      | Gold Chain             SAFE   |
| Backpack            -12,000      |                               |
|----------------------------------+-------------------------------|
| Insurance return ETA: 22h | Tip: Carry fast bleed treatment      |
|------------------------------------------------------------------|
| [Continue] [Death Replay] [Report Player] [Rebuild Preset]       |
+------------------------------------------------------------------+
```

| Section | yêu cầu |
| :--- | :--- |
| Outcome banner | kết quả, map, survival thời gian, cause |
| XP breakdown | Itemized sources trước total |
| Loot/losses | Extracted, lost, kept, insured, quest-tagged items |
| Combat stats | Kills, damage, accuracy, distance, healing, revives |
| Quest progress | Completed, advanced, failed, hoặc lost objectives |
| Squad summary | người chơi outcomes và social actions |
| Next actions | Deploy Again, Return to Stash, Watch Replay, Main Menu |

### AAR trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Extracted | Emphasize loot giá trị, XP, quest progress, và stash transfer |
| KIA | Emphasize cause of death, lost/kept items, insurance ETA, replay |
| MIA / timeout | Explain timer hoặc disconnect consequence |
| Server issue | Explain compensation hoặc pending reconciliation nếu applicable |
| Data delayed | Show partial report và "finalizing results" trạng thái |

### AAR Progression / Reward Rules

| Result Type | Required Behavior |
| :--- | :--- |
| XP gained | Show source breakdown và progression tracks nào advanced |
| Battle pass progress | Show tier/XP delta và claimable reward link, không purchase confirmation |
| Quest progress | Show advanced, completed, failed, lost-item, và ready-to-turn-in states |
| Event objective progress | Show event name, objective count, event currency, và Event Hub route |
| Reward claimable | Route tới Reward Inbox hoặc exact source screen, preserve source context |
| Reward blocked | Name blocker: stash full, cap reached, offline, premium locked, duplicate, hoặc expired |
| Server reconciliation | Dùng pending/finalizing state và tránh duplicate reward claim CTAs |

---

## Death Replay

Layout (PC/Console)

```
+------------------------------------------------------------------+
| DEATH REPLAY                                      [Skip] [Save]  |
|------------------------------------------------------------------|
|                                                                  |
|                  [SERVER REPLAY VIEW 10s + 3s]                   |
|                                                                  |
|------------------------------------------------------------------|
| -10s     -7s      -4s       -1s       DEATH       +2s reveal     |
| |--------|--------|---------|---------|X----------|              |
| Hit arm     Suppressed        Headshot by SVD                    |
|------------------------------------------------------------------|
| [Report Player] [Watch Again] [Continue to AAR]                  |
+------------------------------------------------------------------+
```

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | giúp the người chơi understand why they died mà không exposing unfair live intel |
| Entry points | AAR replay button, death transition nếu auto-play is enabled |
| primary CTA | Watch / Skip |
| secondary actions | Save clip, report người chơi, scrub timeline |
| unavailable trạng thái | MIA, server crash, no death event, expired replay |

### Replay UI

| Element | Behavior |
| :--- | :--- |
| Timeline | Shows hit events, death moment, và reveal window |
| Cause label | vũ khí, hit location, attacker type; no địch inventory |
| Camera | Standard top-down hoặc server-approved replay view |
| Report shortcut | Pre-fills match và killer context |
| Save clip | Shows storage limit và confirmation |

---

## Loot Transfer

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         LOOT TRANSFER COMPLETE                   |
|------------------------------------------------------------------|
| Extracted items are already in stash.                            |
|                                                                  |
| NEW IN STASH                    | ACTIONS                        |
| AK-74M                 45,000   | [Open Stash]                   |
| Armor Lv4              38,000   | [Turn In Quest Item]           |
| Prometheus Data        QUEST    | [Sell Junk]                    |
|                                                                  |
| Stash Capacity: 178 / 200       Insurance scheduled: 2 items     |
|------------------------------------------------------------------|
| [Continue]                                      [Deploy Again]   |
+------------------------------------------------------------------+
```

| trạng thái | Behavior |
| :--- | :--- |
| Normal transfer | Items already moved to stash; show NEW tags |
| Stash full | Show overflow inbox, auto-sort, sell, hoặc upgrade path |
| Quest turn-in available | Highlight quest item và deep link to trader/quest |
| Insurance scheduled | Show provider và ETA |
| Secure container | Separate kept items from extracted items |

Loot transfer must never make the người chơi wonder whether items were saved. The first line should trạng thái the kết quả plainly.

---

## Quest Progress

Layout (PC/Console)

```
+------------------------------------------------------------------+
| QUEST PROGRESS                                                   |
|------------------------------------------------------------------|
| Supply Run                         COMPLETED                     |
| [x] Find rations 3/3                                             |
| [x] Extract alive                                                |
| [ ] Turn in to Salvage trader                                    |
|                                                                  |
| Lab Rat                            ITEM LOST                     |
| [x] Find document                                                |
| [!] Deliver item - item lost on death                            |
|------------------------------------------------------------------|
| [Track Next] [Turn In Available] [Find Replacement]              |
+------------------------------------------------------------------+
```

| kết quả | UI Behavior |
| :--- | :--- |
| Completed | Show reward preview và Turn In nếu required |
| Advanced | Show old và new progress |
| failed | Explain failure condition và retry availability |
| Item lost | Identify lost objective item và where to reacquire |
| New quest unlocked | Show unlock reason và faction |

---

## Squad Summary và Social Actions

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         SQUAD SUMMARY                            |
|------------------------------------------------------------------|
| Player      Outcome     Kills     Loot       XP       Actions    |
| You         Extracted   5         93K        1700     -          |
| Player2     Extracted   1         44K        950      [Commend]  |
| Player3     KIA         3         0          600      [Add]      |
|------------------------------------------------------------------|
| Commend category: [Good Teammate v]     [Submit Commendation]    |
| Report: select player -> category -> evidence -> submit          |
+------------------------------------------------------------------+
```

| Action | yêu cầu |
| :--- | :--- |
| Commend | One commendation per eligible teammate; categories are rõ và positive |
| Add friend | available for recent squad và encounter rules where allowed |
| Report | Category required; optional text và clip attach |
| Stay với squad | Keeps party together và routes to lobby/home |
| Leave party | Confirmation nếu party is still queued hoặc regrouping |

### Report flow

| Step | UI yêu cầu |
| :--- | :--- |
| Select người chơi | From squad summary, death replay, hoặc kill context |
| Select category | Cheating, abusive voice/text, griefing, exploit, name, other |
| Add evidence | Optional text và clip nếu available |
| Submit | Confirmation toast; no punishment chi tiết |
| Cooldown | Prevent spam và explain nếu report is rate-limited |

---

## Redeploy flow

#### trạng thái Diagram

```
AAR Continue
     |
     v
Valid same kit? ---- yes ----> [Deploy Again]
     |
     no
     v
[Rebuild Preset] -> [Fix Loadout] -> [Squad Ready] -> [Queue]
     |
     v
[Return to Stash]
```

| trạng thái | Behavior |
| :--- | :--- |
| Valid same kit | Deploy Again is primary |
| Missing lost gear | offer rebuild from preset, budget kit, hoặc stash |
| Squad not ready | Route to Squad Lobby và show blockers |
| Quest completed | Suggest turn-in trước redeploy, nhưng do not block unless required |
| Inventory full | Suggest stash management trước redeploy |

---

## Platform Layout

| Platform | Layout |
| :--- | :--- |
| PC / Console | Tabbed AAR với Summary, Loot, XP, Stats, Replay, Squad |
| Mobile | Scroll summary với sticky bottom CTA và tabs for Loot, Stats, Replay |
| Console | Large focusable cards; no dense tables mà không row focus |
| Tablet | Two-column summary plus chi tiết panel |

---

## Designer-Ready màn hình Specs

Post-raid màn hình must explain outcome, preserve người chơi trust, và route quickly back to stash, recovery, squad, hoặc redeploy. Summary tables above are navigation; the specs below own layout và trạng thái chi tiết.

### sau Action Report

**người chơi Intent**

Understand raid kết quả, rewards, losses, performance, và the next best action.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| AFTER ACTION REPORT                         Result: EXTRACTED       [Continue] |
|--------------------------------------------------------------------------------|
| OUTCOME CARD        | XP / STATS                         | NEXT ACTIONS        |
| Extracted           | XP +1,700 | Kills 4 | Loot 7       | [Move Loot]         |
| Sector 7 / 31m      | Survival 31m | Damage 620          | [Turn In Quest]     |
| Insurance safe      | Quest progress: Supply Run +3/3   | [Deploy Again]       |
|--------------------------------------------------------------------------------|
| Tabs: Summary | Loot | XP | Stats | Replay | Squad                             |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Outcome card | kết quả, map, duration, survival/death reason, insurance/loss summary |
| Stat panel | XP, kills, damage, survival, quest deltas |
| Next actions | move loot, turn in quest, rebuild, deploy again |
| Tabs | deeper chi tiết mà không hiding primary outcome |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Outcome và next action | hiển thị rõ immediately |
| 2 | Gains/losses | Plain totals với deltas |
| 3 | chi tiết stats | secondary tabs |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| kết quả badge | extracted, KIA, MIA, disconnected, run-thông qua với text |
| XP breakdown | source rows và total |
| Next action card | one primary route based on kết quả |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Extraction | Move Loot và Deploy Again promoted |
| Death | Rebuild và Death Replay promoted |
| MIA/disconnect | Explain gear consequence |
| Data delayed | Show pending stats và safe next route |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch tab | Click | Bumpers | Tab row |
| Continue | Enter/click | A / Cross | Sticky CTA |
| View chi tiết | Click row | Focus row | Tap card |

**Designer ghi chú**

- The first màn hình should answer: what happened, what changed, what now.
- Do not force người chơi thông qua every tab trước continuing.

**Acceptance checklist**

- [ ] kết quả, gains, losses, và next action are hiển thị rõ above the fold.
- [ ] Delayed stat trạng thái does not block safe continuation.

### Death Replay

**người chơi Intent**

Understand how they died, learn the counterplay, và optionally report suspicious behavior.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| DEATH REPLAY                                  [Report] [Skip]                  |
|--------------------------------------------------------------------------------|
| Replay viewport: final 12s from player-legal perspective                       |
| Timeline: -12s ---- impact ---- death                                          |
|--------------------------------------------------------------------------------|
| KILL CARD: Attacker, weapon, distance, hit location, visible rules             |
| [Watch Again] [View Damage] [Report Suspicious] [Continue]                     |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Replay viewport | legal camera, playback controls, timeline |
| Kill card | attacker, vũ khí, distance, hit location, damage |
| Actions | watch again, report, continue |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Cause of death | Kill card dễ đọc mà không playback |
| 2 | Replay controls | Obvious nhưng not dominant |
| 3 | Report | Accessible và contextual |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Timeline | impact markers và scrub controls |
| Visibility note | explains perspective limits |
| Report CTA | carries replay context |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Replay available | Autoplay muted hoặc per settings |
| Replay unavailable | Explain reason: privacy, server, corrupted, spectate limit |
| Suspected team kill | Promote report/appeal nếu supported |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Play/pause | Space/click | A / Cross | Tap |
| Scrub | Drag | Triggers | Drag timeline |
| Report | Click | Focus CTA | Tap CTA |

**Designer ghi chú**

- Replay is educational first; avoid sensational presentation.
- Never show địch intel beyond allowed replay rules.

**Acceptance checklist**

- [ ] Kill cause is dễ đọc even nếu replay cannot play.
- [ ] unavailable replay trạng thái explain why.

### Loot Transfer

**người chơi Intent**

Move extracted loot into stash, resolve overflow, và understand what is safe, quest-critical, hoặc valuable.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| LOOT TRANSFER                              Stash 182/200            [Continue] |
|--------------------------------------------------------------------------------|
| EXTRACTED LOOT                      | STASH GRID / TARGET                      |
| [Rifle 4x2] [Key FIR] [Meds]        | valid cells, containers, overflow lane   |
|--------------------------------------------------------------------------------|
| SELECTED: Keycard | Quest: Lab Rat | Value 45K | FIR Yes                       |
| WARNING: Stash will be full after transfer. [Sell Junk] [Open Stash]           |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Extracted loot | all carried-out items và statuses |
| Stash target | capacity, valid placement, containers |
| chi tiết panel | selected item giá trị/FIR/quest |
| cảnh báo lane | overflow và destructive cảnh báo |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Unresolved loot | phải được rõ trước leaving |
| 2 | Stash capacity | Persistent |
| 3 | Quest/FIR giá trị | Text labels |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Loot tile | footprint, giá trị, FIR, quest/protected badge |
| Overflow lane | temporary trạng thái và required resolution |
| Continue CTA | disabled nếu unresolved loot requires action |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Stash has room | Auto-place suggestion available |
| Stash full | Block continue hoặc require discard/sell based on rules |
| Item protected | Warn trước discard/sell |
| Server pending | Preserve loot và show pending trạng thái |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop | Grid cursor | Tap item then target |
| Auto place | Click | Y / Triangle | Auto button |
| Continue | Click | A / Cross | Sticky CTA |

**Designer ghi chú**

- Treat extracted loot as emotionally quan trọng; avoid casual loss copy.
- Overflow must feel solvable, not punitive.

**Acceptance checklist**

- [ ] Stash-full và overflow trạng thái are explicit.
- [ ] Quest/FIR items are clearly labeled.

### Quest Progress

**người chơi Intent**

See which objectives advanced, completed, failed, hoặc need turn-in trước the next raid.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| QUEST PROGRESS                                                                 |
|--------------------------------------------------------------------------------|
| Supply Run      READY TO TURN IN     Find rations 3/3 | Extracted Yes          |
| Lab Rat         IN PROGRESS          Samples 1/3      | Location Sector 7      |
| Old Debt        FAILED               Died before extract                       |
|--------------------------------------------------------------------------------|
| [Turn In Ready] [Track Next] [View Quest Board]                                |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Quest rows | title, status, objective delta, failure reason |
| Reward/turn-in area | ready rewards và required items |
| Actions | turn in, track next, quest board |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Ready/failed trạng thái | rõ labels |
| 2 | Objective deltas | Show trước/sau counts |
| 3 | Rewards | hiển thị rõ for completed quests |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Quest row | status label, progress delta, location, extraction/FIR rule |
| Failure reason | plain explanation và retry availability |
| Turn-in CTA | checks inventory capacity |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Completed | Promote turn-in |
| failed | Show reason và retry |
| Partial | Suggest track next |
| Reward stash full | Block turn-in và route to stash |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Select quest | Click row | D-pad | Tap row |
| Turn in | Click CTA | A / Cross | Sticky CTA |

**Designer ghi chú**

- Quest progress should explain extraction-dependent failures gently và directly.
- Do not cách dùng checkmarks alone for completion.

**Acceptance checklist**

- [ ] Completed, failed, partial, và blocked reward trạng thái are covered.

### Squad Summary và Social Actions

**người chơi Intent**

Review squad outcomes, commend/report người chơi, add friends, và continue với the party.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| SQUAD SUMMARY                                                                  |
|--------------------------------------------------------------------------------|
| Player        Result      Role       Damage     Actions                        |
| You           Extracted   Recon      620        --                             |
| Player2       KIA         Support    210        [Commend] [Add Friend]         |
| Player3       Extracted   Assault    840        [Commend] [Report]             |
|--------------------------------------------------------------------------------|
| [Stay With Squad] [Leave Party] [Invite Again]                                 |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| người chơi rows | identity, outcome, role, cốt lõi stat |
| Social actions | commend, add friend, report, mute/block |
| Party actions | stay, leave, invite |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Party continuation | rõ stay/leave actions |
| 2 | Outcome per member | Text labels |
| 3 | Safety actions | Accessible nhưng not accusatory |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| người chơi row | privacy-safe name, platform, role, kết quả |
| Report action | opens reason picker với match context |
| Commend | one-tap với undo nếu supported |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| người chơi left | Show left status và allowed actions |
| Blocked người chơi | Hide invite/add friend |
| Report submitted | Show confirmation và support ID |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Focus row | Click | D-pad | Tap |
| Social action | Click | A / Cross | Tap |

**Designer ghi chú**

- Safety actions nên được calm và rõ.
- Do not reveal private stats beyond allowed summary.

**Acceptance checklist**

- [ ] Commend/report/add friend trạng thái are hiển thị rõ và privacy-safe.

### Redeploy flow

**người chơi Intent**

Return to the next raid quickly nếu valid, hoặc understand exactly what phải được fixed first.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| REDEPLOY CHECK                                                                 |
|--------------------------------------------------------------------------------|
| Same kit: INVALID | Missing armor | Stash has replacement | Squad 2/3 ready    |
| Suggested route: Rebuild preset -> Fix Loadout -> Squad Ready -> Queue         |
|--------------------------------------------------------------------------------|
| [Return to Stash] [Rebuild Preset] [Fix Loadout] [Deploy Again Locked]         |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Validation summary | kit, stash, squad, quest, inventory |
| Suggested route | step sequence to redeploy |
| CTA row | deploy nếu valid, otherwise fix path |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Valid/invalid redeploy status | Direct label |
| 2 | First blocker | Names exact fix |
| 3 | Deploy Again | Only active khi validation passes |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Validation chip | pass/warn/block với text |
| Preset rebuild | shows chi phí và missing gear |
| Deploy CTA | repeats pre-raid validation rules |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Valid same kit | Deploy Again primary |
| Missing lost gear | offer preset/budget/stash routes |
| Squad not ready | Route to Squad Lobby |
| Inventory full | Suggest stash management |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Fix blocker | Click chip | Focus chip | Tap chip |
| Deploy again | Hold CTA | Hold A / Cross | Hold sticky CTA |

**Designer ghi chú**

- Redeploy phải được fast, nhưng never bypass loadout validation.

**Acceptance checklist**

- [ ] Deploy Again never activates với critical blockers.
- [ ] First blocker và fix route are obvious.

---

## Analytics

| Metric | cách dùng |
| :--- | :--- |
| AAR thời gian spent by tab | Determine which information người chơi giá trị |
| Replay watch/skip rate | Tune auto-play và teaching giá trị |
| Deploy Again conversion | Measure session momentum |
| Report submission rate | Monitor fair play và friction |
| Stash full sau extraction | Tune overflow và stash upgrades |
| Quest turn-in deep link usage | Validate quest progress clarity |

---

## checklist Nghiệm Thu

- [ ] Every outcome explains gains, losses, và next action.
- [ ] Death replay unavailable trạng thái are explicit.
- [ ] Loot transfer is unambiguous và handles stash-full.
- [ ] Report/commend flow are accessible from relevant contexts.
- [ ] Deploy Again never bypasses critical loadout validation.
- [ ] Mobile AAR keeps a rõ exit/continue CTA hiển thị rõ.
