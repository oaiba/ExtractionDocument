---
title: Performance Optimization
type: docs
---


### Overview

This document defines the technical implementation of performance optimization systems for mobile platforms including device profiling, rendering settings, memory management, and profiling tools.

**Responsibilities:**

* Device tier detection and auto-configuration
* Rendering quality scaling
* Memory budget management
* Object pooling and tick optimization
* Performance monitoring and profiling

***

### Enums & Types

#### EDeviceTier

Device performance classification.

| Code Name      | Display Name | RAM Range | GPU Score | Target FPS | Resolution | Description      |
| -------------- | ------------ | --------- | --------- | ---------- | ---------- | ---------------- |
| `EDT_LowEnd`   | Low End      | < 4 GB    | < 5000    | 30 FPS     | 720p       | Budget devices   |
| `EDT_MidRange` | Mid Range    | 4-6 GB    | 5000-8000 | 45 FPS     | 900p       | Average devices  |
| `EDT_HighEnd`  | High End     | > 6 GB    | > 8000    | 60 FPS     | 1080p+     | Premium devices  |
| `EDT_Unknown`  | Unknown      | N/A       | N/A       | 30 FPS     | 720p       | Detection failed |

***

#### EQualityLevel

Graphics quality preset.

| Code Name    | Display Name | Shadows  | Textures | Effects  | Post-Process | Description         |
| ------------ | ------------ | -------- | -------- | -------- | ------------ | ------------------- |
| `EQL_Low`    | Low          | Off      | Low      | Minimal  | Off          | Maximum performance |
| `EQL_Medium` | Medium       | Simple   | Medium   | Reduced  | Basic        | Balanced            |
| `EQL_High`   | High         | Soft     | High     | Full     | Enhanced     | Best visuals        |
| `EQL_Ultra`  | Ultra        | Full     | Ultra    | Full     | Maximum      | PC/High-end only    |
| `EQL_Custom` | Custom       | Variable | Variable | Variable | Variable     | User-defined        |

***

#### ELODLevel

Level of Detail tier.

| Code Name     | Display Name | Distance | Triangle % | Texture Res | Tick Rate   | Description    |
| ------------- | ------------ | -------- | ---------- | ----------- | ----------- | -------------- |
| `ELOD_0`      | LOD 0        | 0-15m    | 100%       | Full        | Every frame | Maximum detail |
| `ELOD_1`      | LOD 1        | 15-50m   | 50%        | 75%         | 30 Hz       | High detail    |
| `ELOD_2`      | LOD 2        | 50-100m  | 25%        | 50%         | 10 Hz       | Medium detail  |
| `ELOD_3`      | LOD 3        | 100-200m | 10%        | 25%         | 2 Hz        | Low detail     |
| `ELOD_Culled` | Culled       | > 200m   | 0%         | None        | None        | Not rendered   |

***

#### EPoolType

Object pool category.

| Code Name        | Display Name | Initial Size | Max Size | Auto-Expand | Description         |
| ---------------- | ------------ | ------------ | -------- | ----------- | ------------------- |
| `EPT_Projectile` | Projectile   | 100          | 500      | Yes         | Bullets, rockets    |
| `EPT_Effect`     | Effect       | 50           | 200      | Yes         | VFX particles       |
| `EPT_Decal`      | Decal        | 100          | 300      | No          | Bullet holes, blood |
| `EPT_Audio`      | Audio        | 30           | 100      | Yes         | Sound emitters      |
| `EPT_AI`         | AI           | 20           | 50       | No          | AI pawns            |
| `EPT_Loot`       | Loot         | 50           | 200      | Yes         | Item pickups        |

***

#### EMemoryCategory

Memory budget category.

| Code Name       | Display Name | Budget (MB) | Priority | Streamable | Description            |
| --------------- | ------------ | ----------- | -------- | ---------- | ---------------------- |
| `EMC_Texture`   | Textures     | 800         | High     | Yes        | Texture data           |
| `EMC_Mesh`      | Meshes       | 200         | High     | Yes        | Static/skeletal meshes |
| `EMC_Audio`     | Audio        | 150         | Medium   | Yes        | Sound data             |
| `EMC_Animation` | Animation    | 100         | High     | No         | Animation data         |
| `EMC_Code`      | Code         | 300         | Critical | No         | Game code, shaders     |
| `EMC_Runtime`   | Runtime      | 250         | Medium   | No         | Runtime allocations    |

