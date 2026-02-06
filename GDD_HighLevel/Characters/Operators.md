# Characters

**[← Previous: Core Gameplay](../GameDesign/CoreGameplay.md)** | **[Index](../README.md)** | **[Next: Map Design →](../World/MapDesign.md)**

---

## Operator Overview

**Operators** are playable characters in the game. Each operator has unique abilities, visual design, and playstyle. Players unlock operators through progression and can level up each operator individually.

**Design Philosophy:**
- Class-based but not rigid
- Abilities complement tactics, don't replace skill
- Visual clarity (easy identification)
- Balanced risk/reward

---

## Operator Classes

### 1. ASSAULT - "Frontline Aggressor"

**Role:** Aggressive entry fragger, high damage dealer

**Character Profile:**
- Former military special forces
- Age: 28-35
- Personality: Confident, aggressive, direct

**Visual Design:**
- Tactical vest with ammo pouches
- Combat helmet option
- Rugged, practical gear
- Color theme: Military green with orange accents

**Ability: Combat Stim**
- Cooldown: 90 seconds
- Duration: 10 seconds
- Effect: +25% damage output, +10% movement speed
- Visual: Orange tint on operator, screen vignette
- Audio: Heartbeat increase, adrenaline sound

**Passive:** Sprint Speed
- Effect: +10% sprint speed permanently
- Synergy: Chasing enemies, reposition quickly

**Starting Gear:**
- Primary: Assault Rifle (mid-tier)
- Secondary: Pistol
- Equipment: 2x Frag Grenades
- Armor: Medium armor (50 armor points)

**Playstyle:**
- Aggressive push
- First into combat
- High risk, high reward
- Best for experienced players

**Counters:**
- Specialist's EMP cancels stim
- Tank can absorb damage
- Ambush tactics

**Strengths:**
- Raw combat power
- Fast rotation
- Intimidation factor

---

### 2. SUPPORT - "Team Medic"

**Role:** Keep team alive, sustain in extended fights

**Character Profile:**
- Former combat medic
- Age: 25-30
- Personality: Caring, strategic, reliable

**Visual Design:**
- Medical cross markings
- First aid pouches visible
- Light armor for mobility
- Color theme: White with blue accents

**Ability: Healing Drone**
- Cooldown: 120 seconds
- Duration: 20 seconds
- Effect: Deploys flying drone, heals 5 HP/sec in 10m radius
- Visual: Green glow around drone, healing particles
- Audio: Soft humming, healing sound

**Passive:** Medical Expertise
- Effect: +20% effectiveness of healing items
- Example: Medkit heals 60 HP instead of 50 HP

**Starting Gear:**
- Primary: SMG (high fire rate)
- Secondary: Pistol
- Equipment: 3x Medkits, 1x Healing Drone
- Armor: Light armor (30 armor points)

**Playstyle:**
- Support from mid-range
- Prioritize team survival
- Play near cover
- Best for team players

**Counters:**
- Focus fire kills before healing
- Flank to kill drone
- Sniper one-shots

**Strengths:**
- Team sustainability
- Economic advantage (fewer healing items needed)
- Extended engagements

---

### 3. RECON - "Information Specialist"

**Role:** Scout enemy positions, provide intel

**Character Profile:**
- Former intelligence operative
- Age: 30-38
- Personality: Calculated, patient, observant

**Visual Design:**
- Sleek, low-profile gear
- Tech devices visible
- Camouflage patterns
- Color theme: Dark gray with cyan accents

**Ability: UAV Scan**
- Cooldown: 100 seconds
- Duration: 8 seconds
- Effect: Reveals all enemies in 30m radius on minimap
- Visual: Radar pulse animation, marked enemies
- Audio: Sonar ping sound

**Passive:** Sneaky Movement
- Effect: +15% movement speed when crouching
- Additional: -30% footstep volume

**Starting Gear:**
- Primary: Silenced SMG
- Secondary: Silenced Pistol
- Equipment: 2x Sensor Mines (detect enemies)
- Armor: Light armor (30 armor points)

**Playstyle:**
- Stealth and information gathering
- Flank routes
- Ambush setups
- Best for strategic players

**Counters:**
- Assault can rush after UAV reveals
- Tank not afraid of being revealed
- Area denial prevents sneaking

**Strengths:**
- Information advantage
- Ambush potential
- Solo viability

---

### 4. TANK - "Damage Sponge"

**Role:** Absorb damage, hold positions, protect team

**Character Profile:**
- Former riot control / bodyguard
- Age: 35-45
- Personality: Stoic, protective, disciplined

