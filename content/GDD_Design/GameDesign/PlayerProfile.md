---
title: "Player Profile & Career Stats"
type: docs
weight: 22
---

## Overview

The Player Profile is a **living trophy case** — the public-facing record of a player's journey, achievements, and identity. In extraction games, stats tell a story of risk-taking and mastery that players want to share and compare. The profile screen bridges social features, achievement systems, and identity customization.

> **Cross-References:** [Progression](Progression.md) — XP, account level, and operator mastery feed into profile stats; [Ranked Mode](RankedMode.md) — seasonal ranks and badges displayed on profile; [Clan System](ClanSystem.md) — clan membership and contribution shown; [Home Screen & Lobby](HomeScreen_Design.md) — profile accessed via player card on Home Screen; [Post-Game Debrief](../Gameplay/Post_Game_Debrief.md) — debrief stats feed into career totals.

---

## 1. Design Philosophy

**What a great profile does:**
- Lets players **signal identity and achievement** to others
- Creates **meta-goals** ("I want to hit 65% extraction rate")
- Makes **skill legible** — someone's profile tells you if they're dangerous
- Drives **social comparison** — healthy competition between friends
- Acts as a **trophy shelf** for seasonal and lifetime accomplishments

**Privacy-first:** All stats are **public by default** but fully hideable by section. Players control what others see.

---

## 2. Profile Screen Layout

### View: Your Own Profile (Full Access)

```
┌─────────────────────────────────────────────────────────────────────┐
│  [← Back]                  MY PROFILE              [✏ Edit Banner]  │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │           [CUSTOM BANNER — animated or static]              │    │
│  │   [OPERATOR 3D — idle animation, holding weapon]           │    │
│  │   Mamba — Assault                Account Lvl 47            │    │
│  │   [WOLF] — Veteran               RankSeason8: Platinum III │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  [OVERVIEW] [STATS] [ACHIEVEMENTS] [OPERATORS] [MATCH HISTORY]      │
│                                                                      │
│  ━━━ OVERVIEW TAB (default) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                                      │
│  CAREER                     THIS SEASON                             │
│  Raids:        1,204        Raids:          88                       │
│  Extractions:  762 (63%)    Extractions:    61 (69%)                 │
│  K/D Ratio:    1.82         K/D Ratio:      2.14                     │
│  Kills:        2,191        Kills:          189                       │
│  Damage:       1.4M         Wealth Extr.:   $2,840,000               │
│  Wealth Extr:  $18M         Peak Rank:      Platinum III             │
│                                                                      │
│  FAVORITE OPERATOR:  Mamba (480 raids)                              │
│  BEST MAP:           Aethelgard Industrial  68% extract rate         │
│  MOST USED WEAPON:   M4A1                   710 kills                │
│                                                                      │
│  RECENT BADGES ─────────────────────────────────────────────────── │
│  [🏆 Season 7 Gold] [✅ 100 Extractions] [🗡 50 Solo Kills] [+12]   │
│                                                                      │
│  EQUIPPED TITLE: "Vault Raider"      EQUIPPED CHARM: ☠ Skull        │
└─────────────────────────────────────────────────────────────────────┘
```

### View: Someone Else's Profile (Public View)

Identical layout but:
- Edit buttons hidden
- "Add Friend / Invite to Squad / Report / Block" action bar shown at top
- Privacy settings respected — hidden sections show "Stats hidden by player"

---

## 3. Profile Header

The profile header is the **first impression** — fully customizable.

| Element | Options | How to Unlock |
| :------ | :------ | :------------ |
| **Banner** | 100+ static banners; 20+ animated | Shop, battle pass, achievements, events |
| **Operator** | Any unlocked operator | Operator unlock system |
| **Title** | Short text title under name | Achievements, rank rewards, quests |
| **Charm display** | Shows equipped weapon charm | Equipped in Loadout Prep |
| **Account Lvl badge** | Auto (cannot be hidden) | Account progression |
| **Rank badge** | Current season rank icon | Ranked Mode |
| **Clan tag + rank** | [CLAN] Member/Veteran/etc. | Clan System |

**Banner layering system:** Background + Foreground motif + Animated particle (3 layers). Each layer unlockable independently.

---

## 4. Stats — Overview Tab

The Overview tab shows the most important high-level statistics:

### Career Statistics

| Stat | Description |
| :--- | :---------- |
| **Raids Completed** | Total raids entered (any mode) |
| **Extractions** | Number of successful extractions |
| **Extraction Rate** | Extractions ÷ Raids (% shown) |
| **K/D Ratio** | Total kills ÷ total deaths |
| **Total Kills** | Lifetime kill count |
| **Total Damage** | Lifetime damage dealt (millions) |
| **Wealth Extracted** | Total credit value extracted over career |
| **Hours Played** | Total time in-raid + menus |
| **Longest Survival** | Longest single raid survived (minutes:seconds) |
| **Boss Kills** | Number of boss eliminations |

### Session Stats

| Stat | Description |
| :--- | :---------- |
| **This Season** | Raids, extraction rate, K/D, wealth extracted, peak rank |
| **Last Session** | Collapsible — last 5 raids summary |
| **Today** | Collapsible — today's session overview |

### Identity Stats (Fun Stats)

