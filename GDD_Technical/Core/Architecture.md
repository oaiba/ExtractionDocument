# System Architecture - Technical Design Document

**[← Technical Index](../README.md)** | **[Next: Networking →](./NetworkingSystem.md)**

---

## Overview

### Purpose

This document describes the **high-level architecture** of the Extraction game, including core classes, module organization, and design patterns.

### Design Goals

```
1. MAINTAINABLE - Clean separation of concerns
2. TESTABLE - Components independently testable
3. PERFORMANT - Strict budget for mobile devices
4. SCALABLE - Easy to add new features
5. SECURE - Server validates all actions
```

---

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                       EXTRACTION GAME                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    LAYER 0: CORE ENGINE                       │  │
│  │   Engine  │  CoreUObject  │  InputCore  │  NavigationSystem   │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                    ▲                                │
│  ┌─────────────────────────────────┴─────────────────────────────┐  │
│  │                  LAYER 1: GAME MODULES                        │  │
│  │   ┌────────────┐    ┌────────────┐    ┌────────────┐          │  │
│  │   │  GAMEPLAY  │    │  NETWORK   │    │   DATA     │          │  │
│  │   │  MODULE    │    │  MODULE    │    │  MODULE    │          │  │
│  │   └────────────┘    └────────────┘    └────────────┘          │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                    ▲                                │
│  ┌─────────────────────────────────┴─────────────────────────────┐  │
│  │                  LAYER 2: FEATURE MODULES                     │  │
│  │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │  │
│  │   │   AI     │  │   UI     │  │  AUDIO   │  │ EFFECTS  │      │  │
│  │   └──────────┘  └──────────┘  └──────────┘  └──────────┘      │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Enums & Types

### ModuleType

| Code Name     | Display Name | Layer | Dependencies   | Description                 |
| :------------ | :----------- | :---- | :------------- | :-------------------------- |
| `MT_Core`     | Core         | 0     | None           | Base engine modules         |
| `MT_Gameplay` | Gameplay     | 1     | Core           | Character, Weapons, Items   |
| `MT_Network`  | Network      | 1     | Core           | Replication, Matchmaking    |
| `MT_AI`       | AI           | 2     | Core, Gameplay | Controllers, Behavior Trees |
| `MT_UI`       | UI           | 2     | Core, Gameplay | Mobile-optimized widgets    |
| `MT_Audio`    | Audio        | 2     | Core           | Sound system, Music         |

### ActorCategory

| Code Name        | Display Name   | Pooled | Max Count | Update Rate |
| :--------------- | :------------- | :----- | :-------- | :---------- |
| `AC_Player`      | Player         | No     | 16        | 30 Hz       |
| `AC_AICharacter` | AI Character   | Yes    | 60        | 15 Hz       |
| `AC_Weapon`      | Weapon         | Yes    | 32        | 30 Hz       |
| `AC_Projectile`  | Projectile     | Yes    | 100       | 60 Hz       |
| `AC_Effect`      | Effect         | Yes    | 200       | 30 Hz       |
| `AC_Loot`        | Loot Container | No     | 300       | On-demand   |

### ComponentPriority

| Code Name     | Display Name | Tick Group     | Order | Description        |
| :------------ | :----------- | :------------- | :---- | :----------------- |
| `CP_Critical` | Critical     | PrePhysics     | 0     | Input, Health      |
| `CP_High`     | High         | DuringPhysics  | 100   | Movement, Combat   |
| `CP_Normal`   | Normal       | PostPhysics    | 200   | Animation, Effects |
| `CP_Low`      | Low          | PostUpdateWork | 300   | UI, Audio          |

### DesignPattern

| Code Name       | Display Name   | Use Case            | Example         |
| :-------------- | :------------- | :------------------ | :-------------- |
| `DP_Component`  | Component      | Feature composition | HealthComponent |
| `DP_DataDriven` | Data-Driven    | Balance, Config     | WeaponDataTable |
| `DP_ObjectPool` | Object Pooling | Performance         | Bullet pool     |
| `DP_Observer`   | Observer       | Events              | OnHealthChanged |
| `DP_Strategy`   | Strategy       | Abilities           | OperatorAbility |

---

## Code Names

### System Events

| Code Name      | Trigger         | Parameters         | Description         |
| :------------- | :-------------- | :----------------- | :------------------ |
| `SYS_INIT`     | System startup  | ModuleList         | Systems initialized |
| `SYS_SHUTDOWN` | System shutdown | Reason             | Clean shutdown      |
| `SYS_ERROR`    | Critical error  | ErrorCode, Message | Error occurred      |

### Memory Events

| Code Name            | Trigger           | Parameters         | Description  |
| :------------------- | :---------------- | :----------------- | :----------- |
| `MEM_POOL_CREATED`   | Pool initialized  | PoolType, Capacity | Pool created |
| `MEM_POOL_EXHAUSTED` | Pool depleted     | PoolType           | Pool empty   |
| `MEM_GC_SPIKE`       | GC spike detected | Duration, FreedMB  | GC spike     |

### Performance Events

| Code Name              | Trigger         | Parameters       | Description            |
| :--------------------- | :-------------- | :--------------- | :--------------------- |
| `PERF_BUDGET_EXCEEDED` | Budget exceeded | System, BudgetMs | Frame budget violation |
| `PERF_ACTOR_LIMIT`     | Actor limit     | ActorType, Count | Actor count warning    |

---

## Core Class Hierarchy

### Actor Classes

```
Actor (Engine Base)
├── GameModeBase
│   └── ExtractionGameMode
├── Character
│   └── ExtractionCharacter
│       ├── ExtractionPlayerCharacter
│       └── ExtractionAICharacter
├── Weapon
│   ├── RangedWeapon
│   └── MeleeWeapon
├── ItemBase
│   ├── PickupItem
│   └── LootContainer
└── ExtractionZone
```

### Component Classes

```
ActorComponent
├── HealthComponent      - HP, armor, damage
├── InventoryComponent   - Grid inventory
├── StaminaComponent     - Sprint resource
├── MobileInputComponent - Touch input
└── AIPerceptionComponent- Enemy detection
```

---

## Design Patterns

### 1. Component-Based Architecture

```
CLASS ExtractionCharacter:
    healthComponent: HealthComponent
    inventoryComponent: InventoryComponent
    staminaComponent: StaminaComponent
    
    FUNCTION Initialize():
        healthComponent = CreateComponent(HealthComponent)
        inventoryComponent = CreateComponent(InventoryComponent)
        staminaComponent = CreateComponent(StaminaComponent)
    END FUNCTION
```

### 2. Data-Driven Design

```
STRUCT WeaponTableRow:
    Damage: Float
    FireRate: Float
    MagazineSize: Integer
    RecoilPattern: RecoilPattern

CLASS WeaponDatabase:
    weaponTable: Map<String, WeaponTableRow>
    
    FUNCTION GetWeaponData(codeName: String) -> WeaponTableRow:
        RETURN weaponTable[codeName]
    END FUNCTION
```

### 3. Object Pooling

```
CLASS ObjectPoolSubsystem:
    pools: Map<ActorClass, List<Actor>>
    
    FUNCTION GetFromPool(actorClass: ActorClass) -> Actor:
        IF pools[actorClass].HasAvailable():
             actor = pools[actorClass].Pop()
             actor.Activate()
             RETURN actor
        ELSE:
             actor = SpawnNew(actorClass)
             RETURN actor
        END IF
    END FUNCTION
```

---

**[← Technical Index](./README.md)** | **[Next: Networking →](./NetworkingSystem.md)**