**Visual Design:**
- Heavy armor plating
- Intimidating silhouette
- Riot shield (when ability active)
- Color theme: Dark metal with red accents

**Ability: Riot Shield Deploy**
- Cooldown: 80 seconds
- Duration: 15 seconds
- Effect: Pull out riot shield, blocks frontal damage 100%
- Downside: Cannot shoot while active, movement -40%
- Visual: Large transparent shield with damage cracks
- Audio: Shield deployment sound, impact clangs

**Passive:** Reinforced Armor
- Effect: +25% maximum armor capacity (125 armor max vs 100)
- Additional: Armor damage reduction +10%

**Starting Gear:**
- Primary: Shotgun (close range power)
- Secondary: Revolver (high damage)
- Equipment: 1x Flashbang, Extra Armor Plate
- Armor: Heavy armor (75 armor points)

**Playstyle:**
- Point defense
- Lead pushes
- Protect teammates
- Best for defensive players

**Counters:**
- Flanking bypasses shield
- Specialist EMP disables shield
- Slow movement vulnerable to kiting

**Strengths:**
- Survivability
- Area denial
- Extraction defense

---

### 5. SPECIALIST - "Tech Expert"

**Role:** Utility, control, disruption

**Character Profile:**
- Former engineer / hacker
- Age: 22-28
- Personality: Clever, unconventional, adaptable

**Visual Design:**
- Tech gadgets visible
- Utility vest with tools
- Fingerless gloves (hacker aesthetic)
- Color theme: Black with yellow accents

**Ability: EMP Blast**
- Cooldown: 110 seconds
- Duration: Instant
- Effect: 15m radius, disables enemy abilities 10 sec, destroys gadgets
- Visual: Blue electric pulse wave
- Audio: Electric discharge sound

**Passive:** Expanded Inventory
- Effect: +2 inventory slots (1x2 grid)
- Benefit: Carry more loot per run

**Starting Gear:**
- Primary: Pistol (versatile)
- Secondary: SMG
- Equipment: 2x EMP Grenades, Lockpick Tool
- Armor: Medium armor (50 armor points)

**Playstyle:**
- Flexible, adaptable
- Counter enemy abilities
- Maximize loot efficiency
- Best for creative players

**Counters:**
- Raw combat power beats utility
- Assault can bum-rush before EMP
- Long range avoids EMP radius

**Strengths:**
- Versatility
- Loot capacity
- Counter-play potential

---

## Operator Balance Matrix

|                | Combat Power | Survivability | Utility | Team Value | Solo Viability |
| -------------- | :----------: | :-----------: | :-----: | :--------: | :------------: |
| **Assault**    |     9/10     |     6/10      |  4/10   |    6/10    |      8/10      |
| **Support**    |     5/10     |     7/10      |  8/10   |   10/10    |      4/10      |
| **Recon**      |     6/10     |     5/10      |  9/10   |    8/10    |      9/10      |
| **Tank**       |     7/10     |     10/10     |  5/10   |    8/10    |      5/10      |
| **Specialist** |     5/10     |     6/10      |  10/10  |    7/10    |      7/10      |

---

## Operator Progression

### Leveling System

**Max Level per Operator:** 50

**XP Sources:**
- Operator usage: XP gained in matches
- Challenges: Operator-specific challenges
- Achievements: Milestones

**Example Progression:**

```
Level 1: Base operator unlocked
Level 5: Unlock ability upgrade slot 1
Level 10: Unlock cosmetic skin 1
Level 15: Unlock stat boost 1 (+5% health)
Level 20: Unlock ability upgrade slot 2
Level 25: Unlock cosmetic skin 2
Level 30: Unlock stat boost 2 (+5% stamina)
Level 35: Unlock ability upgrade slot 3
Level 40: Unlock elite cosmetic skin
Level 45: Unlock stat boost 3 (+5% sprint speed)
Level 50: Unlock prestige cosmetics
```

### Ability Upgrades

**Example (Assault Combat Stim):**

**Upgrade Slot 1:**
- Option A: Extended Duration (+5 seconds)
- Option B: Reduced Cooldown (-20 seconds)
- Option C: Health Regen (+10 HP over duration)

**Upgrade Slot 2:**
- Option A: Damage Boost (+30% instead of +25%)
- Option B: Damage Resistance (+20% damage reduction)
- Option C: Reload Speed (+50% reload speed)

**Upgrade Slot 3:**
- Option A: Team Buff (Nearby allies get +10% damage)
- Option B: Overheal (Heal 20 HP on activation)
- Option C: Immunity (Cannot be stunned during stim)

