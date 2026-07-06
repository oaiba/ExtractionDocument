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
| PC/console layout | Full-screen or large overlay with map, legend, extracts, objectives, squad |
| Mobile layout | Full-screen map with bottom sheet for legend/objectives |
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
| Entry points | Inventory key/button, mobile gesture, loot context |
| Layout | Equipment, backpack, secure container, quick slots, weight |
| Primary CTA | Use / Equip / Move based on selected item |
| Restrictions | Some stash-only actions are disabled in raid with explanation |

### Mid-Raid Item Rules

| Action | In-Raid UI Rule |
| :--- | :--- |
| Use medical item | Show duration, movement constraints, cancel rule |
| Move to secure container | Confirm if replacing protected item |
| Drop item | Confirm for insured, quest, rare, or high-value items |
| Split stack | Available only when screen space permits; mobile uses stepper sheet |
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
| Close overlay | ESC | B / Circle | Close button / system back |
| Ping | Middle mouse / ping key | D-pad / bumper | Ping button / long press map |
| Pause | ESC | Start/Menu | Pause button |

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
