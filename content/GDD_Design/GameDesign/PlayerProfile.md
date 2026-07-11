---
title: "Player Profile & Career Stats"
type: docs
weight: 22
---

## Overview

The Player Profile communicates identity, mastery, history, and social trust. It should help players celebrate progress while giving privacy controls for public information.

The profile should answer two different needs. For the owner, it is a career dashboard and memory book. For other players, it is a social trust surface: who is this person, what do they play, are they active, and can I invite them safely?

Profile design must avoid shaming players with raw stats alone. Extraction games involve learning, risk, and streaks of failure. The profile should celebrate milestones, favorite roles, memorable runs, and improvement as much as rank or K/D.

## Profile Tabs

Tabs should separate identity from analysis. The Overview tab gives a quick read, while Stats and Match History support deeper review. Social actions should be present but not so aggressive that profile browsing becomes spammy.

| Tab | Content | Purpose |
| :--- | :--- | :--- |
| Overview | Banner, title, favorite operator, key stats | Fast identity read |
| Stats | Extraction rate, K/D, survival time, loot value | Performance review |
| Operators | Per-operator mastery and usage | Role identity |
| Weapons | Weapon usage, accuracy, favorite builds | Combat identity |
| Achievements | Badges, milestones, event trophies | Collection and pride |
| Match History | Recent raids, outcomes, rewards | Learning and review |
| Social | Friends, clan, invite actions | Connection |

## Public And Private Views

Privacy defaults should protect sensitive behavior such as match history, online status, and recent teammates. Public identity can still be expressive through banners, titles, badges, and chosen showcase stats.

| Field | Own Profile | Public Profile | Privacy Option |
| :--- | :--- | :--- | :--- |
| Display name | Full | Full | No |
| Current rank | Full | Full or hidden | Yes |
| Career stats | Full | Summary | Yes |
| Match history | Full | Hidden by default | Yes |
| Clan | Full | Visible | Yes |
| Online status | Full | Configurable | Yes |

## Career Metrics

Career metrics should teach what the game values. Extraction rate, loot value, operator mastery, and streaks communicate survival and decision quality. K/D can be shown, but it should not dominate the profile.

| Metric | Why It Matters |
| :--- | :--- |
| Extraction rate | Measures survival and decision discipline |
| Average loot value | Measures economy knowledge |
| Operator mastery | Shows role commitment |
| Favorite map | Shows player identity |
| Highest rank | Competitive prestige |
| Longest extraction streak | Memorable achievement |

## Match History Row

Match history is a learning tool. Each row should help the player remember what happened and decide what to do next: change route, adjust loadout, retry a quest, or review a death.

| Field | Example |
| :--- | :--- |
| Outcome | Extracted / Killed / Timeout |
| Map | Industrial Zone |
| Mode | The Raid |
| Squad | Solo / Duo / Trio |
| Loot value | Credits estimate |
| Key event | Boss kill, quest complete, rare item extracted |

## Profile Examples

A player who extracts often but avoids combat should be able to show survival skill through extraction rate, streaks, loot value, and favorite roles. The profile should not reduce all identity to K/D.

A ranked player should have a clear seasonal badge and history, but privacy options should let them hide match history details if they do not want every route or teammate visible.

A clan recruiter should quickly see activity, preferred modes, operator mastery, and social status without needing access to private match records.

## Profile Failure Cases

- If public stats encourage harassment, default visibility should be reduced.
- If the profile hides all progress behind tabs, players lose pride moments.
- If match history has no learning detail, it becomes a trophy list instead of a review tool.
- If social actions are too aggressive, profile browsing can become spam.

## Social Actions

| Action | Rule |
| :--- | :--- |
| Add friend | Respect privacy and block lists |
| Invite to party | Only if player allows invites |
| View clan | Opens clan profile |
| Report | Available from public profile and match history |
| Mute / block | Persistent account-level action |

## Cross-References

| Topic | Page |
| :--- | :--- |
| Ranked data | [Ranked Mode](rankedmode/index.html) |
| Clan identity | [Clan System](clansystem/index.html) |
| Progression | [Progression](progression/index.html) |
| Privacy settings | [User Settings](usersettings/index.html) |
