---
title: "Gameplay Review Checklist & Benchmark"
type: docs
weight: 10
---

## Overview

This document supports the review and re-planning of Gameplay mechanics for the Multiplayer Hero Shooter Top-down Extraction cross-platform game. It contains: (1) a per-doc review checklist aligned to design pillars and cross-platform parity, (2) a mechanics benchmark table vs. competitors, and (3) a record of consistency fixes applied across docs.

> **Reference:** [Design Pillars](../../ProjectScope/design-pillars-enhanced.md), [Controls](../../GameDesign/Controls.md), [Competitive Analysis](../../Inventory_Gear/competitive-analysis-extraction-shooters.md).

---

## 1. Per-Document Review Checklist

| Document | Pillar alignment | Competitor benchmark | Cross-platform | Consistency | Done |
| :------- | :--------------- | :------------------- | :------------- | :---------- | :--- |
| CoreLoop.md | Aligned: 5 phases, risk profiles, economy; session 15–20 min in pillars | Benchmark below | Subsection added (session, pacing, link to Controls) | Links to Extraction, Gear, LOS | ✅ |
| Movement_and_Stamina.md | Aligned: tactical fluidity, weight penalty, sound | Same movement values across platforms | Subsection added (input ref: stick vs WASD) | Gear weight refs | ✅ |
| Gear_Mechanics.md | Aligned: resource heavy, weight consequences | Tetris + weight vs Tarkov/Arena Breakout | Already has Cross-Platform Considerations | Movement refs | ✅ |
| Medical_System.md | Aligned: survival priority, health scarcity | Deep triage vs Arena Breakout mobile | Subsection added (heal UX: wheel vs hotkey) | Body part HP consistent | ✅ |
| Looting_Interactions.md | Aligned: resource heavy, looting vulnerability | Container times, FIR vs genre | Subsection added (tap vs drag, auto-sort) | Gear grid refs | ✅ |
| Hero_Abilities.md | Aligned: gunplay first, counterplay, extraction-aware | Cooldown vs ARC/Hawked | Already has Cross-Platform Ability Balance | LOS refs | ✅ |
| Environmental_Hazards.md | Aligned: time pressure, tactical adaptation | Weather/hazard vs Tarkov/Hunt | Subsection added (performance/LOD) | Timer scale note confirmed | ✅ |
| Extraction_Mechanics.md | Aligned: climax, time vulnerability | Zone types vs genre | Subsection added (hold vs tap, timer visibility) | Insurance fixed — see §3 | ✅ |
| LOS_Fog_Visibility.md | Aligned: fair visibility, intel | Shared vision vs team shooters | Subsection added (minimap/HUD same data) | Wraith ref fixed — see §3 | ✅ |
| **Camera_System.md** *(NEW)* | Aligned: topdown-specific; info parity no exploit | Unique to topdown genre — no competitor comparison | Full mobile, console, PC section | Inertia coupled to Gear_Mechanics | ✅ |
| **AI_Enemy_Behavior.md** *(NEW)* | Aligned: tactical pressure, sound-critical, Scav karma | Tarkov AI depth; ARC machine variety | Same AI rules all platforms | Sound ranges from Movement & Stamina | ✅ |
| **Matchmaking_Lobby.md** *(NEW)* | Aligned: cross-platform parity, fair play, no SBMM | ABMM inspired by ARC Raiders | Full cross-platform pool section | Disconnect rule from Extraction | ✅ |
| **Hydration_Energy.md** *(NEW)* | Aligned: survival priority, gear packing depth | Tarkov hydration/energy model adapted | Same bars/rules all platforms; HUD adapts | Stomach link to Medical_System | ✅ |
| **Hideout_Crafting.md** *(NEW)* | Aligned: persistent progression, economy sinks | Tarkov hideout depth; ARC Speranza | Server-clock timers; mobile offline notify | Economy refs to GameDesign/Economy | ✅ |

---

## 2. Mechanics Benchmark (Our Game vs. Competitors)

