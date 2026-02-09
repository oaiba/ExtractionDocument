---
title: "Map & Environment System - Technical Specification"
type: docs
---
# Map & Environment System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: AI System →](./AISystem.md)**

**Reference:** [High-Level Environment Design](../../GDD_HighLevel/Environments/EnvironmentDesign.md)

---

## Overview

The **Map & Environment System** manages all map-related gameplay including zones, extraction points, containers, supply drops, hazards, and weather. Designed for performance with level streaming and dynamic elements.

**Responsibilities:**
- Zone management (danger levels, loot tiers)
- Extraction point lifecycle
- Container spawning and interaction
- Supply drop system
- Environmental hazards
- Weather effects
- Match phase progression
- Contamination/storm zone
- Level streaming
- Spawn point management

---

## Enums & Types

### ZoneType
Map zone classification.

| Code Name       | Display Name  | Loot Tier       | AI Density  | Danger Level | Description                            |
| :-------------- | :------------ | :-------------- | :---------- | :----------- | :------------------------------------- |
| `ZT_Safe`       | Safe Zone     | Common          | None        | 0%           | Spawn areas, tutorial                  |
| `ZT_Low`        | Low Danger    | Common/Uncommon | Low         | 20%          | Perimeter areas                        |
| `ZT_Medium`     | Medium Danger | Uncommon/Rare   | Medium      | 50%          | Mid-map areas                          |
| `ZT_High`       | High Danger   | Rare/Epic       | High        | 75%          | Key locations                          |
| `ZT_Hot`        | Hot Zone      | Epic/Legendary  | Very High   | 90%          | High loot, high danger (center of map) |
| `ZT_Extraction` | Extraction    | N/A             | Varies      | 70%          | Extraction points                      |
| `ZT_Boss`       | Boss Zone     | Legendary       | Boss + Adds | 100%         | Boss encounter areas                   |

---

### ExtractionType
Extraction point type.

| Code Name        | Display Name | Duration | Capacity | Visibility | Frequency | Description                 |
| :--------------- | :----------- | :------- | :------- | :--------- | :-------- | :-------------------------- |
| `EXT_Helicopter` | Helicopter   | 30s      | 4        | High       | 40%       | Standard visible extraction |
| `EXT_Vehicle`    | Vehicle      | 20s      | 2        | Medium     | 30%       | Faster, less capacity       |
| `EXT_Sewer`      | Sewer        | 45s      | 1        | Low        | 20%       | Hidden, solo only           |
| `EXT_Zipline`    | Zipline      | 15s      | 2        | High       | 10%       | Fast, exposed               |

---

### ExtractionState
Extraction point lifecycle state.

| Code Name       | Display Name | Player Visible | Can Extract | Description          |
| :-------------- | :----------- | :------------- | :---------- | :------------------- |
| `ES_Inactive`   | Inactive     | No             | No          | Not yet available    |
| `ES_Available`  | Available    | Yes            | Yes         | Ready for extraction |
| `ES_Occupied`   | Occupied     | Yes            | Yes         | Players extracting   |
| `ES_Extracting` | Extracting   | Yes            | No          | Countdown active     |
| `ES_Cooldown`   | Cooldown     | No             | No          | Recently used        |
| `ES_Disabled`   | Disabled     | No             | No          | Permanently off      |

---

### ContainerType
Loot container type.

| Code Name        | Display Name | Loot Tier      | Interactable  | Respawn | Description              |
| :--------------- | :----------- | :------------- | :------------ | :------ | :----------------------- |
| `CT_LooseItem`   | Loose Item   | Common         | Instant       | No      | Single item pickup       |
| `CT_Crate`       | Crate        | Uncommon       | 2s            | No      | Standard loot crate      |
| `CT_Safe`        | Safe         | Rare           | 4s (lockpick) | No      | Valuables, requires tool |
| `CT_Weapon`      | Weapon Crate | Varied         | 3s            | No      | Weapon spawn             |
| `CT_Medical`     | Medical      | Healing items  | 2s            | No      | Medical supplies         |
| `CT_Ammo`        | Ammo         | Ammo only      | 1s            | No      | Ammunition box           |
| `CT_KeyLocked`   | Key Locked   | Epic/Legendary | Key required  | No      | High-tier, needs key     |
| `CT_HiddenCache` | Hidden Cache | Epic           | 3s            | No      | Hidden stash             |
| `CT_Airdrop`     | Airdrop      | Legendary      | 5s            | No      | Supply drop crate        |

---

### SupplyDropState
Supply drop lifecycle state.

| Code Name     | Display Name | Visible     | Interactable | Description       |
| :------------ | :----------- | :---------- | :----------- | :---------------- |
| `SD_Pending`  | Pending      | No          | No           | Scheduled         |
| `SD_Incoming` | Incoming     | Yes (plane) | No           | Plane approaching |
| `SD_Dropping` | Dropping     | Yes (chute) | No           | Crate falling     |
| `SD_Landed`   | Landed       | Yes         | Yes          | Ready to loot     |
| `SD_Looted`   | Looted       | Yes (empty) | No           | Already opened    |
| `SD_Expired`  | Expired      | No          | No           | Removed           |

---

### HazardType
Environmental hazard type.

| Code Name          | Display Name  | DPS  | Radius     | Spread    | Description            |
| :----------------- | :------------ | :--- | :--------- | :-------- | :--------------------- |
| `HZ_Electrical`    | Electrical    | 5    | 3m         | No        | Sparking wires, panels |
| `HZ_Radiation`     | Radiation     | 10   | 5m         | No        | Radioactive area       |
| `HZ_Fire`          | Fire          | 15   | 2m         | Yes       | Spreading fire         |
| `HZ_Gas`           | Gas           | 8    | 4m         | No        | Toxic gas cloud        |
| `HZ_Contamination` | Contamination | 12   | Zone-based | Shrinking | Storm zone damage      |

---

### WeatherType
Weather condition.

| Code Name      | Display Name | Visibility | Sound Mult | Duration   | Description                 |
| :------------- | :----------- | :--------- | :--------- | :--------- | :-------------------------- |
| `WT_Clear`     | Clear        | 100%       | 1.0×       | Base       | Normal conditions           |
| `WT_Rain`      | Rain         | 70%        | 1.5×       | 3-5 min    | Reduced vis, louder steps   |
| `WT_Fog`       | Fog          | 40%        | 0.8×       | 2-4 min    | Very low vis, muffled sound |
| `WT_Sandstorm` | Sandstorm    | 20%        | 0.5×       | 2-3 min    | Minimal vis, blocked sound  |
| `WT_Night`     | Night        | 50%        | 1.0×       | Full match | Flashlight gameplay         |

