# Weapon System - Technical Specification

**[← Previous: Character System](./CharacterSystem.md)** | **[Index](../README.md)** | **[Next: Inventory System →](./InventorySystem.md)**

---

## Overview

This document defines the technical implementation of the weapon system including enums, codenames, data structures, and implementation TODOs.

**Responsibilities:**
- Weapon spawning and pooling
- Damage calculation
- Recoil and ballistics
- Attachment system
- Weapon state management

---

## Enumerations

### EWeaponType
```
None = 0
AssaultRifle = 1
SubmachineGun = 2
Shotgun = 3
SniperRifle = 4
LightMachineGun = 5
Pistol = 6
Melee = 7
```

### EWeaponRarity
```
Common = 0         // White
Uncommon = 1       // Green
Rare = 2           // Blue
Epic = 3           // Purple
Legendary = 4      // Gold
```

### EFireMode
```
Single = 0         // Semi-automatic
Burst = 1          // 3-round burst
Auto = 2           // Full-automatic
BoltAction = 3     // Manual cycling
```

### EAttachmentSlot
```
None = 0
Optic = 1
Barrel = 2
Stock = 3
Magazine = 4
Underbarrel = 5
```

### ERecoilPattern
```
Vertical = 0       // Straight up
VerticalLeft = 1   // Up and left
VerticalRight = 2  // Up and right
Diagonal = 3       // Zigzag pattern
Random = 4         // Unpredictable
```

### EAmmoType
```
Pistol_9mm = 0
Rifle_556 = 1
Rifle_762 = 2
Shotgun_12gauge = 3
Sniper_762 = 4
Sniper_50cal = 5
```

---

## Code Names Reference

### Primary Weapons

**Assault Rifles:**
```
WPN_AR_AK47
WPN_AR_M4A1
WPN_AR_SCAR
WPN_AR_HK416
WPN_AR_AUG
```

**Submachine Guns:**
```
WPN_SMG_MP5
WPN_SMG_VECTOR
WPN_SMG_P90
WPN_SMG_UMP45
WPN_SMG_MP7
```

**Shotguns:**
```
WPN_SG_R870
WPN_SG_M590
WPN_SG_AA12
WPN_SG_SPAS12
WPN_SG_SAIGA
```

**Sniper Rifles:**
```
WPN_SR_M24
WPN_SR_AWP
WPN_SR_SVD
WPN_SR_M107
WPN_SR_VSS
```

**Light Machine Guns:**
```
WPN_LMG_M249
WPN_LMG_PKM
WPN_LMG_MG42
WPN_LMG_RPK
```

### Secondary Weapons

**Pistols:**
```
WPN_PISTOL_GLOCK
WPN_PISTOL_DEAGLE
WPN_PISTOL_USP
WPN_PISTOL_M1911
WPN_PISTOL_P226
WPN_PISTOL_REVOLVER
```

**Melee:**
```
WPN_MELEE_KNIFE
WPN_MELEE_AXE
WPN_MELEE_MACHETE
WPN_MELEE_BATON
```

### Attachments

**Optics:**
```
ATT_OPTIC_REDDOT
ATT_OPTIC_HOLO
ATT_OPTIC_ACOG
ATT_OPTIC_THERMAL
ATT_OPTIC_SNIPER
ATT_OPTIC_REFLEX
```

**Barrels:**
```
ATT_BARREL_SUPPRESSOR
ATT_BARREL_COMP
ATT_BARREL_EXTENDED
ATT_BARREL_HEAVY
ATT_BARREL_LIGHTWEIGHT
```

**Stocks:**
```
ATT_STOCK_TACTICAL
ATT_STOCK_LIGHT
ATT_STOCK_HEAVY
ATT_STOCK_SKELETON
```

**Magazines:**
```
ATT_MAG_EXTENDED
ATT_MAG_FAST
ATT_MAG_DRUM
ATT_MAG_TACTICAL
```

**Underbarrel:**
```
ATT_UNDER_FOREGRIP
ATT_UNDER_ANGLED
ATT_UNDER_LASER
ATT_UNDER_LIGHT
ATT_UNDER_BIPOD
```

