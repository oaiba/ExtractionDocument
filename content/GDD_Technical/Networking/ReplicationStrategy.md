---
title: "Replication Strategy & Bandwidth Optimization"
type: docs
---

##  The Problem: High Density
Extraction Shooters have a unique networking challenge: **Huge Maps + High AI Count + High Loot Count.**
Standard Unreal `NetCullDistance` is not enough.

##  Replication Graph

We implement a custom `UReplicationGraph` to manage the immense number of replicated actors.

### 1. The Grid (Spatialization)
*   **Concept:** The map is divided into a 2D grid cells (e.g., 50x50 meters).
*   **Logic:**
    *   Dynamic Actors (AI, Players) are registered to their current cell.
    *   Clients only receive updates from actors in their cell + adjacent cells.
    *   **Result:** A client on the West side never processes data from the East side.

### 2. Dormancy (Sleeping Actors)
*   **Loot Containers:** By default, all containers are `DORM_Initial`.
    *   *Server:* Never replicates container state (Open/Close) until a player is within 5m interaction range.
    *   *Client:* Only sees static mesh.
*   **AI (Far):** AI beyond 150m tick at 1hz on Server and do NOT replicate movement to clients (Server-side simulation only).

### 3. Priority & Frequency
| Actor Type | NetUpdateFrequency (Hz) | Priority |
| :--- | :--- | :--- |
| **Player (Active)** | 60Hz | 1.0 (Highest) |
| **Player (Far > 50m)** | 20Hz | 0.8 |
| **Enemy AI (Combat)** | 30Hz | 0.9 |
| **Enemy AI (Patrol)** | 10Hz | 0.5 |
| **Loot Item** | 0Hz (On Spawn only) | 0.1 |
| **Door/Gate** | OnEvent | 1.0 |

---

##  Loot Replication (The "Thousands of Items" Problem)

### Structural Items (Containers)
*   Use `NetDormancy` heavily.
*   Only replicate the *State* (Open/Closed/Locked), never the *Contents* array to all clients.
*   **Contents** are only sent via `Client_` RPC to the *specific player* who opens the UI.

### Dropped Items (Physics)
*   **Optimization:** When an item is dropped:
    1.  Spawn `BP_LootItem` (Replicated).
    2.  Wait for Physics to settle (Sleep).
    3.  Server destroys `StaticMeshComponent` physics and replaces it with a simple, non-ticking location update.
    4.  Client interpolates to rest position.

---

##  Weapon Replication

### 1. Firing (Client-Side Prediction)
*   **Client:** plays muzzle flash & audio *immediately* (Zero latency feel).
*   **Server:** Validates ammo and cooldown.
*   **Replication:** Do NOT replicate every bullet.
    *   Use `Burst` replication: "Player A started firing at time T".
    *   Remote clients simulate the burst.

### 2. Projectiles vs. Hitscan
*   **Hitscan (Close < 50m):** Instant trace. Efficient.
*   **Projectile (Long > 50m):**
    *   Spawn "Fake" projectile on Client (Visual only).
    *   Server traces trajectory.
    *   Do NOT replicate an Actor for every bullet. Use `FVector` arrays in a compressed struct if ballistic visuals are needed.

---

##  Bandwidth Budget

**Target:** < 40KB/s per client.

*   **Movement:** 60% of budget. Compressed `FVector_NetQuantize10`.
*   **Actions:** 20% (Firing, interacting).
*   **Environment:** 10% (Doors, lights).
*   **VOIP:** 10% (Ideally separate channel/server).


