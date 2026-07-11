---
title: "Accessibility Design"
type: docs
---

## Overview

Accessibility đảm bảo extraction loop có thể được hiểu, cấu hình, và chơi bởi nhiều người nhất có thể mà không làm hỏng competitive integrity.

Accessibility là một phần của core design, không phải một settings dump sau launch. Extraction games dựa vào sound, timing, visual contrast, inventory reading, và pressure decisions; mỗi thứ đó có thể loại trừ người chơi nếu chỉ có một cách trình bày. Mục tiêu là cung cấp information và control tương đương, không tạo hidden advantage.

Accessibility choices phải có trước tutorial raid đầu tiên. Player cần text lớn hơn, reduced flash, remapped inputs, subtitles, hoặc simplified HUD không nên phải hoàn thành combat encounter mới tới được option đó.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Accessibility entry point | Available from first launch and Settings |
| Defaults | Subtitles on, flash reduction on, readable text scale |
| Competitive integrity | Accessibility assists cannot reveal hidden information |
| Testing | Every major feature needs accessibility review |

## Visual Accessibility

Visual accessibility phải xét combat readability và inventory readability riêng. Loot rarity color hoạt động trong menu có thể fail trên map sáng. Danger marker ổn trên desktop có thể quá nhỏ trên mobile. Mọi critical signal cần ít nhất một kênh reinforce không dựa vào màu.

| Feature | Requirement |
| :--- | :--- |
| Colorblind modes | Protanopia, Deuteranopia, Tritanopia, Achromatopsia |
| Rarity without color | Shape, icon, text label, hoặc pattern hỗ trợ rarity color |
| Text readability | Scalable text và contrast-safe UI |
| High contrast | Outline, marker, và focus state mạnh hơn |
| Reduced flash | Giới hạn bright flash và rapid strobing |
| Motion reduction | Giảm camera shake và transition aggressive |

## Auditory Accessibility

Audio là tactical information, nên game cần alternative cẩn thận cho player không thể dựa hoàn toàn vào âm thanh. Visual sound indicator nên truyền direction và category, nhưng không được reveal exact position hoặc thông tin mà hearing players không nhận được.

| Feature | Requirement |
| :--- | :--- |
| Subtitles | On by default cho narrative và tutorial speech |
| Directional sound indicators | Optional visual cue cho gunfire, ping, và extraction sounds |
| Voice chat captions | Future-facing, phụ thuộc platform capability |
| Audio mix presets | Night, standard, wide dynamic range |

## Motor Accessibility

Motor accessibility nên giảm input strain không cần thiết nhưng vẫn giữ risk. Hold-to-extract, repeated looting, sprint behavior, và ability casting cần alternative vì đây là action thường xuyên dưới pressure. Ranked restriction phải explicit khi timing assistance thay đổi competitive assumption.

| Feature | Requirement |
| :--- | :--- |
| Remapping | Core actions remappable nơi platform cho phép |
| Hold alternatives | Tap, hold, và toggle variants cho repeated/long actions |
| Aim assist | Configurable cho touch/controller, bị giới hạn bởi fairness rules |
| Touch layout presets | Default, left-handed, claw, simplified |
| Timing windows | Tutorial và non-ranked content có thể cho timing dễ hơn |

## Cognitive Accessibility

Cognitive accessibility đặc biệt quan trọng vì extraction games có thể overwhelm player với nhiều goal cùng lúc. Objective hierarchy, death recap clarity, pinned goals, và simplified HUD mode giúp player quyết định thứ gì quan trọng ngay bây giờ.

| Feature | Requirement |
| :--- | :--- |
| Tutorial guidance | Dạy từng concept một |
| Objective clarity | Current objective và extraction state luôn recoverable |
| Death recap | Giải thích cause of death và learning opportunity tiếp theo |
| Simplified HUD | Giảm optional widget và visual noise |
| Memory aids | Quest reminder, pinned goals, route markers |

## Accessibility Checklist

Checklist này dùng trong feature review, không chỉ QA. Một system chưa sẵn sàng nếu nó phụ thuộc màu duy nhất, giấu text critical ở size nhỏ, yêu cầu rapid input lặp lại, hoặc không có recovery path sau confusion.

| Check | Required For |
| :--- | :--- |
| Text remains readable at mobile size | All UI |
| Core signals have non-color alternatives | Loot, danger, rarity, squad |
| Actions have remap or alternative input | Controls, UI, minigames |
| Motion and flash can be reduced | Camera, VFX, transitions |
| Tutorial explains settings where relevant | FTUE and settings |

## Accessibility Examples

Player có color vision deficiency vẫn phải phân biệt loot rarity bằng icon shape, text label, hoặc pattern. Color có thể reinforce signal, nhưng không được là kênh duy nhất.

Player không thể giữ button thoải mái nên đổi được sprint, aim, interact, và extraction behavior nơi fairness cho phép. Với risky action, alternative vẫn có thể yêu cầu confirmation.

Player nhạy với motion nên giảm được camera shake, flash intensity, và aggressive menu transition trước khi tutorial bắt đầu.

## Review Notes

- Accessibility options phải test trên UI kích thước mobile, không chỉ desktop.
- Ranked restriction cần review case-by-case thay vì disable cả category accessibility rộng.
- Tutorial prompt nên nhắc settings liên quan khi player struggle lặp lại.
- Subtitle và critical warning phải sống được qua combat ồn và màn hình nhỏ.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Settings options | [User Settings](usersettings/index.html), [Settings Matrix](usersettings_matrix/index.html) |
| Controls | [Controls](controls/index.html) |
| Navigation signals | [Navigation & Map](navigationandmap/index.html) |
| Tutorial | [Tutorial Raid](tutorialraid/index.html) |
