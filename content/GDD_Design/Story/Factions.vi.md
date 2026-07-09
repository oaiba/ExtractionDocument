---
title: "Factions — Detailed Breakdown"
type: docs
weight: 3
---

## Faction hệ thống Overview

### Role of Factions

Factions are **NOT** playable sides. They function as:
- **Quest Givers**: Provide missions và objectives aligned với their ideology
- **Vendors**: Sell exclusive items locked behind reputation tiers
- **Lore Sources**: Expand world building thông qua NPC dialogue và quest narratives
- **Reputation hệ thống**: Unlock rewards thông qua sustained loyalty
- **Territory Controllers**: Influence which map zones are safe, contested, hoặc hostile

### Faction Design Philosophy

Every faction must satisfy three design yêu cầu:

1. **Understandable Motivation**: A new người chơi should understand what a faction wants within 30 seconds of meeting their first NPC
2. **Moral mơ hồ**: No faction is purely good hoặc evil. Each has justifiable reasoning và uncomfortable compromises
3. **cơ chế Identity**: Each faction's quests, rewards, và playstyle must feel distinct from the others

---

## Faction Ideology Spectrum

<!-- REF_IMAGE: Faction ideology chart — 2D grid với Order/Chaos on X-axis và Idealism/Pragmatism on Y-axis, với each faction plotted as a colored circle -->

```
            IDEALISM
               |
               |  Peacekeepers
               |  (Order + Idealism)
               |
 ORDER --------+-------- CHAOS
               |
   Salvage     |    Underground
   Corps       |    Network
   (Order +    |    (Chaos +
    Pragmatism)|     Pragmatism)
               |
            PRAGMATISM

   Tech Syndicate sits center-left:
   (Slight Order + Slight Idealism)
   — They believe in systems, but only systems they control
```

---

## Inter-Faction Relationship matrix

### hiện tại Status (Season 1)

```
                 SALVAGE   TECH    UNDERGROUND   PEACEKEEPERS
SALVAGE CORPS      --       ○          ○             ●
TECH SYNDICATE     ○        --         ●             X
UNDERGROUND        ○        ●          --            X
PEACEKEEPERS       ●        X          X             --

Legend:
-- = Self
●  = Friendly (Trade, non-aggression)
○  = Neutral (Cautious cooperation)
X  = Hostile (Active conflict)
```

### Relationship chi tiết

| Faction A | Faction B | Status | Reason | Tension Point |
| :-------- | :-------- | :----- | :----- | :------------ |
| Salvage | Tech | Neutral | Trade tech components for raw materials | Tech wants exclusive access to Sector 7 workshops |
| Salvage | Underground | Neutral | Occasional supply deals, both pragmatic | Underground tries to recruit Salvage workers for smuggling |
| Salvage | Peacekeepers | Friendly | Both giá trị stability và order | Peacekeepers pressure Salvage to stop trading với Underground |
| Tech | Underground | Friendly | Information exchange, mutual distrust of authority | The Broker may know Director Park's secrets about Prometheus |
| Tech | Peacekeepers | Hostile | Peacekeepers want to seize Nexus data; Tech guards it | Peacekeepers view un-regulated tech hoarding as dangerous |
| Underground | Peacekeepers | Hostile | Criminal enterprise vs. law enforcement | Ideological opposition — order vs. freedom |

### Dynamic Relationship Events (Per Season)

Faction relationships are not static. Scheduled narrative events shift the balance:

| Season | Event | Relationship Shift | người chơi Impact |
| :----- | :---- | :----------------- | :------------ |
| Season 1 | Stable introduction | Baseline matrix above | người chơi learn each faction's identity |
| Season 2 | "Resource War" — Tech và Salvage clash over a discovered server farm in Sector 7 | Tech ↔ Salvage: Neutral → Hostile | người chơi must choose a side. Losing faction's vendor prices increase 20% |
| Season 2 | "Peacekeepers Overreach" — Commander Vance authorizes raids on Underground safehouses | Underground ↔ Peacekeepers: Hostile → War | Underground quests become sabotage missions. Peacekeepers offer bounties on Underground agents |
| Season 3 | "Prometheus Revelation" — Director Park's role in Project Prometheus is exposed | Tech Syndicate internal split. Some NPCs defect to other factions | Tech reputation partially resets. New NPC questlines appear |
| Season 3 | "Unlikely Alliance" — External threat forces temporary cooperation | All factions: +1 relationship tier for one season | Cooperative extraction events, shared vendors, unique joint quests |

