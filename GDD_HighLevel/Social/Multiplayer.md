# Social & Multiplayer Systems

**[← Back to Index](../README.md)** | **[Next: Core Gameplay →](../GameDesign/CoreGameplay.md)**

---

## 🎯 Social Design Philosophy

**Core Principle:** "Alone is viable, together is powerful"

The game must be:
- **Solo-friendly** - Single players can succeed without feeling disadvantaged
- **Squad-rewarding** - Playing with friends provides tangible benefits
- **Community-building** - Systems encourage forming lasting connections
- **Toxicity-resistant** - Design discourages griefing and harassment

---

## 👥 Squad System

### Squad Types

| Type      | Size | Matchmaking   | Description                                       |
| :-------- | :--- | :------------ | :------------------------------------------------ |
| **Solo**  | 1    | Mixed lobbies | Individual player, matched with/against all types |
| **Duo**   | 2    | Mixed lobbies | Two-player team                                   |
| **Squad** | 3-4  | Mixed lobbies | Full team, maximum coordination                   |

### Squad Formation

**Pre-Match Lobby:**
```
┌─────────────────────────────────────────────┐
│  SQUAD LOBBY                    [READY]     │
├─────────────────────────────────────────────┤
│  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐         │
│  │ You │  │ P2  │  │ P3  │  │  +  │         │
│  │READY│  │READY│  │ ... │  │ ADD │         │
│  └─────┘  └─────┘  └─────┘  └─────┘         │
│                                             │
│  [INVITE FRIEND]  [FIND SQUAD]  [START]     │
└─────────────────────────────────────────────┘
```

**Invite Methods:**
1. **Friend List** - Invite from online friends
2. **Recent Players** - Invite from last 20 matches
3. **Clan Members** - Invite from clan roster
4. **Share Code** - Generate 6-digit code (expires in 10 min)
5. **QR Code** - Scan to join (mobile-friendly)

### Squad Roles (Optional Assignment)

Players can assign themselves roles for coordination:

| Role          | Icon | Description                       | Gameplay Benefit                           |
| :------------ | :--- | :-------------------------------- | :----------------------------------------- |
| **Leader**    | 👑    | Shot-caller, extraction decisions | Ping priority on map                       |
| **Point**     | ⚔️    | First into combat                 | Sees enemy outlines 0.5s earlier           |
| **Support**   | ❤️    | Healing priority                  | Healing items 10% more effective on others |
| **Overwatch** | 👁️    | Rear guard, intel                 | Wider minimap range                        |

*Note: Roles are optional quality-of-life, not required*

### Squad Communication

#### Voice Chat

**Channels:**
| Channel       | Scope                | Default Key              | Notes                            |
| :------------ | :------------------- | :----------------------- | :------------------------------- |
| **Squad**     | Your team only       | Always on / Push-to-talk | Primary communication            |
| **Proximity** | Nearby players (15m) | Toggle                   | Can hear enemies too (tactical!) |
| **Mute All**  | Disable incoming     | Settings                 | For solo focus                   |

**Voice Settings:**
- **Voice Volume**: 0-100%
- **Voice Activation**: Push-to-talk / Voice Activity / Muted
- **Voice Threshold**: Sensitivity for voice activation
- **Individual Mute**: Mute specific players

**Anti-Toxicity:**
- Auto-mute after 3 reports
- Voice chat recording for reports (last 60 seconds)
- Offensive language filter (client-side option)

#### Text Chat

**Channels:**
| Channel    | Scope              | Color  |
| :--------- | :----------------- | :----- |
| **Squad**  | Team only          | Green  |
| **All**    | Everyone in match  | White  |
| **System** | Game notifications | Yellow |

**Features:**
- Profanity filter (default ON, toggle OFF in settings)
- Message rate limit (5 messages per 10 seconds)
- Report message button

#### Ping System

**Quick Ping (Single Tap/Click):**
Context-aware ping based on what you're looking at:
| Looking At  | Ping Result      | Voice Callout        |
| :---------- | :--------------- | :------------------- |
| Ground      | "Go here" marker | "Moving here"        |
| Enemy       | "Enemy spotted"  | "Enemy there!"       |
| Loot        | "Loot here"      | "Found something"    |
| Extraction  | "Extract here"   | "Let's extract here" |
| Danger zone | "Danger"         | "Watch out!"         |

