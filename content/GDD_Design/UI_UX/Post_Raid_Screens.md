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