***

#### ETextureImportance

Texture streaming priority.

| Code Name       | Display Name | LOD Bias | Stream  | Max Size | Description         |
| --------------- | ------------ | -------- | ------- | -------- | ------------------- |
| `ETI_Critical`  | Critical     | 0        | Never   | 2048     | Characters, weapons |
| `ETI_Important` | Important    | 1        | Delayed | 1024     | Environment key     |
| `ETI_Normal`    | Normal       | 2        | Always  | 512      | Props, details      |
| `ETI_Optional`  | Optional     | 3        | Always  | 256      | Background elements |

***

#### ETickPriority

Actor tick rate classification.

| Code Name        | Display Name | Interval | Use Case   | CPU Cost | Description       |
| ---------------- | ------------ | -------- | ---------- | -------- | ----------------- |
| `ETP_EveryFrame` | Every Frame  | 0        | Player     | High     | Critical gameplay |
| `ETP_High`       | High         | 0.016s   | Nearby AI  | Medium   | 60 Hz updates     |
| `ETP_Medium`     | Medium       | 0.1s     | Mid-range  | Low      | 10 Hz updates     |
| `ETP_Low`        | Low          | 0.5s     | Far actors | Very Low | 2 Hz updates      |
| `ETP_Minimal`    | Minimal      | 1.0s     | Background | Minimal  | 1 Hz updates      |

***

#### EProfilingMode

Performance profiling mode.

| Code Name      | Display Name | Overhead | Detail         | Use Case   | Description     |
| -------------- | ------------ | -------- | -------------- | ---------- | --------------- |
| `EPM_Off`      | Off          | None     | None           | Production | No profiling    |
| `EPM_Basic`    | Basic        | < 1%     | FPS, Memory    | Dev        | Essential stats |
| `EPM_Detailed` | Detailed     | 2-5%     | Full breakdown | Debug      | Comprehensive   |
| `EPM_Capture`  | Capture      | 5-10%    | Frame capture  | Analysis   | Recording mode  |

***

### Code Names

#### Performance Events

| Code Name               | Trigger            | Parameters                      | Description             |
| ----------------------- | ------------------ | ------------------------------- | ----------------------- |
| `PERF_FPS_DROP`         | FPS below target   | CurrentFPS, TargetFPS, Duration | Performance degradation |
| `PERF_FPS_RECOVER`      | FPS recovered      | CurrentFPS, TargetFPS           | Performance restored    |
| `PERF_QUALITY_CHANGE`   | Quality adjusted   | OldLevel, NewLevel, Reason      | Auto-quality changed    |
| `PERF_RESOLUTION_SCALE` | Resolution changed | OldScale, NewScale              | Dynamic resolution      |

#### Memory Events

| Code Name           | Trigger           | Parameters             | Description                |
| ------------------- | ----------------- | ---------------------- | -------------------------- |
| `MEM_BUDGET_WARN`   | Near budget limit | Category, Used, Budget | Memory warning             |
| `MEM_BUDGET_EXCEED` | Budget exceeded   | Category, Used, Budget | Over budget                |
| `MEM_GC_START`      | GC triggered      | Reason                 | Garbage collection started |
| `MEM_GC_END`        | GC completed      | FreedMB, Duration      | Garbage collection done    |
| `MEM_STREAM_IN`     | Asset loaded      | AssetPath, SizeMB      | Asset streamed in          |
| `MEM_STREAM_OUT`    | Asset unloaded    | AssetPath, SizeMB      | Asset streamed out         |

#### Pool Events

