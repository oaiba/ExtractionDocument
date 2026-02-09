---
title: "Save System - Technical Specification"
type: docs
---
# Save System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: Tutorial System →](./TutorialSystem.md)**

**Reference:** [High-Level Persistence Design](../../GDD_HighLevel/Technical/Persistence.md)

---

## Overview

The **Save System** manages all data persistence including local saves, cloud sync, data validation, encryption, and recovery. Designed for reliability with backup and conflict resolution.

**Responsibilities:**
- Local save/load operations
- Cloud synchronization
- Data validation and checksums
- Encryption for sensitive data
- Version migration
- Backup and recovery
- Match state persistence
- Cross-device sync
- Conflict resolution

---

## Enums & Types

### SaveDataType
Data category for saving.

| Code Name           | Display Name   | Priority | Sync Freq | Size (Avg) | Description                     |
| :------------------ | :------------- | :------- | :-------- | :--------- | :------------------------------ |
| `SDT_PlayerProfile` | Player Profile | Critical | Real-time | 2 KB       | Account info, level, currencies |
| `SDT_Inventory`     | Inventory      | Critical | On change | 50 KB      | Items, stash contents           |
| `SDT_Progression`   | Progression    | High     | On change | 10 KB      | Quests, achievements, unlocks   |
| `SDT_MatchState`    | Match State    | Critical | Real-time | 10 KB      | Current match (recovery)        |
| `SDT_Settings`      | Settings       | Low      | On change | 1 KB       | Player preferences              |
| `SDT_Statistics`    | Statistics     | Medium   | Periodic  | 5 KB       | Gameplay stats                  |
| `SDT_Social`        | Social         | Low      | On change | 3 KB       | Friends, clan data              |
| `SDT_Cosmetics`     | Cosmetics      | Medium   | On change | 2 KB       | Skins, loadouts                 |

---

### SyncState
Cloud synchronization state.

| Code Name        | Display Name | Icon | Sync Action | Description             |
| :--------------- | :----------- | :--- | :---------- | :---------------------- |
| `SS_Synced`      | Synced       | ✓    | None        | Local matches cloud     |
| `SS_Pending`     | Pending      | ↑    | Upload      | Local changes to upload |
| `SS_Downloading` | Downloading  | ↓    | Download    | Receiving cloud data    |
| `SS_Uploading`   | Uploading    | ↑    | Upload      | Sending to cloud        |
| `SS_Conflict`    | Conflict     | ⚠    | Resolve     | Local and cloud differ  |
| `SS_Error`       | Error        | ✗    | Retry       | Sync failed             |
| `SS_Offline`     | Offline      | −    | Queue       | No connection           |

---

### SaveResult
Save operation result.

| Code Name             | Display Name      | Success | Retry   | Description              |
| :-------------------- | :---------------- | :------ | :------ | :----------------------- |
| `SR_Success`          | Success           | Yes     | No      | Save completed           |
| `SR_Failed`           | Failed            | No      | Yes     | Save failed (retry)      |
| `SR_ValidationFailed` | Validation Failed | No      | No      | Data invalid             |
| `SR_DiskFull`         | Disk Full         | No      | No      | No storage space         |
| `SR_PermissionDenied` | Permission Denied | No      | No      | No write access          |
| `SR_Corrupted`        | Corrupted         | No      | No      | Data corruption detected |
| `SR_VersionMismatch`  | Version Mismatch  | No      | Migrate | Old data version         |

---

### CloudService
Cloud save provider.

| Code Name       | Display Name | Platform | Priority | Description           |
| :-------------- | :----------- | :------- | :------- | :-------------------- |
| `CS_GameServer` | Game Server  | All      | 1        | Primary authoritative |
| `CS_GooglePlay` | Google Play  | Android  | 2        | Android fallback      |
| `CS_iCloud`     | iCloud       | iOS      | 2        | iOS backup            |
| `CS_Steam`      | Steam        | PC       | 2        | Steam Cloud           |
| `CS_None`       | None         | All      | 99       | Local only            |

---

### ConflictResolution
Conflict resolution strategy.

| Code Name      | Display Name | Auto | Description        |
| :------------- | :----------- | :--- | :----------------- |
| `CR_UseLocal`  | Use Local    | No   | Keep local version |
| `CR_UseCloud`  | Use Cloud    | No   | Use cloud version  |
| `CR_UseNewest` | Use Newest   | Yes  | Timestamp-based    |
| `CR_Merge`     | Merge        | Yes  | Combine data       |
| `CR_AskUser`   | Ask User     | No   | Show UI prompt     |

---

### DataMigrationStatus
Data version migration status.

| Code Name        | Display Name | Can Continue | Description      |
| :--------------- | :----------- | :----------- | :--------------- |
| `DM_NotRequired` | Not Required | Yes          | Already current  |
| `DM_Required`    | Required     | Yes          | Needs migration  |
| `DM_InProgress`  | In Progress  | Wait         | Migrating        |
| `DM_Completed`   | Completed    | Yes          | Migration done   |
| `DM_Failed`      | Failed       | No           | Migration failed |

---

## Code Names

### Save Events

| Code Name       | Trigger       | Parameters       | Description             |
| :-------------- | :------------ | :--------------- | :---------------------- |
| `SAVE_START`    | Save begins   | DataType, Size   | Save operation started  |
| `SAVE_COMPLETE` | Save finishes | DataType, Result | Save operation complete |
| `SAVE_FAILED`   | Save error    | DataType, Error  | Save operation failed   |
| `LOAD_START`    | Load begins   | DataType         | Load operation started  |
| `LOAD_COMPLETE` | Load finishes | DataType, Size   | Load operation complete |
| `LOAD_FAILED`   | Load error    | DataType, Error  | Load operation failed   |

### Sync Events

| Code Name       | Trigger             | Parameters                   | Description         |
| :-------------- | :------------------ | :--------------------------- | :------------------ |
| `SYNC_START`    | Sync begins         | DataType                     | Cloud sync started  |
| `SYNC_COMPLETE` | Sync finishes       | DataType, Direction          | Cloud sync complete |
| `SYNC_CONFLICT` | Conflict detected   | DataType, LocalVer, CloudVer | Data conflict found |
| `SYNC_RESOLVED` | Conflict resolved   | DataType, Resolution         | Conflict resolved   |
| `SYNC_OFFLINE`  | Connection lost     | LastSyncTime                 | Went offline        |
| `SYNC_ONLINE`   | Connection restored | QueuedChanges                | Came online         |

