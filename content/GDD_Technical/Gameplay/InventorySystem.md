---
title: "Inventory System - Technical Design Sutureument"
type: docs
---

## Related Sutureuments

| Sutureument             | Relationship           | Link                                                                 |
| :------------------- | :--------------------- | :------------------------------------------------------------------- |
| **Items Design**     | High-level item design | [GDD_HighLevel/Combat/Items.md](../../GDD_HighLevel/Combat/Items.md) |
| **Weapon System**    | Weapon storage         | [WeaponSystem.md](./WeaponSystem.md)                                 |
| **Character System** | Equipped items         | [CharacterSystem.md](./CharacterSystem.md)                           |
| **UI System**        | Inventory UI           | [../Systems/UISystem.md](../Systems/UISystem.md)                     |
| **Trading System**   | Item exchange          | [../Systems/TradingSystem.md](../Systems/TradingSystem.md)           |

---

## Overview

### Purpose

The **Inventory System** manages all item storage, retrieval, and manipulation in a grid-based (Tetris-style) format similar to Escape from Tarkov.

### Core Functions

| Function            | Description                                  |
| :------------------ | :------------------------------------------- |
| **Grid Management** | 2D cell-based item placement                 |
| **Item Stacking**   | Combine similar items into stacks            |
| **Weight Tracking** | Calculate encumbrance and movement penalties |
| **Rotation**        | Rotate items to fit available space          |
| **Persistence**     | Save/load inventory to database              |
| **Secure Storage**  | Protected containers surviving death         |

### Design Goals

```
1. INTUITIVE - Drag-and-drop feels natural
2. VISUAL - Items visible with distinct icons
3. STRATEGIC - Space management adds depth
4. PERSISTENT - Stash survives between raids
5. PROTECTED - Secure container for valuable items
```

---

## System Architecture

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        INVENTORY SYSTEM                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │  INVENTORY   │    │    GRID      │    │   STASH      │          │
│  │  MANAGER     │───▶│   SYSTEM     │───▶│   SYSTEM     │          │
│  │              │    │              │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ Item         │    │ Collision    │    │ Database     │          │
│  │ Operations   │    │ Detection    │    │ Persistence  │          │
│  │ Add/Remove   │    │ Fitting      │    │ Save/Load    │          │
│  │ Move/Rotate  │    │ Auto-sort    │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Core Components

| Component                | Responsibility             | Dependencies         |
| :----------------------- | :------------------------- | :------------------- |
| **InventoryManager**     | Central item handling      | GridSystem, Database |
| **GridSystem**           | Cell management, collision | None                 |
| **ContainerManager**     | Container types            | InventoryManager     |
| **StashSystem**          | Persistent storage         | Database             |
| **WeightSystem**         | Encumbrance calculation    | CharacterSystem      |
| **LootContainerHandler** | World containers           | MapSystem            |

---

## Enums & Types

### EItemType
Item category classification.

| Code Name             | Display Name      | Stackable | Max Stack | Weight Range | Description                |
| :-------------------- | :---------------- | :-------- | :-------- | :----------- | :------------------------- |
| `IT_None`             | None              | N/A       | N/A       | N/A          | Invalid/undefined item     |
| `IT_Weapon`           | Weapon            | No        | 1         | 2-8 kg       | Firearms and melee weapons |
| `IT_Attachment`       | Attachment        | No        | 1         | 0.1-0.5 kg   | Weapon modifications       |
| `IT_Armor`            | Armor             | No        | 1         | 1-5 kg       | Protective gear            |
| `IT_Backpack`         | Backpack          | No        | 1         | 1-3 kg       | Storage expansion          |
| `IT_Medical`          | Medical           | Yes       | 10        | 0.1-0.5 kg   | Healing items              |
| `IT_Consumable`       | Consumable        | Yes       | 20        | 0.1-0.3 kg   | Food, drinks, buffs        |
| `IT_Tactical`         | Tactical          | Yes       | 5         | 0.2-1 kg     | Grenades, gadgets          |
| `IT_Key`              | Key               | Yes       | 10        | 0.01 kg      | Access keys                |
| `IT_CraftingMaterial` | Crafting Material | Yes       | 50        | 0.1-0.5 kg   | Crafting components        |
| `IT_Quest`            | Quest             | No        | 1         | 0.1 kg       | Quest objectives           |
| `IT_Currency`         | Currency          | Yes       | 999999    | 0 kg         | In-game currencies         |

---

### EItemRarity
Item rarity tier.

| Code Name      | Display Name | Color  | Drop Rate | Sell Mult | Description       |
| :------------- | :----------- | :----- | :-------- | :-------- | :---------------- |
| `IR_Common`    | Common       | White  | 50%       | 1.0×      | Basic items       |
| `IR_Uncommon`  | Uncommon     | Green  | 30%       | 1.5×      | Slightly improved |
| `IR_Rare`      | Rare         | Blue   | 15%       | 3.0×      | Good quality      |
| `IR_Epic`      | Epic         | Purple | 4%        | 6.0×      | High quality      |
| `IR_Legendary` | Legendary    | Gold   | 1%        | 15.0×     | Best in slot      |

