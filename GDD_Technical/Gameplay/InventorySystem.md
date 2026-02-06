# Inventory System - Technical Specification

**[← Previous: Weapon System](./WeaponSystem.md)** | **[Index](../README.md)**

---

## Overview

This document defines the technical implementation of the grid-based inventory system including enums, codenames, data structures, and implementation TODOs.

**Responsibilities:**
- Grid-based item management
- Secure container handling
- Weight & encumbrance calculation
- Item stacking and rotation
- Stash persistence

---

## Enumerations

### EItemType
```
None = 0
Weapon = 1
Attachment = 2
Armor = 3
Backpack = 4
Medical = 5
Consumable = 6
Tactical = 7
Key = 8
CraftingMaterial = 9
Quest = 10
Currency = 11
```

### EItemRarity
```
Common = 0         // White
Uncommon = 1       // Green
Rare = 2           // Blue
Epic = 3           // Purple
Legendary = 4      // Gold
```

### EArmorType
```
Helmet = 0
BodyArmor = 1
Backpack = 2
```

### EContainerType
```
Inventory = 0          // Main inventory
SecureContainer = 1    // Safe from death
Stash = 2              // Permanent storage
Loot = 3               // World container
```

### EItemRotation
```
Rotation0 = 0
Rotation90 = 1
Rotation180 = 2
Rotation270 = 3
```

---

## Code Names Reference

### Armor Items

**Helmets:**
```
ITEM_HELM_LIGHT
ITEM_HELM_MEDIUM
ITEM_HELM_HEAVY
ITEM_HELM_TACTICAL
ITEM_HELM_SPEC
```

**Body Armor:**
```
ITEM_VEST_LIGHT
ITEM_VEST_MEDIUM
ITEM_VEST_HEAVY
ITEM_VEST_TACTICAL
ITEM_VEST_CARRIER
```

**Backpacks:**
```
ITEM_BAG_SMALL
ITEM_BAG_MEDIUM
ITEM_BAG_LARGE
ITEM_BAG_TACTICAL
ITEM_BAG_ASSAULT
```

### Medical Items
```
ITEM_MED_BANDAGE
ITEM_MED_MEDKIT
ITEM_MED_STIM
ITEM_MED_SURGERY
ITEM_MED_PAINKILLER
ITEM_MED_BLOODBAG
ITEM_MED_FIRSTAID
```

### Consumables
```
ITEM_CONS_ENERGY
ITEM_CONS_ADRENALINE
ITEM_CONS_RATION
ITEM_CONS_WATER
ITEM_CONS_PROTEIN
```

### Tactical Equipment
```
ITEM_TAC_SENSOR
ITEM_TAC_CLAYMORE
ITEM_TAC_COVER
ITEM_TAC_BARRICADE
ITEM_TAC_C4
ITEM_TAC_BEACON
```

### Keys
```
ITEM_KEY_LOOTROOM
ITEM_KEY_SAFE
ITEM_KEY_SUPPLY
ITEM_KEY_BUNKER
ITEM_KEY_OFFICE
ITEM_KEY_MASTER
```

### Crafting Materials
```
ITEM_CRAFT_SCRAP
ITEM_CRAFT_ELECTRONICS
ITEM_CRAFT_RARECOMP
ITEM_CRAFT_LEGENDARY
ITEM_CRAFT_CIRCUITS
ITEM_CRAFT_POLYMER
ITEM_CRAFT_TOOLS
```

### Grenades
```
ITEM_GREN_FRAG
ITEM_GREN_FLASH
ITEM_GREN_SMOKE
ITEM_GREN_EMP
ITEM_GREN_INCENDIARY
ITEM_GREN_STUN
```

---

## Data Structures

### GridPosition
```csharp
[System.Serializable]
public struct GridPosition
{
    public int X;
    public int Y;
    
    public GridPosition(int x, int y)
    {
        X = x;
        Y = y;
    }
}
```

### GridSize
```csharp
[System.Serializable]
public struct GridSize
{
    public int Width;   // Horizontal cells
    public int Height;  // Vertical cells
    
    public int TotalCells => Width * Height;
}
```

### ItemData
```csharp
[System.Serializable]
public struct ItemData
{
    public string CodeName;         // e.g., "ITEM_MED_BANDAGE"
    public string DisplayName;
    public EItemType Type;
    public EItemRarity Rarity;
    
    // Grid properties
    public GridSize Size;           // How many cells it occupies
    public bool Rotatable;          // Can be rotated?
    public int MaxStackSize;        // 1 = non-stackable
    
    // Weight
    public float WeightKg;          // Weight per unit
    
    // Value
    public int SellValue;           // Vendor price
    public int BuyValue;            // Purchase price
    
    // Metadata
    public string IconPath;
    public string PrefabPath;
    public string Description;
}
```