---

## Salvage Corps

### Identity

| Attribute | chi tiết |
| :-------- | :----- |
| **Motto** | "Honest Work in Lawless Lands" |
| **Colors** | Orange và Gray |
| **Symbol** | Crossed wrenches over a gear |
| **Leader** | "Foreman" Viktor Koval |
| **Base** | Converted factory complex (off-map safe zone) |
| **Territory** | Workers' quarters, warehouse districts, industrial workshops |
| **Marking Style** | Orange spray-painted gear symbols on walls. Functional barricades made from repurposed machinery |

### Leadership Profile

**Viktor Koval — "The Foreman"**

| Attribute | chi tiết |
| :-------- | :----- |
| Age | 52 |
| Origin | Ukrainian factory supervisor |
| Pre-Collapse | Plant manager overseeing 200 workers in the NAIC |
| The Collapse | Organized surviving workers into self-sufficient crews. Refused to abandon the factory |
| Philosophy | "Build, don't destroy" |
| Voice | Gruff, fatherly, practical. Heavy Eastern European accent |
| Hidden Agenda | Wants to restore the NAIC's infrastructure to prove that civilization can be rebuilt — nhưng fears that Nexus tech hidden in the factories is too dangerous to reactivate |

**Characteristic Voice Lines:**
- *"You look like you haven't eaten in days. Here — you can't work on an empty stomach."*
- *"Every bolt you bring back is one step closer to putting this world back together."*
- *"I don't trust anyone who doesn't know how to cách dùng a wrench."*

### Faction Structure

```
         [Foreman Viktor Koval]
                  |
     +------------+------------+
     |            |            |
[Chief Engineer] [Quartermaster] [Recruiter]
     Yuri         Mama Rosa      "Wrench" Lee
     |            |            |
[Work Crews]  [Supply Team] [New Contractors]
```

### chính NPCs

| Name | Role | Quest Type | Location | Hidden Agenda |
| :--- | :--- | :--------- | :------- | :------------ |
| Viktor Koval | Leader | Main story, faction philosophy | Safe Zone HQ | Hiding knowledge of active Nexus hệ thống in the factory basement |
| Yuri | Chief Engineer | Repair và technical missions | Field deployments | Secretly studying Prometheus tech. Fascinated, not afraid |
| Mama Rosa | Quartermaster | Supply runs, resource gathering | Safe Zone market | Running a small charity for orphaned children. Uses Salvage funds |
| "Wrench" Lee | Recruiter | Introduction quests, tutorials | Various | Former Underground member. Reformed, nhưng old contacts still call |

### Reputation hệ thống

| Level | Title | Rep Required | Benefits | Unlock |
| :---: | :---- | :----------: | :------- | :----- |
| 1 | Newcomer | 0 | Basic quests, standard vendor prices | Starting |
| 2 | Worker | 1,000 | 5% vendor discount, expanded quest pool | Complete 3 Salvage quests |
| 3 | Foreman's Pick | 3,000 | Exclusive gear unlocks (Worker's Backpack, Heavy-Duty Tool) | Complete Yuri's repair chain |
| 4 | Trusted | 7,000 | High-giá trị quests, 15% discount, priority supply access | Complete main Salvage storyline |
| 5 | Veteran | 15,000 | Unique cosmetics (Orange/Gray theme), Salvage Legend title | 30+ completed Salvage quests |

### Unique Reputation Items

| Item | Level | Type | Stats | Lore |
| :--- | :---: | :--- | :---- | :--- |
| Worker's Backpack | 2 | Storage | +2 inventory slots | Reinforced canvas với Salvage Corps patch. "Built to last." |
| Heavy-Duty Tool | 3 | Utility | Looting speed +15% | Modified pry bar với integrated LED. Yuri's personal design |
| Foreman's Vest | 4 | giáp | +15% carry weight capacity | Kevlar-lined work vest. "Viktor's personal endorsement" |
| Salvage Legend Skin | 5 | cosmetic | Orange/Gray operator theme | Full hardhat-và-coveralls aesthetic với faction patches |

