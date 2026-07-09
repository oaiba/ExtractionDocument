---
title: "Social & Multiplayer hệ thống"
type: docs
---

## Social Design Philosophy

**cốt lõi Principle:** *"Alone is viable, together is powerful"*

The social layer is the connective tissue that transforms a session-based extraction shooter into a living community. Every hệ thống must reinforce three pillars:

| Pillar                 | mục tiêu                                                                 |
| :--------------------- | :------------------------------------------------------------------- |
| **Meaningful Risk**    | Social interactions carry weight vì betrayal và trust are real. |
| **Emergent Stories**   | hệ thống tạo memorable, shareable moments organically.             |
| **Community Longevity** | người chơi form bonds that extend beyond a single session.              |

**Design Tenets:**
- **Solo-friendly** — Solo Người chơi có thể succeed mà không feeling disadvantaged.
- **Squad-rewarding** — Playing với friends provides tangible, non-exploitative benefits.
- **Community-building** — hệ thống encourage forming lasting connections.
- **Toxicity-resistant** — Design discourages griefing và harassment thông qua cơ chế, not just moderation.
- **Trust as Currency** — Trust is earned thông qua actions, not granted by a UI element.

> *Reference: Escape from Tarkov, Hunt: Showdown, DMZ, Dark và Darker, ARC Raiders*

<!--  IMAGE PLACEHOLDER: Infographic showing the Social Design Pillars và how they connect to each game hệ thống -->

---

## Squad hệ thống

### Squad Types & Lobby Configuration

| Type      | Size | Matchmaking Pool | Description                                       |
| :-------- | :--- | :--------------- | :------------------------------------------------ |
| **Solo**  | 1    | Mixed lobbies    | Individual người chơi, matched với/against all types |
| **Duo**   | 2    | Mixed lobbies    | Two-người chơi team                                   |
| **Squad** | 3-4  | Mixed lobbies    | Full team, maximum coordination                   |

