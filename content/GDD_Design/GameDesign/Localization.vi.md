---
title: "Localization Strategy"
type: docs
---

## Tổng Quan

Localization ensures the game can ship clearly across target markets mà không breaking UI layout, tutorial clarity, monetization transparency, hoặc cultural expectations.

Localization is a design yêu cầu vì extraction games rely on quick comprehension. A mistranslated extraction cảnh báo, insurance rule, monetization label, hoặc tutorial prompt can tạo real frustration. The language pipeline must preserve meaning, timing, và UI fit.

The game should cách dùng controlled terminology from the start. Terms such as extract, stash, insured, operator, faction, raid, và safe house need stable translations so Người chơi có thể learn hệ thống across menus, tutorials, và patch ghi chú.

## Language Tiers

Language tiers should reflect business priority, community demand, support capacity, và UI readiness. A language không nên be added at launch nếu the team cannot support patch ghi chú, purchase text, tutorial text, và critical dịch vụ messages at an acceptable quality.

| Tier | Languages | Target |
| :--- | :--- | :--- |
| Tier 1 | English, Vietnamese, Thai, Indonesian, Portuguese, Spanish | Launch hoặc early launch markets |
| Tier 2 | French, German, Japanese, Korean, Simplified Chinese | Expansion markets |
| Tier 3 | Additional regional languages | Post-launch based on demand |

## Text Rules

Text rules reduce future layout bugs. Short English labels often expand dramatically in other languages, so buttons, cards, HUD markers, và mobile navigation need flexible layouts và tested truncation behavior.

| Rule | yêu cầu |
| :--- | :--- |
| cách dùng placeholders | Write `Extract {0} items`, not hardcoded thông số |
| Avoid text in images | UI art must support translation |
| Allow expansion | UI must handle 30-50% longer strings |
| cách dùng glossary | Terms like extract, stash, insured, faction, operator must stay nhất quán |
| Keep tone nhất quán | Tactical, rõ, not overly slang-heavy |

## Voice Strategy

Voice localization should prioritize comprehension-critical content first. Tutorial VO, cảnh báo, và hệ thống callouts matter more than flavor barks. Operator personality can still be preserved thông qua subtitles khi full dubbing is not practical.

| Content | Localization Direction |
| :--- | :--- |
| Critical tutorial VO | Localize for Tier 1 where budget allows |
| Operator barks | Subtitle all, dub selectively |
| hệ thống callouts | Prefer concise localized text và icon support |
| Seasonal narrative | Localize text first, dub by market priority |

## Cultural Review

Cultural review should happen trước final art lock. Symbols, gestures, faction names, monetization presentation, và event themes can require changes that are expensive nếu discovered sau UI, VO, hoặc trailer production.

| Area | Review Need |
| :--- | :--- |
| Faction names | Avoid unintended political hoặc cultural offense |
| Cosmetics | Check symbols, colors, và gestures |
| Monetization | Ensure regional legal compliance |
| Age ratings | Check violence, chat, purchases, và user-generated content |

## Localization Pipeline

| Step | Stage | Output |
| :--- | :--- | :--- |
| 1 | String authoring | source text với placeholders và context |
| 2 | Glossary check | Approved terminology |
| 3 | Localization export | Translation package |
| 4 | Translation | Localized strings |
| 5 | LQA pass | Language và context issues |
| 6 | UI overflow fix | Layout-safe text |
| 7 | Release candidate | Approved localized build content |

## Localization Examples

An extraction cảnh báo must remain short, urgent, và unambiguous in every supported language. nếu the translated string becomes too long for the HUD, the UI should support a shorter approved variant rather than shrinking text until it becomes unreadable.

An insurance rule needs exact terminology across loadout, recap, inbox, và support articles. nếu one màn hình says "recovered" và another says "returned" với different meanings, người chơi will misunderstand loss outcomes.

A seasonal event name can be creative, nhưng objective instructions should stay plain. Flavor text may cách dùng style; mission-critical text should prioritize clarity.

## Localization Failure Cases

- nếu translated buttons truncate on mobile, the layout needs flexible width hoặc alternate strings.
- nếu glossary terms drift between trang, tutorial và support burden increases.
- nếu monetization copy is unclear, regional compliance và người chơi trust are at risk.
- nếu voice is not localized, subtitles must carry timing, speaker identity, và tone.

## Tham Chiếu Chéo

| Topic | trang |
| :--- | :--- |
| Settings language options | [User Settings](usersettings/index.html) |
| Tutorial text | [Tutorial Raid](tutorialraid/index.html) |
| Accessibility text scale | [Accessibility](accessibility/index.html) |
