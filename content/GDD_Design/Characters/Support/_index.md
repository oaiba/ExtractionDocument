---
title: Support
linkTitle: Support
type: docs
weight: 2
---


### Class Overview

The **Support** class operators are the backbone of any team, keeping allies alive and enabling extended engagements. They sacrifice personal combat power for team utility.

#### Class Identity

| Attribute           | Value                 | Notes                |
| ------------------- | --------------------- | -------------------- |
| **Role**            | Team Healer / Sustain | Keep team alive      |
| **Difficulty**      | Low                   | Beginner-friendly    |
| **Team Dependency** | High                  | Best with teammates  |
| **Skill Ceiling**   | Medium                | Positioning + timing |

#### Class Traits (All Support Operators)

| Trait                 | Effect                          | Gameplay Impact               |
| --------------------- | ------------------------------- | ----------------------------- |
| **Medical Expertise** | +20% Healing Item Effectiveness | Medkits heal 60 instead of 50 |
| **Quick Revive**      | +15% Revive Speed               | Faster teammate pickup        |
| **Slow Movement**     | -5% Movement Speed              | Slight positioning penalty    |

***

### Operators

| Operator                                                                                                                         | Codename | Specialty         | Unlock                   |
| -------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------------- | ------------------------ |
| [Tariq Al-Sayed](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Suture/README.md)   | SUTURE   | Area Healing      | Free Starter             |
| [Victoria Sterling](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Support/Aegis/README.md) | AEGIS    | Damage Prevention | Level 18, 10,000 Credits |

***

### Playstyle Guide

#### When to Pick Support

**Pick Support when:**

* Your team has aggressive players
* Map requires holding positions
* Extended engagements expected
* You want to enable teammates

**Avoid Support when:**

* Playing solo
* Team already has a Support
* Map is wide open (no cover)
* Enemy has heavy burst damage

#### Positioning Guidelines

**Golden Rule:** Stay behind your damage dealers.

| Position    | Priority                    |
| ----------- | --------------------------- |
| Behind Tank | Highest — Protected         |
| Mid-team    | Good — Can reach everyone   |
| Flank       | Dangerous — Only for ambush |
| Front       | Never — You will die first  |

#### Healing Priority

```
1. Low HP teammate in combat
2. Yourself (if low)
3. Pre-healing before push
4. Topping off full HP allies (low priority)
```

***

### Counter Strategies

#### How to Counter Support Operators

| Operator   | Counter Strategy                     |
| ---------- | ------------------------------------ |
| **SUTURE** | Kill drone first, then focus SUTURE  |
| **AEGIS**  | Wait for shield duration, then burst |

#### Best Counters to Support

| Counter Pick | Why                              |
| ------------ | -------------------------------- |
| **MAMBA**    | Burst damage exceeds healing     |
| **TARTARUS** | CQB kills before healing matters |
| **GLITCH**   | EMP disables support abilities   |

***

### Synergies

#### Best Support Duos

| Partner     | Synergy           | Notes                           |
| ----------- | ----------------- | ------------------------------- |
| **MAMBA**   | Assault + Sustain | Push harder, heal after         |
| **BASTION** | Tank + Healer     | Classic defensive combo         |
| **SONAR**   | Intel + Safety    | Know when to heal, when to hide |

***

### Top-Down Visual Identity

Support operators have a **medium silhouette** with medical/utility pack on their back as the primary identifier from above.

| Feature            | Design Rule                                             | Visibility |
| ------------------ | ------------------------------------------------------- | ---------- |
| **Shoulder Width** | Standard — between Recon and Assault                    | 60+ units  |
| **Headgear**       | Medical cap or visor with cross markings                | 60+ units  |
| **Color Accent**   | White/Green (#22C55E) on cross armband and backpack     | 80+ units  |
| **Back Profile**   | Large medical pack (SUTURE) or shield generator (AEGIS) | 80+ units  |
| **Movement Anim**  | Standard pace, slightly cautious posture                | 50+ units  |

#### Operator-Specific Top-Down Tells

| Operator | Unique Visual From Above                                            |
| -------- | ------------------------------------------------------------------- |
| SUTURE   | Green pulsing circle around Healing Drone when deployed             |
| AEGIS    | Blue-white hemispherical shield dome visible from above when active |

***

### Class Stamina Profile

| Parameter               | Support Value  | Comparison |
| ----------------------- | -------------- | ---------- |
| **Stamina Pool**        | 100 (Standard) | Average    |
| **Sprint Drain**        | 10/second      | Standard   |
| **Recovery Rate**       | 8/second       | Standard   |
| **Net Sprint Duration** | 10.0 seconds   | Average    |

**Design Intent:** Support has standard stamina. They do not need to sprint to engage (like Assault) or reposition (like Recon). Their -5% movement speed class trait is the real limitation, not stamina.

***

### Status Effect Modifiers

| Effect | Support Resistance | Notes                                              |
| ------ | ------------------ | -------------------------------------------------- |
| Stun   | 0%                 | Full stun duration                                 |
| Slow   | 10%                | Slight slow resist for reaching downed allies      |
| Burn   | 0%                 | Full burn damage                                   |
| EMP    | 0%                 | Healing Drone and Guardian Shield destroyed by EMP |

**Design Intent:** Support has minimal resistances. Their value comes from sustaining teammates, not from personal survivability. The slight slow resist ensures they can still reach wounded allies during combat.

***

### Map Suitability

| Map Archetype        | Suitability | Recommended Operator | Why                                                       |
| -------------------- | ----------- | -------------------- | --------------------------------------------------------- |
| **Extraction Zones** | Highest     | AEGIS                | Guardian Shield protects team during extraction countdown |
| **Tight Corridors**  | High        | SUTURE               | Healing Drone radius covers corridor width                |
| **Multi-Floor**      | Medium      | SUTURE               | Drone heals through floors if placed on correct level     |
| **Open Fields**      | Low         | AEGIS                | Shield provides cover in open terrain                     |
| **Dense Urban**      | Medium      | Either               | Multiple engagement points require mobile healing         |

See [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) for detailed map layouts.