| Code Name        | Trigger         | Parameters                 | Description             |
| ---------------- | --------------- | -------------------------- | ----------------------- |
| `POOL_ACQUIRE`   | Object acquired | PoolType, ActiveCount      | Object taken from pool  |
| `POOL_RELEASE`   | Object released | PoolType, ActiveCount      | Object returned to pool |
| `POOL_EXPAND`    | Pool expanded   | PoolType, OldSize, NewSize | Pool grew               |
| `POOL_EXHAUSTED` | Pool empty      | PoolType, RequestCount     | No objects available    |

#### LOD Events

| Code Name    | Trigger           | Parameters              | Description    |
| ------------ | ----------------- | ----------------------- | -------------- |
| `LOD_CHANGE` | LOD level changed | ActorID, OldLOD, NewLOD | LOD transition |
| `LOD_CULL`   | Actor culled      | ActorID, Distance       | Actor hidden   |
| `LOD_UNCULL` | Actor visible     | ActorID, Distance       | Actor shown    |

#### Device Events

| Code Name           | Trigger         | Parameters            | Description        |
| ------------------- | --------------- | --------------------- | ------------------ |
| `DEV_TIER_DETECTED` | Tier determined | Tier, Score, RAM, GPU | Device classified  |
| `DEV_THERMAL_WARN`  | Device heating  | Temperature, Throttle | Thermal throttling |
| `DEV_BATTERY_LOW`   | Battery low     | Percent, PowerSaver   | Low battery mode   |

***

### Mobile Performance Targets

#### Frame Rate Targets

| Device Tier | Target FPS | Minimum FPS | Resolution      |
| ----------- | ---------- | ----------- | --------------- |
| High-end    | 60 FPS     | 55 FPS      | Native (1080p+) |
| Mid-range   | 45 FPS     | 40 FPS      | 900p            |
| Low-end     | 30 FPS     | 28 FPS      | 720p            |

#### Device Categorization

```cpp
UENUM(BlueprintType)
enum class EDeviceTier : uint8
{
    LowEnd,
    MidRange,
    HighEnd,
    Unknown
};

class FDeviceProfiler
{
public:
    static EDeviceTier DetectDeviceTier()
    {
        // Get device specs
        FPlatformMemoryStats MemStats = FPlatformMemory::GetStats();
        int32 TotalRAM = MemStats.TotalPhysical / (1024 * 1024); // MB
        
        // Get chipset info
        FString GPUBrand = FPlatformMisc::GetPrimaryGPUBrand();
        
        // Calculate device score
        int32 Score = CalculateDeviceScore(TotalRAM, GPUBrand);
        
        if (Score >= 8000)
            return EDeviceTier::HighEnd;
        else if (Score >= 5000)
            return EDeviceTier::MidRange;
        else
            return EDeviceTier::LowEnd;
    }
    
private:
    static int32 CalculateDeviceScore(int32 RAM, const FString& GPU)
    {
        int32 Score = 0;
        
        // RAM scoring
        Score += FMath::Min(RAM / 100, 50) * 100; // Max 5000 from RAM
        
        // GPU scoring (simplified)
        if (GPU.Contains(TEXT("Adreno 7")) || GPU.Contains(TEXT("Apple A15")))
            Score += 4000;
        else if (GPU.Contains(TEXT("Adreno 6")) || GPU.Contains(TEXT("Apple A13")))
            Score += 3000;
        else if (GPU.Contains(TEXT("Mali")))
            Score += 2000;
        else
            Score += 1000;
        
        return Score;
    }
};
```

***

### Rendering Optimization

#### Level of Detail (LOD)

**LOD Configuration:**

