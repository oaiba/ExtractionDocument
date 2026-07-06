---
title: "Commerce, Settings & System Screens"
type: docs
weight: 9
---

## Purpose

Commerce, settings, and system screens handle the sensitive parts of the experience: account access, platform services, purchases, configuration, privacy, diagnostics, errors, and recovery. These screens must be plain, trustworthy, and explicit.

Primary references:

| System | Source |
| :--- | :--- |
| User settings | [User Settings & Configuration](../GameDesign/UserSettings.md) |
| Settings matrix | [Settings Matrix](../GameDesign/UserSettings_Matrix.md) |
| Accessibility | [Accessibility Design](../GameDesign/Accessibility.md) |
| Economy | [Economy & Monetization Design](../GameDesign/Economy.md) |
| Loading screens | [Async Loading Screen Design](LoadingScreen_Design.md) |
| Settings technical system | [Settings System](../../GDD_Technical/Systems/SettingsSystem.md) |

---

## Screen Inventory

| Screen | Goal | Primary CTA | Key States |
| :--- | :--- | :--- | :--- |
| Boot / Splash | Start app and meet platform requirements | Continue / Skip if allowed | first boot, shader prep, update required |
| Login / Account Link | Authenticate and sync identity | Sign In / Link | failed auth, conflict, offline, age gate |
| EULA / Privacy | Collect required consent | Accept | declined, updated policy, region-specific |
| First-Time Setup | Choose language, accessibility, controls, privacy | Continue | incomplete, recommended preset |
| Tutorial Gate | Route new players into basics | Start Tutorial | skipped, required, returning player |
| Shop | Browse cosmetic/non-power offers | Purchase / Preview | unavailable, owned, discounted, platform restricted |
| Wallet / Currency | Explain balances and transactions | Buy / View History | pending, failed, refunded |
| Settings | Configure controls, graphics, audio, gameplay, accessibility | Apply | unsaved changes, platform lock, ranked lock |
| Account / Privacy | Manage identity, cross-play, streamer mode, data | Save | unlink warning, privacy conflict |
| Diagnostics | Show FPS, network, logs, support info | Copy / Submit | offline, report sent, permission denied |
| System Dialogs | Handle errors, maintenance, version mismatch, reconnect | Retry / Update / Exit | non-recoverable, queued maintenance |

---

## Boot, Splash, And Loading

Boot and splash screens should stay minimal. Loading taxonomy lives in [Loading Screen Design](LoadingScreen_Design.md); this section owns the system-facing states.

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

| Step | Requirement |
| :--- | :--- |
| Language | Text/audio/subtitle choices and region defaults |
| Accessibility starter | Offer text size, colorblind, motion, subtitle, hold alternatives |
| Controls | Detect input and offer preset |
| Privacy | Cross-play, presence, chat/voice, streamer-safe defaults |
| Tutorial | Explain tutorial value and whether it can be skipped |

First-time setup must be short. Advanced settings should be reachable but not forced before first play.

---

## Shop And Wallet

| Spec | Requirement |
| :--- | :--- |
| Goal | Let players preview and purchase cosmetic/value-safe items with trust |
| Layout | Offer grid, selected preview, ownership, currency, legal/platform info |
| Primary CTA | Purchase or Equip if owned |
| Secondary actions | Preview, wishlist/favorite, gift if supported, view bundle contents |
| Monetization rule | No gameplay advantage hidden in premium offers |

### Purchase States

| State | Behavior |
| :--- | :--- |
| Owned | CTA becomes Equip/View |
| Insufficient currency | Show top-up path and exact missing amount |
| Platform restricted | Explain platform policy or region lock |
| Pending transaction | Disable repeat purchase and show spinner/status |
| Failed transaction | Show reason, retry, and support link |
| Refund/chargeback issue | Plain account state and support path |

---

## Settings

Settings categories follow [User Settings](../GameDesign/UserSettings.md) and the detailed [Settings Matrix](../GameDesign/UserSettings_Matrix.md).

| Category | UI Requirements |
| :--- | :--- |
| Controls | Remap, sensitivity, aim assist, gyro, mobile HUD layout |
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

| Dialog | Required Content |
| :--- | :--- |
| Network error | What failed, retry, offline/local option if available |
| Version mismatch | Current version, required version, update action |
| Maintenance | Expected end time if available, status link |
| Server full/queue | Queue position or retry timing |
| Save conflict | Source, timestamp, impact, choices |
| Data corruption | What is recoverable and support path |
| Transaction error | Provider, status, receipt/support path |

---

## Analytics

| Metric | Use |
| :--- | :--- |
| Login failure rate by provider | Improve auth flow |
| Account conflict choices | Tune sync messaging |
| Settings search terms | Improve category naming |
| Preset apply/revert rate | Validate preset trust |
| Purchase failure and cancellation | Improve shop clarity |
| Error retry success | Improve system recovery |
| Accessibility preset adoption | Measure discoverability |

---

## Acceptance Checklist

- [ ] Account and purchase screens state consequences plainly.
- [ ] First-time setup offers accessibility before gameplay.
- [ ] Settings support apply, revert, platform locks, and ranked locks.
- [ ] System errors include retry/cancel/support paths.
- [ ] Shop distinguishes owned, premium, cosmetic, and unavailable items.
- [ ] Privacy and streamer mode protect names, invite codes, and account IDs.
