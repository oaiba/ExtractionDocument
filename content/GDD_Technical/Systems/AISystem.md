---
title: "AI System - Technical Specification"
type: docs
---
# AI System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: Map System →](./MapSystem.md)**

**Reference:** [High-Level AI Design](../../GDD_HighLevel/AI/EnemyBehavior.md)

---

## Overview

The **AI System** manages all non-player enemies including behavior trees, perception systems, navigation, and combat logic. Designed for mobile performance with scalable complexity.

**Responsibilities:**
- Enemy spawning and lifecycle management
- Behavior tree execution and state management
- Perception (vision, hearing) processing
- Pathfinding and navigation
- Combat decision making
- Boss fight phases and mechanics

---

## Enums & Types

### AIType
Enemy type classification determining base stats, behavior, and threat level.

| Code Name          | Display Name | Tier | HP   | Armor | Primary Weapon | Description                      |
| :----------------- | :----------- | :--- | :--- | :---- | :------------- | :------------------------------- |
| `AIT_Scavenger`    | Scavenger    | 1    | 80   | 0     | Pistol         | Fodder, low threat, flees easily |
| `AIT_Looter`       | Looter       | 1    | 100  | 10    | SMG            | Fodder, uses basic cover         |
| `AIT_Guard`        | Guard        | 2    | 150  | 30    | AR             | Soldier, patrols in pairs        |
| `AIT_Sniper`       | Sniper       | 2    | 100  | 20    | Sniper         | Soldier, long range overwatch    |
| `AIT_Heavy`        | Heavy        | 3    | 300  | 80    | LMG            | Elite, high HP/armor             |
| `AIT_Operative`    | Operative    | 3    | 200  | 50    | AR+Nade        | Elite, tactical flanking         |
| `AIT_BossWarden`   | Warden       | 4    | 5000 | 200   | Special        | Boss, Map 1, 4 phases            |
| `AIT_BossDirector` | Director     | 4    | 8000 | 300   | Special        | Boss, Map 2, 5 phases            |

---

### AIState
Current behavioral state of an AI entity.

| Code Name        | Display Name | Alert Level | Description                      |
| :--------------- | :----------- | :---------- | :------------------------------- |
| `AIS_Unaware`    | Unaware      | 0%          | Patrol mode, not alerted         |
| `AIS_Suspicious` | Suspicious   | 25%         | Noticed something, investigating |
| `AIS_Alert`      | Alert        | 50%         | Heard/saw something, searching   |
| `AIS_Engaged`    | Engaged      | 100%        | In combat, actively fighting     |
| `AIS_Fleeing`    | Fleeing      | 75%         | Retreating due to low HP         |
| `AIS_Dead`       | Dead         | 0%          | Corpse state, lootable           |

---

### AIBehavior
Tactical behavior patterns for AI decision making.

| Code Name          | Display Name    | Category | Description          |
| :----------------- | :-------------- | :------- | :------------------- |
| `AIB_PatrolPoint`  | Patrol (Point)  | Patrol   | Stationary guard     |
| `AIB_PatrolPath`   | Patrol (Path)   | Patrol   | Follow waypoints     |
| `AIB_PatrolRandom` | Patrol (Random) | Patrol   | Wander in area       |
| `AIB_PatrolPair`   | Patrol (Pair)   | Patrol   | Coordinated patrol   |
| `AIB_Search`       | Search          | Alert    | Looking for player   |
| `AIB_AttackDirect` | Attack (Direct) | Combat   | Rush target          |
| `AIB_AttackCover`  | Attack (Cover)  | Combat   | Use cover, peek-fire |
| `AIB_AttackFlank`  | Attack (Flank)  | Combat   | Flanking maneuver    |
| `AIB_Retreat`      | Retreat         | Combat   | Fall back            |
| `AIB_Suppress`     | Suppress        | Combat   | Suppressive fire     |

---

### AIAggression
Aggression level affecting combat behavior.

