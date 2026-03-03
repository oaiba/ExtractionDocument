---
title: "User Interface Visual Design"
type: docs
weight: 4
---

## UI Design Philosophy

The UI visual design supports the **Cyberpunk Neo-Industrial** art direction. Interfaces feel like military-grade tech terminals — dark panels with neon accent borders, holographic-style overlays, and crisp typography. The design must work seamlessly across **PC, Console, and Mobile**.

**Cross-Platform Principles:**

| Principle | PC | Console | Mobile |
| :-------- | :- | :------ | :----- |
| Primary Input | Mouse + Keyboard | Gamepad | Touch |
| Interaction Model | Click, hover, scroll wheel | D-pad focus, face buttons | Tap, swipe, long-press |
| Information Density | High (small text OK) | Medium (living room distance) | Low (thumb zone priority) |
| Min Touch Target | N/A | 44x44 dp (focus highlight) | 48x48 dp (Apple HIG + buffer) |
| Button Spacing | 8px minimum | 12px minimum | 16px minimum |

**Design Hierarchy:**
1. **Readability** — Information is instantly scannable
2. **Consistency** — Every screen uses the same component library
3. **Feedback** — Every interaction has visual + audio confirmation
4. **Cyberpunk Identity** — Orange-cyan accents, dark panels, subtle tech effects

---

## UI Visual Style

### Panel Design

**Base Panel:**

