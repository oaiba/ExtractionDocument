---
title: "In-Raid màn hình"
type: docs
weight: 5
---

## Mục Đích

In-raid màn hình must giúp the người chơi survive under pressure. They should preserve visibility, communicate risk immediately, và avoid opening full-màn hình interfaces unless the người chơi intentionally accepts that danger.

Tham chiếu chính:

| hệ thống | source |
| :--- | :--- |
| HUD | [In-Raid HUD Design](hud_design/index.html) |
| Notifications | [Notification & Feedback hệ thống](notification_systems/index.html) |
| Navigation map | [Navigation & Map hệ thống Design](../gamedesign/navigationandmap/index.html) |
| Looting | [Looting & Inventory Interactions](../gameplay/looting_interactions/index.html) |
| Extraction | [Extraction cơ chế](../gameplay/extraction_mechanics/index.html) |
| Downstate | [Downstate & Revive hệ thống](../gameplay/downstate_revive/index.html) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Full UI/UX documentation hub |
| [màn hình Groups Overview](screen_groups_overview/index.html) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](global_ux_standards/index.html) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [HUD Design](hud_design/index.html) | HUD element placement, visibility, và performance rules |
| [Notification hệ thống](notification_systems/index.html) | Combat feedback, toasts, danger communication |
| [Post-Raid màn hình](post_raid_screens/index.html) | AAR, replay, loot transfer, redeploy sau raid |

---

## Inventory Màn Hình

| Surface | mục tiêu | hành động chính | Critical trạng thái |
| :--- | :--- | :--- | :--- |
| HUD | Show survival, combat, squad, objective, và extraction status | Contextual gameplay | low máu, combat, looting, extraction |
| Tactical Map | Plan route, extracts, pings, objectives | Set ping / close map | jammed, partial intel, danger nearby |
| Looting Overlay | Transfer items quickly while exposed | Take / close | container locked, overweight, interrupted |
| Inventory Overlay | cách dùng, move, discard, hoặc secure items mid-raid | cách dùng / move / close | combat nearby, overweight, invalid slot |
| Interaction Prompts | Explain context actions | Press / hold action | blocked, locked, timed, interrupted |
| Pause Overlay | Settings và abandon while raid continues | Resume | damage auto-dismiss, abandon confirm |
| Spectator View | Watch teammates sau death | Cycle teammate | anti-ghosting limits, all squad dead |
| Reconnect Overlay | Restore raid session | Reconnect / cancel | timeout, version mismatch, gear loss cảnh báo |

---

## HUD

The chi tiết element catalog lives in [HUD Design](hud_design/index.html). Trang này định nghĩa how HUD participates in the broader in-raid màn hình group.

| trạng thái | HUD Behavior |
| :--- | :--- |
| Exploration | Minimal opacity for non-critical combat widgets |
| Combat | máu, đạn, squad, minimap, compass, hit feedback at full priority |
| Looting | Container UI takes focus; minimap/squad shrink hoặc dim nhưng remain hiển thị rõ |
| Healing | máu và progress are emphasized; non-critical widgets dim |
| Extraction | Extraction timer/progress dominates; threats remain hiển thị rõ |
| Downed | Revive trạng thái, bleedout timer, squad pings, và limited camera controls |
| Death | HUD transitions to death/replay flow |

### HUD Acceptance

- [ ] Critical trạng thái changes are dễ đọc in under 0.5 seconds.
- [ ] HUD never hides extraction, máu, đạn, hoặc squad-critical alerts.
- [ ] Mobile combat controls do not cover critical interaction prompts.
- [ ] Custom HUD settings cannot move critical widgets outside safe zones.

---

## Tactical Map

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | giúp người chơi plan movement mà không giving unfair địch information |
| Entry points | `M`, controller map button, minimap click/tap, quest deep link |
| Exit points | Back, close map, ping commit, damage auto-close nếu configured |
| Layout | PC/Console landscape standard: full-màn hình hoặc large overlay với map, legend, extracts, objectives, squad |
| primary CTA | Set Ping / Track Objective |
| secondary actions | Filter markers, zoom, recenter, kiểm tra extract |

### Tactical Map trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Normal | Shows known terrain, squad, active objective, extracts |
| Jammed / no signal | Hide live elements và explain source nếu known |
| Partial intel | Unknown extracts hoặc areas cách dùng fog/unknown labels |
| Danger nearby | Keep audio live và show cảnh báo edge treatment |
| Quest focus | Highlight relevant area mà không revealing exact hidden objective nếu design forbids it |