---

### MatchPhase
Match progression phase.

| Code Name          | Display Name  | Timer Start | Description                     |
| :----------------- | :------------ | :---------- | :------------------------------ |
| `MP_PreMatch`      | Pre-Match     | 0:00        | Loading, countdown              |
| `MP_EarlyGame`     | Early Game    | 0:00        | Looting phase (0-5 min)         |
| `MP_MidGame`       | Mid Game      | 5:00        | PvP heating up (5-10 min)       |
| `MP_LateGame`      | Late Game     | 10:00       | Extraction pressure (10-12 min) |
| `MP_Contamination` | Contamination | 12:00       | Zone closing (12-15 min)        |
| `MP_Overtime`      | Overtime      | 15:00       | Forced extraction               |
| `MP_PostMatch`     | Post-Match    | 17:00       | Results                         |

---

## Code Names

### Map Events

| Code Name                  | Trigger            | Parameters                    | Description                  |
| :------------------------- | :----------------- | :---------------------------- | :--------------------------- |
| `MAP_ZONE_ENTER`           | Player enters zone | ZoneID, ZoneType              | Zone boundary crossed        |
| `MAP_ZONE_EXIT`            | Player exits zone  | ZoneID, ZoneType              | Zone boundary exited         |
| `MAP_PHASE_CHANGE`         | Phase transition   | OldPhase, NewPhase            | Match phase changed          |
| `MAP_EXTRACTION_AVAILABLE` | Extraction opens   | ExtractionID, Type            | Extraction point activated   |
| `MAP_EXTRACTION_START`     | Extract begins     | ExtractionID, PlayerIDs       | Extraction countdown started |
| `MAP_EXTRACTION_COMPLETE`  | Extract success    | ExtractionID, PlayerIDs, Loot | Players extracted            |
| `MAP_EXTRACTION_CANCEL`    | Extract cancelled  | ExtractionID, Reason          | Extraction interrupted       |

### Supply Drop Events

| Code Name          | Trigger        | Parameters              | Description           |
| :----------------- | :------------- | :---------------------- | :-------------------- |
| `SUPPLY_ANNOUNCED` | Drop incoming  | DropID, TargetLocation  | Supply drop announced |
| `SUPPLY_DROPPING`  | Crate released | DropID, Location        | Crate falling         |
| `SUPPLY_LANDED`    | Crate landed   | DropID, FinalLocation   | Crate ready to loot   |
| `SUPPLY_LOOTED`    | Crate opened   | DropID, PlayerID, Items | Crate looted          |

### Container Events

| Code Name            | Trigger            | Parameters                    | Description                 |
| :------------------- | :----------------- | :---------------------------- | :-------------------------- |
| `CONTAINER_INTERACT` | Player starts loot | ContainerID, PlayerID         | Container being opened      |
| `CONTAINER_OPENED`   | Loot available     | ContainerID, Items            | Container contents revealed |
| `CONTAINER_LOOTED`   | Item taken         | ContainerID, ItemID, PlayerID | Item picked up              |
| `CONTAINER_EMPTY`    | Fully looted       | ContainerID                   | Container emptied           |

### Hazard Events

| Code Name       | Trigger              | Parameters                 | Description           |
| :-------------- | :------------------- | :------------------------- | :-------------------- |
| `HAZARD_ENTER`  | Player enters hazard | HazardID, HazardType       | Player in danger zone |
| `HAZARD_EXIT`   | Player exits hazard  | HazardID                   | Player left hazard    |
| `HAZARD_DAMAGE` | Damage tick          | HazardID, PlayerID, Damage | Hazard damage applied |
| `HAZARD_SPREAD` | Fire spreads         | HazardID, NewLocation      | Hazard expanded       |

### Weather Events

| Code Name        | Trigger              | Parameters             | Description            |
| :--------------- | :------------------- | :--------------------- | :--------------------- |
| `WEATHER_CHANGE` | Weather transition   | OldWeather, NewWeather | Weather changing       |
| `WEATHER_ACTIVE` | Weather fully active | WeatherType            | Weather effect at full |

---

## Architecture

### Class Diagram

```
                    ┌─────────────────┐
                    │   MapManager    │
                    │   (Singleton)   │
                    └────────┬────────┘
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
┌───▼───────┐    ┌───────────▼───────────┐    ┌───────▼───────┐
│ ZoneMgr   │    │  ExtractionManager    │    │ContainerMgr   │
│           │    │                       │    │               │
└───────────┘    └───────────────────────┘    └───────────────┘
    │                        │                        │
    │            ┌───────────┼───────────┐           │
    │            │           │           │           │
    │    ┌───────▼───┐ ┌─────▼────┐ ┌────▼────┐     │
    │    │SupplyDrop │ │Hazard    │ │Weather  │     │
    │    │ Manager   │ │ Manager  │ │ Manager │     │
    │    └───────────┘ └──────────┘ └─────────┘     │
    │                                                │
    └────────────────────────────────────────────────┘
```

---

## Core Classes

### MapManager

**Purpose:** Central map controller and subsystem access.

