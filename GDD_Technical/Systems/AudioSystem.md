# Audio System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: Narrative System →](./NarrativeSystem.md)**

**Reference:** [High-Level Audio Design](../../GDD_HighLevel/Visuals/AudioDesign.md)

---

## Overview

The **Audio System** manages all game audio including sound effects, music, voice lines, ambient, and mixing. Optimized for mobile performance with streaming, pooling, and smart prioritization.

**Responsibilities:**
- 3D spatial audio
- Dynamic music intensity
- Weapon/footstep sounds
- Voice line queue system
- Occlusion and reverb
- Audio mixing by category
- Pool-based audio components
- Memory management

---

## Enums & Types

### SoundCategory
Sound category classification for mixing.

| Code Name      | Display Name  | Mix Group | Default Volume | Description                      |
| :------------- | :------------ | :-------- | :------------- | :------------------------------- |
| `SC_Master`    | Master        | Master    | 100%           | Top-level mix, affects all audio |
| `SC_Music`     | Music         | Music     | 80%            | Background music tracks          |
| `SC_SFX`       | Sound Effects | SFX       | 100%           | General sound effects            |
| `SC_Weapons`   | Weapons       | SFX       | 100%           | Gunfire, explosions              |
| `SC_Footsteps` | Footsteps     | SFX       | 90%            | Movement sounds                  |
| `SC_Voice`     | Voice         | Voice     | 100%           | Character voice lines            |
| `SC_Ambient`   | Ambient       | Ambient   | 70%            | Environment ambience             |
| `SC_UI`        | UI            | UI        | 100%           | Menu/HUD sounds                  |
| `SC_VoiceChat` | Voice Chat    | VoiceChat | 80%            | Player communication             |

---

### SoundPriority
Sound playback priority.

| Code Name     | Display Name | Priority | Reserve Channels | Interrupt | Description                      |
| :------------ | :----------- | :------- | :--------------- | :-------- | :------------------------------- |
| `SP_Critical` | Critical     | 100      | 4                | Never     | Player death, extraction, alerts |
| `SP_High`     | High         | 75       | 8                | Low only  | Weapon fire, voice lines         |
| `SP_Medium`   | Medium       | 50       | 16               | Low only  | Footsteps, impacts               |
| `SP_Low`      | Low          | 25       | 0                | Any       | Ambient detail, debris           |
| `SP_Lowest`   | Lowest       | 10       | 0                | Any       | Optional fluff sounds            |

---

### MusicIntensity
Dynamic music intensity level.

| Code Name       | Display Name | Layers Active | Description                   |
| :-------------- | :----------- | :------------ | :---------------------------- |
| `MI_Silent`     | Silent       | 0             | No music (stealth, pre-match) |
| `MI_Ambient`    | Ambient      | 1             | Exploration, light atmosphere |
| `MI_Low`        | Low          | 2             | Tension building, searching   |
| `MI_Medium`     | Medium       | 3             | Combat nearby, alert          |
| `MI_High`       | High         | 4             | Active combat, PvP            |
| `MI_Boss`       | Boss         | 5+            | Boss encounter, special track |
| `MI_Extraction` | Extraction   | 4             | Extraction countdown tension  |

---

### SurfaceType
Surface material for footsteps.

| Code Name      | Display Name | Sound Set             | Volume Mult | Description            |
| :------------- | :----------- | :-------------------- | :---------- | :--------------------- |
| `SFT_Concrete` | Concrete     | SFX_Footstep_Concrete | 1.0×        | Hard urban surfaces    |
| `SFT_Metal`    | Metal        | SFX_Footstep_Metal    | 1.1×        | Metallic floors/grates |
| `SFT_Wood`     | Wood         | SFX_Footstep_Wood     | 0.9×        | Wooden floors/boards   |
| `SFT_Grass`    | Grass        | SFX_Footstep_Grass    | 0.6×        | Outdoor grass          |
| `SFT_Dirt`     | Dirt         | SFX_Footstep_Dirt     | 0.7×        | Dirt/earth             |
| `SFT_Gravel`   | Gravel       | SFX_Footstep_Gravel   | 0.95×       | Loose gravel           |
| `SFT_Water`    | Water        | SFX_Footstep_Water    | 1.15×       | Shallow water          |
| `SFT_Sand`     | Sand         | SFX_Footstep_Sand     | 0.5×        | Desert sand            |
| `SFT_Snow`     | Snow         | SFX_Footstep_Snow     | 0.65×       | Winter snow            |
| `SFT_Tile`     | Tile         | SFX_Footstep_Tile     | 0.85×       | Ceramic/tile floors    |

---

### WeaponSoundType
Weapon sound event type.

| Code Name        | Display Name | Priority | Description          |
| :--------------- | :----------- | :------- | :------------------- |
| `WS_Fire`        | Fire         | High     | Gunshot firing       |
| `WS_FireTail`    | Fire Tail    | Medium   | Gunshot tail/reverb  |
| `WS_FireAuto`    | Fire Auto    | High     | Automatic fire loop  |
| `WS_Reload`      | Reload       | Medium   | Magazine reload      |
| `WS_ReloadEmpty` | Reload Empty | Medium   | Empty mag reload     |
| `WS_Equip`       | Equip        | Low      | Weapon draw          |
| `WS_DryFire`     | Dry Fire     | Medium   | Click on empty       |
| `WS_MechAction`  | Mech Action  | Low      | Cocking/bolt action  |
| `WS_ShellCasing` | Shell Casing | Low      | Casing ejection/land |

---

### VoiceLineType
Voice line category.

| Code Name     | Display Name | Priority | Cooldown | Description             |
| :------------ | :----------- | :------- | :------- | :---------------------- |
| `VL_Combat`   | Combat       | High     | 3s       | Combat callouts         |
| `VL_Reload`   | Reload       | Medium   | 5s       | Reloading announcements |
| `VL_Hurt`     | Hurt         | High     | 2s       | Damage reactions        |
| `VL_Death`    | Death        | Critical | 0s       | Death screams           |
| `VL_Interact` | Interact     | Low      | 1s       | Looting/interaction     |
| `VL_Spot`     | Spot         | High     | 4s       | Enemy spotted           |
| `VL_Tactical` | Tactical     | Medium   | 5s       | Team callouts           |
| `VL_Idle`     | Idle         | Lowest   | 30s      | Idle chatter            |

---