> **Design Note (Hunt: Showdown Reference):** Mixed lobbies (solos vs. squads) tạo tension và emergent stories. Dedicated solo-only modes fracture the người chơi base — instead, we cách dùng MMR adjustments và underdog bonuses to make solos competitive against teams (Xem [Matchmaking chi tiết](#-matchmaking-chi tiết)).

<!--  IMAGE PLACEHOLDER: Screenshot reference of Hunt: Showdown's squad size selection màn hình -->

### Squad Formation

**Pre-Match Lobby:**
```
┌───────────────────────────────────────────────────┐
│  SQUAD LOBBY                          [READY]     │
├───────────────────────────────────────────────────┤
│  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐       │
│  │  You  │  │  P2   │  │  P3   │  │   +   │       │
│  │ READY │  │ READY │  │  ...  │  │  ADD  │       │
│  │ Lv.32 │  │ Lv.28 │  │ Lv.15 │  │       │       │
│  │[ROLE] │  │[ROLE] │  │[ROLE] │  │       │       │
│  └───────┘  └───────┘  └───────┘  └───────┘       │
│                                                   │
│  Gear Value: ████████░░ [285,000₽]                │
│  Squad Karma:  (Good Standing)            │
│                                                   │
│  [INVITE]  [FIND SQUAD]  [LFG POST]  [DEPLOY]     │
└───────────────────────────────────────────────────┘
```

<!--  IMAGE PLACEHOLDER: UI mockup of the Squad Lobby màn hình với gear giá trị indicator và karma display -->

**Invite Methods:**
1. **Friend List** — Invite from online friends
2. **Recent người chơi** — Invite from last 20 matches
3. **Clan Members** — Invite from clan roster
4. **Share Code** — Generate 6-digit code (expires in 10 min)
5. **QR Code** — Scan to join (mobile-friendly)
6. **LFG Board** — Post hoặc browse looking-for-group listings (Xem [LFG hệ thống](#-lfg-looking-for-group-hệ thống))

### Squad Roles (Optional Assignment)

Người chơi có thể assign themselves roles for coordination — these are optional quality-of-life tools, **not** class-locks:

| Role          | Icon | Description                       | Gameplay Benefit                           |
| :------------ | :--- | :-------------------------------- | :----------------------------------------- |
| **Leader**    |    | Shot-caller, extraction quyết định | Ping priority on map, waypoints for squad  |
| **Point**     |    | First into combat                 | Sees địch outlines 0.5s earlier           |
| **Support**   |    | Healing priority                  | Healing items 10% more effective on others |
| **Overwatch** |    | Rear guard, intel                 | Wider minimap range                        |

> **Design Note:** Roles display as small icons next to the người chơi name in the HUD và squad panel. They giúp với quick visual communication trong khi combat.

<!--  IMAGE PLACEHOLDER: HUD mockup showing squad member frames với role icons, máu bars, và status indicators -->

---

## Communication hệ thống

### Voice Chat (VOIP)

Voice communication is a **cốt lõi tactical tool**, not just a social tính năng. Inspired by Tarkov's VOIP hệ thống, speech has *consequences*.

#### Voice Channels

| Channel            | Scope                       | Default chính              | ghi chú                                                                 |
| :----------------- | :-------------------------- | :----------------------- | :-------------------------------------------------------------------- |
| **Squad**          | Your team only              | Always on / Push-to-talk | primary communication. Encrypted — địch cannot intercept.          |
| **Proximity**      | Nearby người chơi (15m radius) | Toggle                   | **Can hear và be heard by địch.** Critical for dynamic encounters. |
| **Proximity Fade** | 15m–30m                     | Automatic                | Voice attenuates với distance. Muffled beyond walls/obstacles.       |
| **Mute All**       | Disable incoming            | Settings                 | For solo focus                                                        |

#### Spatial Audio for Voice

Proximity voice chat uses **3D spatial audio**:
- Voice direction is accurately represented (left/right ear panning)
- Volume attenuates based on distance (inverse square falloff)
- Walls và obstacles **muffle** voice (occlusion filter)
- Indoor vs. outdoor environments affect reverb (environment-aware processing)

> *Reference: Tarkov's VOIP hệ thống allows negotiations, cease-fires, và betrayals via proximity chat. Many iconic extraction shooter moments are born from VOIP interactions.*

<!--  IMAGE PLACEHOLDER: Diagram showing proximity voice range (15m full clarity, 15-30m fade zone) với spatial audio direction indicators -->

#### Tactical Voice Usage

Unlike traditional shooters, voice chat in an extraction shooter has **tactical weight**:

| Scenario                 | Risk                                                  | Reward                                         |
| :----------------------- | :---------------------------------------------------- | :--------------------------------------------- |
| Calling out to a stranger | They now know your position và that you're alone/weak | Could negotiate a ceasefire hoặc trade            |
| Staying silent            | Miss opportunity for cooperation                      | Maintain tactical advantage (stealth)           |
| Fake callout             | nếu discovered, trust is permanently broken             | Could bait địch into an ambush               |
| cảnh báo a stranger       | Reveal your position                                   | Build trust for co-op extract (karma bonus)     |

#### Voice Settings

- **Voice Volume**: 0-100%
- **Voice Activation**: Push-to-talk / Voice Activity / Muted
- **Voice Threshold**: Sensitivity for voice activation
- **Individual Mute**: Mute cụ thể người chơi
- **Spatial Audio Toggle**: Enable/disable 3D voice positioning
- **VOIP Bandwidth**: Low (16kbps Opus) / Medium (24kbps) / High (48kbps)

#### Voice Anti-Abuse

- Auto-mute sau 3 confirmed reports
- Voice chat recording for reports (rolling last 60 seconds buffer)
- Offensive language filter (client-side option, default ON)
- Music/noise detection: Auto-warn → Auto-mute sau repeated offenses
- VOIP ban tiers: 24h → 7d → 30d → Permanent (for repeated violations)

### Text Chat

**Channels:**
| Channel    | Scope             | Color  |
| :--------- | :----------------- | :----- |
| **Squad**  | Team only          | Green  |
| **All**    | Everyone in match  | White  |
| **hệ thống** | Game notifications | Yellow |

**tính năng:**
- Profanity filter (default ON, toggle OFF in settings)
- Message rate limit (5 messages per 10 seconds)
- Report message button (right-click on message)
- Persistent chat log trong khi match (scrollable, 200 message buffer)

### Ping hệ thống

#### Quick Ping (Single Tap)

Context-aware ping based on what you're looking at:

| Looking At     | Ping kết quả         | Voice Callout        | Color  |
| :------------- | :------------------ | :------------------- | :----- |
| Ground/Floor   | "Go here" marker    | "Moving here"        | Blue   |
| địch          | "địch spotted"     | "địch there!"       | Red    |
| Loot (item)    | "Loot here"         | "Found something"    | Gold   |
| Extraction POI | "Extract here"      | "Let's extract here" | Green  |
| Danger zone    | "Danger"            | "Watch out!"         | Orange |
| Teammate       | "Follow them"       | "On them"            | Cyan   |

<!--  IMAGE PLACEHOLDER: In-game screenshot showing different colored ping markers on the HUD và minimap -->

#### Ping Wheel (Hold)

```
              [ENEMY]
                │
  [NEED HELP] ──┼── [GO HERE]
                │
     [WAIT] ────┼── [REGROUP]
                │
            [EXTRACT]
```

#### Advanced Ping cơ chế

- **Double-tap**: "Focus fire here!" (flashing red marker)
- **Triple-tap**: "Retreat / Cancel" (flashing orange 'X')
- **Ping on teammate**: "Follow them" (directional arrow)
- **Ping on loot**: Shows item name và rarity to squad

**Ping Limits:**
- Max 3 pings per 5 seconds (prevent spam)
- Standard pings fade sau 10 seconds
- địch pings last 5 seconds (địch move — stale info is dangerous)
- Extract pings persist until cancelled

---

## Karma & Trust hệ thống

> *Inspired by Escape from Tarkov's Scav Karma và PMC Karma hệ thống. The karma hệ thống transforms người chơi morality from an abstract concept into a tangible game cơ chế với real consequences.*

### Design Philosophy

The Karma hệ thống tạo a **reputation economy** where người chơi behavior has lasting consequences. It answers a cốt lõi extraction shooter question: *"Should I shoot first, hoặc try to cooperate?"*

<!--  IMAGE PLACEHOLDER: Conceptual art showing two người chơi in a standoff — one với a "Trusted" aura, one với a "Hostile" marker -->

### Karma Score

**Hidden Score** (0–1000, starting at 500):

| Range        | Tier               | Visual Indicator                     |
| :----------- | :------------------ | :----------------------------------- |
| 800–1000     |  **Trusted**      | Green glow on người chơi card            |
| 600–799      |  **Honorable**    | Blue border on người chơi card           |
| 400–599      |  **Neutral**       | Default appearance                   |
| 200–399      |  **Suspicious**   | Orange cảnh báo on người chơi card        |
| 0–199        |  **Hostile**      | Red skull icon, hostile AI behavior  |

> **Design Note:** The exact score is hidden. người chơi only see their tier thông qua visual indicators on their profile và in-game.

### Karma Actions

#### Positive Actions (Karma Gain)

| Action                           | Karma Change | ghi chú                                    |
| :------------------------------- | :----------- | :--------------------------------------- |
| Complete a raid mà không PvP kills | +5           | Peaceful extraction rewarded             |
| cách dùng co-op extraction point       | +15          | Both parties must extract together       |
| Revive a random teammate (LFG)   | +10          | Only với non-friend squad members       |
| Share loot với squad (drop item) | +3           | Detected khi teammate picks up          |
| Receive commendation             | +8           | From post-match commendation hệ thống      |
| Complete Fence/Peacekeeper quest | +5           | Faction-tied karma restoration           |
| Report confirmed cheater         | +2           | Only on confirmed bans                   |

#### Negative Actions (Karma Loss)

| Action                          | Karma Change | ghi chú                                          |
| :------------------------------ | :----------- | :---------------------------------------------- |
| Kill a Trusted/Honorable người chơi unprovoked | -20 | First shot determines aggressor                |
| Teamkill (friendly fire)        | -25          | Accidental vs. intentional detected via pattern |
| Abandon match (disconnect)      | -15          | Grace period: 60s reconnect window              |
| Betray co-op extraction partner | -30          | Killing someone trong khi co-op extract sequence   |
| Camp extraction point (detected) | -10         | Stationary in extract zone for 3+ min mà không extracting |
| Confirmed grief report          | -20          | Manual review required                          |

<!--  IMAGE PLACEHOLDER: UI mockup showing Karma change notification ("+15 Co-op Extract Bonus" hoặc "-20 Unprovoked Kill") -->

### Karma Consequences

| Tier            | Effects                                                                                                   |
| :-------------- | :-------------------------------------------------------------------------------------------------------- |
|  **Trusted**   | Reduced Scav/AI aggression, better vendor prices (-5%), access to exclusive co-op extract points, priority LFG |
|  **Honorable** | Standard vendor prices, normal AI behavior, "Honorable" badge                                             |
|  **Neutral**    | Default trải nghiệm                                                                                        |
|  **Suspicious** | AI patrols are more alert near you, vendors charge 10% more, LFG queue disadvantage                       |
|  **Hostile**   | AI bosses actively hunt you, vendors refuse rare items, matchmade với other Hostile người chơi, bounty on head |

> *Reference: Tarkov's PMC Karma hệ thống introduced a boss (Partisan) who specifically hunts low-karma người chơi. We adapt this concept — at Hostile tier, special AI "Bounty Hunters" spawn và track the người chơi.*

### Karma Recovery

- **Natural Decay**: Negative karma slowly recovers (+2/day of active play) toward Neutral.
- **Redemption Quests**: Special "Peacekeeper" quests available at Suspicious tier to recover faster.
- **Community dịch vụ**: Helping new người chơi (mentorship program) grants karma bonuses.
- **Season Reset**: Partial reset at season boundaries (pulled toward 500 by 30%).

<!--  IMAGE PLACEHOLDER: Flowchart showing Karma tier progression, actions that move người chơi up/down, và the consequences at each tier -->

---

## In-Raid Dynamic Interactions

> *The most memorable moments in extraction shooters happen thông qua unscripted người chơi encounters. These hệ thống facilitate (nhưng never force) cooperation và betrayal.*

### Co-op Extraction Points

cụ thể extraction points require **two hoặc more unrelated người chơi** to activate simultaneously:

```
┌──────────────────────────────────────────────────────┐
│  CO-OP EXTRACTION: "Bridge Checkpoint"               │
│                                                      │
│  Requires: 2 players from different squads           │
│  Timer: 30 seconds (both must remain in zone)        │
│  Reward: +15 Karma, +25% bonus loot, rare item roll  │
│                                                      │
│  ┌─────────┐           ┌─────────┐                   │
│  │ Player A│◄── 10m ──►│ Player B│                   │
│  │ (Squad1)│           │ (Solo)  │                   │
│  └─────────┘           └─────────┘                   │
│                                                      │
│  Status: WAITING FOR SECOND PLAYER...                │
└──────────────────────────────────────────────────────┘
```

> *Reference: Tarkov's Scav/PMC co-op extracts are among the most tense và rewarding moments in the game. The trust required tạo powerful emergent narratives.*

<!--  IMAGE PLACEHOLDER: Screenshot reference of Tarkov's co-op extraction point (e.g., Scav Camp on Interchange) -->

### Temporary Alliances

**Ceasefire cơ chế:**
1. **White Flag Gesture** — Performing the "ceasefire" emote lowers your vũ khí for 3 seconds (vulnerable trạng thái)
2. **Proximity VOIP Negotiation** — cách dùng voice chat to propose terms
3. **Item Exchange** — Drop items on ground as a show of good faith
4. **Alliance Timer** — nếu both người chơi don't fire for 30 seconds within 10m, a "Temporary Truce" icon appears for both

**Alliance Risks:**
- No cơ chế binding — either người chơi can break the truce at any thời gian
- Breaking a truce sau "Temporary Truce" icon = **-30 Karma** (betrayal penalty)
- Alliances dissolve nếu người chơi move more than 50m apart for 60 seconds

### Betrayal hệ thống

**Why Include Betrayal?**

Betrayal is a tính năng, not a bug. It tạo the tension that defines the genre. However, it must have consequences:

| Betrayal Type         | Detection Method                    | Consequence                               |
| :-------------------- | :---------------------------------- | :---------------------------------------- |
| Break Temporary Truce | Timer-based (30s peace → kill)      | -30 Karma, "Traitor" tag for 3 matches    |
| Kill trong khi Co-op Extract | Proximity + extract zone detection | -30 Karma, banned from co-op extracts 24h |
| Teamkill in Squad     | Friendly fire tracking              | -25 Karma, auto-kick from squad           |

<!--  IMAGE PLACEHOLDER: Storyboard showing a dynamic interaction sequence: two strangers meet, negotiate via VOIP, exchange items, và either cooperate hoặc betray -->

---

## Emote & Gesture hệ thống

> *Non-verbal communication is critical khi proximity VOIP might reveal your position to unintended listeners. Emotes provide a silent alternative.*

### Quick Gestures (Tactical)

These are **silent, fast animations** that don't lower your vũ khí:

| Gesture        | chính  | Animation                  | Duration | cách dùng Case                         |
| :------------- | :--- | :------------------------- | :------- | :------------------------------- |
| **Stop**       | G1   | Closed fist raised         | 0.5s     | Signal squad to halt             |
| **Move Up**    | G2   | Open hand sweep forward    | 0.5s     | Signal to advance                |
| **địch**      | G3   | Pointed finger + direction | 0.5s     | Silent địch callout             |
| **Follow Me**  | G4   | Beckoning wave             | 0.5s     | Lead the squad                   |
| **Cover Me**   | G5   | Tap own shoulder           | 0.5s     | Request covering fire            |

### Social Emotes (Expressive)

These are **longer animations** that may lower your vũ khí (vulnerable trạng thái):

| Emote             | Animation                     | Duration | ghi chú                                    |
| :---------------- | :---------------------------- | :------- | :--------------------------------------- |
| **Wave**          | Friendly wave                 | 1.5s     | Non-threatening greeting                 |
| **Ceasefire**     | Both hands raised, vũ khí lowered | 2.0s | Signals peaceful intent (Xem [Temporary Alliances](#temporary-alliances)) |
| **Thumbs Up**     | Thumbs up gesture             | 1.0s     | Acknowledgment / approval               |
| **Come Here**     | Beckoning với vũ khí lowered | 1.5s     | Invite stranger to approach              |
| **Shrug**         | Exaggerated shrug             | 1.5s     | "I don't know" / "Your call"            |
| **Surrender**     | Hands up, kneel               | 3.0s     | Full surrender pose (longest vulnerability) |
| **Celebration**   | Fist pump / Victory pose      | 2.0s     | Post-kill hoặc post-extract celebration    |

> *Reference: Dark và Darker's surrender emote has become iconic — it allows người chơi to negotiate mà không words, tạo memorable dungeon encounters.*

### Emote Wheel

```
             [STOP ]
                │
  [CEASEFIRE] ──┼── [WAVE ]
                │
   [ENEMY ] ──┼── [FOLLOW ]
                │
            [THUMBS UP ]
```

**Access:** Hold `T` (default) → Select với mouse → Release to execute.

### Emote Customization

- **8 emote slots** (4 tactical + 4 social) customizable in loadout
- **Earn emotes** thông qua: Battle Pass, Clan achievements, Commendation milestones, Store
- **Faction-cụ thể emotes** unlock at high faction reputation (e.g., military salute for BEAR faction equivalent)

<!--  IMAGE PLACEHOLDER: UI mockup of the Emote Wheel với tactical gestures on the left và social emotes on the right -->

<!--  IMAGE PLACEHOLDER: In-game screenshot showing a người chơi performing the "Ceasefire" emote với hands raised -->

---

## LFG (Looking for Group) hệ thống

> *External LFG (Discord, Reddit) fragments the community và excludes người chơi who don't cách dùng third-party tools. A built-in LFG hệ thống keeps matchmaking social và accessible.*

### LFG Board

**Location:** Accessible from Main Menu → Social Tab → LFG Board

```
┌──────────────────────────────────────────────────────────────┐
│   LOOKING FOR GROUP                        [CREATE POST]   │
├──────────────────────────────────────────────────────────────┤
│  Filter: [Map ▼] [Squad Size ▼] [Language ▼] [Playstyle ▼]   │
├──────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────────┐  │
│  │  "NightWolf_42" [ Karma]       Duo → Need 1  │  │
│  │    Map: Factory | Playstyle: Aggressive | Mic: Yes     │  │
│  │    Note: "Looking for confident player, quick raid"    │  │
│  │    [JOIN REQUEST]                           2 min ago  │  │
│  ├────────────────────────────────────────────────────────┤  │
│  │  "MedkitMary" [ Karma]         Squad → Need 2 │ │
│  │    Map: Any | Playstyle: Loot Run | Mic: Preferred     │  │
│  │    Note: "Chill loot run, helping new players"         │  │
│  │    [JOIN REQUEST]                           5 min ago  │  │
│  ├────────────────────────────────────────────────────────┤  │
│  │  "HatchetRunner" [ Karma]      Duo → Need 1  │  │
│  │    Map: Customs | Playstyle: Quest | Mic: Optional     │  │
│  │    Note: "Need help with Quest: Find Documents"        │  │
│  │    [JOIN REQUEST]                          12 min ago  │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  [← Prev Page]  Page 1 of 24  [Next Page →]                  │
└──────────────────────────────────────────────────────────────┘
```

<!--  IMAGE PLACEHOLDER: UI mockup of the LFG Board với filter controls và người chơi listings -->

### LFG Post Fields

| Field            | Type         | Options                                                 |
| :--------------- | :----------- | :------------------------------------------------------- |
| **Squad Size**   | Dropdown     | Duo (need 1), Trio (need 1-2), Quad (need 1-3)          |
| **Map**          | Dropdown     | Any, hoặc cụ thể map name                                |
| **Playstyle**    | Tag Select   | Aggressive, Stealthy, Loot Run, Quest Focus, PvP Hunt   |
| **Mic Required** | Toggle       | Yes / Preferred / No                                     |
| **Language**     | Dropdown     | Auto-detected, hoặc manual selection                       |
| **Note**         | Free text    | 100 nhân vật max                                       |
| **Level Range**  | Slider       | Min-Max level filter for applicants                      |

### LFG Matching Intelligence

- **Karma Display**: Each LFG post shows the poster's Karma tier (star rating)
- **Playstyle Tag Matching**: Posts với matching playstyle tags appear first
- **Region Priority**: Posts from your region appear first (lower latency)
- **New người chơi Friendly**: Posts tagged "Helping Newbies" get a boost in visibility
- **Auto-Expire**: Posts expire sau 30 minutes hoặc khi squad is full

---

## Clan hệ thống

### Clan Overview

A **Clan** is a persistent community of người chơi who play regularly together, earning collective rewards và competing in events. Clans are the primary vehicle for long-term social engagement.

**Clan Tiers:**
| Tier         | Max Members | Creation chi phí   | Benefits                                         |
| :----------- | :---------- | :-------------- | :----------------------------------------------- |
| **Starter**  | 10          | Free            | Basic tính năng, clan chat, shared tag             |
| **Standard** | 25          | 10,000 Credits  | Clan bank, custom tag, clan challenges (basic)    |
| **Premium**  | 50          | 50,000 Credits  | All tính năng, advanced challenges, clan emblem    |
| **Elite**    | 100         | 100,000 Credits | Priority matchmaking, exclusive events, clan wars |

### Clan Creation

**yêu cầu:**
- Account Level 10+
- Creation chi phí (hoặc earn thông qua gameplay milestones)
- Unique clan name (3-20 nhân vật, profanity filtered)
- Unique clan tag (2-5 nhân vật, displayed as `[TAG]`)

**Customization:**
- **Clan Name**: e.g., "Shadow Wolves"
- **Clan Tag**: e.g., `[WOLF]`
- **Clan Description**: 200 nhân vật max
- **Clan Emblem**: Choose from presets hoặc upload (moderated, reviewed within 24h)
- **Clan Colors**: primary & secondary (displayed on clan tag và banner)
- **Clan Motto**: Short tagline (50 nhân vật max)

<!--  IMAGE PLACEHOLDER: UI mockup of the Clan Creation màn hình với emblem editor, color picker, và preview -->

### Clan Hierarchy

| Rank        | Permissions                                                | ghi chú                    |
| :---------- | :--------------------------------------------------------- | :----------------------- |
| **Leader**  | All permissions, transfer leadership, disband clan         | Founder hoặc appointed     |
| **Officer** | Invite/Kick members, bank access, start events, edit MOTD  | Trusted members (max 5)  |
| **Veteran** | Invite members, limited bank withdrawal, vote in polls     | Active người chơi (auto-promote sau 30 days) |
| **Member**  | Basic access, deposit to bank, join events                 | Default rank             |
| **Recruit** | View-only, 7-day trial period, limited chat                | New joins                |

> **Design Note:** Auto-promotion reduces officer workload. sau 30 days of active play (10+ matches as Member), người chơi auto-promote to Veteran.

### Clan tính năng

#### 1. Clan Bank (shared Stash)

A shared storage for items và credits that tạo a sense of collective investment:

**Deposits:**
- Any member can deposit items và credits
- Tracks who deposited what (full audit log)
- Deposits increase "Clan Contribution Score" for the depositor

**Withdrawals:**
| Rank        | Daily Withdrawal Limit | ghi chú                    |
| :---------- | :--------------------- | :----------------------- |
| **Recruit** | None                   | Cannot withdraw          |
| **Member**  | 1 item hoặc 1,000 ₽      | Basic access             |
| **Veteran** | 3 items hoặc 5,000 ₽     | —                        |
| **Officer** | 10 items hoặc 20,000 ₽   | —                        |
| **Leader**  | Unlimited              | Full access              |

**Contents:**
- Credits pool (for clan upgrades)
- shared vũ khí/gear (for equipping lower-level members)
- Clan-earned rewards (trophies, seasonal rewards)

<!--  IMAGE PLACEHOLDER: UI mockup of the Clan Bank inventory màn hình với deposit/withdraw buttons và audit log -->

#### 2. Clan Challenges

Weekly objectives that all clan members contribute toward collectively:

| Challenge            | yêu cầu                | Reward                    |
| :------------------- | :------------------------- | :------------------------ |
| **Extract Together** | Squad extract 50 times     | 50,000 Credits (split)    |
| **Total Kills**      | Clan total 1,000 kills     | Exclusive emblem          |
| **Loot Hoarders**    | Extract 500 rare+ items    | Clan XP boost (24h)       |
| **Faction Focus**    | Complete 100 faction quests | Faction reputation boost  |
| **Co-op Heroes**     | 20 co-op extractions       | Rare cosmetic for all     |
| **Survival Masters** | 80% avg. survival rate     | Clan banner upgrade       |

#### 3. Clan Leaderboards

**Categories:**
- Total Clan XP (Season)
- Total Extractions
- Average Survival Rate
- PvP Kills
- Wealth Accumulated
- Co-op Extractions (promotes positive play)

**Season Rewards by Ranking:**
| Rank     | Reward                                    |
| :------- | :---------------------------------------- |
| Top 1    | Legendary Clan Banner + 500,000 Credits   |
| Top 10   | Epic Clan Banner + 200,000 Credits        |
| Top 100  | Rare Clan Banner + 50,000 Credits         |
| Top 1000 | Uncommon Banner + 10,000 Credits          |

<!--  IMAGE PLACEHOLDER: UI mockup of the Clan Leaderboard màn hình showing top clans với emblems và stats -->

#### 4. Clan Communication

**Channels:**
| Channel       | Access         | mục đích                          |
| :------------ | :------------- | :------------------------------- |
| **General**   | All members    | General discussion               |
| **Officers**  | Officers+      | Leadership coordination          |
| **Events**    | All members    | Scheduling và raid coordination |
| **Trading**   | Veterans+      | Item exchange between members    |
| **Recruitment** | Officers+    | Discuss applicants               |

**tính năng:**
- Persistent chat history (7 days)
- @mentions for notifications (individual hoặc @role)
- Pinned messages (Officers+, max 10 pins)
- Message of the Day (MOTD) — displayed on clan trang load

#### 5. Clan Events

| Event                   | Description                         | Reward                            |
| :---------------------- | :---------------------------------- | :-------------------------------- |
| **Raid Night**          | Scheduled squad sessions (calendar) | Bonus XP for all participants     |
| **Internal Tournament** | 1v1 hoặc squad battles (custom match) | Bragging rights + clan bank bonus |
| **Faction Push**        | Focus raids on one faction's map    | Boosted faction reputation        |
| **Training**            | Veterans giúp Recruits              | Loyalty points + karma bonus      |
| **Clan Wars**           | Compete against rival clan          | Winner gets exclusive banner      |

<!--  IMAGE PLACEHOLDER: UI mockup of the Clan Events calendar với scheduled Raid Nights và active challenges -->

---

## Friends hệ thống

### Friend List

**tính năng:**
- Add friends via username, share code, hoặc QR
- Online/Offline/In-Match status với activity chi tiết
- "Last Online" timestamp
- Favorite friends (pinned to top, max 10)
- ghi chú (personal reminders about friends, 100 char, private)
- Nickname (set a custom display name for a friend, hiển thị rõ only to you)

**Friend Limit:** 100 friends (expandable to 200 với Premium)

### Friend Categories

| Category         | Icon | Description                        |
| :--------------- | :--- | :--------------------------------- |
| **Favourites**   | ⭐   | Pinned to top, quick invite        |
| **Clan**         |    | Auto-categorized clan members      |
| **Recent**       |    | Last 24 hours played together      |
| **All**          |    | Full friend list                   |
| **pending**      | ⏳   | Sent/Received friend requests      |
| **Blocked**      |    | Cannot contact you                 |

### Friend Interactions

**From Friend List (Right-Click Menu):**
- Invite to Squad
- Invite to Clan
- Send Direct Message
- View Profile & Stats
- Compare Stats (side-by-side)
- Send Gift (cosmetics, credits — daily limit: 3 gifts)
- Spectate (nếu in match và spectating enabled)
- Set Nickname
- Unfriend / Block

### Social Presence

| Status             | Icon | Description                    | Joinable? |
| :----------------- | :--- | :----------------------------- | :-------- |
| **Online**         |    | In menus, available            | Yes       |
| **In Lobby**       |    | In pre-match lobby             | nếu open   |
| **In Match**       |    | Currently in a raid            | No        |
| **In Safe House**  |    | In Safe House (social hub)     | Visit     |
| **Away**           |    | Idle 10+ minutes               | Yes       |
| **Do Not Disturb** |    | Blocks all invites/messages    | No        |
| **Invisible**      |    | Appears offline to all         | No        |

<!--  IMAGE PLACEHOLDER: UI mockup of the Friends List panel showing different status indicators, categories, và right-click context menu -->

---

## Safe House (Social Hub)

> *Inspired by Tarkov's Hideout và ARC Raiders' Social Hub. A persistent safe space where người chơi interact between raids.*

### Hub Overview

The **Safe House** is a personal instanced space that serves as the người chơi's home base. It can also be opened to friends for **social visits**. Full specification: [Safe House Design](../GameDesign/Safe_House_Design.md).

**Functions:**
| Area              | Function                                              |
| :---------------- | :--------------------------------------------------- |
| **Stash Room**    | Manage inventory, sort loot, prepare loadouts         |
| **Workbench**     | Craft items, modify vũ khí, repair gear              |
| **Intel Board**   | View available raids, quest status, map intel         |
| **Trophy Wall**   | Display achievements, rare items, season rewards      |
| **Trading Post**  | Access the Flea Market / người chơi Marketplace           |
| **Squad Planning** | 3D map bảng for tactical planning với squad        |
| **Radio**         | Ambient music selection, faction radio chatter        |

### Social Visits

**How It Works:**
- Friends can "Visit Safe House" from the friend list
- Up to 4 visitors at once
- Visitors can see your trophy wall, kiểm tra your stash (view-only), và cách dùng the squad planning bảng
- Voice chat active trong khi visits (private channel)
- Drop items on the ground to trade với visitors

<!--  IMAGE PLACEHOLDER: Concept art of the Safe House interior showing different functional areas (stash, workbench, trophy wall, intel board) -->

### Trading Post (In-Safe House)

**Direct Trade:**
- Each người chơi places items in a trade window
- Both người chơi must confirm trước exchange
- Trade history logged (audit trail for scam prevention)
- Maximum trade giá trị differential: 10x (anti-RMT measure)

---

## Matchmaking chi tiết

> *Matchmaking is where social design và game balance intersect. The hệ thống must feel fair for solos, duos, và full squads while keeping queue times short.*

### MMR (Matchmaking Rating)

**hệ thống:** Modified ELO / Glicko-2 hybrid

**Rating Components:**
| Component           | Weight | Description                                    |
| :------------------ | :----- | :--------------------------------------------- |
| **Survival Rate**   | 30%    | % of raids successfully extracted              |
| **KDA**             | 25%    | Kill/Death/Assist ratio (PvP only)             |
| **Loot giá trị**      | 20%    | Average extracted loot giá trị per raid           |
| **Quest Completion** | 15%   | Efficiency in completing objectives             |
| **thời gian Survived**   | 10%    | Average raid duration trước death hoặc extract   |

**Star Rating Display:**
| Stars   | MMR Range   | Percentile      |
| :------ | :---------- | :---------------|
|  | 0–500       | Bottom 15%      |
|  | 501–1000    | 15–30%          |
|  | 1001–1500   | 30–55%          |
|  | 1501–2000   | 55–80%          |
|  | 2001–2500   | 80–95%          |
|  | 2501+       | Top 5%          |

> *Reference: Hunt: Showdown uses a similar 1-6 star rating với a modified ELO hệ thống. người chơi want to see a general indicator mà không knowing exact thông số.*

### Squad Matchmaking Balancing

| Scenario         | MMR Adjustment                                               |
| :--------------- | :----------------------------------------------------------- |
| **Solo vs. Lobby** | Solo người chơi's effective MMR reduced by 15% (matched into easier lobbies) |
| **Duo vs. Lobby** | No adjustment                                                |
| **Trio**          | Team MMR = average + 5% bonus (slight upward adjustment)     |
| **Full Squad (4)** | Team MMR = average + 10% bonus (matched against stronger opposition) |

### Underdog Bonus

khi a **solo người chơi** successfully extracts from a lobby với squads:
- **+20% bonus XP**
- **+15% bonus loot giá trị**
- **"Lone Wolf"** post-match badge

> *Reference: Hunt: Showdown awards an "Underdog Bonus" to solo người chơi who extract với a bounty while outnumbered.*

<!--  IMAGE PLACEHOLDER: Diagram showing matchmaking flow: người chơi enters queue → MMR calculation → Squad size adjustment → Lobby filling → Match start -->

### Lobby Composition

**Target Lobby (per map):**
| Map Size   | Total người chơi | Mix Target                       |
| :--------- | :------------ | :------------------------------- |
| Small      | 8-12          | 2-3 squads + 2-4 solos           |
| Medium     | 12-16         | 3-4 squads + 3-5 solos           |
| Large      | 16-20         | 4-5 squads + 4-6 solos           |

**Queue thời gian Targets:**
| Region        | Peak Hours | Off-Peak       |
| :------------ | :--------- | :------------- |
| **Ideal**     | < 30s      | < 60s          |
| **Acceptable** | < 60s     | < 120s         |
| **Fallback**  | < 90s      | Expand MMR range by ±1 star |

---

## Social Rewards

### Play Together Bonuses

**Squad Bonuses:**
| Squad Size     | XP Bonus | Credit Bonus |
| :------------- | :------- | :----------- |
| Solo           | 0%       | 0%           |
| Duo            | +10%     | +5%          |
| Trio           | +15%     | +10%         |
| Full Squad (4) | +25%     | +15%         |

**Friend Bonuses (stacks với squad):**
| Condition                           | Additional Bonus |
| :---------------------------------- | :--------------- |
| Playing với Friend                 | +5% XP           |
| Playing với Clan Member            | +10% XP          |
| First match với new Friend         | +50 XP flat      |
| Complete 10 matches với same squad | "Loyalty" Badge   |
| Complete 50 matches với same squad | "Brothers in Arms" Badge + exclusive skin |

### Referral hệ thống

**How It Works:**
1. Generate unique referral code from Profile → Referral tab
2. New người chơi uses code trong khi account creation
3. Both người chơi earn rewards as the referred người chơi progresses

**Referral Milestones:**
| Milestone        | Referrer Gets            | New người chơi Gets   |
| :--------------- | :----------------------- | :---------------- |
| Account Created  | 500 Credits              | 1,000 Credits     |
| Level 5          | 2,000 Credits            | 2,000 Credits     |
| Level 10         | Rare vũ khí Skin         | Rare vũ khí Skin  |
| Level 20         | 10,000 Credits           | 10,000 Credits    |
| First Extraction | Exclusive Referral Badge | Welcome Badge     |

**Referral Limit:** 50 successful referrals per account (anti-exploit)

<!--  IMAGE PLACEHOLDER: UI mockup of the Referral Program màn hình showing referral code, progress tracker, và reward milestones -->

---

## Post-Match Social flow

> *The 30 seconds sau a match ends are a critical social window. Done right, this flow converts strangers into friends và one-thời gian squads into clans.*

### sau Action Report (AAR)

**Displayed immediately sau extraction/death:**

```
┌──────────────────────────────────────────────────────────────┐
│  AFTER ACTION REPORT                         Match #284712  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  RESULT:  EXTRACTED          Duration: 18:42               │
│  Map: Factory                  Extraction: Gate 3            │
│                                                              │
│  ┌─── PERFORMANCE ───────────────────────────────────────┐   │
│  │  Kills: 3 (PMC: 2, AI: 1)    Deaths: 0               │   │
│  │  Damage Dealt: 847            Damage Taken: 243       │   │
│  │  Loot Extracted: 142,500₽     Items: 12               │   │
│  │  Quests Completed: 1          XP Earned: 2,450        │   │
│  │  Karma Change: +5 (Peaceful Extract)                  │   │
│  └───────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─── SQUAD PERFORMANCE ─────────────────────────────────┐   │
│  │  You     P2       P3                │   │
│  │  K:3 D:0       K:1 D:0       K:5 D:1                 │   │
│  │  Loot: 142K    Loot: 98K     Loot: 215K              │   │
│  └───────────────────────────────────────────────────────┘   │
│                                                              │
│  [COMMEND TEAMMATE ▼]  [ADD FRIEND]  [REPORT]  [CONTINUE]   │
└──────────────────────────────────────────────────────────────┘
```

<!--  IMAGE PLACEHOLDER: UI mockup of the sau Action Report màn hình với squad performance comparison và action buttons -->

### Post-Match Commendation

sau each match, Người chơi có thể commend teammates (1 commendation per match):

| Category           | Icon | Description                          |
| :----------------- | :--- | :----------------------------------- |
| **Good Teammate**  |    | Communicated well, played objectives |
| **Skilled người chơi** |    | Impressive gameplay performance      |
| **Friendly**       |    | Positive attitude, helped team       |
| **Leader**         |    | Made good calls, coordinated squad   |
| **Clutch**         |    | Pulled off a critical play           |

**Commendation Rewards:**
| Milestone            | Reward                             |
| :------------------- | :--------------------------------- |
| 10 commendations     | 500 Credits + "Good Sport" badge   |
| 50 commendations     | 2,500 Credits + "Respected" badge  |
| 100 commendations    | Exclusive emote ("Salute")         |
| 250 commendations    | Rare vũ khí skin                   |
| 500 commendations    | Legendary title: "Community Pillar" |

### Spectator Mode

khi eliminated trong khi a squad match:

**Spectator tính năng:**
- Free-cam around **your teammates only** (no địch spectating to prevent ghosting)
- Toggle between first-person và third-person spectator view
- Minimap remains hiển thị rõ (callout support for squad)
- Ping hệ thống still available for eliminated người chơi (max 1 ping per 10s)
- Auto-spectate ends khi all squad members are eliminated hoặc extracted

**Spectator Restrictions:**
- No địch position information (prevent ghosting via voice comms)
- Cannot Xem địch máu bars hoặc outlines
- Spectator delay: 5 seconds (prevents real-thời gian callouts)

<!--  IMAGE PLACEHOLDER: UI mockup of the Spectator View showing teammate POV với limited HUD elements và ping capability -->

---

## Anti-Toxicity hệ thống

### Report hệ thống

**Report Categories:**
| Category             | Severity       | Automated Action                     |
| :------------------- | :------------- | :----------------------------------- |
| Cheating / Hacking   |  Critical    | Immediate shadow-flag, priority review |
| Abusive Voice / Text |  High        | Auto-mute + queue for review          |
| Griefing / Teamkilling |  High      | Behavior score impact + karma loss    |
| Intentional Disconnecting |  Medium | Matchmaking penalty escalation       |
| Inappropriate Name   |  Medium      | Forced name change                    |
| AFK / Abandonment    |  Medium      | Matchmaking cooldown                  |
| Exploit / Bug Abuse  |  High        | Flag for investigation                |
| Other                |  Low         | Manual review                         |

**Report Process:**
1. Select người chơi from scoreboard, kill feed, hoặc post-match màn hình
2. Choose category
3. Optional: Add description (200 nhân vật)
4. Optional: Attach clip (last 60 seconds auto-recorded)
5. Submit → Confirmation toast notification

**Report Feedback:**
- Notification khi action is taken: "A người chơi you reported has been penalized"
- No chi tiết about cụ thể punishment (privacy protection)
- "Report Accuracy" score — người chơi who file accurate reports get priority processing

### Behavior Score

**Hidden score** (0–100) affecting matchmaking và privileges:

**Score Adjustments:**
| Action                     | Impact  |
| :------------------------- | :------ |
| Complete match normally    | +1      |
| Extract successfully       | +2      |
| Receive commendation       | +5      |
| Confirmed valid report     | -20     |
| Abandon match              | -10     |
| Teamkill (friendly fire)   | -15     |
| Chat violation             | -10     |
| False report filed         | -5      |

**Behavior Score Effects:**
| Score Range | Effect                                             |
| :---------- | :------------------------------------------------- |
| 80–100      | Normal matchmaking, full privileges                |
| 50–79       | Matched với similar scores (soft quarantine)      |
| 20–49       | Chat restricted, LFG disabled, hiển thị rõ cảnh báo     |
| Below 20    | Temporary ban, appeal via support ticket required  |

**Score Recovery:**
- Natural recovery: +1 per completed match (encourages continued play)
- Good behavior streak: 10 matches mà không incident → +10 bonus
- Commendation received: +5 per commendation

<!--  IMAGE PLACEHOLDER: Diagram showing the Behavior Score hệ thống feedback loop: good behavior → higher score → better matches → more fun → continued good behavior -->

---

## Mobile Social tính năng

### Quick Social Access

**Floating Social Button:**
- Always accessible trong khi menus (bottom-right corner)
- Shows online friend count as badge
- Notification dot for pending invites (pulsing animation)
- Swipe up for quick invite to last squad

### Simplified Communication

**Mobile Optimizations:**
- Large push-to-talk button (thumb-friendly, bottom-center)
- Voice activity với smart threshold (auto-calibrates to environment noise)
- Automatic noise suppression (AI-powered, filters wind/background)
- Low-bandwidth codec (Opus at 16kbps for mobile data)
- Quick-chat preset messages (tap to send common phrases)

### Share tính năng

**One-Tap Sharing:**
- Share match results to social media (auto-generated card image)
- Share extraction loot (screenshot với item names)
- Share clan achievements (milestone card)
- Generate shareable profile cards (stats, badges, karma tier)
- Share replay clips (15s / 30s auto-captured highlights)

<!--  IMAGE PLACEHOLDER: Mobile UI mockup showing the social quick-access button, push-to-talk placement, và share card examples -->

---

## Cross-Platform Ecosystem (Powered by EOS)

### Epic Online Services (EOS) Integration

We utilize **Epic Online Services** to provide a seamless multiplayer trải nghiệm across all devices.

**Benefits for người chơi:**
| tính năng                 | Description                                                        |
| :---------------------- | :----------------------------------------------------------------- |
| **One Identity**        | Link accounts across Steam, PlayStation, Xbox, Google, Apple. Progress và purchases sync. |
| **Universal Friends**   | See friends from *all* platforms in one unified list.               |
| **Cross-Platform Voice** | High-quality Opus voice chat between mobile và PC mà không Discord. |
| **Cloud Save**          | Safe House progress, settings, và stash sync across devices.          |

### Unified Lobbies & Parties

**The "Smart Lobby" hệ thống:**
- **Persistent Parties** — Your squad stays together sau the match ends. No re-invite needed.
- **Drop-In / Drop-Out** — Friends can join your lobby while in the main menu (nếu privacy set to "Friends Only").
- **Cross-Platform Invites** — Send game invites directly via EOS Overlay hoặc in-game Social Panel, regardless of platform.
- **Party Transfer** — All party members follow the leader between modes (lobby → Safe House → raid).

### Cross-Play Settings

| Option                  | Description                                             | Default |
| :---------------------- | :------------------------------------------------------ | :------ |
| **Enable Cross-Play**   | Match với other platforms via EOS Matchmaking           | ON      |
| **Input Matchmaking**   | Prioritize same input type (controller / touch / KB+M)  | OFF     |
| **Platform Indicators** | Icons showing nếu a người chơi is on PC, Console, hoặc Mobile  | ON      |

**Platform Icons:**
| Platform      | Icon | ghi chú                    |
| :------------ | :--- | :----------------------- |
| PC (Steam)    |    | KB+M hoặc Controller       |
| PlayStation   |    | Controller               |
| Xbox          |    | Controller               |
| Mobile (iOS)  |    | Touch hoặc Controller      |
| Mobile (Android) |  | Touch hoặc Controller      |

<!--  IMAGE PLACEHOLDER: Diagram showing cross-platform party formation với icons for each platform connecting thông qua EOS -->

---

## Social Analytics (Backend)

### Metrics to Track

**Squad Formation:**
- % solo vs. duo vs. squad người chơi per region
- Average squad size by thời gian of day
- Friend vs. random vs. LFG squad ratio
- Squad retention rate (% that re-queue together)

**Communication:**
- Voice chat usage rate (% of người chơi với mic active)
- Proximity VOIP engagement rate (how often used vs. muted)
- Ping usage frequency per match
- Chat message volume per channel

**Clan máu:**
- Average clan size vs. active members (engagement ratio)
- Clan retention rate (monthly)
- Clan activity (matches/week per member)
- Clan bank utilization rate

**Karma Ecosystem:**
- Karma distribution curve (nên được normal, centered at Neutral)
- Co-op extraction rate vs. betrayal rate
- Karma recovery rate for Suspicious+ người chơi
- Correlation: Karma tier vs. người chơi retention

**Toxicity:**
- Report rate per 100 matches
- Commendation vs. report ratio (target: 5:1)
- Behavior score distribution
- Report accuracy rate
- Mute/block usage rate

**LFG hệ thống:**
- Post creation rate per hour
- Average thời gian-to-fill for LFG posts
- LFG→Friend conversion rate (how often LFG partners become friends)
- Repeat squad rate (LFG partners who re-queue together)

---

## Social tính năng Roadmap

### Phase 1: Launch (v1.0)

| tính năng              | Status | Priority |
| :------------------- | :----- | :------- |
| Squad hệ thống (1-4)   |      | P0       |
| Voice chat (squad + proximity) |  | P0   |
| Ping hệ thống          |      | P0       |
| Friends list         |      | P0       |
| Basic reporting      |      | P0       |
| Text chat            |      | P1       |
| Behavior score       |      | P1       |
| Basic emotes (5)     |      | P1       |

### Phase 2: Community Foundation (v1.1 — Month 2)

| tính năng                 | Status | Priority |
| :---------------------- | :----- | :------- |
| Clan hệ thống (basic)     |      | P1       |
| Clan chat               |      | P1       |
| LFG Board               |      | P1       |
| Referral program        |      | P2       |
| Commendation hệ thống     |      | P1       |
| Karma hệ thống (basic)    |      | P1       |

### Phase 3: Social Depth (v1.2 — Month 3)

| tính năng                   | Status | Priority |
| :------------------------ | :----- | :------- |
| Clan challenges           |      | P2       |
| Clan leaderboards         |      | P2       |
| Co-op extraction points   |      | P1       |
| Expanded emote hệ thống     |      | P2       |
| Social Hub / Safe House   |      | P2       |
| sau Action Report (AAR) |      | P1       |

### Phase 4: Competitive Social (v1.3 — Season 2)

| tính năng                   | Status | Priority |
| :------------------------ | :----- | :------- |
| Clan wars events          |      | P3       |
| Mentorship program        |      | P3       |
| Community tournaments     |      | P3       |
| In-Safe House trading     |      | P2       |
| Advanced karma (bounties) |      | P2       |
| Spectator mode (enhanced) |      | P3       |

---

## Reference Games & Inspirations

| Game                   | chính Social tính năng to Study               | What We Adopt                          |
| :--------------------- | :---------------------------------------- | :------------------------------------- |
| **Escape from Tarkov** | Scav/PMC Karma, VOIP, Co-op Extracts, Hideout | Karma hệ thống, proximity VOIP, social hub |
| **Hunt: Showdown**     | MMR Star Rating, Underdog Bonus, Bounty hệ thống | Matchmaking balancing, solo incentives |
| **DMZ (Warzone)**      | Faction missions, LFG culture, Squad dynamics | LFG board, faction-tied quests         |
| **Dark và Darker**    | Emote/Gesture hệ thống, Dungeon encounters  | Emote wheel, silent communication      |
| **The Finals**         | Cross-platform parties, emote wheel       | EOS integration, social UX             |
| **ARC Raiders**        | Social Hub design, team synergy hệ thống   | Hideout concept, squad bonuses         |
| **Arena Breakout**     | sau Action Report, Recap hệ thống         | Post-match flow, AAR màn hình            |

> **Note:** This is a *design reference* bảng, not a tính năng copy list. Each hệ thống is adapted to fit our game's identity và design pillars.

<!--  IMAGE PLACEHOLDER: Comparison grid showing screenshots from each reference game's social tính năng (Tarkov Karma UI, Hunt MMR stars, DMZ LFG, Dark và Darker emotes) -->