```
CLASS MapManager:
    STATIC instance: MapManager
    
    // Sub-managers
    zoneManager: ZoneManager
    extractionManager: ExtractionManager
    containerManager: ContainerManager
    supplyDropManager: SupplyDropManager
    hazardManager: HazardManager
    weatherManager: WeatherManager
    spawnManager: SpawnManager
    contaminationManager: ContaminationManager
    
    // Map data
    currentMapData: MapData
    currentPhase: MatchPhase = MP_PreMatch
    matchTimeElapsed: Float = 0.0
    matchDuration: Float = 900.0  // 15 minutes
    
    // Events
    OnPhaseChanged: Event<(oldPhase, newPhase)>
    OnMatchEnd: Event<(reason)>
    
    FUNCTION InitializeMap(mapID: String):
        currentMapData = LoadMapData(mapID)
        
        // Initialize zones
        zoneManager.InitializeZones(currentMapData.zones)
        
        // Spawn containers
        containerManager.SpawnContainers(currentMapData.containers)
        
        // Setup extractions
        extractionManager.InitializeExtractions(currentMapData.extractions)
        
        // Setup spawn points
        spawnManager.SetSpawnPoints(currentMapData.spawnPoints)
        
        // Start weather
        weatherManager.SetWeather(WT_Clear)
        
        currentPhase = MP_PreMatch
    END FUNCTION
    
    FUNCTION StartMatch():
        matchTimeElapsed = 0.0
        
        SetPhase(MP_EarlyGame)
        
        // Schedule supply drops
        supplyDropManager.ScheduleDrops(matchDuration)
        
        // Activate initial extractions
        extractionManager.ActivateInitialExtractions()
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        matchTimeElapsed += deltaTime
        
        // Check phase transitions
        CheckPhaseTransition()
        
        // Update sub-managers
        extractionManager.Update(deltaTime)
        supplyDropManager.Update(deltaTime)
        contaminationManager.Update(deltaTime)
        weatherManager.Update(deltaTime)
    END FUNCTION
    
    FUNCTION CheckPhaseTransition():
        timings = PHASE_TIMINGS
        
        FOR EACH (phase, startTime) IN timings:
            IF matchTimeElapsed >= startTime AND currentPhase < phase:
                SetPhase(phase)
                BREAK
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION SetPhase(newPhase: MatchPhase):
        oldPhase = currentPhase
        currentPhase = newPhase
        
        OnPhaseChanged.Broadcast(oldPhase, newPhase)
        
        EMIT EVENT "MAP_PHASE_CHANGE" WITH (oldPhase, newPhase)
        
        // Phase-specific logic
        SWITCH newPhase:
            CASE MP_LateGame:
                extractionManager.ActivateAllExtractions()
            
            CASE MP_Contamination:
                contaminationManager.StartContamination()
            
            CASE MP_Overtime:
                ForceAllPlayersToExtract()
        END SWITCH
    END FUNCTION
    
    FUNCTION GetCurrentPhase() -> MatchPhase:
        RETURN currentPhase
    END FUNCTION
    
    FUNCTION GetMatchTimeRemaining() -> Float:
        RETURN Max(0, matchDuration - matchTimeElapsed)
    END FUNCTION
    
    FUNCTION GetZoneAtLocation(location: Vector3) -> ZoneData:
        RETURN zoneManager.GetZoneAtLocation(location)
    END FUNCTION
    
    FUNCTION RegisterPlayerInZone(player: Player, zone: ZoneData):
        zoneManager.RegisterPlayer(player, zone)
        
        EMIT EVENT "MAP_ZONE_ENTER" WITH (zone.zoneID, zone.zoneType)
    END FUNCTION

// Phase timing configuration (15 min match)
CONST PHASE_TIMINGS = {
    MP_PreMatch: 0.0,
    MP_EarlyGame: 0.0,
    MP_MidGame: 300.0,       // 5 min
    MP_LateGame: 600.0,      // 10 min
    MP_Contamination: 720.0, // 12 min
    MP_Overtime: 900.0,      // 15 min
    MP_PostMatch: 1020.0     // 17 min max
}
```

---

### ZoneManager

**Purpose:** Map zone management and tracking.

```
CLASS ZoneManager:
    // Zones
    zones: Map<String, ZoneData>
    zoneVolumes: List<ZoneVolume>
    
    // Player tracking
    playerZones: Map<Player, ZoneData>
    
    // Events
    OnPlayerEnteredZone: Event<(player, zone)>
    OnPlayerExitedZone: Event<(player, zone)>
    
    FUNCTION InitializeZones(zoneConfigs: List<ZoneConfig>):
        FOR EACH config IN zoneConfigs:
            zoneData = NEW ZoneData()
            zoneData.zoneID = config.zoneID
            zoneData.zoneType = config.zoneType
            zoneData.lootTier = GetLootTierForZone(config.zoneType)
            zoneData.aiDensity = config.aiDensity
            zoneData.bounds = config.bounds
            
            zones[config.zoneID] = zoneData
            
            // Create zone volume for detection
            volume = SpawnZoneVolume(config.bounds)
            volume.OnPlayerEnter.AddListener(player => OnPlayerEnterVolume(player, zoneData))
            volume.OnPlayerExit.AddListener(player => OnPlayerExitVolume(player, zoneData))
            
            zoneVolumes.Add(volume)
        END FOR
    END FUNCTION
    
    FUNCTION GetZoneAtLocation(location: Vector3) -> ZoneData:
        FOR EACH (zoneID, zone) IN zones:
            IF zone.bounds.Contains(location):
                RETURN zone
            END IF
        END FOR
        
        RETURN defaultSafeZone
    END FUNCTION
    
    FUNCTION GetZoneType(zoneID: String) -> ZoneType:
        RETURN zones[zoneID].zoneType
    END FUNCTION
    
    FUNCTION GetDangerLevel(zoneID: String) -> Float:
        zone = zones[zoneID]
        RETURN ZONE_DANGER_LEVELS[zone.zoneType]
    END FUNCTION
    
    FUNCTION GetPlayersInZone(zoneID: String) -> List<Player>:
        result = []
        
        FOR EACH (player, zone) IN playerZones:
            IF zone.zoneID == zoneID:
                result.Add(player)
            END IF
        END FOR
        
        RETURN result
    END FUNCTION
    
    FUNCTION RegisterPlayer(player: Player, zone: ZoneData):
        previousZone = playerZones.GetOrDefault(player, null)
        
        IF previousZone != zone:
            IF previousZone != null:
                OnPlayerExitedZone.Broadcast(player, previousZone)
            END IF
            
            playerZones[player] = zone
            OnPlayerEnteredZone.Broadcast(player, zone)
        END IF
    END FUNCTION
    
    FUNCTION OnPlayerEnterVolume(player: Player, zone: ZoneData):
        RegisterPlayer(player, zone)
        
        EMIT EVENT "MAP_ZONE_ENTER" WITH (zone.zoneID, zone.zoneType)
    END FUNCTION
    
    FUNCTION OnPlayerExitVolume(player: Player, zone: ZoneData):
        EMIT EVENT "MAP_ZONE_EXIT" WITH (zone.zoneID, zone.zoneType)
    END FUNCTION

STRUCT ZoneData:
    zoneID: String
    zoneType: ZoneType
    displayName: String
    bounds: BoundingVolume
    lootTier: LootTier
    aiDensity: Float
    playerCount: Integer = 0

// Zone danger level percentages
CONST ZONE_DANGER_LEVELS = {
    ZT_Safe: 0.0,
    ZT_Low: 0.2,
    ZT_Medium: 0.5,
    ZT_High: 0.75,
    ZT_Hot: 0.9,
    ZT_Extraction: 0.7,
    ZT_Boss: 1.0
}
```

---

### ExtractionManager

**Purpose:** Extraction point lifecycle management.

