---
title: "Out-of-Raid màn hình"
type: docs
weight: 3
---

## Mục Đích

Out-of-raid màn hình are the người chơi's command center. They support recovery sau failure, celebration sau extraction, inventory quyết định, long-term progression, và the fastest safe route back into a raid.

This trang owns the người chơi-facing layout contract for out-of-raid surfaces. Game design trang own economy và progression rules; technical trang own implementation names, data events, và dịch vụ contracts.

Tham chiếu chính:

| hệ thống | source |
| :--- | :--- |
| Home hub | [Home màn hình & Main Lobby Design](../GameDesign/HomeScreen_Design.md) |
| Loadout preparation | [Pre-Raid Loadout & Preparation màn hình](../GameDesign/LoadoutPreparation.md) |
| Safe House | [Safe House Design](../GameDesign/Safe_House_Design.md) |
| Stash | [Stash Design](../Stash_Design.md) |
| Profile | [người chơi Profile & Career Stats](../GameDesign/PlayerProfile.md) |
| Quests | [Quest & Objective hệ thống](../Gameplay/Quest_Objective_System.md) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [màn hình Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](Global_UX_Standards.md) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [Pre-Raid màn hình](Pre_Raid_Screens.md) | Mode, map, deploy confirmation, squad lobby, matchmaking |
| [Post-Raid màn hình](Post_Raid_Screens.md) | AAR, death replay, loot transfer, redeploy |
| [UX flow](UX_Flows.md) | End-to-end journey mapping |

---

## Inventory Màn Hình

This bảng is a navigation summary. chi tiết visual, trạng thái, input, và acceptance yêu cầu live inside each màn hình section below.

| màn hình | mục tiêu | primary CTA | chính trạng thái |
| :--- | :--- | :--- | :--- |
| Home / Safe House Hub | Show identity, changed trạng thái, và deploy path | Deploy / Continue Preparation | first session, return victory, return death, event active, offline |
| Operator Select | Choose nhân vật role và kiểm tra ability identity | Select Operator | locked, injured/cooldown, recommended, cosmetic preview |
| Loadout Workbench | Build a valid kit và understand risk | Ready / Continue to Mission | missing vũ khí, missing đạn, overweight, uninsured giá trị |
| Stash | Store, sort, search, sell, và move items | Move / Equip / Sell | empty stash, full stash, filter no results, item locked |
| Traders / Market | mua, sell, barter, và turn in faction items | purchase / Sell / Trade | insufficient funds, rep locked, barter missing items, sale confirmation |
| Safe House Modules | upgrade base, craft, repair, và claim returns | upgrade / Start Craft / claim | module locked, missing materials, queue full, timer complete |
| Quest Board | Track objectives và turn in rewards | Track / Turn In | completed, failed, missing item, location locked |
| người chơi Profile | Review identity, stats, titles, achievements, cosmetics | Equip Title / View Stats | private profile, seasonal reset, no achievements |

---

## Home / Safe House Hub

**người chơi Intent**

The người chơi wants to understand what changed since the last session, confirm whether the hiện tại kit is raid-ready, và choose the fastest safe next action: deploy, recover, manage inventory, hoặc kiểm tra progression.

| Spec | yêu cầu |
| :--- | :--- |
| Entry points | Post-login loading, AAR continue, app resume, party leader navigation, event deep link |
| Exit points | Deploy, Loadout, Stash, Safe House, Traders, Quests, Profile, Settings |
| primary CTA | Deploy nếu valid; Continue Preparation nếu blockers exist; Tutorial Raid for first session |
| secondary actions | kiểm tra operator, open last raid recap, claim returns, check squad, open event, manage stash |
| Destructive actions | None on hub; destructive actions must deep link to their owning màn hình và confirm there |

**Expanded ASCII Wireframe**

