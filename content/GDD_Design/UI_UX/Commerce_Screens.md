---
title: "Commerce Screens"
type: docs
weight: 9
---

## Purpose

Commerce screens help players inspect, preview, and buy cosmetic or service offers without creating pay-to-win ambiguity. The group owns shop browsing, offer detail, premium currency top-up, purchase confirmation, purchase result, entitlement claim, and shop-adjacent upgrade flows.

Primary references:

| System | Source |
| :--- | :--- |
| Economy | [Economy & Monetization Design](../GameDesign/Economy.md) |
| Progression / Battle Pass | [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) |
| Global UX | [Global UX Standards](Global_UX_Standards.md) |
| Visual style | [Visual Style & Art Guidelines](Visual_Style.md) |
| Settings and system states | [Settings & System Screens](Commerce_Settings_System_Screens.md) |

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) | Battle pass progress, event progress, ranked, rewards, and news |
| [Settings & System Screens](Commerce_Settings_System_Screens.md) | Auth, setup, settings, privacy, diagnostics, and system dialogs |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |

---

## Screen Inventory

| Screen | Goal | Primary CTA | Key States |
| :--- | :--- | :--- | :--- |
| Shop Home | Browse current shop sections and highlighted offers | View Offer / Preview | loading, empty rotation, offline, platform restricted |
| Featured Offers / Rotating Store | Scan daily/weekly offers, discounts, and owned items | Inspect / Buy | owned, discounted, expires soon, unavailable |
| Bundle Detail | Understand bundle contents and adjusted value | Preview Bundle / Purchase | partially owned, discounted, insufficient balance |
| Item Detail / 3D Preview | Inspect a cosmetic before purchase | Rotate / Equip Preview / Buy | incompatible item, selectable variants, owned |
| Event / Collection Store | Track limited collection progress and event rewards | View Reward / Buy Item | event ended, collection complete, timer warning |
| Battle Pass Upgrade | Upgrade free pass to premium or premium bundle | Upgrade Pass | already premium, season ending, insufficient balance |
| Currency Top-Up | Buy premium currency packs through platform checkout | Select Pack / Continue | platform unavailable, pending checkout, bonus pack |
| Purchase Confirmation | Confirm exact price, contents, and consequence | Confirm Purchase | insufficient balance, platform handoff, hold required |
| Purchase Result / Receipt | Show success, failure, pending, refund, and next action | Equip / View / Retry | success, pending, failed, refunded |
| Redeem Code / Entitlement Claim | Claim promo codes, founders packs, and platform entitlements | Redeem / Claim | duplicate, expired, region locked, already owned |

Commerce does not define a standalone Wallet screen. Currency balance appears only as a component in shop headers, currency top-up, confirmations, and receipts.

---

## Commerce Rules

| Rule | Requirement |
| :--- | :--- |
| No gameplay advantage | Offers must be cosmetic, account service, or clearly non-power. If an item changes presentation only, say so near purchase. |
| Price clarity | Final price, discounted price, original price, tax/platform handoff, and currency type must be visible before confirmation. |
| Ownership clarity | Owned, partially owned, duplicate, and bundle-adjusted states must use readable labels, not color alone. |
| Timer clarity | Daily, weekly, event, and season timers must show exact remaining time and a plain expired state. |
| Confirmation | Premium currency and real-money actions require a confirmation state. Expensive or irreversible actions use hold-to-confirm. |
| Failure safety | Pending/failed purchase copy must say not to retry if the transaction may still complete, and must expose support. |

---

## Designer-Ready Screen Specs

### Shop Home

#### Player Intent

