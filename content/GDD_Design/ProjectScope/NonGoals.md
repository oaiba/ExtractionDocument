---
title: "Non-Goals & Explicit Exclusions"
type: docs
---

## 🚫 Purpose of This Document

**Why define what we WON'T do?**

This document explicitly states features, systems, and approaches that are **intentionally excluded** from the game. This prevents:
- **Scope creep** - "Why don't we just add X?"
- **Design drift** - Losing focus on core pillars
- **Resource waste** - Building things that don't fit
- **Team confusion** - Everyone understands boundaries

**Important:** Non-goals are not "never" - they're "not now and not a priority." Some may be reconsidered post-launch based on data.

---

## ❌ Gameplay Non-Goals

### We Are NOT Building a Battle Royale

| Aspect          | Our Game           | Battle Royale      |
| :-------------- | :----------------- | :----------------- |
| Player count    | 15-20              | 100+               |
| Win condition   | Extract with loot  | Be last alive      |
| Match structure | Enter/exit anytime | Single elimination |
| Loadout         | Bring your own     | Find in-match      |
| Progression     | Persistent         | Per-match reset    |

**Why not:**
- Market saturated with BRs
- Different core fantasy
- Technical complexity not justified
- Our extraction loop is the differentiator

**Decision status:** ✅ Final - Will not change

---

### We Are NOT Building an MMORPG

**Excluded features:**
- ❌ Persistent open world (instance-based instead)
- ❌ Massive player counts in same space
- ❌ World bosses requiring 50+ players
- ❌ Player housing/persistent bases
- ❌ Deep crafting with gathering professions
- ❌ Story-driven questing as primary content

**Why not:**
- Scope explosion
- Mobile performance/battery concerns
- Session time mismatch (10-15 min vs hours)
- Different audience expectations

**Decision status:** ✅ Final

---

### We Are NOT Building an Esport (Initially)

**Excluded at launch:**
- ❌ Spectator mode (add post-launch)
- ❌ Tournament infrastructure
- ❌ Official competitive leagues
- ❌ LAN event support
- ❌ Detailed replay system

**Why not:**
- Launch focus is on core game
- Esport features expensive to build well
- Must prove game success first
- Community must grow organically

**Decision status:** 🟡 Deferred to Year 2+

---

### We Are NOT Targeting Ultra-Realism

**Excluded approaches:**
- ❌ Simulation-level weapon ballistics
- ❌ Complex medical system (EFT-style surgery)
- ❌ Realistic magazine management
- ❌ Permanent character injury
- ❌ Hunger/thirst survival mechanics

**Why not:**
- Mobile audience preference for accessibility
- Session time constraints
- Steep learning curve hurts retention
- We want "tactical" not "tedious"

**Decision status:** ✅ Final

---

### We Are NOT Adding Vehicles (Initially)

**Excluded:**
- ❌ Drivable vehicles
- ❌ Vehicle combat
- ❌ Vehicle customization

**Why not:**
- Map size doesn't require vehicles
- Physics complexity on mobile
- Balance implications with extraction
- Dev time better spent elsewhere

**Decision status:** 🟡 Consider for large desert map (Season 4+)

---

### We Are NOT Building Base Building

**Excluded:**
- ❌ Player-constructed structures
- ❌ Fortification mechanics
- ❌ Clan bases/hideouts

**Why not:**
- Significantly increases scope
- Server/persistence complexity
- Doesn't fit extraction loop
- Fortnite already owns this space

**Decision status:** ✅ Final

---

## ❌ Monetization Non-Goals

### We Will NOT Sell Gameplay Advantage

**Explicitly NOT for sale:**
- ❌ Weapons with better stats
- ❌ Armor with better protection
- ❌ Operator stat boosts
- ❌ Reduced matchmaking times for money
- ❌ Better loot chance for payers
- ❌ Extra protected slots for money (only credits)

**Why not:**
- Destroys competitive integrity
- Community backlash guaranteed
- Long-term player value > short-term revenue
- This is a non-negotiable pillar

**Decision status:** ✅ Final - Red line

---

### We Will NOT Have Loot Boxes (Randomized Purchases)

**Excluded:**
- ❌ Blind random item boxes for real money
- ❌ Gacha-style character pulls
- ❌ Mystery bundles

**What we DO have:**
- ✅ Battle Pass (known rewards)
- ✅ Direct purchase cosmetics
- ✅ Occasional free random rewards (gameplay only)

**Why not:**
- Legal issues in multiple regions
- Ethical concerns
- Negative player perception
- Transparent model builds trust

**Decision status:** ✅ Final

---

### We Will NOT Have Energy Systems

**Excluded:**
- ❌ Limited plays per day
- ❌ Lives that regenerate over time
- ❌ Pay-to-play-more mechanics

**Why not:**
- Players should play as much as they want
- Energy systems are frustrating
- Revenue comes from engagement, not gating

**Decision status:** ✅ Final

---

### We Will NOT Have Forced Ads

**Excluded:**
- ❌ Interstitial ads between matches
- ❌ Ads required for core gameplay
- ❌ Banner ads in gameplay

**What we MIGHT have:**
- ⚠️ Optional rewarded ads (watch for small bonus)
- Only in specific contexts (post-match, daily reward)

**Why not:**
- Premium experience expectation
- Ads destroy immersion
- Whales won't tolerate ads

**Decision status:** ✅ Final

---

## ❌ Technical Non-Goals

### We Are NOT Supporting Ancient Devices

**Minimum specs (firm):**
- Android: 3GB RAM, Snapdragon 660 equivalent, Android 8.0+
- iOS: iPhone 8 / iPad 6th gen or newer, iOS 14+