### AudioOcclusion
Sound occlusion state.

| Code Name    | Display Name | Volume Mult | LowPass Hz | Reverb | Description         |
| :----------- | :----------- | :---------- | :--------- | :----- | :------------------ |
| `AO_None`    | None         | 100%        | 22000      | 0.0    | Clear line of sight |
| `AO_Partial` | Partial      | 70%         | 8000       | 0.3    | Thin wall/door      |
| `AO_Full`    | Full         | 30%         | 2000       | 0.6    | Thick wall          |
| `AO_Muffled` | Muffled      | 20%         | 800        | 0.8    | Underwater/gas      |
| `AO_Indoor`  | Indoor       | 100%        | 22000      | 0.4    | Indoor reverb       |
| `AO_Outdoor` | Outdoor      | 100%        | 22000      | 0.0    | Normal outdoor      |

---

### MixPreset
Audio mix preset for scenarios.

| Code Name      | Display Name | Music dB | SFX dB | Voice dB | Ambient dB | Description       |
| :------------- | :----------- | :------- | :----- | :------- | :--------- | :---------------- |
| `MP_Default`   | Default      | 0        | 0      | 0        | 0          | Normal gameplay   |
| `MP_Combat`    | Combat       | -3       | +3     | +2       | -6         | Combat focus      |
| `MP_Menu`      | Menu         | -2       | -4     | 0        | -10        | Menu/lobby        |
| `MP_LowHealth` | Low Health   | -6       | -2     | +3       | -8         | Low health filter |
| `MP_Stealth`   | Stealth      | -4       | -2     | +1       | +2         | Quiet/sneaking    |

---

### StingerType
One-shot music stinger type.

| Code Name        | Display Name     | Duration | Description         |
| :--------------- | :--------------- | :------- | :------------------ |
| `STG_Kill`       | Kill             | 1.5s     | Enemy eliminated    |
| `STG_Death`      | Death            | 2.0s     | Player death        |
| `STG_LevelUp`    | Level Up         | 3.0s     | Level milestone     |
| `STG_LootRare`   | Loot Rare        | 2.0s     | Epic/Legendary loot |
| `STG_Extraction` | Extraction Start | 2.5s     | Extraction begins   |
| `STG_Victory`    | Victory          | 4.0s     | Match won           |
| `STG_Defeat`     | Defeat           | 3.0s     | Match lost          |
| `STG_BossSpawn`  | Boss Spawn       | 3.0s     | Boss appears        |

---

## Code Names

### Audio Events

| Code Name         | Trigger            | Parameters                  | Description             |
| :---------------- | :----------------- | :-------------------------- | :---------------------- |
| `SFX_PLAY`        | Sound played       | SoundID, Location, Priority | Sound effect triggered  |
| `SFX_STOP`        | Sound stopped      | SoundID                     | Sound effect ended      |
| `MUSIC_INTENSITY` | Intensity changed  | OldLevel, NewLevel          | Music layer transition  |
| `MUSIC_STINGER`   | Stinger played     | StingerType                 | One-shot music event    |
| `VOICE_PLAY`      | Voice line played  | VoiceLineID, Speaker        | Voice line started      |
| `VOICE_QUEUE`     | Voice line queued  | VoiceLineID, QueuePos       | Voice line waiting      |
| `AUDIO_OCCLUDE`   | Occlusion applied  | SourceID, OcclusionType     | Sound occlusion changed |
| `MIX_CHANGE`      | Mix preset changed | OldPreset, NewPreset        | Audio mix transition    |

### Playback Events

| Code Name          | Trigger          | Parameters            | Description                |
| :----------------- | :--------------- | :-------------------- | :------------------------- |
| `AUDIO_POOL_LIMIT` | Pool exhausted   | Category, ActiveCount | No available channels      |
| `AUDIO_PRELOAD`    | Sounds preloaded | SoundIDs, MemoryUsed  | Sounds loaded to memory    |
| `AUDIO_UNLOAD`     | Sounds unloaded  | SoundIDs, MemoryFreed | Sounds removed from memory |

---

## Architecture

### Class Diagram

```
                    ┌─────────────────┐
                    │  AudioManager   │
                    │   (Singleton)   │
                    └────────┬────────┘
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
┌───▼───────┐    ┌───────────▼───────────┐    ┌───────▼───────┐
│MusicMgr   │    │     MixManager        │    │SoundPoolMgr   │
│           │    │                       │    │               │
└───────────┘    └───────────────────────┘    └───────────────┘
    │                        │                        │
    │            ┌───────────┼───────────┐           │
    │            │           │           │           │
    │    ┌───────▼───┐ ┌─────▼────┐ ┌────▼────┐     │
    │    │VoiceLine  │ │Footstep  │ │Occlusion│     │
    │    │ Manager   │ │ Manager  │ │ Manager │     │
    │    └───────────┘ └──────────┘ └─────────┘     │
    │                                                │
    └────────────────────────────────────────────────┘
```

---

## Core Classes

### AudioManager

**Purpose:** Central audio controller and subsystem access.

