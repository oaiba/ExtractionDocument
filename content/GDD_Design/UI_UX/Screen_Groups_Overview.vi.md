---
title: "Screen Groups Overview"
type: docs
weight: 1
---

## Purpose

Trang này là screen inventory canonical cho package UI/UX design. Nó nhóm screen theo player lifecycle thay vì widget type để designer, game designer, và engineer có thể suy nghĩ theo player journey hoàn chỉnh.

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Hub tài liệu UI/UX đầy đủ |
| [Global UX Standards](Global_UX_Standards.md) | Rule chung cho navigation, focus, state, modal, accessibility |
| [Out-of-Raid Screens](Out_Of_Raid_Screens.md) | Home, loadout, stash, traders, safe house, quests, profile |
| [Pre-Raid Screens](Pre_Raid_Screens.md) | Mode, map, deploy confirmation, squad lobby, matchmaking |
| [In-Raid Screens](In_Raid_Screens.md) | HUD, tactical map, looting, inventory overlay, pause, spectator |
| [Post-Raid Screens](Post_Raid_Screens.md) | AAR, death replay, loot transfer, quest progress, redeploy |

Mỗi screen group phải trả lời bốn câu hỏi:

| Question | Requirement |
| :--- | :--- |
| Player đang cố làm gì? | Nêu player intent trước layout detail |
| Thông tin nào bắt buộc? | Show risk, cost, progress, hoặc failure reason đúng lúc |
| Next action là gì? | Làm primary CTA rõ và giữ exits predictable |
| Điều gì có thể lỗi? | Định nghĩa loading, empty, locked, invalid, offline, error states |

---

## Screen Group Taxonomy

#### System Diagram

```
+----------------+     +----------------+     +----------------+
| BOOT / AUTH    | --> | OUT OF RAID    | --> | PRE RAID       |
| login, setup   |     | home, stash    |     | mode, map      |
| tutorial gate  |     | traders, quest |     | squad, deploy  |
+----------------+     +----------------+     +----------------+
                                                        |
                                                        v
+----------------+     +----------------+     +----------------+
| SYSTEM / LIVE  | <-- | POST RAID      | <-- | IN RAID        |
| shop, settings |     | AAR, replay    |     | HUD, map       |
| events, social |     | loot, redeploy |     | loot, pause    |
+----------------+     +----------------+     +----------------+
```

- Primary loop chạy theo chiều kim đồng hồ từ account entry tới raid recovery.
- Social, LiveOps, commerce, và settings có thể deep link vào loop nhưng không được bury Deploy.
- Mỗi group sở hữu screen states, input mapping, và accessibility behavior cho surface của nó.

| Phase | Screen Group | Primary Job | Key Pages |
| :--- | :--- | :--- | :--- |
| Boot and account | Onboarding / Auth | Đưa player an toàn vào valid account và tutorial state | [Settings & System Screens](Commerce_Settings_System_Screens.md), [Loading Screen Design](LoadingScreen_Design.md) |
| Out of raid | Home, profile, stash, traders, safe house, quests | Prepare, recover, progress, và manage risk | [Out-of-Raid Screens](Out_Of_Raid_Screens.md) |
| Pre-raid | Mode, map, squad, deploy, matchmaking | Confirm rules, risk, party readiness, và queue state | [Pre-Raid Screens](Pre_Raid_Screens.md) |
| In raid | HUD, map, looting, overlays, pause, spectator | Giữ survival-critical information rõ khi có pressure | [In-Raid Screens](In_Raid_Screens.md), [HUD Design](HUD_Design.md) |
| Post-raid | AAR, death replay, loot transfer, report, redeploy | Giải thích outcome và route player vào loop tiếp theo | [Post-Raid Screens](Post_Raid_Screens.md) |
| Social | Friends, party, clan, LFG, communication, moderation | Giúp player coordinate trong khi hạn chế abuse | [Social Screens](Social_Screens.md) |
| Progression and LiveOps | Battle pass, events, ranked, rewards, inbox | Surface long-term goals mà không bury raid flow | [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) |
| Commerce | Shop, offers, bundles, item preview, currency top-up, confirmation, receipts, redeem | Xử lý cosmetic browsing và checkout trust states | [Commerce Screens](Commerce_Screens.md) |
| Settings and system | Settings, account, privacy, diagnostics, dialogs | Xử lý configuration, account, platform, và system states | [Settings & System Screens](Commerce_Settings_System_Screens.md) |

---

## Screen Spec Template

Dùng template này cho mọi screen spec mới. Giữ đủ ngắn để update được, nhưng đủ hoàn chỉnh cho designer layout, UX review, và implementation planning. [Out-of-Raid Screens](Out_Of_Raid_Screens.md) là baseline example cho format designer-ready đầy đủ.