---

### EArmorType
Armor slot classification.

| Code Name      | Display Name | Slot  | Protection Zone | Durability Range |
| :------------- | :----------- | :---- | :-------------- | :--------------- |
| `AT_Helmet`    | Helmet       | Head  | Head only       | 20-50            |
| `AT_BodyArmor` | Body Armor   | Torso | Chest, Stomach  | 30-80            |
| `AT_Backpack`  | Backpack     | Back  | None            | N/A              |

---

### EContainerType
Inventory container classification.

| Code Name            | Display Name     | Grid Size  | Persistent | Safe on Death | Description        |
| :------------------- | :--------------- | :--------- | :--------- | :------------ | :----------------- |
| `CT_Inventory`       | Inventory        | Variable   | Per-raid   | No            | Main inventory bag |
| `CT_SecureContainer` | Secure Container | 2×2 to 3×3 | Always     | Yes           | Safe from death    |
| `CT_Stash`           | Stash            | 10×20+     | Always     | Yes           | Permanent storage  |
| `CT_Loot`            | Loot             | Variable   | Per-raid   | No            | World container    |
| `CT_Trader`          | Trader           | Variable   | Always     | N/A           | NPC shop inventory |

---

### EItemRotation
Grid rotation state.

| Code Name | Display Name | Degrees | Width/Height | Description         |
| :-------- | :----------- | :------ | :----------- | :------------------ |
| `ROT_0`   | Normal       | 0°      | Original     | Default orientation |
| `ROT_90`  | Rotated 90   | 90°     | Swapped      | 90° clockwise       |
| `ROT_180` | Rotated 180  | 180°    | Original     | Upside down         |
| `ROT_270` | Rotated 270  | 270°    | Swapped      | 270° clockwise      |

---

### EEncumbranceLevel
Weight encumbrance tier.

| Code Name       | Display Name | Weight Range | Speed Mult | Stamina Drain | Description         |
| :-------------- | :----------- | :----------- | :--------- | :------------ | :------------------ |
| `EL_Light`      | Light        | 0-15 kg      | 100%       | 1.0×          | Normal movement     |
| `EL_Medium`     | Medium       | 15-25 kg     | 90%        | 1.2×          | Slightly encumbered |
| `EL_Heavy`      | Heavy        | 25-35 kg     | 75%        | 1.5×          | Encumbered          |
| `EL_Overweight` | Overweight   | 35+ kg       | 60%        | 2.0×          | Severely encumbered |

---

### ELootContainerType
World loot container classification.

| Code Name         | Display Name | Search Time | Lock Type | Loot Quality | Description      |
| :---------------- | :----------- | :---------- | :-------- | :----------- | :--------------- |
| `LCT_WoodenCrate` | Wooden Crate | 2s          | None      | Common       | Basic supplies   |
| `LCT_MetalLocker` | Metal Locker | 3s          | None      | Uncommon     | Military gear    |
| `LCT_WeaponRack`  | Weapon Rack  | 4s          | None      | Rare         | Weapons only     |
| `LCT_Safe`        | Safe         | 5s          | Key/Code  | Epic         | Valuables        |
| `LCT_SupplyDrop`  | Supply Drop  | 3s          | None      | Epic+        | Airdrop loot     |
| `LCT_DeadPlayer`  | Dead Player  | 1s          | None      | Variable     | Player inventory |

---

## Code Names

### Inventory Events

| Code Name         | Trigger      | Parameters                      | Description                 |
| :---------------- | :----------- | :------------------------------ | :-------------------------- |
| `INV_ITEM_ADD`    | Item added   | ItemID, ContainerType, Position | Item placed in inventory    |
| `INV_ITEM_REMOVE` | Item removed | ItemID, ContainerType, Reason   | Item removed from inventory |
| `INV_ITEM_MOVE`   | Item moved   | ItemID, FromPos, ToPos          | Item repositioned           |
| `INV_ITEM_ROTATE` | Item rotated | ItemID, Rotation                | Item orientation changed    |
| `INV_ITEM_USE`    | Item used    | ItemID, Effect                  | Consumable/medical used     |

### Stack Events

| Code Name     | Trigger         | Parameters                 | Description              |
| :------------ | :-------------- | :------------------------- | :----------------------- |
| `STACK_MERGE` | Stacks combined | ItemID, FromStack, ToStack | Items stacked together   |
| `STACK_SPLIT` | Stack divided   | ItemID, Amount, NewStackID | Stack split into parts   |
| `STACK_FULL`  | Stack maxed     | ItemID, Overflow           | Cannot add more to stack |

### Container Events

