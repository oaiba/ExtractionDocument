---
title: "Out-of-Raid Screens"
type: docs
weight: 3
---

## Purpose

Out-of-raid screens are the player's command center. They support recovery after failure, celebration after extraction, inventory decisions, long-term progression, and the fastest safe route back into a raid.

This page owns the player-facing layout contract for out-of-raid surfaces. Game design pages own economy and progression rules; technical pages own implementation names, data events, and service contracts.

Primary references:

| System | Source |
| :--- | :--- |
| Home hub | [Home Screen & Main Lobby Design](../gamedesign/homescreen_design/index.html) |
| Loadout preparation | [Pre-Raid Loadout & Preparation Screen](../gamedesign/loadoutpreparation/index.html) |
| Safe House | [Safe House Design](../gamedesign/safe_house_design/index.html) |
| Stash | [Stash Design](../stash_design/index.html) |
| Profile | [Player Profile & Career Stats](../gamedesign/playerprofile/index.html) |
| Quests | [Quest & Objective System](../gameplay/quest_objective_system/index.html) |

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Full UI/UX documentation hub |
| [Screen Groups Overview](screen_groups_overview/index.html) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](global_ux_standards/index.html) | Shared navigation, focus, state, modal, and accessibility rules |
| [Pre-Raid Screens](pre_raid_screens/index.html) | Mode, map, deploy confirmation, squad lobby, matchmaking |
| [Post-Raid Screens](post_raid_screens/index.html) | AAR, death replay, loot transfer, redeploy |
| [UX Flows](ux_flows/index.html) | End-to-end journey mapping |

---

## Screen Inventory

This table is a navigation summary. Detailed visual, state, input, and acceptance requirements live inside each screen section below.

| Screen | Goal | Primary CTA | Key States |
| :--- | :--- | :--- | :--- |
| Home / Safe House Hub | Show identity, changed state, and deploy path | Deploy / Continue Preparation | first session, return victory, return death, event active, offline |
| Operator Select | Choose character role and inspect ability identity | Select Operator | locked, injured/cooldown, recommended, cosmetic preview |
| Loadout Workbench | Build a valid kit and understand risk | Ready / Continue to Mission | missing weapon, missing ammo, overweight, uninsured value |
| Stash | Store, sort, search, sell, and move items | Move / Equip / Sell | empty stash, full stash, filter no results, item locked |
| Traders / Market | Buy, sell, barter, and turn in faction items | Purchase / Sell / Trade | insufficient funds, rep locked, barter missing items, sale confirmation |
| Safe House Modules | Upgrade base, craft, repair, and claim returns | Upgrade / Start Craft / Claim | module locked, missing materials, queue full, timer complete |
| Quest Board | Track objectives and turn in rewards | Track / Turn In | completed, failed, missing item, location locked |
| Player Profile | Review identity, stats, titles, achievements, cosmetics | Equip Title / View Stats | private profile, seasonal reset, no achievements |

---

## Home / Safe House Hub

**Player Intent**

The player wants to understand what changed since the last session, confirm whether the current kit is raid-ready, and choose the fastest safe next action: deploy, recover, manage inventory, or inspect progression.

| Spec | Requirement |
| :--- | :--- |
| Entry points | Post-login loading, AAR continue, app resume, party leader navigation, event deep link |
| Exit points | Deploy, Loadout, Stash, Safe House, Traders, Quests, Profile, Settings |
| Primary CTA | Deploy if valid; Continue Preparation if blockers exist; Tutorial Raid for first session |
| Secondary actions | Inspect operator, open last raid recap, claim returns, check squad, open event, manage stash |
| Destructive actions | None on hub; destructive actions must deep link to their owning screen and confirm there |

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

| Region | Purpose | Required Content |
| :--- | :--- | :--- |
| Global header | Persistent account and economy status | level, faction rep, credits, notifications, network state |
| Horizontal global nav | Primary out-of-raid destination map | Home, Loadout, Stash, Traders, Safe House, Quests, Profile, Settings, current selection, unread badges, disabled reasons |
| Operator showcase | Identity, loadout readability, emotional anchor | operator model, current weapon, armor silhouette, rotate/inspect hint |
| Last raid snapshot | Explain changed state after returning | extraction/death label, XP, loot count, rep delta, AAR action |
| Deploy panel | Readiness and risk before commitment | mode, map, squad, queue estimate, gear value, weight, insurance |
| Context cards | Next-best actions from system state | blockers, claims, full stash, event, quest progress |
| Status bar | Persistent social/progression context | friends, party, battle pass, deploy/continue CTA |

**Visual Hierarchy**

