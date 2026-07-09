---
title: "Settings & hệ thống màn hình"
type: docs
weight: 10
---

## Mục Đích

Settings và hệ thống màn hình handle the sensitive parts of the trải nghiệm: account access, platform services, configuration, privacy, diagnostics, errors, và recovery. These màn hình phải được plain, trustworthy, và explicit.

Tham chiếu chính:

| hệ thống | source |
| :--- | :--- |
| User settings | [User Settings & Configuration](../GameDesign/UserSettings.md) |
| Settings matrix | [Settings matrix](../GameDesign/UserSettings_Matrix.md) |
| Accessibility | [Accessibility Design](../GameDesign/Accessibility.md) |
| loading màn hình | [Async loading màn hình Design](LoadingScreen_Design.md) |
| Commerce | [Commerce màn hình](Commerce_Screens.md) |
| Settings technical hệ thống | [Settings hệ thống](../../GDD_Technical/hệ thống/SettingsSystem.md) |

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [màn hình Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](Global_UX_Standards.md) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [Commerce màn hình](Commerce_Screens.md) | Shop, offer, currency top-up, purchase confirmation, receipts, và entitlement claim |
| [loading màn hình Design](LoadingScreen_Design.md) | Boot, splash, lobby, kết quả, và reconnect loading rules |
| [Progression & LiveOps màn hình](Progression_LiveOps_Screens.md) | Battle pass, rewards, ranked, news, và LiveOps goals |
| [Social màn hình](Social_Screens.md) | Privacy, safety, report/block, và communication settings |

---

## Inventory Màn Hình

| màn hình | mục tiêu | primary CTA | chính trạng thái |
| :--- | :--- | :--- | :--- |
| Boot / Splash | Start app và meet platform yêu cầu | Continue / Skip nếu allowed | first boot, shader prep, update required |
| Login / Account Link | Authenticate và sync identity | Sign In / Link | failed auth, conflict, offline, age gate |
| EULA / Privacy | Collect required consent | Accept | declined, updated policy, region-cụ thể |
| First-thời gian Setup | Choose language, accessibility, controls, privacy | Continue | incomplete, recommended preset |
| Tutorial Gate | Route new người chơi into basics | Start Tutorial | skipped, required, returning người chơi |
| Settings | Configure controls, graphics, audio, gameplay, accessibility | Apply | unsaved changes, platform lock, ranked lock |
| Account / Privacy | Manage identity, cross-play, streamer mode, data | Save | unlink cảnh báo, privacy conflict |
| Diagnostics | Show FPS, network, logs, support info | Copy / Submit | offline, report sent, permission denied |
| hệ thống Dialogs | Handle errors, maintenance, version mismatch, reconnect | Retry / Update / Exit | non-recoverable, queued maintenance |

---

## Boot, Splash, và loading

