---
title: "Global UX Standards"
type: docs
weight: 2
---

## Purpose

Global UX standards define the reusable interaction rules that every UI screen must follow. Screen-specific documents can override these rules only when they explain why the exception improves raid speed, clarity, accessibility, or platform fit.

---

## Interaction Principles

| Principle | Rule |
| :--- | :--- |
| Fast path first | Common actions should be reachable in 1-3 inputs from the current context |
| Risk is visible | Gear loss, currency spend, ranked impact, privacy, and destructive actions must be explained before commit |
| One primary action | Each screen has one visually dominant CTA and no competing fake-primary buttons |
| Recoverable mistakes | Non-destructive changes support undo, cancel, or reset |
| Platform parity | Information is equivalent across PC, console, and mobile even when layout differs |
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
| Back navigation | `ESC`, `B/Circle`, and mobile system back close the top modal, then overlay, then screen |
| Focus order | Controller and keyboard focus moves left-to-right, top-to-bottom unless the layout has a stronger task order |
| Focus memory | Returning to a screen restores the last selected tab/item when safe |
| Deep links | Deep links open the target state, not just the parent screen |
| Breadcrumbs | Use only in multi-step flows; avoid them on the Home hub and in-raid overlays |
| Disabled actions | Disabled controls must show a reason and a direct fix when possible |

### Standard Focus States

| State | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Hover | Border or surface lift | Not applicable | Not applicable |
| Focused | Visible outline if keyboard active | Persistent high-contrast outline | Press ripple or selected chip |
| Pressed | 90-95% scale for 100ms | Haptic pulse plus scale | Haptic pulse plus ripple |
| Disabled | Reduced opacity plus reason tooltip/sheet | Reduced opacity plus reason on focus | Reduced opacity plus reason on tap |
| Loading | Inline spinner and blocked repeat input | Spinner and focus retained | Spinner and touch disabled for that control |

---

## Responsive Layout Rules

#### Layout (PC/Console)

```
+-------------------------------------------------------------------+
| TOP BAR: profile, currency, notifications, search                 |
|-------------------------------------------------------------------|
| NAV RAIL | MAIN CONTENT AREA                           | CONTEXT  |
|          | selected screen, list, grid, preview        | PANEL    |
| Home     |                                             | details  |
| Loadout  | +------------------+ +------------------+   | risk     |
| Stash    | | Card / Row       | | Card / Row       |   | status   |
| Social   | +------------------+ +------------------+   | CTA      |
| Settings |                                             |          |
|-------------------------------------------------------------------|
| FOOTER: hints, back, focus state, destructive warning if needed   |
+-------------------------------------------------------------------+
```

#### Layout (Mobile Portrait)

```
+-----------------------------+
| Top: profile / currency     |
|-----------------------------|
| Screen title        [Action]|
|-----------------------------|
| Main content list / cards   |
|                             |
| +-------------------------+ |
| | selected item or state  | |
| +-------------------------+ |
|                             |
| Sticky summary / warning    |
| [ Primary CTA ]             |
|-----------------------------|
| Home Loadout Stash Social   |
+-----------------------------+
```

| Platform | Layout Standard |
| :--- | :--- |
| PC 16:9 | Dense but scannable; preserve stable navigation rail and avoid oversized marketing layouts |
| PC ultrawide | Keep primary content in a centered 1920px-safe region; use side space for context panels only |
| Console | Maintain 5% safe zone, large focus states, and no precision-only interactions |
| Mobile portrait | Thumb-first vertical flow, persistent bottom action where commitment is likely |
| Mobile landscape | Prioritize gameplay visibility and avoid covering both thumb zones |
| Tablet | Use split panels when readable; do not simply scale phone layouts |

### Minimum Targets

| Element | Minimum |
| :--- | :--- |
| Touch target | 44x44 px absolute minimum; 60x60 px preferred for combat-relevant actions |
| Controller focus target | 64 px height for primary list rows |
| Body text | 16 px desktop/console, 18 px mobile where space allows |
| Critical numbers | Use tabular or monospace digits where values update rapidly |
| Safe margins | 16 px PC, 5% console overscan, platform safe area on mobile |

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

## Accessibility Baseline

| Area | Standard |
| :--- | :--- |
| Color | Do not encode meaning by color alone; pair color with icon, label, shape, or pattern |
| Contrast | Meet WCAG 2.1 AA for all text and critical icons |
| Text scale | Support 100-200% without clipping primary actions |
| Motion | Respect reduce-motion; replace long animation with fade or instant state change |
| Timing | Hold-to-confirm and timed prompts need adjustable duration where feasible |
| Screen reader | All buttons, tabs, list items, and alerts need descriptive labels |
| Input assist | Provide tap alternatives to hold actions where motor accessibility requires it |

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

- [ ] Back behavior is defined for keyboard, controller, and mobile.
- [ ] Primary CTA is obvious and has disabled/error behavior.
- [ ] Every destructive action has a confirmation standard.
- [ ] Empty, locked, offline, loading, and error states are specified.
- [ ] Text survives 200% scaling without hiding primary actions.
- [ ] Colorblind mode has non-color meaning for critical status.
- [ ] Analytics events capture drop-off and blocker reasons.