```
+---------------------------------------------------------------------------------+
| GLOBAL HEADER: Lv.12 Salvage Rep 3     EXTRACTION PROTOCOL   Credits 425K [N]  |
|---------------------------------------------------------------------------------|
| PRIMARY NAV: Home | Loadout | Stash | Traders | SafeHouse | Quests | Profile   |
|              Settings                                                           |
|---------------------------------------------------------------------------------|
| PRIMARY HERO / OPERATOR SHOWCASE                              | DEPLOY PANEL    |
| +------------------------------------------------------------+ | Mode: Solo      |
| | 3D OPERATOR MODEL / SAFE HOUSE BACKDROP                    | | Map: Sector 7   |
| | - current armor and weapon visible                         | | Time: Day       |
| | - rotate / inspect affordance                              | | Squad: 1/4      |
| | - injury, insurance, and cosmetic badges                   | | Queue: 45s      |
| +------------------------------------------------------------+ |-----------------|
| LAST RAID SNAPSHOT                                             | Gear 125K       |
| EXTRACTED  +1,700 XP  Loot 7 items  Rep +0.05                  | Weight 24/40    |
| [View AAR] [Move Loot] [Redeploy Route]                        | Insured 4/6     |
|----------------------------------------------------------------+-----------------|
| CONTEXT CARDS                                                                   |
| [Loadout OK] [Stash 92% Full] [Insurance Return 22h] [Daily 1/3] [Event 2d]     |
|---------------------------------------------------------------------------------|
| ACTION / STATUS BAR                                                             |
| Friends 3 online | Party open | Battle Pass 12/50        [CONTINUE PREP/DEPLOY] |
+---------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | mục đích | Required Content |
| :--- | :--- | :--- |
| global header | Persistent account và economy status | level, faction rep, credits, notifications, network trạng thái |
| Horizontal global nav | primary out-of-raid điểm đến map | Home, Loadout, Stash, Traders, Safe House, Quests, Profile, Settings, hiện tại selection, unread badges, disabled reasons |
| Operator showcase | Identity, loadout readability, cảm xúc anchor | operator model, hiện tại vũ khí, giáp silhouette, rotate/kiểm tra hint |
| Last raid snapshot | Explain changed trạng thái sau returning | extraction/death label, XP, loot count, rep delta, AAR action |
| Deploy panel | Readiness và risk trước commitment | mode, map, squad, queue estimate, gear giá trị, weight, insurance |
| Context cards | Next-best actions from hệ thống trạng thái | blockers, claims, full stash, event, quest progress |
| Status bar | Persistent social/progression context | friends, party, battle pass, deploy/continue CTA |

**Visual Hierarchy**

| Priority | Element | Designer yêu cầu |
| :--- | :--- | :--- |
| 1 | Deploy/Continue CTA và blocker reason | phải được dễ đọc within 2 seconds; disabled CTA must name the exact blocker |
| 2 | Operator và hiện tại kit | cách dùng size và silhouette, not only labels, to show readiness |
| 3 | Last raid hoặc recovery snapshot | Only appears khi recent trạng thái changed; collapse sau acknowledged |
| 4 | Context cards | Limit to 4-5 cards to avoid turning hub into a dashboard wall |
| 5 | LiveOps và social | Present nhưng secondary; never visually compete với deploy path |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Deploy panel | Fixed width across trạng thái; CTA position never jumps khi blockers appear |
| Blocker list | Max 3 hiển thị rõ blockers, ordered by severity; each has a deep link và plain-language fix |
| Last raid card | Shows extraction/death, XP delta, notable loot, và a single route to full AAR |
| Squad card | Shows leader, ready count, voice trạng thái, và party mismatch reason nếu blocked |
| Event strip | Shows event name, thời gian remaining, và whether it changes raid rules |
| Notification badges | Must pair icon/color với text hoặc count; no color-only trạng thái meaning |

**trạng thái & Edge Cases**

| trạng thái | UI Behavior |
| :--- | :--- |
| First session | Tutorial Raid becomes primary; locked hệ thống show short reason và unlock path |
| Return sau extraction | Show compact loot/XP recap với Move Loot và Redeploy actions |
| Return sau death | Show rebuild kit, insurance return, preset, và recovery quest actions |
| Party active | Deploy panel shows squad cards, leader status, member blockers, và ready count |
| Loadout invalid | CTA becomes Continue Preparation; first blocker receives focus/deep link |
| Stash full | Surface capacity percentage, sell junk, upgrade stash, và move items actions |
| Offline | Allow settings và local profile view; disable deploy, traders, social với reason |
| loading | Skeleton header, nav, operator area, và deploy panel separately so layout does not shift |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Navigate hub | Click horizontal global nav / number shortcuts | Shoulder tabs hoặc horizontal focus | Bottom nav hoặc drawer |
| Rotate operator | Drag hero | Right stick | Swipe hero |
| Open blocker fix | Click blocker | Focus blocker + A / Cross | Tap blocker row |
| Deploy | Click CTA / Enter khi focused | A / Cross on CTA | Sticky bottom CTA |
| Open context card | Click card | Focus card | Tap card |

Focus order: global header, horizontal global nav, deploy panel CTA, blocker list, last raid actions, context cards, header utilities.

**Designer ghi chú**

- Keep the deploy panel visually stable; cảnh báo expand inside it, not below it.
- Người chơi nên understand "Can I raid now?" trước reading any secondary card.
- cách dùng text labels for trạng thái badges such as Offline, Full, Ready, Locked, và Expired.
- Do not place shop, event, hoặc battle pass promotions above deploy readiness.

**Acceptance checklist**

- [ ] Hub shows the next best action in under 5 seconds.
- [ ] Invalid loadout, full stash, và offline trạng thái each show exact disabled reasons.
- [ ] Deploy CTA, blocker list, và squad readiness remain hiển thị rõ at desktop và mobile sizes.
- [ ] No hành động phá hủy/không hồi phục is executed directly from the hub.

---

## Operator Select

**người chơi Intent**

The người chơi wants to choose an operator based on role, ability identity, readiness, unlock status, squad fit, và cosmetics mà không losing the path back to raid preparation.

| Spec | yêu cầu |
| :--- | :--- |
| Entry points | Home operator card, Loadout operator slot, new người chơi setup, cosmetic preview link |
| Exit points | Select Operator, Back to previous màn hình, View Mastery, preview Cosmetics |
| primary CTA | Select Operator khi available và not on cooldown/injured |
| secondary actions | Favorite, compare role, preview skin, view mastery, kiểm tra ability chi tiết |
| Accessibility | Ability descriptions phải được text-dễ đọc và not icon-only |

**Expanded ASCII Wireframe**

```
+---------------------------------------------------------------------------------+
| < Back                         OPERATOR SELECT                         [Select] |
|---------------------------------------------------------------------------------|
| FILTERS / ROSTER        | OPERATOR PREVIEW                     | ROLE / ABILITY |
| Search [__________]     | +----------------------------------+ | Assault        |
| Role: All v             | | 3D OPERATOR MODEL                | | Breach Charge  |
| Owned: Owned v          | | - selected skin                  | | Cooldown Ready |
| Sort: Recommended v     | | - weapon pose                    | | Range 8m       |
|-------------------------| | - injury/cooldown badge          | | Noise High     |
| [REC] Mamba       READY | +----------------------------------+ |----------------|
| Ignition          READY | COSMETIC STRIP                       | Strengths      |
| Sonar             READY | [Default] [Urban] [Prestige] [Lock]  | Room clear     |
| Suture            HURT  |                                      | Weakness       |
| Bastion           LOCK  | SQUAD FIT                            | Long cooldown  |
|-------------------------| Current squad: Assault / Recon / --  |----------------|
| ACTION BAR              | Recommendation: Support would help   | Unlock 8/12    |
| [Compare] [Favorite] [Preview Skin]                         [SELECT OPERATOR]   |
+---------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | mục đích | Required Content |
| :--- | :--- | :--- |
| Filter rail | Reduce roster scanning chi phí | role, owned/locked, favorite, search, recommended sort |
| Roster list | Fast operator comparison | name, role tag, readiness, lock/cooldown/injury badge |
| preview | cảm xúc identity và cosmetic inspection | full model, hiện tại vũ khí pose, skin, rotate affordance |
| Ability panel | Explain gameplay identity | role, active ability, cooldown, range, risk, counterplay summary |
| Squad fit | giúp team composition | hiện tại squad roles, recommendation, duplicate role cảnh báo |
| Action bar | Keep selection path stable | compare, favorite, preview skin, select |

**Visual Hierarchy**

| Priority | Element | Designer yêu cầu |
| :--- | :--- | :--- |
| 1 | Selected operator và Select CTA | Selection phải được unambiguous in roster và preview |
| 2 | Role và ability summary | cách dùng text labels for role, cooldown, và readiness |
| 3 | Locked/injured trạng thái | Show yêu cầu hoặc recovery route next to disabled CTA |
| 4 | Cosmetics | secondary to gameplay selection unless entered from cosmetic preview |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Roster row | Includes role, readiness, ownership/lock trạng thái, favorite indicator, và recommendation marker |
| Ability card | Shows plain-language effect, cooldown, range, cách dùng case, và chính limitation |
| Locked operator | Shows unlock yêu cầu, progress, và allowed preview/trial trạng thái nếu available |
| Injured/cooldown operator | Shows remaining thời gian hoặc required recovery action và whether selection is blocked |
| cosmetic strip | Locked cosmetics show yêu cầu; selection preview does not equip until confirmed |

**trạng thái & Edge Cases**

