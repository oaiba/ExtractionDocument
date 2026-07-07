---
title: "User Settings & Configuration"
type: docs
---

## Overview

User Settings defines how players configure controls, video, audio, gameplay, accessibility, privacy, and diagnostics. This page is the UX and policy hub. The full option list lives in [Settings Matrix](usersettings_matrix.html), and technical tags live in [Settings Tags](usersettings_tags.html).

Settings should feel powerful without feeling hostile. Competitive players need precision, creators need privacy tools, mobile players need battery and touch controls, and accessibility users need support before play begins. The page should group choices by player intent rather than expose every technical variable at the same level.

The settings experience should also protect ranked fairness. When a setting is locked, limited, or platform-specific, the UI should say why in plain language. A disabled control without explanation creates distrust.

## Design Principles

These principles guide both screen layout and data ownership. A category can contain many options in the matrix, but the player-facing settings screen should prioritize common decisions, safe previews, search, presets, and clear reset behavior.

| Principle | Rule |
| :--- | :--- |
| Fast to scan | Categories must be predictable and searchable |
| Safe to change | Risky changes need confirmation or preview |
| Platform-aware | Hide or disable settings that do not apply |
| Competitive integrity | Ranked-locked settings must be explained |
| Accessibility-first | Accessibility settings must be easy to find |
| Cloud-friendly | Sync settings when useful, keep device-specific overrides local |

## Category Summary

Categories should stay stable across platforms even when individual options differ. A mobile player and PC player should both know where "Controls" or "Accessibility" lives, even if the available controls inside that category are platform-specific.

| Category | Owns | Detail |
| :--- | :--- | :--- |
| Controls | Input device, sensitivity, remap, gyro, aim assist | [Controls](controls.html) |
| Graphics | Display, quality, post-processing, performance profile | [Settings Matrix](usersettings_matrix.html) |
| Audio | Volumes, output device, voice chat, subtitles | [Communication](communication.html) |
| Gameplay & HUD | Reticle, minimap, hit feedback, loot prompts | [Navigation & Map](navigationandmap.html) |
| Accessibility | Color, motion, timing, input assist, text size | [Accessibility](accessibility.html) |
| Social & Privacy | Invites, presence, chat, matchmaking privacy | [Player Profile](playerprofile.html) |
| Language & Region | Text, audio, region, units, date format | [Localization](localization.html) |
| Diagnostics | FPS, network, telemetry, crash reporting | Technical systems |

## Presets

Presets are starting points, not hidden bundles. Applying a preset should show what changed and allow the player to undo or customize. This is especially important for Accessibility Starter, Battery Saver, and Streamer presets where trust matters.

| Preset | Target Player | Changes |
| :--- | :--- | :--- |
| Competitive | Ranked and serious play | Lower visual noise, stronger performance display, minimal motion |
| Immersive | Narrative and atmosphere | Richer audio/visuals, reduced HUD clutter |
| Battery Saver | Mobile and laptop | Lower FPS target, reduced effects, lower brightness prompts |
| Accessibility Starter | Players needing quick support | Larger text, reduced motion, stronger contrast, hold alternatives |
| Streamer | Content creators | Privacy protection, hide names, reduce notification leakage |

## Cloud Sync And Conflict Flow

Cloud sync should preserve comfort without breaking device-specific tuning. Sensitivity, keybinds, and HUD layout may need separate platform profiles, while language, subtitle preference, privacy, and accessibility defaults can sync more broadly.

| Step | Condition | Result |
| :--- | :--- | :--- |
| 1 | Player signs in | Game checks for cloud settings |
| 2A | No cloud settings exist | Use local settings |
| 2B | Cloud settings exist and local settings are unchanged | Apply cloud settings |
| 2C | Cloud and local settings both changed recently | Show conflict prompt |
| 3A | Player chooses local | Keep device settings and optionally upload |
| 3B | Player chooses cloud | Apply synced settings |
| 3C | Player chooses merge | Merge safe categories and ask for device-specific choices |

## Competitive Integrity Locks

Competitive locks should be rare, explainable, and mode-aware. A player should understand whether a lock exists because of fairness, anti-cheat, visibility parity, or platform limitation. Accessibility settings should be reviewed separately before being restricted.

| Setting Type | Ranked Rule |
| :--- | :--- |
| Visual clarity assists | Allowed if accessibility-safe and non-exploitative |
| FOV / zoom | Restricted if it changes information advantage |
| Macros | Disabled |
| Debug overlays | Disabled |
| Input remap | Allowed |
| Aim assist | Platform and mode tuned |

## Settings Examples

A mobile player on low battery applies Battery Saver. The settings screen should show reduced FPS target, lower VFX intensity, and any gameplay visibility tradeoffs before saving.

A competitive PC player applies Competitive. The preset should reduce visual noise and enable useful diagnostics, but it must not hide effects that other players rely on for fairness.

A streamer applies Streamer mode. The preset should hide names, invite codes, and sensitive notifications while keeping squad and match-critical information available.

## Settings Failure Cases

- If presets silently change too many options, players lose trust.
- If platform-specific settings sync incorrectly, HUD scale or focus settings may break PC/Console comfort.
- If ranked locks appear without explanation, players assume bugs or unfairness.
- If accessibility settings are buried, some players may churn before the first raid.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Full option table | [Settings Matrix](usersettings_matrix.html) |
| Technical tags | [Settings Tags](usersettings_tags.html) |
| Controls | [Controls](controls.html) |
| Accessibility | [Accessibility](accessibility.html) |
| Localization | [Localization](localization.html) |
