# Networking System

**[← Previous: Architecture](./01_Architecture.md)** | **[Technical Index](./README.md)** | **[Next: Character System →](./03_CharacterSystem.md)**

---

## Network Architecture Overview

**Model:** Dedicated Server Architecture  
**Authority:** Server Authoritative  
**Topology:** Client-Server (Star)  
**Protocol:** UDP with reliability layer  

---

## Server-Client Model

### Architecture Diagram

```
        ┌─────────┐
        │ Master  │
        │ Server  │  (Matchmaking, Lobbies)
        └────┬────┘
             │
      ┌──────┴──────┐
      │             │
  ┌───▼───┐     ┌───▼───┐
  │  Game │     │  Game │  (Dedicated Game Servers)
  │Server1│     │Server2│
  └───┬───┘     └───┬───┘
      │             │
  ┌───┼────┬────────┼────┐
  │   │    │        │    │
┌─▼─┐ │ ┌─▼─┐    ┌─▼─┐  │
│C1 │ │ │C2 │    │C3 │  │  (Clients)
└───┘ │ └───┘    └───┘  │
    ┌─▼─┐             ┌─▼─┐
    │C4 │             │C5 │
    └───┘             └───┘
```

---

## Server Authority

### Server Responsibilities

**Authoritative on:**
- All gameplay state
- Character positions (with client prediction)
- Combat calculations (damage, hits)
- Loot spawning và distribution
- Match flow (timer, events)
- Win/loss conditions
- Anti-cheat validation

**Implementation:**
```cpp
// Server validates all important actions
UFUNCTION(Server, Reliable, WithValidation)
void AExtractionCharacter::ServerFire_Implementation(
    const FVector& TargetLocation)
{
    // Server performs actual hit detection
    FHitResult HitResult;
    FVector Start = GetActorLocation();
    FVector End = TargetLocation;
    
    GetWorld()->LineTraceSingleByChannel(
        HitResult, Start, End, ECC_Visibility);
    
    if (HitResult.bBlockingHit)
    {
        // Server applies damage
        if (AExtractionCharacter* HitChar = 
            Cast<AExtractionCharacter>(HitResult.GetActor()))
        {
            HitChar->TakeDamage(WeaponDamage, ...);
        }
        
        // Server broadcasts to all clients
        MulticastPlayFireEffects(HitResult.Location);
    }
}

bool AExtractionCharacter::ServerFire_Validate(
    const FVector& TargetLocation)
{
    // Anti-cheat: Validate reasonable target
    float Distance = FVector::Distance(
        GetActorLocation(), TargetLocation);
    
    // Reject if beyond weapon range
    return Distance <= CurrentWeapon->MaxRange * 1.2f;
}
```

---

## Replication

### Replication Strategy

**High Priority (30 Hz):**
- Character Transform (Location, Rotation)
- Health/Armor values
- Weapon state (firing, ammo)
- Ability activation

**Medium Priority (10 Hz):**
- Inventory changes
- Quest progress
- Match state updates

**Low Priority (On-Change):**
- Cosmetics
- Emotes
- Non-critical UI data

---

### Property Replication

```cpp
// Character replication
void AExtractionCharacter::GetLifetimeReplicatedProps(
    TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    
    // Always replicate to all
    DOREPLIFETIME(AExtractionCharacter, Health);
    DOREPLIFETIME(AExtractionCharacter, Armor);
    DOREPLIFETIME(AExtractionCharacter, CurrentWeapon);
    
    // Replicate only to owner
    DOREPLIFETIME_CONDITION(AExtractionCharacter, Inventory, 
        COND_OwnerOnly);
    DOREPLIFETIME_CONDITION(AExtractionCharacter, Stamina, 
        COND_OwnerOnly);
    
    // Skip owner (they already know)
    DOREPLIFETIME_CONDITION(AExtractionCharacter, bIsAiming,
        COND_SkipOwner);
}

// RepNotify for state changes
UPROPERTY(ReplicatedUsing=OnRep_Health)
float Health;

UFUNCTION()
void AExtractionCharacter::OnRep_Health()
{
    // Update UI
    UpdateHealthUI();
    
    // Play effects
    if (Health < PreviousHealth)
    {
        PlayDamageEffects();
    }
    
    PreviousHealth = Health;
}
```

