---
title: "Social Screens"
type: docs
weight: 7
---

## Purpose

Social screens help players coordinate, build trust, and manage abuse across friends, parties, clans, LFG, chat, voice, reports, and privacy. They should support solo play without making the social layer feel mandatory.

Primary references:

| System | Source |
| :--- | :--- |
| Social design | [Social & Multiplayer Systems](../Social/Multiplayer.md) |
| Clan design | [Clan & Guild System](../GameDesign/ClanSystem.md) |
| Communication | [In-Game Communication](../GameDesign/Communication.md) |
| Privacy/settings | [User Settings](../GameDesign/UserSettings.md) |
| Social technical system | [Social System](../../GDD_Technical/Systems/SocialSystem.md) |

---

## Screen Inventory

| Screen | Goal | Primary CTA | Key States |
| :--- | :--- | :--- | :--- |
| Social Panel | Quick access to friends, invites, party, messages | Invite / Join | offline, invite pending, privacy blocked |
| Friends List | Manage friends and presence | Invite / Message | empty, blocked, platform offline |
| Party Panel | Manage current squad party outside raid | Ready / Invite | leader, member, matchmaking locked |
| Invite Flow | Send, accept, decline, or join by code | Send Invite / Accept | expired, full party, incompatible mode |
| LFG Board | Find or post squad requests | Join / Post | no posts, filters empty, behavior restricted |
| Clan Hub | View clan identity, roster, chat, challenges | Open Roster / Start Challenge | no clan, invite pending, permission locked |
| Chat | Text communication and moderation | Send | rate limited, muted, filtered |
| Voice Settings | Configure squad/proximity voice | Apply | device missing, muted, banned |
| Block / Report | Safety controls | Submit | category missing, clip unavailable, cooldown |

---

## Social Panel

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| current screen dimmed behind side panel                          |
|--------------------------------------+---------------------------|
|                                      | SOCIAL PANEL              |
|                                      | Online Friends: 3         |
|                                      | Invites: 1 pending        |
|                                      |---------------------------|
|                                      | [Accept Invite: P2]       |
|                                      | Kai        In Menu [Inv]  |
|                                      | SutureFan  In Raid [View] |
|                                      | Recent: Dxt_Raptor [Add]  |
|                                      |---------------------------|
|                                      | [Friends] [Party] [LFG]   |
+------------------------------------------------------------------+
```

#### Layout (Mobile Portrait)

```
+-----------------------------+
| SOCIAL                 [X]  |
|-----------------------------|
| Invite from Player2         |
| [Accept] [Decline]          |
|-----------------------------|
| Friends Online              |
| Kai          [Invite]       |
| SutureFan    In Raid        |
|-----------------------------|
| Party  LFG  Clan  Settings  |
+-----------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Provide quick social actions without leaving the current screen unnecessarily |
| Entry points | Top bar, Home bottom nav, squad lobby, post-match, mobile floating social button |
| Layout | Compact overlay on PC; full-height panel on console/mobile |
| Primary CTA | Contextual: Invite, Join, Accept |
| Secondary actions | Friends, recent players, clan, LFG, privacy settings |
| Offline state | Show cached friends if available and explain unavailable actions |

### Social Panel Badges

| Badge | Meaning |
| :--- | :--- |
| Online count | Friends currently available |
| Invite dot | Pending invite requiring action |
| Voice warning | Mic muted, device missing, or permission issue |
| Privacy lock | Current privacy setting blocks incoming joins |

---

