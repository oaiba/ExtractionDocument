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

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |
| [Pre-Raid Screens](Pre_Raid_Screens.md) | Squad lobby, readiness, matchmaking, and party blockers |
| [Post-Raid Screens](Post_Raid_Screens.md) | Squad summary, commend, report, and add-friend routes |
| [Settings & System Screens](Commerce_Settings_System_Screens.md) | Privacy, streamer mode, account, and safety settings |

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

Layout (PC/Console)

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

| Spec | Requirement |
| :--- | :--- |
| Goal | Provide quick social actions without leaving the current screen unnecessarily |
| Entry points | Top bar / horizontal global nav, squad lobby, and post-match |
| Layout | PC/Console landscape standard: compact side overlay panel with controller-friendly focus states |
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

Layout (PC/Console)

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

Layout (PC/Console)

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

Layout (PC/Console)

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

Layout (PC/Console)

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

Layout (PC/Console)

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

Layout (PC/Console)

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

## Designer-Ready Screen Specs

Social UI must make coordination fast while protecting privacy and safety. Every row/action must respect streamer mode, block state, platform compatibility, and parental/region restrictions.

### Social Panel

**Player Intent**

Open a compact social command center for friends, party, recent players, notifications, and safety shortcuts without leaving the current lifecycle screen.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| SOCIAL PANEL                                           [Search] [Close]        |
|--------------------------------------------------------------------------------|
| Tabs: Friends | Party | Recent | Clan | LFG                                    |
| Friends Online 3 | Invites 2 | Voice OK | Privacy: Friends                     |
|--------------------------------------------------------------------------------|
| Rows: avatar, name, status, platform, compatibility, quick action              |
| Detail: selected player/profile/party state                                    |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Tabs | friends, party, recent, clan, LFG with unread counts |
| List rows | identity, status, platform, privacy-safe activity |
| Detail panel | selected player actions and blockers |
| Safety row | mute, block, report, privacy settings |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Invite/party actions | One-click when compatible |
| 2 | Compatibility blockers | Visible before action |
| 3 | Safety actions | Available but separated |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Player row | name/alias, platform, online state, activity privacy, action |
| Badge | text label plus icon for muted, blocked, crossplay, invite pending |
| Detail actions | invite, join, message, profile, mute, block, report |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Empty friends | Suggest recent players, LFG, invite code |
| Privacy hidden | Show allowed generic status |
| Blocked user | Hide invite/message and show unblock path |
| Offline/social service down | Disable online actions with reason |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Open panel | Social key/click | Menu shortcut | Social button |
| Select row | Click | D-pad | Tap |
| Quick action | Click CTA | A / Cross | Tap action |

**Designer Notes**

- Social panel is utility, not a profile gallery.
- Do not leak exact map/party status under privacy or streamer mode.

**Acceptance Checklist**

- [ ] Empty, offline, privacy-hidden, blocked, and invite-pending states are covered.

### Friends List

**Player Intent**

Find friends, understand availability, and invite/join/message with clear compatibility and privacy rules.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| FRIENDS                                      Search [________] Filter Online v |
|--------------------------------------------------------------------------------|
| Kai       Online  In Lobby   PC     Compatible     [Invite] [Message]          |
| Mira      In Raid Hidden     PS     Busy           [Profile]                   |
| Dax       Offline 2h         XB     --             [Profile]                   |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Search/filter | online, platform, joinable, recent |
| Friend rows | identity, status, privacy-safe activity, platform, action |
| Detail | profile, mutual party, block/mute state |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Joinable/invitable status | Text label |
| 2 | Friend identity | Privacy-safe |
| 3 | Secondary actions | Message/profile after invite |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Status text | online, offline, in raid, hidden, do not disturb |
| Compatibility chip | crossplay, region, mode/ranked restriction |
| Invite CTA | disabled with reason if blocked |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| No friends | Add friend, invite code, recent players |
| Friend busy | Disable invite with activity reason |
| Crossplay blocked | Explain platform setting route |
| Request pending | Show cancel/resent state |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Search | Ctrl-F | Y / Triangle | Search field |
| Invite | Click | A / Cross | Tap |
| Open profile | Right-click/profile | Focus action | Tap row |

**Designer Notes**

- Online status is sensitive; obey privacy defaults.
- Invite must never be the only visible action.

**Acceptance Checklist**

- [ ] Invite disabled states name the blocker.

### Party Panel

**Player Intent**

