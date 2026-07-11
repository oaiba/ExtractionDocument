---
title: "Global UX Standards"
type: docs
weight: 2
---

## Purpose

Global UX standards định nghĩa các interaction rules tái sử dụng mà mọi UI screen phải tuân theo. Screen-specific documents chỉ được override khi giải thích rõ exception đó cải thiện raid speed, clarity, accessibility, hoặc platform fit.

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Hub tài liệu UI/UX đầy đủ |
| [Screen Groups Overview](screen_groups_overview/index.html) | Lifecycle taxonomy và designer-ready spec template |
| [Visual Style](visual_style/index.html) | Rule visual, typography, iconography, mockup |
| [UX Flows](ux_flows/index.html) | Journey-level navigation và handoff mapping |
| [Menus & Screens Legacy](menus/index.html) | Compatibility mapping cho old screen links |

---

## Interaction Principles

| Principle | Rule |
| :--- | :--- |
| Fast path first | Common actions nên reachable trong 1-3 input từ context hiện tại |
| Risk is visible | Gear loss, currency spend, ranked impact, privacy, destructive actions phải explained trước commit |
| One primary action | Mỗi screen có một CTA visually dominant và không có fake-primary cạnh tranh |
| Recoverable mistakes | Non-destructive changes support undo, cancel, hoặc reset |
| Platform parity | Information tương đương trên PC và console bằng shared landscape layout standard |
| Pressure-aware UI | In-raid overlays readable, dismissible, và audio-transparent |

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

- Back đóng deepest visible layer trước.
- Modal decision block input phía sau; toast thì không.
- Focus phải quay lại control đã mở overlay hoặc modal.

| Topic | Standard |
| :--- | :--- |
| Back navigation | `ESC` và `B/Circle` đóng top modal, rồi overlay, rồi screen |
| Focus order | Controller/keyboard focus đi left-to-right, top-to-bottom trừ khi task order mạnh hơn |
| Focus memory | Quay lại screen sẽ restore tab/item cuối khi an toàn |
| Deep links | Deep link mở target state, không chỉ parent screen |
| Breadcrumbs | Chỉ dùng trong multi-step flows; tránh trên Home hub và in-raid overlays |
| Disabled actions | Disabled controls phải show reason và direct fix khi có thể |

### Standard Focus States

| State | PC | Console |
| :--- | :--- | :--- |
| Hover | Border or surface lift | Not applicable |
| Focused | Visible outline nếu keyboard active | Persistent high-contrast outline |
| Pressed | 90-95% scale for 100ms | Haptic pulse plus scale |
| Disabled | Reduced opacity plus reason tooltip/sheet | Reduced opacity plus reason on focus |
| Loading | Inline spinner and blocked repeat input | Spinner and focus retained |

---

## Responsive Layout Rules

Layout (PC/Console)

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
| PC 16:9 | Dense nhưng scannable; giữ horizontal global nav ổn định và tránh oversized marketing layouts |
| PC ultrawide | Giữ primary content trong vùng centered 1920px-safe; side space chỉ dùng cho context panels |
| Console | Giữ 5% safe zone, focus state lớn, không dùng precision-only interaction |

Mobile-specific và portrait-only layouts nằm ngoài scope standard này. Nếu gặp, block interaction, redirect tới PC/Console landscape guidance, hoặc show unsupported-orientation message.

### Navigation Roles

| Role | Standard |
| :--- | :--- |
| Primary navigation | Horizontal global nav trong top header area; dùng cho Home, Loadout, Stash, Traders, Safe House, Quests, Profile, Settings |
| Secondary rail | Vertical left rail chỉ dùng cho local categories, filters, sub-sections, scoped lists trong primary destination hiện tại |
| Local rail examples | Stash filters, operator roster filters, trader list, quest list, settings categories, social/LFG lists |
| Context panel | Right-side detail/risk/status panel thay đổi theo selected item, screen state, hoặc workflow |
| Action/status bar | Bottom hoặc pinned action strip cho hints, destructive warnings, primary/secondary CTAs |

### Minimum Targets

