---
title: "In-Raid Screens"
type: docs
weight: 5
---

## Purpose

In-raid screens must help the player survive under pressure. They should preserve visibility, communicate risk immediately, and avoid opening full-screen interfaces unless the player intentionally accepts that danger.

Primary references:

| System | Source |
| :--- | :--- |
| HUD | [In-Raid HUD Design](HUD_Design.md) |
| Notifications | [Notification & Feedback Systems](Notification_Systems.md) |
| Navigation map | [Navigation & Map System Design](../GameDesign/NavigationAndMap.md) |
| Looting | [Looting & Inventory Interactions](../Gameplay/Looting_Interactions.md) |
| Extraction | [Extraction Mechanics](../Gameplay/Extraction_Mechanics.md) |
| Downstate | [Downstate & Revive System](../Gameplay/Downstate_Revive.md) |

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |
| [HUD Design](HUD_Design.md) | HUD element placement, visibility, and performance rules |
| [Notification Systems](Notification_Systems.md) | Combat feedback, toasts, danger communication |
| [Post-Raid Screens](Post_Raid_Screens.md) | AAR, replay, loot transfer, redeploy after raid |

---

## Screen Inventory

| Surface | Goal | Primary Action | Critical States |
| :--- | :--- | :--- | :--- |
| HUD | Show survival, combat, squad, objective, and extraction status | Contextual gameplay | low health, combat, looting, extraction |
| Tactical Map | Plan route, extracts, pings, objectives | Set ping / close map | jammed, partial intel, danger nearby |
| Looting Overlay | Transfer items quickly while exposed | Take / close | container locked, overweight, interrupted |
| Inventory Overlay | Use, move, discard, or secure items mid-raid | Use / move / close | combat nearby, overweight, invalid slot |
| Interaction Prompts | Explain context actions | Press / hold action | blocked, locked, timed, interrupted |
| Pause Overlay | Settings and abandon while raid continues | Resume | damage auto-dismiss, abandon confirm |
| Spectator View | Watch teammates after death | Cycle teammate | anti-ghosting limits, all squad dead |
| Reconnect Overlay | Restore raid session | Reconnect / cancel | timeout, version mismatch, gear loss warning |

---

## HUD

The detailed element catalog lives in [HUD Design](HUD_Design.md). This page defines how HUD participates in the broader in-raid screen group.

| State | HUD Behavior |
| :--- | :--- |
| Exploration | Minimal opacity for non-critical combat widgets |
| Combat | Health, ammo, squad, minimap, compass, hit feedback at full priority |
| Looting | Container UI takes focus; minimap/squad shrink or dim but remain visible |
| Healing | Health and progress are emphasized; non-critical widgets dim |
| Extraction | Extraction timer/progress dominates; threats remain visible |
| Downed | Revive state, bleedout timer, squad pings, and limited camera controls |
| Death | HUD transitions to death/replay flow |

### HUD Acceptance

- [ ] Critical state changes are readable in under 0.5 seconds.
- [ ] HUD never hides extraction, health, ammo, or squad-critical alerts.
- [ ] Mobile combat controls do not cover critical interaction prompts.
- [ ] Custom HUD settings cannot move critical widgets outside safe zones.

---

## Tactical Map

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| TACTICAL MAP                                      [Close: M/ESC] |
|------------------------------------------------------------------|
| LEGEND     |                  MAP AREA                 | DETAILS |
| You        | +--------------------------------------+  | Extract |
| Squad      | |        Sector 7 known terrain        |  | Open    |
| Quest      | |   P1 -> route ping                   |  | 30 sec  |
| Extract    | |        [Quest Zone]       [Exit]     |  | Risk Med|
| Danger     | +--------------------------------------+  |         |
|------------------------------------------------------------------|
| [Set Ping] [Track Quest] [Filter Markers] Audio remains live     |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Help players plan movement without giving unfair enemy information |
| Entry points | `M`, controller map button, minimap click/tap, quest deep link |
| Exit points | Back, close map, ping commit, damage auto-close if configured |
| Layout | PC/Console landscape standard: full-screen or large overlay with map, legend, extracts, objectives, squad |
| Primary CTA | Set Ping / Track Objective |
| Secondary actions | Filter markers, zoom, recenter, inspect extract |