## Friends List

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| FRIENDS                                           Search [____]  |
|------------------------------------------------------------------|
| NAME          STATUS       PLATFORM     PARTY        ACTION      |
| Kai           In Menu      PC           Joinable     [Invite]    |
| Mira          In Raid      Mobile       Locked       [Message]   |
| Dxt_Raptor    Offline      Console      -            [Profile]   |
| Blocked       Hidden       -            -            [Unblock]   |
|------------------------------------------------------------------|
| [Add Friend] [Recent Players] [Invite Code] [Privacy Settings]   |
+------------------------------------------------------------------+
```

| State | Behavior |
| :--- | :--- |
| No friends | Offer search, recent players, referral, and LFG |
| Friend online | Invite/message/join according to privacy |
| Friend in raid | Show status but block join with reason |
| Cross-platform friend | Show platform icon and input method if available |
| Blocked player | Hide presence and offer unblock confirmation |

### Friend Row Fields

| Field | Purpose |
| :--- | :--- |
| Name and platform | Identity and cross-play clarity |
| Presence | Online, in raid, in menu, away, offline |
| Party status | Joinable, full, private, incompatible |
| Voice status | Available, muted, unavailable |
| Last played / recent | Helps reconnect with recent squadmates |

---

## Party Panel

The party panel overlaps with [Pre-Raid Screens](Pre_Raid_Screens.md), but this screen owns persistent social party management outside the deploy flow.

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| PARTY                                      Privacy: Friends Only |
|------------------------------------------------------------------|
| +----------------+ +----------------+ +----------------+         |
| | You Leader     | | Player2        | | Empty Slot     |         |
| | Ready          | | Editing kit    | | [Invite]       |         |
| | Voice OK       | | Voice OK       | | [Share Code]   |         |
| +----------------+ +----------------+ +----------------+         |
| Mission: Sector 7 / Squad / Night                                |
|------------------------------------------------------------------|
| [Transfer Leader] [Invite] [Leave Party] [Ready]                 |
+------------------------------------------------------------------+
```

| Role | Available Controls |
| :--- | :--- |
| Leader | Invite, kick, transfer leader, set privacy, queue, cancel queue |
| Member | Ready, leave, invite if allowed, view mission, voice/chat |
| Guest / pending | Accept, decline, inspect party summary |

### Party States

| State | UI Behavior |
| :--- | :--- |
| Open party | Friends can join; show privacy status |
| Friends only | Show join eligibility |
| Invite only | Show invite code and expiration |
| In queue | Lock incompatible edits and show cancel rules |
| In raid | Show spectate/rejoin if supported; block party edits |

---

## Invite Flow

#### State Diagram

```
Select Target -> Preview Party -> Send Invite -> Pending
      |                |              |
      v                v              v
 Recent Player   Incompatible     Accepted -> Party Panel
 Friend          Full Party       Declined -> Toast
 Share Code      Privacy Blocked  Expired  -> Retry
```

| Step | Requirement |
| :--- | :--- |
| Select target | Friend, recent player, clan member, share code, platform overlay |
| Preview party | Show mode, squad size, leader, platform restrictions |
| Send / accept | Confirm and show pending state |
| Failure | Explain full party, expired invite, blocked privacy, cross-play off, rank mismatch |

Mobile invite flow must support share code and QR/deep link if platform policy allows it.

---

## LFG Board

#### Layout (PC/Console)

