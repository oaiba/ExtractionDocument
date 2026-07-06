---
title: Pre-Raid Loadout & Preparation Screen
type: docs
weight: 17
---

# Pre-Raid Loadout & Preparation Screen

### Overview

The **Loadout Preparation Screen** is the tactical gateway between the Home Screen and a live raid. This is the most consequential UI in the game — it is where the player's strategy crystallizes into risk. Poor UX here is the #1 reason Escape from Tarkov loses new players. Our goal is **Tarkov's depth without Tarkov's friction**.

**Design goal:** A player who has never played our game before should be able to equip a weapon, insure it, select a map, and deploy within **90 seconds** on their first attempt. A veteran player should be able to execute a full kit swap from the previous raid's losses within **30 seconds**.

> **Cross-References:** [Home Screen & Lobby](HomeScreen_Design.md) — Deploy button flows into this screen; [Safe House Design](Safe_House_Design.md) — Workbench/stash accessed from Safe House; Loadout Preparation occurs in Operator Lounge within Safe House; [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — queue begins after Deploy confirmation; [Gear Mechanics](../Gameplay/Gear_Mechanics.md) — weight tiers, durability rules; [Gears](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/README.md) — [ArmorGear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/ArmorGear/README.md) and [StorageGear](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Gears/StorageGear/README.md) for armor/rig/backpack/secure container specs and loadout slots; [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md) — weapon mod changes accessible here; [Economy](Economy.md) — credit cost of insurance; [GameModes](GameModes.md) — the 5 game modes selectable on this screen; [Quest & Objective System](../Gameplay/Quest_Objective_System.md) — active quests drive loadout recommendations.

***

### 1. Design Philosophy — "The Ritual"

In every extraction shooter, the preparation phase is a **psychological ritual** that separates extraction games from traditional shooters:

| Attribute                      | Traditional Shooter           | Extraction Shooter                            |
| ------------------------------ | ----------------------------- | --------------------------------------------- |
| Pre-match                      | Select character, press start | Plan loadout, weigh risk, insure gear         |
| Emotional state entering match | Excitement, confidence        | Mix of anticipation, tension, and calculation |
| Design goal                    | Minimize friction             | _Contain_ friction — make it feel deliberate  |
| Time spent in prep             | 10–20 seconds                 | 1–3 minutes (ideal)                           |

**Three layers of the Ritual:**

1. **Equip** — What do I bring?
2. **Insure** — What am I willing to lose?
3. **Plan** — Where am I going and what do I want to accomplish?

Each layer should have its own distinct UI zone. Players should never feel lost between layers.

**Anti-patterns from Tarkov we explicitly avoid:**

*  Drag gear from stash in one window, then navigate to a separate insurance tab
*  Squad lobby on a separate screen from loadout
*  Map selection only accessible at queue confirmation
*  No visual representation of current loadout value at risk

***

### 2. PC / Console Layout

The loadout preparation screen is a **single unified screen** — no navigation required between tasks. Everything lives on one screen with three vertical columns.

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                      OPERATION PREP — AETHELGARD INDUSTRIAL                   │
│   [ ← Back to Home ]                           [  Settings ] [  Chat ]    │
├───────────────────┬───────────────────────────┬───────────────────────────────┤
│   LEFT COLUMN     │      CENTER COLUMN         │       RIGHT COLUMN            │
│   (Operator &     │   (Stash Quick Access)     │   (Mission & Squad)           │
│   Gear Preview)   │                            │                               │
│                   │  ┌────────────────────────┐│  ┌───────────────────────────┐│
│  [3D OPERATOR]    │  │  FILTER: [All▼][Wpn▼]  ││  │   MAP SELECTION           ││
│  wearing full     │  │  [Sort: Value/Slot▼]   ││  │   ┌───────────────────┐   ││
│  equipped loadout │  ├────────────────────────┤│  │   │ Aethelgard Ind.   │   ││
│                   │  │ [ M4A1      3.5kg] ││  │   │  Overcast  Risk:│   ││
│  ┌─────────────┐  │  │ [ AKM       3.8kg]  ││  │   │ Loot Bias: Weapons │   ││
│  │ PRIMARY    ▼│  │  │ [ HK416     3.2kg]  ││  │   └───────────────────┘   ││
│  │ [M4A1 ___] │  │  │ ───────────────────────││  │   [◀] [1/2] [▶]           ││
│  └─────────────┘  │  │ [Plate Carrier 4kg]  ││  │                           ││
│  ┌─────────────┐  │  │ [IFAK ×2      0.3kg] ││  │   MODE:                   ││
│  │ SECONDARY  ▼│  │  │ [Splint ×1    0.1kg]   ││  │   ● The Raid              ││
│  │ [Glock 17] │  │  │ ───────────────────────││  │   ○ Blitz                 ││
│  └─────────────┘  │  │ [Water Bottle  0.4kg]  ││  │   ○ Scav Run              ││
│  ┌─────────────┐  │  │ [Energy Bar   0.1kg]   ││  │   ○ Ranked Ops            ││
│  │ ARMOR      ▼│  │  │ ───────────────────────││  │   ○ Co-op (Blackout)      ││
│  │ [Plate Car.]│  │  │   WEIGHT: 12.4 / 25kg ││  │                           ││
│  └─────────────┘  │  │  [████████░░░░░░]  Tier 1 ││  ├───────────────────────────┤│
│  ┌─────────────┐  │  │  DRAG TO EQUIP:         ││  │   SQUAD                   ││
│  │ HELMET     ▼│  │  │  Slots: [Primary]       ││  │   ┌─── Slot 1: YOU ──────┐││
│  │ [M/65 Helm.]│  │  │         [Secondary]     ││  │   │ [Mamba]  12.4kg   │││
│  └─────────────┘  │  │         [Armor]         ││  │   └──────────────────────┘││
│                   │  │         [Helmet]        ││  │   ┌─── Slot 2: Kai_V ────┐││
│  ┌─────────────┐  │  │         [Backpack]      ││  │   │ [Hawk]   8.1kg    │││
│  │ BACKPACK   ▼│  │  │         [Pocket ×5]     ││  │   └──────────────────────┘││
│  │ [Std. Pack] │  │  └────────────────────────┘│  │   ┌─── Slot 3: [+ Invite]─┐││
│  └─────────────┘  │                             │  │   └──────────────────────┘││
│                   │  ┌────────────────────────┐ │  ├───────────────────────────┤│
│   LOADOUT       │  │  QUICK STASH SEARCH     │ │  │   ACTIVE QUESTS (2)       ││
│  Value: $24,500   │  │  [ Search items...]   │ │  │    Retrieve Circuit Bd.  ││
│  Weight: 12.4 kg  │  └────────────────────────┘ │  │    Kill 5 Scavengers     ││
│  Tier: 1 (Light)  │                             │  │   → [Show Relevant Gear]   ││
│                   │                             │  └───────────────────────────┘│
├───────────────────┴───────────────────────────┴───────────────────────────────┤
│ LOADOUT PRESETS: [Budget▼] [Standard▼] [Full Kit▼] [+ Save Current] [Import]  │
│ INSURANCE: [Insure All Equipped — Viktor $2,250] [Per-Item] [Review Queue]     │
│                                       Missing: Backpack (empty slot)          │
│                          ┌─────────────────────────────┐                       │
│                          │  ◉  DEPLOY TO RAID          │                       │
│                          └─────────────────────────────┘                       │
└────────────────────────────────────────────────────────────────────────────────┘
```

#### Column Roles

| Column          | Primary Role                                      | Secondary Role                 |
| --------------- | ------------------------------------------------- | ------------------------------ |
| **Left**        | Operator 3D preview + equipped gear slots         | See value-at-risk, weight tier |
| **Center**      | Stash quick-access — drag items to equip          | Weight bar, slot highlight     |
| **Right**       | Map & mode selection, Squad status, Active quests | Deploy CTA                     |
| **Bottom rail** | Loadout presets + Insurance + Deploy button       | Global actions always visible  |

***

### 3. Mobile Layout

On mobile, the loadout prep screen uses a **4-tab layout** with a persistent bottom DEPLOY bar.

```
┌─────────────────────────────────────┐
│  PREP — AETHELGARD INDUSTRIAL  ←    │
├─────────────────────────────────────┤
│                                     │
│  [  GEAR  ] [STASH] [MAP ] [SQUAD]  │  ← Tab bar
│                                     │
│  ━━━━━━━━ GEAR TAB (active) ━━━━━━━ │
│                                     │
│  [Operator 3D — compact, 30% height]│
│  Mamba   Wt: 12.4kg   Val: $24,500  │
│                                     │
│  PRIMARY    [M4A1 ────────────── ▼] │
│  SECONDARY  [Glock 17 ──────── ▼]   │
│  ARMOR      [Plate Carrier ──── ▼]  │
│  HELMET     [M/65 Helmet ───── ▼]   │
│  BACKPACK   [Standard Pack ─── ▼]   │
│  POCKET ×5  [IFAK] [Splint] [+] …   │
│                                     │
│   Weight: [████████░░] 12.4/25 kg  │
│  Tier 1 (Light) — Full sprint       │
│                                     │
├─────────────────────────────────────┤
│  [ Insure All: $2,250]            │
│  ┌─────────────────────────────────┐│
│  │  ◉  DEPLOY                      ││  ← Always visible, thumb zone
│  └─────────────────────────────────┘│
└─────────────────────────────────────┘
```

#### Mobile Tab Descriptions

| Tab       | Content                                                                       |
| --------- | ----------------------------------------------------------------------------- |
| **GEAR**  | Operator preview + all gear slots; tap any slot to open filtered stash picker |
| **STASH** | Full stash grid — tap item → draggable into gear slot; search and filter      |
| **MAP**   | Map card swipe; mode pills; weather badge; current loot bias                  |
| **SQUAD** | Party status; invite; each member's operator + weight + ready toggle          |

**Persistent bottom bar (all tabs):** Insurance shortcut + Deploy button. Weight bar moves to tiny indicator in the tab header when scrolled past.

***

### 4. Operator & Gear Preview Viewport

The left column (PC) or top section (Mobile) renders the **operator in real-time wearing their current equipped loadout**. This is critical for player confidence — "I can see exactly what I'm bringing."

#### Visual Fidelity Rules

| Equipped Item         | How It Renders on Operator                                |
| --------------------- | --------------------------------------------------------- |
| Primary weapon        | Visible slung on back OR held in hands (togglable)        |
| Secondary weapon      | Small holster on thigh                                    |
| Backpack              | Visible on back (size/shape varies by pack tier)          |
| Plate Carrier / Vest  | Over torso — visible vest model with pouch geometry       |
| Helmet                | On head — correct model per helmet type                   |
| No helmet             | Operator's bare head                                      |
| Attachments on weapon | Suppressor, scope, grip visually attached to weapon model |

#### Viewport Interaction

| Action                               | Result                                                  |
| ------------------------------------ | ------------------------------------------------------- |
| Hover/tap equipment slot             | That item on the 3D model highlights with a subtle glow |
| Click/tap the weapon in the viewport | Opens weapon detail → attachment editor (quick access)  |
| Hover/tap operator's body            | Shows armor zone coverage diagram as overlay            |
| Scroll wheel over viewport           | Slight zoom in/out (inspect detail)                     |
| Right-click viewport (PC)            | "Change Operator" quick-switch                          |
| Long press viewport (Mobile)         | Inspect mode — 360° rotate loadout-equipped operator    |

#### Loadout Value & Weight Summary (always visible under preview)

```
┌────────────────────────────────────┐
│   LOADOUT AT RISK                │
│  Total Value:     $24,500          │
│  Insured Value:   $18,000         │
│  Uninsured Value: $6,500          │
│  Net Loss if KIA: ~$6,500          │
│                                    │
│   Weight:   12.4 kg              │
│  → TIER 1 (Light) — Full sprint   │
│  → Capacity remaining: 12.6 kg    │
└────────────────────────────────────┘
```

***

### 5. Saved Loadout Preset System

Players can save named loadout configurations for rapid re-gearing after a death or between raid types.

#### Preset Slots

| Slot Count | Unlock Condition                  |
| ---------- | --------------------------------- |
| 5 presets  | Account Level 1 (default)         |
| 8 presets  | Account Level 20                  |
| 10 presets | Account Level 40 OR Stash Level 2 |

#### Default Preset Templates (first launch)

| Preset           | Contents                                                                                      | Est. Cost |
| ---------------- | --------------------------------------------------------------------------------------------- | --------- |
| **Budget Run**   | M4A1 (no mods), Class 2 Vest, no helmet, IFAK ×1, budget ammo                                 | \~$5,000  |
| **Standard Kit** | M4A1 (red dot, comp), Plate Carrier, M/65 Helmet, IFAK ×2                                     | \~$18,000 |
| **Full Kit**     | HK416 (suppressed, ACOG, heavy barrel), Class 4 Plate, Lvl 3 Helmet, full medkit, 3 mags each | \~$45,000 |

#### Custom Preset Behavior

**Saving:**

1. Equip desired loadout manually
2. Click "Save Current" → Name dialog appears
3. Preset saved — name + thumbnail of operator + weight + value recorded

**Loading a Preset:**

1. Click preset name
2. System checks stash for all items
3. Items found → auto-equipped instantly (0.5s animation)
4. Items missing → show **Missing Items dialog**:

```
┌────────────────────────────────────────────┐
│   PRESET "FULL KIT" — ITEMS MISSING      │
│  ──────────────────────────────────────── │
│   HK416 ............... Found in stash   │
│   Plate Carrier ........ Found in stash   │
│   ACOG Scope ........... NOT in stash    │
│     → Nearest replacement: Red Dot Sight   │
│     → Buy from Viktor: $3,500             │
│   Class 4 Plate ....... NOT in stash     │
│     → Nearest replacement: Class 3 Plate   │
│                                            │
│  [ Use Replacements ]  [ Buy Missing ]     │
│  [ Load What's Available ]   [ Cancel ]    │
└────────────────────────────────────────────┘
```

**Preset icons and metadata displayed on button:**

* Operator name + class icon
* Total weight tier (color coded:  Light /  Moderate /  Heavy)
* Estimated value
* Insurance status of preset ( if all items insured in queue)
* "Last used: 3 raids ago"

***

### 6. Quick Stash Access Panel (Center Column)

The center panel shows a **filtered, prioritized view** of the player's full stash without leaving the loadout screen. This eliminates the Tarkov problem of switching between stash view and loadout view.

#### Stash Panel Features

| Feature                 | Detail                                                   |
| ----------------------- | -------------------------------------------------------- |
| **Category tabs**       | Weapons, Armor, Medical, Ammo, Consumables, Quest Items  |
| **Sorting**             | By: Weight / Value / Value-per-slot / Recently Used      |
| **Smart highlight**     | Items needed by active quests glow with quest-icon badge |
| **Weight preview**      | Hovering any item shows: "Adding this: +1.2 kg → Tier 2" |
| **Condition indicator** |  100% /  50-99% /  <50% durability                 |
| **Quick search**        | Type item name, filters instantly                        |
| **Recently used**       | Top 10 items from last 3 raids shown first               |

#### Equip Flow (Drag & Drop and Tap-to-Equip)

**PC — Drag and Drop:**

1. Drag item from center panel → drop onto gear slot in left column
2. System checks compatibility
3. If compatible: previous item returns to stash, new item equipped (0.2s swap animation)
4. If incompatible (e.g., wrong caliber mag on a different weapon): red X flash + tooltip why

**Mobile — Tap to Equip:**

1. Tap item in STASH tab
2. Compatible slots highlighted
3. Tap destination slot
4. Swap confirmed

#### Weight Budget Bar

Always visible at the bottom of center column:

```
 Current: 12.4 kg / 25 kg max
[████████░░░░░░░░░░░░] Tier 1 — Light
                    ↑              ↑
                  15kg           25kg
             Tier 1→2          Tier 2→3
```

Tier thresholds show clearly as tick marks. When player drags an item that would push them to a new tier, the bar animates to show the projected new tier in orange before the equip is confirmed.

***

### 7. Insurance Screen

Insurance is integrated directly into the bottom rail — no separate screen required.

#### Insurance Design Principles

* **Default: OFF** — Insurance is opt-in. First-time players get a tutorial prompt on their second raid.
* **Visual:** Insured items display a small ** shield icon** in the gear slot. Uninsured items show no icon.
* **Scope:** Individual items OR gear slot batch-insure OR full loadout insure.
* **Items that CANNOT be insured:** Secure container, quest items (FIR), ammo, consumables (food/medical/water), keys.

#### Two Insurers

| Insurer                    | NPC           | Cost              | Return Time | Return Hold       | Best For                        |
| -------------------------- | ------------- | ----------------- | ----------- | ----------------- | ------------------------------- |
| **Viktor** (Salvage Corps) | Viktor Kozlov | 15% of item value | 12–16 hours | Items held 4 days | Active players, high-value kit  |
| **Ada** (Tech Syndicate)   | Ada Chen      | 8% of item value  | 36–48 hours | Items held 2 days | Budget players, infrequent play |

> **Design note:** Items are returned ONLY if not looted by another player. If you die and someone takes your gear, insurance does not pay out. Incentivizes loot denial tactics (hiding gear in obscure spots).

#### Insurance UI (Bottom Rail)

```
┌────────────────────────────────────────────────────────────────────┐
│  INSURANCE                                                          │
│                                                                     │
│  Insurer: [Viktor ▼]  Cost: $3,675 (15% of equipped value $24,500) │
│                                                                     │
│  [ Insure ALL Equipped — $3,675]   [Per-Item]   [Review Queue]   │
│                                                                     │
│  Current Queue: M4A1 (insured) · Plate Carrier (insured)           │
│  → Returning in ~4h (Viktor)                                        │
└────────────────────────────────────────────────────────────────────┘
```

**Per-Item Insurance Panel** (expanded on click):

| Slot      | Item          | Value       | Insure? | Cost       |
| --------- | ------------- | ----------- | ------- | ---------- |
| Primary   | M4A1 (modded) | $12,000     |  ON   | $1,800     |
| Armor     | Plate Carrier | $8,000      |  ON   | $1,200     |
| Helmet    | M/65 Helmet   | $2,500      | ⬜ OFF   | —          |
| Backpack  | Standard Pack | $2,000      |  ON   | $300       |
| **Total** | —             | **$24,500** | —       | **$3,300** |

**Insurance Queue Preview:**

* "3 items returning from Viktor in \~4 hours"
* Click "Review Queue" → opens full insurance inbox overlay showing all pending returns

***

### 8. Map & Mode Selection Panel

Located in the Right Column top section (PC) or the MAP tab (Mobile).

#### Map Cards

Each available map is rendered as a **card** with:

| Element            | Content                                                 |
| ------------------ | ------------------------------------------------------- |
| **Map thumbnail**  | Top-down aerial screenshot of map                       |
| **Map name**       | Bold — e.g., "Aethelgard Industrial Zone"               |
| **Weather badge**  |  Overcast /  Clear /  Rain /  Fog /  Snow        |
| **Risk indicator** |  (based on average player count and loot density)  |
| **Loot bias**      | e.g., "Weapons-heavy" / "Medical-heavy" / "Balanced"    |
| **Player count**   | "8–16 players"                                          |
| **Featured badge** | Orange "FEATURED" ribbon if selected for daily rotation |

**Card navigation:** Left/right arrows (PC) or swipe (Mobile). Max visible: 2 cards at once. Total planned maps at launch: 3.

#### Mode Pills

Below the map card, a row of mode pills:

```
[● The Raid ]  [ Blitz ]  [ Scav Run ]  [ Ranked  ]  [ Co-op ]
```

**Selected mode** shows:

* Duration range
* Player/squad count constraints
* Risk badge
* Any special rule tooltips (hover/tap)

#### Queue Size Selector

```
SQUAD SIZE:  ○ Solo    ○ Duo    ● Trio
Auto-fill:   [ ] Match me with available players if squad incomplete
Est. Queue:  ~40 seconds
```

***

### 9. Squad Team Ready Screen

The bottom of the Right Column (PC) or the SQUAD tab (Mobile) shows real-time squad status.

#### Squad Slot Design

Each squad slot displays:

```
┌────────────────────────────────────────────────────────┐
│  Slot 1: YOU (Leader)                                   │
│  [Mamba — Assault]   Wt: 12.4 kg  Light    Insured │
│  ● READY                                                │
└────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────┐
│  Slot 2: Kai_Virtanen                                   │
│  [Hawk — Scout]      Wt: 8.1 kg   Light    Insured │
│  ● READY                                                │
└────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────┐
│  Slot 3: [EMPTY]                        [+ Invite]     │
│          or if LFG enabled: [Searching for 1 player…]  │
└────────────────────────────────────────────────────────┘
```

#### Per-Slot Information

| Field                   | Purpose                                                   |
| ----------------------- | --------------------------------------------------------- |
| **Operator + class**    | Team synergy visibility at a glance                       |
| **Weight tier (color)** |  Light /  Moderate /  Heavy — mobility coordination |
| **Insurance status**    |  Insured /  Uninsured — communicates risk tolerance    |
| **Ready / Not Ready**   | Prevents accidental early deploy                          |
| **\[ Invite]** button  | Sends invite directly to friend in friend list            |

#### Squad Leader Controls

| Action                   | Method                                                                                                |
| ------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Deploy (force start)** | Leader can deploy when all slots are READY; OR override with 10s countdown if one member is not ready |
| **Kick member**          | Long press/right-click on slot → "Remove from squad"                                                  |
| **Transfer leadership**  | Long press → "Make Leader"                                                                            |
| **Lock squad**           | Toggle to prevent LFG auto-fill adds                                                                  |
| **Change map/mode**      | Only squad leader can change these; changes sync to all members                                       |

#### Ready Sync Behavior

When all members are Ready:

* Deploy button **pulses green**
* Audio: subtle 3-note sting
* "All Ready — Deploying in 5s…" countdown appears (cancellable)

When a member is not ready:

* Deploy button is grey with tooltip: "Waiting for \[Name]"
* Auto-deploy never triggers

***

### 10. Anti-Friction & Quality-of-Life Features

| Feature                          | Detail                                                                                                                                              |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **"Same as Last Raid" shortcut** | One-click to re-equip the exact loadout from previous raid (if items still in stash). Shown prominently after a death.                              |
| **Missing gear warning**         | If a gear slot is empty, yellow  badge on that slot + warning in bottom rail: " No armor equipped"                                                |
| **Low balance warning**          | If credit balance < loadout value + insurance cost, orange banner: " Low funds — you may not afford this loadout"                                  |
| **Weight tier alert**            | If loadout crosses into Tier 3 (Heavy), popup: "You will be unable to sprint. Consider removing low-value items."                                   |
| **Quest item reminder**          | If a quest requires a specific item to be brought into raid, yellow quest badge appears on relevant stash slot. "Required for: Viktor Quest 3"      |
| **Quick repair**                 | If a weapon or armor is at <50% durability, red  on that slot + "Repair at Safe House Workbench — $500" tooltip                                    |
| **Insure All shortcut**          | Single-click bottom rail button insures all currently equipped insurable items with selected insurer                                                |
| **Deploy confirmation**          | If uninsured value > $10,000, a confirmation dialog appears: "You have $12,000 in uninsured gear. Deploy anyway?" — prevents accidental costly runs |
| **Auto-calculate insurance**     | Insurance total updates in real-time as items are swapped                                                                                           |
| **Offline stash editing**        | All stash changes are saved immediately — if player closes app before deploying, all loadout changes persist                                        |

***

### 11. Matchmaking Transition Screen

After pressing DEPLOY, the matchmaking waiting screen plays:

#### Visual State

```
┌────────────────────────────────────────────────────────────────┐
│                                                                 │
│       DEPLOYING TO:  AETHELGARD INDUSTRIAL ZONE               │
│       MODE:          THE RAID (TRIO)                           │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │              [3D MAP ROTATING SLOWLY]                   │  │
│   │     Top-down map view spins gently at ~5 rpm            │  │
│   │     Zone highlights pulse — shows loot density         │  │
│   │     Extraction points marked with green helicopter      │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│   WEATHER TODAY:  Overcast — Reduced visibility +10m          │
│   LOOT NOTES: Medical supplies +20% spawn (Industrial event)   │
│                                                                 │
│   PLAYERS FOUND: [●●●●●●●●●●●●●●○○] 14/16                    │
│   QUEUE TIME: 0:32                     Est. start: ~0:15       │
│                                                                 │
│   ─────────────────────────────────────────────────────────−   │
│    TIP: "AI Scavs patrol in groups. Shoot one, alert all."  │
│             [ ◀ Previous  |  Next ▶ ]                          │
│                                                                 │
│   SQUAD:  ● Kai_Virtanen [Ready]   ● Dxt_Raptor [Ready]       │
│                                                                 │
│                          [ CANCEL ]                            │
└────────────────────────────────────────────────────────────────┘
```

#### Loading Tip Rotation (L4\_LobbyToMatch)

During the \[6] Loading Screen phase (L4\_LobbyToMatch per [Loading Screen Design](../UI_UX/LoadingScreen_Design.md)), tips rotate every 8s. Players can manually page through them. Categories:

| Category              | Content                                                                             |
| --------------------- | ----------------------------------------------------------------------------------- |
| **Tactical**          | Combat, cover, flanking                                                             |
| **Economy**           | Insurance, what to sell, trader rep                                                 |
| **Exploration**       | Loot zones, map callouts, extraction routes                                         |
| **Operator-specific** | One tip per operator about the currently selected operator's ability                |
| **Fun Fact / Lore**   | Per [Lore Delivery](../Story/Lore_Delivery.md) — lore fragments, faction philosophy |

#### Match Found Transition

When match fills:

* "PLAYERS FOUND: 16/16" → all dots turn green
* 3-second countdown with audio: three tones
* Screen dims → fast fade to black
* Match begins — Player spawns at edge of map

***

### 12. First-Raid Onboarding State

For new players opening the loadout screen for the first time after the tutorial:

| Element                | Behavior                                                                                                         |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Starter kit displayed  | M4A1, Class 2 Vest, IFAK ×2 — pre-equipped from tutorial reward                                                  |
| Guided highlights      | Pulsing arrows on Insurance rail → Map card → Deploy button                                                      |
| First insurance prompt | "Your gear can be returned if you die — insure it? (Viktor: $0 — First insurance FREE)"                          |
| First map pre-selected | Aethelgard Industrial Zone locked as first raid map                                                              |
| Mode locked            | "The Raid" pre-selected; other modes show "Unlock at Account Level 5"                                            |
| First deploy tip       | "Remember: your equipped gear will be LOST if you die without extracting. Your Secure Container is always safe." |
| Tutorial flow          | After reading tip → click Deploy → 2s acknowledgment animation → matchmaking begins                              |

First insurance is **FREE** — Viktor sponsors the first raid insurance to teach the mechanic without penalizing new players. Credit cost displayed as "Viktor's Compliments."

***

### Cross-References

* [Loading Screen Design](../UI_UX/LoadingScreen_Design.md) — L4\_LobbyToMatch layout, content types, async loading flow.
* [Home Screen & Lobby](HomeScreen_Design.md) — Deploy button on Home Screen opens this Loadout Preparation screen.
* [Gear Mechanics](../Gameplay/Gear_Mechanics.md) — Weight tier thresholds (Tier 1/2/3), durability degradation rules.
* [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md) — Attachments visible on operator preview; quick-access attachment editor from viewport click.
* [Safe House Design](Safe_House_Design.md) — Repair shortcut links to Workbench; Insurance queue managed via Safe House mail.
* [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — Squad formation, queue parameters, server-side match assembly.
* [GameModes](GameModes.md) — Mode rules referenced in mode pill descriptions.
* [Economy](Economy.md) — Insurance costs calculated as % of item credit value; Viktor/Ada as economy NPCs.
* [Quest & Objective System](../Gameplay/Quest_Objective_System.md) — Active quest items highlighted in stash; quest reminder badges on gear slots.
* [Loot Table Design](../Gameplay/Loot_Table_Design.md) — Map loot bias indicators sourced from zone loot tables.
* [TutorialRaid](TutorialRaid.md) — First-launch loadout screen state aligns with post-tutorial onboarding flow.
