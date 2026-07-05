---
title: Tank
linkTitle: Tank
type: docs
weight: 4
---

# Tank

### Class Overview

The **Tank** class operators absorb damage and protect teammates. They excel at holding positions and leading pushes with their superior survivability. In an extraction shooter where every bullet matters, a Tank buys time — and time means loot.

#### Class Identity

| Attribute           | Value         | Notes                                              |
| ------------------- | ------------- | -------------------------------------------------- |
| **Role**            | Damage Sponge | Absorb and protect                                 |
| **Difficulty**      | Medium        | Beginner-friendly mechanics, positioning matters   |
| **Team Dependency** | Medium        | Better with team, can anchor solo extractions      |
| **Skill Ceiling**   | Medium        | Positioning and cooldown management define mastery |

#### Class Traits (All Tank Operators)

| Trait                | Effect                | Gameplay Impact                     |
| -------------------- | --------------------- | ----------------------------------- |
| **Reinforced Armor** | +25% Maximum Armor    | 125 armor cap (vs 100 standard)     |
| **Damage Reduction** | +10% Armor Absorption | Take less damage through armor      |
| **Heavy Frame**      | -15% Sprint Speed     | Slow rotations, commit to positions |

***

### Operators

| Operator                                                                                                                     | Codename | Specialty          | Unlock                   |
| ---------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------ | ------------------------ |
| [Mikhail Ivanov](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Bastion/README.md) | BASTION  | Frontal Protection | Level 10, 7,500 Credits  |
| [Wei Chen](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Tank/Goliath/README.md)       | GOLIATH  | Team Defense       | Level 20, 12,000 Credits |

***

### Playstyle Guide

#### When to Pick Tank

**Pick Tank when:**

* Your team needs a point leader for pushes
* Map has narrow chokepoints to hold
* Enemy team has aggressive Assault operators
* You need to anchor an extraction zone

**Avoid Tank when:**

* Map requires fast rotations between objectives
* Enemy team has multiple flankers (OBSIDIAN, MIRAGE)
* Your team already has a Tank
* You are playing solo and need to cover ground quickly

#### Positioning Guidelines

**Golden Rule:** Control space. You decide where fights happen.

| Position                      | Priority  | Why                                        |
| ----------------------------- | --------- | ------------------------------------------ |
| Chokepoint                    | Highest   | Force enemies through your kill zone       |
| Extraction Zone               | High      | Anchor the exit, protect looting teammates |
| Behind cover, facing approach | Good      | Reduce flanking exposure                   |
| Open ground                   | Dangerous | Even Tanks die to focus fire in the open   |

#### Combat Tactics

**The Push:**

1. Communicate intent ("Pushing left, follow me")
2. Deploy defensive ability (Shield or Armor Overcharge)
3. Move forward at walk speed — do not sprint
4. Draw enemy fire while teammates engage from sides
5. Hold position once you reach cover
6. Wait for cooldowns before pushing again

**The Hold:**

1. Position at extraction zone or objective
2. Deploy ability when enemy appears
3. Call out enemy positions
4. Let DPS teammates handle kills
5. Only retreat if ability is on cooldown AND health is critical

**Critical Mistake to Avoid:** Tanks often overcommit. Your job is to absorb damage, not chase kills. If your ability ends and enemies are still fighting, **fall back** and wait for cooldown. A dead Tank helps nobody.

***

### Counter Strategies

#### How to Counter Tank Operators

| Operator    | Counter Strategy                                                                     |
| ----------- | ------------------------------------------------------------------------------------ |
| **BASTION** | Flank behind the shield, use grenades around corners, wait out shield duration (15s) |
| **GOLIATH** | Focus fire before armor overcharge completes, use EMP to strip bonus armor           |

#### Best Counters to Tank