| Code Name        | Display Name | Retreat HP | Cover Use | Rush Distance |
| :--------------- | :----------- | :--------- | :-------- | :------------ |
| `AIA_Coward`     | Coward       | 40%        | 90%       | Never         |
| `AIA_Cautious`   | Cautious     | 25%        | 80%       | Never         |
| `AIA_Normal`     | Normal       | 15%        | 60%       | 10m           |
| `AIA_Aggressive` | Aggressive   | 10%        | 30%       | 20m           |
| `AIA_Berserker`  | Berserker    | Never      | 0%        | 50m           |

---

### AIAccuracy
Shooting accuracy affecting hit chance.

| Code Name           | Display Name  | Base Hit% | Headshot% | Description     |
| :------------------ | :------------ | :-------- | :-------- | :-------------- |
| `AIAC_Poor`         | Poor          | 15%       | 0%        | Tier 1 enemies  |
| `AIAC_BelowAverage` | Below Average | 25%       | 5%        | Most Tier 1     |
| `AIAC_Average`      | Average       | 40%       | 10%       | Tier 2 common   |
| `AIAC_AboveAverage` | Above Average | 55%       | 15%       | Tier 2 elite    |
| `AIAC_Marksman`     | Marksman      | 70%       | 25%       | Snipers, Tier 3 |

---

### DetectionSource
Source of player detection for AI perception.

| Code Name             | Display Name        | Alert Level | Range     | Description           |
| :-------------------- | :------------------ | :---------- | :-------- | :-------------------- |
| `DS_VisionDirect`     | Vision (Direct)     | 100%        | Varies    | Center of vision cone |
| `DS_VisionPeripheral` | Vision (Peripheral) | 50%         | Varies    | Edge of vision cone   |
| `DS_SoundFootstep`    | Sound (Footstep)    | 30%         | 10-20m    | Player footsteps      |
| `DS_SoundGunfire`     | Sound (Gunfire)     | 100%        | 50-80m    | Player shooting       |
| `DS_SoundExplosion`   | Sound (Explosion)   | 100%        | 80-100m   | Explosions            |
| `DS_AlertAlly`        | Alert (Ally)        | 80%         | Unlimited | Another AI alerted    |
| `DS_DamageTaken`      | Damage Taken        | 100%        | N/A       | AI took damage        |

---

### AITier
Enemy tier classification for difficulty scaling.

| Code Name  | Display Name | XP Reward | Loot Quality | Spawn Weight |
| :--------- | :----------- | :-------- | :----------- | :----------- |
| `AITIER_1` | Fodder       | 25        | Common       | 60%          |
| `AITIER_2` | Soldier      | 75        | Uncommon     | 30%          |
| `AITIER_3` | Elite        | 200       | Rare         | 10%          |
| `AITIER_4` | Boss         | 1000      | Epic+        | Event        |

---

### BossPhase
Boss fight phase for multi-phase encounters.

| Code Name       | Display Name | HP Threshold | Description                  |
| :-------------- | :----------- | :----------- | :--------------------------- |
| `BP_Phase1`     | Phase 1      | 100-75%      | Initial phase, basic attacks |
| `BP_Phase2`     | Phase 2      | 75-50%       | Adds minions, new attacks    |
| `BP_Phase3`     | Phase 3      | 50-25%       | Enraged, faster attacks      |
| `BP_Phase4`     | Phase 4      | 25-0%        | Desperation, all mechanics   |
| `BP_Transition` | Transition   | N/A          | Invulnerable during change   |

---

## Code Names

### AI Type Identifiers

| Code Name          | Type      | Tier | Notes              |
| :----------------- | :-------- | :--- | :----------------- |
| `AI_T1_SCAVENGER`  | Scavenger | 1    | Basic fodder       |
| `AI_T1_LOOTER`     | Looter    | 1    | Cover-using fodder |
| `AI_T2_GUARD`      | Guard     | 2    | Patrol soldier     |
| `AI_T2_SNIPER`     | Sniper    | 2    | Long-range         |
| `AI_T3_HEAVY`      | Heavy     | 3    | Tank enemy         |
| `AI_T3_OPERATIVE`  | Operative | 3    | Tactical flanker   |
| `AI_BOSS_WARDEN`   | Warden    | 4    | Map 1 Boss         |
| `AI_BOSS_DIRECTOR` | Director  | 4    | Map 2 Boss         |

### Perception Config Identifiers

