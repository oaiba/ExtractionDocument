---
title: "Pre-Raid Screens"
type: docs
weight: 4
---

## Purpose

Pre-raid screens convert preparation into commitment. They must communicate selected rules, map risk, squad readiness, gear value, insurance status, and matchmaking state before the player loses control.

Primary references:

| System | Source |
| :--- | :--- |
| Matchmaking | [Matchmaking & Lobby System](../Gameplay/Matchmaking_Lobby.md) |
| Loadout | [Loadout Preparation](../GameDesign/LoadoutPreparation.md) |
| Modes | [Game Modes Design](../GameDesign/GameModes.md) |
| Maps | [Map Design](../GameDesign/MapDesign.md) |
| Insurance | [Insurance System Design](../GameDesign/InsuranceSystem.md) |

---

## Screen Inventory

| Screen | Goal | Primary CTA | Critical States |
| :--- | :--- | :--- | :--- |
| Mode Select | Choose raid rules and squad size | Select Mode | locked, ranked restrictions, event modifier |
| Map Select | Choose destination and understand extracts/difficulty | Select Map | locked map, high risk, unavailable region |
| Deploy Confirmation | Summarize risk before queue | Deploy | invalid loadout, high uninsured value, squad not ready |
| Squad Lobby | Coordinate party readiness | Ready / Deploy | member not ready, missing kit, voice muted, leader only |
| Matchmaking | Communicate queue progress and cancel rules | Cancel Queue | match found, timeout, server error, party changed |
| Match Found | Final accept or countdown | Accept / Deploying | player declined, party member failed, reconnecting |

---

## Mode Select

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| < Back                         MODE SELECT                       |
|------------------------------------------------------------------|
| +----------------+ +----------------+ +----------------+         |
| | SOLO           | | DUO            | | SQUAD          |         |
| | Mixed lobbies  | | 2 players      | | 3-4 players    |         |
| | Low comms risk | | Team bonus     | | High reward    |         |
| | [SELECTED]     | | [SELECT]       | | [SELECT]       |         |
| +----------------+ +----------------+ +----------------+         |
| +----------------+ +----------------+                            |
| | RANKED         | | EVENT RAID     | Rules, losses, rewards     |
| | Locked Lv15    | | Modifier active| shown for selected card    |
| +----------------+ +----------------+                            |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| User intent | Pick the ruleset that matches desired risk, squad size, and reward |
| Entry points | Home deploy card, Loadout mission tab, event deep link |
| Layout | Mode cards with rules, losses, rewards, matchmaking pool, and availability |
| Primary CTA | Select Mode |
| Secondary actions | View rules, compare rewards, toggle squad fill, view ranked restrictions |
| Accessibility | Rule changes must be text labels, not only badges or colors |

### Mode States

| State | Behavior |
| :--- | :--- |
| Available | Normal card with reward/risk summary |
| Locked | Show requirement and unlock path |
| Event | Show modifier badge and expiry time |
| Ranked | Show rank impact, party restrictions, and locked settings |
| Disabled | Explain server, region, or maintenance reason |

---

## Map Select

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| < Back                         MAP SELECT              [Ready]   |
|------------------------------------------------------------------|
| MAP LIST            | MAP PREVIEW / INTEL              | DETAILS |
| [Selected] Sector 7 | +------------------------------+ | Hard    |
| District 14         | | Industrial map art           | | 8-12    |
| Firebase Delta      | | Extract markers + landmarks  | | Boss 1  |
| [Locked] The Mire   | +------------------------------+ | Night v |
|                     | Extracts: Crossroads, Boat       | Quest 2 |
|                     | Queue estimate: 45s              | Squad 1 |
|------------------------------------------------------------------|
| [Show Quests] [Compare Risk] [Change Time] [READY]               |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Make destination choice readable: difficulty, extracts, player count, time of day, quest relevance |
| Layout | PC/Console landscape standard: map list left, preview/map art center, extracts and squad context right |
| Primary CTA | Select Map / Ready |
| Secondary actions | Preview extracts, show quests, change time of day, compare difficulty |

### Required Map Fields

| Field | Purpose |
| :--- | :--- |
| Difficulty | Sets expectation for combat and survival |
| Player count | Communicates PvP density |
| Boss / high-value target | Flags high-risk opportunities |
| Extraction rules | Prevents surprise loss conditions |
| Quest relevance | Helps choose useful destination |
| Time of day | Communicates visibility and AI behavior changes |
| Queue estimate | Sets wait expectation before commit |

---

## Deploy Confirmation

