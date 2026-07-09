---
title: "Settings & System Screens"
type: docs
weight: 10
---

## Purpose

Settings and system screens handle the sensitive parts of the experience: account access, platform services, configuration, privacy, diagnostics, errors, and recovery. These screens must be plain, trustworthy, and explicit.

Primary references:

| System | Source |
| :--- | :--- |
| User settings | [User Settings & Configuration](../GameDesign/UserSettings.md) |
| Settings matrix | [Settings Matrix](../GameDesign/UserSettings_Matrix.md) |
| Accessibility | [Accessibility Design](../GameDesign/Accessibility.md) |
| Loading screens | [Async Loading Screen Design](LoadingScreen_Design.md) |
| Commerce | [Commerce Screens](Commerce_Screens.md) |
| Settings technical system | [Settings System](../../GDD_Technical/Systems/SettingsSystem.md) |

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |
| [Commerce Screens](Commerce_Screens.md) | Shop, offers, currency top-up, purchase confirmation, receipts, and entitlement claim |
| [Loading Screen Design](LoadingScreen_Design.md) | Boot, splash, lobby, result, and reconnect loading rules |
| [Progression & LiveOps Screens](Progression_LiveOps_Screens.md) | Battle pass, rewards, ranked, news, and LiveOps goals |
| [Social Screens](Social_Screens.md) | Privacy, safety, report/block, and communication settings |

---

## Screen Inventory

| Screen | Goal | Primary CTA | Key States |
| :--- | :--- | :--- | :--- |
| Boot / Splash | Start app and meet platform requirements | Continue / Skip if allowed | first boot, shader prep, update required |
| Login / Account Link | Authenticate and sync identity | Sign In / Link | failed auth, conflict, offline, age gate |
| EULA / Privacy | Collect required consent | Accept | declined, updated policy, region-specific |
| First-Time Setup | Choose language, accessibility, controls, privacy | Continue | incomplete, recommended preset |
| Tutorial Gate | Route new players into basics | Start Tutorial | skipped, required, returning player |
| Settings | Configure controls, graphics, audio, gameplay, accessibility | Apply | unsaved changes, platform lock, ranked lock |
| Account / Privacy | Manage identity, cross-play, streamer mode, data | Save | unlink warning, privacy conflict |
| Diagnostics | Show FPS, network, logs, support info | Copy / Submit | offline, report sent, permission denied |
| System Dialogs | Handle errors, maintenance, version mismatch, reconnect | Retry / Update / Exit | non-recoverable, queued maintenance |

---

## Boot, Splash, And Loading

Boot and splash screens should stay minimal. Loading taxonomy lives in [Loading Screen Design](LoadingScreen_Design.md); this section owns the system-facing states.

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

| State | Requirement |
| :--- | :--- |
| First boot | Show logo, progress, and what is being prepared if longer than expected |
| Shader/cache prep | Name the process and avoid fake progress |
| Update required | Show current/required version and platform update path |
| Maintenance | Show start/end time if known and support/status link |
| Offline start | Explain which local screens are available |
| Splash skip | Allowed only after minimum brand/legal display duration |

---

## Login And Account Link

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

| Spec | Requirement |
| :--- | :--- |
| Goal | Get the player into the correct account with clear consequences for linking/sync |
| Entry points | App start, account settings, cross-progression prompt |
| Primary CTA | Sign In / Link Account |
| Secondary actions | Continue offline if supported, switch account, support |
| Destructive actions | Unlink account requires explicit consequence confirmation |

### Account States

| State | Behavior |
| :--- | :--- |
| No account | Show sign-in providers and privacy note |
| Auth failed | Show provider, retry, and support |
| Account conflict | Compare account names, timestamps, and progression summaries |
| Cloud sync conflict | Use local/cloud/merge choices from [User Settings](../GameDesign/UserSettings.md) |
| Age gate | Region-appropriate messaging and blocked feature explanation |

---

## First-Time Setup

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

| Step | Requirement |
| :--- | :--- |
| Language | Text/audio/subtitle choices and region defaults |
| Accessibility starter | Offer text size, colorblind, motion, subtitle, hold alternatives |
| Controls | Detect input and offer preset |
| Privacy | Cross-play, presence, chat/voice, streamer-safe defaults |
| Tutorial | Explain tutorial value and whether it can be skipped |