Manage party membership, readiness, voice, leader controls, and matchmaking blockers.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| PARTY PANEL                                  Leader: You            [Invite]   |
|--------------------------------------------------------------------------------|
| You READY Voice OK | Player2 NOT READY Missing meds | Empty Slot [Invite]      |
| Mission: Sector 7 / Squad / Night | Fill Off | Crossplay On                    |
|--------------------------------------------------------------------------------|
| [Ready] [Change Mission] [Voice Settings] [Leave Party]                        |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Party cards | member, role, ready, blocker, voice/platform |
| Mission strip | selected mode/map/time and restrictions |
| Controls | ready, invite, leader actions, leave |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Readiness/blocker | Drives deploy state |
| 2 | Leader/member permissions | Clear disabled reasons |
| 3 | Voice status | Visible per member |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Member card | identity, platform, role, ready, blocker, voice |
| Kick/leave | confirmation with party consequence |
| Ready CTA | disabled only with exact reason |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Empty slot | invite, match fill, close slot |
| Member disconnected | show reconnect grace |
| Ranked mismatch | show level/rank restriction |
| Leader migrated | update controls and announce |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Ready | Click | A / Cross | Sticky CTA |
| Invite | Click | Y / Triangle | Invite button |
| Leave | Click + confirm | Hold B / Circle | Confirm sheet |

**Designer Notes**

- Party panel should mirror deploy blockers from pre-raid.
- Do not expose exact gear details unless player permits inspection.

**Acceptance Checklist**

- [ ] Ready, leader, disconnected, empty slot, and ranked mismatch states are covered.

### Invite Flow

**Player Intent**

Send, receive, accept, decline, or recover invites with clear context and privacy-safe sender information.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| INVITE RECEIVED                                                                |
| Kai invites you to Squad / Sector 7 / Night                                    |
| Compatibility: OK | Voice: Squad | Expires 00:25                               |
|--------------------------------------------------------------------------------|
| [Decline] [View Party] [Accept]                                                |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Invite card | sender, activity, mode/map if allowed, timeout |
| Compatibility | crossplay, ranked, region, party size |
| Actions | accept, decline, view party |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Sender and destination | Clear and privacy-safe |
| 2 | Accept deadline | Visible timer |
| 3 | Compatibility blockers | Before accept |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Invite toast/modal | safe sender identity, context, expiry |
| Accept CTA | disabled with reason if incompatible |
| Decline | does not punish or expose reason |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Expired | show expired and request new invite |
| Party full | disable accept with reason |
| Privacy blocked | hide unavailable context |
| Already in queue | explain leaving current flow |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Accept | Click/Enter | A / Cross | Tap |
| Decline | Esc/click | B / Circle | Swipe/decline |

**Designer Notes**

- Invite context should be useful but never leak hidden activity.

**Acceptance Checklist**

- [ ] Expired, incompatible, party-full, and already-queued states are covered.

### LFG Board

**Player Intent**

Find or post a group with matching mode, map, region, voice, role, and experience expectations.

**Expanded ASCII Wireframe**

