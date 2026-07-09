---
title: "Post-Raid Screens"
type: docs
weight: 6
---

## Purpose

Post-raid screens convert raid outcome into learning, reward, recovery, and the next run. They must explain what happened, what changed, what was gained or lost, and how the player can act next.

Primary references:

| System | Source |
| :--- | :--- |
| Debrief | [Post-Game Debrief & Replay](../Gameplay/Post_Game_Debrief.md) |
| Extraction outcomes | [Extraction Mechanics](../Gameplay/Extraction_Mechanics.md) |
| Progression | [Progression & Monetization](../GameDesign/Progression.md) |
| Quest objectives | [Quest & Objective System](../Gameplay/Quest_Objective_System.md) |
| Fair play | [Anti-Cheat & Fair Play](../Gameplay/Anti_Cheat_Fair_Play.md) |

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |
| [In-Raid Screens](In_Raid_Screens.md) | Raid overlays and reconnect before results |
| [Out-of-Raid Screens](Out_Of_Raid_Screens.md) | Stash, quests, profile, and recovery actions after results |
| [Social Screens](Social_Screens.md) | Commend, report, add friend, and squad continuation |

---

## Screen Inventory

| Screen | Goal | Primary CTA | Critical States |
| :--- | :--- | :--- | :--- |
| Outcome Transition | Bridge raid end into results | Continue | extracted, KIA, MIA, disconnected |
| After Action Report | Explain rewards, losses, XP, stats, quests | Continue / Deploy Again | success, death, partial rewards, server issue |
| Death Replay | Teach cause of death | Watch / Skip | unavailable, saved clip, report |
| Loot Transfer | Confirm extracted items are stored | Continue to Stash | stash full, quest turn-in available |
| Quest Progress | Show objective changes | Track Next / Turn In | completed, failed, item lost |
| Squad Summary | Compare squad outcomes | Commend / Continue | solo, party stayed, member disconnected |
| Report / Commend | Positive and negative social actions | Submit | clip attached, category missing, cooldown |
| Redeploy Flow | Return to next run with valid setup | Deploy Again | missing kit, preset rebuild, party not ready |

---

## After Action Report

The AAR is the most important post-raid screen. It should be calm, readable, and fast to exit.

#### Layout (PC/Console)

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

#### Layout (PC/Console)

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

| Section | Requirement |
| :--- | :--- |
| Outcome banner | Result, map, survival time, cause |
| XP breakdown | Itemized sources before total |
| Loot/losses | Extracted, lost, kept, insured, quest-tagged items |
| Combat stats | Kills, damage, accuracy, distance, healing, revives |
| Quest progress | Completed, advanced, failed, or lost objectives |
| Squad summary | Player outcomes and social actions |
| Next actions | Deploy Again, Return to Stash, Watch Replay, Main Menu |

### AAR States

| State | Behavior |
| :--- | :--- |
| Extracted | Emphasize loot value, XP, quest progress, and stash transfer |
| KIA | Emphasize cause of death, lost/kept items, insurance ETA, replay |
| MIA / timeout | Explain timer or disconnect consequence |
| Server issue | Explain compensation or pending reconciliation if applicable |
| Data delayed | Show partial report and "finalizing results" state |

---

## Death Replay

#### Layout (PC/Console)

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

| Spec | Requirement |
| :--- | :--- |
| Goal | Help the player understand why they died without exposing unfair live intel |
| Entry points | AAR replay button, death transition if auto-play is enabled |
| Primary CTA | Watch / Skip |
| Secondary actions | Save clip, report player, scrub timeline |
| Unavailable states | MIA, server crash, no death event, expired replay |

### Replay UI

| Element | Behavior |
| :--- | :--- |
| Timeline | Shows hit events, death moment, and reveal window |
| Cause label | Weapon, hit location, attacker type; no enemy inventory |
| Camera | Standard top-down or server-approved replay view |
| Report shortcut | Pre-fills match and killer context |
| Save clip | Shows storage limit and confirmation |

---

## Loot Transfer

#### Layout (PC/Console)

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

| State | Behavior |
| :--- | :--- |
| Normal transfer | Items already moved to stash; show NEW tags |
| Stash full | Show overflow inbox, auto-sort, sell, or upgrade path |
| Quest turn-in available | Highlight quest item and deep link to trader/quest |
| Insurance scheduled | Show provider and ETA |
| Secure container | Separate kept items from extracted items |

Loot transfer must never make the player wonder whether items were saved. The first line should state the result plainly.

---

## Quest Progress

#### Layout (PC/Console)

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

| Result | UI Behavior |
| :--- | :--- |
| Completed | Show reward preview and Turn In if required |
| Advanced | Show old and new progress |
| Failed | Explain failure condition and retry availability |
| Item lost | Identify lost objective item and where to reacquire |
| New quest unlocked | Show unlock reason and faction |

---

## Squad Summary And Social Actions