| Code Name     | Trigger            | Parameters                 | Description                |
| :------------ | :----------------- | :------------------------- | :------------------------- |
| `CONT_OPEN`   | Container opened   | ContainerID, ContainerType | Container UI opened        |
| `CONT_CLOSE`  | Container closed   | ContainerID                | Container UI closed        |
| `CONT_LOOT`   | Loot taken         | ContainerID, ItemID        | Item looted from container |
| `CONT_LOCKED` | Lock encounter     | ContainerID, LockType      | Locked container found     |
| `CONT_UNLOCK` | Container unlocked | ContainerID, KeyUsed       | Container opened with key  |

### Weight Events

| Code Name           | Trigger              | Parameters               | Description              |
| :------------------ | :------------------- | :----------------------- | :----------------------- |
| `WEIGHT_THRESHOLD`  | Weight level changed | OldLevel, NewLevel       | Encumbrance tier changed |
| `WEIGHT_OVERWEIGHT` | Max weight exceeded  | CurrentWeight, MaxWeight | Cannot add more items    |
| `WEIGHT_UPDATE`     | Weight recalculated  | TotalWeight              | Total weight changed     |

### Stash Events

| Code Name      | Trigger        | Parameters          | Description                   |
| :------------- | :------------- | :------------------ | :---------------------------- |
| `STASH_SAVE`   | Stash saved    | PlayerID, ItemCount | Stash persisted to database   |
| `STASH_LOAD`   | Stash loaded   | PlayerID, ItemCount | Stash retrieved from database |
| `STASH_EXPAND` | Stash upgraded | OldSize, NewSize    | Stash capacity increased      |
| `STASH_FULL`   | Stash full     | AttemptedItem       | Cannot store more items       |

---

## Data Structures

### GridPosition

**Purpose:** Represents a cell position in the inventory grid.

```
STRUCT GridPosition:
    X: Integer          // Horizontal cell index (0-based)
    Y: Integer          // Vertical cell index (0-based)
    
    FUNCTION Equals(other: GridPosition) -> Boolean:
        RETURN X == other.X AND Y == other.Y
    END FUNCTION
```

### GridSize

**Purpose:** Defines dimensions of a grid or item.

```
STRUCT GridSize:
    Width: Integer      // Number of horizontal cells
    Height: Integer     // Number of vertical cells
    
    FUNCTION TotalCells() -> Integer:
        RETURN Width * Height
    END FUNCTION
    
    FUNCTION Swapped() -> GridSize:
        // For rotation
        RETURN GridSize(Height, Width)
    END FUNCTION
```

### ItemData

**Purpose:** Static item definition (read from database/config).

```
STRUCT ItemData:
    // Identification
    CodeName: String                // e.g., "ITEM_MED_BANDAGE"
    DisplayName: String             // Localized name
    Description: String             // Item description
    
    // Classification
    Type: EItemType                 // Category
    Rarity: EItemRarity            // Rarity tier
    
    // Grid properties
    Size: GridSize                  // How many cells it occupies
    Rotatable: Boolean              // Can be rotated?
    MaxStackSize: Integer           // 1 = non-stackable
    
    // Weight
    WeightKg: Float                 // Weight per unit
    
    // Value
    SellValue: Integer              // Vendor sell price
    BuyValue: Integer               // Vendor buy price
    
    // Assets
    IconPath: String                // UI icon
    PrefabPath: String              // 3D model
```

### ItemInstance

**Purpose:** Runtime instance of an item in the world/inventory.

```
CLASS ItemInstance:
    // Unique identification
    InstanceID: String              // UUID for this specific item
    BaseData: ItemData              // Reference to static data
    
    // Grid placement
    Position: GridPosition          // Current grid position
    Rotation: EItemRotation         // Current rotation
    Container: EContainerType       // Which container it's in
    
    // Stack info
    StackCount: Integer             // Current stack amount (1 if non-stackable)
    
    // Durability (for armor, weapons)
    Durability: Float               // 0-100 percentage
    MaxDurability: Float            // Maximum durability value
    
    // Special flags
    IsQuestItem: Boolean            // Cannot be dropped/sold
    IsFavorited: Boolean            // Protected from accidental sell
    IsInsured: Boolean              // Will be returned via insurance
    
    // Computed properties
    FUNCTION GetTotalWeight() -> Float:
        RETURN BaseData.WeightKg * StackCount
    END FUNCTION
    
    FUNCTION GetEffectiveSize() -> GridSize:
        IF Rotation == ROT_90 OR Rotation == ROT_270:
            RETURN BaseData.Size.Swapped()
        END IF
        RETURN BaseData.Size
    END FUNCTION
    
    FUNCTION CanStackWith(other: ItemInstance) -> Boolean:
        RETURN BaseData.CodeName == other.BaseData.CodeName
           AND StackCount < BaseData.MaxStackSize
           AND Durability == MaxDurability  // Only pristine items stack
    END FUNCTION
```

### InventoryContainer

**Purpose:** Represents a container that holds items (inventory, stash, etc.)

