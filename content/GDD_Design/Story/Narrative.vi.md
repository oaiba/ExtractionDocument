---
title: "Narrative Design Bible"
type: docs
weight: 1
---

### Narrative Philosophy

This game tells its story thông qua the **world itself**, not thông qua the người chơi. The narrative exists whether hoặc not anyone is watching — the người chơi is an intruder in a world that continued mà không them.

#### Storytelling Hierarchy

| Priority | Channel                   | người chơi Effort                       | Example                                                     |
| :------: | ------------------------- | ----------------------------------- | ----------------------------------------------------------- |
|     1    | **Environmental**         | Zero — người chơi sees it naturally     | Skeleton clutching a family photo near an exit door         |
|     2    | **cơ chế**            | Zero — gameplay communicates it     | The weight of looted gear tạo anxiety about extraction |
|     3    | **Audio Logs**            | Low — interact với object          | A panicked recording from a worker trong khi The Collapse      |
|     4    | **Quest NPC Dialogue**    | Medium — accept và complete quests | Viktor Koval explaining why a supply route matters          |
|     5    | **Collectible Documents** | High — seek và find                | A classified Nexus Corp memo hidden behind a locked door    |
|     6    | **Codex Entries**         | High — menu reading                 | Compiled lore entries unlocked thông qua gameplay             |

**The rule**: A người chơi who never reads a tài liệu hoặc listens to a log should still _feel_ the story thông qua the environment và cơ chế. A người chơi who seeks lore nên được rewarded với depth.

#### What This Game Is NOT

* **Not a cinematic trải nghiệm**: No pre-rendered cutscenes. No camera-stealing moments. The người chơi is always in control.
* **Not a dialogue RPG**: NPC interactions are brief và purposeful. No branching dialogue trees.
* **Not a linear narrative**: The story unfolds thông qua exploration, not progression gates. người chơi discover lore in any order.