### Backup Events

| Code Name         | Trigger        | Parameters       | Description     |
| :---------------- | :------------- | :--------------- | :-------------- |
| `BACKUP_CREATED`  | Backup made    | BackupName, Size | Backup created  |
| `BACKUP_RESTORED` | Backup loaded  | BackupName       | Backup restored |
| `BACKUP_DELETED`  | Backup removed | BackupName       | Backup deleted  |

---

## Architecture

### Class Diagram

```
                    ┌─────────────────┐
                    │   SaveManager   │
                    │   (Singleton)   │
                    └────────┬────────┘
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
┌───▼───────┐    ┌───────────▼───────────┐    ┌───────▼───────┐
│LocalStore │    │    CloudProvider      │    │DataValidator  │
│ Manager   │    │                       │    │               │
└───────────┘    └───────────────────────┘    └───────────────┘
    │                        │                        │
    │            ┌───────────┼───────────┐           │
    │            │           │           │           │
    │    ┌───────▼───┐ ┌─────▼────┐ ┌────▼────┐     │
    │    │Encryption │ │Migration │ │Backup   │     │
    │    │ Manager   │ │ Manager  │ │ Manager │     │
    │    └───────────┘ └──────────┘ └─────────┘     │
    │                                                │
    └────────────────────────────────────────────────┘
```

---

## Core Classes

### SaveManager

**Purpose:** Central save/load controller.

```
CLASS SaveManager:
    STATIC instance: SaveManager
    
    // Sub-managers
    localStorageManager: LocalStorageManager
    cloudProvider: CloudProvider
    dataValidator: DataValidator
    encryptionManager: EncryptionManager
    migrationManager: MigrationManager
    backupManager: BackupManager
    syncManager: SyncManager
    matchStateManager: MatchStateManager
    
    // State
    currentSyncState: SyncState = SS_Synced
    pendingChanges: Map<SaveDataType, Boolean>
    autoSaveConfig: AutoSaveConfig
    
    // Events
    OnSaveComplete: Event<(dataType, result)>
    OnLoadComplete: Event<(dataType, data)>
    OnSyncStateChanged: Event<(oldState, newState)>
    
    FUNCTION SaveData(dataType: SaveDataType, data: Object) -> SaveResult:
        // Validate data
        validationResult = dataValidator.Validate(dataType, data)
        IF NOT validationResult.isValid:
            EMIT EVENT "SAVE_FAILED" WITH (dataType, "Validation failed")
            RETURN SR_ValidationFailed
        END IF
        
        EMIT EVENT "SAVE_START" WITH (dataType, GetDataSize(data))
        
        // Serialize
        serializedData = SerializeData(data)
        
        // Generate checksum
        checksum = GenerateChecksum(serializedData)
        
        // Encrypt if needed
        IF ShouldEncrypt(dataType):
            serializedData = encryptionManager.Encrypt(serializedData)
        END IF
        
        // Add metadata
        savePackage = CreateSavePackage(dataType, serializedData, checksum)
        
        // Save locally
        localResult = localStorageManager.Save(GetFilePath(dataType), savePackage)
        
        IF localResult != SR_Success:
            EMIT EVENT "SAVE_FAILED" WITH (dataType, localResult)
            RETURN localResult
        END IF
        
        // Mark for cloud sync
        MarkPendingSync(dataType)
        
        OnSaveComplete.Broadcast(dataType, SR_Success)
        
        EMIT EVENT "SAVE_COMPLETE" WITH (dataType, SR_Success)
        
        RETURN SR_Success
    END FUNCTION
    
    FUNCTION LoadData(dataType: SaveDataType) -> LoadResult:
        EMIT EVENT "LOAD_START" WITH (dataType)
        
        filePath = GetFilePath(dataType)
        
        // Load from local storage
        loadResult = localStorageManager.Load(filePath)
        
        IF loadResult.failed:
            EMIT EVENT "LOAD_FAILED" WITH (dataType, loadResult.error)
            RETURN LoadResult.Failed(loadResult.error)
        END IF
        
        savePackage = loadResult.data
        
        // Validate checksum
        IF NOT ValidateChecksum(savePackage):
            EMIT EVENT "LOAD_FAILED" WITH (dataType, "Checksum mismatch")
            
            // Try to restore from backup
            backupResult = backupManager.RestoreLatest(dataType)
            IF backupResult.success:
                RETURN LoadData(dataType) // Retry with backup
            END IF
            
            RETURN LoadResult.Failed("Data corrupted")
        END IF
        
        // Decrypt if needed
        serializedData = savePackage.data
        IF encryptionManager.IsEncrypted(serializedData):
            serializedData = encryptionManager.Decrypt(serializedData)
        END IF
        
        // Check version and migrate if needed
        migrationStatus = migrationManager.CheckMigrationNeeded(dataType, savePackage.dataVersion)
        
        IF migrationStatus == DM_Required:
            serializedData = migrationManager.MigrateData(dataType, serializedData, 
                savePackage.dataVersion, GetCurrentVersion(dataType))
        END IF
        
        // Deserialize
        data = DeserializeData(dataType, serializedData)
        
        OnLoadComplete.Broadcast(dataType, data)
        
        EMIT EVENT "LOAD_COMPLETE" WITH (dataType, GetDataSize(data))
        
        RETURN LoadResult.Success(data)
    END FUNCTION
    
    FUNCTION SaveAllPendingData():
        FOR EACH (dataType, pending) IN pendingChanges:
            IF pending:
                data = GetCurrentData(dataType)
                SaveData(dataType, data)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION SyncWithCloud():
        IF NOT cloudProvider.IsConnected():
            SetSyncState(SS_Offline)
            RETURN
        END IF
        
        syncManager.BeginSync()
    END FUNCTION
    
    FUNCTION SetSyncState(newState: SyncState):
        oldState = currentSyncState
        currentSyncState = newState
        
        OnSyncStateChanged.Broadcast(oldState, newState)
    END FUNCTION
    
    FUNCTION MarkPendingSync(dataType: SaveDataType):
        pendingChanges[dataType] = true
        
        IF autoSaveConfig.periodicSaveInterval > 0:
            ScheduleAutoSave()
        END IF
    END FUNCTION
    
    FUNCTION HasPendingChanges() -> Boolean:
        FOR EACH (type, pending) IN pendingChanges:
            IF pending:
                RETURN true
            END IF
        END FOR
        
        RETURN false
    END FUNCTION
    
    FUNCTION DeleteAllData():
        localStorageManager.DeleteAll()
        backupManager.DeleteAllBackups()
        pendingChanges.Clear()
    END FUNCTION

STRUCT SavePackage:
    dataType: SaveDataType
    data: ByteArray
    dataVersion: Integer
    checksum: String
    timestamp: DateTime
    playerID: String
```