```
CLASS InventoryContainer:
    // Container properties
    Type: EContainerType
    GridSize: GridSize
    Items: List<ItemInstance>
    
    // Capacity limits
    MaxWeight: Float                // Maximum weight in kg
    CurrentWeight: Float            // Current total weight
    
    // Grid state
    OccupiedCells: Boolean[,]       // 2D array tracking occupied cells
    
    // Initialize empty container
    FUNCTION Initialize(size: GridSize):
        GridSize = size
        OccupiedCells = NEW Boolean[size.Width, size.Height]
        Items = NEW List<ItemInstance>()
        CurrentWeight = 0
    END FUNCTION
    
    // Check if position is valid and unoccupied
    FUNCTION CanPlaceAt(item: ItemInstance, position: GridPosition) -> Boolean:
        itemSize = item.GetEffectiveSize()
        
        // Check bounds
        IF position.X + itemSize.Width > GridSize.Width:
            RETURN false
        END IF
        IF position.Y + itemSize.Height > GridSize.Height:
            RETURN false
        END IF
        
        // Check each cell
        FOR x FROM position.X TO position.X + itemSize.Width - 1:
            FOR y FROM position.Y TO position.Y + itemSize.Height - 1:
                IF OccupiedCells[x, y] == true:
                    RETURN false
                END IF
            END FOR
        END FOR
        
        // Check weight limit
        IF CurrentWeight + item.GetTotalWeight() > MaxWeight:
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    // Mark cells as occupied/unoccupied
    FUNCTION SetCellsOccupied(position: GridPosition, size: GridSize, occupied: Boolean):
        FOR x FROM position.X TO position.X + size.Width - 1:
            FOR y FROM position.Y TO position.Y + size.Height - 1:
                OccupiedCells[x, y] = occupied
            END FOR
        END FOR
    END FUNCTION
```

---

## Core Classes

### InventoryManager

**Purpose:** Central manager for all inventory operations.

**Pseudocode:**
```
CLASS InventoryManager:
    
    // Singleton instance
    STATIC instance: InventoryManager
    
    // Player containers
    playerInventory: InventoryContainer
    secureContainer: InventoryContainer
    stash: InventoryContainer
    equippedItems: Map<EquipSlot, ItemInstance>
    
    // Open world containers
    openLootContainers: List<LootContainer>
    
    // Initialize player inventory
    FUNCTION InitializePlayerInventory(backpackSize: GridSize):
        playerInventory = NEW InventoryContainer()
        playerInventory.Initialize(backpackSize)
        playerInventory.Type = CT_Inventory
        playerInventory.MaxWeight = 35.0  // Default max weight
        
        secureContainer = NEW InventoryContainer()
        secureContainer.Initialize(GridSize(2, 2))  // 2x2 default
        secureContainer.Type = CT_SecureContainer
        secureContainer.MaxWeight = 999  // No weight limit
    END FUNCTION
    
    // Add item to container
    FUNCTION AddItem(container: InventoryContainer, item: ItemInstance, position: GridPosition) -> Boolean:
        // Validate placement
        IF NOT container.CanPlaceAt(item, position):
            EMIT EVENT "INV_ITEM_ADD_FAILED" WITH (item.InstanceID, "Invalid position")
            RETURN false
        END IF
        
        // Try to stack first
        IF item.BaseData.MaxStackSize > 1:
            existingStack = FindStackableItem(container, item)
            IF existingStack != null:
                merged = MergeStacks(existingStack, item)
                IF merged:
                    EMIT EVENT "STACK_MERGE"
                    RETURN true
                END IF
            END IF
        END IF
        
        // Place item
        item.Position = position
        item.Container = container.Type
        container.Items.Add(item)
        container.SetCellsOccupied(position, item.GetEffectiveSize(), true)
        container.CurrentWeight += item.GetTotalWeight()
        
        // Update encumbrance
        UpdateEncumbrance()
        
        EMIT EVENT "INV_ITEM_ADD" WITH (item.InstanceID, container.Type, position)
        RETURN true
    END FUNCTION
    
    // Remove item from container
    FUNCTION RemoveItem(container: InventoryContainer, item: ItemInstance, reason: String) -> Boolean:
        IF NOT container.Items.Contains(item):
            RETURN false
        END IF
        
        // Clear occupied cells
        container.SetCellsOccupied(item.Position, item.GetEffectiveSize(), false)
        
        // Remove from list
        container.Items.Remove(item)
        container.CurrentWeight -= item.GetTotalWeight()
        
        // Update encumbrance
        UpdateEncumbrance()
        
        EMIT EVENT "INV_ITEM_REMOVE" WITH (item.InstanceID, container.Type, reason)
        RETURN true
    END FUNCTION
    
    // Move item within or between containers
    FUNCTION MoveItem(item: ItemInstance, toContainer: InventoryContainer, toPosition: GridPosition) -> Boolean:
        fromContainer = GetContainerForItem(item)
        
        // Temporarily remove from old position
        RemoveItem(fromContainer, item, "Moving")
        
        // Try to add to new position
        success = AddItem(toContainer, item, toPosition)
        
        IF NOT success:
            // Rollback - put back in original position
            AddItem(fromContainer, item, item.Position)
            RETURN false
        END IF
        
        EMIT EVENT "INV_ITEM_MOVE" WITH (item.InstanceID, fromContainer.Type, toContainer.Type)
        RETURN true
    END FUNCTION
    
    // Rotate item
    FUNCTION RotateItem(item: ItemInstance) -> Boolean:
        container = GetContainerForItem(item)
        oldRotation = item.Rotation
        
        // Calculate new rotation
        newRotation = GetNextRotation(oldRotation)
        item.Rotation = newRotation
        
        // Check if new orientation fits
        IF NOT container.CanPlaceAt(item, item.Position):
            // Revert rotation
            item.Rotation = oldRotation
            RETURN false
        END IF
        
        // Update occupied cells
        container.SetCellsOccupied(item.Position, item.GetEffectiveSize(), true)
        
        EMIT EVENT "INV_ITEM_ROTATE" WITH (item.InstanceID, newRotation)
        RETURN true
    END FUNCTION
    
    // Find first available position for item
    FUNCTION FindAvailablePosition(container: InventoryContainer, item: ItemInstance) -> GridPosition?:
        FOR y FROM 0 TO container.GridSize.Height - 1:
            FOR x FROM 0 TO container.GridSize.Width - 1:
                testPos = GridPosition(x, y)
                IF container.CanPlaceAt(item, testPos):
                    RETURN testPos
                END IF
            END FOR
        END FOR
        
        // Try rotated
        IF item.BaseData.Rotatable:
            item.Rotation = ROT_90
            FOR y FROM 0 TO container.GridSize.Height - 1:
                FOR x FROM 0 TO container.GridSize.Width - 1:
                    testPos = GridPosition(x, y)
                    IF container.CanPlaceAt(item, testPos):
                        RETURN testPos
                    END IF
                END FOR
            END FOR
            item.Rotation = ROT_0  // Reset
        END IF
        
        RETURN null  // No space found
    END FUNCTION
    
    // Auto-pickup with auto-placement
    FUNCTION AutoPickup(item: ItemInstance) -> Boolean:
        position = FindAvailablePosition(playerInventory, item)
        
        IF position == null:
            EMIT EVENT "INV_FULL"
            RETURN false
        END IF
        
        RETURN AddItem(playerInventory, item, position)
    END FUNCTION
```