| Priority | Element | Designer Requirement |
| :--- | :--- | :--- |
| 1 | Deploy/Continue CTA and blocker reason | Must be readable within 2 seconds; disabled CTA must name the exact blocker |
| 2 | Operator and current kit | Use size and silhouette, not only labels, to show readiness |
| 3 | Last raid or recovery snapshot | Only appears when recent state changed; collapse after acknowledged |
| 4 | Context cards | Limit to 4-5 cards to avoid turning hub into a dashboard wall |
| 5 | LiveOps and social | Present but secondary; never visually compete with deploy path |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Deploy panel | Fixed width across states; CTA position never jumps when blockers appear |
| Blocker list | Max 3 visible blockers, ordered by severity; each has a deep link and plain-language fix |
| Last raid card | Shows extraction/death, XP delta, notable loot, and a single route to full AAR |
| Squad card | Shows leader, ready count, voice state, and party mismatch reason if blocked |
| Event strip | Shows event name, time remaining, and whether it changes raid rules |
| Notification badges | Must pair icon/color with text or count; no color-only state meaning |

**States & Edge Cases**

| State | UI Behavior |
| :--- | :--- |
| First session | Tutorial Raid becomes primary; locked systems show short reason and unlock path |
| Return after extraction | Show compact loot/XP recap with Move Loot and Redeploy actions |
| Return after death | Show rebuild kit, insurance return, preset, and recovery quest actions |
| Party active | Deploy panel shows squad cards, leader status, member blockers, and ready count |
| Loadout invalid | CTA becomes Continue Preparation; first blocker receives focus/deep link |
| Stash full | Surface capacity percentage, sell junk, upgrade stash, and move items actions |
| Offline | Allow settings and local profile view; disable deploy, traders, social with reason |
| Loading | Skeleton header, nav, operator area, and deploy panel separately so layout does not shift |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Navigate hub | Click horizontal global nav / number shortcuts | Shoulder tabs or horizontal focus | Bottom nav or drawer |
| Rotate operator | Drag hero | Right stick | Swipe hero |
| Open blocker fix | Click blocker | Focus blocker + A / Cross | Tap blocker row |
| Deploy | Click CTA / Enter when focused | A / Cross on CTA | Sticky bottom CTA |
| Open context card | Click card | Focus card | Tap card |

Focus order: global header, horizontal global nav, deploy panel CTA, blocker list, last raid actions, context cards, header utilities.

**Designer Notes**

- Keep the deploy panel visually stable; warnings expand inside it, not below it.
- The player should understand "Can I raid now?" before reading any secondary card.
- Use text labels for state badges such as Offline, Full, Ready, Locked, and Expired.
- Do not place shop, event, or battle pass promotions above deploy readiness.

**Acceptance Checklist**

- [ ] Hub shows the next best action in under 5 seconds.
- [ ] Invalid loadout, full stash, and offline states each show exact disabled reasons.
- [ ] Deploy CTA, blocker list, and squad readiness remain visible at desktop and mobile sizes.
- [ ] No destructive action is executed directly from the hub.

---

## Operator Select

**Player Intent**

The player wants to choose an operator based on role, ability identity, readiness, unlock status, squad fit, and cosmetics without losing the path back to raid preparation.

| Spec | Requirement |
| :--- | :--- |
| Entry points | Home operator card, Loadout operator slot, new player setup, cosmetic preview link |
| Exit points | Select Operator, Back to previous screen, View Mastery, Preview Cosmetics |
| Primary CTA | Select Operator when available and not on cooldown/injured |
| Secondary actions | Favorite, compare role, preview skin, view mastery, inspect ability details |
| Accessibility | Ability descriptions must be text-readable and not icon-only |

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

| Region | Purpose | Required Content |
| :--- | :--- | :--- |
| Filter rail | Reduce roster scanning cost | role, owned/locked, favorite, search, recommended sort |
| Roster list | Fast operator comparison | name, role tag, readiness, lock/cooldown/injury badge |
| Preview | Emotional identity and cosmetic inspection | full model, current weapon pose, skin, rotate affordance |
| Ability panel | Explain gameplay identity | role, active ability, cooldown, range, risk, counterplay summary |
| Squad fit | Help team composition | current squad roles, recommendation, duplicate role warning |
| Action bar | Keep selection path stable | compare, favorite, preview skin, select |

**Visual Hierarchy**

| Priority | Element | Designer Requirement |
| :--- | :--- | :--- |
| 1 | Selected operator and Select CTA | Selection must be unambiguous in roster and preview |
| 2 | Role and ability summary | Use text labels for role, cooldown, and readiness |
| 3 | Locked/injured state | Show requirement or recovery route next to disabled CTA |
| 4 | Cosmetics | Secondary to gameplay selection unless entered from cosmetic preview |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Roster row | Includes role, readiness, ownership/lock state, favorite indicator, and recommendation marker |
| Ability card | Shows plain-language effect, cooldown, range, use case, and key limitation |
| Locked operator | Shows unlock requirement, progress, and allowed preview/trial state if available |
| Injured/cooldown operator | Shows remaining time or required recovery action and whether selection is blocked |
| Cosmetic strip | Locked cosmetics show requirement; selection preview does not equip until confirmed |