| Code Name        | Vision Range | Sound Range | FOV  | Description        |
| :--------------- | :----------- | :---------- | :--- | :----------------- |
| `PERC_SCAVENGER` | 15m          | 10m         | 90°  | Poor awareness     |
| `PERC_LOOTER`    | 20m          | 15m         | 100° | Basic awareness    |
| `PERC_GUARD`     | 30m          | 20m         | 110° | Trained soldier    |
| `PERC_SNIPER`    | 60m          | 25m         | 60°  | Long-range focused |
| `PERC_HEAVY`     | 25m          | 30m         | 120° | Wide awareness     |
| `PERC_OPERATIVE` | 40m          | 35m         | 120° | Elite perception   |
| `PERC_BOSS`      | 50m          | 50m         | 180° | Near-omniscient    |

### Event Code Names

| Code Name               | Trigger          | Description             |
| :---------------------- | :--------------- | :---------------------- |
| `AI_SPAWNED`            | AI created       | New AI spawned in world |
| `AI_DIED`               | HP <= 0          | AI killed               |
| `AI_STATE_CHANGED`      | State transition | AI state changed        |
| `AI_ALERTED`            | Detection        | AI detected player      |
| `AI_ENGAGED`            | Combat start     | AI entered combat       |
| `AI_RETREATING`         | Low HP           | AI starts retreating    |
| `AI_LOST_TARGET`        | Search timeout   | AI lost sight of player |
| `AI_BOSS_PHASE_CHANGED` | HP threshold     | Boss entered new phase  |

---

## Architecture

### Class Diagram

```
                    ┌─────────────────┐
                    │   AIManager     │
                    │ (Singleton)     │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐   ┌───────▼───────┐   ┌───────▼───────┐
│ AISpawner     │   │ AIPoolManager │   │ AIPathfinder  │
│               │   │               │   │               │
└───────────────┘   └───────────────┘   └───────────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────▼────────┐
                    │ AICharacter     │
                    │ (Entity)        │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐   ┌───────▼───────┐   ┌───────▼───────┐
│ PerceptionComp│   │ BehaviorTree  │   │ CombatComp    │
│               │   │               │   │               │
└───────────────┘   └───────────────┘   └───────────────┘
```

---

## Core Classes

### AIManager

**Purpose:** Main system controller for all AI entities.

```
CLASS AIManager:
    STATIC instance: AIManager
    
    // AI Lifecycle
    activeAI: List<AICharacter>
    maxActiveAI: Integer = 30
    aiTickRate: Float = 0.1  // 10 Hz
    
    // Sub-managers
    poolManager: AIPoolManager
    spawner: AISpawner
    pathfinder: AIPathfinder
    
    FUNCTION SpawnAI(type: AIType, location: Vector3, rotation: Rotator) -> AICharacter:
        IF activeAI.Count >= maxActiveAI:
            EMIT EVENT "AI_POOL_EXHAUSTED"
            RETURN null
        END IF
        
        // Get from pool or spawn new
        ai = poolManager.AcquireAI(type)
        
        IF ai == null:
            ai = CreateNewAI(type)
        END IF
        
        ai.SetPosition(location)
        ai.SetRotation(rotation)
        ai.Initialize()
        
        activeAI.Add(ai)
        
        EMIT EVENT "AI_SPAWNED" WITH (ai.ID, type, location)
        
        RETURN ai
    END FUNCTION
    
    FUNCTION DespawnAI(ai: AICharacter):
        ai.Cleanup()
        activeAI.Remove(ai)
        poolManager.ReleaseAI(ai)
    END FUNCTION
    
    FUNCTION GetAIInRadius(center: Vector3, radius: Float) -> List<AICharacter>:
        result = NEW List<AICharacter>
        
        FOR EACH ai IN activeAI:
            IF Distance(ai.Position, center) <= radius:
                result.Add(ai)
            END IF
        END FOR
        
        RETURN result
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        // Staggered updates for performance
        FOR EACH ai IN activeAI:
            ai.tickTimer += deltaTime
            
            IF ai.tickTimer >= GetTickRate(ai):
                ai.UpdateAI(ai.tickTimer)
                ai.tickTimer = 0
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION GetTickRate(ai: AICharacter) -> Float:
        distanceToPlayer = Distance(ai.Position, GetPlayerPosition())
        
        IF distanceToPlayer < 20.0:
            RETURN 0.05   // 20 Hz - near player
        ELSE IF distanceToPlayer < 50.0:
            RETURN 0.1    // 10 Hz - mid range
        ELSE IF ai.IsOnScreen():
            RETURN 0.2    // 5 Hz - far but visible
        ELSE:
            RETURN 0.5    // 2 Hz - offscreen
        END IF
    END FUNCTION
```

