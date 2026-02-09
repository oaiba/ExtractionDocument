# Coding Standards & Guidelines

**[← Back to Index](../README.md)**

---

## 🏗️ Naming Conventions (Unreal Engine Standard)

We strictly follow the [Unreal Engine Coding Standard](https://docs.unrealengine.com/5.0/en-US/epic-cplusplus-coding-standard-for-unreal-engine/). Consistency is mandatory.

### Class Prefixes
| Prefix | Type | Example |
| :--- | :--- | :--- |
| `A` | Actor (Spawnable) | `AExtractionCharacter` |
| `U` | UObject (Data/Component) | `UInventoryComponent` |
| `F` | Struct / Plain C++ Class | `FWeaponData`, `FJsonParser` |
| `E` | Enum | `EWeaponState` |
| `I` | Interface | `IInteractable` |
| `T` | Template | `TArray<T>` |
| `S` | Slate Widget | `SInventoryWidget` |

### Variable Naming
*   **Booleans:** Must start with `b`.
    *   *Correct:* `bIsDead`, `bCanReload`
    *   *Incorrect:* `isDead`, `Dead`
*   **Member Variables:** PascalCase (UpperCamelCase). Do NOT use `m_` prefix.
    *   *Correct:* `Health`, `AmmoCount`
    *   *Incorrect:* `health`, `m_Health`
*   **Function Parameters:** PascalCase.
    *   *Correct:* `void TakeDamage(float DamageAmount)`

### File Naming
*   Files must match the class name exactly.
    *   `AExtractionCharacter` -> `ExtractionCharacter.h` and `ExtractionCharacter.cpp`

---

## 🛡️ Code Architecture

### "Composition over Inheritance"
*   Avoid deep inheritance hierarchies. Use **Components** to add functionality.
*   *Example:* Do not create `AHealingItem` inheriting from `AItem`. Instead, create an `AItem` and give it a `UHealingEffectComponent`.

### Network Replication
*   **Authority First:** All gameplay-critical logic (Health, Inventory, Loot) happens on the Server.
*   **Replication Functions:**
    *   `Server_`: Function runs on Server. (e.g., `Server_FireWeapon`)
    *   `Client_`: Function runs on owning Client. (e.g., `Client_PlayHitMarker`)
    *   `Multicast_`: Function runs on all clients. (e.g., `Multicast_ExplosionEffect`)
*   **Variable Replication:** Use `OnRep_` functions for visual updates.
    *   *Example:* `UPROPERTY(ReplicatedUsing=OnRep_Health) float Health;`

---

## 📝 Best Practices

1.  **minimize `Tick()` Usage:**
    *   Do not put logic in `Tick()` unless absolutely necessary.
    *   Use **Timers** or **Event Delegates** instead.
2.  **Cast Safely:**
    *   Use `Cast<Type>(Object)` and always check for `nullptr`.
3.  **Logging:**
    *   Use `UE_LOG` with specific Log Categories. Do not use `UE_LOG(LogTemp...)` in production code.
    *   Define category: `DEFINE_LOG_CATEGORY_STATIC(LogWeapon, All, All);`

---

## 🚫 Common Pitfalls (Anti-Patterns)

*   **Hardcoding Paths:** Never use `ConstructorHelpers::FClassFinder` inside usage functions. Load assets via `UPROPERTY(EditDefaultsOnly)` in Blueprints.
*   **god Classes:** If a class has more that 2000 lines, it's doing too much. Break it down.
*   **Blueprint Logic:** Heavy math or complex loops must be C++. Blueprints are for configuration and simple flow.

---
