---
title: "World & Map Design"
type: docs
---

## Map Design Philosophy

**Core Principles:**
1. **Readability** - Top-down perspective requires clear visual hierarchy.
2. **Tactical Depth** - Multiple routes, cover options, and vertical elements.
3. **Risk vs Reward** - Loot quality scales with danger level.
4. **Memorable Landmarks** - Facilitates easy navigation and team callouts.

---

## Extraction-Shooter Specifics

Primary and secondary design factors adapted for the extraction genre, directly influencing zone layouts.

### Primary Factors
1. **Verticality**
   - **Definition:** How height and layers affect play, visibility, and flanking.
   - **Application:**
     - **Hot Zones:** High verticality (3+ floors, catwalks) for complex CQB and vertical ambushes.
     - **Mid Zones:** Moderate verticality (2 floors, accessible rooftops) for vantage points.
     - **Edge Zones:** Mostly ground level with natural elevation changes.

2. **Size**
   - **Definition:** Horizontal scale relative to match duration (travel time vs. looting time).
   - **Application:**
     - **Hot Zones:** Condensed footprint with high asset density to force encounters.
     - **Edge Zones:** Expansive areas to allow safe spawning and initial movement.

3. **Population**
   - **Definition:** Player and AI entity density per square meter.
   - **Application:**
     - **Hot Zones:** Maximum density (High player convergence + Elite AI squads).
     - **Mid Zones:** Medium density (Roaming AI patrols, transiting players).
     - **Edge Zones:** Low density (Scattered AI, spawning/extracting players).

### Secondary Factors
- **Spawn/Exit Points:** Primarily located in **Edge Zones** to force inward movement. Conditional high-risk exits (e.g., rooftop helipads) may exist in **Hot Zones**.
- **Event Pockets / POIs:** Dynamic areas (Supply Drops, Contamination) that can temporarily transform safe **Mid Zones** into combat-heavy **Hot Zones**.
- **Line of Sight (LOS):** **Hot Zones** feature frequent blind spots and LOS breaks for tactical movement; **Edge Zones** offer longer sightlines but less hard cover.
- **Navigator Elements:** Ziplines, jump pads, and ladders are placed strategically to bridge **Mid Zone** gaps or provide rapid access to **Hot Zone** verticality.

---

## Map Structure

### Zone Types

#### 1. Hot Zones (Center Areas)
**Characteristics:**
- 60% loot spawn rate
- Rare and Epic items
- Heavy AI presence (10-15 enemies)
- Multiple entry points (5-7)
- Vertical gameplay (multi-floor buildings)

**Examples:**
- Power Plant central reactor
- Military Command Center
- Tech Research Facility

**Design Goals:**
- Create focal points for conflict
- Reward brave players
- Dynamic combat spaces

---

#### 2. Mid Zones (Transition Areas)
**Characteristics:**
- 40% loot spawn rate
- Uncommon and Rare items
- Moderate AI (5-8 enemies)
- 3-4 entry points
- Mixed indoor/outdoor environments

**Examples:**
- Office buildings
- Warehouses
- Residential blocks
- Industrial workshops

**Design Goals:**
- Provide safer looting options
- Connect hot zones to map edges
- Offer tactical choices for engagement

---

#### 3. Edge Zones (Perimeter)
**Characteristics:**
- 20% loot spawn rate
- Common items, basic supplies
- Minimal AI (0-3 enemies)
- Open areas
- Near extraction points

**Examples:**
- Forest perimeters
- Parking lots
- Abandoned camps
- Roadways

**Design Goals:**
- Safe spawn areas
- Quick escape routes
- Extraction defense positions

---

## Map Layouts

### Map 1: "Industrial Decay"

**Theme:** Abandoned industrial complex
**Size:** 1600m x 1600m
**Player Capacity:** 12-16 players
**Match Duration:** 15 minutes

**Layout Overview:**
```
                    NORTH
       [Extraction]   [Extraction]
            |             |
    [Forest]--[Warehouse District]--[Forest]
        |           |            |
[Spawn]---[Offices]--[POWER]--[Labs]---[Spawn]
        |           | PLANT|       |
    [Parking]--[Workshops] --[Storage]
            |             |
       [Extraction]   [Extraction]
                    SOUTH
```

**Key Locations:**

**1. Power Plant (Hot Zone - Center)**
- 4 floors
- Central reactor room (best loot)
- Catwalks and tight corridors
- AI Boss: "Reactor Guardian"
- Highly contested area

**2. Warehouse District (Mid Zone - West)**
- 6 large warehouses
- Open floor plans
- Good cover density
- Vehicle section (future update: drivable)

**3. Tech Labs (Mid Zone - East)**
- Research facility
- Clean rooms (sterile environment)
- Quest items spawn here
- Vertical gameplay (3 floors)

**4. Office Complex (Mid Zone - North)**
- Corporate offices
- Cubicle maze
- Excellent ambush spots
- Medium tier loot

**5. Workshops (Mid Zone - South)**
- Industrial repair shops
- Heavy machinery provides cover
- Crafting materials abundant