| trạng thái | UI Behavior |
| :--- | :--- |
| available | Select CTA active; ability và preview fully hiển thị rõ |
| Recommended | Roster badge explains why, such as squad role gap hoặc quest relevance |
| Locked | CTA disabled; panel shows level, quest, purchase, hoặc mastery yêu cầu |
| Injured/cooldown | CTA disabled hoặc cảnh báo based on tuning; recovery deep link hiển thị rõ |
| cosmetic preview | Action bar changes to Equip/Back nếu already selected operator |
| No results | empty roster trạng thái offer rõ Filters |
| loading | Roster skeleton và preview placeholder keep panel sizes fixed |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse roster | Mouse wheel / arrow keys | D-pad / left stick | Swipe list |
| kiểm tra ability | Hover / click ability card | Focus card | Tap info row |
| Rotate model | Drag preview | Right stick | Swipe model |
| Change filters | Click dropdown | Shoulder focus + A / Cross | Filter chips drawer |
| Select | Click / Enter | A / Cross | Sticky CTA |

Focus order: roster, selected preview, ability panel, squad fit, action bar.

**Designer ghi chú**

- Do not hide readiness behind color alone; every blocked row needs a dễ đọc label.
- Roster row height should stay stable khi badges change.
- The ability panel nên được dễ đọc mà không opening a modal.
- cosmetic preview must never make the người chơi think the operator has been selected unless the CTA confirms it.

**Acceptance checklist**

- [ ] Locked, injured, recommended, và selected operators are visually distinct với text labels.
- [ ] Ability identity, cooldown, range, và limitation are hiển thị rõ on the chi tiết panel.
- [ ] Select CTA clearly explains why it is disabled khi blocked.
- [ ] Controller focus can reach filters, roster, preview, và CTA predictably.

---

## Loadout Workbench

The chi tiết preparation rules live in [Loadout Preparation](../GameDesign/LoadoutPreparation.md). This UI group owns the màn hình trạng thái contract và platform layout.

**người chơi Intent**

The người chơi wants to build a valid raid kit, understand risk, resolve blockers, và move toward mission selection mà không accidentally deploying với missing đạn, excessive weight, hoặc uninsured giá trị.

| Spec | yêu cầu |
| :--- | :--- |
| Entry points | Home deploy blocker, Home Loadout, Operator Select return, Quest item deep link |
| Exit points | Ready to Map, Back Home, Stash, Insurance, Presets, Mission tab |
| primary CTA | Ready to Map nếu valid; Fix Loadout nếu blocked |
| secondary actions | Equip, move, kiểm tra, compare, insure, preset apply/save, filter compatible items |
| Destructive actions | Discard, sell, overwrite preset, remove insured item require confirmation |

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| < Back                      LOADOUT WORKBENCH                         Presets v|
|--------------------------------------------------------------------------------|
| OPERATOR / GEAR      | STASH + COMPATIBLE ITEMS               | MISSION / RISK |
| +------------------+ | Search [_________] Filter v Sort v     | Mode: Solo     |
| | Operator Model   | | Category: Weapons Ammo Meds Keys       | Map: Sector 7  |
| +------------------+ |----------------------------------------| Squad: 1/4     |
| Primary  [AK-74M]   | GRID 12 x N                             | Quests: 2      |
| Sidearm  [Empty]    | +--+--+--+--+--+--+--+--+---+--+--+--+  |----------------|
| Armor    [Lv3 85%]  | |Rifle    |Med|Ammo|Ammo|Key|  |  |  |  | Gear 125K      |
| Helmet   [Empty]    | |         |   |    |    |   |  |  |  |  | Weight 24/40kg |
| Rig      [12 slots] | +--+--+--+--+--+--+--+--+---+--+--+--+  | Insured 4/6    |
| Pack     [24 slots] | Selected: 5.45 BP x60                   | Ammo: OK       |
| Secure   [4 slots]  | Compare: +Pen -Cost  Fits: AK-74M       | Warning: 1     |
|---------------------+-----------------------------------------+----------------|
| WARNING LANE: [!] Sidearm empty optional | [!] 2 items uninsured [Insure All]  |
|--------------------------------------------------------------------------------|
| ACTION BAR: Value 125K | Weight 24/40kg | Capacity 31/40 | [FIX] [READY TO MAP]|
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | mục đích | Required Content |
| :--- | :--- | :--- |
| Gear column | Show equipped kit và slot validity | operator, vũ khí slots, giáp, helmet, rig, pack, secure container |
| Stash grid | source of available items | search, filters, sort, compatible highlight, selected item summary |
| Mission/risk panel | Keep deployment context hiển thị rõ | mode, map, squad, quests, gear giá trị, weight, insurance, đạn trạng thái |
| cảnh báo lane | Make blockers actionable | severity icon, blocker text, cách sửa trực tiếp action |
| Action bar | Persistent readiness contract | giá trị, weight, capacity, fix/ready CTA |

**Visual Hierarchy**

| Priority | Element | Designer yêu cầu |
| :--- | :--- | :--- |
| 1 | Invalid slot hoặc blocking cảnh báo | cách dùng direct label và focus target; do not bury in tooltip |
| 2 | Gear slots | Slot trạng thái phải được scannable by silhouette, name, và status |
| 3 | Stash compatibility | Compatible items highlighted mà không hiding incompatible inventory |
| 4 | Risk footer | Persistent giá trị, weight, capacity, insurance; no layout jump |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Gear slot | Shows item name, durability/đạn nếu relevant, slot restriction, và cảnh báo trạng thái |
| Stash item tile | Shows footprint, category icon, stack count, durability nếu relevant, rarity/tier, FIR, quest, protected, insured, contraband, locked, equipped, và compatibility marker |
| Selected item summary | Shows stats delta, giá trị, weight, durability, compatibility, insurance eligibility, quest/FIR/protected flags, và allowed actions |
| Gear comparison panel | Gọi tên trade-off bằng text: capacity vs weight, armor class vs mobility, durability vs repair cost, insured vs ineligible |
| cảnh báo lane | Orders blockers first, cảnh báo second, suggestions third; max 3 hiển thị rõ với View All |
| Preset control | Shows Save, Apply, Rename, Delete; overwrite/delete require confirmation |
| Ready CTA | Active only khi required rules pass; disabled label names first blocker |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Missing vũ khí | Block Ready; focus primary vũ khí slot và filter compatible vũ khí |
| Missing đạn | Warn hoặc block per tuning; show compatible đạn filter và đạn count needed |
| Overweight | Block hoặc confirm per tuning; show weight source và suggested removals |
| High giá trị | cảnh báo với explicit gear giá trị; allow confirmation nếu no blocker |
| Uninsured eligible items | cảnh báo với Insure All và item count |
| Quest item missing | cảnh báo với quest chi tiết và stash/trader/map deep link |
| Stash full trong khi move | Reject move, show capacity, offer stash upgrade/sell junk |
| empty stash | Explain source paths: traders, starter kit, raid, quest rewards |
| Broken required gear | Block Ready; route tới repair, replacement, hoặc remove item |
| Low durability weapon | Warning với malfunction/durability risk và repair route |
| Contraband item | Show restricted deploy/sell/insurance behavior trước Ready |
| Locked item | Disable invalid action và show unlock/protection reason |
| Invalid container item | Block Ready/move; show container restriction và valid target |
| Preset apply failure | List missing items, substitutions, cost, và stash capacity result |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop hoặc click source then slot | Grid cursor + A / Cross | Tap item then target |
| Rotate item | R while moving | Y / Triangle | Rotate button near item |
| kiểm tra item | Right-click / hover chi tiết | Hold focus | Long press |
| Quick equip | Ctrl-click | Hold A / Cross | Double tap |
| Filter compatible | Click cảnh báo/filter | Focus cảnh báo + A / Cross | Tap cảnh báo chip |

