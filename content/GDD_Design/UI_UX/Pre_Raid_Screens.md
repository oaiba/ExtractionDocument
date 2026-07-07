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

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |
| [Out-of-Raid Screens](Out_Of_Raid_Screens.md) | Loadout, stash, quests, traders, safe house |
| [In-Raid Screens](In_Raid_Screens.md) | HUD, tactical map, looting, pause, reconnect |
| [Loading Screen Design](LoadingScreen_Design.md) | L4 lobby-to-match loading and reconnect transitions |

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
| [Cancel Queue]                         Status: can cancel        |
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

## Designer-Ready Screen Specs

The sections below are the canonical low-level handoff for pre-raid layout work. Summary tables above remain useful for navigation, but interaction, state, and visual requirements should be taken from these screen-level specs.

### Mode Select

#### Player Intent

Choose the ruleset that matches desired risk, squad size, reward, and time commitment before any gear is put at risk.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| < Back                              MODE SELECT                  Rules [i]     |
|--------------------------------------------------------------------------------|
| MODE CARDS                                                                     |
| +----------------+ +----------------+ +----------------+ +----------------+    |
| | SOLO           | | DUO            | | SQUAD          | | RANKED         |    |
| | 1 player       | | 2 players      | | 3-4 players    | | Lv15 required  |    |
| | Loss: Normal   | | Shared extracts| | High reward    | | Rank impact    |    |
| | [SELECTED]     | | [SELECT]       | | [SELECT]       | | LOCKED         |    |
| +----------------+ +----------------+ +----------------+ +----------------+    |
|--------------------------------------------------------------------------------|
| DETAIL: Solo | Risk Low | PvP Medium | Insurance Allowed | Queue 45s           |
| Rules: no revive, no shared quest progress, normal extraction rules            |
|--------------------------------------------------------------------------------|
| [Compare Rewards] [View Rules]                                      [SELECT]   |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Mode cards | Show squad size, loss rule, reward/risk summary, queue pool, selected/locked state |
| Detail panel | Explain selected mode rule changes before CTA |
| Action bar | Keep Select Mode stable; compare and rules are secondary |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Selected mode | Clear by border, label, and detail panel title |
| 2 | Rule/loss differences | Text labels required; never color-only badges |
| 3 | Locked/restricted modes | Show exact requirement and route to unlock |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Mode card | mode name, party size, risk, loss rule, reward modifier, queue estimate |
| Ranked card | rank impact, party restrictions, locked settings, unlock requirement |
| Event card | modifier, expiry, special extraction/loss changes |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Available | Select CTA active and detail panel populated |
| Locked | CTA disabled; requirement and unlock path visible |
| Event active | Badge includes time remaining and rule modifier |
| Disabled | Explain maintenance, region, or server pool issue |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse modes | Click card / arrows | D-pad grid | Horizontal card swipe |
| View rules | Click info | Focus + Y / Triangle | Tap info chip |
| Select | Click CTA / Enter | A / Cross | Sticky CTA |

#### Designer Notes

- Cards must be comparable at a glance; keep fields aligned.
- Do not hide loss rules in tooltips.
- Locked cards stay visible so players understand progression.

#### Acceptance Checklist

- [ ] Every mode shows squad size, loss rule, risk/reward, and queue expectation.
- [ ] Locked and disabled modes explain the exact reason.
- [ ] Selected state is visible without relying on color.

### Map Select

#### Player Intent