---

### LocalStorageManager

**Purpose:** Local file system operations.

```
CLASS LocalStorageManager:
    // Paths
    saveDirectory: String
    
    // Config
    maxSaveSize: Integer = 10485760  // 10 MB per file
    
    FUNCTION GetSaveDirectory() -> String:
        RETURN Platform.GetPersistentDataPath() + "/Saves/"
    END FUNCTION
    
    FUNCTION Initialize():
        saveDirectory = GetSaveDirectory()
        
        IF NOT DirectoryExists(saveDirectory):
            CreateDirectory(saveDirectory)
        END IF
    END FUNCTION
    
    FUNCTION Save(filePath: String, data: ByteArray) -> SaveResult:
        // Check disk space
        IF NOT HasEnoughSpace(data.Length):
            RETURN SR_DiskFull
        END IF
        
        // Check file size limit
        IF data.Length > maxSaveSize:
            LOG_ERROR("Save data too large: " + data.Length)
            RETURN SR_Failed
        END IF
        
        TRY:
            fullPath = saveDirectory + filePath
            
            // Write to temp file first
            tempPath = fullPath + ".tmp"
            WriteFile(tempPath, data)
            
            // Verify write
            IF NOT VerifyFile(tempPath, data):
                DeleteFile(tempPath)
                RETURN SR_Failed
            END IF
            
            // Atomic rename
            IF FileExists(fullPath):
                DeleteFile(fullPath)
            END IF
            
            RenameFile(tempPath, fullPath)
            
            RETURN SR_Success
            
        CATCH IOException e:
            LOG_ERROR("Save failed: " + e.Message)
            RETURN SR_Failed
        CATCH SecurityException e:
            RETURN SR_PermissionDenied
        END TRY
    END FUNCTION
    
    FUNCTION Load(filePath: String) -> LoadResult:
        fullPath = saveDirectory + filePath
        
        IF NOT FileExists(fullPath):
            RETURN LoadResult.NotFound()
        END IF
        
        TRY:
            data = ReadFile(fullPath)
            RETURN LoadResult.Success(data)
            
        CATCH IOException e:
            LOG_ERROR("Load failed: " + e.Message)
            RETURN LoadResult.Failed(e.Message)
        CATCH SecurityException e:
            RETURN LoadResult.Failed("Permission denied")
        END TRY
    END FUNCTION
    
    FUNCTION Delete(filePath: String) -> Boolean:
        fullPath = saveDirectory + filePath
        
        IF FileExists(fullPath):
            DeleteFile(fullPath)
            RETURN true
        END IF
        
        RETURN false
    END FUNCTION
    
    FUNCTION DeleteAll():
        files = GetFilesInDirectory(saveDirectory)
        
        FOR EACH file IN files:
            DeleteFile(file)
        END FOR
    END FUNCTION
    
    FUNCTION FileExists(filePath: String) -> Boolean:
        RETURN System.FileExists(saveDirectory + filePath)
    END FUNCTION
    
    FUNCTION GetFileSize(filePath: String) -> Integer:
        RETURN System.GetFileSize(saveDirectory + filePath)
    END FUNCTION
    
    FUNCTION GetLastModified(filePath: String) -> DateTime:
        RETURN System.GetFileModifiedTime(saveDirectory + filePath)
    END FUNCTION
    
    FUNCTION HasEnoughSpace(requiredBytes: Integer) -> Boolean:
        availableBytes = Platform.GetAvailableDiskSpace()
        RETURN availableBytes >= requiredBytes + 1048576  // 1 MB buffer
    END FUNCTION

STRUCT LoadResult:
    success: Boolean
    data: ByteArray
    error: String
    
    STATIC FUNCTION Success(data: ByteArray) -> LoadResult:
        RETURN { success: true, data: data, error: "" }
    END FUNCTION
    
    STATIC FUNCTION Failed(error: String) -> LoadResult:
        RETURN { success: false, data: null, error: error }
    END FUNCTION
    
    STATIC FUNCTION NotFound() -> LoadResult:
        RETURN { success: false, data: null, error: "File not found" }
    END FUNCTION
```

---

### CloudProvider

**Purpose:** Cloud save synchronization provider.