### ItemInstance
```csharp
public class ItemInstance
{
    public string InstanceID;           // Unique identifier
    public ItemData BaseData;
    
    // Grid placement
    public GridPosition Position;
    public EItemRotation Rotation;
    public EContainerType Container;
    
    // Stack info
    public int StackCount;              // Current stack amount
    
    // Durability (for armor, weapons)
    public float Durability;            // 0-100
    
    // Special flags
    public bool IsQuestItem;
    public bool IsFavorited;            // Can't accidentally sell
}
```

### InventoryContainer
```csharp
public class InventoryContainer
{
    public EContainerType Type;
    public GridSize GridSize;
    public List<ItemInstance> Items;
    
    // Capacity
    public int MaxWeight;               // Kg
    public float CurrentWeight;
    
    // Grid occupancy
    private bool[,] OccupiedCells;     // 2D array of occupied cells
}
```

---

## System Architecture

### InventoryManager
**Responsibilities:**
- Manage player inventories
- Handle item transfers
- Validate item placement
- Save/load inventory state

**TODO List:**
```csharp
// TODO(P0): Implement inventory container creation
// TODO(P0): Add item placement validation (grid check)
// TODO(P0): Create item add/remove methods
// TODO(P1): Implement Tetris-style rotation
// TODO(P1): Add auto-sort functionality
// TODO(P1): Create quick-slot system
// TODO(P2): Implement item split/stack merge
// TODO(P2): Add item search/filter
// TODO(P3): Create inventory presets (loadouts)
```

### GridSystem
**Responsibilities:**
- Grid cell management
- Collision detection
- Item fitting algorithm
- Visual grid representation

**TODO List:**
```csharp
// TODO(P0): Create 2D grid representation
// TODO(P0): Implement cell occupancy check
// TODO(P0): Add item bounds checking
// TODO(P1): Create auto-fit algorithm (find first available spot)
// TODO(P1): Implement item rotation logic
// TODO(P2): Add grid visualization (debug)
// TODO(P2): Create optimal packing algorithm
// TODO(P3): Implement grid resize (backpack upgrade)
```

### SecureContainer
**Responsibilities:**
- Manage secure (safe) container
- Enforce container rules
- Prevent exploits

**TODO List:**
```csharp
// TODO(P0): Implement secure container with fixed size (2x2)
// TODO(P0): Add "can only insert, not extract" during raid
// TODO(P1): Create container upgrade system (2x3 for premium)
// TODO(P1): Implement container unlock conditions
// TODO(P2): Add container contents visualization
// TODO(P2): Create container analytics tracking
```

### Stash System
**Responsibilities:**
- Persistent storage
- Database save/load
- Stash expansion

**TODO List:**
```csharp
// TODO(P0): Implement stash database schema
// TODO(P0): Create save/load functionality
// TODO(P0): Add stash size limits
// TODO(P1): Implement stash expansion system (purchase)
// TODO(P1): Add stash organization (tabs/categories)
// TODO(P2): Create stash search functionality
// TODO(P2): Implement stash value calculator
// TODO(P3): Add stash statistics (total value, items)
```

---

## Weight & Encumbrance System

### Weight Thresholds
```
Light = 0          // 0-15 kg: Normal movement
Medium = 1         // 15-25 kg: 90% speed, +20% stamina drain
Heavy = 2          // 25-35 kg: 75% speed, +50% stamina drain
Overweight = 3     // 35+ kg: 60% speed, +100% stamina drain
```

**TODO List:**
```csharp
// TODO(P0): Implement total weight calculation
// TODO(P0): Add movement speed modifier based on weight
// TODO(P1): Create stamina drain multiplier
// TODO(P1): Add weight UI indicator
// TODO(P2): Implement weight-based footstep sounds
// TODO(P2): Add haptic feedback for overweight
```

---

## Item Stacking

### Stack Rules
```csharp
public struct StackRules
{
    public static bool CanStack(ItemInstance item1, ItemInstance item2)
    {
        // Items must have same CodeName
        // Stack count must be < MaxStackSize
        // Cannot stack damaged items (unless full durability)
        // TODO(P1): Implement stack validation logic
        return false;
    }
}
```

**TODO List:**
```csharp
// TODO(P0): Implement automatic stacking on pickup
// TODO(P1): Add manual stack split UI
// TODO(P1): Create stack merge functionality
// TODO(P2): Implement stack swap (exchange quantities)
// TODO(P3): Add "stack all similar items" button
```

