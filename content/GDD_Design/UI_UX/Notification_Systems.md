---
title: "Notification & Feedback Systems"
type: docs
weight: 23
---

## Quick Navigation

| Destination | Use |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [Screen Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy and designer-ready spec template |
| [Global UX Standards](Global_UX_Standards.md) | Shared navigation, focus, state, modal, and accessibility rules |
| [HUD Design](HUD_Design.md) | HUD placement and element visibility rules |
| [In-Raid Screens](In_Raid_Screens.md) | Notification behavior in raid overlays and combat states |
| [UX Flows](UX_Flows.md) | Flow-level feedback and state machine references |

---

## Notification Design Philosophy

The notification system operates on one rule: **information arrives in proportion to its urgency**. Critical notifications interrupt; ambient notifications wait.

### Priority Hierarchy

| Priority | Category | Behavior | Duration | Example |
| :------: | :------- | :------- | :------- | :------ |
| **1 - Critical** | Survival | Full-screen effect + audio + haptic | Until resolved | Low health vignette, incoming fire indicator |
| **2 - High** | Combat | Edge-of-screen indicator + sound | 3-5 seconds | Kill confirmation, headshot, armor break |
| **3 - Medium** | Progress | Toast notification + subtle sound | 4 seconds | Quest objective completed, item discovered |
| **4 - Low** | Ambient | Small text in feed + no sound | 3 seconds | Player joined/left area, environmental event |

### Queue Management Rules

- Maximum **3 notifications visible** at any time
- If a new Priority 1 notification arrives, it replaces everything
- Priority 2-4 notifications queue in order, displayed sequentially
- If the queue exceeds 5 pending notifications, lowest priority items are dropped
- Duplicate notifications within 2 seconds are merged (e.g., "Picked up 5.45 ammo x3" instead of three separate toasts)

#### State Diagram

```
Incoming Event
     |
     v
Priority 1? ---- yes ----> Clear visible stack -> Show critical
     |
     no
     v
Duplicate? ---- yes ----> Merge count / refresh timer
     |
     no
     v
Queue by priority -> Show if visible slots < 3 -> Drop low priority if queue > 5
```

---

## Kill Feed

### Position and Layout

| Property | Specification |
| :------- | :------------ |
| Position | Top-right corner, below minimap |
| Width | 300px maximum |
| Entry height | 24px per line |
| Max visible entries | 5 at a time |
| Entry duration | 5 seconds, then fade out over 500ms |
| Font | Inter Regular, 14px |
| Scroll | Newest entries push older ones up |

Layout (PC/Console)

```
+------------------------------------------------------------------+
| HP / Armor                         Extract 22:15       Minimap   |
| Toast 1: Quest updated                                Kill Feed  |
| Toast 2: Rare item found                              Kai > PMC  |
| Toast 3: Faction rep +0.05                            P2 > AI    |
|                                                                  |
|                         Gameplay area                            |
|                                                                  |
| Damage arcs appear on screen edge. Critical alerts replace stack.|
+------------------------------------------------------------------+
```

### Entry Format

```
[Killer Icon] [Killer Name] [Weapon Icon] [Victim Name]
```

### Color Coding

| Event | Killer Color | Victim Color | Special |
| :---- | :----------- | :----------- | :------ |
| You killed someone | Signal Green (#22C55E) | White | Bold text |
| You were killed | White | Critical Red (#EF4444) | Bold text |
| Squadmate kill | Tactical Blue (#3B82F6) | White | Normal weight |
| Squadmate died | White | Tactical Blue (#3B82F6) | Normal weight |
| Other players | Steel Gray (#6B7280) | Steel Gray (#6B7280) | Light weight |
| AI kill (by player) | Player color | Muted gray | Italic |

### Special Kill Icons

| Type | Icon | Audio Cue |
| :--- | :--- | :-------- |
| Headshot | Crosshair on head silhouette | Sharp "ding" sound |
| Grenade kill | Explosion icon | None (explosion sound suffices) |
| Melee kill | Knife icon | Slash sound |
| Long-range kill (100m+) | Distance number in brackets | Sniper "crack" echo |
| Squad wipe | Skull with X | Distinct multi-kill chime |

<!-- REF_IMAGE: Kill feed mockup — showing 5 stacked entries with different color coding, weapon icons, and headshot indicator -->

---

## Damage Feedback

### Hit Markers (Outgoing Damage)

| Property | Specification |
| :------- | :------------ |
| Position | Centered on crosshair |
| Shape | 4 short lines forming an X pattern around crosshair center |
| Normal hit color | White (#FFFFFF), 80% opacity |
| Headshot color | Critical Red (#EF4444), 100% opacity, thicker lines |
| Armor hit color | Tactical Blue (#3B82F6), with metallic sound |
| Kill confirmation | Hit marker briefly expands + changes to Signal Green, accompanied by kill sound |
| Duration | 150ms (fast — must not obscure continued aiming) |
| Size | 16px radius from center, expanding to 20px on hit |

### Hit Markers (Incoming Damage)

| Property | Specification |
| :------- | :------------ |
| Position | Screen edges, directional indicators |
| Shape | Red arc segments pointing toward the damage source |
| Indicator count | 1-4 arcs depending on damage amount (light graze = 1, heavy hit = 4) |
| Color | Critical Red (#EF4444) to dark red (#7F1D1D) gradient |
| Duration | 1 second, fading linearly |
| Directional accuracy | 45-degree arc resolution (8 possible directions) |
| Multi-source | Multiple attackers show separate directional indicators |
| Unknown source | If damage source is not visible, indicator flashes briefly in all directions |

<!-- REF_IMAGE: Hit marker diagram — showing outgoing (crosshair-centered X) and incoming (edge-of-screen directional arcs) examples side-by-side -->

### Damage Numbers (Optional Toggle)

Damage numbers are **disabled by default** (extraction shooters favor realism), but available as an option.

| Property | Specification |
| :------- | :------------ |
| Toggle | Settings > Gameplay > "Damage Numbers: On / Off" |
| Position | Float upward from point of impact on enemy |
| Font | JetBrains Mono Bold |
| Normal damage | White, 16px, floats up 30px over 600ms |
| Critical / Headshot | Yellow (#FACC15), 22px, bounces slightly |
| Armor damage | Blue (#3B82F6), 14px (smaller — less effective hit) |
| Blocked (0 damage) | Gray (#6B7280), "BLOCKED" text, 12px |
| Stacking | Rapid hits merge after 200ms (e.g., "45 + 45 = 90" displayed as "90") |

### Screen Effects (Incoming Damage)

| Effect | Trigger | Visual | Duration |
| :----- | :------ | :----- | :------- |
| Blood vignette | Taking any damage | Red-tinted edges, intensity proportional to damage | 2 seconds |
| Screen shake | Explosive damage or heavy caliber | Subtle camera displacement (2-4px amplitude) | 300ms |
| Suppression blur | Bullets passing near player without hitting | Mild radial blur at screen edges | While suppressed + 1s fade |
| Armor crack | Armor durability reaches 0 | Crack pattern overlay briefly flashes | 500ms |
| Near-death pulse | Health below 15% | Rhythmic red pulse matched to heartbeat sound | Until healed or dead |

---

## Status Effect Indicators

### Icon System

Status effects appear as small icons below the health bar, stacking horizontally:

| Status | Icon | Color | Screen Effect | Audio |
| :----- | :--- | :---- | :------------ | :---- |
| **Bleeding** | Blood drop with timer | Red (#EF4444) | Small blood drops at screen edge, ticking HP loss | Wet dripping sound |
| **Heavy Bleeding** | Double blood drop, urgent | Bright red, pulsing | Stronger blood effect + periodic screen darken | Faster drip + heartbeat |
| **Fracture** | Cracked bone | Orange (#F97316) | Screen shakes on movement (micro-jitter) | Bone grinding on movement |
| **Pain** | Exclamation in triangle | Yellow (#FACC15) | Slight blur on screen edges | Low moaning, breathing |
| **Contamination** | Hazard trefoil | Green (#22C55E) | Green fog at screen edges, slowly increasing | Geiger counter ticks |
| **Dehydration** | Empty canteen | Orange (#F97316) | Slight desaturation, vision narrows | Dry breathing sound |
| **Starvation** | Empty plate | Orange (#F97316) | Screen brightness slowly decreases | Stomach rumble |
| **Hypothermia** | Snowflake | Cyan (#06B6D4) | Frost creep at screen edges | Teeth chattering |
| **Overheating** | Thermometer | Red (#EF4444) | Heat shimmer at screen edges | Heavy panting |
| **Tremor** | Shaky hand | Yellow (#FACC15) | Weapon sway increases | None (mechanical effect) |

### Status Icon Behavior

| Rule | Implementation |
| :--- | :------------- |
| Maximum visible | 4 icons at a time. If more than 4 active, show highest severity |
| Order | Left to right by severity (most dangerous first) |
| Timer | Each icon shows remaining duration if applicable (e.g., painkiller suppressing pain) |
| Stacking | Same effect at higher tier replaces lower (e.g., Heavy Bleeding replaces Bleeding) |
| Resolution | Icon disappears immediately when status is cured. Brief green flash confirms cure |

<!-- REF_IMAGE: Status effect icon strip — showing 4 active effects below health bar with timer indicators and severity ordering -->

---

Layout (PC/Console)

```
+-------------------------------+
| HP 85 / 100   Armor 42        |
| [Bleed 0:32] [Pain 1:10]      |
| [Fracture]   [Dehydration]    |
+-------------------------------+
Order: highest severity first. More than 4 active -> show +N indicator.
```

## Toast Messages

### Position and Layout

| Property | Specification |
| :------- | :------------ |
| Position | Center-left, 200px from left edge, vertically centered |
| Width | 350px maximum |
| Height | 48px per toast |
| Max visible | 3 stacked toasts |
| Animation | Slide in from left (200ms ease-out), slide out left (300ms ease-in) |
| Duration | 4 seconds standard, 6 seconds for quest completions |

### Toast Categories

| Category | Icon | Border Color | Audio | Example |
| :------- | :--- | :----------- | :---- | :------ |
| Quest Progress | Clipboard icon | Neon Yellow (#FACC15) | Subtle chime | "Kill target: 2/5" |
| Quest Complete | Green check | Signal Green (#22C55E) | Success fanfare | "Supply Run — COMPLETED" |
| Item Pickup | Box icon | White | Soft click | "Picked up: AK-74M" |
| Rare Item | Star icon | Rarity color | Rare discovery sound | "Found: Lab Keycard (Rare)" |
| Achievement | Trophy icon | Gold (#F59E0B) | Achievement unlock sound | "First Blood — Kill first PMC" |
| System Message | Info icon | Steel Gray (#6B7280) | None | "Server: Auto-save complete" |
| Faction Rep | Faction badge | Faction color | Rep gain/loss sound | "Salvage Corps: +0.05 Rep" |
| Skill Increase | Arrow up | Cyan (#06B6D4) | Level-up chime | "Endurance: Level 3" |

### Toast Content Format

```
+-------------------------------------------+
|  [Icon]  [Title - Bold]                   |
|          [Description - Regular, smaller]  |
+-------------------------------------------+
```

Example:
```
+-------------------------------------------+
|  [Clipboard]  Kill Target: 2/5            |
|               Quest: Supply Run            |
+-------------------------------------------+
```

---

## Contextual Prompts

### Interaction Prompts

Appear when the player is near an interactable object:

| Object Type | Prompt Text | Input | Duration |
| :---------- | :---------- | :---- | :------- |
| Door | "Open Door" / "Close Door" | Press E/A | Instant |
| Lootable Container | "Search [Container Name]" | Hold F/A (1.5s) | Progress circle fills |
| Dead Body | "Search Body" | Hold F/A (2.0s) | Progress circle fills |
| Quest Item | "Pick Up [Item Name]" | Press E/A | Instant. Quest toast follows |
| Locked Door | "Locked — Requires [Key Name]" | None (information only) | Displayed while in range |
| Extraction Point | "Extract — Hold [Key]" | Hold F/A (5.0s) | Large progress circle |
| Vehicle | "Enter Vehicle" | Press E/A | Instant |
| Teammate (downed) | "Revive [Player Name]" | Hold F/A (8.0s) | Progress circle + revive animation |

### Prompt Visual Style

| Property | Specification |
| :------- | :------------ |
| Background | Semi-transparent dark (#1E293B at 70% opacity) |
| Border | 1px solid, color matches interaction type (yellow for loot, green for extract) |
| Key indicator | Rounded rectangle showing the keybind/button, styled as physical key |
| Text | Inter Semi-Bold, 16px, white |
| Progress circle | Circular fill around the key indicator. Color matches interaction type |

---

## Danger Communication

### Threat Proximity System

Visual and audio cues that communicate danger without directly revealing enemy positions:

Layout (PC/Console)

```
+------------------------------------------------------------------+
|                         red compass pip                          |
|                               v                                  |
| HP 85                                             Minimap        |
|                                                                  |
|        left edge damage arc        [PLAYER]      grenade !       |
|                                                                  |
|             suppression blur and desaturation at edges           |
|                                                                  |
| Ammo 30/120                                      Squad status    |
+------------------------------------------------------------------+
```

| Threat Level | Trigger | Visual | Audio |
| :----------- | :------ | :----- | :---- |
| **Nearby gunfire** | Shots fired within 100m | Brief red compass pip in direction. No screen effect | Gunshot sounds with environmental echo |
| **Suppression** | Bullets pass within 2m of player | Radial blur at screen edges, slight desaturation | Bullet crack/whiz sound |
| **Sniper threat** | Sustained scope aim at player (4+ seconds) | NO visual indicator (realism) — audio only | Distant scope glint sound (optional design) |
| **Being spotted** | AI enemy detects player | Enemy awareness icon above their head (!, !!, !!!) | Alert sound (barking, shouting) |
| **Grenade warning** | Grenade lands within 10m | Red grenade icon with direction arrow | "Grenade!" voice callout + bouncing sound |
| **Boss proximity** | Within 50m of boss enemy | Subtle environmental change (lights flicker, ground tremor) | Bass rumble, unique boss audio theme |
| **Extraction available** | Extraction window opens | Green flash on extraction timer + compass marker | Radio static + extraction announcement |

### Suppression Effect Details

| Property | Value |
| :------- | :---- |
| Trigger distance | Bullets passing within 2 meters of player camera |
| Visual intensity | Scales with number of near-miss bullets (1 bullet = 20% effect, 5+ = 100%) |
| Effect | Radial blur (radius 100px from edges), slight chromatic aberration, desaturation |
| Recovery | Effect fades over 1.5 seconds after last near-miss |
| Gameplay impact | Increased weapon sway while suppressed. No aim penalty |
| Audio | Bullet crack sounds, muffled hearing (low-pass filter on other sounds) |

---

## Designer-Ready Notification Family Specs

Notifications must prioritize survival. Combat-critical alerts can interrupt; informational or reward messages queue, fade, or wait until pressure drops.

### Notification Placement Map

#### Player Intent

Receive the right signal at the right urgency without losing combat readability.

#### Expanded ASCII Wireframe

```
+--------------------------------------------------------------------------------+
| Kill feed / squad alerts                                      Raid warnings    |
|                                                                                |
|                          combat read area, mostly clear                        |
|                                                                                |
| Toast queue / item pickup                        Damage / ammo / status alerts |
+--------------------------------------------------------------------------------+
```

#### Layout Anatomy

| Region | Requirement |
| :--- | :--- |
| Top left | kill feed and squad/system alerts |
| Top right | raid timer, extraction, server warnings |
| Center edge | incoming damage, grenade, suppression, low health |
| Bottom left | toast queue and pickups |
| Bottom right | ammo, reload, status effect reminders |

#### Visual Hierarchy

| Priority | Notification | Requirement |
| :--- | :--- | :--- |
| 1 | lethal threats | grenade, low health, downed, extraction critical |
| 2 | combat feedback | hit marker, kill confirm, suppression, damage direction |
| 3 | objective/economy | quest complete, XP, pickup, reward |
| 4 | social/system | invite, chat, news, noncritical tips |

#### Component Requirements

| Component | Requirement |
| :--- | :--- |
| Notification shell | icon, short label, optional detail, timer/progress if relevant |
| Queue item | priority, max visible count, expiry/fade behavior |
| Interrupt alert | allowed only for lethal or irreversible events |

#### States & Edge Cases

| State | Behavior |
| :--- | :--- |
| Combat pressure | suppress noncritical toasts |
| Queue overflow | collapse low-priority messages into count |
| Muted/reduced effects | preserve text or haptic fallback |
| Colorblind mode | icons/text replace hue-only coding |

#### Input / Focus / Touch

| Action | PC | Console | Mobile |
| :--- | :--- | :--- | :--- |
| Expand toast | Hover/click | Focus notification | Tap |
| Dismiss noncritical | Click X | X / Square | Swipe |
| Open related screen | Click toast | A / Cross | Tap toast |

#### Designer Notes

- If a notification does not affect the next 3 seconds of survival, it should not occupy the combat center.
- Toast copy must be short enough to read while moving.

#### Acceptance Checklist

- [ ] Each family has a placement, queue rule, interrupt rule, and accessible fallback.

### Family Requirements

| Family | Trigger | Placement | Queue / Interrupt Rule | Accessibility / Sync |
| :--- | :--- | :--- | :--- | :--- |
| Kill Feed | player/squad kill events | top-left stack | queue max 4; never center interrupt | icon + text; paired kill audio optional |
| Damage Feedback | incoming/outgoing damage | reticle/edge/status cluster | incoming lethal interrupts; outgoing hit markers stay compact | direction, haptic, and audio support |
| Status Effects | bleed, fracture, poison, buff/debuff | bottom/status cluster | persistent until cleared; escalates if lethal | text labels and icon shapes |
| Toast Messages | rewards, unlocks, pickup, social info | bottom-left queue | defer during combat unless reward is time-sensitive | readable text, no color-only rarity |
| Contextual Prompts | interactable object or blocked action | near object/bottom prompt | replaces previous prompt; blocked prompt names reason | input icon plus action verb |
| Danger Communication | grenade, boss, extraction, suppression | edge/center-edge | may interrupt based on lethality | audio/haptic pair required |

### Notification QA Checklist

- [ ] Noncritical notifications defer during combat pressure.
- [ ] Lethal warnings can interrupt but do not fully blind the playfield.
- [ ] Every color-coded state also has text or icon shape.
- [ ] Audio, visual, and haptic feedback match the same event priority.

---

## Audio-Visual Sync Reference

Every notification type has paired audio-visual feedback:

| Event | Visual | Audio | Haptic (Controller) |
| :---- | :----- | :---- | :------------------ |
| Kill confirmed | Hit marker → green + kill feed entry | Kill sound (distinct "thunk") | Strong single pulse (300ms) |
| Headshot kill | Hit marker → red flash + headshot icon in kill feed | "Ding" + kill sound | Double pulse |
| You were hit | Directional damage indicator + blood vignette | Impact sound + grunt | Sharp short pulse |
| You died | Screen fades to gray + death overlay | Flatline tone + fade to silence | Long rumble (500ms) |
| Quest complete | Toast notification + XP flyout number | Success chime (3-note ascending) | Double tap |
| Item picked up | Brief item icon flash near hands | Item-specific sound (metal, fabric, glass) | Light tap |
| Extraction started | Green progress circle + screen tint | Radio crackle + helicopter approach | Slow building rumble |
| Level up | Full-screen flash + level number overlay | Fanfare (4-note ascending, brass) | Strong rumble pattern |
| Empty magazine | "RELOAD" text flash + red ammo counter | Magazine click + dry fire sound | Triple tap |
| Low health | Red vignette + heartbeat pulse | Heartbeat audio + labored breathing | Rhythmic pulse (matching BPM) |
