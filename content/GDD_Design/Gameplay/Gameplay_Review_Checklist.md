---
title: "Gameplay Review Checklist & Benchmark"
type: docs
weight: 10
---

## Overview

This document supports the review and re-planning of Gameplay mechanics for the Multiplayer Hero Shooter Top-down Extraction cross-platform game. It contains: (1) a per-doc review checklist aligned to design pillars and cross-platform parity, and (2) a mechanics benchmark table vs. competitors.

> **Reference:** [Design Pillars](../../ProjectScope/design-pillars-enhanced.md), [Controls](../../GameDesign/Controls.md), [Competitive Analysis](../../Inventory_Gear/competitive-analysis-extraction-shooters.md).

---

## 1. Per-Document Review Checklist

| Document | Pillar alignment | Competitor benchmark | Cross-platform | Consistency | Done |
| :------- | :--------------- | :------------------- | :------------- | :---------- | :--- |
| CoreLoop.md | Aligned: 5 phases, risk profiles, economy; session 15–20 min in pillars | Benchmark below | Subsection added (session, pacing, link to Controls) | Links to Extraction, Gear, LOS | Yes |
| Movement_and_Stamina.md | Aligned: tactical fluidity, weight penalty, sound | Same movement values across platforms | Subsection added (input ref: stick vs WASD) | Gear weight refs | Yes |
| Gear_Mechanics.md | Aligned: resource heavy, weight consequences | Tetris + weight vs Tarkov/Arena Breakout | Already has Cross-Platform Considerations | Movement refs | Yes |
| Medical_System.md | Aligned: survival priority, health scarcity | Deep triage vs Arena Breakout mobile | Subsection added (heal UX: wheel vs hotkey) | Body part HP consistent | Yes |
| Looting_Interactions.md | Aligned: resource heavy, looting vulnerability | Container times, FIR vs genre | Subsection added (tap vs drag, auto-sort) | Gear grid refs | Yes |
| Hero_Abilities.md | Aligned: gunplay first, counterplay, extraction-aware | Cooldown vs ARC/Hawked | Already has Cross-Platform Ability Balance | LOS refs | Yes |
| Environmental_Hazards.md | Aligned: time pressure, tactical adaptation | Weather/hazard vs Tarkov/Hunt | Subsection added (performance/LOD) | Timer refs | Yes |
| Extraction_Mechanics.md | Aligned: climax, time vulnerability | Zone types vs genre | Subsection added (hold vs tap, timer visibility) | CoreLoop refs | Yes |
| LOS_Fog_Visibility.md | Aligned: fair visibility, intel | Shared vision vs team shooters | Subsection added (minimap/HUD same data) | Hero_Abilities refs | Yes |

---

## 2. Mechanics Benchmark (Our Game vs. Competitors)

| Mechanic | Tarkov | Hunt | Arena Breakout | Hawked | ARC Raiders | Our game |
| :------- | :----- | :--- | :------------- | :----- | :---------- | :------- |
| **Raid timer** | ~45 min (varies) | ~30 min | ~25–30 min (mobile) | Shorter sessions | 30 min + grace | 25–30 min standard; optional Quick Raid 15 min |
| **Session target** | Long | Medium | Mobile variable | Short | ~30 min | 15–20 min (mobile-friendly) |
| **Extract types** | Multiple, some conditional | Multiple, banish | Multiple, covert option | Extract with artifact | Timed pads | Standard, Emergency, Vehicle, Cooperative, Paid (future) |
| **Heal depth** | Body part, bleed, fracture, blacked | Health chunks, burn | Body part, complex (mobile) | Simpler | Moderate | Full body part, bleed, fracture, pain, blacked limb |
| **Ability model** | None (gear only) | Traits, no cooldown | None | Character abilities | Role gadgets, objective-tied | Operator cooldowns (30–90 s active, 120–240 s signature) |
| **Cross-play** | No | No | No (mobile vs PC separate) | PC + console | N/A | Yes (PC, Console, Mobile); same rules, platform UX |
| **Perspective** | First-person | First-person | First-person | Third-person | Third-person | Top-down |
| **Squad size** | 1–5 | 1–3 | 1–4 | 1–3 | Squad-based | 3 (squad); solo viable |

**Decisions recorded:** Raid timer 25–30 min with optional Quick Raid 15 min for 15–20 min session target. Medical depth kept (tactical pillar). Ability economy: cooldown-only, no per-raid charge limit; max ~2 signature uses per 20 min. Cross-platform: subsection in each Gameplay doc; same rules, input/UX by platform (see Controls).

---

## 3. Cross-References

- [Core Gameplay Loop](CoreLoop.md) — Session length & pacing, extraction flow.
- [Design Pillars](../../ProjectScope/design-pillars-enhanced.md) — Genre pillars, our positioning, target session.
- [Controls](../../GameDesign/Controls.md) — Input and UX by platform (PC, Mobile, Console).
- [Competitive Analysis](../../Inventory_Gear/competitive-analysis-extraction-shooters.md) — Market and competitor mechanics.
