# Development Roadmap & TODO Tracking

**[← Previous: Performance Optimization](./08_PerformanceOptimization.md)** | **[Technical Index](./README.md)**

---

## Current Status

**Project Phase:** 🔴 **Pre-Development**  
**Current Sprint:** Sprint 0 - Project Setup  
**Team Size:** TBD  
**Start Date:** TBD  

---

## Phase 1: Core Development
**Duration:** Months 1-4  
**Status:** 🔴 Not Started (0%)

### Month 1-2: Foundation

#### Week 1-2: Project Setup
**Status:** 🔴 TODO

**Tasks:**
- [ ] Create UE5 project (mobile template)
- [ ] Setup version control (Git + LFS)
- [ ] Configure build pipeline
- [ ] Setup development environment docs
- [ ] Create coding standards document
- [ ] Initialize project structure

**Assignees:** TBD  
**Blockers:** None

---

#### Week 3-4: Core Character System
**Status:** 🔴 TODO

**Tasks:**
- [ ] Implement `AExtractionCharacter` base class
  - [ ] Basic movement (walk, sprint, crouch)
  - [ ] Health system integration
  - [ ] Stamina system
  - [ ] Death/respawn logic
  
- [ ] Create `UMobileInputComponent`
  - [ ] Virtual joystick for movement
  - [ ] Touch aim controls
  - [ ] Aim assist implementation
  - [ ] Button mapping

- [ ] Animation setup
  - [ ] Idle, walk, run animations
  - [ ] Crouch animations
  - [ ] Death animations

**Assignees:** TBD  
**Dependencies:** Project setup complete  
**Blockers:** None

---

#### Week 5-6: Basic Combat
**Status:** 🔴 TODO

**Tasks:**
- [ ] Implement `AExtractionWeapon` base class
  - [ ] Firing mechanics
  - [ ] Ammo system
  - [ ] Reload system
  - [ ] Weapon switching

- [ ] Create weapon types
  - [ ] Assault Rifle (prototype)
  - [ ] Pistol (prototype)
  
- [ ] Implement `UHealthComponent`
  - [ ] Health tracking
  - [ ] Armor system
  - [ ] Damage calculation
  - [ ] Death handling

- [ ] Hit detection
  - [ ] Line trace implementation
  - [ ] Hit validation
  - [ ] Damage application

**Assignees:** TBD  
**Dependencies:** Character system  
**Blockers:** None

---

#### Week 7-8: Network Foundation
**Status:** 🔴 TODO

**Tasks:**
- [ ] Setup dedicated server architecture
  - [ ] Server project configuration
  - [ ] Client-server separation
  - [ ] Connection handling

- [ ] Implement replication
  - [ ] Character replication
  - [ ] Movement prediction
  - [ ] Combat replication
  - [ ] Health/damage replication

- [ ] Create `AExtractionGameMode`
  - [ ] Match flow logic
  - [ ] Spawn management
  - [ ] Win conditions

- [ ] Create `AExtractionGameState`
  - [ ] Match timer
  - [ ] Player count tracking
  - [ ] Event management

**Assignees:** TBD  
**Dependencies:** Character + Combat  
**Blockers:** None

---

### Month 3-4: Core Systems

#### Week 9-10: Inventory System
**Status:** 🔴 TODO

**Tasks:**
- [ ] Implement `UInventoryComponent`
  - [ ] Grid-based inventory
  - [ ] Add/remove items
  - [ ] Weight system
  - [ ] Secure container

- [ ] Create item system
  - [ ] `FItemData` structure
  - [ ] Item database setup
  - [ ] Loot tables

- [ ] UI implementation
  - [ ] Inventory widget
  - [ ] Drag-and-drop
  - [ ] Item tooltips

**Assignees:** TBD  
**Dependencies:** Core character  
**Blockers:** None

---

#### Week 11-12: Loot System
**Status:** 🔴 TODO

**Tasks:**
- [ ] Create `ALootContainer` actor
  - [ ] Container interaction
  - [ ] Loot generation
  - [ ] Rarity system

- [ ] Implement loot distribution
  - [ ] Zone-based spawning
  - [ ] Rarity weighting
  - [ ] Dynamic loot tables

- [ ] Item pickup system
  - [ ] Ground items
  - [ ] Auto-pickup logic
  - [ ] Inventory integration

**Assignees:** TBD  
**Dependencies:** Inventory system  
**Blockers:** None

---

#### Week 13-14: AI System
**Status:** 🔴 TODO

**Tasks:**
- [ ] Implement `AExtractionAICharacter`
  - [ ] Inherit từ base character
  - [ ] AI-specific behaviors

