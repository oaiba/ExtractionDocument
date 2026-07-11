---
title: "In-Raid HUD Design"
type: docs
weight: 20
---

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Full UI/UX documentation hub |
| [màn hình Groups Overview](screen_groups_overview/index.html) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](global_ux_standards/index.html) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [In-Raid màn hình](in_raid_screens/index.html) | HUD in context với tactical map, looting, pause, spectator, reconnect |
| [Notification hệ thống](notification_systems/index.html) | Combat feedback, damage, status effects, toasts, danger communication |
| [UX flow](ux_flows/index.html) | người chơi journeys that reference HUD và overlays |

---

## HUD Philosophy

The in-raid HUD follows one principle: **show only what matters, khi it matters**.

| Rule | Implementation |
| :--- | :------------- |
| Minimum obstruction | HUD elements occupy no more than 15% of total màn hình area |
| Contextual visibility | Elements appear/disappear based on game trạng thái |
| Glanceable design | Any single HUD element phải được dễ đọc in under 0.5 seconds |
| No clutter stacking | Maximum 3 notification types hiển thị rõ simultaneously |
| Platform consistency | Same information on all platforms, adapted layout for màn hình size |

### Diegetic vs. Non-Diegetic Elements

| Type | Description | Examples |
| :--- | :---------- | :------- |
| **Diegetic** | UI exists within the game world, seen by the nhân vật | vũ khí đạn count on the magazine, watch for thời gian, geiger counter radiation display |
| **Non-Diegetic** | Traditional overlay HUD, hiển thị rõ only to the người chơi | máu bar, minimap, kill feed, extraction timer |
| **Spatial** | Exists in 3D space nhưng not hiển thị rõ to the nhân vật | Squad mate markers, objective waypoints, extraction zone indicators |

This game uses primarily **non-diegetic HUD** for clarity in top-down perspective, với **spatial markers** for squad và objective tracking.

---

## HUD Element Catalog

### Complete Element List

| Element | Position | Always hiển thị rõ | Priority |
| :------ | :------- | :------------- | :------- |
| máu & giáp Bar | Top-Left | Yes | Critical |
| Stamina Bar | Below máu | trong khi activity only | High |
| đạn Counter | Bottom-Left | Yes (in combat) | Critical |
| vũ khí Indicator | Bottom-Left | Yes | High |
| Minimap / Compass | Top-Right | Yes | Critical |
| Extraction Timer | Top-Center | Yes | Critical |
| Squad Panel | Right edge | Yes (in squad mode) | High |
| Weight Indicator | Near inventory | khi near capacity only | Medium |
| Stance Indicator | Near nhân vật | khi stance changes | Low |
| Interaction Prompt | Center-Bottom | khi near interactable | Medium |
| Status Effect Icons | Below máu | khi affected | High |
| Notification Feed | Top-Left (below máu) | khi triggered | Medium |
| Kill Feed | Top-Right (below minimap) | khi triggered | Medium |

---

## HUD Layout — PC / Console (Landscape)

```
+--------------------------------------------------------------------+
|                                                                    |
|  [HP: 85/100]  [ARMOR: 42]        EXTRACT: 22:15      [MINIMAP]    |
|  [STAMINA: ---|||||||||-- ]                              N         |
|  [Bleed] [Fracture]                                   W     E      |
|                                                          S         |
|                                                                    |
|                                                                    |
|                                                                    |
|                   [  GAMEPLAY AREA  ]                              |
|                   (Maximum visibility)                             |
|                                                                    |
|                                                                    |
|                          [Hold F: Loot Body]                       |
|                                                                    |
|  [PRIMARY]                                         [SQUAD]         |
|  AK-74M                                           P1: 85HP [OK]    |
|  [30 / 120] 7.62x39                               P2: 42HP [!]     |
|  [FIRE MODE: Auto]                                P3: DEAD  [X]    |
|  [GRENADE x2]                                                      |
|                                                                    |
+----------------------------------------------------------------==--+
```

<!-- REF_IMAGE: HUD layout annotated diagram — showing element positions với callout labels và safe zone boundaries for PC/Console -->

---

## HUD Layout — Mobile (Portrait)

```
+-----------------------------+
|  HP:85  ARM:42  [22:15] [M] |
|  [Bleed]                     |
|                              |
|                              |
|                              |
|      [GAMEPLAY AREA]         |
|                              |
|                              |
|                              |
|                              |
|  [Crouch]           [Reload] |
|  [JOYSTICK]  AK 30/120 [AIM]|
|              [FIRE]   [GREN] |
+-----------------------------+

Mobile-specific:
- Touch controls overlay on bottom 25% of screen
- HUD elements condensed to single status bar at top
- Minimap: small icon, tap to expand full-screen
- Squad panel: hidden by default, swipe from right edge
```