**Ping Wheel (Hold):**
```
        [Enemy]
           │
[Need Help] ─┼─ [Go Here]
           │
        [Wait]
```

**Advanced Pings:**
- Double-tap: "Focus fire here!"
- Triple-tap: "Retreat/Cancel"
- Ping on teammate: "Follow them"

**Ping Limits:**
- Max 3 pings per 5 seconds (prevent spam)
- Pings fade after 10 seconds
- Enemy pings last 5 seconds

---

## 🏰 Clan System

### Clan Overview

**What is a Clan?**
A persistent group of players who play together regularly, earning collective rewards and competing in events.

**Clan Limits:**
| Tier         | Max Members | Creation Cost   | Benefits                               |
| :----------- | :---------- | :-------------- | :------------------------------------- |
| **Starter**  | 10          | Free            | Basic features                         |
| **Standard** | 25          | 10,000 Credits  | Clan bank, custom tag                  |
| **Premium**  | 50          | 50,000 Credits  | All features, clan challenges          |
| **Elite**    | 100         | 100,000 Credits | Priority matchmaking, exclusive events |

### Clan Creation

**Requirements:**
- Account Level 10+
- Creation cost (or earned through gameplay)
- Unique clan name (3-20 characters)
- Unique clan tag (2-5 characters)

**Customization:**
- Clan Name: "Shadow Wolves"
- Clan Tag: [WOLF]
- Clan Description: 200 characters max
- Clan Emblem: Choose from presets or upload (moderated)
- Clan Colors: Primary & Secondary (displayed on clan tag)

### Clan Hierarchy

| Rank        | Permissions                                    | Notes                |
| :---------- | :--------------------------------------------- | :------------------- |
| **Leader**  | All                                            | Founder or appointed |
| **Officer** | Invite/Kick members, bank access, start events | Trusted members      |
| **Veteran** | Invite members, limited bank withdrawal        | Active players       |
| **Member**  | Basic access                                   | Default rank         |
| **Recruit** | View only, 7-day trial                         | New joins            |

### Clan Features

#### 1. Clan Bank

A shared storage for items and credits:

**Deposits:**
- Any member can deposit
- Tracks who deposited what

**Withdrawals:**
- Veterans: 1 item per day
- Officers: 5 items per day
- Leader: Unlimited

**Contents:**
- Credits pool (for clan upgrades)
- Shared weapons/gear (for lower-level members)
- Clan-earned rewards

#### 2. Clan Challenges

Weekly objectives that all clan members contribute to:

**Example Challenges:**
| Challenge        | Requirement                 | Reward                   |
| :--------------- | :-------------------------- | :----------------------- |
| Extract Together | Squad extract 50 times      | 50,000 Credits (split)   |
| Total Kills      | Clan total 1,000 kills      | Exclusive emblem         |
| Loot Hoarders    | Extract 500 rare+ items     | Clan XP boost (24h)      |
| Faction Focus    | Complete 100 faction quests | Faction reputation boost |

#### 3. Clan Leaderboards

**Categories:**
- Total Clan XP (Season)
- Total Extractions
- Average Survival Rate
- PvP Kills
- Wealth Accumulated

**Rewards by Ranking:**
| Rank     | Season Reward                           |
| :------- | :-------------------------------------- |
| Top 1    | Legendary Clan Banner + 500,000 Credits |
| Top 10   | Epic Clan Banner + 200,000 Credits      |
| Top 100  | Rare Clan Banner + 50,000 Credits       |
| Top 1000 | Uncommon Banner + 10,000 Credits        |

#### 4. Clan Chat

**Channels:**
- **General** - All members
- **Officers** - Officers+ only
- **Events** - Scheduling and coordination
- **Trading** - Item exchange between members

**Features:**
- Persistent chat history (7 days)
- @mentions for notifications
- Pinned messages (Officers+)

#### 5. Clan Events

