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
| Economy | [Economy & Monetization Design](../gamedesign/economy/index.html) |
| Progression / Battle Pass | [Progression & LiveOps màn hình](progression_liveops_screens/index.html) |
| Global UX | [Global UX Standards](global_ux_standards/index.html) |
| Visual style | [Visual Style & Art Guidelines](visual_style/index.html) |
| Settings và hệ thống trạng thái | [Settings & hệ thống màn hình](commerce_settings_system_screens/index.html) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index/index.html) | Hub tài liệu UI/UX đầy đủ |
| [Screen Groups Overview](screen_groups_overview/index.html) | Taxonomy vòng đời màn hình và template spec cho designer |
| [Progression & LiveOps màn hình](progression_liveops_screens/index.html) | Battle pass progress, event progress, ranked, rewards, và news |
| [Settings & hệ thống màn hình](commerce_settings_system_screens/index.html) | Auth, setup, settings, privacy, diagnostics, và hệ thống dialogs |
| [Global UX Standards](global_ux_standards/index.html) | Quy tắc chung cho navigation, focus, trạng thái, modal, và accessibility |

---

## Inventory Màn Hình

| màn hình | mục tiêu | CTA chính | trạng thái chính |
| :--- | :--- | :--- | :--- |
| Shop Home | Duyệt các section hiện tại của shop và offer nổi bật | Xem offer / preview | loading, empty rotation, offline, platform restricted |
| Featured offer / Rotating Store | Scan daily/weekly offer, discounts, và owned items | kiểm tra / mua | owned, discounted, expires soon, unavailable |
| Bundle chi tiết | Hiểu nội dung bundle và giá đã điều chỉnh | Preview Bundle / mua | partially owned, discounted, insufficient balance |
| Item chi tiết / 3D preview | kiểm tra a cosmetic trước purchase | Rotate / Equip preview / mua | incompatible item, selectable variants, owned |
| Event / Collection Store | Track limited collection progress và event rewards | View Reward / mua Item | event ended, collection complete, timer cảnh báo |
| Battle Pass upgrade | upgrade free pass to premium hoặc premium bundle | upgrade Pass | already premium, season ending, insufficient balance |
| Currency Top-Up | mua premium currency packs thông qua platform checkout | Select Pack / Continue | platform unavailable, pending checkout, bonus pack |
| purchase Confirmation | Confirm exact giá, contents, và consequence | Confirm purchase | insufficient balance, platform handoff, hold required |
| purchase kết quả / Receipt | Show success, failure, pending, refund, và next action | Equip / View / Retry | success, pending, failed, refunded |
| Redeem Code / Entitlement claim | claim promo codes, founders packs, và platform entitlements | Redeem / claim | duplicate, expired, region locked, already owned |

Commerce không định nghĩa màn hình Wallet riêng. Currency balance chỉ xuất hiện như một component trong shop header, currency top-up, confirmation, và receipt.

---

## Commerce Rules

| Rule | Yêu cầu |
| :--- | :--- |
| No gameplay advantage | Offer phải là cosmetic, account service, hoặc non-power rõ ràng. Nếu item chỉ đổi presentation, hãy nói rõ gần purchase CTA. |
| Price clarity | Final price, discounted price, original price, tax/platform handoff, và currency type phải hiển thị trước confirmation. |
| Ownership clarity | Owned, partially owned, duplicate, và bundle-adjusted states phải dùng label đọc được, không chỉ dựa vào màu. |
| Timer clarity | Daily, weekly, event, và season timer phải show exact remaining time và expired state rõ ràng. |
| Confirmation | Premium currency và real-money action luôn cần confirmation. Purchase đắt hoặc irreversible dùng hold-to-confirm. |
| Failure safety | Pending/failed purchase copy phải cảnh báo không spam retry nếu transaction có thể vẫn hoàn tất, đồng thời expose support. |

---

## Commerce System Model

Commerce là hệ thống nhạy cảm về niềm tin. UI phải giúp người chơi hiểu họ đang mua gì, vì sao offer khả dụng, họ đã sở hữu gì, payment rời game như thế nào, và support có thể kiểm chứng gì sau đó.