Boot và splash màn hình should stay minimal. loading taxonomy lives in [loading màn hình Design](LoadingScreen_Design.md); this section owns the hệ thống-facing trạng thái.

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                                                                  |
|                         EXTRACTION PROTOCOL                      |
|                                                                  |
|                    [========== 45% ==========]                   |
|                    Preparing shaders and profile...              |
|                                                                  |
| Version 1.0.4                                      Status: OK    |
+------------------------------------------------------------------+
```

| trạng thái | yêu cầu |
| :--- | :--- |
| First boot | Show logo, progress, và what is being prepared nếu longer than expected |
| Shader/cache prep | Name the process và avoid fake progress |
| Update required | Show hiện tại/required version và platform update path |
| Maintenance | Show start/end thời gian nếu known và support/status link |
| Offline start | Explain which local màn hình are available |
| Splash skip | Allowed only sau minimum brand/legal display duration |

---

## Login và Account Link

Layout (PC/Console)

```
+------------------------------------------------------------------+
| ACCOUNT SIGN IN                                                  |
|------------------------------------------------------------------|
| Sign in to sync stash, progress, purchases, and settings.        |
|                                                                  |
| [Sign in with Platform]                                          |
| [Link Existing Account]                                          |
| [Continue Offline]                                               |
|                                                                  |
| Conflict / error area: none                                      |
|------------------------------------------------------------------|
| Privacy Policy | Terms | Support ID                              |
+------------------------------------------------------------------+
```

| Spec | yêu cầu |
| :--- | :--- |
| mục tiêu | Get the người chơi into the correct account với rõ consequences for linking/sync |
| Entry points | App start, account settings, cross-progression prompt |
| primary CTA | Sign In / Link Account |
| secondary actions | Continue offline nếu supported, switch account, support |
| Destructive actions | Unlink account requires explicit consequence confirmation |

### Account trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| No account | Show sign-in providers và privacy note |
| Auth failed | Show provider, retry, và support |
| Account conflict | Compare account names, timestamps, và progression summaries |
| Cloud sync conflict | cách dùng local/cloud/merge choices from [User Settings](../GameDesign/UserSettings.md) |
| Age gate | Region-appropriate messaging và blocked tính năng explanation |

---

## First-thời gian Setup

Layout (PC/Console)

```
+------------------------------------------------------------------+
| PRIVACY AND TERMS                                                |
|------------------------------------------------------------------|
| Please review required terms before online play.                 |
|                                                                  |
| [ ] I accept Terms of Service                                    |
| [ ] I accept Privacy Policy                                      |
| [ ] I understand voice/chat moderation rules                     |
|                                                                  |
| Region: SEA                 Age gate: Passed                     |
|------------------------------------------------------------------|
| [Back] [Open Terms] [Open Privacy]              [Continue]       |
+------------------------------------------------------------------+
```

Layout (PC/Console)

```
+--------------------------------------------------------------------+
| FIRST-TIME SETUP                                      Step 2 / 5   |
|--------------------------------------------------------------------|
| Steps: Language -> Accessibility -> Controls -> Privacy -> Tutorial|
|                                                                    |
| Accessibility Starter                                              |
| [x] Larger text       [x] Subtitles                                |
| [ ] Reduce motion     [ ] Colorblind mode v                        |
| [ ] Hold alternatives                                              |
|--------------------------------------------------------------------|
| [Back]                                      [Continue]             |
+--------------------------------------------------------------------+
```

| Step | yêu cầu |
| :--- | :--- |
| Language | Text/audio/subtitle choices và region defaults |
| Accessibility starter | offer text size, colorblind, motion, subtitle, hold alternatives |
| Controls | Detect input và offer preset |
| Privacy | Cross-play, presence, chat/voice, streamer-safe defaults |
| Tutorial | Explain tutorial giá trị và whether it can be skipped |

First-thời gian setup phải được short. Advanced settings nên được reachable nhưng not forced trước first play.

Layout (PC/Console)

```
+-------------------------------------------------------------------+
| TUTORIAL RAID                                                     |
|-------------------------------------------------------------------|
| Operation Zero teaches movement, looting, healing, and extraction.|
| Recommended before entering live raids.                           |
|                                                                   |
| Rewards: Starter medkit, 5,000 credits, basic ammo                |
| Status: Not completed                                             |
|                                                                   |
| [Start Tutorial] [Skip for Now] [Accessibility Settings]          |
+-------------------------------------------------------------------+
```

## Settings

Settings categories follow [User Settings](../GameDesign/UserSettings.md) và the chi tiết [Settings matrix](../GameDesign/UserSettings_Matrix.md).

Layout (PC/Console)

```
+-----------------------------------------------------------------------------------------------+
| SETTINGS                                                                                      |
|-----------------------------------------------------------------------------------------------|
| Controls | Graphics | Audio | Gameplay/HUD | Accessibility | Privacy | Language | Diagnostics |
|-----------------------------------------------------------------------------------------------|
| SETTINGS DETAIL                                                   | HELP / PREVIEW            |
| Preset: Competitive v                                             | affects input             |
| Resolution 1920x1080 v                                            | preview/revert            |
| V-Sync [On | Off]                                                 | platform note             |
| FPS Limit [-----144-----]                                         | ranked lock why           |
| Texture Quality High v                                            |                           |
| Ranked locked settings show reason                                |                           |
|-----------------------------------------------------------------------------------------------|
| [Reset Category] [Revert]                                                   [Apply]           |
+-----------------------------------------------------------------------------------------------+
```

| Category | UI yêu cầu |
| :--- | :--- |
| Controls | Remap, sensitivity, aim assist, gyro, và PC/Console HUD layout |
| Graphics | Presets, resolution/performance, preview và revert timer for risky changes |
| Audio | Volumes, output, voice, subtitles, dynamic range |
| Gameplay & HUD | Reticle, minimap, prompts, damage feedback, HUD scale |
| Accessibility | Color, text, motion, timing, input assist |
| Social & Privacy | Invites, presence, chat, cross-play, streamer mode |
| Language & Region | Text, audio, units, server region |
| Diagnostics | FPS, ping, telemetry, crash reporting |

### Settings trạng thái

| trạng thái | Behavior |
| :--- | :--- |
| Unsaved changes | Apply / Revert / Cancel hiển thị rõ |
| Risky display change | Revert countdown |
| Ranked lock | disabled với fairness explanation |
| Platform unavailable | Hidden nếu irrelevant; disabled với reason nếu người chơi expects it |
| Cloud conflict | Show local/cloud/merge choices |
| Preset applied | Show changed settings và undo |

---

## Account, Privacy, và Safety

Layout (PC/Console)

```
+------------------------------------------------------------------+
| ACCOUNT / PRIVACY                                                |
|------------------------------------------------------------------|
| ACCOUNT                         | PRIVACY / SAFETY               |
| Player ID: EP-284712            | Profile: Friends v             |
| Linked: Steam, EOS              | Invites: Friends Only v        |
| Region: SEA                     | Cross-play: On                 |
|                                 | Streamer Mode: Off             |
|------------------------------------------------------------------|
| [Link Provider] [Unlink Account] [Block List] [Save]             |
+------------------------------------------------------------------+
```

| màn hình | yêu cầu |
| :--- | :--- |
| Account | Linked providers, người chơi ID, region, support IDs |
| Privacy | Presence, profile visibility, invite rules, cross-play |
| Streamer Mode | Hide names, invite codes, account IDs, sensitive notifications |
| Data | Telemetry consent, privacy policy, data request path |
| Block List | View và unblock với confirmation |

Privacy changes should apply immediately khi possible và show restart/session yêu cầu otherwise.

---

## Diagnostics và Support

Layout (PC/Console)

```
+------------------------------------------------------------------+
| DIAGNOSTICS / SUPPORT                                            |
|------------------------------------------------------------------|
| Network: SEA-02  Ping 38ms  Loss 0%                              |
| Performance: 86 FPS  Frame 11.6ms  Preset High                   |
| Account: EP-284712                                               |
|                                                                  |
| Bug category: [UI / Menu v]                                      |
| Notes: [____________________________________________]            |
| Attach: [x] Screenshot [x] Logs                                  |
|------------------------------------------------------------------|
| [Copy Support ID] [Submit Report] [Open Support]                 |
+------------------------------------------------------------------+
```

| Function | yêu cầu |
| :--- | :--- |
| Network info | Ping, packet loss, region, server ID khi safe |
| Performance | FPS, frame thời gian, graphics preset, device profile |
| Bug report | Category, description, screenshot/log attach, consent |
| Crash recovery | Explain crash, restore options, report path |
| Copy support ID | One-click copy với confirmation |

Diagnostics should avoid exposing sensitive tokens, IPs, hoặc private account information in shareable screenshots.

---

## hệ thống Dialogs

Layout (PC/Console)

```
+------------------------------------------------------------------+
| dimmed parent screen                                             |
|                                                                  |
|              +--------------------------------------+            |
|              | VERSION MISMATCH                     |            |
|              |--------------------------------------|            |
|              | Current: 1.0.3                       |            |
|              | Required: 1.0.4                      |            |
|              | Update is required to play online.   |            |
|              |                                      |            |
|              | [Exit]                  [Update]     |            |
|              +--------------------------------------+            |
+------------------------------------------------------------------+
```

| Dialog | Required Content |
| :--- | :--- |
| Network error | What failed, retry, offline/local option nếu available |
| Version mismatch | hiện tại version, required version, update action |
| Maintenance | Expected end thời gian nếu available, status link |
| Server full/queue | Queue position hoặc retry timing |
| Save conflict | source, timestamp, impact, choices |
| Data corruption | What is recoverable và support path |
| Entitlement/dịch vụ conflict | Account provider, sync status, support path; purchase receipts live in [Commerce màn hình](Commerce_Screens.md) |

---

## Designer-Ready màn hình Specs

Settings và hệ thống surfaces phải được plain, trustworthy, và explicit. Every disabled trạng thái must explain why, và every account, privacy, unlink, hoặc abandon action must trạng thái its consequence trước commit.

### Boot / Splash / loading

**người chơi Intent**

Start the application, understand long waits, và know whether online play is available.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
|                                EXTRACTION PROTOCOL                             |
|--------------------------------------------------------------------------------|
| Progress: 45%  Preparing shaders and profile                                   |
| Version 1.0.4 | Status OK | Region service online                              |
| [Offline Options]                                              [Continue]      |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Brand area | logo/title với required legal timing |
| Progress area | real operation name và truthful progress/indeterminate trạng thái |
| Status footer | version, dịch vụ, offline availability |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | hiện tại operation | nếu wait exceeds expected thời gian |
| 2 | Error/update trạng thái | Must override normal loading |
| 3 | Version/status | Footer-level |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Progress indicator | No fake precision; operation label required |
| Update prompt | hiện tại/required version và platform action |
| Offline option | only shown nếu supported và names limits |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| First boot | show setup/legal sequence |
| Shader prep | name process và avoid fake progress |
| Update required | block online với update route |
| Maintenance | show known end thời gian/status link |
| Offline start | list available local màn hình |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Continue | Enter/click | A / Cross | Tap CTA |
| Retry | Click | A / Cross | Tap |
| Offline | Click option | Focus option | Tap option |

**Designer ghi chú**

- loading copy nên được operational, not lore-only, khi wait is long.

**Acceptance checklist**

- [ ] Update, maintenance, offline, first boot, và shader prep trạng thái are covered.

### Login / Account Link / EULA

**người chơi Intent**

Enter the correct account, resolve sync/linking conflicts, và understand required legal consent trước online play.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| ACCOUNT SIGN IN / LINK                                                         |
|--------------------------------------------------------------------------------|
| Sign in to sync stash, progress, purchases, and settings.                      |
| [Sign in with Platform] [Link Existing Account] [Continue Offline]             |
| Conflict area: account names, timestamps, progression summary, consequence     |
| Legal: [Terms] [Privacy] Required consent [Accept]                             |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Auth actions | provider sign-in, link, offline |
| Consequence text | what sync/link/offline changes |
| Conflict panel | compared accounts và choice impact |
| Legal panel | required policy, region, accept/decline |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | primary sign-in/link action | rõ và trustworthy |
| 2 | Consequence/conflict | trước irreversible choice |
| 3 | Support/legal links | Persistent footer |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Provider button | provider name, network/loading/error trạng thái |
| Conflict choice | local/cloud/merge label và timestamp |
| Consent CTA | disabled until required terms acknowledged |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Auth failed | provider, retry, support |
| Account conflict | compare names/timestamps/progression |
| Cloud sync conflict | local/cloud/merge choices |
| Age gate | region-appropriate blocked tính năng explanation |
| Declined terms | explain online access consequence |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Sign in | Click | A / Cross | Tap |
| Review legal | Link/click | Focus link | Tap link |
| Choose conflict | Radio/click | D-pad + A | Tap option |

**Designer ghi chú**

- Do not compress account conflict copy; trust is more quan trọng than speed here.

**Acceptance checklist**

- [ ] Auth failure, account conflict, sync conflict, age gate, và declined terms are covered.

### First-thời gian Setup / Tutorial Gate

**người chơi Intent**

Choose language, accessibility, controls, privacy, và tutorial path trước entering the game loop.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| FIRST-TIME SETUP                                      Step 2/5                 |
|--------------------------------------------------------------------------------|
| Language | Accessibility Preset | Controls | Privacy | Tutorial                |
| Selected: Larger Text + Subtitles + Hold Alternatives                          |
| Recommendation: Start Tutorial before first raid                               |
| [Back] [Preview Settings] [Continue]                                           |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Stepper | hiện tại step và remaining setup |
| Main choice | language/accessibility/control/privacy/tutorial |
| preview | shows impact trước commit |
| CTA row | back, preview, continue |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | hiện tại step action | rõ và simple |
| 2 | Accessibility choices | Offered trước gameplay |
| 3 | Tutorial recommendation | rõ nhưng not coercive unless required |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Accessibility preset | labels affected settings |
| Privacy preset | public/friends/private/streamer mode explanation |
| Tutorial gate | start/skip/required trạng thái |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Incomplete | Continue disabled với missing field |
| Recommended preset | explain why recommended |
| Tutorial required | start CTA only |
| Returning người chơi | skip to home với edit settings route |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Choose option | Click | D-pad + A | Tap |
| preview | Click | Y / Triangle | preview button |
| Continue | Enter/click | A / Cross | Sticky CTA |

**Designer ghi chú**

- Accessibility is part of onboarding, not buried in settings.

**Acceptance checklist**

- [ ] Language, accessibility, control, privacy, và tutorial trạng thái are covered.

### Settings

**người chơi Intent**

Find a setting, understand its effect, apply/revert safely, và know khi platform/ranked locks prevent changes.

**Expanded ASCII Wireframe**

```
+---------------------------------------------------------------------------------------------------------+
| SETTINGS                                                                            Unsaved *           |
|---------------------------------------------------------------------------------------------------------|
| Controls | Graphics | Audio | Gameplay/HUD | Accessibility | Account | Privacy | Language | Diagnostics |
|---------------------------------------------------------------------------------------------------------|
| SETTING LIST / SELECTED TAB                                      | HELP / PREVIEW PANEL                 |
| Aim Sensitivity 42 [slider]                                      | affects camera aim speed             |
| Controller Layout: Tactical v                                    | device-specific note                 |
| Hold-to-confirm 1.5s [stepper]                                   | accessibility impact                 |
| Ranked lock: input preset cannot change                          | fairness reason                      |
|---------------------------------------------------------------------------------------------------------|
| ACTION BAR: [Reset Category] [Revert]                                             [Apply Changes]       |
+---------------------------------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Settings top tabs | horizontal category navigation inside Settings: Controls, Graphics, Audio, Gameplay/HUD, Accessibility, Account, Privacy, Language, Diagnostics |
| Setting list | label, control, hiện tại giá trị, lock trạng thái |
| giúp panel | selected setting explanation |
| Apply bar | unsaved, revert, apply, reset |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Unsaved/apply trạng thái | Persistent |
| 2 | Selected setting và giúp | rõ relationship |
| 3 | Locks/cảnh báo | hiển thị rõ trước attempted change |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Setting row | label, control, giá trị, platform/ranked lock |
| Search kết quả | category path và setting name |
| Apply bar | changed count, apply/revert/reset |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Unsaved changes | Apply/revert hiển thị rõ |
| Platform lock | disabled với reason |
| Ranked lock | disabled với mode reason |
| Invalid giá trị | error và revert |
| Requires restart | flag trước apply |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Search | Ctrl-F | Y / Triangle | Search field |
| Adjust giá trị | Mouse/keys | D-pad/sticks | Slider/stepper |
| Apply | Click | A / Cross | Sticky CTA |