---

## Data Structures

### WeaponData
```csharp
[System.Serializable]
public struct WeaponData
{
    public string CodeName;           // e.g., "WPN_AR_AK47"
    public string DisplayName;        // e.g., "AK-47"
    public EWeaponType Type;
    public EWeaponRarity Rarity;
    public EFireMode FireMode;
    public EAmmoType AmmoType;
    
    // Stats
    public int Damage;
    public int RPM;                   // Rounds per minute
    public int MagazineSize;
    public float Range;               // Effective range in meters
    public float ReloadTime;          // Seconds
    
    // Recoil
    public ERecoilPattern RecoilPattern;
    public float VerticalRecoil;
    public float HorizontalRecoil;
    
    // Attachments
    public int AttachmentSlots;       // Based on rarity
    public List<EAttachmentSlot> AvailableSlots;
    
    // Economy
    public int Value;                 // In-game currency value
    
    // Metadata
    public string PrefabPath;
    public string IconPath;
}
```

### AttachmentData
```csharp
[System.Serializable]
public struct AttachmentData
{
    public string CodeName;           // e.g., "ATT_OPTIC_REDDOT"
    public string DisplayName;
    public EAttachmentSlot Slot;
    public EWeaponRarity Rarity;
    
    // Effects (modifiers)
    public float AccuracyModifier;    // +/- percentage
    public float RangeModifier;
    public float RecoilModifier;
    public float ADSSpeedModifier;    // Aim down sights
    public float MobilityModifier;
    
    // Economy
    public int Value;
    
    // Compatibility
    public List<EWeaponType> CompatibleWeapons;
    
    // Metadata
    public string PrefabPath;
    public string IconPath;
}
```

### WeaponInstance
```csharp
public class WeaponInstance
{
    public string InstanceID;         // Unique instance identifier
    public WeaponData BaseData;
    public List<AttachmentData> Attachments;
    
    // Runtime state
    public int CurrentAmmo;
    public int ReserveAmmo;
    public float Durability;          // 0-100, for future degradation system
    
    // Calculated stats (base + attachments)
    public int FinalDamage;
    public float FinalAccuracy;
    public float FinalRecoil;
    public float FinalRange;
}
```

---

## System Architecture

### WeaponManager
**Responsibilities:**
- Weapon spawning and pooling
- Weapon registration and lookup
- Global weapon configuration

**TODO List:**
```csharp
// TODO(P0): Implement weapon object pooling
// TODO(P0): Create weapon spawn system
// TODO(P1): Add weapon database loader (JSON/ScriptableObject)
// TODO(P1): Implement weapon registry with codename lookup
// TODO(P2): Add weapon diagnostic tools
// TODO(P2): Create weapon inspector for testing
```

### WeaponController
**Responsibilities:**
- Player weapon handling
- Fire rate control
- Ammo management
- Recoil application

**TODO List:**
```csharp
// TODO(P0): Implement fire rate limiter
// TODO(P0): Add ammo consumption logic
// TODO(P0): Create reload system with animation
// TODO(P1): Implement recoil pattern system
// TODO(P1): Add weapon sway and bob
// TODO(P2): Implement weapon inspection feature
// TODO(P3): Add firing sound variations
```

### DamageSystem
**Responsibilities:**
- Damage calculation
- Armor penetration
- Hit registration
- Damage falloff

**TODO List:**
```csharp
// TODO(P0): Implement base damage calculation
// TODO(P0): Add armor damage absorption
// TODO(P0): Create headshot multiplier system
// TODO(P1): Implement distance-based damage falloff
// TODO(P1): Add penetration system for cover
// TODO(P2): Create damage indicator UI
// TODO(P2): Add kill feed system
```

### AttachmentSystem
**Responsibilities:**
- Attachment equipping
- Stat modification
- Visual attachment management

**TODO List:**
```csharp
// TODO(P0): Create attachment slot system
// TODO(P0): Implement stat modifier calculation
// TODO(P1): Add attachment visual mounting
// TODO(P1): Create attachment compatibility check
// TODO(P2): Implement attachment save/load
// TODO(P2): Add attachment preview system
// TODO(P3): Create attachment crafting system
```