Mobile layout uses tabs: Operator, Stash, Mission. The risk summary và Ready CTA remain pinned above the bottom safe area.

**Designer ghi chú**

- Treat the footer as the người chơi's contract: it should always tell giá trị, weight, insurance, và readiness.
- Incompatible items may be dimmed, nhưng should remain discoverable và inspectable.
- Grid cell size phải được stable; badges cannot resize item tiles.
- Every blocked Ready trạng thái must provide one cách sửa trực tiếp path.

**Acceptance checklist**

- [ ] Missing vũ khí, missing đạn, overweight, uninsured giá trị, và quest item missing trạng thái are represented.
- [ ] Blocker, warning, và advisory severities are visually distinct and text-labeled.
- [ ] Broken gear, low durability, contraband, locked, insured/uninsured, và invalid container states are represented.
- [ ] Gear comparison explains trade-offs bằng text, không chỉ green/red deltas.
- [ ] Stash grid supports item movement mà không precision-only interactions.
- [ ] Ready CTA never activates while a blocking validation trạng thái is present.
- [ ] Risk summary remains hiển thị rõ while duyệt stash items.

---

## Stash

**người chơi Intent**

The người chơi wants to store, sort, search, move, sell, và kiểm tra items quickly while understanding capacity pressure, item giá trị, item mục đích, và whether an item is safe to discard hoặc sell.

| Spec | yêu cầu |
| :--- | :--- |
| Entry points | Home, Loadout, post-raid loot transfer, trader sell flow, quest item deep link |
| Exit points | Move to Loadout, Sell, Turn In, kiểm tra, upgrade Stash, Back |
| primary CTA | Contextual: Equip, Move, Sell, cách dùng, Turn In, hoặc kiểm tra |
| secondary actions | Auto-sort, filter, search, favorite, tag junk, split stack, rotate, lock item |
| Destructive actions | Discard và sell protected/quest/high-giá trị items require confirmation |

**Stash Information Architecture**

| Surface | Requirement |
| :--- | :--- |
| Filter rail | Category, rarity/tier, FIR, quest, protected, insured, contraband, damaged, value, saved filters |
| Grid | Stable cells, item footprints, stacks, empty cells, valid target preview, rotate-needed preview |
| Selected item panel | Name, category, tier/rarity, durability, value, weight, footprint, ownership flags, related quest/trader/craft |
| Capacity summary | Used/total cells, incoming overflow, large-item pressure, locked/protected count, stash value |
| Overflow / reward inbox lane | Temporary holding cho post-raid, support, reward, hoặc sync items với source context |
| Action bar | Move, equip, sell, use, inspect, split, rotate, protect, discard; destructive actions visually separated |

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| < Back                              STASH                    Search [_________]|
|--------------------------------------------------------------------------------|
| FILTER RAIL       | GRID 12 x N                                      | INFO    |
| All               | +--+--+--+--+--+--+--+--+----+----+--+--+        | AK-74M  |
| Weapons           | |Rifle    |Med|Ammo|Ammo|Key |Junk|  |  |        | Rifle   |
| Armor             | |         |   |x60 |x30 |FIR |    |  |  |        | 85% Dur |
| Ammo              | +--+--+--+--+--+--+--+--+--+--+--+--+            | 45,000  |
| Meds              | |Armor |Helmet|       Empty Cells                | 4x2     |
| Quest             | +--+--+--+--+--+--+--+--+--+--+--+--+            | FIR: No |
| Junk              | Capacity 145 / 200  Value 2.45M  Locked 12       | Locked  |
|-------------------+--------------------------------------------------|---------|
| QUICK TOOLS: [Auto Sort] [Sell Junk] [Find Quest Items] [Upgrade Stash]        |
| WARNING LANE: [!] Stash 92% full. Sell junk, use containers, or upgrade.       |
|--------------------------------------------------------------------------------|
| ACTION BAR: Selected 1 item | [Move to Loadout] [Sell] [Inspect] [Discard]     |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | mục đích | Required Content |
| :--- | :--- | :--- |
| Filter rail | Fast category narrowing | all categories, saved filters, quest/protected toggles |
| Grid | Spatial inventory management | item footprints, stacks, empty cells, invalid placement preview |
| Info panel | Explain selected item | name, category, durability, giá trị, footprint, FIR, protected/quest trạng thái |
| Quick tools | Resolve capacity và sorting problems | auto sort, sell junk, find quest items, upgrade stash |
| cảnh báo lane | Surface capacity và invalid moves | full stash, protected item cảnh báo, filter no results |
| Action bar | Contextual item actions | move, equip, sell, cách dùng, kiểm tra, discard |

**Visual Hierarchy**

