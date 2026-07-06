---
title: "Control System - Design & Experience"
type: docs
---

## Overview

Controls define how the tactical fantasy feels in the player's hands. The game is mobile-first, but must support touch, controller, keyboard, and mouse without compromising competitive readability.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Primary platform | Mobile touch |
| Secondary inputs | Controller, keyboard, mouse |
| Combat feel | Responsive, readable, tactical |
| Camera | Top-down tactical view with limited zoom and clear silhouettes |
| Aim assistance | Allowed for touch and controller, tuned for fairness |
| Remapping | Supported for all non-critical actions |

## Input Switching

| Current Input | Trigger | New Input | UI Update |
| :--- | :--- | :--- | :--- |
| Touch | Controller input detected | Controller | Button prompts switch to controller glyphs |
| Touch | Keyboard or mouse input detected | Keyboard/Mouse | Prompts switch to keyboard and mouse labels |
| Controller | Touch input detected | Touch | Mobile touch controls become primary |
| Controller | Keyboard or mouse input detected | Keyboard/Mouse | Prompts switch to keyboard and mouse labels |
| Keyboard/Mouse | Touch input detected | Touch | Mobile touch controls become primary |
| Keyboard/Mouse | Controller input detected | Controller | Button prompts switch to controller glyphs |

Input hints, button prompts, and tutorial callouts must update within one second of the active input changing.

## Mobile Touch Layout

| Zone | Primary Actions | Design Rule |
| :--- | :--- | :--- |
| Left thumb | Move, sprint modifier, crouch shortcut | Never block critical threat visibility |
| Right thumb | Aim, fire, interact, ability, reload | Cluster actions by urgency |
| Top left | Squad, minimap, objective summary | Read-only during combat |
| Top right | Ammo, weapon, status warnings | Compact and high contrast |
| Bottom center | Context prompts | Appear only when actionable |

## Controller Layout

| Action | Default Binding | Notes |
| :--- | :--- | :--- |
| Move | Left stick | Stick press toggles sprint only if accessibility allows |
| Aim / rotate | Right stick | Supports sensitivity curves and dead zones |
| Fire | Right trigger | Haptic feedback on shot and empty mag |
| Aim / focus | Left trigger | Optional soft lock or precision aim behavior |
| Interact | Face button | Hold for risky actions |
| Ability | Shoulder button | Must be visible in HUD prompt |
| Ping | D-pad or shoulder combo | Fast single tap plus hold wheel |

## Keyboard And Mouse

| Action | Default | Notes |
| :--- | :--- | :--- |
| Move | WASD | Fully remappable |
| Fire | Left mouse | No aim assist |
| Aim / focus | Right mouse | Optional hold/toggle |
| Interact | F | Hold for extraction, revive, and high-risk actions |
| Ping | Middle mouse | Hold opens ping wheel |
| Inventory | Tab | Opens tactical inventory |
| Map | M | Opens tactical map |

## Aim Assistance

| Assist | Touch | Controller | Keyboard/Mouse |
| :--- | :--- | :--- | :--- |
| Target friction | Yes | Yes | No |
| Snap strength | Very low | Low | No |
| Bullet magnetism | Avoid | Avoid | No |
| Accessibility assist | Optional | Optional | Optional for accessibility only |

Aim assistance must never reveal hidden targets or override player intent.

## Camera Rules

| Rule | Requirement |
| :--- | :--- |
| Tactical readability | Player, enemies, cover, loot, and extraction cues remain legible on small screens |
| Zoom | Limited pinch zoom, no competitive scouting exploit |
| Rotation | Fixed or constrained rotation per map readability needs |
| Shake | Reducible through accessibility settings |
| Occlusion | Buildings and props must fade, cut away, or outline when they hide the player |

## Settings Ownership

This page owns control feel and input behavior. The complete settings matrix belongs in [User Settings](usersettings.html) and [Settings Matrix](usersettings_matrix.html).

## Cross-References

| Topic | Page |
| :--- | :--- |
| Raid flow | [Core Gameplay](coregameplay.html) |
| HUD and map controls | [Navigation & Map](navigationandmap.html) |
| Settings UX | [User Settings](usersettings.html) |
| Accessibility options | [Accessibility](accessibility.html) |
| Tutorial prompts | [Tutorial Raid](tutorialraid.html) |
