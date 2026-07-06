---
title: Menus & Screens
type: docs
weight: 1
---


### Menu Design Philosophy

Every menu screen follows these rules:

1. **Maximum 3 clicks** to reach any action from the Main Menu
2. **Consistent back navigation** — ESC/B always goes one level up, never closes the game
3. **No dead-end screens** — every screen has a clear "next action" or "back" option
4. **Platform parity** — same information across PC, Console, and Mobile, adapted for input method

> For settings screen details (graphics, audio, controls, gameplay), see [User Settings](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/UserSettings/README.md).

***

### Main Menu / Safe House

The Main Menu is the player's home base — it must communicate safety, progression, and readiness.

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
|  [Profile: Lv.12]      EXTRACTION PROTOCOL      [Credits: 425K]  |
|  [Faction: Salvage 3]                            [Premium: 10]    |
|------------------------------------------------------------------|
|                                                                    |
|              [3D OPERATOR MODEL - SPOTLIGHT RENDER]                |
|         Equipped gear visible on model. Rotatable (drag/stick)    |
|                                                                    |
|                      [ START RAID ]                                |
|                   (Primary CTA — pulsing border)                   |
|                   [Solo | Duo | Squad  ▼]                          |
|                                                                    |
|  +-------------+  +-------------+  +-------------+  +-----------+ |
|  | LOADOUT     |  | TRADERS     |  | STASH       |  | HIDEOUT   | |
|  | Gear Up     |  | Buy / Sell  |  | Manage Loot |  | Upgrades  | |
|  +-------------+  +-------------+  +-------------+  +-----------+ |
|                                                                    |
|  [Battle Pass: Tier 12/50]    [Daily Quests: 1/3]   [Friends: 3]  |
|  [News / Events]              [Seasonal Timer]      [Settings]    |
+------------------------------------------------------------------+
```

#### Layout (Mobile Portrait)

```
+-----------------------------+
|  Lv.12    Credits: 425K     |
|  [Faction Badge]   [$10]    |
|-----------------------------|
|                             |
|  [3D OPERATOR - CENTERED]   |
|  (Tap to rotate)            |
|                             |
|      [ START RAID ]         |
|      [Solo|Duo|Squad ▼]    |
|                             |
|  [======== 12/50 ========]  |
|  Battle Pass                |
|                             |
|  +------+ +------+ +------+|
|  |LOAD  | |TRADE | |STASH ||
|  |OUT   | |RS    | |      ||
|  +------+ +------+ +------+|
|                             |
|  [Quests]  [Friends] [Gear] |
+-----------------------------+
```

#### Element Specifications

| Element             | Behavior                                                                | Platform Differences                                                      |
| ------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Operator Model      | 3D render, rotatable, shows equipped gear in real-time                  | PC: mouse drag. Console: right stick. Mobile: finger swipe                |
| Start Raid Button   | Primary CTA. Animated border pulse (1s cycle). Leads to Map Selection   | Same across platforms. 60x200px min touch target on mobile                |
| Mode Selector       | Dropdown: Solo, Duo (2-player), Squad (3-4 player)                      | PC: click dropdown. Console: cycle with bumpers. Mobile: horizontal swipe |
| Navigation Cards    | Grid of 4 cards leading to sub-screens                                  | PC: hover highlight. Console: D-pad focus. Mobile: tap. 44x44px min       |
| Battle Pass Bar     | Progress bar showing current tier. Tap/click to open Battle Pass screen | Same across. Shows "NEW" badge when unclaimed reward available            |
| Daily Quest Summary | Shows X/3 daily quests completed. Click for full quest list             | Same across                                                               |
| Friends List        | Count of online friends. Expandable panel                               | PC: small overlay. Console: full-screen panel. Mobile: slide-up sheet     |

***

### Loadout Screen

Players assemble their gear before entering a raid. The design must communicate: what you bring, what it costs, and what you risk losing.

#### Layout

```
+------------------------------------------------------------------+
|  < BACK               LOADOUT                    [PRESETS ▼]      |
|------------------------------------------------------------------|
|                                                                    |
|  [OPERATOR MODEL]        EQUIPMENT SLOTS          STATS SUMMARY   |
|  (Shows gear on body)    +------------------+    +---------------+|
|                          | Primary    [AK-74]|    | Weight: 24kg  ||
|  [ < | Preset 1 | > ]   | Secondary  [PM  ] |    | Armor: Lv.3   ||
|                          | Melee     [Knife] |    | Speed: -15%   ||
|                          | Helmet   [SSH-68] |    | Ergo: 42      ||
|                          | Armor    [6B23-1] |    | Total: 125K   ||
|                          | Rig      [Triton] |    +---------------+|
|                          | Backpack [Berkut] |                     |
|                          | Secure   [Alpha] |    [INSURE: 12,500]|
|                          +------------------+    [INSURE ALL]     |
|                                                                    |
|  +------------------------------------------------------------+   |
|  | STASH (Quick Access)       [Filter ▼] [Sort ▼] [Search]    |   |
|  | [Item][Item][Item][Item][Item][Item][Item][Item][Item][Item] |   |
|  | [Item][Item][Item][Item][Item][Item][Item][Item][Item][Item] |   |
|  +------------------------------------------------------------+   |
|                                                                    |
|  [SAVE PRESET]    [CLEAR ALL]    [READY - GO TO MAP SELECTION]    |
+------------------------------------------------------------------+
```

#### Key Interactions

| Action        | PC                                                 | Console                                 | Mobile                                 |
| ------------- | -------------------------------------------------- | --------------------------------------- | -------------------------------------- |
| Equip item    | Drag from stash to slot, or right-click "Equip"    | A on item → Equip option                | Tap item → Equip button                |
| Compare items | Hover over item → tooltip with stat comparison     | Hold A on item → comparison overlay     | Long-press → comparison sheet          |
| Remove item   | Right-click → "Unequip" or drag back to stash      | X on equipped slot → returns to stash   | Swipe left on equipped slot            |
| Insure items  | Click "Insure All" or right-click individual items | Y button → Insurance overlay            | Toggle checkbox per item, tap "Insure" |
| Save preset   | Click "Save Preset" → name input → confirm         | Select "Save Preset" → virtual keyboard | Tap "Save" → name input                |
| Switch preset | Dropdown selector above loadout                    | LB/RB to cycle presets                  | Swipe left/right on preset name        |

#### Preset System

* Maximum **10 saved presets** per player
* Preset stores: all equipment slots, attachment configurations, ammo loads
* "Smart Fill" option: auto-fills a preset from stash using best available matching items
* Missing items highlighted in red with "Find in Traders" shortcut

***

### Trader / Market Screen

Players buy, sell, and barter with faction vendors. Each faction has its own trader with reputation-gated inventory.

#### Layout

```
+------------------------------------------------------------------+
|  < BACK        TRADERS         [Salvage | Tech | Underground | PK]|
|------------------------------------------------------------------|
|                                                                    |
|  [TRADER PORTRAIT]    AVAILABLE ITEMS         YOUR OFFER          |
|  Viktor Koval         +------------------+   +------------------+ |
|  Salvage Corps        | AK-74M    45,000 |   | From Stash:      | |
|  Rep: Level 3         | 5.45 BP x60  800 |   | [Drag items here]| |
|  "Fair trades, kid."  | Medkit     2,500 |   |                  | |
|                       | [LOCKED Lv.4]    |   | Total Value:     | |
|  [BUY] [SELL] [BARTER]| [LOCKED Lv.5]    |   | 0 credits        | |
|                       +------------------+   +------------------+ |
|                                                                    |
|  FILTERS: [All | Weapons | Ammo | Gear | Meds | Barter]           |
|  SORT:    [Price ▼ | Name | New | Favorites]                      |
|                                                                    |
|  +------------------------------------------------------------+   |
|  | YOUR STASH (Sell Mode)                  [Quick-Sell Junk]   |   |
|  | [Item][Item][Item][Item][Item][Item][Item][Item][Item]       |   |
|  +------------------------------------------------------------+   |
+------------------------------------------------------------------+
```

#### Trader Tab Modes

| Mode       | Left Panel                                  | Right Panel                         | Action                               |
| ---------- | ------------------------------------------- | ----------------------------------- | ------------------------------------ |
| **Buy**    | Trader inventory (items for sale)           | Player wallet + purchase summary    | Select items → "Purchase" button     |
| **Sell**   | Player stash (sellable items)               | Sell value calculation              | Select items → "Sell" button         |
| **Barter** | Trader barter offers (item-for-item trades) | Required items checklist from stash | Drag required items → "Trade" button |

#### Reputation Gating Visual

* Available items: normal opacity, colored border matching rarity
* Locked items (higher rep required): 30% opacity, lock icon overlay, tooltip shows "Requires Reputation Level X"
* Newly unlocked items: "NEW" badge for 48 hours after unlocking

***

### Stash / Inventory Management

The primary item management screen, separate from the quick-access view in Loadout.

#### Layout

```
+------------------------------------------------------------------+
|  < BACK          STASH            [Search] [Filter ▼] [Sort ▼]   |
|------------------------------------------------------------------|
|                                                                    |
|  GRID VIEW (12 columns x N rows)                                  |
|  +------------------------------------------------------------+   |
|  | [===][===][      ][==][  ][  ][  ][  ][  ][  ][  ][  ]     |   |
|  | [===][Rifle     ][==][  ][  ][  ][  ][  ][  ][  ][  ][  ] |   |
|  | [  ][           ][==][  ][  ][Vest      ][  ][  ][  ][  ] |   |
|  | [  ][  ][  ][  ][  ][  ][           ][  ][  ][  ][  ][  ] |   |
|  | [  ][  ][  ][  ][  ][  ][  ][  ][  ][  ][  ][  ][  ][  ] |   |
|  +------------------------------------------------------------+   |
|                                                                    |
|  CAPACITY: 145 / 200 slots       TOTAL VALUE: 2,450,000 credits   |
|                                                                    |
|  ACTIONS: [Auto-Sort] [Sell Junk] [Move to Loadout] [Discard]     |
+------------------------------------------------------------------+
```

#### Grid Mechanics

| Mechanic       | Description                                          | Platform Input                                                              |
| -------------- | ---------------------------------------------------- | --------------------------------------------------------------------------- |
| Item placement | Items occupy grid cells based on size (1x1 to 2x4)   | PC: drag-drop. Console: cursor + A. Mobile: tap-to-select then tap-to-place |
| Rotation       | Rotate items 90 degrees to optimize space            | PC: R key while dragging. Console: Y while holding. Mobile: rotate button   |
| Stacking       | Same ammo/consumables stack (max per type varies)    | Automatic when placed on matching stack                                     |
| Quick transfer | Move item directly to equipped loadout slot          | PC: Ctrl+Click. Console: hold A. Mobile: double-tap                         |
| Search         | Text filter highlights matching items, dims others   | PC: Ctrl+F. Console: Y → virtual keyboard. Mobile: search bar               |
| Auto-Sort      | Reorganize all items for optimal space usage         | Single button press. Maintains category grouping                            |
| Quick-Sell     | Mark items for sale, batch sell to best-price trader | PC: middle-click to tag. Console: X to tag. Mobile: swipe-left              |

#### Stash Upgrades

|    Level    | Slots | Unlock Method                                    |
| :---------: | :---: | ------------------------------------------------ |
| 1 (Default) |  100  | Starting stash                                   |
|      2      |  150  | Safe House upgrade (50K credits + 10 materials)  |
|      3      |  200  | Safe House upgrade (200K credits + 25 materials) |
| 4 (Maximum) |  300  | Safe House upgrade (500K credits + 50 materials) |

***

### Map Selection Screen

After pressing "Start Raid," players choose their deployment destination.

#### Layout

```
+------------------------------------------------------------------+
|  < BACK              MAP SELECTION                    [READY]     |
|------------------------------------------------------------------|
|                                                                    |
|  +------------------+  +--------------------------------------+   |
|  | SECTOR 7         |  |                                      |   |
|  | Industrial Decay  |  |  [MAP PREVIEW IMAGE]                |   |
|  | Difficulty: Hard  |  |  Showing key landmarks and           |   |
|  | Bosses: 1        |  |  extraction points                   |   |
|  | Players: 8-12    |  |                                      |   |
|  | [SELECTED]       |  +--------------------------------------+   |
|  +------------------+                                              |
|  +------------------+  EXTRACTION POINTS:                         |
|  | DISTRICT 14      |  - Crossroads (Always open)                 |
|  | Urban Ruins      |  - Boat Extract (30s wait, conditional)     |
|  | Difficulty: Med  |  - Emergency Exit (last 5 min only)         |
|  | Bosses: 0        |                                              |
|  | Players: 6-10    |  TIME OF DAY: [Day | Dusk | Night ▼]       |
|  | [SELECT]         |                                              |
|  +------------------+  ESTIMATED WAIT: ~45 seconds                |
|  +------------------+                                              |
|  | FIREBASE DELTA   |  SQUAD STATUS:                              |
|  | Military Outpost |  Player1 (You) — READY                      |
|  | Difficulty: Extreme| Player2 — READY                           |
|  | [LOCKED Lv.30]   |  Player3 — NOT READY                        |
|  +------------------+                                              |
+------------------------------------------------------------------+
```

#### Map Card Information

| Field             | Source                                           | Purpose                          |
| ----------------- | ------------------------------------------------ | -------------------------------- |
| Map Name          | Static                                           | Identify the location            |
| Difficulty        | Static per map                                   | Set expectations for new players |
| Boss Count        | Dynamic (season-dependent)                       | Inform high-value target hunters |
| Player Count      | Range (varies by server load)                    | Indicate expected PvP density    |
| Extraction Points | Dynamic (randomized per session)                 | Pre-raid planning                |
| Time of Day       | Player selection (affects lighting, AI behavior) | Tactical choice                  |
| Lock Status       | Player level requirement                         | Progression gate                 |
| Estimated Wait    | Server matchmaking queue                         | Manage expectations              |

***

### Squad / Lobby Screen

The waiting room before a raid. Focused on readiness communication and social interaction.

#### Layout

```
+------------------------------------------------------------------+
|  < BACK              SQUAD LOBBY              [INVITE] [LEAVE]    |
|------------------------------------------------------------------|
|                                                                    |
|  +-------------------+  +-------------------+  +-----------------+|
|  | [OPERATOR MODEL]  |  | [OPERATOR MODEL]  |  | [EMPTY SLOT]   ||
|  | You (Leader)      |  | Player2            |  | [INVITE FRIEND]||
|  | Loadout: 24kg     |  | Loadout: 18kg     |  | or             ||
|  | Status: READY     |  | Status: NOT READY |  | [MATCH FILL]   ||
|  | [Inspect Gear]    |  | [Inspect Gear]    |  |                 ||
|  +-------------------+  +-------------------+  +-----------------+|
|                                                                    |
|  MAP: Sector 7 — Industrial Decay                                 |
|  TIME: Night                                                       |
|  MODE: Squad (3-player)                                            |
|                                                                    |
|  [Voice Chat: ON]  [Text Chat Field________________] [Send]       |
|                                                                    |
|  [CHANGE MAP]   [CHANGE LOADOUT]   [ DEPLOY  ] (requires all READY)|
+------------------------------------------------------------------+
```

#### Squad Interactions

| Action        | Description                                                          | Input                                 |
| ------------- | -------------------------------------------------------------------- | ------------------------------------- |
| Invite Friend | Open friends list, select player to invite                           | Button or slash command               |
| Match Fill    | Auto-fill empty slots with random matchmade players                  | Toggle option, only squad leader      |
| Inspect Gear  | View teammate's equipped loadout (no item details, just silhouettes) | Click/A on teammate card              |
| Ready Toggle  | Mark yourself as ready (green) or not ready (gray)                   | Button press                          |
| Deploy        | Squad leader only. Requires all members READY. Starts matchmaking    | Hold for 1 second (prevents misclick) |
| Voice Test    | Microphone icon shows voice activity indicator                       | Automatic (push-to-talk or open mic)  |
| Kick Player   | Squad leader only. Opens confirmation dialog                         | Right-click / hold on player card     |

***

### After Action Report

Post-raid summary screen. Must serve two purposes: emotional payoff (or processing) and data review.

#### Layout (Successful Extraction)

```
+------------------------------------------------------------------+
|                    EXTRACTION SUCCESSFUL                           |
|                    Sector 7 — Industrial Decay                     |
|                    Raid Duration: 18:42                             |
|------------------------------------------------------------------|
|                                                                    |
|  LOOT ACQUIRED (sorted by value)            XP BREAKDOWN          |
|  +----------------------------------+      +--------------------+ |
|  | AK-74M (FIR)           45,000    |      | Kills:      +450   | |
|  | Body Armor Lv.4        38,000    |      | Looting:    +320   | |
|  | Prometheus Data (Quest) [QUEST]  |      | Healing:    +80    | |
|  | Medical Supplies x3     6,000    |      | Extraction: +200   | |
|  | Misc Components x12     4,800    |      | Quest:      +500   | |
|  +----------------------------------+      | Survival:   +150   | |
|  TOTAL VALUE: 93,800 credits               +--------------------+ |
|                                             TOTAL XP: +1,700      |
|  QUEST PROGRESS:                                                   |
|  [x] Supply Run — Completed (3/3 rations delivered)                |
|  [/] Lab Rat — In Progress (1/1 document found, need to turn in)  |
|                                                                    |
|  COMBAT STATS:                                                     |
|  Kills: 5 (3 AI, 2 PMC)  |  Damage Dealt: 847  | Accuracy: 34%  |
|  Damage Taken: 420        |  Heals Used: 3       | Headshots: 1   |
|                                                                    |
|  [CONTINUE TO STASH]          [VIEW REPLAY]         [MAIN MENU]  |
+------------------------------------------------------------------+
```

#### Layout (Death / Failed Extraction)

```
+------------------------------------------------------------------+
|                       KILLED IN ACTION                             |
|                  Sector 7 — Industrial Decay                       |
|                  Survived: 12:08 / 30:00                           |
|------------------------------------------------------------------|
|                                                                    |
|  CAUSE OF DEATH: Headshot by [PlayerName] (SVD Dragunov)           |
|                                                                    |
|  ITEMS LOST:                   ITEMS SAVED (Secure Container):    |
|  +------------------------+   +------------------------------+    |
|  | AK-74M         -45,000 |   | Quest Key (Lab)    [SAFE]    |    |
|  | Body Armor     -38,000 |   | Gold Chain         [SAFE]    |    |
|  | Backpack       -12,000 |   +------------------------------+    |
|  +------------------------+                                        |
|  TOTAL LOST: 95,000 credits   INSURANCE RETURN: ETA 24 hours     |
|                                                                    |
|  XP EARNED (partial):          QUEST PROGRESS:                     |
|  Kills: +200 | Looting: +150  | [x] Kill targets — Saved          |
|  Total: +350 (reduced 50%)    | [ ] Deliver items — Items lost    |
|                                                                    |
|  [CONTINUE]        [DEATH CAM]        [REPORT PLAYER]             |
+------------------------------------------------------------------+
```

#### Element Details

| Element        | Successful Extraction           | Failed Extraction                                    |
| -------------- | ------------------------------- | ---------------------------------------------------- |
| Header color   | Signal Green accent             | Critical Red accent                                  |
| Loot panel     | Items acquired with values      | Items lost with negative values                      |
| XP display     | Full XP earned                  | 50% XP penalty applied                               |
| Quest progress | Shows completed and in-progress | Shows which progress was saved vs. lost              |
| Combat stats   | Full stats displayed            | Same stats displayed                                 |
| Insurance      | Not shown (no loss)             | Shows estimated return time for insured items        |
| Death Cam      | Not available                   | Replay of final 10 seconds from killer's perspective |

***

### Battle Pass / Seasonal Screen

#### Layout

```
+------------------------------------------------------------------+
|  < BACK           SEASON 1: SHADOWS OF PROMETHEUS         [BUY]  |
|------------------------------------------------------------------|
|                                                                    |
|  CURRENT TIER: 12 / 50         TIME REMAINING: 47 days            |
|  [============================================-----------------]   |
|  XP to next tier: 2,400 / 5,000                                   |
|                                                                    |
|  TIER TRACK (horizontal scroll):                                   |
|  [10][11][ 12 ][13][14][15][16]...[48][49][50]                    |
|   X    X  [YOU]  ?   ?   ?   ?          ?   ?   LEGENDARY        |
|                                                                    |
|  SELECTED TIER 12:                                                 |
|  +----------------------------------+                              |
|  | FREE:    Title — "Zone Runner"   |                              |
|  | PREMIUM: Operator Skin — "Ghost" |                              |
|  | [CLAIM FREE] [UNLOCK PREMIUM]    |                              |
|  +----------------------------------+                              |
|                                                                    |
|  [VIEW ALL REWARDS]    [BUY PREMIUM PASS: $9.99]                  |
+------------------------------------------------------------------+
```

#### Battle Pass Rules

| Rule                  | Detail                                                                                 |
| --------------------- | -------------------------------------------------------------------------------------- |
| Free track            | All players earn tier progress. Cosmetics and minor consumables                        |
| Premium track         | Paid upgrade. Exclusive skins, emotes, and bonus XP                                    |
| XP sources            | Raids (time survived + extraction bonus), quest completion, daily/weekly               |
| Tier skip             | Players can purchase 1 tier skip per day (credits, not premium currency)               |
| Season end            | Unclaimed free rewards claimable for 2 weeks after season ends. Premium rewards locked |
| No gameplay advantage | Battle pass NEVER contains weapons, armor, or gameplay-affecting items                 |

***

### Settings Menu

#### Layout

```
+------------------------------------------------------------------+
|  < BACK              SETTINGS                                     |
|------------------------------------------------------------------|
|                                                                    |
|  [Graphics]  [Audio]  [Controls]  [Gameplay]  [Accessibility]     |
|                                                                    |
|  +------------------------------------------------------------+   |
|  |  GRAPHICS                                                   |   |
|  |                                                             |   |
|  |  Resolution:        [1920x1080 ▼]                           |   |
|  |  Display Mode:      [Fullscreen ▼]                          |   |
|  |  Quality Preset:    [High ▼]                                |   |
|  |  V-Sync:            [On | Off]                              |   |
|  |  FPS Limit:         [--- 144 ---]                           |   |
|  |                                                             |   |
|  |  ADVANCED:                                                  |   |
|  |  Texture Quality:   [High ▼]                                |   |
|  |  Shadow Quality:    [Medium ▼]                              |   |
|  |  Anti-Aliasing:     [TAA ▼]                                 |   |
|  |  ...                                                        |   |
|  +------------------------------------------------------------+   |
|                                                                    |
|  [RESET TO DEFAULT]    [APPLY]    [CANCEL]                        |
+------------------------------------------------------------------+
```

> For the full list of settings options, descriptions, and platform-specific defaults, see [User Settings](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/UserSettings/README.md).

#### Settings Tab Overview

| Tab           | Key Settings                                                           | Platform Differences                                                               |
| ------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Graphics      | Resolution, quality presets, FPS limit, individual graphical options   | PC: full control. Console: Performance/Quality toggle. Mobile: Low/Med/High preset |
| Audio         | Master, Music, SFX, Voice, Voice Chat volume. Spatial audio toggle     | Same across platforms. Mobile adds speaker/headphone detection                     |
| Controls      | Key bindings (PC), button mapping (console), HUD layout (mobile)       | Fully platform-specific. Cross-ref: each platform's control standards              |
| Gameplay      | Language, subtitle size, minimap style, auto-run, crosshair            | Same across platforms                                                              |
| Accessibility | Colorblind mode, text scaling, motion reduction, subtitles, aim assist | Same across platforms                                                              |

***

### Pause Menu (In-Raid System Overlay)

**Context**: Accessed during gameplay by pressing `ESC` (PC) or `Start/Menu` (Console). The game **does not pause** in online raids.

**Design Philosophy**: The menu acts as a translucent overlay. Players must maintain situational awareness — visuals remain visible through blur, and game audio continues unmuted.

#### Visual Style

* **Background**: Heavy frosted glass blur (Gaussian radius 15px). De-saturates the game world but keeps motion visible (enemy shadows, explosions)
* **Typography**: Oxanium (headers), Inter (body). High contrast white-on-dark
* **Layout**: Left column (actions), Right column (raid status), Bottom (squad info)

#### Menu Structure

| Section      | Elements              | Functionality                                                               |
| ------------ | --------------------- | --------------------------------------------------------------------------- |
| Main Actions | **Resume**            | Closes menu immediately                                                     |
|              | **Options**           | Opens Settings Menu (graphics, keybinds)                                    |
|              | **Statistics**        | Current session stats (kills, damage, XP so far)                            |
|              | **Abandon Raid**      | Critical Red button. Triggers "Confirm Disconnect" popup. Gear will be lost |
| Raid Status  | **Raid Timer**        | Countdown (e.g., `25:43`). Color turns red at under 10 minutes              |
|              | **Extraction Points** | List of available exits with status (Open, Conditional, Closed)             |
|              | **Network Info**      | Ping (ms), Packet Loss (%), Raid Hash ID                                    |
| Squad Info   | **Teammate Cards**    | Small widgets: Name, HP bar, Status (Alive / Dead / Extracting)             |

#### UX Safeguards

| Safeguard          | Description                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------ |
| Hold to Abandon    | "Abandon Raid" requires a 0.5-second hold to prevent panic clicks                          |
| Audio pass-through | Game audio is NOT muted. Footsteps and gunshots remain at 100% volume                      |
| Cursor mode        | Frees mouse cursor for UI interaction. Camera movement locked                              |
| Input override     | Pressing Tab (Inventory) or M (Map) while in this menu immediately switches to those views |
| Auto-dismiss       | If player takes damage while menu is open, menu closes automatically with a warning flash  |
