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

| Result | UI Behavior |
| :--- | :--- |
| Completed | Show reward preview and Turn In if required |
| Advanced | Show old and new progress |
| Failed | Explain failure condition and retry availability |
| Item lost | Identify lost objective item and where to reacquire |
| New quest unlocked | Show unlock reason and faction |

---

## Squad Summary And Social Actions

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
