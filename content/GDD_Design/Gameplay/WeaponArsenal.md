---
title: "Weapon Arsenal & Combat Systems"
type: docs
weight: 25
---

## Combat Philosophy

Combat in Extraction Shooter is built on five principles:

1. **Tactical Over Twitch** — Positioning and decision-making matter more than raw reflexes. The top-down camera amplifies this by giving players full spatial awareness.
2. **Weapon Identity** — Every weapon category has a distinct role. No single "best gun for all situations" exists.
3. **Risk vs. Reward** — Better weapons extract more value from a raid but carry a heavier loss penalty if you die.
4. **Skill Expression** — High skill ceiling with recoil pattern control, ammo selection, and positional play.
5. **Mobile Optimized** — All mechanics designed with touch controls in mind: gyro recoil assist, large hit targets, haptic feedback.

> **Cross-References:** [Weapon Attachment System](Weapon_Attachment_System.md) — in-depth attachment slot rules, stat trade-offs, and in-raid swap system; [Combat Feel (Top-Down)](Combat_Feel_Topdown.md) — recoil cone model, suppression, cover footprint; [Items & Gear](ItemsAndGear.md) — armor, ammo stacks, throwables as loot items; [Loot Table Design](Loot_Table_Design.md) — weapon rarity spawn rates per zone; [Gear Mechanics](Gear_Mechanics.md) — how weapon weight affects loadout.

---

## Primary Weapon Categories

### 1. Assault Rifles (AR)

**Role:** Versatile all-rounders, effective at medium range.

| Property | Value |
| :-------- | :---- |
| Damage | 30–40 per shot |
| Fire Rate | 600–750 RPM |
| Effective Range | 30–50 m |
| Magazine | 30 rounds |
| Recoil | Moderate, controllable |

**Tactical Notes:** Strong opening weapon. Good for holding angles. Versatile in most combat scenarios. Magazine management is critical in sustained fights.

#### AR Full Reference

| Code Name | Display Name | Caliber | Rarity | Damage | RPM | Mag | Range (m) | Recoil | Penetration | Value ($) | Notes |
| :-------- | :----------- | :------ | :----- | :----: | :-: | :-: | :-------: | :----- | :---------- | --------: | :---- |
| WPN_AR_AK47 | AK-47 | 7.62×39mm | Common | 35 | 600 | 30 | 40 | High | Medium | 1,200 | High damage, cheap, reliable |
| WPN_AR_M4A1 | M4A1 | 5.56×45mm | Uncommon | 32 | 750 | 30 | 45 | Low | Medium | 3,500 | Very controllable, versatile |
| WPN_AR_SCAR | SCAR-H | 7.62×51mm | Rare | 40 | 625 | 20 | 50 | Medium | High | 7,000 | Hard-hitting, medium recoil |
| WPN_AR_HK416 | HK416 | 5.56×45mm | Rare | 34 | 850 | 30 | 48 | Low | Medium | 6,500 | High fire rate, stable |
| WPN_AR_AUG | Steyr AUG | 5.56×45mm | Uncommon | 30 | 680 | 30 | 42 | Very Low | Low | 3,000 | Built-in scope, compact |

---

### 2. Submachine Guns (SMG)

**Role:** Close-quarters specialist, high mobility.

| Property | Value |
| :-------- | :---- |
| Damage | 20–28 per shot |
| Fire Rate | 900–1,100 RPM |
| Effective Range | 10–25 m |
| Magazine | 25–50 rounds |
| Recoil | High but manageable |

**Tactical Notes:** Excellent for building clearing. Grants high movement speed. Weak at range. High ammo consumption — carry extras.

#### SMG Full Reference

