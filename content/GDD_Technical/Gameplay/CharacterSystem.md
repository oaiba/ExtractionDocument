---
title: Character System - Technical Design Sutureument
type: docs
---

# Character System - Technical Design Sutureument

### Related Sutureuments

| Sutureument           | Relationship                | Link                                                                                                                                          |
| --------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Operators Design**  | High-level character design | [GDD\_HighLevel/Characters/Operators.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_HighLevel/Characters/Operators.md) |
| **Control System**    | Input handling              | [ControlSystem.md](ControlSystem.md)                                                                                                          |
| **Weapon System**     | Weapon integration          | [WeaponSystem.md](WeaponSystem.md)                                                                                                            |
| **Inventory System**  | Equipment & weight          | [InventorySystem.md](InventorySystem.md)                                                                                                      |
| **Networking System** | Character sync              | [../Core/NetworkingSystem.md](../Core/NetworkingSystem.md)                                                                                    |

***

### Overview

#### Purpose

The **Character System** manages all aspects of player-controlled characters including health, movement, abilities, and interactions.

#### Core Functions

| Function               | Description                                  |
| ---------------------- | -------------------------------------------- |
| **Character Spawning** | Instantiate and initialize player characters |
| **Health Management**  | Track HP, armor, damage, death               |
| **Movement**           | Handle walk, sprint, crouch, rotation        |
| **Operator Abilities** | Unique class-based abilities with cooldowns  |
| **Stamina System**     | Sprint resource management                   |
| **Interactions**       | World object interaction (loot, doors, etc.) |

#### Design Goals

```
1. RESPONSIVE - Movement feels tight and immediate
2. BALANCED - Each operator class has clear strengths/weaknesses
3. SYNCHRONIZED - Consistent state across network
4. MODULAR - Components can be modified independently
5. EXTENSIBLE - Easy to add new operators/abilities
```

***

### System Architecture

#### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CHARACTER SYSTEM                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │  CHARACTER   │    │   HEALTH     │    │  MOVEMENT    │          │
│  │  MANAGER     │───▶│   SYSTEM     │───▶│  SYSTEM      │          │
│  │              │    │              │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ Spawning     │    │ Damage Calc  │    │ State Machine│          │
│  │ Operator Data│    │ Armor System │    │ Speed Mods   │          │
│  │ Database     │    │ Death/Revive │    │ Rotation     │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │  ABILITY     │    │  STAMINA     │    │ INTERACTION  │          │
│  │  SYSTEM      │    │  SYSTEM      │    │ SYSTEM       │          │
│  │              │    │              │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### Core Components

| Component                | Responsibility                        | Dependencies      |
| ------------------------ | ------------------------------------- | ----------------- |
| **CharacterManager**     | Spawning, pooling, operator selection | Database          |
| **HealthComponent**      | HP, armor, damage, death              | None              |
| **MovementComponent**    | Walk, sprint, crouch, rotation        | StaminaComponent  |
| **AbilityComponent**     | Operator abilities, cooldowns         | CharacterManager  |
| **StaminaComponent**     | Sprint resource                       | MovementComponent |
| **InteractionComponent** | World interactions                    | UI System         |

***

### Enums & Types

#### EOperatorClass

Operator class/role classification.

| Code Name       | Display Name | Playstyle    | Ability Type | Base HP | Speed Bonus | Description            |
| --------------- | ------------ | ------------ | ------------ | ------- | ----------- | ---------------------- |
| `OC_None`       | None         | N/A          | N/A          | 100     | 0%          | Unassigned operator    |
| `OC_Assault`    | Assault      | Aggressive   | Damage Buff  | 100     | +5%         | Aggressive fragger     |
| `OC_Support`    | Support      | Team-focused | Healing      | 100     | 0%          | Team medic             |
| `OC_Recon`      | Recon        | Information  | Reveal       | 90      | +10%        | Information specialist |
| `OC_Tank`       | Tank         | Defensive    | Shield       | 120     | -5%         | Damage sponge          |
| `OC_Specialist` | Specialist   | Tech         | Disable      | 100     | 0%          | Tech expert            |

***

#### EMovementState

Character movement state machine.

| Code Name      | Display Name | Speed Mult | Stamina Drain | Noise Level | Description        |
| -------------- | ------------ | ---------- | ------------- | ----------- | ------------------ |
| `MS_Idle`      | Idle         | 0×         | 0/s           | Silent      | Standing still     |
| `MS_Walking`   | Walking      | 1×         | 0/s           | Low         | Normal movement    |
| `MS_Sprinting` | Sprinting    | 1.5×       | 10/s          | High        | Fast movement      |
| `MS_Crouching` | Crouching    | 0.6×       | 0/s           | Very Low    | Sneaking           |
| `MS_Sliding`   | Sliding      | 1.8×       | 15 burst      | Medium      | Quick slide        |
| `MS_Dead`      | Dead         | 0×         | 0/s           | None        | Character deceased |

***

#### EAbilityState

Operator ability state.