- [ ] Create `AExtractionAIController`
  - [ ] Behavior tree setup
  - [ ] Blackboard configuration
  - [ ] Perception system

- [ ] AI behaviors
  - [ ] Patrol
  - [ ] Chase
  - [ ] Combat
  - [ ] Cover usage

**Assignees:** TBD  
**Dependencies:** Character + Combat  
**Blockers:** None

---

#### Week 15-16: Extraction & Match Flow
**Status:** 🔴 TODO

**Tasks:**
- [ ] Implement `AExtractionZone`
  - [ ] Zone activation
  - [ ] Extraction timer
  - [ ] Player tracking
  - [ ] Interruption logic

- [ ] Match flow implementation
  - [ ] Match start
  - [ ] Supply drops
  - [ ] Contamination system
  - [ ] Match end conditions

- [ ] Prototype map
  - [ ] Basic layout
  - [ ] Spawn points
  - [ ] Extraction zones
  - [ ] Loot locations

**Assignees:** TBD  
**Dependencies:** All core systems  
**Blockers:** None

**Milestone:** ✅ **Playable Prototype Complete**

---

## Phase 2: Content Creation
**Duration:** Months 5-7  
**Status:** 🔴 Not Started (0%)

### Month 5-6: Operators & Weapons

#### Week 17-20: Operator Implementation
**Status:** 🔴 TODO

**Tasks:**
- [ ] Implement 5 operator classes
  - [ ] Assault (Combat Stim)
  - [ ] Support (Healing Drone)
  - [ ] Recon (UAV Scan)
  - [ ] Tank (Riot Shield)
  - [ ] Specialist (EMP Blast)

- [ ] Operator ability system
  - [ ] Base ability class
  - [ ] Cooldown system
  - [ ] Effect implementation
  - [ ] Upgrades system

- [ ] Operator progression
  - [ ] Level system
  - [ ] XP tracking
  - [ ] Unlock system

**Assignees:** TBD  
**Dependencies:** Core character system  
**Blockers:** None

---

#### Week 21-24: Weapon Expansion
**Status:** 🔴 TODO

**Tasks:**
- [ ] Implement 15+ weapons across categories
  - [ ] Assault Rifles (3-4)
  - [ ] SMGs (3-4)
  - [ ] Shotguns (2-3)
  - [ ] Sniper Rifles (2-3)
  - [ ] Pistols (3-4)
  - [ ] Melee (2)

- [ ] Weapon stats balancing
  - [ ] Damage values
  - [ ] Fire rates
  - [ ] Recoil patterns
  - [ ] Effective ranges

- [ ] Weapon attachments (optional)
  - [ ] Scopes
  - [ ] Magazines
  - [ ] Grips

**Assignees:** TBD  
**Dependencies:** Base weapon system  
**Blockers:** None

---

### Month 7: Maps & UI

#### Week 25-28: Map Development
**Status:** 🔴 TODO

**Tasks:**
- [ ] Map 1: "Industrial Zone"
  - [ ] Layout design
  - [ ] Art pass
  - [ ] Loot placement
  - [ ] AI spawns
  - [ ] Extraction zones
  - [ ] Optimization

- [ ] Map 2: "Abandoned City"
  - [ ] Layout design
  - [ ] Art pass
  - [ ] Loot placement
  - [ ] AI spawns
  - [ ] Extraction zones
  - [ ] Optimization

**Assignees:** TBD  
**Dependencies:** Core systems  
**Blockers:** None

---

#### Week 29-30: UI/UX Implementation
**Status:** 🔴 TODO

**Tasks:**
- [ ] Main menu
  - [ ] Home screen
  - [ ] Operator selection
  - [ ] Loadout management
  - [ ] Settings

- [ ] In-game HUD
  - [ ] Health/armor bars
  - [ ] Minimap
  - [ ] Ammo counter
  - [ ] Virtual controls

- [ ] Post-match screens
  - [ ] Victory/defeat
  - [ ] Loot summary
  - [ ] XP breakdown

**Assignees:** TBD  
**Dependencies:** Core gameplay  
**Blockers:** None

---

#### Week 31-32: Matchmaking System
**Status:** 🔴 TODO

**Tasks:**
- [ ] Implement matchmaking backend
  - [ ] Queue system
  - [ ] MMR calculation
  - [ ] Team formation

- [ ] Server browser (optional)
  
- [ ] Party system
  - [ ] Invite friends
  - [ ] Squad formation
  - [ ] Voice chat integration (future)

**Assignees:** TBD  
**Dependencies:** Network system  
**Blockers:** Backend services