```
CLASS CloudProvider:
    // State
    currentService: CloudService
    isConnected: Boolean = false
    lastSyncTime: DateTime
    
    // Events
    OnConnected: Event<()>
    OnDisconnected: Event<()>
    OnDataReceived: Event<(dataType, data)>
    
    FUNCTION Initialize(service: CloudService):
        currentService = service
        
        SWITCH service:
            CASE CS_GameServer:
                InitializeGameServer()
            CASE CS_GooglePlay:
                InitializeGooglePlay()
            CASE CS_iCloud:
                InitializeiCloud()
            CASE CS_Steam:
                InitializeSteam()
        END SWITCH
    END FUNCTION
    
    FUNCTION Connect() -> Boolean:
        TRY:
            SWITCH currentService:
                CASE CS_GameServer:
                    isConnected = GameServerClient.Connect()
                CASE CS_GooglePlay:
                    isConnected = PlayGamesClient.SignIn()
                CASE CS_iCloud:
                    isConnected = iCloudClient.CheckAvailability()
                CASE CS_Steam:
                    isConnected = SteamCloud.IsAvailable()
            END SWITCH
            
            IF isConnected:
                OnConnected.Broadcast()
            END IF
            
            RETURN isConnected
            
        CATCH Exception e:
            LOG_ERROR("Cloud connect failed: " + e.Message)
            RETURN false
        END TRY
    END FUNCTION
    
    FUNCTION Disconnect():
        isConnected = false
        OnDisconnected.Broadcast()
    END FUNCTION
    
    FUNCTION IsConnected() -> Boolean:
        RETURN isConnected
    END FUNCTION
    
    FUNCTION Upload(dataType: SaveDataType, data: ByteArray) -> Boolean:
        IF NOT isConnected:
            RETURN false
        END IF
        
        key = GetCloudKey(dataType)
        
        TRY:
            SWITCH currentService:
                CASE CS_GameServer:
                    result = GameServerClient.UploadSave(key, data)
                CASE CS_GooglePlay:
                    result = PlayGamesClient.SaveSnapshot(key, data)
                CASE CS_iCloud:
                    result = iCloudClient.WriteFile(key, data)
                CASE CS_Steam:
                    result = SteamCloud.WriteFile(key, data)
            END SWITCH
            
            IF result:
                lastSyncTime = DateTime.Now
            END IF
            
            RETURN result
            
        CATCH Exception e:
            LOG_ERROR("Cloud upload failed: " + e.Message)
            RETURN false
        END TRY
    END FUNCTION
    
    FUNCTION Download(dataType: SaveDataType) -> CloudDownloadResult:
        IF NOT isConnected:
            RETURN CloudDownloadResult.Offline()
        END IF
        
        key = GetCloudKey(dataType)
        
        TRY:
            data = null
            metadata = null
            
            SWITCH currentService:
                CASE CS_GameServer:
                    (data, metadata) = GameServerClient.DownloadSave(key)
                CASE CS_GooglePlay:
                    (data, metadata) = PlayGamesClient.LoadSnapshot(key)
                CASE CS_iCloud:
                    (data, metadata) = iCloudClient.ReadFile(key)
                CASE CS_Steam:
                    data = SteamCloud.ReadFile(key)
            END SWITCH
            
            IF data != null:
                OnDataReceived.Broadcast(dataType, data)
                RETURN CloudDownloadResult.Success(data, metadata)
            END IF
            
            RETURN CloudDownloadResult.NotFound()
            
        CATCH Exception e:
            LOG_ERROR("Cloud download failed: " + e.Message)
            RETURN CloudDownloadResult.Failed(e.Message)
        END TRY
    END FUNCTION
    
    FUNCTION GetCloudMetadata(dataType: SaveDataType) -> CloudMetadata:
        key = GetCloudKey(dataType)
        
        SWITCH currentService:
            CASE CS_GameServer:
                RETURN GameServerClient.GetMetadata(key)
            CASE CS_GooglePlay:
                RETURN PlayGamesClient.GetSnapshotMetadata(key)
            CASE CS_iCloud:
                RETURN iCloudClient.GetFileMetadata(key)
            CASE CS_Steam:
                RETURN SteamCloud.GetFileMetadata(key)
        END SWITCH
    END FUNCTION
    
    FUNCTION GetCloudKey(dataType: SaveDataType) -> String:
        RETURN "save_" + dataType.ToString().ToLower()
    END FUNCTION

STRUCT CloudMetadata:
    lastModified: DateTime
    size: Integer
    checksum: String
    deviceID: String

STRUCT CloudDownloadResult:
    success: Boolean
    data: ByteArray
    metadata: CloudMetadata
    error: String
```

---

### SyncManager

**Purpose:** Cloud sync orchestration and conflict resolution.