| Priority | Element | Designer yêu cầu |
| :--- | :--- | :--- |
| 1 | Selected item và valid target | Selection outline và target preview phải được unmistakable |
| 2 | Capacity pressure | Capacity count và cảnh báo lane hiển thị rõ mà không scrolling |
| 3 | Protected/FIR/quest trạng thái | Badges must include dễ đọc labels hoặc accessible text |
| 4 | Bulk tools | Useful nhưng secondary; avoid overwhelming normal move flow |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Item tile | Shows footprint, stack count, category shape/icon, durability nếu relevant, rarity/tier, và badges for FIR, quest, protected, insured, contraband, locked, equipped |
| Grid target preview | Shows valid, invalid, rotate-needed, và blocked-by-item trạng thái |
| Info panel | Gives enough chi tiết to decide keep/sell/equip mà không opening kiểm tra modal |
| Sell junk | Lists estimated giá trị và excludes quest/protected/favorited items by default |
| Search | Searches item name, category, đạn caliber, quest tag, và trader relevance |
| Full stash cảnh báo | offer cụ thể actions: sell junk, cách dùng container, upgrade, filter large items |
| Destructive confirmation | Names item, value, flags, và consequence for protected, quest, high-value, insured, hoặc contraband items |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| empty stash | Explain no items; offer traders, starter kit, hoặc raid path |
| Full stash | Persistent cảnh báo; invalid incoming moves explain needed space |
| Filter no results | Show rõ Filters và explain active filter stack |
| Item locked/protected | Disable destructive actions unless confirmation path is allowed |
| Quest item selected | Show related quest, turn-in trạng thái, và whether FIR is required |
| Incoming loot overflow | Show temporary holding lane và required resolution trước exit |
| loading | Grid skeleton preserves cell dimensions và filter rail width |
| Pending sync | Disable duplicate move/sell/claim actions và show finalizing state |
| Contraband selected | Show sale, trade, insurance, deploy, hoặc mode restriction trong info panel |
| Damaged/broken item | Show repair route, effective value, và deploy restriction nếu applicable |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop | Grid cursor + A / Cross | Tap item then target |
| Rotate | R while dragging | Y / Triangle | Rotate button |
| Quick equip | Ctrl-click | Hold A / Cross | Double tap |
| Context menu | Right-click | Hold focus | Long press |
| Search | Ctrl-F | Y / Triangle opens keyboard | Search field |

Focus order: search, filter rail, grid, info panel actions, quick tools, action bar.

**Designer ghi chú**

- Capacity và selected item chi tiết must remain hiển thị rõ while scrolling large stashes.
- Item badges không nên shrink item names below dễ đọc size.
- The discard action nên được visually separated from common positive actions.
- Dense grid is acceptable, nhưng interaction targets must remain generous on touch.

**Acceptance checklist**

- [ ] empty, full, filter-empty, locked item, và quest item trạng thái are designed.
- [ ] Item info panel shows giá trị, footprint, tier/rarity, durability, FIR/protected/insured/contraband state, và allowed actions.
- [ ] Overflow, pending sync, damaged/broken item, và contraband states are designed.
- [ ] Mouse, controller, và touch can move và rotate items.
- [ ] Destructive actions warn for protected, quest, hoặc high-giá trị items.

---

## Traders / Market

**người chơi Intent**

The người chơi wants to mua, sell, barter, và turn in items while understanding giá, reputation locks, stash capacity, missing barter parts, và whether a transaction is risky hoặc irreversible.

| Spec | yêu cầu |
| :--- | :--- |
| Entry points | Home traders, stash sell action, quest turn-in deep link, safe house material need |
| Exit points | purchase, Sell, Trade, Turn In, kiểm tra Item, Back |
| primary CTA | purchase, Sell Selected, Trade, hoặc Turn In based on mode |
| secondary actions | Filter, sort, kiểm tra, compare, pin missing item, switch trader |
| Destructive actions | Selling premium, high-giá trị, protected, hoặc quest-critical items requires confirmation |

**Expanded ASCII Wireframe**

