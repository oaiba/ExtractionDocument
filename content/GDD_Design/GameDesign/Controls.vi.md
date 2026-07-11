---
title: "Control System - Design & Experience"
type: docs
---

## Overview

Controls định nghĩa tactical fantasy có cảm giác thế nào trong tay người chơi. Game mobile-first, nhưng phải support touch, controller, keyboard, và mouse mà không làm hỏng competitive readability.

Control system nên khiến player cảm thấy họ chịu trách nhiệm cho tactical decision, không phải đang vật lộn với interface. Movement, aiming, looting, pinging, và extraction prompt phải đủ nhanh cho combat nhưng đủ deliberate để high-risk action không bị trigger nhầm. Design target là "confident under pressure": player biết input tiếp theo sẽ làm gì ngay cả khi màn hình bận rộn.

Mobile touch là baseline constraint. Nếu một rule không thể readable và reliable trên touch, nó không nên trở thành core combat requirement trên platform khác. Keyboard, mouse, controller có thể thêm precision và comfort, nhưng không được mở hidden advantage như thêm information, interaction chain nhanh hơn, hoặc bypass recoil dễ hơn.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Primary platform | Mobile touch |
| Secondary inputs | Controller, keyboard, mouse |
| Combat feel | Responsive, readable, tactical |
| Camera | Top-down tactical view với zoom giới hạn và silhouette rõ |
| Aim assistance | Cho phép trên touch/controller, tune để fair |
| Remapping | Support cho mọi non-critical action |

## Input Switching

Input switching là comfort feature, không phải competitive exploit. Game có thể đổi button prompt và UI affordance khi device mới được dùng, nhưng combat rules phải ổn định. Chuyển từ controller sang mouse không được reset recoil, cancel animation, bypass hold confirmation, hoặc reveal thêm UI layer.

| Current Input | Trigger | New Input | UI Update |
| :--- | :--- | :--- | :--- |
| Touch | Controller input detected | Controller | Button prompt đổi sang controller glyph |
| Touch | Keyboard or mouse input detected | Keyboard/Mouse | Prompt đổi sang keyboard/mouse label |
| Controller | Touch input detected | Touch | Mobile touch controls thành primary |
| Controller | Keyboard or mouse input detected | Keyboard/Mouse | Prompt đổi sang keyboard/mouse label |
| Keyboard/Mouse | Touch input detected | Touch | Mobile touch controls thành primary |
| Keyboard/Mouse | Controller input detected | Controller | Button prompt đổi sang controller glyph |

Input hint, button prompt, và tutorial callout phải update trong vòng một giây sau khi active input đổi.

## Mobile Touch Layout

Touch layout phải bảo vệ trung tâm màn hình để đọc threat. Button nên nằm nơi ngón cái nghỉ tự nhiên, nhưng action nguy hiểm cần spacing và confirmation rule. Ví dụ, fire và interact có thể gần nhau, nhưng extraction, discard, purchase, và squad-leave cần hold hoặc confirm behavior.

| Zone | Primary Actions | Design Rule |
| :--- | :--- | :--- |
| Left thumb | Move, sprint modifier, crouch shortcut | Không bao giờ che critical threat visibility |
| Right thumb | Aim, fire, interact, ability, reload | Cluster action theo urgency |
| Top left | Squad, minimap, objective summary | Read-only trong combat |
| Top right | Ammo, weapon, status warnings | Compact và high contrast |
| Bottom center | Context prompts | Chỉ xuất hiện khi actionable |

## Controller Layout

Controller play nên có cảm giác deliberate và physical. Haptic có thể truyền đạt empty magazine, armor break, suppression, và extraction confirmation, nhưng vibration phải configurable. Aim assist tuning phải test riêng touch và keyboard/mouse để không input nào trở thành default competitive answer.

| Action | Default Binding | Notes |
| :--- | :--- | :--- |
| Move | Left stick | Stick press toggle sprint chỉ nếu accessibility cho phép |
| Aim / rotate | Right stick | Supports sensitivity curves và dead zones |
| Fire | Right trigger | Haptic feedback khi shot và empty mag |
| Aim / focus | Left trigger | Optional soft lock hoặc precision aim behavior |
| Interact | Face button | Hold cho risky actions |
| Ability | Shoulder button | Phải visible trong HUD prompt |
| Ping | D-pad hoặc shoulder combo | Single tap nhanh + hold wheel |

## Keyboard And Mouse

Keyboard/mouse ưu tiên clarity và remapping depth. PC players kỳ vọng fast inventory access, alternate bind, push-to-talk, và hold/toggle behavior riêng. System nên support các expectation đó mà không tạo mode-only action không thể đại diện trên device khác.

