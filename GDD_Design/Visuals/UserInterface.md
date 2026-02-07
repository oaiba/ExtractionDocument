# User Interface

**[← Previous: Art Direction](./ArtDirection.md)** | **[Index](../README.md)** | **[Next: Sound Design →](../Audio/SoundDesign.md)**

---

## UI Design Philosophy

**Mobile-First Principles:**
1. **Thumb-Friendly** - Controls within reach
2. **Clear Hierarchy** - Important info stands out
3. **Minimalist** - Not cluttered
4. **Responsive** - Instant feedback
5. **Accessible** - Readable, colorblind-safe

---

## Touch Control Standards

### Minimum Touch Targets

**Button Sizes:**
- Small buttons: 60x60 px (minimum)
- Medium buttons: 80x80 px (recommended)
- Large buttons: 100x100 px (primary actions)
- Touch zones: +20px padding around visual

**Spacing:**
- Between buttons: 16px minimum
- Screen edges: 24px margin
- Grouped elements: 8px gap

---

### Control Zones

```
┌─────────────────────────────┐
│  [HP][Stamina]    [Timer]   │ Top (Status)
│                  [Players]  │
│                             │
│     [Minimap]               │ Top-Right (Info)
│                             │
│                             │ Center (Gameplay)
│         [Crosshair]         │
│                             │
│                             │
│ [Joystick]      [Fire Btn]  │ Bottom (Controls)
│ [Crouch]    [Reload][Swap]  │
│ [Interact]     [Inventory]  │
└─────────────────────────────┘
```

**Thumb Zones:**
- Left thumb: Movement, crouch, interact
- Right thumb: Fire, reload, swap, inventory
- Top: Non-critical info only (no buttons)

---

## Main Menu & Screens

### Home Screen

**Layout:**

```
┌─────────────────────────────┐
│ [Logo]          [Settings]  │
│                 [Profile]   │
│                             │
│   ┌─────────────────────┐   │
│   │  Operator Preview   │   │ 3D Model Showcase
│   │    [Character]      │   │
│   └─────────────────────┘   │
│                             │
│      [═ PLAY MATCH ═]       │ Large, prominent
│                             │
│  [Loadout] [Stash] [Quests] │ Secondary actions
│                             │
│ ┌─────────────┐ ┌─────────┐ │
│ │Daily Reward │ │  News   │ │ Info panels
│ └─────────────┘ └─────────┘ │
│                             │
│ [Friends] [Clan] [Store]    │ Social/monetization
└─────────────────────────────┘
```

**Elements:**

**Operator Display:**
- 3D model preview
- Current operator name
- Level progress bar
- Tap to change operator

**Play Button:**
- Size: 300x80px (large)
- Color: Bright cyan
- Animation: Pulse glow
- Haptic feedback on press

**Daily Reward Banner:**
- Countdown timer
- Reward preview
- Tap to claim
- New reward indicator (red dot)

**News Panel:**
- Latest updates
- Events
- Patch notes link

---

### Operator Selection Screen

**Layout:**

```
┌─────────────────────────────┐
│  ← Back     OPERATORS       │
│                             │
│ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ │
│ │ A │ │ S │ │ R │ │ T │ │ Sp│ │ Operator Cards
│ └───┘ └───┘ └───┘ └───┘ └───┘ │
│  ✓              🔒    🔒     │ Lock indicators
│                             │
│   ┌─────────────────────┐   │
│   │  Selected Operator  │   │ Preview
│   │      3D Model       │   │
│   └─────────────────────┘   │
│                             │
│  Class: ASSAULT             │ Info
│  Level: 12  [Progress Bar] │
│                             │
│  Ability: Combat Stim       │ Ability
│  ┌─────────────────────┐   │ description
│  │ +25% damage for     │   │
│  │ 10 seconds          │   │
│  └─────────────────────┘   │
│                             │
│         [SELECT]            │ Confirm button
└─────────────────────────────┘
```

**Operator Cards:**
- Portrait thumbnail
- Class icon
- Level number
- Locked overlay (if locked)
- Tap to preview

**Unlock Indicators:**
- Gray overlay + padlock
- "Level 10 Required"
- "Complete Quest" button
- Or "Purchase" option

---

### Loadout Screen

**Layout:**

