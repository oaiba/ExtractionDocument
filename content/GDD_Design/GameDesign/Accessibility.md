---
title: "Accessibility Design"
type: docs
---

## Overview

Accessibility ensures the extraction loop can be understood, configured, and played by as many players as possible without compromising competitive integrity.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Accessibility entry point | Available from first launch and Settings |
| Defaults | Subtitles on, flash reduction on, readable text scale |
| Competitive integrity | Accessibility assists cannot reveal hidden information |
| Testing | Every major feature needs accessibility review |

## Visual Accessibility

| Feature | Requirement |
| :--- | :--- |
| Colorblind modes | Protanopia, Deuteranopia, Tritanopia, Achromatopsia |
| Rarity without color | Shape, icon, text label, or pattern supports rarity color |
| Text readability | Scalable text and contrast-safe UI |
| High contrast | Stronger outlines, markers, and focus states |
| Reduced flash | Limits bright flashes and rapid strobing |
| Motion reduction | Reduces camera shake and aggressive transitions |

## Auditory Accessibility

| Feature | Requirement |
| :--- | :--- |
| Subtitles | On by default for narrative and tutorial speech |
| Directional sound indicators | Optional visual cue for gunfire, ping, and extraction sounds |
| Voice chat captions | Future-facing, dependent on platform capability |
| Audio mix presets | Night, standard, wide dynamic range |

## Motor Accessibility

| Feature | Requirement |
| :--- | :--- |
| Remapping | Core actions remappable where platform allows |
| Hold alternatives | Tap, hold, and toggle variants for repeated or long actions |
| Aim assist | Configurable for touch/controller, bounded by fairness rules |
| Touch layout presets | Default, left-handed, claw, simplified |
| Timing windows | Tutorial and non-ranked content can offer forgiving timing |

## Cognitive Accessibility

| Feature | Requirement |
| :--- | :--- |
| Tutorial guidance | Teach one concept at a time |
| Objective clarity | Current objective and extraction state are always recoverable |
| Death recap | Explain cause of death and next learning opportunity |
| Simplified HUD | Reduce optional widgets and visual noise |
| Memory aids | Quest reminders, pinned goals, route markers |

## Accessibility Checklist

| Check | Required For |
| :--- | :--- |
| Text remains readable at mobile size | All UI |
| Core signals have non-color alternatives | Loot, danger, rarity, squad |
| Actions have remap or alternative input | Controls, UI, minigames |
| Motion and flash can be reduced | Camera, VFX, transitions |
| Tutorial explains settings where relevant | FTUE and settings |

## Cross-References

| Topic | Page |
| :--- | :--- |
| Settings options | [User Settings](usersettings.html), [Settings Matrix](usersettings_matrix.html) |
| Controls | [Controls](controls.html) |
| Navigation signals | [Navigation & Map](navigationandmap.html) |
| Tutorial | [Tutorial Raid](tutorialraid.html) |
