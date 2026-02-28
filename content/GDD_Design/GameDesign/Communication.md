---
title: "In-Game Communication — Voice Chat & Ping System"
type: docs
weight: 21
---

## Overview

Communication is a **force multiplier** — a team that communicates wins fights they would otherwise lose. Our communication system must work seamlessly across Mobile (where voice is natural) and PC (where keyboard shortcuts are preferred), serve hardcore coordinated squads AND total strangers auto-matched together, and function even when voice is unavailable (mic-less players, public spaces, hearing accessibility needs).

> **Cross-References:** [Accessibility](Accessibility.md) — visual/audio accessibility alternatives; [Navigation & HUD](NavigationAndMap.md) — ping indicators on minimap; [Loadout Preparation](LoadoutPreparation.md) — squad voice available during prep phase; [Ranked Mode](RankedMode.md) — voice and ping rules in ranked; [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — voice channel activation on team formation.

---

## 1. Communication Pillars

| Pillar | Description |
| :----- | :---------- |
| **Zero-friction pings** | Communicate tactically without speaking, in <1 second |
| **Voice as optional layer** | No mechanic should require voice to participate effectively |
| **Cross-platform audio** | Mobile mic users and PC players share the same voice rooms |
| **Toxic-proof defaults** | Proximity voice OFF for enemy bodies; mute-one-tap from scoreboard |

---

## 2. Voice Chat System

### Channel Structure

| Channel | Who Hears | Default State | Activation |
| :------ | :-------- | :------------ | :--------- |
| **Squad Voice** | Your squad (2–3 players) | ✅ ON | Auto on squad join |
| **Proximity Voice** | Any player within 15m (incl. enemies) | ✅ ON (optional) | Toggle in settings |
| **Spectator Voice** | Dead squadmates listening | ✅ ON | Auto on death |
| **All-chat (text only)** | All players in lobby | Pre-match only | None |

### Proximity Voice Design

- **Range:** 15m radius — scales with room type (60m outdoors open field)
- **Directional audio:** Voice has stereo position matching in-game direction of source player
- **Enemy voice:** Enemies within 15m heard — creates tension ("I can hear them looting") — adds authentic PvPvE immersion
- **Dead player bodies:** Dead players' voices DO NOT continue — prevents ghost-comms exploitation
- **Muffling:** Proximity voice through walls: -50% volume, loses directionality

### Voice Quality & Technical

| Setting | Default | Range |
| :------ | :------ | :---- |
| Voice codec | Opus 12kbps | 8–32kbps (adjustable) |
| Noise suppression | AI-based (on by default) | RNNoise |
| Push-to-Talk | Default mobile / optional PC | Toggle in settings |
| Voice Activity Detection (VAD) | Default PC | Threshold adjustable |
| Mic volume (others) | 100% | 0–150% per player |

### In-Match Voice Controls (HUD)

```
┌──────────────────────────────────────────────────────────────────┐
│  SQUAD VOICE BAR (bottom-right, mobile: above thumb zone)        │
│                                                                   │
│  [🎤 Kai_V  ▐▐▐░░]  [🎤 Dxt_R  ░░░░░]  [🎤 YOU  ▐░░░░]        │
│  ─────────────────────────────────────────────────────────────── │
│  [Mute Self]  [Push to Talk]  [🔊 Volume]  [Settings]           │
└──────────────────────────────────────────────────────────────────┘
```

- Audio-level bars animated when player speaks
- Tap any player name → mute that player instantly (no confirmation)
- Voice icon on operator nameplate shows 🎤 when speaking in-world

---

## 3. Ping System

The ping system is a **first-class communication tool** — not a fallback. Even squads who use voice should use pings to mark persistent world-space information.

### Ping Types

| Ping | Shortcut | Duration | Visual | Audio Cue |
| :--- | :------- | :------- | :----- | :-------- |
| **⚑ Attack Here** | Single tap world | 30s | Red arrow pointing down | "Enemy spotted!" / Squad: "Attack that!" |
| **✋ Defend / Hold** | Hold + release | 30s | Yellow shield icon | "Hold position!" |
| **📦 Loot Here** | Single tap on item/container | 45s | Blue box icon | "Loot here!" |
| **👁 Enemy Spotted** | Single tap enemy | 20s | Orange exclamation | "Enemy spotted!" |
| **🚁 Go Here** | Double tap world | 30s | Green arrow on ground | "Move to my marker" |
| **⚕ Need Help** | Hold self + release | 45s | Flashing red cross | "I need help!" |
| **✅ Acknowledged** | Tap any existing ping | — | Green check on ping | "Got it!" |
| **❌ Negative** | Long-hold tap | — | Red X | "Negative" / "No" |

### Ping Context Intelligence

The system reads context to auto-select ping sub-type:

| Context | Ping Detected | Auto-label |
| :------ | :------------ | :--------- |
| Tapped on enemy body | Enemy Spotted | "Enemy spotted here" |
| Tapped on weapon item | Loot Here | "Weapon here" |
| Tapped on extraction zone | Go Here | "Extract here" |
| Tapped while downed | Need Help | "I'm down" |
| Tapped on empty ground near threat | Attack Here | "Threat area" |

### Ping Wheel (PC / Long Hold Mobile)

Hold middle mouse (PC) or long-press world (Mobile) → 8-slot radial wheel:

```
              [⚑ Attack]
     [❌ Cancel]       [🚁 Move]
[⚕ Help]                       [👁 Enemy]
     [✅ OK]          [📦 Loot]
              [✋ Defend]
```

### Ping UI — In World vs. Minimap

| Location | Display |
| :------- | :------ |
| **World space** | Floating icon above ping point, fades over duration |
| **Minimap** | Same icon at map position |
| **HUD notification** | Team member ping: "Kai_V → [Loot Here] at Mill" (3s banner) |
| **Distance indicator** | "18m" label below world-space ping |

---

## 4. Quick Chat (Text Callouts)

For players who cannot or choose not to use voice — quick localized chat phrases triggered by single inputs.

### Quick Chat Categories

| Category | Example Phrases |
| :------- | :-------------- |
| **Tactical** | "Pushing East" / "Covering North" / "Falling back" |
| **Combat** | "One down!" / "Multiple enemies!" / "Reloading!" |
| **Economy** | "Out of ammo" / "Grabbing loot, cover me" / "Good loot here" |
| **Social** | "Nice shot!" / "Good game" / "Thanks for the revive" |
| **Status** | "Wait for me" / "I'm extracting" / "Going to extract" |

**Select method:**
- **Mobile:** Tap speech bubble icon → 3 category tabs → tap phrase → auto-voice-acted line plays (operator-specific VO)
- **PC:** Configurable key (default: `Z`) → command rose → phrase

**Localization:** All quick chat phrases are pre-translated. Players see them in their own language regardless of sender's language.

---

## 5. Communication Rules by Mode

| Mode | Squad Voice | Proximity Voice | Ping | Quick Chat | Notes |
| :--- | :---------- | :-------------- | :--- | :--------- | :---- |
| **The Raid** | ✅ | ✅ (optional) | ✅ | ✅ | Full feature set |
| **Blitz** | ✅ | ✅ (optional) | ✅ | ✅ | Faster pacing, pings expire 15s |
| **Scav Run** | ❌ (solo mode) | ✅ (against PMCs) | ✅ (enemy pings only) | ✅ | No squad voice |
| **Ranked Ops** | ✅ | ❌ (disabled) | ✅ | ✅ | Proximity voice disabled for competitive integrity |
| **Blackout Co-op** | ✅ | ❌ (PvE) | ✅ | ✅ | No enemy players to hear |
| **Training Grounds** | ❌ | ❌ | ✅ | ❌ | Solo practice only |

---

## 6. Anti-Toxicity Design

| Feature | Implementation |
| :------ | :------------- |
| **One-tap mute** | Any player in scoreboard → 1-tap mute (no confirm); persists for session |
| **Report from voice** | Tap player name in voice bar → "Report [reason]" dropdown while in-match |
| **Auto mute on report threshold** | Player reported 3× in one session → auto-muted for all future squads that session |
| **Verbal toxicity detection** | AI voice moderation flags slurs; human review queue for repeated offenders |
| **Global block** | Block player permanently from all future communication and auto-remove from any shared squads |
| **Ping spam prevention** | Max 3 pings per player within 5 seconds; further pings rejected silently |
| **Push notification mute** | Players can opt out of all voice-based features globally without losing playing ability |

---

## Cross-References

- [Navigation & HUD](NavigationAndMap.md) — Ping icons displayed on minimap; directional ping sounds integrated into audio mix.
- [Accessibility](Accessibility.md) — Visual ping indicators for hearing-impaired; high-contrast mode for ping icons; subtitles for quick chat VO lines.
- [Ranked Mode](RankedMode.md) — Proximity voice disabled in Ranked Ops; toxicity penalties escalate faster (voice ban → ranked ban).
- [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — Voice channels auto-created on team formation; LFG players default to squad voice opt-in.
- [Loadout Preparation](LoadoutPreparation.md) — Squad voice active during prep phase; party chat visible in squad panel.