See what is new, understand current balance and platform status, and choose a shop section without losing context.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| SHOP                               Balance 1,250 C   Platform OK   Offers refresh: 18h 22m     |
|------------------------------------------------------------------------------------------------|
| Home | Featured | Bundles | Event | Battle Pass | Currency | Redeem                            |
|------------------------------------------------------------------------------------------------|
| HERO OFFER: Season Operator Pack                         | DAILY SNAPSHOT                      |
| [Large cosmetic preview]                                 | Featured 12 offers                  |
| 2,400 C  was 3,200 C  25% off                            | 3 owned / 9 new                     |
| [Preview] [View Bundle]                                  | Platform checkout available         |
|------------------------------------------------------------------------------------------------|
| FEATURED ROW: [Card] [Card] [Card] [Card]                | SYSTEM MESSAGE / TRUST COPY         |
| WEEKLY BUNDLES: [Card] [Card] [Card]                     | Cosmetics only. No gameplay power.  |
| EVENT OFFERS: [Card] [Card] [Card]                       | [Purchase Help]                     |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Commerce header | title, balance component, platform status, refresh timer |
| Horizontal commerce tabs | Home, Featured, Bundles, Event, Battle Pass, Currency, Redeem |
| Hero offer | largest current promotion with preview, price, discount, and CTA |
| Offer rows | scannable sections with cards grouped by rotation or theme |
| Trust panel | non-power copy, purchase help, service warning if needed |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Hero offer | largest visual, price visible without opening detail |
| 2 | Balance/platform | persistent and readable in 1 second |
| 3 | Offer rows | cards show name, type, price, owned/discount/timer |
| 4 | Trust copy | visible but quieter than purchase CTAs |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Offer card | image, name, category, price, ownership, discount, timer, compatibility |
| Balance chip | premium balance, earnable balance if applicable, top-up shortcut |
| Platform status | OK, offline, checkout unavailable, region restricted |
| Refresh timer | daily/weekly/event timer with expired fallback |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Loading | skeleton hero and card rows; balance waits for account service |
| Empty rotation | explain no offers available and show refresh time/support note |
| Offline | browse cached owned items only; purchase CTAs disabled with reason |
| Platform restricted | disable purchase and show platform/account requirement |

#### Input / Focus / Touch

PC focus starts on hero CTA, then tabs, card rows, trust links. Console shoulder buttons move tabs; D-pad moves cards by row. Touch uses horizontal tab scroll and card carousel snapping.

#### Designer Notes

The page must feel like a store, not a wallet. Balance is a utility chip; offers and previews carry the surface.

#### Acceptance Checklist

- [ ] Hero offer has price, discount, timer, ownership, and preview CTA.
- [ ] Every purchase-disabled state has a readable reason.
- [ ] Balance is visible without creating a Wallet destination.

### Featured Offers / Rotating Store

#### Player Intent

Scan many timed offers quickly and decide which item or bundle deserves inspection.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| FEATURED OFFERS                    Balance 1,250 C                     Daily refresh 18h 22m   |
|------------------------------------------------------------------------------------------------|
| Home | Featured | Bundles | Event | Battle Pass | Currency | Redeem                            |
|------------------------------------------------------------------------------------------------|
| FILTERS: All | Operators | Weapons | Emotes | Charms | Owned Hidden [x]                        |
|------------------------------------------------------------------------------------------------|
| TODAY'S BEST:  [Card: New] [Card: 25% off] [Card: Owned] [Card: Ends Soon]                     |
| DAILY OFFERS:  [Card] [Card] [Card] [Card] [Card] [Card]                                       |
| WEEKLY OFFERS: [Card] [Card] [Card] [Card]                                                     |
|------------------------------------------------------------------------------------------------|
| SELECTED OFFER SUMMARY: name, type, price, ownership, timer, [Preview] [Inspect]               |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Filter strip | category tabs and owned-hidden toggle |
| Offer grid | dense card grid grouped by rotation |
| Selected summary | stable footer with selected card price and CTAs |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Selected offer | selected state clear across mouse, focus, and touch |
| 2 | Price/timer badges | readable on every card |
| 3 | Filters | compact and persistent above grid |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Card badge stack | New, Owned, Discount, Ends Soon, Platform Locked |
| Discount display | show discounted and original price together |
| Timer | daily/weekly exact time, warning under final hour |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Owned item | card remains inspectable; buy CTA becomes View / Equip if relevant |
| Ends soon | timer escalates visually and textually; no flashing |
| Filter empty | show clear filter CTA and refresh time |
| Price update | selected summary refreshes and asks player to reconfirm if checkout was open |

#### Input / Focus / Touch

Grid navigation wraps by row on console. Filters are shoulder-tab reachable. Touch cards need a first tap for select and second tap/CTA for inspect.

#### Designer Notes

Do not hide important price information in hover-only UI. Console and touch must see the same offer facts.

#### Acceptance Checklist

- [ ] All timed offers show exact timer and expired fallback.
- [ ] Owned/discount/platform states have readable labels.
- [ ] Selected summary remains stable while browsing.

### Bundle Detail

