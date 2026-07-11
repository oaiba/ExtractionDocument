---
title: "Social màn hình"
type: docs
weight: 7
---

## Mục Đích

Social màn hình giúp người chơi coordinate, build trust, và manage abuse across friends, parties, clans, LFG, chat, voice, reports, và privacy. They should support solo play mà không making the social layer feel mandatory.

Tham chiếu chính:

| hệ thống | source |
| :--- | :--- |
| Social design | [Social & Multiplayer hệ thống](../Social/Multiplayer.md) |
| Clan design | [Clan & Guild hệ thống](../GameDesign/ClanSystem.md) |
| Communication | [In-Game Communication](../GameDesign/Communication.md) |
| Privacy/settings | [User Settings](../GameDesign/UserSettings.md) |
| Social technical hệ thống | [Social hệ thống](../../GDD_Technical/hệ thống/SocialSystem.md) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [màn hình Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](Global_UX_Standards.md) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [Pre-Raid màn hình](Pre_Raid_Screens.md) | Squad lobby, readiness, matchmaking, và party blockers |
| [Post-Raid màn hình](Post_Raid_Screens.md) | Squad summary, commend, report, và add-friend routes |
| [Settings & hệ thống màn hình](Commerce_Settings_System_Screens.md) | Privacy, streamer mode, account, và safety settings |

---

## Inventory Màn Hình

| màn hình | mục tiêu | primary CTA | chính trạng thái |
| :--- | :--- | :--- | :--- |
| Social Panel | Quick access to friends, invites, party, messages | Invite / Join | offline, invite pending, privacy blocked |
| Friends List | Manage friends và presence | Invite / Message | empty, blocked, platform offline |
| Party Panel | Manage hiện tại squad party outside raid | Ready / Invite | leader, member, matchmaking locked |
| Invite flow | Send, accept, decline, hoặc join by code | Send Invite / Accept | expired, full party, incompatible mode |
| LFG Board | Find hoặc post squad requests | Join / Post | no posts, filters empty, behavior restricted |
| Clan Hub | View clan identity, roster, chat, challenges | Open Roster / Start Challenge | no clan, invite pending, permission locked |
| Chat | Text communication và moderation | Send | rate limited, muted, filtered |
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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Provide quick social actions mà không leaving the hiện tại màn hình unnecessarily |
| Entry points | Top bar / horizontal global nav, squad lobby, và post-match |
| Layout | PC/Console landscape standard: compact side overlay panel với controller-friendly focus trạng thái |
| primary CTA | Contextual: Invite, Join, Accept |
| secondary actions | Friends, recent người chơi, clan, LFG, privacy settings |
| Offline trạng thái | Show cached friends nếu available và explain unavailable actions |

### Social Panel Badges

| Badge | Meaning |
| :--- | :--- |
| Online count | Friends currently available |
| Invite dot | pending invite requiring action |
| Voice cảnh báo | Mic muted, device missing, hoặc permission issue |
| Privacy lock | hiện tại privacy setting blocks incoming joins |

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

| trạng thái | Behavior |
| :--- | :--- |
| No friends | offer search, recent người chơi, referral, và LFG |
| Friend online | Invite/message/join according to privacy |
| Friend in raid | Show status nhưng block join với reason |
| Cross-platform friend | Show platform icon và input method nếu available |
| Blocked người chơi | Hide presence và offer unblock confirmation |

### Friend Row Fields

| Field | mục đích |
| :--- | :--- |
| Name và platform | Identity và cross-play clarity |
| Presence | Online, in raid, in menu, away, offline |
| Party status | Joinable, full, private, incompatible |
| Voice status | available, muted, unavailable |
| Last played / recent | giúp reconnect với recent squadmates |

---

## Party Panel

The party panel overlaps với [Pre-Raid màn hình](Pre_Raid_Screens.md), nhưng this màn hình owns persistent social party management outside the deploy flow.

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

| Role | available Controls |
| :--- | :--- |
| Leader | Invite, kick, transfer leader, set privacy, queue, cancel queue |
| Member | Ready, leave, invite nếu allowed, view mission, voice/chat |
| Guest / pending | Accept, decline, kiểm tra party summary |

### Party trạng thái

| trạng thái | UI Behavior |
| :--- | :--- |
| Open party | Friends can join; show privacy status |
| Friends only | Show join eligibility |
| Invite only | Show invite code và expiration |
| In queue | Lock incompatible edits và show cancel rules |
| In raid | Show spectate/rejoin nếu supported; block party edits |

---

## Invite flow

#### trạng thái Diagram

```
Select Target -> Preview Party -> Send Invite -> Pending
      |                |              |
      v                v              v
 Recent Player   Incompatible     Accepted -> Party Panel
 Friend          Full Party       Declined -> Toast
 Share Code      Privacy Blocked  Expired  -> Retry
```