```
CLASS SyncManager:
    // State
    syncInProgress: Boolean = false
    pendingSync: List<SaveDataType>
    
    // Config
    conflictResolution: ConflictResolution = CR_UseNewest
    
    // Events
    OnSyncProgress: Event<(dataType, progress)>
    OnConflictDetected: Event<(dataType, localData, cloudData)>
    
    FUNCTION BeginSync():
        IF syncInProgress:
            RETURN
        END IF
        
        syncInProgress = true
        
        SaveManager.SetSyncState(SS_Downloading)
        
        EMIT EVENT "SYNC_START" WITH (SDT_All)
        
        // Download first
        FOR EACH dataType IN GetSyncPriorityOrder():
            DownloadAndMerge(dataType)
        END FOR
        
        SaveManager.SetSyncState(SS_Uploading)
        
        // Upload pending changes
        FOR EACH dataType IN pendingSync:
            UploadData(dataType)
        END FOR
        
        syncInProgress = false
        pendingSync.Clear()
        
        SaveManager.SetSyncState(SS_Synced)
        
        EMIT EVENT "SYNC_COMPLETE" WITH (SDT_All, "Both")
    END FUNCTION
    
    FUNCTION DownloadAndMerge(dataType: SaveDataType):
        downloadResult = CloudProvider.Download(dataType)
        
        IF NOT downloadResult.success:
            RETURN
        END IF
        
        cloudData = downloadResult.data
        cloudMetadata = downloadResult.metadata
        
        localData = LocalStorageManager.Load(GetFilePath(dataType))
        
        // Compare versions
        IF NeedsResolution(localData, cloudData, cloudMetadata):
            ResolveConflict(dataType, localData, cloudData, cloudMetadata)
        ELSE IF cloudMetadata.lastModified > LocalLastModified(dataType):
            // Cloud is newer, use it
            SaveManager.SaveDataLocal(dataType, cloudData)
        END IF
    END FUNCTION
    
    FUNCTION UploadData(dataType: SaveDataType):
        data = LocalStorageManager.Load(GetFilePath(dataType))
        
        IF data.success:
            CloudProvider.Upload(dataType, data.data)
        END IF
    END FUNCTION
    
    FUNCTION NeedsResolution(localData: ByteArray, cloudData: ByteArray, cloudMetadata: CloudMetadata) -> Boolean:
        // Same checksum = no conflict
        localChecksum = GenerateChecksum(localData)
        
        IF localChecksum == cloudMetadata.checksum:
            RETURN false
        END IF
        
        // Different data, check timestamps
        localModified = LocalStorageManager.GetLastModified(GetFilePath())
        
        // Both modified since last sync = conflict
        IF localModified > LastSyncTime AND cloudMetadata.lastModified > LastSyncTime:
            RETURN true
        END IF
        
        RETURN false
    END FUNCTION
    
    FUNCTION ResolveConflict(dataType: SaveDataType, localData: ByteArray, cloudData: ByteArray, cloudMetadata: CloudMetadata):
        EMIT EVENT "SYNC_CONFLICT" WITH (dataType, localData.Version, cloudMetadata.version)
        
        SaveManager.SetSyncState(SS_Conflict)
        
        OnConflictDetected.Broadcast(dataType, localData, cloudData)
        
        resolution = conflictResolution
        
        SWITCH resolution:
            CASE CR_UseLocal:
                // Upload local to cloud
                CloudProvider.Upload(dataType, localData)
            
            CASE CR_UseCloud:
                // Save cloud data locally
                SaveManager.SaveDataLocal(dataType, cloudData)
            
            CASE CR_UseNewest:
                localModified = LocalStorageManager.GetLastModified(GetFilePath(dataType))
                
                IF localModified > cloudMetadata.lastModified:
                    CloudProvider.Upload(dataType, localData)
                ELSE:
                    SaveManager.SaveDataLocal(dataType, cloudData)
                END IF
            
            CASE CR_Merge:
                mergedData = MergeData(dataType, localData, cloudData)
                SaveManager.SaveData(dataType, mergedData)
                CloudProvider.Upload(dataType, mergedData)
            
            CASE CR_AskUser:
                UIManager.ShowConflictResolutionUI(dataType, localData, cloudData, LAMBDA choice:
                    ApplyResolution(dataType, choice, localData, cloudData)
                END LAMBDA)
        END SWITCH
        
        EMIT EVENT "SYNC_RESOLVED" WITH (dataType, resolution)
    END FUNCTION
    
    FUNCTION MergeData(dataType: SaveDataType, localData: ByteArray, cloudData: ByteArray) -> ByteArray:
        // Type-specific merge logic
        SWITCH dataType:
            CASE SDT_Inventory:
                RETURN MergeInventory(localData, cloudData)
            CASE SDT_Progression:
                RETURN MergeProgression(localData, cloudData)
            DEFAULT:
                // Default to newest
                RETURN UseNewest(localData, cloudData)
        END SWITCH
    END FUNCTION
    
    FUNCTION GetSyncPriorityOrder() -> List<SaveDataType>:
        RETURN [
            SDT_PlayerProfile,   // Most critical
            SDT_Inventory,       // High value
            SDT_Progression,     // Important
            SDT_MatchState,      // Recovery
            SDT_Statistics,      // Nice to have
            SDT_Settings,
            SDT_Social,
            SDT_Cosmetics
        ]
    END FUNCTION
```

---

### DataValidator

**Purpose:** Data integrity validation.

```
CLASS DataValidator:
    FUNCTION Validate(dataType: SaveDataType, data: Object) -> ValidationResult:
        result = NEW ValidationResult()
        result.isValid = true
        
        // Type-specific validation
        SWITCH dataType:
            CASE SDT_PlayerProfile:
                ValidatePlayerProfile(data, result)
            CASE SDT_Inventory:
                ValidateInventory(data, result)
            CASE SDT_Progression:
                ValidateProgression(data, result)
            CASE SDT_Settings:
                ValidateSettings(data, result)
        END SWITCH
        
        RETURN result
    END FUNCTION
    
    FUNCTION ValidatePlayerProfile(data: PlayerProfileData, result: ValidationResult):
        // PlayerID required
        IF data.playerID.IsEmpty():
            result.AddError("PlayerID is required")
        END IF
        
        // Level valid range
        IF data.accountLevel < 1 OR data.accountLevel > MAX_LEVEL:
            result.AddError("Account level out of range")
        END IF
        
        // Currencies non-negative
        IF data.credits < 0:
            result.AddError("Credits cannot be negative")
        END IF
        
        IF data.premiumCurrency < 0:
            result.AddError("Premium currency cannot be negative")
        END IF
    END FUNCTION
    
    FUNCTION ValidateInventory(data: InventoryData, result: ValidationResult):
        // Check capacity
        IF data.stashItems.Count > data.stashCapacity:
            result.AddError("Stash exceeds capacity")
        END IF
        
        // Validate each item
        FOR EACH item IN data.stashItems:
            IF NOT ValidateItem(item):
                result.AddError("Invalid item: " + item.itemID)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION ValidateItem(item: SavedItemData) -> Boolean:
        // ItemID must exist
        IF NOT ItemDatabase.Exists(item.itemID):
            RETURN false
        END IF
        
        // Quantity valid
        IF item.quantity <= 0:
            RETURN false
        END IF
        
        // Durability valid
        IF item.durability < 0 OR item.durability > 100:
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    FUNCTION ValidateProgression(data: ProgressionData, result: ValidationResult):
        // XP valid
        IF data.currentXP < 0:
            result.AddError("XP cannot be negative")
        END IF
        
        // Quest IDs valid
        FOR EACH questID IN data.completedQuests:
            IF NOT QuestDatabase.Exists(questID):
                result.AddWarning("Unknown quest: " + questID)
            END IF
        END FOR
    END FUNCTION
    
    FUNCTION ValidateSettings(data: SettingsData, result: ValidationResult):
        // Volume ranges
        IF data.masterVolume < 0 OR data.masterVolume > 1:
            result.AddError("Master volume out of range")
        END IF
        
        // Sensitivity ranges
        IF data.sensitivity < 0.1 OR data.sensitivity > 5.0:
            result.AddError("Sensitivity out of range")
        END IF
    END FUNCTION
    
    FUNCTION ValidateChecksum(data: ByteArray, expectedChecksum: String) -> Boolean:
        actualChecksum = GenerateChecksum(data)
        RETURN actualChecksum == expectedChecksum
    END FUNCTION
    
    FUNCTION GenerateChecksum(data: ByteArray) -> String:
        RETURN SHA256.ComputeHash(data).ToHexString()
    END FUNCTION

STRUCT ValidationResult:
    isValid: Boolean = true
    errors: List<String>
    warnings: List<String>
    
    FUNCTION AddError(message: String):
        errors.Add(message)
        isValid = false
    END FUNCTION
    
    FUNCTION AddWarning(message: String):
        warnings.Add(message)
    END FUNCTION
```