---

### GridSystem

**Purpose:** Handles grid operations, collision detection, and visualization.

**Pseudocode:**
```
CLASS GridSystem:
    
    // Validate item can be placed
    FUNCTION ValidatePlacement(container: InventoryContainer, item: ItemInstance, position: GridPosition) -> PlacementResult:
        result = NEW PlacementResult()
        result.IsValid = true
        result.BlockedCells = []
        
        itemSize = item.GetEffectiveSize()
        
        // Check bounds
        IF position.X < 0 OR position.Y < 0:
            result.IsValid = false
            result.Reason = "Position out of bounds"
            RETURN result
        END IF
        
        IF position.X + itemSize.Width > container.GridSize.Width:
            result.IsValid = false
            result.Reason = "Item exceeds grid width"
            RETURN result
        END IF
        
        IF position.Y + itemSize.Height > container.GridSize.Height:
            result.IsValid = false
            result.Reason = "Item exceeds grid height"
            RETURN result
        END IF
        
        // Check cell occupancy
        FOR x FROM position.X TO position.X + itemSize.Width - 1:
            FOR y FROM position.Y TO position.Y + itemSize.Height - 1:
                IF container.OccupiedCells[x, y]:
                    result.IsValid = false
                    result.BlockedCells.Add(GridPosition(x, y))
                END IF
            END FOR
        END FOR
        
        IF result.BlockedCells.Count > 0:
            result.Reason = "Cells already occupied"
        END IF
        
        RETURN result
    END FUNCTION
    
    // Auto-sort container (optimize space)
    FUNCTION AutoSort(container: InventoryContainer):
        // Get all items sorted by size (largest first)
        items = container.Items.OrderByDescending(i => i.BaseData.Size.TotalCells())
        
        // Clear all cells
        FOR x FROM 0 TO container.GridSize.Width - 1:
            FOR y FROM 0 TO container.GridSize.Height - 1:
                container.OccupiedCells[x, y] = false
            END FOR
        END FOR
        
        container.Items.Clear()
        
        // Re-place all items
        FOR EACH item IN items:
            position = FindOptimalPosition(container, item)
            IF position != null:
                item.Position = position
                container.Items.Add(item)
                container.SetCellsOccupied(position, item.GetEffectiveSize(), true)
            END IF
        END FOR
    END FUNCTION
    
    // Get cells occupied by an item (for visualization)
    FUNCTION GetItemCells(item: ItemInstance) -> List<GridPosition>:
        cells = NEW List<GridPosition>()
        size = item.GetEffectiveSize()
        
        FOR x FROM 0 TO size.Width - 1:
            FOR y FROM 0 TO size.Height - 1:
                cells.Add(GridPosition(item.Position.X + x, item.Position.Y + y))
            END FOR
        END FOR
        
        RETURN cells
    END FUNCTION
```