---

## Tech Syndicate

### Identity

| Attribute | chi tiết |
| :-------- | :----- |
| **Motto** | "Knowledge is the Ultimate Currency" |
| **Colors** | Cyan và Black |
| **Symbol** | Circuit pattern forming an eye |
| **Leader** | "Director" Seo-Yun Park |
| **Base** | Hidden server farm (location unknown — encrypted coordinates) |
| **Territory** | Tech labs, server rooms, communications infrastructure |
| **Marking Style** | Circuit-pattern stencils in UV-reactive paint (hiển thị rõ only under blacklight/NVG). Digital locks on controlled doors |

### Leadership Profile

**Seo-Yun Park — "The Director"**

| Attribute | chi tiết |
| :-------- | :----- |
| Age | 41 |
| Origin | Korean tech executive, former Nexus Corp Chief Data Officer |
| Pre-Collapse | Led Nexus's data infrastructure division. Had access to Prometheus files |
| The Collapse | Stole classified Prometheus data và defected. Went underground |
| Philosophy | "Information sets you free" |
| Voice | Cold, calculated, với occasional cracks of genuine warmth |
| Hidden Agenda | Guilt about Prometheus. She knew about the risks và said nothing until it was too late. Founding the Tech Syndicate is her attempt at redemption — nhưng she cannot bring herself to reveal her full role |

**Characteristic Voice Lines:**
- *"Data doesn't lie. People do. That's why I prefer data."*
- *"You retrieved the drive? Good. Don't read it. Some knowledge costs more than you can afford."*
- *"Trust is a vulnerability I can't afford. nhưng... competence, I can reward."*

### Faction Structure

```
          [Director Seo-Yun Park]
                    |
       +------------+------------+
       |            |            |
  [Lead Hacker]  [Archivist]  [Field Ops]
    "Zero"       Dr. Huang     "Glitch"
       |            |            |
 [Cyber Team]  [Data Team]  [Operatives]
```

### chính NPCs

| Name | Role | Quest Type | Location | Hidden Agenda |
| :--- | :--- | :--------- | :------- | :------------ |
| Seo-Yun Park | Director | Main story, data recovery | Encrypted comms only | Slowly leaking Prometheus data to người chơi to expose Nexus mà không exposing herself |
| "Zero" | Lead Hacker | Technical intrusion missions | Remote (voice only) | Suspects Park knows more than she reveals. Running parallel investigation |
| Dr. Huang | Archivist | Data recovery, lore quests | Safe Zone terminal | Genuinely believes knowledge nên được free. Friction với Park's secrecy |
| "Glitch" | Field Ops | Reconnaissance, stealth missions | Field | Former military drone operator. Haunted by collateral damage |

### Reputation hệ thống

| Level | Title | Rep Required | Benefits | Unlock |
| :---: | :---- | :----------: | :------- | :----- |
| 1 | Unknown | 0 | Basic access, standard prices | Starting |
| 2 | Registered | 1,500 | Tech item 5% discount, electronic component quests | Complete 3 Tech quests |
| 3 | Trusted Node | 4,000 | Gadget unlocks (Signal Scanner, Crypto Wallet) | Complete Zero's infiltration chain |
| 4 | Inner Circle | 9,000 | Secret quest lines, 15% discount, encrypted intel drops | Complete main Tech storyline |
| 5 | Elite Hacker | 20,000 | Exclusive skins (Cyan/Black theme), Elite Hacker title | 30+ completed Tech quests |

### Unique Reputation Items

| Item | Level | Type | Stats | Lore |
| :--- | :---: | :--- | :---- | :--- |
| Signal Scanner | 2 | Gadget | Reveals nearby địch within 20m for 5 seconds (90s cooldown) | Modified Wi-Fi module repurposed as a motion sensor |
| Crypto Wallet | 3 | Utility | +10% credit gain from all sources | Encrypted digital wallet. "The Syndicate takes a smaller cut" |
| Stealth Module | 4 | Attachment | địch detection range reduced by 15% | Sound-dampening mesh for boots và gear. Glitch's personal design |
| Syndicate Ghost Skin | 5 | cosmetic | Cyan/Black operator theme | Full tactical infiltration suit với circuit-pattern accents |

