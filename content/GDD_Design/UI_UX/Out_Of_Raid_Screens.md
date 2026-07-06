---
title: "Out-of-Raid Screens"
type: docs
weight: 3
---

## Purpose

Out-of-raid screens are the player's command center. They support recovery after failure, celebration after extraction, inventory decisions, long-term progression, and the fastest safe route back into a raid.

Primary references:

| System | Source |
| :--- | :--- |
| Home hub | [Home Screen & Main Lobby Design](../GameDesign/HomeScreen_Design.md) |
| Loadout preparation | [Pre-Raid Loadout & Preparation Screen](../GameDesign/LoadoutPreparation.md) |
| Safe House | [Safe House Design](../GameDesign/Safe_House_Design.md) |
| Stash | [Stash Design](../Stash_Design.md) |
| Profile | [Player Profile & Career Stats](../GameDesign/PlayerProfile.md) |
| Quests | [Quest & Objective System](../Gameplay/Quest_Objective_System.md) |

---

## Screen Inventory

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

| Spec | Requirement |
| :--- | :--- |
| User intent | Understand what changed since last session and decide whether to deploy, recover, or manage inventory |
| Entry points | Post-login loading, AAR continue, app resume, party leader navigation |
| Exit points | Deploy, Loadout, Stash, Safe House, Traders, Profile, Settings |
| PC/console layout | Operator showcase center, navigation rail left, deploy/status panel right, contextual strip bottom |
| Mobile layout | Top account bar, operator/loadout summary, deploy card, event/feed stack, bottom nav |
| Primary CTA | Deploy if loadout is valid; Continue Preparation if blockers exist |
| Destructive actions | None on hub; destructive actions must deep link to their owning screen |

### Home States

| State | UI Behavior |
| :--- | :--- |
| First session | Tutorial Raid is primary; store/ranked/live events are secondary or locked |
| Return after extraction | Show compact loot/XP recap with route to stash or redeploy |
| Return after death | Show rebuild, insurance, preset, and recovery actions |
| Party active | Show squad cards and leader status in deploy panel |
| Offline | Allow local settings/profile view; disable deploy, traders, and social with reason |

---

## Operator Select

| Spec | Requirement |
| :--- | :--- |
| Goal | Let players select an operator based on role, ability, progression, and readiness |
| Layout | Roster list/grid, selected operator showcase, ability panel, role tags, unlock path |
| Primary CTA | Select Operator |
| Secondary actions | Preview cosmetics, compare role, view mastery, favorite operator |
| Locked state | Show requirement, trial availability if any, and progression shortcut |
| Accessibility | Ability descriptions must be text-readable and not icon-only |

### Input Mapping

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Browse roster | Mouse wheel / arrow keys | D-pad / stick | Swipe list |
| Inspect ability | Hover / click | Focus card | Tap info |
| Rotate model | Drag | Right stick | Swipe model |
| Select | Click / Enter | A / Cross | Tap CTA |

---

## Loadout Workbench

The detailed preparation rules live in [Loadout Preparation](../GameDesign/LoadoutPreparation.md). This UI group owns the screen state contract and platform layout.

| Region | PC / Console | Mobile |
| :--- | :--- | :--- |
| Identity | Operator and gear slots left | Operator tab |
| Inventory | Stash grid center | Stash tab with persistent summary |
| Mission | Mode, map, squad, quests right | Mission and Squad tabs |
| Risk | Footer value/weight/insurance strip | Pinned summary above deploy button |

### Validation States

| State | Behavior |
| :--- | :--- |
| Missing weapon | Block deploy and focus weapon slot |
| Missing ammo | Warn with direct filter to compatible ammo |
| Overweight | Block deploy or require item removal based on tuning |
| High value | Warn; allow explicit confirmation |
| Uninsured eligible items | Warn and offer Insure All |
| Quest item missing | Warn with quest deep link |

---

## Stash

| Spec | Requirement |
| :--- | :--- |
| Goal | Make inventory management fast without hiding item value, size, FIR status, and risk |
| Primary CTA | Contextual: Equip, Move, Sell, Use, or Turn In |
| Secondary actions | Auto-sort, filter, search, favorite, tag junk, inspect |
| Empty state | Explain no items and offer trader, starter kit, or raid path |
| Full state | Surface capacity, upgrade path, sell junk, and quick filters |