| Entity | Định nghĩa | Yêu cầu UI |
| :--- | :--- | :--- |
| `Offer` | Cách merchandised một hoặc nhiều product có thể mua | Hiển thị title, visual, price, timer, ownership, restriction, và CTA |
| `SKU` | Đơn vị mua hàng của platform/provider | Không phải primary UI; chỉ hiện trong receipt/help khi cần support |
| `Product` | Item hoặc service được grant sau purchase | Hiển thị category, rarity, compatibility, và non-power context |
| `Bundle` | Offer gồm nhiều product | Hiển thị từng product và owned-item adjustment |
| `Entitlement` | Quyền sở hữu được grant sau purchase, redeem, event, hoặc platform claim | Hiển thị destination, status, duplicate state, và support route |
| `CurrencyPack` | Real-money purchase grant premium currency | Hiển thị amount, bonus, localized price, provider, và handoff state |
| `Receipt` | Bằng chứng transaction hoặc entitlement sync cho player | Hiển thị status, provider/reference id, timestamp nếu có, và granted items |
| `PlatformProvider` | Steam, PlayStation, Xbox, Epic, App Store, Google Play, hoặc provider tương đương | Hiển thị availability, account/region restriction, và provider handoff copy |
| `OwnershipState` | Quan hệ giữa player và product/bundle | `new`, `owned`, `partially owned`, `duplicate`, `incompatible`, `locked`, `pending` |

### Offer Data Contract

| Field | Dùng cho | Display rule |
| :--- | :--- | :--- |
| Offer id / SKU id | support, analytics, provider handoff | Không phải primary UI; dùng trong receipt/help khi cần |
| Title và short description | mọi offer | Fit trong card/detail header, không phụ thuộc hover |
| Product category | mọi product | Operator skin, weapon skin, emote, banner, charm, service, currency pack |
| Rarity / collection | cosmetic và event item | Text label cộng icon/color treatment |
| Price và currency type | mọi purchasable offer | Final price gần CTA; original price khi có discount |
| Timer / availability | rotating, event, seasonal offer | Exact remaining time cộng expired fallback |
| Ownership state | mọi product và bundle | Label đọc được trên card, detail, confirmation, receipt |
| Compatibility | item detail và bundle | Supported operator/weapon/class hoặc limitation rõ |
| Platform / region restriction | offer bị restriction | Disabled CTA với exact reason và support/account route |
| Non-power label | cosmetic/service | Plain copy gần price hoặc confirmation |

### Product / SKU Taxonomy

| Type | Allowed | Commerce rule |
| :--- | :--- | :--- |
| Operator cosmetics | Yes | Không stat, hitbox, visibility, audio, hoặc ability advantage |
| Weapon skins | Yes | Không recoil, sight clarity, silhouette, tracer, sound, hoặc hit readability advantage |
| Emotes / banners / charms | Yes | Cosmetic only; không ảnh hưởng combat timing hoặc visibility |
| Battle pass upgrade | Yes | Purchase UX ở đây; reward/progress view ở Progression/LiveOps |
| Currency pack | Yes | Top-up only; không ledger hoặc standalone Wallet screen |
| Convenience service | Conditional | Phải earnable/capped và không đổi combat certainty |
| Paid RNG / loot box | No | Không hỗ trợ randomized real-money purchase |
| Combat power | No | Không bán weapon, armor, stat, protected combat slot, hoặc better matchmaking |

### Checkout, Entitlement, Và Compliance Rules

| Topic | Requirement |
| :--- | :--- |
| Ownership | Owned/duplicate purchase bị block; partially owned bundle show adjusted price |
| Price stale | Block confirmation, refresh price, và yêu cầu confirm lại |
| Provider handoff | Show provider name/localized price; game không assume success trước provider result |
| Pending charge | Copy phải nói không retry vì transaction có thể vẫn hoàn tất |
| Refund/removal | Explain entitlement removal hoặc balance restoration |
| Minor/region/spending limit | CTA disabled với exact requirement và platform/account route |
| Random rewards | Paid RNG không supported; deterministic purchase phải nói chính xác item được grant |