---

## Underground Network

### Identity

| Attribute | chi tiết |
| :-------- | :----- |
| **Motto** | "Survive Together hoặc Die Alone" |
| **Colors** | Purple và Gold |
| **Symbol** | Clasped hands in shadows |
| **Leader** | "The Broker" (identity unknown) |
| **Base** | Multiple safehouses, never the same location twice |
| **Territory** | Sewers, subway tunnels, hidden rooms behind false walls |
| **Marking Style** | Hand-drawn purple symbols (chalk, easily erased). Dead drops marked với gold paint scratches. Radio frequency codes etched into surfaces |

### Leadership Profile

**"The Broker" — Identity Unknown**

| Attribute | chi tiết |
| :-------- | :----- |
| Age | Unknown (voice analysis suggests 30-50) |
| Origin | Unknown (accent shifts between communications) |
| Pre-Collapse | Unknown |
| The Collapse | Emerged as an information kingpin within months of societal breakdown |
| Philosophy | "Everyone has a giá" |
| Voice | Always distorted. Never seen in person. Communication thông qua intermediaries hoặc encrypted channels |
| Hidden Agenda | [REDACTED — Season 4 reveal]. Theories: surviving Nexus executive, AI that achieved consciousness, collective of information brokers, someone the người chơi knows from the tutorial |

**Characteristic Voice Lines:**
- *"I don't deal in trust. I deal in certainty. Do the job, get paid. Simple."*
- *"You're asking questions. Good. The wrong ones, nhưng still — progress."*
- *"This conversation never happened. nhưng the credits in your account? Those are very real."*

### Faction Structure

```
              [The Broker]
                   | (voice only, identity unknown)
                   |
      +------------+------------+
      |            |            |
  [Fixers]    [Smugglers]   [Enforcers]
  Madame X    "Rat King"    "Big Bear"
      |            |            |
 [Informants] [Runners]    [Muscle]
```

### chính NPCs

| Name | Role | Quest Type | Location | Hidden Agenda |
| :--- | :--- | :--------- | :------- | :------------ |
| The Broker | Leader | High-level directives | Voice only — encrypted channel | [Season 4 reveal] |
| Madame X | Fixer | Contract kills, information gathering | Hidden meeting spots (rotate per week) | Building a power base to eventually replace The Broker |
| "Rat King" | Smuggler | Delivery quests, dead drop exchanges | Sewer network | Genuinely cares about the street-level survivors. Uses smuggling to fund refugee camps |
| "Big Bear" | Enforcer | Elimination missions, territory defense | Field — follows the action | Former university professor. Embraced violence reluctantly. Reads philosophy between jobs |

### Reputation hệ thống

| Level | Title | Rep Required | Benefits | Unlock |
| :---: | :---- | :----------: | :------- | :----- |
| 1 | Nobody | 0 | Black market access, inflated prices | Starting |
| 2 | Known Face | 2,000 | Better mua/sell prices (-10%), expanded quest pool | Complete 3 Underground quests |
| 3 | Trusted Runner | 5,000 | Smuggling quest chain, exclusive items | Complete Rat King's delivery chain |
| 4 | Inner Circle | 12,000 | Assassination contracts, 20% giá discount, Broker direct contact | Complete main Underground storyline |
| 5 | Shadow Elite | 25,000 | Legendary items, exclusive cosmetics, Shadow Elite title | 30+ completed Underground quests |

### Unique Reputation Items

| Item | Level | Type | Stats | Lore |
| :--- | :---: | :--- | :---- | :--- |
| Forged ID | 2 | Utility | Access certain restricted areas mà không a chính (single cách dùng per raid) | Professionally crafted. "Don't look too closely" |
| Silencer Kit | 3 | Attachment | Gunfire sound radius reduced by 50% | Custom-machined suppressor components. Rat King's workshop special |
| Broker's Favor | 4 | Consumable | One-thời gian cách dùng: Skip a quest yêu cầu hoặc double a quest reward | A calling card với a frequency. "cách dùng wisely. I don't offer these often." |
| Shadow Wraith Skin | 5 | cosmetic | Purple/Gold operator theme | Full stealth outfit với face wrap và gold accent stitching |

