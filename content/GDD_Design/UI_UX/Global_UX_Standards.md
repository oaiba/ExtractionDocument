---
title: "Global UX Standards"
type: docs
weight: 2
---

## Purpose

Global UX standards define the reusable interaction rules that every UI screen must follow. Screen-specific documents can override these rules only when they explain why the exception improves raid speed, clarity, accessibility, or platform fit.

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Visual Style](Visual_Style.md) | Visual, typography, iconography, and mockup rules |
| [UX Flows](UX_Flows.md) | Journey-level navigation and handoff mapping |
| [Menus & Screens Legacy](Menus.md) | Compatibility mapping for old screen links |

---

## Interaction Principles

| Principle | Rule |
| :--- | :--- |
| Fast path first | Common actions should be reachable in 1-3 inputs from the current context |
| Risk is visible | Gear loss, currency spend, ranked impact, privacy, and destructive actions must be explained before commit |
| One primary action | Each screen has one visually dominant CTA and no competing fake-primary buttons |
| Recoverable mistakes | Non-destructive changes support undo, cancel, or reset |
| Platform parity | Information is equivalent across PC and console using the shared landscape layout standard |
| Pressure-aware UI | In-raid overlays stay readable, dismissible, and audio-transparent |

---

## Navigation And Focus

#### System Diagram

```
+---------------------------------------------------------------+
| BASE SCREEN                                                   |
| Home / Stash / Map / Settings                                 |
|                                                               |
|   +-------------------------------------------------------+   |
|   | OVERLAY                                               |   |
|   | Inventory, tactical map, social panel, pause          |   |
|   |                                                       |   |
|   |     +---------------------------------------------+   |   |
|   |     | MODAL                                       |   |   |
|   |     | Confirm, error, conflict, destructive action|   |   |
|   |     +---------------------------------------------+   |   |
|   +-------------------------------------------------------+   |
|                                                               |
| Toasts / system alerts live above all non-blocking layers     |
+---------------------------------------------------------------+
```

- Back closes the deepest visible layer first.
- Modal decisions block input behind them; toasts do not.
- Focus must return to the control that opened the overlay or modal.

| Topic | Standard |
| :--- | :--- |
| Back navigation | `ESC` and `B/Circle` close the top modal, then overlay, then screen |
| Focus order | Controller and keyboard focus moves left-to-right, top-to-bottom unless the layout has a stronger task order |
| Focus memory | Returning to a screen restores the last selected tab/item when safe |
| Deep links | Deep links open the target state, not just the parent screen |
| Breadcrumbs | Use only in multi-step flows; avoid them on the Home hub and in-raid overlays |
| Disabled actions | Disabled controls must show a reason and a direct fix when possible |

### Standard Focus States

| State | PC | Console |
| :--- | :--- | :--- |
| Hover | Border or surface lift | Not applicable |
| Focused | Visible outline if keyboard active | Persistent high-contrast outline |
| Pressed | 90-95% scale for 100ms | Haptic pulse plus scale |
| Disabled | Reduced opacity plus reason tooltip/sheet | Reduced opacity plus reason on focus |
| Loading | Inline spinner and blocked repeat input | Spinner and focus retained |

---

## Responsive Layout Rules

#### Layout (PC/Console)

```
+-------------------------------------------------------------------+
| GLOBAL HEADER: profile, currency, notifications, search           |
|-------------------------------------------------------------------|
| PRIMARY NAV: Home | Loadout | Stash | Traders | SafeHouse | Quests |
|              Profile | Settings                                   |
|-------------------------------------------------------------------|
| SECONDARY | MAIN CONTENT AREA                         | CONTEXT  |
| RAIL      | selected screen, list, grid, preview      | PANEL    |
| filters   |                                           | details  |
| category  | +------------------+ +------------------+ | risk     |
| list      | | Card / Row       | | Card / Row       | | status   |
| local nav | +------------------+ +------------------+ | CTA      |
|-------------------------------------------------------------------|
| FOOTER: hints, back, focus state, destructive warning if needed   |
+-------------------------------------------------------------------+
```

| Platform | Layout Standard |
| :--- | :--- |
| PC 16:9 | Dense but scannable; preserve a stable horizontal global nav and avoid oversized marketing layouts |
| PC ultrawide | Keep primary content in a centered 1920px-safe region; use side space for context panels only |
| Console | Maintain 5% safe zone, large focus states, and no precision-only interactions |

Mobile-specific and portrait-only layouts are out of scope for this standard. If encountered, block interaction, redirect to supported PC/Console landscape guidance, or show an unsupported-orientation message.

### Navigation Roles

| Role | Standard |
| :--- | :--- |
| Primary navigation | Horizontal global nav in the top header area; used for Home, Loadout, Stash, Traders, Safe House, Quests, Profile, Settings |
| Secondary rail | Vertical left rail only for local categories, filters, sub-sections, or scoped lists inside the current primary destination |
| Local rail examples | Stash filters, operator roster filters, trader list, quest list, settings categories, social/LFG lists |
| Context panel | Right-side detail/risk/status panel that changes with the selected item, screen state, or workflow |
| Action/status bar | Bottom or pinned action strip for hints, destructive warnings, and primary/secondary CTAs |

### Minimum Targets

| Element | Minimum |
| :--- | :--- |
| Interactive target | 44x44 px absolute minimum; 60x60 px preferred for combat-relevant actions |
| Controller focus target | 64 px height for primary list rows |
| Body text | 16 px desktop/console; larger sizes are allowed for readability |
| Critical numbers | Use tabular or monospace digits where values update rapidly |
| Safe margins | 16 px PC, 5% console overscan |

