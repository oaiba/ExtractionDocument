---
title: "In-Raid HUD Design"
type: docs
weight: 20
---

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Full UI/UX documentation hub |
| [Screen Groups Overview](screen_groups_overview/index.html) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](global_ux_standards/index.html) | Shared navigation, focus, state, modal, and accessibility rules |
| [In-Raid Screens](in_raid_screens/index.html) | HUD in context with tactical map, looting, pause, spectator, reconnect |
| [Notification Systems](notification_systems/index.html) | Combat feedback, damage, status effects, toasts, danger communication |
| [UX Flows](ux_flows/index.html) | Player journeys that reference HUD and overlays |

---

## HUD Philosophy

The in-raid HUD follows one principle: **show only what matters, when it matters**.

| Rule | Implementation |
| :--- | :------------- |
| Minimum obstruction | HUD elements occupy no more than 15% of total screen area |
| Contextual visibility | Elements appear/disappear based on game state |
| Glanceable design | Any single HUD element must be readable in under 0.5 seconds |
| No clutter stacking | Maximum 3 notification types visible simultaneously |
| Platform consistency | Same information on all platforms, adapted layout for screen size |

### Diegetic vs. Non-Diegetic Elements

| Type | Description | Examples |
| :--- | :---------- | :------- |
| **Diegetic** | UI exists within the game world, seen by the character | Weapon ammo count on the magazine, watch for time, geiger counter radiation display |
| **Non-Diegetic** | Traditional overlay HUD, visible only to the player | Health bar, minimap, kill feed, extraction timer |
| **Spatial** | Exists in 3D space but not visible to the character | Squad mate markers, objective waypoints, extraction zone indicators |

This game uses primarily **non-diegetic HUD** for clarity in top-down perspective, with **spatial markers** for squad and objective tracking.

---

## HUD Element Catalog

### Complete Element List

| Element | Position | Always Visible | Priority |
| :------ | :------- | :------------- | :------- |
| Health & Armor Bar | Top-Left | Yes | Critical |
| Stamina Bar | Below Health | During activity only | High |
| Ammo Counter | Bottom-Left | Yes (in combat) | Critical |
| Weapon Indicator | Bottom-Left | Yes | High |
| Minimap / Compass | Top-Right | Yes | Critical |
| Extraction Timer | Top-Center | Yes | Critical |
| Squad Panel | Right edge | Yes (in squad mode) | High |
| Weight Indicator | Near inventory | When near capacity only | Medium |
| Stance Indicator | Near character | When stance changes | Low |
| Interaction Prompt | Center-Bottom | When near interactable | Medium |
| Status Effect Icons | Below Health | When affected | High |
| Notification Feed | Top-Left (below health) | When triggered | Medium |
| Kill Feed | Top-Right (below minimap) | When triggered | Medium |

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

<!-- REF_IMAGE: HUD layout annotated diagram — showing element positions with callout labels and safe zone boundaries for PC/Console -->

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

### Health and Armor Bar

| Property | Specification |
| :------- | :------------ |
| Position | Top-left corner, 16px from edges |
| Size | Health: 200x16px. Armor: 160x12px (below health) |
| Health color | Green (above 50%), Yellow (25-50%), Red (below 25%), Flashing red (below 10%) |
| Armor color | Steel Blue, segments break as armor degrades (each segment = 25%) |
| Number display | Current / Max shown in JetBrains Mono (e.g., "85 / 100") |
| Damage flash | Bar briefly flashes white when taking damage (100ms) |
| Healing animation | Bar fills with brighter shade, sparkle particle at fill edge |
| Low health warning | Below 25%: subtle red vignette at screen edges, heartbeat sound |

### Stamina Bar

| Property | Specification |
| :------- | :------------ |
| Position | Below health bar, same left alignment |
| Size | 160x8px (thinner than health — less important) |
| Visibility | Fades in when sprinting/jumping, fades out 3 seconds after full recovery |
| Color | Blue gradient, drains left-to-right |
| Empty state | Bar pulses red, "Exhausted" text appears briefly, movement speed reduced |
| Arm vs. Leg stamina | Two sub-bars visible when relevant (sprinting depletes leg, aiming depletes arm) |

### Ammo Counter and Weapon Indicator