```cpp
struct FLODSettings
{
    // Distance thresholds
    static constexpr float LOD0_Distance = 500.0f;   // High detail
    static constexpr float LOD1_Distance = 1500.0f;  // Medium detail
    static constexpr float LOD2_Distance = 3000.0f;  // Low detail
    static constexpr float CullDistance = 5000.0f;   // Beyond: cull
};

// Apply LOD to static mesh
void ConfigureStaticMeshLOD(UStaticMeshComponent* Mesh)
{
    if (!Mesh || !Mesh->GetStaticMesh())
        return;
    
    UStaticMesh* StaticMesh = Mesh->GetStaticMesh();
    
    // Setup LOD distances
    StaticMesh->LODGroup = NAME_None;
    
    // Per LOD settings
    for (int32 LODIndex = 0; LODIndex < StaticMesh->GetNumLODs(); LODIndex++)
    {
        FStaticMeshLODInfo& LODInfo = StaticMesh->GetLODInfo(LODIndex);
        
        switch (LODIndex)
        {
        case 0:
            LODInfo.ScreenSize = 1.0f;
            break;
        case 1:
            LODInfo.ScreenSize = 0.5f;
            break;
        case 2:
            LODInfo.ScreenSize = 0.25f;
            break;
        }
    }
    
    // Set cull distance
    Mesh->SetCullDistance(FLODSettings::CullDistance);
}
```

***

#### Occlusion Culling

**Precomputed Visibility:**

```cpp
// Enable precomputed visibility volumes
// Place volumes in dense areas (buildings)
class APrecomputedVisibilityVolume : public AActor
{
public:
    void Configure()
    {
        // Set in editor or via code
        CellSize = 100.0f; // Smaller = more accurate, slower build
        NumCellsPerVisibilityOverride = 1024;
    }
};
```

**Software Occlusion:**

```cpp
// UE5 Software Occlusion for mobile
void EnableSoftwareOcclusion()
{
    // In DefaultEngine.ini:
    // [/Script/Engine.RendererSettings]
    // r.Mobile.AllowSoftwareOcclusion=1
    // r.Mobile.AllowSoftwareOcculsion.LODGracePeriod=1.0
}
```

***

#### Dynamic Resolution

**Adaptive Resolution Scaling:**

```cpp
class UDynamicResolutionManager : public UGameInstanceSubsystem
{
public:
    void Initialize(FSubsystemCollectionBase& Collection) override
    {
        Super::Initialize(Collection);
        
        // Enable dynamic resolution
        IConsoleVariable* DynamicRes = IConsoleManager::Get().FindConsoleVariable(
            TEXT("r.DynamicRes.OperationMode"));
        if (DynamicRes)
        {
            DynamicRes->Set(2); // 2 = Enabled
        }
        
        // Set target frame rate
        IConsoleVariable* TargetFPS = IConsoleManager::Get().FindConsoleVariable(
            TEXT("r.DynamicRes.TargetFrameTime"));
        if (TargetFPS)
        {
            TargetFPS->Set(33.3f); // 30 FPS = 33.3ms
        }
    }
    
    void Tick(float DeltaTime) override
    {
        // Monitor frame rate
        float CurrentFPS = 1.0f / DeltaTime;
        
        // Adjust resolution scale
        if (CurrentFPS < TargetFPS - 5.0f)
        {
            DecreaseResolution();
        }
        else if (CurrentFPS > TargetFPS + 5.0f)
        {
            IncreaseResolution();
        }
    }
    
private:
    float TargetFPS = 30.0f;
    float CurrentResolutionScale = 1.0f;
    
    void DecreaseResolution()
    {
        CurrentResolutionScale = FMath::Max(0.5f, CurrentResolutionScale - 0.05f);
        ApplyResolutionScale();
    }
    
    void IncreaseResolution()
    {
        CurrentResolutionScale = FMath::Min(1.0f, CurrentResolutionScale + 0.05f);
        ApplyResolutionScale();
    }
    
    void ApplyResolutionScale()
    {
        IConsoleVariable* ScreenPercentage = IConsoleManager::Get().FindConsoleVariable(
            TEXT("r.ScreenPercentage"));
        if (ScreenPercentage)
        {
            ScreenPercentage->Set(CurrentResolutionScale * 100.0f);
        }
    }
};
```

***

#### Texture Optimization

**Texture Streaming:**