**Types:**
| Event                   | Description              | Reward                            |
| :---------------------- | :----------------------- | :-------------------------------- |
| **Raid Night**          | Scheduled squad sessions | Bonus XP                          |
| **Internal Tournament** | 1v1 or squad battles     | Bragging rights + clan bank bonus |
| **Faction Push**        | Focus on one faction     | Boosted reputation                |
| **Training**            | Veterans help Recruits   | Loyalty points                    |

---

## 👫 Friends System

### Friend List

**Features:**
- Add friends via username, code, or QR
- Online/Offline/In-Match status
- "Last Online" timestamp
- Favorite friends (pinned to top)
- Notes (personal reminders about friends)

**Friend Limit:** 100 friends (expandable with premium)

### Friend Categories

| Category         | Description                   |
| :--------------- | :---------------------------- |
| **Favourites** ⭐ | Pinned to top, quick invite   |
| **Clan** 🏰       | Auto-categorized clan members |
| **Recent** 🕐     | Last 24 hours played together |
| **All** 👥        | Full friend list              |
| **Blocked** 🚫    | Cannot contact you            |

### Friend Interactions

**From Friend List:**
- Invite to Squad
- Invite to Clan
- Send Message
- View Profile
- Compare Stats
- Send Gift (cosmetics, credits)
- Unfriend / Block

### Social Presence

**Status Options:**
| Status             | Icon | Description        |
| :----------------- | :--- | :----------------- |
| **Online**         | 🟢    | Available          |
| **In Match**       | 🔴    | Currently playing  |
| **In Lobby**       | 🟡    | In pre-match lobby |
| **Away**           | 🟠    | Idle 10+ minutes   |
| **Do Not Disturb** | ⛔    | Blocks invites     |
| **Invisible**      | ⚫    | Appears offline    |

---

## 🎁 Social Rewards

### Play Together Bonuses

**Squad Bonuses:**
| Squad Size     | XP Bonus | Credit Bonus |
| :------------- | :------- | :----------- |
| Solo           | 0%       | 0%           |
| Duo            | +10%     | +5%          |
| Trio           | +15%     | +10%         |
| Full Squad (4) | +25%     | +15%         |

**Friend Bonuses (stacks):**
| Condition                           | Additional Bonus |
| :---------------------------------- | :--------------- |
| Playing with Friend                 | +5% XP           |
| Playing with Clan Member            | +10% XP          |
| First match with new Friend         | +50 XP flat      |
| Complete 10 matches with same squad | Loyalty Badge    |

### Referral System

**How It Works:**
1. Generate referral code
2. New player uses code during signup
3. Both players earn rewards as referred player progresses

**Rewards:**
| Milestone        | Referrer Gets            | New Player Gets  |
| :--------------- | :----------------------- | :--------------- |
| Account Created  | 500 Credits              | 1,000 Credits    |
| Level 5          | 2,000 Credits            | 2,000 Credits    |
| Level 10         | Rare Weapon Skin         | Rare Weapon Skin |
| Level 20         | 10,000 Credits           | 10,000 Credits   |
| First Extraction | Exclusive Referral Badge | Welcome Badge    |

**Referral Limit:** 50 successful referrals per account

---

## 🔇 Anti-Toxicity Systems

### Report System

**Report Categories:**
| Category             | Severity   | Action                          |
| :------------------- | :--------- | :------------------------------ |
| Cheating/Hacking     | 🔴 Critical | Immediate review, potential ban |
| Abusive Voice/Text   | 🟠 High     | Mute + review                   |
| Griefing/Teamkilling | 🟠 High     | Behavior score impact           |
| Inappropriate Name   | 🟡 Medium   | Forced name change              |
| AFK/Abandonment      | 🟡 Medium   | Matchmaking penalty             |
| Other                | 🟢 Low      | Manual review                   |

**Report Process:**
1. Select player from scoreboard or kill feed
2. Choose category
3. Optional: Add description (100 char)
4. Optional: Attach clip (last 60 seconds auto-saved)
5. Submit

**Feedback:**
- Notification when action is taken ("A player you reported has been penalized")
- No details about specific punishment (privacy)

### Behavior Score

**Hidden score** affecting matchmaking and privileges:

