---
title: "UX Flows & Wireframes"
type: docs
weight: 22
---

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |
| [Out-of-Raid Screens](Out_Of_Raid_Screens.md) | Home, loadout, stash, quests, profile |
| [Pre-Raid Screens](Pre_Raid_Screens.md) | Mode/map/deploy/squad/matchmaking flow |
| [Post-Raid Screens](Post_Raid_Screens.md) | Result, loot, replay, redeploy flow |

---

## Player Journey Map

### Session Flow (The "Happy Path")

```mermaid
graph TD
    Start(App Launch) --> L1[L1 Boot]
    L1 --> L2[L2 Splash]
    L2 --> Platform{Platform Check}
    Platform -->|PC/Console| Login{Auth Check}
    Platform -->|Mobile| MobileOpt[Mobile-Optimized Splash]
    MobileOpt --> Login
    
    Login -- New User --> Tutorial[Tutorial Mission]
    Login -- Returning --> DailyReward{Daily Login Bonus}
    DailyReward --> L3[L3 PostLogin]
    Tutorial --> L3
    L3 --> MainMenu[Main Menu / Safe House]
    
    MainMenu --> Prep[Preparation Phase]
    Prep -->|Select Loadout| LoadoutUI[Loadout Screen]
    Prep -->|Browse Traders| TradersUI[Traders / Market]
    Prep -->|Manage Stash| InventoryUI[Inventory / Stash]
    
    LoadoutUI -->|Ready| MatchmakingUI[Matchmaking Lobby]
    MatchmakingUI -->|Squad Full| MapSelection[Map Selection]
    MapSelection --> L4[L4 LobbyToMatch]
    
    L4 --> Spawn[In-Raid Gameplay]
    
    Spawn -->|Death| DefeatScreen[Death Screen]
    Spawn -->|Extract Success| ExtractionUI[Extraction Animation]
    Spawn -->|Time Expired| ForceExtractUI[Emergency Extraction]
    
    DefeatScreen --> DeathCam[Death Replay]
    ExtractionUI --> L5[L5 IngameToResult]
    ForceExtractUI --> L5
    DeathCam --> L5
    
    L5 --> Summary[After Action Report]
    
    Summary -->|Continue| L6[L6 ResultToMain]
    Summary -->|Quit| End(Session End)
    L6 --> MainMenu
```

**Loading nodes (L1–L8):** See [Loading Screen Design](LoadingScreen_Design.md) for full taxonomy. L7 (Map Transition) and L8 (Reconnect) apply to multi-zone raids and disconnect recovery respectively.

<!-- REF_IMAGE: Player session flow diagram — full-color version of the mermaid chart above with visual polish and game-specific artwork -->

---

## Cross-Platform Wireframe Sets

### 1. Main Menu / Safe House (The Hub)

**Goal:** Immediate "Play" CTA while showcasing progression across all platforms.

#### **Desktop/Console Layout (16:9 Landscape)**

```
+------------------------------------------------------------+
| [Profile: Lvl 12]  EXTRACTION ROYALE  [₽ 425,000] [$10]    |
|                                                            |
|              [3D OPERATOR MODEL - SPOTLIGHT]               |
|         (Character Preview with Equipped Gear)             |
|                                                            |
|                    [ ▶ START RAID ]                        |
|               (Pulsing Orange Action Button)               |
|                   [Solo | Duo | Squad ▼]                   |
|                                                            |
| +----------------+ +----------------+ +----------------+   |
| | [LOADOUT]      | | [TRADERS]      | | [HIDEOUT]      |   |
| |  Customize     | |  Buy/Sell      | |  Upgrades      |   |
| +----------------+ +----------------+ +----------------+   |
|                                                            |
| [Battle Pass Tier 12/50]      [Friends Online: 3]  []      |
+------------------------------------------------------------+
```

<!-- REF_IMAGE: Main Menu high-fidelity mockup — showing the PC/Console landscape layout with the Neo-Industrial visual style -->

**Key Differences:**
*   **Mobile:** Vertical stacking, simplified labels, larger touch targets
*   **Desktop:** Horizontal layout, more info density, mouse-over tooltips
*   **Console:** D-Pad grid navigation with clear highlight states

---

### 2. Inventory Management ("The Tetris")

**Goal:** Efficient sorting and equipping across input methods.

#### **Desktop (Mouse + Keyboard)**

