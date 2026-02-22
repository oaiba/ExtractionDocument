---
# title: "Extraction Shooter GDD"
type: docs
sidebar:
  hide: true
---

<div style="text-align: center;">

```
███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║
███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

**MASTER DOCUMENTATION PORTAL**

**[👉 Go to GDD Task Tracker](/ExtractionDocument/tracker/tasks/gdd_tasktracker/)**

</div>

---

This is the central repository and gateway for all documentation related to the **Extraction Shooter** project. It serves as the single source of truth for both the creative vision and the technical implementation of our top-down, high-stakes tactical experience.

---

## Project Snapshot

{{< cards cols="3" >}}
  {{< card title="Engine" icon="server" subtitle="Unreal Engine 5 (C++)" >}}
  {{< card title="Platform" icon="device-mobile" subtitle="Mobile (iOS/Android) + PC" >}}
  {{< card title="Genre" icon="fire" subtitle="Top-down Extraction Shooter" >}}
{{< /cards >}}

**Current Phase:** Pre-Production / Core Prototyping

---

## Documentation Hubs

Access the specialized documentation portals based on your role and current task.

{{< cards cols="2" >}}
  {{< card link="/ExtractionDocument/gdd_design/" title="Design & Creative Hub" icon="sparkles" subtitle="Player experience, world-building, visual/audio aesthetics, and narrative." >}}
  {{< card link="/ExtractionDocument/gdd_technical/" title="Technical & Engineering Hub" icon="terminal" subtitle="Implementation specs, systems architecture, networking, and performance." >}}
{{< /cards >}}

{{< cards cols="2" >}}
  {{< card link="/ExtractionDocument/tracker/tasks/gdd_tasktracker/" title="Task Tracker" icon="clipboard-list" subtitle="Comprehensive project-wide task tracking and milestones." >}}
  {{< card link="/ExtractionDocument/gdd_agents/" title="AI Agent Guidelines" icon="chip" subtitle="Rules, workflows, and skills for AI coding agents (Gemini, Copilot, Cursor)." >}}
{{< /cards >}}

---

## Quick Start by Role

### 🎨 For Design & Art Teams

- **Single Source of Truth**: Always refer to the [Design Hub](/GDD_Design/) before starting creative work
- **Visual Consistency**: Follow the [Style Guide](/GDD_Design/Visuals/StyleGuide) for cross-platform fidelity
- **Core Loop**: Keep the [Core Gameplay](/GDD_Design/GameDesign/CoreGameplay) aligned with mechanic changes
- **Asset Submission**: Use [Asset Guidelines](/GDD_Design/Visuals/AssetGuidelines) for UE5 specs

### 💻 For Technical & Dev Teams

- **Implementation Specs**: All enums, codenames, and interfaces are in the [Technical Hub](/GDD_Technical/)
- **Performance First**: Adhere to [Performance Budgets](/GDD_Technical/Performance/Optimization)
- **Task Management**: Follow the [Development Roadmap](/GDD_Technical/Core/DevelopmentRoadmap)
- **Code Standards**: Maintain modularity per [Architecture](/GDD_Technical/Core/Architecture) docs

---

## Project Scope & Progress

{{< cards cols="3" >}}
  {{< card link="/GDD_Design/ProjectScope/MVP" title="MVP Definition" icon="flag" subtitle="Minimum Viable Product features and scope boundaries." >}}
  {{< card link="/GDD_Design/ProjectScope/NonGoals" title="Non-Goals" icon="x-circle" subtitle="Features explicitly out of current scope." >}}
  {{< card link="/GDD_Design/ProjectScope/Risks" title="Risk Assessment" icon="exclamation-circle" subtitle="Known challenges and mitigation strategies." >}}
{{< /cards >}}

### Recent Milestones

{{< cards cols="3" >}}
  {{< card title="Audio Architecture" icon="volume-up" subtitle="Completed Soundscape and Tactical Audio definitions" >}}
  {{< card title="Visual Direction" icon="photograph" subtitle="Finalized Art Bible and Mobile Performance Budgets" >}}
  {{< card title="Map System" icon="map" subtitle="Expanded Industrial Zone hotspots and loot heatmaps" >}}
{{< /cards >}}

---

## Quick Navigation

### New to the Project?
1. **Read the [MVP Scope](/GDD_Design/ProjectScope/MVP)** to understand the current focus
2. **Explore the [Core Loop](/GDD_Design/GameDesign/CoreGameplay)** to grasp the game's heartbeat
3. **Review the [Technical Roadmap](/GDD_Technical/Core/DevelopmentRoadmap)** if you are contributing code

### Key Systems Documentation
- **Task Tracker** → [GDD Task Tracker](/ExtractionDocument/tracker/tasks/gdd_tasktracker/)
- **World & Maps** → [Map Design](/GDD_Design/World/MapDesign)
- **Combat & Weapons** → [Weapon System](/GDD_Technical/Gameplay/WeaponSystem)
- **Inventory & Loot** → [Inventory System](/GDD_Technical/Gameplay/InventorySystem)
- **Networking** → [Networking System](/GDD_Technical/Core/NetworkingSystem)
- **AI Behavior** → [AI System](/GDD_Technical/Systems/AISystem)

---

<div style="text-align: center; color: #888; font-size: 0.9em;">

*Last Updated: February 13, 2026*  
*Lead Designer: [Name] | Technical Lead: [Name]*

</div>