| Property | Specification |
| :------- | :------------ |
| Position | Bottom-left corner, 16px from edges |
| Layout | Weapon icon + name on top line, ammo count on bottom line |
| Ammo format | `[Magazine / Reserve]` in JetBrains Mono (e.g., "30 / 120") |
| Magazine color | White normally. Yellow at 25% remaining. Red at 10% or last magazine |
| Fire mode | Text indicator: "Auto", "Semi", "Burst". Flashes when switched |
| Grenade counter | Small icon + count below ammo (e.g., grenade icon x2) |
| Empty magazine | Ammo text turns red, "RELOAD" text pulses |
| Weapon swap | Old weapon slides out left, new weapon slides in from left (200ms) |

### Minimap

| Property | Specification |
| :------- | :------------ |
| Position | Top-right corner, 16px from edges |
| Size | 180x180px circle (PC/Console), 100x100px (Mobile) |
| Rotation | Map rotates with player direction (north is NOT always up) |
| Zoom | 2 zoom levels: Close (25m radius) and Far (75m radius). Toggle with key/button |
| Player icon | White arrow pointing in facing direction |
| Squad icons | Blue arrows with player name label |
| Enemy icons | NOT shown (no minimap enemy tracking — this is a hardcore shooter) |
| Objective markers | Yellow diamond for active quest objectives |
| Extraction markers | Green hexagon for open extractions, gray for closed |
| Terrain | Simplified floor plan (walls shown as dark lines, open areas as dark surface) |
| Edge fade | Circular fade at minimap border (no hard edge cutoff) |
| Interactive | Click/tap minimap to open full-screen tactical map |

<!-- REF_IMAGE: Minimap specification diagram — showing icon legend, zoom level comparison, and terrain rendering style -->

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
| Style | Horizontal strip showing 90-degree FOV arc with bearing marks |
| Bearing marks | N, NE, E, SE, S, SW, W, NW labeled. Minor ticks every 15 degrees |
| Squad callouts | When a squadmate pings, a colored marker appears on the compass at the correct bearing |
| Quest objectives | Yellow marker on compass bearing toward active objective |
| Gunshot detection | Brief red flash on compass in the direction of nearby gunfire (fades in 2 seconds) |
| No enemy tracking | Compass does NOT show enemies. Only sound-based directional hints |

### Extraction Timer

| Property | Specification |
| :------- | :------------ |
| Position | Top-center of screen |
| Format | `MM:SS` countdown in Oxanium Bold |
| Color states | White (normal), Yellow (under 10 minutes), Red (under 5 minutes), Flashing red (under 2 minutes) |
| Audio cues | Subtle tick sound starts at 5 minutes. Urgent alarm at 2 minutes |
| Overtime | If timer hits 0:00, "EMERGENCY EXTRACT" flashes. 60-second grace period begins |

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
| Position | Right edge of screen, vertically stacked |
| Visibility | Always visible in squad mode. Hidden in solo |
| Per-member info | Name, HP bar (mini), Status icon |
| Status icons | Green check (alive + healthy), Yellow exclamation (wounded), Red X (dead), Blue arrow (extracting) |
| Distance | Shown in meters when squadmate is beyond 50m |
| Voice indicator | Small speaker icon animates when teammate is transmitting |
| Click interaction | PC: click teammate card to ping their location. Console: D-pad select + A |

### Interaction Prompt

| Property | Specification |
| :------- | :------------ |
| Position | Center-bottom, 200px above screen bottom |
| Trigger | Player looks at or is within range of an interactable object |
| Format | `[Key/Button] + Action` (e.g., "Hold F: Search Body", "Press E: Open Door") |
| Fade timing | Appears: 200ms fade-in. Disappears: immediate when out of range |
| Priority | If multiple interactables overlap, show the closest one. Secondary shown as smaller text |
| Progress bar | For timed interactions (searching, healing), circular progress fills around the prompt |

### Weight Indicator

| Property | Specification |
| :------- | :------------ |
| Position | Near the ammo counter, bottom-left area |
| Visibility | Hidden when below 60% capacity. Visible at 60%+. Prominent at 80%+ |
| Format | `24.5 / 40.0 kg` |
| Color | White (below 60%), Yellow (60-80%), Orange (80-95%), Red (95%+) |
| Movement penalty | Text below weight shows speed modifier: "-15% movement" |
| Overweight | Above 100%: Cannot sprint. Red flashing weight indicator. "OVERLOADED" text |

