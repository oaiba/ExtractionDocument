---
title: "Navigation & Map System Design"
type: docs
---

## Overview

Navigation systems help players understand where they are, where danger may be, where objectives are, and how to extract. They must support tactical decision-making without revealing too much information.

The navigation system should give players confidence without giving them omniscience. It can help with orientation, squad coordination, route planning, and extraction commitment, but it should not erase the value of sound, scouting, memory, and map knowledge.

Good navigation makes players say "we chose the wrong route," not "the UI lied to us." Every marker, ping, threat hint, and extraction cue needs a clear source and an understandable level of certainty.

## System Layers

Each layer answers a different question. The compass answers "which direction?" The minimap answers "what is nearby?" The tactical map answers "what is the plan?" World markers answer "where do I look now?" Audio answers "what changed while I was moving?"

| Layer | Purpose | Visibility |
| :--- | :--- | :--- |
| Compass ring | Directional awareness and pings | Always visible, compact |
| Minimap | Nearby terrain, squad, objective hints | HUD element |
| Tactical map | Full route planning | Opened by player |
| World markers | In-world objective and ping direction | Contextual |
| Audio cues | Directional threat and extraction information | Always active if audible |

## Navigation Signal Flow

Signal routing should be conservative. A loud gunshot can create a directional cue, but it should not become a perfect enemy marker. A squad ping can be precise because a teammate placed it. Objective and extraction markers can be stable because they are system-authored.

| Signal Source | HUD Compass | Minimap | Tactical Map | Player Decision |
| :--- | :--- | :--- | :--- | :--- |
| World observation | Directional context | Nearby route context | Full context on open | Choose route or cover |
| Squad ping | Direction and distance | Marker and label | Shared marker | Coordinate action |
| Objective update | Optional direction | Objective marker | Objective details | Prioritize goal |
| Extraction update | Direction if known | Extraction marker | Extraction details | Commit to exit route |
| Gunfire or danger | Directional pulse | Optional threat hint | Not exact by default | Avoid, flank, or engage |

## Compass Rules

The compass is the least disruptive navigation layer, so it should carry fast directional information during combat. It must remain compact enough that players can read it peripherally without losing sight of threats.

| Signal | Display |
| :--- | :--- |
| Cardinal direction | Always shown |
| Squad ping | Direction, distance, short label |
| Gunfire | Directional pulse if heard |
| Extraction | Direction only after discovered or assigned |
| Danger zone | Warning wedge, not exact player reveal |

## Minimap Rules

| Element | Rule |
| :--- | :--- |
| Player | Centered or offset by movement direction |
| Squad | Always visible if connected |
| Enemies | Never permanently visible by default |
| AI | Visible only through scan, noise, or objective rules |
| Loot | Not globally shown; markers only after discovery |
| Extraction | Shows assigned and discovered extracts |

## Tactical Map

The tactical map is a planning tool, not a pause button. Opening it should be risky in unsafe areas, so the information must be valuable enough to justify the moment of attention. On mobile, pan and zoom need generous hit targets and predictable gestures.

| Feature | Requirement |
| :--- | :--- |
| Pan and zoom | Touch and controller friendly |
| Floor support | Clear floor selector for multi-level spaces |
| Objectives | Filterable quest, squad, and extraction markers |
| Route planning | Player can place personal waypoint |
| Risk info | Zone danger tiers and event areas shown if known |

## Ping System

Pings replace voice dependency. They should let squads communicate danger, intent, loot, extraction, and movement without requiring open microphone use. Priority rules should prevent spam from burying urgent danger calls.

| Ping | Input | Result |
| :--- | :--- | :--- |
| Context ping | Tap / quick press | Marks object, location, enemy, loot, or route |
| Ping wheel | Hold | Lets player choose intent |
| Danger ping | Enemy or suspicious area | Higher priority visual and audio |
| Objective ping | Quest or extraction | Shared with squad |
| Cancel ping | Re-tap or menu action | Removes marker |

## Navigation Examples

A squad hears gunfire to the north. The compass can pulse direction and intensity, but the minimap should not place an exact enemy marker unless another system explicitly revealed it.

A player discovers an extraction point. The minimap and tactical map can now show that extract, while the compass can provide direction when the player is close enough or has it selected.

A teammate pings rare loot and then changes their mind. The ping should be cancellable, decay naturally, and remain lower priority than danger or help pings.

## Navigation Failure Cases

- If players follow markers blindly into danger, route risk may be under-communicated.
- If map opening is too safe, tactical planning loses tension.
- If pings overlap unreadably, priority and decay rules need tuning.
- If audio cues and visual cues disagree, trust in navigation breaks quickly.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Map rules | [Map Design](mapdesign/index.html) |
| Communication and pings | [Communication](communication/index.html) |
| Controls | [Controls](controls/index.html) |
| Accessibility alternatives | [Accessibility](accessibility/index.html) |