| Code Name     | Display Name | Can Activate | UI Display | Description              |
| ------------- | ------------ | ------------ | ---------- | ------------------------ |
| `AS_Ready`    | Ready        | Yes          | Full icon  | Can be activated         |
| `AS_Active`   | Active       | No           | Glowing    | Currently active         |
| `AS_Cooldown` | Cooldown     | No           | Timer      | On cooldown              |
| `AS_Disabled` | Disabled     | No           | Grayed out | Cannot use (EMP'd, etc.) |

***

#### EInteractionType

Interactable object type.

| Code Name             | Display Name     | Hold Time | Range | Priority | Description        |
| --------------------- | ---------------- | --------- | ----- | -------- | ------------------ |
| `INT_None`            | None             | N/A       | N/A   | 0        | No interaction     |
| `INT_LootContainer`   | Loot Container   | 0.5s      | 2m    | 3        | Open loot box      |
| `INT_Door`            | Door             | 0s        | 1.5m  | 2        | Open/close door    |
| `INT_ExtractionPoint` | Extraction Point | 3s        | 5m    | 1        | Begin extraction   |
| `INT_DeadBody`        | Dead Body        | 1s        | 2m    | 4        | Loot corpse        |
| `INT_QuestItem`       | Quest Item       | 0.3s      | 2m    | 5        | Pick up quest item |
| `INT_Vendor`          | Vendor           | 0s        | 3m    | 6        | Open shop UI       |

***

#### ECharacterState

Character life state.

| Code Name       | Display Name | Can Move | Can Shoot    | Revivable | Description        |
| --------------- | ------------ | -------- | ------------ | --------- | ------------------ |
| `CS_Alive`      | Alive        | Yes      | Yes          | N/A       | Normal state       |
| `CS_Downed`     | Downed       | No       | Sidearm only | Yes       | Can be revived     |
| `CS_Dead`       | Dead         | No       | No           | No        | Fully deceased     |
| `CS_Extracting` | Extracting   | Limited  | Yes          | N/A       | In extraction zone |

***

#### EAnimationState

Character animation state.

| Code Name         | Display Name | Priority | Blend Time | Interruptible | Description        |
| ----------------- | ------------ | -------- | ---------- | ------------- | ------------------ |
| `ANIM_Idle`       | Idle         | 0        | 0.2s       | Yes           | Standing animation |
| `ANIM_Walk`       | Walk         | 1        | 0.15s      | Yes           | Walking loop       |
| `ANIM_Run`        | Run          | 2        | 0.15s      | Yes           | Running loop       |
| `ANIM_Crouch`     | Crouch       | 1        | 0.2s       | Yes           | Crouching          |
| `ANIM_Shoot`      | Shoot        | 5        | 0.05s      | No            | Firing weapon      |
| `ANIM_Reload`     | Reload       | 4        | 0.1s       | Yes           | Reloading          |
| `ANIM_UseAbility` | Use Ability  | 6        | 0.1s       | No            | Ability activation |
| `ANIM_Death`      | Death        | 10       | 0s         | No            | Death animation    |

***

### Code Names

#### Operator Events

| Code Name     | Trigger           | Parameters                           | Description                   |
| ------------- | ----------------- | ------------------------------------ | ----------------------------- |
| `CHAR_SPAWN`  | Character spawned | PlayerID, OperatorClass, SpawnPoint  | Character entered match       |
| `CHAR_DEATH`  | Character died    | VictimID, KillerID, WeaponID, Damage | Character killed              |
| `CHAR_DOWNED` | Character downed  | VictimID, AttackerID                 | Character downed (revivable)  |
| `CHAR_REVIVE` | Character revived | VictimID, ReviverID                  | Character revived by teammate |

#### Movement Events

| Code Name               | Trigger       | Parameters             | Description               |
| ----------------------- | ------------- | ---------------------- | ------------------------- |
| `MOVE_STATE_CHANGE`     | State changed | OldState, NewState     | Movement state transition |
| `MOVE_SPRINT_START`     | Sprint begins | StaminaCurrent         | Started sprinting         |
| `MOVE_SPRINT_END`       | Sprint ends   | StaminaCurrent, Reason | Stopped sprinting         |
| `MOVE_STAMINA_DEPLETED` | Stamina empty | -                      | Stamina reached zero      |

#### Health Events

| Code Name            | Trigger            | Parameters                 | Description            |
| -------------------- | ------------------ | -------------------------- | ---------------------- |
| `HEALTH_DAMAGE`      | Damage received    | Amount, Source, DamageType | Health reduced         |
| `HEALTH_HEAL`        | Health restored    | Amount, Source             | Health increased       |
| `HEALTH_ARMOR_BREAK` | Armor destroyed    | -                          | Armor reached zero     |
| `HEALTH_LOW`         | Low health warning | CurrentHP, Threshold       | Health below threshold |

#### Ability Events

| Code Name                | Trigger         | Parameters           | Description            |
| ------------------------ | --------------- | -------------------- | ---------------------- |
| `ABILITY_ACTIVATE`       | Ability used    | AbilityID, TargetPos | Ability activated      |
| `ABILITY_END`            | Ability ends    | AbilityID, Duration  | Ability effect ended   |
| `ABILITY_COOLDOWN_START` | Cooldown begins | AbilityID, Duration  | Cooldown timer started |
| `ABILITY_READY`          | Ability ready   | AbilityID            | Cooldown complete      |

#### Interaction Events

| Code Name            | Trigger               | Parameters                | Description             |
| -------------------- | --------------------- | ------------------------- | ----------------------- |
| `INTERACT_START`     | Interaction begins    | TargetID, InteractionType | Started interacting     |
| `INTERACT_COMPLETE`  | Interaction done      | TargetID, InteractionType | Interaction finished    |
| `INTERACT_CANCEL`    | Interaction cancelled | TargetID, Reason          | Interaction interrupted |
| `INTERACT_AVAILABLE` | Target found          | TargetID, InteractionType | Interactable in range   |

***

### Data Structures

#### CharacterStats

**Purpose:** Runtime stats for a character instance.

```
STRUCT CharacterStats:
    // Health
    MaxHealth: Float = 100          // Base maximum HP
    CurrentHealth: Float            // Current HP
    
    // Armor
    MaxArmor: Float = 0             // Based on equipped armor
    CurrentArmor: Float             // Current armor value
    ArmorAbsorption: Float = 0.7    // 70% damage absorbed by armor
    
    // Movement
    BaseMovementSpeed: Float = 5.0  // Base speed in m/s
    SprintMultiplier: Float = 1.5   // Sprint speed multiplier
    CrouchMultiplier: Float = 0.6   // Crouch speed multiplier
    
    // Stamina
    MaxStamina: Float = 100         // Maximum stamina
    CurrentStamina: Float           // Current stamina
    StaminaDrainRate: Float = 10.0  // Per second while sprinting
    StaminaRegenRate: Float = 15.0  // Per second when not sprinting
    StaminaRegenDelay: Float = 1.0  // Seconds before regen starts
```

#### OperatorData

**Purpose:** Static definition of an operator class.

```
STRUCT OperatorData:
    // Identification
    CodeName: String                // e.g., "OPER_ASSAULT_MAMBA"
    DisplayName: String             // e.g., "MAMBA"
    Class: EOperatorClass           // Class category
    
    // Unique ability
    AbilityCodeName: String         // e.g., "ABILITY_ASSAULT_COMBATSTEM"
    AbilityCooldown: Float          // Seconds
    AbilityDuration: Float          // Seconds (0 = instant)
    
    // Passive bonuses
    MovementSpeedBonus: Float       // Multiplier (e.g., 1.1 = +10%)
    HealthBonus: Float              // Additive (e.g., +10 HP)
    ArmorBonus: Float               // Additive armor
    
    // Assets
    ModelPath: String               // 3D model path
    IconPath: String                // Portrait icon
    AbilityIconPath: String         // Ability icon
```

#### CharacterInstance

**Purpose:** Runtime instance of a player character.

```
CLASS CharacterInstance:
    // Unique identification
    InstanceID: String              // Player unique ID
    Operator: OperatorData          // Selected operator
    Stats: CharacterStats           // Current stats
    
    // State machines
    MovementState: EMovementState   // Current movement state
    CharacterState: ECharacterState // Alive/Downed/Dead
    AbilityState: EAbilityState     // Ability availability
    
    // Equipment references
    EquippedWeaponID: String        // Currently held weapon
    EquippedArmorID: String         // Worn armor
    EquippedBackpackID: String      // Current backpack
    
    // Runtime tracking
    AbilityCooldownRemaining: Float // Time until ability ready
    Position: Vector3               // World position
    Rotation: Quaternion            // World rotation
    LookDirection: Vector3          // Aim direction
    
    // Network
    OwnerPlayerID: String           // Owning player
    IsLocalPlayer: Boolean          // True if this is local client
    LastSyncTime: Float             // Last network update time
```

***

### Core Classes

#### CharacterManager

**Purpose:** Central manager for character spawning and operator data.

**Pseudocode:**

```
CLASS CharacterManager:
    
    // Singleton instance
    STATIC instance: CharacterManager
    
    // Operator database
    operatorDatabase: Map<EOperatorClass, OperatorData>
    
    // Active characters
    activeCharacters: List<CharacterInstance>
    characterPool: ObjectPool<CharacterInstance>
    
    // Initialize on game start
    FUNCTION Initialize():
        LoadOperatorDatabase()
        CreateCharacterPool(poolSize: 20)
    END FUNCTION
    
    // Load all operators from database
    FUNCTION LoadOperatorDatabase():
        FOR EACH operatorAsset IN Resources.Load("Operators"):
            data = ParseOperatorData(operatorAsset)
            operatorDatabase[data.Class] = data
        END FOR
        
        // Validate all classes have data
        FOR EACH class IN EOperatorClass.Values:
            IF class != OC_None AND NOT operatorDatabase.Contains(class):
                LOG ERROR "Missing operator data for: " + class
            END IF
        END FOR
    END FUNCTION
    
    // Spawn a character for a player
    FUNCTION SpawnCharacter(playerID: String, operatorClass: EOperatorClass, spawnPoint: Transform) -> CharacterInstance:
        // Get operator data
        operatorData = operatorDatabase[operatorClass]
        
        // Get character from pool
        character = characterPool.Get()
        
        // Initialize stats
        character.InstanceID = GenerateUUID()
        character.Operator = operatorData
        character.OwnerPlayerID = playerID
        
        // Apply operator bonuses
        character.Stats.MaxHealth = 100 + operatorData.HealthBonus
        character.Stats.CurrentHealth = character.Stats.MaxHealth
        character.Stats.BaseMovementSpeed *= operatorData.MovementSpeedBonus
        
        // Set position
        character.Position = spawnPoint.position
        character.Rotation = spawnPoint.rotation
        
        // Initialize states
        character.MovementState = MS_Idle
        character.CharacterState = CS_Alive
        character.AbilityState = AS_Ready
        
        // Add to active list
        activeCharacters.Add(character)
        
        // Network: Spawn on all clients
        NetworkManager.SpawnNetworkObject(character)
        
        EMIT EVENT "CHAR_SPAWN" WITH (playerID, operatorClass, spawnPoint)
        
        RETURN character
    END FUNCTION
    
    // Despawn a character
    FUNCTION DespawnCharacter(character: CharacterInstance):
        activeCharacters.Remove(character)
        NetworkManager.DespawnNetworkObject(character)
        characterPool.Return(character)
    END FUNCTION
    
    // Get character by player ID
    FUNCTION GetCharacterByPlayerID(playerID: String) -> CharacterInstance?:
        FOR EACH character IN activeCharacters:
            IF character.OwnerPlayerID == playerID:
                RETURN character
            END IF
        END FOR
        RETURN null
    END FUNCTION
```

***

#### HealthSystem

**Purpose:** Manage health, armor, damage, and death.

**Pseudocode:**

```
CLASS HealthSystem:
    
    // Reference to owning character
    character: CharacterInstance
    
    // Constants
    CONST HEADSHOT_MULTIPLIER = 2.0
    CONST LIMB_MULTIPLIER = 0.8
    CONST LOW_HEALTH_THRESHOLD = 25
    
    // Apply damage to character
    FUNCTION ApplyDamage(amount: Float, source: String, damageType: EDamageType, hitBone: String):
        IF character.CharacterState == CS_Dead:
            RETURN  // Can't damage dead characters
        END IF
        
        // Calculate final damage with modifiers
        finalDamage = CalculateDamage(amount, hitBone)
        
        // Process armor first
        armorDamage = 0
        healthDamage = finalDamage
        
        IF character.Stats.CurrentArmor > 0:
            // Armor absorbs percentage of damage
            absorbed = finalDamage * character.Stats.ArmorAbsorption
            armorDamage = Min(character.Stats.CurrentArmor, absorbed)
            healthDamage = finalDamage - armorDamage
            
            character.Stats.CurrentArmor -= armorDamage
            
            IF character.Stats.CurrentArmor <= 0:
                character.Stats.CurrentArmor = 0
                EMIT EVENT "HEALTH_ARMOR_BREAK"
            END IF
        END IF
        
        // Apply health damage
        character.Stats.CurrentHealth -= healthDamage
        
        EMIT EVENT "HEALTH_DAMAGE" WITH (healthDamage, source, damageType)
        
        // Check for low health warning
        IF character.Stats.CurrentHealth <= LOW_HEALTH_THRESHOLD:
            EMIT EVENT "HEALTH_LOW" WITH (character.Stats.CurrentHealth, LOW_HEALTH_THRESHOLD)
        END IF
        
        // Check for death
        IF character.Stats.CurrentHealth <= 0:
            HandleDeath(source)
        END IF
    END FUNCTION
    
    // Calculate damage with hit location modifiers
    FUNCTION CalculateDamage(baseDamage: Float, hitBone: String) -> Float:
        multiplier = 1.0
        
        SWITCH hitBone:
            CASE "Head":
                multiplier = HEADSHOT_MULTIPLIER
            CASE "Arm", "Hand", "Leg", "Foot":
                multiplier = LIMB_MULTIPLIER
            CASE "Chest", "Stomach":
                multiplier = 1.0
        END SWITCH
        
        RETURN baseDamage * multiplier
    END FUNCTION
    
    // Handle character death
    FUNCTION HandleDeath(killerID: String):
        character.Stats.CurrentHealth = 0
        character.CharacterState = CS_Dead
        character.MovementState = MS_Dead
        
        // Disable components
        DisableMovement()
        DisableInput()
        
        // Enable ragdoll physics
        EnableRagdoll()
        
        // Spawn loot bag with inventory contents
        SpawnLootBag()
        
        // Network broadcast
        EMIT EVENT "CHAR_DEATH" WITH (character.OwnerPlayerID, killerID)
        
        // Notify kill feed
        UISystem.ShowKillFeed(killerID, character.OwnerPlayerID)
    END FUNCTION
    
    // Heal character
    FUNCTION Heal(amount: Float, source: String):
        IF character.CharacterState != CS_Alive:
            RETURN
        END IF
        
        oldHealth = character.Stats.CurrentHealth
        character.Stats.CurrentHealth = Min(
            character.Stats.CurrentHealth + amount,
            character.Stats.MaxHealth
        )
        
        actualHealed = character.Stats.CurrentHealth - oldHealth
        
        EMIT EVENT "HEALTH_HEAL" WITH (actualHealed, source)
    END FUNCTION
    
    // Restore armor
    FUNCTION RepairArmor(amount: Float):
        character.Stats.CurrentArmor = Min(
            character.Stats.CurrentArmor + amount,
            character.Stats.MaxArmor
        )
    END FUNCTION
```

***

#### MovementSystem

**Purpose:** Handle character movement, states, and speed modifiers.

**Pseudocode:**

```
CLASS MovementSystem:
    
    // Reference to owning character
    character: CharacterInstance
    staminaSystem: StaminaSystem
    
    // Speed modifiers
    modifiers: Map<String, Float>
    
    // Process movement input each frame
    FUNCTION ProcessMovement(moveInput: Vector2, deltaTime: Float):
        IF character.CharacterState == CS_Dead:
            RETURN
        END IF
        
        // Calculate wish direction (camera-relative)
        wishDirection = ConvertToWorldSpace(moveInput)
        
        // Calculate final speed
        finalSpeed = CalculateFinalSpeed()
        
        // Apply movement
        velocity = wishDirection * finalSpeed
        character.Position += velocity * deltaTime
        
        // Update movement state
        UpdateMovementState(moveInput)
    END FUNCTION
    
    // Calculate final movement speed with all modifiers
    FUNCTION CalculateFinalSpeed() -> Float:
        baseSpeed = character.Stats.BaseMovementSpeed
        
        // Movement state multiplier
        stateMultiplier = GetStateSpeedMultiplier()
        
        // Combine all modifiers
        totalModifier = 1.0
        FOR EACH (name, value) IN modifiers:
            totalModifier *= value
        END FOR
        
        RETURN baseSpeed * stateMultiplier * totalModifier
    END FUNCTION
    
    // Get speed multiplier for current movement state
    FUNCTION GetStateSpeedMultiplier() -> Float:
        SWITCH character.MovementState:
            CASE MS_Idle:
                RETURN 0.0
            CASE MS_Walking:
                RETURN 1.0
            CASE MS_Sprinting:
                RETURN character.Stats.SprintMultiplier
            CASE MS_Crouching:
                RETURN character.Stats.CrouchMultiplier
            CASE MS_Sliding:
                RETURN 1.8
            CASE MS_Dead:
                RETURN 0.0
        END SWITCH
    END FUNCTION
    
    // Update movement state based on input
    FUNCTION UpdateMovementState(moveInput: Vector2):
        oldState = character.MovementState
        
        IF moveInput.Length() < 0.1:
            // No input = idle
            SetMovementState(MS_Idle)
        ELSE IF InputManager.IsHeld(IA_Sprint) AND staminaSystem.HasStamina():
            // Sprint requested and has stamina
            SetMovementState(MS_Sprinting)
        ELSE IF InputManager.IsHeld(IA_Crouch):
            // Crouch requested
            SetMovementState(MS_Crouching)
        ELSE:
            // Normal walking
            SetMovementState(MS_Walking)
        END IF
    END FUNCTION
    
    // Set movement state with events
    FUNCTION SetMovementState(newState: EMovementState):
        IF newState == character.MovementState:
            RETURN
        END IF
        
        oldState = character.MovementState
        character.MovementState = newState
        
        // Handle state transitions
        IF oldState == MS_Sprinting:
            EMIT EVENT "MOVE_SPRINT_END" WITH (staminaSystem.CurrentStamina, "State changed")
        END IF
        
        IF newState == MS_Sprinting:
            EMIT EVENT "MOVE_SPRINT_START" WITH (staminaSystem.CurrentStamina)
        END IF
        
        EMIT EVENT "MOVE_STATE_CHANGE" WITH (oldState, newState)
    END FUNCTION
    
    // Add a speed modifier
    FUNCTION AddModifier(name: String, multiplier: Float):
        modifiers[name] = multiplier
    END FUNCTION
    
    // Remove a speed modifier
    FUNCTION RemoveModifier(name: String):
        modifiers.Remove(name)
    END FUNCTION
    
    // Handle character rotation (top-down aiming)
    FUNCTION ProcessRotation(lookInput: Vector2):
        IF character.CharacterState == CS_Dead:
            RETURN
        END IF
        
        // Calculate look direction from input
        lookDirection = Vector3(lookInput.x, 0, lookInput.y).Normalized()
        
        IF lookDirection.Length() > 0.1:
            // Smoothly rotate toward look direction
            targetRotation = LookRotation(lookDirection)
            character.Rotation = SmoothDamp(
                character.Rotation,
                targetRotation,
                rotationSpeed: 10.0
            )
            character.LookDirection = lookDirection
        END IF
    END FUNCTION
```

***

#### StaminaSystem

**Purpose:** Manage stamina for sprinting.

**Pseudocode:**

```
CLASS StaminaSystem:
    
    // Reference to owning character
    character: CharacterInstance
    
    // State
    CurrentStamina: Float
    timeSinceStaminaUse: Float = 0
    
    // Update stamina each frame
    FUNCTION Update(deltaTime: Float):
        IF character.MovementState == MS_Sprinting:
            // Drain stamina while sprinting
            DrainStamina(character.Stats.StaminaDrainRate * deltaTime)
            timeSinceStaminaUse = 0
        ELSE:
            // Regenerate stamina when not sprinting
            timeSinceStaminaUse += deltaTime
            
            IF timeSinceStaminaUse >= character.Stats.StaminaRegenDelay:
                RegenerateStamina(character.Stats.StaminaRegenRate * deltaTime)
            END IF
        END IF
    END FUNCTION
    
    // Drain stamina
    FUNCTION DrainStamina(amount: Float):
        CurrentStamina = Max(0, CurrentStamina - amount)
        
        IF CurrentStamina <= 0:
            EMIT EVENT "MOVE_STAMINA_DEPLETED"
            // Force exit sprint state
            MovementSystem.SetMovementState(MS_Walking)
        END IF
    END FUNCTION
    
    // Regenerate stamina
    FUNCTION RegenerateStamina(amount: Float):
        CurrentStamina = Min(character.Stats.MaxStamina, CurrentStamina + amount)
    END FUNCTION
    
    // Check if has stamina to sprint
    FUNCTION HasStamina() -> Boolean:
        RETURN CurrentStamina > 0
    END FUNCTION
    
    // Get stamina percentage for UI
    FUNCTION GetStaminaPercent() -> Float:
        RETURN CurrentStamina / character.Stats.MaxStamina
    END FUNCTION
```

***

#### AbilitySystem

**Purpose:** Manage operator abilities and cooldowns.

**Pseudocode:**

```
CLASS AbilitySystem:
    
    // Reference to owning character
    character: CharacterInstance
    
    // Current ability data
    abilityData: OperatorAbilityData
    cooldownRemaining: Float = 0
    activeDuration: Float = 0
    
    // Initialize ability for operator
    FUNCTION Initialize(operator: OperatorData):
        abilityData = LoadAbilityData(operator.AbilityCodeName)
        character.AbilityState = AS_Ready
        cooldownRemaining = 0
    END FUNCTION
    
    // Try to activate ability
    FUNCTION TryActivate() -> Boolean:
        // Check if can activate
        IF NOT CanActivate():
            PlayErrorSound()
            RETURN false
        END IF
        
        // Activate ability
        character.AbilityState = AS_Active
        activeDuration = abilityData.Duration
        
        // Apply ability effect
        ApplyAbilityEffect()
        
        EMIT EVENT "ABILITY_ACTIVATE" WITH (abilityData.CodeName, character.Position)
        
        // If instant ability (duration = 0), go straight to cooldown
        IF abilityData.Duration <= 0:
            StartCooldown()
        END IF
        
        RETURN true
    END FUNCTION
    
    // Check if ability can be activated
    FUNCTION CanActivate() -> Boolean:
        IF character.AbilityState != AS_Ready:
            RETURN false
        END IF
        
        IF character.CharacterState != CS_Alive:
            RETURN false
        END IF
        
        // Check for disable effects (EMP, stun, etc.)
        IF HasStatusEffect("Disabled"):
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    // Update ability state each frame
    FUNCTION Update(deltaTime: Float):
        SWITCH character.AbilityState:
            CASE AS_Active:
                activeDuration -= deltaTime
                IF activeDuration <= 0:
                    EndAbility()
                ELSE:
                    UpdateAbilityEffect(deltaTime)
                END IF
                
            CASE AS_Cooldown:
                cooldownRemaining -= deltaTime
                IF cooldownRemaining <= 0:
                    cooldownRemaining = 0
                    character.AbilityState = AS_Ready
                    EMIT EVENT "ABILITY_READY" WITH (abilityData.CodeName)
                END IF
        END SWITCH
    END FUNCTION
    
    // End active ability
    FUNCTION EndAbility():
        RemoveAbilityEffect()
        character.AbilityState = AS_Cooldown
        
        EMIT EVENT "ABILITY_END" WITH (abilityData.CodeName, abilityData.Duration)
        
        StartCooldown()
    END FUNCTION
    
    // Start cooldown timer
    FUNCTION StartCooldown():
        cooldownRemaining = abilityData.Cooldown
        character.AbilityState = AS_Cooldown
        
        EMIT EVENT "ABILITY_COOLDOWN_START" WITH (abilityData.CodeName, abilityData.Cooldown)
    END FUNCTION
    
    // Get cooldown percentage for UI
    FUNCTION GetCooldownPercent() -> Float:
        IF character.AbilityState != AS_Cooldown:
            RETURN 0
        END IF
        RETURN cooldownRemaining / abilityData.Cooldown
    END FUNCTION
    
    // Disable ability (from EMP, etc.)
    FUNCTION DisableAbility(duration: Float):
        previousState = character.AbilityState
        character.AbilityState = AS_Disabled
        
        // Pause cooldown or end active effect
        IF previousState == AS_Active:
            EndAbility()
        END IF
        
        // Schedule re-enable
        ScheduleTask(duration, FUNCTION():
            IF character.AbilityState == AS_Disabled:
                character.AbilityState = AS_Ready
            END IF
        END FUNCTION)
    END FUNCTION
```

***

#### InteractionSystem

**Purpose:** Detect and execute world interactions.

**Pseudocode:**

```
CLASS InteractionSystem:
    
    // Reference to owning character
    character: CharacterInstance
    
    // Current interaction target
    currentTarget: IInteractable = null
    interactionProgress: Float = 0
    isInteracting: Boolean = false
    
    // Detection settings
    CONST DETECTION_RADIUS = 3.0
    CONST DETECTION_RATE = 0.1  // Seconds between detection checks
    
    // Scan for nearby interactables
    FUNCTION DetectInteractables():
        // Find all interactables in range
        colliders = Physics.OverlapSphere(character.Position, DETECTION_RADIUS, InteractableLayer)
        
        bestTarget = null
        bestPriority = -1
        bestDistance = DETECTION_RADIUS + 1
        
        FOR EACH collider IN colliders:
            interactable = collider.GetComponent<IInteractable>()
            IF interactable == null:
                CONTINUE
            END IF
            
            // Check if visible (not through walls)
            IF NOT IsVisible(interactable.Position):
                CONTINUE
            END IF
            
            // Check range for this interaction type
            distance = Distance(character.Position, interactable.Position)
            IF distance > interactable.InteractionRange:
                CONTINUE
            END IF
            
            // Select by priority, then distance
            IF interactable.Priority > bestPriority:
                bestTarget = interactable
                bestPriority = interactable.Priority
                bestDistance = distance
            ELSE IF interactable.Priority == bestPriority AND distance < bestDistance:
                bestTarget = interactable
                bestDistance = distance
            END IF
        END FOR
        
        // Update current target
        IF bestTarget != currentTarget:
            currentTarget = bestTarget
            IF currentTarget != null:
                EMIT EVENT "INTERACT_AVAILABLE" WITH (currentTarget.ID, currentTarget.Type)
                UISystem.ShowInteractionPrompt(currentTarget)
            ELSE:
                UISystem.HideInteractionPrompt()
            END IF
        END IF
    END FUNCTION
    
    // Check visibility with raycast
    FUNCTION IsVisible(targetPosition: Vector3) -> Boolean:
        direction = targetPosition - character.Position
        hit = Physics.Raycast(character.Position, direction, distance: direction.Length(), LayerMask: WallsLayer)
        RETURN NOT hit  // No walls blocking = visible
    END FUNCTION
    
    // Start interaction with current target
    FUNCTION StartInteraction():
        IF currentTarget == null:
            RETURN
        END IF
        
        IF isInteracting:
            RETURN
        END IF
        
        isInteracting = true
        interactionProgress = 0
        
        EMIT EVENT "INTERACT_START" WITH (currentTarget.ID, currentTarget.Type)
        
        // If instant interaction (hold time = 0), complete immediately
        IF currentTarget.HoldTime <= 0:
            CompleteInteraction()
        END IF
    END FUNCTION
    
    // Update interaction progress
    FUNCTION UpdateInteraction(deltaTime: Float):
        IF NOT isInteracting OR currentTarget == null:
            RETURN
        END IF
        
        // Check if still in range
        distance = Distance(character.Position, currentTarget.Position)
        IF distance > currentTarget.InteractionRange:
            CancelInteraction("Out of range")
            RETURN
        END IF
        
        // Progress interaction
        interactionProgress += deltaTime
        
        // Update UI progress bar
        UISystem.UpdateInteractionProgress(interactionProgress / currentTarget.HoldTime)
        
        // Check completion
        IF interactionProgress >= currentTarget.HoldTime:
            CompleteInteraction()
        END IF
    END FUNCTION
    
    // Complete the interaction
    FUNCTION CompleteInteraction():
        IF currentTarget == null:
            RETURN
        END IF
        
        // Execute interaction
        currentTarget.OnInteract(character)
        
        EMIT EVENT "INTERACT_COMPLETE" WITH (currentTarget.ID, currentTarget.Type)
        
        // Reset state
        isInteracting = false
        interactionProgress = 0
        UISystem.HideInteractionProgress()
    END FUNCTION
    
    // Cancel interaction
    FUNCTION CancelInteraction(reason: String):
        IF NOT isInteracting:
            RETURN
        END IF
        
        EMIT EVENT "INTERACT_CANCEL" WITH (currentTarget?.ID, reason)
        
        isInteracting = false
        interactionProgress = 0
        UISystem.HideInteractionProgress()
    END FUNCTION
```

***

### Operator Abilities

#### Ability Summary Table

| Operator       | Ability       | Code                           | Duration | Cooldown | Effect                                 |
| -------------- | ------------- | ------------------------------ | -------- | -------- | -------------------------------------- |
| **Assault**    | Combat Stim   | `ABILITY_ASSAULT_COMBATSTEM`   | 10s      | 90s      | +25% damage, +10% speed                |
| **Support**    | Healing Drone | `ABILITY_SUPPORT_HEALINGDRONE` | 20s      | 120s     | 5 HP/sec in 10m radius                 |
| **Recon**      | UAV Scan      | `ABILITY_RECON_UAVSCAN`        | 8s       | 100s     | Reveal enemies in 30m                  |
| **Tank**       | Riot Shield   | `ABILITY_TANK_RIOTSHIELD`      | 15s      | 80s      | Block 100% frontal damage              |
| **Specialist** | EMP Blast     | `ABILITY_SPEC_EMPBLAST`        | Instant  | 110s     | Disable abilities 10s, destroy gadgets |

#### Ability Implementation Template

```
CLASS OperatorAbility:
    
    // Ability data
    codeName: String
    displayName: String
    duration: Float
    cooldown: Float
    
    // References
    owner: CharacterInstance
    
    // Lifecycle methods
    FUNCTION OnActivate():
        // Apply immediate effects
        // Spawn visual effects
        // Play activation sound
    END FUNCTION
    
    FUNCTION OnUpdate(deltaTime: Float):
        // Update ongoing effects
        // Check for targets in range
    END FUNCTION
    
    FUNCTION OnDeactivate():
        // Remove effects
        // Clean up spawned objects
    END FUNCTION
```

***

### Network Synchronization

#### Replicated Properties

| Property            | Replicate To | Update Rate | Notes               |
| ------------------- | ------------ | ----------- | ------------------- |
| **Position**        | All          | 20Hz        | Interpolated        |
| **Rotation**        | All          | 20Hz        | Interpolated        |
| **Health**          | All          | On change   | Enemies see hp bars |
| **Armor**           | All          | On change   | -                   |
| **MovementState**   | All          | On change   | Animation sync      |
| **CharacterState**  | All          | On change   | Death/downed        |
| **Stamina**         | Owner only   | 10Hz        | UI only             |
| **AbilityCooldown** | Owner only   | On change   | UI only             |

#### Movement Prediction

```
CLIENT-SIDE PREDICTION FLOW:

1. Client receives input
   → Apply movement locally (immediate response)
   → Send input to server
   
2. Server receives input
   → Validate input
   → Apply movement authoritatively
   → Send result to all clients
   
3. Client receives server result
   → Compare local position to server position
   → If divergence > threshold (0.1m):
      → Snap to server position (rubber-band)
   → Else:
      → Continue local prediction
```

***

### Performance Considerations

#### Memory Budget

| Asset      | Max Size | Per Character | Max Characters |
| ---------- | -------- | ------------- | -------------- |
| Model      | 5 MB     | 5 MB          | 20             |
| Textures   | 2 MB     | 2 MB          | 20             |
| Animations | 3 MB     | 3 MB          | 20             |
| **Total**  | 10 MB    | 10 MB         | **200 MB max** |

#### Optimization Strategies

```
1. OBJECT POOLING
   - Pre-instantiate character objects
   - Recycle instead of destroy/create
   
2. LOD SYSTEM
   - Reduce mesh quality at distance
   - Simplify animations for distant characters
   
3. NETWORK CULLING
   - Don't sync distant characters at full rate
   - Reduce update frequency based on distance
```

***

### TODO: Implementation Tasks

#### HIGH Priority 

* [ ] Implement CharacterManager spawn system
* [ ] Create HealthSystem damage calculation
* [ ] Add MovementSystem state machine
* [ ] Implement basic ability cooldown
* [ ] Create InteractionSystem detection

#### MEDIUM Priority 

* [ ] Add all operator abilities
* [ ] Implement downed/revive mechanic
* [ ] Create animation state machine
* [ ] Add network movement prediction
* [ ] Implement stamina sprint system

#### LOW Priority 

* [ ] Add hit reaction animations
* [ ] Create spectator mode
* [ ] Implement kill replay
* [ ] Add character leveling
* [ ] Create emote system

***

### System Relationships

#### Dependency Diagram

```
                    ┌────────────────────┐
                    │  CHARACTER SYSTEM  │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ CONTROL         │  │ WEAPON          │  │ INVENTORY       │
│ SYSTEM          │  │ SYSTEM          │  │ SYSTEM          │
│                 │  │                 │  │                 │
│ • Movement input│  │ • Weapon equip  │  │ • Weight penalty│
│ • Look input    │  │ • Firing        │  │ • Equipment     │
│ • Ability input │  │ • Reloading     │  │ • Item use      │
└─────────────────┘  └─────────────────┘  └─────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ UI              │  │ AUDIO           │  │ NETWORKING      │
│ SYSTEM          │  │ SYSTEM          │  │ SYSTEM          │
│                 │  │                 │  │                 │
│ • Health/stamina│  │ • Footsteps     │  │ • State sync    │
│ • Ability UI    │  │ • Ability sounds│  │ • Movement pred │
│ • Interaction   │  │ • Hit sounds    │  │ • Hit validation│
└─────────────────┘  └─────────────────┘  └─────────────────┘
```