---

## Looting Overlay

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Let người chơi choose loot quickly while understanding exposure và weight |
| Visual model | Partial overlay; game remains hiển thị rõ và audible |
| primary CTA | Take selected / Take all nếu allowed |
| secondary actions | kiểm tra, compare, quick equip, mark, close |
| Destructive actions | Discard hoặc swap valuable item requires confirmation nếu safe to do so |

### Looting trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Searching | Timed progress với cancel on movement/damage rules |
| Open container | Container list/grid và backpack summary |
| Overweight | Show movement penalty và block nếu above hard limit |
| Interrupted | Close hoặc pause transfer, show reason |
| Locked | Show required chính/tool và whether người chơi owns it |
| empty | Compact empty message; quick close remains focused |

---

## Inventory Overlay

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Support survival item cách dùng và limited item management mà không turning raid into stash management |
| Entry points | Inventory chính/button, loot context |
| Layout | Equipment, backpack, secure container, quick slots, weight |
| primary CTA | cách dùng / Equip / Move based on selected item |
| Restrictions | Some stash-only actions are disabled in raid với explanation |

### Mid-Raid Item Rules

| Action | In-Raid UI Rule |
| :--- | :--- |
| cách dùng medical item | Show duration, movement constraints, cancel rule |
| Move to secure container | Confirm nếu replacing protected item |
| Drop item | Confirm for insured, quest, rare, hoặc high-giá trị items |
| Split stack | available only khi màn hình space permits; otherwise keep the action disabled với an explanation |
| Repair/mod vũ khí | disabled unless cụ thể field action is supported |

---

## Pause Overlay

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Allow settings và exit quyết định while preserving online raid danger |
| Background | Frosted/dim overlay; game world motion và audio remain perceptible |
| primary CTA | Resume |
| secondary actions | Settings, controls, report issue, squad, network info |
| hành động phá hủy/không hồi phục | Abandon Raid requires hold confirm và rõ gear-loss message |

### Safeguards

| Safeguard | Rule |
| :--- | :--- |
| Damage received | Auto-dismiss hoặc flash cảnh báo depending tuning |
| Audio | Never mute gameplay audio by default |
| Cursor/camera | Cursor unlocked; camera input paused |
| Tab switching | Inventory/map inputs switch directly to those overlays |

---

## Spectator View

Layout (PC/Console)

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

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Keep eliminated squad người chơi engaged mà không enabling unfair ghosting |
| View | Teammates only; no địch freecam |
| primary CTA | Cycle Teammate |
| secondary actions | Ping nếu allowed, report, mute, open AAR sau squad end |
| Restrictions | Delay, limited map intel, no địch máu/inventory |

---

## Reconnect Overlay

Layout (PC/Console)

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

| trạng thái | Behavior |
| :--- | :--- |
| Reconnecting | Spinner, attempt count, timeout, last known raid |
| Reconnected | Fade back to raid và restore HUD trạng thái |
| Timeout | Explain MIA/gear consequence và route to Home |
| Version mismatch | Require update; show no retry until version matches |
| Cancel | Confirm that cancel may abandon raid và lose gear |

---

## Input Mapping

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Open map | M / minimap click | Map/View button | Tap minimap |
| Open inventory | Tab / I | Menu combo hoặc D-pad shortcut | Swipe/top button |
| Loot | F / click | A / Cross | Tap / hold |
| Close overlay | ESC | B / Circle | Close button |
| Ping | Middle mouse / ping chính | D-pad / bumper | Ping button / long press map |
| Pause | ESC | Start/Menu | Pause button |

---

## Designer-Ready màn hình Specs

In-raid specs must preserve threat awareness. Every overlay below must keep audio dễ đọc, close immediately, và avoid hiding survival-critical trạng thái unless the design explicitly accepts that risk.

### HUD Reference

**người chơi Intent**

Read survival-critical information while moving, fighting, looting, và extracting mà không opening a blocking menu.

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