| Stat | Description |
| :--- | :---------- |
| **Favorite Operator** | Most raids played with |
| **Best Map** | Highest extraction rate map |
| **Most Killed By** | Weapon type or operator class that kills you most |
| **Most Used Weapon** | By kill count |
| **Total Insurance Claims** | Number of items returned via insurance |
| **Credits Spent on Insurance** | Lifetime insurance spend |
| **Biggest Single Haul** | Highest value extracted in a single raid |
| **Bloodiest Raid** | Highest kill count in one match |

---

## 5. Stats — Deep Dive Tab

Detailed per-category breakdowns for competitive players who want granular data.

### By Operator

| Column | Data |
| :----- | :--- |
| Operator Name | With class icon |
| Raids | Total raids using this operator |
| K/D | Kills / Deaths |
| Extraction Rate | % extractions |
| Avg Wealth/Raid | Average credit value extracted |
| Best Streak | Longest consecutive extraction streak |
| Playtime | Hours played as this operator |

### By Weapon

| Column | Data |
| :----- | :--- |
| Weapon | With category icon |
| Kills | Total kills |
| Headshot Rate | % headshots |
| Avg Damage/Hit | Average damage per bullet landed |
| Accuracy | Shots landed / shots fired |
| Most Used Attachment | Most equipped scope/grip/suppressor |

### By Map

| Column | Data |
| :----- | :--- |
| Map Name | Name + thumbnail |
| Raids | Total raids on this map |
| Extraction Rate | % |
| Avg Kills | Per raid |
| Avg Wealth | Credit value extracted per raid |
| Favorite Route | Most common entry/exit points (heatmap preview) |

---

## 6. Achievements Tab

Achievements are **lifetime unlocks** that feed the badge wall.

### Achievement Categories

| Category | Examples |
| :------- | :------- |
| **Milestones** | 10 / 50 / 100 / 500 / 1000 raids; 50% / 60% / 70% extraction rate |
| **Combat** | 100 kills, 1,000 kills, 10,000 kills; 50 headshots; Kill a boss solo |
| **Economic** | Extract $100,000 lifetime; Complete a raid with a $0 loadout |
| **Social** | Play 10 raids with same squad; 100 games with clanmates |
| **Exploration** | Find every named location on 1 map; Extract via every extraction point |
| **Seasonal** | Season rank rewards (Gold Season 1, Platinum Season 2, etc.) |
| **Rare / Hidden** | "Ghost" — extract without firing a shot; "Jackpot" — extract a Legendary item |

### Badge Display

- Profile shows **6 featured badges** (player-selected from earned)
- Full wall of all badges: locked badges shown as silhouettes with unlock hint
- Rarity tiers: Common / Uncommon / Rare / Epic / Legendary (animated)

---

## 7. Match History Tab

Last **50 matches** shown in list form, with expandable detail per match.

### Match History Row

```
┌──────────────────────────────────────────────────────────────────────┐
│  [✅ EXTRACTED]  Aethelgard Industrial  •  The Raid  •  Trio        │
│  Duration: 12:34 min    Kills: 3    Wealth: $18,200    RP: +42      │
│  Feb 28, 2026  14:06   [Mamba — Assault]                             │
│  Squad: Kai_V, Dxt_Raptor                          [▼ Details]       │
└──────────────────────────────────────────────────────────────────────┘
```

**Expanded details:** Full inventory extracted, damage dealt/received, ability uses, insurance returned from this raid, opponent highlights (if any).

### Filters

- Filter by: Mode (Raid / Blitz / Ranked / All)
- Filter by: Outcome (Extract / KIA / All)
- Filter by: Operator
- Filter by: Date range

---

## 8. Social Actions on Profile

| Action | Visible to | Confirmation? |
| :----- | :--------- | :------------ |
| **Add Friend** | Non-friend players | No |
| **Invite to Squad** | Any player not in a squad | No |
| **View Clan** | Any player with a clan | No |
| **Compare Stats** | Friends | No — side-by-side overlay |
| **Report Player** | Any player | Yes — reason required |
| **Block Player** | Any player | Yes |

**Compare Stats (Friend Only):** Side-by-side comparison overlay shows K/D, extraction rate, and wealth extracted between you and the friend — drives friendly competition.

---

## 9. Privacy Settings

| Setting | Options |
| :------ | :------ |
| Profile visibility | Public / Friends Only / Private |
| Stats visibility | All stats / Summary only / Hidden |
| Match history | Visible / Hidden |
| Online status | Show / Hide |
| Rank visibility | Show / Hide |
| Clan visibility | Show / Hide |

*Note: Account Level and Operator shown on nameplate in-game are ALWAYS visible regardless of profile privacy.*

---

## Cross-References

- [Progression](Progression.md) — Account XP, operator mastery, and quest completion count all feed into career stats.
- [Ranked Mode](RankedMode.md) — Seasonal rank badges, RP history, and peak rank displayed on profile; match history includes RP changes.
- [Post-Game Debrief](../Gameplay/Post_Game_Debrief.md) — Each debrief contributes stats to career totals in real-time.
- [Clan System](ClanSystem.md) — Clan emblem, rank title, and contribution metrics shown on profile.
- [Home Screen & Lobby](HomeScreen_Design.md) — Tap player card on Home Screen to open own profile; tap friend's name → their profile.
- [LiveOps](LiveOps.md) — Event-exclusive badges and profile frames earned through limited-time events.