```
+--------------------------------------------------------------------+
| < BACK        STASH (12x40 Grid)                   [Sort] []       |
| ------------------------------------------------------------------ |
| [GRID VIEW - DRAG & DROP]               | [EQUIPPED LOADOUT]       |
| +-----------------------------------+   | +----------------------+ |
| | [] [] [Rifle    ] [] []           |   | | PRIMARY: AK-74M      | |
| | [] [] [         ] [] []           |   | | DMG 45  RPM 650      | |
| | [] [Vest      ] [] [] []          |   | +----------------------+ |
| | [] [          ] [] [] []          |   | [HELMET] [ARMOR Lv3]     |
| | [] [] [] [] [] [] []              |   | [RIG 12] [PACK 24L]      |
| +-----------------------------------+   | [SECURE 4] Protected     |
| FILTERS: [Weapons] [Meds] [Ammo]        | Weight: 24.5 / 40kg      |
| [SELL ALL JUNK] [AUTO SORT]             | Speed: -15%              |
+--------------------------------------------------------------------+
```

<!-- REF_IMAGE: Inventory Management mockup — showing PC drag-and-drop grid view, Console cursor mode, and Mobile list view -->

#### **Console (Controller)**

```
+--------------------------------------------------------------------+
| STASH                         [LB/RB Tabs]            [Y=Sort]     |
| ------------------------------------------------------------------ |
| GRID CURSOR MODE                        | [EQUIPPED LOADOUT]       |
| +--[Selected Item]----------------+     | +----------------------+ |
| | AK-74M Rifle                    |     | | PRIMARY: Empty      |  |
| | Durability: 85%                 |     | | HELMET  ARMOR       |  |
| | Value: RUB 45,000               |     | | RIG     BACKPACK    |  |
| +---------------------------------+     | +----------------------+ |
|                                                                    |
| [A] Equip     [X] Drop     [B] Back     [Y] Quick-Sell             |
| Navigation: D-Pad grid                 Left Stick scroll           |
+--------------------------------------------------------------------+
```

#### **Mobile (Touch)**

```
+------------------------------------+
| STASH             [Sort] [Filter]  |
| ---------------------------------- |
| [SWIPE SCROLL LIST VIEW]           |
| +------------------------------+   |
| | AK-74M                Equip |    |
| | Medkit                  Use |    |
| | Battery                Drop |    |
| +------------------------------+   |
|                                    |
| [EQUIPPED]      [Weight Bar]       |
| [Rifle] [Helmet] [Armor]           |
|                                    |
| [TAP TO EQUIP]                     |
+------------------------------------+
```

**Platform Interactions:**
*   **PC:** Drag & Drop primary. Right-click context menus. Middle-click to quick-examine.
*   **Console:** Cursor-based grid navigation. Hold button to preview stats. Double-tap to equip.
*   **Mobile:** Swipe to scroll. Tap to select. Long-press for context menu. Pinch to zoom grid.

---

### 3. In-Raid HUD (Gameplay Overlay)

**Goal:** Minimal obstruction, maximum information. Adapt to screen size & input.

#### **PC/Console (Landscape)**

```
+------------------------------------------------------------+
| [HEALTH]  [STAMINA]          EXTRACT: 15:32    [MINIMAP]   |
| [ 100] [ 85%]                               [ NE ]         |
|                                                            |
|                                                            |
|                    [GAMEPLAY AREA]                         |
|               (Minimal HUD Interference)                   |
|                                                            |
|                                                            |
| [PRIMARY ]                                         [SQUAD] |
| [AK-74 | 30/120]                               [ Player1 ] |
| [GRENADE x2]                                   [ Player2 ] |
|                                                [ Player3 ] |
+------------------------------------------------------------+

PROXIMITY INDICATORS (Dynamic):
- Red pips on compass for nearby enemies (180° FOV)
- Blue markers for squadmates (through walls)
- Yellow ! for loot containers (within 25m)
```

#### **Mobile (Portrait - Condensed)**

```
+---------------------------+
| 100 85% [⏱15:32][]        |
|                           |
|                           |
|   [GAMEPLAY]              |
|                           |
|                           |
|                           |
| [] [FIRE] [RELOAD][JUMP]  |
| [JOYSTICK] AK 30/120      |
+---------------------------+

ADAPTIVE CHANGES:
- Auto-hide UI elements after 3 seconds of inactivity
- Tap minimap to expand full-screen
- Swipe down from top to access inventory (pauses movement)
```

---

### 4. Looting Interface (In-Raid Risk/Reward)

**Goal:** Speed vs. Risk. Looting partially blocks vision and movement.