```
CLASS AudioManager:
    STATIC instance: AudioManager
    
    // Sub-managers
    musicManager: MusicManager
    voiceLineManager: VoiceLineManager
    footstepManager: FootstepManager
    mixManager: MixManager
    occlusionManager: OcclusionManager
    soundPoolManager: SoundPoolManager
    memoryManager: AudioMemoryManager
    
    // Volume levels
    categoryVolumes: Map<SoundCategory, Float>
    
    // Events
    OnSoundPlayed: Event<(soundId, location)>
    
    FUNCTION PlaySound(soundID: String, location: Vector3, priority: SoundPriority = SP_Medium) -> AudioComponent:
        // Check if can play
        IF NOT soundPoolManager.CanPlaySound(priority):
            LOG_WARNING("Audio channel limit reached for priority: " + priority)
            RETURN null
        END IF
        
        // Get pooled component
        component = soundPoolManager.GetPooledComponent()
        IF component == null:
            RETURN null
        END IF
        
        // Setup component
        soundData = GetSoundData(soundID)
        component.SetSound(soundData.soundWave)
        component.SetWorldLocation(location)
        component.SetVolumeMultiplier(GetCategoryVolume(soundData.category))
        
        // Apply spatialization
        IF soundData.is3D:
            ApplySpatialSettings(component, soundData)
        END IF
        
        // Play
        component.Play()
        
        EMIT EVENT "SFX_PLAY" WITH (soundID, location, priority)
        
        RETURN component
    END FUNCTION
    
    FUNCTION PlaySound2D(soundID: String, priority: SoundPriority = SP_Medium) -> AudioComponent:
        component = soundPoolManager.GetPooledComponent()
        
        soundData = GetSoundData(soundID)
        component.SetSound(soundData.soundWave)
        component.SetIs3D(false)
        component.SetVolumeMultiplier(GetCategoryVolume(soundData.category))
        
        component.Play()
        
        RETURN component
    END FUNCTION
    
    FUNCTION StopSound(component: AudioComponent):
        component.Stop()
        soundPoolManager.ReturnToPool(component)
        
        EMIT EVENT "SFX_STOP" WITH (component.soundID)
    END FUNCTION
    
    FUNCTION StopAllSounds():
        soundPoolManager.StopAllAndReturn()
    END FUNCTION
    
    FUNCTION SetCategoryVolume(category: SoundCategory, volume: Float):
        categoryVolumes[category] = Clamp(volume, 0, 1)
        
        // Update all active sounds in category
        FOR EACH component IN soundPoolManager.GetActiveComponents():
            IF component.category == category:
                component.SetVolumeMultiplier(volume)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION GetCategoryVolume(category: SoundCategory) -> Float:
        RETURN categoryVolumes.GetOrDefault(category, 1.0)
    END FUNCTION
    
    FUNCTION SetMasterVolume(volume: Float):
        SetCategoryVolume(SC_Master, volume)
    END FUNCTION
    
    FUNCTION PlayWeaponSound(weaponID: String, soundType: WeaponSoundType, location: Vector3):
        soundID = GetWeaponSoundID(weaponID, soundType)
        priority = GetWeaponSoundPriority(soundType)
        
        PlaySound(soundID, location, priority)
    END FUNCTION
    
    FUNCTION PlayFootstep(surface: SurfaceType, location: Vector3, isRunning: Boolean = false):
        footstepManager.PlayFootstep(surface, location, isRunning)
    END FUNCTION
    
    FUNCTION SetMusicIntensity(intensity: MusicIntensity):
        musicManager.SetIntensity(intensity)
    END FUNCTION
    
    FUNCTION PlayStinger(stingerType: StingerType):
        musicManager.PlayStinger(stingerType)
    END FUNCTION
    
    FUNCTION PlayVoiceLine(lineID: String, lineType: VoiceLineType, speaker: Actor):
        voiceLineManager.PlayLine(lineID, lineType, speaker)
    END FUNCTION
    
    FUNCTION SetMixPreset(preset: MixPreset, transitionTime: Float = 1.0):
        mixManager.SetPreset(preset, transitionTime)
    END FUNCTION
    
    FUNCTION PreloadSoundsForArea(areaID: String):
        soundIDs = GetSoundsForArea(areaID)
        memoryManager.PreloadSounds(soundIDs)
    END FUNCTION

STRUCT SoundData:
    soundID: String
    soundWave: SoundAsset
    category: SoundCategory
    priority: SoundPriority
    is3D: Boolean = true
    maxDistance: Float = 10000.0
    rolloffFactor: Float = 1.0
    variations: Integer = 1
```

---

### MusicManager

**Purpose:** Dynamic music intensity and layer management.

```
CLASS MusicManager:
    // Current state
    currentIntensity: MusicIntensity = MI_Ambient
    targetIntensity: MusicIntensity
    transitionProgress: Float = 1.0
    
    // Music components
    musicLayers: List<AudioComponent>
    activeTrackID: String
    
    // Stinger component
    stingerComponent: AudioComponent
    
    // Config
    intensityTransitionTime: Float = 3.0
    
    // Events
    OnIntensityChanged: Event<(oldIntensity, newIntensity)>
    
    FUNCTION SetIntensity(intensity: MusicIntensity):
        IF intensity == currentIntensity:
            RETURN
        END IF
        
        oldIntensity = currentIntensity
        targetIntensity = intensity
        transitionProgress = 0.0
        
        StartLayerTransition()
        
        OnIntensityChanged.Broadcast(oldIntensity, intensity)
        
        EMIT EVENT "MUSIC_INTENSITY" WITH (oldIntensity, intensity)
    END FUNCTION
    
    FUNCTION GetCurrentIntensity() -> MusicIntensity:
        RETURN currentIntensity
    END FUNCTION
    
    FUNCTION PlayStinger(stingerType: StingerType):
        stingerData = GetStingerData(stingerType)
        
        // Duck music briefly
        DuckMusic(stingerData.duration, -6.0)
        
        stingerComponent.SetSound(stingerData.sound)
        stingerComponent.Play()
        
        EMIT EVENT "MUSIC_STINGER" WITH (stingerType)
    END FUNCTION
    
    FUNCTION PlayTrack(trackID: String, fadeInTime: Float = 2.0):
        IF activeTrackID == trackID:
            RETURN
        END IF
        
        // Fade out current
        IF activeTrackID != "":
            FadeOutTrack(fadeInTime)
        END IF
        
        // Load and fade in new track
        trackData = GetTrackData(trackID)
        
        FOR i = 0 TO trackData.layerCount:
            layer = musicLayers[i]
            layer.SetSound(trackData.layers[i])
            layer.FadeIn(fadeInTime)
        END FOR
        
        activeTrackID = trackID
    END FUNCTION
    
    FUNCTION StopMusic(fadeOutTime: Float = 2.0):
        FOR EACH layer IN musicLayers:
            layer.FadeOut(fadeOutTime)
        END FOR
        
        activeTrackID = ""
        currentIntensity = MI_Silent
    END FUNCTION
    
    FUNCTION StartLayerTransition():
        activeLayers = GetActiveLayerCount(targetIntensity)
        
        FOR i = 0 TO musicLayers.Count:
            layer = musicLayers[i]
            
            IF i < activeLayers:
                layer.FadeIn(intensityTransitionTime)
            ELSE:
                layer.FadeOut(intensityTransitionTime)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION DuckMusic(duration: Float, duckDB: Float):
        originalVolume = GetMusicVolume()
        duckedVolume = DBToLinear(LinearToDB(originalVolume) + duckDB)
        
        FOR EACH layer IN musicLayers:
            layer.SetVolumeMultiplier(duckedVolume)
        END FOR
        
        SetTimer(duration, LAMBDA:
            FOR EACH layer IN musicLayers:
                layer.FadeVolumeTo(originalVolume, 0.5)
            END FOR
        END LAMBDA)
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        IF transitionProgress < 1.0:
            transitionProgress += deltaTime / intensityTransitionTime
            transitionProgress = Min(transitionProgress, 1.0)
            
            IF transitionProgress >= 1.0:
                currentIntensity = targetIntensity
            END IF
        END IF
    END FUNCTION

STRUCT MusicTrackData:
    trackID: String
    layers: List<SoundAsset>
    layerCount: Integer
    bpm: Float
    loopPoint: Float

STRUCT StingerData:
    stingerType: StingerType
    sound: SoundAsset
    duration: Float
    duckAmount: Float = -6.0

// Music track configurations
CONST MUSIC_TRACKS = {
    "MSC_Map1_Main": { layerCount: 5, bpm: 120, loopPoint: 32.0 },
    "MSC_Map2_Main": { layerCount: 5, bpm: 140, loopPoint: 64.0 },
    "MSC_Boss_Warden": { layerCount: 6, bpm: 160, loopPoint: 48.0 }
}

// Intensity layer counts
CONST INTENSITY_LAYERS = {
    MI_Silent: 0,
    MI_Ambient: 1,
    MI_Low: 2,
    MI_Medium: 3,
    MI_High: 4,
    MI_Boss: 5,
    MI_Extraction: 4
}
```

