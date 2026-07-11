---
title: AI & Enemy Design
linkTitle: AI
type: docs
weight: 1
---


###  System Overview

The AI in **Extraction Shooter** is designed not just as cannon fodder, but as a core pillar of the extraction gameplay loop. AI enemies serve as **pacing mechanisms**, **loot guardians**, and **sound traps** that drive player-to-player interaction.

The system is built on two main components:

1. **Individual Behavior:** How a single unit thinks, fights, and reacts.
2. **Faction Ecology:** How groups of AI interact with the world and each other.

{{< cards cols="2" >}}
{{< card link="enemybehavior/index.html" title="Enemy Behaviors" icon="chip" subtitle="Archetypes, states, combat tactics, and difficulty scaling." >}}
{{< card link="factionbehaviors/index.html" title="Faction Ecology" icon="users" subtitle="Relationships between Scavengers, Syndicate, UN-PK, and Wildlife." >}}
{{< /cards >}}

***

###  Design Pillars

#### 1. Challenge without Cheating

AI should be difficult because of **tactics and numbers**, not because they have aimbot or inflated health pools.

* **Good:** AI using cover, flanking, and suppressing fire.
* **Bad:** AI spinning 180° instantly or tracking players through walls.

#### 2. Information Warfare

AI acts as a **broadcast system** for the match.

* **Gunfire:** Tells players where a fight is happening.
* **Barking/Callouts:** Reveals the AI's state (Relaxed vs. Combat) and potentially the player's location to reliable third-parties.

#### 3. Predictability vs. Threat

Players should be able to learn AI patterns to master PvE encounters, but mistakes should still be punished.

* **Tier 1 AI (Scavengers):** chaotic, loud, inaccurate.
* **Tier 3 AI (Elites):** disciplined, quiet, lethal.

***

###  Ecology Snapshot

The world is populated by distinct factions with their own goals and relationships.

| Faction        | Role              | Threat Level | Key Trait                            |
| -------------- | ----------------- | ------------ | ------------------------------------ |
| **Scavengers** | The "Rats"        | Low          | swarm mechanics, loud, unpredictable |
| **Syndicate**  | The "Elites"      | High         | tactical squads, use advanced gear   |
| **UN-PK**      | The "Law"         | Extreme      | defensive, warn before shooting      |
| **Wildlife**   | The "Environment" | Variable     | ambush predators, fear fire          |

> > > [**View Full Faction Matrix & Behaviors**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/AI/FactionBehaviors/README.md)

***

###  AI Archetypes

Different enemies require different tactical approaches.

* **Fodder (Scavengers):** Rush them or pick them off. They rely on numbers.
* **Soldiers (Guards):** require use of cover. They will suppress you.
* **Specialists (Snipers/Medics):** Priority targets. Take them out first.
* **Bosses (The Warden):** Raid objectives. Requires squad coordination and heavy ordnance.

> > > [**View Detailed Enemy Stats & Logic**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/AI/EnemyBehavior/README.md)