| Step | yêu cầu |
| :--- | :--- |
| Select target | Friend, recent người chơi, clan member, share code, platform overlay |
| preview party | Show mode, squad size, leader, platform restrictions |
| Send / accept | Confirm và show pending trạng thái |
| Failure | Explain full party, expired invite, blocked privacy, cross-play off, rank mismatch |

Mobile invite flow must support share code và QR/deep link nếu platform policy allows it.

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | giúp người chơi form temporary squads around intent và trust |
| Filters | Region, mode, map, language, mic, trải nghiệm, role, risk level |
| Post fields | Title, mục tiêu, mode/map, mic required, role needs, privacy |
| primary CTA | Join Post hoặc tạo Post |
| Safety | Behavior-restricted người chơi see reason và recovery path |

### LFG trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| No posts | Suggest widening filters hoặc tạo post |
| Post full | Disable join và update in place |
| Incompatible | Explain level, rank, platform, hoặc privacy reason |
| Reported post | Hide nếu removed; show moderation trạng thái to owner |

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

| màn hình | mục đích |
| :--- | :--- |
| Clan Overview | Identity, level, message, active challenge |
| Roster | Members, roles, online trạng thái, permissions |
| Clan Chat | Persistent clan communication |
| Challenges | shared goals và rewards |
| Applications | Invite/request review |
| Management | Roles, permissions, description, privacy |

người chơi mà không a clan should see Join Clan, tạo Clan, và Browse recommendations rather than a dead empty trang.

---

## Chat và Voice

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
| Text chat | Rate limit, profanity filter, report message, channel color và label |
| Squad voice | Private squad channel với voice activity indicator |
| Proximity voice | In-raid tactical channel với risk messaging |
| Quick chat | Mobile/controller presets for common tactical messages |
| Mute/block | available from chat row, voice indicator, profile, AAR |

### Voice Error trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Mic unavailable | Show device/settings shortcut |
| Permission denied | Show OS/platform permission giúp |
| Voice banned | Explain duration và appeal/support path |
| Network degraded | Show low-bandwidth mode hoặc reconnect cảnh báo |

---

## Report và Block

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
| Block người chơi | Confirmation; explain friend/party/chat impact |
| Report người chơi | Category required; optional description và clip |
| Report message | Preselect abusive text/chat category |
| Report voice | Attach last available voice buffer nếu policy allows |
| Feedback | Confirmation only; do not expose punishment chi tiết |

---

## Designer-Ready màn hình Specs

Social UI must make coordination fast while protecting privacy và safety. Every row/action must respect streamer mode, block trạng thái, platform compatibility, và parental/region restrictions.

### Social Panel

**người chơi Intent**

Open a compact social command center for friends, party, recent người chơi, notifications, và safety shortcuts mà không leaving the hiện tại lifecycle màn hình.

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

| Region | yêu cầu |
| :--- | :--- |
| Tabs | friends, party, recent, clan, LFG với unread counts |
| List rows | identity, status, platform, privacy-safe activity |
| chi tiết panel | selected người chơi actions và blockers |
| Safety row | mute, block, report, privacy settings |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Invite/party actions | One-click khi compatible |
| 2 | Compatibility blockers | hiển thị rõ trước action |
| 3 | Safety actions | available nhưng separated |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| người chơi row | name/alias, platform, online trạng thái, activity privacy, action |
| Badge | text label plus icon for muted, blocked, crossplay, invite pending |
| chi tiết actions | invite, join, message, profile, mute, block, report |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| empty friends | Suggest recent người chơi, LFG, invite code |
| Privacy hidden | Show allowed generic status |
| Blocked user | Hide invite/message và show unblock path |
| Offline/social dịch vụ down | Disable online actions với reason |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Open panel | Social chính/click | Menu shortcut | Social button |
| Select row | Click | D-pad | Tap |
| Quick action | Click CTA | A / Cross | Tap action |

**Designer ghi chú**

- Social panel is utility, not a profile gallery.
- Do not leak exact map/party status under privacy hoặc streamer mode.

**Acceptance checklist**

- [ ] empty, offline, privacy-hidden, blocked, và invite-pending trạng thái are covered.

### Friends List

**người chơi Intent**

Find friends, understand availability, và invite/join/message với rõ compatibility và privacy rules.

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