Commerce grant account entitlements, cosmetics, premium currency packs, battle pass upgrades, và non-power services. Commerce không được grant paid physical combat-power item instances như weapons, armor, ammo, high-tier storage, protected combat slots, hoặc stat-bearing gear. Nếu purchase unlock cosmetic cho gear, gameplay-bearing item instance vẫn theo Inventory/Gear lifecycle rules.

---

## Shop Information Architecture

Commerce entry point phải giữ context: global Shop nav, Battle Pass upgrade, Event Store, insufficient balance route, redeem/deep link, hoặc receipt/support route.

| Entry Point | Hành vi landing |
| :--- | :--- |
| Horizontal global nav: Shop | Mở Shop Home với curated/featured sections |
| Battle Pass upgrade | Mở Battle Pass Upgrade và có return link về Battle Pass progress |
| Event purchase CTA | Mở Event / Collection Store scoped theo active event |
| Insufficient balance | Mở Currency Top-Up với return context về blocked offer |
| Redeem/deep link | Mở Redeem / Entitlement Claim hoặc target offer nếu valid |
| Receipt/support | Mở Purchase Result / Receipt với support context |

### Commerce Tabs Và Shop Home Priority

| Tab / Section | Purpose / Rule |
| :--- | :--- |
| Home | Curated overview và hero offer |
| Featured | Daily/weekly rotating offers |
| Bundles | Bundle value, content count, owned adjustment |
| Event | Event collection, deterministic rewards, event timer |
| Battle Pass | Upgrade purchase surface only |
| Currency | Premium currency pack top-up, không Wallet |
| Redeem | Code entry và entitlement claim |

Thứ tự ưu tiên của Shop Home: hero offer, daily/weekly featured, bundles, event offers, Battle Pass upsell, currency top-up, redeem/claim. Personalized row có thể đổi thứ tự card, nhưng thứ tự tab và vocabulary của section phải ổn định.

### Offer Card Anatomy Và Merchandising Guardrails

| Element / Rule | Requirement |
| :--- | :--- |
| Card image | Stable 4:5 hoặc 16:9 ratio theo section; không layout shift |
| Title/category/rarity | Text label readable; color alone không đủ |
| Price/discount | Final price + currency type; original price khi discounted |
| Timer | Exact remaining time; không flashing pressure animation |
| Badge stack | Priority: `Owned`, `Platform Locked`, `Ends Soon`, `Discount`, `New`, `Event`; tối đa 3 badge |
| Best value | Chỉ dùng nếu value-per-price thật sự cao nhất trong set hiển thị |
| Bundle value | Phải show content count và owned-item adjustment |
| Cosmetic trust | Non-power copy gần price ở detail và confirmation |

---

## Designer-Ready màn hình Specs

### Shop Home

**người chơi Intent**

Xem nội dung mới, hiểu balance và platform status hiện tại, rồi chọn shop section mà không mất ngữ cảnh.

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

Trang này phải cho cảm giác là một cửa hàng, không phải ví. Balance chỉ là utility chip; offer và preview mới là trọng tâm của surface.

**Acceptance checklist**

- [ ] Hero offer has giá, discount, timer, ownership, và preview CTA.
- [ ] Every purchase-disabled trạng thái has a dễ đọc reason.
- [ ] Balance hiển thị rõ mà không tạo điểm đến Wallet riêng.

### Featured offer / Rotating Store

**người chơi Intent**

Scan nhanh nhiều offer có thời hạn và quyết định item hoặc bundle nào đáng xem kỹ.

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

Hiểu bundle gồm gì, người chơi đã sở hữu gì, và giá đã điều chỉnh có hợp lý không.

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
- [ ] Trạng thái owned không hiển thị mua như CTA chính.

### Event / Collection Store

**người chơi Intent**

Hiểu offer sự kiện có thời hạn, tiến độ hoàn tất collection, và reward được mở khi hoàn tất.

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
| pending checkout | hiển thị receipt pending và không khuyến khích checkout lặp lại một cách mù quáng |
| Age/region restricted | block purchase với account/platform yêu cầu |
| Bonus promotion ended | refresh pack data và require reselection |

**Input / Focus / Touch**