| Code Name | Display Name | Caliber | Rarity | Damage | RPM | Mag | Range (m) | Recoil | Mobility | Value ($) | Notes |
| :-------- | :----------- | :------ | :----- | :----: | :-: | :-: | :-------: | :----- | :------- | --------: | :---- |
| WPN_SMG_MP5 | MP5 | 9×19mm | Common | 24 | 900 | 30 | 20 | Medium | High | 800 | CQB standard, reliable |
| WPN_SMG_VECTOR | Vector .45 | .45 ACP | Rare | 28 | 1,100 | 25 | 18 | Very Low | High | 5,500 | Ultra-fast fire, low recoil |
| WPN_SMG_P90 | P90 | 5.7×28mm | Uncommon | 22 | 1,000 | 50 | 22 | Medium | Very High | 2,800 | Large mag, suppressive |
| WPN_SMG_UMP45 | UMP-45 | .45 ACP | Common | 26 | 700 | 25 | 25 | Low | High | 1,500 | Balanced, affordable |
| WPN_SMG_MP7 | MP7 | 4.6×30mm | Rare | 23 | 950 | 40 | 28 | Low | Very High | 6,000 | High penetration, compact |

---

### 3. Shotguns

**Role:** Point-blank devastation, room clearing.

| Property | Value |
| :-------- | :---- |
| Damage | 15–25 per pellet × 8 pellets |
| Fire Rate | 60–300 RPM |
| Effective Range | 5–15 m |
| Capacity | 4–20 shells |

**Tactical Notes:** Devastating in confined spaces — useless at range. High risk/high reward. Limited ammo capacity demands careful counting.

#### Shotgun Full Reference

| Code Name | Display Name | Caliber | Rarity | Dmg/Pellet | Pellets | RPM | Capacity | Range (m) | Value ($) | Notes |
| :-------- | :----------- | :------ | :----- | :--------: | :-----: | :-: | :------: | :-------: | --------: | :---- |
| WPN_SG_R870 | Remington 870 | 12 Gauge | Common | 20 | 8 | 60 | 6 | 12 | 600 | Pump-action, one-shot potential |
| WPN_SG_M590 | Mossberg 590 | 12 Gauge | Common | 18 | 8 | 70 | 8 | 14 | 900 | More capacity, tactical |
| WPN_SG_AA12 | AA-12 | 12 Gauge | Epic | 18 | 8 | 300 | 20 | 15 | 14,000 | Full-auto, devastating CQB |
| WPN_SG_SPAS12 | SPAS-12 | 12 Gauge | Rare | 22 | 8 | 80 | 6 | 10 | 4,500 | Pump/auto switch, tight spread |
| WPN_SG_SAIGA | Saiga-12 | 12 Gauge | Uncommon | 16 | 8 | 200 | 10 | 16 | 3,200 | Semi-auto, magazine-fed |

---

### 4. Designated Marksman Rifles (DMR)

**Role:** Semi-auto precision at medium-long range; bridge between AR and Sniper. Faster follow-up than bolt-action; lower per-shot damage than sniper.

| Property | Value |
| :-------- | :---- |
| Damage | 55–80 per shot |
| Fire Rate | 120–220 RPM (semi-auto) |
| Effective Range | 40–80 m |
| Magazine | 10–20 rounds |

**Tactical Notes:** 2–3 shot kills at optimal range. Reposition between shots; use cover for reload. Best used from positions between AR and Sniper engagement ranges. See [Weapon Categories Deep Dive](../Weapons/Weapon_Categories_Deep_Dive.md) for DMR doctrine and matchups.

#### DMR Full Reference

| Code Name | Display Name | Caliber | Rarity | Damage | RPM | Mag | Range (m) | Value ($) | Notes |
| :-------- | :----------- | :------ | :----- | :----: | :-: | :-: | :-------: | --------: | :---- |
| WPN_DMR_SKS | SKS | 7.62×39mm | Common | 55 | 120 | 10 | 45 | 2,000 | Budget DMR; semi-auto |
| WPN_DMR_SVD | SVD Dragunov | 7.62×54mmR | Uncommon | 75 | 180 | 10 | 80 | 5,000 | Semi-auto; faster follow-up |
| WPN_DMR_SR25 | SR-25 | 7.62×51mm | Rare | 78 | 200 | 20 | 75 | 9,000 | Precision marksman |
| WPN_DMR_MK14 | MK 14 EBR | 7.62×51mm | Epic | 80 | 220 | 20 | 80 | 14,000 | Peak DMR; versatile |

---

### 5. Sniper Rifles

**Role:** Long-range elimination, overwatch.

