---
title: "Unreal Engine Skills"
type: docs
weight: 1
---

## 🧠 Unreal Engine 5 Skills for AI Agents

This document covers essential UE5 patterns, frameworks, and best practices that agents must understand and apply correctly.

---

### 🎮 Gameplay Ability System (GAS)

GAS is the preferred framework for abilities, effects, and attribute management.

**Core Components:**

| Component | Class | Purpose |
|:----------|:------|:--------|
| Ability System Component | `UAbilitySystemComponent` | Manages abilities, effects, tags |
| Gameplay Ability | `UGameplayAbility` | Defines a single ability |
| Gameplay Effect | `UGameplayEffect` | Modifies attributes (damage, buffs) |
| Attribute Set | `UAttributeSet` | Defines character stats (Health, Stamina) |
| Gameplay Cue | `UGameplayCueNotify` | Visual/audio feedback for effects |

**Naming:**
```cpp
// Abilities
UGA_Dash            // Gameplay Ability — Dash
UGA_Heal            // Gameplay Ability — Heal
UGA_ThrowGrenade    // Gameplay Ability — Throw Grenade

// Effects
UGE_DamageInstant   // Gameplay Effect — Instant damage
UGE_HealOverTime    // Gameplay Effect — Heal over time
UGE_SpeedBuff       // Gameplay Effect — Speed buff

// Attribute Sets
UAS_Combat          // Attribute Set — Combat attributes
UAS_Survival        // Attribute Set — Survival attributes
```

**Key Rules:**
- Use GAS for any combat ability, buff/debuff, or stat modification
- Never modify attributes directly — always go through `UGameplayEffect`
- Use Gameplay Tags to manage states (e.g., `State.Character.Stunned`)
- Use Gameplay Cues for client-side VFX/SFX (they replicate automatically)

---

### 🎯 Enhanced Input System

Use Enhanced Input (not the legacy system) for all player input:

```cpp
// Input Action assets: IA_Fire, IA_Reload, IA_Interact
// Input Mapping Context assets: IMC_OnFoot, IMC_Vehicle, IMC_Menu

// In Character/Controller setup:
void AExtractionPlayerController::SetupInputComponent()
{
    Super::SetupInputComponent();
    
    if (UEnhancedInputComponent* EnhancedInput = Cast<UEnhancedInputComponent>(InputComponent))
    {
        EnhancedInput->BindAction(IA_Fire, ETriggerEvent::Started, this, &ThisClass::OnFireStarted);
        EnhancedInput->BindAction(IA_Fire, ETriggerEvent::Completed, this, &ThisClass::OnFireStopped);
        EnhancedInput->BindAction(IA_Reload, ETriggerEvent::Triggered, this, &ThisClass::OnReload);
    }
}
```

**Rules:**
- One `UInputAction` per action (not per key)
- Use `ETriggerEvent::Started` for one-shot actions
- Use `ETriggerEvent::Triggered` for continuous actions
- Switch `UInputMappingContext` for different gameplay states

---

### 🌐 Replication & Networking

#### Property Replication

```cpp
// Header
UPROPERTY(ReplicatedUsing = OnRep_Health)
float Health;

UFUNCTION()
void OnRep_Health();

// Source
void AMyCharacter::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    
    DOREPLIFETIME(AMyCharacter, Health);
    // Or with conditions:
    DOREPLIFETIME_CONDITION(AMyCharacter, Ammo, COND_OwnerOnly);
}
```

#### RPC Pattern

```cpp
// Client wants to perform action → call Server RPC
UFUNCTION(Server, Reliable, WithValidation)
void Server_RequestFire();

bool AMyCharacter::Server_RequestFire_Validate()
{
    return bCanFire; // Server validates
}

void AMyCharacter::Server_RequestFire_Implementation()
{
    // Server executes authoritative logic
    PerformFire();
    
    // Notify all clients
    Multicast_OnFired();
}

UFUNCTION(NetMulticast, Unreliable)
void Multicast_OnFired();
```