Pack cards are a horizontal row on PC/console và a two-column grid on mobile. Confirm focus starts on selected pack, then checkout CTA.

**Designer ghi chú**

Đây không phải Wallet. Không thêm history, ledger, hoặc balance management ở đây.

**Acceptance checklist**

- [ ] No standalone wallet/history UI exists.
- [ ] Platform provider và localized giá are hiển thị rõ trước checkout.
- [ ] Pending checkout ngăn purchase lặp lại ngoài ý muốn.

### purchase Confirmation

**người chơi Intent**

Đưa ra quyết định cuối cùng với đầy đủ nội dung, giá, tác động tới balance, và ghi chú refund/platform.

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

| Signal | Cách dùng |
| :--- | :--- |
| Shop impression | Đo volume vào shop theo source và platform |
| Tab / section impression | Đo row và tab nào player thật sự thấy |
| Offer card selected | Tune card clarity, badging, và hero placement |
| Preview opened / interacted | Hiểu hành vi inspect cosmetic và lỗi asset |
| Purchase intent | Track Buy/Upgrade/Top-Up CTA trước confirmation |
| Top-up started / completed / cancelled | Tách direct top-up khỏi insufficient-balance recovery |
| Confirmation shown / confirmed / cancelled | Tìm vấn đề pricing clarity, trust, hoặc accidental entry |
| Platform checkout pending / failed / succeeded | Detect provider, region, và account issues |
| Receipt viewed / refreshed | Đo result state có giải quyết uncertainty không |
| Support opened | Tìm purchase trust hoặc entitlement problem areas |
| Redeem failure reason | Cải thiện code formatting, entitlement sync, và support copy |

Analytics không được log full payment detail, personal data, hoặc raw redemption code. Dùng offer id, reason enum, provider class, và safe receipt reference.

---

## Commerce QA Checklist

| Scenario | Expected Result |
| :--- | :--- |
| Price changes while confirmation is open | Confirm bị block, price refresh, và player phải confirm lại |
| Offer expires while selected | Buy disabled với expired copy và refresh/back route |
| Owned item purchase attempt | Purchase bị block và route tới Equip/View Owned |
| Partially owned bundle | Adjusted price và per-item owned labels hiển thị rõ |
| Fully owned bundle | Purchase disabled; bundle route tới owned items |
| Insufficient balance | Exact shortfall và Currency Top-Up route hiển thị |
| Platform checkout unavailable | Checkout disabled với provider/account reason |
| Pending transaction | Receipt cảnh báo không retry và có refresh/support |
| Refund/removal | Entitlement removal hoặc balance restoration được giải thích |
| Region/minor/spending restriction | CTA disabled với exact requirement và platform/account route |
| Offline/cached shop | Chỉ browse phần an toàn; purchase disabled với reason |
| Duplicate entitlement | Already claimed/owned destination và support route hiển thị |
| Missing entitlement | Receipt/provider/account context và support route hiển thị |
| Preview asset failure | Fallback visual xuất hiện mà không che price hoặc compatibility |

---

## checklist Nghiệm Thu

- [ ] Commerce không có standalone Wallet screen.
- [ ] Shop Home, Featured Offers, Bundle Detail, Item Detail, Event Store, Battle Pass Upgrade, Currency Top-Up, Purchase Confirmation, Purchase Result, và Redeem Claim đều covered.
- [ ] Mọi purchasable item show price, currency type, ownership, platform restriction, và non-power/cosmetic context khi relevant.
- [ ] Balance chỉ xuất hiện như component trong commerce header, top-up, confirmation, hoặc receipt.
- [ ] Purchase failure và pending state có duplicate-charge-safe copy và support route.
- [ ] Battle Pass purchase UX link sang Progression/LiveOps cho reward progress thay vì duplicate.
- [ ] Offer data contract, SKU/product taxonomy, ownership states, pricing rules, và checkout provider states đã defined.
- [ ] Shop IA cover entry points, tab structure, section priority, empty/offline fallback, và offer card anatomy.
- [ ] Analytics cover full commerce funnel mà không log raw payment data hoặc redemption code.
- [ ] QA checklist cover stale price, expired offer, pending transaction, refund, minor/region restriction, và missing entitlement.