---

### VoiceLineManager

**Purpose:** Voice line queue and cooldown management.

```
CLASS VoiceLineManager:
    // Queue
    voiceLineQueue: List<QueuedVoiceLine>
    currentlyPlaying: VoiceLineData
    
    // Cooldowns
    typeCooldowns: Map<VoiceLineType, Float>
    speakerCooldowns: Map<Actor, Float>
    
    // Active component
    voiceComponent: AudioComponent
    
    // Config
    maxQueueSize: Integer = 3
    globalCooldown: Float = 0.5
    
    FUNCTION PlayLine(lineID: String, lineType: VoiceLineType, speaker: Actor) -> Boolean:
        // Check cooldowns
        IF NOT CanPlayLine(lineType, speaker):
            RETURN false
        END IF
        
        lineData = GetVoiceLineData(lineID)
        
        // If something playing, queue if high enough priority
        IF IsPlaying():
            IF lineData.priority > currentlyPlaying.priority:
                QueueLine(lineID, lineType, speaker)
            END IF
            RETURN false
        END IF
        
        // Play directly
        PlayLineImmediate(lineData, speaker)
        
        SetCooldown(lineType, speaker)
        
        EMIT EVENT "VOICE_PLAY" WITH (lineID, speaker)
        
        RETURN true
    END FUNCTION
    
    FUNCTION QueueLine(lineID: String, lineType: VoiceLineType, speaker: Actor):
        IF voiceLineQueue.Count >= maxQueueSize:
            // Remove lowest priority
            RemoveLowestPriority()
        END IF
        
        queuedLine = NEW QueuedVoiceLine()
        queuedLine.lineID = lineID
        queuedLine.lineType = lineType
        queuedLine.speaker = speaker
        queuedLine.timestamp = GetTime()
        
        voiceLineQueue.Add(queuedLine)
        
        // Sort by priority
        voiceLineQueue.SortBy(line => -line.priority)
        
        EMIT EVENT "VOICE_QUEUE" WITH (lineID, voiceLineQueue.IndexOf(queuedLine))
    END FUNCTION
    
    FUNCTION PlayLineImmediate(lineData: VoiceLineData, speaker: Actor):
        voiceComponent.SetSound(lineData.soundAsset)
        voiceComponent.SetWorldLocation(speaker.GetLocation())
        voiceComponent.Play()
        
        currentlyPlaying = lineData
        
        // Set callback for when finished
        voiceComponent.OnComplete.AddListener(LAMBDA:
            OnLineFinished()
        END LAMBDA)
    END FUNCTION
    
    FUNCTION OnLineFinished():
        currentlyPlaying = null
        
        // Play next in queue
        IF voiceLineQueue.Count > 0:
            nextLine = voiceLineQueue.RemoveFirst()
            
            IF CanPlayLine(nextLine.lineType, nextLine.speaker):
                lineData = GetVoiceLineData(nextLine.lineID)
                PlayLineImmediate(lineData, nextLine.speaker)
                SetCooldown(nextLine.lineType, nextLine.speaker)
            ELSE:
                OnLineFinished() // Try next
            END IF
        END IF
    END FUNCTION
    
    FUNCTION CanPlayLine(lineType: VoiceLineType, speaker: Actor) -> Boolean:
        // Check type cooldown
        IF typeCooldowns.Contains(lineType):
            IF GetTime() < typeCooldowns[lineType]:
                RETURN false
            END IF
        END IF
        
        // Check speaker cooldown
        IF speakerCooldowns.Contains(speaker):
            IF GetTime() < speakerCooldowns[speaker]:
                RETURN false
            END IF
        END IF
        
        RETURN true
    END FUNCTION
    
    FUNCTION IsPlaying() -> Boolean:
        RETURN currentlyPlaying != null AND voiceComponent.IsPlaying()
    END FUNCTION
    
    FUNCTION CancelQueue():
        voiceLineQueue.Clear()
    END FUNCTION
    
    FUNCTION CancelCurrent():
        IF IsPlaying():
            voiceComponent.Stop()
            currentlyPlaying = null
        END IF
    END FUNCTION
    
    FUNCTION SetCooldown(lineType: VoiceLineType, speaker: Actor):
        cooldownDuration = GetCooldownForType(lineType)
        typeCooldowns[lineType] = GetTime() + cooldownDuration
        speakerCooldowns[speaker] = GetTime() + globalCooldown
    END FUNCTION

STRUCT VoiceLineData:
    lineID: String
    lineType: VoiceLineType
    soundAsset: SoundAsset
    priority: Integer
    duration: Float
    subtitleText: String

STRUCT QueuedVoiceLine:
    lineID: String
    lineType: VoiceLineType
    speaker: Actor
    priority: Integer
    timestamp: Float

// Voice line cooldowns per type
CONST VOICE_LINE_COOLDOWNS = {
    VL_Combat: 3.0,
    VL_Reload: 5.0,
    VL_Hurt: 2.0,
    VL_Death: 0.0,
    VL_Interact: 1.0,
    VL_Spot: 4.0,
    VL_Tactical: 5.0,
    VL_Idle: 30.0
}
```