| Property | Value |
| :-------- | :---- |
| Damage | 65–130 per shot |
| Fire Rate | 35–180 RPM |
| Effective Range | 50–150+ m |
| Magazine | 5–20 rounds |

**Tactical Notes:** Requires positioning and patience. Top-down perspective makes sniping unique — best used from elevated positions or long corridors. Vulnerable if rushed.

#### Sniper Rifle Full Reference

| Code Name | Display Name | Caliber | Rarity | Damage | RPM | Mag | Range (m) | Bullet Vel. | Value ($) | Notes |
| :-------- | :----------- | :------ | :----- | :----: | :-: | :-: | :-------: | :---------- | --------: | :---- |
| WPN_SR_M24 | M24 | 7.62×51mm | Rare | 85 | 50 | 5 | 100 | Fast | 8,000 | Bolt-action, reliable |
| WPN_SR_AWP | AWP | .338 Lapua | Epic | 120 | 40 | 5 | 120 | Very Fast | 16,000 | One-shot chest kill |
| WPN_SR_M107 | Barrett M107 | .50 BMG | Legendary | 130 | 35 | 10 | 150 | Fast | 25,000 | Anti-materiel, penetrates all |
| WPN_SR_VSS | VSS Vintorez | 9×39mm | Rare | 65 | 120 | 20 | 60 | Medium | 7,500 | Integrated suppressor, subsonic |

---

### 6. Light Machine Guns (LMG)

**Role:** Suppression, sustained fire, area denial.

| Property | Value |
| :-------- | :---- |
| Damage | 30–38 per shot |
| Fire Rate | 600–1,200 RPM |
| Effective Range | 30–60 m |
| Magazine | 75–100 rounds |

**Tactical Notes:** Heavy weapon — reduces movement speed. Excellent for holding choke points. Long reload creates a vulnerability window. Bipod reduces recoil when prone/crouched.

#### LMG Full Reference

| Code Name | Display Name | Caliber | Rarity | Damage | RPM | Mag | Range (m) | Bipod | Mobility | Value ($) | Notes |
| :-------- | :----------- | :------ | :----- | :----: | :-: | :-: | :-------: | :---: | :------- | --------: | :---- |
| WPN_LMG_M249 | M249 SAW | 5.56×45mm | Rare | 32 | 750 | 100 | 55 | Yes | Low | 9,000 | Suppressive fire king |
| WPN_LMG_PKM | PKM | 7.62×54mmR | Uncommon | 38 | 650 | 75 | 60 | Yes | Very Low | 6,000 | High damage, heavy |
| WPN_LMG_MG42 | MG42 | 7.62×51mm | Epic | 35 | 1,200 | 100 | 50 | Yes | Very Low | 15,000 | Extreme rate — "Buzzsaw" |
| WPN_LMG_RPK | RPK-74 | 7.62×39mm | Uncommon | 30 | 600 | 75 | 45 | No | Medium | 4,500 | Mobile LMG, no bipod needed |

---

## Secondary Weapons

### Pistols

**Role:** Backup weapon, last resort, silent option.

| Code Name | Display Name | Caliber | Rarity | Damage | RPM | Mag | Range (m) | Value ($) | Notes |
| :-------- | :----------- | :------ | :----- | :----: | :-: | :-: | :-------: | --------: | :---- |
| WPN_PISTOL_GLOCK | Glock 19 | 9×19mm | Common | 25 | 400 | 17 | 25 | 300 | Reliable sidearm |
| WPN_PISTOL_DEAGLE | Desert Eagle | .50 AE | Rare | 55 | 200 | 7 | 35 | 2,500 | Hand cannon, skill-based |
| WPN_PISTOL_USP | USP-S | .45 ACP | Uncommon | 28 | 350 | 12 | 30 | 1,200 | Integrated suppressor |
| WPN_PISTOL_M1911 | M1911 | .45 ACP | Common | 40 | 280 | 7 | 28 | 500 | Classic .45, reliable |
| WPN_PISTOL_P226 | SIG P226 | 9×19mm | Uncommon | 30 | 380 | 15 | 32 | 1,500 | Balanced, accurate |
| WPN_PISTOL_REVOLVER | .357 Magnum | .357 Mag | Rare | 60 | 180 | 6 | 30 | 2,000 | High damage; no reload (cylinder) |