---

## Ballistics System

### Projectile Types
```
Hitscan = 0        // Instant hit (close range)
Projectile = 1     // Physical projectile (long range)
Hybrid = 2         // Hitscan < 20m, Projectile > 20m
```

### Penetration System
```
Wood = 0           // Penetrable, low damage loss
ThinMetal = 1      // 50% penetration chance
Concrete = 2       // Non-penetrable
Flesh = 3          // Over-penetration (multi-kill)
```

**TODO List:**
```csharp
// TODO(P0): Implement hitscan raycast system
// TODO(P1): Add projectile physics for long range
// TODO(P1): Create hybrid ballistics (distance-based)
// TODO(P1): Implement material penetration system
// TODO(P2): Add bullet tracer visualization
// TODO(P2): Create impact particle effects
// TODO(P3): Implement bullet drop (minimal for gameplay)
```

---

## Recoil System

### Pattern Definition

```csharp
[System.Serializable]
public struct RecoilCurve
{
    public AnimationCurve VerticalCurve;
    public AnimationCurve HorizontalCurve;
    public float RecoverySpeed;
    public float MaxRecoilAngle;
}
```

**TODO List:**
```csharp
// TODO(P0): Create recoil pattern data for each weapon
// TODO(P0): Implement camera recoil application
// TODO(P1): Add player recoil compensation input
// TODO(P1): Create gyroscope recoil control (mobile)
// TODO(P2): Add haptic feedback for recoil
// TODO(P2): Implement recoil recovery animation
// TODO(P3): Create recoil pattern visualization tool
```

---

## Performance Considerations

### Object Pooling
```csharp
// TODO(P0): Pool weapon instances (max 50 concurrent)
// TODO(P0): Pool projectiles (max 200 in flight)
// TODO(P1): Pool muzzle flash VFX
// TODO(P1): Pool bullet casings (limit 100)
// TODO(P2): Implement pool cleanup on scene change
```

### Memory Budget
```
Weapon Prefabs: Max 10MB total
Attachment Meshes: Max 2MB total
Fire Sounds: Max 5MB total
Impact Sounds: Max 3MB total
```

### Network Optimization
```csharp
// TODO(P0): Implement weapon state synchronization
// TODO(P0): Add client-side prediction for firing
// TODO(P1): Create server-authoritative hit validation
// TODO(P1): Optimize attachment sync (send bitmask)
// TODO(P2): Add network interpolation for projectiles
```

---

## Testing & Debugging

### Debug Commands
```csharp
// TODO(P2): Add weapon.spawn <codename> command
// TODO(P2): Add weapon.giveAmmo <amount> command
// TODO(P2): Add weapon.showRecoil command
// TODO(P3): Add weapon.testDamage command
// TODO(P3): Create weapon stats inspector UI
```

### Unit Tests Required
```csharp
// TODO(P1): Test damage calculation with armor
// TODO(P1): Test ammo management (fire, reload)
// TODO(P1): Test attachment stat modifiers
// TODO(P2): Test recoil pattern application
// TODO(P2): Test weapon pooling create/destroy
```

---

## Integration Points

### With Character System
- Weapon equipping/unequipping
- Operator weapon restrictions
- Animation triggers

### With Inventory System
- Weapon storage
- Ammo management
- Attachment storage

### With UI System
- Weapon HUD display
- Ammo counter
- Reticle/crosshair

### With Audio System
- Fire sounds
- Reload sounds
- Impact sounds

---

## Future Enhancements

```csharp
// TODO(P3): Weapon skin system
// TODO(P3): Weapon degradation/durability
// TODO(P3): Weapon jamming mechanic (rare)
// TODO(P3): Weapon kill tracker stat
// TODO(P3): Custom weapon loadout presets
// TODO(P3): Firing range practice mode
```

---

**[← Previous: Character System](./CharacterSystem.md)** | **[Index](../README.md)** | **[Next: Inventory System →](./InventorySystem.md)**