First-time setup must be short. Advanced settings should be reachable but not forced before first play.

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

Settings categories follow [User Settings](../GameDesign/UserSettings.md) and the detailed [Settings Matrix](../GameDesign/UserSettings_Matrix.md).

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

| Category | UI Requirements |
| :--- | :--- |
| Controls | Remap, sensitivity, aim assist, gyro, and PC/Console HUD layout |
| Graphics | Presets, resolution/performance, preview and revert timer for risky changes |
| Audio | Volumes, output, voice, subtitles, dynamic range |
| Gameplay & HUD | Reticle, minimap, prompts, damage feedback, HUD scale |
| Accessibility | Color, text, motion, timing, input assist |
| Social & Privacy | Invites, presence, chat, cross-play, streamer mode |
| Language & Region | Text, audio, units, server region |
| Diagnostics | FPS, ping, telemetry, crash reporting |

### Settings States

| State | Behavior |
| :--- | :--- |
| Unsaved changes | Apply / Revert / Cancel visible |
| Risky display change | Revert countdown |
| Ranked lock | Disabled with fairness explanation |
| Platform unavailable | Hidden if irrelevant; disabled with reason if player expects it |
| Cloud conflict | Show local/cloud/merge choices |
| Preset applied | Show changed settings and undo |

---

## Account, Privacy, And Safety

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

| Screen | Requirement |
| :--- | :--- |
| Account | Linked providers, player ID, region, support IDs |
| Privacy | Presence, profile visibility, invite rules, cross-play |
| Streamer Mode | Hide names, invite codes, account IDs, sensitive notifications |
| Data | Telemetry consent, privacy policy, data request path |
| Block List | View and unblock with confirmation |

Privacy changes should apply immediately when possible and show restart/session requirements otherwise.

---

## Diagnostics And Support

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

| Function | Requirement |
| :--- | :--- |
| Network info | Ping, packet loss, region, server ID when safe |
| Performance | FPS, frame time, graphics preset, device profile |
| Bug report | Category, description, screenshot/log attach, consent |
| Crash recovery | Explain crash, restore options, report path |
| Copy support ID | One-click copy with confirmation |

Diagnostics should avoid exposing sensitive tokens, IPs, or private account information in shareable screenshots.

---

## System Dialogs

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
| Network error | What failed, retry, offline/local option if available |
| Version mismatch | Current version, required version, update action |
| Maintenance | Expected end time if available, status link |
| Server full/queue | Queue position or retry timing |
| Save conflict | Source, timestamp, impact, choices |
| Data corruption | What is recoverable and support path |
| Entitlement/service conflict | Account provider, sync status, support path; purchase receipts live in [Commerce Screens](Commerce_Screens.md) |

---

## Designer-Ready Screen Specs

Settings and system surfaces must be plain, trustworthy, and explicit. Every disabled state must explain why, and every account, privacy, unlink, or abandon action must state its consequence before commit.

### Boot / Splash / Loading

**Player Intent**

Start the application, understand long waits, and know whether online play is available.

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

| Region | Requirement |
| :--- | :--- |
| Brand area | logo/title with required legal timing |
| Progress area | real operation name and truthful progress/indeterminate state |
| Status footer | version, service, offline availability |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Current operation | If wait exceeds expected time |
| 2 | Error/update state | Must override normal loading |
| 3 | Version/status | Footer-level |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Progress indicator | No fake precision; operation label required |
| Update prompt | current/required version and platform action |
| Offline option | only shown if supported and names limits |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| First boot | show setup/legal sequence |
| Shader prep | name process and avoid fake progress |
| Update required | block online with update route |
| Maintenance | show known end time/status link |
| Offline start | list available local screens |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Continue | Enter/click | A / Cross | Tap CTA |
| Retry | Click | A / Cross | Tap |
| Offline | Click option | Focus option | Tap option |

**Designer Notes**

- Loading copy should be operational, not lore-only, when wait is long.

**Acceptance Checklist**

- [ ] Update, maintenance, offline, first boot, and shader prep states are covered.

### Login / Account Link / EULA

**Player Intent**

Enter the correct account, resolve sync/linking conflicts, and understand required legal consent before online play.

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

