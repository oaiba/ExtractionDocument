---
title: "Control System - Design & Experience"
type: docs
---

## Overview

Controls define how the tactical fantasy feels in the player's hands. The game is mobile-first, but must support touch, controller, keyboard, and mouse without compromising competitive readability.

The control system should make the player feel responsible for tactical decisions, not for fighting the interface. Movement, aiming, looting, pinging, and extraction prompts must be fast enough for combat but deliberate enough that high-risk actions are not triggered by accident. The design target is "confident under pressure": a player should know what their next input will do even when the screen is busy.

Mobile touch is the baseline constraint. If a rule cannot be made readable and reliable on touch, it should not become a core combat requirement on other platforms. Keyboard, mouse, and controller can add precision and comfort, but they should not expose hidden advantages such as extra information, faster interaction chains, or easier recoil bypass.

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

Input switching is treated as a comfort feature, not a competitive exploit. The game may change button prompts and UI affordances when a new device is used, but combat rules must remain stable. Switching from controller to mouse should not reset recoil, cancel animations, bypass hold confirmations, or reveal extra UI layers.

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

Touch layout must protect the center of the screen for threat reading. Buttons should live where thumbs already rest, but the most dangerous actions need spacing and confirmation rules. For example, firing and interacting can be close, but extraction, discard, purchase, and squad-leave actions require hold or confirm behavior.

| Zone | Primary Actions | Design Rule |
| :--- | :--- | :--- |
| Left thumb | Move, sprint modifier, crouch shortcut | Never block critical threat visibility |
| Right thumb | Aim, fire, interact, ability, reload | Cluster actions by urgency |
| Top left | Squad, minimap, objective summary | Read-only during combat |
| Top right | Ammo, weapon, status warnings | Compact and high contrast |
| Bottom center | Context prompts | Appear only when actionable |

## Controller Layout

Controller play should feel deliberate and physical. Haptics can communicate empty magazines, armor break, suppression, and extraction confirmation, but vibration must remain configurable. Any aim assist tuning should be tested against touch and keyboard/mouse separately so that one device does not become the default competitive answer.

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

Keyboard and mouse should prioritize clarity and remapping depth. PC players expect fast inventory access, alternate binds, push-to-talk, and separate hold/toggle behavior. The system should support those expectations without introducing mode-only actions that cannot be represented on other devices.

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

Aim assistance exists to compensate for input friction, not to make decisions for the player. It should help players stay on a target they already found, while avoiding target discovery, automatic target transfer, or shots that feel corrected after the fact. Accessibility aim assistance can be stronger, but ranked rules must communicate how it is handled.

| Assist | Touch | Controller | Keyboard/Mouse |
| :--- | :--- | :--- | :--- |
| Target friction | Yes | Yes | No |
| Snap strength | Very low | Low | No |
| Bullet magnetism | Avoid | Avoid | No |
| Accessibility assist | Optional | Optional | Optional for accessibility only |

Aim assistance must never reveal hidden targets or override player intent.

## Camera Rules

The camera is part of the control scheme. Zoom level, occlusion fade, rotation speed, and screen shake all affect whether players can read danger. Camera changes should be smooth in menus and decisive in combat, with reduced-motion options available from the first session.

| Rule | Requirement |
| :--- | :--- |
| Tactical readability | Player, enemies, cover, loot, and extraction cues remain legible on small screens |
| Zoom | Limited pinch zoom, no competitive scouting exploit |
| Rotation | Fixed or constrained rotation per map readability needs |
| Shake | Reducible through accessibility settings |
| Occlusion | Buildings and props must fade, cut away, or outline when they hide the player |

## Platform Experience Notes

Touch players need generous hit targets, reliable gesture separation, and strong contextual prompts. The design should avoid placing high-frequency combat buttons where the player naturally swipes the camera. Accidental taps are especially costly in extraction because one wrong interaction can reveal position or waste resources.

Controller players need predictable acceleration, deadzone tuning, and haptic feedback that supports decision-making. Empty magazine pulses, low-health warnings, and extraction confirmation feedback can reduce UI scanning during pressure.

Keyboard and mouse players need precision, remapping, and quick access to inventory, map, and ping tools. These inputs can support more shortcuts, but the core combat information should remain equivalent across all platforms.

## Failure Cases

- If input switching changes prompts during combat, it must not steal focus or block firing.
- If a player remaps a critical action, conflicts must be detected before saving.
- If touch buttons overlap on small devices, the layout should offer simplified presets.
- If aim assist loses target, it should fade out smoothly rather than snapping away.
- If camera occlusion hides a threat, outline or cutaway rules should take priority over visual fidelity.

## Control Tuning Knobs

- Touch button size controls confidence; smaller buttons increase mis-taps faster than they improve screen space.
- Aim friction controls target tracking; too much feels automated, too little makes touch combat exhausting.
- Camera rotation speed controls scouting comfort; high speed can create motion strain on small screens.
- Hold duration controls accidental actions; extraction and discard need stronger confirmation than looting.
- Haptic strength controls feedback; empty magazine and confirmation pulses should be distinct.
- Deadzone and response curve controls controller trust; defaults should fit average hardware but remain editable.

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