```
+----------------------------------------------------------------------------------+
| < Back                              TRADERS             Credits 425K Rep 3       |
|----------------------------------------------------------------------------------|
| TRADER LIST        | OFFERS / INVENTORY                         | YOUR OFFER     |
| > Viktor Koval     | Mode Tabs: [Buy] [Sell] [Barter] [Turn-in] | Credits 425K   |
|   Dr. Sera         | Search [________] Filter: Ammo v Sort Price| Stash 145/200  |
|   Scrap Union      |--------------------------------------------|----------------|
|--------------------| AK-74M Rifle        45,000   In stock 3    | Selected: 2    |
| TRADER PROFILE     | 5.45 BP x60            800   Rep Lv3       | AK-74M         |
| Rep Level 3        | Medkit               2,500   In stock 12   | Medkit         |
| Next: 12,000 spend | [LOCKED Lv4] Armor   85,000   Need Rep 4   |----------------|
| Quote: Fair trades |--------------------------------------------| Total 47,500   |
| Daily reset 03:14  | DETAILS: selected offer stats, limits,     | Stash after    |
|                    | compatibility, required barter items       | 147/200        |
|----------------------------------------------------------------------------------|
| WARNING LANE: [!] Purchase would exceed stash capacity by 2 cells.               |
| ACTION BAR: [Inspect] [Compare] [Clear]                         [PURCHASE]       |
+----------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | mục đích | Required Content |
| :--- | :--- | :--- |
| Trader list | Switch vendor context | trader name, faction, unread/quest badge, availability |
| Trader profile | Explain access và progression | rep level, next unlock yêu cầu, reset timer, flavor line |
| offer list | Browse mua/sell/barter/turn-in candidates | mode tabs, search, filters, item row, giá, stock, lock reason |
| chi tiết strip | Explain selected offer | stats, compatibility, limits, barter checklist, item cảnh báo |
| Your offer | Confirm transaction summary | credits/funds, selected items, total, stash sau transaction |
| cảnh báo lane | Prevent failed hoặc regretted transaction | stash full, insufficient funds, protected item, missing barter |

**Visual Hierarchy**

| Priority | Element | Designer yêu cầu |
| :--- | :--- | :--- |
| 1 | Mode tab và CTA | mua/Sell/Barter/Turn-in mode phải được impossible to confuse |
| 2 | giá/total và failure reason | Transaction chi phí và blocker hiển thị rõ trước CTA |
| 3 | Rep lock và stock | Locked rows remain hiển thị rõ với exact yêu cầu |
| 4 | Trader identity | Flavor supports worldbuilding nhưng does not obscure commerce data |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| offer row | Shows name, category, giá/giá trị, stock/limit, lock trạng thái, và compatibility tag |
| Mode tabs | Persist selected mode; changing mode clears incompatible selections sau cảnh báo nếu needed |
| Your offer panel | Shows selected count, total, credits/funds delta, stash capacity kết quả, và CTA |
| Barter checklist | Shows required items, owned count, FIR yêu cầu, và missing item pin action |
| Sell cảnh báo | Flags protected, quest, insured, equipped, hoặc high-giá trị items trước sale |
| Confirmation dialog | Required for premium currency, high-giá trị gear, quest-critical items, và irreversible trades |

**trạng thái & Edge Cases**

| trạng thái | UI Behavior |
| :--- | :--- |
| Insufficient funds | CTA disabled; credits/funds shortage shown in Your offer panel |
| Rep locked | Row disabled; yêu cầu và unlock route hiển thị rõ |
| Stash full | CTA disabled hoặc cảnh báo per transaction; show capacity sau transaction |
| Barter missing items | checklist highlights missing item và offer stash/trader/quest route |
| offer expired | Row disabled; reset timer shown; selected expired offer removed với message |
| Sale confirmation | Modal names item, giá trị, protected/quest status, và final action |
| Offline | Disable transaction modes; allow duyệt cached trader profiles nếu supported |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch trader | Click trader | D-pad / shoulder group | Trader drawer |
| Change mode | Click tab | Bumper tabs | Segmented tabs |
| Select offer | Click row | Focus row + A / Cross | Tap row |
| kiểm tra item | Right-click / chi tiết | Hold focus | Long press |
| Confirm transaction | Click CTA | A / Cross on CTA | Sticky CTA |

Focus order: trader list, mode tabs, offer list, chi tiết strip, your offer panel, CTA.

**Designer ghi chú**

- mua, Sell, Barter, và Turn-in need distinct text labels, not only tab color.
- The người chơi's total chi phí và stash capacity kết quả phải được hiển thị rõ trước purchase.
- Confirmation copy should name the item và consequence, not cách dùng generic "Are you sure?" text.
- Locked offer should teach progression instead of disappearing.

**Acceptance checklist**

- [ ] mua, sell, barter, và turn-in modes are visually và behaviorally distinct.
- [ ] Insufficient funds, rep lock, stash full, missing barter, và sale confirmation trạng thái are specified.
- [ ] High-giá trị, premium, protected, và quest-critical transactions require confirmation.
- [ ] The transaction CTA always matches the selected mode.

---

## Safe House Modules

**người chơi Intent**

The người chơi wants to understand base progression, upgrade benefits, crafting/repair timers, insurance returns, và material blockers mà không losing track of what can be claimed hoặc improved now.

| Spec | yêu cầu |
| :--- | :--- |
| Entry points | Home safe house, stash upgrade prompt, insurance return card, crafting material deep link |
| Exit points | upgrade, Start Craft, claim, Repair, Track Materials, Back |
| primary CTA | upgrade, Start Craft, claim, hoặc Repair based on selected module trạng thái |
| secondary actions | View prerequisites, pin materials, kiểm tra queue, cancel/collect craft nếu supported |
| Destructive actions | Spend materials/currency, cancel craft, discard return require confirmation where applicable |

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| < Back                              SAFE HOUSE                    Timers 3     |
|--------------------------------------------------------------------------------|
| MODULE MAP / ROOMS                                      | MODULE DETAIL        |
| +----------+     +----------+     +----------+          | Stash Room Lv2       |
| | Lounge   |-----| Stash    |-----| Workbench|          | Status: Upgradeable  |
| | Passive  |     | Lv2 *    |     | Crafting |          |----------------------|
| +----------+     +----------+     +----------+          | Benefit Next Lv3:    |
|      |                 |                |               | +50 stash slots      |
| +----------+     +----------+     +----------+          | Unlock: Item Case    |
| | Radio    |-----| Med Bay  |-----| Generator|          |----------------------|
| | Locked   |     | Craft 12m|     | Fuel 65% |          | Cost: 50K credits    |
| +----------+     +----------+     +----------+          | 10 Metal Parts 7/10  |
|---------------------------------------------------------| 2 Wires 2/2          |
| QUEUE / INBOX                                           | Prereq: Generator OK |
| Med Craft 12m | Ammo Craft Ready | Insurance Return 22h |----------------------|
| WARNING LANE: [!] Missing 3 Metal Parts. [Track Materials]                     |
|--------------------------------------------------------------------------------|
| ACTION BAR: [View Benefits] [Track Materials] [Confirm Spend]       [UPGRADE]  |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | mục đích | Required Content |
| :--- | :--- | :--- |
| Module map | Spatial overview of base progression | rooms, level, locked/ready/in-progress trạng thái, connections |
| Module chi tiết | Explain selected module | hiện tại level, status, next benefit, chi phí, prerequisites, CTA |
| Queue/inbox | Surface timers và claims | crafting, repairs, insurance returns, ready-to-claim badge |
| cảnh báo lane | Explain blockers | missing materials, stash full on claim, queue full, prerequisite locked |
| Action bar | Commit hoặc track next action | view benefits, track materials, confirm spend, upgrade/claim |

**Visual Hierarchy**

| Priority | Element | Designer yêu cầu |
| :--- | :--- | :--- |
| 1 | claim-ready và upgrade-ready modules | Must stand out với text và icon, not color alone |
| 2 | Selected module benefits/chi phí | Benefit must appear trước spend CTA |
| 3 | Missing materials/prerequisites | Show owned/required counts và direct tracking route |
| 4 | Long-term map | Keep dễ đọc nhưng secondary to selected module chi tiết |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Module node | Shows name, level, status, active timer/claim badge, locked reason nếu selected |
| chi tiết panel | Shows hiện tại benefit, next benefit, chi phí, yêu cầu, và spend confirmation trạng thái |
| Material row | Shows item name, owned/required count, source hint, và pin/track action |
| Timer chip | Shows remaining thời gian, ready trạng thái, và điểm đến module |
| Insurance inbox | Shows returned item count, expiry risk, stash capacity kết quả, và claim CTA |
| Confirmation | Spending currency/materials names chi phí và resulting benefit trước final commit |

**trạng thái & Edge Cases**

| trạng thái | UI Behavior |
| :--- | :--- |
| Module locked | chi tiết panel shows prerequisite chain và next reachable step |
| upgrade available | CTA active only nếu materials, currency, và prerequisites pass |
| Missing materials | CTA disabled; material rows show owned/required counts và tracking |
| upgrade in progress | CTA disabled; timer và completion kết quả hiển thị rõ |
| Craft queue full | Start Craft disabled; show queue capacity và claim/cancel options |
| Timer complete | Ready badge on map và queue; claim CTA promoted |
| Stash full on claim | claim blocked; show required space và route to stash |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Select module | Click node | D-pad module graph | Tap room card |
| kiểm tra material | Hover/click row | Focus row | Tap material |
| Track material | Click Track | A / Cross on focused row | Tap track chip |
| claim timer | Click ready chip | Focus timer + A / Cross | Tap queue card |
| Confirm spend | Click CTA + modal | A / Cross + confirm | Sticky CTA + modal |

Mobile layout uses tabs: Modules, chi tiết, Queue. claim-ready timers should appear as a persistent top summary.

**Designer ghi chú**

- Always show benefit trước chi phí to make upgrade giá trị rõ.
- Module map can be stylized, nhưng text labels must remain dễ đọc.
- Timers need absolute trạng thái labels: In Progress, Ready, Expiring Soon, Locked.
- claim actions must explain where items go và what blocks them.

**Acceptance checklist**

- [ ] upgrade benefits are hiển thị rõ trước chi phí commitment.
- [ ] Locked modules show the next prerequisite và reachable step.
- [ ] Missing materials show owned/required counts và tracking actions.
- [ ] Timers show remaining thời gian, completion, expiry risk, và claim điểm đến.

---

## Quest Board

**người chơi Intent**

The người chơi wants to choose useful objectives, understand where to go, know what item hoặc extraction yêu cầu matters, track objectives into raid, và turn in rewards mà không confusion.

| Spec | yêu cầu |
| :--- | :--- |
| Entry points | Home quest card, trader turn-in, map quest hint, post-raid progress recap |
| Exit points | Track, Turn In, Show on Map, Find Item in Stash, Back |
| primary CTA | Track Quest for active/incomplete; Turn In for ready quests |
| secondary actions | Pin objective, show on map, find required item, view faction, abandon nếu supported |
| Destructive actions | Abandon quest requires confirmation và failure consequence text |

**Expanded ASCII Wireframe**

```
+---------------------------------------------------------------------------------+
| < Back                              QUEST BOARD                   Faction v     |
|---------------------------------------------------------------------------------|
| QUEST LIST              | QUEST DETAIL                            | REWARDS     |
| Filters: Active v       | Supply Run                              | XP 500      |
| Search [________]       | Faction: Salvage  Status: Tracked       | Rep +0.05   |
|-------------------------|-----------------------------------------| 12,000 Cr   |
| [TRACKED] Supply Run    | OBJECTIVES                              | Medkit x1   |
| [READY]   Lab Rat       | [x] Find rations 3/3                    |-------------|
| [NEW]     Signal Lost   | [ ] Extract from Sector 7               | TURN-IN     |
| [LOCKED]  Black Box     | [ ] Deliver to Salvage trader           | Required:   |
| [FAILED]  Old Debt      |-----------------------------------------| Rations FIR |
|-------------------------| LOCATION / RISK                         | Owned: 3/3  |
| QUEST CHAIN             | Sector 7 / Warehouse / Requires extract | [TURN IN]   |
| 1 Supply Run > 2 Lab    | Failure loses carried quest item        |             |
|---------------------------------------------------------------------------------|
| ACTION BAR: [Track] [Show on Map] [Find Item in Stash] [Abandon]                |
+---------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | mục đích | Required Content |
| :--- | :--- | :--- |
| Quest list | Compare và filter objectives | status badge, faction, location, reward preview, lock/failure trạng thái |
| Quest chi tiết | Explain completion yêu cầu | objectives, counts, extraction/FIR rules, location, risk |
| Reward panel | Make giá trị và turn-in readiness rõ | XP, rep, credits, items, unlocks, required hand-in items |
| Quest chain | Show progression context | prior/next quest, unlock status, faction path |
| Action bar | Route to next action | track, map, stash item search, abandon |