| Counter Pick | Why                                                  |
| ------------ | ---------------------------------------------------- |
| **OBSIDIAN** | Smoke flanks around shield, attacks from blind angle |
| **GLITCH**   | EMP disables Shield and strips Overcharge armor      |
| **SONAR**    | Intel reveals Tank position for flanking setup       |

***

### Synergies

#### Best Tank Duos

| Partner      | Synergy            | Notes                                                        |
| ------------ | ------------------ | ------------------------------------------------------------ |
| **SUTURE**   | Tank + Healer      | Sustain through any fight, classic combo                     |
| **TARTARUS** | Shield + CQB       | BASTION leads, TARTARUS flanks behind shield chaos           |
| **IGNITION** | Tank + Area Denial | Hold chokepoint, set fire to flanking routes                 |
| **AEGIS**    | Double Defense     | Guardian Shield + Riot Shield = near-invulnerable extraction |

***

### Top-Down Visual Identity

Tank operators have the **widest silhouette** in the roster. From the top-down camera, they are immediately recognizable by their broad shoulder plates and heavy armor profile.

| Feature            | Design Rule                                                 | Visibility |
| ------------------ | ----------------------------------------------------------- | ---------- |
| **Shoulder Width** | Widest in roster — 1.5x standard                            | 100+ units |
| **Headgear**       | Heavy riot visor or full-face helmet                        | 80+ units  |
| **Color Accent**   | Steel Blue (#3B82F6) on shoulder plates and visor edge      | 100+ units |
| **Back Profile**   | Shield (BASTION) or armor pack (GOLIATH) visible from above | 80+ units  |
| **Movement Anim**  | Slow, deliberate trudge — heaviest footfalls in roster      | 60+ units  |

#### Operator-Specific Top-Down Tells

| Operator | Unique Visual From Above                                                        |
| -------- | ------------------------------------------------------------------------------- |
| BASTION  | Riot shield visible on back when stowed; 120-degree arc indicator when deployed |
| GOLIATH  | Glowing armor plates when Overcharge is active, blue energy pulse effect        |

***

### Class Stamina Profile

| Parameter               | Tank Value        | Comparison             |
| ----------------------- | ----------------- | ---------------------- |
| **Stamina Pool**        | 80 (-20%)         | Lowest sprint duration |
| **Sprint Drain**        | 12/second (+20%)  | Drains fast            |
| **Recovery Rate**       | 7.2/second (-10%) | Slow recovery          |
| **Net Sprint Duration** | 6.7 seconds       | Shortest in roster     |

**Design Intent:** Tanks commit to positions. Sprinting to cover is a short burst, not a sustained run. This forces deliberate positioning decisions and prevents Tanks from excessively rotating.

***

### Status Effect Modifiers

| Effect | Tank Resistance | Notes                                                         |
| ------ | --------------- | ------------------------------------------------------------- |
| Stun   | 25%             | Reduced stun duration — harder to lock down                   |
| Slow   | 25%             | Partial slow resist — already slow, further slow is punishing |
| Burn   | 10%             | Minor fire resistance from heavy armor                        |
| EMP    | 0%              | Shield and Overcharge fully disabled by EMP                   |

**Design Intent:** Tanks resist physical CC effects (stun, slow) but are fully vulnerable to tech disruption (EMP). This creates the core Tank vs Specialist counterplay dynamic.

***

### Map Suitability

| Map Archetype        | Suitability | Recommended Operator | Why                                              |
| -------------------- | ----------- | -------------------- | ------------------------------------------------ |
| **Tight Corridors**  | Highest     | BASTION              | Shield covers entire corridor width              |
| **Extraction Zones** | High        | GOLIATH              | Armor Overcharge protects team during extraction |
| **Multi-Floor**      | Medium      | BASTION              | Shield protects against single-direction threats |
| **Open Fields**      | Low         | Neither              | Easy to flank around shield, no cover advantage  |
| **Dense Urban**      | Low         | Neither              | Too many angles to protect against               |

See [World Design](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/World/README.md) for detailed map layouts.