| Mechanic | Tarkov | Hunt | Arena Breakout | Hawked | ARC Raiders | Our game |
| :------- | :----- | :--- | :------------- | :----- | :---------- | :------- |
| **Raid timer** | ~45 min | ~30 min | ~25–30 min (mobile) | Short sessions | 30 min + grace | 25–30 min standard; Quick Raid 15 min |
| **Extract types** | Multiple, conditional | Multiple, banish | Multiple | Extract with artifact | Timed pads | Standard, Emergency, Vehicle, Cooperative, Paid |
| **Heal depth** | Body part, bleed, fracture | Health chunks, burn | Body part (mobile) | Simpler | Moderate | Full: body part, bleed, fracture, pain, blacked limb |
| **Ability model** | None | Traits, no cooldown | None | Character abilities | Role gadgets | Operator cooldowns + Signature (30–240 s) |
| **Cross-play** | No | No | No | PC + console | No | PC + Console + Mobile (same rules) |
| **Perspective** | FPS | FPS | FPS | Third-person | Third-person | **Top-down (unique)** |
| **Squad size** | 1–5 | 1–3 | 1–4 | 1–3 | Squad-based | 1–3 |
| **AI system** | Deep Scav + bosses | Grunt/boss types | Basic AI | Limited | Machine AI types | Tier 1–4 enemies + 3 bosses + Player-as-Scav karma |
| **Matchmaking** | Regional, no SBMM | Regional | Regional | Regional | ABMM (beta) | Regional + soft ABMM for new players |
| **Hydration/Energy** | Yes (full) | No | No | No | No | Yes (stomach-linked survival bars) |
| **Hideout** | Yes (deep) | Camp (limited) | Limited | Limited | Speranza | Module tree + Bitcoin Farm + crafting |
| **Camera** | FPS | FPS | FPS | Third-person | Third-person | **Top-down (new design pillar)** |

**Decisions recorded:** Raid timer 25–30 min with optional Quick Raid 15 min for 15–20 min session target. Medical depth kept (tactical pillar). Ability economy: cooldown-only, no per-raid charge limit; max ~2 signature uses per 20 min. Cross-platform: subsection in each Gameplay doc; same rules, input/UX by platform (see Controls). Five new GDDs created 2026-02-28 to fill critical gaps.

---

## 3. Consistency Fixes Applied (2026-02-28)

| # | Bug | Files Affected | Fix Applied |
| - | --- | -------------- | ----------- |
| 1 | **Insurance contradiction**: Extraction_Mechanics.md said "backpack NOT covered"; Gear_Mechanics.md said "rig AND backpack covered" | Extraction_Mechanics.md | Extraction_Mechanics.md updated — backpack items ARE insured. Now matches Gear_Mechanics.md. |
| 2 | **"Wraith/Recon" operator** referenced in LOS_Fog_Visibility.md smoke table — operator does not exist in Hero_Abilities.md roster | LOS_Fog_Visibility.md | Replaced with "Smoke Grenade (Viper / future operator)". Wraith reserved for future expansion in P1. |
| 3 | **Contamination timer scale** in Environmental_Hazards.md uses 15-min Quick Raid table | Environmental_Hazards.md | Clarification note already present in doc (line 97). Verified correct — no change needed. |
| 4 | **Scav Mode vs AI Scav Wave** — CoreLoop.md and Environmental_Hazards.md used the terms interchangeably | AI_Enemy_Behavior.md (new) | Resolved by AI_Enemy_Behavior.md §"Player-as-Scav" and §"AI Scav Raid Event" cleanly separating both concepts. |
| 5 | **Bulwark Fortress + Extraction** — Fortress Protocol reduces damage; unclear if reduced damage still resets extraction timer | Hero_Abilities.md, Extraction_Mechanics.md | **Design decision (recorded here):** Any damage, even reduced through Fortress, resets the extraction timer. Damage reduction affects HP loss only. No file edit needed. |

---

## 4. Cross-References

- [Core Gameplay Loop](CoreLoop.md) — Session length & pacing, extraction flow.
- [Design Pillars](../../ProjectScope/design-pillars-enhanced.md) — Genre pillars, our positioning, target session.
- [Controls](../../GameDesign/Controls.md) — Input and UX by platform (PC, Mobile, Console).
- [Competitive Analysis](../../Inventory_Gear/competitive-analysis-extraction-shooters.md) — Market and competitor mechanics.
- [Camera System](Camera_System.md) — Top-down camera design, altitude, FOV.
- [AI Enemy Behavior](AI_Enemy_Behavior.md) — Enemy types, detection, bosses, Scav karma.
- [Matchmaking & Lobby](Matchmaking_Lobby.md) — Queue, squad, reconnect.
- [Hydration & Energy](Hydration_Energy.md) — Survival resource bars.
- [Hideout & Crafting](Hideout_Crafting.md) — Module tree, passive income.
