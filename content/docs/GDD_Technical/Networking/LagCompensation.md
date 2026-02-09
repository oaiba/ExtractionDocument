# Lag Compensation & Netcode Logic

**[← Back to Index](../README.md)** | **[Replication Strategy ←](./ReplicationStrategy.md)**

---

## 🏃 The Problem: "Peeker's Advantage"
In shooters, the client is always ahead of the server. When Player A peeks a corner, they see Player B *before* the server knows Player A has moved. This creates unfair kills.

### 1. Server-Side Rewind (The Solution)

When a player fires a hitscan weapon:
1.  **Client:** Sends `InputFire(TimeStamp)` to Server.
2.  **Server:** Receives packet 50ms later.
3.  **Rewind:** Before checking collision, **Server rewinds ALL other players** to where they were at `TimeStamp`.
4.  **Check:** Did the shot hit the *rewound* position?
5.  **Result:** Grant damage, even if the enemy is currently safe behind a wall on the Server.

> **Why?** It favors the shooter's screen ("If I hit them on my screen, they should die").

### 2. Client-Side Prediction (Movement)

*   **Prediction:** Client simulates movement *instantly*.
*   **Correction:** Server checks position. If Client is > 50 units (error tolerance) away from Server, force *teleport* back (Rubberbanding).
    *   **Tolerance:** 50 units (Close), 150 units (Far/Lagging).
    *   **Smoothing:** `UCharacterMovementComponent` interpolates the correction over 0.2s to reduce jarring snaps.

---

## 🛡️ Hit Registration & Validation

### 1. Headshot Detection
*   **Problem:** Clients can fake headshots easily.
*   **Validation:**
    *   Server checks `BoneName` hit.
    *   Server checks angle of incidence (Did bullet come from front?).
    *   Server checks if `BoneName` was occluded by `Chest` or `Arm` (Penetration).

### 2. Projectile Physics
*   **Ballistics:** Simulated locally for visuals.
*   **Trajectory:** Server calculates trajectory based on `MuzzleVelocity`, `Gravity`, and `Drag`.
*   **Sync:** Every 0.5s, Server sends `ProjectileCorrection` if discrepancy > 1m.

---

## 🕰️ Time Management (Clock Sync)

### Server Time vs. Client Time
*   **GameTime:** Synced at login. Client maintains local `ServerTimeOffset`.
*   **Ping:** Calculated every 1s using `ICMP` or round-trip packet.
*   **Jitter:** Filtered using a rolling average of last 10 pings.

### High Ping Mitigation (> 150ms)
*   **Disable Rewind:** If Ping > 200ms, Server *ignores* rewind requests to prevent "dying around corners" for low-ping players.
*   **Prediction Limit:** Visuals stop predicting enemy movement beyond 300ms (preventing teleporting enemies).

---