| Region | yêu cầu |
| :--- | :--- |
| Top band | squad, compass, raid timer only |
| Center | kept mostly rõ for combat readability |
| Bottom band | prompts, status effects, đạn, ability, weight |
| Corners | reserve for persistent nhưng non-blocking HUD clusters |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Lethal status | máu, giáp break, bleed, extraction timer |
| 2 | Action readiness | đạn, ability, interaction prompt |
| 3 | Navigation | compass, minimap, extraction hint |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| HUD cluster | Stable position và no layout jump khi values change |
| cảnh báo trạng thái | Text hoặc symbol plus color; never color alone |
| Prompt | Names input, action, hold/tap yêu cầu, và risk nếu noisy |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Combat | Reduce noncritical hints; keep máu/đạn hiển thị rõ |
| Low máu | Promote medical/status indicators |
| Extract active | Timer và extraction trạng thái become top priority |
| HUD disabled/custom | Critical cảnh báo still appear |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| cách dùng prompt | F / hold | A / Cross | Tap/hold prompt |
| Ping | Middle mouse | D-pad / bumper | Long press |
| Open map | M | View button | Tap minimap |

**Designer ghi chú**

- HUD is not a decorative frame; keep the playfield dominant.
- Any hidden HUD option must preserve death-prevention alerts.

**Acceptance checklist**

- [ ] Critical trạng thái remains dễ đọc trong khi combat.
- [ ] HUD clusters do not cover the operator hoặc immediate threat zone.

### Tactical Map

**người chơi Intent**

Orient, plan route, kiểm tra extracts, view squad pings, và check quest landmarks mà không gaining unfair địch tracking.

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

| Region | yêu cầu |
| :--- | :--- |
| Map canvas | largest area; shows terrain, extracts, pings, quest zones |
| Filters/legend | text labels for all symbols |
| chi tiết panel | selected marker rule, distance, risk, availability |
| Exposure notice | persistent reminder that raid continues |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | người chơi/squad position và extracts | Always hiển thị rõ |
| 2 | Selected marker chi tiết | Must explain rule và risk |
| 3 | Filters | secondary và compact |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Extract marker | name, availability, rule, distance |
| Ping marker | owner, age, type, decay |
| Quest marker | objective, status, yêu cầu |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| No map intel | Show partial map và explain missing intel |
| địch nearby | Do not reveal địch unless hệ thống rules allow |
| Jammed/EMP | Show degraded map reason |
| Online raid | Never hard-pauses gameplay |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Pan/zoom | Drag/wheel | Sticks/triggers | Pinch/drag |
| Place ping | Right-click | A / Cross | Long press |
| Close | M/Esc | B / Circle | Close button |

**Designer ghi chú**

- Map should feel like an exposed tactical tool, not a safe menu.
- All icons need legend labels.

**Acceptance checklist**

- [ ] Extract rules are dễ đọc.
- [ ] Raid exposure is hiển thị rõ while map is open.

### Looting Overlay

**người chơi Intent**

Search, compare, và transfer loot fast while understanding noise, exposure, weight, và inventory capacity.

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

| Region | yêu cầu |
| :--- | :--- |
| Container list/grid | item identity, size, rarity/giá trị, FIR/quest trạng thái |
| người chơi inventory | target capacity và valid placement |
| Exposure header | noise/search trạng thái và vulnerability cảnh báo |
| Selected chi tiết | giá trị, weight, quest/FIR, actions |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Exposure và close action | Always hiển thị rõ |
| 2 | Item giá trị/quest trạng thái | hiển thị rõ trước transfer |
| 3 | Capacity/weight | Persistent trong khi movement |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Loot tile | name, footprint, stack, FIR/quest/giá trị badges |
| Transfer preview | valid/invalid target và resulting weight |
| Search progress | truthful timer và noise trạng thái |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Searching | Progress, noise, cancel available |
| Container empty | Show empty kết quả và close path |
| Inventory full | Block transfer, show needed cells |
| Under fire | Overlay may auto-minimize hoặc cảnh báo intensifies |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Take item | Click/drag | A / Cross | Tap |
| Quick move | Ctrl-click | X / Square | Double tap |
| Close | Esc | B / Circle | Close |

**Designer ghi chú**

- Do not hide the risk of standing still.
- Quest/FIR labels phải được text-dễ đọc.

**Acceptance checklist**

- [ ] Exposure, weight, và capacity are hiển thị rõ while looting.
- [ ] empty/full/under-fire trạng thái are specified.

### Inventory Overlay

**người chơi Intent**

Rearrange gear mid-raid under pressure mà không mistaking safe stash behavior for exposed raid behavior.

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

