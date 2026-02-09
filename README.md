# Extraction Shooter Project - Game Design Document (GDD)

**Version:** 1.1  
**Last Updated:** February 7, 2026  
**Platform:** Mobile (iOS/Android), Windows PC, Controller support  
**Engine:** Unreal Engine 5 (C++)  
**Genre:** Extraction Shooter, Top-down, Multiplayer

---

## 📌 Project Overview

This is the central Game Design Document for a top-down extraction shooter. Players infiltrate hazardous zones, scavenge for valuable loot, fight hostile factions and other players, and extract to secure their gains. High stakes, tactical gameplay, and persistent progression are the core pillars.

---

## 📚 Table of Contents

### 1. 🌍 World Building & Level Design
Defines the setting, maps, and environmental storytelling.
*   **[Map Design Overview](./GDD_Design/World/MapDesign.md)** - General philosophy and structure.
*   **[Map Layouts](./GDD_Design/World/MapLayouts.md)** - Points of Interest (POIs), hotspots, and tactical choke points.
*   **[Environmental Narrative](./GDD_Design/World/EnvironmentalNarrative.md)** - Lore integration into the map.
*   **[Loot Distribution](./GDD_Design/World/LootDistribution.md)** - Heatmaps and loot rarity zones.
*   **[Industrial Zone Design](./GDD_Design/World/MapDesign_IndustrialZone.md)** - Detailed spec for the first map.
*   **[Neon Slums Design](./GDD_Design/World/MapDesign_NeonSlums.md)** - Draft for the urban map.
*   **[Wilderness Design](./GDD_Design/World/MapDesign_Wilderness.md)** - Draft for the open area map.

### 2. 📖 Narrative & Lore
The story behind the collapse and the factions vying for control.
*   **[Backstory & Timeline](./GDD_Design/Story/Backstory.md)** - History of the world and The Collapse.
*   **[Factions](./GDD_Design/Story/Factions.md)** - Detailed breakdown of the 4 major groups.
*   **[Quest Lines](./GDD_Design/Story/QuestLines.md)** - Mission structure and types.
*   **[Narrative Overview](./GDD_Design/Story/Narrative.md)** - High-level story themes.

### 3. 🎨 Art Direction & Visuals
Guidelines for maintaining a consistent and high-quality visual style.
*   **[Art Direction Overview](./GDD_Design/Visuals/ArtDirection.md)** - Core visual pillars.
*   **[Style Guide (Art Bible)](./GDD_Design/Visuals/StyleGuide.md)** - Color palettes, lighting, and mood.
*   **[Asset Guidelines](./GDD_Design/Visuals/AssetGuidelines.md)** - Technical specs for 3D models and textures.
*   **[User Interface (UI)](./GDD_Design/Visuals/UserInterface.md)** - UI style and layout concepts.

### 4. 🔊 Audio Design
Sound strategy for immersion and tactical gameplay.
*   **[Sound Design Overview](./GDD_Design/Audio/SoundDesign.md)** - General philosophy.
*   **[Soundscape](./GDD_Design/Audio/Soundscape.md)** - Ambient audio and environmental effects.
*   **[Tactical Audio](./GDD_Design/Audio/TacticalAudio.md)** - Footsteps, weapons, and combat feedback.
*   **[Voice Lines](./GDD_Design/Audio/VoiceLines.md)** - Character dialogue and callouts.

### 5. ⚔️ Gameplay & Combat
Core mechanics, weapons, and combat systems.
*   **[Core Gameplay Loop](./GDD_Design/GameDesign/CoreGameplay.md)** - The cycle of Infiltrate -> Loot -> Extract.
*   **[Weapons](./GDD_Design/Combat/Weapons.md)** - List of firearms and melee weapons.
*   **[Items](./GDD_Design/Combat/Items.md)** - Consumables, grenades, and utility items.
*   **[Operators](./GDD_Design/Characters/Operators.md)** - Playable characters and classes.
*   **[Controls](./GDD_Design/GameDesign/Controls.md)** - Input schemes for Mobile/PC.

### 6. ⚙️ Systems & Economy
Metagame progression and technical systems.
*   **[Economy & Monetization](./GDD_Design/GameDesign/Economy.md)** - Currency, market, and store.
*   **[Progression](./GDD_Design/GameDesign/Progression.md)** - Leveling and unlocks.
*   **[Multiplayer Architecture](./GDD_Design/GameDesign/Multiplayer.md)** - Server/Client structure.
*   **[Localization](./GDD_Design/GameDesign/Localization.md)** - Language support plan.
*   **[Accessibility](./GDD_Design/GameDesign/Accessibility.md)** - Inclusive design features.

### 7. 📅 Project Management
Scope, risks, and planning documents.
*   **[MVP Scope](./GDD_Design/ProjectScope/MVP.md)** - Features for Alpha/Beta.
*   **[Risk Analysis](./GDD_Design/ProjectScope/Risks.md)** - Potential pitfalls and mitigation.
*   **[Non-Goals](./GDD_Design/ProjectScope/NonGoals.md)** - What we are NOT building.

---

## 🛠️ Recent Updates

*   **Audio:** Added full `Soundscape` and `Tactical Audio` documentation.
*   **Visuals:** Created `Style Guide` and `Asset Guidelines`.
*   **World:** Expanded `Map Layouts` and `Loot Distribution`.
*   **Scope:** Defined `MVP` features for upcoming milestones.

---

## 📝 Next Steps

1.  **Prototype Implementation:** Begin coding the core extraction loop based on `CoreGameplay.md`.
2.  **Map Greyboxing:** Start blocking out the Industrial Zone using `MapLayouts.md`.
3.  **Character Art:** Create first pass of the Assault operator using `AssetGuidelines.md`.
4.  **Audio Implementation:** Set up Wwise/FMOD project structure as per `SoundDesign.md`.

---

**[Contact & Contributors]**
*   Lead Designer: [Name]
*   Technical Lead: [Name]