**States & Edge Cases**

| State | UI Behavior |
| :--- | :--- |
| Available | Select CTA active; ability and preview fully visible |
| Recommended | Roster badge explains why, such as squad role gap or quest relevance |
| Locked | CTA disabled; panel shows level, quest, purchase, or mastery requirement |
| Injured/cooldown | CTA disabled or warning based on tuning; recovery deep link visible |
| Cosmetic preview | Action bar changes to Equip/Back if already selected operator |
| No results | Empty roster state offers Clear Filters |
| Loading | Roster skeleton and preview placeholder keep panel sizes fixed |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse roster | Mouse wheel / arrow keys | D-pad / left stick | Swipe list |
| Inspect ability | Hover / click ability card | Focus card | Tap info row |
| Rotate model | Drag preview | Right stick | Swipe model |
| Change filters | Click dropdown | Shoulder focus + A / Cross | Filter chips drawer |
| Select | Click / Enter | A / Cross | Sticky CTA |

Focus order: roster, selected preview, ability panel, squad fit, action bar.

**Designer Notes**

- Do not hide readiness behind color alone; every blocked row needs a readable label.
- Roster row height should stay stable when badges change.
- The ability panel should be readable without opening a modal.
- Cosmetic preview must never make the player think the operator has been selected unless the CTA confirms it.

**Acceptance Checklist**

- [ ] Locked, injured, recommended, and selected operators are visually distinct with text labels.
- [ ] Ability identity, cooldown, range, and limitation are visible on the detail panel.
- [ ] Select CTA clearly explains why it is disabled when blocked.
- [ ] Controller focus can reach filters, roster, preview, and CTA predictably.

---

## Loadout Workbench

The detailed preparation rules live in [Loadout Preparation](../gamedesign/loadoutpreparation/index.html). This UI group owns the screen state contract and platform layout.

**Player Intent**

The player wants to build a valid raid kit, understand risk, resolve blockers, and move toward mission selection without accidentally deploying with missing ammo, excessive weight, or uninsured value.

| Spec | Requirement |
| :--- | :--- |
| Entry points | Home deploy blocker, Home Loadout, Operator Select return, Quest item deep link |
| Exit points | Ready to Map, Back Home, Stash, Insurance, Presets, Mission tab |
| Primary CTA | Ready to Map if valid; Fix Loadout if blocked |
| Secondary actions | Equip, move, inspect, compare, insure, preset apply/save, filter compatible items |
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

| Region | Purpose | Required Content |
| :--- | :--- | :--- |
| Gear column | Show equipped kit and slot validity | operator, weapon slots, armor, helmet, rig, pack, secure container |
| Stash grid | Source of available items | search, filters, sort, compatible highlight, selected item summary |
| Mission/risk panel | Keep deployment context visible | mode, map, squad, quests, gear value, weight, insurance, ammo state |
| Warning lane | Make blockers actionable | severity icon, blocker text, direct fix action |
| Action bar | Persistent readiness contract | value, weight, capacity, fix/ready CTA |

**Visual Hierarchy**

| Priority | Element | Designer Requirement |
| :--- | :--- | :--- |
| 1 | Invalid slot or blocking warning | Use direct label and focus target; do not bury in tooltip |
| 2 | Gear slots | Slot state must be scannable by silhouette, name, and status |
| 3 | Stash compatibility | Compatible items highlighted without hiding incompatible inventory |
| 4 | Risk footer | Persistent value, weight, capacity, insurance; no layout jump |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Gear slot | Shows item name, durability/ammo if relevant, slot restriction, and warning state |
| Stash item tile | Shows footprint, category icon, stack count, durability if relevant, rarity/tier, FIR, quest, protected, insured, contraband, locked, equipped, and compatibility marker |
| Selected item summary | Shows stats delta, value, weight, durability, compatibility, insurance eligibility, quest/FIR/protected flags, and allowed actions |
| Gear comparison panel | Names the trade-off in text: capacity vs weight, armor class vs mobility, durability vs repair cost, insured vs ineligible |
| Warning lane | Orders blockers first, warnings second, suggestions third; max 3 visible with View All |
| Preset control | Shows Save, Apply, Rename, Delete; overwrite/delete require confirmation |
| Ready CTA | Active only when required rules pass; disabled label names first blocker |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Missing weapon | Block Ready; focus primary weapon slot and filter compatible weapons |
| Missing ammo | Warn or block per tuning; show compatible ammo filter and ammo count needed |
| Overweight | Block or confirm per tuning; show weight source and suggested removals |
| High value | Warning with explicit gear value; allow confirmation if no blocker |
| Uninsured eligible items | Warning with Insure All and item count |
| Quest item missing | Warning with quest detail and stash/trader/map deep link |
| Stash full during move | Reject move, show capacity, offer stash upgrade/sell junk |
| Empty stash | Explain source paths: traders, starter kit, raid, quest rewards |
| Broken required gear | Block Ready; route to repair, replacement, or remove item |
| Low durability weapon | Warning with malfunction/durability risk and repair route |
| Contraband item | Show restricted deploy/sell/insurance behavior before Ready |
| Locked item | Disable invalid action and show unlock or protection reason |
| Invalid container item | Block Ready/move; show container restriction and valid target |
| Preset apply failure | List missing items, substitutions, cost, and stash capacity result |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop or click source then slot | Grid cursor + A / Cross | Tap item then target |
| Rotate item | R while moving | Y / Triangle | Rotate button near item |
| Inspect item | Right-click / hover detail | Hold focus | Long press |
| Quick equip | Ctrl-click | Hold A / Cross | Double tap |
| Filter compatible | Click warning/filter | Focus warning + A / Cross | Tap warning chip |

