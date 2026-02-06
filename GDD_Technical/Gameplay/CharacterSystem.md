# Character System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: Weapon System →](./WeaponSystem.md)**

---

## Overview

This document defines the technical implementation of the character system including operators, components, enums, and TODOs.

**Responsibilities:**
- Character movement and rotation
- Health and armor management
- Operator abilities
- Character state synchronization
- Interaction system

---

## Enumerations

### EOperatorClass
```
None = 0
Assault = 1       // Aggressive fragger
Support = 2       // Team medic
Recon = 3         // Information specialist
Tank = 4          // Damage sponge
Specialist = 5    // Tech expert
```

### EMovementState
```
Idle = 0
Walking = 1
Sprinting = 2
Crouching = 3
Dead = 4
```

### EAbilityState
```
Ready = 0          // Can be activated
Active = 1         // Currently active
Cooldown = 2       // On cooldown
Disabled = 3       // Cannot use (EMP'd, etc.)
```

### EInteractionType
```
None = 0
LootContainer = 1
Door = 2
ExtractionPoint = 3
DeadBody = 4
QuestItem = 5
Vendor = 6
```

### ECharacterState
```
Alive = 0
Downed = 1         // Can be revived
Dead = 2
Extracting = 3     // In extraction zone
```

---

## Code Names Reference

### Operator Classes
```
OPER_CLASS_ASSAULT
OPER_CLASS_SUPPORT
OPER_CLASS_RECON
OPER_CLASS_TANK
OPER_CLASS_SPECIALIST
```

### Abilities (by Operator)
```
ABILITY_ASSAULT_COMBATSTEM
ABILITY_SUPPORT_HEALINGDRONE
ABILITY_RECON_UAVSCAN
ABILITY_TANK_RIOTShield
ABILITY_SPEC_EMPBLAST
```

---

## Character Components

### Core Components
Character is composed of modular components for maintainability:

**HealthComponent**
- Health management
- Armor absorption
- Damage calculation
- Death handling

**StaminaComponent**
- Sprint stamina tracking
- Regeneration logic
- Exhaustion states

**InventoryComponent**
- Grid-based storage
- Weight calculation
- Equipment management

**AbilityComponent**
- Operator ability logic
- Cooldown tracking
- Effect application

**MovementComponent** (Unity CharacterController)
- Movement speed calculation
- Sprint/crouch modifiers
- Weight penalties

**InteractionComponent**
- Nearby interactable detection
- Interaction validation
- Range checking

---

## Data Structures

### CharacterStats
```
// Health
MaxHealth: float           // Base: 100
CurrentHealth: float

// Armor
MaxArmor: float            // Based on equipped armor
CurrentArmor: float

// Movement
BaseMovementSpeed: float   // Base: 5.0 m/s
SprintMultiplier: float    // Default: 1.5x
CrouchMultiplier: float    // Default: 0.6x

// Stamina
MaxStamina: float          // Base: 100
CurrentStamina: float
StaminaDrainRate: float    // Per second while sprinting
StaminaRegenRate: float    // Per second when not sprinting
```

### OperatorData
```
CodeName: string              // e.g., "OPER_CLASS_ASSAULT"
DisplayName: string           // e.g., "Assault"
Class: EOperatorClass

// Unique ability
AbilityCodeName: string       // e.g., "ABILITY_ASSAULT_COMBATSTEM"
AbilityCooldown: float        // Seconds
AbilityDuration: float        // Seconds

// Passive bonuses
MovementSpeedBonus: float     // Multiplier (e.g., 1.1 = +10%)
HealthBonus: float            // Additive (e.g., +10 HP)

// Visual
ModelPath: string
IconPath: string
```

### CharacterInstance
```
InstanceID: string           // Player unique ID
Operator: OperatorData
Stats: CharacterStats

// Current state
MovementState: EMovementState
CharacterState: ECharacterState
AbilityState: EAbilityState

// Equipped items
EquippedWeaponID: string
EquippedArmorID: string
EquippedBackpackID: string

// Runtime tracking
AbilityCooldownRemaining: float
Position: Vector3
Rotation: Quaternion
```

---

## System Architecture

### CharacterManager
**Responsibilities:**
- Character spawning
- Operator selection
- Character pooling

