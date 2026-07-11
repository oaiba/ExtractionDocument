---
title: "User Settings Matrix"
type: docs
weight: 18
---

## Overview

This matrix lists player-facing settings by category. It is intentionally table-first so design, UI, engineering, QA, and localization can audit settings without reading the UX hub.

Use this page as the canonical checklist for settings coverage, default values, platform behavior, and QA review. Player-facing explanation, category philosophy, presets, cloud sync, and competitive lock policy live in [User Settings](usersettings/index.html).

The matrix should stay concise. If an option needs a long rationale, keep the option here and place the reasoning in the hub or the owning feature page. This keeps the table useful for implementation and localization review.

## Controls

| Setting | Options | Default | Notes |
| :--- | :--- | :--- | :--- |
| Active input | Auto / Touch / Controller / Keyboard Mouse | Auto | Auto switches based on recent input |
| Look sensitivity | Slider | 50 | Per input type |
| Aim sensitivity | Slider | 45 | Separate from camera look |
| Gyro aiming | Off / On | Off | Mobile and supported controllers |
| Aim assist | Off / Low / Standard | Standard on touch | Ranked-tuned |
| Hold to aim | Hold / Toggle | Hold | Accessibility compatible |
| Interact behavior | Tap / Hold | Hold for risky actions | Prevents accidental extraction |
| Button layout | Default / Claw / Left-handed / Custom | Default | Mobile only |

## Graphics

| Setting | Options | Default | Notes |
| :--- | :--- | :--- | :--- |
| Quality preset | Low / Medium / High / Ultra | Device auto | Mobile profile driven |
| FPS target | 30 / 60 / 90 / 120 | Device auto | Competitive modes may cap |
| Resolution scale | 50-100% | Auto | Used for thermal control |
| VFX intensity | Low / Medium / High | Medium | Affects readability |
| Camera shake | 0-100% | 50% | Accessibility override allowed |
| Colorblind mode | Off / Protanopia / Deuteranopia / Tritanopia / Achromatopsia | Off | Also in Accessibility |

## Audio

| Setting | Options | Default | Notes |
| :--- | :--- | :--- | :--- |
| Master volume | 0-100% | 80% | Global |
| Effects volume | 0-100% | 85% | Gunshots, footsteps, UI |
| Voice chat volume | 0-100% | 80% | Squad and proximity |
| Music volume | 0-100% | 60% | Lower during raids |
| Dynamic range | Night / Normal / Wide | Normal | Device-friendly |
| Subtitles | Off / On | On | Accessibility requirement |

## Gameplay & HUD

| Setting | Options | Default | Notes |
| :--- | :--- | :--- | :--- |
| HUD scale | 75-150% | 100% | Mobile and PC |
| Minimap rotation | Fixed / Rotating | Rotating | Player preference |
| Loot labels | Minimal / Standard / Detailed | Standard | Detailed may clutter |
| Hit feedback | Minimal / Standard / Detailed | Standard | Competitive clarity |
| Damage numbers | Off / On | Off | If supported by mode |
| Extraction warnings | Off / On | On | Recommended always on |

## Accessibility

| Setting | Options | Default | Notes |
| :--- | :--- | :--- | :--- |
| Text size | Small / Medium / Large / XL | Medium | Applies globally |
| High contrast | Off / On | Off | Stronger UI separation |
| Reduce motion | Off / On | Off | Reduces shake and animated noise |
| Flash reduction | Off / On | On | Safety default |
| Hold alternatives | Off / On | Off | Converts rapid taps to hold |
| Navigation assist | Off / Waypoint / Full | Waypoint | Onboarding support |

## Social & Privacy

| Setting | Options | Default | Notes |
| :--- | :--- | :--- | :--- |
| Friend requests | Everyone / Friends of Friends / Closed | Everyone | User privacy |
| Party invites | Everyone / Friends Only / Closed | Friends Only | Reduces spam |
| Show presence | Detailed / Basic / Off | Basic | Controls public activity |
| Voice chat | Off / Party / Squad / All Allowed | Squad | Mode can override |
| Profanity filter | Off / On | On | Required for safety |
| Anonymous mode | Off / On | Off | Streamer support |

## Language, Region, And Diagnostics

| Setting | Options | Default | Notes |
| :--- | :--- | :--- | :--- |
| Text language | Supported languages | System | See Localization |
| Audio language | Supported languages / Match text | Match text | Optional downloads |
| Region | Auto / Region list | Auto | Matchmaking |
| Network diagnostics | Off / On | Off | Debug information |
| FPS display | Off / On | Off | Performance visibility |
| Telemetry | Essential / Anonymous / Full | Anonymous | Must follow privacy law |