---

### EncryptionManager

**Purpose:** Data encryption for sensitive saves.

```
CLASS EncryptionManager:
    // Config
    CONST KEY_SIZE = 256  // AES-256
    
    FUNCTION Encrypt(data: ByteArray) -> ByteArray:
        // Derive key from device ID
        key = DeriveKey(GetDeviceID())
        
        // Generate random IV
        iv = GenerateIV()
        
        // Encrypt using AES-256-CBC
        encryptedData = AES.Encrypt(data, key, iv)
        
        // Prepend IV to encrypted data
        result = ConcatArrays(iv, encryptedData)
        
        RETURN result
    END FUNCTION
    
    FUNCTION Decrypt(encryptedData: ByteArray) -> ByteArray:
        // Extract IV (first 16 bytes)
        iv = encryptedData.Slice(0, 16)
        cipherText = encryptedData.Slice(16)
        
        // Derive key
        key = DeriveKey(GetDeviceID())
        
        // Decrypt
        TRY:
            data = AES.Decrypt(cipherText, key, iv)
            RETURN data
        CATCH CryptographicException e:
            LOG_ERROR("Decryption failed: " + e.Message)
            RETURN null
        END TRY
    END FUNCTION
    
    FUNCTION IsEncrypted(data: ByteArray) -> Boolean:
        // Check for encryption header/marker
        IF data.Length < 16:
            RETURN false
        END IF
        
        // Check magic bytes
        RETURN data[0] == 0xEF AND data[1] == 0xBE
    END FUNCTION
    
    FUNCTION DeriveKey(deviceID: String) -> ByteArray:
        // Use PBKDF2 to derive key from device ID + salt
        salt = GetApplicationSalt()
        iterations = 10000
        
        RETURN PBKDF2.DeriveKey(deviceID, salt, iterations, KEY_SIZE / 8)
    END FUNCTION
    
    FUNCTION GenerateIV() -> ByteArray:
        iv = NEW ByteArray(16)
        Random.FillBytes(iv)
        RETURN iv
    END FUNCTION
    
    FUNCTION GetDeviceID() -> String:
        RETURN Platform.GetUniqueDeviceID()
    END FUNCTION
    
    FUNCTION GetApplicationSalt() -> ByteArray:
        // Static salt stored in application
        RETURN BASE64.Decode("YOUR_BASE64_SALT_HERE")
    END FUNCTION
```

---

### MigrationManager

**Purpose:** Save data version migration.

```
CLASS MigrationManager:
    // Version tracking
    CONST CURRENT_PROFILE_VERSION = 2
    CONST CURRENT_INVENTORY_VERSION = 2
    CONST CURRENT_PROGRESSION_VERSION = 1
    CONST CURRENT_SETTINGS_VERSION = 1
    
    FUNCTION CheckMigrationNeeded(dataType: SaveDataType, loadedVersion: Integer) -> DataMigrationStatus:
        currentVersion = GetCurrentDataVersion(dataType)
        
        IF loadedVersion == currentVersion:
            RETURN DM_NotRequired
        END IF
        
        IF loadedVersion > currentVersion:
            LOG_WARNING("Save data is from newer version")
            RETURN DM_NotRequired  // Don't downgrade
        END IF
        
        RETURN DM_Required
    END FUNCTION
    
    FUNCTION MigrateData(dataType: SaveDataType, data: ByteArray, fromVersion: Integer, toVersion: Integer) -> ByteArray:
        currentData = data
        currentVersion = fromVersion
        
        // Apply migrations in sequence
        WHILE currentVersion < toVersion:
            migrationFunc = GetMigrationFunction(dataType, currentVersion, currentVersion + 1)
            
            IF migrationFunc == null:
                LOG_ERROR("Missing migration for " + dataType + " v" + currentVersion)
                RETURN data  // Return original
            END IF
            
            currentData = migrationFunc(currentData)
            currentVersion += 1
        END WHILE
        
        RETURN currentData
    END FUNCTION
    
    FUNCTION GetCurrentDataVersion(dataType: SaveDataType) -> Integer:
        SWITCH dataType:
            CASE SDT_PlayerProfile: RETURN CURRENT_PROFILE_VERSION
            CASE SDT_Inventory: RETURN CURRENT_INVENTORY_VERSION
            CASE SDT_Progression: RETURN CURRENT_PROGRESSION_VERSION
            CASE SDT_Settings: RETURN CURRENT_SETTINGS_VERSION
            DEFAULT: RETURN 1
        END SWITCH
    END FUNCTION
    
    // Profile migrations
    FUNCTION MigrateProfile_V1_V2(data: ByteArray) -> ByteArray:
        profileV1 = Deserialize<ProfileDataV1>(data)
        
        profileV2 = NEW ProfileDataV2()
        profileV2.playerID = profileV1.playerID
        profileV2.displayName = profileV1.displayName
        profileV2.accountLevel = profileV1.level
        profileV2.credits = profileV1.credits
        
        // New fields with defaults
        profileV2.premiumCurrency = 0
        profileV2.createdAt = DateTime.Now
        profileV2.lastLoginAt = DateTime.Now
        
        RETURN Serialize(profileV2)
    END FUNCTION
    
    // Inventory migrations
    FUNCTION MigrateInventory_V1_V2(data: ByteArray) -> ByteArray:
        inventoryV1 = Deserialize<InventoryDataV1>(data)
        
        inventoryV2 = NEW InventoryDataV2()
        inventoryV2.stashCapacity = inventoryV1.capacity
        
        // Migrate items with new structure
        FOR EACH itemV1 IN inventoryV1.items:
            itemV2 = NEW ItemDataV2()
            itemV2.itemID = itemV1.itemID
            itemV2.quantity = itemV1.count
            itemV2.durability = 100  // New field, default to max
            itemV2.attachments = []  // New field
            
            inventoryV2.stashItems.Add(itemV2)
        END FOR
        
        RETURN Serialize(inventoryV2)
    END FUNCTION
```