---

### AICharacter

**Purpose:** Base AI entity with stats and components.

```
CLASS AICharacter:
    // Identity
    id: String
    aiType: AIType
    currentState: AIState = AIS_Unaware
    
    // Stats
    maxHealth: Float = 100.0
    currentHealth: Float
    maxArmor: Float = 0.0
    currentArmor: Float
    moveSpeed: Float = 350.0
    sprintSpeed: Float = 500.0
    damagePerHit: Float = 20.0
    
    // Behavior
    aggression: AIAggression = AIA_Normal
    accuracy: AIAccuracy = AIAC_Average
    fleeHealthPercent: Float = 0.2
    
    // Components
    perceptionComp: AIPerceptionComponent
    combatComp: AICombatComponent
    behaviorTree: BehaviorTree
    
    // Target
    currentTarget: Actor
    lastKnownTargetPos: Vector3
    
    FUNCTION Initialize():
        currentHealth = maxHealth
        currentArmor = maxArmor
        
        perceptionComp = CreateComponent(AIPerceptionComponent)
        combatComp = CreateComponent(AICombatComponent)
        
        LoadBehaviorTree(GetBehaviorTreeForType(aiType))
        
        perceptionComp.OnTargetDetected.AddListener(OnTargetDetected)
        perceptionComp.OnTargetLost.AddListener(OnTargetLost)
    END FUNCTION
    
    FUNCTION SetState(newState: AIState):
        IF newState == currentState:
            RETURN
        END IF
        
        oldState = currentState
        currentState = newState
        
        OnStateChanged(oldState, newState)
        
        EMIT EVENT "AI_STATE_CHANGED" WITH (id, oldState, newState)
    END FUNCTION
    
    FUNCTION OnTargetDetected(target: Actor, source: DetectionSource):
        currentTarget = target
        lastKnownTargetPos = target.Position
        
        IF source == DS_VisionDirect OR source == DS_DamageTaken:
            SetState(AIS_Engaged)
            EMIT EVENT "AI_ENGAGED" WITH (id, target.ID)
        ELSE:
            SetState(AIS_Alert)
            EMIT EVENT "AI_ALERTED" WITH (id, source)
        END IF
        
        // Alert nearby AI
        AlertNearbyAI(10.0)
    END FUNCTION
    
    FUNCTION OnTargetLost():
        lastKnownTargetPos = currentTarget.Position
        currentTarget = null
        
        SetState(AIS_Alert)
        
        EMIT EVENT "AI_LOST_TARGET" WITH (id)
    END FUNCTION
    
    FUNCTION TakeDamage(amount: Float, source: Actor):
        // Armor absorbs first
        IF currentArmor > 0:
            armorDamage = Min(amount * 0.8, currentArmor)
            currentArmor -= armorDamage
            amount -= armorDamage
        END IF
        
        currentHealth -= amount
        
        // Auto-detect attacker
        IF currentTarget == null:
            OnTargetDetected(source, DS_DamageTaken)
        END IF
        
        // Check flee threshold
        IF GetHealthPercent() <= fleeHealthPercent AND CanFlee():
            SetState(AIS_Fleeing)
            EMIT EVENT "AI_RETREATING" WITH (id)
        END IF
        
        // Check death
        IF currentHealth <= 0:
            Die(source)
        END IF
    END FUNCTION
    
    FUNCTION Die(killer: Actor):
        SetState(AIS_Dead)
        
        // Drop loot
        SpawnLoot()
        
        EMIT EVENT "AI_DIED" WITH (id, killer.ID, aiType)
    END FUNCTION
    
    FUNCTION GetHealthPercent() -> Float:
        RETURN currentHealth / maxHealth
    END FUNCTION
    
    FUNCTION AlertNearbyAI(radius: Float):
        nearbyAI = AIManager.GetAIInRadius(Position, radius * 100)  // Convert to cm
        
        FOR EACH ai IN nearbyAI:
            IF ai != self AND ai.currentState == AIS_Unaware:
                ai.OnTargetDetected(currentTarget, DS_AlertAlly)
            END IF
        END FOR
    END FUNCTION
```

