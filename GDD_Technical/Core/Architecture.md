# System Architecture

**[← Technical Index](./README.md)** | **[Next: Networking →](./02_NetworkingSystem.md)**

---

## Overview

Tài liệu này mô tả high-level architecture của Extraction game, bao gồm core classes, module organization, và design patterns được sử dụng trong Unreal Engine 5 C++.

---

## Project Structure

```
ExtractionGame/
├── Source/
│   ├── ExtractionGame/
│   │   ├── Public/
│   │   │   ├── Core/
│   │   │   │   ├── ExtractionGameMode.h
│   │   │   │   ├── ExtractionGameState.h
│   │   │   │   ├── ExtractionPlayerController.h
│   │   │   │   └── ExtractionPlayerState.h
│   │   │   ├── Character/
│   │   │   │   ├── ExtractionCharacter.h
│   │   │   │   ├── ExtractionAICharacter.h
│   │   │   │   └── OperatorData.h
│   │   │   ├── Components/
│   │   │   │   ├── HealthComponent.h
│   │   │   │   ├── InventoryComponent.h
│   │   │   │   ├── StaminaComponent.h
│   │   │   │   └── MobileInputComponent.h
│   │   │   ├── Weapons/
│   │   │   │   ├── ExtractionWeapon.h
│   │   │   │   ├── RangedWeapon.h
│   │   │   │   ├── MeleeWeapon.h
│   │   │   │   └── WeaponData.h
│   │   │   ├── Items/
│   │   │   │   ├── ItemBase.h
│   │   │   │   ├── LootContainer.h
│   │   │   │   └── ItemData.h
│   │   │   ├── Systems/
│   │   │   │   ├── ExtractionZone.h
│   │   │   │   ├── ContaminationSystem.h
│   │   │   │   ├── SupplyDropSystem.h
│   │   │   │   └── MatchStateManager.h
│   │   │   ├── AI/
│   │   │   │   ├── ExtractionAIController.h
│   │   │   │   ├── AIPerceptionComponent.h
│   │   │   │   └── BehaviorTrees/
│   │   │   ├── Network/
│   │   │   │   ├── ExtractionNetworkManager.h
│   │   │   │   ├── ReplicationGraph.h
│   │   │   │   └── MatchmakingSubsystem.h
│   │   │   ├── UI/
│   │   │   │   ├── ExtractionHUD.h
│   │   │   │   ├── InventoryWidget.h
│   │   │   │   ├── VirtualJoystickWidget.h
│   │   │   │   └── ExtractionMenuWidget.h
│   │   │   └── Data/
│   │   │       ├── ItemDatabase.h
│   │   │       ├── WeaponDatabase.h
│   │   │       └── OperatorDatabase.h
│   │   └── Private/
│   │       └── (Implementations matching Public/)
│   └── ExtractionGame.Target.cs
├── Content/
│   ├── Blueprints/
│   │   ├── UI/ (UI Widgets only)
│   │   └── GameModes/ (Minimal, inherit từ C++)
│   ├── Characters/
│   │   ├── Operators/
│   │   └── AI/
│   ├── Weapons/
│   ├── Items/
│   ├── Maps/
│   │   ├── Menus/
│   │   └── GameMaps/
│   ├── UI/
│   │   ├── Textures/
│   │   ├── Fonts/
│   │   └── Widgets/
│   ├── Audio/
│   │   ├── SFX/
│   │   ├── Music/
│   │   └── VO/
│   └── VFX/
├── Config/
│   ├── DefaultEngine.ini
│   ├── DefaultGame.ini
│   └── DefaultInput.ini
└── Plugins/ (Third-party và custom plugins)
```

---

## Core Class Hierarchy

### Actor Classes

```cpp
AActor (Unreal Base)
│
├── AGameModeBase
│   └── AExtractionGameMode
│
├── ACharacter
│   └── AExtractionCharacter (Base character)
│       ├── AExtractionPlayerCharacter
│       └── AExtractionAICharacter
│
├── AWeapon (Base weapon actor)
│   ├── ARangedWeapon
│   │   ├── AAssaultRifle
│   │   ├── ASMG
│   │   ├── ASniperRifle
│   │   └── AShotgun
│   └── AMeleeWeapon
│
├── AItemBase
│   ├── APickupItem
│   └── ALootContainer
│
├── AExtractionZone
│
└── ASupplyDrop
```

### Component Classes

```cpp
UActorComponent (Unreal Base)
│
├── UHealthComponent
│   - Manages health, armor, damage
│   - Replication: DOREPLIFETIME
│
├── UInventoryComponent
│   - Grid-based inventory
│   - Replication: Owner only
│
├── UStaminaComponent
│   - Sprint, dodge stamina
│   - Replication: Owner only
│
├── UMobileInputComponent
│   - Touch input handling
│   - Aim assist
│   - No replication (client-side)
│
└── UAIPerceptionComponent (Enhanced)
    - Enemy detection
    - Audio/visual sensing
```