### Tactical Map States

| State | Behavior |
| :--- | :--- |
| Normal | Shows known terrain, squad, active objective, extracts |
| Jammed / no signal | Hide live elements and explain source if known |
| Partial intel | Unknown extracts or areas use fog/unknown labels |
| Danger nearby | Keep audio live and show warning edge treatment |
| Quest focus | Highlight relevant area without revealing exact hidden objective if design forbids it |

---

## Looting Overlay

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| blurred live gameplay - threats and audio still visible     [X]  |
|------------------------------------------------------------------|
| CONTAINER: Dead PMC              | YOUR BACKPACK                 |
| +-----------------------------+  | +----------------------------+|
| | AK-74M Rifle        [Take]  |  | | Medkit       Ammo         | |
| | IFAK Medkit         [Take]  |  | | Empty slot   Quest key    | |
| | Lab Key             [Take]  |  | +---------------------------+ |
| | Credits 15,000      [Take]  |  | Weight: 32 / 40kg             |
| +-----------------------------+  | Move speed: -25%              |
|------------------------------------------------------------------|
| [Hold Take All] [Compare] [Close]       Warning: exposed         |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Let players choose loot quickly while understanding exposure and weight |
| Visual model | Partial overlay; game remains visible and audible |
| Primary CTA | Take selected / Take all if allowed |
| Secondary actions | Inspect, compare, quick equip, mark, close |
| Destructive actions | Discard or swap valuable item requires confirmation if safe to do so |

### Looting States

| State | Behavior |
| :--- | :--- |
| Searching | Timed progress with cancel on movement/damage rules |
| Open container | Container list/grid and backpack summary |
| Overweight | Show movement penalty and block if above hard limit |
| Interrupted | Close or pause transfer, show reason |
| Locked | Show required key/tool and whether player owns it |
| Empty | Compact empty message; quick close remains focused |

---

## Inventory Overlay

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| IN-RAID INVENTORY                                  Audio live [X]|
|------------------------------------------------------------------|
| EQUIPPED             | BACKPACK GRID              | QUICK SLOTS  |
| Primary AK-74M       | +--+--+--+--+--+--+        | 1 Bandage    |
| Armor Lv3            | |Med|Ammo |Key|  |        | 2 Painkiller  |
| Rig 12 slots         | +--+--+--+--+--+--+        | 3 Grenade    |
| Secure 4 slots       | Weight 34 / 40kg           | 4 Empty      |
|------------------------------------------------------------------|
| [Use] [Move Secure] [Drop] [Split]  Combat nearby: [!]           |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Support survival item use and limited item management without turning raid into stash management |
| Entry points | Inventory key/button, loot context |
| Layout | Equipment, backpack, secure container, quick slots, weight |
| Primary CTA | Use / Equip / Move based on selected item |
| Restrictions | Some stash-only actions are disabled in raid with explanation |

### Mid-Raid Item Rules

| Action | In-Raid UI Rule |
| :--- | :--- |
| Use medical item | Show duration, movement constraints, cancel rule |
| Move to secure container | Confirm if replacing protected item |
| Drop item | Confirm for insured, quest, rare, or high-value items |
| Split stack | Available only when screen space permits; otherwise keep the action disabled with an explanation |
| Repair/mod weapon | Disabled unless specific field action is supported |

---