**Designer ghi chú**

- giúp copy should describe người chơi-facing effect, not engine terms.

**Acceptance checklist**

- [ ] Unsaved, revert, platform lock, ranked lock, invalid, và restart trạng thái are covered.

### Account / Privacy / Safety

**người chơi Intent**

Manage identity, cross-play, streamer mode, data/privacy, account links, và safety preferences với rõ consequences.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| ACCOUNT / PRIVACY / SAFETY                                                     |
|--------------------------------------------------------------------------------|
| Profile visibility: Friends v | Streamer Mode: Off | Crossplay: On             |
| Linked accounts: Platform OK | Unlink [Danger]                                 |
| Data: Export | Delete Request | Support ID                                     |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Privacy controls | visibility, streamer, invite code, online status |
| Account links | providers, link/unlink trạng thái |
| Data controls | export/delete/support |
| Safety | blocked users, muted users, communication filters |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Privacy visibility | rõ hiện tại trạng thái |
| 2 | Unlink/delete consequences | trước CTA |
| 3 | Safety lists | Manageable và reversible |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Privacy dropdown | explains hiển thị rõ fields |
| Streamer toggle | names hidden fields |
| Unlink CTA | consequence modal required |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Privacy conflict | show setting precedence |
| Streamer on | preview replaced fields |
| Unlink cảnh báo | name lost sync/purchase implications |
| Delete request | cooldown/confirmation/support path |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Toggle | Click | A / Cross | Tap |
| Manage list | Click row | Focus row | Tap row |
| Dangerous action | Hold/confirm | Hold confirm | Confirm sheet |