**NOT supported:**
- ❌ Devices below 3GB RAM
- ❌ Android 7.x or below
- ❌ iPhone 7 or older
- ❌ Devices without OpenGL ES 3.0

**Why not:**
- Performance compromises hurt everyone
- Diminishing returns chasing old hardware
- Security concerns with old OS
- Future-proofing the codebase

**Decision status:** ✅ Final

---

### We Are NOT Building Offline Mode

**Excluded:**
- ❌ Single-player offline play
- ❌ Play without internet
- ❌ Local multiplayer

**Why not:**
- Anti-cheat requires server authority
- Progression must be verified
- Core experience is multiplayer
- Data sync complexity not worth it

**Decision status:** ✅ Final

---

### We Are NOT Native on All Platforms Initially

**Launch platforms:**
- ✅ Android (Google Play)
- ✅ iOS (App Store)
- ⏳ PC (Epic/Steam) - Post-launch

**NOT at launch:**
- ❌ Console (PlayStation, Xbox, Switch)
- ❌ Web version
- ❌ Mac native

**Why not:**
- Focus resources on core platforms
- Console certification is expensive/slow
- Mobile-first means mobile quality first

**Decision status:** 🟡 Console considered for Year 2

---

## ❌ Content Non-Goals

### We Are NOT Pursuing Licensing/IP Crossovers

**Excluded:**
- ❌ Movie/TV character skins
- ❌ Other game character crossovers
- ❌ Celebrity athlete partnerships
- ❌ Brand collaborations (energy drinks, etc.)

**Why not:**
- Expensive licensing fees
- Potential lore conflicts
- Dependency on external partners
- Want to build our own IP value

**Decision status:** 🟡 Reconsider after Year 1 success

---

### We Are NOT Creating Player-Generated Content

**Excluded:**
- ❌ Custom maps
- ❌ Mod support
- ❌ User-created skins
- ❌ Workshop/marketplace

**Why not:**
- QA nightmare on mobile
- Moderation requirements massive
- Technical complexity
- Security vulnerabilities

**Decision status:** ✅ Final for mobile

---

### We Are NOT Doing Extensive Voice Acting

**Excluded:**
- ❌ Full narrative voice acting
- ❌ Voiced quest dialogues
- ❌ NPC conversations

**What we DO have:**
- ✅ Operator combat callouts
- ✅ Tutorial narration
- ✅ Announcer voice

**Why not:**
- Budget constraints
- Localization multiplication
- Download size concerns
- Text is more flexible

**Decision status:** ✅ Final for launch

---

## ❌ Social/Community Non-Goals

### We Are NOT Building Social Media

**Excluded:**
- ❌ In-game feed/timeline
- ❌ Public profiles with posts
- ❌ Following/followers system
- ❌ Content sharing within game

**Why not:**
- Moderation nightmare
- Liability concerns
- Distracts from gameplay
- Use existing platforms instead

**Decision status:** ✅ Final

---

### We Are NOT Allowing Real-Money Trading

**Excluded:**
- ❌ Player-to-player item sales for cash
- ❌ Official marketplace for real money
- ❌ NFTs or blockchain items

**Why not:**
- Legal complexity (gambling, securities)
- Black market encouragement
- Exploit incentive for hackers
- Damages economy design

**Decision status:** ✅ Final - Red line

---

## 📋 Non-Goal Review Process

### Adding to Non-Goals

1. Feature request identified
2. Evaluate against design pillars
3. Assess scope/resource impact
4. Team discussion
5. If rejected: Add to Non-Goals with rationale
6. Communicate to team

### Reconsidering Non-Goals

Non-goals can be reconsidered when:
- Market conditions change significantly
- Post-launch data suggests opportunity
- Technical constraints are resolved
- Resources become available
- Community demand is overwhelming AND aligned with vision

**Review frequency:** Quarterly

---

## ⚖️ Trade-Off Principles

When facing choices, we prioritize:

| Priority          | Over          | Rationale                       |
| :---------------- | :------------ | :------------------------------ |
| Core loop quality | More features | Fun first, breadth later        |
| Mobile experience | PC parity     | Mobile-first philosophy         |
| Player fairness   | Revenue       | Trust is our currency           |
| Launch quality    | Launch date   | Better to delay than fail       |
| Team health       | Crunch        | Sustainable pace wins long-term |

---

## 🗂️ Summary Table

| Non-Goal               | Category     | Status     |
| :--------------------- | :----------- | :--------- |
| Battle Royale mode     | Gameplay     | ✅ Final    |
| MMO features           | Gameplay     | ✅ Final    |
| Esport infrastructure  | Gameplay     | 🟡 Deferred |
| Ultra-realism          | Gameplay     | ✅ Final    |
| Vehicles               | Gameplay     | 🟡 Deferred |
| Base building          | Gameplay     | ✅ Final    |
| Pay-to-win             | Monetization | ✅ Red Line |
| Loot boxes             | Monetization | ✅ Final    |
| Energy systems         | Monetization | ✅ Final    |
| Forced ads             | Monetization | ✅ Final    |
| Ancient device support | Technical    | ✅ Final    |
| Offline mode           | Technical    | ✅ Final    |
| Console launch         | Technical    | 🟡 Deferred |
| IP crossovers          | Content      | 🟡 Deferred |
| User-generated content | Content      | ✅ Final    |
| Extensive voice acting | Content      | ✅ Final    |
| Social media features  | Social       | ✅ Final    |
| Real-money trading     | Social       | ✅ Red Line |



