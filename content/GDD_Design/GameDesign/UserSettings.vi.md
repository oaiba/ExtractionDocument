---
title: "User Settings & Configuration"
type: docs
---

## Tổng Quan

User Settings defines how người chơi configure controls, video, audio, gameplay, accessibility, privacy, và diagnostics. This trang is the UX và policy hub. The full option list lives in [Settings matrix](usersettings_matrix.html), và technical tags live in [Settings Tags](usersettings_tags.html).

Settings should feel powerful mà không feeling hostile. Competitive người chơi need precision, creators need privacy tools, mobile người chơi need battery và touch controls, và accessibility users need support trước play begins. The trang should group choices by người chơi intent rather than expose every technical variable at the same level.

The settings trải nghiệm should also protect ranked fairness. khi a setting is locked, limited, hoặc platform-cụ thể, the UI should say why in plain language. A disabled control mà không explanation tạo distrust.

## Nguyên Tắc Thiết Kế

These principles guide both màn hình layout và data ownership. A category can contain many options in the matrix, nhưng the người chơi-facing settings màn hình should prioritize common quyết định, safe previews, search, presets, và rõ reset behavior.

| Principle | Rule |
| :--- | :--- |
| Fast to scan | Categories phải được predictable và searchable |
| Safe to change | Risky changes need confirmation hoặc preview |
| Platform-aware | Hide hoặc disable settings that do not apply |
| Competitive integrity | Ranked-locked settings phải được explained |
| Accessibility-first | Accessibility settings phải được easy to find |
| Cloud-friendly | Sync settings khi useful, keep device-cụ thể overrides local |

## Category Summary

Categories should stay stable across platforms even khi individual options differ. A mobile người chơi và PC người chơi should both know where "Controls" hoặc "Accessibility" lives, even nếu the available controls inside that category are platform-cụ thể.

| Category | Owns | chi tiết |
| :--- | :--- | :--- |
| Controls | Input device, sensitivity, remap, gyro, aim assist | [Controls](controls.html) |
| Graphics | Display, quality, post-processing, performance profile | [Settings matrix](usersettings_matrix.html) |
| Audio | Volumes, output device, voice chat, subtitles | [Communication](communication.html) |
| Gameplay & HUD | Reticle, minimap, hit feedback, loot prompts | [Navigation & Map](navigationandmap.html) |
| Accessibility | Color, motion, timing, input assist, text size | [Accessibility](accessibility.html) |
| Social & Privacy | Invites, presence, chat, matchmaking privacy | [người chơi Profile](playerprofile.html) |
| Language & Region | Text, audio, region, units, date format | [Localization](localization.html) |
| Diagnostics | FPS, network, telemetry, crash reporting | Technical hệ thống |

## Presets

Presets are starting points, not hidden bundles. Applying a preset should show what changed và allow the người chơi to undo hoặc customize. This is especially quan trọng for Accessibility Starter, Battery Saver, và Streamer presets where trust matters.

| Preset | Target người chơi | Changes |
| :--- | :--- | :--- |
| Competitive | Ranked và serious play | Lower visual noise, stronger performance display, minimal motion |
| Immersive | Narrative và atmosphere | Richer audio/visuals, reduced HUD clutter |
| Battery Saver | Mobile và laptop | Lower FPS target, reduced effects, lower brightness prompts |
| Accessibility Starter | người chơi needing quick support | Larger text, reduced motion, stronger contrast, hold alternatives |
| Streamer | Content creators | Privacy protection, hide names, reduce notification leakage |

## Cloud Sync và Conflict flow

Cloud sync should preserve comfort mà không breaking device-cụ thể tuning. Sensitivity, keybinds, và HUD layout may need separate platform profiles, while language, subtitle preference, privacy, và accessibility defaults can sync more broadly.

| Step | Condition | kết quả |
| :--- | :--- | :--- |
| 1 | người chơi signs in | Game checks for cloud settings |
| 2A | No cloud settings exist | cách dùng local settings |
| 2B | Cloud settings exist và local settings are unchanged | Apply cloud settings |
| 2C | Cloud và local settings both changed recently | Show conflict prompt |
| 3A | người chơi chooses local | Keep device settings và optionally upload |
| 3B | người chơi chooses cloud | Apply synced settings |
| 3C | người chơi chooses merge | Merge safe categories và ask for device-cụ thể choices |

## Competitive Integrity Locks

Competitive locks nên được rare, explainable, và mode-aware. A người chơi should understand whether a lock exists vì of fairness, anti-cheat, visibility parity, hoặc platform limitation. Accessibility settings nên được reviewed separately trước being restricted.

| Setting Type | Ranked Rule |
| :--- | :--- |
| Visual clarity assists | Allowed nếu accessibility-safe và non-exploitative |
| FOV / zoom | Restricted nếu it changes information advantage |
| Macros | disabled |
| Debug overlays | disabled |
| Input remap | Allowed |
| Aim assist | Platform và mode tuned |

## Settings Examples

A mobile người chơi on low battery applies Battery Saver. The settings màn hình should show reduced FPS target, lower VFX intensity, và any gameplay visibility tradeoffs trước saving.

A competitive PC người chơi applies Competitive. The preset should reduce visual noise và enable useful diagnostics, nhưng it không được hide effects that other người chơi rely on for fairness.

A streamer applies Streamer mode. The preset should hide names, invite codes, và sensitive notifications while keeping squad và match-critical information available.

## Settings Failure Cases

- nếu presets silently change too many options, người chơi lose trust.
- nếu platform-cụ thể settings sync incorrectly, HUD scale hoặc focus settings may break PC/Console comfort.
- nếu ranked locks appear mà không explanation, người chơi assume bugs hoặc unfairness.
- nếu accessibility settings are buried, some người chơi may churn trước the first raid.

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| Full option bảng | [Settings matrix](usersettings_matrix.html) |
| Technical tags | [Settings Tags](usersettings_tags.html) |
| Controls | [Controls](controls.html) |
| Accessibility | [Accessibility](accessibility.html) |
| Localization | [Localization](localization.html) |