| Region | yêu cầu |
| :--- | :--- |
| Search/filter | online, platform, joinable, recent |
| Friend rows | identity, status, privacy-safe activity, platform, action |
| chi tiết | profile, mutual party, block/mute trạng thái |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Joinable/invitable status | Text label |
| 2 | Friend identity | Privacy-safe |
| 3 | secondary actions | Message/profile sau invite |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Status text | online, offline, in raid, hidden, do not disturb |
| Compatibility chip | crossplay, region, mode/ranked restriction |
| Invite CTA | disabled với reason nếu blocked |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| No friends | Add friend, invite code, recent người chơi |
| Friend busy | Disable invite với activity reason |
| Crossplay blocked | Explain platform setting route |
| Request pending | Show cancel/resent trạng thái |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Search | Ctrl-F | Y / Triangle | Search field |
| Invite | Click | A / Cross | Tap |
| Open profile | Right-click/profile | Focus action | Tap row |

**Designer ghi chú**

- Online status is sensitive; obey privacy defaults.
- Invite must never be the only hiển thị rõ action.

**Acceptance checklist**

- [ ] Invite disabled trạng thái name the blocker.

### Party Panel

**người chơi Intent**

Manage party membership, readiness, voice, leader controls, và matchmaking blockers.

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

| Region | yêu cầu |
| :--- | :--- |
| Party cards | member, role, ready, blocker, voice/platform |
| Mission strip | selected mode/map/thời gian và restrictions |
| Controls | ready, invite, leader actions, leave |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Readiness/blocker | Drives deploy trạng thái |
| 2 | Leader/member permissions | rõ disabled reasons |
| 3 | Voice status | hiển thị rõ per member |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Member card | identity, platform, role, ready, blocker, voice |
| Kick/leave | confirmation với party consequence |
| Ready CTA | disabled only với exact reason |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| empty slot | invite, match fill, close slot |
| Member disconnected | show reconnect grace |
| Ranked mismatch | show level/rank restriction |
| Leader migrated | update controls và announce |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Ready | Click | A / Cross | Sticky CTA |
| Invite | Click | Y / Triangle | Invite button |
| Leave | Click + confirm | Hold B / Circle | Confirm sheet |

**Designer ghi chú**

- Party panel should mirror deploy blockers from pre-raid.
- Do not expose exact gear chi tiết unless người chơi permits inspection.

**Acceptance checklist**

- [ ] Ready, leader, disconnected, empty slot, và ranked mismatch trạng thái are covered.

### Invite flow

**người chơi Intent**

Send, receive, accept, decline, hoặc recover invites với rõ context và privacy-safe sender information.

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

| Region | yêu cầu |
| :--- | :--- |
| Invite card | sender, activity, mode/map nếu allowed, timeout |
| Compatibility | crossplay, ranked, region, party size |
| Actions | accept, decline, view party |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Sender và điểm đến | rõ và privacy-safe |
| 2 | Accept deadline | hiển thị rõ timer |
| 3 | Compatibility blockers | trước accept |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Invite toast/modal | safe sender identity, context, expiry |
| Accept CTA | disabled với reason nếu incompatible |
| Decline | does not punish hoặc expose reason |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Expired | show expired và request new invite |
| Party full | disable accept với reason |
| Privacy blocked | hide unavailable context |
| Already in queue | explain leaving hiện tại flow |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Accept | Click/Enter | A / Cross | Tap |
| Decline | Esc/click | B / Circle | Swipe/decline |

**Designer ghi chú**

- Invite context nên được useful nhưng never leak hidden activity.

**Acceptance checklist**

- [ ] Expired, incompatible, party-full, và already-queued trạng thái are covered.

### LFG Board

**người chơi Intent**

Find hoặc post a group với matching mode, map, region, voice, role, và trải nghiệm expectations.

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

| Region | yêu cầu |
| :--- | :--- |
| Filters | mode, map, role, voice, region, language |
| Post rows | host, mission, needed roles, yêu cầu, join trạng thái |
| tạo post | expectations và privacy settings |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Join eligibility | rõ join/locked labels |
| 2 | yêu cầu | hiển thị rõ trước request |
| 3 | Voice/language | prominent for coordination |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| LFG row | host alias, mission, roles, voice, language, yêu cầu |
| yêu cầu chip | level/rank/region/platform reason |
| tạo form | validates required fields trước posting |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| No posts | suggest tạo post và broaden filters |
| Post full | disable join và update row |
| yêu cầu mismatch | show unmet condition |
| Abuse/spam | report post action |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Filter | Click controls | Focus chips | Filter sheet |
| Join/request | Click | A / Cross | Tap |
| tạo | Button | Y / Triangle | FAB/button |

**Designer ghi chú**

- LFG should reduce mơ hồ, not become a chat room.

**Acceptance checklist**

- [ ] No-post, full, locked, và mismatch trạng thái are covered.

### Clan Hub

**người chơi Intent**

Understand clan identity, members, roles, activity, invites, và contribution/reward trạng thái.

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

