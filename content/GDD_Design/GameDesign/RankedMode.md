---
title: "Ranked Mode & Competitive Systems"
type: docs
---

## 🏆 Competitive Philosophy

**Core Principle:** "Earn your rank through consistent performance"

Ranked mode is designed to:
- **Reward skill** - Better players climb faster
- **Create fair matches** - Similar skill levels play together
- **Provide progression goals** - Something to strive for beyond loot
- **Foster competition** - Leaderboards and seasonal rewards

**NOT:**
- Pay-to-win advantages
- Extremely grindy (should reflect skill, not hours)
- Toxic or frustrating
- Mandatory (casual play always available)

---

## 🎖️ Ranking System

### Rank Tiers

| Tier         | Divisions    | Icon | Player Distribution |
| :----------- | :----------- | :--- | :------------------ |
| **Bronze**   | I, II, III   | 🥉    | ~30%                |
| **Silver**   | I, II, III   | 🥈    | ~30%                |
| **Gold**     | I, II, III   | 🥇    | ~20%                |
| **Platinum** | I, II, III   | 💎    | ~12%                |
| **Diamond**  | I, II, III   | 💠    | ~5%                 |
| **Master**   | No divisions | 🏆    | ~2%                 |
| **Champion** | Top 500      | 👑    | ~1%                 |

### Rank Points (RP) System

**Base RP Structure:**
```
Starting RP: 0 (Bronze III)
Bronze → Silver: 300 RP
Silver → Gold: 600 RP
Gold → Platinum: 1000 RP
Platinum → Diamond: 1500 RP
Diamond → Master: 2000 RP
Master → Champion: Top 500 players
```

**Division Thresholds (Example: Gold):**
```
Gold III: 600-699 RP
Gold II: 700-799 RP
Gold I: 800-999 RP
Platinum III: 1000+ RP
```

### RP Gains & Losses

**RP Calculation Formula:**
```
RP Change = Base RP ± Performance Modifier ± Rank Modifier

Base RP:
- Extraction: +30 RP
- Death (early): -25 RP
- Death (mid-match): -15 RP
- Death (late-match): -10 RP
```

**Performance Modifiers:**

| Factor                    | RP Modifier  |
| :------------------------ | :----------- |
| Kills (per kill)          | +5 RP        |
| High-value loot extracted | +5 to +15 RP |
| Squad wipe achieved       | +10 RP       |
| Top 3 finish              | +10 RP       |
| Survived 10+ minutes      | +5 RP        |
| Quest completion          | +3 RP        |

**Rank Modifiers:**

| Rank Comparison              | Modifier                   |
| :--------------------------- | :------------------------- |
| Playing against higher ranks | +25% RP gains, -25% losses |
| Playing against same ranks   | Normal                     |
| Playing against lower ranks  | -25% RP gains, +25% losses |

**Protection Systems:**

| System                | Description                                      |
| :-------------------- | :----------------------------------------------- |
| **Demotion Shield**   | 2 games protection when entering new tier        |
| **Streak Protection** | After 3 losses, reduced RP loss for next 2 games |
| **Rank Floor**        | Cannot drop below Bronze I once reached          |

---

## 🎮 Ranked Queue

### Queue Requirements

**To Queue Ranked:**
- Account Level 15+
- 20+ casual matches completed
- At least 3 operators unlocked
- Valid phone number linked (anti-smurf)

### Queue Types

| Type      | Description      | Notes                                      |
| :-------- | :--------------- | :----------------------------------------- |
| **Solo**  | Individual queue | Matched with other solos or partial squads |
| **Duo**   | 2-player team    | RP averaged for matching                   |
| **Squad** | 3-4 players      | RP averaged, tighter matching              |

### Rank Restrictions (Squad)

**Maximum rank difference for squadding:**

