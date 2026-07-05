---
title: Weapon System - Technical Design Sutureument
type: docs
---

# Weapon System - Technical Design Sutureument

### Related Sutureuments

| Sutureument          | Relationship             | Link                                                                                                                              |
| -------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **Weapons Design**   | High-level weapon design | [GDD\_HighLevel/Combat/Weapons.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_HighLevel/Combat/Weapons.md) |
| **Character System** | Weapon equipping         | [CharacterSystem.md](CharacterSystem.md)                                                                                          |
| **Inventory System** | Weapon storage           | [InventorySystem.md](InventorySystem.md)                                                                                          |
| **Audio System**     | Weapon sounds            | [../Systems/AudioSystem.md](../Systems/AudioSystem.md)                                                                            |

***

### Overview

#### Purpose

The **Weapon System** handles all aspects of weapon behavior including firing, reloading, recoil, attachments, and damage calculation.

#### Core Functions

| Function               | Description                             |
| ---------------------- | --------------------------------------- |
| **Weapon Management**  | Spawning, pooling, registration         |
| **Fire Control**       | Fire rate, fire modes, ammo consumption |
| **Damage Calculation** | Base damage, modifiers, penetration     |
| **Recoil System**      | Pattern-based recoil, recovery          |
| **Attachment System**  | Slot-based modifications                |
| **Ballistics**         | Hitscan, projectile, penetration        |

#### Design Goals

```
1. RESPONSIVE - Instant feedback on fire input
2. SATISFYING - Impactful sound and visual feedback
3. BALANCED - Each weapon has clear pros/cons
4. CUSTOMIZABLE - Attachments change playstyle
5. FAIR - Server-authoritative hit validation
```

***

### System Architecture

#### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         WEAPON SYSTEM                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   WEAPON     │    │   DAMAGE     │    │   RECOIL     │          │
│  │   MANAGER    │───▶│   SYSTEM     │───▶│   SYSTEM     │          │
│  │              │    │              │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ Database     │    │ Hit Detection│    │ Camera Kick  │          │
│  │ Pooling      │    │ Penetration  │    │ Pattern      │          │
│  │ Spawning     │    │ Falloff      │    │ Recovery     │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │  WEAPON      │    │ ATTACHMENT   │    │  BALLISTICS  │          │
│  │  CONTROLLER  │    │ SYSTEM       │    │  SYSTEM      │          │
│  │              │    │              │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### Core Components

| Component            | Responsibility              | Dependencies     |
| -------------------- | --------------------------- | ---------------- |
| **WeaponManager**    | Database, pooling, spawning | None             |
| **WeaponController** | Fire control, ammo, reload  | CharacterSystem  |
| **DamageSystem**     | Damage calc, hit detection  | HealthSystem     |
| **RecoilSystem**     | Recoil patterns, recovery   | CameraController |
| **AttachmentSystem** | Slot management, modifiers  | None             |
| **BallisticsSystem** | Projectile, penetration     | Physics          |

***

### Enums & Types

#### EWeaponType

Weapon category classification.

| Code Name            | Display Name      | Slot      | Range  | Fire Style | Description                 |
| -------------------- | ----------------- | --------- | ------ | ---------- | --------------------------- |
| `WT_None`            | None              | N/A       | N/A    | N/A        | Invalid/undefined weapon    |
| `WT_AssaultRifle`    | Assault Rifle     | Primary   | Medium | Auto/Semi  | Versatile combat rifle      |
| `WT_SubmachineGun`   | Submachine Gun    | Primary   | Close  | Auto       | High fire rate, close range |
| `WT_Shotgun`         | Shotgun           | Primary   | Close  | Pump/Semi  | High damage, spread shot    |
| `WT_SniperRifle`     | Sniper Rifle      | Primary   | Long   | Bolt/Semi  | Precision long range        |
| `WT_LightMachineGun` | Light Machine Gun | Primary   | Medium | Auto       | High capacity suppression   |
| `WT_Pistol`          | Pistol            | Secondary | Close  | Semi       | Backup sidearm              |
| `WT_Melee`           | Melee             | Melee     | Melee  | N/A        | Close quarters combat       |

***

#### EWeaponRarity

Weapon quality tier.

| Code Name      | Display Name | Color  | Damage Mult | Attach Slots | Description      |
| -------------- | ------------ | ------ | ----------- | ------------ | ---------------- |
| `WR_Common`    | Common       | White  | 1.0×        | 1            | Standard issue   |
| `WR_Uncommon`  | Uncommon     | Green  | 1.1×        | 2            | Improved quality |
| `WR_Rare`      | Rare         | Blue   | 1.2×        | 3            | Military grade   |
| `WR_Epic`      | Epic         | Purple | 1.35×       | 4            | Elite weapon     |
| `WR_Legendary` | Legendary    | Gold   | 1.5×        | 5            | Unique weapon    |

***

#### EFireMode

Weapon firing mode.

| Code Name       | Display Name | Rounds/Trigger | Fire Rate Mult | Recoil Mult |
| --------------- | ------------ | -------------- | -------------- | ----------- |
| `FM_Single`     | Single       | 1              | 0.4×           | 0.8×        |
| `FM_Burst`      | Burst        | 3              | 0.7×           | 1.0×        |
| `FM_Auto`       | Auto         | Continuous     | 1.0×           | 1.0×        |
| `FM_BoltAction` | Bolt Action  | 1              | 0.2×           | 1.5×        |

***

#### EAttachmentSlot

Weapon attachment slot.