---

### BackupManager

**Purpose:** Save backup and restoration.

```
CLASS BackupManager:
    // Config
    maxBackups: Integer = 5
    autoBackupInterval: Float = 3600.0  // 1 hour
    
    // Paths
    backupDirectory: String
    
    FUNCTION Initialize():
        backupDirectory = LocalStorageManager.GetSaveDirectory() + "Backups/"
        
        IF NOT DirectoryExists(backupDirectory):
            CreateDirectory(backupDirectory)
        END IF
    END FUNCTION
    
    FUNCTION CreateBackup(name: String) -> Boolean:
        backupInfo = NEW BackupInfo()
        backupInfo.name = name
        backupInfo.createdAt = DateTime.Now
        backupInfo.isAutoBackup = false
        
        TRY:
            // Create backup folder
            backupPath = backupDirectory + name + "/"
            CreateDirectory(backupPath)
            
            // Copy all save files
            saveFiles = GetAllSaveFiles()
            totalSize = 0
            
            FOR EACH file IN saveFiles:
                CopyFile(file, backupPath + GetFileName(file))
                totalSize += GetFileSize(file)
            END FOR
            
            backupInfo.sizeBytes = totalSize
            backupInfo.dataVersion = SaveManager.GetCurrentVersion()
            
            // Save backup metadata
            SaveBackupMetadata(backupPath, backupInfo)
            
            // Cleanup old backups
            CleanupOldBackups()
            
            EMIT EVENT "BACKUP_CREATED" WITH (name, totalSize)
            
            RETURN true
            
        CATCH Exception e:
            LOG_ERROR("Backup failed: " + e.Message)
            RETURN false
        END TRY
    END FUNCTION
    
    FUNCTION RestoreBackup(name: String) -> Boolean:
        backupPath = backupDirectory + name + "/"
        
        IF NOT DirectoryExists(backupPath):
            RETURN false
        END IF
        
        TRY:
            // Copy backup files to save directory
            backupFiles = GetFilesInDirectory(backupPath)
            
            FOR EACH file IN backupFiles:
                IF NOT file.EndsWith("metadata.json"):
                    targetPath = LocalStorageManager.GetSaveDirectory() + GetFileName(file)
                    CopyFile(file, targetPath)
                END IF
            END FOR
            
            EMIT EVENT "BACKUP_RESTORED" WITH (name)
            
            RETURN true
            
        CATCH Exception e:
            LOG_ERROR("Restore failed: " + e.Message)
            RETURN false
        END TRY
    END FUNCTION
    
    FUNCTION RestoreLatest(dataType: SaveDataType) -> RestoreResult:
        backups = GetBackups()
        
        // Sort by date descending
        backups.SortByDescending(b => b.createdAt)
        
        FOR EACH backup IN backups:
            backupPath = backupDirectory + backup.name + "/"
            filePath = backupPath + GetFilePath(dataType)
            
            IF FileExists(filePath):
                // Copy this file
                CopyFile(filePath, LocalStorageManager.GetSaveDirectory() + GetFilePath(dataType))
                RETURN RestoreResult.Success(backup.name)
            END IF
        END FOR
        
        RETURN RestoreResult.Failed("No backup found")
    END FUNCTION
    
    FUNCTION DeleteBackup(name: String) -> Boolean:
        backupPath = backupDirectory + name + "/"
        
        IF DirectoryExists(backupPath):
            DeleteDirectory(backupPath, recursive: true)
            
            EMIT EVENT "BACKUP_DELETED" WITH (name)
            
            RETURN true
        END IF
        
        RETURN false
    END FUNCTION
    
    FUNCTION DeleteAllBackups():
        backups = GetBackups()
        
        FOR EACH backup IN backups:
            DeleteBackup(backup.name)
        END FOR
    END FUNCTION
    
    FUNCTION GetBackups() -> List<BackupInfo>:
        result = []
        
        directories = GetSubdirectories(backupDirectory)
        
        FOR EACH dir IN directories:
            metadataPath = dir + "metadata.json"
            
            IF FileExists(metadataPath):
                metadata = LoadBackupMetadata(metadataPath)
                result.Add(metadata)
            END IF
        END FOR
        
        RETURN result
    END FUNCTION
    
    FUNCTION CreateAutoBackup():
        timestamp = DateTime.Now.ToString("yyyyMMdd_HHmmss")
        name = "auto_" + timestamp
        
        backupInfo = NEW BackupInfo()
        backupInfo.isAutoBackup = true
        
        CreateBackup(name)
    END FUNCTION
    
    FUNCTION CleanupOldBackups():
        backups = GetBackups()
        
        // Keep only maxBackups, prioritize manual backups
        autoBackups = backups.Where(b => b.isAutoBackup).SortBy(b => b.createdAt)
        
        WHILE backups.Count > maxBackups AND autoBackups.Count > 0:
            oldest = autoBackups.First()
            DeleteBackup(oldest.name)
            backups.Remove(oldest)
            autoBackups.Remove(oldest)
        END WHILE
    END FUNCTION

STRUCT BackupInfo:
    name: String
    createdAt: DateTime
    sizeBytes: Integer
    dataVersion: Integer
    isAutoBackup: Boolean
```

---

### MatchStateManager

**Purpose:** In-match state persistence for recovery.