```cpp
// Enable texture streaming
// DefaultEngine.ini:
// [/Script/Engine.RendererSettings]
// r.Streaming.PoolSize=1000
// r.Streaming.UseFixedPoolSize=True

// Per-texture settings
void ConfigureTexture(UTexture2D* Texture, ETextureImportance Importance)
{
    if (!Texture)
        return;
    
    // Compression
    Texture->CompressionSettings = TC_Default;
    
    // Mip maps
    Texture->MipGenSettings = TMGS_SimpleAverage;
    
    // LOD bias based on importance
    switch (Importance)
    {
    case ETextureImportance::Critical: // Characters, weapons
        Texture->LODBias = 0;
        break;
    case ETextureImportance::Important: // Environment
        Texture->LODBias = 1;
        break;
    case ETextureImportance::Normal: // Props
        Texture->LODBias = 2;
        break;
    }
    
    // Never stream critical textures
    if (Importance == ETextureImportance::Critical)
    {
        Texture->NeverStream = true;
    }
}
```

***

### CPU Optimization

#### Object Pooling

**Generic Object Pool:**

```cpp
template<typename T>
class TObjectPool
{
public:
    TObjectPool(UWorld* World, int32 InitialSize = 20)
        : World(World)
    {
        PreAllocate(InitialSize);
    }
    
    void PreAllocate(int32 Count)
    {
        for (int32 i = 0; i < Count; i++)
        {
            T* NewObject = World->SpawnActor<T>();
            NewObject->SetActorHiddenInGame(true);
            NewObject->SetActorEnableCollision(false);
            Pool.Add(NewObject);
        }
    }
    
    T* Acquire(FVector Location = FVector::ZeroVector, 
               FRotator Rotation = FRotator::ZeroRotator)
    {
        T* Object = nullptr;
        
        if (Pool.Num() > 0)
        {
            Object = Pool.Pop();
        }
        else
        {
            // Pool exhausted, create new
            Object = World->SpawnActor<T>();
        }
        
        // Activate object
        Object->SetActorLocationAndRotation(Location, Rotation);
        Object->SetActorHiddenInGame(false);
        Object->SetActorEnableCollision(true);
        
        ActiveObjects.Add(Object);
        return Object;
    }
    
    void Release(T* Object)
    {
        if (!Object)
            return;
        
        // Deactivate
        Object->SetActorHiddenInGame(true);
        Object->SetActorEnableCollision(false);
        
        // Return to pool
        ActiveObjects.Remove(Object);
        Pool.Add(Object);
    }
    
    void ReleaseAll()
    {
        for (T* Object : ActiveObjects)
        {
            Object->SetActorHiddenInGame(true);
            Object->SetActorEnableCollision(false);
            Pool.Add(Object);
        }
        ActiveObjects.Empty();
    }
    
private:
    UWorld* World;
    TArray<T*> Pool;
    TArray<T*> ActiveObjects;
};

// Usage:
TObjectPool<ABulletActor> BulletPool;
ABulletActor* Bullet = BulletPool.Acquire(SpawnLocation, SpawnRotation);
// ... use bullet ...
BulletPool.Release(Bullet);
```

***

#### Tick Optimization

**Selective Ticking:**

```cpp
// Disable tick when not needed
void AExtractionCharacter::SetTickEnabled(bool bEnabled)
{
    SetActorTickEnabled(bEnabled);
    
    // Also disable component ticks
    for (UActorComponent* Component : GetComponents())
    {
        if (UPrimitiveComponent* PrimComp = Cast<UPrimitiveComponent>(Component))
        {
            PrimComp->PrimaryComponentTick.bCanEverTick = bEnabled;
        }
    }
}

// Variable tick rates
void AExtractionAICharacter::BeginPlay()
{
    Super::BeginPlay();
    
    // AI doesn't need 60 Hz tick
    PrimaryActorTick.TickInterval = 0.1f; // 10 Hz
}

// Distance-based tick rates
void UpdateTickInterval(AActor* Actor, APlayerController* Player)
{
    float Distance = FVector::Distance(
        Actor->GetActorLocation(),
        Player->GetPawn()->GetActorLocation()
    );
    
    if (Distance < 1000.0f)
        Actor->SetActorTickInterval(0.0f); // Every frame
    else if (Distance < 3000.0f)
        Actor->SetActorTickInterval(0.1f); // 10 Hz
    else
        Actor->SetActorTickInterval(0.5f); // 2 Hz
}
```

***

### Memory Optimization