Mobile layout uses tabs: Operator, Stash, Mission. The risk summary and Ready CTA remain pinned above the bottom safe area.

**Designer Notes**

- Treat the footer as the player's contract: it should always tell value, weight, insurance, and readiness.
- Incompatible items may be dimmed, but should remain discoverable and inspectable.
- Grid cell size must be stable; badges cannot resize item tiles.
- Every blocked Ready state must provide one direct fix path.

**Acceptance Checklist**

- [ ] Missing weapon, missing ammo, overweight, uninsured value, and quest item missing states are represented.
- [ ] Blocker, warning, and advisory severities are visually distinct and text-labeled.
- [ ] Broken gear, low durability, contraband, locked, insured/uninsured, and invalid container states are represented.
- [ ] Gear comparison explains trade-offs in text, not only green/red deltas.
- [ ] Stash grid supports item movement without precision-only interactions.
- [ ] Ready CTA never activates while a blocking validation state is present.
- [ ] Risk summary remains visible while browsing stash items.

---

## Stash

**Player Intent**

The player wants to store, sort, search, move, sell, and inspect items quickly while understanding capacity pressure, item value, item purpose, and whether an item is safe to discard or sell.

| Spec | Requirement |
| :--- | :--- |
| Entry points | Home, Loadout, post-raid loot transfer, trader sell flow, quest item deep link |
| Exit points | Move to Loadout, Sell, Turn In, Inspect, Upgrade Stash, Back |
| Primary CTA | Contextual: Equip, Move, Sell, Use, Turn In, or Inspect |
| Secondary actions | Auto-sort, filter, search, favorite, tag junk, split stack, rotate, lock item |
| Destructive actions | Discard and sell protected/quest/high-value items require confirmation |

**Stash Information Architecture**

| Surface | Requirement |
| :--- | :--- |
| Filter rail | Category, rarity/tier, FIR, quest, protected, insured, contraband, damaged, value, and saved filters |
| Grid | Stable cells, item footprints, stacks, empty cells, valid target preview, rotate-needed preview |
| Selected item panel | Name, category, tier/rarity, durability, value, weight, footprint, ownership flags, related quest/trader/craft |
| Capacity summary | Used/total cells, incoming overflow, large-item pressure, locked/protected count, stash value |
| Overflow / reward inbox lane | Temporary holding for post-raid, support, reward, or sync items with source context |
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

| Region | Purpose | Required Content |
| :--- | :--- | :--- |
| Filter rail | Fast category narrowing | all categories, saved filters, quest/protected toggles |
| Grid | Spatial inventory management | item footprints, stacks, empty cells, invalid placement preview |
| Info panel | Explain selected item | name, category, durability, value, footprint, FIR, protected/quest state |
| Quick tools | Resolve capacity and sorting problems | auto sort, sell junk, find quest items, upgrade stash |
| Warning lane | Surface capacity and invalid moves | full stash, protected item warning, filter no results |
| Action bar | Contextual item actions | move, equip, sell, use, inspect, discard |

**Visual Hierarchy**

| Priority | Element | Designer Requirement |
| :--- | :--- | :--- |
| 1 | Selected item and valid target | Selection outline and target preview must be unmistakable |
| 2 | Capacity pressure | Capacity count and warning lane visible without scrolling |
| 3 | Protected/FIR/quest state | Badges must include readable labels or accessible text |
| 4 | Bulk tools | Useful but secondary; avoid overwhelming normal move flow |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Item tile | Shows footprint, stack count, category shape/icon, durability when relevant, rarity/tier, and badges for FIR, quest, protected, insured, contraband, locked, equipped |
| Grid target preview | Shows valid, invalid, rotate-needed, and blocked-by-item states |
| Info panel | Gives enough detail to decide keep/sell/equip without opening inspect modal |
| Sell junk | Lists estimated value and excludes quest/protected/favorited items by default |
| Search | Searches item name, category, ammo caliber, quest tag, and trader relevance |
| Full stash warning | Offers specific actions: sell junk, use container, upgrade, filter large items |
| Destructive confirmation | Names item, value, flags, and consequence for protected, quest, high-value, insured, or contraband items |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Empty stash | Explain no items; offer traders, starter kit, or raid path |
| Full stash | Persistent warning; invalid incoming moves explain needed space |
| Filter no results | Show Clear Filters and explain active filter stack |
| Item locked/protected | Disable destructive actions unless confirmation path is allowed |
| Quest item selected | Show related quest, turn-in state, and whether FIR is required |
| Incoming loot overflow | Show temporary holding lane and required resolution before exit |
| Loading | Grid skeleton preserves cell dimensions and filter rail width |
| Pending sync | Disable duplicate move/sell/claim actions and show finalizing state |
| Contraband selected | Show sale, trade, insurance, deploy, or mode restriction in info panel |
| Damaged/broken item | Show repair route, effective value, and deploy restriction if applicable |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop | Grid cursor + A / Cross | Tap item then target |
| Rotate | R while dragging | Y / Triangle | Rotate button |
| Quick equip | Ctrl-click | Hold A / Cross | Double tap |
| Context menu | Right-click | Hold focus | Long press |
| Search | Ctrl-F | Y / Triangle opens keyboard | Search field |