---

## Client-Side Prediction

### Movement Prediction

**Why:** Immediate feedback, hide latency

**Implementation:**
```cpp
void AExtractionCharacter::MoveForward(float Value)
{
    // Client predicts immediately
    AddMovementInput(GetActorForwardVector(), Value);
    
    // Send to server
    if (!HasAuthority())
    {
        ServerMove(Value, GetActorLocation(), 
            GetWorld()->GetTimeSeconds());
    }
}

UFUNCTION(Server, Unreliable)
void AExtractionCharacter::ServerMove_Implementation(
    float Value, FVector ClientLocation, float Timestamp)
{
    // Server executes move
    AddMovementInput(GetActorForwardVector(), Value);
    
    // Check for significant misprediction
    FVector ServerLocation = GetActorLocation();
    float Error = FVector::Distance(ClientLocation, ServerLocation);
    
    if (Error > 100.0f) // Threshold
    {
        // Force correction
        ClientCorrectPosition(ServerLocation, Timestamp);
    }
}

UFUNCTION(Client, Unreliable)
void AExtractionCharacter::ClientCorrectPosition_Implementation(
    FVector ServerLocation, float Timestamp)
{
    // Smoothly correct to server position
    SetActorLocation(ServerLocation);
    
    // Replay inputs since correction time (advanced)
    ReplayInputsSince(Timestamp);
}
```

---

## Lag Compensation

### Hit Registration

**Problem:** Client shoots where enemy WAS, not where they ARE

**Solution:** Server rewinds time for hit detection

```cpp
class ULagCompensationComponent : public UActorComponent
{
public:
    // Store position history
    struct FPositionHistory
    {
        FVector Location;
        FRotator Rotation;
        float Timestamp;
    };
    
    TArray<FPositionHistory> PositionHistory;
    static constexpr float HISTORY_LENGTH = 1.0f; // 1 second
    
    void RecordPosition(float DeltaTime)
    {
        PositionHistory.Add({
            GetOwner()->GetActorLocation(),
            GetOwner()->GetActorRotation(),
            GetWorld()->GetTimeSeconds()
        });
        
        // Remove old entries
        float MinTime = GetWorld()->GetTimeSeconds() - HISTORY_LENGTH;
        PositionHistory.RemoveAll([MinTime](const FPositionHistory& Entry) {
            return Entry.Timestamp < MinTime;
        });
    }
    
    FVector GetPositionAtTime(float TargetTime)
    {
        // Find bracketing positions
        for (int i = 0; i < PositionHistory.Num() - 1; i++)
        {
            if (PositionHistory[i].Timestamp <= TargetTime &&
                PositionHistory[i + 1].Timestamp >= TargetTime)
            {
                // Interpolate between positions
                float Alpha = (TargetTime - PositionHistory[i].Timestamp) /
                    (PositionHistory[i + 1].Timestamp - 
                     PositionHistory[i].Timestamp);
                
                return FMath::Lerp(
                    PositionHistory[i].Location,
                    PositionHistory[i + 1].Location,
                    Alpha
                );
            }
        }
        
        return GetOwner()->GetActorLocation();
    }
};

// Server-side hit validation
bool AExtractionGameMode::ValidateHit(
    AExtractionCharacter* Shooter,
    AExtractionCharacter* Victim,
    const FHitResult& ClientHit,
    float ClientTimestamp)
{
    // Get shooter's ping
    float RTT = Shooter->GetPlayerState()->ExactPing / 1000.0f;
    
    // Rewind to when shooter fired (client time)
    float ServerTime = GetWorld()->GetTimeSeconds();
    float HitTime = ServerTime - RTT;
    
    // Get victim's position at that time
    ULagCompensationComponent* LagComp = 
        Victim->FindComponentByClass<ULagCompensationComponent>();
    
    FVector VictimPosAtHit = LagComp->GetPositionAtTime(HitTime);
    
    // Validate hit
    FVector ShooterPos = Shooter->GetActorLocation();
    FVector ToVictim = VictimPosAtHit - ShooterPos;
    
    // Check if hit is plausible
    float Distance = ToVictim.Size();
    float AngleToHit = FMath::Acos(
        FVector::DotProduct(
            ToVictim.GetSafeNormal(),
            Shooter->GetActorForwardVector()
        )
    ) * 180.0f / PI;
    
    // Allow hit if within tolerance
    bool bValidDistance = Distance <= Shooter->CurrentWeapon->MaxRange;
    bool bValidAngle = AngleToHit <= 45.0f; // Reasonable aim cone
    
    return bValidDistance && bValidAngle;
}
```

