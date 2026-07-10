---
title: "Game Modes Design"
type: docs
---

## Overview

Game modes define why players enter the extraction loop and what rules shape each run. The Raid is the core experience; all other modes must support onboarding, recovery, competition, or live operations without diluting the extraction identity.

Every mode should answer one player need. The Raid is the main identity. Scavenger Run helps players recover. Blitz supports short sessions. Ranked gives mastery a competitive stage. Co-op Training lets players practice systems without PvP pressure. Featured modes create novelty without rewriting the core economy every week.

Mode design should avoid splitting the audience into incompatible games. A player who learns routes, sound, extraction timing, and inventory risk in one mode should carry that knowledge into the others. Rule changes can adjust pressure, but they should not teach habits that fail in the core raid.

## Mode Selection Flow

The selection flow should make risk visible before matchmaking starts. Players should never discover after loading that insurance is disabled, gear loss is harsher, squad fill is on, or the selected event has special extraction rules. The confirmation step is the contract between the mode and the player.

| Step | Screen / Action | Result |
| :--- | :--- | :--- |
| 1 | Home Screen | Player chooses to deploy |
| 2 | Loadout Preparation | Player reviews gear and squad state |
| 3 | Choose Mode | Player selects Raid, Scav, Blitz, Ranked, Co-op, or Featured |
| 4 | Choose Map or Event | Player commits to zone rules and event modifiers |
| 5 | Choose Squad Size | Player confirms Solo, Duo, Trio, or fill |
| 6 | Confirm Risk | UI summarizes gear loss, insurance, and rewards |
| 7 | Matchmaking | Queue begins with selected rules |

## Mode Catalogue

| Mode | Purpose | Risk | Squad Size | Notes |
| :--- | :--- | :--- | :--- | :--- |
| The Raid | Core extraction experience | Normal | Solo, Duo, Trio | Full loot, full progression, insurance supported |
| Scavenger Run | Recovery and practice | Low | Solo, Duo | Free temporary kit, limited rewards, no insurance |
| Blitz | Short session quick play | Medium | Solo, Duo, Trio | Faster timer, reduced map size, faster extraction pressure |
| Ranked Operations | Competitive extraction | High | Solo, Duo, Trio | RP enabled, stricter matchmaking, limited rule changes |
| Co-op Training | Low-pressure mastery | Low | Solo, Duo, Trio | PvE learning, no premium rewards |
| Featured Mode | Live Ops variety | Variable | Event-defined | Rotates through seasonal rules |

## Mode Rule Contract

Each mode card and deploy confirmation must show the rule contract before matchmaking starts. If a mode changes loss, insurance, quest progress, extraction timing, or rewards, the player must see that before pressing Deploy.

| Mode | Timer | Squad Size | Player Density | AI Density | Gear Loss | Insurance | Quest Progress | Reward Cap | Extraction Modifier | Matchmaking Pool |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| The Raid | 10-15 min target run | Solo/Duo/Trio | Standard | Standard | Enabled | Enabled | Full | None | Standard extraction rules | Casual regional |
| Scavenger Run | Standard or shorter | Solo/Duo | Standard or lower | Standard | Temporary scav kit only | Disabled | Limited | Lower loot ceiling | Standard, but lower-value extracts allowed | Recovery-weighted casual |
| Blitz | Short | Solo/Duo/Trio | Medium-high | Reduced or focused | Enabled | Enabled unless event says otherwise | Limited or full per map | Lower raid value ceiling | Faster late pressure and shorter extract windows | Casual quick-play |
| Ranked Operations | Season-defined | Solo/Duo/Trio | Competitive target | Standard | Enabled | Restricted or disabled | Ranked-safe only | Ranked rewards and cosmetics | Standard unless season rule is explicit | Ranked pool |
| Co-op Training | Flexible | Solo/Duo/Trio | None PvP | Tutorial/training | Disabled or restored | Not needed | Tutorial/training only | No premium/economy farming | Guided extraction and retry support | PvE training |
| Featured Mode | Event-defined | Event-defined | Event-defined | Event-defined | Must be disclosed | Must be disclosed | Must be disclosed | Event-defined | Any modifier must be disclosed | LiveOps event pool |

## Mode Compatibility Matrix

Mode variants can adjust pressure, but they should not teach habits that fail in the core raid.

