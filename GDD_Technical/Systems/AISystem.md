# AI System

**[← Previous: Inventory System](./05_InventorySystem.md)** | **[Technical Index](./README.md)** | **[Next: Map System →](./07_MapSystem.md)**

---

## Overview

AI implementation cho enemy characters, behavior trees, perception, và combat AI.

**Status:** 🔴 TODO - To be detailed

---

## Quick Reference

### Core Classes

- `AExtractionAICharacter` - AI character class
- `AExtractionAIController` - AI controller
- `UBehaviorTree` - AI behavior logic
- `UAIPerceptionComponent` - Vision/hearing

### Key Systems

- Behavior trees
- Perception system (sight, sound)
- Pathfinding
- Combat AI
- Patrol routes

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] Create `AExtractionAICharacter`
- [ ] Implement AI controller
- [ ] Basic behavior tree
- [ ] Perception system setup
- [ ] Simple patrol behavior

### MEDIUM Priority 🟡
- [ ] Combat AI logic
- [ ] Cover system integration
- [ ] Team coordination
- [ ] Difficulty levels
- [ ] AI spawning system

### LOW Priority 🟢
- [ ] Advanced behaviors
- [ ] Boss AI
- [ ] Dynamic difficulty
- [ ] AI voice lines

---

## Code Stub

```cpp
UCLASS()
class EXTRACTION_API AExtractionAICharacter : public AExtractionCharacter
{
    GENERATED_BODY()
    
public:
    UPROPERTY(EditAnywhere, Category = "AI")
    EAIDifficulty Difficulty = EAIDifficulty::Normal;
    
    UPROPERTY(EditAnywhere, Category = "AI")
    float DetectionRange = 2000.0f;
    
    UPROPERTY(EditAnywhere, Category = "AI")
    float AttackRange = 1500.0f;
    
protected:
    UPROPERTY()
    AActor* CurrentTarget;
    
    UFUNCTION()
    void UpdateAI(float DeltaTime);
    
    UFUNCTION()
    AActor* FindNearestThreat();
};
```

---

**[← Previous: Inventory System](./05_InventorySystem.md)** | **[Technical Index](./README.md)** | **[Next: Map System →](./07_MapSystem.md)**