**Design Note:** Only 1 option per slot active. Encourages build diversity.

---

## Operator Unlock Progression

### Starting Operators (Free)
- **Assault** - Beginner-friendly
- **Support** - Learn teamplay

### Unlock Requirements

**Recon:**
- Level 5 account level
- Complete "Scout Quest" (Deploy 10 sensor mines)
- OR Purchase with 5,000 Credits

**Tank:**
- Level 10 account level
- Complete "Tank Quest" (Absorb 5,000 damage)
- OR Purchase with 7,500 Credits

**Specialist:**
- Level 15 account level
- Complete "Tech Quest" (Destroy 20 gadgets)
- OR Purchase with 10,000 Credits

**Future Operators:**
- Season Battle Pass rewards
- Special events
- Purchase with Credits or Premium Currency

---

## Operator Synergies

### Good Combinations

**Assault + Support:**
- Assault pushes, Support heals
- High aggression with sustainability

**Recon + Specialist:**
- Intel + Utility
- Information control dominance

**Tank + Assault:**
- Tank leads, Assault follows
- Overwhelming push power

**Support + Anyone:**
- Healing always valuable

### Counter Compositions

**vs Heavy Tank Team:**
- Use Specialist EMP + Recon flanks

**vs Stealth Recon Team:**
- Use Tank area control + Support healing

**vs Aggressive Assault Team:**
- Use Recon information + Tank defense

---

## Visual Design Guidelines (For Artists)

### Character Silhouettes

**Priority:** Instant recognition from top-down

**Design Rules:**
1. Each operator must have unique silhouette
2. Differentiate through gear and posture
3. Size variations (Tank biggest, Recon smallest)
4. Distinct color themes

### Color Coding

**Team Colors (Multiplayer):**
- Your Team: Blue markers
- Enemy Teams: Red markers
- Neutral (AI): Yellow markers

**Operator Accent Colors:**
- Assault: Orange
- Support: Blue
- Recon: Cyan
- Tank: Red
- Specialist: Yellow

### Animation Guidelines

**Movement:**
- Walk cycle: 1 second loop
- Sprint cycle: 0.7 second loop
- Crouch walk: 1.3 second loop

**Combat:**
- Weapon fire: Quick, snappy
- Reload: Clear, readable
- Ability use: Distinct, recognizable

**Hit Reactions:**
- Light hit: Small flinch
- Heavy hit: Larger stagger
- Death: Dramatic but quick (mobile)

---

## Cosmetic Customization

### Cosmetic Types

**1. Skins (Full Operator Reskin)**
- Default skin: Free
- Common skins: 500 Credits
- Rare skins: 1,000 Credits
- Epic skins: Premium Currency only
- Legendary skins: Battle Pass / Events

**2. Headgear**
- Helmets, hats, masks
- Mix and match with skins

**3. Weapon Skins**
- Applied to all weapons of operator
- Separate from operator skins

**4. Emotes**
- Victory emotes
- Taunt emotes (risky in-game)

**5. Kill Effects**
- Visual effect when eliminating enemy
- Subtle, no P2W advantage

### Monetization Note

**All cosmetic only - No gameplay advantages**

---

## Voice Lines & Personality

### Assault Voice Examples
- "Contact! Engaging!"
- "Pushing in!"
- "They're not getting away!"
- "Extraction secured. Let's move!"

### Support Voice Examples
- "Healing up!"
- "Cover me while I patch you!"
- "Stay close, I've got your back!"
- "Everyone okay?"

### Recon Voice Examples
- "Multiple contacts detected."
- "Staying low."
- "They won't see me coming."
- "Intel gathered."

### Tank Voice Examples
- "I'll take point."
- "On me! I'll cover you!"
- "That all you got?"
- "Position held."

### Specialist Voice Examples
- "Systems disrupted!"
- "Got something here..."
- "Let's see what this does."
- "Tech advantage secured."

---

## Future Operators (Post-Launch)

### Operator 6: "SHADOW" - Stealth Assassin
- Ability: Turn invisible for 5 seconds
- Passive: Bonus damage from behind

### Operator 7: "ENGINEER" - Deployable Turret
- Ability: Deploy auto-turret
- Passive: Faster interaction speed

### Operator 8: "PYROMANIAC" - Fire Specialist
- Ability: Molotov area denial
- Passive: Fire damage immunity

**Note:** Detailed design after feedback from launch operators

---

**[← Previous: Core Gameplay](../GameDesign/CoreGameplay.md)** | **[Index](../README.md)** | **[Next: Map Design →](../World/MapDesign.md)**