---

### FootstepManager

**Purpose:** Surface-aware footstep sounds.

```
CLASS FootstepManager:
    // Sound pools per surface
    footstepSounds: Map<SurfaceType, List<SoundAsset>>
    
    // Last played tracking (for variation)
    lastPlayedIndex: Map<SurfaceType, Integer>
    
    // Config
    walkVolume: Float = 0.7
    runVolume: Float = 1.0
    crouchVolume: Float = 0.3
    
    FUNCTION PlayFootstep(surface: SurfaceType, location: Vector3, isRunning: Boolean = false, isCrouched: Boolean = false):
        // Get surface config
        config = GetSurfaceConfig(surface)
        
        // Get random sound (avoiding repeat)
        soundAsset = GetRandomFootstepSound(surface)
        
        // Calculate volume
        baseVolume = walkVolume
        IF isRunning:
            baseVolume = runVolume
        ELSE IF isCrouched:
            baseVolume = crouchVolume
        END IF
        
        finalVolume = baseVolume * config.volumeMultiplier
        
        // Play
        AudioManager.PlaySound(soundAsset.ID, location, SP_Medium)
    END FUNCTION
    
    FUNCTION PlayLanding(surface: SurfaceType, location: Vector3, fallHeight: Float):
        intensity = Clamp(fallHeight / 500.0, 0.5, 1.5)
        
        soundID = "SFX_Land_" + surface.ToString()
        
        component = AudioManager.PlaySound(soundID, location, SP_Medium)
        component.SetVolumeMultiplier(intensity)
    END FUNCTION
    
    FUNCTION DetectSurface(location: Vector3) -> SurfaceType:
        // Trace down to detect physical material
        hit = TraceLineDown(location, 100.0)
        
        IF hit.IsValid:
            physMat = hit.GetPhysicalMaterial()
            RETURN GetSurfaceFromPhysMat(physMat)
        END IF
        
        RETURN SFT_Concrete // Default
    END FUNCTION
    
    FUNCTION GetRandomFootstepSound(surface: SurfaceType) -> SoundAsset:
        sounds = footstepSounds[surface]
        
        IF sounds.IsEmpty():
            RETURN defaultFootstepSound
        END IF
        
        // Avoid playing same sound twice
        lastIndex = lastPlayedIndex.GetOrDefault(surface, -1)
        newIndex = Random.RangeExcluding(0, sounds.Count, lastIndex)
        
        lastPlayedIndex[surface] = newIndex
        
        RETURN sounds[newIndex]
    END FUNCTION

STRUCT SurfaceConfig:
    surfaceType: SurfaceType
    volumeMultiplier: Float
    pitchVariation: Float = 0.1
    soundSet: String

// Surface configurations
CONST SURFACE_CONFIGS = {
    SFT_Concrete: { volumeMult: 1.0, pitchVar: 0.05 },
    SFT_Metal: { volumeMult: 1.1, pitchVar: 0.1 },
    SFT_Wood: { volumeMult: 0.9, pitchVar: 0.1 },
    SFT_Grass: { volumeMult: 0.6, pitchVar: 0.15 },
    SFT_Dirt: { volumeMult: 0.7, pitchVar: 0.1 },
    SFT_Gravel: { volumeMult: 0.95, pitchVar: 0.15 },
    SFT_Water: { volumeMult: 1.15, pitchVar: 0.2 }
}
```

---

### WeaponSoundComponent

**Purpose:** Weapon audio with fire/reload sounds.

```
CLASS WeaponSoundComponent:
    // Parent weapon
    owningWeapon: Weapon
    
    // Sound data
    weaponSoundData: WeaponSoundData
    
    // Fire tracking
    lastFireTime: Float
    isAutoFiring: Boolean = false
    autoFireComponent: AudioComponent
    
    FUNCTION PlayFire():
        location = owningWeapon.GetMuzzleLocation()
        
        // Main fire sound
        AudioManager.PlaySound(weaponSoundData.fireSound, location, SP_High)
        
        // Fire tail (distant echo)
        IF weaponSoundData.fireTailSound != "":
            SetTimer(0.05, LAMBDA:
                AudioManager.PlaySound(weaponSoundData.fireTailSound, location, SP_Low)
            END LAMBDA)
        END IF
        
        // Shell casing
        IF weaponSoundData.shellCasingSound != "":
            SetTimer(0.1, LAMBDA:
                AudioManager.PlaySound(weaponSoundData.shellCasingSound, location, SP_Lowest)
            END LAMBDA)
        END IF
        
        lastFireTime = GetTime()
    END FUNCTION
    
    FUNCTION StartAutoFire():
        IF isAutoFiring:
            RETURN
        END IF
        
        isAutoFiring = true
        
        // Use looping fire sound for auto
        IF weaponSoundData.autoFireLoop != "":
            autoFireComponent = AudioManager.PlaySound(weaponSoundData.autoFireLoop, owningWeapon.GetMuzzleLocation(), SP_High)
            autoFireComponent.SetLooping(true)
        END IF
    END FUNCTION
    
    FUNCTION StopAutoFire():
        IF NOT isAutoFiring:
            RETURN
        END IF
        
        isAutoFiring = false
        
        IF autoFireComponent != null:
            autoFireComponent.FadeOut(0.1)
            autoFireComponent = null
        END IF
        
        // Play fire tail on stop
        IF weaponSoundData.fireTailSound != "":
            AudioManager.PlaySound(weaponSoundData.fireTailSound, owningWeapon.GetMuzzleLocation(), SP_Low)
        END IF
    END FUNCTION
    
    FUNCTION PlayReload(isEmpty: Boolean = false):
        soundID = isEmpty ? weaponSoundData.reloadEmptySound : weaponSoundData.reloadSound
        location = owningWeapon.GetLocation()
        
        AudioManager.PlaySound(soundID, location, SP_Medium)
    END FUNCTION
    
    FUNCTION PlayEquip():
        AudioManager.PlaySound(weaponSoundData.equipSound, owningWeapon.GetLocation(), SP_Low)
    END FUNCTION
    
    FUNCTION PlayDryFire():
        AudioManager.PlaySound(weaponSoundData.dryFireSound, owningWeapon.GetMuzzleLocation(), SP_Medium)
    END FUNCTION
    
    FUNCTION PlayMechAction(actionType: String):
        actionSound = weaponSoundData.mechActions.GetOrDefault(actionType, "")
        
        IF actionSound != "":
            AudioManager.PlaySound(actionSound, owningWeapon.GetLocation(), SP_Low)
        END IF
    END FUNCTION

STRUCT WeaponSoundData:
    weaponID: String
    fireSound: String
    fireTailSound: String
    autoFireLoop: String
    reloadSound: String
    reloadEmptySound: String
    equipSound: String
    dryFireSound: String
    shellCasingSound: String
    mechActions: Map<String, String>

// Weapon sound configurations
CONST WEAPON_SOUNDS = {
    "WPN_AR_M4": {
        fireSound: "SFX_M4_Fire",
        fireTailSound: "SFX_AR_Tail",
        autoFireLoop: "SFX_M4_AutoLoop",
        reloadSound: "SFX_AR_Reload",
        reloadEmptySound: "SFX_AR_ReloadEmpty",
        equipSound: "SFX_Rifle_Equip",
        dryFireSound: "SFX_DryFire"
    },
    "WPN_SMG_MP5": {
        fireSound: "SFX_MP5_Fire",
        fireTailSound: "SFX_SMG_Tail",
        autoFireLoop: "SFX_MP5_AutoLoop",
        reloadSound: "SFX_SMG_Reload"
    }
}
```