### Melee Weapons

| Code Name | Display Name | Rarity | Slash Dmg | Backstab Dmg | Range (m) | Speed | Value ($) | Notes |
| :-------- | :----------- | :----- | :-------: | :----------: | :-------: | :---- | --------: | :---- |
| WPN_MELEE_KNIFE | Combat Knife | Default | 50 | 100 | 2.0 | Fast | 100 | Default melee — always equipped |
| WPN_MELEE_AXE | Tactical Axe | Rare | 75 | 150 | 2.5 | Medium | 800 | Better reach, more damage |
| WPN_MELEE_MACHETE | Machete | Uncommon | 65 | 130 | 2.3 | Fast | 500 | Fast slashing |
| WPN_MELEE_BATON | Stun Baton | Rare | 40 | 80 | 2.0 | Very Fast | 1,200 | Stuns enemies 2 sec |

---

## Ammunition System

### Ammo Philosophy

Ammunition is the bridge between weapon and target. While the gun dictates handling, the **Ammo Type** dictates the impact result. Our caliber system creates shared ammo pools across weapon categories — a strategic inventory choice.

### Ammo Variants (Per Caliber)

| Variant | Role | Penetration | Flesh Damage | Cost |
| :------ | :--- | :---------- | :----------- | :--- |
| **Standard (FMJ/Ball)** | Balanced | Medium | Medium | Cheap |
| **Armor Piercing (AP)** | Armor Destroyer | High → Extreme | Reduced (over-pen) | Expensive, rare |
| **Hollow Point (HP)** | Flesh Tearer | None → Low | Very High, causes bleeding | Moderate |
| **Tracer** | Visual Feedback | Mixed | Mixed | Standard |

**AP Use Case:** Late-game PvP, boss hunting.
**HP Use Case:** "Leg meta" (unarmored limbs), AI scavs.
**Tracer Trade-off:** Visible flight path helps aiming — but reveals your position to enemies.

### Full Caliber Reference Table

| Caliber | Type | Pen Class | Flesh Dmg | Velocity | Used By |
| :------ | :--- | :-------: | :-------: | :------- | :------ |
| **9×19mm** | FMJ | Low (2) | 50 | 340 m/s | Glock, MP5, P226 |
| | AP 6.3 | Medium (3) | 35 | 400 m/s | |
| | RIP (HP) | None (0) | 90 | 300 m/s | |
| **.45 ACP** | FMJ | Low (2) | 60 | 285 m/s | M1911, Vector, USP |
| | Hydro (HP) | None (1) | 95 | 290 m/s | |
| **5.56×45mm** | M855 (Std) | Medium (3) | 45 | 900 m/s | M4A1, HK416, AUG, M249 |
| | M995 (AP) | High (5) | 38 | 980 m/s | |
| | Warmage (HP) | Low (1) | 70 | 880 m/s | |
| **7.62×39mm** | PS (Std) | Medium (3) | 55 | 700 m/s | AK-47, RPK |
| | BP (AP) | High (5) | 48 | 730 m/s | |
| **7.62×51mm** | M80 (Std) | High (4) | 70 | 830 m/s | SCAR-H, M24, MG42 |
| | M61 (AP) | Extreme (6) | 60 | 850 m/s | |
| **7.62×54mmR** | LPS (Std) | High (4) | 78 | 800 m/s | SVD, PKM |
| | SNB (AP) | Extreme (6) | 65 | 820 m/s | |
| **.338 Lapua** | AP | Ultimate (7) | 110 | 950 m/s | AWP |
| **12 Gauge** | Buckshot | Low (1) | 30×8 | 380 m/s | All Shotguns |
| | Slug | Medium (3) | 140 | 420 m/s | |
| | Flechette | High (4) | 20×8 | 400 m/s | |
| **.50 BMG** | Anti-Materiel | Extreme+ (8) | 150 | 900 m/s | Barrett M107 only |

---

## Attachment System

> **Full attachment slot system, conflict rules, and in-raid swapping** → see [Weapon Attachment System](Weapon_Attachment_System.md).

This section provides the **complete item reference** for attaching gear to weapons.

### Optics & Sights