**Visual Hierarchy**

| Priority | Element | Designer yêu cầu |
| :--- | :--- | :--- |
| 1 | Objective status và primary CTA | Ready-to-turn-in phải được unmistakable |
| 2 | Required item/extraction condition | FIR, extraction, location, và delivery rules phải được explicit |
| 3 | Rewards | Always hiển thị rõ for selected quest; secondary to yêu cầu |
| 4 | Chain/faction context | Helpful nhưng not required for immediate completion |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Quest row | Shows title, status, faction, location tag, và progress count |
| Objective checklist | Shows exact count, completion trạng thái, FIR/extract yêu cầu, và failure risk |
| Location block | Shows map, sub-location, access/lock status, và Show on Map action |
| Reward panel | Shows all rewards và whether inventory space is needed |
| Turn-in panel | Shows required items, owned count, FIR validity, và wrong-item reason |
| Abandon action | Visually separated và confirmed với consequence text |

**trạng thái & Edge Cases**

| trạng thái | UI Behavior |
| :--- | :--- |
| available | Show faction, location, risk, rewards, và Track CTA |
| Tracked | Pin objective to HUD và tactical map; row shows Tracked label |
| Ready to turn in | Promote Turn In CTA; highlight required item source và reward |
| Missing item | Deep link to stash filter hoặc trader nếu known; show owned/required count |
| failed | Explain failed condition, lost items, retry availability, và next step |
| Locked | Show prerequisite quest, level, faction, map, hoặc trader yêu cầu |
| Reward inventory full | Turn In blocked; show required stash space và stash route |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse quests | Mouse wheel / click | D-pad list | Swipe list |
| Filter status | Click filters | Shoulder tabs | Top tabs |
| Track quest | Click CTA | A / Cross on CTA | Sticky CTA |
| Show on map | Click action | Focus action | Tap action |
| Find item | Click item yêu cầu | Focus item row | Tap item row |

Mobile layout uses tabs: Active, available, Completed, Rewards. chi tiết và reward panels stack below the selected quest.

**Designer ghi chú**

- Status labels nên được words: New, Tracked, Ready, Locked, failed.
- Quest risk copy nên được short và direct, especially for extraction-required objectives.
- Người chơi nên not need to infer FIR validity from icon color.
- Turn-in should never accept a wrong item silently; show exact reason.

**Acceptance checklist**

- [ ] available, tracked, ready, missing item, failed, và locked trạng thái are designed.
- [ ] FIR, extraction, delivery, location, và reward yêu cầu are explicit.
- [ ] Quest board can deep link to stash, map, trader, và HUD tracking.
- [ ] Abandon has confirmation và consequence text.

---

## người chơi Profile

**người chơi Intent**

The người chơi wants to review identity, stats, achievements, cosmetics, titles, và privacy settings, và to understand what other Người chơi có thể see.