<!-- REF_IMAGE: Mobile HUD layout — showing condensed top bar, touch controls at bottom, gameplay area maximized -->

---

## Element Specifications

### máu và giáp Bar

| Property | Specification |
| :------- | :------------ |
| Position | Top-left corner, 16px from edges |
| Size | máu: 200x16px. giáp: 160x12px (below máu) |
| máu color | Green (above 50%), Yellow (25-50%), Red (below 25%), Flashing red (below 10%) |
| giáp color | Steel Blue, segments break as giáp degrades (each segment = 25%) |
| Number display | hiện tại / Max shown in JetBrains Mono (e.g., "85 / 100") |
| Damage flash | Bar briefly flashes white khi taking damage (100ms) |
| Healing animation | Bar fills với brighter shade, sparkle particle at fill edge |
| Low máu cảnh báo | Below 25%: subtle red vignette at màn hình edges, heartbeat sound |

### Stamina Bar

| Property | Specification |
| :------- | :------------ |
| Position | Below máu bar, same left alignment |
| Size | 160x8px (thinner than máu — less quan trọng) |
| Visibility | Fades in khi sprinting/jumping, fades out 3 seconds sau full recovery |
| Color | Blue gradient, drains left-to-right |
| empty trạng thái | Bar pulses red, "Exhausted" text appears briefly, movement speed reduced |
| Arm vs. Leg stamina | Two sub-bars hiển thị rõ khi relevant (sprinting depletes leg, aiming depletes arm) |

### đạn Counter và vũ khí Indicator

| Property | Specification |
| :------- | :------------ |
| Position | Bottom-left corner, 16px from edges |
| Layout | vũ khí icon + name on top line, đạn count on bottom line |
| đạn format | `[Magazine / Reserve]` in JetBrains Mono (e.g., "30 / 120") |
| Magazine color | White normally. Yellow at 25% remaining. Red at 10% hoặc last magazine |
| Fire mode | Text indicator: "Auto", "Semi", "Burst". Flashes khi switched |
| Grenade counter | Small icon + count below đạn (e.g., grenade icon x2) |
| empty magazine | đạn text turns red, "RELOAD" text pulses |
| vũ khí swap | Old vũ khí slides out left, new vũ khí slides in from left (200ms) |

### Minimap

| Property | Specification |
| :------- | :------------ |
| Position | Top-right corner, 16px from edges |
| Size | 180x180px circle (PC/Console), 100x100px (Mobile) |
| Rotation | Map rotates với người chơi direction (north is NOT always up) |
| Zoom | 2 zoom levels: Close (25m radius) và Far (75m radius). Toggle với chính/button |
| người chơi icon | White arrow pointing in facing direction |
| Squad icons | Blue arrows với người chơi name label |
| địch icons | NOT shown (no minimap địch tracking — this is a hardcore shooter) |
| Objective markers | Yellow diamond for active quest objectives |
| Extraction markers | Green hexagon for open extractions, gray for closed |
| Terrain | Simplified floor plan (walls shown as dark lines, open areas as dark surface) |
| Edge fade | Circular fade at minimap border (no hard edge cutoff) |
| Interactive | Click/tap minimap to open full-màn hình tactical map |

<!-- REF_IMAGE: Minimap specification diagram — showing icon legend, zoom level comparison, và terrain rendering style -->

Layout (PC/Console)

```
+----------------------+
|        MINIMAP       |
|      N               |
|   W  ^Player     E   |
|      |               |
|  o Squad     ! Quest |
|  H Extract   x Closed|
|      S               |
+----------------------+
Legend: o squad | ! objective | H open extract | x closed extract
```

### Compass

| Property | Specification |
| :------- | :------------ |
| Position | Top-center, integrated into extraction timer area |
| Style | Horizontal strip showing 90-degree FOV arc với bearing marks |
| Bearing marks | N, NE, E, SE, S, SW, W, NW labeled. Minor ticks every 15 degrees |
| Squad callouts | khi a squadmate pings, a colored marker appears on the compass at the correct bearing |
| Quest objectives | Yellow marker on compass bearing toward active objective |
| Gunshot detection | Brief red flash on compass in the direction of nearby gunfire (fades in 2 seconds) |
| No địch tracking | Compass does NOT show địch. Only sound-based directional hints |