Pick a destination while understanding difficulty, extracts, player density, quest relevance, time of day, and queue impact.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| < Back                               MAP SELECT                       [Ready]  |
|--------------------------------------------------------------------------------|
| MAP LIST            | MAP PREVIEW / INTEL                       | DETAILS      |
| > Sector 7          | +---------------------------------------+ | Difficulty H |
|   District 14       | | map art, extracts, landmarks          | | Players 8-12 |
|   Firebase Delta    | | selected quest zone highlights        | | Boss: 1      |
|   The Mire LOCKED   | | danger zones and extracts             | | Time: Night v|
|---------------------| +---------------------------------------+ | Extracts 3   |
| Region Best Ping    | Extracts: Crossroads, Boat, Elevator      | Quests: 2    |
| Quest Relevant Only | Queue estimate: 45s                       | [SELECT MAP] |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Map list | Shows selected, locked, quest-relevant, event-modified, and unavailable maps |
| Preview | Uses map art/intel with extract markers, quest highlights, and risk zones |
| Details panel | Fixed summary: difficulty, player count, boss, time, extracts, quests, queue |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Selected map and Select/Ready CTA | Always visible |
| 2 | Extraction and risk rules | Must appear before commit |
| 3 | Quest relevance | Highlight useful maps without hiding others |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Map row | name, difficulty, availability, quest badge, event badge |
| Extract marker | name, rule type, availability, special requirements |
| Time selector | communicates visibility, AI, and queue differences |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Locked map | Show unlock source and preview permission |
| Unavailable region | Disable CTA and explain server/latency reason |
| High risk | Warn but allow selection unless mode blocks it |
| Quest mismatch | Show no relevant quests and a route to Quest Board |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse maps | Click list / arrows | D-pad list | Swipe list |
| Inspect extract | Hover/click marker | Focus marker | Tap marker |
| Change time | Dropdown | Focus selector | Bottom sheet |

#### Designer Notes

- Extract names and rules must be text-readable; marker icons are not enough.
- Keep map preview inspectable without becoming a tactical map replacement.

#### Acceptance Checklist

- [ ] Difficulty, extracts, player count, time of day, quests, and queue estimate are visible.
- [ ] Locked/unavailable maps provide a clear reason.

### Deploy Confirmation

#### Player Intent

Make one final informed commitment after seeing mode, map, squad, loadout blockers, gear value, insurance, quests, and queue estimate.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
|                                DEPLOY CONFIRMATION                             |
|--------------------------------------------------------------------------------|
| MISSION: Solo / Sector 7 / Night            Queue estimate: 45s                |
| SQUAD: You READY                            Fill: Off                          |
|--------------------------------------------------------------------------------|
| Gear value 125,000 | Weight 24/40kg | Ammo OK | Insurance 4/6 insured          |
| Quests: Supply Run, Lab Rat                                                    |
| WARNING: [!] 2 eligible items uninsured. [Insure All] [Review Items]           |
|--------------------------------------------------------------------------------|
| [Back to Loadout]                    [Insure All]             [HOLD TO DEPLOY] |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Mission summary | mode, map, time, queue, squad/fill |
| Loadout risk | gear value, weight, ammo, insurance, quests |
| Warning lane | blockers and warnings with direct fixes |
| CTA row | back, fix/insure, hold-to-deploy |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Hold to Deploy | Only primary when no blockers exist |
| 2 | Blocking warning | Must sit directly above CTA row |
| 3 | Gear value and insurance | Always visible for risk trust |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Hold CTA | Requires hold or equivalent accessible confirmation |
| Warning chip | Severity, item count, direct route |
| Quest summary | Top 1-3 relevant quests with extraction/FIR warning if needed |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Valid kit | Single hold-to-deploy action |
| Missing weapon | Block and focus weapon slot |
| Missing ammo | Warn or block per tuning with ammo filter action |
| Overweight | Block and route to loadout removal |
| High value | Require explicit risk acknowledgement |
| Ranked | Show rank impact and locked settings |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Deploy | Hold click / keyboard hold | Hold A / Cross | Hold sticky CTA |
| Fix blocker | Click warning | Focus warning + A | Tap warning |
| Back | Esc / click | B / Circle | Back button |

#### Designer Notes

- This screen is a trust checkpoint, not a dashboard.
- Disabled deploy must name the exact first blocker.

#### Acceptance Checklist

- [ ] Deploy never hides gear value, insurance, mode, map, and squad status.
- [ ] Every blocker has a direct fix action.

### Squad Lobby

#### Player Intent