**Factors:**
| Action                   | Impact |
| :----------------------- | :----- |
| Complete match           | +1     |
| Extract successfully     | +2     |
| Receive commendation     | +5     |
| Reported (confirmed)     | -20    |
| Abandon match            | -10    |
| Teamkill (friendly fire) | -15    |
| Chat violation           | -10    |

**Score Effects:**
| Score Range | Effect                         |
| :---------- | :----------------------------- |
| 100-80      | Normal matchmaking             |
| 79-50       | Matched with similar scores    |
| 49-20       | Chat restricted, warning       |
| Below 20    | Temporary ban, appeal required |

### Commendation System

**Positive reinforcement:**

After each match, players can commend teammates:
| Category           | Description                          |
| :----------------- | :----------------------------------- |
| **Good Teammate**  | Communicated well, played objectives |
| **Skilled Player** | Impressive gameplay                  |
| **Friendly**       | Positive attitude                    |
| **Leader**         | Made good calls                      |

**Rewards:**
- 10 commendations = 500 Credits
- 50 commendations = "Good Sport" badge
- 100 commendations = Exclusive emote

---

## 📱 Mobile Social Features

### Quick Social Access

**Floating Social Button:**
- Always accessible during menus
- Shows online friend count
- Notification dot for invites

### Simplified Voice Chat

**Mobile Optimizations:**
- Large push-to-talk button
- Voice activity with smart threshold
- Automatic noise suppression
- Low-bandwidth codec (Opus)

### Share Features

**One-Tap Sharing:**
- Share match results to social media
- Share extraction loot
- Share clan achievements
- Generate shareable profile cards

---

## 🔄 Cross-Platform Ecosystem (Powered by EOS)

### 🌐 Epic Online Services (EOS) Integration

We utilize **Epic Online Services** to provide a seamless multiplayer experience across all devices.

**Benefits for Players:**
*   **One Identity:** Log in with your preferred platform (Steam, PlayStation, Xbox, Google, Apple), and it links to a backend Epic Account. Your progress travels with you.
*   **Universal Friends List:** See friends from *all* platforms in one list. If you are on Steam, you can still see and invite your friend playing on PlayStation.
*   **Cross-Platform Voice:** High-quality voice chat that works between mobile and PC without third-party apps.

### 🎮 Unified Lobbies & Parties

**The "Smart Lobby" System:**
*   **Persistent Parties:** Your squad stays together after the match ends. No need to re-invite.
*   **Drop-In/Drop-Out:** Friends can join your lobby while you are in the main menu (if set to "Friends Only").
*   **Cross-Platform Invites:** Send game invites directly to a friend's device, regardless of what platform they are on, using the EOS Overlay or in-game Social Panel.

### ⚔️ Cross-Play Matchmaking

| Option                  | Description                                            | Default |
| :---------------------- | :----------------------------------------------------- | :------ |
| **Enable Cross-Play**   | Match with other platforms via EOS Matchmaking         | ON      |
| **Input Matchmaking**   | Prioritize same input type (controller/touch/KB+M)     | OFF     |
| **Platform Indicators** | Icons showing if a player is on PC, Console, or Mobile | ON      |

---

## 📊 Social Analytics (Backend)

### Metrics to Track

**Squad Formation:**
- % solo vs squad players
- Average squad size
- Friend vs random squad ratio

**Communication:**
- Voice chat usage rate
- Ping usage frequency
- Chat message volume

**Clan Health:**
- Average clan size
- Clan retention rate
- Clan activity (matches/week)

**Toxicity:**
- Report rate per match
- Commendation vs report ratio
- Behavior score distribution

---

## 🚀 Social Features Roadmap

### Launch (v1.0)
- ✅ Squad system (1-4 players)
- ✅ Voice chat (squad + proximity)
- ✅ Ping system
- ✅ Friends list
- ✅ Basic reporting

### Post-Launch (v1.1 - Month 2)
- Clan system (basic)
- Clan chat
- Referral program

### Season 2 (v1.2 - Month 3)
- Clan challenges
- Clan leaderboards
- Commendation system

### Future
- Clan wars events
- Mentorship program
- Community tournaments

---

**[← Back to Index](../README.md)** | **[Next: Core Gameplay →](../GameDesign/CoreGameplay.md)**