#### Spec Template Layout

```
+------------------------------------------------------------------+
| SCREEN NAME                                      [Primary CTA]   |
| Entry: Home / Deep Link / Event                 Exit: Back / X   |
|------------------------------------------------------------------|
| Goal: One sentence                                               |
| Intent: What the player came here to do                          |
|                                                                  |
| +----------------------+  +------------------------------------+ |
| | Main Content         |  | Context / Detail Panel             | |
| | selected item/state  |  | rules, cost, risk, requirement     | |
| +----------------------+  +------------------------------------+ |
|                                                                  |
| States: Default | Loading | Empty | Locked | Error | Success     |
| Input: Mouse/KB | Controller | Touch | Accessibility notes       |
+------------------------------------------------------------------+
```

| Section | Required Content |
| :--- | :--- |
| Player Intent | Vì sao player mở screen, success nghĩa là gì, risk/cost nào phải hiểu |
| Expanded ASCII Wireframe | Layout PC/console landscape với header, primary area, detail panel, warning lane, action bar |
| Layout Anatomy | Named regions và content chính xác từng region cần giữ |
| Visual Hierarchy | Thứ tự priority: đọc trước, đọc thứ hai, đọc thứ ba |
| Component Requirements | Requirement low-level cho row, card, panel, CTA, warning, badge, dialog |
| States & Edge Cases | Default, loading, empty, invalid, blocked, locked, offline, error, success, destructive confirmation |
| Input / Focus / Touch | Mouse/keyboard, controller, mobile touch, focus order, hold/tap alternative |
| Designer Notes | Constraint ngắn, actionable về density, copy, responsiveness, non-color state meaning |
| Acceptance Checklist | Checklist review cho layout handoff và implementation QA |

### Designer-Ready Handoff Rules

| Rule | Requirement |
| :--- | :--- |
| Summary is not enough | Requirement critical phải nằm trong section screen sở hữu nó, không chỉ ở inventory table |
| Disabled means explained | Mọi disabled CTA phải nêu blocker đầu tiên và route nếu có |
| Color is never alone | State, rarity, danger, lock, success phải có text hoặc icon-shape support |
| Action bars stay stable | Primary CTA không nhảy khi warning text xuất hiện |
| Mobile is not an afterthought | Mọi screen cần touch layout note và primary CTA sticky/reachable |
| Destructive actions confirm | Sell, discard, abandon, unlink, delete, spend, report/block phải state consequence trước commit |

---

## Global Navigation Model

#### Screen Ownership Map

```
+--------------------+       +-----------------------+
| SCREEN GROUP DOC   | ----> | GAME DESIGN DOC       |
| layout, states     |       | rules, economy, flow  |
+--------------------+       +-----------------------+
          |                              |
          v                              v
+--------------------+       +-----------------------+
| TECHNICAL SYSTEM   | <---- | UX FLOWS / STANDARDS  |
| code names, events |       | journey, input, QA    |
+--------------------+       +-----------------------+
```

- Screen group pages sở hữu player-facing layout contract.
- Game design pages sở hữu gameplay rules và economy outcomes.
- Technical pages sở hữu code names, events, data contracts, implementation constraints.

| Surface | Navigation Rule |
| :--- | :--- |
| Home hub | Horizontal global navigation bar theo PC/Console landscape standard |
| Preparation flow | Đủ linear cho new players, đủ jumpable cho experts |
| In-raid overlays | Không bao giờ pause online raid state hoàn toàn; giữ audio và threat awareness |
| Modal dialogs | Một decision mỗi modal; destructive actions cần hold hoặc second confirmation |
| Back behavior | `ESC` / `B` luôn đóng deepest layer trước |
| Deep links | Event, quest, reward, và trader cards phải mở đúng destination screen |
| Vertical rails | Chỉ dùng secondary/local navigation: stash filters, roster filters, trader list, quest list, settings categories, social/LFG lists |

---

## Coverage Checklist

- [ ] Mọi player lifecycle phase có screen group.
- [ ] Mọi group theo PC/Console landscape standard.
- [ ] Primary navigation dùng horizontal global nav; vertical rail chỉ secondary/local.
- [ ] Mọi group định nghĩa blocked, empty, locked, loading, offline, error states.
- [ ] Mọi major game system có UI owner hoặc cross-reference.
- [ ] Không một document nào sở hữu unrelated screens đáng ra thuộc group khác.
- [ ] Technical terms khớp [UI System](../../GDD_Technical/Systems/UISystem.md) khi cần code-facing name.
