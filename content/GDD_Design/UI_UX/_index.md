---
title: "User Experience (UX)"
linkTitle: "UI/UX"
type: docs
weight: 10
---

## 💆 Designing the Interaction

Good UX is invisible. It gets the player into the game faster and makes complex systems intuitive. In a cross-platform topdown extraction shooter, every millisecond and every input counts.

### Core UX Pillars

#### **1. Speed Over Complexity**
*   **Minimal Clicks:** Every action should take the minimum number of inputs across all platforms
*   **Quick Access:** Critical systems (Inventory, Map, Comms) accessible within 2 inputs maximum
*   **Smart Defaults:** Pre-select common choices to reduce decision fatigue

#### **2. Multi-Platform First**
*   **Console First Philosophy:** Design for gamepad D-Pad navigation, then scale up for PC
*   **Touch Optimization:** Mobile requires 44x44px minimum touch targets (Apple HIG standard)
*   **Unified Visual Language:** Same icons, colors, and feedback across all platforms

#### **3. Tension & Feedback**
*   **Clear Feedback:** Every button press must have visual/audio/haptic confirmation
*   **Risk Communication:** UI must clearly show "you're exposed" vs "you're safe"
*   **Status at a Glance:** Health, ammo, squad status visible without opening menus

### Platform-Specific Considerations

#### **PC (Keyboard + Mouse)**
*   Hotkeys for all major actions (I = Inventory, M = Map, TAB = Scoreboard)
*   Cursor-based interactions for precision looting
*   Scalable UI for 1080p to 4K displays
*   FOV slider (60-120 degrees)

#### **Console (Controller)**
*   Radial menus for item selection (hold button + analog stick direction)
*   Contextual actions on single button press (A/X for "Use/Pickup/Open")
*   Safe zone margins for different TV overscan settings
*   Aim assist options (configurable)

#### **Mobile (Touch)**
*   Customizable HUD layout (players can drag elements)
*   Gyroscope aiming toggle
*   Simplified inventory (swipe to sort, tap to equip)
*   Auto-run toggle to reduce constant thumb pressure

### Extraction Shooter-Specific UX

#### **Pre-Raid Flow**
1.  **Loadout Selection:** Visual comparison of gear stats
2.  **Map Preview:** Show extraction points and danger zones
3.  **Squad Formation:** Clear roles and ready status
4.  **Insurance:** One-click insurance for high-value items

#### **In-Raid Essentials**
*   **Extraction Timer:** Persistent countdown to final extract window
*   **Threat Level Indicator:** Visual/audio cues for nearby players/AI
*   **Secure Container Access:** Quick-slot protected items mid-raid
*   **Weight System:** Real-time feedback on movement speed penalty

#### **Post-Raid Debrief**
*   **Loot Summary:** Rarity-coded item list with sell value
*   **XP Breakdown:** Show what actions earned experience
*   **Quest Progress:** Track objectives completed this session
*   **Replay Highlights:** Death cam showing who/how you died

---

## 🎯 Accessibility Standards

Following WCAG 2.1 Level AA compliance:

*   **Colorblind Modes:** Deuteranopia, Protanopia, Tritanopia filters
*   **Text Scaling:** 100%-200% without breaking layout
*   **Subtitles:** Directional audio indicators for hearing-impaired
*   **Button Remapping:** Full customization across all platforms
*   **Motion Reduction:** Toggle for screen shake and blur effects

---

## 📊 Cross-Platform Testing Matrix

| Feature                |  PC   | Console | Mobile | Priority |
| :--------------------- | :---: | :-----: | :----: | :------: |
| Controller Support     |   ✅   |    ✅    |   ⚠️    |   High   |
| Touch Controls         |   ❌   |    ❌    |   ✅    |   High   |
| Gyro Aiming            |   ❌   |   ✅*    |   ✅    |  Medium  |
| Text Chat              |   ✅   |    ⚠️    |   ⚠️    |  Medium  |
| Voice Chat (Proximity) |   ✅   |    ✅    |   ✅    | Critical |
| Cross-Progression      |   ✅   |    ✅    |   ✅    | Critical |

✅ = Fully Supported | ⚠️ = Limited Support | ❌ = Not Supported  
\* = PlayStation DualSense only

---

{{< cards >}}
  {{< card link="ux_flows.html" title="User Flows" icon="cursor-click" subtitle="Wireframes for inventory, matchmaking, looting, and extraction." >}}
  {{< card link="visual_style.html" title="Interface Style" icon="color-swatch" subtitle="Color palettes, typography, iconography, and platform adaptations." >}}
{{< /cards >}}

---

## 🔄 Continuous Improvement

**Analytics to Track:**
*   Average time to enter first raid (target: <90 seconds)
*   Inventory management time per session
*   Drop-off points in tutorial (first 3 missions)
*   Platform-specific crash reports
*   Control scheme preference distribution

**User Testing Cadence:**
*   Weekly playtests with 5-10 players per platform
*   A/B testing for controversial UI changes
*   Heatmap tracking for menu navigation
*   Sentiment analysis on post-raid surveys