#### Player Intent

Understand what the bundle includes, what they already own, and whether the adjusted price is fair.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| < Back   BUNDLE DETAIL: Night Raid Pack                         Balance 1,250 C                |
|------------------------------------------------------------------------------------------------|
| [Large bundle preview / carousel]                  | CONTENTS                                  |
|                                                     | [Operator Skin] New                      |
| Price 1,800 C  was 2,600 C                         | [Weapon Skin] Owned                       |
| Owned item adjustment: -400 C                      | [Charm] New                               |
| Cosmetics only. No gameplay power.                 | [Banner] New                              |
|------------------------------------------------------------------------------------------------|
| DETAILS: rarity, availability, event relation, compatibility, refund/platform note             |
|------------------------------------------------------------------------------------------------|
| [Preview All] [Inspect Items]                                      [Purchase Bundle 1,800 C]   |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Preview area | bundle art and item carousel |
| Contents panel | item list with owned/new/incompatible labels |
| Price block | final price, original price, discount, owned adjustment |
| Action bar | preview, inspect, purchase |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Final adjusted price | closest text to purchase CTA |
| 2 | Contents list | owned and new status visible per item |
| 3 | Non-power copy | near price block |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Bundle contents | item name, category, rarity, owned, compatibility |
| Adjustment row | owned item credit or "no adjustment" reason |
| Purchase CTA | disabled with reason for insufficient balance or restriction |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Partially owned | adjusted price shown with calculation summary |
| Fully owned | purchase disabled; CTA becomes View Owned Items |
| Insufficient balance | show shortfall and route to Currency Top-Up |
| Region/platform lock | show exact unavailable reason and support route |

#### Input / Focus / Touch

Focus order: back, preview carousel, contents list, price block, action bar. Console triggers cycle items; touch swipes carousel and taps content rows.

#### Designer Notes

Owned adjustment must be impossible to miss; this is a trust-building screen.

#### Acceptance Checklist

- [ ] Final price and original price are both visible when discounted.
- [ ] Owned items are labeled in the contents list.
- [ ] Purchase disabled state gives the next valid action.

### Item Detail / 3D Preview

#### Player Intent

Inspect a cosmetic from all useful angles before buying or equipping.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| < Back   ITEM DETAIL: Wraith Runner Jacket                     Balance 1,250 C                 |
|------------------------------------------------------------------------------------------------|
| [3D PREVIEW / ROTATE / ZOOM]                         | ITEM INFO                               |
|                                                      | Type: Operator Skin                     |
|                                                      | Rarity: Epic                            |
|                                                      | Compatible: Operator class A/B          |
|                                                      | Variants: Default | Masked | Hooded     |
|------------------------------------------------------------------------------------------------|
| PREVIEW CONTROLS: Rotate L/R | Zoom | Lighting | Compare Owned                                 |
|------------------------------------------------------------------------------------------------|
| Price 1,200 C   Cosmetics only. No gameplay power.                         [Buy] [Wishlist]    |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Preview viewport | stable 3D/model preview area with controls |
| Item info | category, rarity, compatibility, variants |
| Preview controls | rotate, zoom, lighting, compare if available |
| Purchase bar | price, non-power copy, buy/wishlist/equip |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Preview | largest surface; not obscured by UI |
| 2 | Price/action | persistent and near consequence copy |
| 3 | Compatibility | visible before purchase |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Preview viewport | loading, fallback image, rotate, zoom, reset view |
| Variant selector | labels and preview thumbnails |
| Compatibility row | supported operator/weapon, locked requirements if any |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Preview asset loading | skeleton/model spinner inside viewport only |
| Preview asset failed | fallback image and retry control |
| Owned | CTA changes to Equip / View In Locker |
| Incompatible | purchase allowed only if cosmetic is account-owned; copy explains use limitation |

#### Input / Focus / Touch

Mouse drag rotates preview; wheel zooms. Console right stick rotates and triggers zoom. Touch drag rotates and pinch zooms with reset button.

#### Designer Notes

Preview controls must feel optional; the purchase facts must remain readable without interacting.

#### Acceptance Checklist

- [ ] Compatibility and variants are visible before purchase.
- [ ] Preview failure has a fallback that does not block purchase facts.
- [ ] Owned state does not show Buy as the primary CTA.

### Event / Collection Store

#### Player Intent