| Region | yêu cầu |
| :--- | :--- |
| Equipped gear | slots, durability, đạn, status |
| Inventory grid | rig/backpack/secure capacity |
| chi tiết panel | selected item effect, giá trị, risk |
| Action bar | cách dùng, move, split, drop, close |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Raid continues cảnh báo | Persistent |
| 2 | Weight và movement penalty | Always hiển thị rõ |
| 3 | Drop/destructive actions | Separated và confirmed |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Item tile | footprint, stack, FIR/quest/protected trạng thái |
| Drop action | consequence copy và confirm for protected/high-giá trị items |
| Secure container | visually distinct restrictions |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Overweight | Show movement penalty và remove options |
| Item locked | Disable invalid move/drop với reason |
| Healing/cách dùng in progress | Show timer và vulnerability |
| Combat detected | cảnh báo, nhưng người chơi retains control |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop | Grid cursor | Tap item then target |
| cách dùng item | Hotkey/click | A / Cross | Tap action |
| Drop | Context menu | Hold button | Long press + confirm |

**Designer ghi chú**

- Mid-raid inventory needs faster exits và stronger risk copy than stash.
- Do not reuse stash destructive affordances mà không raid-cụ thể cảnh báo.

**Acceptance checklist**

- [ ] Raid exposure, weight, và destructive drop cảnh báo are rõ.
- [ ] Controller và touch can move items mà không precision-only input.

### Pause Overlay

**người chơi Intent**

Access settings, squad/social, abandon, report, hoặc reconnect options while understanding that online raid trạng thái is not paused.

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

| Region | yêu cầu |
| :--- | :--- |
| Action list | resume first, settings/support secondary |
| Danger notice | non-paused trạng thái và vulnerability |
| Abandon | separated hành động phá hủy/không hồi phục |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Resume | Default focus |
| 2 | Online continues notice | Near header |
| 3 | Abandon | Low và separated |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Resume CTA | immediate close |
| Abandon CTA | hold/confirm với gear consequence |
| Settings shortcut | opens safe subset mà không hiding danger notice |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Offline/local | May pause nếu mode allows |
| Online | Does not pause; audio continues |
| Downed/dead | Action set changes to spectate/report |
| Abandon confirm | Names MIA/gear consequence |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Resume | Esc / click | Start/B | Resume button |
| Navigate | Mouse/arrows | D-pad | Tap |
| Abandon | Hold confirm | Hold confirm | Hold CTA |

**Designer ghi chú**

- Default focus must never land on Abandon.
- Keep background dễ đọc enough to preserve threat context.

**Acceptance checklist**

- [ ] Online non-pause consequence is explicit.
- [ ] Abandon requires confirmation.

### Spectator View

**người chơi Intent**

Watch eligible teammates, understand remaining squad trạng thái, và avoid unfair ghosting sau death.

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

| Region | yêu cầu |
| :--- | :--- |
| Header | spectated người chơi, squad alive, report |
| View | allowed teammate/camera only |
| Controls | previous/next, camera mode, leave |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Spectated identity | Always hiển thị rõ |
| 2 | Anti-ghosting limits | Communicated khi camera is restricted |
| 3 | Leave/report actions | available nhưng secondary |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| người chơi switcher | only eligible teammates |
| Camera mode | labels restrictions |
| Report action | keeps match context |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Teammates alive | Spectate allowed allies |
| All eliminated | Route to post-raid |
| địch spectate blocked | Show restriction reason |
| Reconnect teammate | Shows temporary unavailable trạng thái |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch target | Q/E | Bumpers | Swipe/tap |
| Change camera | C | Y / Triangle | Camera button |
| Leave | Click | Menu | Leave button |

**Designer ghi chú**

- Spectator UI không được reveal địch information unavailable to the squad.
- Keep report reachable mà không making it primary.

**Acceptance checklist**

- [ ] Anti-ghosting camera restrictions are explicit.
- [ ] All-eliminated trạng thái routes cleanly to post-raid.

### Reconnect Overlay

**người chơi Intent**

Understand reconnection progress, attempts, timeout, và the consequence of canceling while gear và raid status are at risk.

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