---

## Peacekeepers

### Identity

| Attribute | chi tiết |
| :-------- | :----- |
| **Motto** | "Order From Chaos" |
| **Colors** | Blue và White |
| **Symbol** | Shield với olive branches |
| **Leader** | Commander Helena Vance |
| **Base** | Fortified outpost at map perimeter |
| **Territory** | Checkpoints, patrol routes, safe zone perimeters |
| **Marking Style** | Official-looking blue-và-white signs. Sandbag positions. Radio repeater stations. Professional, military-grade presence |

### Leadership Profile

**Helena Vance — "The Commander"**

| Attribute | chi tiết |
| :-------- | :----- |
| Age | 47 |
| Origin | Former UN Peacekeeper |
| Pre-Collapse | Deployed to conflict zones across three continents. Witnessed the failure of international intervention |
| The Collapse | Tried to maintain order in the NAIC. Saw colleagues killed, civilians abandoned. Refused to give up |
| Philosophy | "Law is all that separates us from animals" |
| Voice | Stern nhưng weary. Authority hardened by exhaustion. Occasional warmth toward those who prove themselves |
| Hidden Agenda | Authorized morally gray operations ("necessary evils") that haunt her. She wants to believe in justice, nhưng survival keeps demanding compromises she can't undo |

**Characteristic Voice Lines:**
- *"I've buried more good people than I care to count. Don't make me add your name to the list."*
- *"Rules exist vì mà không them, the strong simply take from the weak. I won't allow that."*
- *"You did good work today. Don't let it go to your head — there's always tomorrow."*

### Faction Structure

```
         [Commander Helena Vance]
                   |
      +------------+------------+
      |            |            |
  [Captain]    [Sergeant]   [Medical]
  Reyes        "Stone"      Dr. Wells
      |            |            |
[Patrol Units] [Combat Team] [Medics]
```

### chính NPCs

| Name | Role | Quest Type | Location | Hidden Agenda |
| :--- | :--- | :--------- | :------- | :------------ |
| Helena Vance | Commander | Main story, strategic operations | Command Post | Seeking Firebase Delta access to find evidence that could legitimize the Peacekeepers as a governing body |
| Captain Reyes | Patrol Lead | Sweep và secure missions | Field patrols | Former cartel member who found mục đích in the Peacekeepers. Nobody knows his past |
| Sergeant "Stone" | Combat Specialist | Boss elimination, high-giá trị targets | Combat hotspots | Addicted to combat stimulants. Performance is slipping. Hiding it from Vance |
| Dr. Wells | Medical Officer | Rescue missions, medical supply procurement | Medical tent | Searching for a Crimson Flu cure. Willing to work với anyone — including the Tech Syndicate, secretly |

### Reputation hệ thống

| Level | Title | Rep Required | Benefits | Unlock |
| :---: | :---- | :----------: | :------- | :----- |
| 1 | Civilian | 0 | Basic recognition, standard prices | Starting |
| 2 | Auxiliary | 1,200 | Medical item 5% discount, patrol quests | Complete 3 Peacekeeper quests |
| 3 | Deputy | 3,500 | giáp unlocks (Tactical Vest), expanded combat quests | Complete Stone's elimination chain |
| 4 | Officer | 8,000 | Elite quest access, 15% discount, Commander's Radio | Complete main Peacekeeper storyline |
| 5 | Commander's Trust | 18,000 | Legendary gear, exclusive cosmetics, Commander's Trust title | 30+ completed Peacekeeper quests |

### Unique Reputation Items

| Item | Level | Type | Stats | Lore |
| :--- | :---: | :--- | :---- | :--- |
| First Aid Training | 2 | Passive | Healing speed +20% | Field medic certification card from Dr. Wells |
| Tactical Vest | 3 | giáp | +20 giáp rating | Standard-issue Peacekeeper body giáp với blue-white markings |
| Commander's Radio | 4 | Gadget | Call in one squad of Peacekeeper NPCs per raid (3 AI allies, 60s duration) | Emergency transponder. "cách dùng only in dire need." |
| Peacekeeper Elite Skin | 5 | cosmetic | Blue/White operator theme | Full tactical uniform với Commander's insignia |