Understand limited-time event offers, collection completion, and what reward unlocks at completion.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| EVENT STORE: Blackout Collection                      Ends in 6d 04h   Owned 8 / 24            |
|------------------------------------------------------------------------------------------------|
| Home | Featured | Bundles | Event | Battle Pass | Currency | Redeem                            |
|------------------------------------------------------------------------------------------------|
| COLLECTION REWARD: Phantom Blade Skin                | PROGRESS LADDER                         |
| [Reward preview]                                     | 8/24 owned                              |
| Unlocks after collecting all event items             | Milestones: 6, 12, 18, 24               |
|------------------------------------------------------------------------------------------------|
| EVENT ITEMS: [Owned] [New] [New] [Discount] [New] [Locked] [New] [New]                         |
|------------------------------------------------------------------------------------------------|
| [Preview Reward] [View Event Challenges]                         [Buy Selected Item]           |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Event header | event name, end timer, owned count |
| Reward preview | collection reward and unlock requirement |
| Progress ladder | milestones and completion clarity |
| Event grid | event item cards with owned/new/locked states |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Event timer and owned count | always visible |
| 2 | Collection reward | visually clear but not misleading |
| 3 | Event item grid | shows cost and ownership per item |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Owned count | owned / total, completion reward state |
| Event item card | item type, price, owned, event-only label |
| Event challenge link | route to LiveOps event progress, not purchase duplicate |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Event ended | purchases disabled; show claim window if applicable |
| Collection complete | reward claim CTA replaces buy emphasis |
| Reward already claimed | show View Owned / Equip |
| Late purchase risk | final-hour warning in text near CTA |

#### Input / Focus / Touch

Focus starts at reward preview then grid. Console shoulder tabs switch shop sections; D-pad grid navigation does not skip locked cards.

#### Designer Notes

The page must not imply random rewards unless the economy actually supports them. If deterministic, say exactly what is bought.

#### Acceptance Checklist

- [ ] Event timer, owned count, and reward requirement are visible.
- [ ] Ended event disables purchase with a clear reason.
- [ ] Event challenge link routes to Progression/LiveOps.

### Battle Pass Upgrade

#### Player Intent

Compare free and premium value, understand tier skip options, and upgrade intentionally.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| BATTLE PASS UPGRADE                         Season ends in 24d      Balance 1,250 C            |
|------------------------------------------------------------------------------------------------|
| PASS SUMMARY: Level 32 / 100        Free claimed 18        Premium pending 12                  |
|------------------------------------------------------------------------------------------------|
| OPTION A: Premium Pass 950 C        | OPTION B: Premium Bundle 2,400 C + 20 tier skips         |
| Includes premium track unlocks      | Includes premium track, skips, exclusive cosmetic        |
| [Compare Rewards] [Upgrade 950 C]   | [Compare Bundle] [Upgrade Bundle]                        |
|------------------------------------------------------------------------------------------------|
| REWARD PREVIEW: Premium rewards you would unlock immediately after upgrade                     |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Pass summary | season time, player level, pending premium rewards |
| Upgrade options | premium and bundle side by side |
| Immediate rewards | items unlocked immediately after purchase |
| Route links | battle pass progress remains in Progression/LiveOps |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Upgrade options | price and contents visible side by side |
| 2 | Immediate unlocks | prevents uncertainty after purchase |
| 3 | Season timer | near title and CTA |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Option card | price, included benefits, tier skip count, exclusives |
| Reward preview | immediate unlocks, future rewards, claimed state |
| Season timer | days/hours; final day warning |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Already premium | show bundle upgrade only if valid; otherwise View Pass |
| Season ending | warn before purchase and require confirmation if under threshold |
| Insufficient balance | route to Currency Top-Up with needed shortfall |
| Pass unavailable | disabled with season/platform reason |

#### Input / Focus / Touch

Option cards are first focus targets. Console left/right compares options; touch stacks option cards vertically on narrow layouts.

#### Designer Notes

Do not duplicate the full Battle Pass page here. This surface owns purchase clarity only.

#### Acceptance Checklist

- [ ] Premium vs bundle value is directly comparable.
- [ ] Immediate unlocks after upgrade are listed.
- [ ] Season-ending warning appears before confirmation.

### Currency Top-Up

#### Player Intent