### Core Framework Classes

```cpp
// Game Mode (Server only)
AExtractionGameMode
├── Manages match flow
├── Spawn management
├── Win conditions
└── Server authoritative logic

// Game State (Replicated to all)
AExtractionGameState
├── Match time
├── Player count
├── Extraction zones
├── Dynamic events
└── Contamination data

// Player Controller (One per player)
AExtractionPlayerController
├── Input handling
├── Camera control
├── UI management
└── Client-server RPC

// Player State (Replicated player data)
AExtractionPlayerState
├── Player stats
├── Kill/death counts
├── Operator selection
└── Match progress

// HUD (Client UI)
AExtractionHUD
├── Health bar
├── Minimap
├── Inventory
└── Virtual controls
```

---

## Module Dependencies

```
ExtractionGame
│
├── Core Modules (UE5)
│   ├── Engine
│   ├── CoreUObject
│   ├── InputCore
│   ├── AIModule
│   ├── NavigationSystem
│   ├── UMG (UI)
│   └── OnlineSubsystem
│
├── Custom Modules
│   ├── ExtractionCore (Character, Weapons, Items)
│   ├── ExtractionNetwork (Replication, Matchmaking)
│   ├── ExtractionAI (AI Controllers, Behavior Trees)
│   └── ExtractionUI (Mobile-optimized widgets)
│
└── Third-party Plugins (Future)
    ├── Anti-Cheat SDK
    ├── Analytics Plugin
    └── Crash Reporter
```

---

## Design Patterns

### 1. Component-Based Architecture

**Why:** Modular, reusable, testable

**Implementation:**
```cpp
// Character composed từ components
AExtractionCharacter::AExtractionCharacter()
{
    // Create components
    HealthComponent = CreateDefaultSubobject<UHealthComponent>(TEXT("Health"));
    InventoryComponent = CreateDefaultSubobject<UInventoryComponent>(TEXT("Inventory"));
    StaminaComponent = CreateDefaultSubobject<UStaminaComponent>(TEXT("Stamina"));
    
    // Components có thể reuse ở AI characters, vehicles, etc
}
```

**Benefits:**
- Easy to add/remove features
- Components testable independently
- Reduced code duplication

### 2. Data-Driven Design

**Why:** Balance changes không cần recompile, designer-friendly

**Implementation:**
```cpp
// Data tables cho weapons
USTRUCT(BlueprintType)
struct FWeaponTableRow : public FTableRowBase
{
    GENERATED_BODY()
    
    UPROPERTY(EditAnywhere)
    float Damage;
    
    UPROPERTY(EditAnywhere)
    float FireRate;
    
    UPROPERTY(EditAnywhere)
    int32 MagazineSize;
    
    // ... more stats
};

// Load từ DataTable
UDataTable* WeaponTable = LoadObject<UDataTable>(...);
FWeaponTableRow* WeaponData = WeaponTable->FindRow<FWeaponTableRow>(...);
```

**Benefits:**
- Designers can balance without programming
- Easy A/B testing
- Quick iterations

### 3. Object Pooling

**Why:** Mobile performance, reduce GC overhead

**Implementation:**
```cpp
// Pool cho bullets, effects, etc
class UObjectPoolSubsystem : public UGameInstanceSubsystem
{
    TMap<UClass*, TArray<AActor*>> PooledObjects;
    
    AActor* GetFromPool(UClass* Class);
    void ReturnToPool(AActor* Actor);
};

// Usage
ABullet* Bullet = PoolSubsystem->GetFromPool(ABullet::StaticClass());
// Use bullet
PoolSubsystem->ReturnToPool(Bullet);
```

**Benefits:**
- Reduced memory allocation
- Fewer GC spikes
- Consistent frame rates

### 4. Observer Pattern (Events)

**Why:** Decouple systems, flexible event handling

**Implementation:**
```cpp
// Health component notifies listeners
DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(
    FOnHealthChanged, float, NewHealth, float, Delta);

class UHealthComponent : public UActorComponent
{
public:
    UPROPERTY(BlueprintAssignable)
    FOnHealthChanged OnHealthChanged;
    
    void TakeDamage(float Amount)
    {
        Health -= Amount;
        OnHealthChanged.Broadcast(Health, -Amount);
    }
};

// Listeners bind
HealthComp->OnHealthChanged.AddDynamic(this, &AExtractionCharacter::OnHealthChanged);
```

**Benefits:**
- Loose coupling
- Easy to add new listeners
- Clear event flow