#### Memory Budget Tracking

```cpp
class FMemoryBudgetTracker
{
public:
    struct FMemoryBudget
    {
        int64 Total = 1500 * 1024 * 1024; // 1.5 GB
        int64 Textures = 800 * 1024 * 1024;
        int64 Audio = 150 * 1024 * 1024;
        int64 Code = 300 * 1024 * 1024;
        int64 Other = 250 * 1024 * 1024;
    };
    
    static void LogMemoryUsage()
    {
        FPlatformMemoryStats MemStats = FPlatformMemory::GetStats();
        
        UE_LOG(LogTemp, Log, TEXT("=== Memory Usage ==="));
        UE_LOG(LogTemp, Log, TEXT("Total: %d MB"), 
            MemStats.UsedPhysical / (1024 * 1024));
        UE_LOG(LogTemp, Log, TEXT("Available: %d MB"), 
            MemStats.AvailablePhysical / (1024 * 1024));
        
        // Texture memory
        int64 TextureMemory = GetTextureMemoryUsage();
        UE_LOG(LogTemp, Log, TEXT("Textures: %d MB"), 
            TextureMemory / (1024 * 1024));
    }
    
private:
    static int64 GetTextureMemoryUsage()
    {
        int64 TotalSize = 0;
        for (TObjectIterator<UTexture2D> It; It; ++It)
        {
            UTexture2D* Texture = *It;
            TotalSize += Texture->CalcTextureMemorySizeEnum(TMC_AllMips);
        }
        return TotalSize;
    }
};
```

***

#### Asset Streaming

```cpp
// Async asset loading
class UAssetStreamingManager : public UGameInstanceSubsystem
{
public:
    void StreamInAssets(const TArray<FSoftObjectPath>& Assets, 
                       FStreamableDelegate OnComplete)
    {
        if (StreamableManager.IsValid())
        {
            StreamableManager->RequestAsyncLoad(
                Assets,
                OnComplete,
                FStreamableManager::AsyncLoadHighPriority
            );
        }
    }
    
    void StreamOutUnusedAssets()
    {
        // Force garbage collection
        GetWorld()->ForceGarbageCollection(true);
        
        // Flush streaming
        if (UGameplayStatics::GetStreamingManager())
        {
            UGameplayStatics::GetStreamingManager()->FlushAll();
        }
    }
    
private:
    TSharedPtr<FStreamableManager> StreamableManager;
};
```

***

### Network Optimization

**See:** [Networking System](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Technical/Performance/02_NetworkingSystem.md) for detailed network optimization

**Key Techniques:**

* Relevancy culling
* Update frequency adjustment
* Delta compression
* Bandwidth monitoring

***

### Mobile-Specific Optimizations

#### Battery Optimization

```cpp
class UBatteryOptimizer : public UGameInstanceSubsystem
{
public:
    void ReducePowerConsumption()
    {
        // Lower frame rate when in menu
        IConsoleVariable* VSync = IConsoleManager::Get().FindConsoleVariable(
            TEXT("r.VSync"));
        if (VSync)
        {
            VSync->Set(1); // Enable VSync to cap FPS
        }
        
        // Reduce tick rates
        ReduceTickRates();
        
        // Disable unnecessary features
        DisablePostProcessing();
    }
    
private:
    void ReduceTickRates()
    {
        // Lower all non-critical tick rates
        for (TActorIterator<AActor> It(GetWorld()); It; ++It)
        {
            AActor* Actor = *It;
            if (!Actor->IsPlayerControlled())
            {
                Actor->SetActorTickInterval(0.1f);
            }
        }
    }
    
    void DisablePostProcessing()
    {
        IConsoleVariable* Bloom = IConsoleManager::Get().FindConsoleVariable(
            TEXT("r.BloomQuality"));
        if (Bloom)
        {
            Bloom->Set(0);
        }
        
        // Disable other expensive effects
        // Motion blur, DOF, etc.
    }
};
```

***

#### Touch Input Optimization