---

### WeightSystem

**Purpose:** Calculate encumbrance and apply movement penalties.

**Pseudocode:**
```
CLASS WeightSystem:
    
    // Current state
    currentWeight: Float
    currentLevel: EEncumbranceLevel
    maxWeight: Float = 35.0
    
    // Weight thresholds
    CONST LIGHT_MAX = 15.0
    CONST MEDIUM_MAX = 25.0
    CONST HEAVY_MAX = 35.0
    
    // Calculate total inventory weight
    FUNCTION CalculateTotalWeight(inventory: InventoryContainer) -> Float:
        total = 0.0
        
        FOR EACH item IN inventory.Items:
            total += item.GetTotalWeight()
        END FOR
        
        RETURN total
    END FUNCTION
    
    // Update weight and encumbrance
    FUNCTION UpdateWeight(inventory: InventoryContainer):
        oldLevel = currentLevel
        currentWeight = CalculateTotalWeight(inventory)
        
        // Determine encumbrance level
        IF currentWeight <= LIGHT_MAX:
            currentLevel = EL_Light
        ELSE IF currentWeight <= MEDIUM_MAX:
            currentLevel = EL_Medium
        ELSE IF currentWeight <= HEAVY_MAX:
            currentLevel = EL_Heavy
        ELSE:
            currentLevel = EL_Overweight
        END IF
        
        // Notify if changed
        IF oldLevel != currentLevel:
            EMIT EVENT "WEIGHT_THRESHOLD" WITH (oldLevel, currentLevel)
            ApplyMovementModifiers(currentLevel)
        END IF
        
        EMIT EVENT "WEIGHT_UPDATE" WITH (currentWeight)
    END FUNCTION
    
    // Get movement speed multiplier
    FUNCTION GetSpeedMultiplier() -> Float:
        SWITCH currentLevel:
            CASE EL_Light:
                RETURN 1.0
            CASE EL_Medium:
                RETURN 0.9
            CASE EL_Heavy:
                RETURN 0.75
            CASE EL_Overweight:
                RETURN 0.6
        END SWITCH
    END FUNCTION
    
    // Get stamina drain multiplier
    FUNCTION GetStaminaDrainMultiplier() -> Float:
        SWITCH currentLevel:
            CASE EL_Light:
                RETURN 1.0
            CASE EL_Medium:
                RETURN 1.2
            CASE EL_Heavy:
                RETURN 1.5
            CASE EL_Overweight:
                RETURN 2.0
        END SWITCH
    END FUNCTION
    
    // Apply modifiers to character
    FUNCTION ApplyMovementModifiers(level: EEncumbranceLevel):
        speedMult = GetSpeedMultiplier()
        staminaMult = GetStaminaDrainMultiplier()
        
        CharacterSystem.SetSpeedModifier("Encumbrance", speedMult)
        CharacterSystem.SetStaminaDrainModifier("Encumbrance", staminaMult)
    END FUNCTION
    
    // Check if can add more weight
    FUNCTION CanAddWeight(additionalWeight: Float) -> Boolean:
        RETURN currentWeight + additionalWeight <= maxWeight
    END FUNCTION
```

---

### StackManager

**Purpose:** Handle item stacking and splitting.

**Pseudocode:**
```
CLASS StackManager:
    
    // Check if two items can stack
    FUNCTION CanStack(item1: ItemInstance, item2: ItemInstance) -> Boolean:
        // Must be same item type
        IF item1.BaseData.CodeName != item2.BaseData.CodeName:
            RETURN false
        END IF
        
        // Must be stackable
        IF item1.BaseData.MaxStackSize <= 1:
            RETURN false
        END IF
        
        // Target must have room
        IF item1.StackCount >= item1.BaseData.MaxStackSize:
            RETURN false
        END IF
        
        // Only pristine items stack (for durability items)
        IF item1.Durability != item1.MaxDurability:
            RETURN false
        END IF
        IF item2.Durability != item2.MaxDurability:
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    // Merge two stacks
    FUNCTION MergeStacks(target: ItemInstance, source: ItemInstance) -> MergeResult:
        result = NEW MergeResult()
        
        IF NOT CanStack(target, source):
            result.Success = false
            RETURN result
        END IF
        
        availableSpace = target.BaseData.MaxStackSize - target.StackCount
        transferAmount = Min(availableSpace, source.StackCount)
        
        target.StackCount += transferAmount
        source.StackCount -= transferAmount
        
        result.Success = true
        result.TransferredAmount = transferAmount
        result.SourceDepleted = (source.StackCount == 0)
        
        IF result.SourceDepleted:
            // Remove empty stack
            InventoryManager.RemoveItem(source.Container, source, "Stack depleted")
        END IF
        
        EMIT EVENT "STACK_MERGE" WITH (target.InstanceID, source.InstanceID, transferAmount)
        RETURN result
    END FUNCTION
    
    // Split stack into two
    FUNCTION SplitStack(source: ItemInstance, amount: Integer) -> ItemInstance?:
        IF amount <= 0 OR amount >= source.StackCount:
            RETURN null  // Invalid split
        END IF
        
        // Create new stack
        newStack = CloneItem(source)
        newStack.InstanceID = GenerateUUID()
        newStack.StackCount = amount
        
        // Reduce source
        source.StackCount -= amount
        
        EMIT EVENT "STACK_SPLIT" WITH (source.InstanceID, amount, newStack.InstanceID)
        RETURN newStack
    END FUNCTION
```

