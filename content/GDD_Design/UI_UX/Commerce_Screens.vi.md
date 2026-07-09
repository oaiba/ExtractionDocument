---
title: "Commerce màn hình"
type: docs
weight: 9
---

## Mục Đích

Commerce màn hình giúp người chơi kiểm tra, preview, và mua cosmetic hoặc dịch vụ offer mà không tạo pay-to-win mơ hồ. Nhóm này phụ trách shop duyệt, offer chi tiết, premium currency top-up, purchase confirmation, purchase kết quả, entitlement claim, và shop-adjacent upgrade flow.

Tham chiếu chính:

| hệ thống | source |
| :--- | :--- |
| Economy | [Economy & Monetization Design](../GameDesign/Economy.md) |
| Progression / Battle Pass | [Progression & LiveOps màn hình](Progression_LiveOps_Screens.md) |
| global UX | [global UX Standards](Global_UX_Standards.md) |
| Visual style | [Visual Style & Art Guidelines](Visual_Style.md) |
| Settings và hệ thống trạng thái | [Settings & hệ thống màn hình](Commerce_Settings_System_Screens.md) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [màn hình Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy và designer-ready spec template |
| [Progression & LiveOps màn hình](Progression_LiveOps_Screens.md) | Battle pass progress, event progress, ranked, rewards, và news |
| [Settings & hệ thống màn hình](Commerce_Settings_System_Screens.md) | Auth, setup, settings, privacy, diagnostics, và hệ thống dialogs |
| [global UX Standards](Global_UX_Standards.md) | shared navigation, focus, trạng thái, modal, và accessibility rules |

---

## Inventory Màn Hình

| màn hình | mục tiêu | primary CTA | chính trạng thái |
| :--- | :--- | :--- | :--- |
| Shop Home | Browse hiện tại shop sections và highlighted offer | View offer / preview | loading, empty rotation, offline, platform restricted |
| Featured offer / Rotating Store | Scan daily/weekly offer, discounts, và owned items | kiểm tra / mua | owned, discounted, expires soon, unavailable |
| Bundle chi tiết | Understand bundle contents và adjusted giá trị | preview Bundle / purchase | partially owned, discounted, insufficient balance |
| Item chi tiết / 3D preview | kiểm tra a cosmetic trước purchase | Rotate / Equip preview / mua | incompatible item, selectable variants, owned |
| Event / Collection Store | Track limited collection progress và event rewards | View Reward / mua Item | event ended, collection complete, timer cảnh báo |
| Battle Pass upgrade | upgrade free pass to premium hoặc premium bundle | upgrade Pass | already premium, season ending, insufficient balance |
| Currency Top-Up | mua premium currency packs thông qua platform checkout | Select Pack / Continue | platform unavailable, pending checkout, bonus pack |
| purchase Confirmation | Confirm exact giá, contents, và consequence | Confirm purchase | insufficient balance, platform handoff, hold required |
| purchase kết quả / Receipt | Show success, failure, pending, refund, và next action | Equip / View / Retry | success, pending, failed, refunded |
| Redeem Code / Entitlement claim | claim promo codes, founders packs, và platform entitlements | Redeem / claim | duplicate, expired, region locked, already owned |

Commerce does not define a standalone Wallet màn hình. Currency balance appears only as a component in shop headers, currency top-up, confirmations, và receipts.

---

## Commerce Rules

| Rule | yêu cầu |
| :--- | :--- |
| No gameplay advantage | offer phải được cosmetic, account dịch vụ, hoặc clearly non-power. nếu an item changes presentation only, say so near purchase. |
| giá clarity | Final giá, discounted giá, original giá, tax/platform handoff, và currency type phải được hiển thị rõ trước confirmation. |
| Ownership clarity | Owned, partially owned, duplicate, và bundle-adjusted trạng thái must cách dùng dễ đọc labels, not color alone. |
| Timer clarity | Daily, weekly, event, và season timers must show exact remaining thời gian và a plain expired trạng thái. |
| Confirmation | Premium currency và real-money actions require a confirmation trạng thái. Expensive hoặc irreversible actions cách dùng hold-to-confirm. |
| Failure safety | pending/failed purchase copy must say not to retry nếu the transaction may still complete, và must expose support. |

---

## Designer-Ready màn hình Specs

### Shop Home

**người chơi Intent**

See what is new, understand hiện tại balance và platform status, và choose a shop section mà không losing context.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Commerce header | title, balance component, platform status, refresh timer |
| Horizontal commerce tabs | Home, Featured, Bundles, Event, Battle Pass, Currency, Redeem |
| Hero offer | largest hiện tại promotion với preview, giá, discount, và CTA |
| offer rows | scannable sections với cards grouped by rotation hoặc theme |
| Trust panel | non-power copy, purchase giúp, dịch vụ cảnh báo nếu needed |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Hero offer | largest visual, giá hiển thị rõ mà không opening chi tiết |
| 2 | Balance/platform | persistent và dễ đọc in 1 second |
| 3 | offer rows | cards show name, type, giá, owned/discount/timer |
| 4 | Trust copy | hiển thị rõ nhưng quieter than purchase CTAs |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| offer card | image, name, category, giá, ownership, discount, timer, compatibility |
| Balance chip | premium balance, earnable balance nếu applicable, top-up shortcut |
| Platform status | OK, offline, checkout unavailable, region restricted |
| Refresh timer | daily/weekly/event timer với expired fallback |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| loading | skeleton hero và card rows; balance waits for account dịch vụ |
| empty rotation | explain no offer available và show refresh thời gian/support note |
| Offline | browse cached owned items only; purchase CTAs disabled với reason |
| Platform restricted | disable purchase và show platform/account yêu cầu |

**Input / Focus / Touch**

PC focus starts on hero CTA, then tabs, card rows, trust links. Console shoulder buttons move tabs; D-pad moves cards by row. Touch uses horizontal tab scroll và card carousel snapping.

**Designer ghi chú**

The trang must feel like a store, not a wallet. Balance is a utility chip; offer và previews carry the surface.

**Acceptance checklist**

- [ ] Hero offer has giá, discount, timer, ownership, và preview CTA.
- [ ] Every purchase-disabled trạng thái has a dễ đọc reason.
- [ ] Balance is hiển thị rõ mà không tạo a Wallet điểm đến.

### Featured offer / Rotating Store

**người chơi Intent**

Scan many timed offer quickly và decide which item hoặc bundle deserves inspection.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Filter strip | category tabs và owned-hidden toggle |
| offer grid | dense card grid grouped by rotation |
| Selected summary | stable footer với selected card giá và CTAs |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Selected offer | selected trạng thái rõ across mouse, focus, và touch |
| 2 | giá/timer badges | dễ đọc on every card |
| 3 | Filters | compact và persistent above grid |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| Card badge stack | New, Owned, Discount, Ends Soon, Platform Locked |
| Discount display | show discounted và original giá together |
| Timer | daily/weekly exact thời gian, cảnh báo under final hour |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Owned item | card remains inspectable; mua CTA becomes View / Equip nếu relevant |
| Ends soon | timer escalates visually và textually; no flashing |
| Filter empty | show rõ filter CTA và refresh thời gian |
| giá update | selected summary refreshes và asks người chơi to reconfirm nếu checkout was open |

**Input / Focus / Touch**

Grid navigation wraps by row on console. Filters are shoulder-tab reachable. Touch cards need a first tap for select và second tap/CTA for kiểm tra.

**Designer ghi chú**

Do not hide quan trọng giá information in hover-only UI. Console và touch must see the same offer facts.

**Acceptance checklist**

- [ ] All timed offer show exact timer và expired fallback.
- [ ] Owned/discount/platform trạng thái have dễ đọc labels.
- [ ] Selected summary remains stable while duyệt.

### Bundle chi tiết

**người chơi Intent**

Understand what the bundle includes, what they already own, và whether the adjusted giá is fair.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| preview area | bundle art và item carousel |
| Contents panel | item list với owned/new/incompatible labels |
| giá block | final giá, original giá, discount, owned adjustment |
| Action bar | preview, kiểm tra, purchase |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Final adjusted giá | closest text to purchase CTA |
| 2 | Contents list | owned và new status hiển thị rõ per item |
| 3 | Non-power copy | near giá block |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| Bundle contents | item name, category, rarity, owned, compatibility |
| Adjustment row | owned item credit hoặc "no adjustment" reason |
| purchase CTA | disabled với reason for insufficient balance hoặc restriction |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Partially owned | adjusted giá shown với calculation summary |
| Fully owned | purchase disabled; CTA becomes View Owned Items |
| Insufficient balance | show shortfall và route to Currency Top-Up |
| Region/platform lock | show exact unavailable reason và support route |

**Input / Focus / Touch**

Focus order: back, preview carousel, contents list, giá block, action bar. Console triggers cycle items; touch swipes carousel và taps content rows.

**Designer ghi chú**

Owned adjustment phải được impossible to miss; this is a trust-building màn hình.

**Acceptance checklist**

- [ ] Final giá và original giá are both hiển thị rõ khi discounted.
- [ ] Owned items are labeled in the contents list.
- [ ] purchase disabled trạng thái gives the next valid action.

### Item chi tiết / 3D preview

**người chơi Intent**

kiểm tra a cosmetic from all useful angles trước buying hoặc equipping.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| preview viewport | stable 3D/model preview area với controls |
| Item info | category, rarity, compatibility, variants |
| preview controls | rotate, zoom, lighting, compare nếu available |
| purchase bar | giá, non-power copy, mua/wishlist/equip |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | preview | largest surface; not obscured by UI |
| 2 | giá/action | persistent và near consequence copy |
| 3 | Compatibility | hiển thị rõ trước purchase |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| preview viewport | loading, fallback image, rotate, zoom, reset view |
| Variant selector | labels và preview thumbnails |
| Compatibility row | supported operator/vũ khí, locked yêu cầu nếu any |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| preview asset loading | skeleton/model spinner inside viewport only |
| preview asset failed | fallback image và retry control |
| Owned | CTA changes to Equip / View In Locker |
| Incompatible | purchase allowed only nếu cosmetic is account-owned; copy explains cách dùng limitation |

**Input / Focus / Touch**

Mouse drag rotates preview; wheel zooms. Console right stick rotates và triggers zoom. Touch drag rotates và pinch zooms với reset button.

**Designer ghi chú**

preview controls must feel optional; the purchase facts must remain dễ đọc mà không interacting.

**Acceptance checklist**

- [ ] Compatibility và variants are hiển thị rõ trước purchase.
- [ ] preview failure has a fallback that does not block purchase facts.
- [ ] Owned trạng thái does not show mua as the primary CTA.

### Event / Collection Store

**người chơi Intent**

Understand limited-thời gian event offer, collection completion, và what reward unlocks at completion.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Event header | event name, end timer, owned count |
| Reward preview | collection reward và unlock yêu cầu |
| Progress ladder | milestones và completion clarity |
| Event grid | event item cards với owned/new/locked trạng thái |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Event timer và owned count | always hiển thị rõ |
| 2 | Collection reward | visually rõ nhưng not misleading |
| 3 | Event item grid | shows chi phí và ownership per item |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| Owned count | owned / total, completion reward trạng thái |
| Event item card | item type, giá, owned, event-only label |
| Event challenge link | route to LiveOps event progress, not purchase duplicate |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Event ended | purchases disabled; show claim window nếu applicable |
| Collection complete | reward claim CTA replaces mua emphasis |
| Reward already claimed | show View Owned / Equip |
| Late purchase risk | final-hour cảnh báo in text near CTA |

**Input / Focus / Touch**

Focus starts at reward preview then grid. Console shoulder tabs switch shop sections; D-pad grid navigation does not skip locked cards.

**Designer ghi chú**

The trang không được imply random rewards unless the economy actually supports them. nếu deterministic, say exactly what is bought.

**Acceptance checklist**

- [ ] Event timer, owned count, và reward yêu cầu are hiển thị rõ.
- [ ] Ended event disables purchase với a rõ reason.
- [ ] Event challenge link routes to Progression/LiveOps.

### Battle Pass upgrade

**người chơi Intent**

Compare free và premium giá trị, understand tier skip options, và upgrade intentionally.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Pass summary | season thời gian, người chơi level, pending premium rewards |
| upgrade options | premium và bundle side by side |
| Immediate rewards | items unlocked immediately sau purchase |
| Route links | battle pass progress remains in Progression/LiveOps |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | upgrade options | giá và contents hiển thị rõ side by side |
| 2 | Immediate unlocks | prevents uncertainty sau purchase |
| 3 | Season timer | near title và CTA |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| Option card | giá, included benefits, tier skip count, exclusives |
| Reward preview | immediate unlocks, future rewards, claimed trạng thái |
| Season timer | days/hours; final day cảnh báo |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Already premium | show bundle upgrade only nếu valid; otherwise View Pass |
| Season ending | warn trước purchase và require confirmation nếu under threshold |
| Insufficient balance | route to Currency Top-Up với needed shortfall |
| Pass unavailable | disabled với season/platform reason |

**Input / Focus / Touch**

Option cards are first focus targets. Console left/right compares options; touch stacks option cards vertically on narrow layouts.

**Designer ghi chú**

Do not duplicate the full Battle Pass trang here. This surface owns purchase clarity only.

**Acceptance checklist**

- [ ] Premium vs bundle giá trị is directly comparable.
- [ ] Immediate unlocks sau upgrade are listed.
- [ ] Season-ending cảnh báo appears trước confirmation.

### Currency Top-Up

**người chơi Intent**

Choose a premium currency pack và understand platform checkout trước leaving the game UI.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| hiện tại balance | balance only; no transaction ledger |
| Pack selector | pack amount, bonus, best giá trị label |
| Checkout panel | platform/provider, localized giá, handoff copy |
| Action bar | back to offer, change pack, continue |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Selected pack giá | next to platform handoff CTA |
| 2 | Pack amounts | easy comparison mà không dark patterns |
| 3 | hiện tại balance | hiển thị rõ nhưng secondary |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| Pack card | amount, bonus, localized giá, best giá trị label nếu true |
| Platform panel | provider, account status, checkout availability |
| Return context | name of offer that required top-up nếu entered from purchase |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Platform checkout unavailable | disable continue và show provider reason |
| pending checkout | show pending receipt và do not offer repeated checkout blindly |
| Age/region restricted | block purchase với account/platform yêu cầu |
| Bonus promotion ended | refresh pack data và require reselection |

**Input / Focus / Touch**

Pack cards are a horizontal row on PC/console và a two-column grid on mobile. Confirm focus starts on selected pack, then checkout CTA.

**Designer ghi chú**

This is not a Wallet. Do not add history, ledger, hoặc balance management here.

**Acceptance checklist**

- [ ] No standalone wallet/history UI exists.
- [ ] Platform provider và localized giá are hiển thị rõ trước checkout.
- [ ] pending checkout prevents accidental repeated purchase.

### purchase Confirmation

**người chơi Intent**

Make a final informed quyết định với exact contents, giá, balance impact, và refund/platform note.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Item summary | exact item/bundle name và contents count |
| giá summary | final giá, adjustment, balance sau |
| Policy note | platform/refund note và non-power copy |
| Confirmation bar | cancel và confirm; hold khi required |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Final giá | closest information to confirm CTA |
| 2 | Contents | exact count và item list access |
| 3 | Balance sau | hiển thị rõ trước committing |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| Confirm CTA | enabled only khi giá và entitlement data are hiện tại |
| Hold progress | shows duration và cancel trạng thái |
| Policy link | opens non-blocking chi tiết panel nếu possible |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| giá changed | block confirm, refresh giá, ask for re-confirm |
| Insufficient balance | route to top-up với exact shortfall |
| dịch vụ timeout | no charge assumed; show retry/status copy |
| Duplicate ownership | block purchase và show owned trạng thái |

**Input / Focus / Touch**

Default focus is Cancel for high-chi phí hoặc real-money confirmation; otherwise focus starts on confirmation only sau summary is read. Touch uses hold button for expensive purchases.

**Designer ghi chú**

The confirmation modal is the trust anchor. No marketing copy should compete với final giá và contents.

**Acceptance checklist**

- [ ] Final giá, balance sau, và contents are hiển thị rõ together.
- [ ] giá change requires re-confirmation.
- [ ] High-chi phí purchase supports hold-to-confirm.

### purchase kết quả / Receipt

**người chơi Intent**

Know whether the purchase succeeded, what was received, và what to do next.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| kết quả title | success, pending, failed, refunded |
| Received items | exact entitlements granted hoặc pending |
| Receipt chi tiết | transaction/reference id khi available |
| Next actions | equip/view/back/giúp/retry depending on trạng thái |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | kết quả status | unmistakable text label |
| 2 | Granted items | names dễ đọc mà không scrolling for small purchases |
| 3 | Support route | hiển thị rõ for pending/failed/refunded |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| kết quả banner | status, timestamp, provider nếu available |
| Item list | item name, type, ownership điểm đến |
| giúp link | support article/report route với receipt id copied nếu possible |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| success | show equip/view primary actions |
| pending | say not to retry nếu charge may still complete; show refresh status |
| failed | show retry only nếu safe và no charge captured |
| Refunded | explain entitlement removal hoặc balance restoration |

**Input / Focus / Touch**

success focuses Equip/View. pending focuses Refresh Status. failed focuses safe Retry hoặc giúp depending on provider response.

**Designer ghi chú**

Never leave người chơi guessing whether money hoặc currency moved. kết quả copy phải được plain.

**Acceptance checklist**

- [ ] pending trạng thái warns against duplicate purchase.
- [ ] Receipt/support path is hiển thị rõ.
- [ ] success trạng thái routes to owned item usage.

### Redeem Code / Entitlement claim

**người chơi Intent**

Enter a code hoặc claim a platform entitlement và resolve duplicate/expired/region errors.

**Expanded ASCII Wireframe**

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

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Code entry | segmented input, paste support, redeem CTA |
| claim list | platform/founder/starter entitlements |
| Status lane | success/error/loading copy |
| giúp link | support for invalid hoặc missing entitlement |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Input/claim CTA | rõ action depending on mode |
| 2 | Status/error | inline và persistent sau submit |
| 3 | claim list | distinguishes ready, claimed, expired |

**Component yêu cầu**

| Component | Data / Behavior |
| :--- | :--- |
| Code input | paste, auto-hyphen, invalid nhân vật handling |
| claim card | entitlement name, source platform, status, contents |
| Error lane | duplicate, expired, region locked, dịch vụ unavailable |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Invalid code | focus returns to input và explains format |
| Duplicate | show already owned/claimed điểm đến |
| Expired | show expiration copy và support nếu applicable |
| Region locked | explain region/account mismatch |

**Input / Focus / Touch**

Keyboard paste should fill all code segments. Console input uses platform text entry. Touch uses large segmented fields và paste shortcut.

**Designer ghi chú**

Do not bury error chi tiết in a toast. claim failures are support-sensitive.

**Acceptance checklist**

- [ ] Duplicate, expired, và region-locked trạng thái have distinct copy.
- [ ] Successful claim lists granted items.
- [ ] Missing entitlement has support route.

---

## Analytics

| Signal | cách dùng |
| :--- | :--- |
| Shop section impressions | Measure which rows và tabs người chơi Xem |
| offer kiểm tra rate | Tune card clarity và hero placement |
| preview interaction | Understand cosmetic inspection behavior |
| Confirmation cancel | Identify unclear pricing hoặc trust issues |
| purchase pending/failure rate | Detect platform hoặc provider issues |
| Top-up entry source | Separate direct top-up from insufficient-balance recovery |
| Redeem failure reason | Improve code formatting và support copy |

---

## checklist Nghiệm Thu

- [ ] Commerce has no standalone Wallet màn hình.
- [ ] Shop Home, Featured offer, Bundle chi tiết, Item chi tiết, Event Store, Battle Pass upgrade, Currency Top-Up, purchase Confirmation, purchase kết quả, và Redeem claim are covered.
- [ ] Every purchasable item shows giá, currency type, ownership, platform restriction, và non-power/cosmetic context khi relevant.
- [ ] Balance appears only as a component in commerce header, top-up, confirmation, hoặc receipt.
- [ ] purchase failures và pending trạng thái include duplicate-charge-safe copy và support route.
- [ ] Battle Pass purchase UX links to Progression/LiveOps for reward progress instead of duplicating it.