---

## Matchmaking System

### Matchmaking Flow

```
Player clicks "Play"
    ↓
Add to matchmaking queue
    ↓
Find suitable match
    ↓
Create game session
    ↓
Assign players to server
    ↓
Load map
    ↓
Start match
```

---

### Implementation

```cpp
UCLASS()
class UMatchmakingSubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()
    
public:
    // Player joins queue
    UFUNCTION(BlueprintCallable)
    void JoinMatchmaking(EGameMode GameMode, ESquadSize SquadSize)
    {
        FMatchmakingRequest Request;
        Request.PlayerID = GetLocalPlayerID();
        Request.MMR = GetPlayerMMR();
        Request.GameMode = GameMode;
        Request.SquadSize = SquadSize;
        Request.Timestamp = FDateTime::Now();
        
        // Send to matchmaking server
        SendMatchmakingRequest(Request);
    }
    
    // Called when match found
    UFUNCTION()
    void OnMatchFound(const FMatchInfo& MatchInfo)
    {
        // Connect to game server
        UGameplayStatics::OpenLevel(
            this, 
            FName(*MatchInfo.ServerIP),
            true,
            TEXT("?SessionID=") + MatchInfo.SessionID
        );
    }
    
private:
    // MMR calculation
    float CalculateMMR()
    {
        float BaseMMR = 1000.0f;
        
        // Factors:
        // - Win rate (40%)
        // - Extraction rate (40%)
        // - Average loot value (10%)
        // - KD ratio (10%)
        
        float WinRate = GetWinRate();
        float ExtractRate = GetExtractionRate();
        float AvgLoot = GetAverageLootValue();
        float KD = GetKDRatio();
        
        return BaseMMR +
            (WinRate * 400.0f) +
            (ExtractRate * 400.0f) +
            (AvgLoot / 100.0f) +
            (KD * 100.0f);
    }
};
```

---

### Matchmaking Algorithm

**Skill-Based Matching:**
```cpp
struct FMatchmakingBucket
{
    float MinMMR;
    float MaxMMR;
    TArray<FMatchmakingRequest> Players;
    
    bool CanMatch(const FMatchmakingRequest& Request)
    {
        return Request.MMR >= MinMMR && Request.MMR <= MaxMMR;
    }
};

// Expand search over time
void ExpandMatchmakingRange(FMatchmakingRequest& Request)
{
    float TimeSinceQueue = (FDateTime::Now() - 
        Request.Timestamp).GetTotalSeconds();
    
    // Expand ±50 MMR per 15 seconds
    float Expansion = (TimeSinceQueue / 15.0f) * 50.0f;
    
    Request.MinMMR = Request.MMR - 100.0f - Expansion;
    Request.MaxMMR = Request.MMR + 100.0f + Expansion;
    
    // Cap expansion at ±500 MMR
    Request.MinMMR = FMath::Max(Request.MinMMR, Request.MMR - 500.0f);
    Request.MaxMMR = FMath::Min(Request.MaxMMR, Request.MMR + 500.0f);
}
```