---

### StashSystem

**Purpose:** Manage permanent player storage.

**Pseudocode:**
```
CLASS StashSystem:
    
    // Player stash
    playerStash: InventoryContainer
    databaseConnection: DatabaseConnection
    
    // Stash size tiers
    CONST STASH_TIER_1 = GridSize(10, 20)   // 200 cells
    CONST STASH_TIER_2 = GridSize(10, 30)   // 300 cells
    CONST STASH_TIER_3 = GridSize(10, 40)   // 400 cells
    CONST STASH_TIER_4 = GridSize(10, 50)   // 500 cells
    
    // Load player stash from database
    FUNCTION LoadStash(playerID: String) -> Boolean:
        TRY:
            data = databaseConnection.Query("SELECT * FROM player_stash WHERE player_id = ?", playerID)
            
            IF data == null:
                // New player - create default stash
                CreateDefaultStash(playerID)
                RETURN true
            END IF
            
            // Parse stash data
            playerStash = NEW InventoryContainer()
            playerStash.Initialize(ParseGridSize(data.gridSize))
            playerStash.Type = CT_Stash
            
            // Load items
            FOR EACH itemData IN data.items:
                item = DeserializeItem(itemData)
                playerStash.Items.Add(item)
                playerStash.SetCellsOccupied(item.Position, item.GetEffectiveSize(), true)
            END FOR
            
            EMIT EVENT "STASH_LOAD" WITH (playerID, playerStash.Items.Count)
            RETURN true
            
        CATCH error:
            LOG ERROR "Failed to load stash: " + error.Message
            RETURN false
        END TRY
    END FUNCTION
    
    // Save player stash to database
    FUNCTION SaveStash(playerID: String) -> Boolean:
        TRY:
            data = {
                player_id: playerID,
                grid_size: SerializeGridSize(playerStash.GridSize),
                items: []
            }
            
            FOR EACH item IN playerStash.Items:
                data.items.Add(SerializeItem(item))
            END FOR
            
            databaseConnection.Upsert("player_stash", data)
            
            EMIT EVENT "STASH_SAVE" WITH (playerID, playerStash.Items.Count)
            RETURN true
            
        CATCH error:
            LOG ERROR "Failed to save stash: " + error.Message
            RETURN false
        END TRY
    END FUNCTION
    
    // Expand stash size
    FUNCTION ExpandStash(playerID: String, newTier: Integer) -> Boolean:
        newSize = GetStashSizeForTier(newTier)
        
        IF newSize.TotalCells() <= playerStash.GridSize.TotalCells():
            RETURN false  // Can't downgrade
        END IF
        
        oldSize = playerStash.GridSize
        
        // Create new larger grid
        newOccupied = NEW Boolean[newSize.Width, newSize.Height]
        
        // Copy existing occupancy
        FOR x FROM 0 TO oldSize.Width - 1:
            FOR y FROM 0 TO oldSize.Height - 1:
                newOccupied[x, y] = playerStash.OccupiedCells[x, y]
            END FOR
        END FOR
        
        playerStash.GridSize = newSize
        playerStash.OccupiedCells = newOccupied
        
        EMIT EVENT "STASH_EXPAND" WITH (oldSize, newSize)
        SaveStash(playerID)
        
        RETURN true
    END FUNCTION
```

---

## Secure Container Rules

### Behavior During Raid

| State          | Can Insert | Can Extract    | Survives Death |
| :------------- | :--------- | :------------- | :------------- |
| **In Raid**    | Yes        | No             | Yes            |
| **In Hideout** | Yes        | Yes            | N/A            |
| **Post-Death** | N/A        | Yes (in stash) | Yes            |

### Secure Container Pseudocode