| Code Name          | Display Name | Position   | Affects           | Max Per Weapon |
| ------------------ | ------------ | ---------- | ----------------- | -------------- |
| `SLOT_None`        | None         | N/A        | N/A               | 0              |
| `SLOT_Optic`       | Optic        | Top rail   | Zoom, ADS speed   | 1              |
| `SLOT_Barrel`      | Barrel       | Muzzle     | Noise, Range      | 1              |
| `SLOT_Stock`       | Stock        | Rear       | Recoil, ADS speed | 1              |
| `SLOT_Magazine`    | Magazine     | Receiver   | Capacity, Reload  | 1              |
| `SLOT_Underbarrel` | Underbarrel  | Lower rail | Recoil, Accuracy  | 1              |

***

#### ERecoilPattern

Weapon recoil behavior.

| Code Name          | Display Name   | Vertical | Horizontal  | Predictability |
| ------------------ | -------------- | -------- | ----------- | -------------- |
| `RP_Vertical`      | Vertical       | High     | None        | High           |
| `RP_VerticalLeft`  | Vertical Left  | High     | Left drift  | Medium         |
| `RP_VerticalRight` | Vertical Right | High     | Right drift | Medium         |
| `RP_Diagonal`      | Diagonal       | Medium   | Alternating | Medium         |
| `RP_Random`        | Random         | Variable | Variable    | Low            |

***

#### EAmmoType

Ammunition caliber type.

| Code Name      | Display Name | Base Damage  | Penetration | Stack Size | Description          |
| -------------- | ------------ | ------------ | ----------- | ---------- | -------------------- |
| `AMMO_9mm`     | 9mm          | 25           | Low         | 60         | Pistol, SMG rounds   |
| `AMMO_556`     | 5.56×45mm    | 35           | Medium      | 30         | NATO rifle rounds    |
| `AMMO_762`     | 7.62×39mm    | 45           | Medium-High | 30         | AK platform rounds   |
| `AMMO_12g`     | 12 Gauge     | 80 (pellets) | Low         | 20         | Shotgun shells       |
| `AMMO_762NATO` | 7.62×51mm    | 65           | High        | 20         | Marksman rounds      |
| `AMMO_50cal`   | .50 BMG      | 120          | Very High   | 10         | Anti-material rounds |

***

#### EProjectileType

Ballistics simulation type.

| Code Name         | Display Name | Speed       | Drop     | Use Case   | Description            |
| ----------------- | ------------ | ----------- | -------- | ---------- | ---------------------- |
| `PROJ_Hitscan`    | Hitscan      | Instant     | None     | < 50m      | Instant hit detection  |
| `PROJ_Projectile` | Projectile   | 400-900 m/s | Yes      | > 50m      | Physical bullet travel |
| `PROJ_Hybrid`     | Hybrid       | Variable    | Variable | All ranges | Distance-based switch  |

***

#### EMaterialPenetration

Material penetration tier.

| Code Name       | Display Name | Penetration | Damage Loss | Description          |
| --------------- | ------------ | ----------- | ----------- | -------------------- |
| `MAT_Wood`      | Wood         | 100%        | 10%         | Thin wooden surfaces |
| `MAT_ThinMetal` | Thin Metal   | 50%         | 30%         | Sheet metal, cars    |
| `MAT_Concrete`  | Concrete     | 0%          | 100%        | Walls, thick cover   |
| `MAT_Flesh`     | Flesh        | 100%        | 20%         | Body penetration     |

***

### Code Names

#### Weapon Events

| Code Name          | Trigger          | Parameters              | Description              |
| ------------------ | ---------------- | ----------------------- | ------------------------ |
| `WPN_EQUIP`        | Weapon equipped  | WeaponID, Slot          | Weapon drawn/selected    |
| `WPN_UNEQUIP`      | Weapon holstered | WeaponID                | Weapon put away          |
| `WPN_FIRE`         | Weapon fired     | WeaponID, AmmoRemaining | Shot fired               |
| `WPN_RELOAD_START` | Reload begins    | WeaponID, ReloadTime    | Reload animation started |
| `WPN_RELOAD_END`   | Reload complete  | WeaponID, NewAmmo       | Reload finished          |
| `WPN_EMPTY`        | Ammo depleted    | WeaponID                | Magazine empty           |

#### Combat Events

| Code Name         | Trigger          | Parameters                 | Description        |
| ----------------- | ---------------- | -------------------------- | ------------------ |
| `DMG_HIT`         | Damage dealt     | VictimID, Damage, Bodypart | Hit registered     |
| `DMG_HEADSHOT`    | Headshot         | VictimID, Damage           | Critical head hit  |
| `DMG_KILL`        | Kill confirmed   | VictimID, WeaponID         | Target eliminated  |
| `DMG_ASSIST`      | Kill assist      | VictimID, DamageDealt      | Assisted in kill   |
| `DMG_PENETRATION` | Wall penetration | Material, DamageReduction  | Shot through cover |

#### Attachment Events

| Code Name          | Trigger            | Parameters                   | Description             |
| ------------------ | ------------------ | ---------------------------- | ----------------------- |
| `ATT_EQUIP`        | Attachment added   | WeaponID, AttachmentID, Slot | Attachment mounted      |
| `ATT_REMOVE`       | Attachment removed | WeaponID, AttachmentID, Slot | Attachment detached     |
| `ATT_INCOMPATIBLE` | Invalid attachment | WeaponID, AttachmentID       | Incompatible attachment |

#### Ammo Events

| Code Name      | Trigger          | Parameters          | Description                |
| -------------- | ---------------- | ------------------- | -------------------------- |
| `AMMO_PICKUP`  | Ammo collected   | AmmoType, Amount    | Ammo added to reserve      |
| `AMMO_CONSUME` | Ammo used        | AmmoType, Amount    | Ammo consumed from reserve |
| `AMMO_LOW`     | Low ammo warning | WeaponID, Remaining | Ammo below threshold       |
| `AMMO_OUT`     | No ammo          | AmmoType            | Reserve empty              |

