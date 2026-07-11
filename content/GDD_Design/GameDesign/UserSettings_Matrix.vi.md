---
title: "User Settings Matrix"
type: docs
weight: 18
---

## Tổng Quan

This matrix lists người chơi-facing settings by category. It is intentionally bảng-first so design, UI, engineering, QA, và localization can audit settings mà không reading the UX hub.

cách dùng this trang as the canonical checklist for settings coverage, default values, platform behavior, và QA review. người chơi-facing explanation, category philosophy, presets, cloud sync, và competitive lock policy live in [User Settings](usersettings/index.html).

The matrix should stay concise. nếu an option needs a long rationale, keep the option here và place the reasoning in the hub hoặc the owning tính năng trang. This keeps the bảng useful for implementation và localization review.

## Điều Khiển

| Setting | Options | Default | ghi chú |
| :--- | :--- | :--- | :--- |
| Active input | Auto / Touch / Controller / Keyboard Mouse | Auto | Auto switches based on recent input |
| Look sensitivity | Slider | 50 | Per input type |
| Aim sensitivity | Slider | 45 | Separate from camera look |
| Gyro aiming | Off / On | Off | Mobile và supported controllers |
| Aim assist | Off / Low / Standard | Standard on touch | Ranked-tuned |
| Hold to aim | Hold / Toggle | Hold | Accessibility compatible |
| Interact behavior | Tap / Hold | Hold for risky actions | Prevents accidental extraction |
| Button layout | Default / Claw / Left-handed / Custom | Default | Mobile only |

## Graphics

| Setting | Options | Default | ghi chú |
| :--- | :--- | :--- | :--- |
| Quality preset | Low / Medium / High / Ultra | Device auto | Mobile profile driven |
| FPS target | 30 / 60 / 90 / 120 | Device auto | Competitive modes may cap |
| Resolution scale | 50-100% | Auto | Used for thermal control |
| VFX intensity | Low / Medium / High | Medium | Affects readability |
| Camera shake | 0-100% | 50% | Accessibility override allowed |
| Colorblind mode | Off / Protanopia / Deuteranopia / Tritanopia / Achromatopsia | Off | Also in Accessibility |

## Audio

| Setting | Options | Default | ghi chú |
| :--- | :--- | :--- | :--- |
| Master volume | 0-100% | 80% | global |
| Effects volume | 0-100% | 85% | Gunshots, footsteps, UI |
| Voice chat volume | 0-100% | 80% | Squad và proximity |
| Music volume | 0-100% | 60% | Lower trong khi raids |
| Dynamic range | Night / Normal / Wide | Normal | Device-friendly |
| Subtitles | Off / On | On | Accessibility yêu cầu |

## Gameplay & HUD

| Setting | Options | Default | ghi chú |
| :--- | :--- | :--- | :--- |
| HUD scale | 75-150% | 100% | Mobile và PC |
| Minimap rotation | Fixed / Rotating | Rotating | người chơi preference |
| Loot labels | Minimal / Standard / chi tiết | Standard | chi tiết may clutter |
| Hit feedback | Minimal / Standard / chi tiết | Standard | Competitive clarity |
| Damage thông số | Off / On | Off | nếu supported by mode |
| Extraction cảnh báo | Off / On | On | Recommended always on |

## Accessibility

| Setting | Options | Default | ghi chú |
| :--- | :--- | :--- | :--- |
| Text size | Small / Medium / Large / XL | Medium | Applies globally |
| High contrast | Off / On | Off | Stronger UI separation |
| Reduce motion | Off / On | Off | Reduces shake và animated noise |
| Flash reduction | Off / On | On | Safety default |
| Hold alternatives | Off / On | Off | Converts rapid taps to hold |
| Navigation assist | Off / Waypoint / Full | Waypoint | Onboarding support |

## Social & Privacy

| Setting | Options | Default | ghi chú |
| :--- | :--- | :--- | :--- |
| Friend requests | Everyone / Friends of Friends / Closed | Everyone | User privacy |
| Party invites | Everyone / Friends Only / Closed | Friends Only | Reduces spam |
| Show presence | chi tiết / Basic / Off | Basic | Controls public activity |
| Voice chat | Off / Party / Squad / All Allowed | Squad | Mode can override |
| Profanity filter | Off / On | On | Required for safety |
| Anonymous mode | Off / On | Off | Streamer support |

## Language, Region, và Diagnostics

| Setting | Options | Default | ghi chú |
| :--- | :--- | :--- | :--- |
| Text language | Supported languages | hệ thống | See Localization |
| Audio language | Supported languages / Match text | Match text | Optional downloads |
| Region | Auto / Region list | Auto | Matchmaking |
| Network diagnostics | Off / On | Off | Debug information |
| FPS display | Off / On | Off | Performance visibility |
| Telemetry | Essential / Anonymous / Full | Anonymous | Must follow privacy law |