---

## Contextual Visibility Rules

HUD elements are not all visible at all times. The system uses game state to determine visibility:

| Game State | Visible Elements | Hidden Elements | Reason |
| :--------- | :--------------- | :-------------- | :----- |
| **Idle** (no combat, no interaction) | Health, Minimap, Timer | Stamina, Ammo (faded), Weight (if low) | Reduce clutter during exploration |
| **Combat** (shots fired, enemies detected) | ALL elements at full opacity | None | Maximum information during danger |
| **Looting** (interacting with container) | Health, Ammo, Weight, Looting UI | Minimap (shrunk), Squad (shrunk) | Focus on loot decisions |
| **Healing** (using medical item) | Health (enlarged), Healing progress, Stamina | Ammo, Minimap (dimmed) | Focus on healing animation |
| **Extraction** (in extraction zone) | Timer (enlarged), Extraction progress, Health | Most elements dimmed | Focus on extraction countdown |
| **Low Health** (below 25%) | Health (enlarged + vignette), Status effects | Non-critical elements dimmed | Communicate danger urgently |
| **Death** | Death screen takes over | All HUD elements | Transition to After Action Report |

### Fade Timing

| Transition | Duration | Easing |
| :--------- | :------- | :----- |
| Element appears | 200ms | Ease-out |
| Element disappears | 500ms | Ease-in (slow fade prevents jarring loss) |
| State change (idle → combat) | 150ms | Ease-out (information appears fast) |
| State change (combat → idle) | 2000ms | Ease-in (slow wind-down, safety buffer) |

---

## HUD Customization Options

### Player-Adjustable Settings

| Setting | Options | Default |
| :------ | :------ | :------ |
| HUD Scale | 75% / 100% / 125% / 150% | 100% |
| HUD Opacity | 50% - 100% slider | 85% |
| Minimap Size | Small / Medium / Large | Medium |
| Minimap Rotation | Rotate with player / Fixed north-up | Rotate |
| Health numbers | Show / Hide numerical values | Show |
| Kill Feed | Show / Hide | Show |
| Hit Markers | Show / Hide | Show |
| Damage Numbers | Show / Hide | Hide (optional feature) |
| Compass | Show / Hide | Show |
| FPS Counter | Show / Hide | Hide |

### HUD Layout Customization

| Feature | Description |
| :------ | :---------- |
| HUD Scale | Global HUD scale adjustment within PC/Console safe-zone limits |
| Element Visibility | Toggle optional elements such as compass, kill feed, damage numbers, and FPS counter |
| Minimap Preset | Small / Medium / Large presets using the PC/Console minimap anchor |
| Opacity | Global HUD opacity slider for non-critical overlays |
| Preset Layouts | Standard / Minimal / Tactical presets; all use the PC/Console landscape layout |
| Reset | One button to restore the default PC/Console HUD layout |

---

## Designer-Ready HUD Element Specs

These specs translate the HUD catalog into layout-ready components. Each element must preserve the central combat read area and must not move when values change.

### Global HUD Placement

#### Player Intent

Read lethal state, navigation, objective, and interaction information without breaking top-down combat focus.

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

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Top left | squad, health, armor, critical injury |
| Top center | compass and objective pulse |
| Top right | extraction timer and raid warnings |
| Bottom left | prompts and status effects |
| Bottom right | ammo, weapon, ability, weight, minimap |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Death-prevention info | health, bleed, ammo empty, extraction timer |
| 2 | Immediate action | prompt, reload, ability ready |
| 3 | Navigation/context | compass, minimap, objective |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| HUD cluster | fixed anchor, safe-zone aware, stable width |
| Warning state | text/icon plus color; no color-only meaning |
| Optional element | can be hidden only if critical override still appears |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Combat | suppress noncritical toasts and tips |
| Low health | health/status cluster promoted |
| Extraction active | timer becomes top-right priority |
| Minimal HUD | critical alerts still break through |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Inspect map | M / click minimap | View button | Tap minimap |
| Use prompt | F / hold | A / Cross | Tap/hold |
| Ping | Middle mouse | D-pad/bumper | Long press |