---

### MixManager

**Purpose:** Audio mixing and preset transitions.

```
CLASS MixManager:
    // Current state
    currentPreset: MixPreset = MP_Default
    targetPreset: MixPreset
    transitionProgress: Float = 1.0
    
    // Mix settings
    currentMixSettings: MixSettings
    
    // Config
    transitionTime: Float = 1.0
    
    FUNCTION SetPreset(preset: MixPreset, transitionTime: Float = 1.0):
        IF preset == currentPreset AND transitionProgress >= 1.0:
            RETURN
        END IF
        
        targetPreset = preset
        this.transitionTime = transitionTime
        transitionProgress = 0.0
        
        EMIT EVENT "MIX_CHANGE" WITH (currentPreset, preset)
    END FUNCTION
    
    FUNCTION GetCurrentPreset() -> MixPreset:
        RETURN currentPreset
    END FUNCTION
    
    FUNCTION GetMusicVolume() -> Float:
        RETURN currentMixSettings.musicVolume
    END FUNCTION
    
    FUNCTION GetSFXVolume() -> Float:
        RETURN currentMixSettings.sfxVolume
    END FUNCTION
    
    FUNCTION GetVoiceVolume() -> Float:
        RETURN currentMixSettings.voiceVolume
    END FUNCTION
    
    FUNCTION GetAmbientVolume() -> Float:
        RETURN currentMixSettings.ambientVolume
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        IF transitionProgress < 1.0:
            transitionProgress += deltaTime / transitionTime
            transitionProgress = Min(transitionProgress, 1.0)
            
            // Lerp mix settings
            fromSettings = GetPresetSettings(currentPreset)
            toSettings = GetPresetSettings(targetPreset)
            
            currentMixSettings = LerpMixSettings(fromSettings, toSettings, transitionProgress)
            
            // Apply to audio system
            ApplyMixSettings(currentMixSettings)
            
            IF transitionProgress >= 1.0:
                currentPreset = targetPreset
            END IF
        END IF
    END FUNCTION
    
    FUNCTION ApplyMixSettings(settings: MixSettings):
        AudioManager.SetCategoryVolume(SC_Music, DBToLinear(settings.musicDB))
        AudioManager.SetCategoryVolume(SC_SFX, DBToLinear(settings.sfxDB))
        AudioManager.SetCategoryVolume(SC_Voice, DBToLinear(settings.voiceDB))
        AudioManager.SetCategoryVolume(SC_Ambient, DBToLinear(settings.ambientDB))
        
        // Apply effects if applicable
        IF settings.lowPassFilter > 0:
            ApplyLowPassFilter(settings.lowPassFilter)
        END IF
        
        IF settings.heartbeatOverlay:
            EnableHeartbeatEffect()
        ELSE:
            DisableHeartbeatEffect()
        END IF
    END FUNCTION

STRUCT MixSettings:
    musicDB: Float = 0.0
    sfxDB: Float = 0.0
    voiceDB: Float = 0.0
    ambientDB: Float = 0.0
    lowPassFilter: Float = 0.0
    heartbeatOverlay: Boolean = false

// Mix preset configurations
CONST MIX_PRESETS = {
    MP_Default: { musicDB: 0.0, sfxDB: 0.0, voiceDB: 0.0, ambientDB: 0.0 },
    MP_Combat: { musicDB: -3.0, sfxDB: +3.0, voiceDB: +2.0, ambientDB: -6.0 },
    MP_Menu: { musicDB: -2.0, sfxDB: -4.0, voiceDB: 0.0, ambientDB: -10.0 },
    MP_LowHealth: { musicDB: -6.0, sfxDB: -2.0, voiceDB: +3.0, ambientDB: -8.0, lowPassFilter: 2000.0, heartbeatOverlay: true },
    MP_Stealth: { musicDB: -4.0, sfxDB: -2.0, voiceDB: +1.0, ambientDB: +2.0 }
}
```

---

### OcclusionManager

**Purpose:** Sound occlusion calculation and application.