```
┌─────────────────────────────┐
│ ← Back      LOADOUT         │
│                             │
│ Operator: ASSAULT [Change]  │
│                             │
│ Primary Weapon:             │
│ ┌─────────────┐             │
│ │ [AR Image]  │ AK-47       │ Weapon slot
│ │             │ DMG: 35     │
│ │             │ FR:  600RPM │
│ └─────────────┘ [Change]    │
│                             │
│ Secondary Weapon:           │
│ ┌─────────────┐             │
│ │ [Pistol Img]│ Glock 19    │
│ └─────────────┘ [Change]    │
│                             │
│ Armor:                      │
│ │ ████████░░  │ Medium (80) │ Armor bar
│                  [Change]   │
│                             │
│ Equipment:                  │
│ ┌───┐ ┌───┐ ┌───┐           │
│ │Gren││Med││ - │  [Add]     │ Gear slots
│ └───┘ └───┘ └───┘           │
│                             │
│ Perks: (Choose 2)           │
│ [✓ Sprint+] [  Armor+]      │ Perk selection
│ [  Reload+] [  Detection-]  │
│                             │
│ Total Gear Value: $15,250   │ Risk indicator
│                             │
│    [Save Loadout] [Ready]   │ Actions
└─────────────────────────────┘
```

**Weapon Selection Modal:**
- Grid of owned weapons
- Filter by type
- Sort by: Level, Rarity, Damage
- Preview stats comparison
- "From Stash" indicator

**Loadout Presets:**
- Save up to 5 loadouts
- Quick-select buttons
- Rename loadouts
- "Budget" vs "Premium" labels

---

### Stash/Inventory Screen

**Layout:**

```
┌─────────────────────────────┐
│ ← Back      STASH           │
│ [Filter▼] [Sort▼] [Search] │
│                             │
│ ┌─────────────────────────┐ │
│ │ ┌──┬──┬──┬──┬──┬──┬──┬──┐ │ │
│ │ │██│  │██│  │  │  │  │  │ │ │
│ │ ├──┼──┼──┼──┼──┼──┼──┼──┤ │ │
│ │ │██│  │██│  │  │  │  │  │ │ │ Grid inventory
│ │ ├──┼──┼──┼──┼──┼──┼──┼──┤ │ │ (drag & drop)
│ │ │  │  │  │  │  │  │  │  │ │ │
│ │ ├──┼──┼──┼──┼──┼──┼──┼──┤ │ │
│ │ │  │  │  │  │  │  │  │  │ │ │
│ │ └──┴──┴──┴──┴──┴──┴──┴──┘ │ │
│ └─────────────────────────┘ │
│                             │
│ Selected Item:              │ Item details
│ ┌─────────────┐             │ panel
│ │ [Item Img]  │             │
│ │             │ AK-47       │
│ │             │ Rarity: Rare│
│ └─────────────┘             │
│ Damage: 35  | Fire Rate: 600│
│ Value: $2,500               │
│                             │
│ [Equip] [Sell] [Details]    │ Actions
│                             │
│ Inventory: 145/200 slots    │ Capacity
│ Value: $125,430 total       │
└─────────────────────────────┘
```

**Features:**

**Drag & Drop:**
- Touch and hold to grab
- Drag to position
- Visual feedback (ghost item)
- Auto-snap to grid
- Haptic feedback on snap

**Filters:**
- All items
- Weapons
- Armor
- Consumables
- Materials
- Quest items

**Sort Options:**
- Rarity
- Value
- Name (A-Z)
- Recent (newly acquired)
- Type

**Quick Actions:**
- Long-press for context menu
- Swipe to sell (with confirmation)
- Double-tap for details

---

## In-Game HUD

### Core HUD Layout

```
┌─────────────────────────────┐
│ ███ Health                  │ Top Left
│ ███ Armor          12:45    │ (Status)
│ ███ Stamina      12 Players │
│                             │
│           ┌───────┐         │ Top Right
│           │ MAP   │         │ (Minimap)
│           └───────┘         │
│                             │
│                             │
│         ⊕                   │ Center
│                             │ (Crosshair)
│                             │
│                   ┌──────┐  │ Right Side
│                   │Loot  │  │ (Notifications)
│                   │Found!│  │
│                   └──────┘  │
│ ◎                         ◉ │ Bottom
│ Movement    30/30  [R] Fire │ (Controls)
│ [C]rouch    [⟳]  [Inv]      │
└─────────────────────────────┘
```

---

### Health & Status Bars