---

## Modal And Dialog Standards

#### Layout (PC/Console)

```
+------------------------------------------------------------------+
| dimmed parent screen                                             |
|                                                                  |
|             +--------------------------------------+             |
|             | CONFIRM DISCARD ITEM                 |             |
|             |--------------------------------------|             |
|             | AK-74M will be removed from stash.   |             |
|             | Value: 45,000 credits                |             |
|             | Quest item: No    Insured: Yes       |             |
|             |                                      |             |
|             | [Cancel]              [Hold Discard] |             |
|             +--------------------------------------+             |
|                                                                  |
+------------------------------------------------------------------+
```

| Dialog Type | Use Case | CTA Rule |
| :--- | :--- | :--- |
| Info | Acknowledgement-only system message | One button: OK / Continue |
| Confirmation | Reversible decision with cost or risk | Primary confirm, secondary cancel |
| Destructive | Abandon raid, discard, spend premium currency, unlink account | Hold confirm or type/second confirmation |
| Conflict | Cloud save/settings conflict | Explain source, timestamp, and choice outcome |
| Error | Network, account, transaction, version mismatch | State what happened, player impact, and next step |

Modal copy must be specific. Use "Discard AK-74M? This removes it from your stash." instead of "Are you sure?"

---

## Standard Screen States

#### State Diagram

```
      +---------+
      | Loading |
      +----+----+
           |
           v
+----------+----------+
| Default Content     |
+----+-----------+----+
     |           |
     v           v
+---------+  +---------+     +---------+
| Empty   |  | Locked  | --> | Fix CTA |
+---------+  +---------+     +---------+
     |
     v
+---------+     +---------+
| Error   | --> | Retry   |
+---------+     +---------+
```

| State | Requirement |
| :--- | :--- |
| Default | Shows useful content and the next action |
| Loading | Keeps layout stable and names what is loading |
| Empty | Explains why there is nothing and offers the best next action |
| Invalid | Shows the exact blocker near the affected control |
| Locked | Shows requirement, progress toward unlock, and shortcut if available |
| Offline | Keeps local-safe actions available and explains unavailable online actions |
| Error | Gives retry, cancel, and support/report path when relevant |
| Success | Confirms the result without trapping the player |

---

## Designer-Ready Screen Rules

These rules apply to every screen, overlay, modal, HUD element, notification, and loading state in the UI/UX package.

| Area | Standard |
| :--- | :--- |
| Layout anatomy | Name the header, primary content, detail/context panel, warning lane, and action bar where they exist |
| CTA priority | One primary action per state; secondary actions must not visually compete with it |
| Disabled reasons | Disabled CTAs must name the first blocker and provide a route when available |
| Warning lanes | Warnings appear near the action they affect and do not shift primary CTA placement |
| Focus order | Define keyboard/controller focus from primary task to secondary actions to utility controls |
| Touch fallback | Mobile/touch layouts need reachable primary CTA, generous targets, and alternatives to precision drag |
| State language | Use readable labels such as Ready, Locked, Offline, Expired, Full, Blocked, and Pending |
| Destructive actions | Sell, discard, abandon, unlink, delete, spend, overwrite, kick, block, and report require consequence copy |
| Icon usage | Icons support scan speed but never carry meaning alone |
| ASCII translation | ASCII wireframes define information architecture, not final art direction |

### Standard Designer-Ready Section Set

Every screen group detail should include: `Player Intent`, `Expanded ASCII Wireframe`, `Layout Anatomy`, `Visual Hierarchy`, `Component Requirements`, `States & Edge Cases`, `Input / Focus / Touch`, `Designer Notes`, and `Acceptance Checklist`.

---

## Accessibility Baseline

| Area | Standard |
| :--- | :--- |
| Color | Do not encode meaning by color alone; pair color with icon, label, shape, or pattern |
| Contrast | Meet WCAG 2.1 AA for all text and critical icons |
| Text scale | Support 100-200% without clipping primary actions |
| Motion | Respect reduce-motion; replace long animation with fade or instant state change |
| Timing | Hold-to-confirm and timed prompts need adjustable duration where feasible |
| Screen reader | All buttons, tabs, list items, and alerts need descriptive labels |
| Input assist | Provide alternate button paths to hold actions where motor accessibility requires it |

---

## Analytics Events

| Event | Parameters |
| :--- | :--- |
| `UI_SCREEN_OPEN` | screen, source, platform, input_method |
| `UI_SCREEN_CLOSE` | screen, duration, exit_reason |
| `UI_CTA_PRESS` | screen, cta_id, valid_state |
| `UI_BLOCKED_ACTION` | screen, action, blocker_id |
| `UI_ERROR_SHOWN` | screen, error_code, retry_available |
| `UI_SETTINGS_CHANGED` | category, setting_id, old_value, new_value, source |
| `UI_DEEP_LINK_USED` | source_screen, target_screen, target_state |

---

## Acceptance Checklist

- [ ] Back behavior is defined for keyboard and controller.
- [ ] Portrait/mobile-specific layouts are blocked, redirected to PC/Console landscape guidance, or show an unsupported-orientation message.
- [ ] Primary CTA is obvious and has disabled/error behavior.
- [ ] Every destructive action has a confirmation standard.
- [ ] Empty, locked, offline, loading, and error states are specified.
- [ ] Text survives 200% scaling without hiding primary actions.
- [ ] Colorblind mode has non-color meaning for critical status.
- [ ] Analytics events capture drop-off and blocker reasons.