Focus order: search, filter rail, grid, info panel actions, quick tools, action bar.

**Designer Notes**

- Capacity and selected item detail must remain visible while scrolling large stashes.
- Item badges should not shrink item names below readable size.
- The discard action should be visually separated from common positive actions.
- Dense grid is acceptable, but interaction targets must remain generous on touch.

**Acceptance Checklist**

- [ ] Empty, full, filter-empty, locked item, and quest item states are designed.
- [ ] Item info panel shows value, footprint, tier/rarity, durability, FIR/protected/insured/contraband state, and allowed actions.
- [ ] Overflow, pending sync, damaged/broken item, and contraband states are designed.
- [ ] Mouse, controller, and touch can move and rotate items.
- [ ] Destructive actions warn for protected, quest, or high-value items.

---

## Traders / Market

**Player Intent**

The player wants to buy, sell, barter, and turn in items while understanding price, reputation locks, stash capacity, missing barter parts, and whether a transaction is risky or irreversible.

| Spec | Requirement |
| :--- | :--- |
| Entry points | Home traders, stash sell action, quest turn-in deep link, safe house material need |
| Exit points | Purchase, Sell, Trade, Turn In, Inspect Item, Back |
| Primary CTA | Purchase, Sell Selected, Trade, or Turn In based on mode |
| Secondary actions | Filter, sort, inspect, compare, pin missing item, switch trader |
| Destructive actions | Selling premium, high-value, protected, or quest-critical items requires confirmation |

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

| Region | Purpose | Required Content |
| :--- | :--- | :--- |
| Trader list | Switch vendor context | trader name, faction, unread/quest badge, availability |
| Trader profile | Explain access and progression | rep level, next unlock requirement, reset timer, flavor line |
| Offer list | Browse buy/sell/barter/turn-in candidates | mode tabs, search, filters, item row, price, stock, lock reason |
| Detail strip | Explain selected offer | stats, compatibility, limits, barter checklist, item warnings |
| Your offer | Confirm transaction summary | credits/funds, selected items, total, stash after transaction |
| Warning lane | Prevent failed or regretted transaction | stash full, insufficient funds, protected item, missing barter |

**Visual Hierarchy**

| Priority | Element | Designer Requirement |
| :--- | :--- | :--- |
| 1 | Mode tab and CTA | Buy/Sell/Barter/Turn-in mode must be impossible to confuse |
| 2 | Price/total and failure reason | Transaction cost and blocker visible before CTA |
| 3 | Rep lock and stock | Locked rows remain visible with exact requirement |
| 4 | Trader identity | Flavor supports worldbuilding but does not obscure commerce data |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Offer row | Shows name, category, price/value, stock/limit, lock state, and compatibility tag |
| Mode tabs | Persist selected mode; changing mode clears incompatible selections after warning if needed |
| Your offer panel | Shows selected count, total, credits/funds delta, stash capacity result, and CTA |
| Barter checklist | Shows required items, owned count, FIR requirement, and missing item pin action |
| Sell warning | Flags protected, quest, insured, equipped, or high-value items before sale |
| Confirmation dialog | Required for premium currency, high-value gear, quest-critical items, and irreversible trades |

**States & Edge Cases**

| State | UI Behavior |
| :--- | :--- |
| Insufficient funds | CTA disabled; credits/funds shortage shown in Your Offer panel |
| Rep locked | Row disabled; requirement and unlock route visible |
| Stash full | CTA disabled or warning per transaction; show capacity after transaction |
| Barter missing items | Checklist highlights missing item and offers stash/trader/quest route |
| Offer expired | Row disabled; reset timer shown; selected expired offer removed with message |
| Sale confirmation | Modal names item, value, protected/quest status, and final action |
| Offline | Disable transaction modes; allow browsing cached trader profiles if supported |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch trader | Click trader | D-pad / shoulder group | Trader drawer |
| Change mode | Click tab | Bumper tabs | Segmented tabs |
| Select offer | Click row | Focus row + A / Cross | Tap row |
| Inspect item | Right-click / detail | Hold focus | Long press |
| Confirm transaction | Click CTA | A / Cross on CTA | Sticky CTA |

