# High-Level Game Design Document
## Extraction Topdown Mobile Multiplayer

**For:** Game Designers, Artists, 3D Artists, Level Designers, Sound Designers, UI/UX Designers

**[← Back to Main](../README.md)** | **[View Technical GDD →](../GDD_Technical/README.md)**

---

## Purpose

This document focuses on **game design, art direction, and player experience**. This is the primary reference for:
- Game Designers designing mechanics and balance
- Artists creating visual assets
- Level Designers building maps
- Sound Designers creating audio experience
- UI/UX Designers designing interfaces

**Does not include:** Implementation details, code, technical specifications (see [Technical GDD](../GDD_Technical/README.md))

---

## 📚 Documentation Structure

### 🎮 Game Design
Core game design, mechanics, and progression systems

- **[Overview](./GameDesign/Overview.md)** - Game concept, pillars, target audience, competitive analysis
- **[Core Gameplay](./GameDesign/CoreGameplay.md)** - Gameplay loop, phases, player psychology, session flow
- **[Progression](./GameDesign/Progression.md)** - Player progression, economy, quests, battle pass, monetization

---

### ⚔️ Combat Systems
Weapon design, items, and combat mechanics

- **[Weapons](./Combat/Weapons.md)** - Weapon categories, modifications, combat mechanics, balance
- **[Items & Economy](./Combat/Items.md)** - Item systems, loot, inventory, trading marketplace

---

### 👤 Characters
Character design and abilities

- **[Operators](./Characters/Operators.md)** - Operator classes, abilities, progression, synergies, cosmetics

---

### 🗺️ World Design
Maps, environments, and level design

- **[Map Design](./World/MapDesign.md)** - Map structure, zones, loot distribution, environmental storytelling

---

### 🎨 Visual Design
Art direction and user interface

- **[Art Direction](./Visuals/ArtDirection.md)** - Visual style, color palette, character/environment art, VFX, animation
- **[User Interface](./Visuals/UserInterface.md)** - UI/UX design, screen layouts, controls, accessibility

---

### 🔊 Audio Design
Sound and music

- **[Sound Design](./Audio/SoundDesign.md)** - Audio vision, combat audio, environmental audio, music, voice lines

---

## 📖 How to Use This Document

**For Game Designers:**
- Read entirely to understand game vision
- Reference when designing new mechanics
- Update when there are balance changes

**For Artists:**
- Focus on Visuals section (Art Direction, UI)
- Reference Characters and World for context
- Follow guidelines when creating assets

**For Level Designers:**
- Deep dive into World → Map Design
- Understand Core Gameplay Loop to design flow
- Coordinate with Artists on visual style

**For Sound Designers:**
- Follow Audio → Sound Design guidelines
- Reference Core Gameplay to understand audio cues
- Coordinate with Game Designers on feedback

**For UI/UX Designers:**
- Follow Visuals → User Interface guidelines
- Understand User Flow and player journey
- Coordinate with Developers on technical constraints

---

## 🎯 Design Philosophy

**Player-First Design:**
- Every design decision must benefit player experience
- Fair and balanced gameplay
- Respect player's time and effort

**Mobile-Optimized:**
- Controls must be intuitive and responsive
- Matches designed for short sessions (10-15 minutes)
- Performance across multiple devices

**Depth Through Simplicity:**
- Easy to learn, hard to master
- Clear mechanics with deep strategy
- Progressive complexity

---

## 📝 Glossary

**Core Terms:**
- **Extraction:** Process of leaving map with loot
- **Hot Zone:** High-risk, high-reward areas
- **Operator:** Playable character class
- **Stash:** Permanent storage for extracted items
- **MMR:** Matchmaking Rating
- **POI:** Point of Interest
- **TTK:** Time to Kill
- **DPS:** Damage Per Second

---

## 📅 Update Log

| Date       | Section   | Changes                            | Updated By |
| ---------- | --------- | ---------------------------------- | ---------- |
| 2026-02-06 | Structure | Reorganized to folder-based system | Team       |
| 2026-02-06 | Combat    | Added Weapons & Items documents    | Team       |
| 2026-02-06 | All       | Initial documentation              | Team       |

---

## 🔗 Quick Navigation

**Start Here:**
- New to project? → [Overview](./GameDesign/Overview.md)
- Understanding gameplay? → [Core Gameplay](./GameDesign/CoreGameplay.md)
- Designing characters? → [Operators](./Characters/Operators.md)

**Deep Dives:**
- Combat systems → [Weapons](./Combat/Weapons.md) + [Items](./Combat/Items.md)
- Visual design → [Art Direction](./Visuals/ArtDirection.md) + [UI](./Visuals/UserInterface.md)
- Progression → [Progression](./GameDesign/Progression.md)

---

**[← Back to Main](../README.md)** | **[View Technical GDD →](../GDD_Technical/README.md)**