---

### AIPerceptionComponent

**Purpose:** Vision and hearing perception for AI.

```
CLASS AIPerceptionComponent:
    // Vision config
    visionRange: Float = 30.0       // meters
    directAngle: Float = 30.0       // degrees
    peripheralAngle: Float = 60.0   // degrees
    
    // Hearing config
    hearingRange: Float = 20.0      // meters
    
    // Detection
    detectionProgress: Float = 0.0
    detectionThreshold: Float = 1.0
    
    // Events
    OnTargetDetected: Event<(Actor, DetectionSource)>
    OnTargetLost: Event<()>
    
    FUNCTION UpdatePerception(deltaTime: Float):
        // Check for visible targets
        FOR EACH target IN GetPotentialTargets():
            IF CanSee(target):
                ProcessVisionDetection(target, deltaTime)
            ELSE IF CanHear(target):
                ProcessAudioDetection(target)
            END IF
        END FOR
        
        // Decay detection if no stimulus
        IF NOT HasActiveStimulus():
            detectionProgress = Max(0, detectionProgress - deltaTime * 0.5)
        END IF
    END FUNCTION
    
    FUNCTION CanSee(target: Actor) -> Boolean:
        toTarget = target.Position - owner.Position
        distance = toTarget.Length()
        
        IF distance > visionRange:
            RETURN false
        END IF
        
        // Check angle
        angle = AngleBetween(owner.Forward, toTarget.Normalized())
        
        IF angle > peripheralAngle:
            RETURN false
        END IF
        
        // Line of sight check
        IF NOT HasLineOfSight(owner.EyePosition, target.Position):
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    FUNCTION ProcessVisionDetection(target: Actor, deltaTime: Float):
        toTarget = target.Position - owner.Position
        angle = AngleBetween(owner.Forward, toTarget.Normalized())
        
        // Calculate detection speed
        IF angle <= directAngle:
            detectionSpeed = 1.0  // Instant for direct vision
        ELSE:
            detectionSpeed = 0.3  // Slow for peripheral
        END IF
        
        // Apply visibility modifiers
        detectionSpeed *= GetVisibilityModifier(target)
        
        detectionProgress += detectionSpeed * deltaTime
        
        IF detectionProgress >= detectionThreshold:
            OnTargetDetected.Broadcast(target, DS_VisionDirect)
        END IF
    END FUNCTION
    
    FUNCTION GetVisibilityModifier(target: Actor) -> Float:
        modifier = 1.0
        
        IF target.IsCrouching():
            modifier *= 0.7
        ELSE IF target.IsProne():
            modifier *= 0.4
        END IF
        
        IF target.IsSprinting():
            modifier *= 2.0
        ELSE IF target.IsMoving():
            modifier *= 1.5
        END IF
        
        IF target.IsFiring():
            RETURN 999.0  // Instant detection
        END IF
        
        RETURN modifier
    END FUNCTION
    
    FUNCTION CanHear(target: Actor) -> Boolean:
        distance = Distance(owner.Position, target.Position)
        
        IF distance > hearingRange:
            RETURN false
        END IF
        
        RETURN target.IsProducingSound()
    END FUNCTION
```

---

### AICombatComponent

**Purpose:** Combat logic for AI entities.