**Designer ghi chú**

- Dangerous account actions need calm, cụ thể copy.

**Acceptance checklist**

- [ ] Privacy, streamer, unlink, delete, block/mute management trạng thái are covered.

### Diagnostics và Support

**người chơi Intent**

See performance/network status, copy support information, submit logs, và understand permission/network failures.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| DIAGNOSTICS / SUPPORT                                                          |
|--------------------------------------------------------------------------------|
| FPS 58 | Ping 62ms | Packet Loss 1% | Region Best Ping | Support ID ABC123     |
| Logs: Available | Screenshot: Attached | Network Test [Run]                    |
| [Copy Support ID] [Submit Report] [Open Known Issues]                          |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Status metrics | FPS, ping, packet loss, region, version |
| Support identifiers | support ID, build, platform |
| Attachments | logs, screenshot, clip permissions |
| Actions | copy, submit, known issues |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Support ID và submit/copy | Easy to find |
| 2 | Network/performance máu | Text values |
| 3 | Attachment permission | trước submit |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Metric row | hiện tại giá trị, status label, timestamp |
| Copy action | confirmation toast |
| Submit report | privacy note và upload trạng thái |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Offline | allow copy, disable upload với reason |
| Permission denied | route to settings |
| Report sent | confirmation và ticket/support ID |
| Upload failed | retry và save local reference |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Copy | Click | A / Cross | Tap |
| Run test | Click | Focus CTA | Tap |
| Submit | Click | A / Cross | Sticky CTA |

