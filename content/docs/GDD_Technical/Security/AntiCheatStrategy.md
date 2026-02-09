# Security & Anti-Cheat Strategy

**[← Back to Index](../README.md)**

---

## 🛡️ The Concept of Trust
**"Never Trust the Client."**
The core principle is simple: The Client sends *intent*, not *results*.

### 1. Server-Side Authority (Validation)
Everything critical happens on the Server.
*   **Ammo:** Client says "I fired 5 rounds." Server subtracts 5 rounds. Server *does not* trust client's ammo count.
*   **Movement:** Client sends Input (Forward, Right). Server calculates Position = Velocity * Time.
    *   **Maximum Speed Check:** If distance > `MaxSpeed * DeltaTime + Tolerance` -> Flag for cheating.
*   **Health:** Only Server can decrease Health. Client only plays damage effects.

### 2. Encryption (Packet Protection)
*   **Protocol:** Use `DTLS` (Datagram Transport Layer Security) over UDP.
*   **Key Exchange:** Secured via HTTPS login (Master Server).
*   **Replay Protection:** Unique `SequenceNumber` per packet. Old packets are discarded.

---

## 🚫 Common Exploits & Mitigation

### 1. Speed Hacks (Teleport)
*   **Detect:** Compare `LastKnownLocation` + `MaxAllowedDistance`.
*   **Result:** Rubberband back (1st offense) -> Kick (3rd offense within 1 min).
*   **Heuristics:** Track average velocity over 10s.

### 2. Wallhack (ESP)
*   **Mitigation:** `Network Culling` (Don't send data about enemies behind walls).
    *   We use the **Replication Graph** to stop replicating distant/occluded actors entirely.
*   **Obfuscation:** Encrypt bone locations in memory (slower but harder to read).

### 3. Aimbot (Auto-Target)
*   **Detection:** Only Server can analyze unnatural mouse movement.
    *   **Snap Check:** 0ms aim adjustment to head -> Flag.
    *   **Recoil:** 0 vertical recoil while firing full auto -> Flag.
    *   **Stats:** Headshot % > 80% over 5 matches -> Review.

### 4. Loot Vacuum (Instant Pickup)
*   **Validation:**
    *   **Distance:** Check distance to item < 3m.
    *   **Line of Sight:** Can player see item? (Trace check).
    *   **Inventory Space:** Can item fit? (Tetris validation).

---

## 👮‍♂️ Report System (Community Policing)

### In-Game Reporting
*   **Categories:** Aimbot, Wallhack, Speedhack, Toxic Voice.
*   **Replay:** Server saves a low-tick replay of the kill-cam (5s before death).
*   **Trust Score:** Players with high accuracy/KD get flagged for manual review if reported frequently.

### Hardware Ban (HWID)
*   **Identifier:** Motherboard Serial + HDD Serial + MAC Address.
*   **Database:** Shared ban list across all accounts.
*   **Review:** Human review required for permanent bans.

---