## Pause Overlay

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| frosted live raid view - game does not pause                     |
|------------------------------------------------------------------|
| PAUSE MENU             | RAID STATUS              | SQUAD        |
| > Resume              | Timer 25:43              | Kai 85 HP     |
|   Settings            | Extracts: Crossroads OK  | P2 42 HP [!]  |
|   Statistics          | Ping 38ms Loss 0%        | P3 Dead       |
|   Report Issue        | Raid ID: S7-284712       |               |
|   Abandon Raid [!]    |                          |               |
|------------------------------------------------------------------|
| Taking damage auto-dismisses overlay. Audio remains unmuted.     |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Allow settings and exit decisions while preserving online raid danger |
| Background | Frosted/dim overlay; game world motion and audio remain perceptible |
| Primary CTA | Resume |
| Secondary actions | Settings, controls, report issue, squad, network info |
| Destructive action | Abandon Raid requires hold confirm and clear gear-loss message |

### Safeguards

| Safeguard | Rule |
| :--- | :--- |
| Damage received | Auto-dismiss or flash warning depending tuning |
| Audio | Never mute gameplay audio by default |
| Cursor/camera | Cursor unlocked; camera input paused |
| Tab switching | Inventory/map inputs switch directly to those overlays |

---

## Spectator View

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| SPECTATING: Player2                         Delay 5s      [AAR]  |
|------------------------------------------------------------------|
|                                                                  |
|                  [TEAMMATE CAMERA VIEW ONLY]                     |
|                                                                  |
|------------------------------------------------------------------|
| Teammates: [Player2] [Player3]      Pings limited: 1 / 10s       |
| [Cycle Teammate] [Ping] [Mute] [Report]                          |
+------------------------------------------------------------------+
```

| Spec | Requirement |
| :--- | :--- |
| Goal | Keep eliminated squad players engaged without enabling unfair ghosting |
| View | Teammates only; no enemy freecam |
| Primary CTA | Cycle Teammate |
| Secondary actions | Ping if allowed, report, mute, open AAR after squad end |
| Restrictions | Delay, limited map intel, no enemy health/inventory |

---

## Reconnect Overlay

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         RECONNECTING TO RAID                     |
|------------------------------------------------------------------|
| Last raid: Sector 7 / Night                                      |
| Attempt: 2 / 5                         Timeout: 00:38            |
| [==================--------------]                               |
| Re-establishing session and player state...                      |
|                                                                  |
| Cancel may mark the raid MIA and gear may be lost.               |
|------------------------------------------------------------------|
| [Cancel]                                      [Retry Now]        |
+------------------------------------------------------------------+
```

| State | Behavior |
| :--- | :--- |
| Reconnecting | Spinner, attempt count, timeout, last known raid |
| Reconnected | Fade back to raid and restore HUD state |
| Timeout | Explain MIA/gear consequence and route to Home |
| Version mismatch | Require update; show no retry until version matches |
| Cancel | Confirm that cancel may abandon raid and lose gear |

---

## Input Mapping

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Open map | M / minimap click | Map/View button | Tap minimap |
| Open inventory | Tab / I | Menu combo or D-pad shortcut | Swipe/top button |
| Loot | F / click | A / Cross | Tap / hold |
| Close overlay | ESC | B / Circle | Close button |
| Ping | Middle mouse / ping key | D-pad / bumper | Ping button / long press map |
| Pause | ESC | Start/Menu | Pause button |

---

## Designer-Ready Screen Specs

In-raid specs must preserve threat awareness. Every overlay below must keep audio readable, close immediately, and avoid hiding survival-critical state unless the design explicitly accepts that risk.

### HUD Reference

**Player Intent**

Read survival-critical information while moving, fighting, looting, and extracting without opening a blocking menu.

**Expanded ASCII Wireframe**