```
CLASS OcclusionManager:
    FUNCTION CalculateOcclusion(source: Vector3, listener: Vector3) -> AudioOcclusion:
        // Trace from listener to source
        hit = TraceLine(listener, source)
        
        IF NOT hit.IsValid:
            RETURN AO_None // Clear line of sight
        END IF
        
        // Get occlusion from material
        occlusion = GetOcclusionFromMaterial(hit.GetPhysicalMaterial())
        
        // Check for multiple obstructions
        obstructionCount = CountObstructions(listener, source)
        
        IF obstructionCount > 2:
            RETURN AO_Full
        ELSE IF obstructionCount > 1:
            RETURN UpgradeOcclusion(occlusion)
        END IF
        
        RETURN occlusion
    END FUNCTION
    
    FUNCTION GetOcclusionMultiplier(occlusion: AudioOcclusion) -> Float:
        RETURN OCCLUSION_SETTINGS[occlusion].volumeMultiplier
    END FUNCTION
    
    FUNCTION GetLowPassFrequency(occlusion: AudioOcclusion) -> Float:
        RETURN OCCLUSION_SETTINGS[occlusion].lowPassHz
    END FUNCTION
    
    FUNCTION ApplyOcclusionToComponent(component: AudioComponent, occlusion: AudioOcclusion):
        settings = OCCLUSION_SETTINGS[occlusion]
        
        component.SetVolumeMultiplier(component.GetBaseVolume() * settings.volumeMultiplier)
        component.SetLowPassFilterFrequency(settings.lowPassHz)
        
        IF settings.reverbSend > 0:
            component.SetReverbSendLevel(settings.reverbSend)
        END IF
        
        EMIT EVENT "AUDIO_OCCLUDE" WITH (component.ID, occlusion)
    END FUNCTION
    
    FUNCTION GetOcclusionFromMaterial(material: PhysicalMaterial) -> AudioOcclusion:
        IF material == null:
            RETURN AO_Partial
        END IF
        
        SWITCH material.surfaceType:
            CASE Glass: RETURN AO_Partial
            CASE Concrete: RETURN AO_Full
            CASE Metal: RETURN AO_Full
            CASE Wood: RETURN AO_Partial
            CASE Fabric: RETURN AO_Partial
            DEFAULT: RETURN AO_Partial
        END SWITCH
    END FUNCTION

STRUCT OcclusionSettings:
    volumeMultiplier: Float
    lowPassHz: Float
    reverbSend: Float

// Occlusion configurations
CONST OCCLUSION_SETTINGS = {
    AO_None: { volumeMultiplier: 1.0, lowPassHz: 22000.0, reverbSend: 0.0 },
    AO_Partial: { volumeMultiplier: 0.7, lowPassHz: 8000.0, reverbSend: 0.3 },
    AO_Full: { volumeMultiplier: 0.3, lowPassHz: 2000.0, reverbSend: 0.6 },
    AO_Muffled: { volumeMultiplier: 0.2, lowPassHz: 800.0, reverbSend: 0.8 },
    AO_Indoor: { volumeMultiplier: 1.0, lowPassHz: 22000.0, reverbSend: 0.4 },
    AO_Outdoor: { volumeMultiplier: 1.0, lowPassHz: 22000.0, reverbSend: 0.0 }
}
```

---

### SpatialAudioSettings

**Purpose:** 3D audio configuration.

```
STRUCT SpatialAudioSettings:
    // Distance Model
    model: DistanceModel = Logarithmic
    referenceDistance: Float = 100.0   // 1m
    maxDistance: Float = 10000.0       // 100m
    rolloffFactor: Float = 1.0
    
    // Spatialization
    useHRTF: Boolean = true
    stereoSpread: Float = 0.5
    
    // Focus
    focusAzimuth: Float = 30.0         // Front cone
    focusDistanceScale: Float = 1.0
    nonFocusDistanceScale: Float = 0.5

ENUM DistanceModel:
    Linear, Logarithmic, Inverse

// Per-category spatial settings
CONST CATEGORY_SPATIAL_SETTINGS = {
    SC_Weapons: { maxDistance: 30000.0, rolloffFactor: 0.8 },  // 300m (gunshots travel far)
    SC_Footsteps: { maxDistance: 3000.0, rolloffFactor: 1.2 }, // 30m (faster falloff)
    SC_Ambient: { maxDistance: 5000.0, rolloffFactor: 0.5 }    // 50m (slower falloff)
}
```

---

### SoundPoolManager

**Purpose:** Audio component pooling and channel management.

```
CLASS SoundPoolManager:
    // Pool
    pool: List<AudioComponent>
    activeComponents: List<AudioComponent>
    
    // Config
    initialPoolSize: Integer = 32
    maxPoolSize: Integer = 64
    
    // Priority tracking
    componentPriorities: Map<AudioComponent, SoundPriority>
    
    FUNCTION GetPooledComponent() -> AudioComponent:
        // Find available in pool
        FOR EACH component IN pool:
            IF NOT component.IsPlaying():
                pool.Remove(component)
                activeComponents.Add(component)
                RETURN component
            END IF
        END FOR
        
        // Expand pool if possible
        IF pool.Count + activeComponents.Count < maxPoolSize:
            component = CreateAudioComponent()
            activeComponents.Add(component)
            RETURN component
        END IF
        
        // Pool exhausted
        EMIT EVENT "AUDIO_POOL_LIMIT" WITH (activeComponents.Count)
        RETURN null
    END FUNCTION
    
    FUNCTION ReturnToPool(component: AudioComponent):
        component.Stop()
        component.ResetToDefaults()
        
        activeComponents.Remove(component)
        pool.Add(component)
        
        componentPriorities.Remove(component)
    END FUNCTION
    
    FUNCTION GetActiveCount() -> Integer:
        RETURN activeComponents.Count
    END FUNCTION
    
    FUNCTION GetPoolSize() -> Integer:
        RETURN pool.Count + activeComponents.Count
    END FUNCTION
    
    FUNCTION CanPlaySound(priority: SoundPriority) -> Boolean:
        // High priority sounds can steal from lower
        IF priority >= SP_High:
            RETURN true
        END IF
        
        // Check if we have available slots
        IF GetActiveCount() < maxPoolSize:
            RETURN true
        END IF
        
        // Check if we can steal from lower priority
        FOR EACH component IN activeComponents:
            IF componentPriorities[component] < priority:
                RETURN true
            END IF
        END FOR
        
        RETURN false
    END FUNCTION
    
    FUNCTION StopLowestPrioritySound():
        lowestComponent = null
        lowestPriority = SP_Critical
        
        FOR EACH component IN activeComponents:
            priority = componentPriorities[component]
            IF priority < lowestPriority:
                lowestPriority = priority
                lowestComponent = component
            END IF
        END FOR
        
        IF lowestComponent != null:
            ReturnToPool(lowestComponent)
        END IF
    END FUNCTION
    
    FUNCTION StopAllAndReturn():
        FOR EACH component IN activeComponents.ToList():
            ReturnToPool(component)
        END FOR
    END FUNCTION
    
    FUNCTION GetActiveComponents() -> List<AudioComponent>:
        RETURN activeComponents.ToList()
    END FUNCTION

// Channel limits by device tier
CONST CHANNEL_LIMITS:
    LowEnd = 16
    MidRange = 32
    HighEnd = 64
```

---

### AudioMemoryManager

**Purpose:** Sound memory budget management.