| Code Name | Display Name | Rarity | Magnification | Effect | Drawback | Value ($) | Compatible |
| :-------- | :----------- | :----- | :-----------: | :----- | :------- | --------: | :--------- |
| ATT_OPTIC_REDDOT | Red Dot Sight | Common | 1.0× | +10% accuracy | None | 200 | AR, SMG, LMG |
| ATT_OPTIC_HOLO | Holographic Sight | Uncommon | 1.0× | +15% accuracy, clearer reticle | None | 500 | AR, SMG, LMG |
| ATT_OPTIC_ACOG | ACOG 4× Scope | Rare | 4.0× | +30m effective range | −10% ADS speed | 1,500 | AR, Sniper |
| ATT_OPTIC_THERMAL | Thermal Scope | Epic | 2.5× | See through smoke/fog | −20% ADS, battery | 5,000 | AR, Sniper, LMG |
| ATT_OPTIC_SNIPER | 8× Sniper Scope | Rare | 8.0× | +50m range, precision | −30% ADS speed | 2,000 | Sniper only |
| ATT_OPTIC_REFLEX | Reflex Sight | Common | 1.0× | +8% accuracy, fast ADS | None | 150 | All weapons |

### Barrels

| Code Name | Display Name | Rarity | Effect | Drawback | Value ($) | Compatible |
| :-------- | :----------- | :----- | :----- | :------- | --------: | :--------- |
| ATT_BARREL_SUPPRESSOR | Suppressor | Uncommon | −80% sound, no muzzle flash | −10% range | 800 | All primary |
| ATT_BARREL_COMP | Compensator | Common | −20% vertical recoil | +5% horizontal recoil | 300 | AR, LMG, SMG |
| ATT_BARREL_EXTENDED | Extended Barrel | Uncommon | +15% range | +10% recoil | 500 | AR, Sniper |
| ATT_BARREL_HEAVY | Heavy Barrel | Rare | +20% damage range, +5% damage | −10% mobility | 1,200 | AR, Sniper |
| ATT_BARREL_LIGHTWEIGHT | Lightweight Barrel | Common | +10% ADS speed | −5% range | 200 | SMG, AR |

### Stocks

| Code Name | Display Name | Rarity | Effect | Drawback | Value ($) | Compatible |
| :-------- | :----------- | :----- | :----- | :------- | --------: | :--------- |
| ATT_STOCK_TACTICAL | Tactical Stock | Common | +15% aim stability | None | 250 | AR, Sniper, LMG |
| ATT_STOCK_LIGHT | Light Stock | Uncommon | +12% movement speed | −8% aim stability | 400 | SMG, AR |
| ATT_STOCK_HEAVY | Heavy Stock | Rare | −25% recoil | −8% movement speed | 900 | AR, LMG, Sniper |
| ATT_STOCK_SKELETON | Skeleton Stock | Uncommon | +15% ADS speed | −10% recoil control | 500 | SMG, AR |

### Magazines

| Code Name | Display Name | Rarity | Effect | Drawback | Value ($) | Compatible |
| :-------- | :----------- | :----- | :----- | :------- | --------: | :--------- |
| ATT_MAG_EXTENDED | Extended Mag | Common | +10 rounds | −5% reload speed | 300 | AR, SMG, Pistol |
| ATT_MAG_FAST | Fast Mag | Uncommon | +40% reload speed | None | 600 | All |
| ATT_MAG_DRUM | Drum Mag | Rare | +20–30 rounds | −10% move, −20% reload | 1,500 | AR, SMG, LMG |
| ATT_MAG_TACTICAL | Tactical Mag | Uncommon | +5 rounds, +20% reload | None | 800 | AR, SMG |

### Underbarrel

| Code Name | Display Name | Rarity | Effect | Drawback | Value ($) | Compatible |
| :-------- | :----------- | :----- | :----- | :------- | --------: | :--------- |
| ATT_UNDER_FOREGRIP | Foregrip | Common | −15% horizontal recoil | −5% ADS speed | 250 | AR, LMG, SMG |
| ATT_UNDER_ANGLED | Angled Grip | Uncommon | −10% recoil, +10% ADS | None | 500 | AR, SMG |
| ATT_UNDER_LASER | Laser Sight | Common | +25% hip-fire accuracy | Visible to enemies | 200 | All |
| ATT_UNDER_LIGHT | Tactical Light | Common | +Visibility in dark (+30m) | Visible to enemies | 150 | All |
| ATT_UNDER_BIPOD | Bipod | Rare | −40% recoil when prone/crouched | +1s setup time | 800 | LMG, Sniper |