---

## Network Optimization

### Bandwidth Management

**Target Bandwidth:**
- Per client: 128 kbps (upload + download)
- Server: 16 MB/s for 100 concurrent players

**Optimization Techniques:**

**1. Relevancy:**
```cpp
// Only replicate nearby actors
bool AExtractionCharacter::IsNetRelevantFor(
    const AActor* RealViewer,
    const AActor* ViewTarget,
    const FVector& SrcLocation) const
{
    // Always relevant to owner
    if (RealViewer == GetOwner())
        return true;
    
    // Check distance
    float Distance = FVector::Distance(
        GetActorLocation(), 
        SrcLocation
    );
    
    // Relevant within 5000 units (50m)
    return Distance <= 5000.0f;
}
```

**2. Update Frequency:**
```cpp
// Adaptive tick rate based on importance
void AExtractionCharacter::UpdateNetworkPriority()
{
    float Priority = 1.0f;
    
    // Increase priority if:
    // - In combat
    if (bIsInCombat)
        Priority *= 2.0f;
    
    // - Near local player
    if (bIsNearLocalPlayer)
        Priority *= 1.5f;
    
    // - Moving fast
    if (GetVelocity().Size() > 500.0f)
        Priority *= 1.3f;
    
    NetPriority = Priority;
}
```

**3. Delta Compression:**
```cpp
// Only send changed properties
DOREPLIFETIME_CONDITION(AExtractionCharacter, Health,
    COND_Custom); // Use custom condition

bool AExtractionCharacter::ReplicateSubobjects(
    UActorChannel* Channel,
    FOutBunch* Bunch,
    FReplicationFlags* RepFlags)
{
    bool bWroteSomething = Super::ReplicateSubobjects(
        Channel, Bunch, RepFlags);
    
    // Only replicate if health changed significantly
    if (FMath::Abs(Health - LastReplicatedHealth) > 1.0f)
    {
        bWroteSomething |= Channel->ReplicateSubobject(
            HealthComponent, *Bunch, *RepFlags);
        LastReplicatedHealth = Health;
    }
    
    return bWroteSomething;
}
```

---

## Anti-Cheat

### Server-Side Validation

**Movement Validation:**
```cpp
bool AExtractionGameMode::ValidateMovement(
    AExtractionCharacter* Character,
    const FVector& NewLocation,
    float DeltaTime)
{
    FVector OldLocation = Character->GetActorLocation();
    float Distance = FVector::Distance(OldLocation, NewLocation);
    float MaxDistance = Character->GetMaxMovementSpeed() * DeltaTime * 1.1f;
    
    // Reject impossible movement
    if (Distance > MaxDistance)
    {
        UE_LOG(LogTemp, Warning, 
            TEXT("Invalid movement detected: %s"), 
            *Character->GetName());
        
        // Force correction
        Character->SetActorLocation(OldLocation);
        return false;
    }
    
    return true;
}
```

**Weapon Fire Rate Validation:**
```cpp
bool AExtractionWeapon::CanFire() const
{
    float TimeSinceLastFire = GetWorld()->GetTimeSeconds() - LastFireTime;
    float MinTimeBetweenShots = 60.0f / FireRate; // RPM to seconds
    
    return TimeSinceLastFire >= MinTimeBetweenShots * 0.95f; // 5% tolerance
}

UFUNCTION(Server, Reliable, WithValidation)
void AExtractionWeapon::ServerFire_Implementation()
{
    if (!CanFire())
    {
        // Log potential speedhack
        LogSuspiciousActivity(GetOwner(), "Fire rate violation");
        return;
    }
    
    // Process shot...
}
```