---

## Negative Reputation Consequences

Working against a faction has real consequences:

| Rep Tier | Threshold | Effect | Recovery |
| :------- | :-------: | :----- | :------- |
| Distrusted | -1,000 | Vendor prices increase by 25%. Some quests become unavailable | Complete 5 positive quests for that faction |
| Hostile | -3,000 | Faction NPCs refuse to trade. Vendor is locked. Patrol NPCs become aggressive on sight | Complete a special "Redemption" quest chain (difficult) |
| địch | -5,000 | Faction sends hit squads into raids (3-5 AI địch hunting the người chơi specifically). Bounty placed on the người chơi (other Người chơi có thể collect) | Nearly impossible. Requires Season wipe hoặc a legendary quest chain |

**How to lose reputation:**
- Killing faction NPCs in-raid (-500 per kill)
- Failing faction quests repeatedly (-200 per failure)
- Completing quests for a hostile faction (-100 per quest)
- Attacking người chơi known to be allied với the faction (-50 per kill, unreliable tracking)

---

## Double-Agent cơ chế

Người chơi có thể work for factions that are hostile to each other simultaneously — nhưng it is risky:

### How It Works

- người chơi maintains separate reputation với each faction
- **No automatic penalty** for having high reputation với opposing factions initially
- At **reputation level 4+ với a faction**, that faction's NPC begins dropping hints: *"I hear you've been talking to the Peacekeepers. Careful who you trust."*
- At **reputation level 5 với a hostile faction**, a **Loyalty Test** quest appears: complete a mission that directly harms the other faction. Declining does not reduce reputation, nhưng the quest disappears permanently

### Risk-Reward

| Scenario | Risk | Reward |
| :------- | :--- | :----- |
| Level 3+ với both Tech và Peacekeepers | Low — no one notices yet | Access to both vendor inventories và quest pools |
| Level 4+ với both | Medium — NPC dialogue hints at suspicion | Unique cross-faction intel quests appear |
| Level 5 với both | High — Loyalty Test demanded by both sides | Attempting to pass both tests unlocks a secret quest line: "The Mediator" |
| failed Loyalty Test | Immediate -2,000 reputation với the testing faction | None — pure failure trạng thái |

---

## Faction Territory Influence

### Map Control

Each map zone has a dominant faction influence. khi a faction controls a zone:

| Control Effect | Description |
| :------------- | :---------- |
| Friendly NPCs | Faction patrol squads appear as non-hostile AI |
| Vendor Access | Faction vendor booth available at certain POIs |
| Quest Markers | Faction-cụ thể quest objectives marked on map |
| Environmental | Faction graffiti/markings, barricade styles, radio frequencies |

### Territory Shifts (Seasonal)

sau Season 2, territory can shift based on community-wide quest completion:

- nếu người chơi collectively complete more Salvage quests than Tech quests in a season, Salvage gains territory in the contested workshops area
- Territory shifts affect vendor locations, patrol routes, và available quest types
- **No territory is permanently owned** — the power balance fluctuates season to season

<!-- REF_IMAGE: NAIC territory map — color-coded zones showing Salvage (orange), Tech (cyan), Underground (purple), Peacekeeper (blue), và contested (gray) areas -->

---

## Faction Comparison Summary

| Aspect | Salvage Corps | Tech Syndicate | Underground Network | Peacekeepers |
| :----- | :------------ | :------------- | :------------------ | :----------- |
| **Focus** | Materials, rebuilding | Data, technology | Contraband, information | Security, order |
| **Playstyle** | Gathering, crafting | Stealth, hacking | Risk/reward, smuggling | Combat, rescue |
| **Morality** | Neutral good | Moral gray | Dark pragmatism | Light gray (compromised ideals) |
| **Difficulty** | Easy (forgiving quests) | Medium (stealth optional) | Hard (high-risk objectives) | Medium (combat-focused) |
| **Best For** | New người chơi, crafters | Solo người chơi, explorers | Veterans, risk-takers | Squad người chơi, fighters |
| **Tone** | Blue-collar, practical | Cyberpunk, secretive | Noir, transactional | Military, weary heroism |