### Extraction Timer

| Property | Specification |
| :------- | :------------ |
| Position | Top-center of màn hình |
| Format | `MM:SS` countdown in Oxanium Bold |
| Color trạng thái | White (normal), Yellow (under 10 minutes), Red (under 5 minutes), Flashing red (under 2 minutes) |
| Audio cues | Subtle tick sound starts at 5 minutes. Urgent alarm at 2 minutes |
| Overtime | nếu timer hits 0:00, "EMERGENCY EXTRACT" flashes. 60-second grace period begins |

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         EXTRACTING: 00:23                        |
|                    [==========--------]                          |
|                                                                  |
|               Stay in zone. Taking fire resets timer.            |
|                                                                  |
| Health 85/100                                      Squad P2 42HP |
+------------------------------------------------------------------+
```

### Squad Panel

| Property | Specification |
| :------- | :------------ |
| Position | Right edge of màn hình, vertically stacked |
| Visibility | Always hiển thị rõ in squad mode. Hidden in solo |
| Per-member info | Name, HP bar (mini), Status icon |
| Status icons | Green check (alive + healthy), Yellow exclamation (wounded), Red X (dead), Blue arrow (extracting) |
| Distance | Shown in meters khi squadmate is beyond 50m |
| Voice indicator | Small speaker icon animates khi teammate is transmitting |
| Click interaction | PC: click teammate card to ping their location. Console: D-pad select + A |

### Interaction Prompt

| Property | Specification |
| :------- | :------------ |
| Position | Center-bottom, 200px above màn hình bottom |
| Trigger | người chơi looks at hoặc is within range of an interactable object |
| Format | `[Key/Button] + Action` (e.g., "Hold F: Search Body", "Press E: Open Door") |
| Fade timing | Appears: 200ms fade-in. Disappears: immediate khi out of range |
| Priority | nếu multiple interactables overlap, show the closest one. secondary shown as smaller text |
| Progress bar | For timed interactions (searching, healing), circular progress fills around the prompt |

### Weight Indicator

| Property | Specification |
| :------- | :------------ |
| Position | Near the đạn counter, bottom-left area |
| Visibility | Hidden khi below 60% capacity. hiển thị rõ at 60%+. Prominent at 80%+ |
| Format | `24.5 / 40.0 kg` |
| Color | White (below 60%), Yellow (60-80%), Orange (80-95%), Red (95%+) |
| Movement penalty | Text below weight shows speed modifier: "-15% movement" |
| Overweight | Above 100%: Cannot sprint. Red flashing weight indicator. "OVERLOADED" text |

---

## Contextual Visibility Rules

HUD elements are not all hiển thị rõ at all times. The hệ thống uses game trạng thái to determine visibility:

| Game trạng thái | hiển thị rõ Elements | Hidden Elements | Reason |
| :--------- | :--------------- | :-------------- | :----- |
| **Idle** (no combat, no interaction) | máu, Minimap, Timer | Stamina, đạn (faded), Weight (nếu low) | Reduce clutter trong khi exploration |
| **Combat** (shots fired, địch detected) | ALL elements at full opacity | None | Maximum information trong khi danger |
| **Looting** (interacting với container) | máu, đạn, Weight, Looting UI | Minimap (shrunk), Squad (shrunk) | Focus on loot quyết định |
| **Healing** (using medical item) | máu (enlarged), Healing progress, Stamina | đạn, Minimap (dimmed) | Focus on healing animation |
| **Extraction** (in extraction zone) | Timer (enlarged), Extraction progress, máu | Most elements dimmed | Focus on extraction countdown |
| **Low máu** (below 25%) | máu (enlarged + vignette), Status effects | Non-critical elements dimmed | Communicate danger urgently |
| **Death** | Death màn hình takes over | All HUD elements | Transition to sau Action Report |

### Fade Timing

| Transition | Duration | Easing |
| :--------- | :------- | :----- |
| Element appears | 200ms | Ease-out |
| Element disappears | 500ms | Ease-in (slow fade prevents jarring loss) |
| trạng thái change (idle → combat) | 150ms | Ease-out (information appears fast) |
| trạng thái change (combat → idle) | 2000ms | Ease-in (slow wind-down, safety buffer) |

---

## HUD Customization Options

### người chơi-Adjustable Settings

| Setting | Options | Default |
| :------ | :------ | :------ |
| HUD Scale | 75% / 100% / 125% / 150% | 100% |
| HUD Opacity | 50% - 100% slider | 85% |
| Minimap Size | Small / Medium / Large | Medium |
| Minimap Rotation | Rotate với người chơi / Fixed north-up | Rotate |
| máu thông số | Show / Hide numerical values | Show |
| Kill Feed | Show / Hide | Show |
| Hit Markers | Show / Hide | Show |
| Damage thông số | Show / Hide | Hide (optional tính năng) |
| Compass | Show / Hide | Show |
| FPS Counter | Show / Hide | Hide |

### HUD Layout Customization

| tính năng | Description |
| :------ | :---------- |
| HUD Scale | global HUD scale adjustment within PC/Console safe-zone limits |
| Element Visibility | Toggle optional elements such as compass, kill feed, damage thông số, và FPS counter |
| Minimap Preset | Small / Medium / Large presets using the PC/Console minimap anchor |
| Opacity | global HUD opacity slider for non-critical overlays |
| Preset Layouts | Standard / Minimal / Tactical presets; all cách dùng the PC/Console landscape layout |
| Reset | One button to restore the default PC/Console HUD layout |

---

## Designer-Ready HUD Element Specs

These specs translate the HUD catalog into layout-ready components. Each element must preserve the central combat read area và không được move khi values change.

### global HUD Placement

#### Ý Định Người Chơi

Read lethal trạng thái, navigation, objective, và interaction information mà không breaking top-down combat focus.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| Squad / Health                  Compass / Objective                    Timer   |
|                                                                                |
|                         clear combat and operator read area                    |
|                                                                                |
| Prompt / Status Effects                         Ammo / Ability / Weight / Map  |
+--------------------------------------------------------------------------------+
```