Focus order: trader list, mode tabs, offer list, detail strip, your offer panel, CTA.

**Designer Notes**

- Buy, Sell, Barter, and Turn-in need distinct text labels, not only tab color.
- The player's total cost and stash capacity result must be visible before purchase.
- Confirmation copy should name the item and consequence, not use generic "Are you sure?" text.
- Locked offers should teach progression instead of disappearing.

**Acceptance Checklist**

- [ ] Buy, sell, barter, and turn-in modes are visually and behaviorally distinct.
- [ ] Insufficient funds, rep lock, stash full, missing barter, and sale confirmation states are specified.
- [ ] High-value, premium, protected, and quest-critical transactions require confirmation.
- [ ] The transaction CTA always matches the selected mode.

---

## Safe House Modules

**Player Intent**

The player wants to understand base progression, upgrade benefits, crafting/repair timers, insurance returns, and material blockers without losing track of what can be claimed or improved now.

| Spec | Requirement |
| :--- | :--- |
| Entry points | Home safe house, stash upgrade prompt, insurance return card, crafting material deep link |
| Exit points | Upgrade, Start Craft, Claim, Repair, Track Materials, Back |
| Primary CTA | Upgrade, Start Craft, Claim, or Repair based on selected module state |
| Secondary actions | View prerequisites, pin materials, inspect queue, cancel/collect craft if supported |
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

| Region | Purpose | Required Content |
| :--- | :--- | :--- |
| Module map | Spatial overview of base progression | rooms, level, locked/ready/in-progress states, connections |
| Module detail | Explain selected module | current level, status, next benefit, cost, prerequisites, CTA |
| Queue/inbox | Surface timers and claims | crafting, repairs, insurance returns, ready-to-claim badge |
| Warning lane | Explain blockers | missing materials, stash full on claim, queue full, prerequisite locked |
| Action bar | Commit or track next action | view benefits, track materials, confirm spend, upgrade/claim |

**Visual Hierarchy**

| Priority | Element | Designer Requirement |
| :--- | :--- | :--- |
| 1 | Claim-ready and upgrade-ready modules | Must stand out with text and icon, not color alone |
| 2 | Selected module benefits/cost | Benefit must appear before spend CTA |
| 3 | Missing materials/prerequisites | Show owned/required counts and direct tracking route |
| 4 | Long-term map | Keep readable but secondary to selected module detail |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Module node | Shows name, level, status, active timer/claim badge, locked reason if selected |
| Detail panel | Shows current benefit, next benefit, cost, requirements, and spend confirmation state |
| Material row | Shows item name, owned/required count, source hint, and pin/track action |
| Timer chip | Shows remaining time, ready state, and destination module |
| Insurance inbox | Shows returned item count, expiry risk, stash capacity result, and Claim CTA |
| Confirmation | Spending currency/materials names cost and resulting benefit before final commit |

**States & Edge Cases**

| State | UI Behavior |
| :--- | :--- |
| Module locked | Detail panel shows prerequisite chain and next reachable step |
| Upgrade available | CTA active only if materials, currency, and prerequisites pass |
| Missing materials | CTA disabled; material rows show owned/required counts and tracking |
| Upgrade in progress | CTA disabled; timer and completion result visible |
| Craft queue full | Start Craft disabled; show queue capacity and claim/cancel options |
| Timer complete | Ready badge on map and queue; Claim CTA promoted |
| Stash full on claim | Claim blocked; show required space and route to stash |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Select module | Click node | D-pad module graph | Tap room card |
| Inspect material | Hover/click row | Focus row | Tap material |
| Track material | Click Track | A / Cross on focused row | Tap track chip |
| Claim timer | Click ready chip | Focus timer + A / Cross | Tap queue card |
| Confirm spend | Click CTA + modal | A / Cross + confirm | Sticky CTA + modal |

Mobile layout uses tabs: Modules, Detail, Queue. Claim-ready timers should appear as a persistent top summary.

**Designer Notes**

- Always show benefit before cost to make upgrade value clear.
- Module map can be stylized, but text labels must remain readable.
- Timers need absolute state labels: In Progress, Ready, Expiring Soon, Locked.
- Claim actions must explain where items go and what blocks them.

**Acceptance Checklist**

- [ ] Upgrade benefits are visible before cost commitment.
- [ ] Locked modules show the next prerequisite and reachable step.
- [ ] Missing materials show owned/required counts and tracking actions.
- [ ] Timers show remaining time, completion, expiry risk, and claim destination.

---

## Quest Board

**Player Intent**

The player wants to choose useful objectives, understand where to go, know what item or extraction requirement matters, track objectives into raid, and turn in rewards without confusion.