Choose a premium currency pack and understand platform checkout before leaving the game UI.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| CURRENCY TOP-UP                                      Current Balance 1,250 C                   |
|------------------------------------------------------------------------------------------------|
| PACKS: [500 C] [1,000 C + bonus] [2,800 C best value] [5,000 C]                                |
|------------------------------------------------------------------------------------------------|
| SELECTED PACK: 2,800 C + 200 bonus                  | PLATFORM CHECKOUT                        |
| Price: platform localized price                      | Provider: Steam / PSN / Xbox / Epic     |
| Bonus: 200 C                                         | Taxes/fees handled by platform          |
|------------------------------------------------------------------------------------------------|
| [Back to Offer] [Change Pack]                                      [Continue to Checkout]      |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Current balance | balance only; no transaction ledger |
| Pack selector | pack amount, bonus, best value label |
| Checkout panel | platform/provider, localized price, handoff copy |
| Action bar | back to offer, change pack, continue |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Selected pack price | next to platform handoff CTA |
| 2 | Pack amounts | easy comparison without dark patterns |
| 3 | Current balance | visible but secondary |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Pack card | amount, bonus, localized price, best value label if true |
| Platform panel | provider, account status, checkout availability |
| Return context | name of offer that required top-up if entered from purchase |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Platform checkout unavailable | disable continue and show provider reason |
| Pending checkout | show pending receipt and do not offer repeated checkout blindly |
| Age/region restricted | block purchase with account/platform requirement |
| Bonus promotion ended | refresh pack data and require reselection |

#### Input / Focus / Touch

Pack cards are a horizontal row on PC/console and a two-column grid on mobile. Confirm focus starts on selected pack, then checkout CTA.

#### Designer Notes

This is not a Wallet. Do not add history, ledger, or balance management here.

#### Acceptance Checklist

- [ ] No standalone wallet/history UI exists.
- [ ] Platform provider and localized price are visible before checkout.
- [ ] Pending checkout prevents accidental repeated purchase.

### Purchase Confirmation

#### Player Intent

Make a final informed decision with exact contents, price, balance impact, and refund/platform note.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| CONFIRM PURCHASE                                                                               |
|------------------------------------------------------------------------------------------------|
| ITEM: Night Raid Pack                              Price: 1,800 C                              |
| Contents: 4 cosmetics                             Balance after: 250 C                         |
| Owned adjustment: -400 C                          Refund/platform note: See platform policy    |
| Cosmetics only. No gameplay power.                                                             |
|------------------------------------------------------------------------------------------------|
| [Cancel]                                                [Hold / Confirm Purchase 1,800 C]      |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Item summary | exact item/bundle name and contents count |
| Price summary | final price, adjustment, balance after |
| Policy note | platform/refund note and non-power copy |
| Confirmation bar | cancel and confirm; hold when required |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Final price | closest information to confirm CTA |
| 2 | Contents | exact count and item list access |
| 3 | Balance after | visible before committing |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Confirm CTA | enabled only when price and entitlement data are current |
| Hold progress | shows duration and cancel state |
| Policy link | opens non-blocking detail panel if possible |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Price changed | block confirm, refresh price, ask for re-confirm |
| Insufficient balance | route to top-up with exact shortfall |
| Service timeout | no charge assumed; show retry/status copy |
| Duplicate ownership | block purchase and show owned state |

#### Input / Focus / Touch

Default focus is Cancel for high-cost or real-money confirmation; otherwise focus starts on confirmation only after summary is read. Touch uses hold button for expensive purchases.

#### Designer Notes

The confirmation modal is the trust anchor. No marketing copy should compete with final price and contents.

#### Acceptance Checklist

- [ ] Final price, balance after, and contents are visible together.
- [ ] Price change requires re-confirmation.
- [ ] High-cost purchase supports hold-to-confirm.

### Purchase Result / Receipt

#### Player Intent