```
CLASS AICombatComponent:
    // Weapon stats
    fireRate: Float = 0.15      // seconds between shots
    accuracySpread: Float = 5.0 // degrees
    reloadTime: Float = 2.0
    magazineSize: Integer = 30
    currentAmmo: Integer
    
    // Grenades
    grenadesRemaining: Integer = 1
    grenadeCooldown: Float = 10.0
    lastGrenadeTime: Float
    
    // State
    isFiring: Boolean = false
    isReloading: Boolean = false
    lastFireTime: Float
    
    FUNCTION StartFiring():
        IF NOT CanAttack():
            RETURN
        END IF
        
        isFiring = true
    END FUNCTION
    
    FUNCTION StopFiring():
        isFiring = false
    END FUNCTION
    
    FUNCTION UpdateCombat(deltaTime: Float):
        IF isFiring AND CanAttack():
            timeSinceLastFire = GetTime() - lastFireTime
            
            IF timeSinceLastFire >= fireRate:
                FireWeapon()
                lastFireTime = GetTime()
            END IF
        END IF
    END FUNCTION
    
    FUNCTION CanAttack() -> Boolean:
        IF isReloading:
            RETURN false
        END IF
        
        IF currentAmmo <= 0:
            StartReload()
            RETURN false
        END IF
        
        IF owner.currentTarget == null:
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    FUNCTION FireWeapon():
        target = owner.currentTarget
        
        IF target == null:
            RETURN
        END IF
        
        // Calculate aim with spread
        aimDir = (target.Position - owner.Position).Normalized()
        aimDir = ApplySpread(aimDir, accuracySpread)
        
        // Check hit based on accuracy
        hitChance = GetHitChance(target)
        
        IF Random() < hitChance:
            target.TakeDamage(owner.damagePerHit, owner)
        END IF
        
        currentAmmo -= 1
        
        // Alert nearby players
        EmitSoundEvent(DS_SoundGunfire, 80.0)
    END FUNCTION
    
    FUNCTION GetHitChance(target: Actor) -> Float:
        baseChance = GetBaseHitChance(owner.accuracy)
        distance = Distance(owner.Position, target.Position)
        
        // Distance falloff
        IF distance > 30.0:
            baseChance *= 0.7
        ELSE IF distance > 50.0:
            baseChance *= 0.4
        END IF
        
        // Target movement penalty
        IF target.IsMoving():
            baseChance *= 0.8
        END IF
        
        IF target.IsSprinting():
            baseChance *= 0.6
        END IF
        
        RETURN Clamp(baseChance, 0.05, 0.95)
    END FUNCTION
    
    FUNCTION CanThrowGrenade() -> Boolean:
        IF grenadesRemaining <= 0:
            RETURN false
        END IF
        
        timeSinceGrenade = GetTime() - lastGrenadeTime
        
        IF timeSinceGrenade < grenadeCooldown:
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    FUNCTION ThrowGrenade(targetLocation: Vector3):
        IF NOT CanThrowGrenade():
            RETURN
        END IF
        
        SpawnGrenade(owner.Position, targetLocation)
        grenadesRemaining -= 1
        lastGrenadeTime = GetTime()
    END FUNCTION
    
    FUNCTION FindBestCover() -> Vector3:
        threat = owner.currentTarget
        
        IF threat == null:
            RETURN owner.Position
        END IF
        
        // Find cover points within 15m
        coverPoints = GetCoverPointsInRadius(owner.Position, 15.0)
        
        bestCover = null
        bestScore = -999
        
        FOR EACH cover IN coverPoints:
            // Score based on:
            // - Distance from threat
            // - Angle to threat (side cover better)
            // - Not visible from threat position
            
            score = 0
            
            distToThreat = Distance(cover.Position, threat.Position)
            score += distToThreat * 0.5
            
            IF NOT IsPositionVisible(cover.Position, threat.Position):
                score += 100
            END IF
            
            IF score > bestScore:
                bestScore = score
                bestCover = cover
            END IF
        END FOR
        
        RETURN bestCover?.Position OR owner.Position
    END FUNCTION
    
    FUNCTION CalculateFlankPath() -> Vector3:
        target = owner.currentTarget
        
        IF target == null:
            RETURN null
        END IF
        
        // Calculate perpendicular directions
        toTarget = (target.Position - owner.Position).Normalized()
        flankDir = CrossProduct(toTarget, Vector3.Up)
        
        // Try both flanking directions
        flankDistance = 15.0
        candidates = [
            target.Position + flankDir * flankDistance,
            target.Position - flankDir * flankDistance
        ]
        
        FOR EACH candidate IN candidates:
            IF PathExists(owner.Position, candidate):
                IF HasCoverNear(candidate):
                    IF NOT IsPositionVisible(candidate, target.Position):
                        RETURN candidate
                    END IF
                END IF
            END IF
        END FOR
        
        RETURN null
    END FUNCTION
```