> For chi tiết environmental storytelling guidelines và art direction, Xem [Environmental Narrative](https://github.com/oaiba/ExtractionDocument/blob/main/content/World/EnvironmentalNarrative/README.md) và [Guidelines](https://github.com/oaiba/ExtractionDocument/blob/main/content/World/EnvironmentalNarrative_Guidelines/README.md). For individual operator backstories và nhân vật profiles, Xem [nhân vật & Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/nhân vật/README.md).

***

### Thematic Pillars

Every piece of narrative content must reinforce at least one of these cốt lõi themes:

#### 1. Trust và Betrayal

The post-Collapse world runs on trust — nhưng trust is currency that can be counterfeited.

| Expression            | Example                                                                    |
| --------------------- | -------------------------------------------------------------------------- |
| Faction relationships | The Broker's identity is unknown — nhưng everyone depends on them            |
| Squad gameplay        | Your teammate could take your loot nếu you die                              |
| Quest design          | Some NPCs lie about quest objectives for their own benefit                 |
| Environmental         | Graffiti cảnh báo "DON'T TRUST THE PEACEKEEPERS" near a civilian mass grave |

#### 2. Survival Ethics

What are you willing to do to survive? Where is the line?

| Expression          | Example                                                                  |
| ------------------- | ------------------------------------------------------------------------ |
| Faction philosophy  | Salvage Corps values fair work; Underground values survival at any giá |
| Quest moral choices | Save a civilian vs. loot their supplies — both options have consequences |
| Environmental       | Medical triage ghi chú showing who was saved và who was left to die       |
| người chơi behavior     | The extraction cơ chế itself — you choose khi "enough is enough"      |

#### 3. Corporate Sin

Nexus Corporation's greed created the Collapse. Their sins echo thông qua every ruined building.

| Expression         | Example                                                                |
| ------------------ | ---------------------------------------------------------------------- |
| Project Prometheus | Human experimentation for profit — the AI bosses are their victims     |
| Environmental      | Corporate memos discussing chi phí-benefit of containment vs. cover-up    |
| Quest revelations  | Discovering that The Collapse was preventable nếu Nexus had acted early |
| World design       | Pristine executive suites next to crumbling worker dormitories         |

#### 4. Identity in Ruins

Who are you khi civilization is gone? Do your old credentials matter?

| Expression           | Example                                                                      |
| -------------------- | ---------------------------------------------------------------------------- |
| Operator backstories | Each operator is defined by who they were _before_ vs. who they are _now_    |
| Faction identity     | Peacekeepers cling to old-world authority; Underground builds new rules      |
| người chơi identity      | The loadout you choose reflects your identity — rat, chad, healer, lone wolf |
| Environmental        | Personal effects showing someone's past life (diplomas, uniforms, toys)      |

***

### Tone Guide

#### General Tone

The narrative tone is **grim nhưng not nihilistic**. The world is broken, nhưng people are still trying. Hope exists, nhưng it costs something.

| Tone Axis                 | Where We Sit                | Reference                                        |
| ------------------------- | --------------------------- | ------------------------------------------------ |
| Hopeful ← → Bleak         | 70% bleak, 30% hope         | _The Road_ (McCarthy) meets _Metro 2033_         |
| Serious ← → Humorous      | 85% serious, 15% dark humor | Gallows humor from soldiers và scavengers       |
| Realistic ← → Fantastical | 90% grounded, 10% sci-fi    | Near-future tech, no magic, minimal supernatural |
| Personal ← → Epic         | 60% personal, 40% epic      | Personal stories against an epic backdrop        |

#### Tone by Context

| Context                     | Tone                                  | Example                                                                                 |
| --------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------- |
| Audio Logs (Workers)        | Scared, confused, human               | "I just want to go home. My daughter's birthday is tomorrow."                           |
| Audio Logs (Military)       | Terse, procedural, cracking           | "All units fall back to Rally Point Bravo. That is an order. ...Please."                |
| Audio Logs (Corporate)      | Cold, calculated, eventually panicked | "Quarterly projections remain on target despite containment issues."                    |
| NPC Dialogue (Salvage)      | Practical, fatherly, tired            | "You look rough, kid. Grab a coffee. Then I need you to grab something else."           |
| NPC Dialogue (Tech)         | Precise, guarded, intellectual        | "The data is incomplete. I need someone I can... rely on. Are you that person?"         |
| NPC Dialogue (Underground)  | Cryptic, transactional, darkly funny  | "I know a guy who knows a guy. You don't want to know the guy."                         |
| NPC Dialogue (Peacekeepers) | Authoritative, weary, principled      | "I've seen too many good people die following bad orders. My orders are good."          |
| Item descriptions           | Factual + one flavor sentence         | "Standard 7.62mm FMJ. Cheap, reliable, và responsible for more deaths than any virus." |
| loading màn hình tips         | In-nhân vật, faction-attributed      | "The Broker says: 'Information is free. Accurate information costs extra.'"             |

***

### Narrative Pacing Framework

#### Per-Raid cảm xúc Arc

Every raid session should follow an implicit cảm xúc narrative:

```
Entry (Dread)
  "What's waiting for me in there?"
    |
Early Raid (Curiosity + Caution)
  "What's that sound? What's in this room?"
    |
Mid-Raid (Tension + Greed)
  "I found something good. Should I push further?"
    |
Late Raid (Urgency + Fear)
  "Timer's running. I need to get out NOW."
    |
Extraction (Relief or Devastation)
  "I made it!" or "I lost everything."
    |
Post-Raid (Reflection + Planning)
  "What did I learn? What will I do differently?"
```

#### Per-Season Narrative Arc

| Season            | Narrative Focus            | cảm xúc Arc                | người chơi Knowledge                                 |
| ----------------- | -------------------------- | ---------------------------- | ------------------------------------------------ |
| Season 1 (Launch) | Introduction to the world  | Curiosity → Unease           | "Something terrible happened here"               |
| Season 2          | Faction conflicts escalate | Loyalty → Doubt              | "These factions are more complex than they seem" |
| Season 3          | Collapse truth revealed    | Shock → Anger                | "Nexus Corp could have stopped this"             |
| Season 4          | The Broker's identity      | Betrayal → Resolution        | "Nothing in this world is what it appears"       |
| Year 2+           | người chơi agency              | Empowerment → Responsibility | "My choices shape what happens next"             |

#### Lore Progression Gating

Not all lore nên được available immediately. Gate by these methods:

| Gating Method                    | What It Gates                            | Design mục đích                           |
| -------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Map access (new maps per season) | Regional history, new faction NPCs       | Rewards long-term engagement             |
| người chơi level                     | Main story quest chapters                | Prevents spoilers, paces revelations     |
| Faction reputation               | Faction-cụ thể dialogue và quest lore | Rewards faction loyalty                  |
| Exploration (hidden areas)       | Easter eggs, deep lore, "true history"   | Rewards thorough người chơi                 |
| Seasonal events                  | Limited-thời gian narrative content           | tạo urgency và community discussion |

***

### Dialogue Writing Guidelines

#### Structure for Quest NPCs

Every NPC interaction follows this format. Total dialogue nên được **under 30 seconds of spoken audio**:

```
1. GREETING (1-2 sentences)
   - Acknowledge the player. Reference recent events if applicable.
   - "You're back. Good. I was starting to think Sector 7 swallowed you whole."

2. CONTEXT (2-3 sentences)
   - Why does this quest matter? What's at stake?
   - "We've got a supply convoy stuck at the loading docks. Scavs hit them
     at dawn. Three of my people are still in there."

3. OBJECTIVE (1-2 sentences)
   - Clear, unambiguous instruction.
   - "Get to the docks, clear the hostiles, and signal for pickup.
     The convoy has to move before nightfall."

4. REWARD MENTION (1 sentence)
   - What the player gets. Always mention it.
   - "Do this, and I'll open our armory to you. Fair trade."

5. SEND-OFF (1 sentence)
   - Character-specific farewell.
   - Viktor: "Go. And try not to die — good workers are hard to find."
   - The Broker: "You have 40 minutes. After that, this conversation
     never happened."
```

#### Voice Line Categories

| Category              |   Length   | Trigger              | Priority                        |
| --------------------- | :--------: | -------------------- | ------------------------------- |
| Combat Callouts       |  1-3 words | Gameplay events      | Highest — phải được heard clearly |
| Tactical Information  | 1 sentence | Context-cụ thể     | High — gameplay-relevant        |
| nhân vật Flavor      | 1 sentence | Idle, entering areas | Medium — atmosphere             |
| Pain/Injury Reactions |  1-2 words | Taking damage        | High — feedback                 |
| Extraction Lines      | 1 sentence | Near extraction zone | Medium — cảm xúc payoff       |

#### Writing Style Rules

**DO:**

* cách dùng active voice ("rõ the hostiles" not "The hostiles nên được cleared")
* Keep sentences under 15 words for spoken dialogue
* Give each NPC a verbal tic hoặc speech pattern (Viktor's metaphors, The Broker's redactions)
* Include tactical information khi possible ("They've got elevated positions on the east side")
* Show emotion thông qua word choice, not stage directions

**DON'T:**

* cách dùng real-world brand names, religions, hoặc political parties
* Write monologues longer than 4 sentences
* Include meta-game references ("Press E to interact")
* cách dùng slang that dates the writing (no hiện tại-year memes)
* Stereotype accents hoặc cultures

***

### Narrative Content Production Pipeline

#### Per-Season Deliverables

| Content Type                  |     Season 1     |    Season 2    |    Season 3    | Per Season sau |
| ----------------------------- | :--------------: | :------------: | :------------: | :--------------: |
| Main Story Quests             |         5        |        5       |        5       |        3-5       |
| Faction Quests (per faction)  |         5        |        5       |        5       |        3-5       |
| Audio Logs (per map)          |       15-20      |      12-15     |      10-12     |       8-10       |
| Collectible Documents         |        10        |       10       |       10       |         8        |
| NPC Voice Lines (per NPC)     |       30-50      |      20-30     |      20-30     |       15-20      |
| loading màn hình Tips           |        20        |       15       |       15       |        10        |
| Item Descriptions (new items) | All launch items | New items only | New items only |  New items only  |

#### Review Process

1. **Writer drafts** → 2. **Narrative Lead reviews for tone/lore consistency** → 3. **Gameplay Designer validates quest flow** → 4. **Localization review** → 5. **Voice acting recording** → 6. **In-engine integration và QA**