### Stash Inputs

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Move item | Drag/drop | Grid cursor + A | Tap item then target |
| Rotate | R while dragging | Y / Triangle | Rotate button |
| Quick equip | Ctrl-click | Hold A | Double tap |
| Context menu | Right-click | Hold focus | Long press |
| Search | Ctrl-F | Y / Triangle opens keyboard | Search field |

---

## Traders / Market

| Mode | Primary Content | CTA | Failure States |
| :--- | :--- | :--- | :--- |
| Buy | Trader inventory and player wallet | Purchase | insufficient funds, rep locked, stash full |
| Sell | Player sellable items and price summary | Sell Selected | protected item, quest item warning, no buyer |
| Barter | Offer list and required item checklist | Trade | missing item, item not FIR if required, offer expired |
| Turn-in | Quest hand-in items and rewards | Turn In | wrong item, missing quantity, reward inventory full |

Every purchase or sale involving premium currency, high-value gear, or quest-critical items must use a confirmation dialog.

---

## Safe House Modules

| Screen | Purpose | Required States |
| :--- | :--- | :--- |
| Module Overview | Show base rooms, unlock path, and active timers | locked, available upgrade, in progress, complete |
| Upgrade Detail | Explain benefit before spend | missing materials, prerequisite locked, confirm spend |
| Crafting Queue | Start and collect crafts | queue full, timer running, output ready, stash full |
| Repair Bench | Repair damaged gear | insufficient materials, max durability loss, confirm |
| Insurance Inbox | Claim returned gear | empty, expired soon, stash full, partial return |

### Safe House Acceptance

- [ ] Upgrade benefits are visible before cost commitment.
- [ ] Timers show remaining time and completion state.
- [ ] Claim actions explain where items go.
- [ ] Locked modules show the next prerequisite.

---

## Quest Board

| Spec | Requirement |
| :--- | :--- |
| Goal | Help players choose, track, and complete objectives without leaving the raid loop confused |
| Layout | Quest list, selected detail, objective checklist, location/map hints, rewards |
| Primary CTA | Track Quest or Turn In |
| Secondary actions | Pin objective, show on map, find required item, abandon if supported |
| Mobile | Tabs: Active, Available, Completed, Rewards |

### Quest States

| State | Behavior |
| :--- | :--- |
| Available | Show faction, location, risk, rewards |
| Tracked | Pin objective to HUD and tactical map |
| Ready to turn in | Promote CTA and highlight required item source |
| Failed | Explain what failed and whether retry is possible |
| Missing item | Deep link to stash filter or trader if known |

---

## Player Profile

| Screen Area | Content |
| :--- | :--- |
| Identity | Name, level, platform, title, faction/karma visible tier |
| Stats | Extraction rate, raids, kills, survival time, favored operators |
| Achievements | Badges, milestones, titles, seasonal accomplishments |
| Cosmetics | Banners, frames, emotes, skins owned/equipped |
| Privacy | Public/friends/private profile controls |

Profile screens must respect streamer mode by hiding names, IDs, invite codes, and sensitive social status.

---

## Analytics

| Metric | Target / Use |
| :--- | :--- |
| Time from Home to matchmaking | Detect excessive prep friction |
| Deploy blocker frequency | Tune validation clarity |
| Stash full encounters | Tune stash progression and sell tools |
| Trader purchase cancellation | Identify pricing or confirmation confusion |
| Quest turn-in failure | Catch unclear item requirements |
| Safe House claim failure | Catch stash capacity and inbox UX issues |

---

## Acceptance Checklist

- [ ] Home shows the next best action in under 5 seconds.
- [ ] Loadout blockers explain exact fixes.
- [ ] Stash supports mouse, controller, and touch without precision-only requirements.
- [ ] Traders clearly distinguish buy, sell, barter, and turn-in modes.
- [ ] Safe House modules show benefit, cost, timer, and prerequisite.
- [ ] Quest board can deep link to stash, map, trader, or HUD tracking.
- [ ] Profile and social-visible surfaces respect privacy and streamer settings.
