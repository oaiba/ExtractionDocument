---
title: "Source References"
type: docs
weight: 1
---

## Knowledge Source References

This document organizes all key reference materials, documentation links, and learning resources for AI agents and developers working on this project.

---

### Project-Internal Documentation (Read First)

| Document | Path | Priority |
|:---------|:-----|:---------|
| **Coding & Asset Standards** | [GDD_Technical/CodingStandards.md](../../GDD_Technical/CodingStandards.md) | CRITICAL |
| **Code Generation Rules** | [GDD_Agents/Rules/CodeGeneration.md](../Rules/CodeGeneration.md) | CRITICAL |
| **Documentation Standards** | [GDD_Agents/Rules/DocumentationStandards.md](../Rules/DocumentationStandards.md) | CRITICAL |
| **GDD Technical Index** | [GDD_Technical/_index.md](../../GDD_Technical/_index.md) | HIGH |
| **GDD Design Index** | [GDD_Design/_index.md](../../GDD_Design/_index.md) | HIGH |
| **Feature Workflow** | [GDD_Agents/Workflows/FeatureImplementation.md](../Workflows/FeatureImplementation.md) | HIGH |
| **UE5 Skills** | [GDD_Agents/Skills/UnrealEngine.md](../Skills/UnrealEngine.md) | HIGH |

---

### Official Unreal Engine Documentation

#### Core Standards & Conventions

| Resource | URL |
|:---------|:----|
| Epic C++ Coding Standard | [dev.epicgames.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine) |
| Recommended Asset Naming | [dev.epicgames.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects) |
| Allar's UE5 Style Guide v2 | [github.com/Allar](https://github.com/Allar/ue5-style-guide/tree/v2) |
| Unreal Directive — Asset Naming | [unrealdirective.com](https://unrealdirective.com/resources/asset-naming-conventions) |

#### Key Engine Systems

| System | URL |
|:-------|:----|
| Gameplay Ability System (GAS) | [dev.epicgames.com/GAS](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine) |
| Enhanced Input System | [dev.epicgames.com/Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine) |
| Networking & Multiplayer | [dev.epicgames.com/Networking](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine) |
| UMG UI Framework | [dev.epicgames.com/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-for-unreal-engine) |
| Subsystems | [dev.epicgames.com/Subsystems](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-subsystems-in-unreal-engine) |
| Gameplay Tags | [dev.epicgames.com/Tags](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-gameplay-tags-in-unreal-engine) |
| Data Assets | [dev.epicgames.com/DataAssets](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine) |
| Actor Lifecycle | [dev.epicgames.com/Lifecycle](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-actor-lifecycle) |

#### Reference Projects

| Project | URL | Notes |
|:--------|:----|:------|
| Lyra Starter Game | [docs.unrealengine.com/Lyra](https://docs.unrealengine.com/5.0/en-US/lyra-sample-game-in-unreal-engine/) | Essential study for multiplayer shooter architecture |
| Valley of the Ancient | [dev.epicgames.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/valley-of-the-ancient-sample-game-for-unreal-engine) | Open-world streaming and Nanite reference |

---

### Game Design References

#### UI/UX Design

| Resource | URL | Use For |
|:---------|:----|:--------|
| Game UI Database | [gameuidatabase.com](https://www.gameuidatabase.com/index.php) | HUD, inventory, menu reference |
| Laws of UX | [lawsofux.com](https://lawsofux.com/) | UX design principles |

#### Game Design & Mechanics

| Resource | URL | Use For |
|:---------|:----|:--------|
| Game Developer (Gamasutra) | [gamedeveloper.com](https://www.gamedeveloper.com/design) | Design theory and postmortems |
| FPS Design Patterns | [gamedesigning.org](https://www.gamedesigning.org/learn/fps-game-design/) | FPS mechanics and level design |
| GDC Vault | [gdcvault.com](https://gdcvault.com/) | Industry talks and presentations |

#### Economy & Progression

| Resource | URL | Use For |
|:---------|:----|:--------|
| Machinations.io | [machinations.io](https://machinations.io/) | Game economy modeling |
| Deconstructor of Fun | [deconstructoroffun.com](https://www.deconstructoroffun.com/) | F2P and economy analysis |

#### Level Design

| Resource | URL | Use For |
|:---------|:----|:--------|
| Level Design Book | [book.leveldesign.io](https://book.leveldesign.io/) | LD theory and practice |
| World of Level Design | [worldofleveldesign.com](https://www.worldofleveldesign.com/) | UE tutorials and LD articles |

#### Audio Design

| Resource | URL | Use For |
|:---------|:----|:--------|
| Sonniss GDC Bundles | [sonniss.com](https://sonniss.com/gameaudio-gdc-bundle-archive) | Free high-quality SFX |
| GDC Vault — Audio | [gdcvault.com/Audio](https://gdcvault.com/browse/track/Audio) | Audio design talks |

---

### Extraction Shooter References

Games studied for design inspiration:

| Game | Key Systems Studied | Relevance |
|:-----|:--------------------|:----------|
| **Escape from Tarkov** | Karma (Scav/PMC), Hideout, VOIP, co-op extracts, inventory grid | Primary reference for core loop |
| **Hunt: Showdown** | MMR/SBMM (star rating), squad balancing, bounty extraction | Primary reference for matchmaking |
| **DMZ (Warzone)** | LFG culture, faction missions, casual extraction loop | Reference for accessibility |
| **Dark and Darker** | Emotes/gestures, dungeon social dynamics | Reference for social systems |
| **The Finals** | Cross-platform parties, emote wheel, destruction | Reference for UX polish |
| **ARC Raiders** | Social hub, team synergy | Reference for co-op design |
| **Arena Breakout** | After action report, mobile extraction shooter | Reference for post-match flow |

---

### Development Tools

| Tool | URL | Use For |
|:-----|:----|:--------|
| Visual Studio 2022 | [visualstudio.microsoft.com](https://visualstudio.microsoft.com/) | Primary IDE for UE5 C++ |
| JetBrains Rider | [jetbrains.com/rider](https://www.jetbrains.com/rider/) | Alternative IDE (better refactoring) |
| Perforce (P4V) | [perforce.com](https://www.perforce.com/) | Alternative VCS for large projects |
| Git LFS | [git-lfs.github.com](https://git-lfs.github.com/) | Large file storage for assets |
| RenderDoc | [renderdoc.org](https://renderdoc.org/) | GPU debugging and profiling |
| Unreal Insights | Built into UE5 | CPU/GPU/Network profiling |