```cpp
// Reduce input polling rate
void OptimizeTouchInput()
{
    // Only poll at frame rate (not higher)
    // Batch touch events
    IConsoleVariable* InputRate = IConsoleManager::Get().FindConsoleVariable(
        TEXT("t.MaxFPS"));
    if (InputRate)
    {
        InputRate->Set(30); // Match game FPS
    }
}
```

***

### Profiling & Debugging

#### Built-in Profilers

**Stat Commands:**

```cpp
// In-game console commands:
// stat fps - Show FPS
// stat unit - Show frame time breakdown
// stat memory - Memory usage
// stat streaming - Texture streaming info
// stat gpu - GPU timing

// Enable profiling
void EnableProfiling()
{
    GEngine->Exec(GetWorld(), TEXT("stat fps"));
    GEngine->Exec(GetWorld(), TEXT("stat unit"));
}
```

***

#### Custom Performance Metrics

```cpp
class FPerformanceMetrics
{
public:
    static void BeginFrame()
    {
        FrameStartTime = FPlatformTime::Seconds();
    }
    
    static void EndFrame()
    {
        double FrameTime = FPlatformTime::Seconds() - FrameStartTime;
        FrameTimes.Add(FrameTime);
        
        // Keep last 60 frames
        if (FrameTimes.Num() > 60)
        {
            FrameTimes.RemoveAt(0);
        }
        
        // Calculate average
        AvgFrameTime = 0.0;
        for (double Time : FrameTimes)
        {
            AvgFrameTime += Time;
        }
        AvgFrameTime /= FrameTimes.Num();
    }
    
    static float GetAverageFPS()
    {
        return 1.0f / AvgFrameTime;
    }
    
private:
    static double FrameStartTime;
    static TArray<double> FrameTimes;
    static double AvgFrameTime;
};
```

***

### Quality Settings

#### Auto-Detection

```cpp
UCLASS()
class UGraphicsSettings : public UGameUserSettings
{
public:
    void AutoDetectQualitySettings()
    {
        EDeviceTier Tier = FDeviceProfiler::DetectDeviceTier();
        
        switch (Tier)
        {
        case EDeviceTier::HighEnd:
            ApplyHighSettings();
            SetFrameRateLimit(60);
            break;
            
        case EDeviceTier::MidRange:
            ApplyMediumSettings();
            SetFrameRateLimit(45);
            break;
            
        case EDeviceTier::LowEnd:
            ApplyLowSettings();
            SetFrameRateLimit(30);
            break;
        }
        
        ApplySettings(false);
    }
    
private:
    void ApplyLowSettings()
    {
        SetViewDistanceQuality(0);
        SetShadowQuality(0);
        SetAntiAliasingQuality(0);
        SetTextureQuality(1);
        SetVisualEffectQuality(0);
        SetPostProcessingQuality(0);
        SetResolutionScaleValue(75);
    }
    
    void ApplyMediumSettings()
    {
        SetViewDistanceQuality(1);
        SetShadowQuality(1);
        SetAntiAliasingQuality(1);
        SetTextureQuality(2);
        SetVisualEffectQuality(1);
        SetPostProcessingQuality(1);
        SetResolutionScaleValue(90);
    }
    
    void ApplyHighSettings()
    {
        SetViewDistanceQuality(2);
        SetShadowQuality(2);
        SetAntiAliasingQuality(2);
        SetTextureQuality(3);
        SetVisualEffectQuality(2);
        SetPostProcessingQuality(2);
        SetResolutionScaleValue(100);
    }
};
```

***

### TODO: Optimization Tasks

#### HIGH Priority 

* [ ] Implement device tier detection
* [ ] Setup LOD system for all meshes
* [ ] Configure texture streaming
* [ ] Implement object pooling (bullets, effects)
* [ ] Performance profiling baseline

#### MEDIUM Priority 

* [ ] Dynamic resolution scaling
* [ ] Occlusion culling setup
* [ ] Tick optimization
* [ ] Memory budget tracking
* [ ] Auto quality settings

#### LOW Priority 

* [ ] Advanced profiling
* [ ] Battery optimization
* [ ] Network bandwidth optimization
* [ ] Custom performance dashboard