***

### Data Structures

#### WeaponData

**Purpose:** Static definition of a weapon type.

```
STRUCT WeaponData:
    // Identification
    CodeName: String                // e.g., "WPN_AR_AK47"
    DisplayName: String             // e.g., "AK-47"
    Description: String             // Flavor text
    
    // Classification
    Type: EWeaponType
    Rarity: EWeaponRarity
    FireMode: EFireMode
    AmmoType: EAmmoType
    
    // Combat stats
    Damage: Integer                 // Base damage per bullet
    RPM: Integer                    // Rounds per minute
    MagazineSize: Integer           // Bullets per mag
    Range: Float                    // Effective range in meters
    
    // Handling
    ReloadTime: Float               // Seconds to reload
    EquipTime: Float                // Seconds to draw weapon
    ADSTime: Float                  // Seconds to aim down sights
    
    // Recoil
    RecoilPattern: ERecoilPattern
    VerticalRecoil: Float           // Degrees per shot
    HorizontalRecoil: Float         // Degrees per shot
    RecoilRecovery: Float           // Seconds to recover
    
    // Attachments
    AttachmentSlots: Integer        // Number of slots
    AvailableSlots: List<EAttachmentSlot>
    
    // Economy
    BuyValue: Integer               // Purchase price
    SellValue: Integer              // Vendor price
    
    // Assets
    PrefabPath: String              // 3D model
    IconPath: String                // UI icon
    FireSoundPath: String           // Firing sound
```

#### AttachmentData

**Purpose:** Static definition of a weapon attachment.

```
STRUCT AttachmentData:
    // Identification
    CodeName: String                // e.g., "ATT_OPTIC_REDDOT"
    DisplayName: String             // e.g., "Red Dot Sight"
    Description: String
    
    // Classification
    Slot: EAttachmentSlot
    Rarity: EWeaponRarity
    
    // Stat modifiers (percentage: 1.0 = no change)
    AccuracyModifier: Float         // e.g., 1.1 = +10% accuracy
    RangeModifier: Float
    RecoilModifier: Float           // e.g., 0.85 = -15% recoil
    ADSSpeedModifier: Float
    MobilityModifier: Float
    MagazineModifier: Integer       // e.g., +10 bullets
    ReloadSpeedModifier: Float
    
    // Special effects
    ZoomLevel: Float                // For optics (1.0 = no zoom)
    SuppressorEffect: Boolean       // Reduces firing sound
    TracerEffect: Boolean           // Visible bullet trails
    
    // Economy
    BuyValue: Integer
    SellValue: Integer
    
    // Compatibility
    CompatibleWeapons: List<EWeaponType>
    
    // Assets
    PrefabPath: String
    IconPath: String
```

#### WeaponInstance

**Purpose:** Runtime instance of a weapon.

```
CLASS WeaponInstance:
    // Unique identification
    InstanceID: String              // UUID
    BaseData: WeaponData            // Reference to static data
    
    // Attachments
    Attachments: Map<EAttachmentSlot, AttachmentData>
    
    // Runtime state
    CurrentAmmo: Integer            // Bullets in magazine
    ReserveAmmo: Integer            // Bullets in inventory
    Durability: Float               // 0-100 (future use)
    
    // Calculated final stats (base ± attachments)
    FinalDamage: Integer
    FinalAccuracy: Float
    FinalRecoil: Float
    FinalRange: Float
    FinalADSSpeed: Float
    FinalMagazineSize: Integer
    FinalReloadTime: Float
    
    // Owner reference
    OwnerCharacterID: String
    
    // Recalculate stats when attachments change
    FUNCTION RecalculateStats():
        FinalDamage = BaseData.Damage
        FinalAccuracy = 1.0
        FinalRecoil = 1.0
        FinalRange = BaseData.Range
        FinalADSSpeed = BaseData.ADSTime
        FinalMagazineSize = BaseData.MagazineSize
        FinalReloadTime = BaseData.ReloadTime
        
        // Apply rarity bonus
        FinalDamage = FinalDamage * GetRarityMultiplier(BaseData.Rarity)
        
        // Apply attachment modifiers
        FOR EACH (slot, attachment) IN Attachments:
            FinalAccuracy *= attachment.AccuracyModifier
            FinalRecoil *= attachment.RecoilModifier
            FinalRange *= attachment.RangeModifier
            FinalADSSpeed *= attachment.ADSSpeedModifier
            FinalMagazineSize += attachment.MagazineModifier
            FinalReloadTime *= attachment.ReloadSpeedModifier
        END FOR
    END FUNCTION
```

***

### Core Classes

#### WeaponManager

**Purpose:** Central weapon database and object pooling.

**Pseudocode:**