```
+---------------------------------------------------------------------------------+
| LFG BOARD                                      [Create Post] Filter: Sector 7   |
|---------------------------------------------------------------------------------|
| Host      Mode/Map        Need        Voice      Requirements       [Join]      |
| Kai       Squad Sector 7  Support     Required   Lv10+ Chill        [Request]   |
| Mira      Ranked          Recon       Optional   Silver+            [Locked]    |
+---------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Filters | mode, map, role, voice, region, language |
| Post rows | host, mission, needed roles, requirements, join state |
| Create post | expectations and privacy settings |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Join eligibility | clear join/locked labels |
| 2 | Requirements | visible before request |
| 3 | Voice/language | prominent for coordination |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| LFG row | host alias, mission, roles, voice, language, requirement |
| Requirement chip | level/rank/region/platform reason |
| Create form | validates required fields before posting |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| No posts | suggest create post and broaden filters |
| Post full | disable join and update row |
| Requirement mismatch | show unmet condition |
| Abuse/spam | report post action |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Filter | Click controls | Focus chips | Filter sheet |
| Join/request | Click | A / Cross | Tap |
| Create | Button | Y / Triangle | FAB/button |

**Designer Notes**

- LFG should reduce ambiguity, not become a chat room.

**Acceptance Checklist**

- [ ] No-post, full, locked, and mismatch states are covered.

### Clan Hub

**Player Intent**

Understand clan identity, members, roles, activity, invites, and contribution/reward state.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| CLAN HUB: Rust Signal                              Members 18/30 [Manage]      |
|--------------------------------------------------------------------------------|
| Banner / MOTD | Activity | Members | Requests | Clan Tasks | Rewards           |
| Selected member/detail panel                                                   |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Identity header | clan name, tag, banner, MOTD, member count |
| Tabs | activity, members, requests, tasks, rewards |
| Detail panel | selected member/task/request |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Clan identity and current task | Always visible |
| 2 | Member/request actions | Permission-gated |
| 3 | Rewards | Visible but not shop-like |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Member row | role, activity, contribution, online privacy |
| Request row | applicant summary and accept/deny permission |
| Clan task | progress, contributors, reward, expiry |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| No clan | create/join/search options |
| Permission denied | disable management with role reason |
| Full clan | block invites with capacity reason |
| Pending request | show status and cancel |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch tab | Click | Bumpers | Tab row |
| Manage row | Click | A / Cross | Tap row |

**Designer Notes**

- Role permissions must be explicit before destructive clan actions.

**Acceptance Checklist**

- [ ] No-clan, permission, full, and pending-request states are covered.

### Chat And Voice

**Player Intent**

Communicate with party/squad safely, identify voice device state, and mute/report quickly when needed.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| CHAT / VOICE                      Channel: Party v  Voice: ON Device: Headset  |
|--------------------------------------------------------------------------------|
| Messages with sender, time, moderation state                                   |
| [Type message________________________] [Send] [Mute] [Settings]                |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Channel header | current channel, voice state, device |
| Message list | sender, time, content, moderation state |
| Composer | input, send, mute/settings |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Voice state | on/muted/device error text |
| 2 | Recent messages | readable without covering gameplay in overlays |
| 3 | Safety actions | quick mute/report |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Message row | sender alias, text, timestamp, report target |
| Voice meter | speaking, muted, disconnected labels |
| Error banner | permission/device/network reason and settings route |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Mic denied | route to platform settings |
| Device missing | device selector and retry |
| Muted player | show muted state and undo |
| Moderated message | hide content with reason |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Chat | Enter | Virtual keyboard | Chat button |
| Mute | Click icon | Focus player | Tap/hold |
| Push-to-talk | Key | Mapped button | Hold mic |

**Designer Notes**

- Voice errors need exact, non-technical fix copy.

**Acceptance Checklist**

- [ ] Permission, device, muted, and moderated states are covered.

### Report And Block

**Player Intent**

Take a safety action with enough context, clear consequence, and no exposure of enforcement outcome.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| REPORT / BLOCK PLAYER                                                          |
|--------------------------------------------------------------------------------|
| Player: Kai | Context: Last Match / Chat / Voice                               |
| Reasons: Harassment | Cheating | Exploit | Griefing | Other                    |
| Evidence: [x] Attach clip/log | Notes [____________________]                   |
|--------------------------------------------------------------------------------|
| [Cancel] [Block Player]                                      [Submit Report]   |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Context header | player, match/chat/voice source, timestamp |
| Reason list | required single/multi-select per policy |
| Evidence | clip/log/message attachment state |
| Actions | cancel, block, submit |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Safety action and reason | Required before submit |
| 2 | Block consequence | Clear and separate |
| 3 | Feedback | Confirmation without punishment details |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Reason option | text label, policy category |
| Block CTA | explains friend/party/chat impact |
| Submit CTA | disabled until required fields valid |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Submitted | confirmation and support ID |
| Evidence unavailable | explain and allow report |
| Already blocked | show unblock/manage route |
| Offline | queue report if supported or explain retry |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Select reason | Click | A / Cross | Tap |
| Submit | Click | Focus CTA | Sticky CTA |
| Block | Click + confirm | Hold CTA | Confirm sheet |

**Designer Notes**

- Keep tone calm and procedural.
- Never expose punishment or investigation details.

**Acceptance Checklist**

- [ ] Report, block, evidence unavailable, submitted, and already-blocked states are covered.

---

## Production State Matrix

| Screen | Loading / Pending | Disabled / Locked | Invalid / Error | Offline / Reconnect | Success |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Social Panel | presence and invites pending | hidden by privacy with label | service error shows retry | platform offline state persistent | panel opens focused on last tab |
| Friends List | row skeletons | invite/message disabled by privacy/block | search fail or stale presence | offline shows cached friends as stale | action toast with target name |
| Party Panel | ready/member states pending | leader-only actions labelled | party mismatch, full party, mode lock | reconnect grace on disconnected member | ready/deploy state confirmed |
| Invite Flow | invite sending | target unavailable/privacy locked | expired/declined/duplicate invite reason | queued invite if supported | accepted joins party or opens details |
| LFG Board | listings loading | post/join locked by level/privacy | listing expired/full/moderated | offline hides join/post with reason | joined or post created |
| Clan Hub | roster/tasks pending | role permissions labelled | rank/edit/moderation error | offline read-only mode | role/task/action confirmed |
| Chat And Voice | channel connect pending | muted/blocked/parental locked | mic denied, voice service fail | reconnecting voice indicator | channel connected |
| Report And Block | evidence upload pending | submit disabled until required fields | upload/submit fail retry | offline draft saved if allowed | receipt/support route shown |

## Platform Behavior And Input

| Platform | Rule |
| :--- | :--- |
| PC | Search and list navigation support keyboard focus, enter action, and escape close. |
| Console | Tabs and rows must have predictable D-pad order; destructive social actions require confirmation. |
| Mobile | Social panels use full-screen or bottom-sheet layout; voice/chat controls avoid tiny inline icons. |

## Analytics Funnel

| Event | Required Properties |
| :--- | :--- |
| `social_surface_viewed` | surface, entry_point, platform |
| `social_action_attempted` | action, target_type, privacy_state |
| `social_action_blocked` | action, blocked_reason, direct_fix_shown |
| `voice_state_changed` | channel, state, error_reason |
| `report_submitted` | category, evidence_attached, result |

## Social QA Checklist

- Presence, privacy, block, platform restriction, and parental lock states have readable text labels.
- Report/block/destructive actions require confirmation and show post-action receipt.
- Offline social surfaces clearly distinguish cached data from live presence.
- Console and mobile never rely on hover-only affordances.

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