| Your Rank         | Can Queue With    |
| :---------------- | :---------------- |
| Bronze - Silver   | Any rank          |
| Gold              | Silver - Platinum |
| Platinum          | Gold - Diamond    |
| Diamond           | Platinum - Master |
| Master - Champion | Diamond+ only     |

*Unranked players treated as Bronze for queue purposes*

### Matchmaking Parameters

**Factors (Priority Order):**
1. Rank (primary)
2. Queue time (expands range after 2 minutes)
3. Squad size balance
4. Server ping

**Queue Time Expansion:**
```
0-60 seconds: ±1 division
60-120 seconds: ±2 divisions
120-180 seconds: ±1 tier
180+ seconds: ±2 tiers (warning shown)
```

---

## 📈 Season Structure

### Season Duration

**Each Season:**
- Duration: 90 days (~3 months)
- Split into 2 Acts (45 days each)
- Act 1 → Act 2: Soft reset
- Season end: Hard reset

### Rank Resets

**Soft Reset (Mid-Season):**
```
Champion → Diamond I
Master → Diamond II
Diamond → Platinum II
Platinum → Gold II
Gold → Gold III
Silver → Silver III
Bronze → Bronze III
```

**Hard Reset (Season End):**
```
All players: Rank reduced by 1.5 tiers
Placement matches: 5 games to determine starting rank
Previous season rank affects placement matches
```

### Season Rewards

**End of Season Rewards by Peak Rank:**

| Peak Rank    | Rewards                                                              |
| :----------- | :------------------------------------------------------------------- |
| **Bronze**   | Bronze Badge, 500 Credits                                            |
| **Silver**   | Silver Badge, 1,000 Credits, Common Weapon Skin                      |
| **Gold**     | Gold Badge, 2,500 Credits, Uncommon Weapon Skin                      |
| **Platinum** | Platinum Badge, 5,000 Credits, Rare Weapon Skin, Operator Charm      |
| **Diamond**  | Diamond Badge, 10,000 Credits, Epic Weapon Skin, Diamond Charm       |
| **Master**   | Master Badge, 25,000 Credits, Legendary Weapon Skin, Master Trail    |
| **Champion** | All above + Champion Badge, Exclusive Operator Skin, Animated Banner |

**Rewards are:**
- Based on peak rank (highest achieved during season)
- Distributed 3 days after season ends
- Exclusive to that season (never return)

---

## 🏅 Leaderboards

### Leaderboard Types

| Board                | Metric                | Reset  |
| :------------------- | :-------------------- | :----- |
| **Global RP**        | Total RP              | Season |
| **Regional RP**      | RP by region          | Season |
| **Weekly RP**        | RP gained this week   | Weekly |
| **Kill Leaders**     | Total kills (ranked)  | Season |
| **Extraction Rate**  | % successful extracts | Season |
| **Wealth Extracted** | Total loot value      | Season |

### Top 500 (Champion)