```
CLASS WeaponManager:
    
    // Singleton instance
    STATIC instance: WeaponManager
    
    // Weapon database
    weaponDatabase: Map<String, WeaponData>
    attachmentDatabase: Map<String, AttachmentData>
    
    // Object pooling
    weaponPool: ObjectPool<WeaponInstance>
    projectilePool: ObjectPool<Projectile>
    
    // Constants
    CONST MAX_POOLED_WEAPONS = 50
    CONST MAX_POOLED_PROJECTILES = 200
    
    // Initialize on game start
    FUNCTION Initialize():
        LoadWeaponDatabase()
        LoadAttachmentDatabase()
        CreateObjectPools()
    END FUNCTION
    
    // Load weapon database from config
    FUNCTION LoadWeaponDatabase():
        FOR EACH weaponAsset IN Resources.Load("Weapons"):
            data = ParseWeaponData(weaponAsset)
            weaponDatabase[data.CodeName] = data
        END FOR
        
        LOG "Loaded " + weaponDatabase.Count + " weapons"
    END FUNCTION
    
    // Get weapon data by code name
    FUNCTION GetWeaponData(codeName: String) -> WeaponData?:
        IF weaponDatabase.Contains(codeName):
            RETURN weaponDatabase[codeName]
        END IF
        LOG ERROR "Weapon not found: " + codeName
        RETURN null
    END FUNCTION
    
    // Spawn a new weapon instance
    FUNCTION SpawnWeapon(codeName: String, position: Vector3) -> WeaponInstance:
        data = GetWeaponData(codeName)
        IF data == null:
            RETURN null
        END IF
        
        // Get from pool
        weapon = weaponPool.Get()
        
        // Initialize
        weapon.InstanceID = GenerateUUID()
        weapon.BaseData = data
        weapon.CurrentAmmo = data.MagazineSize
        weapon.ReserveAmmo = data.MagazineSize * 3
        weapon.Durability = 100
        weapon.Attachments.Clear()
        
        // Calculate initial stats
        weapon.RecalculateStats()
        
        // Position in world
        SetWorldPosition(weapon, position)
        
        RETURN weapon
    END FUNCTION
    
    // Return weapon to pool
    FUNCTION DespawnWeapon(weapon: WeaponInstance):
        weapon.OwnerCharacterID = null
        weaponPool.Return(weapon)
    END FUNCTION
    
    // Check attachment compatibility
    FUNCTION CanAttach(weapon: WeaponInstance, attachment: AttachmentData) -> Boolean:
        // Check if slot is available
        IF NOT weapon.BaseData.AvailableSlots.Contains(attachment.Slot):
            RETURN false
        END IF
        
        // Check if slot is empty
        IF weapon.Attachments.Contains(attachment.Slot):
            RETURN false
        END IF
        
        // Check weapon type compatibility
        IF NOT attachment.CompatibleWeapons.Contains(weapon.BaseData.Type):
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
```

***

#### WeaponController

**Purpose:** Handle weapon firing, reloading, and state management.

**Pseudocode:**

```
CLASS WeaponController:
    
    // Owner reference
    ownerCharacter: CharacterInstance
    
    // Current weapon
    currentWeapon: WeaponInstance
    
    // State
    isReloading: Boolean = false
    isFiring: Boolean = false
    lastFireTime: Float = 0
    burstCount: Integer = 0
    
    // Fire rate calculation
    FUNCTION GetFireInterval() -> Float:
        // Convert RPM to seconds between shots
        RETURN 60.0 / currentWeapon.BaseData.RPM
    END FUNCTION
    
    // Try to fire weapon
    FUNCTION TryFire() -> Boolean:
        IF currentWeapon == null:
            RETURN false
        END IF
        
        IF isReloading:
            RETURN false
        END IF
        
        IF currentWeapon.CurrentAmmo <= 0:
            EMIT EVENT "WPN_EMPTY" WITH (currentWeapon.InstanceID)
            PlaySound("EmptyClick")
            RETURN false
        END IF
        
        // Check fire rate
        timeSinceLastFire = CurrentTime() - lastFireTime
        IF timeSinceLastFire < GetFireInterval():
            RETURN false
        END IF
        
        // Execute fire
        ExecuteFire()
        RETURN true
    END FUNCTION
    
    // Execute actual firing
    FUNCTION ExecuteFire():
        lastFireTime = CurrentTime()
        
        // Consume ammo
        currentWeapon.CurrentAmmo -= 1
        
        // Handle fire mode
        SWITCH currentWeapon.BaseData.FireMode:
            CASE FM_Single:
                FireOnce()
            CASE FM_Burst:
                StartBurst(3)
            CASE FM_Auto:
                FireOnce()
            CASE FM_BoltAction:
                FireOnce()
                StartBoltCycle()
        END SWITCH
        
        // Apply recoil
        RecoilSystem.ApplyRecoil(currentWeapon)
        
        // Play effects
        PlayMuzzleFlash()
        PlayFireSound()
        SpawnCasing()
        
        EMIT EVENT "WPN_FIRE" WITH (currentWeapon.InstanceID, currentWeapon.CurrentAmmo)
    END FUNCTION
    
    // Fire a single shot
    FUNCTION FireOnce():
        // Get aim direction from character
        aimOrigin = ownerCharacter.GetAimOrigin()
        aimDirection = ownerCharacter.GetAimDirection()
        
        // Apply accuracy spread
        spread = CalculateSpread()
        finalDirection = ApplySpread(aimDirection, spread)
        
        // Execute ballistics
        BallisticsSystem.Fire(
            origin: aimOrigin,
            direction: finalDirection,
            weapon: currentWeapon,
            shooter: ownerCharacter
        )
    END FUNCTION
    
    // Calculate current accuracy spread
    FUNCTION CalculateSpread() -> Float:
        baseSpread = 1.0 - currentWeapon.FinalAccuracy
        
        // Moving penalty
        IF ownerCharacter.MovementState == MS_Walking:
            baseSpread *= 1.3
        ELSE IF ownerCharacter.MovementState == MS_Sprinting:
            baseSpread *= 2.0
        END IF
        
        // ADS bonus
        IF IsAiming():
            baseSpread *= 0.3
        END IF
        
        // Crouching bonus
        IF ownerCharacter.MovementState == MS_Crouching:
            baseSpread *= 0.7
        END IF
        
        RETURN Clamp(baseSpread, 0.01, 0.5)
    END FUNCTION
    
    // Start reload
    FUNCTION TryReload() -> Boolean:
        IF currentWeapon == null:
            RETURN false
        END IF
        
        IF isReloading:
            RETURN false
        END IF
        
        IF currentWeapon.CurrentAmmo >= currentWeapon.FinalMagazineSize:
            RETURN false  // Already full
        END IF
        
        IF currentWeapon.ReserveAmmo <= 0:
            RETURN false  // No reserve ammo
        END IF
        
        // Start reload
        isReloading = true
        PlayReloadAnimation()
        
        EMIT EVENT "WPN_RELOAD_START" WITH (currentWeapon.InstanceID, currentWeapon.FinalReloadTime)
        
        // Schedule reload complete
        ScheduleTask(currentWeapon.FinalReloadTime, CompleteReload)
        
        RETURN true
    END FUNCTION
    
    // Complete reload
    FUNCTION CompleteReload():
        IF NOT isReloading:
            RETURN
        END IF
        
        // Calculate ammo to add
        neededAmmo = currentWeapon.FinalMagazineSize - currentWeapon.CurrentAmmo
        availableAmmo = Min(neededAmmo, currentWeapon.ReserveAmmo)
        
        // Transfer ammo
        currentWeapon.CurrentAmmo += availableAmmo
        currentWeapon.ReserveAmmo -= availableAmmo
        
        isReloading = false
        
        EMIT EVENT "WPN_RELOAD_END" WITH (currentWeapon.InstanceID, currentWeapon.CurrentAmmo)
    END FUNCTION
    
    // Equip weapon
    FUNCTION EquipWeapon(weapon: WeaponInstance):
        IF currentWeapon != null:
            UnequipWeapon()
        END IF
        
        currentWeapon = weapon
        weapon.OwnerCharacterID = ownerCharacter.InstanceID
        
        PlayEquipAnimation()
        
        EMIT EVENT "WPN_EQUIP" WITH (weapon.InstanceID, weapon.BaseData.Type)
    END FUNCTION
    
    // Unequip current weapon
    FUNCTION UnequipWeapon():
        IF currentWeapon == null:
            RETURN
        END IF
        
        EMIT EVENT "WPN_UNEQUIP" WITH (currentWeapon.InstanceID)
        
        currentWeapon.OwnerCharacterID = null
        currentWeapon = null
        
        isReloading = false
        isFiring = false
    END FUNCTION
```

