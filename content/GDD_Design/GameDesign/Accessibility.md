---
title: "Accessibility Design"
type: docs
---

## Overview

Accessibility ensures the extraction loop can be understood, configured, and played by as many players as possible without compromising competitive integrity.

Accessibility is part of the core design, not a post-launch settings dump. Extraction games rely on sound, timing, visual contrast, inventory reading, and pressure decisions; each of those can exclude players if it has only one presentation. The goal is to offer equivalent information and control, not extra hidden advantage.

Accessibility choices should be available before the first tutorial raid. A player who needs larger text, reduced flash, remapped inputs, subtitles, or simplified HUD should not have to complete a combat encounter to reach those options.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Accessibility entry point | Available from first launch and Settings |
| Defaults | Subtitles on, flash reduction on, readable text scale |
| Competitive integrity | Accessibility assists cannot reveal hidden information |
| Testing | Every major feature needs accessibility review |

## Visual Accessibility

Visual accessibility must account for combat readability and inventory readability separately. A loot rarity color that works in a menu may fail on a bright map. A danger marker that works on desktop may be too small on mobile. Every critical signal needs at least one non-color reinforcement.

| Feature | Requirement |
| :--- | :--- |
| Colorblind modes | Protanopia, Deuteranopia, Tritanopia, Achromatopsia |
| Rarity without color | Shape, icon, text label, or pattern supports rarity color |
| Text readability | Scalable text and contrast-safe UI |
| High contrast | Stronger outlines, markers, and focus states |
| Reduced flash | Limits bright flashes and rapid strobing |
| Motion reduction | Reduces camera shake and aggressive transitions |

## Auditory Accessibility

Audio is tactical information, so the game needs careful alternatives for players who cannot rely on it fully. Visual sound indicators should communicate direction and category, but they must avoid revealing exact positions or information that hearing players would not receive.

| Feature | Requirement |
| :--- | :--- |
| Subtitles | On by default for narrative and tutorial speech |
| Directional sound indicators | Optional visual cue for gunfire, ping, and extraction sounds |
| Voice chat captions | Future-facing, dependent on platform capability |
| Audio mix presets | Night, standard, wide dynamic range |

## Motor Accessibility

Motor accessibility should reduce unnecessary input strain while preserving risk. Hold-to-extract, repeated looting, sprint behavior, and ability casting need alternatives because they are frequent actions under pressure. Ranked restrictions should be explicit where timing assistance changes competitive assumptions.

| Feature | Requirement |
| :--- | :--- |
| Remapping | Core actions remappable where platform allows |
| Hold alternatives | Tap, hold, and toggle variants for repeated or long actions |
| Aim assist | Configurable for touch/controller, bounded by fairness rules |
| Touch layout presets | Default, left-handed, claw, simplified |
| Timing windows | Tutorial and non-ranked content can offer forgiving timing |

## Cognitive Accessibility

Cognitive accessibility is especially important because extraction games can overwhelm players with simultaneous goals. Objective hierarchy, death recap clarity, pinned goals, and simplified HUD modes help players decide what matters now.

| Feature | Requirement |
| :--- | :--- |
| Tutorial guidance | Teach one concept at a time |
| Objective clarity | Current objective and extraction state are always recoverable |
| Death recap | Explain cause of death and next learning opportunity |
| Simplified HUD | Reduce optional widgets and visual noise |
| Memory aids | Quest reminders, pinned goals, route markers |

## Accessibility Checklist

The checklist should be used during feature review, not only QA. A system is not ready if it depends on color alone, hides critical text at small sizes, requires repeated rapid inputs, or gives no recovery path after confusion.

| Check | Required For |
| :--- | :--- |
| Text remains readable at mobile size | All UI |
| Core signals have non-color alternatives | Loot, danger, rarity, squad |
| Actions have remap or alternative input | Controls, UI, minigames |
| Motion and flash can be reduced | Camera, VFX, transitions |
| Tutorial explains settings where relevant | FTUE and settings |

## Accessibility Examples

A player with color vision deficiency should still distinguish loot rarity through icon shape, text label, or pattern. Color can reinforce the signal, but it cannot be the only channel.

A player who cannot hold buttons comfortably should be able to change sprint, aim, interact, and extraction behavior where fairness allows. For risky actions, the alternative can still require confirmation.

A player who is sensitive to motion should be able to reduce camera shake, flash intensity, and aggressive menu transitions before the tutorial begins.

## Review Notes

- Accessibility options should be tested on mobile-size UI, not only desktop.
- Ranked restrictions must be reviewed case by case rather than disabling broad accessibility categories.
- Tutorial prompts should mention relevant settings when a player struggles repeatedly.
- Subtitles and critical warnings should survive loud combat and small screens.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Settings options | [User Settings](usersettings.html), [Settings Matrix](usersettings_matrix.html) |
| Controls | [Controls](controls.html) |
| Navigation signals | [Navigation & Map](navigationandmap.html) |
| Tutorial | [Tutorial Raid](tutorialraid.html) |
