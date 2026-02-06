# Map & Environment System

**[← Previous: AI System](./06_AISystem.md)** | **[Technical Index](./README.md)** | **[Next: Performance Optimization →](./08_PerformanceOptimization.md)**

---

## Overview

Technical implementation của map structure, level streaming, dynamic events, và environmental systems.

**Status:** 🔴 TODO - To be detailed

---

## Quick Reference

### Core Classes

- `AExtractionGameState` - Match state management
- `AExtractionZone` - Extraction point actors
- `ASupplyDrop` - Supply drop system
- `AContaminationSystem` - Zone contamination

### Key Systems

- Level streaming
- Extraction zones
- Supply drops
- Contamination system
- Dynamic events
- Map transitions

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] Implement extraction zones
- [ ] Map streaming setup
- [ ] Match timer system
- [ ] Supply drop spawning
- [ ] Basic contamination system

### MEDIUM Priority 🟡
- [ ] Dynamic events system
- [ ] Environmental hazards
- [ ] Weather system
- [ ] Map transitions
- [ ] Zone activation logic

### LOW Priority 🟢
- [ ] Advanced weather
- [ ] Destructible environments
- [ ] Interactive elements
- [ ] Map-specific mechanics

---

## Code Stub

```cpp
UCLASS()
class EXTRACTION_API AExtractionZone : public AActor
{
    GENERATED_BODY()
    
public:
    UPROPERTY(Replicated, BlueprintReadOnly)
    bool bIsActive = false;
    
    UPROPERTY(EditAnywhere)
    float ExtractionDuration = 30.0f;
    
    UPROPERTY(EditAnywhere)
    int32 MaxPlayers = 4;
    
    UFUNCTION(BlueprintCallable)
    void BeginExtraction(AExtractionCharacter* Player);
    
    UFUNCTION(BlueprintCallable)
    void CancelExtraction(AExtractionCharacter* Player);
    
protected:
    TArray<AExtractionCharacter*> ExtractingPlayers;
    TMap<AExtractionCharacter*, float> ExtractionTimers;
};
```

---

**[← Previous: AI System](./06_AISystem.md)** | **[Technical Index](./README.md)** | **[Next: Performance Optimization →](./08_PerformanceOptimization.md)**