| Element | Minimum |
| :--- | :--- |
| Interactive target | 44x44 px absolute minimum; 60x60 px preferred cho combat-relevant actions |
| Controller focus target | 64 px height cho primary list rows |
| Body text | 16 px desktop/console; size lớn hơn được phép để readable |
| Critical numbers | Dùng tabular hoặc monospace digits khi value update nhanh |
| Safe margins | 16 px PC, 5% console overscan |

---

## Modal And Dialog Standards

Layout (PC/Console)

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
| Confirmation | Reversible decision có cost/risk | Primary confirm, secondary cancel |
| Destructive | Abandon raid, discard, spend premium currency, unlink account | Hold confirm hoặc type/second confirmation |
| Conflict | Cloud save/settings conflict | Explain source, timestamp, choice outcome |
| Error | Network, account, transaction, version mismatch | State what happened, player impact, next step |

Modal copy phải cụ thể. Dùng "Discard AK-74M? This removes it from your stash." thay vì "Are you sure?"

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
| Default | Show useful content và next action |
| Loading | Giữ layout stable và nêu thứ đang loading |
| Empty | Giải thích vì sao không có gì và offer best next action |
| Invalid | Show exact blocker gần affected control |
| Locked | Show requirement, progress toward unlock, shortcut nếu có |
| Offline | Giữ local-safe actions available và giải thích online actions unavailable |
| Error | Có retry, cancel, support/report path khi relevant |
| Success | Confirm result mà không trap player |

---

## Designer-Ready Screen Rules

Các rule này áp dụng cho mọi screen, overlay, modal, HUD element, notification, và loading state trong UI/UX package.

| Area | Standard |
| :--- | :--- |
| Layout anatomy | Nêu header, primary content, detail/context panel, warning lane, action bar nơi có |
| CTA priority | Một primary action mỗi state; secondary actions không visually compete |
| Disabled reasons | Disabled CTA phải nêu blocker đầu tiên và route khi có |
| Warning lanes | Warning xuất hiện gần action bị ảnh hưởng và không shift primary CTA placement |
| Focus order | Define keyboard/controller focus từ primary task tới secondary actions tới utility controls |
| Touch fallback | Touch layout cần primary CTA reachable, target rộng, alternative cho precision drag |
| State language | Dùng label readable như Ready, Locked, Offline, Expired, Full, Blocked, Pending |
| Destructive actions | Sell, discard, abandon, unlink, delete, spend, overwrite, kick, block, report cần consequence copy |
| Icon usage | Icon hỗ trợ scan speed nhưng không mang meaning một mình |
| ASCII translation | ASCII wireframe định nghĩa information architecture, không phải final art direction |

### Standard Designer-Ready Section Set

Mọi screen group detail nên gồm: `Player Intent`, `Expanded ASCII Wireframe`, `Layout Anatomy`, `Visual Hierarchy`, `Component Requirements`, `States & Edge Cases`, `Input / Focus / Touch`, `Designer Notes`, và `Acceptance Checklist`.

---

## Accessibility Baseline

| Area | Standard |
| :--- | :--- |
| Color | Không encode meaning bằng color alone; pair color với icon, label, shape, pattern |
| Contrast | Meet WCAG 2.1 AA cho mọi text và critical icons |
| Text scale | Support 100-200% không clip primary actions |
| Motion | Respect reduce-motion; thay long animation bằng fade hoặc instant state change |
| Timing | Hold-to-confirm và timed prompts cần adjustable duration khi feasible |
| Screen reader | Mọi button, tab, list item, alert cần descriptive labels |
| Input assist | Provide alternate button paths cho hold actions khi motor accessibility yêu cầu |

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

- [ ] Back behavior được define cho keyboard và controller.
- [ ] Portrait/mobile-specific layouts được block, redirect tới PC/Console landscape guidance, hoặc show unsupported-orientation message.
- [ ] Primary CTA rõ và có disabled/error behavior.
- [ ] Mọi destructive action có confirmation standard.
- [ ] Empty, locked, offline, loading, error states được specify.
- [ ] Text sống được 200% scaling mà không hide primary actions.
- [ ] Colorblind mode có non-color meaning cho critical status.
- [ ] Analytics events capture drop-off và blocker reasons.