### Attachment Slots by Rarity

| Rarity | Attachment Slots |
| :----- | :-------------- |
| Common | 2 slots |
| Uncommon | 3 slots |
| Rare | 4 slots |
| Epic / Legendary | 5 slots (Legendary: 5 + unique bonus slot) |

---

## Combat Mechanics

### Damage System

```
Base Damage → Armor Absorption → Health Damage
```

**Armor Mechanics:**
- Absorbs 70% of incoming damage (at full condition)
- Depletes with each hit — does not regenerate during raid
- Must be replaced or repaired (Safe House repair bench)
- Armor class determines which ammo types can penetrate — see caliber table above

**Health Model:**
- Base: 100 HP
- No auto-regeneration — heals require medical items (see [Items & Gear](ItemsAndGear.md))
- Bleeds if struck (slow HP drain until bandaged)
- Body-part-specific HP tracked internally (see [Medical System](Medical_System.md) for detail)

### Hit Location Multipliers

| Location | No Protection | Light Helmet (Common) | Medium Helmet (Rare) | Heavy Helmet (Epic) |
| :------- | :-----------: | :-------------------: | :------------------: | :-----------------: |
| **Head** | ×2.0 | ×1.5 | ×1.3 | ×1.1 |
| **Chest** | ×1.0 | — | — | — |
| **Arms** | ×0.9 | — | — | — |
| **Legs** | ×0.8 | — | — | — |

### Recoil System

**Recoil Patterns:**
- Each weapon has a unique 2D recoil pattern (vertical pull + horizontal drift)
- First-shot accuracy bonus — initial bullet more precise
- Crouching reduces recoil by 20%
- Burst firing more accurate than full-auto

**Mobile Adaptations:**
- Gyroscope support maps recoil to device tilt
- Auto-recoil compensation option (reduced — rewards manual control)
- Haptic feedback per shot at adjustable intensity

### Ballistics

| Range | System |
| :---- | :----- |
| < 20m | Hitscan — instant result |
| > 20m | Projectile — travel time applies |

**Penetration Table:**

| Material | Penetration | Damage Loss |
| :------- | :---------- | :---------- |
| Wood | Full | −20% |
| Thin Metal | 50% chance | −40% |
| Concrete | None | — |
| Players | Over-penetration possible | Minimal (hits target behind) |

### Cover System

| Type | Materials | Penetrable | Destructible |
| :--- | :-------- | :--------: | :----------: |
| **Soft Cover** | Wood crates, thin walls | ✅ Yes | ✅ Yes |
| **Hard Cover** | Concrete, vehicles, metal | ❌ No | ❌ No |

**Cover Mechanics:**
- Auto-crouch near cover (optional — settings toggle)
- Peek left/right directional buttons
- Blind fire option — fires without exposing character body (reduced accuracy)

---

## Throwables & Equipment

See [Items & Gear](ItemsAndGear.md) for full item tables with stack sizes, weights, and grid dimensions.

### Grenade Quick Reference

| Grenade | Damage | Radius | Fuse | Special |
| :------ | :----: | :----: | :--: | :------ |
| **Frag** | 100 direct / 50–10 falloff | 8m | 3s | Cookable (hold to reduce fuse) |
| **Flashbang** | 0 | 10m | 1.5s | 5s blind + disorient |
| **Smoke** | 0 | 8m | 2s | 15s cloud — blocks vision (not thermal) |
| **EMP** | 0 | 15m | 2s | Disables abilities 10s; destroys deployables |
| **Incendiary** | 40 DoT/sec | 6m | 2s | 8s burn zone |
| **Stun** | 0 | 8m | 1.5s | 3s stun |

---

## Time to Kill (TTK)

**Target:** 100 HP, 50 Armor

