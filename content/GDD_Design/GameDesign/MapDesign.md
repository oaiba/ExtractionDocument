---
title: "Map Design - Level & Zone Design Rules"
type: docs
---

## Overview

Map Design defines how extraction zones are built for top-down tactical play. Maps must create readable routes, meaningful risk gradients, clear extraction choices, and strong landmarks without becoming battle royale arenas.

Each map should behave like a pressure machine. Spawns give players enough room to form a plan, mid-zones tempt them with better value, hotspots create collision, and extraction routes ask whether the current haul is worth protecting. The map is successful when players can explain their route after the raid: where they went, why they turned, where they heard danger, and why extraction felt possible or impossible.

Top-down readability is the governing constraint. A beautiful space that hides threats, blocks touch movement, or makes floor levels ambiguous is not ready for production. Landmarks, silhouettes, lighting, sound, and minimap language must all reinforce the same route decisions.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Primary map role | Support extraction decisions, not last-player-standing collapse |
| Camera assumption | Top-down tactical view with occlusion handling |
| Raid duration | 10-15 minutes |
| Core tension | High-value loot pulls players inward; extraction pulls them outward |
| Readability target | Threat, cover, path, floor level, and extraction state readable on mobile |

## Zone Model

Zones are not just loot bands. They are pacing tools. Edge zones teach the map and give low-pressure value, mid-zones create branching decisions, and hot zones create stories players remember. The player should understand when they are moving into danger before the first shot is fired.

| Zone | Loot | AI Threat | Player Pressure | Design Purpose |
| :--- | :--- | :--- | :--- | :--- |
| Edge / Spawn | Common | Light | Low | Let players orient and build confidence |
| Mid Zone | Common to Rare | Medium | Medium | Create route decisions and first contact |
| Hot Zone | Rare to Legendary | Heavy | High | Create major risk/reward decisions |
| Event Zone | Event-defined | Variable | Very high | Pull players together for timed opportunities |
| Extraction Zone | Reward-neutral | Variable | High near end | Force commitment and route discipline |

## Raid Movement Logic

Routes should support different player personalities. A cautious solo needs a survivable edge path. A confident squad needs a contestable route through value. A quest-focused player needs a readable way to reach an objective and leave. These routes can intersect, but they should not collapse into one mandatory lane.

| Decision Point | Safe Route | Balanced Route | High-Risk Route |
| :--- | :--- | :--- | :--- |
| Spawn on edge | Read nearby extraction and edge loot | Move toward mid-zone objective | Rush hotspot or event zone |
| First loot choice | Common value, low contact | Mixed loot, moderate contact | Rare loot, high contact |
| Rotation | Early extraction path | Mid-map flank to extraction | Contest center then rotate late |
| Final choice | Extract and bank loot | Extract or re-enter based on squad state | Push final value or risk timeout |

## Extraction Placement Rules

Extraction placement is where the map cashes out its promises. If extraction is too safe, looting has no tension. If extraction is too random or too campable, losses feel cheap. The best extraction point creates a short, readable final test: commit, defend, and leave.

| Rule | Requirement |
| :--- | :--- |
| Minimum options | Each player should have multiple plausible extraction routes |
| Distance | At least one extraction must require route planning, not immediate safety |
| Contestability | High-value extracts should have readable risk and counterplay |
| Signaling | Extraction state must be visible and audible before commitment |
| Anti-camping | Cover, sightlines, alternate routes, and timers must limit hard camping |
| Mode support | Ranked, Scav, and events can modify extraction rules but not clarity |

## Top-Down Readability

Readability issues must be solved in level design before UI tries to patch them. If roofs, props, fog, or vertical floors hide critical combat information, the map should use cutaways, fade rules, simplified collision, or stronger silhouettes. The HUD should confirm information, not rescue a confusing layout.

| Problem | Design Response |
| :--- | :--- |
| Tall buildings hide players | Use cutaways, fade roofs, outlines, or floor indicators |
| Visual clutter hides loot | Use rarity shapes, glow limits, and contextual labels |
| Verticality becomes confusing | Keep floor transitions explicit and minimize hidden sightlines |
| Cover is unclear | Use consistent silhouettes and readable edge highlights |
| Players lose extraction direction | Compass, minimap, world marker, and audio cues reinforce each other |

## Building And Interior Rules

| Element | Guideline |
| :--- | :--- |
| Rooms | Large enough for touch movement, cover, and squad visibility |
| Corridors | Avoid long invisible kill tunnels; add side exits and readable cover |
| Doors | Use as tactical information, not cheap surprise blockers |
| Windows | Support scouting and risk, but avoid unreadable one-way shots |
| Stairs / elevators | Mark floor changes clearly in HUD and map |

## Loot Placement Rules

Loot placement should tell players what kind of place they are entering. A clinic implies medical value and quiet risk; an armory implies conflict; a server room implies tech rewards and flank routes. Repeated loot language helps players plan without memorizing every container spawn.

| Loot Type | Best Location | Risk Requirement |
| :--- | :--- | :--- |
| Medical | Clinics, ambulances, checkpoints | Low to medium |
| Industrial | Factories, warehouses, maintenance rooms | Medium |
| Military | Checkpoints, armories, command rooms | High |
| Tech | Labs, offices, server rooms | Medium to high |
| Legendary | Hot zones, bosses, events, locked rooms | Very high |

## Encounter Examples

A safe edge route might contain low-value containers, one light AI patrol, and a clear extraction branch. It teaches the map and lets a cautious player bank value without becoming the best farming option.

A mid-zone route might split between a clinic, a warehouse, and a noisy shortcut. The player can choose healing security, industrial value, or speed. Each option creates different sound and sightline risks.

A hot zone should create a readable promise: rare value is present, but the route in and out is exposed, loud, or AI-defended. Players should know they are entering a contested space before the first fight begins.

## Map Failure Cases

- If players repeatedly die without seeing the attacker, sightlines or occlusion are failing.
- If extraction camping dominates, exits need alternate approaches, audio tells, or timer changes.
- If all squads take the same route, loot and objective distribution are too centralized.
- If players ignore interiors, room scale, entry risk, or rewards may be wrong.
- If mobile players miss stairs or doors, floor markers and silhouettes need stronger treatment.

## Map Tuning Knobs

- Spawn spacing controls early safety; crowded spawns create cheap deaths before planning begins.
- Loot density controls route pressure; dense hotspots need multiple readable exits.
- Landmark strength controls memory; every major route should have a nameable reference point.
- Extraction distance controls commitment; short routes reduce tension and long routes punish slow players.
- AI placement controls information; AI can reveal routes, protect value, and create sound pressure.
- Cover spacing controls combat rhythm; too little cover creates aim checks, too much creates stalemates.

## Map Readiness Checklist

| Check | Pass Criteria |
| :--- | :--- |
| Route clarity | New player can identify at least two plausible paths |
| Hotspot clarity | High-value areas are visually and mechanically obvious |
| Extraction fairness | Extracts are contestable but not impossible |
| Mobile readability | Threats and cover remain readable on 5 inch screens |
| Spawn fairness | Spawn positions avoid immediate unavoidable deaths |
| Audio support | Key threats and extraction events have clear sound cues |

## Cross-References

| Topic | Page |
| :--- | :--- |
| Raid pacing | [Core Gameplay](coregameplay/index.html) |
| Map UI and pings | [Navigation & Map](navigationandmap/index.html) |
| Mode variations | [Game Modes](gamemodes/index.html) |
| Loadout map selection | [Loadout Preparation](loadoutpreparation/index.html) |