```
CLASS ExtractionManager:
    // Extractions
    extractions: Map<String, ExtractionZone>
    activeExtractions: List<ExtractionZone>
    
    // Config
    minActiveExtractions: Integer = 2
    extractionCooldown: Float = 60.0
    
    // Events
    OnExtractionActivated: Event<(extraction)>
    OnExtractionStarted: Event<(extraction, players)>
    OnExtractionCompleted: Event<(extraction, players)>
    
    FUNCTION InitializeExtractions(extractionConfigs: List<ExtractionConfig>):
        FOR EACH config IN extractionConfigs:
            extraction = SpawnExtractionZone(config)
            extraction.SetState(ES_Inactive)
            
            extractions[config.extractionID] = extraction
        END FOR
    END FUNCTION
    
    FUNCTION ActivateInitialExtractions():
        availableExtractions = GetInactiveExtractions()
        
        FOR i = 0 TO minActiveExtractions:
            IF i < availableExtractions.Count:
                ActivateExtraction(availableExtractions[i])
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION ActivateAllExtractions():
        FOR EACH (id, extraction) IN extractions:
            IF extraction.currentState == ES_Inactive:
                ActivateExtraction(extraction)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION ActivateExtraction(extraction: ExtractionZone):
        extraction.Activate()
        activeExtractions.Add(extraction)
        
        OnExtractionActivated.Broadcast(extraction)
        
        EMIT EVENT "MAP_EXTRACTION_AVAILABLE" WITH (extraction.extractionID, extraction.extractionType)
    END FUNCTION
    
    FUNCTION GetActiveExtractions() -> List<ExtractionZone>:
        RETURN activeExtractions
    END FUNCTION
    
    FUNCTION GetNearestExtraction(location: Vector3) -> ExtractionZone:
        nearestDistance = Float.MaxValue
        nearestExtraction = null
        
        FOR EACH extraction IN activeExtractions:
            distance = Vector3.Distance(location, extraction.GetLocation())
            
            IF distance < nearestDistance:
                nearestDistance = distance
                nearestExtraction = extraction
            END IF
        END FOR
        
        RETURN nearestExtraction
    END FUNCTION
    
    FUNCTION BeginExtraction(extraction: ExtractionZone, players: List<Player>):
        IF extraction.currentState != ES_Available:
            RETURN
        END IF
        
        extraction.SetState(ES_Extracting)
        extraction.SetExtractingPlayers(players)
        extraction.StartCountdown()
        
        OnExtractionStarted.Broadcast(extraction, players)
        
        EMIT EVENT "MAP_EXTRACTION_START" WITH (extraction.extractionID, players)
    END FUNCTION
    
    FUNCTION CancelExtraction(extraction: ExtractionZone, reason: String):
        extraction.SetState(ES_Available)
        extraction.CancelCountdown()
        
        EMIT EVENT "MAP_EXTRACTION_CANCEL" WITH (extraction.extractionID, reason)
    END FUNCTION
    
    FUNCTION CompleteExtraction(extraction: ExtractionZone):
        extractingPlayers = extraction.GetExtractingPlayers()
        
        // Process each player's extraction
        FOR EACH player IN extractingPlayers:
            ProcessPlayerExtraction(player)
        END FOR
        
        extraction.SetState(ES_Cooldown)
        
        // Remove from active
        activeExtractions.Remove(extraction)
        
        // Start cooldown timer
        SetTimer(extractionCooldown, LAMBDA:
            extraction.SetState(ES_Inactive)
            // Potentially reactivate
            EnsureMinActiveExtractions()
        END LAMBDA)
        
        OnExtractionCompleted.Broadcast(extraction, extractingPlayers)
        
        EMIT EVENT "MAP_EXTRACTION_COMPLETE" WITH (extraction.extractionID, extractingPlayers)
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        FOR EACH extraction IN activeExtractions:
            extraction.Update(deltaTime)
            
            // Check if extraction completed
            IF extraction.IsCountdownComplete():
                CompleteExtraction(extraction)
            END IF
        END FOR
    END FUNCTION
```

---

### ExtractionZone (Actor)

**Purpose:** Individual extraction point actor.

```
CLASS ExtractionZone:
    // Identity
    extractionID: String
    extractionType: ExtractionType
    
    // State
    currentState: ExtractionState = ES_Inactive
    
    // Extracting
    extractingPlayers: List<Player>
    extractionProgress: Float = 0.0
    extractionDuration: Float
    
    // Components
    triggerVolume: CollisionVolume
    visualMesh: StaticMesh
    extractionVFX: ParticleSystem
    
    // Events
    OnStateChanged: Event<(oldState, newState)>
    OnCountdownTick: Event<(remaining)>
    
    FUNCTION Activate():
        SetState(ES_Available)
        
        // Enable visuals
        visualMesh.SetVisibility(true)
        extractionVFX.Activate()
    END FUNCTION
    
    FUNCTION Deactivate():
        SetState(ES_Inactive)
        
        visualMesh.SetVisibility(false)
        extractionVFX.Deactivate()
    END FUNCTION
    
    FUNCTION SetState(newState: ExtractionState):
        oldState = currentState
        currentState = newState
        
        OnStateChanged.Broadcast(oldState, newState)
    END FUNCTION
    
    FUNCTION BeginExtraction(player: Player):
        IF currentState != ES_Available AND currentState != ES_Occupied:
            RETURN
        END IF
        
        extractingPlayers.Add(player)
        
        IF currentState == ES_Available:
            SetState(ES_Occupied)
        END IF
    END FUNCTION
    
    FUNCTION CancelExtraction(player: Player):
        extractingPlayers.Remove(player)
        
        IF extractingPlayers.IsEmpty():
            SetState(ES_Available)
            extractionProgress = 0.0
        END IF
    END FUNCTION
    
    FUNCTION StartCountdown():
        extractionProgress = 0.0
        SetState(ES_Extracting)
    END FUNCTION
    
    FUNCTION CancelCountdown():
        extractionProgress = 0.0
        SetState(ES_Available)
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        IF currentState == ES_Extracting:
            extractionProgress += deltaTime
            
            remaining = extractionDuration - extractionProgress
            OnCountdownTick.Broadcast(remaining)
        END IF
    END FUNCTION
    
    FUNCTION IsCountdownComplete() -> Boolean:
        RETURN currentState == ES_Extracting AND extractionProgress >= extractionDuration
    END FUNCTION
    
    FUNCTION GetExtractionProgress(player: Player) -> Float:
        IF currentState == ES_Extracting:
            RETURN extractionProgress / extractionDuration
        END IF
        RETURN 0.0
    END FUNCTION
    
    FUNCTION GetExtractingPlayers() -> List<Player>:
        RETURN extractingPlayers.ToList()
    END FUNCTION
    
    FUNCTION OnPlayerEnterTrigger(player: Player):
        IF currentState == ES_Available OR currentState == ES_Occupied:
            BeginExtraction(player)
        END IF
    END FUNCTION
    
    FUNCTION OnPlayerExitTrigger(player: Player):
        CancelExtraction(player)
    END FUNCTION

// Extraction type configurations
CONST EXTRACTION_CONFIGS = {
    EXT_Helicopter: { duration: 30.0, capacity: 4, visibility: "High" },
    EXT_Vehicle: { duration: 20.0, capacity: 2, visibility: "Medium" },
    EXT_Sewer: { duration: 45.0, capacity: 1, visibility: "Low" },
    EXT_Zipline: { duration: 15.0, capacity: 2, visibility: "High" }
}
```

