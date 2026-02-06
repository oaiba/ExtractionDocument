# Game Design Document
# Extraction Topdown Mobile Multiplayer

---

**Version:** 1.0  
**Date:** February 6, 2026  
**Platform:** Mobile (iOS/Android)  
**Engine:** Unreal Engine 5 (C++)  
**Genre:** Extraction Shooter, Top-down, Multiplayer  
**Target Audience:** 16+  

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Game Overview](#game-overview)
3. [Core Gameplay Loop](#core-gameplay-loop)
4. [Game Mechanics](#game-mechanics)
5. [Multiplayer Architecture](#multiplayer-architecture)
6. [Technical Specification](#technical-specification)
7. [Map Design](#map-design)
8. [Character Systems](#character-systems)
9. [Progression and Economy](#progression-and-economy)
10. [User Interface](#user-interface)
11. [Monetization Strategy](#monetization-strategy)
12. [Audio Design](#audio-design)
13. [Performance Optimization](#performance-optimization)
14. [Development Roadmap](#development-roadmap)

---

## Executive Summary

An intense multiplayer extraction game where players drop into a hostile top-down environment, gather valuable loot, complete objectives, and extract before time runs out or they are eliminated. The game combines tactical combat, resource management, and risk-reward decision making in a mobile-optimized package.

**Key Features:**
- Real-time multiplayer matches (8-16 players)
- Top-down tactical combat
- Extraction-based gameplay with permanent loot loss
- Deep progression system
- Mobile-optimized controls
- Cross-platform matchmaking
- Season-based content updates

---

## Game Overview

### Game Concept

Players are mercenaries entering dangerous zones to extract valuable resources. Each match is a high-stakes operation where death means losing all carried items. Success requires tactical planning, combat skills, and knowing when to extract.

### Core Pillars

**1. Risk vs Reward**
- Every decision carries weight
- The longer you stay, the more you can earn
- Death means losing everything in your backpack

**2. Tactical Combat**
- Top-down perspective allows for strategic positioning
- Cover system and line-of-sight mechanics
- Variety of weapons and equipment

**3. Persistent Progression**
- Extracted loot is permanently kept
- Unlockable operators with unique abilities
- Base building and upgrades

**4. Mobile Optimization**
- Intuitive touch controls
- Matches designed for 10-15 minute sessions
- Performance optimized for various devices

---

## Core Gameplay Loop

### Pre-Match Phase

1. **Loadout Selection**
   - Choose operator
   - Equip weapons and gear from stash
   - Select starting perks
   - Review map and extraction points

2. **Matchmaking**
   - Server-based matchmaking
   - Skill-based rating system
   - Squad formation (Solo/Duo/Squad)

### In-Match Phase

1. **Deployment**
   - Random spawn points around map edges
   - 10-second protection after spawn
   - Gather bearings and plan route

2. **Exploration and Looting**
   - Search buildings and containers
   - Engage or avoid AI enemies
   - Collect resources, weapons, and special items

3. **Combat Encounters**
   - Fight against other players
   - Defeat AI-controlled enemies
   - Secure high-value areas

4. **Extraction Decision**
   - Call for extraction at designated zones
   - Defend extraction point during countdown
   - Secure loot in your backpack

### Post-Match Phase

1. **Loot Management**
   - Store extracted items in stash
   - Sell items on marketplace
   - Craft or upgrade equipment

2. **Progression**
   - Gain experience and rating
   - Unlock new operators and gear
   - Complete missions and challenges

---

## Game Mechanics

### Movement System

**Implementation:** `AExtractionCharacter` class

```cpp
// Core movement parameters
UPROPERTY(EditAnywhere, Category = "Movement")
float BaseMovementSpeed = 500.0f;

UPROPERTY(EditAnywhere, Category = "Movement")  
float SprintSpeedMultiplier = 1.5f;

UPROPERTY(EditAnywhere, Category = "Movement")
float CrouchSpeedMultiplier = 0.6f;
```

**Movement States:**
- Normal Walk: 500 units/sec
- Sprint: 750 units/sec (drains stamina)
- Crouch: 300 units/sec (reduces visibility/sound)
- Combat (while aiming): 350 units/sec

**Stamina System:**
- Regenerating resource
- Consumed by sprinting and dodging
- Base pool: 100 points
- Regen rate: 10 points/sec after 2-second delay

### Combat System

**Top-Down Shooting Mechanics:**

```cpp
// FRotationComponent - handles aim rotation
class URotationComponent : public UActorComponent
{
    UPROPERTY()
    float AimRotationSpeed = 720.0f; // Degrees per second
    
    UPROPERTY()
    bool bAutoAim = false; // Mobile auto-aim assist
    
    UPROPERTY()
    float AutoAimRange = 1000.0f;
};
```

**Weapon Categories:**
1. Assault Rifles: Medium range, balanced
2. SMGs: High fire rate, close range
3. Shotguns: High damage, very close range
4. Sniper Rifles: Long range, slow fire rate
5. Pistols: Backup, fast draw
6. Melee: Silent kills, no ammo

**Weapon Stats:**
- Damage
- Fire Rate (RPM)
- Magazine Size
- Reload Time
- Effective Range
- Accuracy (spread pattern)
- Recoil Pattern

### Cover System

```cpp
// FCoverPoint structure
USTRUCT(BlueprintType)
struct FCoverPoint
{
    GENERATED_BODY()
    
    UPROPERTY()
    FVector Location;
    
    UPROPERTY()
    FVector Normal; // Direction of cover
    
    UPROPERTY()
    ECoverHeight CoverHeight; // Full/Half/Crouch
    
    UPROPERTY()
    float Protection; // 0.0 to 1.0 damage reduction
};
```

**Cover Mechanics:**
- Auto-detection when near cover objects
- Damage reduction based on cover quality
- Pop-out shooting mechanics
- Destructible cover (advanced feature)

### Loot System

**Item Rarity Tiers:**
- Common (Gray): Basic supplies
- Uncommon (Green): Standard equipment
- Rare (Blue): Quality gear
- Epic (Purple): Advanced technology
- Legendary (Gold): Unique items

**Item Categories:**

```cpp
UENUM(BlueprintType)
enum class EItemCategory : uint8
{
    Weapon,
    Armor,
    Consumable,
    Material,
    QuestItem,
    Currency
};

USTRUCT(BlueprintType)
struct FItemData
{
    GENERATED_BODY()
    
    UPROPERTY()
    FString ItemID;
    
    UPROPERTY()
    FText ItemName;
    
    UPROPERTY()
    EItemCategory Category;
    
    UPROPERTY()
    EItemRarity Rarity;
    
    UPROPERTY()
    int32 StackSize;
    
    UPROPERTY()
    int32 Weight; // Affects movement speed
    
    UPROPERTY()
    int32 Value;
};
```

### Inventory System

**Backpack Mechanics:**
- Grid-based inventory (6x8 = 48 slots)
- Items take varying slot sizes
- Weight affects movement speed
- Secure container (2x2) - items never lost on death

**Implementation:**

```cpp
// UInventoryComponent
class UInventoryComponent : public UActorComponent
{
    UPROPERTY()
    TArray<FInventorySlot> InventorySlots;
    
    UPROPERTY()
    int32 MaxWeight = 50;
    
    UPROPERTY()
    int32 CurrentWeight = 0;
    
    UFUNCTION()
    bool CanAddItem(const FItemData& Item);
    
    UFUNCTION()
    bool AddItem(const FItemData& Item, int32 Quantity);
    
    UFUNCTION()
    void RemoveItem(const FString& ItemID, int32 Quantity);
    
    UFUNCTION()
    float GetMovementSpeedPenalty() const;
};
```

### Extraction Mechanics

**Extraction Points:**
- 4-6 extraction zones per map
- Random activation each match
- Visual and audio indicators
- Requires 30-second wait time

**Extraction Process:**

```cpp
// AExtractionZone actor
class AExtractionZone : public AActor
{
    UPROPERTY()
    bool bIsActive = false;
    
    UPROPERTY()
    float ExtractionDuration = 30.0f;
    
    UPROPERTY()
    int32 MaxPlayers = 4;
    
    UFUNCTION()
    void BeginExtraction(AExtractionCharacter* Player);
    
    UFUNCTION()
    void CancelExtraction(AExtractionCharacter* Player);
    
    UFUNCTION()
    void CompleteExtraction(AExtractionCharacter* Player);
    
private:
    TArray<AExtractionCharacter*> ExtractingPlayers;
    TMap<AExtractionCharacter*, float> ExtractionTimers;
};
```

**Extraction Rules:**
- Players must remain in zone
- Taking damage resets timer
- Visible notification to all nearby players
- Limited extractions per zone

---

## Multiplayer Architecture

### Network Model

**Server Architecture:**
- Dedicated server authoritative model
- Client-side prediction for movement
- Server reconciliation for combat
- Anti-cheat validation

**Session Structure:**

```cpp
// Game session configuration
struct FExtractionSessionConfig
{
    int32 MaxPlayers = 12;
    int32 MinPlayers = 6;
    float MatchDuration = 900.0f; // 15 minutes
    FString MapName;
    EGameMode GameMode;
    bool bRankedMode = false;
};
```

### Replication Strategy

**High Priority (Always Replicate):**
- Character position and rotation
- Health and armor values
- Weapon state (firing, reloading)
- Inventory changes

**Medium Priority (Relevancy-based):**
- Character animations
- Equipment visuals
- Proximity voice chat

**Low Priority (On-demand):**
- Loot container contents
- AI behavior
- Environmental interactions

**Implementation:**

```cpp
// AExtractionCharacter replication
void AExtractionCharacter::GetLifetimeReplicatedProps(
    TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    
    // Always replicate
    DOREPLIFETIME(AExtractionCharacter, Health);
    DOREPLIFETIME(AExtractionCharacter, Armor);
    DOREPLIFETIME(AExtractionCharacter, CurrentWeapon);
    
    // Replicate to owner only
    DOREPLIFETIME_CONDITION(AExtractionCharacter, Inventory, 
        COND_OwnerOnly);
    
    // Conditional replication
    DOREPLIFETIME_CONDITION(AExtractionCharacter, bIsAiming, 
        COND_SkipOwner);
}
```

### Lag Compensation

**Techniques:**
- Client-side prediction for local player
- Server reconciliation for mispredictions
- Interpolation for remote players
- Hit registration using server timeline rewind

```cpp
// Server-side hit validation
bool AExtractionGameMode::ValidateHit(
    AExtractionCharacter* Shooter,
    AExtractionCharacter* Victim,
    const FHitResult& ClientHit,
    float ClientTimestamp)
{
    // Rewind server to client's timestamp
    float Latency = GetWorld()->GetTimeSeconds() - ClientTimestamp;
    FVector VictimPosAtHit = InterpolatePosition(Victim, Latency);
    
    // Perform server-side trace
    FHitResult ServerHit;
    ServerValidateTrace(Shooter, VictimPosAtHit, ServerHit);
    
    // Allow some tolerance for network variance
    float MaxDistance = 50.0f; // UE units
    return FVector::Distance(ClientHit.Location, 
        ServerHit.Location) < MaxDistance;
}
```

### Matchmaking System

**Rating System:**
- MMR (Matchmaking Rating) based on:
  - Kill/Death ratio (30%)
  - Extraction success rate (40%)
  - Average loot value extracted (20%)
  - Survival time (10%)

**Queue Types:**
- Solo: Individual players
- Duo: 2-player squads
- Squad: 3-4 player teams
- Ranked: Competitive with visible rating

---

## Technical Specification

### Core Classes Architecture

```cpp
// Class hierarchy
AActor
├── AExtractionCharacter (Player/AI character)
├── AExtractionWeapon (Base weapon class)
│   ├── ARangedWeapon
│   │   ├── AAssaultRifle
│   │   ├── ASMG
│   │   └── ASniperRifle
│   └── AMeleeWeapon
├── AExtractionZone (Extraction points)
├── ALootContainer (Searchable containers)
└── AExtractionGameMode (Game rules)

UActorComponent
├── UInventoryComponent
├── UHealthComponent
├── UStaminaComponent
└── URotationComponent

UGameInstanceSubsystem
├── UMatchmakingSubsystem
├── UProgressionSubsystem
└── UEconomySubsystem
```

### Character System

```cpp
// AExtractionCharacter.h
UCLASS()
class EXTRACTION_API AExtractionCharacter : public ACharacter
{
    GENERATED_BODY()
    
public:
    AExtractionCharacter();
    
    virtual void Tick(float DeltaTime) override;
    virtual void SetupPlayerInputComponent(
        UInputComponent* PlayerInputComponent) override;
    
    // Components
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    UInventoryComponent* InventoryComponent;
    
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    UHealthComponent* HealthComponent;
    
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    UStaminaComponent* StaminaComponent;
    
    // Combat
    UPROPERTY(Replicated)
    AExtractionWeapon* CurrentWeapon;
    
    UFUNCTION(Server, Reliable, WithValidation)
    void ServerFire(FVector TargetLocation);
    
    UFUNCTION(NetMulticast, Reliable)
    void MulticastPlayFireEffects();
    
    // Movement
    UFUNCTION()
    void Sprint();
    
    UFUNCTION()
    void StopSprint();
    
    // Interaction
    UFUNCTION(Server, Reliable, WithValidation)
    void ServerInteract(AActor* InteractableActor);
    
protected:
    virtual void BeginPlay() override;
    
    UPROPERTY(Replicated)
    float Health;
    
    UPROPERTY(Replicated)
    float Armor;
    
    UPROPERTY(Replicated)
    bool bIsAiming;
    
    UPROPERTY(Replicated)
    bool bIsSprinting;
    
private:
    void HandleMovementInput(FVector2D Input);
    void HandleAimInput(FVector2D Input);
    void UpdateRotation(float DeltaTime);
};
```

### Weapon System

```cpp
// AExtractionWeapon.h
UCLASS(Abstract)
class EXTRACTION_API AExtractionWeapon : public AActor
{
    GENERATED_BODY()
    
public:
    UPROPERTY(EditDefaultsOnly, Category = "Weapon Stats")
    float Damage;
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon Stats")
    float FireRate; // Rounds per minute
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon Stats")
    int32 MagazineSize;
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon Stats")
    float ReloadTime;
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon Stats")
    float EffectiveRange;
    
    UPROPERTY(EditDefaultsOnly, Category = "Weapon Stats")
    TSubclassOf<UDamageType> DamageType;
    
    UFUNCTION(BlueprintCallable)
    virtual void Fire();
    
    UFUNCTION(BlueprintCallable)
    virtual void Reload();
    
    UFUNCTION(BlueprintCallable)
    bool CanFire() const;
    
protected:
    UPROPERTY(Replicated)
    int32 CurrentAmmo;
    
    UPROPERTY()
    float LastFireTime;
    
    UPROPERTY()
    bool bIsReloading;
    
    virtual void ProcessHit(const FHitResult& Hit);
    virtual void ApplyRecoil();
    virtual void PlayFireEffects();
};
```

### Damage System

```cpp
// UHealthComponent.h
UCLASS(ClassGroup = (Custom), meta = (BlueprintSpawnableComponent))
class EXTRACTION_API UHealthComponent : public UActorComponent
{
    GENERATED_BODY()
    
public:
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Replicated)
    float MaxHealth = 100.0f;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Replicated)
    float CurrentHealth;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Replicated)
    float MaxArmor = 100.0f;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Replicated)
    float CurrentArmor;
    
    UFUNCTION()
    void TakeDamage(float Damage, EDamageType DamageType, 
        AActor* DamageCauser);
    
    UFUNCTION()
    void Heal(float Amount);
    
    UFUNCTION()
    void RepairArmor(float Amount);
    
    UFUNCTION()
    bool IsDead() const { return CurrentHealth <= 0.0f; }
    
    DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(
        FOnHealthChanged, float, NewHealth, float, Delta);
    UPROPERTY(BlueprintAssignable)
    FOnHealthChanged OnHealthChanged;
    
    DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnDeath);
    UPROPERTY(BlueprintAssignable)
    FOnDeath OnDeath;
    
protected:
    virtual void BeginPlay() override;
    
    UFUNCTION()
    void OnRep_Health();
    
    UFUNCTION()
    void OnRep_Armor();
    
private:
    float CalculateArmorAbsorption(float IncomingDamage);
};
```

### AI System

```cpp
// AExtractionAICharacter.h
UCLASS()
class EXTRACTION_API AExtractionAICharacter : public AExtractionCharacter
{
    GENERATED_BODY()
    
public:
    UPROPERTY(EditAnywhere, Category = "AI")
    EAIDifficulty Difficulty;
    
    UPROPERTY(EditAnywhere, Category = "AI")
    float DetectionRange = 2000.0f;
    
    UPROPERTY(EditAnywhere, Category = "AI")
    float AttackRange = 1500.0f;
    
    UPROPERTY(EditAnywhere, Category = "AI Loot")
    TArray<FLootTableEntry> LootTable;
    
protected:
    UPROPERTY()
    AActor* CurrentTarget;
    
    UPROPERTY()
    FVector PatrolDestination;
    
    UFUNCTION()
    void UpdateAI(float DeltaTime);
    
    UFUNCTION()
    AActor* FindNearestThreat();
    
    UFUNCTION()
    void EngageTarget();
    
    UFUNCTION()
    void Patrol();
    
    UFUNCTION()
    void TakeCover();
};
```

### Mobile Input System

```cpp
// Mobile-optimized input handling
UCLASS()
class EXTRACTION_API UMobileInputComponent : public UActorComponent
{
    GENERATED_BODY()
    
public:
    // Virtual joystick for movement
    UPROPERTY(EditAnywhere, Category = "Input")
    FVector2D MovementJoystickPosition;
    
    UPROPERTY(EditAnywhere, Category = "Input")
    float JoystickDeadzone = 0.15f;
    
    // Aim assist for mobile
    UPROPERTY(EditAnywhere, Category = "Aim Assist")
    bool bEnableAimAssist = true;
    
    UPROPERTY(EditAnywhere, Category = "Aim Assist")
    float AimAssistRange = 800.0f;
    
    UPROPERTY(EditAnywhere, Category = "Aim Assist")
    float AimAssistStrength = 0.4f;
    
    UFUNCTION()
    FVector2D GetMovementInput() const;
    
    UFUNCTION()
    AActor* GetAimAssistTarget() const;
    
    UFUNCTION()
    FVector GetAimAssistAdjustedDirection(FVector BaseDirection);
    
private:
    AActor* FindBestAimAssistTarget();
    float CalculateTargetScore(AActor* Target);
};
```

---

## Map Design

### Map Structure

**Zone Types:**

1. **Hot Zones** (High Risk/Reward)
   - Dense loot spawns
   - AI patrols
   - Central locations
   - Multiple entry points

2. **Mid Zones** (Balanced)
   - Moderate loot
   - Scattered AI
   - Tactical positions
   - Cover-rich areas

3. **Edge Zones** (Low Risk/Reward)
   - Sparse loot
   - Few AI encounters
   - Spawn points
   - Extraction zones

### Map Size and Density

**Technical Specifications:**
- Map Size: 2000m x 2000m
- Playable Area: 1600m x 1600m
- POI (Points of Interest): 12-15 locations
- Loot Containers: 200-300 per map
- AI Spawn Points: 40-60

**Performance Targets:**
- Draw calls: < 2000
- Polygon count: < 2M on screen
- Texture memory: < 1GB
- Frame rate: 60 FPS on high-end, 30 FPS on mid-range

### Example Map Layout

**"Abandoned Industrial Zone"**

```
Map Zones:
1. Power Plant (Hot Zone) - Center
   - 3 floors
   - Dense loot spawns
   - Boss AI (Warden)
   - High-tier weapons

2. Warehouse District (Mid Zone) - West
   - Multiple buildings
   - Mixed loot
   - AI patrols
   - Good cover positions

3. Office Complex (Mid Zone) - East
   - Vertical gameplay
   - Quest items
   - Moderate AI presence

4. Parking Lots (Edge Zone) - North/South
   - Sparse loot
   - Open areas
   - 2 extraction zones
   - Minimal AI

5. Forest Perimeter (Edge Zone) - Borders
   - Natural cover
   - Spawn points
   - Extraction zones
   - Escape routes
```

### Dynamic Elements

**Time-based Events:**
- Supply drops at 5 and 10-minute marks
- Zone contamination (shrinking play area)
- Random event triggers (heavy rain, fog)

**Implementation:**

```cpp
// AExtractionGameState.h
UCLASS()
class EXTRACTION_API AExtractionGameState : public AGameStateBase
{
    GENERATED_BODY()
    
public:
    UPROPERTY(Replicated, BlueprintReadOnly)
    float MatchTimeRemaining;
    
    UPROPERTY(Replicated, BlueprintReadOnly)
    TArray<FVector> ActiveExtractionPoints;
    
    UPROPERTY(Replicated, BlueprintReadOnly)
    FVector ContaminationCenter;
    
    UPROPERTY(Replicated, BlueprintReadOnly)
    float ContaminationRadius;
    
    UFUNCTION()
    void TriggerSupplyDrop(FVector Location);
    
    UFUNCTION()
    void UpdateContamination(float DeltaTime);
    
    UFUNCTION()
    void ActivateRandomExtractions();
};
```

---

## Character Systems

### Operators (Playable Characters)

**Operator Classes:**

1. **Assault**
   - Role: Frontline combat
   - Ability: Combat Stim (+25% damage, 10 seconds)
   - Passive: +10% sprint speed
   - Starting gear: Assault rifle, grenades

2. **Support**
   - Role: Team sustain
   - Ability: Healing Drone (heals nearby allies)
   - Passive: +20% healing item effectiveness
   - Starting gear: SMG, medical supplies

3. **Recon**
   - Role: Information gathering
   - Ability: UAV Scan (reveals enemies in radius)
   - Passive: +15% movement speed while crouched
   - Starting gear: Silenced pistol, sensor mine

4. **Tank**
   - Role: Damage absorption
   - Ability: Riot Shield (blocks frontal damage)
   - Passive: +25% armor capacity
   - Starting gear: Shotgun, heavy armor

5. **Specialist**
   - Role: Utility and control
   - Ability: EMP Blast (disables electronics)
   - Passive: +2 inventory slots
   - Starting gear: Pistol, utility items

### Operator Progression

```cpp
// FOperatorData structure
USTRUCT(BlueprintType)
struct FOperatorData
{
    GENERATED_BODY()
    
    UPROPERTY()
    FString OperatorID;
    
    UPROPERTY()
    FText OperatorName;
    
    UPROPERTY()
    EOperatorClass Class;
    
    UPROPERTY()
    int32 Level = 1;
    
    UPROPERTY()
    int32 Experience = 0;
    
    UPROPERTY()
    TArray<FString> UnlockedAbilities;
    
    UPROPERTY()
    TArray<FSkillData> SkillTree;
    
    UPROPERTY()
    FOperatorStats BaseStats;
};

// Skill tree system
USTRUCT(BlueprintType)
struct FSkillData
{
    GENERATED_BODY()
    
    UPROPERTY()
    FString SkillID;
    
    UPROPERTY()
    FText SkillName;
    
    UPROPERTY()
    FText Description;
    
    UPROPERTY()
    int32 RequiredLevel;
    
    UPROPERTY()
    int32 PointCost;
    
    UPROPERTY()
    bool bIsUnlocked = false;
    
    UPROPERTY()
    TArray<FStatModifier> StatModifiers;
};
```

---

## Progression and Economy

### Player Progression

**Level System:**
- Max Level: 100
- Experience sources:
  - Kills: 50 XP
  - Extractions: 200 XP
  - Loot extracted: 1 XP per value point
  - Quests completed: Variable
  - Survival time: 10 XP per minute

**Prestige System:**
- Reset to Level 1 at Level 100
- Unlock exclusive cosmetics
- Permanent stat bonuses
- Prestige-only quests

### Economy System

**Currency Types:**

1. **Credits** (Soft Currency)
   - Earned from extracting loot
   - Used for purchasing common items
   - Trading with vendors

2. **Tokens** (Premium Currency)
   - Purchased with real money
   - Used for cosmetics and convenience
   - Battle pass progression

3. **Reputation** (Faction Currency)
   - Earned from faction quests
   - Unlocks faction-specific items
   - 4 factions with unique vendors

**Marketplace System:**

```cpp
// UEconomySubsystem.h
UCLASS()
class EXTRACTION_API UEconomySubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()
    
public:
    UFUNCTION(BlueprintCallable)
    bool PurchaseItem(const FString& ItemID, int32 Quantity);
    
    UFUNCTION(BlueprintCallable)
    bool SellItem(const FString& ItemID, int32 Quantity);
    
    UFUNCTION(BlueprintCallable)
    int32 GetItemPrice(const FString& ItemID);
    
    UFUNCTION(BlueprintCallable)
    void AddCurrency(ECurrencyType Type, int32 Amount);
    
    UFUNCTION(BlueprintCallable)
    bool RemoveCurrency(ECurrencyType Type, int32 Amount);
    
    UFUNCTION(BlueprintCallable)
    int32 GetCurrencyAmount(ECurrencyType Type) const;
    
protected:
    UPROPERTY()
    TMap<ECurrencyType, int32> PlayerCurrencies;
    
    UPROPERTY()
    TMap<FString, int32> MarketPrices;
    
    void UpdateMarketPrices();
    void SaveEconomyData();
};
```

### Quest System

**Quest Types:**

1. **Daily Quests** (Reset every 24 hours)
   - Extract X value of loot
   - Kill X enemies
   - Extract from specific zone

2. **Weekly Quests** (Reset every 7 days)
   - More challenging objectives
   - Better rewards
   - Multiple objectives

3. **Story Quests** (One-time)
   - Narrative progression
   - Unlock new content
   - Unique rewards

4. **Faction Quests** (Repeatable)
   - Faction reputation
   - Faction-specific rewards
   - Conflict with other factions

**Implementation:**

```cpp
// FQuestData structure
USTRUCT(BlueprintType)
struct FQuestData
{
    GENERATED_BODY()
    
    UPROPERTY()
    FString QuestID;
    
    UPROPERTY()
    FText QuestName;
    
    UPROPERTY()
    FText Description;
    
    UPROPERTY()
    EQuestType QuestType;
    
    UPROPERTY()
    TArray<FQuestObjective> Objectives;
    
    UPROPERTY()
    TArray<FQuestReward> Rewards;
    
    UPROPERTY()
    bool bIsCompleted = false;
    
    UPROPERTY()
    FDateTime ExpirationTime;
};

USTRUCT(BlueprintType)
struct FQuestObjective
{
    GENERATED_BODY()
    
    UPROPERTY()
    FText ObjectiveText;
    
    UPROPERTY()
    EObjectiveType Type; // Kill, Extract, Loot, Survive
    
    UPROPERTY()
    int32 RequiredAmount;
    
    UPROPERTY()
    int32 CurrentProgress;
    
    UPROPERTY()
    TMap<FString, FString> ObjectiveParameters;
};
```

---

## User Interface

### Mobile UI Design Principles

**Optimization for Touch:**
- Minimum button size: 60x60 pixels
- Edge placement for thumbs
- Minimal UI clutter
- Context-sensitive buttons
- Scalable UI elements

### Main Menu Screens

**1. Home Screen**
- Operator selection
- Loadout management
- Play button (prominent)
- Daily rewards banner
- Quest tracker
- Social panel (friends, chat)
- Store button
- Settings

**2. Loadout Screen**
- Weapon selection (primary, secondary, melee)
- Equipment slots (armor, backpack, gear)
- Perks selection
- Saved loadouts
- Stat preview

**3. Stash Screen**
- Grid-based inventory
- Filter and sort options
- Item details panel
- Quick sell
- Crafting access

**4. Store Screen**
- Featured items
- Categories (weapons, equipment, cosmetics)
- Currency display
- Bundle deals

### In-Game HUD

**HUD Elements:**

```cpp
// UExtractionHUD.h
UCLASS()
class EXTRACTION_API UExtractionHUD : public AHUD
{
    GENERATED_BODY()
    
protected:
    // Core UI elements
    UPROPERTY(EditAnywhere, Category = "Widgets")
    TSubclassOf<UUserWidget> HealthBarWidgetClass;
    
    UPROPERTY(EditAnywhere, Category = "Widgets")
    TSubclassOf<UUserWidget> MinimapWidgetClass;
    
    UPROPERTY(EditAnywhere, Category = "Widgets")
    TSubclassOf<UUserWidget> AmmoCounterWidgetClass;
    
    UPROPERTY(EditAnywhere, Category = "Widgets")
    TSubclassOf<UUserWidget> InteractionPromptWidgetClass;
    
    // Virtual controls
    UPROPERTY(EditAnywhere, Category = "Widgets")
    TSubclassOf<UUserWidget> VirtualJoystickWidgetClass;
    
    UPROPERTY(EditAnywhere, Category = "Widgets")
    TSubclassOf<UUserWidget> ActionButtonsWidgetClass;
    
public:
    UFUNCTION(BlueprintCallable)
    void ShowExtractionTimer(float Duration);
    
    UFUNCTION(BlueprintCallable)
    void UpdateKillFeed(const FString& KillerName, 
        const FString& VictimName);
    
    UFUNCTION(BlueprintCallable)
    void ShowLootNotification(const FItemData& Item);
};
```

**HUD Layout:**

```
Top Left:
- Health bar (horizontal)
- Armor bar (horizontal)
- Stamina bar (horizontal)
- Active effects/buffs

Top Right:
- Match timer
- Extraction available indicator
- Player count

Bottom Left:
- Movement joystick (virtual)
- Crouch button
- Interaction prompt

Bottom Right:
- Fire button (large)
- Reload button
- Weapon swap
- Inventory button
- Settings

Center:
- Crosshair/aim indicator
- Hit markers
- Damage indicators (directional)
- Kill feed
- Objective markers

Mini-map (Top Center or Corner):
- Player position
- Squad members
- Extraction zones
- Points of interest
```

### UI Widget Components

```cpp
// UHealthBarWidget.h
UCLASS()
class EXTRACTION_API UHealthBarWidget : public UUserWidget
{
    GENERATED_BODY()
    
protected:
    UPROPERTY(meta = (BindWidget))
    UProgressBar* HealthProgressBar;
    
    UPROPERTY(meta = (BindWidget))
    UProgressBar* ArmorProgressBar;
    
    UPROPERTY(meta = (BindWidget))
    UTextBlock* HealthText;
    
public:
    UFUNCTION(BlueprintCallable)
    void UpdateHealth(float Current, float Max);
    
    UFUNCTION(BlueprintCallable)
    void UpdateArmor(float Current, float Max);
    
    UFUNCTION()
    void ShowDamageFlash();
};
```

---

## Monetization Strategy

### Business Model

**Free-to-Play with Optional Purchases**

**Non-Pay-to-Win Principles:**
- No purchasable gameplay advantages
- All operators unlockable through gameplay
- Weapons not purchasable (only earnable)
- Fair matchmaking regardless of spending

### Revenue Streams

**1. Battle Pass** (Seasonal)
- Price: $9.99 USD
- 100 tiers of rewards
- Free and premium tracks
- Cosmetics, operators, currency
- XP boosters (not power increases)

**2. Cosmetic Store**
- Operator skins: $5-15 USD
- Weapon skins: $3-10 USD
- Emotes and animations: $2-5 USD
- Bundle deals: $20-30 USD

**3. Convenience Items**
- Stash expansion: $4.99 USD
- Loadout slots: $2.99 USD
- Battle pass tier skips: $1.00 USD each

**4. Premium Currency (Tokens)**
- $4.99 USD = 500 tokens
- $9.99 USD = 1,100 tokens (+10% bonus)
- $19.99 USD = 2,400 tokens (+20% bonus)
- $49.99 USD = 6,500 tokens (+30% bonus)

### Retention Mechanics

**Daily Login Rewards:**
- Day 1-6: Small rewards (credits, consumables)
- Day 7: Larger reward (operator unlock, premium currency)
- Monthly cumulative rewards

**Limited-Time Events:**
- Seasonal events (2-3 weeks)
- Unique game modes
- Exclusive rewards
- Increased engagement

**Social Features:**
- Friend referral bonuses
- Squad play bonuses (+10% XP)
- Clan system
- Leaderboards

---

## Audio Design

### Sound Categories

**1. Combat Audio**
- Weapon firing (distinct per weapon class)
- Bullet impacts (varied by material)
- Explosions and grenades
- Ability activations
- Melee combat

**2. Environmental Audio**
- Footsteps (varied by surface)
- Door opening/closing
- Container looting
- Weather effects
- Ambient zone sounds

**3. UI Audio**
- Menu navigation
- Button clicks
- Notifications
- Item pickup
- Extraction countdown

**4. Voice Lines**
- Operator callouts
- Extraction alerts
- Enemy spotted
- Low health warnings
- Quest updates

### Audio Implementation

```cpp
// UAudioManager.h
UCLASS()
class EXTRACTION_API UAudioManager : public UGameInstanceSubsystem
{
    GENERATED_BODY()
    
public:
    UFUNCTION(BlueprintCallable)
    void PlayWeaponSound(USoundBase* Sound, FVector Location);
    
    UFUNCTION(BlueprintCallable)
    void PlayFootstepSound(EPhysicalSurface Surface, FVector Location);
    
    UFUNCTION(BlueprintCallable)
    void PlayUISound(USoundBase* Sound);
    
    UFUNCTION(BlueprintCallable)
    void UpdateAudioListener(FVector Location, FRotator Rotation);
    
protected:
    UPROPERTY()
    TMap<EPhysicalSurface, USoundBase*> FootstepSounds;
    
    UPROPERTY()
    USoundMix* CombatSoundMix;
    
    UPROPERTY()
    USoundMix* MenuSoundMix;
    
    void ApplySoundAttenuation(UAudioComponent* AudioComp, 
        float Distance);
};
```

### Audio Budget (Mobile)

**Memory Limits:**
- Total audio memory: 150 MB
- Streaming audio buffer: 30 MB
- Simultaneous sources: 32 channels

**Optimization:**
- Compressed audio (Vorbis/Opus)
- Streaming for music/ambient
- Distance-based culling
- Priority system for audio sources

---

## Performance Optimization

### Mobile Performance Targets

**Target Devices:**
- High-end: iPhone 13+, Samsung S21+ (60 FPS)
- Mid-range: iPhone 11, Samsung S10 (30-60 FPS)
- Low-end: iPhone 8, Samsung A50 (30 FPS)

**Quality Settings:**

```cpp
// Graphics quality presets
enum class EGraphicsQuality : uint8
{
    Low,      // 30 FPS, reduced effects
    Medium,   // 30-45 FPS, balanced
    High,     // 45-60 FPS, enhanced visuals
    Ultra     // 60 FPS, maximum quality
};

// Auto-detect device capability
void UGraphicsSettings::AutoDetectQuality()
{
    int32 DeviceScore = CalculateDeviceScore();
    
    if (DeviceScore >= 8000)
        SetQuality(EGraphicsQuality::Ultra);
    else if (DeviceScore >= 5000)
        SetQuality(EGraphicsQuality::High);
    else if (DeviceScore >= 3000)
        SetQuality(EGraphicsQuality::Medium);
    else
        SetQuality(EGraphicsQuality::Low);
}
```

### Rendering Optimization

**Techniques:**
- LOD (Level of Detail) system
- Occlusion culling
- Dynamic resolution scaling
- Texture streaming
- Light baking for static objects
- Particle system pooling

**Implementation:**

```cpp
// LOD Configuration
USTRUCT()
struct FLODConfig
{
    UPROPERTY()
    float LOD0Distance = 500.0f;   // High detail
    
    UPROPERTY()
    float LOD1Distance = 1500.0f;  // Medium detail
    
    UPROPERTY()
    float LOD2Distance = 3000.0f;  // Low detail
    
    UPROPERTY()
    float CullDistance = 5000.0f;  // Beyond this, cull
};
```

### Network Optimization

**Bandwidth Management:**
- Adaptive tick rate (10-30 Hz)
- Prioritized replication
- Delta compression
- Relevancy filtering

**Update Frequency:**
- Critical updates: 30 Hz (player position, combat)
- Standard updates: 10 Hz (inventory, objectives)
- Low priority: 2 Hz (cosmetics, emotes)

```cpp
// Network update frequency
void AExtractionCharacter::GetLifetimeReplicatedProps(
    TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    
    // 30 Hz updates
    DOREPLIFETIME_CONDITION(AExtractionCharacter, Location, 
        COND_None);
    DOREPLIFETIME_CONDITION(AExtractionCharacter, Rotation, 
        COND_SkipOwner);
    
    // 10 Hz updates
    DOREPLIFETIME_CONDITION_NOTIFY(AExtractionCharacter, Health,
        COND_None, REPNOTIFY_Always);
    
    // On-change only
    DOREPLIFETIME_CONDITION(AExtractionCharacter, CurrentWeapon,
        COND_InitialOnly);
}
```

### Memory Management

**Memory Budget:**
- Total app size: < 2 GB
- Runtime memory: < 1.5 GB
- Texture memory: < 800 MB
- Audio memory: < 150 MB
- Code and assets: < 1.2 GB

**Asset Streaming:**

```cpp
// Streamable asset management
UCLASS()
class EXTRACTION_API UAssetStreamingManager : public UGameInstanceSubsystem
{
    GENERATED_BODY()
    
public:
    UFUNCTION()
    void PreloadMapAssets(const FString& MapName);
    
    UFUNCTION()
    void UnloadUnusedAssets();
    
    UFUNCTION()
    void SetMemoryBudget(int64 MaxMemoryBytes);
    
protected:
    UPROPERTY()
    TArray<FSoftObjectPath> LoadedAssets;
    
    UPROPERTY()
    TSharedPtr<FStreamableManager> StreamableManager;
    
    void MonitorMemoryUsage();
    void PrioritizeAssetLoading();
};
```

### Battery Optimization

**Power Saving Measures:**
- Reduce frame rate when idle
- Dim screen during menus
- Throttle network updates in background
- Efficient lighting calculations
- Shader complexity reduction

---

## Development Roadmap

### Phase 1: Core Development (Months 1-4)

**Month 1-2: Foundation**
- Project setup in UE5
- Core character controller
- Basic movement and combat
- Network architecture foundation
- Mobile input system

**Month 3-4: Core Systems**
- Inventory system
- Loot system
- AI enemies
- Weapon variety (5 weapons)
- Health and damage system
- Single map (prototype)

**Deliverable:** Playable prototype with core loop

### Phase 2: Content Creation (Months 5-7)

**Month 5-6: Expansion**
- 3 playable operators
- 15+ weapons
- 2 complete maps
- Extraction mechanics
- Matchmaking system
- Basic UI/UX

**Month 7: Polish**
- Balance tuning
- Bug fixing
- Performance optimization
- Audio implementation
- Visual effects

**Deliverable:** Alpha build for internal testing

### Phase 3: Testing and Refinement (Months 8-10)

**Month 8: Closed Alpha**
- 50-100 testers
- Feedback collection
- Critical bug fixes
- Balance adjustments

**Month 9: Open Beta**
- Public testing
- Server stress testing
- Monetization testing
- Community feedback
- Extended content (operators, weapons)

**Month 10: Pre-Launch**
- Final optimization
- Content completion
- Store implementation
- Marketing materials

**Deliverable:** Release candidate

### Phase 4: Launch and Live Service (Month 11+)

**Month 11: Soft Launch**
- Limited region release
- Monitor metrics
- Quick iteration
- Community building

**Month 12: Global Launch**
- Worldwide release
- Marketing campaign
- Launch events
- Content roadmap announcement

**Post-Launch (Ongoing):**
- Season 1 (Month 13-15)
  - New operators (2)
  - New map
  - Battle Pass
  - Balance patches

- Season 2 (Month 16-18)
  - New game mode
  - Operators (2)
  - Map updates
  - Weapon additions

- Season 3+ (Month 19+)
  - Continued content
  - Major feature additions
  - Community events

### Development Team Structure

**Core Team (Minimum):**
- 1 Lead Programmer (UE5 C++)
- 2 Gameplay Programmers
- 1 Network Programmer
- 1 UI/UX Programmer
- 2 3D Artists (characters, weapons)
- 1 Environment Artist
- 1 Technical Artist
- 1 Game Designer
- 1 Level Designer
- 1 Sound Designer
- 1 QA Lead
- 1 Product Manager

**Extended Team:**
- Contract artists for cosmetics
- Community manager
- Marketing specialist
- Additional QA testers

---

## Technical Requirements

### Minimum System Requirements (Mobile)

**iOS:**
- Device: iPhone 8 or newer
- OS: iOS 14.0 or later
- RAM: 3 GB
- Storage: 2 GB available

**Android:**
- Device: Snapdragon 660 or equivalent
- OS: Android 9.0 or later
- RAM: 3 GB
- Storage: 2 GB available

### Recommended Specifications

**iOS:**
- Device: iPhone 11 or newer
- OS: iOS 15.0 or later
- RAM: 4 GB+
- Storage: 3 GB available

**Android:**
- Device: Snapdragon 845 or equivalent
- OS: Android 11.0 or later
- RAM: 6 GB+
- Storage: 3 GB available

### Backend Infrastructure

**Server Requirements:**
- Dedicated game servers (AWS/GCP)
- Database: PostgreSQL for player data
- Redis for session management
- CDN for asset delivery
- Analytics platform (GameAnalytics, Firebase)
- Crash reporting (Sentry, Crashlytics)

**Scalability:**
- Auto-scaling server instances
- Global server regions
- Load balancing
- DDoS protection

---

## Risk Assessment and Mitigation

### Technical Risks

**1. Mobile Performance**
- Risk: Game doesn't run well on target devices
- Mitigation: Early profiling, scalable quality settings, regular device testing

**2. Network Latency**
- Risk: Poor multiplayer experience in high-latency regions
- Mitigation: Regional servers, lag compensation, client prediction

**3. Cheating**
- Risk: Exploits and hacks ruin competitive integrity
- Mitigation: Server-authoritative design, anti-cheat systems, regular updates

### Design Risks

**1. Balance Issues**
- Risk: Weapons/operators become meta-dominant
- Mitigation: Regular balance patches, community feedback, data analytics

**2. Retention**
- Risk: Players lose interest quickly
- Mitigation: Engaging progression, regular content updates, events

**3. Monetization Backlash**
- Risk: Community perceives game as pay-to-win
- Mitigation: Cosmetic-only purchases, transparent communication

### Business Risks

**1. Market Competition**
- Risk: Competing against established titles
- Mitigation: Unique features, quality polish, strong marketing

**2. Development Delays**
- Risk: Missing launch windows
- Mitigation: Agile development, realistic timelines, prioritized features

**3. Budget Overruns**
- Risk: Development costs exceed budget
- Mitigation: Milestone-based development, regular budget reviews

---

## Success Metrics

### Key Performance Indicators (KPIs)

**Player Engagement:**
- Daily Active Users (DAU)
- Monthly Active Users (MAU)
- DAU/MAU Ratio (target: 20%+)
- Average session length (target: 15+ minutes)
- Sessions per day (target: 2+)

**Retention:**
- Day 1 retention (target: 40%+)
- Day 7 retention (target: 20%+)
- Day 30 retention (target: 10%+)

**Monetization:**
- ARPDAU (Average Revenue Per Daily Active User)
- Conversion rate (target: 3-5%)
- ARPPU (Average Revenue Per Paying User)
- LTV (Lifetime Value)

**Technical:**
- Crash rate (target: <1%)
- Average FPS (target: 30+ on mid-range)
- Server uptime (target: 99.5%+)
- Average match wait time (target: <60 seconds)

---

## Appendix

### Glossary

- **Extraction:** The process of leaving the map with collected loot
- **Hot Zone:** High-risk, high-reward areas with dense loot and enemies
- **Operator:** Playable character class with unique abilities
- **Stash:** Player's permanent storage for extracted items
- **MMR:** Matchmaking Rating, used for skill-based matchmaking
- **KDA:** Kill/Death/Assist ratio
- **POI:** Point of Interest, notable locations on the map

### Reference Materials

**Similar Games:**
- Escape from Tarkov (PC)
- The Cycle: Frontier (PC)
- Vigor (Console/PC)

**Technical References:**
- Unreal Engine Documentation
- Unreal Multiplayer Networking Guide
- Mobile Development Best Practices
- Anti-Cheat Implementation Guides

### Contact and Feedback

**Development Team Contact:**
- Lead Designer: [Contact Info]
- Technical Director: [Contact Info]
- Product Manager: [Contact Info]

**Document Version Control:**
- Version 1.0 - Initial Draft (Feb 6, 2026)
- Living document - Updated regularly during development

---

**End of Game Design Document**