**Designer ghi chú**

- Diagnostics nên được dễ đọc by người chơi và support staff.

**Acceptance checklist**

- [ ] Offline, permission denied, sent, và upload failed trạng thái are covered.

### hệ thống Dialogs

**người chơi Intent**

Recover from errors, maintenance, version mismatch, network issues, save conflicts, hoặc entitlement/dịch vụ conflicts với rõ choices.

**Expanded ASCII Wireframe**

```
+--------------------------------------------------------------------------------+
| SYSTEM DIALOG: VERSION MISMATCH                                                |
|--------------------------------------------------------------------------------|
| Current: 1.0.3 | Required: 1.0.4                                               |
| Update is required to play online. Offline settings remain available.          |
| [Exit] [Offline Settings] [Update]                                             |
+--------------------------------------------------------------------------------+
```

**Layout Anatomy**

| Region | yêu cầu |
| :--- | :--- |
| Title | cụ thể problem, not generic error |
| Explanation | what failed và người chơi impact |
| Choices | retry/update/offline/exit/support |
| Support | code, timestamp, status link where useful |

**Visual Hierarchy**

| Priority | Element | yêu cầu |
| :--- | :--- | :--- |
| 1 | Required action | primary CTA matches recovery path |
| 2 | Consequence | trước destructive/exit choice |
| 3 | Support code | Copyable nhưng secondary |