---

## Loot Containers

### World Container Types
```
WoodenCrate = 0
MetalLocker = 1
WeaponRack = 2
Safe = 3
SupplyDrop = 4
DeadPlayer = 5
```

**TODO List:**
```csharp
// TODO(P0): Implement loot container spawning
// TODO(P0): Create loot generation based on container type
// TODO(P0): Add container open/close interaction
// TODO(P1): Implement locked container system (needs key)
// TODO(P1): Add container search time (lockpicking)
// TODO(P2): Create container loot rarity distribution
// TODO(P2): Implement dynamic loot scaling
// TODO(P3): Add container respawn system
```

---

## UI Systems

### Drag & Drop
**TODO List:**
```csharp
// TODO(P0): Implement item drag-and-drop
// TODO(P0): Add drop validation (can place here?)
// TODO(P1): Create visual feedback (green/red highlight)
// TODO(P1): Implement drag preview (ghost icon)
// TODO(P2): Add snap-to-grid functionality
// TODO(P2): Create drag cancel (ESC or outside grid)
```

### Context Menus
**TODO List:**
```csharp
// TODO(P1): Create right-click context menu
// TODO(P1): Add "Use", "Drop", "Inspect" options
// TODO(P1): Implement "Mark as Favorite" toggle
// TODO(P2): Add "Move to Stash" quick action
// TODO(P2): Create "Discard All" for stacks
```

### Quick Access
**TODO List:**
```csharp
// TODO(P1): Implement quick-slot bar (1-5 keys)
// TODO(P1): Add quick-heal keybind
// TODO(P2): Create consumable priority system
// TODO(P2): Implement auto-reload from inventory
```

---

## Performance Considerations

### Memory Budget
```
Item Icons: Max 50KB per icon
Item Prefabs: Max 500KB per item
Total Items in Scene: Max 500 concurrent
```

### Optimization
```csharp
// TODO(P1): Implement item icon atlas
// TODO(P1): Add item pooling system
// TODO(P2): Create lazy loading for stash
// TODO(P2): Implement LOD for dropped items
// TODO(P3): Add culling for distant items
```

### Network Sync
```csharp
// TODO(P0): Implement inventory state sync
// TODO(P0): Add container lock/unlock sync
// TODO(P1): Create delta compression for inventory changes
// TODO(P1): Implement server-side validation
// TODO(P2): Add rollback for invalid moves
```

---

## Data Persistence

### Save Format
```json
{
  "playerId": "uuid",
  "stash": {
    "gridSize": { "width": 10, "height": 20 },
    "items": [
      {
        "instanceId": "uuid",
        "codeName": "ITEM_MED_BANDAGE",
        "position": { "x": 0, "y": 0 },
        "rotation": 0,
        "stackCount": 5,
        "durability": 100
      }
    ]
  },
  "secureContainer": { ... }
}
```

**TODO List:**
```csharp
// TODO(P0): Implement JSON serialization
// TODO(P0): Create database schema (PostgreSQL)
// TODO(P0): Add save on inventory change
// TODO(P1): Implement backup/restore system
// TODO(P2): Add cloud save synchronization
// TODO(P3): Create inventory import/export
```

---

## Testing & Debugging

### Debug Commands
```csharp
// TODO(P2): Add inventory.clear command
// TODO(P2): Add inventory.giveItem <codename> <count>
// TODO(P2): Add inventory.setWeight <kg>
// TODO(P3): Add inventory.export command (JSON)
// TODO(P3): Create visual debug overlay
```

### Unit Tests Required
```csharp
// TODO(P1): Test item placement validation
// TODO(P1): Test weight calculation
// TODO(P1): Test stack merge/split
// TODO(P2): Test rotation logic
// TODO(P2): Test save/load integrity
```

---

## Integration Points

### With Weapon System
- Weapon storage in inventory
- Ammo management
- Attachment storage

### With Character System
- Equipped armor calculation
- Backpack capacity

### With Loot System
- Item pickup
- Container opening

### With Trading System
- Item transfer between players
- Marketplace listing

---

## Future Enhancements

```csharp
// TODO(P3): Implement auto-loot filter (custom rules)
// TODO(P3): Add item comparison tooltip
// TODO(P3): Create inventory value calculator
// TODO(P3): Implement item rental system
// TODO(P3): Add item insurance tracking
// TODO(P3): Create item history log
```

---

**[← Previous: Weapon System](./WeaponSystem.md)** | **[Index](../README.md)**
