---
title: "Code Generation Rules"
type: docs
weight: 1
---

## Code Generation Rules for AI Agents

These rules are **mandatory** for all AI agents generating C++ or Blueprint code for this Unreal Engine 5 project. Violations will cause build failures, UHT errors, or inconsistency with the team's codebase.

> **Pre-requisite:** Read [Coding & Asset Standards](../../GDD_Technical/CodingStandards.md) before proceeding.

---

### Critical Rules (Must Never Violate)

#### 1. UE5 Type Prefixes
Every class, struct, enum, and interface **must** use the correct prefix:

```cpp
// Mandatory prefixes
A  → Actors              (AExtractionCharacter)
U  → UObject subclasses  (UInventoryComponent)
F  → Structs / non-UE    (FWeaponData, FItemSlot)
E  → Enums              (EWeaponType, EItemRarity)
I  → Interfaces          (IInteractable, IDamageable)
S  → Slate widgets       (SInventoryGrid)
T  → Templates          (TArray, TMap)
b  → Booleans           (bIsAlive, bCanFire)
```

#### 2. Generated Header Must Be Last Include
```cpp
// Correct
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "MyActor.generated.h"  // ALWAYS last

// Wrong — will cause UHT compilation failure
#include "MyActor.generated.h"
#include "CoreMinimal.h"
```

#### 3. GENERATED_BODY() Macro
Every `UCLASS`, `USTRUCT`, and `UENUM` **must** include `GENERATED_BODY()`:

```cpp
UCLASS()
class MYMODULE_API AMyActor : public AActor
{
    GENERATED_BODY()  // MUST be first line inside class body
    // ...
};
```

#### 4. Forward Declare Over Include (in Headers)
```cpp
// Good — forward declare in .h
class UInventoryComponent;
class AWeaponBase;

// Bad — include in .h when forward declaration suffices
#include "Components/InventoryComponent.h"
#include "Weapons/WeaponBase.h"
```

#### 5. Use TObjectPtr<> for UPROPERTY Pointers
```cpp
// UE5 style
UPROPERTY()
TObjectPtr<UInventoryComponent> InventoryComp;

// Raw pointers (UE4 legacy)
UPROPERTY()
UInventoryComponent* InventoryComp;
```

---

### High Priority Rules

#### 6. Class Organization Order
Follow this order inside every class:

```
1. GENERATED_BODY()
2. public: Constructor, public API
3. #pragma region (by feature group)
4. protected: Overrides (BeginPlay, Tick)
5. private: Internal state
```

#### 7. UPROPERTY Category Convention
Always use hierarchical categories:

```cpp
// Hierarchical
UPROPERTY(EditDefaultsOnly, Category = "Weapon|Stats")
UPROPERTY(EditDefaultsOnly, Category = "Weapon|Ammo")

// Flat or inconsistent
UPROPERTY(EditDefaultsOnly, Category = "Damage")
UPROPERTY(EditDefaultsOnly, Category = "WeaponAmmo")
```

#### 8. Use `#pragma region` for Feature Grouping

```cpp
#pragma region // ============ Combat ============
    // Combat-related properties and functions together
#pragma endregion // Combat
```

**Do NOT** use `#pragma region` inside `USTRUCT` (breaks UHT).

#### 9. Braces on New Line (Allman Style)
```cpp
// Epic standard
if (bIsAlive)
{
    TakeDamage(Amount);
}

// K&R style
if (bIsAlive) {
    TakeDamage(Amount);
}
```

#### 10. Always Include Braces for Single-Statement Blocks
```cpp
// Always braces
if (bCanFire)
{
    Fire();
}

// No braces
if (bCanFire)
    Fire();
```

---

### Style Rules

#### 11. Naming Consistency
- Variables: **PascalCase** nouns (`CurrentHealth`, `MaxAmmo`)
- Functions: **PascalCase** verbs (`CalculateDamage()`, `FindNearestEnemy()`)
- Booleans: `b` prefix + adjective (`bIsDead`, `bCanSprint`)
- Delegates: `F` prefix + `On` + event name (`FOnHealthChanged`)
- Output params: `Out` prefix (`OutHitResult`)

#### 12. Comment Convention
```cpp
/** Single-line doc comment for brief descriptions */

/**
 * Multi-line doc comment for complex functions.
 * 
 * @param DamageAmount  The amount of damage to apply (> 0).
 * @param DamageCauser  The actor responsible for the damage.
 * @return true if the target died from this damage.
 */
```

#### 13. Log Category Per Module
```cpp
// In module header
DECLARE_LOG_CATEGORY_EXTERN(LogExtractionGameplay, Log, All);

// In module .cpp
DEFINE_LOG_CATEGORY(LogExtractionGameplay);

// Usage
UE_LOG(LogExtractionGameplay, Warning, TEXT("Player %s failed to extract"), *PlayerName);
```

#### 14. Include Order
```
1. Matching .h file
2. Project module includes (alphabetical)
3. Other project plugin includes
4. Engine includes (alphabetical)
5. Third-party includes
```

#### 15. Avoid Magic Numbers
```cpp
// Named constant
static constexpr float DefaultSprintSpeedMultiplier = 1.5f;

// Or use UPROPERTY for designer tuning
UPROPERTY(EditDefaultsOnly, Category = "Movement")
float SprintSpeedMultiplier = 1.5f;

// Magic number
MovementSpeed *= 1.5f;
```

---

### Common Mistakes to Avoid

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| Using `NewObject<>()` for Actors | Actors must be spawned | Use `GetWorld()->SpawnActor<>()` |
| Missing `Super::` calls | Breaks engine initialization | Always call `Super::BeginPlay()` etc. |
| `Tick` for everything | Performance disaster | Use timers, delegates, event-driven |
| Raw `new`/`delete` | UE has its own memory management | Use `NewObject<>`, `CreateDefaultSubobject<>` |
| Including `.cpp` files | Compilation error | Only include `.h` files |
| `using namespace` in headers | Pollutes global namespace, breaks unity builds | Never in headers, sparingly in `.cpp` |
| Putting logic in constructors | Not safe for all UE lifecycle | Use `BeginPlay()` or `PostInitializeComponents()` |
| Forgetting `const` on getters | Violates const correctness | `float GetHealth() const;` |

---

### Code Generation Checklist

Before submitting any generated code, verify:

- [ ] All types use correct UE5 prefixes (A, U, F, E, I, S, T, b)
- [ ] `.generated.h` is the last include
- [ ] `GENERATED_BODY()` is present in all reflected types
- [ ] `UPROPERTY` pointers use `TObjectPtr<>`
- [ ] Categories are hierarchical (`"System|Feature"`)
- [ ] Braces on new lines (Allman style)
- [ ] No magic numbers
- [ ] Forward declarations in headers (not includes)
- [ ] Include order follows the standard
- [ ] Functions have doc comments with `@param` and `@return`
- [ ] Module API macro is present on exported classes
- [ ] Booleans use `b` prefix