| Action | Default | Notes |
| :--- | :--- | :--- |
| Move | WASD | Fully remappable |
| Fire | Left mouse | No aim assist |
| Aim / focus | Right mouse | Optional hold/toggle |
| Interact | F | Hold cho extraction, revive, high-risk actions |
| Ping | Middle mouse | Hold mở ping wheel |
| Inventory | Tab | Opens tactical inventory |
| Map | M | Opens tactical map |

## Aim Assistance

Aim assistance tồn tại để bù input friction, không phải quyết định thay player. Nó nên giúp player giữ target họ đã thấy, đồng thời tránh target discovery, automatic transfer, hoặc shot có cảm giác bị chỉnh sau khi bắn. Accessibility aim assist có thể mạnh hơn, nhưng ranked rules phải nói rõ nó được xử lý thế nào.

| Assist | Touch | Controller | Keyboard/Mouse |
| :--- | :--- | :--- | :--- |
| Target friction | Yes | Yes | No |
| Snap strength | Very low | Low | No |
| Bullet magnetism | Avoid | Avoid | No |
| Accessibility assist | Optional | Optional | Optional for accessibility only |

Aim assistance không bao giờ được reveal hidden target hoặc override player intent.

## Camera Rules

Camera là một phần của control scheme. Zoom level, occlusion fade, rotation speed, và screen shake đều ảnh hưởng việc player đọc danger. Camera change nên smooth trong menu và decisive trong combat, với reduced-motion option từ session đầu.

| Rule | Requirement |
| :--- | :--- |
| Tactical readability | Player, enemy, cover, loot, và extraction cue vẫn legible trên màn hình nhỏ |
| Zoom | Limited pinch zoom, không tạo competitive scouting exploit |
| Rotation | Fixed hoặc constrained rotation theo readability của từng map |
| Shake | Reducible qua accessibility settings |
| Occlusion | Building và prop phải fade, cut away, hoặc outline khi che player |

## Platform Experience Notes

Touch players cần hit target rộng, gesture separation đáng tin, và contextual prompt mạnh. Tránh đặt combat button tần suất cao ở nơi player thường swipe camera. Accidental tap đặc biệt đắt trong extraction vì một interaction sai có thể lộ vị trí hoặc phí resource.

Controller players cần acceleration dễ đoán, deadzone tuning, và haptic feedback hỗ trợ decision-making. Empty magazine pulse, low-health warning, và extraction confirmation feedback có thể giảm việc scan UI khi áp lực.

Keyboard/mouse players cần precision, remapping, và quick access tới inventory, map, ping tools. Những input này có thể support nhiều shortcut hơn, nhưng core combat information phải tương đương trên mọi platform.

## Failure Cases

- Nếu input switching đổi prompt trong combat, nó không được steal focus hoặc block firing.
- Nếu player remap critical action, conflict phải detect trước khi save.
- Nếu touch button overlap trên device nhỏ, layout nên có simplified presets.
- Nếu aim assist mất target, nó nên fade out mượt thay vì snap away.
- Nếu camera occlusion che threat, outline/cutaway rule ưu tiên hơn visual fidelity.

## Control Tuning Knobs

- Touch button size kiểm soát confidence; button nhỏ tăng mis-tap nhanh hơn lợi ích screen space.
- Aim friction kiểm soát target tracking; quá nhiều thấy automated, quá ít làm touch combat mệt.
- Camera rotation speed kiểm soát scouting comfort; quá nhanh gây motion strain trên màn hình nhỏ.
- Hold duration kiểm soát accidental actions; extraction và discard cần confirmation mạnh hơn looting.
- Haptic strength kiểm soát feedback; empty magazine và confirmation pulse phải phân biệt rõ.
- Deadzone và response curve kiểm soát controller trust; default phải hợp average hardware nhưng editable.

## Settings Ownership

Trang này sở hữu control feel và input behavior. Complete settings matrix thuộc về [User Settings](usersettings/index.html) và [Settings Matrix](usersettings_matrix/index.html).

## Cross-References

| Topic | Page |
| :--- | :--- |
| Raid flow | [Core Gameplay](coregameplay/index.html) |
| HUD and map controls | [Navigation & Map](navigationandmap/index.html) |
| Settings UX | [User Settings](usersettings/index.html) |
| Accessibility options | [Accessibility](accessibility/index.html) |
| Tutorial prompts | [Tutorial Raid](tutorialraid/index.html) |