**Health Bar:**
- Location: Top-left
- Style: Segmented (10 segments x 10 HP each)
- Color: Bright red (#DC2626)
- Animation: Smooth depletion, flash on damage
- Size: 200x20px

**Armor Bar:**
- Below health bar
- Style: Segmented (matching health)
- Color: Bright blue (#3B82F6)
- Shows before health depletes

**Stamina Bar:**
- Below armor
- Style: Solid bar (no segments)
- Color: Yellow (#FBBF24)
- Auto-hide when full
- Pulsing when low (<20%)

**Design Notes:**
- High contrast colors
- Visible against any background
- Large enough for glance reading
- Damage direction indicators around bars

---

### Minimap

For detailed functional design, see **[Navigation & Map System](../GameDesign/NavigationAndMap.md)**.

**Position:** Top-right corner
**Size:** 150x150px (scalable in settings)
**Style:** Top-down. Default: Rotating with player.

**Elements:**

**Player:**
- Cyan triangle (pointing forward)
- Fixed center (default) or North-up mode

**Teammates:**
- Blue circles with ID numbers
- Off-screen direction indicators

**Enemies:**
- **Visual:** Red solid dot (if scanned/detected)
- **Audio:** Pulsing waves pointing to sound source (See [Navigation GDD](../GameDesign/NavigationAndMap.md))

**POIs:**
- Loot containers: White dots
- Extraction zones: Green helicopter icons
- Supply drop: Yellow parachute
- Contamination: Red pulsing circle

**Map Features:**
- Building outlines (simplified)
- Roads (gray lines)
- Zone boundaries
- Zoom levels: Auto-zoom based on movement speed

---

### Ammo Counter

**Position:** Bottom-right (near fire button)  
**Style:**

```
    30  Current mag
   ───
   120  Reserve ammo
```

**States:**
- Normal: White text
- Low (<10 rounds): Yellow text
- Empty: Red text + warning icon
- Reloading: Progress circle animation

---

### Crosshair

**Position:** Screen center  
**Style:** Minimal, tactical

**States:**

**Default:**
```
    │
  ─ ⊕ ─
    │
```

**Aiming (smaller):**
```
   │
 ─ + ─
   │
```

**Enemy in sights (red):**
```
   │
 ─ ⊕ ─  (Red color)
   │
```

**Customization Options:**
- Color (white, green, cyan, red)
- Size (small, medium, large)
- Style (cross, dot, circle)
- Opacity (50-100%)

---

### Virtual Joystick

**Position:** Bottom-left  
**Size:** 120x120px touch area, 80x80px visual

**Design:**
```
     ╔═══╗
     ║ ◉ ║  Outer ring (fixed)
     ╚═══╝
       ●    Inner dot (follows thumb)
```

**Behavior:**
- Appears on touch
- Follows thumb within deadzone
- Returns to center on release
- Visual opacity: 60% (not blocking view)
- Deadzone: 15% (no movement in center)

**Haptic Feedback:**
- Light pulse at edge of deadzone
- Helps thumb positioning without looking

---

### Action Buttons

**Fire Button:**
- Position: Bottom-right corner
- Size: 100x100px (largest button)
- Color: Red (#EF4444)
- Icon: Crosshair target
- Behavior: Hold to auto-fire, tap for single shot

**Reload Button:**
- Position: Above right side, middle
- Size: 70x70px
- Color: Yellow (#FBBF24)
- Icon: Circular arrows
- Auto-hidden when full ammo

**Weapon Swap:**
- Position: Right of reload
- Size: 60x60px
- Color: Gray (#6B7280)
- Icon: Two rifles crossed
- Shows current weapon icon

**Crouch Button:**
- Position: Next to joystick
- Size: 70x70px
- Color: Gray (normal), Blue (crouched)
- Icon: Person crouching
- Toggle behavior

**Interaction Button:**
- Position: Below joystick
- Size: 80x80px
- Color: Cyan (#06B6D4)
- Icon: Hand (changes contextual)
- Context: "Open", "Pick Up", "Revive"
- Only appears when near interactable

**Inventory Button:**
- Position: Bottom-right, below fire
- Size: 60x60px
- Color: Gray
- Icon: Backpack
- Opens inventory overlay

---

### Damage Indicators

**Hit Direction:**
- Red arc on screen edge
- Direction of damage source
- Fades over 1 second
- Intensity shows damage amount

**Damage Numbers:**
- Float up from hit location
- Size scales with damage
- Color: Yellow (normal), Red (critical), White (armor)
- Optional toggle in settings

---

### Kill Feed

**Position:** Top-right, below timer  
**Style:** Scrolling list (3 recent kills)

**Format:**
```
[Killer] 🔫 [Victim]        (Top, newest)
  You   🔫  Enemy2          (Middle)
Player3 💀  You             (Bottom, oldest)
```

**Icons:**
- 🔫 Gun kill (shows weapon icon)
- 💥 Explosion
- 🔪 Melee
- 💀 Died to contamination/fall

**Behavior:**
- Fades in (0.3s)
- Stays (5s)
- Fades out (0.5s)
- Scrolls up for new kills

---

### Objective & Quest Tracker

**Position:** Left side, middle  
**Style:** Minimal list

```
├ Main Quest: Extract $5,000
│  ├ Progress: $3,245 / $5,000
│  └ Time: 8:32 remaining
│
└ Daily: Kill 5 enemies
   └ Progress: 3 / 5
```

**Behavior:**
- Collapsible (tap to minimize)
- Updates real-time
- Flash on progress
- Completion animation

---

### Extraction UI

**Extraction Call:**
- Large button appears near extraction zone
- "Call Extraction" (green, pulsing)
- Shows zone name
- Tap to activate

**Extraction Timer:**
```
┌─────────────────┐
│  EXTRACTING     │
│                 │
│   ⏱ 00:24      │  Large countdown
│                 │
│  ████████░░░░   │  Progress bar
│                 │
│ Stay in zone!   │  Instruction
└─────────────────┘
```

**States:**
- Countdown: Green
- Interrupted: Red flash + alert
- Success: Gold + checkmark
- Failed: Gray + X

---

### Notification System

**Types:**

**Toast Notifications:**
- Position: Top-center
- Duration: 3 seconds
- Examples: "Quest completed!", "Level up!"

**Popup Notifications:**
- Position: Center screen (modal)
- Requires dismiss
- Examples: "Achievement unlocked"

**Loot Notifications:**
- Position: Right side, scrolling
- Shows item icon + name + rarity color
- Auto-dismisses after 4 seconds

**Alert Notifications:**
- Position: Center-top
- Urgent warnings
- Examples: "Contamination approaching!"
- Red background, pulsing

---

## Post-Match Screens

### Victory Screen

```
┌─────────────────────────────┐
│        EXTRACTED!           │
│                             │
│   ┌─────────────────────┐   │
│   │  Operator Standing  │   │ 3D model
│   │   (Victory Pose)    │   │ celebration
│   └─────────────────────┘   │
│                             │
│ Loot Extracted:             │
│ ┌──────────────────┐        │
│ │ [Item] [Item]    │        │ Scrolling
│ │ [Item] [Item]    │        │ loot list
│ │                  │        │
│ └──────────────────┘        │
│ Total Value: $8,450         │
│                             │
│ ┌──────┬──────┬──────┐      │
│ │ XP   │Kills│ Time │      │ Stats
│ │+1250 │  3  │12:34 │      │
│ └──────┴──────┴──────┘      │
│                             │
│ [Continue] [Play Again]     │
└─────────────────────────────┘
```

**Animations:**
- Loot icons fly in
- XP bar fills with satisfying sound
- Rare items glow
- Victory music

---

### Defeat Screen

```
┌─────────────────────────────┐
│          KILLED             │
│                             │
│ Eliminated by: PlayerXYZ    │ Killer info
│ Weapon: AK-47               │
│ Distance: 45m               │
│                             │
│ You Lost:                   │
│ ┌──────────────────┐        │
│ │ [Item] [Item]    │        │ Lost loot
│ │ [Item] [Item]    │        │ (grayed out)
│ └──────────────────┘        │
│ Value Lost: $12,340         │
│                             │
│ ┌──────┬──────┬──────┐      │
│ │ XP   │Kills│ Time │      │ Consolation
│ │ +250 │  1  │7:23  │      │ stats
│ └──────┴──────┴──────┘      │
│                             │
│ [View Replay] [Try Again]   │
└─────────────────────────────┘
```

**Tone:**
- Not overly negative
- Show what was lost (learning)
- Encourage retry
- Somber music

---

## Settings UI

### Settings Categories

**Graphics:**
- Quality presets (Low/Med/High/Ultra)
- Resolution
- Frame rate cap
- Effects quality
- Shadow quality
- Anti-aliasing

**Audio:**
- Master volume
- Music volume
- SFX volume
- Voice volume
- Mono audio (accessibility)

**Controls:**
- Sensitivity (aim, movement)
- Invert Y-axis
- Fire button: Tap/Hold
- Left-handed mode
- Button size scaling
- Button opacity

**Gameplay:**
- Auto-pickup
- Aim assist strength
- Crosshair customization
- HUD scaling
- Colorblind modes

**Account:**
- Linked accounts
- Language
- Logout

---

## Accessibility Features

**Colorblind Modes:**
- Deuteranopia (red-green)
- Protanopia (red-green)
- Tritanopia (blue-yellow)
- Adjusts UI colors, not art

**Visual Aids:**
- High contrast mode
- Larger text option
- Screen reader support (future)
- Simplified UI option

**Audio Aids:**
- Subtitles for voice lines
- Visual sound indicators
- Mono audio option

**Controls:**
- Customizable button layouts
- One-handed mode (future)
- External controller support

---

**[← Previous: Audio Design](./06_AudioDesign.md)** | **[High-Level Index](./README.md)** | **[Next: Progression →](./08_Progression.md)**