**TODO List:**
```csharp
// TODO(P0): Implement character spawning system
// TODO(P0): Create operator selection UI
// TODO(P0): Add character database loader
// TODO(P1): Implement character pooling
// TODO(P2): Add character customization system
// TODO(P2): Create character preview system
```

### HealthSystem
**Responsibilities:**
- Health/armor calculation
- Damage processing
- Death handling
- Revive mechanics (future)

**TODO List:**
```csharp
// TODO(P0): Implement health/armor damage absorption
// TODO(P0): Create death system with item drop
// TODO(P0): Add headshot multiplier logic
// TODO(P1): Implement bleeding mechanic
// TODO(P1): Add limb-specific damage
// TODO(P2): Create revive system (downed state)
// TODO(P3): Add kill cam system
```

### MovementSystem
**Responsibilities:**
- Movement input handling
- Speed calculation with modifiers
- Sprint/crouch states
- Top-down rotation

**TODO List:**
```csharp
// TODO(P0): Implement basic movement (WASD)
// TODO(P0): Add sprint system with stamina
// TODO(P0): Create crouch mechanic
// TODO(P0): Implement top-down mouse rotation
// TODO(P1): Add weight-based speed penalty
// TODO(P1): Create smoothdirection changes
// TODO(P2): Add footstep sounds
// TODO(P3): Implement dodge roll mechanic
```

### AbilitySystem
**Responsibilities:**
- Ability activation
- Cooldown tracking
- Effect application
- Network synchronization

**TODO List:**
```csharp
// TODO(P0): Create base ability class/interface
// TODO(P0): Implement cooldown timer system
// TODO(P0): Add ability activation validation
// TODO(P1): Create visual ability effects
// TODO(P1): Implement ability upgrade system
// TODO(P2): Add ability combo detection
// TODO(P2): Create ability statistics tracking
// TODO(P3): Implement ability loadout presets
```

### InteractionSystem
**Responsibilities:**
- Detect nearby interactables
- Validate interaction range
- Execute interactions
- Show UI prompts

**TODO List:**
```csharp
// TODO(P0): Implement interaction range detection
// TODO(P0): Create interaction validation
// TODO(P0): Add interaction UI prompt
// TODO(P1): Implement hold-to-interact timer
// TODO(P1): Add contextual interaction options
// TODO(P2): Create interaction priority system
// TODO(P2): Add interaction cooldown (prevent spam)
```

---

## Operator Abilities

### Assault - Combat Stim
```csharp
// Code: ABILITY_ASSAULT_COMBATSTEM
// Effect: +25% damage, +10% speed for 10 seconds
// Cooldown: 90 seconds
// TODO(P1): Implement damage buff system
// TODO(P1): Add visual orange tint effect
// TODO(P2): Create heartbeat audio effect
```

### Support - Healing Drone
```csharp
// Code: ABILITY_SUPPORT_HEALINGDRONE
// Effect: Deploy drone, heals 5 HP/sec in 10m radius for 20 seconds
// Cooldown: 120 seconds
// TODO(P1): Create drone AI movement
// TODO(P1): Implement area-of-effect healing
// TODO(P2): Add drone destruction mechanic
```

### Recon - UAV Scan
```csharp
// Code: ABILITY_RECON_UAVSCAN
// Effect: Reveal all enemies in 30m radius for 8 seconds
// Cooldown: 100 seconds
// TODO(P1): Implement enemy reveal system
// TODO(P1): Create radar pulse animation
// TODO(P2): Add counter-UAV ability
```

### Tank - Riot Shield
```csharp
// Code: ABILITY_TANK_RIOTSHIELD
// Effect: Deploy shield, blocks 100% frontal damage for 15 seconds
// Cooldown: 80 seconds
// TODO(P1): Create shield blocking logic
// TODO(P1): Implement movement penalty
// TODO(P2): Add shield health/durability
```

### Specialist - EMP Blast
```csharp
// Code: ABILITY_SPEC_EMPBLAST
// Effect: 15m radius, disable abilities for 10 seconds, destroy gadgets
// Cooldown: 110 seconds
// TODO(P1): Implement ability disable system
// TODO(P1): Create gadget destruction logic
// TODO(P2): Add electric pulse VFX
```

---

## Movement Modifiers

### Speed Calculation
```csharp
FinalSpeed = BaseSpeed 
    * MovementStateMultiplier    // Sprint/Crouch
    * WeightMultiplier            // From inventory
    * AbilityMultiplier           // From active abilities
    * TerrainMultiplier           // Water, mud, etc.
```