***

#### DamageSystem

**Purpose:** Calculate and apply damage.

**Pseudocode:**

```
CLASS DamageSystem:
    
    // Damage modifiers
    CONST HEADSHOT_MULTIPLIER = 2.0
    CONST LIMB_MULTIPLIER = 0.75
    CONST CHEST_MULTIPLIER = 1.0
    CONST STOMACH_MULTIPLIER = 0.9
    
    // Falloff distances
    CONST FALLOFF_START = 30.0      // Meters
    CONST FALLOFF_END = 80.0        // Meters
    CONST MIN_FALLOFF_DAMAGE = 0.5  // 50% minimum damage
    
    // Calculate damage with all modifiers
    FUNCTION CalculateDamage(weapon: WeaponInstance, hitInfo: HitInfo) -> DamageResult:
        result = NEW DamageResult()
        
        // Base damage
        baseDamage = weapon.FinalDamage
        
        // Bodypart multiplier
        bodypartMult = GetBodypartMultiplier(hitInfo.HitBone)
        
        // Distance falloff
        distance = Distance(hitInfo.Origin, hitInfo.HitPoint)
        falloffMult = CalculateFalloff(distance, weapon.FinalRange)
        
        // Penetration damage loss
        penetrationMult = 1.0
        IF hitInfo.PenetratedMaterial != null:
            penetrationMult = GetPenetrationDamageMult(hitInfo.PenetratedMaterial)
        END IF
        
        // Calculate final damage
        result.FinalDamage = baseDamage * bodypartMult * falloffMult * penetrationMult
        result.IsHeadshot = (hitInfo.HitBone == "Head")
        result.IsCritical = result.IsHeadshot
        result.DamageType = weapon.BaseData.AmmoType
        
        RETURN result
    END FUNCTION
    
    // Get damage multiplier for hit location
    FUNCTION GetBodypartMultiplier(bone: String) -> Float:
        SWITCH bone:
            CASE "Head":
                RETURN HEADSHOT_MULTIPLIER
            CASE "Chest":
                RETURN CHEST_MULTIPLIER
            CASE "Stomach":
                RETURN STOMACH_MULTIPLIER
            CASE "Arm", "Hand":
                RETURN LIMB_MULTIPLIER
            CASE "Leg", "Foot":
                RETURN LIMB_MULTIPLIER
            DEFAULT:
                RETURN 1.0
        END SWITCH
    END FUNCTION
    
    // Calculate distance-based damage falloff
    FUNCTION CalculateFalloff(distance: Float, weaponRange: Float) -> Float:
        IF distance <= FALLOFF_START:
            RETURN 1.0  // No falloff
        END IF
        
        IF distance >= FALLOFF_END:
            RETURN MIN_FALLOFF_DAMAGE  // Minimum damage
        END IF
        
        // Linear falloff between start and end
        falloffProgress = (distance - FALLOFF_START) / (FALLOFF_END - FALLOFF_START)
        RETURN Lerp(1.0, MIN_FALLOFF_DAMAGE, falloffProgress)
    END FUNCTION
    
    // Apply damage to target
    FUNCTION ApplyDamage(targetID: String, damageResult: DamageResult, attackerID: String):
        target = CharacterManager.GetCharacterByID(targetID)
        IF target == null:
            RETURN
        END IF
        
        // Apply through health system
        HealthSystem.ApplyDamage(
            target,
            damageResult.FinalDamage,
            attackerID,
            damageResult.DamageType
        )
        
        // Fire events
        EMIT EVENT "DMG_HIT" WITH (targetID, damageResult.FinalDamage, damageResult.HitBone)
        
        IF damageResult.IsHeadshot:
            EMIT EVENT "DMG_HEADSHOT" WITH (targetID, damageResult.FinalDamage)
        END IF
        
        IF target.Stats.CurrentHealth <= 0:
            EMIT EVENT "DMG_KILL" WITH (targetID, attackerID)
        END IF
    END FUNCTION
```