| Region | yêu cầu |
| :--- | :--- |
| Session summary | map, mode/thời gian, last known trạng thái |
| Progress | attempt count, timeout, hiện tại operation |
| Consequence cảnh báo | MIA/gear risk |
| Actions | cancel với confirm, retry nếu allowed |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Timeout và attempt | Always hiển thị rõ |
| 2 | Gear consequence | Above cancel |
| 3 | Retry status | secondary |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Progress bar | names real operation |
| Cancel | confirm với consequence |
| Error code | shown on failure for support |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Reconnecting | Spinner/progress, attempt count, timeout |
| Reconnected | Fade back và restore HUD |
| Timeout | Explain MIA/gear kết quả và route home |
| Version mismatch | Require update; retry disabled |
| Cancel | Confirm abandon consequence |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Retry | Click | A / Cross | Retry button |
| Cancel | Click + confirm | B / Circle + confirm | Cancel + confirm |

**Designer ghi chú**

- Do not make cancel look safe.
- Timeout nên được concrete, not vague.

**Acceptance checklist**

- [ ] Attempts, timeout, và gear consequence are hiển thị rõ.
- [ ] Version mismatch và timeout have rõ next steps.

---

## Production State Matrix

| Surface | Loading / Pending | Disabled / Locked | Invalid / Error | Offline / Reconnect | Success / Recovery |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HUD | late-bound squad/objective widgets skeleton | hidden chỉ bởi explicit HUD setting | missing data dùng safe fallback icon/text | reconnect banner/timer priority | restored widgets animate tối thiểu |
| Tactical Map | map tiles/objective pins stream in | unavailable intel nói lý do | route/ping fail nêu blocked reason | cached map có stale label | ping/route confirmed với text/icon |
| Looting Overlay | container search progress | locked container show key/tool requirement | invalid transfer, full bag, protected item | pending sync block destructive actions | item moved với source/destination toast |
| Inventory Overlay | item details pending | invalid slots show compatibility reason | split/drop/use failure nêu rule | reconnect freezes move/discard | server confirms placement |
| Pause Overlay | online status checking | abandon/report/settings gated with reason | failed report/settings save retry | raid not paused warning persistent | resume returns focus |
| Spectator View | replay/spectator target loading | enemy info locked by fairness rule | unavailable camera names reason | reconnect CTA prioritized while eligible | target switch confirms |
| Reconnect Overlay | attempt count and timeout visible | cancel disabled only during server lock | failed attempt shows retry/support | primary reconnect state | resume hoặc MIA transition explained |

## Platform Behavior And Input

| Platform | Rule |
| :--- | :--- |
| PC | Overlay open state owns keyboard focus; Esc/back closes non-destructive overlays first. |
| Console | Radial/bumper shortcuts không được hide extraction, downed, hoặc reconnect warnings. |
| Mobile | Touch targets tránh combat-critical center khi có thể; bottom sheets không cover lethal state nếu không có indicator. |

## Analytics Funnel

| Event | Required Properties |
| :--- | :--- |
| `in_raid_surface_opened` | surface, raid_phase, platform |
| `in_raid_action_attempted` | surface, action, item_id_or_target, input_method |
| `in_raid_action_blocked` | blocker_type, severity, player_state |
| `reconnect_attempt_result` | attempt_index, remaining_window, result |
| `overlay_closed` | surface, reason, duration |

## In-Raid QA Checklist

- Không overlay nào hide death, extraction, downed, reconnect, hoặc critical health state nếu không có persistent indicator khác.
- Mọi blocked item/action/ping giải thích rule bằng text, không chỉ color.
- Controller focus quay về triggering element khi overlay đóng.
- Pending sync disables destructive item actions đến khi server confirm.

## Analytics

| Metric | cách dùng |
| :--- | :--- |
| Death while in overlay | Identify risky UI coverage hoặc auto-dismiss rules |
| Loot transfer thời gian | Tune speed và weight clarity |
| Tactical map open duration | Detect map readability hoặc overuse |
| Abandon raid attempts | Identify frustration hoặc disconnect issues |
| Reconnect success rate | Track network recovery quality |

---

## checklist Nghiệm Thu

- [ ] Game audio remains useful under all in-raid overlays.
- [ ] Overlay close behavior is immediate và nhất quán.
- [ ] Looting và inventory communicate exposure và weight.
- [ ] Tactical map avoids unfair địch tracking.
- [ ] Reconnect và abandon flow explain gear consequences.
- [ ] Spectator view has anti-ghosting restrictions.
