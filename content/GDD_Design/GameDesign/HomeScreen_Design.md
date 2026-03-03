---
title: "Home Screen & Main Lobby Design"
type: docs
weight: 16
---

## Overview

The Home Screen is the **first thing a player sees every session** and the **last thing they see before a raid**. It must simultaneously serve as an orientation hub, a character showcase, a social space, and a quick-launch pad for gameplay. Done correctly, the Home Screen reinforces the player's emotional investment in their operator and communicates the game's identity at a glance.

> **Cross-References:** [Hero Abilities](../Gameplay/Hero_Abilities.md) — operator classes and ability descriptions shown in showcase; [GameModes](GameModes.md) — all modes accessible from Home Screen; [Progression](Progression.md) — progression widget data source; [LiveOps](LiveOps.md) — news feed and event content; [Economy](Economy.md) — shop integration; [TutorialRaid](TutorialRaid.md) — first-launch Home Screen state; [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — deploy flow continues into matchmaking.

---

## 1. Design Philosophy & Goals

### Three Core Goals

| Goal | Design Intent | Anti-Pattern to Avoid |
| :--- | :------------ | :-------------------- |
| **Identity** | The Home Screen is the player's *locker room*. Their chosen operator IS their avatar. The home screen should feel personal and owned. | Tarkov's cold, sterile menus — no character presence, no emotional connection. |
| **Clarity** | Any feature should be reachable within ≤2 taps/clicks from the Home Screen. No buried menus, no dead ends. | Warframe's Orbiter — powerful and immersive but overwhelming for new players (too many unlabelled stations). |
| **Immersion** | The Home Screen is a tactical staging area, not a menu screen. It should *feel alive* — ambient sound, operator breathing, environmental details. | Overwatch 2's over-advertising approach — the home screen becomes a billboard instead of a player sanctuary. |

### Design Words

- **Alive** — the operator moves, reacts, and has presence
- **Focused** — one clear primary action (Deploy)
- **Personal** — the screen reflects the player's choices (operator, skin, last raid)
- **Efficient** — minimum steps to any destination

---

## 2. Operator Showcase System

The operator showcase is the **centerpiece** of the Home Screen — a 3D viewport rendering the player's currently selected operator in real-time, visible at all times regardless of which panel is active.

### Viewport Position & Size

| Layout | Position | Viewport Width | Viewport Height | Character Placement |
| :----- | :------- | :------------- | :-------------- | :------------------ |
| PC (16:9) | Left 1/3 of screen | 33% | 100% (full height) | Character at bottom 20% of viewport, fills ~60% of viewport height |
| PC (21:9 Ultrawide) | Left 25% of screen | 25% | 100% | Same scaling |
| Mobile Portrait | Full-bleed background | 100% | 100% | Character at center-bottom, fills ~50% of screen height |
| Mobile Landscape | Left 40% | 40% | 100% | Similar to PC |
| Tablet | Left 35% | 35% | 100% | Same as PC |

**Key positioning rule:** The operator's face and upper torso must always be visible and unobstructed by UI elements. Navigation panels overlay the *right side* of the screen — the left 1/3 (operator viewport) is **protected space**, UI-free.

### Background Environment

The operator does not stand in an empty void. They stand in a **diegetic staging environment** — a stylized version of the Aethelgard world:

| Default Scene | Description |
| :------------ | :---------- |
| **Exterior: Aethelgard Dusk** | Industrial rooftop, foggy horizon, amber skyline. Default scene. Ambient dust particles. |
| **Interior: Safehouse Bunker** | Concrete walls, tactical maps pinned, warm lamp light. Unlocked at Account Level 10. |
| **Ranked: Operations Command** | Cold blue LED lighting, holographic screens, sterile tactical aesthetic. Shown when in Ranked queue focus. |

**Featured Map Scene (LiveOps):** During seasonal events, the background changes to reflect the featured map. Example: snow-covered ruins during "Zero Winter" event.

**Player customization:** Unlockable background environments per [Economy](Economy.md) Cosmetics system. Up to 8 environment variants planned for launch.

### Operator Animation State Machine

The operator runs a real-time animation state machine with 5 states. Transitions are blended (0.3s crossfade between states).

```
┌──────────────────────────────────────────────────────────────────┐
│                     OPERATOR ANIMATION FSM                        │
│                                                                   │
│  ┌──────────────┐   idle 30s    ┌──────────────────────────────┐  │
│  │  IDLE LOOP   │──────────────▶│  PASSIVE ACTIVITY            │  │
│  │  (breathing) │               │  (equipment check / stretch) │  │  
│  └──────┬───────┘               └──────────────┬───────────────┘  │
│         │                                       │                  │
│   hover/│                               returns │ after 8s         │
│   touch │                               to IDLE │                  │
│         ▼                                       │                  │
│  ┌──────────────┐                               │                  │
│  │  CAM REACT   │◀──────────────────────────────┘                  │
│  │  (looks at   │       any hover                                  │
│  │   camera +   │                                                  │
│  │   voice line)│◀──────────────────────────────────────           │
│  └──────┬───────┘           tap/click on operator                  │
│         │                                                          │
│   click │ head                                                     │
│         ▼                                                          │
│  ┌──────────────┐   long press   ┌──────────────────────────────┐  │
│  │  SIGNATURE   │                │  INSPECT MODE                │  │
│  │  GESTURE     │   (hold 0.5s)  │  (360° rotation, drag to     │  │
│  │  (unique per │────────────────▶  spin, tap to exit)          │  │
│  │   operator)  │                └──────────────────────────────┘  │
│  └──────────────┘                                                  │
└──────────────────────────────────────────────────────────────────┘
```

#### State Details

| State | Trigger | Animation | Duration |
| :---- | :------ | :-------- | :------- |
| **IDLE LOOP** | Default; after any state returns | Subtle breathing, weight shift every 8–12s (randomized) | Infinite loop |
| **PASSIVE ACTIVITY** | Idle >30s with no player input | Operator inspects weapon, cracks neck, adjusts gear, glances off-camera | 6–10s sequence, then returns to IDLE |
| **CAM REACT** | Player hover over operator OR mouse enters viewport | Operator turns head, makes eye contact with camera. Triggers a random voice line. | 2–3s head turn animation; voice line plays simultaneously |
| **SIGNATURE GESTURE** | Click/tap directly on operator's head or torso | Operator performs their unique gesture (each operator has 1 default + 2 unlockable). | 3–5s non-looping, returns to IDLE |
| **INSPECT MODE** | Long press (0.5s hold) anywhere on operator | Camera orbits operator. Player drag = rotation. Tap anywhere outside = exit. | Until dismissed |

#### Player Interaction Reactions — Full Detail

| Player Action | Operator Response | Voice Line Probability |
| :------------ | :---------------- | :--------------------- |
| **Mouse enters viewport / First hover** | Operator turns head toward camera. Slight posture sharpening. | 70% — plays a greeting or readiness line |
| **Click/tap on operator body** | CAM REACT + leans slightly forward | 100% — plays a line from operator's "taunts" pool |
| **Click/tap on operator head** | SIGNATURE GESTURE (unique per operator) | No voice line — gesture IS the expression |
| **Idle 30s** | PASSIVE ACTIVITY starts | 30% — mutters something under breath (ambient quality) |
| **Idle 90s** | Sheathe animation + operator sits on ledge / leans against wall | 20% — long ambient line ("feels like another long wait…") |
| **Long press 0.5s** | INSPECT MODE — 360° rotation viewport unlocks | No voice — ambient sound effect of equipment shift |
| **Return from completed raid (success)** | Victory pose plays for 3s then returns to IDLE | 100% — post-extraction victory line |
| **Return from failed raid (death)** | Operator dusts off, checks wounds briefly | 80% — determined / stoic recovery line |
| **Operator not played in 7+ days** | Special "missed you" animation on first login | 100% — unique "been a while" voice line |

#### Voice Line Pool — Per Operator (Minimum Requirements)

Each operator must have the following voice lines recorded for Home Screen use:

| Category | Count | Examples (Mamba — Assault) |
| :-------- | :---: | :------------------------- |
| Greeting (first hover) | 3 | "Ready when you are." / "Another run?" / "Let's do this." |
| Readiness (hover) | 5 | "Locked and loaded." / "Zone's waiting." / "Light me up." |
| Taunt/Personality (body click) | 5 | "You gonna stare or we gonna fight?" / "I don't miss." |
| Idle ambient (30s) | 4 | "Still waiting…" / *loads magazine* |
| Post-extract victory | 2 | "That's how it's done." / "Fortune favors." |
| Post-death recovery | 2 | "Not today." / "I'll be back for that gear." |
| Long idle (90s) | 2 | "Are we doing this or what?" / *yawns subtly* |
| "Been a while" (7-day) | 1 | "Finally. I was starting to think you forgot about me." |
| **TOTAL minimum** | **24** | — |

---

## 3. Home Screen Layout — PC / Console

### Zone Breakdown

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         HOME SCREEN — PC (16:9)                             │
├──────────────┬──────────────────────────────┬──────────────────────────────┤
│              │                              │                               │
│  OPERATOR    │      DEPLOY PANEL            │   RIGHT SIDEBAR               │
│  SHOWCASE    │      (Center Stage)          │                               │
│              │                              │  ┌────────────────────────┐  │
│  [3D Render] │  ┌──────────────────────┐   │  │ PROGRESSION WIDGET     │  │
│              │  │  [OPERATOR NAME]     │   │  │ Lvl 34 ████████░░ 74%  │  │
│              │  │  [CLASS] · [MASTERY] │   │  │ Season Rank: GOLD II   │  │
│  Operator    │  └──────────────────────┘   │  │ Battle Pass: 44/100    │  │
│  stands at   │                              │  │ 3 Daily Quests Active  │  │
│  bottom,     │   ┌──────────────────────┐   │  └────────────────────────┘  │
│  face + body │   │  ◉  DEPLOY           │   │                               │
│  visible     │   │  [Primary Button]    │   │  ┌────────────────────────┐  │
│              │   └──────────────────────┘   │  │  NEWS & EVENTS         │  │
│              │                              │  │  ┌──────────────────┐   │  │
│              │  ┌────────────────────────┐  │  │  │ SEASON 3: FROST  │  │  │
│              │  │ MODE SELECT:           │  │  │  │ 6 days remaining │  │  │
│              │  │ [Raid] [Blitz] [Scav]  │  │  │  └──────────────────┘  │  │
│              │  │ [Ranked] [Co-op]       │  │  │  - Viktor sale 24h     │  │
│              │  └────────────────────────┘  │  │  - New map: Ironworks  │  │
│              │                              │  └────────────────────────┘  │
│              │  ┌────────────────────────┐  │                               │
│              │  │ SQUAD: [P1] [+] [+]    │  │  ┌────────────────────────┐  │
│              │  └────────────────────────┘  │  │  FRIENDS ONLINE (4)    │  │
│              │                              │  │  ○ Kai_V  [Hawk] Lv29  │  │
│              │                              │  │  ○ DXTR   [Mamba] Lv41 │  │
│              │                              │  │  + 2 more...            │  │
│              │                              │  └────────────────────────┘  │
├──────────────┴──────────────────────────────┴──────────────────────────────┤
│  [Home]  [Armory]  [Stash]  [Safe House]  [Traders]  [Ranked]  [Shop]  [⚙️]   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Navigation Bar — Bottom Rail

| Tab | Icon | Shortcut (PC) | Content |
| :-- | :--- | :------------ | :------ |
| **Home** | 🏠 House | `H` | Returns to operator showcase + deploy panel |
| **Armory** | 🔫 Gun | `A` | Weapon loadout, attachment editor, operator skin |
| **Stash** | 📦 Box | `S` | Full stash grid, item management, insurance queue |
| **Safe House** | 🏚️ Shelter | `D` | Safe House modules, crafting queue, upgrade tree. See [Safe House Design](Safe_House_Design.md). |
| **Traders** | 🏪 Shop | `T` | 5 trader screens, quest turn-in, barter |
| **Ranked** | 🏆 Trophy | `R` | Season rank, leaderboard, ranked queue |
| **Shop** | 💎 Diamond | `P` | Cosmetics store, battle pass |
| **Settings** | ⚙️ Gear | `Esc / ,` | Audio, graphics, controls, accessibility |

---

## 4. Home Screen Layout — Mobile

### Portrait Mode (Primary)

```
┌─────────────────────────────────┐
│                                 │
│     [OPERATOR — full bleed bg]  │  ← Operator rendered full screen
│     Character at foreground,    │     background = staging environment
│     bottom half of screen       │
│                                 │
│                   ┌───────────┐ │
│                   │ Rank ●    │ │  ← Season rank badge (top-right)
│                   │ Lv34 GOLD │ │
│                   └───────────┘ │
│                                 │
│  ┌─────────────────────────────┐│
│  │ SEASON 3: FROST EVENT       ││  ← News banner (dismissible)
│  │ 6 days left ►               ││
│  └─────────────────────────────┘│
│                                 │
│  ┌─────────────────────────────┐│
│  │    ◉  DEPLOY                ││  ← Primary CTA — thumb zone
│  └─────────────────────────────┘│
│                                 │
│  [Raid ▼]  [Blitz] [Scav]      │  ← Mode quick-select pills
│                                 │
├─────────────────────────────────┤
│ 🏠   🔫   📦   🏚️   🏪   💎   │  ← Bottom nav (6 tabs)
└─────────────────────────────────┘
```

### Mobile Gesture Support

| Gesture | Action |
| :------ | :----- |
| **Tap operator** | CAM REACT + voice line |
| **Long press operator** | INSPECT MODE (360° drag) |
| **Swipe left on center panel** | Open Armory |
| **Swipe right on center panel** | Open Stash |
| **Swipe up on news banner** | Open full news/events screen |
| **Pull down anywhere** | Refresh online status / friend list |
| **Two-finger spread on operator** | Zoom in for cosmetic detail inspection |

### Mobile Bottom Nav — 6 Tabs

| Tab | Icon | Content |
| :-- | :--- | :------ |
| **Home** | 🏠 | Operator showcase + deploy |
| **Armory** | 🔫 | Loadout + weapon + operator cosmetics |
| **Stash** | 📦 | Stash + Safe House combined |
| **Missions** | 📋 | Quests + traders + objectives |
| **Social** | 👥 | Friends + squad + recent players |
| **Shop** | 💎 | Store + battle pass |

> **Note on mobile vs PC:** Safe House and Traders are merged under "Missions" tab on mobile to stay within 6-tab limit (the thumb-reachable zone). Both are listed as sub-tabs within.

---

## 5. Game Mode Quick Access Panel

Located in the center panel below the operator name display.

### Mode Selector UI

```
┌─────────────────────────────────────────────────────┐
│  SELECT MODE                                        │
│                                                     │
│  [● THE RAID ]  [ BLITZ ]  [ SCAV RUN ]            │
│                                                     │
│  [ RANKED ♦ ]  [ CO-OP ]  [ FEATURED ★ ]          │
│                                                     │
│  SELECTED: THE RAID                                 │
│  ┌─────────────────────────────────────────────────┐│
│  │ 📍 Aethelgard Industrial  👤 Solo  ⏱ 15-30min  ││
│  │ ⚠ RISK: High — Gear fear active                 ││
│  └─────────────────────────────────────────────────┘│
│                                                     │
│  Queue:  ○ Solo  ○ Duo  ● Trio    Est. ~45s         │
│                                                     │
│  ◉ DEPLOY                                           │
└─────────────────────────────────────────────────────┘
```

### Mode Preview Cards

Each mode has a preview card that appears when selected:

| Mode | Map Preview | Player Count | Duration | Risk Badge |
| :--- | :---------- | :----------- | :------- | :--------- |
| **The Raid** | Featured map thumbnail | 8–16 players | 15–30 min | ⚠ HIGH |
| **Blitz** | Small-map thumbnail | 6–10 players | 8 min | ⚡ MEDIUM |
| **Scav Run** | Same as current Raid map | 8–16 players | 10–20 min | ✅ ZERO |
| **Ranked Ops** | Featured ranked map | 8–12 players | 20–30 min | ♦ EXTREME |
| **Co-op (Blackout)** | Horde map | 1–3 players | 15 min | 🛡 MEDIUM |
| **Featured ★** | Event-specific | Varies | Varies | Varies |

### Queue Size Selector

Before deploying, the player selects their squad size:
- **Solo** — queues into solo-matching pool
- **Duo** — requires 2 confirmed members
- **Trio** — requires 3 confirmed members (squad must be full to queue)

Estimated queue time is displayed dynamically next to the selector, updated every 10s from the matchmaking server per [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md).

**Auto-fill option:** Solo players can opt into a "Auto-Fill Duo/Trio" toggle — system will match with an LFG (Looking For Group) player. Shown as a checkbox below the squad selector.

---

## 6. Full Navigation Flow

```
                         ┌─────────────┐
                         │  HOME SCREEN│
                         └──────┬──────┘
                                │
          ┌──────────────────────┼──────────────────────┐
          ▼                      ▼                       ▼
    ┌─────────┐           ┌─────────────┐         ┌──────────┐
    │ ARMORY  │           │   DEPLOY    │         │  SOCIAL  │
    │         │           │   FLOW      │         │  PANEL   │
    │ - Weapons│          │             │         │          │
    │ - Operator│         │ Mode Select │         │ Friends  │
    │   cosmetics│        │ Squad Setup │         │ Party    │
    │ - Loadout │         │ Insurance   │         │ LFG      │
    │   presets │         │   check     │         │ Recent   │
    └─────┬────┘          │ → Matchmaking│        └──────────┘
          │               └─────────────┘
          ▼
    ┌─────────┐
    │  STASH  │
    │         │
    │ - Item grid│
    │ - Sorting │
    │ - Insurance│
    │   queue   │
    └─────┬────┘
          │
          ▼
    ┌─────────┐           ┌─────────────┐         ┌──────────┐
    │ HIDEOUT │           │  TRADERS    │         │  RANKED  │
    │         │           │             │         │          │
    │ - Modules│          │ - Viktor    │         │ - Season │
    │ - Craft  │          │ - Ada       │         │   rank   │
    │   queue  │          │ - Vasilis   │         │ - Ladder │
    │ - Upgrade│          │ - Militia   │         │ - Queue  │
    └──────────┘          │ - Black Mkt │         └──────────┘
                          └─────────────┘
          ┌──────────┐                            ┌──────────┐
          │   SHOP   │                            │ SETTINGS │
          │          │                            │          │
          │ - Battle │                            │ - Audio  │
          │   Pass   │                            │ - Graphics│
          │ - Skins  │                            │ - Controls│
          │ - Store  │                            │ - Access. │
          └──────────┘                            └──────────┘
```

### Navigation Rules

- **Back navigation:** All screens have a `←` back button + `Esc` on PC. Always returns to previous screen, never resets to Home.
- **Home shortcut:** `H` key (PC) or tap 🏠 tab always returns to Home Screen from anywhere.
- **Deep link:** Clicking the progression widget takes player directly to Progression screen. Clicking a specific quest in Home screen news takes player directly to that trader's quest board.
- **Breadcrumb trail:** Top of every non-Home screen shows: `Home > Armory > Weapon` — each crumb is clickable.
- **No dead ends:** Every screen has a clear path back or forward. No screens without exit.

---

## 7. News & Events Feed

### PC — Right Sidebar (Events Block)

Positioned below the Progression Widget in the Right Sidebar.

| Content Type | Format | Duration Shown |
| :----------- | :----- | :------------- |
| **Season Feature (Banner)** | Large card with countdown — most prominent | Full season duration |
| **Limited-Time Mode** | Medium card with "NEW" badge | While event is active |
| **Trader Discount** | Small card with trader avatar + % icon | 24h sale window |
| **Patch Notes** | Text card with version number | 7 days post-patch |
| **Community Challenge** | Progress bar card showing global completion | While active |
| **Upcoming Event Preview** | "COMING SOON" card, greyed | 3 days before start |

**Max visible:** 4 cards at one time. Overflow scrollable (subtle scroll indicator).

**Priority order:** Season > LTM > Patch Notes > Trader Sale > Community > Upcoming.

### Mobile — Swipeable Banner

On mobile, News & Events is a horizontally swipeable banner between the operator showcase and the Deploy button:
- Auto-scrolls every 6s
- Player can manually swipe left/right
- Pagination dots shown beneath banner
- Tap → opens full news screen (overlay)

### News Deep-Link Behavior

- Tap "Trader Sale" card → opens that trader's screen directly
- Tap "Patch Notes" → in-game patch notes viewer (markdown renderer)
- Tap "LTM event" → directly queues into that mode's pre-lobby

---

## 8. Progression Summary Widget

Located at the top of the Right Sidebar (PC) or as a pull-down panel (Mobile).

### Widget Design — Compact View

```
┌────────────────────────────────────────────┐
│  ◈  MAMBA           Mastery ★★★★☆          │
│                                            │
│  ▌ACCOUNT Lv.34    ████████████░░░  74%   │
│  ▌SEASON  S3       ████████░░░░░░░  44/100│
│  ▌PASS    Premium  ████████████░░░  60/100│
│                                            │
│  📋 Daily: 2/3 quests done  [Go →]         │
│  ⚔ Last Raid: EXTRACTED  +1,240 XP        │
└────────────────────────────────────────────┘
```

### Widget Interactions

| Element | Click/Tap Action |
| :------ | :--------------- |
| Account Level row | → Opens full Account Progression screen |
| Season Rank row | → Opens Ranked Mode screen and current rank |
| Battle Pass row | → Opens Battle Pass screen |
| Daily quest count | → Opens quest board (filtered: Dailies) |
| Last Raid result | → Opens last session's Post-Game Debrief replay |
| Operator Mastery stars | → Opens Operator Mastery details for current operator |

---

## 9. Social Panel

### PC — Friends Panel (Bottom of Right Sidebar)

```
┌────────────────────────────────────────────┐
│  FRIENDS ONLINE — 4 / 12                  │
│  ──────────────────────────────────────── │
│  ● Kai_Virtanen    [Hawk]   Lv.29          │
│    > In Raid — Industrial Zone             │
│                         [Invite to Squad]  │
│  ● Dxt_Raptor      [Mamba]  Lv.41          │
│    > In Lobby — Solo queue                 │
│                         [Join Their Squad] │
│  ● NightSeal99     [Glitch] Lv.17          │
│    > In Safe House                         │
│                         [Invite to Squad]  │
│  ● 4R3S             [Ghost] Lv.55          │
│    > In Ranked Lobby                       │
│                         [Invite to Squad]  │
│  ──────────────────────────────────────── │
│  [View All Friends]        [Find Players]  │
└────────────────────────────────────────────┘
```

### Social Panel — Full Screen (via View All Friends)

| Section | Content |
| :------ | :------ |
| **Party / Current Squad** | Shows all squad slot (1–3). Empty slots show [+Invite] button. |
| **Friends** | Full friend list, sorted by: Online first; then Last Active |
| **LFG (Looking For Group)** | Players who flagged themselves as LFG — filterable by operator class, level range, mode |
| **Recent Players** | Players met in the last 5 raids — tap to view profile, send friend request, or report |
| **Blocked List** | Access via ⚙️ icon in social panel |

### Party Management

| Action | Trigger |
| :----- | :------ |
| Invite friend to squad | "Invite" button in friends list |
| Set squad to open (LFG auto-fill) | Toggle in squad panel |
| Kick player from squad | Long press of player slot → "Remove" |
| Transfer party leader | Long press of player slot → "Make Leader" |
| Lock squad (prevent new joins) | Lock icon on squad panel |
| Set squad voice chat channel | Auto-assigned on squad creation |

---

## 10. Operator & Cosmetics Quick Access

The operator showcase viewport includes a quick-access cosmetics panel, expanding from the left edge of the viewport when the player hovers the operator or presses a hotkey.

### Quick Access Cosmetics Tray (PC)

```
┌─────────────────────────────────────────────────────────────┐
│  MAMBA — CUSTOMIZATION                         [Full Armory]│
│  ─────────────────────────────────────────────────────────  │
│  Skin:    [Tactical Black ▼]   [Shadow Ops ▼]  [◀ ▶]       │
│  Emote:   [Lock & Load ▼]                      [◀ ▶]       │
│  Badge:   [Iron Extraction ★]                  [◀ ▶]       │
│  Title:   ["The Last Extract"]                 [◀ ▶]       │
│  ─────────────────────────────────────────────────────────  │
│  OPERATOR SWITCH:  [Hawk] [Glitch] [Bastion] [Ghost] [+...]  │
└─────────────────────────────────────────────────────────────┘
```

### Operator Switch Row

- Clicking a different operator immediately transitions the showcase viewport to that operator (0.5s slide-out / slide-in transition)
- New operator walks onto screen from the side (animated entrance)
- If operator not yet unlocked: shows lock icon + unlock tooltip

### Cosmetics Preview

- Changing skin: Operator in viewport instantly applies new skin (real-time update)
- Changing emote: Operator plays emote in-viewport as preview (one time only, returns to IDLE)
- All changes auto-saved

### Mobile Quick Cosmetics

On mobile, the cosmetics tray is accessed by a small "🎨 Customize" button floating at the top of the operator viewport. Opens a bottom sheet half-screen with the same options.

---

## 11. Audio Design

### Background Music

| State | Music Track | Description | Loop Duration |
| :---- | :---------- | :---------- | :------------ |
| **Default idle** | `home_ambient_01.wav` | Dark industrial ambient — distant metalwork sounds, low drone, sparse percussion | 2:15 loop |
| **Queue searching** | `queue_building_01.wav` | Slightly elevated tension — adds rhythmic element to base ambient | 1:30 loop |
| **Match found** | `match_found_sting.wav` | 2s alert sting, then crossfade to matchmaking lobby music | 2s one-shot |
| **Season event active** | `season_theme_overlay.wav` | Seasonal motif layered over default ambient (e.g., ice crackle for winter event) | Crossfaded with base |
| **Post-extraction return** | `post_raid_victory.wav` | Brief 4-bar triumphant resolve, then fades to ambient | 10s one-shot |
| **Post-death return** | `post_raid_loss.wav` | Low, somber 3-bar resolve, fades to ambient | 8s one-shot |

**Music ducking:** When an operator voice line triggers, music volume reduces to 40% for the duration of the line, then re-fades up over 1.5s. No abrupt cuts.

### UI Sound Effects

| UI Action | Sound | Duration |
| :-------- | :---- | :------- |
| Navigate to new screen | Subtle whoosh + click | 0.15s |
| Hover over button | Soft tone (positive) | 0.1s |
| Click button (confirm) | Satisfying click + tone | 0.2s |
| Click button (cancel/back) | Reverse tone | 0.15s |
| Match found popup | Three-note alert sting | 0.5s |
| Operator switch | Footstep walk-on | 0.8s |
| News card expand | Paper unfold + tone | 0.3s |
| Progression level-up widget flash | Level-up chime | 1s |
| Friend invite received | Distinct two-note ping | 0.4s |

### Ambient Sound Layer (Environment)

The background staging environment has its own ambient audio layer independent of music:
- **Exterior: Aethelgard Dusk** — distant sirens, wind, metal creak, far-off gunshot echo
- **Interior: Safehouse Bunker** — dripping water, radio crackle, ventilation hum
- **Operations Command** — server fans, keyboard clicks, satellite beep

Volume: 20% of master SFX volume. Always present underneath music.

---

## 12. Performance & Tech Notes

### Operator Model on Home Screen

The operator model displayed on the Home Screen is a **LOD2 variant** of the in-game model:

| Property | In-Raid Model | Home Screen Model |
| :-------- | :------------ | :---------------- |
| Polygon count | ~15,000 tris | ~8,000 tris |
| Texture resolution | 2048×2048 | 1024×1024 |
| Bone count (rig) | 90 bones | 60 bones (simplified rig) |
| Shadow casting | Dynamic | Pre-baked shadow map |
| Animation updates | 60Hz | 30Hz (sufficient for lobby idle) |

### Mobile Performance Tiers

| Device Tier | Operator Showcase | Background Environment | Particle FX |
| :---------- | :---------------- | :--------------------- | :----------- |
| **High-end** (iPhone 15+, S24) | Full animation, full LOD2 | Full dynamic scene | Full ambient particles |
| **Mid-range** (iPhone 12, S21) | Full animation, simplified LOD | Static background image | Reduced particles |
| **Low-end** (budget Android) | Static pose + breathing only | Color-gradient background | None |

**Low-end fallback:** On low-end devices, the operator is displayed as a high-quality static 2D render (not a 3D model) with a subtle idle breathing animation via sprite-frame swap. This is still visually engaging but removes 3D rendering overhead.

### Loading State (L3_PostLogin)

This loading phase corresponds to **L3_PostLogin** in the [Loading Screen Design](../UI_UX/LoadingScreen_Design.md) taxonomy. When the Home Screen loads (first launch or return from raid):
- **0–300ms:** Background loads first (instant for static; fade-in for dynamic)
- **300–800ms:** Operator model shimmer-in animation (render appears with 0→100% opacity + slight scale from 0.95→1.0)
- **800ms+:** Animation state machine activates; idle loop begins

For full L3 layout (operator showcase, tips, fun facts, progress bar), see [Loading Screen Design — L3_PostLogin](../UI_UX/LoadingScreen_Design.md#43-l3_postlogin).

---

## 13. Onboarding & State Variants

### First Launch State (New Player)

| Element | Behavior |
| :------ | :------- |
| Operator displayed | Mamba (default / first operator selected in Tutorial) |
| Background | Exterior: Aethelgard Dusk (non-customizable on first launch) |
| News feed | "WELCOME TO AETHELGARD" banner + link to tutorial |
| Operator animation | Operator waves at camera on first load (1× only, never repeats) |
| Deploy button | Pulsing glow + "START TUTORIAL" text override |
| Navigation bar | Dimmed except Home and (after tutorial) Armory |
| Progression widget | Shows empty state: "Complete your first raid to begin tracking" |
| Guided arrow | Animated arrow pointing from operator toward Deploy button |

### Returning Player State (Standard)

All elements show their current state. No guided arrows. Last selected operator is shown.

### Post-Raid Return States

| Raid Outcome | Operator Pose | Operator Voice Line | Screen Difference |
| :----------- | :------------ | :------------------ | :---------------- |
| **EXTRACTED** | Victory stance (weapon raised briefly), then IDLE | "That's how it's done." | Loot summary toast appears for 5s bottom-right |
| **KIA** | Brushes off dust, checks arm | "Not today." | "Continue?" toast: retry with same loadout (if sufficient stash) |
| **MIA (disconnect)** | Idle (no special pose) | None | "Connection lost" yellow warning toast |
| **Time Out** | Head shake, then IDLE | "Too close." | Standard return |

### Operator Not-Played Variant (7+ Day Absence)

Triggered once per 7-day session gap. On first login after long absence:
- Operator does the "been a while" animation first instead of idle
- Progress widget shows "Welcome back!" instead of standard header
- A streak-break "welcome back package" notification appears (if applicable per LiveOps)

---

## 14. Cross-References

- [Loading Screen Design](../UI_UX/LoadingScreen_Design.md) — L3_PostLogin loading phase; operator showcase, tips, fun facts during load.
- [Hero Abilities](../Gameplay/Hero_Abilities.md) — Operator names, class descriptions, and ability names shown in operator tooltip on Home Screen.
- [GameModes](GameModes.md) — All 5 game modes (Raid, Blitz, Scav Run, Ranked, Co-op) with descriptions used in Mode Quick Access Panel.
- [Progression](Progression.md) — Account Level XP thresholds, Season Rank data source for Progression Widget.
- [LiveOps](LiveOps.md) — Events, patch schedule, and featured modes driving the News & Events Feed.
- [Economy](Economy.md) — Monetization model; cosmetics available in Quick Access tray and shop tab.
- [TutorialRaid](TutorialRaid.md) — First-launch Home Screen state corresponds to post-tutorial first return.
- [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — Deploy button flows into matchmaking; queue time estimate sourced from matchmaking server.
- [Post-Game Debrief](../Gameplay/Post_Game_Debrief.md) — Last Raid widget links to previous session's debrief screen.
- [Quest & Objective System](../Gameplay/Quest_Objective_System.md) — Daily quest count widget links to quest board.
- [Operator Synergy Guide](../Gameplay/Operator_Synergy_Guide.md) — Operator selection from Home Screen informs synergy display in squad panel.