---

### ContainerManager

**Purpose:** Loot container spawning and management.

```
CLASS ContainerManager:
    // Containers
    activeContainers: Map<String, Container>
    containerConfigs: List<ContainerSpawnData>
    
    // Loot tables
    lootTables: Map<String, LootTable>
    
    FUNCTION SpawnContainers(configs: List<ContainerSpawnData>):
        containerConfigs = configs
        
        FOR EACH config IN configs:
            SpawnContainer(config)
        END FOR
    END FUNCTION
    
    FUNCTION SpawnContainer(config: ContainerSpawnData):
        container = CreateContainer(config.containerType)
        container.SetLocation(config.location)
        container.SetRequiresKey(config.requiresKey)
        container.SetLootTableID(config.lootTableID)
        
        // Generate loot
        loot = GenerateLoot(config.lootTableID, GetZoneModifier(config.location))
        container.SetContents(loot)
        
        containerID = GenerateContainerID()
        activeContainers[containerID] = container
        
        container.OnOpened.AddListener(LAMBDA player, items:
            EMIT EVENT "CONTAINER_OPENED" WITH (containerID, items)
        END LAMBDA)
        
        container.OnLooted.AddListener(LAMBDA player, item:
            EMIT EVENT "CONTAINER_LOOTED" WITH (containerID, item.ID, player)
        END LAMBDA)
    END FUNCTION
    
    FUNCTION GetContainerAtLocation(location: Vector3, radius: Float = 200.0) -> Container:
        FOR EACH (id, container) IN activeContainers:
            IF Vector3.Distance(location, container.GetLocation()) < radius:
                RETURN container
            END IF
        END FOR
        
        RETURN null
    END FUNCTION
    
    FUNCTION InteractWithContainer(containerID: String, player: Player) -> Boolean:
        container = activeContainers[containerID]
        
        IF container == null OR container.IsEmpty():
            RETURN false
        END IF
        
        IF container.RequiresKey() AND NOT player.HasKey(container.GetRequiredKeyID()):
            RETURN false
        END IF
        
        EMIT EVENT "CONTAINER_INTERACT" WITH (containerID, player)
        
        // Start interaction timer
        InteractionManager.StartInteraction(player, container, container.GetInteractionTime())
        
        RETURN true
    END FUNCTION
    
    FUNCTION OpenContainer(containerID: String, player: Player):
        container = activeContainers[containerID]
        container.Open()
        
        contents = container.GetContents()
        
        EMIT EVENT "CONTAINER_OPENED" WITH (containerID, contents)
        
        // Show loot UI to player
        UIManager.ShowContainerLoot(player, contents)
    END FUNCTION
    
    FUNCTION GenerateLoot(lootTableID: String, zoneModifier: Float) -> List<ItemData>:
        lootTable = lootTables[lootTableID]
        items = []
        
        FOR i = 0 TO lootTable.itemCount:
            roll = Random.Range(0.0, 1.0) * zoneModifier
            item = lootTable.RollItem(roll)
            
            IF item != null:
                items.Add(item)
            END IF
        END FOR
        
        RETURN items
    END FUNCTION

STRUCT ContainerSpawnData:
    location: Vector3
    containerType: ContainerType
    lootTableID: String
    requiresKey: Boolean = false
    requiredKeyID: String = ""
```

---

### SupplyDropManager

**Purpose:** Supply drop scheduling and lifecycle.

```
CLASS SupplyDropManager:
    // Active drops
    scheduledDrops: List<ScheduledDrop>
    activeDrops: Map<String, SupplyDrop>
    
    // Config
    dropIntervalMin: Float = 120.0  // 2 min
    dropIntervalMax: Float = 180.0  // 3 min
    dropDuration: Float = 120.0     // 2 min until expires
    
    // Events
    OnDropAnnounced: Event<(dropID, location)>
    OnDropLanded: Event<(dropID, location)>
    
    FUNCTION ScheduleDrops(matchDuration: Float):
        currentTime = 60.0  // First drop at 1 min
        
        WHILE currentTime < matchDuration - 120.0:
            scheduleDropAtTime(currentTime)
            currentTime += Random.Range(dropIntervalMin, dropIntervalMax)
        END WHILE
    END FUNCTION
    
    FUNCTION scheduleDropAtTime(time: Float):
        drop = NEW ScheduledDrop()
        drop.scheduledTime = time
        drop.targetLocation = GetRandomDropLocation()
        drop.dropID = GenerateDropID()
        
        scheduledDrops.Add(drop)
    END FUNCTION
    
    FUNCTION BeginDrop(scheduledDrop: ScheduledDrop):
        supplyDrop = SpawnSupplyDrop(scheduledDrop)
        supplyDrop.SetState(SD_Incoming)
        
        activeDrops[scheduledDrop.dropID] = supplyDrop
        
        OnDropAnnounced.Broadcast(scheduledDrop.dropID, scheduledDrop.targetLocation)
        
        EMIT EVENT "SUPPLY_ANNOUNCED" WITH (scheduledDrop.dropID, scheduledDrop.targetLocation)
        
        // Announce to all players
        NotifyAllPlayers("Supply drop incoming!", scheduledDrop.targetLocation)
        
        // Spawn plane
        SpawnDropPlane(scheduledDrop.targetLocation)
    END FUNCTION
    
    FUNCTION ExecuteDrop(dropID: String, location: Vector3):
        supplyDrop = activeDrops[dropID]
        supplyDrop.SetState(SD_Dropping)
        
        // Spawn visual crate with parachute
        SpawnFallingCrate(location, LAMBDA finalLocation:
            OnDropLanded(dropID, finalLocation)
        END LAMBDA)
        
        EMIT EVENT "SUPPLY_DROPPING" WITH (dropID, location)
    END FUNCTION
    
    FUNCTION OnDropLanded(dropID: String, location: Vector3):
        supplyDrop = activeDrops[dropID]
        supplyDrop.SetLocation(location)
        supplyDrop.SetState(SD_Landed)
        
        // Generate high-tier loot
        loot = GenerateSupplyDropLoot()
        supplyDrop.SetContents(loot)
        
        OnDropLanded.Broadcast(dropID, location)
        
        EMIT EVENT "SUPPLY_LANDED" WITH (dropID, location)
        
        // Set expiration timer
        SetTimer(dropDuration, LAMBDA:
            ExpireDrop(dropID)
        END LAMBDA)
    END FUNCTION
    
    FUNCTION LootDrop(dropID: String, player: Player):
        supplyDrop = activeDrops[dropID]
        
        IF supplyDrop.currentState != SD_Landed:
            RETURN
        END IF
        
        items = supplyDrop.GetContents()
        
        supplyDrop.SetState(SD_Looted)
        
        EMIT EVENT "SUPPLY_LOOTED" WITH (dropID, player, items)
        
        // Show loot to player
        UIManager.ShowContainerLoot(player, items)
    END FUNCTION
    
    FUNCTION ExpireDrop(dropID: String):
        supplyDrop = activeDrops[dropID]
        
        IF supplyDrop.currentState == SD_Landed:
            supplyDrop.SetState(SD_Expired)
            supplyDrop.Destroy()
            activeDrops.Remove(dropID)
        END IF
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        matchTime = MapManager.GetMatchTimeElapsed()
        
        // Check scheduled drops
        FOR EACH drop IN scheduledDrops.ToList():
            IF matchTime >= drop.scheduledTime:
                BeginDrop(drop)
                scheduledDrops.Remove(drop)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION GetRandomDropLocation() -> Vector3:
        // Get valid drop zones (avoid safe zones, boss areas)
        validZones = ZoneManager.GetZonesOfTypes([ZT_Medium, ZT_High, ZT_Hot])
        
        randomZone = validZones.Random()
        
        RETURN randomZone.GetRandomPointInside()
    END FUNCTION

STRUCT ScheduledDrop:
    dropID: String
    scheduledTime: Float
    targetLocation: Vector3
```

