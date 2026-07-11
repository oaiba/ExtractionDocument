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
| [UI/UX Index](_index/index.html) | Hub tài liệu UI/UX đầy đủ |
| [Global UX Standards](global_ux_standards/index.html) | Rule chung cho navigation, focus, state, modal, accessibility |
| [Out-of-Raid Screens](out_of_raid_screens/index.html) | Home, loadout, stash, traders, safe house, quests, profile |
| [Pre-Raid Screens](pre_raid_screens/index.html) | Mode, map, deploy confirmation, squad lobby, matchmaking |
| [In-Raid Screens](in_raid_screens/index.html) | HUD, tactical map, looting, inventory overlay, pause, spectator |
| [Post-Raid Screens](post_raid_screens/index.html) | AAR, death replay, loot transfer, quest progress, redeploy |

Để kiểm tra ownership liên domain, decision còn mở và readiness MVP, xem [Cross-System Traceability](../projectscope/cross_system_traceability.vi/index.html), [Design Decision Register](../projectscope/design_decision_register.vi/index.html) và [MVP Readiness Review](../projectscope/mvp_readiness_review.vi/index.html).

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
| Boot and account | Onboarding / Auth | Đưa player an toàn vào valid account và tutorial state | [Settings & System Screens](commerce_settings_system_screens/index.html), [Loading Screen Design](loadingscreen_design/index.html) |
| Out of raid | Home, profile, stash, traders, safe house, quests | Prepare, recover, progress, và manage risk | [Out-of-Raid Screens](out_of_raid_screens/index.html) |
| Pre-raid | Mode, map, squad, deploy, matchmaking | Confirm rules, risk, party readiness, và queue state | [Pre-Raid Screens](pre_raid_screens/index.html) |
| In raid | HUD, map, looting, overlays, pause, spectator | Giữ survival-critical information rõ khi có pressure | [In-Raid Screens](in_raid_screens/index.html), [HUD Design](hud_design/index.html) |
| Post-raid | AAR, death replay, loot transfer, report, redeploy | Giải thích outcome và route player vào loop tiếp theo | [Post-Raid Screens](post_raid_screens/index.html) |
| Social | Friends, party, clan, LFG, communication, moderation | Giúp player coordinate trong khi hạn chế abuse | [Social Screens](social_screens/index.html) |
| Progression and LiveOps | Battle pass, events, ranked, rewards, inbox | Surface long-term goals mà không bury raid flow | [Progression & LiveOps Screens](progression_liveops_screens/index.html) |
| Commerce | Shop, offers, bundles, item preview, currency top-up, confirmation, receipts, redeem | Xử lý cosmetic browsing và checkout trust states | [Commerce Screens](commerce_screens/index.html) |
| Settings and system | Settings, account, privacy, diagnostics, dialogs | Xử lý configuration, account, platform, và system states | [Settings & System Screens](commerce_settings_system_screens/index.html) |

---

### Commerce Coverage Checklist

Commerce screen coverage chỉ hoàn chỉnh khi canonical page định nghĩa rõ offer information architecture, offer card anatomy, checkout trust states, receipt/support routes, và platform/region restrictions.

| Coverage Area | Requirement |
| :--- | :--- |
| Offer IA | Entry points, tabs, section priority, và empty/offline fallback explicit |
| Checkout trust | Price, currency type, ownership, balance impact, provider handoff, và confirmation visible |
| Receipt/support | Success, pending, failed, refunded, duplicate, và missing entitlement states expose support routes |
| Platform restrictions | Region, age, account, provider, và spending-limit blocks có readable reasons |
| No wallet drift | Premium balance chỉ là component; không tạo standalone Wallet destination |

---

### Progression / LiveOps Coverage Checklist

Progression và LiveOps coverage chỉ hoàn chỉnh khi canonical page định nghĩa reward claim states, season/event timing, deep links, expiry/conversion behavior, và boundary với Commerce.

| Coverage Area | Requirement |
| :--- | :--- |
| Reward model | Locked, earned, claimable, claimed, blocked, overflow, expired, converted, và retroactive grants explicit |
| Season state | Preseason, active, ending, grace, archived, và offline/cached states có UI behavior |
| Event clarity | Event rules, modifiers, objectives, reward ladder, event currency, expiry, và playable route visible |
| Claim trust | Rewards show source, destination, expiry, blocker, claim-all leftovers, và support route khi cần |
| Commerce boundary | Battle pass/event purchase CTAs route tới Commerce; reward/progress context ở Progression/LiveOps |

---

## Screen Spec Template

Dùng template này cho mọi screen spec mới. Giữ đủ ngắn để update được, nhưng đủ hoàn chỉnh cho designer layout, UX review, và implementation planning. [Out-of-Raid Screens](out_of_raid_screens/index.html) là baseline example cho format designer-ready đầy đủ.

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
- [ ] Technical terms khớp [UI System](../../gdd_technical/systems/uisystem/index.html) khi cần code-facing name.