**Component yêu cầu**

| Component | yêu cầu |
| :--- | :--- |
| Dialog title | names network/update/maintenance/conflict/entitlement problem |
| CTA set | one primary, one safe cancel/exit, support nếu needed |
| Error code | copyable for support |

**trạng thái & Edge Cases**

| trạng thái | Behavior |
| :--- | :--- |
| Network error | retry, offline/local option nếu available |
| Version mismatch | hiện tại/required version và update |
| Maintenance | expected end/status link |
| Save conflict | source, timestamp, impact, choices |
| Entitlement/dịch vụ conflict | provider, sync status, support path; route purchase receipts to Commerce màn hình |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| primary recovery | Enter/click | A / Cross | Tap primary |
| Cancel/exit | Esc/click | B / Circle | secondary |
| Copy code | Click | Focus action | Tap |

**Designer ghi chú**

- Never cách dùng "Something went wrong" as the only message.

**Acceptance checklist**

- [ ] Network, version, maintenance, save conflict, data corruption, và entitlement/dịch vụ dialogs have recovery paths.

---

## Analytics

| Metric | cách dùng |
| :--- | :--- |
| Login failure rate by provider | Improve auth flow |
| Account conflict choices | Tune sync messaging |
| Settings search terms | Improve category naming |
| Preset apply/revert rate | Validate preset trust |
| Error retry success | Improve hệ thống recovery |
| Accessibility preset adoption | Measure discoverability |

---

## checklist Nghiệm Thu

- [ ] Account, privacy, unlink, và abandon màn hình trạng thái consequences plainly.
- [ ] First-thời gian setup offer accessibility trước gameplay.
- [ ] Settings support apply, revert, platform locks, và ranked locks.
- [ ] hệ thống errors include retry/cancel/support paths.
- [ ] Privacy và streamer mode protect names, invite codes, và account IDs.