---

### HazardManager

**Purpose:** Environmental hazard management.

```
CLASS HazardManager:
    // Active hazards
    activeHazards: List<HazardZone>
    
    // Config
    hazardTickRate: Float = 0.5  // Damage tick every 0.5s
    
    FUNCTION SpawnHazard(hazardType: HazardType, location: Vector3, radius: Float = 300.0) -> HazardZone:
        config = HAZARD_CONFIGS[hazardType]
        
        hazard = CreateHazardZone(hazardType)
        hazard.SetLocation(location)
        hazard.SetRadius(radius)
        hazard.SetDamagePerSecond(config.dps)
        hazard.SetCanSpread(config.canSpread)
        
        activeHazards.Add(hazard)
        
        RETURN hazard
    END FUNCTION
    
    FUNCTION RemoveHazard(hazard: HazardZone):
        activeHazards.Remove(hazard)
        hazard.Destroy()
    END FUNCTION
    
    FUNCTION GetHazardsAtLocation(location: Vector3) -> List<HazardZone>:
        result = []
        
        FOR EACH hazard IN activeHazards:
            IF hazard.ContainsPoint(location):
                result.Add(hazard)
            END IF
        END FOR
        
        RETURN result
    END FUNCTION
    
    FUNCTION GetTotalDamageAtLocation(location: Vector3) -> Float:
        totalDPS = 0.0
        
        FOR EACH hazard IN GetHazardsAtLocation(location):
            totalDPS += hazard.GetDamagePerSecond()
        END FOR
        
        RETURN totalDPS
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        // Process hazard damage
        FOR EACH hazard IN activeHazards:
            players = GetPlayersInHazard(hazard)
            
            FOR EACH player IN players:
                damage = hazard.GetDamagePerSecond() * hazardTickRate
                ApplyHazardDamage(player, hazard, damage)
            END FOR
            
            // Handle spreading
            IF hazard.CanSpread():
                hazard.UpdateSpread(deltaTime)
            END IF
            
            // Check duration
            IF hazard.HasDuration() AND hazard.IsExpired():
                RemoveHazard(hazard)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION ApplyHazardDamage(player: Player, hazard: HazardZone, damage: Float):
        damageInfo = NEW DamageInfo()
        damageInfo.damage = damage
        damageInfo.damageType = hazard.GetDamageType()
        damageInfo.source = hazard
        
        player.TakeDamage(damageInfo)
        
        EMIT EVENT "HAZARD_DAMAGE" WITH (hazard.ID, player, damage)
    END FUNCTION

STRUCT HazardConfig:
    hazardType: HazardType
    dps: Float
    defaultRadius: Float
    canSpread: Boolean
    vfxName: String

// Hazard configurations
CONST HAZARD_CONFIGS = {
    HZ_Electrical: { dps: 5.0, radius: 300.0, spread: false, vfx: "VFX_Sparks" },
    HZ_Radiation: { dps: 10.0, radius: 500.0, spread: false, vfx: "VFX_Radiation" },
    HZ_Fire: { dps: 15.0, radius: 200.0, spread: true, vfx: "VFX_Fire" },
    HZ_Gas: { dps: 8.0, radius: 400.0, spread: false, vfx: "VFX_Gas" }
}
```

---

### HazardZone (Actor)

**Purpose:** Individual hazard zone actor.

```
CLASS HazardZone:
    // Identity
    hazardID: String
    hazardType: HazardType
    
    // Config
    radius: Float = 300.0
    damagePerSecond: Float = 10.0
    canSpread: Boolean = false
    spreadRate: Float = 0.0
    duration: Float = -1.0  // -1 = permanent
    
    // State
    timeAlive: Float = 0.0
    
    // Visual
    hazardVFX: ParticleSystem
    decalMaterial: Material
    
    FUNCTION SetRadius(newRadius: Float):
        radius = newRadius
        UpdateVisuals()
    END FUNCTION
    
    FUNCTION SetDamagePerSecond(dps: Float):
        damagePerSecond = dps
    END FUNCTION
    
    FUNCTION GetDamagePerSecond() -> Float:
        RETURN damagePerSecond
    END FUNCTION
    
    FUNCTION SetCanSpread(canSpread: Boolean):
        this.canSpread = canSpread
    END FUNCTION
    
    FUNCTION CanSpread() -> Boolean:
        RETURN canSpread
    END FUNCTION
    
    FUNCTION ContainsPoint(point: Vector3) -> Boolean:
        distance = Vector3.Distance(GetLocation(), point)
        RETURN distance <= radius
    END FUNCTION
    
    FUNCTION ApplyDamage(target: Character, deltaTime: Float):
        damage = damagePerSecond * deltaTime
        
        damageInfo = NEW DamageInfo()
        damageInfo.damage = damage
        damageInfo.damageType = GetDamageType()
        
        target.TakeDamage(damageInfo)
    END FUNCTION
    
    FUNCTION UpdateSpread(deltaTime: Float):
        IF canSpread AND spreadRate > 0:
            radius += spreadRate * deltaTime
            UpdateVisuals()
            
            EMIT EVENT "HAZARD_SPREAD" WITH (hazardID, GetLocation())
        END IF
    END FUNCTION
    
    FUNCTION HasDuration() -> Boolean:
        RETURN duration > 0
    END FUNCTION
    
    FUNCTION IsExpired() -> Boolean:
        RETURN HasDuration() AND timeAlive >= duration
    END FUNCTION
    
    FUNCTION GetDamageType() -> DamageType:
        SWITCH hazardType:
            CASE HZ_Electrical: RETURN DT_Electrical
            CASE HZ_Radiation: RETURN DT_Radiation
            CASE HZ_Fire: RETURN DT_Fire
            CASE HZ_Gas: RETURN DT_Poison
            DEFAULT: RETURN DT_Environmental
        END SWITCH
    END FUNCTION
```