***

#### RecoilSystem

**Purpose:** Apply and manage weapon recoil.

**Pseudocode:**

```
CLASS RecoilSystem:
    
    // Current recoil state
    currentVerticalRecoil: Float = 0
    currentHorizontalRecoil: Float = 0
    shotsFiredInBurst: Integer = 0
    isRecovering: Boolean = false
    
    // Recoil pattern data
    patterns: Map<ERecoilPattern, RecoilPatternData>
    
    // Apply recoil from a shot
    FUNCTION ApplyRecoil(weapon: WeaponInstance):
        shotsFiredInBurst += 1
        isRecovering = false
        
        // Get pattern data
        patternData = patterns[weapon.BaseData.RecoilPattern]
        
        // Calculate vertical recoil
        verticalKick = weapon.BaseData.VerticalRecoil * weapon.FinalRecoil
        verticalKick *= patternData.GetVerticalMultiplier(shotsFiredInBurst)
        
        // Calculate horizontal recoil
        horizontalKick = weapon.BaseData.HorizontalRecoil * weapon.FinalRecoil
        horizontalKick *= patternData.GetHorizontalMultiplier(shotsFiredInBurst)
        
        // Apply random variation
        verticalKick *= Random(0.9, 1.1)
        horizontalKick *= Random(-1.0, 1.0)  // Can go left or right
        
        // Add to current recoil
        currentVerticalRecoil += verticalKick
        currentHorizontalRecoil += horizontalKick
        
        // Clamp maximum recoil
        currentVerticalRecoil = Min(currentVerticalRecoil, patternData.MaxVertical)
        currentHorizontalRecoil = Clamp(currentHorizontalRecoil, -patternData.MaxHorizontal, patternData.MaxHorizontal)
        
        // Apply to camera
        CameraController.AddRecoilOffset(verticalKick, horizontalKick)
        
        EMIT EVENT "RECOIL_APPLY" WITH (weapon.InstanceID, verticalKick, horizontalKick)
    END FUNCTION
    
    // Update recoil recovery
    FUNCTION Update(deltaTime: Float, weapon: WeaponInstance):
        // Check if should recover
        IF NOT isFiring AND NOT isRecovering:
            isRecovering = true
            shotsFiredInBurst = 0
        END IF
        
        IF isRecovering:
            recoverySpeed = weapon.BaseData.RecoilRecovery * deltaTime
            
            // Recover vertical
            IF currentVerticalRecoil > 0:
                recovery = Min(currentVerticalRecoil, recoverySpeed)
                currentVerticalRecoil -= recovery
                CameraController.AddRecoilOffset(-recovery, 0)
            END IF
            
            // Recover horizontal
            IF Abs(currentHorizontalRecoil) > 0.01:
                recovery = Sign(currentHorizontalRecoil) * Min(Abs(currentHorizontalRecoil), recoverySpeed)
                currentHorizontalRecoil -= recovery
                CameraController.AddRecoilOffset(0, -recovery)
            END IF
            
            // Reset when recovered
            IF currentVerticalRecoil <= 0 AND Abs(currentHorizontalRecoil) < 0.01:
                currentVerticalRecoil = 0
                currentHorizontalRecoil = 0
                isRecovering = false
                
                EMIT EVENT "RECOIL_RECOVER" WITH (weapon.InstanceID)
            END IF
        END IF
    END FUNCTION
    
    // Apply player compensation (counter-recoil)
    FUNCTION ApplyCompensation(inputDelta: Vector2):
        // Player pulling down to compensate
        compensation = inputDelta.y * compensationMultiplier
        currentVerticalRecoil = Max(0, currentVerticalRecoil - compensation)
        
        EMIT EVENT "RECOIL_CONTROL" WITH (inputDelta)
    END FUNCTION
```

***

#### BallisticsSystem

**Purpose:** Handle projectile simulation and hit detection.

**Pseudocode:**

