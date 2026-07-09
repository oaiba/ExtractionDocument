---
title: "User Experience (UX)"
linkTitle: "UI/UX"
type: docs
weight: 10
sidebar:
  open: false
---

## Start Here / Section Contents

Các page screen group theo vòng đời là spec canonical, designer-ready. Chúng chứa expanded ASCII wireframe, layout anatomy, visual hierarchy, component requirement, state behavior, input/focus/touch rule, designer note, và acceptance checklist. Các support page như HUD, notification, loading, flow, visual style, và global standard định nghĩa rule tái sử dụng để các screen spec tham chiếu.

{{< cards >}}
  {{< card link="Screen_Groups_Overview" title="Screen Groups Overview" icon="view-grid" subtitle="Screen taxonomy canonical theo player lifecycle, spec template, navigation model, và coverage checklist" >}}
  {{< card link="Global_UX_Standards" title="Global UX Standards" icon="adjustments" subtitle="Navigation, focus, responsive layout, modal, state, accessibility, và analytics standard" >}}
  {{< card link="Out_Of_Raid_Screens" title="Out-of-Raid Screens" icon="home" subtitle="Home, operator, loadout, stash, traders, safe house, quests, và profile surfaces" >}}
  {{< card link="Pre_Raid_Screens" title="Pre-Raid Screens" icon="play" subtitle="Mode select, map select, deploy confirmation, squad lobby, matchmaking, và match found" >}}
  {{< card link="In_Raid_Screens" title="In-Raid Screens" icon="eye" subtitle="HUD, tactical map, looting, inventory overlay, pause, spectator, và reconnect states" >}}
  {{< card link="Post_Raid_Screens" title="Post-Raid Screens" icon="chart-bar" subtitle="AAR, death replay, loot transfer, quest progress, report/commend, và redeploy flows" >}}
  {{< card link="Social_Screens" title="Social Screens" icon="user-group" subtitle="Friends, party, invite, LFG, clan, chat, voice, block, và report screens" >}}
  {{< card link="Progression_LiveOps_Screens" title="Progression & LiveOps Screens" icon="sparkles" subtitle="Battle pass, event, daily and weekly task, ranked, leaderboard, reward, và news" >}}
  {{< card link="Commerce_Screens" title="Commerce Screens" icon="shopping-cart" subtitle="Shop, rotating offer, bundle, item preview, currency top-up, purchase confirmation, receipt, và redeem flow" >}}
  {{< card link="Commerce_Settings_System_Screens" title="Settings & System Screens" icon="cog" subtitle="Auth, setup, settings, privacy, diagnostics, account safety, và system dialog" >}}
  {{< card link="LoadingScreen_Design" title="Async Loading Screen Design" icon="clock" subtitle="Loading type taxonomy L1-L8, content type, layout, async loading flow" >}}
  {{< card link="HUD_Design" title="In-Raid HUD Design" icon="eye" subtitle="HUD element catalog, contextual visibility, minimap, compass, và customization option" >}}
  {{< card link="UX_Flows" title="UX Flows & Wireframes" icon="cursor-click" subtitle="Player journey map, cross-platform wireframe, state machine, navigation pattern" >}}
  {{< card link="Notification_Systems" title="Notification & Feedback Systems" icon="bell" subtitle="Kill feed, damage feedback, status effect, toast message, danger communication" >}}
  {{< card link="Visual_Style" title="Visual Style & Art Guidelines" icon="color-swatch" subtitle="Color palette, typography, iconography, lighting, VFX, và platform adaptation" >}}
  {{< card link="Menus" title="Menus & Screens (Legacy)" icon="document-text" subtitle="Compatibility page map old menu section sang lifecycle screen group mới" >}}
{{< /cards >}}

---

## Thiết Kế Interaction

UX tốt là UX vô hình. Nó đưa người chơi vào game nhanh hơn và làm hệ thống phức tạp trở nên trực quan. Trong một cross-platform top-down extraction shooter, từng millisecond và từng input đều quan trọng.

### Core UX Pillars

#### 1. Speed Over Complexity

- **Minimal Clicks**: Mọi action nên cần số input tối thiểu trên mọi platform
- **Quick Access**: Hệ thống critical (Inventory, Map, Comms) truy cập trong tối đa 2 input
- **Smart Defaults**: Pre-select lựa chọn phổ biến để giảm decision fatigue

#### 2. Multi-Platform First

- **Console First Philosophy**: Thiết kế cho gamepad D-Pad navigation, sau đó scale lên PC
- **Touch Optimization**: Mobile yêu cầu touch target tối thiểu 44x44px (Apple HIG standard)
- **Unified Visual Language**: Cùng icon, color, và feedback trên mọi platform

#### 3. Tension and Feedback

- **Clear Feedback**: Mọi button press phải có xác nhận visual/audio/haptic
- **Risk Communication**: UI phải cho thấy rõ "you're exposed" vs. "you're safe"
- **Status at a Glance**: Health, ammo, squad status nhìn được mà không mở menu

### Platform-Specific Considerations

#### PC (Keyboard + Mouse)

- Hotkey cho mọi major action (I = Inventory, M = Map, TAB = Scoreboard)
- Cursor-based interaction cho precision looting
- UI scalable cho display 1080p đến 4K
- FOV slider (60-120 degrees)

#### Console (Controller)

- Radial menu cho item selection (giữ button + hướng analog stick)
- Contextual action trên một lần bấm (A/X cho "Use/Pickup/Open")
- Safe zone margin cho các TV overscan setting khác nhau
- Aim assist option (configurable)

#### Mobile (Touch)

- HUD layout có thể customize (người chơi kéo thả element)
- Gyroscope aiming toggle
- Inventory đơn giản hóa (swipe để sort, tap để equip)
- Auto-run toggle để giảm áp lực giữ ngón liên tục

### UX Riêng Cho Extraction Shooter

#### Pre-Raid Flow

1. **Loadout Selection**: So sánh visual các gear stat
2. **Map Preview**: Hiển thị extraction point và danger zone
3. **Squad Formation**: Role và ready status rõ ràng
4. **Insurance**: One-click insurance cho item giá trị cao

#### In-Raid Essentials

- **Extraction Timer**: Countdown persistent tới final extract window
- **Threat Level Indicator**: Visual/audio cue cho player/AI gần đó
- **Secure Container Access**: Quick-slot item được bảo vệ giữa raid
- **Weight System**: Feedback thời gian thực về movement speed penalty

#### Post-Raid Debrief

- **Loot Summary**: Danh sách item theo rarity với sell value
- **XP Breakdown**: Cho biết action nào tạo experience
- **Quest Progress**: Theo dõi objective hoàn thành trong session này
- **Replay Highlights**: Death cam cho biết ai giết và bằng cách nào

---

## Accessibility Standards

Theo WCAG 2.1 Level AA compliance:

- **Colorblind Modes**: Filter Deuteranopia, Protanopia, Tritanopia
- **Text Scaling**: 100%-200% mà không phá layout
- **Subtitles**: Directional audio indicator cho người khiếm thính
- **Button Remapping**: Full customization trên mọi platform
- **Motion Reduction**: Toggle cho screen shake và blur effect

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
