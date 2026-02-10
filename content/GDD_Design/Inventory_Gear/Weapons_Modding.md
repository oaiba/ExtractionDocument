---
title: "Weapon Modding (Gunsmith)"
weight: 3
type: docs
---

## The Gunsmith Philosophy

Weapons are modular platforms. A "Gun" is just a Receiver; everything else is an attachment.

## Anatomy of a Weapon

### Vital Parts (Required to Fire)
1.  **Receiver:** The core ID of the gun.
2.  **Barrel:** Defines velocity, accuracy, and recoil base.
3.  **Gas Block:** (Gas-operated guns) Cycles the bolt.
4.  **Bolt Carrier Group:** The firing mechanism.
5.  **Grip:** Ergonomics interface.

### Tactical Mods
1.  **Muzzle:**
    *   *Brake:* -Recoil, +Loudness (Side blast).
    *   *Suppressor:* -Sound, -Recoil, +Heat, -Ergonomics (Heavy).
2.  **Handguard:** Rail space for attachments.
3.  **Tactical Device:**
    *   *Flashlight:* Blinds enemies in CQC.
    *   *Laser:* Increases hip-fire accuracy (tightens spread mechanically).
    *   *IR Light:* Only visible under Night Vision (NVG).
4.  **Optics:**
    *   *Height Over Bore:* Close range shots land *lower* than the reticle because the scope is physically higher than the barrel.
5.  **Canted Sights:** Backup red dot mounted at 45 degrees for CQB.

---

## Weapon Statistics (The Meta)

### 1. Ergonomics (Ergo)
*   **ADS Speed:** How fast the gun snaps to the eye.
*   **Stamina Hold:** How long you can aim steady before arms shake.
*   **Noise:** Aiming down sights with low Ergo makes a "clothing rustle" sound.

### 2. Recoil Control
*   **Vertical:** Climb.
*   **Horizontal:** Drift.
*   **Camera Recoil:** Visual shake separate from the gun's physical recoil.
*   **Convergence:** How fast the crosshair returns to center after firing.

### 3. MOA (Accuracy)
*   **Minutes of Angle:** Dispersion at 100m.
*   **Durability Factor:** As durability drops <50%, MOA increases drastically (bullets go sideways).

---

## Weapon Malfunctions & Heat

### Malfunctions
Driven by Durability and Ammo Quality.
1.  **Failure to Feed:** Bullet stuck. -> *Fix: Rack Bolt (Shift+T).*
2.  **Stovepipe:** Casing stuck in ejection port. -> *Fix: Check Chamber + Rack Bolt.*
3.  **Hard Jam:** Bolt physically stuck. -> *Fix: Crouch, remove mag, 5-second animation.*

### Overheating
*   **Visual:** Barrel glows red. Heat shimmer distorts scope view (Mirage).
*   **Mechanic:** Firing full auto continuously causes the gun to jam immediately.
*   **Suppressors:** Reach critical heat faster than muzzle brakes.

---