```
CLASS MatchStateManager:
    // Config
    matchStateTimeout: Float = 300.0  // 5 minutes
    saveInterval: Float = 30.0
    
    // State
    lastSaveTime: Float = 0.0
    
    FUNCTION SaveMatchState(state: MatchStateData):
        state.savedAt = DateTime.Now
        state.isValid = true
        
        SaveManager.SaveData(SDT_MatchState, state)
    END FUNCTION
    
    FUNCTION HasPendingMatchState() -> Boolean:
        loadResult = SaveManager.LoadData(SDT_MatchState)
        
        IF NOT loadResult.success:
            RETURN false
        END IF
        
        state = loadResult.data AS MatchStateData
        
        IF NOT state.isValid:
            RETURN false
        END IF
        
        // Check if timed out
        elapsed = DateTime.Now - state.savedAt
        
        IF elapsed.TotalSeconds > matchStateTimeout:
            ClearMatchState()
            RETURN false
        END IF
        
        RETURN true
    END FUNCTION
    
    FUNCTION LoadMatchState() -> MatchStateData:
        loadResult = SaveManager.LoadData(SDT_MatchState)
        
        IF loadResult.success:
            RETURN loadResult.data AS MatchStateData
        END IF
        
        RETURN null
    END FUNCTION
    
    FUNCTION ClearMatchState():
        emptyState = NEW MatchStateData()
        emptyState.isValid = false
        
        SaveManager.SaveData(SDT_MatchState, emptyState)
    END FUNCTION
    
    FUNCTION CanRecover() -> Boolean:
        state = LoadMatchState()
        
        IF state == null OR NOT state.isValid:
            RETURN false
        END IF
        
        // Check if match still exists on server
        RETURN GameServer.CheckMatchExists(state.matchID)
    END FUNCTION
    
    FUNCTION Update(deltaTime: Float):
        IF NOT IsInMatch():
            RETURN
        END IF
        
        lastSaveTime += deltaTime
        
        IF lastSaveTime >= saveInterval:
            SaveCurrentMatchState()
            lastSaveTime = 0.0
        END IF
    END FUNCTION
    
    FUNCTION SaveCurrentMatchState():
        state = NEW MatchStateData()
        state.matchID = CurrentMatch.GetID()
        state.mapID = CurrentMatch.GetMapID()
        state.matchTimeRemaining = CurrentMatch.GetTimeRemaining()
        state.playerPosition = LocalPlayer.GetPosition()
        state.playerHealth = LocalPlayer.GetHealth()
        state.playerArmor = LocalPlayer.GetArmor()
        state.currentInventory = LocalPlayer.GetInventorySnapshot()
        
        SaveMatchState(state)
    END FUNCTION

STRUCT MatchStateData:
    matchID: String
    mapID: String
    matchTimeRemaining: Float
    playerPosition: Vector3
    playerHealth: Float
    playerArmor: Float
    currentInventory: List<SavedItemData>
    savedAt: DateTime
    isValid: Boolean = false
```

---

## Data Structures

```
STRUCT PlayerProfileData:
    playerID: String
    displayName: String
    accountLevel: Integer = 1
    currentXP: Integer = 0
    credits: Integer = 0
    premiumCurrency: Integer = 0
    createdAt: DateTime
    lastLoginAt: DateTime
    totalPlayTime: Float = 0.0
    dataVersion: Integer = 1
    checksum: String

STRUCT InventoryData:
    stashItems: List<SavedItemData>
    stashCapacity: Integer = 100
    equippedLoadout: LoadoutData
    dataVersion: Integer = 1
    checksum: String

STRUCT SavedItemData:
    itemID: String
    quantity: Integer = 1
    durability: Float = 100.0
    attachments: List<String>
    customData: Map<String, String>

STRUCT ProgressionData:
    operatorProgress: Map<String, OperatorProgressData>
    completedQuests: Set<String>
    activeQuests: List<ActiveQuestData>
    achievements: Set<String>
    battlePassLevel: Integer = 1
    battlePassXP: Integer = 0
    dataVersion: Integer = 1
    checksum: String

STRUCT SettingsData:
    // Audio
    masterVolume: Float = 1.0
    musicVolume: Float = 0.8
    sfxVolume: Float = 1.0
    voiceVolume: Float = 1.0
    
    // Controls
    sensitivity: Float = 1.0
    invertY: Boolean = false
    aimAssist: Boolean = true
    
    // Graphics
    graphicsQuality: Integer = 2
    targetFPS: Integer = 60
    showFPS: Boolean = false
    
    // UI
    hudScale: Float = 1.0
    minimapSize: Float = 150.0
    crosshairColor: Color = #FFFFFF
    
    dataVersion: Integer = 1

STRUCT StatisticsData:
    totalMatchesPlayed: Integer = 0
    totalWins: Integer = 0
    totalKills: Integer = 0
    totalDeaths: Integer = 0
    totalDamageDealt: Float = 0.0
    totalItemsLooted: Integer = 0
    totalExtractions: Integer = 0
    totalPlayTime: Float = 0.0
    dataVersion: Integer = 1
```

---

## Auto-Save Configuration

```
STRUCT AutoSaveConfig:
    // Triggers
    saveOnMatchComplete: Boolean = true
    saveOnLevelUp: Boolean = true
    saveOnQuestComplete: Boolean = true
    saveOnPurchase: Boolean = true
    saveOnSettingsChange: Boolean = true
    saveOnInventoryChange: Boolean = true
    
    // Intervals
    periodicSaveInterval: Float = 60.0
    minTimeBetweenSaves: Float = 5.0
    
    // During Match
    saveMatchStateOnDeath: Boolean = true
    matchStateSaveInterval: Float = 30.0
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] SaveManager core
- [ ] LocalStorageManager
- [ ] Player profile save/load
- [ ] Inventory save/load
- [ ] Settings save/load

### MEDIUM Priority 🟡
- [ ] CloudProvider implementation
- [ ] SyncManager
- [ ] DataValidator
- [ ] EncryptionManager
- [ ] Conflict resolution UI

### LOW Priority 🟢
- [ ] MigrationManager
- [ ] BackupManager
- [ ] MatchStateManager
- [ ] Advanced sync strategies
- [ ] Data compression

---

## Testing Checklist

- [ ] Local save/load works offline
- [ ] Data persists across app restarts
- [ ] Cloud sync uploads correctly
- [ ] Cloud sync downloads correctly
- [ ] Conflict detection works
- [ ] Conflict resolution UI shows
- [ ] Data migration updates old saves
- [ ] Checksums detect corruption
- [ ] Encryption protects data
- [ ] Backup/restore works
- [ ] Match state recovery works
- [ ] Auto-save triggers correctly

---

**[← Back to Index](../README.md)** | **[Next: Tutorial System →](./TutorialSystem.md)**