```
CLASS BallisticsSystem:
    
    // Distance thresholds for hybrid ballistics
    CONST HITSCAN_MAX_DISTANCE = 20.0
    CONST PROJECTILE_MIN_DISTANCE = 20.0
    
    // Fire a shot
    FUNCTION Fire(origin: Vector3, direction: Vector3, weapon: WeaponInstance, shooter: CharacterInstance):
        projectileType = weapon.BaseData.ProjectileType
        
        SWITCH projectileType:
            CASE PROJ_Hitscan:
                FireHitscan(origin, direction, weapon, shooter)
            CASE PROJ_Projectile:
                FireProjectile(origin, direction, weapon, shooter)
            CASE PROJ_Hybrid:
                // Use hitscan for close, projectile for far
                FireHybrid(origin, direction, weapon, shooter)
        END SWITCH
    END FUNCTION
    
    // Instant hitscan raycast
    FUNCTION FireHitscan(origin: Vector3, direction: Vector3, weapon: WeaponInstance, shooter: CharacterInstance):
        // Raycast for hit detection
        hit = Physics.Raycast(origin, direction, maxDistance: weapon.FinalRange, layerMask: HittableLayers)
        
        IF hit.Success:
            ProcessHit(hit, weapon, shooter)
        END IF
        
        // Spawn tracer visual
        SpawnTracer(origin, hit.Success ? hit.Point : origin + direction * weapon.FinalRange)
    END FUNCTION
    
    // Physical projectile
    FUNCTION FireProjectile(origin: Vector3, direction: Vector3, weapon: WeaponInstance, shooter: CharacterInstance):
        // Get projectile from pool
        projectile = WeaponManager.projectilePool.Get()
        
        // Initialize projectile
        projectile.Position = origin
        projectile.Velocity = direction * GetBulletSpeed(weapon.BaseData.AmmoType)
        projectile.Weapon = weapon
        projectile.Shooter = shooter
        projectile.RemainingDistance = weapon.FinalRange
        projectile.IsActive = true
        
        // Add to active projectiles
        activeProjectiles.Add(projectile)
    END FUNCTION
    
    // Hybrid: hitscan close, projectile far
    FUNCTION FireHybrid(origin: Vector3, direction: Vector3, weapon: WeaponInstance, shooter: CharacterInstance):
        // First check close range with hitscan
        closeHit = Physics.Raycast(origin, direction, maxDistance: HITSCAN_MAX_DISTANCE, layerMask: HittableLayers)
        
        IF closeHit.Success:
            ProcessHit(closeHit, weapon, shooter)
            SpawnTracer(origin, closeHit.Point)
        ELSE:
            // Switch to projectile for longer range
            FireProjectile(origin + direction * HITSCAN_MAX_DISTANCE, direction, weapon, shooter)
        END IF
    END FUNCTION
    
    // Process a hit
    FUNCTION ProcessHit(hit: RaycastHit, weapon: WeaponInstance, shooter: CharacterInstance):
        // Check if hit character
        hitCharacter = hit.Collider.GetComponent<CharacterInstance>()
        
        IF hitCharacter != null:
            // Create hit info
            hitInfo = NEW HitInfo()
            hitInfo.Origin = shooter.Position
            hitInfo.HitPoint = hit.Point
            hitInfo.HitBone = GetBoneFromCollider(hit.Collider)
            hitInfo.PenetratedMaterial = null
            
            // Calculate and apply damage
            damageResult = DamageSystem.CalculateDamage(weapon, hitInfo)
            DamageSystem.ApplyDamage(hitCharacter.InstanceID, damageResult, shooter.InstanceID)
        ELSE:
            // Hit world geometry - check for penetration
            TryPenetration(hit, weapon, shooter)
        END IF
        
        // Spawn impact effect
        SpawnImpactEffect(hit.Point, hit.Normal, hit.Material)
    END FUNCTION
    
    // Try to penetrate material
    FUNCTION TryPenetration(hit: RaycastHit, weapon: WeaponInstance, shooter: CharacterInstance):
        material = GetMaterialPenetration(hit.Material)
        
        // Check if can penetrate
        penetrationChance = GetPenetrationChance(weapon.BaseData.AmmoType, material)
        
        IF Random() < penetrationChance:
            // Continue raycast from other side
            exitPoint = hit.Point + hit.Direction * 0.5  // Small offset
            
            penetratedHit = Physics.Raycast(
                exitPoint, 
                hit.Direction, 
                maxDistance: weapon.FinalRange - hit.Distance,
                layerMask: HittableLayers
            )
            
            IF penetratedHit.Success:
                // Create hit info with penetration
                hitInfo = NEW HitInfo()
                hitInfo.PenetratedMaterial = material
                
                ProcessHit(penetratedHit, weapon, shooter)
            END IF
            
            EMIT EVENT "DMG_PENETRATION" WITH (material, GetPenetrationDamageLoss(material))
        END IF
    END FUNCTION
    
    // Update active projectiles
    FUNCTION Update(deltaTime: Float):
        FOR EACH projectile IN activeProjectiles:
            IF NOT projectile.IsActive:
                CONTINUE
            END IF
            
            // Apply gravity (bullet drop)
            projectile.Velocity.y -= 9.81 * deltaTime * 0.1  // Reduced gravity for gameplay
            
            // Calculate movement this frame
            movement = projectile.Velocity * deltaTime
            
            // Check for hit
            hit = Physics.Raycast(projectile.Position, movement.Normalized(), movement.Length(), HittableLayers)
            
            IF hit.Success:
                ProcessHit(hit, projectile.Weapon, projectile.Shooter)
                ReturnProjectile(projectile)
            ELSE:
                // Move projectile
                projectile.Position += movement
                projectile.RemainingDistance -= movement.Length()
                
                // Check if exceeded range
                IF projectile.RemainingDistance <= 0:
                    ReturnProjectile(projectile)
                END IF
            END IF
        END FOR
    END FUNCTION
```

***

#### AttachmentSystem

**Purpose:** Manage weapon attachments and stat modifiers.

**Pseudocode:**

