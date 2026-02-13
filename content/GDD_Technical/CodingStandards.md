---
title: "Coding & Asset Standards"
type: docs
weight: 1
---

## 📋 Overview

This document defines the **mandatory standards** for all C++ code, Blueprints, assets, and project structure in our Unreal Engine 5 project. Following these standards ensures:

- **Consistency** — Code and assets look like one person created them
- **Scalability** — Easy to extend with plugins, modules, and submodules
- **Team Collaboration** — Clear conventions prevent merge conflicts and confusion
- **Optimization** — Structured content enables cooking, streaming, and bundling efficiency

> **Authoritative Sources:**
> - [Epic C++ Coding Standard](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine)
> - [Epic Recommended Asset Naming Conventions](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects)
> - [Allar's UE5 Style Guide v2](https://github.com/Allar/ue5-style-guide/tree/v2)
> - [Unreal Directive — Asset Naming](https://unrealdirective.com/resources/asset-naming-conventions)

---

## 🏗️ Project Architecture

### Module & Plugin Strategy

Our project is organized into **Gameplay Modules** and **Engine Plugins** to enforce separation of concerns and enable independent iteration.

```
ExtractionGame/
├── Source/
│   ├── ExtractionCore/          ← Core module (shared types, interfaces)
│   ├── ExtractionGameplay/      ← Main gameplay module
│   ├── ExtractionUI/            ← UI/UMG widgets module
│   ├── ExtractionAI/            ← AI behavior & perception module
│   └── ExtractionEditor/        ← Editor-only tools module
│
├── Plugins/
│   ├── ExtractionInventory/     ← Inventory & item system plugin
│   ├── ExtractionWeapons/       ← Weapon mechanics plugin
│   ├── ExtractionSocial/        ← Social, clan, VOIP plugin
│   ├── ExtractionProgression/   ← XP, quests, battle pass plugin
│   └── ThirdParty/              ← External SDK integrations
│       ├── EOS/                  ← Epic Online Services
│       └── Vivox/                ← Voice chat SDK
│
├── Content/                      ← UE5 Content (Assets)
├── Config/                       ← Configuration files
└── Build/                        ← Build scripts & CI configs
```

<!-- 📸 IMAGE PLACEHOLDER: Architecture diagram showing module dependencies and plugin boundaries -->

### Module Dependency Rules

| Rule | Description |
|:-----|:------------|
| **Core is standalone** | `ExtractionCore` depends on nothing project-specific. Only Engine modules. |
| **Gameplay depends on Core** | `ExtractionGameplay` → `ExtractionCore` |
| **Plugins depend on Core only** | Plugins use `ExtractionCore` interfaces, never depend on each other directly |
| **UI depends on Gameplay** | `ExtractionUI` → `ExtractionGameplay` → `ExtractionCore` |
| **Editor depends on everything** | `ExtractionEditor` can reference all modules (Editor-only) |
| **No circular dependencies** | Use interfaces (`I` prefix) in Core to decouple modules |

### Module `.Build.cs` Template

```csharp
// ExtractionGameplay.Build.cs
using UnrealBuildTool;

public class ExtractionGameplay : ModuleRules
{
    public ExtractionGameplay(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
        
        // Strict include-what-you-use
        bEnforceIWYU = true;
        
        PublicDependencyModuleNames.AddRange(new string[]
        {
            "Core",
            "CoreUObject",
            "Engine",
            "ExtractionCore",        // Our core interfaces
            "GameplayAbilities",     // GAS
            "GameplayTags",          // Gameplay Tags
            "GameplayTasks",
        });

        PrivateDependencyModuleNames.AddRange(new string[]
        {
            "InputCore",
            "EnhancedInput",
            "UMG",
            "Slate",
            "SlateCore",
        });
    }
}
```

---

## 📛 C++ Naming Conventions

### Type Prefixes (Epic Standard — Mandatory)

| Prefix | Type | Example |
|:-------|:-----|:--------|
| `A` | Classes inheriting `AActor` | `AExtractionCharacter`, `AWeaponBase` |
| `U` | Classes inheriting `UObject` | `UInventoryComponent`, `UHealthComponent` |
| `F` | Structs and most other classes | `FWeaponData`, `FItemSlot`, `FDamageResult` |
| `S` | Classes inheriting `SWidget` (Slate) | `SInventoryGrid`, `SHealthBar` |
| `I` | Abstract interfaces | `IInteractable`, `IDamageable`, `ILootable` |
| `E` | Enums | `EWeaponType`, `EItemRarity`, `EDamageType` |
| `T` | Templates | `TArray`, `TMap`, `TSubclassOf` |
| `b` | Boolean variables | `bIsAlive`, `bCanFire`, `bHasExtracted` |

> **⚠️ Critical:** The Unreal Header Tool (UHT) **requires** correct prefixes. Incorrect prefixes cause compilation failures.

### Variable Naming

| Convention | Example | Bad Example |
|:-----------|:--------|:------------|
| **PascalCase** for all variables | `CurrentHealth`, `MaxAmmo` | `currentHealth`, `max_ammo` |
| **`b` prefix** for booleans | `bIsReloading`, `bCanSprint` | `IsReloading`, `CanSprint` |
| **No type names** in variable names | `Health`, `Name` | `HealthFloat`, `NameString` |
| **No redundant context** | In `APlayerCharacter`: use `Score` | `PlayerScore` (redundant) |
| **`Out` prefix** for output params | `OutHitResult`, `OutDamage` | `HitResult` (ambiguous) |
| **Descriptive nouns** for variables | `TargetLocation`, `EquippedWeapon` | `TgtLoc`, `Wpn` |
| **Descriptive verbs** for functions | `CalculateDamage()`, `FindNearestEnemy()` | `Damage()`, `Enemy()` |

### Function Naming

```cpp
// ✅ Good — verbs that describe effect or return value
void EquipWeapon(AWeaponBase* NewWeapon);
float CalculateDamage(const FDamageEvent& DamageEvent) const;
bool CanExtract() const;
AExtractionPoint* FindNearestExtractionPoint() const;
void OnHealthChanged(float OldValue, float NewValue);

// ❌ Bad
void Weapon(AWeaponBase* W);          // No verb, unclear
float Damage(const FDamageEvent& DE);  // Abbreviated, unclear
bool Extract();                        // Ambiguous: check or do?
```

### Enum Naming

```cpp
// ✅ Good — E prefix, PascalCase values
UENUM(BlueprintType)
enum class EWeaponType : uint8
{
    AssaultRifle,
    Shotgun,
    SniperRifle,
    SubmachineGun,
    Pistol,
    MeleeWeapon,
};

// ✅ Good — Use enum class (strongly-typed), never old-style enums
UENUM(BlueprintType)
enum class EItemRarity : uint8
{
    Common,
    Uncommon,
    Rare,
    Epic,
    Legendary,
};
```

### Delegate Naming

```cpp
// Signature: F + description + Delegate/Signature
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnHealthChanged, float, NewHealth);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnItemPickedUp, UItemData*, Item, int32, Quantity);
DECLARE_DELEGATE_RetVal_OneParam(bool, FCanInteractSignature, AActor*);
```

### Macro Naming

```cpp
// ✅ Good — UE_ prefix, SCREAMING_SNAKE_CASE
#define UE_EXTRACTION_LOG(Category, Verbosity, Format, ...) \
    UE_LOG(LogExtraction, Verbosity, TEXT(Format), ##__VA_ARGS__)

// Log categories
DECLARE_LOG_CATEGORY_EXTERN(LogExtraction, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogExtractionWeapon, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogExtractionInventory, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogExtractionAI, Log, All);
```

---

## 📁 C++ File Organization

### Header File Layout

Every `.h` file should follow this structure, using `#pragma region` for collapsible sections:

```cpp
// Copyright [Year] [Company]. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "ExtractionCharacter.generated.h"  // MUST be last include

// Forward declarations (avoid #include in headers where possible)
class UInventoryComponent;
class UHealthComponent;
class AWeaponBase;

/**
 * AExtractionCharacter
 * 
 * Base character class for all playable operators in the extraction shooter.
 * Handles movement, health, inventory, and weapon management.
 * 
 * @see UHealthComponent, UInventoryComponent
 */
UCLASS(Abstract, Blueprintable)
class EXTRACTIONGAMEPLAY_API AExtractionCharacter : public ACharacter
{
    GENERATED_BODY()

public:
    AExtractionCharacter();

#pragma region // ============ Components ============

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Components")
    TObjectPtr<UHealthComponent> HealthComponent;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Components")
    TObjectPtr<UInventoryComponent> InventoryComponent;

#pragma endregion // Components

#pragma region // ============ Weapon System ============

    /** Equip a weapon from inventory to the active slot. */
    UFUNCTION(BlueprintCallable, Category = "Weapon")
    void EquipWeapon(AWeaponBase* NewWeapon);

    /** Returns the currently equipped weapon, or nullptr. */
    UFUNCTION(BlueprintPure, Category = "Weapon")
    AWeaponBase* GetEquippedWeapon() const;

#pragma endregion // Weapon System

#pragma region // ============ Health & Damage ============

    /** Apply damage to this character. */
    UFUNCTION(BlueprintCallable, Category = "Health")
    void ApplyDamage(float DamageAmount, EDamageType DamageType, AActor* DamageCauser);

    /** Check if this character is alive. */
    UFUNCTION(BlueprintPure, Category = "Health")
    bool IsAlive() const;

    /** Broadcast when health changes. */
    UPROPERTY(BlueprintAssignable, Category = "Health")
    FOnHealthChanged OnHealthChanged;

#pragma endregion // Health & Damage

#pragma region // ============ Extraction ============

    UFUNCTION(BlueprintCallable, Category = "Extraction")
    bool CanExtract() const;

    UFUNCTION(BlueprintCallable, Category = "Extraction")
    void StartExtraction();

#pragma endregion // Extraction

protected:
    virtual void BeginPlay() override;
    virtual void Tick(float DeltaTime) override;

private:
    UPROPERTY()
    TObjectPtr<AWeaponBase> EquippedWeapon;

    UPROPERTY()
    bool bIsExtracting = false;
};
```

### Source File Layout

```cpp
// Copyright [Year] [Company]. All Rights Reserved.

#include "Characters/ExtractionCharacter.h"

// Module includes
#include "Components/HealthComponent.h"
#include "Components/InventoryComponent.h"
#include "Weapons/WeaponBase.h"

// Engine includes
#include "GameFramework/CharacterMovementComponent.h"

// ============ Constructor ============

AExtractionCharacter::AExtractionCharacter()
{
    PrimaryActorTick.bCanEverTick = true;

    HealthComponent = CreateDefaultSubobject<UHealthComponent>(TEXT("HealthComponent"));
    InventoryComponent = CreateDefaultSubobject<UInventoryComponent>(TEXT("InventoryComponent"));
}

// ============ Lifecycle ============

void AExtractionCharacter::BeginPlay()
{
    Super::BeginPlay();
    // ...
}

void AExtractionCharacter::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
    // ...
}

// ============ Weapon System ============

void AExtractionCharacter::EquipWeapon(AWeaponBase* NewWeapon)
{
    if (!NewWeapon)
    {
        return;
    }
    
    EquippedWeapon = NewWeapon;
    // ...
}

AWeaponBase* AExtractionCharacter::GetEquippedWeapon() const
{
    return EquippedWeapon;
}

// ============ Health & Damage ============

void AExtractionCharacter::ApplyDamage(float DamageAmount, EDamageType DamageType, AActor* DamageCauser)
{
    if (!IsAlive())
    {
        return;
    }

    HealthComponent->TakeDamage(DamageAmount, DamageType, DamageCauser);
}

bool AExtractionCharacter::IsAlive() const
{
    return HealthComponent && HealthComponent->GetCurrentHealth() > 0.f;
}

// ============ Extraction ============

bool AExtractionCharacter::CanExtract() const
{
    return IsAlive() && !bIsExtracting;
}

void AExtractionCharacter::StartExtraction()
{
    if (!CanExtract())
    {
        return;
    }

    bIsExtracting = true;
    // ...
}
```

### Include Order

Organize `#include` statements in this exact order, separated by blank lines:

```cpp
// 1. Matching .h file (always first in .cpp)
#include "Characters/ExtractionCharacter.h"

// 2. Project module includes (alphabetical within each module)
#include "Components/HealthComponent.h"
#include "Components/InventoryComponent.h"
#include "Weapons/WeaponBase.h"

// 3. Other project plugin includes
#include "ExtractionInventory/ItemData.h"

// 4. Engine includes (alphabetical)
#include "GameFramework/CharacterMovementComponent.h"
#include "Net/UnrealNetwork.h"

// 5. Third-party includes (rare, use sparingly)
```

### `#pragma region` Best Practices

| Rule | Description |
|:-----|:------------|
| **Use in headers** | Organize `UPROPERTY` and `UFUNCTION` groups by feature area |
| **Avoid in structs** | `#pragma region` inside `USTRUCT` can break UHT |
| **Match opening/closing** | Always add a comment: `#pragma endregion // SectionName` |
| **Keep sections 10-40 lines** | Too small = noise. Too large = defeats purpose |
| **Group by feature, not by type** | Group "Weapon" properties + functions together, not "all UPROPERTYs" |

---

## 🔧 UPROPERTY & UFUNCTION Guidelines

### UPROPERTY Categories

Organize with consistent, hierarchical categories:

```cpp
// ✅ Good — Hierarchical categories
UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Weapon|Stats")
float BaseDamage = 25.f;

UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Weapon|Stats")
float FireRate = 0.1f;

UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Weapon|Ammo")
int32 MaxAmmo = 30;

UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Weapon|Recoil")
float RecoilStrength = 1.5f;

// ❌ Bad — Inconsistent or flat categories
UPROPERTY(EditDefaultsOnly, Category = "Damage")
float BaseDamage;

UPROPERTY(EditDefaultsOnly, Category = "Gun")
float FireRate;
```

### UPROPERTY Specifier Cheat Sheet

| Use Case | Specifiers |
|:---------|:-----------|
| **Designer-tunable, read in BP** | `EditDefaultsOnly, BlueprintReadOnly` |
| **Designer-tunable, writable in BP** | `EditDefaultsOnly, BlueprintReadWrite` |
| **Per-instance editable** | `EditAnywhere, BlueprintReadWrite` |
| **Runtime-only, visible in BP** | `VisibleAnywhere, BlueprintReadOnly` |
| **Component reference** | `VisibleAnywhere, BlueprintReadOnly` |
| **Replicated variable** | `Replicated` or `ReplicatedUsing = OnRep_VarName` |
| **Pure internal** | No specifiers (just `UPROPERTY()` for GC) |
| **Delegate** | `BlueprintAssignable` |

### UFUNCTION Specifier Cheat Sheet

| Use Case | Specifiers |
|:---------|:-----------|
| **Callable from BP** | `BlueprintCallable, Category = "..."` |
| **Pure getter (no side-effects)** | `BlueprintPure, Category = "..."` |
| **Implementable in BP** | `BlueprintImplementableEvent` |
| **Native + BP override** | `BlueprintNativeEvent` |
| **Server RPC** | `Server, Reliable, WithValidation` |
| **Client RPC** | `Client, Reliable` |
| **Multicast RPC** | `NetMulticast, Reliable` |

---

## 📂 Content Folder Structure (UE5 Assets)

### Project-Level Structure

```
Content/
├── ExtractionGame/                    ← Top-level project folder
│   ├── Art/
│   │   ├── Characters/
│   │   │   ├── Operators/
│   │   │   │   ├── Assault/           ← Per-operator folder
│   │   │   │   │   ├── SK_Assault.uasset
│   │   │   │   │   ├── T_Assault_D.uasset
│   │   │   │   │   ├── T_Assault_N.uasset
│   │   │   │   │   └── ABP_Assault.uasset
│   │   │   │   ├── Recon/
│   │   │   │   └── Support/
│   │   │   └── NPCs/
│   │   ├── Environment/
│   │   │   ├── Industrial/
│   │   │   ├── Military/
│   │   │   └── Nature/
│   │   ├── Props/
│   │   ├── VFX/
│   │   └── UI/
│   │       ├── Icons/
│   │       ├── HUD/
│   │       └── Menus/
│   │
│   ├── Audio/
│   │   ├── SFX/
│   │   │   ├── Weapons/
│   │   │   ├── Footsteps/
│   │   │   └── Environment/
│   │   ├── Music/
│   │   └── VO/                        ← Voice Over
│   │
│   ├── Blueprints/
│   │   ├── Core/                      ← Game modes, game state
│   │   ├── Characters/
│   │   ├── Weapons/
│   │   ├── Items/
│   │   ├── AI/
│   │   └── UI/
│   │
│   ├── Data/
│   │   ├── DataTables/
│   │   ├── DataAssets/
│   │   ├── CurveTables/
│   │   └── GameplayTags/
│   │
│   ├── Maps/
│   │   ├── Campaign/
│   │   │   ├── Factory/
│   │   │   ├── Customs/
│   │   │   └── Interchange/
│   │   ├── Menu/                      ← Main menu levels
│   │   └── Test/                      ← Testing levels (not shipped)
│   │
│   ├── Materials/
│   │   ├── Master/                    ← Master materials
│   │   │   ├── M_Master_Opaque.uasset
│   │   │   ├── M_Master_Translucent.uasset
│   │   │   └── M_Master_Character.uasset
│   │   ├── Instances/                 ← Material instances
│   │   ├── Functions/                 ← Material functions library
│   │   └── PostProcess/
│   │
│   └── Core/                          ← Critical non-destructible assets
│       ├── GameModes/
│       ├── InputActions/
│       └── DefaultLoadout/
│
├── Developers/                        ← Personal dev folders (git-ignored)
│   ├── DevJohn/
│   └── DevMary/
│
└── _Shared/                           ← Cross-project shared assets
    ├── MaterialLibrary/
    └── UtilityBlueprints/
```

<!-- 📸 IMAGE PLACEHOLDER: Content Browser screenshot showing the top-level folder structure with proper organization -->

### Folder Naming Rules

| Rule | Example | Bad Example |
|:-----|:--------|:------------|
| **PascalCase** | `WeaponAttachments` | `weapon_attachments` |
| **No spaces** | `AssaultRifles` | `Assault Rifles` |
| **Plural for collections** | `Materials`, `Textures` | `Material`, `Texture` |
| **Never name "Assets" or "Meshes"** | `Environment/Industrial` | `Meshes/IndustrialMeshes` |
| **No redundant type in name** | `Materials/` contains `.uasset` | `MaterialsAssets/` |

---

## 📛 Asset Naming Conventions

### Base Pattern

```
[Prefix]_[AssetName]_[Variant]_[Suffix]
```

| Part | Purpose | Example |
|:-----|:--------|:--------|
| **Prefix** | Asset type identifier | `SM_`, `T_`, `M_`, `BP_` |
| **AssetName** | Descriptive name (PascalCase) | `AK47`, `DesertEagle`, `MedKit` |
| **Variant** | Optional sub-variant | `_Evil`, `_Retro`, `_01`, `_02` |
| **Suffix** | Context descriptor | `_D` (Diffuse), `_N` (Normal), `_Icon` |

### Asset Prefix Table

#### Common Assets

| Asset Type | Prefix | Example |
|:-----------|:-------|:--------|
| Blueprint | `BP_` | `BP_WeaponRifle` |
| Static Mesh | `SM_` | `SM_Crate_Military_01` |
| Skeletal Mesh | `SK_` | `SK_Operator_Assault` |
| Material | `M_` | `M_Metal_Rusted` |
| Material Instance | `MI_` | `MI_Metal_Rusted_Dark` |
| Texture | `T_` | `T_Crate_Military_D` |
| Widget Blueprint | `WBP_` | `WBP_InventoryGrid` |
| Data Asset | `DA_` | `DA_WeaponStats_AK47` |
| Data Table | `DT_` | `DT_ItemDatabase` |
| Curve Table | `CT_` | `CT_DamageFalloff` |
| Gameplay Tag Table | `GTT_` | `GTT_AbilityTags` |

#### Animation

| Asset Type | Prefix | Example |
|:-----------|:-------|:--------|
| Animation Blueprint | `ABP_` | `ABP_Operator_Assault` |
| Animation Sequence | `AS_` | `AS_Rifle_Fire` |
| Animation Montage | `AM_` | `AM_Reload_AK47` |
| Blendspace | `BS_` | `BS_Locomotion` |
| Blendspace 1D | `BS1D_` | `BS1D_AimOffset` |
| Aim Offset | `AO_` | `AO_Rifle` |
| Control Rig | `CR_` | `CR_IK_LeftHand` |

#### Effects & Audio

| Asset Type | Prefix | Example |
|:-----------|:-------|:--------|
| Niagara System | `NS_` | `NS_MuzzleFlash` |
| Niagara Emitter | `NE_` | `NE_Sparks_Metal` |
| Sound Cue | `SC_` | `SC_Rifle_Fire` |
| Sound Wave | `SW_` | `SW_Gunshot_AK47_01` |
| Sound Attenuation | `SA_` | `SA_Weapon_Indoor` |
| Sound Concurrency | `SCO_` | `SCO_Footsteps` |
| Sound Mix | `SMX_` | `SMX_Gameplay` |
| MetaSound | `MS_` | `MS_WeaponFire` |

#### AI

| Asset Type | Prefix | Example |
|:-----------|:-------|:--------|
| Behavior Tree | `BT_` | `BT_EnemyPatrol` |
| Blackboard | `BB_` | `BB_EnemyAI` |
| AI Controller | `AIC_` | `AIC_EnemySoldier` |
| EQS Query | `EQS_` | `EQS_FindCover` |

#### Physics & Input

| Asset Type | Prefix | Example |
|:-----------|:-------|:--------|
| Physics Asset | `PHYS_` | `PHYS_Operator_Assault` |
| Physics Material | `PM_` | `PM_Concrete` |
| Input Action | `IA_` | `IA_Fire`, `IA_Reload` |
| Input Mapping Context | `IMC_` | `IMC_OnFoot`, `IMC_Vehicle` |

### Texture Suffixes

| Suffix | Texture Type | Example |
|:-------|:-------------|:--------|
| `_D` | Diffuse / Base Color | `T_Crate_D` |
| `_N` | Normal Map | `T_Crate_N` |
| `_E` | Emissive | `T_Crate_E` |
| `_M` | Metallic | `T_Crate_M` |
| `_R` | Roughness | `T_Crate_R` |
| `_AO` | Ambient Occlusion | `T_Crate_AO` |
| `_ORM` | Packed OcclusionRoughnessMetallic | `T_Crate_ORM` |
| `_MRA` | Packed MetallicRoughnessAO | `T_Crate_MRA` |
| `_Mask` | Generic Mask | `T_Crate_Mask` |
| `_A` | Alpha / Opacity | `T_Crate_A` |
| `_H` | Height / Displacement | `T_Crate_H` |
| `_F` | Flow Map | `T_Water_F` |
| `_L` | Light Map | `T_Scene_L` |

---

## 🎨 Blueprint Naming & Standards

### Blueprint Naming

| Blueprint Type | Prefix | Example |
|:---------------|:-------|:--------|
| Standard BP | `BP_` | `BP_PlayerCharacter` |
| Widget BP | `WBP_` | `WBP_HealthBar` |
| Anim BP | `ABP_` | `ABP_Operator_Assault` |
| Game Mode | `GM_` | `GM_Extraction` |
| Game State | `GS_` | `GS_ExtractionMatch` |
| Player State | `PS_` | `PS_ExtractionPlayer` |
| Player Controller | `PC_` | `PC_ExtractionPlayer` |
| HUD | `HUD_` | `HUD_InGame` |
| Component BP | `BPC_` | `BPC_InteractionSensor` |

### Blueprint Variable Naming

Same rules as C++:
- **PascalCase** for all variables
- **`b` prefix** for booleans
- **No type in name** (use `Speed`, not `SpeedFloat`)
- **Descriptive nouns** (use `MaxHealth`, not `MH`)

### Blueprint Function Categories

Organize functions in consistent categories matching the C++ `#pragma region` structure:

```
Category: "Combat|Damage"
Category: "Combat|Weapons"
Category: "Movement|Sprint"
Category: "Inventory|Items"
Category: "UI|HUD"
```

---

## 💬 Code Comments

### Comment Style (JavaDoc-compatible)

```cpp
/**
 * UInventoryComponent
 *
 * Manages the player's in-raid inventory using a grid-based system.
 * Items occupy cells based on their width/height defined in the ItemData asset.
 *
 * Grid layout is defined by GridWidth and GridHeight properties.
 *
 * @see FItemSlot, UItemData
 */
UCLASS(ClassGroup = (Extraction), meta = (BlueprintSpawnableComponent))
class EXTRACTIONGAMEPLAY_API UInventoryComponent : public UActorComponent
{
    // ...

    /**
     * Attempts to add an item to the inventory at the first available position.
     *
     * @param ItemData    The item data asset describing the item to add.
     * @param Quantity    Number of items to add (must be > 0).
     * @param OutSlot     [Out] The slot where the item was placed, if successful.
     * @return true if item was successfully added.
     *
     * @warning This does not check weight limits. Call CanCarry() first.
     * @see RemoveItem, CanCarry
     */
    UFUNCTION(BlueprintCallable, Category = "Inventory")
    bool AddItem(UItemData* ItemData, int32 Quantity, FItemSlot& OutSlot);
};
```

### TODO/FIXME Format

```cpp
// TODO(P0): Critical — must be done before alpha
// TODO(P1): High — should be done this sprint
// TODO(P2): Medium — nice to have this milestone
// TODO(P3): Low — backlog item

// TODO(P0): Implement server-authoritative inventory validation
// TODO(P1): Add weapon sway based on movement state
// FIXME: Extraction timer doesn't reset on zone exit
// HACK: Temporary workaround for UE5.4 animation bug — remove after upgrade
```

---

## 🏷️ Gameplay Tags Convention

Gameplay Tags follow a hierarchical namespace:

```
// Format: System.Category.Subcategory.Name
Ability.Skill.Dash
Ability.Skill.Heal
Weapon.Type.AssaultRifle
Weapon.Type.Shotgun
Weapon.Attachment.Optic.RedDot
Weapon.Attachment.Muzzle.Suppressor
Item.Rarity.Common
Item.Rarity.Legendary
State.Character.Dead
State.Character.Extracting
State.Character.Downed
Damage.Type.Bullet
Damage.Type.Explosive
Damage.Type.Fire
Input.Action.Fire
Input.Action.Reload
Input.Action.Interact
```

### Tag File Organization

| File | Contents |
|:-----|:---------|
| `GameplayTags_Abilities.ini` | All `Ability.*` tags |
| `GameplayTags_Weapons.ini` | All `Weapon.*` tags |
| `GameplayTags_Items.ini` | All `Item.*` tags |
| `GameplayTags_States.ini` | All `State.*` tags |
| `GameplayTags_Damage.ini` | All `Damage.*` tags |
| `GameplayTags_Input.ini` | All `Input.*` tags |

---

## 🔀 Source Control Conventions

### Branch Naming

```
// Format: type/ticket-description
feature/EXT-123-inventory-grid-system
bugfix/EXT-456-health-not-replicating
hotfix/EXT-789-crash-on-extraction
refactor/EXT-012-weapon-system-cleanup
docs/EXT-345-gdd-social-update
```

### Commit Messages

```
// Format: [TYPE] Brief description (ticket)
[Feature] Add grid-based inventory system (EXT-123)
[Bugfix] Fix health not replicating to clients (EXT-456)
[Refactor] Simplify weapon attachment slot logic (EXT-012)
[Docs] Update Social & Multiplayer GDD (EXT-345)
[Config] Adjust weapon damage balance values
[Asset] Add new assault rifle model and textures
```

### `.gitignore` Rules

```
# UE5 generated
Binaries/
Intermediate/
Build/
Saved/
DerivedDataCache/

# Developer personal folders
Content/Developers/
*.log

# IDE
.vs/
.idea/
*.sln.docstates

# OS
Thumbs.db
.DS_Store
```

---

## ⚡ Performance & Optimization Rules

### Memory Rules

| Rule | Guideline |
|:-----|:----------|
| **Use `TObjectPtr<>`** | For all `UPROPERTY` pointer members (UE5.1+) |
| **Use `TWeakObjectPtr<>`** | For non-owning references that may become invalid |
| **Use `TSoftObjectPtr<>`** | For assets that should be loaded on demand |
| **Avoid `TSharedPtr` for UObjects** | UObjects have their own GC — use `TObjectPtr` |
| **Pool frequently spawned objects** | Projectiles, VFX, decals |

### Tick Rules

| Rule | Guideline |
|:-----|:----------|
| **Disable tick by default** | `PrimaryActorTick.bCanEverTick = false;` |
| **Use timers over tick** | `GetWorldTimerManager().SetTimer(...)` |
| **Use delegates over polling** | Subscribe to changes, don't check every frame |
| **Batch raycasts** | Use async trace batches for AI perception |

---

## 📚 Reference Links

| Resource | URL |
|:---------|:----|
| Epic C++ Coding Standard | [docs.unrealengine.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine) |
| Epic Asset Naming Conventions | [docs.unrealengine.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects) |
| Allar UE5 Style Guide v2 | [github.com/Allar](https://github.com/Allar/ue5-style-guide/tree/v2) |
| Unreal Directive Naming | [unrealdirective.com](https://unrealdirective.com/resources/asset-naming-conventions) |
| UE5 Lyra Sample Game | [docs.unrealengine.com](https://docs.unrealengine.com/5.0/en-US/lyra-sample-game-in-unreal-engine/) |
| Epic Gameplay Framework | [docs.unrealengine.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) |