```
CLASS SecureContainer:
    
    container: InventoryContainer
    isInRaid: Boolean
    
    // Override add/remove to enforce rules
    FUNCTION TryAddItem(item: ItemInstance, position: GridPosition) -> Boolean:
        // Can always add during raid
        IF isInRaid:
            // Check if item is allowed in secure
            IF NOT IsItemAllowedInSecure(item):
                RETURN false
            END IF
        END IF
        
        RETURN InventoryManager.AddItem(container, item, position)
    END FUNCTION
    
    FUNCTION TryRemoveItem(item: ItemInstance) -> Boolean:
        // Cannot remove during raid
        IF isInRaid:
            ShowMessage("Cannot remove items from secure container during raid")
            RETURN false
        END IF
        
        RETURN InventoryManager.RemoveItem(container, item, "Player removed")
    END FUNCTION
    
    // Items not allowed in secure container
    FUNCTION IsItemAllowedInSecure(item: ItemInstance) -> Boolean:
        // Guns and armor not allowed
        IF item.BaseData.Type == IT_Weapon:
            RETURN false
        END IF
        IF item.BaseData.Type == IT_Armor:
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
```

---

## UI Integration

### Drag & Drop Flow

```
1. USER clicks item
   → Highlight item cells
   → Show item tooltip
   
2. USER drags item
   → Show ghost icon following cursor
   → Calculate target position (snap to grid)
   → Validate placement in real-time
   → Show green/red highlight on target cells
   
3. USER releases over valid target
   → Call MoveItem()
   → Update UI
   → Play placement sound
   
4. USER releases over invalid target
   → Return item to original position
   → Show error feedback
   → Play error sound
```

### Context Menu Actions

| Action            | Condition                | Result                     |
| :---------------- | :----------------------- | :------------------------- |
| **Use**           | Consumable/Medical       | Apply effect, reduce stack |
| **Equip**         | Weapon/Armor             | Move to equipped slot      |
| **Inspect**       | Any                      | Show detailed 3D view      |
| **Rotate**        | Rotatable item           | Change rotation            |
| **Split**         | Stack > 1                | Open split dialog          |
| **Move to Stash** | In inventory, stash open | Auto-find stash position   |
| **Discard**       | Any (not quest)          | Remove from game           |
| **Favorite**      | Any                      | Toggle favorite flag       |

---

## Performance Considerations

### Memory Budget

| Asset Type       | Max Size  | Pooled      |
| :--------------- | :-------- | :---------- |
| Item Icons       | 50 KB     | Yes (Atlas) |
| Item Prefabs     | 500 KB    | Yes         |
| Concurrent Items | 500       | -           |
| Grid Cells (Max) | 500 cells | -           |

### Optimization Strategies

```
1. ICON ATLAS
   - Combine item icons into texture atlases
   - Reduce draw calls in inventory UI

2. OBJECT POOLING
   - Pool ItemInstance objects
   - Pool UI inventory slot objects
   - Recycle instead of create/destroy

3. LAZY LOADING
   - Load stash items on-demand
   - Paginate large stashes
   
4. DELTA SYNC
   - Only sync changed items over network
   - Use version numbers for states
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] Implement InventoryContainer base class
- [ ] Create GridSystem collision detection
- [ ] Add item add/remove operations
- [ ] Implement weight calculation
- [ ] Create basic UI drag-and-drop

### MEDIUM Priority 🟡
- [ ] Add item rotation (R key)
- [ ] Implement stack merge/split
- [ ] Create auto-sort algorithm
- [ ] Add secure container rules
- [ ] Implement stash save/load

### LOW Priority 🟢
- [ ] Add quick-slot bar
- [ ] Create inventory search/filter
- [ ] Implement loadout presets
- [ ] Add item comparison tooltip
- [ ] Create debug commands

---

## Data Persistence

### Save Format (JSON)

```json
{
  "playerId": "uuid-string",
  "version": 1,
  "stash": {
    "gridSize": { "width": 10, "height": 20 },
    "items": [
      {
        "instanceId": "uuid-string",
        "codeName": "ITEM_MED_BANDAGE",
        "position": { "x": 0, "y": 0 },
        "rotation": 0,
        "stackCount": 5,
        "durability": 100,
        "isFavorited": false
      }
    ]
  },
  "secureContainer": {
    "gridSize": { "width": 2, "height": 2 },
    "items": []
  },
  "lastModified": "2024-01-15T10:30:00Z"
}
```

---

## System Relationships

### Dependency Diagram

```
                    ┌────────────────────┐
                    │  INVENTORY SYSTEM  │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ WEAPON          │  │ CHARACTER       │  │ UI              │
│ SYSTEM          │  │ SYSTEM          │  │ SYSTEM          │
│                 │  │                 │  │                 │
│ • Weapon storage│  │ • Equipped armor│  │ • Inventory UI  │
│ • Ammo mgmt     │  │ • Backpack size │  │ • Drag-and-drop │
│ • Attachments   │  │ • Encumbrance   │  │ • Tooltips      │
└─────────────────┘  └─────────────────┘  └─────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ LOOT            │  │ TRADING         │  │ DATABASE        │
│ SYSTEM          │  │ SYSTEM          │  │ SYSTEM          │
│                 │  │                 │  │                 │
│ • World loot    │  │ • Player trade  │  │ • Stash persist │
│ • Container open│  │ • Marketplace   │  │ • Save/Load     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```