**Loot Validation:**
```cpp
UFUNCTION(Server, Reliable, WithValidation)
void AExtractionCharacter::ServerPickupItem_Implementation(
    AActor* ItemActor)
{
    // Validate distance
    float Distance = FVector::Distance(
        GetActorLocation(),
        ItemActor->GetActorLocation()
    );
    
    if (Distance > 300.0f) // Max pickup range
    {
        LogSuspiciousActivity(this, "Teleport pickup");
        return;
    }
    
    // Validate item exists
    if (!IsValid(ItemActor))
    {
        LogSuspiciousActivity(this, "Invalid item pickup");
        return;
    }
    
    // Process pickup...
}

bool AExtractionCharacter::ServerPickupItem_Validate(AActor* ItemActor)
{
    return IsValid(ItemActor);
}
```

---

## Session Management

### Match Lifecycle

```cpp
UCLASS()
class AExtractionGameMode : public AGameModeBase
{
public:
    virtual void BeginPlay() override
    {
        Super::BeginPlay();
        
        // Initialize match
        MatchState = EMatchState::WaitingToStart;
        MatchTime = 0.0f;
        MaxMatchDuration = 900.0f; // 15 minutes
        
        // Wait for players
        if (GetNumPlayers() >= MinPlayers)
        {
            StartMatchTimer();
        }
    }
    
    void StartMatchTimer()
    {
        GetWorldTimerManager().SetTimer(
            MatchStartTimerHandle,
            this,
            &AExtractionGameMode::StartMatch,
            PreMatchDelay,
            false
        );
    }
    
    void StartMatch()
    {
        MatchState = EMatchState::InProgress;
        
        // Spawn players
        for (APlayerController* PC : PlayerControllers)
        {
            SpawnPlayer(PC);
        }
        
        // Start match timer
        GetWorldTimerManager().SetTimer(
            MatchUpdateTimerHandle,
            this,
            &AExtractionGameMode::UpdateMatch,
            1.0f,
            true
        );
        
        // Schedule events
        ScheduleSupplyDrops();
        ScheduleContamination();
    }
    
    void UpdateMatch()
    {
        MatchTime += 1.0f;
        
        // Update game state
        GetGameState<AExtractionGameState>()->MatchTimeRemaining = 
            MaxMatchDuration - MatchTime;
        
        // Check end conditions
        if (MatchTime >= MaxMatchDuration)
        {
            EndMatch();
        }
        else if (GetNumAlivePlayers() == 0)
        {
            EndMatch();
        }
    }
    
    void EndMatch()
    {
        MatchState = EMatchState::PostMatch;
        
        // Stop timers
        GetWorldTimerManager().ClearTimer(MatchUpdateTimerHandle);
        
        // Process results
        ProcessMatchResults();
        
        // Return to lobby after delay
        GetWorldTimerManager().SetTimer(
            ReturnToLobbyTimerHandle,
            this,
            &AExtractionGameMode::ReturnToLobby,
            10.0f,
            false
        );
    }
};
```

---

## TODO: Networking Tasks

### Phase 1 (HIGH Priority) 🔴
- [ ] Setup dedicated server configuration
- [ ] Implement basic character replication
- [ ] Client-side prediction for movement
- [ ] Server hit validation
- [ ] Basic matchmaking system

### Phase 2 (MEDIUM Priority) 🟡
- [ ] Lag compensation implementation
- [ ] Advanced replication (inventory, etc)
- [ ] Bandwidth optimization
- [ ] Anti-cheat systems
- [ ] Session management

### Phase 3 (LOW Priority) 🟢
- [ ] Reconnection handling
- [ ] Spectator mode
- [ ] Replay system
- [ ] Advanced matchmaking (MMR)
- [ ] Regional servers

---

**[← Previous: Architecture](./01_Architecture.md)** | **[Technical Index](./README.md)** | **[Next: Character System →](./03_CharacterSystem.md)**
