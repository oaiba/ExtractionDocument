---
title: "Weapons & Combat Systems"
type: docs
---

> **Canonical source:** Full weapon categories, stats, ammo, attachments, damage model, TTK, and combat mechanics are documented in **[Weapon Arsenal & Combat Systems](../gameplay/weaponarsenal/index.html)**. This page retains combat philosophy only.

---

## Combat Philosophy

**Core Principles:**

1. **Tactical Over Twitch** — Positioning and decision-making matter more than raw reflexes.
2. **Weapon Variety** — Each weapon has a distinct role and feel.
3. **Risk vs Reward** — Better weapons come with higher loss penalty.
4. **Skill Expression** — High skill ceiling with recoil control and positioning.
5. **Mobile Optimized** — Controls and mechanics designed for touch screens.

For weapon categories, specifications, ammunition, attachments, damage system, ballistics, and time-to-kill data, see [Weapon Arsenal & Combat Systems](../gameplay/weaponarsenal/index.html).

## Combat-Facing Weapon Role Taxonomy

Weapon roles are defined by the combat question they ask, not by raw DPS. A strong weapon should create a readable advantage in its intended band and a readable weakness outside it.

| Role | Primary Range | Skill Ask | Mobility | Recoil / Spread Identity | Suppression Role | Loot / Economy Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| AR | Close-mid to mid | Track target, control burst, choose cover | Medium | Controllable burst, moderate sustained climb | Flexible pressure | Default earned/trader power baseline |
| SMG | Close | Flank timing, hip-fire discipline, ammo management | High | Fast bloom, fast recovery, short falloff | Room clear pressure | Budget-to-specialist CQB option |
| Shotgun | Close burst | Angle trap, pellet discipline, reload timing | Medium | Wide spread, high punishment for miss | Breach / denial | High-risk close loot value |
| DMR | Mid-long | Patience, semi-auto cadence, sightline control | Medium-low | Low bloom, high aim penalty while moving | Pick pressure | Precision economy sink |
| Sniper | Long | Setup, line control, extraction timing | Low | Sway, slow follow-up, high commitment | Area denial | Rare/high-value objective weapon |
| LMG | Mid suppression | Setup, lane control, reload planning | Low | Heavy sustained recoil, strong volume | Primary suppression | Expensive squad support kit |
| Pistol | Close backup | Draw timing, emergency aim | High | Low stability under spam | Last-resort pressure | Recovery/budget safety net |
| Melee | Contact | Stealth, ambush, desperation | Highest | No spread, high exposure | Silent finish only | Low/no-cost fallback |

## Damage And Readability Principles

Players must understand why a shot hit, missed, failed to penetrate, staggered them, suppressed them, or killed them. Combat UI and audio should teach without turning firefights into spreadsheet overlays.

| Event | Required Feedback | Must Avoid |
| :--- | :--- | :--- |
| Flesh hit | Clear hit marker, impact sound, blood/cloth effect | Same feedback as armor hit |
| Armor hit | Hard impact sound, armor spark/debris, armor hit marker variant | Hidden blocked damage |
| No penetration | Blocked/deflected cue and reduced or no HP feedback | Making player think netcode failed |
| Headshot | Distinct but short cue, death recap confirmation | Large mid-fight celebration clutter |
| Suppression | Vignette/audio ducking/aim pressure that is readable and brief | Color-only or permanent blur |
| Ricochet | Sharp deflect sound and visible glancing cue | Silent zero-damage result |
| Low ammo / reload | Ammo color, click/VO, reload progress | Surprise empty gun without warning |

## Firefight Pacing And Counterplay

| Principle | Requirement |
| :--- | :--- |
| Mistake punishment | Bad positioning should be punished faster than cautious repositioning. |
| Counterplay window | Most non-sniper deaths should give a short readable cause: angle, sound, armor failure, reload, or overexposure. |
| Armor trust | Armor must visibly reduce or deflect damage, but damaged armor must explain why it failed later. |
| Attachment trade-off | Attachments can improve a role, but should add weight, ADS cost, noise, visibility, price, or slot conflict. |
| No paid power | Premium cosmetics or entitlements never grant combat-power item instances. |

## Combat QA Checklist

- Each weapon role has a preferred range, skill ask, and counterplay.
- No weapon is best at close, mid, long, mobility, recoil, cost, and armor penetration simultaneously.
- Armor hit, flesh hit, ricochet, blocked shot, suppression, headshot, and low ammo feedback are distinguishable by more than color.
- Death recap can name weapon, hit zone, armor interaction, and key cause without exposing unfair enemy inventory data.
- Tuning changes link back to [Weapon Balance Framework](../weapons/weapon_balance_framework/index.html) rather than inventing one-off rules here.
