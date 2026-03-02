---
title: "Weapon Master Database"
type: docs
weight: 0
---

## Philosophy & Baseline

Weapons follow a "Realism-Lite" approach. Key stats:

- **Recoil:** Vertical (climb) and horizontal (bounce). Lower is better. See [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md).
- **Ergonomics:** ADS speed, stamina drain, noise. Higher (0–100) is better. See [Weapon Modding](../Inventory_Gear/Weapons_Modding.md).
- **Fire Rate (RPM):** Fixed per receiver; not changed by mods.
- **MOA (Accuracy):** Dispersion at 100 m. Lower is better.

Full category design: [Weapon Categories Deep Dive](Weapon_Categories_Deep_Dive.md). Full stats and ammo: [Weapon Arsenal](../Gameplay/WeaponArsenal.md).

---

## Assault Rifles (AR)

| Code Name | Display Name | Caliber | Rarity | Base Damage | Base RPM | Base Mag | Base Range (m) | Recoil | Fully Modded (Est) | Mod Slots | Role |
| :-------- | :----------- | :------ | :----- | :---------: | :------: | :------: | :------------: | :----- | :----------------- | :-------: | :--- |
| WPN_AR_AK47 | AK-47 | 7.62×39mm | Common | 35 | 600 | 30 | 40 | High | Recoil 55V/130H; Ergo 58; Range 450m; MOA 1.9 | 8+ | Budget equalizer; armor pen cheap |
| WPN_AR_M4A1 | M4A1 | 5.56×45mm | Uncommon | 32 | 750 | 30 | 45 | Low | Recoil 32V/125H; Ergo 75; Range 650m; MOA 1.1 | 12+ | Meta king; scales best with mods |
| WPN_AR_SCAR | SCAR-H | 7.62×51mm | Rare | 40 | 625 | 20 | 50 | Medium | Recoil 50V/120H; Ergo 62; Range 550m; MOA 1.4 | 10+ | Hard-hitting; mid-long range |
| WPN_AR_HK416 | HK416 | 5.56×45mm | Rare | 34 | 850 | 30 | 48 | Low | Recoil 38V/118H; Ergo 72; Range 600m; MOA 1.2 | 12+ | High ROF; stable |
| WPN_AR_AUG | Steyr AUG | 5.56×45mm | Uncommon | 30 | 680 | 30 | 42 | Very Low | Recoil 45V/135H; Ergo 70; Range 520m; MOA 1.5 | 8+ | Built-in scope; compact |

---

## Submachine Guns (SMG)

| Code Name | Display Name | Caliber | Rarity | Base Damage | Base RPM | Base Mag | Base Range (m) | Recoil | Fully Modded (Est) | Mod Slots | Role |
| :-------- | :----------- | :------ | :----- | :---------: | :------: | :------: | :------------: | :----- | :----------------- | :-------: | :--- |
| WPN_SMG_MP5 | MP5 | 9×19mm | Common | 24 | 900 | 30 | 20 | Medium | Recoil 22V/110H; Ergo 78; Range 120m; MOA 3.0 | 5+ | CQC headshot; leg meta hose |
| WPN_SMG_VECTOR | Vector .45 | .45 ACP | Rare | 28 | 1100 | 25 | 18 | Very Low | Recoil 18V/95H; Ergo 80; Range 100m | 6+ | Ultra-fast TTK CQB |
| WPN_SMG_P90 | P90 | 5.7×28mm | Uncommon | 22 | 1000 | 50 | 22 | Medium | Recoil 28V/115H; Ergo 75; Range 130m | 5+ | Large mag; suppressive |
| WPN_SMG_UMP45 | UMP-45 | .45 ACP | Common | 26 | 700 | 25 | 25 | Low | Recoil 35V/125H; Ergo 72; Range 110m | 5+ | Balanced; affordable |
| WPN_SMG_MP7 | MP7 | 4.6×30mm | Rare | 23 | 950 | 40 | 28 | Low | Recoil 25V/108H; Ergo 76; Range 135m | 6+ | High penetration; compact |

---

## Shotguns