```
CLASS AudioMemoryManager:
    // Loaded sounds
    loadedSounds: Map<String, SoundAsset>
    
    // Memory tracking
    currentMemoryBytes: Integer = 0
    maxMemoryBytes: Integer = 157286400  // 150 MB
    
    FUNCTION GetCurrentMemoryUsage() -> Integer:
        RETURN currentMemoryBytes
    END FUNCTION
    
    FUNCTION PreloadSounds(soundIDs: List<String>):
        memoryToLoad = 0
        
        FOR EACH soundID IN soundIDs:
            IF NOT loadedSounds.Contains(soundID):
                soundData = GetSoundMetadata(soundID)
                memoryToLoad += soundData.sizeBytes
            END IF
        END FOR
        
        // Check if we need to unload some sounds
        IF currentMemoryBytes + memoryToLoad > maxMemoryBytes:
            FreeMemory(memoryToLoad)
        END IF
        
        // Load sounds
        FOR EACH soundID IN soundIDs:
            IF NOT loadedSounds.Contains(soundID):
                sound = LoadSoundAsset(soundID)
                loadedSounds[soundID] = sound
                currentMemoryBytes += sound.GetSizeBytes()
            END IF
        END FOR
        
        EMIT EVENT "AUDIO_PRELOAD" WITH (soundIDs, memoryToLoad)
    END FUNCTION
    
    FUNCTION UnloadSounds(soundIDs: List<String>):
        memoryFreed = 0
        
        FOR EACH soundID IN soundIDs:
            IF loadedSounds.Contains(soundID):
                sound = loadedSounds[soundID]
                memoryFreed += sound.GetSizeBytes()
                
                sound.Unload()
                loadedSounds.Remove(soundID)
            END IF
        END FOR
        
        currentMemoryBytes -= memoryFreed
        
        EMIT EVENT "AUDIO_UNLOAD" WITH (soundIDs, memoryFreed)
    END FUNCTION
    
    FUNCTION UnloadDistantSounds(playerLocation: Vector3, distance: Float):
        toUnload = []
        
        FOR EACH (soundID, sound) IN loadedSounds:
            IF NOT IsNearPlayer(sound.associatedLocation, playerLocation, distance):
                toUnload.Add(soundID)
            END IF
        END FOR
        
        UnloadSounds(toUnload)
    END FUNCTION
    
    FUNCTION FreeMemory(bytesNeeded: Integer):
        // Prioritize unloading less important sounds
        // Using LRU (Least Recently Used)
        
        sortedSounds = loadedSounds.Values.SortBy(s => s.lastUsedTime)
        memoryFreed = 0
        
        FOR EACH sound IN sortedSounds:
            IF memoryFreed >= bytesNeeded:
                BREAK
            END IF
            
            IF CanUnload(sound):
                memoryFreed += sound.GetSizeBytes()
                UnloadSounds([sound.ID])
            END IF
        END FOR
    END FUNCTION

// Target memory budget
CONST AUDIO_MEMORY_BUDGET:
    MusicStreamBuffer = 30   // MB
    SFXLoaded = 80           // MB
    VoiceLoaded = 30         // MB
    Reserve = 10             // MB
    Total = 150              // MB
```

---

## Audio Settings Data

```
STRUCT AudioSettings:
    // Volume levels (0-1)
    masterVolume: Float = 1.0
    musicVolume: Float = 0.8
    sfxVolume: Float = 1.0
    voiceVolume: Float = 1.0
    voiceChatVolume: Float = 0.8
    
    // Options
    monoAudio: Boolean = false
    subtitlesEnabled: Boolean = true
    visualSoundIndicators: Boolean = false
    reduceBackgroundAudio: Boolean = false
    
    // Quality
    quality: AudioQuality = Medium
    useHRTF: Boolean = true

ENUM AudioQuality:
    Low,     // 16 channels, compressed
    Medium,  // 32 channels, standard
    High     // 64 channels, high quality
```

---

## Audio File Specifications

```
CONST AUDIO_FILE_SPECS:
    // Music
    MusicFormat = "ogg"
    MusicBitrate = 128000     // 128 kbps
    MusicSampleRate = 44100
    MusicStreamed = true
    
    // SFX
    SFXFormat = "ogg"
    SFXBitrate = 96000        // 96 kbps
    SFXSampleRate = 44100
    SFXStreamed = false
    
    // Voice
    VoiceFormat = "ogg"
    VoiceBitrate = 64000      // 64 kbps
    VoiceSampleRate = 22050
    VoiceStreamed = false
    
    // UI
    UIFormat = "wav"
    UISampleRate = 44100
```

---

## Sound Class Hierarchy

```
Master
├── Music (DuckTarget)
├── SFX
│   ├── Weapons
│   │   ├── WeaponsFire
│   │   ├── WeaponsReload
│   │   └── WeaponsFoley
│   ├── Footsteps
│   ├── Abilities
│   ├── Impacts
│   └── Interactions
├── Ambient
│   ├── Environment
│   ├── Weather
│   └── Hazards
├── Voice
│   ├── Player
│   ├── AI
│   └── Radio
├── UI
│   ├── Menu
│   ├── HUD
│   └── Notifications
└── VoiceChat
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] AudioManager core playback
- [ ] WeaponSoundComponent
- [ ] MusicManager with intensity
- [ ] FootstepManager with surfaces
- [ ] Category volume controls

### MEDIUM Priority 🟡
- [ ] VoiceLineManager with queue
- [ ] MixManager with presets
- [ ] OcclusionManager
- [ ] 3D spatial audio setup
- [ ] SoundPoolManager

### LOW Priority 🟢
- [ ] HRTF implementation
- [ ] Advanced reverb zones
- [ ] Low health audio filter
- [ ] Sound visualization
- [ ] Audio middleware integration

---

## Testing Checklist

- [ ] All weapon types have distinct sounds
- [ ] Footsteps match surface materials
- [ ] Music intensity transitions smoothly
- [ ] Voice lines don't overlap
- [ ] Voice line cooldowns work
- [ ] Occlusion muffles correctly
- [ ] 3D positioning is accurate
- [ ] Channel limits respected
- [ ] Memory budget not exceeded
- [ ] Volume settings persist
- [ ] Mono audio works correctly
- [ ] No audio pops/clicks

---

**[← Back to Index](../README.md)** | **[Next: Narrative System →](./NarrativeSystem.md)**
