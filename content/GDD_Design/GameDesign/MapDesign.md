---
title: "Map Design - Level & Zone Design Rules"
type: docs
---

## Overview

Map Design defines how extraction zones are built for top-down tactical play. Maps must create readable routes, meaningful risk gradients, clear extraction choices, and strong landmarks without becoming battle royale arenas.

## Key Decisions

| Area | Direction |
| :--- | :--- |
| Primary map role | Support extraction decisions, not last-player-standing collapse |
| Camera assumption | Top-down tactical view with occlusion handling |
| Raid duration | 10-15 minutes |
| Core tension | High-value loot pulls players inward; extraction pulls them outward |
| Readability target | Threat, cover, path, floor level, and extraction state readable on mobile |

## Zone Model

| Zone | Loot | AI Threat | Player Pressure | Design Purpose |
| :--- | :--- | :--- | :--- | :--- |
| Edge / Spawn | Common | Light | Low | Let players orient and build confidence |
| Mid Zone | Common to Rare | Medium | Medium | Create route decisions and first contact |
| Hot Zone | Rare to Legendary | Heavy | High | Create major risk/reward decisions |
| Event Zone | Event-defined | Variable | Very high | Pull players together for timed opportunities |
| Extraction Zone | Reward-neutral | Variable | High near end | Force commitment and route discipline |

## Raid Movement Logic

| Decision Point | Safe Route | Balanced Route | High-Risk Route |
| :--- | :--- | :--- | :--- |
| Spawn on edge | Read nearby extraction and edge loot | Move toward mid-zone objective | Rush hotspot or event zone |
| First loot choice | Common value, low contact | Mixed loot, moderate contact | Rare loot, high contact |
| Rotation | Early extraction path | Mid-map flank to extraction | Contest center then rotate late |
| Final choice | Extract and bank loot | Extract or re-enter based on squad state | Push final value or risk timeout |

## Extraction Placement Rules

| Rule | Requirement |
| :--- | :--- |
| Minimum options | Each player should have multiple plausible extraction routes |
| Distance | At least one extraction must require route planning, not immediate safety |
| Contestability | High-value extracts should have readable risk and counterplay |
| Signaling | Extraction state must be visible and audible before commitment |
| Anti-camping | Cover, sightlines, alternate routes, and timers must limit hard camping |
| Mode support | Ranked, Scav, and events can modify extraction rules but not clarity |

## Top-Down Readability

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

| Loot Type | Best Location | Risk Requirement |
| :--- | :--- | :--- |
| Medical | Clinics, ambulances, checkpoints | Low to medium |
| Industrial | Factories, warehouses, maintenance rooms | Medium |
| Military | Checkpoints, armories, command rooms | High |
| Tech | Labs, offices, server rooms | Medium to high |
| Legendary | Hot zones, bosses, events, locked rooms | Very high |

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
| Raid pacing | [Core Gameplay](coregameplay.html) |
| Map UI and pings | [Navigation & Map](navigationandmap.html) |
| Mode variations | [Game Modes](gamemodes.html) |
| Loadout map selection | [Loadout Preparation](loadoutpreparation.html) |