---

### WeatherManager

**Purpose:** Weather state and transitions.

```
CLASS WeatherManager:
    // State
    currentWeather: WeatherType = WT_Clear
    targetWeather: WeatherType
    transitionProgress: Float = 1.0
    
    // Config
    defaultTransitionTime: Float = 5.0
    
    // Events
    OnWeatherChanged: Event<(oldWeather, newWeather)>
    
    FUNCTION SetWeather(weather: WeatherType, transitionTime: Float = 5.0):
        IF weather == currentWeather AND transitionProgress >= 1.0:
            RETURN
        END IF
        
        targetWeather = weather
        this.defaultTransitionTime = transitionTime
        transitionProgress = 0.0
        
        EMIT EVENT "WEATHER_CHANGE" WITH (currentWeather, weather)
    END FUNCTION
    
    FUNCTION GetCurrentWeather() -> WeatherType:
        RETURN currentWeather
    END FUNCTION
    
    FUNCTION GetVisibilityMultiplier() -> Float:
        RETURN WEATHER_EFFECTS[currentWeather].visibilityMultiplier
    END FUNCTION
    
    FUNCTION GetSoundMultiplier() -> Float:
        RETURN WEATHER_EFFECTS[currentWeather].soundMultiplier
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        IF transitionProgress < 1.0:
            transitionProgress += deltaTime / defaultTransitionTime
            transitionProgress = Min(transitionProgress, 1.0)
            
            // Lerp weather effects
            UpdateWeatherEffects(transitionProgress)
            
            IF transitionProgress >= 1.0:
                currentWeather = targetWeather
                OnWeatherChanged.Broadcast(currentWeather, targetWeather)
                
                EMIT EVENT "WEATHER_ACTIVE" WITH (currentWeather)
            END IF
        END IF
    END FUNCTION
    
    FUNCTION UpdateWeatherEffects(progress: Float):
        fromEffects = WEATHER_EFFECTS[currentWeather]
        toEffects = WEATHER_EFFECTS[targetWeather]
        
        // Lerp fog
        fogDensity = Lerp(fromEffects.fogDensity, toEffects.fogDensity, progress)
        SetFogDensity(fogDensity)
        
        // Lerp particle intensity
        rainIntensity = Lerp(fromEffects.rainIntensity, toEffects.rainIntensity, progress)
        SetRainIntensity(rainIntensity)
        
        // Update ambient sound
        ambientVolume = Lerp(fromEffects.ambientVolume, toEffects.ambientVolume, progress)
        AudioManager.SetAmbientVolume(ambientVolume)
    END FUNCTION

STRUCT WeatherEffects:
    visibilityMultiplier: Float
    soundMultiplier: Float
    fogDensity: Float
    rainIntensity: Float
    ambientVolume: Float
    ambientSoundID: String

// Weather effect configurations
CONST WEATHER_EFFECTS = {
    WT_Clear: { visibility: 1.0, sound: 1.0, fog: 0.0, rain: 0.0, ambient: "Env_Clear" },
    WT_Rain: { visibility: 0.7, sound: 1.5, fog: 0.1, rain: 1.0, ambient: "Env_Rain" },
    WT_Fog: { visibility: 0.4, sound: 0.8, fog: 0.8, rain: 0.0, ambient: "Env_Fog" },
    WT_Sandstorm: { visibility: 0.2, sound: 0.5, fog: 0.9, rain: 0.0, ambient: "Env_Sandstorm" }
}
```

---

### ContaminationManager

**Purpose:** Shrinking contamination zone.

```
CLASS ContaminationManager:
    // State
    isActive: Boolean = false
    currentRadius: Float
    targetRadius: Float
    centerPoint: Vector3
    
    // Config
    initialRadius: Float = 2000.0      // Full map
    finalRadius: Float = 100.0         // Tiny circle
    shrinkDuration: Float = 180.0      // 3 minutes to shrink
    damagePerSecond: Float = 12.0
    
    // Timing
    shrinkStartTime: Float
    shrinkProgress: Float = 0.0
    
    FUNCTION StartContamination():
        isActive = true
        currentRadius = initialRadius
        targetRadius = finalRadius
        centerPoint = CalculateFinalCenter()
        shrinkStartTime = GetTime()
        shrinkProgress = 0.0
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        IF NOT isActive:
            RETURN
        END IF
        
        // Update shrink progress
        shrinkProgress = (GetTime() - shrinkStartTime) / shrinkDuration
        shrinkProgress = Clamp(shrinkProgress, 0.0, 1.0)
        
        // Lerp radius
        currentRadius = Lerp(initialRadius, targetRadius, shrinkProgress)
        
        // Damage players outside safe zone
        allPlayers = GetAllPlayers()
        
        FOR EACH player IN allPlayers:
            IF NOT IsInsideSafeZone(player.GetLocation()):
                ApplyContaminationDamage(player, deltaTime)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION IsInsideSafeZone(location: Vector3) -> Boolean:
        distance = Vector3.Distance(location, centerPoint)
        RETURN distance <= currentRadius
    END FUNCTION
    
    FUNCTION GetDistanceToSafeZone(location: Vector3) -> Float:
        distance = Vector3.Distance(location, centerPoint)
        RETURN Max(0, distance - currentRadius)
    END FUNCTION
    
    FUNCTION GetSafeZoneCenter() -> Vector3:
        RETURN centerPoint
    END FUNCTION
    
    FUNCTION GetSafeZoneRadius() -> Float:
        RETURN currentRadius
    END FUNCTION
    
    FUNCTION GetTimeRemaining() -> Float:
        RETURN Max(0, shrinkDuration * (1.0 - shrinkProgress))
    END FUNCTION
    
    FUNCTION ApplyContaminationDamage(player: Player, deltaTime: Float):
        // Damage increases the further outside
        distanceOutside = GetDistanceToSafeZone(player.GetLocation())
        damageMultiplier = 1.0 + (distanceOutside / 500.0)
        
        damage = damagePerSecond * deltaTime * damageMultiplier
        
        damageInfo = NEW DamageInfo()
        damageInfo.damage = damage
        damageInfo.damageType = DT_Contamination
        
        player.TakeDamage(damageInfo)
    END FUNCTION
    
    FUNCTION CalculateFinalCenter() -> Vector3:
        // Pick a random point that has extraction access
        extractions = ExtractionManager.GetActiveExtractions()
        
        IF extractions.Count > 0:
            // Center on random extraction
            randomExtraction = extractions.Random()
            RETURN randomExtraction.GetLocation()
        END IF
        
        // Default to map center
        RETURN MapManager.GetMapCenter()
    END FUNCTION
```