| Region | yêu cầu |
| :--- | :--- |
| Identity header | clan name, tag, banner, MOTD, member count |
| Tabs | activity, members, requests, tasks, rewards |
| chi tiết panel | selected member/task/request |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Clan identity và hiện tại task | Always hiển thị rõ |
| 2 | Member/request actions | Permission-gated |
| 3 | Rewards | hiển thị rõ nhưng not shop-like |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Member row | role, activity, contribution, online privacy |
| Request row | applicant summary và accept/deny permission |
| Clan task | progress, contributors, reward, expiry |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| No clan | tạo/join/search options |
| Permission denied | disable management với role reason |
| Full clan | block invites với capacity reason |
| pending request | show status và cancel |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch tab | Click | Bumpers | Tab row |
| Manage row | Click | A / Cross | Tap row |

**Designer ghi chú**

- Role permissions phải được explicit trước destructive clan actions.

**Acceptance checklist**

- [ ] No-clan, permission, full, và pending-request trạng thái are covered.

### Chat và Voice

**người chơi Intent**

Communicate với party/squad safely, identify voice device trạng thái, và mute/report quickly khi needed.

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

| Region | yêu cầu |
| :--- | :--- |
| Channel header | hiện tại channel, voice trạng thái, device |
| Message list | sender, thời gian, content, moderation trạng thái |
| Composer | input, send, mute/settings |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Voice trạng thái | on/muted/device error text |
| 2 | Recent messages | dễ đọc mà không covering gameplay in overlays |
| 3 | Safety actions | quick mute/report |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Message row | sender alias, text, timestamp, report target |
| Voice meter | speaking, muted, disconnected labels |
| Error banner | permission/device/network reason và settings route |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Mic denied | route to platform settings |
| Device missing | device selector và retry |
| Muted người chơi | show muted trạng thái và undo |
| Moderated message | hide content với reason |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Chat | Enter | Virtual keyboard | Chat button |
| Mute | Click icon | Focus người chơi | Tap/hold |
| Push-to-talk | chính | Mapped button | Hold mic |

**Designer ghi chú**

- Voice errors need exact, non-technical fix copy.

**Acceptance checklist**

- [ ] Permission, device, muted, và moderated trạng thái are covered.

### Report và Block

**người chơi Intent**

Take a safety action với enough context, rõ consequence, và no exposure of enforcement outcome.

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

| Region | yêu cầu |
| :--- | :--- |
| Context header | người chơi, match/chat/voice source, timestamp |
| Reason list | required single/multi-select per policy |
| Evidence | clip/log/message attachment trạng thái |
| Actions | cancel, block, submit |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Safety action và reason | Required trước submit |
| 2 | Block consequence | rõ và separate |
| 3 | Feedback | Confirmation mà không punishment chi tiết |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Reason option | text label, policy category |
| Block CTA | explains friend/party/chat impact |
| Submit CTA | disabled until required fields valid |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Submitted | confirmation và support ID |
| Evidence unavailable | explain và allow report |
| Already blocked | show unblock/manage route |
| Offline | queue report nếu supported hoặc explain retry |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Select reason | Click | A / Cross | Tap |
| Submit | Click | Focus CTA | Sticky CTA |
| Block | Click + confirm | Hold CTA | Confirm sheet |

**Designer ghi chú**

- Keep tone calm và procedural.
- Never expose punishment hoặc investigation chi tiết.

**Acceptance checklist**

- [ ] Report, block, evidence unavailable, submitted, và already-blocked trạng thái are covered.

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
| Console | Tabs and rows have predictable D-pad order; destructive social actions require confirmation. |
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

- Presence, privacy, block, platform restriction, và parental lock states có readable text labels.
- Report/block/destructive actions require confirmation và show post-action receipt.
- Offline social surfaces phân biệt cached data và live presence.
- Console/mobile không rely vào hover-only affordances.

## Analytics

| Metric | cách dùng |
| :--- | :--- |
| Invite acceptance rate | Tune invite context và privacy defaults |
| LFG post fill thời gian | Measure social discoverability |
| Friend conversion from recent người chơi | Measure post-match social flow |
| Voice setup failure rate | Improve device/permission UX |
| Mute/block/report rate | Monitor safety và friction |
| Clan join/tạo conversion | Tune clan onboarding |

---

## checklist Nghiệm Thu

- [ ] Social actions explain privacy và compatibility blockers.
- [ ] empty friend/LFG/clan trạng thái provide useful next actions.
- [ ] Voice và chat failures include settings hoặc support paths.
- [ ] Report và block are reachable from profile, chat, AAR, và replay contexts.
- [ ] Mobile social access supports quick invite và quick mute.
- [ ] Streamer/privacy modes hide sensitive social data.