**Rules:**
- Server is **authoritative** — never trust client data
- Use `WithValidation` on Server RPCs
- Use `Reliable` for important state changes, `Unreliable` for cosmetic
- Minimize replicated data — only what clients need

---

### 🖥️ UMG (UI Framework)

```cpp
// Widget Classes
UCLASS()
class UExtractionHealthBar : public UUserWidget
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category = "UI")
    void SetHealthPercent(float Percent);

protected:
    virtual void NativeConstruct() override;
    
    UPROPERTY(meta = (BindWidget))
    TObjectPtr<UProgressBar> HealthBar;
    
    UPROPERTY(meta = (BindWidget))
    TObjectPtr<UTextBlock> HealthText;
};
```

**Rules:**
- Use `meta = (BindWidget)` to bind to named widgets in the Blueprint
- Override `NativeConstruct()` instead of `BeginPlay()` for widgets
- Use `meta = (BindWidgetOptional)` for optional UI elements
- Widget names in C++ must exactly match the widget names in the Blueprint

---

### 📦 Subsystem Pattern

Use subsystems for global managers that don't need to be Actors:

```cpp
// Game Instance Subsystem — persists across levels
UCLASS()
class UInventorySubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()
    // Manages persistent player inventory
};

// World Subsystem — per-level
UCLASS()
class UExtractionSubsystem : public UWorldSubsystem
{
    GENERATED_BODY()
    // Manages extraction zones for the current map
};

// Local Player Subsystem — per-player
UCLASS()
class USettingsSubsystem : public ULocalPlayerSubsystem
{
    GENERATED_BODY()
    // Manages player settings
};

// Access anywhere:
UInventorySubsystem* Inv = GetGameInstance()->GetSubsystem<UInventorySubsystem>();
UExtractionSubsystem* Ext = GetWorld()->GetSubsystem<UExtractionSubsystem>();
```

**When to use each:**

| Subsystem Type | Lifetime | Use For |
|:---------------|:---------|:--------|
| `UGameInstanceSubsystem` | Entire game session | Persistent data, global managers |
| `UWorldSubsystem` | Current level | Level-specific systems |
| `ULocalPlayerSubsystem` | Per local player | Player-specific settings, UI state |
| `UEngineSubsystem` | Engine lifetime | Engine-level utilities |

---

### 📋 Data-Driven Design

Prefer Data Assets and Data Tables over hardcoded values:

```cpp
// Data Asset
UCLASS()
class UWeaponDataAsset : public UPrimaryDataAsset
{
    GENERATED_BODY()
    
public:
    UPROPERTY(EditDefaultsOnly, Category = "Weapon|Identity")
    FText DisplayName;
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon|Stats")
    float BaseDamage = 25.f;
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon|Stats")
    float FireRate = 600.f; // Rounds per minute
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon|Assets")
    TSoftObjectPtr<USkeletalMesh> WeaponMesh;
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon|Assets")
    TSoftClassPtr<AProjectile> ProjectileClass;
};
```

**Rules:**
- Use `UPrimaryDataAsset` for assets loaded by the Asset Manager
- Use `TSoftObjectPtr<>` and `TSoftClassPtr<>` for lazy-loaded references
- Use `UDataTable` for large collections (item databases, loot tables)
- Never hardcode stats — always expose via `UPROPERTY(EditDefaultsOnly)`

---

### 📚 Key UE5 Documentation Links

| Topic | URL |
|:------|:----|
| Gameplay Ability System | [docs.unrealengine.com/GAS](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine) |
| Enhanced Input | [docs.unrealengine.com/EnhancedInput](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine) |
| Network Replication | [docs.unrealengine.com/Networking](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine) |
| UMG Framework | [docs.unrealengine.com/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-for-unreal-engine) |
| Subsystems | [docs.unrealengine.com/Subsystems](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-subsystems-in-unreal-engine) |
| Lyra Sample Game | [docs.unrealengine.com/Lyra](https://docs.unrealengine.com/5.0/en-US/lyra-sample-game-in-unreal-engine/) |