---

## Behavior Trees

### State Transitions

```
┌──────────────────────────────────────────────────────────┐
│                    STATE MACHINE                         │
├──────────────────────────────────────────────────────────┤
│                                                          │
│   ┌─────────┐    Noise/Peripheral    ┌─────────┐        │
│   │ UNAWARE │ ─────────────────────▶ │  ALERT  │        │
│   │(Patrol) │ ◀───────────────────── │(Search) │        │
│   └────┬────┘    30s no contact      └────┬────┘        │
│        │                                   │             │
│        │ Direct Vision                     │ Found Target│
│        ▼                                   ▼             │
│   ┌─────────────────────────────────────────────┐       │
│   │              ENGAGED (Combat)               │       │
│   └──────────────────────┬──────────────────────┘       │
│                          │                               │
│        Lost LOS 10s      │        HP < FleeThreshold     │
│        ┌─────────────────┴─────────────────┐            │
│        ▼                                   ▼             │
│   ┌─────────┐                         ┌─────────┐       │
│   │  ALERT  │                         │ FLEEING │       │
│   │(Search) │                         │         │       │
│   └─────────┘                         └─────────┘       │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Behavior Tree Nodes

```
// Task Nodes
BTTask_Patrol           // Move along patrol path
BTTask_Search           // Investigate last known position
BTTask_TakeCover        // Find and move to cover
BTTask_ShootAtTarget    // Fire at current target
BTTask_Suppress         // Suppressive fire at position
BTTask_Flank            // Move to flanking position
BTTask_ThrowGrenade     // Throw grenade at target
BTTask_Retreat          // Move away from threat
BTTask_CallForBackup    // Alert nearby AI

// Decorator Nodes
BTDecorator_HasTarget           // Check if target exists
BTDecorator_HealthAbove         // Check HP threshold
BTDecorator_InRange             // Check distance to target
BTDecorator_HasLineOfSight      // Check LOS to target
BTDecorator_InCover             // Check if in cover
BTDecorator_CanFlank            // Check flank path exists

// Service Nodes
BTService_UpdateTarget          // Refresh target selection
BTService_UpdateCover           // Re-evaluate cover positions
BTService_CheckThreats          // Scan for new threats
```

---

## AI Type Configurations

### Tier 1: Scavenger

```
CONST ScavengerConfig:
    type: AIT_Scavenger
    health: 50.0
    armor: 0.0
    damagePerHit: 12.0
    moveSpeed: 300.0
    sprintSpeed: 500.0
    visionRange: 15.0
    hearingRange: 10.0
    aggression: AIA_Coward
    accuracy: AIAC_Poor
    fleeThreshold: 0.40
    canFlee: true
    weaponType: WT_Pistol
    lootTable: "LT_SCAVENGER"
```

### Tier 2: Guard

```
CONST GuardConfig:
    type: AIT_Guard
    health: 100.0
    armor: 50.0
    damagePerHit: 27.0
    moveSpeed: 400.0
    sprintSpeed: 600.0
    visionRange: 30.0
    hearingRange: 20.0
    aggression: AIA_Aggressive
    accuracy: AIAC_AboveAverage
    fleeThreshold: 0.0
    canFlee: false
    weaponType: WT_AssaultRifle
    lootTable: "LT_GUARD"
    patrolType: AIB_PatrolPair
    canThrowGrenades: true
    canFlank: true
```

### Tier 3: Heavy

```
CONST HeavyConfig:
    type: AIT_Heavy
    health: 200.0
    armor: 100.0
    damagePerHit: 37.0
    moveSpeed: 250.0          // Slow
    sprintSpeed: 0.0          // Cannot sprint
    visionRange: 25.0
    hearingRange: 30.0
    aggression: AIA_Berserker
    accuracy: AIAC_Average
    fleeThreshold: 0.0
    canFlee: false
    weaponType: WT_LMG
    lootTable: "LT_HEAVY"
    weakPointMultiplier: 2.0
    weakPointBone: "Backpack"
    turnRate: 90.0            // Slow turn