#### Giải Phẫu Bố Cục

| Region | yêu cầu |
| :--- | :--- |
| Top left | squad, máu, giáp, critical injury |
| Top center | compass và objective pulse |
| Top right | extraction timer và raid cảnh báo |
| Bottom left | prompts và status effects |
| Bottom right | đạn, vũ khí, ability, weight, minimap |

#### Thứ Bậc Thị Giác

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Death-prevention info | máu, bleed, đạn empty, extraction timer |
| 2 | Immediate action | prompt, reload, ability ready |
| 3 | Navigation/context | compass, minimap, objective |

#### Yêu Cầu Component

| Component | yêu cầu |
| :--- | :--- |
| HUD cluster | fixed anchor, safe-zone aware, stable width |
| cảnh báo trạng thái | text/icon plus color; no color-only meaning |
| Optional element | can be hidden only nếu critical override still appears |

#### Trạng Thái & Edge Case

| trạng thái | Behavior |
| :--- | :--- |
| Combat | suppress noncritical toasts và tips |
| Low máu | máu/status cluster promoted |
| Extraction active | timer becomes top-right priority |
| Minimal HUD | critical alerts still break thông qua |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| kiểm tra map | M / click minimap | View button | Tap minimap |
| cách dùng prompt | F / hold | A / Cross | Tap/hold |
| Ping | Middle mouse | D-pad/bumper | Long press |

#### Ghi Chú Cho Designer

- Reserve the center for target, cover, projectiles, và operator silhouette.
- Never let changing thông số resize the đạn hoặc timer cluster.

#### checklist Nghiệm Thu

- [ ] Critical clusters are safe-zone aware on PC, console, và mobile.
- [ ] Minimal/custom HUD still shows lethal cảnh báo.

### Element-Level yêu cầu

| Element | Anatomy | Visibility Rule | Failure / Edge trạng thái | Platform Behavior |
| :--- | :--- | :--- | :--- | :--- |
| máu và giáp | body HP, giáp durability, injury icons | always hiển thị rõ in combat và damage trạng thái | broken giáp, bleed, fracture, downed | mobile uses compact stacked bars |
| Stamina | hiện tại stamina, exhaustion marker | fades khi full và safe | exhausted, overweight, sprint locked | mobile keeps near movement controls |
| đạn và vũ khí | magazine, reserve, fire mode, vũ khí name | always hiển thị rõ trong khi vũ khí-ready trạng thái | empty, jammed, wrong đạn, reload blocked | console adds button hint for reload |
| Minimap | người chơi, extracts, squad pings, noise-safe markers | optional nhưng extraction cảnh báo overrides | jammed, no intel, map disabled | mobile can expand from corner |
| Compass | heading, pings, objective tick | hiển thị rõ while moving/aiming | jammed hoặc objective hidden | mobile uses shortened ticks |
| Extraction Timer | raid thời gian, extraction countdown, overtime | always hiển thị rõ under 5 minutes hoặc extracting | timer critical, extract blocked | enlarged cảnh báo on mobile |
| Squad Panel | teammate HP, role, distance, downed trạng thái | hiển thị rõ in squad modes | disconnected, downed, dead, muted | collapsible on mobile |
| Interaction Prompt | input, action verb, hold/tap, risk/noise | appears only khi actionable | blocked, locked, noisy, inventory full | touch prompt phải được tappable |
| Weight Indicator | hiện tại/max, penalty tier | hiển thị rõ khi looting hoặc overweight | overweight, movement penalty, cannot sprint | pinned near inventory on mobile |