```
+---------------------------------------------------------------------------------+
| Squad / Health                         Compass                         Timer    |
|                                                                                 |
|                                                                                 |
|                         GAMEPLAY SPACE / TOP-DOWN RAID                          |
|                                                                                 |
| Prompt: Hold F Search                                      Minimap / Extracts   |
| Status effects                                  Ammo / Weapon / Weight / Ability|
+---------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Top band | squad, compass, raid timer only |
| Center | kept mostly clear for combat readability |
| Bottom band | prompts, status effects, ammo, ability, weight |
| Corners | reserve for persistent but non-blocking HUD clusters |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Lethal status | health, armor break, bleed, extraction timer |
| 2 | Action readiness | ammo, ability, interaction prompt |
| 3 | Navigation | compass, minimap, extraction hint |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| HUD cluster | Stable position and no layout jump when values change |
| Warning state | Text or symbol plus color; never color alone |
| Prompt | Names input, action, hold/tap requirement, and risk if noisy |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Combat | Reduce noncritical hints; keep health/ammo visible |
| Low health | Promote medical/status indicators |
| Extract active | Timer and extraction state become top priority |
| HUD disabled/custom | Critical warnings still appear |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Use prompt | F / hold | A / Cross | Tap/hold prompt |
| Ping | Middle mouse | D-pad / bumper | Long press |
| Open map | M | View button | Tap minimap |

**Designer Notes**

- HUD is not a decorative frame; keep the playfield dominant.
- Any hidden HUD option must preserve death-prevention alerts.

**Acceptance Checklist**

- [ ] Critical state remains readable during combat.
- [ ] HUD clusters do not cover the operator or immediate threat zone.

### Tactical Map

**Player Intent**

Orient, plan route, inspect extracts, view squad pings, and check quest landmarks without gaining unfair enemy tracking.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| TACTICAL MAP                                             [Pins] [Close]        |
|--------------------------------------------------------------------------------|
| MAP CANVAS: fog, landmarks, extracts, pings, quest zones                       |
|                                                                                |
|                                                                                |
|--------------------------------------------------------------------------------|
| LEGEND / FILTERS                 | DETAIL: Extract Crossroads                  |
| [Extracts] [Quests] [Pings]      | Rule: open 10m after flare                  |
| Exposure: Raid continues         | Distance 210m | Risk: exposed road          |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Map canvas | largest area; shows terrain, extracts, pings, quest zones |
| Filters/legend | text labels for all symbols |
| Detail panel | selected marker rule, distance, risk, availability |
| Exposure notice | persistent reminder that raid continues |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Player/squad position and extracts | Always visible |
| 2 | Selected marker detail | Must explain rule and risk |
| 3 | Filters | Secondary and compact |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Extract marker | name, availability, rule, distance |
| Ping marker | owner, age, type, decay |
| Quest marker | objective, status, requirement |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| No map intel | Show partial map and explain missing intel |
| Enemy nearby | Do not reveal enemy unless system rules allow |
| Jammed/EMP | Show degraded map reason |
| Online raid | Never hard-pauses gameplay |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Pan/zoom | Drag/wheel | Sticks/triggers | Pinch/drag |
| Place ping | Right-click | A / Cross | Long press |
| Close | M/Esc | B / Circle | Close button |

**Designer Notes**

- Map should feel like an exposed tactical tool, not a safe menu.
- All icons need legend labels.

**Acceptance Checklist**

- [ ] Extract rules are readable.
- [ ] Raid exposure is visible while map is open.

### Looting Overlay

**Player Intent**

Search, compare, and transfer loot fast while understanding noise, exposure, weight, and inventory capacity.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| LOOTING: Weapon Crate                                 Exposure: HIGH [Close]   |
|--------------------------------------------------------------------------------|
| CONTAINER ITEMS                  | PLAYER QUICK INVENTORY                      |
| [Rifle 4x2] [Ammo x60] [Key FIR] | Rig slots | Backpack grid | Secure slot     |
|--------------------------------------------------------------------------------|
| SELECTED: Keycard | Value 45K | Quest: Lab Rat | Weight +0.1kg                 |
| [Take] [Quick Move] [Inspect] [Leave]                                          |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Container list/grid | item identity, size, rarity/value, FIR/quest state |
| Player inventory | target capacity and valid placement |
| Exposure header | noise/search state and vulnerability warning |
| Selected detail | value, weight, quest/FIR, actions |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Exposure and close action | Always visible |
| 2 | Item value/quest state | Visible before transfer |
| 3 | Capacity/weight | Persistent during movement |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Loot tile | name, footprint, stack, FIR/quest/value badges |
| Transfer preview | valid/invalid target and resulting weight |
| Search progress | truthful timer and noise state |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Searching | Progress, noise, cancel available |
| Container empty | Show empty result and close path |
| Inventory full | Block transfer, show needed cells |
| Under fire | Overlay may auto-minimize or warning intensifies |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Take item | Click/drag | A / Cross | Tap |
| Quick move | Ctrl-click | X / Square | Double tap |
| Close | Esc | B / Circle | Close |

**Designer Notes**

- Do not hide the risk of standing still.
- Quest/FIR labels must be text-readable.

**Acceptance Checklist**

- [ ] Exposure, weight, and capacity are visible while looting.
- [ ] Empty/full/under-fire states are specified.

### Inventory Overlay

**Player Intent**

Rearrange gear mid-raid under pressure without mistaking safe stash behavior for exposed raid behavior.

**Expanded ASCII Wireframe**

```
+---------------------------------------------------------------------------------+
| INVENTORY OVERLAY                              Raid continues | [Close]         |
|---------------------------------------------------------------------------------|
| EQUIPPED GEAR             | BACKPACK / RIG GRID                 | ITEM DETAIL   |
| Weapon / Armor / Rig      | item footprints and valid targets   | Stats, value  |
| Weight 33/40kg            |                                     | Drop warning  |
|---------------------------------------------------------------------------------|
| [Use] [Move] [Split] [Drop] [Discard Confirm]                                   |
+---------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Equipped gear | slots, durability, ammo, status |
| Inventory grid | rig/backpack/secure capacity |
| Detail panel | selected item effect, value, risk |
| Action bar | use, move, split, drop, close |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Raid continues warning | Persistent |
| 2 | Weight and movement penalty | Always visible |
| 3 | Drop/destructive actions | Separated and confirmed |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Item tile | footprint, stack, FIR/quest/protected state |
| Drop action | consequence copy and confirm for protected/high-value items |
| Secure container | visually distinct restrictions |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Overweight | Show movement penalty and remove options |
| Item locked | Disable invalid move/drop with reason |
| Healing/use in progress | Show timer and vulnerability |
| Combat detected | Warning, but player retains control |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop | Grid cursor | Tap item then target |
| Use item | Hotkey/click | A / Cross | Tap action |
| Drop | Context menu | Hold button | Long press + confirm |