#### Layout (PC/Console)

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

| Action | Requirement |
| :--- | :--- |
| Commend | One commendation per eligible teammate; categories are clear and positive |
| Add friend | Available for recent squad and encounter rules where allowed |
| Report | Category required; optional text and clip attach |
| Stay with squad | Keeps party together and routes to lobby/home |
| Leave party | Confirmation if party is still queued or regrouping |

### Report Flow

| Step | UI Requirement |
| :--- | :--- |
| Select player | From squad summary, death replay, or kill context |
| Select category | Cheating, abusive voice/text, griefing, exploit, name, other |
| Add evidence | Optional text and clip if available |
| Submit | Confirmation toast; no punishment details |
| Cooldown | Prevent spam and explain if report is rate-limited |

---

## Redeploy Flow

#### State Diagram

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

| State | Behavior |
| :--- | :--- |
| Valid same kit | Deploy Again is primary |
| Missing lost gear | Offer rebuild from preset, budget kit, or stash |
| Squad not ready | Route to Squad Lobby and show blockers |
| Quest completed | Suggest turn-in before redeploy, but do not block unless required |
| Inventory full | Suggest stash management before redeploy |

---

## Platform Layout

| Platform | Layout |
| :--- | :--- |
| PC / Console | Tabbed AAR with Summary, Loot, XP, Stats, Replay, Squad |
| Mobile | Scroll summary with sticky bottom CTA and tabs for Loot, Stats, Replay |
| Console | Large focusable cards; no dense tables without row focus |
| Tablet | Two-column summary plus detail panel |

---

## Designer-Ready Screen Specs

Post-raid screens must explain outcome, preserve player trust, and route quickly back to stash, recovery, squad, or redeploy. Summary tables above are navigation; the specs below own layout and state detail.

### After Action Report

**Player Intent**

Understand raid result, rewards, losses, performance, and the next best action.

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

| Region | Requirement |
| :--- | :--- |
| Outcome card | result, map, duration, survival/death reason, insurance/loss summary |
| Stat panel | XP, kills, damage, survival, quest deltas |
| Next actions | move loot, turn in quest, rebuild, deploy again |
| Tabs | deeper detail without hiding primary outcome |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Outcome and next action | Visible immediately |
| 2 | Gains/losses | Plain totals with deltas |
| 3 | Detailed stats | Secondary tabs |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Result badge | extracted, KIA, MIA, disconnected, run-through with text |
| XP breakdown | source rows and total |
| Next action card | one primary route based on result |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Extraction | Move Loot and Deploy Again promoted |
| Death | Rebuild and Death Replay promoted |
| MIA/disconnect | Explain gear consequence |
| Data delayed | Show pending stats and safe next route |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch tab | Click | Bumpers | Tab row |
| Continue | Enter/click | A / Cross | Sticky CTA |
| View detail | Click row | Focus row | Tap card |

**Designer Notes**

- The first screen should answer: what happened, what changed, what now.
- Do not force players through every tab before continuing.

**Acceptance Checklist**

- [ ] Result, gains, losses, and next action are visible above the fold.
- [ ] Delayed stat state does not block safe continuation.

### Death Replay

**Player Intent**

Understand how they died, learn the counterplay, and optionally report suspicious behavior.

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

| Region | Requirement |
| :--- | :--- |
| Replay viewport | legal camera, playback controls, timeline |
| Kill card | attacker, weapon, distance, hit location, damage |
| Actions | watch again, report, continue |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Cause of death | Kill card readable without playback |
| 2 | Replay controls | Obvious but not dominant |
| 3 | Report | Accessible and contextual |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Timeline | impact markers and scrub controls |
| Visibility note | explains perspective limits |
| Report CTA | carries replay context |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Replay available | Autoplay muted or per settings |
| Replay unavailable | Explain reason: privacy, server, corrupted, spectate limit |
| Suspected team kill | Promote report/appeal if supported |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Play/pause | Space/click | A / Cross | Tap |
| Scrub | Drag | Triggers | Drag timeline |
| Report | Click | Focus CTA | Tap CTA |

**Designer Notes**

- Replay is educational first; avoid sensational presentation.
- Never show enemy intel beyond allowed replay rules.

**Acceptance Checklist**

- [ ] Kill cause is readable even if replay cannot play.
- [ ] Unavailable replay states explain why.

### Loot Transfer

**Player Intent**

Move extracted loot into stash, resolve overflow, and understand what is safe, quest-critical, or valuable.

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