```

### Tier 4: Boss - The Warden

```
CONST WardenConfig:
    type: AIT_BossWarden
    health: 500.0
    armor: 200.0
    armorRegenRate: 5.0
    moveSpeed: 300.0
    chargeSpeed: 1000.0
    visionRange: 50.0
    aggression: AIA_Berserker
    accuracy: AIAC_AboveAverage
    lootTable: "LT_BOSS_WARDEN"
    phases: [
        { threshold: 0.75, behavior: "BT_BOSS_WARDEN_PHASE1" },  // Stalking
        { threshold: 0.50, behavior: "BT_BOSS_WARDEN_PHASE2" },  // Aggressive
        { threshold: 0.25, behavior: "BT_BOSS_WARDEN_PHASE3" },  // Berserk
        { threshold: 0.00, behavior: "BT_BOSS_WARDEN_PHASE4" }   // Desperation
    ]
```

---

## Performance Optimization

### AI LOD System

```
ENUM AILODLevel:
    LOD_Full        // Full behavior, animations, VFX
    LOD_Reduced     // Simplified behavior, basic animations
    LOD_Minimal     // State updates only
    LOD_Dormant     // Paused, only check activation

FUNCTION GetAILOD(ai: AICharacter) -> AILODLevel:
    distance = Distance(ai.Position, GetPlayerPosition())
    
    IF distance < 20.0:
        RETURN LOD_Full
    ELSE IF distance < 50.0:
        RETURN LOD_Reduced
    ELSE IF distance < 100.0:
        RETURN LOD_Minimal
    ELSE:
        RETURN LOD_Dormant
    END IF
END FUNCTION
```

### Object Pooling

```
CLASS AIPoolManager:
    pools: Map<AIType, List<AICharacter>>
    initialPoolSize: Integer = 10
    maxPoolSize: Integer = 50
    
    FUNCTION Initialize(type: AIType):
        pool = NEW List<AICharacter>
        
        FOR i = 0 TO initialPoolSize:
            ai = SpawnDeactivatedAI(type)
            pool.Add(ai)
        END FOR
        
        pools[type] = pool
    END FUNCTION
    
    FUNCTION AcquireAI(type: AIType) -> AICharacter:
        pool = pools[type]
        
        FOR EACH ai IN pool:
            IF NOT ai.IsActive:
                ai.SetActive(true)
                ai.ResetState()
                RETURN ai
            END IF
        END FOR
        
        // Pool exhausted - expand if possible
        IF pool.Count < maxPoolSize:
            ai = SpawnNewAI(type)
            pool.Add(ai)
            RETURN ai
        END IF
        
        RETURN null
    END FUNCTION
    
    FUNCTION ReleaseAI(ai: AICharacter):
        ai.SetActive(false)
        ai.ResetState()
    END FUNCTION
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] AIManager - Main AI system manager
- [ ] AICharacter - Base AI character class
- [ ] AIPerceptionComponent - Vision/hearing
- [ ] Basic behavior trees (Patrol, Engage)
- [ ] Scavenger, Looter, Guard implementations
- [ ] Pathfinding integration (NavMesh)

### MEDIUM Priority 🟡
- [ ] Cover system integration
- [ ] Flanking logic
- [ ] Suppression mechanics
- [ ] Heavy, Sniper, Operative types
- [ ] AI spawning system
- [ ] Object pooling

### LOW Priority 🟢
- [ ] Boss behavior trees (multi-phase)
- [ ] The Warden implementation
- [ ] The Director implementation
- [ ] AI voice callouts
- [ ] Reinforcement wave system

---

## Testing Checklist

- [ ] AI spawns correctly at designated points
- [ ] Perception detects players at correct ranges
- [ ] State transitions work as documented
- [ ] Behavior trees execute without errors
- [ ] Pathfinding works on all map areas
- [ ] Cover system evaluates positions correctly
- [ ] Combat damage matches specs
- [ ] Flanking paths are valid
- [ ] Boss phases transition correctly
- [ ] Performance within budget (30 AI at 30 FPS)
- [ ] Object pooling prevents GC spikes

---

**[← Back to Index](../README.md)** | **[Next: Map System →](./MapSystem.md)**