---

### SpawnManager

**Purpose:** Player spawn point management.

```
CLASS SpawnManager:
    // Spawn points
    allSpawnPoints: List<Vector3>
    usedSpawnPoints: List<Vector3>
    
    // Config
    minDistanceFromPlayers: Float = 10000.0  // 100m
    minDistanceFromCombat: Float = 5000.0    // 50m
    spawnProtectionDuration: Float = 10.0
    
    FUNCTION SetSpawnPoints(points: List<Vector3>):
        allSpawnPoints = points
        usedSpawnPoints.Clear()
    END FUNCTION
    
    FUNCTION GetValidSpawnPoint(existingPlayers: List<Player>) -> Vector3:
        validPoints = []
        
        FOR EACH point IN allSpawnPoints:
            IF IsSpawnPointValid(point, existingPlayers):
                validPoints.Add(point)
            END IF
        END FOR
        
        IF validPoints.IsEmpty():
            // Fallback: return least bad option
            RETURN GetLeastCongestedSpawn(existingPlayers)
        END IF
        
        // Pick random valid point
        selectedPoint = validPoints.Random()
        usedSpawnPoints.Add(selectedPoint)
        
        RETURN selectedPoint
    END FUNCTION
    
    FUNCTION IsSpawnPointValid(point: Vector3, players: List<Player>) -> Boolean:
        // Check if already used
        IF usedSpawnPoints.Contains(point):
            RETURN false
        END IF
        
        // Check distance from other players
        FOR EACH player IN players:
            distance = Vector3.Distance(point, player.GetLocation())
            
            IF distance < minDistanceFromPlayers:
                RETURN false
            END IF
        END FOR
        
        // Check line of sight to players
        IF HasLineOfSightToPlayer(point, players):
            RETURN false
        END IF
        
        // Check distance from combat
        IF IsNearCombat(point):
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    FUNCTION GetAllSpawnPoints() -> List<Vector3>:
        RETURN allSpawnPoints.ToList()
    END FUNCTION
    
    FUNCTION HasLineOfSightToPlayer(point: Vector3, players: List<Player>) -> Boolean:
        FOR EACH player IN players:
            hit = TraceLine(point + Vector3(0, 0, 100), player.GetLocation() + Vector3(0, 0, 100))
            
            IF NOT hit.IsValid:
                RETURN true  // Clear LOS
            END IF
        END FOR
        
        RETURN false
    END FUNCTION
    
    FUNCTION IsNearCombat(point: Vector3) -> Boolean:
        recentCombatLocations = CombatTracker.GetRecentCombatLocations(30.0)  // Last 30s
        
        FOR EACH combatLocation IN recentCombatLocations:
            IF Vector3.Distance(point, combatLocation) < minDistanceFromCombat:
                RETURN true
            END IF
        END FOR
        
        RETURN false
    END FUNCTION
    
    FUNCTION GetLeastCongestedSpawn(players: List<Player>) -> Vector3:
        bestPoint = allSpawnPoints[0]
        bestDistance = 0.0
        
        FOR EACH point IN allSpawnPoints:
            minPlayerDistance = Float.MaxValue
            
            FOR EACH player IN players:
                distance = Vector3.Distance(point, player.GetLocation())
                minPlayerDistance = Min(minPlayerDistance, distance)
            END FOR
            
            IF minPlayerDistance > bestDistance:
                bestDistance = minPlayerDistance
                bestPoint = point
            END IF
        END FOR
        
        RETURN bestPoint
    END FUNCTION
```

---

## Data Structures

```
STRUCT MapData:
    mapID: String
    displayName: String
    mapSize: Vector2           // 1600x1600, etc.
    maxPlayers: Integer
    matchDuration: Float
    zones: List<ZoneData>
    extractions: List<ExtractionData>
    spawnPoints: List<Vector3>
    containers: List<ContainerSpawnData>

STRUCT ExtractionData:
    extractionID: String
    extractionType: ExtractionType
    location: Vector3
    rotation: Rotator

STRUCT StreamingConfig:
    loadDistance: Float = 15000.0     // 150m
    unloadDistance: Float = 20000.0   // 200m
    alwaysLoaded: Boolean = false
    priority: Integer = 0
    lod0Distance: Float = 0.0
    lod1Distance: Float = 5000.0
    lod2Distance: Float = 10000.0

// Zone streaming configurations
CONST ZONE_STREAMING_CONFIGS = {
    "PowerPlant": { loadDist: 15000, unloadDist: 20000, priority: 10 },
    "Forest": { loadDist: 10000, unloadDist: 15000, priority: 1 },
    "Spawn_Areas": { loadDist: 0, unloadDist: 0, alwaysLoaded: true, priority: 100 }
}
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] MapManager core
- [ ] ExtractionZone with network replication
- [ ] ContainerManager, Container
- [ ] Basic zone system
- [ ] Match phase progression

### MEDIUM Priority 🟡
- [ ] SupplyDropManager with flight path
- [ ] ContaminationManager with shrinking
- [ ] SpawnManager with validation
- [ ] Level streaming setup
- [ ] HazardManager basics

### LOW Priority 🟢
- [ ] WeatherManager
- [ ] Dynamic fire spreading
- [ ] Environmental storytelling objects
- [ ] Destructible elements
- [ ] Night mode with flashlights

---

## Testing Checklist

- [ ] All extraction zones activate correctly
- [ ] Extraction timer syncs across clients
- [ ] Containers spawn according to zone type
- [ ] Loot tables generate correct rarity
- [ ] Supply drops land in valid zones
- [ ] Contamination damages players correctly
- [ ] Zone shrinking is visible to all
- [ ] Hazards apply damage consistently
- [ ] Spawn points avoid combat areas
- [ ] Level streaming doesn't cause stutters
- [ ] Weather transitions smoothly

---

**[← Back to Index](../README.md)** | **[Next: AI System →](./AISystem.md)**