**Designer Notes**

- Mid-raid inventory needs faster exits and stronger risk copy than stash.
- Do not reuse stash destructive affordances without raid-specific warning.

**Acceptance Checklist**

- [ ] Raid exposure, weight, and destructive drop warnings are clear.
- [ ] Controller and touch can move items without precision-only input.

### Pause Overlay

**Player Intent**

Access settings, squad/social, abandon, report, or reconnect options while understanding that online raid state is not paused.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| PAUSE OVERLAY                                      Online raid continues       |
|--------------------------------------------------------------------------------|
| [Resume] [Settings] [Controls] [Report] [Support]                              |
|                                                                                |
| Danger notice: audio remains live; character remains vulnerable                |
|--------------------------------------------------------------------------------|
| [Abandon Raid]                                                     [Resume]    |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Action list | resume first, settings/support secondary |
| Danger notice | non-paused state and vulnerability |
| Abandon | separated destructive action |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Resume | Default focus |
| 2 | Online continues notice | Near header |
| 3 | Abandon | Low and separated |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Resume CTA | immediate close |
| Abandon CTA | hold/confirm with gear consequence |
| Settings shortcut | opens safe subset without hiding danger notice |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Offline/local | May pause if mode allows |
| Online | Does not pause; audio continues |
| Downed/dead | Action set changes to spectate/report |
| Abandon confirm | Names MIA/gear consequence |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Resume | Esc / click | Start/B | Resume button |
| Navigate | Mouse/arrows | D-pad | Tap |
| Abandon | Hold confirm | Hold confirm | Hold CTA |

**Designer Notes**

- Default focus must never land on Abandon.
- Keep background readable enough to preserve threat context.

**Acceptance Checklist**