#### Designer Notes

- Reserve the center for target, cover, projectiles, and operator silhouette.
- Never let changing numbers resize the ammo or timer cluster.

#### Acceptance Checklist

- [ ] Critical clusters are safe-zone aware on PC, console, and mobile.
- [ ] Minimal/custom HUD still shows lethal warnings.

### Element-Level Requirements

| Element | Anatomy | Visibility Rule | Failure / Edge State | Platform Behavior |
| :--- | :--- | :--- | :--- | :--- |
| Health and Armor | body HP, armor durability, injury icons | always visible in combat and damage states | broken armor, bleed, fracture, downed | mobile uses compact stacked bars |
| Stamina | current stamina, exhaustion marker | fades when full and safe | exhausted, overweight, sprint locked | mobile keeps near movement controls |
| Ammo and Weapon | magazine, reserve, fire mode, weapon name | always visible during weapon-ready state | empty, jammed, wrong ammo, reload blocked | console adds button hint for reload |
| Minimap | player, extracts, squad pings, noise-safe markers | optional but extraction warning overrides | jammed, no intel, map disabled | mobile can expand from corner |
| Compass | heading, pings, objective tick | visible while moving/aiming | jammed or objective hidden | mobile uses shortened ticks |
| Extraction Timer | raid time, extraction countdown, overtime | always visible under 5 minutes or extracting | timer critical, extract blocked | enlarged warning on mobile |
| Squad Panel | teammate HP, role, distance, downed state | visible in squad modes | disconnected, downed, dead, muted | collapsible on mobile |
| Interaction Prompt | input, action verb, hold/tap, risk/noise | appears only when actionable | blocked, locked, noisy, inventory full | touch prompt must be tappable |
| Weight Indicator | current/max, penalty tier | visible when looting or overweight | overweight, movement penalty, cannot sprint | pinned near inventory on mobile |

### HUD QA Checklist

- [ ] Every HUD element has a stable anchor and does not shift when values change.
- [ ] Every warning has a text/icon fallback beyond color.
- [ ] Combat, looting, extraction, downed, jammed, and mobile condensed states are represented.
- [ ] Optional HUD customization cannot hide death-prevention alerts.

---

## HUD Production State Matrix

| Element | Normal | Warning | Critical / Error | Offline / Reconnect | Accessibility Requirement |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Health / armor | current values and armor zone | low HP, armor damaged | downed, bleed, armor broken | reconnect banner overrides non-critical motion | text/icon plus color |
| Ammo / weapon | ammo, fire mode, weapon name | low ammo, reload needed | empty, jam/broken if supported | weapon action disabled while reconnecting | audio + icon + number |
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

- Critical HUD states must remain visible over maps, looting, pause, spectator, and reconnect surfaces.
- Combat feedback cannot rely on color alone.
- HUD customization cannot hide required raid outcome or extraction consequence states.
- Mobile HUD must preserve touch-safe combat center and avoid overlapping fire/aim controls.

## Performance Budget

### HUD Rendering Rules

| Metric | Budget | Enforcement |
| :----- | :----- | :---------- |
| Draw calls (HUD total) | Maximum 50 per frame | Batch all HUD elements into 3 texture atlases |
| Update frequency (health, ammo) | Every frame (critical elements) | Direct binding to game state |
| Update frequency (minimap) | Every 3 frames | Reduces GPU cost of minimap rendering |
| Update frequency (kill feed, notifications) | Event-driven only | No per-frame polling — triggered by game events |
| Memory (HUD textures) | Maximum 32MB | Single 2048x2048 atlas for icons + elements |
| Overdraw | Maximum 2x for HUD region | Semi-transparent elements use pre-multiplied alpha |

### Platform-Specific HUD FPS Targets

| Platform | HUD Rendering Target | Notes |
| :------- | :------------------- | :---- |
| PC | Matches game FPS (up to 144) | HUD animations scale with delta time |
| Console | 60 FPS | HUD never drops below game FPS |
| Mobile | 60 FPS target, 30 FPS minimum | Simplified HUD shader on low-end devices |