| Spec | Requirement |
| :--- | :--- |
| Entry points | Home quest card, trader turn-in, map quest hint, post-raid progress recap |
| Exit points | Track, Turn In, Show on Map, Find Item in Stash, Back |
| Primary CTA | Track Quest for active/incomplete; Turn In for ready quests |
| Secondary actions | Pin objective, show on map, find required item, view faction, abandon if supported |
| Destructive actions | Abandon quest requires confirmation and failure consequence text |

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

| Region | Purpose | Required Content |
| :--- | :--- | :--- |
| Quest list | Compare and filter objectives | status badge, faction, location, reward preview, lock/failure state |
| Quest detail | Explain completion requirements | objectives, counts, extraction/FIR rules, location, risk |
| Reward panel | Make value and turn-in readiness clear | XP, rep, credits, items, unlocks, required hand-in items |
| Quest chain | Show progression context | prior/next quest, unlock status, faction path |
| Action bar | Route to next action | track, map, stash item search, abandon |

**Visual Hierarchy**

| Priority | Element | Designer Requirement |
| :--- | :--- | :--- |
| 1 | Objective status and primary CTA | Ready-to-turn-in must be unmistakable |
| 2 | Required item/extraction condition | FIR, extraction, location, and delivery rules must be explicit |
| 3 | Rewards | Always visible for selected quest; secondary to requirements |
| 4 | Chain/faction context | Helpful but not required for immediate completion |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Quest row | Shows title, status, faction, location tag, and progress count |
| Objective checklist | Shows exact count, completion state, FIR/extract requirement, and failure risk |
| Location block | Shows map, sub-location, access/lock status, and Show on Map action |
| Reward panel | Shows all rewards and whether inventory space is needed |
| Turn-in panel | Shows required items, owned count, FIR validity, and wrong-item reason |
| Abandon action | Visually separated and confirmed with consequence text |

**States & Edge Cases**

| State | UI Behavior |
| :--- | :--- |
| Available | Show faction, location, risk, rewards, and Track CTA |
| Tracked | Pin objective to HUD and tactical map; row shows Tracked label |
| Ready to turn in | Promote Turn In CTA; highlight required item source and reward |
| Missing item | Deep link to stash filter or trader if known; show owned/required count |
| Failed | Explain failed condition, lost items, retry availability, and next step |
| Locked | Show prerequisite quest, level, faction, map, or trader requirement |
| Reward inventory full | Turn In blocked; show required stash space and stash route |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse quests | Mouse wheel / click | D-pad list | Swipe list |
| Filter status | Click filters | Shoulder tabs | Top tabs |
| Track quest | Click CTA | A / Cross on CTA | Sticky CTA |
| Show on map | Click action | Focus action | Tap action |
| Find item | Click item requirement | Focus item row | Tap item row |

Mobile layout uses tabs: Active, Available, Completed, Rewards. Detail and reward panels stack below the selected quest.

**Designer Notes**

- Status labels should be words: New, Tracked, Ready, Locked, Failed.
- Quest risk copy should be short and direct, especially for extraction-required objectives.
- The player should not need to infer FIR validity from icon color.
- Turn-in should never accept a wrong item silently; show exact reason.

**Acceptance Checklist**

- [ ] Available, tracked, ready, missing item, failed, and locked states are designed.
- [ ] FIR, extraction, delivery, location, and reward requirements are explicit.
- [ ] Quest board can deep link to stash, map, trader, and HUD tracking.
- [ ] Abandon has confirmation and consequence text.

---

## Player Profile

**Player Intent**

The player wants to review identity, stats, achievements, cosmetics, titles, and privacy settings, and to understand what other players can see.

| Spec | Requirement |
| :--- | :--- |
| Entry points | Home profile, squad member inspect, social profile link, post-raid player card |
| Exit points | Equip Title, Equip Cosmetic, View Match History, Privacy Settings, Back |
| Primary CTA | Equip selected title/cosmetic or View Stats depending selected tab |
| Secondary actions | Compare seasons, inspect achievements, view commendations, report safety |
| Privacy | Respect streamer mode by hiding names, IDs, invite codes, and sensitive social status |

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

| Region | Purpose | Required Content |
| :--- | :--- | :--- |
| Identity card | Establish public profile identity | avatar, banner, name, level, platform, title, karma/faction tier |
| Career stats | Show performance and progression | extraction rate, raids, kills, survival time, favorite operator, seasonal rank |
| Cosmetics panel | Equip personalization | title, frame, badge, emote, skins, selected cosmetic detail |
| History/safety tabs | Support review and moderation | achievements, match history, commendations, report safety |
| Privacy controls | Explain visibility | public/friends/private, streamer mode, hidden fields |
| Action bar | Common profile actions | edit banner, equip, privacy settings, copy invite code |

**Visual Hierarchy**