| Property | Value |
| :------- | :---- |
| Background | Void Black (#0A0A0B) at 85% opacity |
| Border | 1px solid, color varies by context |
| Border Color (default) | Steel (#374151) |
| Border Color (active) | Signal Orange (#F97316) or Tactical Cyan (#06B6D4) |
| Corner Radius | 4px (sharp, tactical) |
| Inner Glow | Subtle 2px glow matching border color at 15% opacity |
| Backdrop Blur | 8px Gaussian (PC/Console), 4px (Mobile), disabled on Low settings |

**Cyberpunk Panel Effects:**
- Panels have a faint **scan line overlay** (horizontal lines at 1% opacity)
- On appearance, panels play a brief **digital glitch** animation (50ms RGB shift)
- Critical panels (danger warnings, extraction) pulse their border color slowly (2s cycle)

<!-- REF_IMAGE: UI panel design system — showing default, active, critical, and disabled panel states with border colors and glow effects -->

### Button Design

**Standard Button:**

| State | Background | Border | Text Color | Effect |
| :---- | :--------- | :----- | :--------- | :----- |
| Default | #1E293B | #374151 (1px) | #F8FAFC (white) | None |
| Hover / Focus | #1E293B | #F97316 (orange, 2px) | #F97316 | Subtle glow |
| Pressed | #F97316 (orange fill) | #F97316 (2px) | #0A0A0B (black) | Brief flash |
| Disabled | #111827 | #1F2937 (1px) | #4B5563 (gray) | 50% opacity |

**Primary Action Button (CTA):**

| State | Background | Border | Text | Effect |
| :---- | :--------- | :----- | :--- | :----- |
| Default | Gradient: #F97316 → #EA580C | None | #0A0A0B (black, bold) | Subtle pulse glow |
| Hover / Focus | Solid #FB923C (lighter) | #FDBA74 (1px) | #0A0A0B | Expanded glow |
| Pressed | Solid #C2410C (darker) | None | #F8FAFC (white) | Compress effect |

**Button Sizes:**

| Size | Min Width | Height | Font Size | Usage |
| :--- | :-------- | :----- | :-------- | :---- |
| Small | 80px | 32px | 12px | Filters, secondary actions |
| Medium | 120px | 40px | 14px | Standard interactions |
| Large | 200px | 48px | 16px | Primary actions (PLAY, DEPLOY) |
| Full-Width | 100% parent | 56px | 18px | Mobile primary actions |

### Typography

| Element | Font | Weight | Size | Color | Tracking |
| :------ | :--- | :----- | :--- | :---- | :------- |
| Screen Title | Oxanium | Bold | 28px | #F8FAFC | +2% |
| Section Header | Oxanium | Semi-Bold | 20px | #F8FAFC | +1% |
| Body Text | Inter | Regular | 14px | #CBD5E1 | 0% |
| Label | Inter | Medium | 12px | #94A3B8 | +1% |
| Value / Number | JetBrains Mono | Bold | 16px | #F8FAFC | 0% |
| Currency / Price | JetBrains Mono | Bold | 18px | #FBBF24 | 0% |
| Alert Text | Inter | Bold | 14px | #EF4444 | +1% |

### Icon Design

| Property | Specification |
| :------- | :------------ |
| Style | Line art, consistent 2px stroke width |
| Min size | 24x24 px (never smaller) |
| Color (default) | #94A3B8 (muted gray) |
| Color (active) | #F97316 (orange) or #06B6D4 (cyan) |
| Color (alert) | #EF4444 (red) |
| Category fills | Weapon icons: outlined. Status icons: filled. Navigation: outlined |

---

## Control Standards by Platform

### PC (Keyboard + Mouse)

- Hotkey bindings for all major screens (I = Inventory, M = Map, TAB = Scoreboard, ESC = Menu)
- Cursor-based interactions: click, drag-and-drop, right-click context menus
- Scroll wheel for lists, zoom on map
- Tooltip popups on hover (200ms delay)
- Scalable UI: 80%-150% scaling for 1080p to 4K displays

### Console (Gamepad)

- **D-pad** navigation with visible focus highlight (orange border, 2px)
- **Face buttons** for primary actions (A/X = Select, B/Circle = Back, Y/Triangle = Context, X/Square = Alt Action)
- **Bumpers** for tab switching (LB/RB cycle through screen tabs)
- **Triggers** for quick actions (RT = Confirm in menus, LT = Quick-sell)
- Radial menus for item selection (hold button + analog stick direction)
- Safe zone margins for TV overscan (configurable in Settings)

### Mobile (Touch)

- **Touch targets**: minimum 48x48 dp with 16px spacing
- **Swipe gestures**: swipe to dismiss notifications, swipe between tabs
- **Long-press**: context menu on items (inspect, equip, sell)
- **Drag-and-drop**: inventory management with ghost item preview
- **Customizable HUD layout**: players can drag and reposition HUD elements
- **Auto-hide controls**: buttons fade to 40% opacity when not in use
- **Gyroscope aiming**: toggle in Settings

---

## Main Menu and Screens

### Home Screen (The Hub)

```
┌─────────────────────────────────────────┐
│ [Logo]                      [Settings]  │
│ [Season Pass]               [Profile]   │
│                                         │
│   ┌───────────────────────────────┐     │
│   │     Operator 3D Preview       │     │  3D model with
│   │       [Character Model]       │     │  cyberpunk lighting
│   │    Neon orange rim light      │     │
│   └───────────────────────────────┘     │
│                                         │
│        [====  DEPLOY  ====]             │  Large CTA button
│                                         │  (orange gradient, pulse)
│   [Loadout]  [Stash]  [Traders]         │  Secondary navigation
│                                         │
│   ┌──────────────┐  ┌──────────────┐    │
│   │ Daily Reward  │  │   News /     │    │  Info panels
│   │  [Claim]      │  │   Events     │    │
│   └──────────────┘  └──────────────┘    │
│                                         │
│   [Squad]   [Shop]   [Battle Pass]      │  Tertiary navigation
└─────────────────────────────────────────┘
```

**Cyberpunk Visual Treatment:**
- Background: darkened 3D scene of the Safe House with neon ambient lighting
- Operator preview: full 3D model with orange rim light, cyan fill light
- Deploy button: orange gradient with slow pulse animation and subtle particle effect
- Panel borders: thin orange or cyan lines with soft inner glow
- Transition: screen elements slide in with brief glitch effect on load

<!-- REF_IMAGE: Home screen high-fidelity mockup — showing operator preview with cyberpunk lighting, orange deploy button, and dark panel layout -->

### Loadout Screen

```
┌─────────────────────────────────────────┐
│ <- Back          LOADOUT         [Save] │
│                                         │
│ Operator: ASSAULT       [Change Class]  │
│                                         │
│ ┌────────────────┐  ┌────────────────┐  │
│ │ Primary Weapon │  │  Weapon Stats  │  │
│ │ ┌────────────┐ │  │  DMG:  35      │  │
│ │ │  [Weapon   │ │  │  RPM:  650     │  │
│ │ │   Image]   │ │  │  Range: 80m    │  │
│ │ └────────────┘ │  │  Recoil: Med   │  │
│ │  AK-74M  [Edit]│  └────────────────┘  │
│ └────────────────┘                      │
│                                         │
│ Secondary:  Glock-19         [Edit]     │
│ Armor:      Level 3 Vest     [Edit]     │
│ Rig:        Tactical 8-slot  [Edit]     │
│                                         │
│ Equipment:  [Frag] [Medkit] [  +  ]     │
│                                         │
│ Insurance:  [Insure All - $2,400]       │
│                                         │
│ Gear Value: $15,250   Weight: 24.5 kg   │
│             Risk: MEDIUM                │
│                                         │
│      [Save Preset]    [DEPLOY]          │
└─────────────────────────────────────────┘
```

**Visual Notes:**
- Weapon images rendered in real-time 3D with cyberpunk lighting
- Stats displayed in monospace font (JetBrains Mono) for clean alignment
- Risk indicator uses color coding: Low (green), Medium (amber), High (red), Extreme (pulsing red)
- Insurance button has cyan border — optional but recommended UI pattern

### Stash / Inventory Screen

```
┌─────────────────────────────────────────┐
│ <- Back          STASH                  │
│ [Filter v]  [Sort v]  [Search...]       │
│                                         │
│ ┌────────────────────────────────────┐  │
│ │ ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐  │  │
│ │ │██│  │██│  │  │  │  │  │  │  │  │  │
│ │ ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤  │  │
│ │ │██│  │██│  │  │  │  │  │  │  │  │  │  Grid inventory
│ │ ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤  │  │  (drag and drop)
│ │ │  │  │  │  │  │  │  │  │  │  │  │  │
│ │ ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤  │  │
│ │ │  │  │  │  │  │  │  │  │  │  │  │  │
│ │ └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘  │  │
│ └────────────────────────────────────┘  │
│                                         │
│ Selected:                               │
│ ┌──────────────┐                        │
│ │  [Item Img]  │  AK-74M                │
│ │              │  Rarity: Rare (blue)    │
│ │              │  DMG: 35 | RPM: 650    │
│ └──────────────┘  Value: $2,500         │
│                                         │
│ [Equip]  [Sell]  [Inspect]  [Insure]    │
│                                         │
│ Capacity: 145/200 slots                 │
│ Total Value: $125,430                   │
└─────────────────────────────────────────┘
```

**Visual Notes:**
- Item cells have rarity-colored borders (thin, 1px)
- Drag-and-drop on PC/Mobile, cursor-select on Console
- Empty cells: dark grid pattern with subtle scan line texture
- Hover/focus: orange border highlight + item name tooltip
- New items: pulsing border + "NEW" badge

---

## In-Game HUD

### Core HUD Layout

For detailed functional specifications, see [HUD Design](../../UI_UX/HUD_Design/).

```
┌─────────────────────────────────────────┐
│ ███ Health                              │  Top-left: Status
│ ███ Armor              12:45            │  Top-right: Timer
│ ███ Stamina          12 Players         │
│                                         │
│                    ┌───────────┐        │
│                    │  Minimap  │        │  Minimap
│                    └───────────┘        │
│                                         │
│              +                          │  Crosshair
│                                         │
│                          ┌──────────┐   │
│                          │ Loot     │   │  Notifications
│                          │ Found!   │   │  (right side)
│                          └──────────┘   │
│                                         │
│ [Move]              30/30  [R]  [Fire]  │  Bottom: Controls
│ [Crouch]       [Reload] [Swap] [Inv]    │  (Mobile layout)
└─────────────────────────────────────────┘
```

**HUD Visual Treatment:**
- All HUD elements use semi-transparent dark panels (#0A0A0B at 70%)
- Status bars: segmented, bright colors against dark background
- Minimap: circular, dark background, orange player marker, cyan teammate markers
- Text: Inter font, white with black text shadow for readability on any background

### Health and Status Bars

| Bar | Color | Style | Size | Animation |
| :-- | :---- | :---- | :--- | :-------- |
| Health | Red #DC2626 | Segmented (10 chunks) | 200x20 px | Smooth depletion, flash white on damage |
| Armor | Cyan #06B6D4 | Segmented (matches health) | 200x16 px | Depletes before health |
| Stamina | Amber #FBBF24 | Solid continuous bar | 200x8 px | Auto-hides when full, pulses when low |

### Ammo Counter

**Position:** Bottom-right (near fire button on Mobile, screen corner on PC/Console)

```
    30     ← Current magazine (large, bold)
   ───
   120     ← Reserve ammo (smaller, muted)
```

| State | Text Color | Extra |
| :---- | :--------- | :---- |
| Normal (>30%) | White #F8FAFC | None |
| Low (<10 rounds) | Amber #FBBF24 | None |
| Empty | Red #EF4444 | "RELOAD" text flash + warning icon |
| Reloading | Cyan #06B6D4 | Circular progress indicator |

### Crosshair

**Position:** Screen center  
**Style:** Minimal, tactical, cyberpunk-influenced

| State | Visual | Color |
| :---- | :----- | :---- |
| Default | 4-line cross with center gap | White #F8FAFC |
| Aiming (tighter) | Smaller cross, thinner lines | White |
| Enemy in sights | Same cross, color shift | Red #EF4444 |
| Friendly in sights | Same cross, color shift | Cyan #06B6D4 |
| Spread indicator | Cross lines expand with distance | White, lines scale |

**Customization Options:**
- Color: white, green, cyan, red, orange (user choice)
- Size: small, medium, large
- Style: cross, dot, circle, dot-cross hybrid
- Opacity: 50%-100%
- Dynamic spread: On/Off

---

## Post-Match Screens

### Extraction Success

```
┌─────────────────────────────────────────┐
│            ★ EXTRACTED ★                │  Title: gold text,
│                                         │  neon glow
│   ┌───────────────────────────────┐     │
│   │    Operator Victory Pose      │     │  3D Model with
│   │     (cyberpunk lighting)      │     │  orange rim light
│   └───────────────────────────────┘     │
│                                         │
│  Loot Extracted:                        │
│  ┌─────────────────────────────────┐    │
│  │ [Icon] AK-74M          $2,500  │    │  Scrolling list
│  │ [Icon] 5.45 Ammo x120    $240  │    │  (rarity borders)
│  │ [Icon] Med Kit x2         $400  │    │
│  │ [Icon] Lab Keycard      $8,000  │    │  Rare items glow
│  └─────────────────────────────────┘    │
│  Total Value: $11,140                   │
│                                         │
│  ┌────────┬─────────┬──────────┐        │
│  │ XP     │  Kills  │  Time    │        │  Stats
│  │ +1,250 │    3    │  12:34   │        │
│  └────────┴─────────┴──────────┘        │
│                                         │
│  [Continue]          [Deploy Again]     │
└─────────────────────────────────────────┘
```

**Animations:**
- Loot icons fly in from left one by one
- Rare items have glow pulse on reveal
- XP bar fills with satisfying progress sound
- Total value counter animates (counting up)
- Victory music: cyberpunk synth with triumphant brass

### Elimination (Death)

```
┌─────────────────────────────────────────┐
│            ELIMINATED                   │  Title: red text,
│                                         │  glitch effect
│  Killed by: PlayerXYZ                   │
│  Weapon: AK-74M                        │
│  Distance: 45m                          │
│                                         │
│  Items Lost:                            │
│  ┌─────────────────────────────────┐    │
│  │ [Icon] AK-74M (grayed)  $2,500 │    │  Grayed-out icons
│  │ [Icon] Armor Vest        $1,200 │    │  (lost items)
│  │ [Icon] 5.45 Ammo x90      $180 │    │
│  └─────────────────────────────────┘    │
│  Value Lost: $3,880                     │
│                                         │
│  Secure Container Saved:                │
│  [Icon] Lab Keycard          $8,000     │  Green highlight
│                                         │
│  ┌────────┬─────────┬──────────┐        │
│  │ XP     │  Kills  │  Time    │        │  Consolation
│  │  +250  │    1    │  7:23    │        │  stats
│  └────────┴─────────┴──────────┘        │
│                                         │
│  [Replay Death]      [Deploy Again]     │
└─────────────────────────────────────────┘
```

**Visual Treatment:**
- Screen briefly glitches (500ms) before death screen appears
- Lost items displayed with desaturated icons and strikethrough value
- Secure container items highlighted with green border (survived)
- Tone: informative, not punishing — always show what was saved
- Music: somber cyberpunk ambient, no sudden silence

---

## Settings UI Overview

For detailed settings specifications, see [User Settings documentation](../../UserSettings/).

### Settings Panel Layout

```
┌─────────────────────────────────────────┐
│ <- Back          SETTINGS               │
│                                         │
│ [Graphics] [Audio] [Controls]           │  Tab bar
│ [Gameplay] [Accessibility] [Account]    │  (bumpers cycle)
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │                                     │ │
│ │  Setting Group                      │ │
│ │  ├─ Setting Name     [Value    v]   │ │  Content area
│ │  ├─ Setting Name     [Slider ●──]   │ │  (scrollable)
│ │  ├─ Setting Name     [Toggle  ON]   │ │
│ │  └─ Setting Name     [  Button  ]   │ │
│ │                                     │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [Reset to Default]  [Apply]  [Cancel]   │  Action bar
└─────────────────────────────────────────┘
```

**Key Visual Rules:**
- Active tab: orange underline
- Changed settings: amber dot indicator next to setting name (unsaved change)
- Applied settings: brief green flash confirmation
- Sliders: filled portion in orange (#F97316), unfilled in dark gray (#374151)
- Toggles: on = orange (#F97316), off = dark gray (#374151)

---

## Accessibility Features

All UI must meet the following accessibility standards:

| Feature | Implementation |
| :------ | :------------- |
| Colorblind Modes | Deuteranopia, Protanopia, Tritanopia filters. Adjusts UI colors only |
| High Contrast Mode | Increases border visibility, enhances text shadow, boosts icon opacity |
| Text Scaling | 100%-200% without breaking layout (responsive containers) |
| Subtitles | Directional audio indicators for hearing-impaired players |
| Button Remapping | Full customization across all platforms |
| Motion Reduction | Toggle for screen shake, glitch effects, scan lines, and particle density |
| One-Handed Mode | Mobile: simplified layout with larger touch zones on one side |
| Screen Reader | Future feature — semantic UI elements prepared now |

---

## Responsive Design Rules

### Aspect Ratio Support

| Aspect Ratio | Platform | UI Adaptation |
| :----------- | :------- | :------------ |
| 16:9 | PC, Console, Tablet | Default layout |
| 21:9 | Ultrawide PC | Extended peripheral view, anchored UI elements |
| 18:9 / 19.5:9 | Mobile (modern) | Safe zone margins, bottom bar adjusted |
| 4:3 | Older tablets | Centered layout, reduced side panels |

### Safe Zone Margins

| Platform | Top | Bottom | Left | Right |
| :------- | :-- | :----- | :--- | :---- |
| PC | 16px | 16px | 16px | 16px |
| Console | 48px (configurable for TV overscan) | 48px | 48px | 48px |
| Mobile | 24px + notch avoidance | 24px + home bar avoidance | 24px | 24px |

### Performance Targets

| UI Element | Render Budget | Update Frequency | Notes |
| :--------- | :------------ | :--------------- | :---- |
| HUD (in-game) | < 50 draw calls | Every frame | Minimal overdraw |
| Menu screens | < 100 draw calls | On interaction | Lazy load panels |
| Inventory grid | < 80 draw calls | On scroll/drag | Virtualized list |
| Notifications | < 10 draw calls | On event | Pool and reuse |
| Total UI | < 200 draw calls | — | Never exceed |
| Texture budget | 32 MB max | — | Atlas aggressively |

<!-- REF_IMAGE: UI component library sheet — showing buttons, panels, sliders, toggles, tabs, and icons at all states with cyberpunk visual treatment -->