**6. Forest Perimeter (Edge Zone)**
- Natural cover (trees and rocks)
- Fewer sightlines
- Player spawn points
- 4 extraction zones

---

### Map 2: "Urban Ruins"

**Theme:** Post-disaster city zone
**Size:** 1800m x 1800m
**Player Capacity:** 16 players
**Match Duration:** 15 minutes

**Layout Overview:**
```
         [Subway]--[Mall]--[Subway]
              |      |        |
    [Park]--[Apts]--[PLAZA]--[Hotel]
         |      |      |         |
[Extraction]--[Street]--[Street]--[Extraction]
```

**Key Locations:**

**1. Central Plaza (Hot Zone)**
- Open square
- Central fountain provides cover
- Underground access points
- Supply drop landing zone

**2. Shopping Mall (Hot Zone)**
- 2 floors
- Stores contain high density loot
- Food court ambush point
- Skylights (dynamic lighting effects)

**3. Apartment Buildings (Mid Zone)**
- 5-story buildings
- Room-to-room CQB combat
- Balcony sniping positions
- Stairwell choke points

**4. Subway System (Mid Zone)**
- Underground tunnels network
- Connects different map areas
- Dark, close-quarters environment
- Unique lighting challenges

**5. Hotel (Mid Zone)**
- Luxury location styling
- Lobbies, guest rooms, rooftop bar
- Quest item spawns
- defensible position for extraction

**6. City Park (Edge Zone)**
- Trees and dense foliage
- Open sightlines across paths
- Extraction zones location

---

### Map 3: "Desert Outpost" (Post-Launch)

**Theme:** Military desert base
**Size:** 2000m x 2000m (larger, more open)
**Weather:** Sandstorms (dynamic)

**Key Features:**
- Long sightlines (sniper-friendly)
- Vehicle spawns
- Underground bunker system
- Dynamic sandstorm reduces visibility

---

## Map Elements

### Points of Interest (POI)

**Design Guidelines:**
- Each map: 12-15 major POIs
- Spacing: 150-250m apart
- Size variation: Small (single building) to Large (complex)
- Unique identifiers (visual landmarks)

**Naming Convention:**
- Memorable, short names
- Easy radio callouts
- Example: "Red Warehouse," "Big Tower," "Reactor"

---

### Cover System

**Cover Types:**

**Full Cover (100% protection)**
- Concrete walls
- Thick pillars
- Armored vehicles
- Metal containers

**Half Cover (60% protection)**
- Wooden crates
- Low walls
- Cars
- Machinery

**Soft Cover (30% protection)**
- Bushes (visual obstruction)
- Chain fences
- Thin walls
- Destructible objects

**Design Rules:**
- Never leave large open areas without cover
- Cover spacing: 5-10m intervals
- Mix cover heights
- Consider top-down sightlines

---

### Loot Distribution

**Container Types:**

**1. Common Crates (Gray)**
- Spawn: Edge và Mid zones
- Contents: Basic supplies, ammo, common weapons
- Quantity: 100-150 per map

**2. Military Lockers (Green)**
- Spawn: Mid zones
- Contents: Uncommon weapons, armor, meds
- Quantity: 60-80 per map

**3. Rare Safes (Blue)**
- Spawn: Hot zones, hidden locations
- Contents: Rare weapons, valuable items
- Quantity: 20-30 per map
- Require: Lockpick or Specialist ability

**4. Epic Vaults (Purple)**
- Spawn: Hot zone centers
- Contents: Epic+ items, quest items
- Quantity: 5-8 per map
- Require: Keycard (found in mid zones)

**5. Legendary Cache (Gold)**
- Spawn: 1-2 per map, random locations
- Contents: Legendary items guaranteed
- Require: Special key or team effort

---

### Extraction Zones

**Per Map:** 4-6 extraction points

**Placement Rules:**
- Near map edges
- 300-400m from hot zones
- Cover available nearby
- Multiple approach routes

**Extraction Types:**

**1. Helicopter Extract**
- Visual: Helicopter landing
- Duration: 30 seconds
- Max players: 4
- Audio cue: Helicopter sounds from far

**2. Vehicle Extract**
- Visual: Armored truck
- Duration: 30 seconds
- Max players: 6
- Audio cue: Engine sounds

**3. Underground Tunnel**
- Visual: Manhole entrance
- Duration: 45 seconds (slower)
- Max players: 2 (bottleneck)
- Audio cue: Metal clanging

**Activation:**
- Random 2-3 active per match
- Announced at 3-minute mark
- Cannot be camped from spawn (protection timer)

---

### Dynamic Elements

**Supply Drops**
- Timing: 5:00 and 10:00 into match
- Landing: Random mid-to-hot zones
- Visual: Signal flare, followed by parachute drop
- Audio: Plane flyover, warning siren
- Contents: High-tier loot, special weapons/items
- Radius: Creates temporary high-heat zone

**Contamination Zone**
- Timing: Starts at 12:00
- Effect: Shrinking safe zone
- Visual: Red fog, particle effects
- Damage: Increasing over time (10→50 HP/sec)
- Purpose: Forces player movement, prevents camping

**Environmental Hazards**

**1. Electrical Hazards**
- Exposed/Broken power lines
- Sparking machinery
- Damage: 5 HP/sec within area

