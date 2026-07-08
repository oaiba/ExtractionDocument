---
title: "User Experience (UX)"
linkTitle: "UI/UX"
type: docs
weight: 10
sidebar:
  open: false
---

## Start Here / Section Contents

The lifecycle screen group pages are the canonical designer-ready specs. They contain the expanded ASCII wireframes, layout anatomy, visual hierarchy, component requirements, state behavior, input/focus/touch rules, designer notes, and acceptance checklists. Support pages such as HUD, notifications, loading, flows, visual style, and global standards define reusable rules that those screen specs reference.

{{< cards >}}
  {{< card link="Screen_Groups_Overview" title="Screen Groups Overview" icon="view-grid" subtitle="Canonical screen taxonomy by player lifecycle, spec template, navigation model, and coverage checklist" >}}
  {{< card link="Global_UX_Standards" title="Global UX Standards" icon="adjustments" subtitle="Navigation, focus, responsive layout, modal, state, accessibility, and analytics standards" >}}
  {{< card link="Out_Of_Raid_Screens" title="Out-of-Raid Screens" icon="home" subtitle="Home, operator, loadout, stash, traders, safe house, quests, and profile surfaces" >}}
  {{< card link="Pre_Raid_Screens" title="Pre-Raid Screens" icon="play" subtitle="Mode select, map select, deploy confirmation, squad lobby, matchmaking, and match found" >}}
  {{< card link="In_Raid_Screens" title="In-Raid Screens" icon="eye" subtitle="HUD, tactical map, looting, inventory overlay, pause, spectator, and reconnect states" >}}
  {{< card link="Post_Raid_Screens" title="Post-Raid Screens" icon="chart-bar" subtitle="AAR, death replay, loot transfer, quest progress, report/commend, and redeploy flows" >}}
  {{< card link="Social_Screens" title="Social Screens" icon="user-group" subtitle="Friends, party, invites, LFG, clans, chat, voice, block, and report screens" >}}
  {{< card link="Progression_LiveOps_Screens" title="Progression & LiveOps Screens" icon="sparkles" subtitle="Battle pass, events, daily and weekly tasks, ranked, leaderboards, rewards, and news" >}}
  {{< card link="Commerce_Screens" title="Commerce Screens" icon="shopping-cart" subtitle="Shop, rotating offers, bundles, item preview, currency top-up, purchase confirmation, receipts, and redeem flows" >}}
  {{< card link="Commerce_Settings_System_Screens" title="Settings & System Screens" icon="cog" subtitle="Auth, setup, settings, privacy, diagnostics, account safety, and system dialogs" >}}
  {{< card link="LoadingScreen_Design" title="Async Loading Screen Design" icon="clock" subtitle="Loading type taxonomy L1-L8, content types, layouts, async loading flow" >}}
  {{< card link="HUD_Design" title="In-Raid HUD Design" icon="eye" subtitle="HUD element catalog, contextual visibility, minimap, compass, and customization options" >}}
  {{< card link="UX_Flows" title="UX Flows & Wireframes" icon="cursor-click" subtitle="Player journey map, cross-platform wireframes, state machines, navigation patterns" >}}
  {{< card link="Notification_Systems" title="Notification & Feedback Systems" icon="bell" subtitle="Kill feed, damage feedback, status effects, toast messages, danger communication" >}}
  {{< card link="Visual_Style" title="Visual Style & Art Guidelines" icon="color-swatch" subtitle="Color palettes, typography, iconography, lighting, VFX, and platform adaptations" >}}
  {{< card link="Menus" title="Menus & Screens (Legacy)" icon="document-text" subtitle="Compatibility page mapping old menu sections to the new lifecycle screen groups" >}}
{{< /cards >}}

---

## Designing the Interaction

Good UX is invisible. It gets the player into the game faster and makes complex systems intuitive. In a cross-platform top-down extraction shooter, every millisecond and every input counts.