| Spec | yêu cầu |
| :--- | :--- |
| Entry points | Home profile, squad member kiểm tra, social profile link, post-raid người chơi card |
| Exit points | Equip Title, Equip cosmetic, View Match History, Privacy Settings, Back |
| primary CTA | Equip selected title/cosmetic hoặc View Stats depending selected tab |
| secondary actions | Compare seasons, kiểm tra achievements, view commendations, report safety |
| Privacy | Respect streamer mode by hiding names, IDs, invite codes, và sensitive social status |

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| < Back                            PLAYER PROFILE                  Privacy v    |
|--------------------------------------------------------------------------------|
| IDENTITY CARD           | CAREER STATS                         | COSMETICS     |
| +--------------------+  | Season: Current v                    | Title v       |
| | Banner / Avatar    |  | Extractions: 42%                     | Frame v       |
| | Name: Kai          |  | Raids: 128                           | Badge v       |
| | Level: 12          |  | PMC Kills: 84                        | Emote v       |
| | Karma: Honorable   |  | Survival Time: 31m avg               | Operator Skin |
| | Platform: PC       |  | Favorite Operator: Sonar             |---------------|
| +--------------------+  | Rank: Silver II                      | SELECTED ITEM |
| Privacy: Friends       |---------------------------------------| Urban Frame   |
| Streamer: Off          | ACHIEVEMENTS / HISTORY / SAFETY       | Owned         |
|------------------------| [Achievements] [Match History]        | [EQUIP FRAME] |
| COMMENDATIONS          | [Commendations] [Report Safety]       |               |
| Helpful 24  Leader 12  | Recent: Extracted / Sector 7 / 18m    |               |
|--------------------------------------------------------------------------------|
| ACTION BAR: [Edit Banner] [Equip Title] [Privacy Settings] [Copy Invite Code]  |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | mục đích | Required Content |
| :--- | :--- | :--- |
| Identity card | Establish public profile identity | avatar, banner, name, level, platform, title, karma/faction tier |
| Career stats | Show performance và progression | extraction rate, raids, kills, survival thời gian, favorite operator, seasonal rank |
| Cosmetics panel | Equip personalization | title, frame, badge, emote, skins, selected cosmetic chi tiết |
| History/safety tabs | Support review và moderation | achievements, match history, commendations, report safety |
| Privacy controls | Explain visibility | public/friends/private, streamer mode, hidden fields |
| Action bar | Common profile actions | edit banner, equip, privacy settings, copy invite code |

**Visual Hierarchy**

| Priority | Element | Designer yêu cầu |
| :--- | :--- | :--- |
| 1 | người chơi identity và privacy trạng thái | Viewer must know whose profile và visibility mode |
| 2 | cốt lõi stats | cách dùng dễ đọc labels và avoid unexplained abbreviations |
| 3 | Equipped cosmetics | Show hiện tại equipped trạng thái trước available alternatives |
| 4 | Safety/reporting | available nhưng not visually dominant on own profile |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Identity card | Shows public-facing name, title, level, platform, và streamer-mode substitutions |
| Stat row | Shows label, giá trị, timeframe/season, và comparison only nếu available |
| cosmetic selector | Shows owned/locked/equipped trạng thái và yêu cầu for locked cosmetics |
| Achievement tile | Shows name, progress, reward, unlock date nếu achieved |
| Match history row | Shows map, outcome, duration, squad size, và privacy-safe participant display |
| Privacy dropdown | Explains exactly which fields are public, friends-only, hoặc hidden |

**trạng thái & Edge Cases**

| trạng thái | UI Behavior |
| :--- | :--- |
| Own public profile | All editable areas hiển thị rõ; privacy controls active |
| Viewing friend | Edit controls hidden; friend-safe stats và invite actions hiển thị rõ |
| Private profile | Hide stats/history; show privacy message và allowed actions |
| Streamer mode | Replace name/ID/invite code và sensitive social status với safe aliases |
| Seasonal reset | Show previous season archive và hiện tại season empty/starting trạng thái |
| No achievements | empty trạng thái explains achievement sources và recommends one active mục tiêu |
| Locked cosmetic | Shows yêu cầu và preview availability |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch tab | Click tab | Bumpers | Segmented tabs |
| Equip cosmetic | Click item + CTA | Focus item + A / Cross | Tap item + sticky CTA |
| Change privacy | Dropdown | Focus dropdown | Privacy sheet |
| kiểm tra history | Click row | Focus row | Tap row |
| Copy invite code | Click action | Action bar focus | Tap action |

Focus order: identity card, privacy control, stat tabs, cosmetic selector, selected cosmetic CTA, action bar.

**Designer ghi chú**

- Profile can be expressive, nhưng private/streamer trạng thái phải được unmistakable.
- Do not expose IDs, invite codes, party status, hoặc match history khi privacy hides them.
- Locked cosmetics should motivate mà không looking like a required purchase path.
- Keep safety/report controls discoverable và plain.

**Acceptance checklist**

- [ ] Own, friend, private, streamer mode, seasonal reset, no achievement, và locked cosmetic trạng thái are specified.
- [ ] Privacy controls trạng thái exactly what information is hiển thị rõ.
- [ ] Equipped cosmetic và selected cosmetic are visually distinct.
- [ ] Sensitive identity fields are hidden under streamer mode.

---

## Analytics

These metrics validate whether the màn hình designs reduce friction và clarify risk. chi tiết event schemas belong in technical documentation.

| Metric | Target / cách dùng |
| :--- | :--- |
| thời gian from Home to matchmaking | Detect excessive prep friction |
| Deploy blocker frequency | Tune validation clarity |
| Blocker fix completion rate | Verify blocker copy và deep links solve the problem |
| Loadout severity distribution | Check blocker/warning/advisory tuning |
| Item comparison opened | Verify gear trade-offs are discoverable trước equip |
| Insurance selection and skipped items | Tune insurance value, ineligible copy, và Insure All behavior |
| Preset apply failure | Catch missing item, substitution, cost, hoặc capacity confusion |
| Stash full encounters | Tune stash progression và sell tools |
| Stash invalid move rate | Catch unclear grid/rotation feedback |
| Stash overflow resolution | Tune post-raid/reward inbox holding lane clarity |
| Sell/discard confirmation cancel | Identify protected, quest, insured, contraband, hoặc high-value warning usefulness |
| Pending sync action attempt | Catch duplicate move/sell/claim prevention issues |
| Trader purchase cancellation | Identify pricing, stash capacity, hoặc confirmation confusion |
| Barter missing item route usage | Check whether missing material flow are discoverable |
| Quest turn-in failure | Catch unclear item, FIR, hoặc reward capacity yêu cầu |
| Safe House claim failure | Catch stash capacity và inbox UX issues |
| Profile privacy changes | Confirm privacy controls are discoverable và trusted |

---

## checklist Nghiệm Thu

- [ ] Every màn hình includes người chơi Intent, Layout Anatomy, Expanded ASCII Wireframe, Visual Hierarchy, Component yêu cầu, trạng thái & Edge Cases, Input / Focus / Touch, Designer ghi chú, và Acceptance checklist.
- [ ] Home shows the next best action in under 5 seconds.
- [ ] Loadout blockers explain exact fixes và focus the relevant slot/item.
- [ ] Stash supports mouse, controller, và touch mà không precision-only yêu cầu.
- [ ] Traders clearly distinguish mua, sell, barter, và turn-in modes.
- [ ] Safe House modules show benefit, chi phí, timer, prerequisite, và claim điểm đến.
- [ ] Quest board can deep link to stash, map, trader, hoặc HUD tracking.
- [ ] Profile và social-hiển thị rõ surfaces respect privacy và streamer settings.
- [ ] ASCII visual blocks render as closed Markdown code fences.
- [ ] trang-level summary does not contain the only copy of any critical màn hình yêu cầu.