#### **PC (Fast Cursor-Based)**

```
+------------------------------------------------------------+
| (75% BLURRED GAME BACKGROUND - DANGER VISIBLE)    [X]      |
|                                                            |
| CONTAINER: Dead PMC              YOUR BACKPACK             |
| +----------------------+      +------------------------+   |
| |  M4A1      [TAKE]    |  >>  |  AK-74                 |   |
| |  IFAK      [TAKE]    |      |  Medkit                |   |
| |  Key308    [TAKE]    |      | [____Empty Slot____]   |   |
| |  $15,000   [TAKE]    |      | [____Empty Slot____]   |   |
| +----------------------+      +------------------------+   |
|                                                            |
| [TAKE ALL] (Hold F - 2 sec)    Weight: 32kg / 40kg         |
|                                Movement: -25% Speed        |
+------------------------------------------------------------+
```

#### **Console (Simplified List)**

```
+------------------------------------------------------------+
| LOOTING CONTAINER                                 [B] CLOSE|
|                                                            |
| D-PAD TO SELECT:                                           |
| >  M4A1 Rifle                            [A] Take          |
|    IFAK Medkit                           [A] Take          |
|    Marked Room Key                       [A] Take          |
|    Rubles (₽15,000)                      [A] Take          |
|                                                            |
| [Y] LOOT ALL (Hold 2 sec)         Backpack: 32/40 kg       |
+------------------------------------------------------------+
```

**Tension Mechanics:**
*   **Screen Obstruction:** 60-75% screen coverage (can still see threats)
*   **Movement Penalty:** Cannot sprint while looting
*   **Audio Cue:** Looting sounds attract nearby AI/players
*   **Progress Bar:** "Loot All" requires 2-second commitment (animation lock)

---

### 5. Social Flow (Party, LFG, Clan)

#### System Diagram

```
Home / Social Button
        |
        v
+------------------+     +------------------+     +------------------+
| Friends / Recent | --> | Party Panel      | --> | Squad Lobby      |
| invite, message  |     | ready, privacy   |     | deploy blockers  |
+------------------+     +------------------+     +------------------+
        |
        v
+------------------+     +------------------+
| LFG Board        | --> | Clan Hub         |
| join/create post |     | roster, chat     |
+------------------+     +------------------+
```

### 6. Progression / LiveOps Flow

#### System Diagram

```
Home event card -> Event Hub -> Track Objective -> Raid -> AAR
       |              |              |             |
       v              v              v             v
 Battle Pass     Reward Inbox    Quest Board    Claim / Redeploy
       |
       v
Ranked Overview -> Leaderboard -> Season Summary
```

#### Progression / Reward Claim Journey

```
+--------------------------------------------------------------------------------+
| Entry: Home Badge / AAR Row / Battle Pass Tile / Event Objective / Inbox       |
|--------------------------------------------------------------------------------|
| 1. Source Context -> 2. Progress Detail -> 3. Claim / Track / Play / Upgrade    |
| 4. Capacity + Expiry Check -> 5. Reward Destination -> 6. Return / Next Goal    |
+--------------------------------------------------------------------------------+
```

| Step | Required Behavior |
| :--- | :--- |
| Source context | Preserve whether the player came from AAR, Battle Pass, Event Hub, Quest Board, Ranked, News, or Inbox |
| Progress detail | Show objective, XP/tier progress, free/premium status, timer, reward, and blocker |
| Action | Claim, Track, Play, View Rules, or Commerce Upgrade must be mutually clear |
| Capacity/expiry check | Stash full, cap reached, expired, offline, premium locked, or duplicate states show next action |
| Destination | Reward lands in stash, inbox, profile, currency balance, battle pass, trader unlock, or season archive |
| Return | Back returns to the source screen; next goal suggests deploy, track, claim next, or view summary |

#### Season / Event Participation Journey

```
News/Home -> Event Hub -> Rule Review -> Track Objective -> Queue/Raid
    -> AAR Progress -> Reward Claim -> Grace/Archive/Season Summary
```

| Phase | Required Behavior |
| :--- | :--- |
| Announcement | Show start/end, rules, rewards, affected maps/modes, and restrictions |
| Participation | Deep link to exact playable route with event rules applied |
| Progress | AAR and Event Hub agree on objective count, reward state, and event currency |
| Ending | Promote unclaimed rewards, conversion policy, and claim grace |
| Archive | Read-only recap keeps achievements/rewards understandable after reset |

### 7. Settings / System Error Flow