Coordinate readiness, identify teammate blockers, manage invites, and let the leader deploy only when the party is valid.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| < Back                              SQUAD LOBBY              [Invite] [Leave]  |
|--------------------------------------------------------------------------------|
| +----------------+ +----------------+ +----------------+ +----------------+    |
| | You Leader     | | Player2        | | Empty Slot     | | Match Fill Off |    |
| | READY          | | NOT READY      | | [Invite]       | | Toggle         |    |
| | Sonar / Recon  | | Missing meds   | |                | |                |    |
| | Voice OK       | | Voice muted    | |                | |                |    |
| +----------------+ +----------------+ +----------------+ +----------------+    |
| Mission: Sector 7 / Night / Squad        Chat [______________________] [Send]  |
| WARNING: Deploy locked because Player2 has a blocker.                          |
|--------------------------------------------------------------------------------|
| [Change Map] [Change Loadout] [Voice Settings]              [DEPLOY LOCKED]    |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Player cards | identity, role, ready, blocker, voice, platform |
| Mission strip | selected map/mode/time and leader controls |
| Communication | chat and voice status without burying readiness |
| Action bar | invite, change map/loadout, deploy/ready |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Ready/blocker state | Clear per member |
| 2 | Leader deploy lock reason | Directly tied to CTA |
| 3 | Voice/chat | Secondary but visible |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Member card | player name, platform, operator, role, readiness, blocker reason |
| Empty slot | invite, match fill, close slot if supported |
| Leader controls | visible but disabled for non-leaders with reason |
| Voice state | muted/disconnected/push-to-talk labels |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Member not ready | Show reason if system knows it |
| Party mismatch | Explain platform, level, ranked, or region restriction |
| Leader only action | Disabled for members with text reason |
| Invite pending | Slot shows recipient and timeout/cancel |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Focus member | Click card | D-pad cards | Tap card |
| Invite | Click Invite | Focus empty slot | Invite sheet |
| Ready | Click CTA | A / Cross | Sticky CTA |

#### Designer Notes

- Squad readiness should read as operational status cards, not social profile cards.
- Do not expose exact teammate inventory; use blocker summaries.

#### Acceptance Checklist

- [ ] Leader and member views both show correct disabled states.
- [ ] Member blockers explain deploy lock.

### Matchmaking / Match Found

#### Player Intent

Understand queue progress, cancel rules, match found countdown, and reconnect/decline outcomes without ambiguity.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
|                                MATCHMAKING                                     |
|--------------------------------------------------------------------------------|
| Searching Sector 7 / Solo / Night                                              |
| [====================        ] 45s elapsed     Estimate 70s                    |
| Server region: Best Ping  Squad: 1/1  Loadout locked                           |
| Status: Finding compatible raid                                                |
|--------------------------------------------------------------------------------|
| MATCH FOUND: Accept within 15s                                                 |
| You: Accepted | Player2: Waiting | Player3: Declined                           |
|--------------------------------------------------------------------------------|
| [Cancel Queue]                                            [ACCEPT / DEPLOYING] |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Queue status | selected mission, elapsed, estimate, region, party state |
| Progress message | truthful current phase, not fake precision |
| Match found panel | countdown, accept states, failure outcome |
| Action bar | cancel before lock; accept when found |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Current queue/match state | Large status text |
| 2 | Countdown/cancel consequence | Always visible |
| 3 | Party accept status | Visible during match found |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Progress indicator | Can be indeterminate; must name current phase |
| Cancel CTA | Disabled after deployment lock with reason |
| Accept panel | Per-player accept status and timeout |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Searching | Show elapsed, estimate, and cancel |
| Timeout | Explain no match and offer retry/change region |
| Server error | Show retry and support code |
| Match found | Show accept countdown and party statuses |
| Player declined | Explain return path and whether queue restarts |
| Reconnecting | Show preserved slot and timeout |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Cancel | Click / Esc confirm | B / Circle confirm | Cancel button |
| Accept | Click / Enter | A / Cross | Large CTA |
| View details | Click mission | Focus mission | Tap mission |

#### Designer Notes

- Avoid fake progress percentages; use phase labels and elapsed time.
- Cancel copy must state if gear is still safe.

#### Acceptance Checklist

- [ ] Searching, timeout, error, match found, declined, and reconnecting states are covered.
- [ ] Player always knows whether cancel is safe.

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