| Core Skill | The Raid | Scavenger Run | Blitz | Ranked | Co-op Training | Featured |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Route reading | Primary | Practice | Compressed | Primary | Guided | Depends on event |
| Loot risk | Primary | Low-stakes | Faster decisions | High-stakes | Tutorial only | Event-defined |
| Combat judgment | Primary | Practice | Frequent | Competitive | AI-focused | Event-defined |
| Extraction timing | Primary | Practice | Faster | Primary | Guided | Must be explicit |
| Gear fear | Primary | Reduced | Medium | High | Disabled | Event-defined |
| Economy impact | Full | Capped | Reduced or full | Full with ranked rules | Minimal | Explicitly capped |
| Tutorial value | Moderate | High for recovery | Low | Low | Primary | Contextual |

If a mode removes both gear risk and extraction pressure, it must be framed as training or event novelty, not as the primary recommendation.

## Core Mode Rules

### The Raid

The Raid is the reference mode. Balance, economy, onboarding, and map design should be judged against this mode first.

The Raid should be emotionally complete by itself: preparation, fear, opportunity, conflict, extraction, and recovery. If a feature only works in another mode but damages The Raid, it should be treated as a variant rule rather than core design.

| Parameter | Target |
| :--- | :--- |
| Match length | 10-15 minutes |
| Player count | Tuned per map size |
| AI threat | Present around loot and objectives |
| Gear loss | Enabled |
| Insurance | Enabled |
| Quest progress | Enabled |

### Scavenger Run

Scavenger Run prevents poverty spirals and gives players a way to practice routes without risking their stash.

This mode should feel useful but not optimal. It is a pressure release valve for players who just lost gear, a learning tool for new routes, and a way to re-enter the loop without giving away premium rewards. It must not become the best farming path.

| Rule | Direction |
| :--- | :--- |
| Starting kit | Randomized low-value kit |
| Cooldown | Required to prevent farming |
| Rewards | Extracted loot allowed, but lower ceiling than The Raid |
| Progression | Limited account XP, no ranked progress |

### Ranked Operations

Ranked Operations uses the core extraction loop with stricter competitive rules. Full RP design lives in [Ranked Mode](rankedmode.html).

Ranked should test extraction mastery, not only elimination skill. The best ranked players should know when to avoid a fight, when to secure value, when to pressure another squad, and when to leave. Rewards should celebrate consistency, discipline, and clutch decisions.

| Rule | Direction |
| :--- | :--- |
| Matchmaking | Rank-aware, latency-aware, anti-smurf monitored |
| Insurance | Disabled or restricted per season rules |
| Rewards | Rank points, cosmetics, leaderboard position |
| Integrity | Stronger penalties for disconnects, boosting, and collusion |

## Mode Card Requirements

Mode cards should communicate the emotional contract of each queue. A player should know whether this is a serious stash-risk raid, a recovery run, a fast warm-up, a competitive match, or a seasonal experiment before pressing confirm.

| Field | Required |
| :--- | :--- |
| Mode name | Yes |
| Risk level | Yes |
| Estimated raid length | Yes |
| Gear loss rules | Yes |
| Insurance rules | Yes |
| Squad sizes | Yes |
| Reward type | Yes |

## Mode Design Examples

The Raid should be the default recommendation for players with a valid kit and no urgent recovery state. It is where economy, quest, map, and insurance systems are balanced first.

Scavenger Run should be recommended after repeated losses or low stash value. Its UI should frame the mode as recovery and practice, not as a shame state.

Blitz should be useful when the player has limited time. It can reduce map size and timer length, but it still needs loot, danger, and extraction decisions.

Featured Mode should be visually distinct but rules-transparent. If an event modifies insurance, extraction timing, AI density, or reward caps, those rules must be shown before matchmaking.

## Mode Failure Cases

- If players farm Scavenger Run instead of normal raids, reward ceilings are too high.
- If Blitz teaches reckless habits that fail in The Raid, pressure tuning is too arcade-like.
- If Ranked becomes kill-only, RP weights need extraction and objective reinforcement.
- If Featured Mode requires long explanation, the modifier may be too complex.
| Event timer | Only for featured modes |

## Cross-References

| Topic | Page |
| :--- | :--- |
| Prep screen integration | [Loadout Preparation](loadoutpreparation.html) |
| Ranked rules | [Ranked Mode](rankedmode.html) |
| Event rotations | [Live Operations](liveops.html) |
| Map rules | [Map Design](mapdesign.html) |
| Insurance mode differences | [Insurance System](insurancesystem.html) |
