# World & Map Design

**[← Previous: Operators](../Characters/Operators.md)** | **[Index](../README.md)** | **[Next: Art Direction →](../Visuals/ArtDirection.md)**

---

## Map Design Philosophy

**Core Principles:**
1. **Readability** - Top-down perspective cần clear visual hierarchy
2. **Tactical Depth** - Multiple routes, cover options, vertical elements
3. **Risk vs Reward** - Loot quality scales với danger
4. **Memorable Landmarks** - Easy navigation và callouts

---

## Map Structure

### Zone Types

#### 1. Hot Zones (Center Areas)
**Characteristics:**
- 60% loot spawn rate
- Rare và Epic items
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
- Uncommon và Rare items
- Moderate AI (5-8 enemies)
- 3-4 entry points
- Mixed indoor/outdoor

**Examples:**
- Office buildings
- Warehouses
- Residential blocks
- Industrial workshops

**Design Goals:**
- Provide safe(r) looting options
- Connect hot zones to edges
- Offer tactical choices

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
- Catwalks và tight corridors
- AI Boss: "Reactor Guardian"
- Highly contested

**2. Warehouse District (Mid Zone - West)**
- 6 large warehouses
- Open floor plans
- Good cover
- Vehicle section (future: drivable)

**3. Tech Labs (Mid Zone - East)**
- Research facility
- Clean rooms
- Quest items spawn here
- Vertical gameplay (3 floors)

**4. Office Complex (Mid Zone - North)**
- Corporate offices
- Cubicle maze
- Good ambush spots
- Medium loot

**5. Workshops (Mid Zone - South)**
- Industrial repair shops
- Heavy machinery cover
- Crafting materials

**6. Forest Perimeter (Edge Zone)**
- Natural cover (trees)
- Fewer sightlines
- Spawn points
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
- Fountain cover
- Underground access
- Supply drop landing zone

**2. Shopping Mall (Hot Zone)**
- 2 floors
- Stores với loot
- Food court ambush point
- Skylights (lighting effects)

**3. Apartment Buildings (Mid Zone)**
- 5-story buildings
- Room-to-room combat
- Balcony sniping positions
- Stairwell chokes

**4. Subway System (Mid Zone)**
- Underground tunnels
- Connect different areas
- Dark, close-quarters
- Unique lighting challenges

**5. Hotel (Mid Zone)**
- Luxury location
- Lobbies, rooms, rooftop
- Quest item spawns
- Good extraction defense

**6. City Park (Edge Zone)**
- Trees và foliage
- Open sightlines
- Extraction zones

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
- Timing: 5:00 và 10:00 into match
- Landing: Random mid-to-hot zones
- Visual: Flare, then parachute drop
- Audio: Plane flyover, warning siren
- Contents: High-tier loot, special items
- Radius: Creates temporary hot zone

**Contamination Zone**
- Timing: Starts at 12:00
- Effect: Shrinking safe zone
- Visual: Red fog, particle effects
- Damage: Increasing over time (10→50 HP/sec)
- Purpose: Force player movement, prevent camping

**Environmental Hazards**

**1. Electrical Hazards**
- Broken power lines
- Sparking machinery
- Damage: 5 HP/sec trong area

**2. Radiation Zones** (Map-specific)
- Contaminated areas
- Damage: 10 HP/sec
- Reward: Best loot inside

**3. Fire** (Dynamic)
- Can be caused by explosions
- Spreads slowly
- Damage: 15 HP/sec
- Blocks paths

---

## Environmental Storytelling

**Narrative Through Environment:**

**Industrial Decay Map:**
- Abandoned worker belongings
- Warning signs về evacuation
- Broken machinery
- Graffiti từ survivors
- Environmental disasters visible

**Visual Clues:**
- Scattered documents (lore items)
- Propaganda posters
- Faction symbols
- Timeline của events qua decay levels

**Purpose:**
- Build world lore
- Create atmosphere
- Player immersion
- Quest context

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
- Lighting differences
- Architectural styles

**Minimap Design:**
- Color-coded zones
- POI icons
- Extraction markers
- Player/enemy indicators
- Scale appropriate cho mobile screens

**In-World Signs:**
- Directional signs (in-universe)
- Zone markers
- Extraction indicators (far visible)

---

## Spawn System

**Spawn Points:**
- 8-12 spawn locations per map
- Near map edges only
- Equidistant từ hot zones (fairness)
- Random assignment
- 10-second protection shield

**Spawn Balancing:**
- No spawns near active combat
- Distance check từ other players (minimum 100m)
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

**[← Previous: Characters](./03_Characters.md)** | **[High-Level Index](./README.md)** | **[Next: Art Direction →](./05_ArtDirection.md)**