**TODO List:**
```csharp
// TODO(P0): Implement movement state multipliers
// TODO(P1): Add weight penalty from InventoryComponent
// TODO(P1): Create ability speed modifiers
// TODO(P2): Implement terrain-based penalties
// TODO(P3): Add momentum system for realistic movement
```

---

## Health & Damage

### Damage Calculation
```csharp
// Armor absorbs 70% of damage first
ArmorDamage = IncomingDamage * 0.7
RemainingDamage = IncomingDamage - ArmorDamage

CurrentArmor -= ArmorDamage
if (CurrentArmor < 0) {
    RemainingDamage += Abs(CurrentArmor)
    CurrentArmor = 0
}

CurrentHealth -= RemainingDamage
```

**TODO List:**
```csharp
// TODO(P0): Implement armor absorption logic
// TODO(P0): Add headshot multiplier (2.0x base)
// TODO(P1): Create limb damage modifiers
// TODO(P1): Implement bleeding damage over time
// TODO(P2): Add critical hit system
// TODO(P2): Create damage resistance buffs
```

---

## Network Synchronization

### Replicated Properties
```csharp
// Always replicate to all
- Health, Armor (visible to enemies)
- Position, Rotation
- Current weapon
- Movement state

// Owner-only replication
- Stamina
- Ability cooldown
- Inventory weight

// Skip owner (cosmetic)
- Aiming state
- Animation states
```

**TODO List:**
```csharp
// TODO(P0): Setup character replication
// TODO(P0): Implement client-side prediction for movement
// TODO(P1): Add server-authoritative validation
// TODO(P1): Create lag compensation for hit detection
// TODO(P2): Implement interpolation for smooth movement
// TODO(P2): Add anti-cheat validation
```

---

## Animation & Visuals

### Animation States
```
Idle = 0
Walk = 1
Run = 2
Crouch = 3
Shoot = 4
Reload = 5
UseAbility = 6
Death = 7
```

**TODO List:**
```csharp
// TODO(P1): Create animation state machine
// TODO(P1): Implement animation blending
// TODO(P1): Add weapon-specific animations
// TODO(P2): Create ability activation animations
// TODO(P2): Implement hit reaction animations
// TODO(P3): Add emote system
```

---

## Performance Considerations

### Memory Budget
```
Character Model: Max 5MB per operator
Character Textures: Max 2MB per operator
Animation Data: Max 3MB per operator
Total per Character: ~10MB
Max Characters in Scene: 20 (200MB total)
```

### Network Optimization
```csharp
// TODO(P1): Implement network culling (distance-based)
// TODO(P1): Reduce update frequency for distant players
// TODO(P2): Compress character state data
// TODO(P2): Use delta compression for updates
```

---

## Testing & Debugging

### Debug Commands
```csharp
// TODO(P2): Add character.spawn <operator> command
// TODO(P2): Add character.kill command
// TODO(P2): Add character.heal <amount> command
// TODO(P2): Add character.setAbilityCooldown <seconds>
// TODO(P3): Create character stat inspector UI
```

### Unit Tests Required
```csharp
// TODO(P1): Test damage calculation with armor
// TODO(P1): Test movement speed modifiers
// TODO(P1): Test ability cooldown system
// TODO(P2): Test stamina consumption/regeneration
// TODO(P2): Test interaction range validation
```

---

## Integration Points

### With Weapon System
- Weapon equipping/holstering
- Aiming state
- Recoil application
- Animation triggers

### With Inventory System
- Weight penalty calculation
- Equipment bonuses
- Item usage

### With UI System
- Health/armor display
- Stamina bar
- Ability cooldown indicator
- Interaction prompts

### With Networking System
- Character state sync
- Movement prediction
- Hit validation

---

## Future Enhancements

```csharp
// TODO(P3): Character progression system (leveling)
// TODO(P3): Operator customization (skins, emotes)
// TODO(P3): Revive/downed state mechanic
// TODO(P3): Character stats tracking (kills, deaths, damage)
// TODO(P3): Spectator mode for dead players
// TODO(P3): Kill replay system
```

---

**[← Back to Index](../README.md)** | **[Next: Weapon System →](./WeaponSystem.md)**