```
+--------------------------------------------------------------------+
| LFG BOARD                         Region SEA  Mic Required [x]     |
|--------------------------------------------------------------------|
| FILTERS        | POSTS                                     | INFO  |
| Mode: Any      | [S7 Quest Run] 2/4  Mic Yes  Risk Med     | Goal  |
| Map: Sector 7  | [Budget Recovery] 1/3  Chill  Risk Low    | Tags  |
| Role: Any      | [Ranked Push] 3/4  Lv15+  Risk High       | Host  |
| Language: EN   |                                           | [Join]|
|--------------------------------------------------------------------|
| [Create Post] [Widen Filters] [Safety Rules]                       |
+--------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Help players form temporary squads around intent and trust |
| Filters | Region, mode, map, language, mic, experience, role, risk level |
| Post fields | Title, goal, mode/map, mic required, role needs, privacy |
| Primary CTA | Join Post or Create Post |
| Safety | Behavior-restricted players see reason and recovery path |

### LFG States

| State | Behavior |
| :--- | :--- |
| No posts | Suggest widening filters or creating post |
| Post full | Disable join and update in place |
| Incompatible | Explain level, rank, platform, or privacy reason |
| Reported post | Hide if removed; show moderation state to owner |

---

## Clan Hub

#### Layout (PC/Console)

```
+-------------------------------------------------------------------+
| CLAN HUB: Salvage Saints                         Level 8          |
|-------------------------------------------------------------------|
| OVERVIEW              | ROSTER / CHAT                 | CHALLENGE |
| Members 18/30         | Kai        Online             | Extract 5 |
| Weekly XP 42,000      | Mira       In Raid            | Progress  |
| Message: Night runs   | Dxt        Offline            | 3 / 5     |
|                       | Clan chat [____________]      | [Track]   |
|-------------------------------------------------------------------|
| [Invite] [Applications] [Manage Roles] [Leave Clan]               |
+-------------------------------------------------------------------+
```

| Screen | Purpose |
| :--- | :--- |
| Clan Overview | Identity, level, message, active challenge |
| Roster | Members, roles, online state, permissions |
| Clan Chat | Persistent clan communication |
| Challenges | Shared goals and rewards |
| Applications | Invite/request review |
| Management | Roles, permissions, description, privacy |

Players without a clan should see Join Clan, Create Clan, and Browse recommendations rather than a dead empty page.

---

## Chat And Voice

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| CHAT / VOICE                                      Channel: Squad |
|------------------------------------------------------------------|
| [Voice] Kai speaking...    Mic OK    Proximity OFF               |
|------------------------------------------------------------------|
| Kai: ready?                                                      |
| You: fixing ammo                                                 |
| System: Player2 joined party                                     |
|------------------------------------------------------------------|
| Message [____________________________________] [Send] [Mute All] |
+------------------------------------------------------------------+
```

| Surface | Rule |
| :--- | :--- |
| Text chat | Rate limit, profanity filter, report message, channel color and label |
| Squad voice | Private squad channel with voice activity indicator |
| Proximity voice | In-raid tactical channel with risk messaging |
| Quick chat | Mobile/controller presets for common tactical messages |
| Mute/block | Available from chat row, voice indicator, profile, AAR |

### Voice Error States

| State | Behavior |
| :--- | :--- |
| Mic unavailable | Show device/settings shortcut |
| Permission denied | Show OS/platform permission help |
| Voice banned | Explain duration and appeal/support path |
| Network degraded | Show low-bandwidth mode or reconnect warning |

---

## Report And Block

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| REPORT PLAYER: PlayerName                                        |
|------------------------------------------------------------------|
| Category                                                         |
| ( ) Cheating / Hacking                                           |
| ( ) Abusive Voice / Text                                         |
| ( ) Griefing / Teamkilling                                       |
| ( ) Exploit / Bug Abuse                                          |
|                                                                  |
| Evidence: [x] Attach last 60s clip                               |
| Notes: [____________________________________________]            |
|------------------------------------------------------------------|
| [Cancel] [Block Player]                         [Submit Report]  |
+------------------------------------------------------------------+
```

| Action | UI Standard |
| :--- | :--- |
| Block player | Confirmation; explain friend/party/chat impact |
| Report player | Category required; optional description and clip |
| Report message | Preselect abusive text/chat category |
| Report voice | Attach last available voice buffer if policy allows |
| Feedback | Confirmation only; do not expose punishment details |

---

## Analytics

| Metric | Use |
| :--- | :--- |
| Invite acceptance rate | Tune invite context and privacy defaults |
| LFG post fill time | Measure social discoverability |
| Friend conversion from recent players | Measure post-match social flow |
| Voice setup failure rate | Improve device/permission UX |
| Mute/block/report rate | Monitor safety and friction |
| Clan join/create conversion | Tune clan onboarding |

---

## Acceptance Checklist

- [ ] Social actions explain privacy and compatibility blockers.
- [ ] Empty friend/LFG/clan states provide useful next actions.
- [ ] Voice and chat failures include settings or support paths.
- [ ] Report and block are reachable from profile, chat, AAR, and replay contexts.
- [ ] Mobile social access supports quick invite and quick mute.
- [ ] Streamer/privacy modes hide sensitive social data.