```
CLASS AttachmentSystem:
    
    // Equip attachment to weapon
    FUNCTION EquipAttachment(weapon: WeaponInstance, attachment: AttachmentData) -> Boolean:
        // Validate
        IF NOT WeaponManager.CanAttach(weapon, attachment):
            EMIT EVENT "ATT_INCOMPATIBLE" WITH (weapon.InstanceID, attachment.CodeName)
            RETURN false
        END IF
        
        // Add attachment
        weapon.Attachments[attachment.Slot] = attachment
        
        // Recalculate stats
        weapon.RecalculateStats()
        
        // Update visuals
        MountAttachmentVisual(weapon, attachment)
        
        EMIT EVENT "ATT_EQUIP" WITH (weapon.InstanceID, attachment.CodeName, attachment.Slot)
        
        RETURN true
    END FUNCTION
    
    // Remove attachment from weapon
    FUNCTION RemoveAttachment(weapon: WeaponInstance, slot: EAttachmentSlot) -> AttachmentData?:
        IF NOT weapon.Attachments.Contains(slot):
            RETURN null
        END IF
        
        attachment = weapon.Attachments[slot]
        weapon.Attachments.Remove(slot)
        
        // Recalculate stats
        weapon.RecalculateStats()
        
        // Update visuals
        UnmountAttachmentVisual(weapon, slot)
        
        EMIT EVENT "ATT_REMOVE" WITH (weapon.InstanceID, attachment.CodeName, slot)
        
        RETURN attachment
    END FUNCTION
    
    // Get all compatible attachments for a weapon
    FUNCTION GetCompatibleAttachments(weapon: WeaponInstance, slot: EAttachmentSlot) -> List<AttachmentData>:
        compatible = NEW List<AttachmentData>()
        
        FOR EACH attachment IN WeaponManager.attachmentDatabase.Values:
            IF attachment.Slot == slot:
                IF attachment.CompatibleWeapons.Contains(weapon.BaseData.Type):
                    compatible.Add(attachment)
                END IF
            END IF
        END FOR
        
        RETURN compatible
    END FUNCTION
    
    // Preview attachment stats (without equipping)
    FUNCTION PreviewStats(weapon: WeaponInstance, attachment: AttachmentData) -> StatPreview:
        preview = NEW StatPreview()
        
        // Calculate what stats would be with attachment
        oldAccuracy = weapon.FinalAccuracy
        oldRecoil = weapon.FinalRecoil
        oldRange = weapon.FinalRange
        oldADS = weapon.FinalADSSpeed
        oldMag = weapon.FinalMagazineSize
        
        newAccuracy = oldAccuracy * attachment.AccuracyModifier
        newRecoil = oldRecoil * attachment.RecoilModifier
        newRange = oldRange * attachment.RangeModifier
        newADS = oldADS * attachment.ADSSpeedModifier
        newMag = oldMag + attachment.MagazineModifier
        
        preview.AccuracyChange = newAccuracy - oldAccuracy
        preview.RecoilChange = newRecoil - oldRecoil
        preview.RangeChange = newRange - oldRange
        preview.ADSChange = newADS - oldADS
        preview.MagazineChange = newMag - oldMag
        
        RETURN preview
    END FUNCTION
```

***

### Network Synchronization

#### Replicated Properties

| Property               | Replicate To | Update Rate | Notes             |
| ---------------------- | ------------ | ----------- | ----------------- |
| **Equipped Weapon ID** | All          | On change   | For animations    |
| **Current Ammo**       | Owner only   | On change   | UI display        |
| **Reserve Ammo**       | Owner only   | On change   | UI display        |
| **Fire events**        | All          | Per shot    | For sound/visuals |
| **Attachment list**    | All          | On change   | Bitmask optimized |

#### Hit Validation

```
CLIENT-SIDE:
1. Player fires
2. Client predicts hit locally (immediate feedback)
3. Send fire event + hit info to server

SERVER-SIDE:
4. Validate fire timing
5. Re-run hitscan from client position
6. Check for cheating (impossible shots)
7. If valid: Apply damage, broadcast
8. If invalid: Reject, rollback client
```

***

### Performance Considerations

#### Memory Budget

| Asset             | Max Size    |
| ----------------- | ----------- |
| Weapon Prefabs    | 10 MB total |
| Attachment Meshes | 2 MB total  |
| Fire Sounds       | 5 MB total  |
| Impact Sounds     | 3 MB total  |

#### Object Pool Sizes

| Object           | Pool Size |
| ---------------- | --------- |
| Weapon Instances | 50        |
| Projectiles      | 200       |
| Muzzle Flash VFX | 20        |
| Bullet Casings   | 100       |
| Impact Effects   | 50        |

***

### TODO: Implementation Tasks

#### HIGH Priority 🔴

* [ ] Implement WeaponController fire system
* [ ] Create DamageSystem calculation
* [ ] Add hitscan raycast
* [ ] Implement reload system
* [ ] Create attachment slot system

#### MEDIUM Priority 🟡

* [ ] Add recoil pattern system
* [ ] Implement projectile simulation
* [ ] Create material penetration
* [ ] Add damage falloff
* [ ] Implement weapon pooling

#### LOW Priority 🟢

* [ ] Add gyro recoil control (mobile)
* [ ] Create weapon inspection
* [ ] Add firing sound variations
* [ ] Implement weapon skins
* [ ] Create firing range mode

***

### System Relationships

#### Dependency Diagram

```
                    ┌────────────────────┐
                    │   WEAPON SYSTEM    │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ CHARACTER       │  │ INVENTORY       │  │ UI              │
│ SYSTEM          │  │ SYSTEM          │  │ SYSTEM          │
│                 │  │                 │  │                 │
│ • Equip/Unequip │  │ • Weapon storage│  │ • Ammo counter  │
│ • Aim direction │  │ • Ammo reserve  │  │ • Crosshair     │
│ • Animation     │  │ • Attachments   │  │ • Hit markers   │
└─────────────────┘  └─────────────────┘  └─────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ AUDIO           │  │ CAMERA          │  │ NETWORKING      │
│ SYSTEM          │  │ SYSTEM          │  │ SYSTEM          │
│                 │  │                 │  │                 │
│ • Fire sounds   │  │ • Recoil kick   │  │ • Fire sync     │
│ • Reload sounds │  │ • Weapon sway   │  │ • Hit validation│
│ • Impact sounds │  │ • ADS zoom      │  │ • State sync    │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```