| Priority | Element | Designer Requirement |
| :--- | :--- | :--- |
| 1 | Player identity and privacy state | Viewer must know whose profile and visibility mode |
| 2 | Core stats | Use readable labels and avoid unexplained abbreviations |
| 3 | Equipped cosmetics | Show current equipped state before available alternatives |
| 4 | Safety/reporting | Available but not visually dominant on own profile |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Identity card | Shows public-facing name, title, level, platform, and streamer-mode substitutions |
| Stat row | Shows label, value, timeframe/season, and comparison only if available |
| Cosmetic selector | Shows owned/locked/equipped states and requirement for locked cosmetics |
| Achievement tile | Shows name, progress, reward, unlock date if achieved |
| Match history row | Shows map, outcome, duration, squad size, and privacy-safe participant display |
| Privacy dropdown | Explains exactly which fields are public, friends-only, or hidden |

**States & Edge Cases**

| State | UI Behavior |
| :--- | :--- |
| Own public profile | All editable areas visible; privacy controls active |
| Viewing friend | Edit controls hidden; friend-safe stats and invite actions visible |
| Private profile | Hide stats/history; show privacy message and allowed actions |
| Streamer mode | Replace name/ID/invite code and sensitive social status with safe aliases |
| Seasonal reset | Show previous season archive and current season empty/starting state |
| No achievements | Empty state explains achievement sources and recommends one active goal |
| Locked cosmetic | Shows requirement and preview availability |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Switch tab | Click tab | Bumpers | Segmented tabs |
| Equip cosmetic | Click item + CTA | Focus item + A / Cross | Tap item + sticky CTA |
| Change privacy | Dropdown | Focus dropdown | Privacy sheet |
| Inspect history | Click row | Focus row | Tap row |
| Copy invite code | Click action | Action bar focus | Tap action |

Focus order: identity card, privacy control, stat tabs, cosmetic selector, selected cosmetic CTA, action bar.

**Designer Notes**

- Profile can be expressive, but private/streamer states must be unmistakable.
- Do not expose IDs, invite codes, party status, or match history when privacy hides them.
- Locked cosmetics should motivate without looking like a required purchase path.
- Keep safety/report controls discoverable and plain.

**Acceptance Checklist**

- [ ] Own, friend, private, streamer mode, seasonal reset, no achievement, and locked cosmetic states are specified.
- [ ] Privacy controls state exactly what information is visible.
- [ ] Equipped cosmetic and selected cosmetic are visually distinct.
- [ ] Sensitive identity fields are hidden under streamer mode.

---

## Analytics

These metrics validate whether the screen designs reduce friction and clarify risk. Detailed event schemas belong in technical documentation.

| Metric | Target / Use |
| :--- | :--- |
| Time from Home to matchmaking | Detect excessive prep friction |
| Deploy blocker frequency | Tune validation clarity |
| Blocker fix completion rate | Verify blocker copy and deep links solve the problem |
| Loadout severity distribution | Check blocker/warning/advisory tuning |
| Item comparison opened | Verify gear trade-offs are discoverable before equip |
| Insurance selection and skipped items | Tune insurance value, ineligible copy, and Insure All behavior |
| Preset apply failure | Catch missing item, substitution, cost, or capacity confusion |
| Stash full encounters | Tune stash progression and sell tools |
| Stash invalid move rate | Catch unclear grid/rotation feedback |
| Stash overflow resolution | Tune post-raid/reward inbox holding lane clarity |
| Sell/discard confirmation cancel | Identify protected, quest, insured, contraband, or high-value warning usefulness |
| Pending sync action attempt | Catch duplicate move/sell/claim prevention issues |
| Trader purchase cancellation | Identify pricing, stash capacity, or confirmation confusion |
| Barter missing item route usage | Check whether missing material flows are discoverable |
| Quest turn-in failure | Catch unclear item, FIR, or reward capacity requirements |
| Safe House claim failure | Catch stash capacity and inbox UX issues |
| Profile privacy changes | Confirm privacy controls are discoverable and trusted |

---

## Acceptance Checklist

- [ ] Every screen includes Player Intent, Layout Anatomy, Expanded ASCII Wireframe, Visual Hierarchy, Component Requirements, States & Edge Cases, Input / Focus / Touch, Designer Notes, and Acceptance Checklist.
- [ ] Home shows the next best action in under 5 seconds.
- [ ] Loadout blockers explain exact fixes and focus the relevant slot/item.
- [ ] Stash supports mouse, controller, and touch without precision-only requirements.
- [ ] Traders clearly distinguish buy, sell, barter, and turn-in modes.
- [ ] Safe House modules show benefit, cost, timer, prerequisite, and claim destination.
- [ ] Quest board can deep link to stash, map, trader, or HUD tracking.
- [ ] Profile and social-visible surfaces respect privacy and streamer settings.
- [ ] ASCII visual blocks render as closed Markdown code fences.
- [ ] Page-level summary does not contain the only copy of any critical screen requirement.