**Champion Tier:**
- Reserved for Top 500 players globally
- Updated every 24 hours
- Visible rank number (#1, #2, etc.)
- Special champion-only rewards
- Decay applies (must play to maintain)

**Champion Decay:**
- After 48 hours of no ranked games: -50 RP/day
- Dropping below Top 500 RP threshold: Demoted to Master
- Playing 1 game resets decay timer

---

## ⚖️ Competitive Integrity

### Anti-Cheat Measures

| System                    | Description                       |
| :------------------------ | :-------------------------------- |
| **Kernel Anti-Cheat**     | Required for ranked (PC)          |
| **Behavior Analysis**     | Abnormal input patterns flagged   |
| **Statistics Tracking**   | Impossible stats reviewed         |
| **Report Prioritization** | Ranked reports reviewed faster    |
| **Hardware Bans**         | Cheaters banned at hardware level |

### Penalties

| Offense                    | Penalty                       |
| :------------------------- | :---------------------------- |
| **First Cheat Detection**  | Permanent ban                 |
| **Boosting (paid)**        | Season ban + rank reset       |
| **Smurfing (intentional)** | Warning → 7-day ban           |
| **AFK/Leaving**            | -50 RP + matchmaking cooldown |
| **Toxicity**               | Voice ban → ranked ban        |

### Matchmaking Cooldowns

| Offense              | Cooldown              |
| :------------------- | :-------------------- |
| Leave 1 game         | 5 minutes             |
| Leave 2 games (24h)  | 30 minutes            |
| Leave 3 games (24h)  | 2 hours               |
| Leave 4+ games (24h) | 24 hours + RP penalty |

---

## 🎯 Ranked-Specific Rules

### Gameplay Differences

| Aspect         | Casual    | Ranked            |
| :------------- | :-------- | :---------------- |
| Player Count   | 15-20     | 20 (always full)  |
| Match Duration | 15 min    | 15 min (strict)   |
| AI Difficulty  | Normal    | Slightly harder   |
| Loot Quality   | Normal    | 10% better spawns |
| Reconnect      | 2 minutes | 5 minutes         |

### Reconnect System

**If Disconnected:**
- Character goes AFK (vulnerable)
- 5 minutes to reconnect
- If reconnect: Resume at current position
- If timeout: Treated as death (RP loss)
- If squad extracts your body: Reduced RP loss

### Map Rotation

**Ranked Map Pool:**
- Curated selection (not all maps)
- Maps rotated bi-weekly
- Community voting on map pool (monthly)
- Newly released maps: 2-week delay before ranked

---

## 📊 Statistics & Analytics

### Player Stats Tracked

**Performance:**
- Matches played (ranked)
- Win rate (extraction rate)
- K/D ratio
- Average survival time
- Peak rank achieved

**Detailed:**
- Damage dealt/received
- Headshot percentage
- Favorite operators (by playtime)
- Best maps (by win rate)
- Squad vs Solo performance

### Match History

**Per Match Data:**
- Date, time, duration
- Map played
- Final placement
- Kills, damage, loot extracted
- RP change (+/-)
- Squad members

### Career Profile

**Public Profile Shows:**
- Current rank + progression
- Season history (past ranks)
- Badges earned
- Stats summary
- Recent matches (last 20)

**Privacy Options:**
- Hide career profile
- Hide current rank
- Hide match history

---

## 🤝 Squad Ranked Features

### Team RP

**Squad Average RP:**
- Matchmaking uses average RP of squad
- Individual RP gains still personal
- Performance modifiers still individual

### Voice Communication

**Ranked Voice:**
- Squad voice: Always available
- Proximity voice: Optional (default ON)
- Enemy death comms: Hear last 2 seconds (optional)

### Squad Synergy Bonus

**Consistent Squad Bonus:**
Playing 10+ ranked games with same squad members:
- +5% RP bonus for all members
- Must maintain 50%+ games together to keep bonus
- Stacks up to 3 squad mates (+15% max)

---

## 🏟️ Competitive Events

### Weekly Tournaments

**Open Ladder:**
- Every weekend
- Single elimination brackets
- Prizes: Credits, exclusive skins
- Entry: Free (Platinum+ rank)

### Monthly Majors

**Format:**
- Top 100 players invited
- Round robin → Finals
- Substantial prizes
- Streamed on official channels

### Seasonal Championships

**End of Season:**
- Top 500 players invited
- Multi-day event
- Largest prize pool
- Exclusive champion-only rewards

---

## 📅 Ranked Roadmap

### Launch (Season 1)
- ✅ Core RP system
- ✅ Bronze → Champion tiers
- ✅ Solo/Squad queue
- ✅ Season rewards
- ✅ Basic leaderboards

### Season 2
- Ranked challenges (bonus RP)
- Improved matchmaking
- Spectator mode (delayed)

### Season 3
- Professional league integration
- Custom lobbies (for tournaments)
- Coaching/replay system

### Future
- Cross-region ranked
- 1v1 arena mode (ranked)
- Team-based seasons