| Code Name | Display Name | Caliber | Rarity | Dmg/Pellet | Pellets | RPM | Capacity | Range (m) | Fully Modded (Est) | Mod Slots | Role |
| :-------- | :----------- | :------ | :----- | :--------: | :-----: | :-: | :------: | :-------: | :----------------- | :-------: | :--- |
| WPN_SG_R870 | Remington 870 | 12 Gauge | Common | 20 | 8 | 60 | 6 | 12 | Recoil 320V/200H; Ergo 55; Range 80m (slug); MOA 5.0 | 6+ | Pump; one-shot potential |
| WPN_SG_M590 | Mossberg 590 | 12 Gauge | Common | 18 | 8 | 70 | 8 | 14 | Recoil 300V/190H; Ergo 52; Range 85m | 6+ | More capacity; tactical |
| WPN_SG_AA12 | AA-12 | 12 Gauge | Epic | 18 | 8 | 300 | 20 | 15 | Recoil 180V/140H; Ergo 45; Range 90m | 8+ | Full-auto; CQB dominance |
| WPN_SG_SPAS12 | SPAS-12 | 12 Gauge | Rare | 22 | 8 | 80 | 6 | 10 | Recoil 280V/180H; Ergo 50; tight spread | 6+ | Pump/auto; tight spread |
| WPN_SG_SAIGA | Saiga-12 | 12 Gauge | Uncommon | 16 | 8 | 200 | 10 | 16 | Recoil 220V/160H; Ergo 58; mag-fed | 8+ | Semi-auto; magazine-fed |

---

## Sniper Rifles

| Code Name | Display Name | Caliber | Rarity | Base Damage | Base RPM | Base Mag | Base Range (m) | Fully Modded (Est) | Mod Slots | Role |
| :-------- | :----------- | :------ | :----- | :---------: | :------: | :------: | :------------: | :----------------- | :-------: | :--- |
| WPN_SR_M24 | M24 | 7.62×51mm | Rare | 85 | 50 | 5 | 100 | Recoil 45V/80H; Ergo 55; Range 120m; MOA 0.6 | 6+ | Bolt-action; reliable |
| WPN_SR_AWP | AWP | .338 Lapua | Epic | 120 | 40 | 5 | 120 | Recoil 55V/90H; Ergo 48; Range 150m; MOA 0.5 | 6+ | One-shot chest kill |
| WPN_SR_M107 | Barrett M107 | .50 BMG | Legendary | 130 | 35 | 10 | 150 | Recoil 70V/100H; Ergo 40; Range 180m; penetrates all | 8+ | Anti-materiel |
| WPN_SR_VSS | VSS Vintorez | 9×39mm | Rare | 65 | 120 | 20 | 60 | Recoil 35V/85H; Ergo 62; integrated suppressor; subsonic | 5+ | Stealth sniper |

---

## Designated Marksman Rifles (DMR)

| Code Name | Display Name | Caliber | Rarity | Base Damage | Base RPM | Base Mag | Base Range (m) | Fully Modded (Est) | Mod Slots | Role |
| :-------- | :----------- | :------ | :----- | :---------: | :------: | :------: | :------------: | :----------------- | :-------: | :--- |
| WPN_DMR_SKS | SKS | 7.62×39mm | Common | 55 | 120 | 10 | 45 | Recoil 48V/110H; Ergo 60; Range 55m; MOA 1.8 | 5+ | Budget DMR; semi-auto |
| WPN_DMR_SVD | SVD Dragunov | 7.62×54mmR | Uncommon | 75 | 180 | 10 | 80 | Recoil 42V/100H; Ergo 58; Range 95m; MOA 1.2 | 7+ | Semi-auto; faster follow-up |
| WPN_DMR_SR25 | SR-25 | 7.62×51mm | Rare | 78 | 200 | 20 | 75 | Recoil 40V/95H; Ergo 62; Range 90m; MOA 1.0 | 10+ | Precision marksman |
| WPN_DMR_MK14 | MK 14 EBR | 7.62×51mm | Epic | 80 | 220 | 20 | 80 | Recoil 38V/90H; Ergo 65; Range 100m; MOA 0.9 | 12+ | Peak DMR; versatile |

---

## Light Machine Guns (LMG)