**Milestone:** ✅ **Alpha Build Complete**

---

## Phase 3: Testing & Refinement
**Duration:** Months 8-10  
**Status:** 🔴 Not Started (0%)

### Month 8: Closed Alpha

**Tasks:**
- [ ] Setup alpha testing infrastructure
- [ ] Recruit 50-100 testers
- [ ] Implement telemetry
- [ ] Bug tracking system
- [ ] Feedback collection

**Focus Areas:**
- Core gameplay loop
- Network stability
- Balance issues
- Critical bugs

---

### Month 9: Open Beta

**Tasks:**
- [ ] Public beta release
- [ ] Stress testing (1000+ players)
- [ ] Anti-cheat implementation
- [ ] Performance optimization
- [ ] Content additions based on feedback

**Focus Areas:**
- Server capacity
- Matchmaking quality
- Economy balance
- Monetization testing

---

### Month 10: Pre-Launch Polish

**Tasks:**
- [ ] Final bug fixes
- [ ] Performance optimization
- [ ] Content completion
- [ ] Store implementation
- [ ] Marketing materials
- [ ] Launch preparation

**Milestone:** ✅ **Release Candidate**

---

## Phase 4: Launch & Live Service
**Duration:** Month 11+  
**Status:** 🔴 Not Started

### Month 11: Soft Launch
- Limited region release
- Monitor metrics
- Quick iterations

### Month 12: Global Launch
- Worldwide release
- Marketing campaign
- Launch events

### Post-Launch: Live Operations
- Weekly balance patches
- Monthly content updates
- Seasonal events
- Battle Pass seasons

---

## Current Sprint (Sprint 0)

**Sprint Goal:** Project Setup & Planning

### Sprint Backlog

#### In Progress 🟡
*No tasks in progress*

#### To Do 🔴
- [ ] Finalize team structure
- [ ] Setup development machines
- [ ] Create project repository
- [ ] Write setup documentation

#### Done ✅
- [x] GDD documentation created
- [x] High-level design complete
- [x] Technical architecture planned

---

## Blocker Tracking

### Active Blockers 🚫
*No active blockers*

### Resolved Blockers
*None yet*

---

## Risk Register

| Risk                      | Probability | Impact | Mitigation                        | Owner       |
| ------------------------- | ----------- | ------ | --------------------------------- | ----------- |
| Mobile performance issues | High        | High   | Early profiling, scalable quality | Tech Lead   |
| Network latency           | Medium      | High   | Regional servers, lag comp        | Network Eng |
| Team resource shortage    | Medium      | High   | Phased hiring, outsourcing        | PM          |
| Scope creep               | Medium      | Medium | Strict prioritization             | PM          |
| Competitor launch         | Low         | Medium | Focus on unique features          | Design Lead |

---

## Metrics Tracking

### Development Metrics

**Code Quality:**
- Unit test coverage: Target 60%
- Build success rate: Target 95%+
- Code review turnaround: < 24 hours

**Velocity:**
- Story points per sprint: TBD (baseline)
- Bug resolution time: < 48 hours (critical)

**Performance:**
- Frame rate: 30 FPS minimum (mid-range)
- Memory usage: < 1GB (mid-range)
- APK size: < 2GB

---

## Team Capacity

### Current Allocation

| Role        | Team Members | Capacity |
| ----------- | ------------ | -------- |
| Programmers | TBD          | TBD      |
| Artists     | TBD          | TBD      |
| Designers   | TBD          | TBD      |
| QA          | TBD          | TBD      |

---

## Next Actions

### Immediate (This Week)
1. Finalize team hiring
2. Setup development infrastructure
3. Create project in UE5
4. First sprint planning

### Short-term (This Month)
1. Complete Phase 1 Week 1-2 tasks
2. Establish coding standards
3. Setup CI/CD pipeline
4. Begin core character implementation

### Long-term (This Quarter)
1. Complete Phase 1 (Core Development)
2. Playable prototype
3. Begin content creation

---

## Review Schedule

**Daily Standup:** 10:00 AM (15 minutes)
**Sprint Planning:** Every 2 weeks (Monday)
**Sprint Review:** Every 2 weeks (Friday)
**Sprint Retro:** Every 2 weeks (Friday)
**Milestone Reviews:** End of each phase

---

## Document Updates

| Date       | Version | Changes         | Author |
| ---------- | ------- | --------------- | ------ |
| 2026-02-06 | 1.0     | Initial roadmap | Team   |

---

**[← Previous: Performance Optimization](./08_PerformanceOptimization.md)** | **[Technical Index](./README.md)**