- [ ] Online non-pause consequence is explicit.
- [ ] Abandon requires confirmation.

### Spectator View

**Player Intent**

Watch eligible teammates, understand remaining squad state, and avoid unfair ghosting after death.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| SPECTATING: Player2                              Squad 2 alive | [Report]      |
|--------------------------------------------------------------------------------|
| gameplay view from allowed teammate perspective                                |
|--------------------------------------------------------------------------------|
| [Prev] [Next] Camera: Follow / Free Ally Only | Extract Timer 12:30 | [Leave]  |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Header | spectated player, squad alive, report |
| View | allowed teammate/camera only |
| Controls | previous/next, camera mode, leave |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Spectated identity | Always visible |
| 2 | Anti-ghosting limits | Communicated when camera is restricted |
| 3 | Leave/report actions | Available but secondary |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Player switcher | only eligible teammates |
| Camera mode | labels restrictions |
| Report action | keeps match context |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Teammates alive | Spectate allowed allies |
| All eliminated | Route to post-raid |
| Enemy spectate blocked | Show restriction reason |
| Reconnect teammate | Shows temporary unavailable state |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch target | Q/E | Bumpers | Swipe/tap |
| Change camera | C | Y / Triangle | Camera button |
| Leave | Click | Menu | Leave button |

**Designer Notes**

- Spectator UI must not reveal enemy information unavailable to the squad.
- Keep report reachable without making it primary.

**Acceptance Checklist**

- [ ] Anti-ghosting camera restrictions are explicit.
- [ ] All-eliminated state routes cleanly to post-raid.

### Reconnect Overlay

**Player Intent**

Understand reconnection progress, attempts, timeout, and the consequence of canceling while gear and raid status are at risk.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| RECONNECTING TO RAID                                                           |
|--------------------------------------------------------------------------------|
| Last raid: Sector 7 / Night       Attempt 2/5        Timeout 00:38             |
| [==================--------------] Re-establishing session and player state    |
| Warning: cancel may mark the raid MIA and gear may be lost.                    |
|--------------------------------------------------------------------------------|
| [Cancel]                                                        [Retry Now]    |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | Requirement |
| :--- | :--- |
| Session summary | map, mode/time, last known state |
| Progress | attempt count, timeout, current operation |
| Consequence warning | MIA/gear risk |
| Actions | cancel with confirm, retry if allowed |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Timeout and attempt | Always visible |
| 2 | Gear consequence | Above cancel |
| 3 | Retry status | Secondary |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Progress bar | names real operation |
| Cancel | confirm with consequence |
| Error code | shown on failure for support |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Reconnecting | Spinner/progress, attempt count, timeout |
| Reconnected | Fade back and restore HUD |
| Timeout | Explain MIA/gear result and route home |
| Version mismatch | Require update; retry disabled |
| Cancel | Confirm abandon consequence |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Retry | Click | A / Cross | Retry button |
| Cancel | Click + confirm | B / Circle + confirm | Cancel + confirm |

**Designer Notes**

- Do not make cancel look safe.
- Timeout should be concrete, not vague.

**Acceptance Checklist**

- [ ] Attempts, timeout, and gear consequence are visible.
- [ ] Version mismatch and timeout have clear next steps.

---

## Analytics

| Metric | Use |
| :--- | :--- |
| Death while in overlay | Identify risky UI coverage or auto-dismiss rules |
| Loot transfer time | Tune speed and weight clarity |
| Tactical map open duration | Detect map readability or overuse |
| Abandon raid attempts | Identify frustration or disconnect issues |
| Reconnect success rate | Track network recovery quality |

---

## Acceptance Checklist

- [ ] Game audio remains useful under all in-raid overlays.
- [ ] Overlay close behavior is immediate and consistent.
- [ ] Looting and inventory communicate exposure and weight.
- [ ] Tactical map avoids unfair enemy tracking.
- [ ] Reconnect and abandon flows explain gear consequences.
- [ ] Spectator view has anti-ghosting restrictions.
