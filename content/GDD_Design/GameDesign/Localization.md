---
title: "Localization Strategy"
type: docs
---

## Overview

Localization ensures the game can ship clearly across target markets without breaking UI layout, tutorial clarity, monetization transparency, or cultural expectations.

Localization is a design requirement because extraction games rely on quick comprehension. A mistranslated extraction warning, insurance rule, monetization label, or tutorial prompt can create real frustration. The language pipeline must preserve meaning, timing, and UI fit.

The game should use controlled terminology from the start. Terms such as extract, stash, insured, operator, faction, raid, and safe house need stable translations so players can learn systems across menus, tutorials, and patch notes.

## Language Tiers

Language tiers should reflect business priority, community demand, support capacity, and UI readiness. A language should not be added at launch if the team cannot support patch notes, purchase text, tutorial text, and critical service messages at an acceptable quality.

| Tier | Languages | Target |
| :--- | :--- | :--- |
| Tier 1 | English, Vietnamese, Thai, Indonesian, Portuguese, Spanish | Launch or early launch markets |
| Tier 2 | French, German, Japanese, Korean, Simplified Chinese | Expansion markets |
| Tier 3 | Additional regional languages | Post-launch based on demand |

## Text Rules

Text rules reduce future layout bugs. Short English labels often expand dramatically in other languages, so buttons, cards, HUD markers, and mobile navigation need flexible layouts and tested truncation behavior.

| Rule | Requirement |
| :--- | :--- |
| Use placeholders | Write `Extract {0} items`, not hardcoded numbers |
| Avoid text in images | UI art must support translation |
| Allow expansion | UI must handle 30-50% longer strings |
| Use glossary | Terms like extract, stash, insured, faction, operator must stay consistent |
| Keep tone consistent | Tactical, clear, not overly slang-heavy |

## Voice Strategy

Voice localization should prioritize comprehension-critical content first. Tutorial VO, warnings, and system callouts matter more than flavor barks. Operator personality can still be preserved through subtitles when full dubbing is not practical.

| Content | Localization Direction |
| :--- | :--- |
| Critical tutorial VO | Localize for Tier 1 where budget allows |
| Operator barks | Subtitle all, dub selectively |
| System callouts | Prefer concise localized text and icon support |
| Seasonal narrative | Localize text first, dub by market priority |

## Cultural Review

Cultural review should happen before final art lock. Symbols, gestures, faction names, monetization presentation, and event themes can require changes that are expensive if discovered after UI, VO, or trailer production.

| Area | Review Need |
| :--- | :--- |
| Faction names | Avoid unintended political or cultural offense |
| Cosmetics | Check symbols, colors, and gestures |
| Monetization | Ensure regional legal compliance |
| Age ratings | Check violence, chat, purchases, and user-generated content |

## Localization Pipeline

| Step | Stage | Output |
| :--- | :--- | :--- |
| 1 | String authoring | Source text with placeholders and context |
| 2 | Glossary check | Approved terminology |
| 3 | Localization export | Translation package |
| 4 | Translation | Localized strings |
| 5 | LQA pass | Language and context issues |
| 6 | UI overflow fix | Layout-safe text |
| 7 | Release candidate | Approved localized build content |

## Localization Examples

An extraction warning must remain short, urgent, and unambiguous in every supported language. If the translated string becomes too long for the HUD, the UI should support a shorter approved variant rather than shrinking text until it becomes unreadable.

An insurance rule needs exact terminology across loadout, recap, inbox, and support articles. If one screen says "recovered" and another says "returned" with different meanings, players will misunderstand loss outcomes.

A seasonal event name can be creative, but objective instructions should stay plain. Flavor text may use style; mission-critical text should prioritize clarity.

## Localization Failure Cases

- If translated buttons truncate on mobile, the layout needs flexible width or alternate strings.
- If glossary terms drift between pages, tutorial and support burden increases.
- If monetization copy is unclear, regional compliance and player trust are at risk.
- If voice is not localized, subtitles must carry timing, speaker identity, and tone.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Settings language options | [User Settings](usersettings/index.html) |
| Tutorial text | [Tutorial Raid](tutorialraid/index.html) |
| Accessibility text scale | [Accessibility](accessibility/index.html) |