**2. Radiation Zones** (Map-specific)
- Contaminated areas
- Damage: 10 HP/sec
- Reward: Best loot located inside

**3. Fire** (Dynamic)
- Can be caused by explosions
- Spreads slowly
- Damage: 15 HP/sec
- Blocks paths

---

## Environmental Storytelling

**Narrative Through Environment:**

**Industrial Decay Map:**
- Abandoned worker belongings and personal items
- Evacuation warning signs
- Broken and rusted machinery
- Graffiti from survivors or scavengers
- Evidence of environmental disasters

**Visual Clues:**
- Scattered documents (lore items)
- Propaganda posters
- Faction symbols and territorial markings
- Timeline of events shown through decay levels

**Purpose:**
- Build world lore
- Create atmosphere
- Deepen player immersion
- Provide context for Quests

---

## Verticality

**Top-Down Considerations:**

**Multi-Floor Buildings:**
- Clear visual distinction per floor
- Stairs và elevators (future)
- Different loot per floor
- Rooftop access

**Visual Solutions:**
- Floor transparency when player above/below
- Minimap floor indicators
- Height markers on UI
- Shadow effects

**Gameplay Impact:**
- Sniper positions (rooftops)
- Ambush from above
- Escape routes (parkour future)

---

## Navigation Design

**Wayfinding:**

**Visual Landmarks:**
- Tall structures (towers, smokestacks)
- Unique color schemes per area
- Distinct lighting differences
- Varied architectural styles

**Minimap Design:**
- Color-coded zones
- POI icons
- Extraction markers
- Player/enemy indicators
- Scale appropriate for mobile screens

**In-World Signs:**
- Directional signs (diegetic/in-universe)
- Zone markers
- Extraction indicators (visible from distance)

---

## Spawn System

**Spawn Points:**
- 8-12 spawn locations per map
- Located near map edges only
- Equidistant from hot zones (fairness)
- Random assignment
- 10-second protection shield

**Spawn Balancing:**
- No spawns near active combat
- Distance check from other players (minimum 100m)
- Visibility check (not in direct sightline)

---

## Map Balance Metrics

**Target Metrics:**

**Loot Distribution:**
- Common items: 60%
- Uncommon items: 25%
- Rare items: 10%
- Epic items: 4%
- Legendary items: 1%

**Combat Density:**
- Hot zones: 40% of kills
- Mid zones: 45% of kills
- Edge zones: 15% of kills

**Extraction Success:**
- Per zone: 20-30% usage rate
- No single zone dominates (>40%)

**Heatmaps Tracking:**
- Player death locations
- Loot pickup locations
- Time spent per zone
- Path travel frequency

---

## Weather & Time of Day

**Launch:** Static day lighting

**Post-Launch Features:**

**Weather System:**
- Clear (default)
- Rain (reduced visibility, louder footsteps)
- Fog (close-range combat favored)
- Sandstorm (Desert map)

**Time of Day:**
- Day (launch default)
- Dusk (future - different aesthetics)
- Night (future - flashlight mechanics)

---

## Map Rotation & Voting

**Launch:**
- 2 maps in rotation
- Random selection

**Post-Launch:**
- Map voting (3 options)
- Weighted random (prevent repeats)
- Featured map (events)

---

## Level Design Checklist

For each new map:

**Layout:**
- [ ] Balanced hot/mid/edge zones
- [ ] Multiple routes between POIs
- [ ] No dead-end areas
- [ ] Extraction zone placement
- [ ] Spawn point placement

**Loot:**
- [ ] Container placement (200-300)
- [ ] Rarity distribution balanced
- [ ] Quest item locations
- [ ] Supply drop landing zones

**Combat:**
- [ ] Cover density appropriate
- [ ] Sightline variety
- [ ] Flanking routes available
- [ ] Vertical elements considered

**Navigation:**
- [ ] Visual landmarks present
- [ ] Minimap readable
- [ ] Wayfinding clear
- [ ] Zone transitions smooth

**Performance:**
- [ ] Occlusion volumes set
- [ ] LOD configured
- [ ] Draw calls optimized
- [ ] Collision simplified

**Playtesting:**
- [ ] 10+ internal playtests
- [ ] Heatmap analysis
- [ ] Balance adjustments
- [ ] Bug fixes

---

## Future Map Concepts

**Map 4: "Flooded City"**
- Water mechanics
- Boat navigation
- Underwater areas

**Map 5: "Mountain Facility"**
- Snowy environment
- Cable cars
- Avalanche hazards

**Map 6: "Abandoned Airport"**
- Huge open tarmac
- Airport terminals
- Plane wrecks

---

---

## 📝 Document Ownership & Changelog

| Role            | Owner                   | Approver           |
| :-------------- | :---------------------- | :----------------- |
| **Author**      | Lead Level Designer     | Lead Game Designer |
| **Tech Review** | Environment Artist Lead | Technical Artist   |

**Recent Changes:**
*   **v1.1 (2026-02-09):** Added "Extraction-Shooter Specifics" section.
*   **v1.0 (2026-02-07):** Initial map design documentation.