| Code Name | Display Name | Caliber | Rarity | Base Damage | Base RPM | Base Mag | Base Range (m) | Bipod | Fully Modded (Est) | Mod Slots | Role |
| :-------- | :----------- | :------ | :----- | :---------: | :------: | :------: | :------------: | :---: | :----------------- | :-------: | :--- |
| WPN_LMG_M249 | M249 SAW | 5.56×45mm | Rare | 32 | 750 | 100 | 55 | Yes | Recoil 35V/115H (bipod 18V/70H); Ergo 45 | 8+ | Suppressive fire king |
| WPN_LMG_PKM | PKM | 7.62×54mmR | Uncommon | 38 | 650 | 75 | 60 | Yes | Recoil 48V/125H (bipod 25V/75H); Ergo 42 | 7+ | High damage; heavy |
| WPN_LMG_MG42 | MG42 | 7.62×51mm | Epic | 35 | 1200 | 100 | 50 | Yes | Recoil 55V/140H (bipod 28V/85H); Ergo 38 | 8+ | Extreme ROF; buzzsaw |
| WPN_LMG_RPK | RPK-74 | 7.62×39mm | Uncommon | 30 | 600 | 75 | 45 | No | Recoil 52V/128H; Ergo 50; mobile LMG | 7+ | Mobile LMG; no bipod |

---

## Pistols

| Code Name | Display Name | Caliber | Rarity | Base Damage | Base RPM | Base Mag | Base Range (m) | Fully Modded (Est) | Mod Slots | Role |
| :-------- | :----------- | :------ | :----- | :---------: | :------: | :------: | :------------: | :----------------- | :-------: | :--- |
| WPN_PISTOL_GLOCK | Glock 19 | 9×19mm | Common | 25 | 400 | 17 | 25 | Recoil 180V/60H; Ergo 92; MOA 2.5 | 6+ | Reliable sidearm |
| WPN_PISTOL_DEAGLE | Desert Eagle | .50 AE | Rare | 55 | 200 | 7 | 35 | Recoil 220V/75H; Ergo 78; hand cannon | 5+ | Skill-based finisher |
| WPN_PISTOL_USP | USP-S | .45 ACP | Uncommon | 28 | 350 | 12 | 30 | Recoil 190V/65H; integrated suppressor | 5+ | Silenced; stealth |
| WPN_PISTOL_M1911 | M1911 | .45 ACP | Common | 40 | 280 | 7 | 28 | Recoil 200V/70H; Ergo 82 | 5+ | Classic .45; reliable |
| WPN_PISTOL_P226 | SIG P226 | 9×19mm | Uncommon | 30 | 380 | 15 | 32 | Recoil 175V/58H; Ergo 85 | 6+ | Balanced; accurate |
| WPN_PISTOL_REVOLVER | .357 Magnum | .357 Mag | Rare | 60 | 180 | 6 | 30 | Recoil 240V/80H; no mag reload | 4+ | High damage; cylinder |

---

## Melee Weapons

| Code Name | Display Name | Rarity | Slash Dmg | Backstab Dmg | Range (m) | Speed | Mod Slots | Role |
| :-------- | :----------- | :----- | :-------: | :----------: | :-------: | :---- | :-------: | :--- |
| WPN_MELEE_KNIFE | Combat Knife | Default | 50 | 100 | 2.0 | Fast | 0 | Default melee; always equipped |
| WPN_MELEE_AXE | Tactical Axe | Rare | 75 | 150 | 2.5 | Medium | 0 | Better reach; more damage |
| WPN_MELEE_MACHETE | Machete | Uncommon | 65 | 130 | 2.3 | Fast | 0 | Fast slashing |
| WPN_MELEE_BATON | Stun Baton | Rare | 40 | 80 | 2.0 | Very Fast | 0 | Stuns enemies 2 s |

---

## Cross-References

- [Weapon Arsenal](../Gameplay/WeaponArsenal.md) — Full specs, ammo tables, attachment reference.
- [Weapon Categories Deep Dive](Weapon_Categories_Deep_Dive.md) — Role, doctrine, hero synergy, matchups.
- [Weapon Balance Framework](Weapon_Balance_Framework.md) — DPS, TTK, cost-efficiency.
- [Weapon Modding (Gunsmith)](../Inventory_Gear/Weapons_Modding.md) — Ergonomics, recoil, MOA, malfunctions.
- [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md) — Slot types and compatibility.