Know whether the purchase succeeded, what was received, and what to do next.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| PURCHASE RESULT: SUCCESS                                                                       |
|------------------------------------------------------------------------------------------------|
| You received Night Raid Pack.                                                                  |
| Items added: Operator Skin, Weapon Skin, Charm, Banner                                         |
| Balance: 250 C                                                                                 |
| Receipt ID: EP-2048-9921                                                                       |
|------------------------------------------------------------------------------------------------|
| [Equip Now] [View Items] [Back to Shop] [Purchase Help]                                        |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Result title | success, pending, failed, refunded |
| Received items | exact entitlements granted or pending |
| Receipt details | transaction/reference id when available |
| Next actions | equip/view/back/help/retry depending on state |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Result status | unmistakable text label |
| 2 | Granted items | names readable without scrolling for small purchases |
| 3 | Support route | visible for pending/failed/refunded |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Result banner | status, timestamp, provider if available |
| Item list | item name, type, ownership destination |
| Help link | support article/report route with receipt id copied if possible |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Success | show equip/view primary actions |
| Pending | say not to retry if charge may still complete; show refresh status |
| Failed | show retry only if safe and no charge captured |
| Refunded | explain entitlement removal or balance restoration |

#### Input / Focus / Touch

Success focuses Equip/View. Pending focuses Refresh Status. Failed focuses safe Retry or Help depending on provider response.

#### Designer Notes

Never leave players guessing whether money or currency moved. Result copy must be plain.

#### Acceptance Checklist

- [ ] Pending state warns against duplicate purchase.
- [ ] Receipt/support path is visible.
- [ ] Success state routes to owned item usage.

### Redeem Code / Entitlement Claim

#### Player Intent

Enter a code or claim a platform entitlement and resolve duplicate/expired/region errors.

#### Expanded ASCII Wireframe

```
+------------------------------------------------------------------------------------------------+
| REDEEM / CLAIM                                                                                 |
|------------------------------------------------------------------------------------------------|
| Enter Code: [____-____-____-____]                                      [Redeem]                |
|------------------------------------------------------------------------------------------------|
| AVAILABLE CLAIMS                                                                               |
| Founder Pack - Ready to claim                     [Claim]                                      |
| Platform Bonus - Already claimed                  [View Items]                                 |
|------------------------------------------------------------------------------------------------|
| STATUS / ERROR: Code expired, duplicate, region locked, or service unavailable                 |
+------------------------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Code entry | segmented input, paste support, redeem CTA |
| Claim list | platform/founder/starter entitlements |
| Status lane | success/error/loading copy |
| Help link | support for invalid or missing entitlement |

#### Visual Hierarchy

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Input/claim CTA | clear action depending on mode |
| 2 | Status/error | inline and persistent after submit |
| 3 | Claim list | distinguishes ready, claimed, expired |

#### Component Requirements

| Component | Data / Behavior |
| :--- | :--- |
| Code input | paste, auto-hyphen, invalid character handling |
| Claim card | entitlement name, source platform, status, contents |
| Error lane | duplicate, expired, region locked, service unavailable |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Invalid code | focus returns to input and explains format |
| Duplicate | show already owned/claimed destination |
| Expired | show expiration copy and support if applicable |
| Region locked | explain region/account mismatch |

#### Input / Focus / Touch

Keyboard paste should fill all code segments. Console input uses platform text entry. Touch uses large segmented fields and paste shortcut.

#### Designer Notes

Do not bury error details in a toast. Claim failures are support-sensitive.

#### Acceptance Checklist

- [ ] Duplicate, expired, and region-locked states have distinct copy.
- [ ] Successful claim lists granted items.
- [ ] Missing entitlement has support route.

---

## Analytics

| Signal | Use |
| :--- | :--- |
| Shop section impressions | Measure which rows and tabs players see |
| Offer inspect rate | Tune card clarity and hero placement |
| Preview interaction | Understand cosmetic inspection behavior |
| Confirmation cancel | Identify unclear pricing or trust issues |
| Purchase pending/failure rate | Detect platform or provider issues |
| Top-up entry source | Separate direct top-up from insufficient-balance recovery |
| Redeem failure reason | Improve code formatting and support copy |

---

## Acceptance Checklist

- [ ] Commerce has no standalone Wallet screen.
- [ ] Shop Home, Featured Offers, Bundle Detail, Item Detail, Event Store, Battle Pass Upgrade, Currency Top-Up, Purchase Confirmation, Purchase Result, and Redeem Claim are covered.
- [ ] Every purchasable item shows price, currency type, ownership, platform restriction, and non-power/cosmetic context when relevant.
- [ ] Balance appears only as a component in commerce header, top-up, confirmation, or receipt.
- [ ] Purchase failures and pending states include duplicate-charge-safe copy and support route.
- [ ] Battle Pass purchase UX links to Progression/LiveOps for reward progress instead of duplicating it.