### 5. Strategy Pattern (Operator Abilities)

**Why:** Easy to add new operators, swap abilities

**Implementation:**
```cpp
// Base ability interface
UCLASS(Abstract)
class UOperatorAbility : public UObject
{
public:
    virtual void Activate() PURE_VIRTUAL(UOperatorAbility::Activate, );
    virtual bool CanActivate() PURE_VIRTUAL(UOperatorAbility::CanActivate, return false;);
};

// Specific abilities
class UCombatStimAbility : public UOperatorAbility { ... };
class UHealingDroneAbility : public UOperatorAbility { ... };

// Operator holds ability
UPROPERTY()
UOperatorAbility* CurrentAbility;

// Swap at runtime
CurrentAbility = NewObject<UCombatStimAbility>();
```

**Benefits:**
- Easy to add operators
- Testable abilities
- Runtime ability swapping (future)

---

## Memory Management

### Garbage Collection

**UPROPERTY Best Practices:**
```cpp
// ALWAYS use UPROPERTY for UObject pointers
UPROPERTY()
UInventoryComponent* InventoryComp; // GC managed

// Raw pointers OK for non-UObjects
float* SomeData; // Manual management needed

// TWeakObjectPtr for non-owning references
TWeakObjectPtr<AActor> CachedTarget; // Won't prevent GC
```

### Smart Pointers

```cpp
// For non-UObject memory
TSharedPtr<FLargeData> SharedData; // Reference counted
TUniquePtr<FTempData> UniqueData; // Exclusive ownership
TWeakPtr<FData> WeakData; // Non-owning reference
```

---

## Replication Architecture

**Server Authority Model:**
- Server makes all decisions
- Clients send input
- Server validates và broadcasts results

```cpp
// Example: Character movement
// Client: Predict movement locally
void AExtractionCharacter::MoveForward(float Value)
{
    // Client-side prediction
    AddMovementInput(GetActorForwardVector(), Value);
    
    // Send to server
    if (!HasAuthority())
    {
        ServerMoveForward(Value);
    }
}

// Server: Validate và replicate
UFUNCTION(Server, Reliable, WithValidation)
void AExtractionCharacter::ServerMoveForward_Implementation(float Value)
{
    // Validate (anti-cheat)
    if (FMath::Abs(Value) > 1.0f) return;
    
    // Execute
    AddMovementInput(GetActorForwardVector(), Value);
}

bool AExtractionCharacter::ServerMoveForward_Validate(float Value)
{
    return FMath::Abs(Value) <= 1.0f;
}
```

**Replication Frequency:**
- Critical (Movement, Health): 30 Hz
- Standard (Inventory, Ammo): 10 Hz
- Low (Cosmetics): On-change only

---

## Performance Targets

### Actor Count Budgets

| Actor Type       | Max Count | Notes              |
| ---------------- | --------- | ------------------ |
| Players          | 16        | Networking limit   |
| AI Characters    | 60        | Balanced spawning  |
| Weapons (active) | 32        | Dropped + equipped |
| Projectiles      | 100       | Pooled             |
| Effects          | 200       | Pooled             |
| Loot Containers  | 300       | Static             |

### Frame Budget (30 FPS = 33.3ms)

| System         | Budget | %   |
| -------------- | ------ | --- |
| Gameplay Logic | 8 ms   | 24% |
| Rendering      | 15 ms  | 45% |
| Physics        | 4 ms   | 12% |
| AI             | 3 ms   | 9%  |
| Audio          | 2 ms   | 6%  |
| Other          | 1.3 ms | 4%  |

---

## TODO: Architecture Tasks

### HIGH Priority 🔴
- [ ] Setup base project structure
- [ ] Implement core classes (GameMode, Character, etc)
- [ ] Create component architecture
- [ ] Setup replication framework

### MEDIUM Priority 🟡
- [ ] Data table integration
- [ ] Object pooling system
- [ ] Event system implementation
- [ ] Performance profiling setup

### LOW Priority 🟢
- [ ] Plugin architecture
- [ ] Advanced optimization
- [ ] Modding support planning

---

## Next Steps

**For Programmers:**
1. Read [Networking System](./02_NetworkingSystem.md) để hiểu multiplayer architecture
2. Read [Character System](./03_CharacterSystem.md) để implement player controller
3. Setup development environment theo [Development Roadmap](./09_DevelopmentRoadmap.md)

**Related Documents:**
- [High-Level GDD](../GDD_HighLevel/README.md) - Game design context
- [Networking System](./02_NetworkingSystem.md) - Multiplayer details
- [Performance Optimization](./08_PerformanceOptimization.md) - Optimization techniques

---

**[← Technical Index](./README.md)** | **[Next: Networking →](./02_NetworkingSystem.md)**