| Region | Requirement |
| :--- | :--- |
| Auth actions | provider sign-in, link, offline |
| Consequence text | what sync/link/offline changes |
| Conflict panel | compared accounts and choice impact |
| Legal panel | required policy, region, accept/decline |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Primary sign-in/link action | Clear and trustworthy |
| 2 | Consequence/conflict | Before irreversible choice |
| 3 | Support/legal links | Persistent footer |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Provider button | provider name, network/loading/error state |
| Conflict choice | local/cloud/merge label and timestamp |
| Consent CTA | disabled until required terms acknowledged |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Auth failed | provider, retry, support |
| Account conflict | compare names/timestamps/progression |
| Cloud sync conflict | local/cloud/merge choices |
| Age gate | region-appropriate blocked feature explanation |
| Declined terms | explain online access consequence |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Sign in | Click | A / Cross | Tap |
| Review legal | Link/click | Focus link | Tap link |
| Choose conflict | Radio/click | D-pad + A | Tap option |

**Designer Notes**

- Do not compress account conflict copy; trust is more important than speed here.

**Acceptance Checklist**

- [ ] Auth failure, account conflict, sync conflict, age gate, and declined terms are covered.

### First-Time Setup / Tutorial Gate

**Player Intent**

Choose language, accessibility, controls, privacy, and tutorial path before entering the game loop.

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

| Region | Requirement |
| :--- | :--- |
| Stepper | current step and remaining setup |
| Main choice | language/accessibility/control/privacy/tutorial |
| Preview | shows impact before commit |
| CTA row | back, preview, continue |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Current step action | Clear and simple |
| 2 | Accessibility choices | Offered before gameplay |
| 3 | Tutorial recommendation | Clear but not coercive unless required |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Accessibility preset | labels affected settings |
| Privacy preset | public/friends/private/streamer mode explanation |
| Tutorial gate | start/skip/required states |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Incomplete | Continue disabled with missing field |
| Recommended preset | explain why recommended |
| Tutorial required | start CTA only |
| Returning player | skip to home with edit settings route |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Choose option | Click | D-pad + A | Tap |
| Preview | Click | Y / Triangle | Preview button |
| Continue | Enter/click | A / Cross | Sticky CTA |

**Designer Notes**

- Accessibility is part of onboarding, not buried in settings.

**Acceptance Checklist**

- [ ] Language, accessibility, control, privacy, and tutorial states are covered.

### Settings

**Player Intent**

Find a setting, understand its effect, apply/revert safely, and know when platform/ranked locks prevent changes.

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

| Region | Requirement |
| :--- | :--- |
| Settings top tabs | horizontal category navigation inside Settings: Controls, Graphics, Audio, Gameplay/HUD, Accessibility, Account, Privacy, Language, Diagnostics |
| Setting list | label, control, current value, lock state |
| Help panel | selected setting explanation |
| Apply bar | unsaved, revert, apply, reset |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Unsaved/apply state | Persistent |
| 2 | Selected setting and help | Clear relationship |
| 3 | Locks/warnings | Visible before attempted change |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Setting row | label, control, value, platform/ranked lock |
| Search result | category path and setting name |
| Apply bar | changed count, apply/revert/reset |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Unsaved changes | Apply/revert visible |
| Platform lock | disabled with reason |
| Ranked lock | disabled with mode reason |
| Invalid value | error and revert |
| Requires restart | flag before apply |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Search | Ctrl-F | Y / Triangle | Search field |
| Adjust value | Mouse/keys | D-pad/sticks | Slider/stepper |
| Apply | Click | A / Cross | Sticky CTA |

**Designer Notes**

- Help copy should describe player-facing effect, not engine terms.

**Acceptance Checklist**

- [ ] Unsaved, revert, platform lock, ranked lock, invalid, and restart states are covered.

### Account / Privacy / Safety

**Player Intent**

Manage identity, cross-play, streamer mode, data/privacy, account links, and safety preferences with clear consequences.

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

