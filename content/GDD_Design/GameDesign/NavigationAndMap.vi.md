---
title: "Navigation & Map hệ thống Design"
type: docs
---

## Tổng Quan

Navigation hệ thống giúp người chơi understand where they are, where danger may be, where objectives are, và how to extract. They must support tactical quyết định-making mà không revealing too much information.

The navigation hệ thống should give người chơi confidence mà không giving them omniscience. It can giúp với orientation, squad coordination, route planning, và extraction commitment, nhưng it không nên erase the giá trị of sound, scouting, memory, và map knowledge.

Good navigation makes người chơi say "we chose the wrong route," not "the UI lied to us." Every marker, ping, threat hint, và extraction cue needs a rõ source và an understandable level of certainty.

## hệ thống Layers

Each layer answers a different question. The compass answers "which direction?" The minimap answers "what is nearby?" The tactical map answers "what is the plan?" World markers answer "where do I look now?" Audio answers "what changed while I was moving?"

| Layer | mục đích | Visibility |
| :--- | :--- | :--- |
| Compass ring | Directional awareness và pings | Always hiển thị rõ, compact |
| Minimap | Nearby terrain, squad, objective hints | HUD element |
| Tactical map | Full route planning | Opened by người chơi |
| World markers | In-world objective và ping direction | Contextual |
| Audio cues | Directional threat và extraction information | Always active nếu audible |

## Navigation Signal flow

Signal routing nên được conservative. A loud gunshot can tạo a directional cue, nhưng it không nên become a perfect địch marker. A squad ping can be precise vì a teammate placed it. Objective và extraction markers can be stable vì they are hệ thống-authored.

| Signal source | HUD Compass | Minimap | Tactical Map | người chơi quyết định |
| :--- | :--- | :--- | :--- | :--- |
| World observation | Directional context | Nearby route context | Full context on open | Choose route hoặc cover |
| Squad ping | Direction và distance | Marker và label | shared marker | Coordinate action |
| Objective update | Optional direction | Objective marker | Objective chi tiết | Prioritize mục tiêu |
| Extraction update | Direction nếu known | Extraction marker | Extraction chi tiết | Commit to exit route |
| Gunfire hoặc danger | Directional pulse | Optional threat hint | Not exact by default | Avoid, flank, hoặc engage |

## Compass Rules

The compass is the least disruptive navigation layer, so it should carry fast directional information trong khi combat. It must remain compact enough that Người chơi có thể read it peripherally mà không losing sight of threats.

| Signal | Display |
| :--- | :--- |
| Cardinal direction | Always shown |
| Squad ping | Direction, distance, short label |
| Gunfire | Directional pulse nếu heard |
| Extraction | Direction only sau discovered hoặc assigned |
| Danger zone | cảnh báo wedge, not exact người chơi reveal |

## Minimap Rules

| Element | Rule |
| :--- | :--- |
| người chơi | Centered hoặc offset by movement direction |
| Squad | Always hiển thị rõ nếu connected |
| địch | Never permanently hiển thị rõ by default |
| AI | hiển thị rõ only thông qua scan, noise, hoặc objective rules |
| Loot | Not globally shown; markers only sau discovery |
| Extraction | Shows assigned và discovered extracts |

## Tactical Map

The tactical map is a planning tool, not a pause button. Opening it nên được risky in unsafe areas, so the information phải được valuable enough to justify the moment of attention. On mobile, pan và zoom need generous hit targets và predictable gestures.

| tính năng | yêu cầu |
| :--- | :--- |
| Pan và zoom | Touch và controller friendly |
| Floor support | rõ floor selector for multi-level spaces |
| Objectives | Filterable quest, squad, và extraction markers |
| Route planning | người chơi can place personal waypoint |
| Risk info | Zone danger tiers và event areas shown nếu known |

## Ping hệ thống

Pings replace voice dependency. They should let squads communicate danger, intent, loot, extraction, và movement mà không requiring open microphone cách dùng. Priority rules should prevent spam from burying urgent danger calls.

| Ping | Input | kết quả |
| :--- | :--- | :--- |
| Context ping | Tap / quick press | Marks object, location, địch, loot, hoặc route |
| Ping wheel | Hold | Lets người chơi choose intent |
| Danger ping | địch hoặc suspicious area | Higher priority visual và audio |
| Objective ping | Quest hoặc extraction | shared với squad |
| Cancel ping | Re-tap hoặc menu action | Removes marker |

## Navigation Examples

A squad hears gunfire to the north. The compass can pulse direction và intensity, nhưng the minimap không nên place an exact địch marker unless another hệ thống explicitly revealed it.

A người chơi discovers an extraction point. The minimap và tactical map can now show that extract, while the compass can provide direction khi the người chơi is close enough hoặc has it selected.

A teammate pings rare loot và then changes their mind. The ping nên được cancellable, decay naturally, và remain lower priority than danger hoặc giúp pings.

## Navigation Failure Cases

- nếu người chơi follow markers blindly into danger, route risk may be under-communicated.
- nếu map opening is too safe, tactical planning loses tension.
- nếu pings overlap unreadably, priority và decay rules need tuning.
- nếu audio cues và visual cues disagree, trust in navigation breaks quickly.

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| Map rules | [Map Design](mapdesign/index.html) |
| Communication và pings | [Communication](communication/index.html) |
| Controls | [Controls](controls/index.html) |
| Accessibility alternatives | [Accessibility](accessibility/index.html) |