### HUD QA checklist

- [ ] Every HUD element has a stable anchor và does not shift khi values change.
- [ ] Every cảnh báo has a text/icon fallback beyond color.
- [ ] Combat, looting, extraction, downed, jammed, và mobile condensed trạng thái are represented.
- [ ] Optional HUD customization cannot hide death-prevention alerts.

---

## HUD Production State Matrix

| Element | Normal | Warning | Critical / Error | Offline / Reconnect | Accessibility Requirement |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Health / armor | current values and armor zone | low HP, armor damaged | downed, bleed, armor broken | reconnect banner overrides non-critical motion | text/icon plus color |
| Ammo / weapon | ammo, fire mode, weapon name | low ammo, reload needed | empty, jam/broken nếu supported | weapon action disabled while reconnecting | audio + icon + number |
| Stamina / weight | stamina and weight tier | encumbered, exhausted | cannot sprint/carry blocker | preserve last known state as stale | label weight tier |
| Extraction | available extract, timer, distance | late raid, contested | interrupted, blocked, not enough time | reconnect window result priority | countdown text and sound |
| Squad | alive/downed/extracted state | low health, split, disconnected | dead/MIA/abandoned | reconnect grace timer | state text, not color only |
| Interaction prompt | action, hold/tap progress | invalid tool/key/item | blocked action reason | disabled while server state unknown | readable button glyph and text |

## Combat Feedback Requirements

| Feedback | HUD / Notification Rule |
| :--- | :--- |
| Flesh hit | short hit marker and optional damage number if enabled |
| Armor hit | distinct marker/sound and armor interaction recap support |
| No penetration / ricochet | blocked/deflected marker; never silent zero damage |
| Suppression | brief directional stress and aim pressure indicator with reduced-motion setting |
| Low ammo / reload | ammo counter warning before empty, reload progress readable |
| Extraction interrupt | timer reset reason shown immediately with audio cue |
| Death cause | concise cause passes to post-raid debrief and death replay |

## HUD Analytics And QA

| Signal | Purpose |
| :--- | :--- |
| `hud_critical_state_shown` | health, armor, ammo, extraction, downed, reconnect |
| `hud_prompt_blocked` | interaction, blocker, input method |
| `hud_customization_changed` | element, visibility, scale, platform |

- Critical HUD states remain visible over maps, looting, pause, spectator, and reconnect surfaces.
- Combat feedback không rely vào color alone.
- HUD customization không được hide required raid outcome hoặc extraction consequence states.
- Mobile HUD giữ touch-safe combat center và tránh overlap fire/aim controls.

## Performance Budget

### HUD Rendering Rules

| Metric | Budget | Enforcement |
| :----- | :----- | :---------- |
| Draw calls (HUD total) | Maximum 50 per frame | Batch all HUD elements into 3 texture atlases |
| Update frequency (máu, đạn) | Every frame (critical elements) | Direct binding to game trạng thái |
| Update frequency (minimap) | Every 3 frames | Reduces GPU chi phí of minimap rendering |
| Update frequency (kill feed, notifications) | Event-driven only | No per-frame polling — triggered by game events |
| Memory (HUD textures) | Maximum 32MB | Single 2048x2048 atlas for icons + elements |
| Overdraw | Maximum 2x for HUD region | Semi-transparent elements cách dùng pre-multiplied alpha |

### Platform-cụ thể HUD FPS Targets

| Platform | HUD Rendering Target | ghi chú |
| :------- | :------------------- | :---- |
| PC | Matches game FPS (up to 144) | HUD animations scale với delta thời gian |
| Console | 60 FPS | HUD never drops below game FPS |
| Mobile | 60 FPS target, 30 FPS minimum | Simplified HUD shader on low-end devices |