### Core UX Pillars

#### 1. Speed Over Complexity

- **Minimal Clicks**: Every action should take the minimum number of inputs across all platforms
- **Quick Access**: Critical systems (Inventory, Map, Comms) accessible within 2 inputs maximum
- **Smart Defaults**: Pre-select common choices to reduce decision fatigue

#### 2. Multi-Platform First

- **Console First Philosophy**: Design for gamepad D-Pad navigation, then scale up for PC
- **Touch Optimization**: Mobile requires 44x44px minimum touch targets (Apple HIG standard)
- **Unified Visual Language**: Same icons, colors, and feedback across all platforms

#### 3. Tension and Feedback

- **Clear Feedback**: Every button press must have visual/audio/haptic confirmation
- **Risk Communication**: UI must clearly show "you're exposed" vs. "you're safe"
- **Status at a Glance**: Health, ammo, squad status visible without opening menus

### Platform-Specific Considerations

#### PC (Keyboard + Mouse)
- Hotkeys for all major actions (I = Inventory, M = Map, TAB = Scoreboard)
- Cursor-based interactions for precision looting
- Scalable UI for 1080p to 4K displays
- FOV slider (60-120 degrees)

#### Console (Controller)
- Radial menus for item selection (hold button + analog stick direction)
- Contextual actions on single button press (A/X for "Use/Pickup/Open")
- Safe zone margins for different TV overscan settings
- Aim assist options (configurable)

#### Mobile (Touch)
- Customizable HUD layout (players can drag elements)
- Gyroscope aiming toggle
- Simplified inventory (swipe to sort, tap to equip)
- Auto-run toggle to reduce constant thumb pressure

### Extraction Shooter-Specific UX

#### Pre-Raid Flow
1. **Loadout Selection**: Visual comparison of gear stats
2. **Map Preview**: Show extraction points and danger zones
3. **Squad Formation**: Clear roles and ready status
4. **Insurance**: One-click insurance for high-value items

#### In-Raid Essentials
- **Extraction Timer**: Persistent countdown to final extract window
- **Threat Level Indicator**: Visual/audio cues for nearby players/AI
- **Secure Container Access**: Quick-slot protected items mid-raid
- **Weight System**: Real-time feedback on movement speed penalty

#### Post-Raid Debrief
- **Loot Summary**: Rarity-coded item list with sell value
- **XP Breakdown**: Show what actions earned experience
- **Quest Progress**: Track objectives completed this session
- **Replay Highlights**: Death cam showing who/how you died

---

## Accessibility Standards

Following WCAG 2.1 Level AA compliance:

- **Colorblind Modes**: Deuteranopia, Protanopia, Tritanopia filters
- **Text Scaling**: 100%-200% without breaking layout
- **Subtitles**: Directional audio indicators for hearing-impaired
- **Button Remapping**: Full customization across all platforms
- **Motion Reduction**: Toggle for screen shake and blur effects

---

## Cross-Platform Testing Matrix

| Feature | PC | Console | Mobile | Priority |
| :------ | :-: | :-----: | :----: | :------: |
| Controller Support | Yes | Yes | Limited | High |
| Touch Controls | No | No | Yes | High |
| Gyro Aiming | No | PS5 only | Yes | Medium |
| Text Chat | Yes | Limited | Limited | Medium |
| Voice Chat (Proximity) | Yes | Yes | Yes | Critical |
| Cross-Progression | Yes | Yes | Yes | Critical |

## Continuous Improvement

**Analytics to Track:**
- Average time to enter first raid (target: under 90 seconds)
- Inventory management time per session
- Drop-off points in tutorial (first 3 missions)
- Platform-specific crash reports
- Control scheme preference distribution

**User Testing Cadence:**
- Weekly playtests with 5-10 players per platform
- A/B testing for controversial UI changes
- Heatmap tracking for menu navigation
- Sentiment analysis on post-raid surveys