| Region | Requirement |
| :--- | :--- |
| Privacy controls | visibility, streamer, invite code, online status |
| Account links | providers, link/unlink state |
| Data controls | export/delete/support |
| Safety | blocked users, muted users, communication filters |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Privacy visibility | Clear current state |
| 2 | Unlink/delete consequences | Before CTA |
| 3 | Safety lists | Manageable and reversible |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Privacy dropdown | explains visible fields |
| Streamer toggle | names hidden fields |
| Unlink CTA | consequence modal required |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Privacy conflict | show setting precedence |
| Streamer on | preview replaced fields |
| Unlink warning | name lost sync/purchase implications |
| Delete request | cooldown/confirmation/support path |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Toggle | Click | A / Cross | Tap |
| Manage list | Click row | Focus row | Tap row |
| Dangerous action | Hold/confirm | Hold confirm | Confirm sheet |

**Designer Notes**

- Dangerous account actions need calm, specific copy.

**Acceptance Checklist**

- [ ] Privacy, streamer, unlink, delete, block/mute management states are covered.

### Diagnostics And Support

**Player Intent**

See performance/network status, copy support information, submit logs, and understand permission/network failures.

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

| Region | Requirement |
| :--- | :--- |
| Status metrics | FPS, ping, packet loss, region, version |
| Support identifiers | support ID, build, platform |
| Attachments | logs, screenshot, clip permissions |
| Actions | copy, submit, known issues |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Support ID and submit/copy | Easy to find |
| 2 | Network/performance health | Text values |
| 3 | Attachment permission | Before submit |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Metric row | current value, status label, timestamp |
| Copy action | confirmation toast |
| Submit report | privacy note and upload state |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Offline | allow copy, disable upload with reason |
| Permission denied | route to settings |
| Report sent | confirmation and ticket/support ID |
| Upload failed | retry and save local reference |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Copy | Click | A / Cross | Tap |
| Run test | Click | Focus CTA | Tap |
| Submit | Click | A / Cross | Sticky CTA |

**Designer Notes**

- Diagnostics should be readable by players and support staff.

**Acceptance Checklist**

- [ ] Offline, permission denied, sent, and upload failed states are covered.

### System Dialogs

**Player Intent**

Recover from errors, maintenance, version mismatch, network issues, save conflicts, or entitlement/service conflicts with clear choices.

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

| Region | Requirement |
| :--- | :--- |
| Title | specific problem, not generic error |
| Explanation | what failed and player impact |
| Choices | retry/update/offline/exit/support |
| Support | code, timestamp, status link where useful |

**Visual Hierarchy**

| Priority | Element | Requirement |
| :--- | :--- | :--- |
| 1 | Required action | Primary CTA matches recovery path |
| 2 | Consequence | Before destructive/exit choice |
| 3 | Support code | Copyable but secondary |

**Component Requirements**

| Component | Requirement |
| :--- | :--- |
| Dialog title | names network/update/maintenance/conflict/entitlement problem |
| CTA set | one primary, one safe cancel/exit, support if needed |
| Error code | copyable for support |

**States & Edge Cases**

| State | Behavior |
| :--- | :--- |
| Network error | retry, offline/local option if available |
| Version mismatch | current/required version and update |
| Maintenance | expected end/status link |
| Save conflict | source, timestamp, impact, choices |
| Entitlement/service conflict | provider, sync status, support path; route purchase receipts to Commerce Screens |

**Input / Focus / Touch**

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Primary recovery | Enter/click | A / Cross | Tap primary |
| Cancel/exit | Esc/click | B / Circle | Secondary |
| Copy code | Click | Focus action | Tap |

**Designer Notes**

- Never use "Something went wrong" as the only message.

**Acceptance Checklist**

- [ ] Network, version, maintenance, save conflict, data corruption, and entitlement/service dialogs have recovery paths.

---

## Analytics

| Metric | Use |
| :--- | :--- |
| Login failure rate by provider | Improve auth flow |
| Account conflict choices | Tune sync messaging |
| Settings search terms | Improve category naming |
| Preset apply/revert rate | Validate preset trust |
| Error retry success | Improve system recovery |
| Accessibility preset adoption | Measure discoverability |

---

## Acceptance Checklist

- [ ] Account, privacy, unlink, and abandon screens state consequences plainly.
- [ ] First-time setup offers accessibility before gameplay.
- [ ] Settings support apply, revert, platform locks, and ranked locks.
- [ ] System errors include retry/cancel/support paths.
- [ ] Privacy and streamer mode protect names, invite codes, and account IDs.