#### State Diagram

```
Settings Open -> Change Option -> Apply
      |              |            |
      v              v            v
 Platform Lock   Unsaved      Success Toast
      |              |
      v              v
 Reason + Help   Revert / Confirm

System Error -> Retry available? -> Retry -> Success
      |              |
      |              no
      v              v
 Support Path    Exit / Update / Offline
```

---

## State Machine Examples

### Button States (Universal Across Platforms)

1.  **Normal:** Default color (Steel Gray #6B7280), 100% opacity
2.  **Hover (PC):** Highlight border (Tactical Blue #3B82F6), 110% scale
3.  **Selected (Console):** Gold outline (#FACC15), subtle pulse animation
4.  **Pressed:** 90% scale + haptic feedback (controller/mobile)
5.  **Disabled:** 50% opacity, grayscale filter
6.  **Loading:** Spinner overlay, 75% opacity

### Feedback Loop Standards

#### **Positive Actions** (Success)
*   **Visual:** Green flash (#22C55E), item icon flies to inventory slot
*   **Audio:** Satisfying "click" + item-specific sound (metal clank, fabric rustle)
*   **Haptic:** Single medium pulse (200ms)

#### **Negative Actions** (Error)
*   **Visual:** Red shake animation (5px amplitude, 3 cycles)
*   **Audio:** Error buzz (low pitch, 100ms)
*   **Haptic:** Double short pulse (100ms each)

#### **Process Indicators** (Ongoing)
*   **Searching Body:** Circular progress bar around cursor/crosshair (2 seconds)
*   **Healing:** Radial fill around health bar (5-10 seconds)
*   **Reloading:** Magazine icon slide animation (weapon-specific timing)

---

## Platform-Specific Navigation Patterns

### PC (Keyboard Priority)
*   **Tab:** Cycle through HUD elements (Inventory → Map → Squad)
*   **ESC:** Hierarchical back (closes deepest menu first)
*   **Spacebar:** Confirm/Select (secondary to mouse click)
*   **Hold Shift:** Quick-loot mode (auto-transfers items to backpack)

### Console (D-Pad Grid)
*   **D-Pad:** Navigate UI grid (horizontal/vertical)
*   **Analog Stick:** Free cursor mode in menus (toggleable)
*   **A/X (Confirm):** Context-sensitive (Pickup/Use/Open/Talk)
*   **B/Circle (Cancel):** Always goes back one menu level
*   **Shoulder Buttons (LB/RB):** Tab switching in multi-panel menus

### Mobile (Gesture-Based)
*   **Tap:** Select/Confirm
*   **Double-Tap:** Quick equip (bypass confirmation)
*   **Long-Press:** Context menu (Discard/Examine/Use)
*   **Swipe Left/Right:** Navigate tabs (Stash → Traders → Safe House)
*   **Pinch:** Zoom in inventory grid (mobile-exclusive)
*   **Two-Finger Swipe Down:** Quick access to settings (global gesture)

---

## Performance Optimization for UI

### Rendering Best Practices
*   **UI Canvas Resolution:** Locked to 1080p with upscaling for 4K (reduces draw calls)
*   **Texture Atlases:** All icons in 2048x2048 sprite sheets (max 3 atlases total)
*   **Dynamic Batching:** UI elements grouped by material to minimize state changes
*   **Occlusion Culling:** Hidden menus fully disabled, not just invisible

### Platform-Specific FPS Targets
| Platform           | UI Target FPS |           Gameplay Target FPS           |
| :----------------- | :-----------: | :-------------------------------------: |
| PC (High-End)      |    144 FPS    |               120-144 FPS               |
| PC (Mid-Range)     |    60 FPS     |                 60 FPS                  |
| Console (Next-Gen) |    60 FPS     | 60 FPS (Performance) / 30 FPS (Quality) |
| Console (Last-Gen) |    30 FPS     |                 30 FPS                  |
| Mobile (Flagship)  |    60 FPS     |                 60 FPS                  |
| Mobile (Mid-Tier)  |    30 FPS     |                 30 FPS                  |

---

## User Testing Scenarios

### Scenario 1: First-Time Player (Tutorial)
**Task:** Complete first raid without opening manual.  
**Success Metrics:**
*   No tutorial skips
*   <5% drop-off before first extraction
*   Post-mission comprehension quiz >70% correct

### Scenario 2: Experienced Player (Speed)
**Task:** Equip loadout and enter matchmaking.  
**Success Metrics:**
*   PC: <15 seconds
*   Console: <25 seconds
*   Mobile: <30 seconds

### Scenario 3: Cross-Platform Switching
**Task:** Player moves from PC to Mobile mid-session.  
**Success Metrics:**
*   Zero confusion on control scheme (auto-detect)
*   All progression synced within 5 seconds
*   No re-tutorial required

---

## Accessibility-Specific Flows

### Colorblind Mode (Protanopia Example)
*   **Red Enemy Indicators → Orange/Purple**
*   **Green Friendly Markers → Blue**
*   **Yellow Loot → White with border**
*   **Rarity Colors:** Use shapes + text labels, not just color

### Screen Reader Support (Mobile Priority)
*   All buttons have accessible labels ("Equip Primary Weapon" not "Button 5")
*   Menu navigation reads current position ("Inventory, Item 3 of 15")
*   Critical alerts read aloud ("Extraction available. 2 minutes remaining.")

### Motor Impairment Assist
*   **Auto-Run Toggle:** Single tap to move (no constant pressure)
*   **Hold-to-Confirm Timeout:** Adjustable 0.5-3 seconds
*   **Aim Assist Slider:** 0%-100% magnetism strength

---

## Designer Handoff Mapping

Use this page to understand journey order and transition intent. Use the linked screen group pages for layout, component, state, and input detail.

| Flow | Canonical Detail Page | Designer Check |
| :--- | :--- | :--- |
| Boot to Home | [Settings & System Screens](Commerce_Settings_System_Screens.md), [Loading Screen Design](LoadingScreen_Design.md) | loading/account errors and setup states are explicit |
| Home to Queue | [Out-of-Raid Screens](Out_Of_Raid_Screens.md), [Pre-Raid Screens](Pre_Raid_Screens.md) | deploy blockers and risk confirmation are preserved |
| Queue to Raid | [Pre-Raid Screens](Pre_Raid_Screens.md), [Loading Screen Design](LoadingScreen_Design.md) | match found, cancel lock, and L4 loading states align |
| In-Raid Action | [HUD Design](HUD_Design.md), [In-Raid Screens](In_Raid_Screens.md), [Notification Systems](Notification_Systems.md) | overlays preserve combat readability and audio awareness |
| Raid to Results | [Post-Raid Screens](Post_Raid_Screens.md), [Loading Screen Design](LoadingScreen_Design.md) | outcome, loot, replay, and redeploy validation are clear |
| Social Coordination | [Social Screens](Social_Screens.md) | invite, voice, privacy, and safety states are respected |
| LiveOps Progression | [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) | rewards, expiry, premium/free, and claim blockers are visible |
| Commerce Purchase | [Commerce Screens](Commerce_Screens.md), [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) | offer, preview, price, confirmation, receipt, and upgrade routes are explicit |
| Settings Recovery | [Settings & System Screens](Commerce_Settings_System_Screens.md), [Global UX Standards](Global_UX_Standards.md) | apply/revert, locks, errors, and support routes are explicit |

### Commerce Purchase Journey

```
Entry
  Home Shop tab / Battle Pass Upgrade / Event Store / Insufficient Balance / Redeem Link
    -> Offer Card or Deep Link Target
    -> Offer Detail / Bundle Detail / Item Preview
    -> Optional Currency Top-Up
    -> Purchase Confirmation
    -> Platform Checkout Handoff when required
    -> Purchase Result / Receipt
    -> Equip / View Owned / Back to Shop / Purchase Help
```

| Step | Required Trust State |
| :--- | :--- |
| Entry | Source context preserved so Back returns to Home, Battle Pass, Event, or blocked offer |
| Offer | Price, ownership, timer, restriction, and non-power context visible |
| Preview | Compatibility and variant limits visible before purchase |
| Top-up | Localized provider price and platform handoff shown before leaving game UI |
| Confirmation | Final price, balance impact, contents, refund/platform note, and hold-to-confirm when required |
| Provider handoff | Pending/cancelled/failed/succeeded states return to a receipt/result surface |
| Receipt | Granted items, provider/reference id, support route, and duplicate-charge-safe copy visible |

### Flow QA Checklist

- [ ] Each journey transition has a clear source screen, destination screen, and failure state.
- [ ] Any flow that risks gear, currency, account access, privacy, or player safety includes confirmation/consequence copy.
- [ ] Mobile flow variants preserve primary CTA reachability and do not rely on desktop hover.
- [ ] Flow diagrams do not contradict screen-level CTAs or disabled-state rules.