Deploy confirmation is the final trust checkpoint. It should be quick for valid kits and explicit for risky kits.

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         DEPLOY CONFIRMATION                      |
|------------------------------------------------------------------|
| Mission: Solo / Sector 7 / Night       Queue estimate: 45s       |
| Squad: You READY                       Fill: Off                 |
|------------------------------------------------------------------|
| Gear value: 125,000        Weight: 24 / 40kg        Ammo: OK     |
| Insurance: 4 insured / 2 uninsured eligible                      |
| Quests: Supply Run, Lab Rat                                      |
| Warnings: [!] High uninsured value                               |
|------------------------------------------------------------------|
| [Back to Loadout]        [Insure All]        [HOLD TO DEPLOY]    |
+------------------------------------------------------------------+
```

| Field | Requirement |
| :--- | :--- |
| Selected mode and map | Always visible |
| Squad size and fill | Always visible |
| Gear value | Always visible |
| Insurance | Show insured, uninsured, and ineligible counts |
| Quest suggestions | Show top 1-3 relevant objectives |
| Loadout blockers | Inline, actionable, and focusable |
| Queue estimate | Update before matchmaking starts |

### Confirmation Rules

| Condition | Behavior |
| :--- | :--- |
| Valid normal kit | Single Deploy CTA |
| Missing weapon | Block; focus missing slot |
| Missing ammo | Warn; allow explicit confirmation only if design permits |
| Overweight | Block; offer quick stash filter |
| High value | Confirm risk with gear value shown |
| Uninsured eligible items | Offer Insure All or Deploy Uninsured |
| Ranked mode | Show rank impact and locked settings summary |

---

## Squad Lobby

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| < Back                         SQUAD LOBBY       [Invite] [Leave]|
|------------------------------------------------------------------|
| +----------------+ +----------------+ +----------------+         |
| | You Leader     | | Player2        | | Empty Slot     |         |
| | READY          | | NOT READY      | | [Invite]       |         |
| | Value 125K     | | Missing meds   | | [Match Fill]   |         |
| | Voice OK       | | Voice muted    | |                |         |
| +----------------+ +----------------+ +----------------+         |
| Mission: Sector 7 / Night / Squad                                |
| Chat [__________________________] [Send]  Voice: Squad ON        |
|------------------------------------------------------------------|
| [Change Map] [Change Loadout]        [DEPLOY LOCKED: P2 blocker] |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Let squads coordinate readiness without hiding blockers |
| Layout | Player cards, selected mission, voice/chat, readiness, leader controls |
| Primary CTA | Ready for member; Deploy for leader when all ready |
| Secondary actions | Invite, inspect loadout summary, change map, change loadout, leave |
| Destructive actions | Kick, leave party, cancel matchmaking require confirmation depending context |

### Squad Card Fields

| Field | Purpose |
| :--- | :--- |
| Player name and platform | Identity and cross-play clarity |
| Operator and role | Team composition |
| Ready state | Blocking status |
| Loadout warnings | Shows why deploy is blocked |
| Voice status | Confirms communication readiness |
| Gear value range | Communicates risk without exposing exact inventory details |

### Squad States

| State | Behavior |
| :--- | :--- |
| Empty slot | Invite, match fill, or close slot |
| Member not ready | Show reason if shared by system |
| Leader only action | Disabled for members with reason |
| Voice muted | Badge and settings shortcut |
| Party mismatch | Explain platform, ranked, or level restriction |

---

## Matchmaking

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         MATCHMAKING                              |
|------------------------------------------------------------------|
| Sector 7 / Solo / Night                                          |
| Searching... 00:42                         Region: SEA  Ping 38  |
| [======================----------]                               |
|                                                                  |
| Squad: Kai READY                                                 |
| Estimated wait: 45s       Search range: Normal                   |
| Tip: Heavy bags make heavy noise.                                |
|------------------------------------------------------------------|
| [Cancel Queue]                         Status: can cancel         |
+------------------------------------------------------------------+
```

#### State Diagram

```
Searching -> Expanding Search -> Match Found -> L4 Loading -> In Raid
     |              |                |
     v              v                v
 Cancelled      Server Error     Player Declined
```

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
|                           MATCH FOUND                            |
|------------------------------------------------------------------|
| Sector 7 / Night / Squad                                         |
| Accept countdown: 00:12                                          |
|                                                                  |
| You        [ACCEPTED]                                            |
| Player2    [PENDING]                                             |
| Player3    [ACCEPTED]                                            |
|                                                                  |
| Loadout locked. Cancelling now returns to Squad Lobby.           |
|------------------------------------------------------------------|
| [Decline]                                      [Accept]          |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Make waiting understandable and cancellable where rules allow |
| Layout | Selected mission summary, squad status, queue timer, region/ping, tips |
| Primary CTA | Cancel Queue until match lock |
| Secondary actions | Voice/chat, inspect mission rules, settings shortcut |
| Loading link | Uses `LT_LobbyToMatch` when match begins; see [Loading Screen Design](LoadingScreen_Design.md) |

### Matchmaking States

| State | Behavior |
| :--- | :--- |
| Searching | Queue time, estimate, region, squad cards |
| Expanding search | Explain MMR/region expansion if used |
| Match found | Countdown and readiness lock |
| Player declined | Return to lobby with explanation |
| Server error | Retry, change region, or cancel |
| Cancel locked | Explain why cancellation is disabled after match allocation |

---

## Platform Input Mapping

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Change tab | Click / number keys | LB/RB | Swipe or tab row |
| Ready toggle | Click / Space | A / Cross | Tap CTA |
| Hold deploy | Hold mouse / key | Hold A / Cross | Hold CTA with accessible tap alternative |
| Invite | Click Invite | Y / Triangle | Tap Invite |
| Open chat | Enter | Focus chat / virtual keyboard | Chat button |
| Cancel queue | ESC / click | B / Circle | Cancel button with confirm |

---

## Analytics

| Metric | Use |
| :--- | :--- |
| Mode select conversion | Identify confusing rules or reward tuning |
| Map select dwell time | Detect unreadable map risk |
| Deploy blocked reason | Improve validation and defaults |
| Queue cancel reason | Tune matchmaking estimates |
| Squad not-ready duration | Improve readiness visibility |
| Match found decline rate | Detect queue mismatch or unclear commitment |

---

## Acceptance Checklist

- [ ] Mode and map rules are visible before queue.
- [ ] Deploy cannot be blocked without an actionable reason.
- [ ] Squad lobby clearly shows who is blocking deploy and why.
- [ ] Matchmaking communicates cancel availability and queue state.
- [ ] Mobile has a persistent selected mission summary.
- [ ] Ranked/event restrictions are explained before commitment.