| Region | Requirement |
| :--- | :--- |
| Extracted loot | all carried-out items and statuses |
| Stash target | capacity, valid placement, containers |
| Detail panel | selected item value/FIR/quest |
| Warning lane | overflow and destructive warnings |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Unresolved loot | Must be clear before leaving |
| 2 | Stash capacity | Persistent |
| 3 | Quest/FIR value | Text labels |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Loot tile | footprint, value, FIR, quest/protected badge |
| Overflow lane | temporary state and required resolution |
| Continue CTA | disabled if unresolved loot requires action |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Stash has room | Auto-place suggestion available |
| Stash full | Block continue or require discard/sell based on rules |
| Item protected | Warn before discard/sell |
| Server pending | Preserve loot and show pending state |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop | Grid cursor | Tap item then target |
| Auto place | Click | Y / Triangle | Auto button |
| Continue | Click | A / Cross | Sticky CTA |

**Designer Notes**

- Treat extracted loot as emotionally important; avoid casual loss copy.
- Overflow must feel solvable, not punitive.

**Acceptance Checklist**

- [ ] Stash-full and overflow states are explicit.
- [ ] Quest/FIR items are clearly labeled.

### Quest Progress

**Player Intent**

See which objectives advanced, completed, failed, or need turn-in before the next raid.

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

| Region | Requirement |
| :--- | :--- |
| Quest rows | title, status, objective delta, failure reason |
| Reward/turn-in area | ready rewards and required items |
| Actions | turn in, track next, quest board |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Ready/failed states | Clear labels |
| 2 | Objective deltas | Show before/after counts |
| 3 | Rewards | Visible for completed quests |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Quest row | status label, progress delta, location, extraction/FIR rule |
| Failure reason | plain explanation and retry availability |
| Turn-in CTA | checks inventory capacity |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Completed | Promote turn-in |
| Failed | Show reason and retry |
| Partial | Suggest track next |
| Reward stash full | Block turn-in and route to stash |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Select quest | Click row | D-pad | Tap row |
| Turn in | Click CTA | A / Cross | Sticky CTA |

**Designer Notes**

- Quest progress should explain extraction-dependent failures gently and directly.
- Do not use checkmarks alone for completion.

**Acceptance Checklist**

- [ ] Completed, failed, partial, and blocked reward states are covered.

### Squad Summary And Social Actions

**Player Intent**

Review squad outcomes, commend/report players, add friends, and continue with the party.

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

| Region | Requirement |
| :--- | :--- |
| Player rows | identity, outcome, role, core stat |
| Social actions | commend, add friend, report, mute/block |
| Party actions | stay, leave, invite |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Party continuation | Clear stay/leave actions |
| 2 | Outcome per member | Text labels |
| 3 | Safety actions | Accessible but not accusatory |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Player row | privacy-safe name, platform, role, result |
| Report action | opens reason picker with match context |
| Commend | one-tap with undo if supported |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Player left | Show left status and allowed actions |
| Blocked player | Hide invite/add friend |
| Report submitted | Show confirmation and support ID |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Focus row | Click | D-pad | Tap |
| Social action | Click | A / Cross | Tap |

**Designer Notes**

- Safety actions should be calm and clear.
- Do not reveal private stats beyond allowed summary.

**Acceptance Checklist**

- [ ] Commend/report/add friend states are visible and privacy-safe.

### Redeploy Flow

**Player Intent**

Return to the next raid quickly if valid, or understand exactly what must be fixed first.

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

| Region | Requirement |
| :--- | :--- |
| Validation summary | kit, stash, squad, quest, inventory |
| Suggested route | step sequence to redeploy |
| CTA row | deploy if valid, otherwise fix path |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Valid/invalid redeploy status | Direct label |
| 2 | First blocker | Names exact fix |
| 3 | Deploy Again | Only active when validation passes |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Validation chip | pass/warn/block with text |
| Preset rebuild | shows cost and missing gear |
| Deploy CTA | repeats pre-raid validation rules |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Valid same kit | Deploy Again primary |
| Missing lost gear | Offer preset/budget/stash routes |
| Squad not ready | Route to Squad Lobby |
| Inventory full | Suggest stash management |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Fix blocker | Click chip | Focus chip | Tap chip |
| Deploy again | Hold CTA | Hold A / Cross | Hold sticky CTA |

**Designer Notes**

- Redeploy must be fast, but never bypass loadout validation.

**Acceptance Checklist**

- [ ] Deploy Again never activates with critical blockers.
- [ ] First blocker and fix route are obvious.

---

## Analytics

| Metric | Use |
| :--- | :--- |
| AAR time spent by tab | Determine which information players value |
| Replay watch/skip rate | Tune auto-play and teaching value |
| Deploy Again conversion | Measure session momentum |
| Report submission rate | Monitor fair play and friction |
| Stash full after extraction | Tune overflow and stash upgrades |
| Quest turn-in deep link usage | Validate quest progress clarity |

---

## Acceptance Checklist

- [ ] Every outcome explains gains, losses, and next action.
- [ ] Death replay unavailable states are explicit.
- [ ] Loot transfer is unambiguous and handles stash-full.
- [ ] Report/commend flows are accessible from relevant contexts.
- [ ] Deploy Again never bypasses critical loadout validation.
- [ ] Mobile AAR keeps a clear exit/continue CTA visible.