| Weapon Type | TTK (Optimal) | Shots to Kill |
| :---------- | :-----------: | :-----------: |
| SMG | 0.2–0.4s | 6–8 shots |
| AR | 0.3–0.5s | 5–7 shots |
| Shotgun | 0.1–0.2s | 1–2 shots |
| Sniper | Instant | 1–2 shots |
| LMG | 0.4–0.6s | 6–8 shots |
| Pistol | 0.5–0.8s | 8–10 shots |

**Design Goal:** TTK fast enough to reward skill execution; slow enough for counterplay and disengagement windows.

---

## Weapon Rarity, Value & Acquisition

### Rarity Table

| Rarity | Color | Spawn Rate | Average Value | Attachment Slots |
| :----- | :---- | :--------: | :-----------: | :--------------: |
| Common | White | 40% | $500–$1,500 | 2 |
| Uncommon | Green | 30% | $2,000–$4,000 | 3 |
| Rare | Blue | 20% | $5,000–$8,000 | 4 |
| Epic | Purple | 8% | $10,000–$15,000 | 5 |
| Legendary | Gold | 2% | $20,000+ | 5 + bonus |

**Legendary Bonuses:** Unique skin, +5% damage stat, special tracer colors, and prestige auction-house floor value.

### Acquisition Sources

| Source | In-Raid | Out-of-Raid |
| :----- | :-----: | :----------: |
| Loot containers | ✅ | — |
| Kill enemy players | ✅ | — |
| Supply drop events | ✅ | — |
| AI enemy drops | ✅ | — |
| Purchase from Stash/Traders | — | ✅ |
| Quest rewards | — | ✅ |
| Battle Pass rewards | — | ✅ |
| Safe House crafting | — | ✅ |

---

## Visual & Audio Feedback

### Visual Effects

| Effect | Design Purpose |
| :----- | :------------- |
| **Muzzle Flash** | Reveals shooter position — suppressor reduces flash |
| **Impact Sparks/Dust/Splinters** | Surface material feedback |
| **Blood Spray** | Hit confirmation |
| **Tracer Rounds** | Every 5th round — aiming feedback without full reveal |

### Audio Design

| Sound | Design Purpose |
| :---- | :------------- |
| **Gunshot volume** | Indicates distance of threat to all nearby players |
| **Directional audio** | Stereo panning reveals enemy bearing |
| **Suppressed variants** | Quieter — stealth advantage vs. audio disadvantage |
| **Reload sounds** | Alert window: mag drop → insertion → chamber = vulnerable phase |

---

## Weapon Balance Principles

1. **Availability ≠ Power** — Common weapons are easier to obtain; Legendary weapons are not always best for every situation.
2. **Risk premium** — Expensive loadouts carry heavier loss. Players must consciously decide when to risk high-tier gear.
3. **Skill floor** — Sniper rifles and LMGs require positioning knowledge. SMGs allow aggressive play at lower skill investment.
4. **Meta prevention** — Regular balance patches, weapon rotation in seasonal loot pools, community feedback integration.
5. **No dominant option** — Every weapon category has a role where it outperforms others. No weapon should be universally "the best pick."

---

## Cross-References

- [Weapon Attachment System](Weapon_Attachment_System.md) — Full attachment slot rules, stat modifiers per attach slot, in-raid swap system.
- [Weapons — Weapon Categories Deep Dive](../Weapons/Weapon_Categories_Deep_Dive.md) — Per-genre doctrine, hero synergy, build archetypes, matchup matrices (includes DMR).
- [Weapons — Weapon Master Database](../Weapons/Weapon_Master_Database.md) — Base and fully modded stats, mod slot counts, role per weapon.
- [Combat Feel (Top-Down)](Combat_Feel_Topdown.md) — Recoil cone model for top-down perspective, suppression, cover footprint.
- [Items & Gear](ItemsAndGear.md) — Armor tiers, throwable item tables, ammo stack sizes and weights.
- [Loot Table Design](Loot_Table_Design.md) — Spawn rates by zone tier; which weapons are in which container tables.
- [Gear Mechanics](Gear_Mechanics.md) — Encumbrance from weapon weight, durability/condition system.
- [Medical System](Medical_System.md) — Body part HP pool; bleed mechanics tie to weapon damage output.
