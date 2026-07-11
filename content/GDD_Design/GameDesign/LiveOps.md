---
title: "Live Operations & Events"
type: docs
---

## Overview

Live Ops keeps the game fresh after launch through seasons, events, featured modes, balance updates, battle pass content, faction wars, and community beats.

Live Ops should make the world feel active without making the base game feel incomplete. A returning player should see new reasons to play, but a new player should still understand the core raid loop without studying a calendar. Seasonal content is a layer on top of extraction, not a replacement for it.

The healthiest live schedule alternates intensity. Quiet weeks support routine play and economy stability. Event weeks create spikes of attention. Patch weeks restore trust by showing that balance, readability, and player feedback are being acted on.

## Cadence

Cadence should be predictable enough for players to plan around and flexible enough for designers to react to live data. The game should not depend on constant novelty to remain fun; live content should refresh goals, routes, rewards, and social conversation.

| Cadence | Content | Purpose |
| :--- | :--- | :--- |
| Weekly | Rotating quests, small modifiers, featured shop refresh | Habit and variety |
| Monthly | Balance patch, event beat, small content drop | Meta health |
| Seasonal | Battle pass, theme, ranked reset, major event | Long-term return |
| Yearly | Major map, feature, or expansion | Reposition and re-engage |

## LiveOps System Model

LiveOps is the operating layer that schedules temporary goals without weakening the core raid loop. Every live beat should name its time window, player action, reward implication, communication surface, and end behavior before it ships.

| Entity | Definition | UI / Design Requirement |
| :--- | :--- | :--- |
| `Season` | A multi-week content and progression period | Shows theme, dates, battle pass, ranked reset, major events, and recap/archive state |
| `Event` | A limited-time objective, mode, modifier, collection, or community beat | Shows rules, expiry, objective progress, reward ladder, and play route |
| `FeaturedMode` | Temporarily promoted mode or rule variant | Shows exact modifier, risk, eligibility, and whether ranked/economy rules differ |
| `Objective` | Player or community task feeding event/progression | Shows count, source, progress, reward, tracking, and reset/expiry |
| `RewardTrack` | Ordered reward ladder for event, season, battle pass, or faction war | Shows free/premium/event distinction, claim states, and reward destinations |
| `EventCurrency` | Seasonal currency earned and spent during an event | Shows cap, expiry, conversion, and store destination |
| `PatchBeat` | Balance/content/update communication unit | Shows affected systems, reason, player impact, and deep links |
| `CompensationGrant` | Targeted grant for incident recovery | Shows reason, eligibility window, claim destination, and support reference |
| `SeasonReset` | End-of-season transition for rank, event, battle pass, and rewards | Shows retained, reset, archived, converted, and claim-grace rules |

## Season Flow

Each season needs a readable arc: announcement, launch, mastery, disruption, final push, and recap. Players should know what is new, what is temporary, what they can still complete, and what happens when the season ends.

| Phase | Timing | Player Message | UI Destination | Reward / Backend State |
| :--- | :--- | :--- | :--- | :--- |
| Pre-season reveal | Before launch | Theme, dates, major rules, rewards preview | News, Season Summary preview | No progression; wish-list/preview only |
| Season launch | Week 1 | New goals are live | Battle Pass, Event Hub, Ranked Overview | Battle pass active, ranked reset applied, launch tasks active |
| Early progression | Weeks 1-3 | Learn the season loop | Daily/Weekly Tasks, Quest Board | Normal earn rates, onboarding/catch-up off or light |
| Mid-season event | Middle weeks | New disruption and renewed goals | Event Hub, News, Map/Mode deep links | Event currency/reward ladder active |
| Balance patch | After live data review | What changed and why | Patch Notes, known issues, affected screens | Economy/meta values updated with migration notes if needed |
| Final push | Last weeks | What can still be completed | Battle Pass, Event Hub, Reward Inbox | Claim reminders, catch-up missions, expiry labels promoted |
| End grace period | After season end | Claim remaining earned rewards | Reward Inbox, Season Summary | Progression disabled; earned claims/conversions remain |
| Recap/archive | End of grace | What was achieved and retained | Season Summary archive | Final grants delivered; archive becomes read-only |

## Event Types

Events should change player behavior in a targeted way. A boss hunt pulls squads into a hotspot. A faction war changes objective priority. A double XP weekend changes progression pacing. If an event does not create a different decision inside the raid, it is probably just a reward multiplier.

| Event | Duration | Objective Pattern | Reward Pattern | Risk / Expiry Rule |
| :--- | :--- | :--- | :--- | :--- |
| Double XP / Credits | Weekend | Play normal raids with boosted eligible sources | XP or credits only | Must not become best way to print wealth; exact boost window shown |
| Limited-Time Mode | 1-2 weeks | Queue into explicit modified rules | Cosmetics, event currency, titles | Opt-in unless modifier is safe for new players |
| Faction Wars | 2-4 weeks | Choose faction, complete personal/clan/community objectives | Banners, titles, faction cosmetics | Winning faction affects presentation, not permanent combat power |
| Boss Hunt | 1-2 weeks | Push into hotspot, defeat boss, extract proof/reward | Unique cosmetics, trophies, event currency | Boss rewards deterministic or clearly tabled; extraction risk visible |
| Collection Event | 2 weeks | Earn/spend event currency toward collection completion | Themed cosmetics and collection reward | Collection progress, owned count, and end grace are explicit |
| Ranked Event | 1-2 weeks | Compete under announced scoring/rule window | Titles, badges, cosmetic frames | Ranked integrity rules published before event starts |
| Community Challenge | 1-3 weeks | Contribute global objectives through normal play | Account-wide grants, banners, event story | Personal contribution and final grant policy visible |

## Featured Mode Rules

| Mode | Modifier | Risk |
| :--- | :--- | :--- |
| Night Ops | Low visibility, stronger audio play | Medium |
| Extraction Rush | Shorter timer, faster extracts | High |
| Hardcore | Reduced HUD, stricter loss rules | Very high |
| Solo Showdown | Solo-only matchmaking | Medium |
| Chaos Mode | Increased events and AI pressure | High |

## Faction Wars

Faction wars are community stories. They should let solo players contribute meaningfully while giving clans a reason to coordinate. The winning faction can change presentation, banners, or world state, but should not grant permanent combat superiority.

| Contribution | Feeds Into | Reward / Outcome |
| :--- | :--- | :--- |
| Player chooses event faction | Faction alignment | Determines event identity and reward track |
| Player completes faction objectives | Personal score | Unlocks personal event rewards |
| Clan members complete objectives | Clan contribution | Moves clan leaderboard position |
| Total faction activity | Faction war outcome | Determines winning faction presentation |
| Event ends | Recap and reward grant | Delivers personal, clan, and faction rewards |

## Live Ops Guardrails

Guardrails protect trust. Players are more willing to engage with temporary content when they believe the event will not invalidate their work, break ranked fairness, or flood the economy with rewards that make normal raids feel pointless.

| Guardrail | Rule |
| :--- | :--- |
| No event-only power | Event rewards cannot create permanent combat advantage |
| Avoid burnout | Weekly goals must be achievable without unhealthy playtime |
| Maintain economy health | Event rewards must respect item supply and currency sinks |
| Protect ranked integrity | Ranked rule changes must be announced and measurable |
| Keep content readable | Event modifiers must not break mobile clarity |

## Event Reward And Currency Rules

| Rule | Requirement |
| :--- | :--- |
| Event currency cap | If currency can be earned repeatedly, show cap, reset, and whether overflow is lost, blocked, or converted |
| Conversion policy | Event currency expiry must show exact conversion or deletion rule before the event ends |
| Claim grace | Earned but unclaimed rewards should move to inbox or grace period, not silently disappear |
| Deterministic clarity | Purchasable or claimable event rewards must show exact contents; no paid RNG |
| No event-only permanent power | Event rewards can change identity, story, cosmetics, or temporary opt-in rules, not permanent combat superiority |
| Store split | Event progress/rewards live in LiveOps; event purchases and checkout live in Commerce |
| Ranked protection | Ranked events must preserve matchmaking, input, exploit, and eligibility rules |

## Patch / Communication Rules

| Communication Type | Requirement |
| :--- | :--- |
| Balance patch | State affected systems, reason, player impact, and whether loadouts/economy values changed |
| Economy adjustment | Explain why values changed and whether existing player inventory is affected |
| Event announcement | Show start/end dates, rules, rewards, restrictions, and playable route |
| Known issue | Include severity, affected platforms, workaround, and next update expectation |
| Compensation | Show reason, eligibility window, grant contents, claim route, and support reference |
| Mandatory update | Use system modal only for version/security blockers; otherwise use News/Patch Notes |

## LiveOps QA Checklist

- [ ] Season reveal, launch, final push, end grace, recap, and archive states are defined.
- [ ] Event end behavior covers objectives, unclaimed rewards, event currency, store access, and archive copy.
- [ ] Reward claims route through Battle Pass, Event Hub, or Reward Inbox with no silent disappearance.
- [ ] Expired objectives explain whether progress was lost, converted, or moved to inbox.
- [ ] Ranked reset and ranked event rules are visible before queue.
- [ ] Compensation grants are targeted, auditable, and duplicate-safe.
- [ ] Offline/cached news states do not show stale playable CTAs.
- [ ] Event modifiers do not break accessibility, mobile readability, or new-player comprehension.
- [ ] Economy-affecting events have caps, sinks, or conversion policies.
- [ ] Commerce purchase routes are linked but not duplicated in LiveOps specs.

## Event Design Examples

A Night Ops event should change route reading, audio value, and extraction tension, not simply darken the screen. The event needs stronger silhouettes, clear accessibility fallbacks, and rewards that fit the theme.

A Faction War should give solo players personal progress while letting clans contribute to a larger public result. The result can change banners, recap presentation, and world flavor without granting permanent combat advantages.

A Boss Hunt should create a hotspot with readable danger. Players should know why squads are converging, what the boss rewards are, and how extraction becomes harder after the objective is completed.

## Live Ops Failure Cases

- If weekly goals require unhealthy hours, reduce objective counts or add alternate paths.
- If event currency floods the economy, add capped sinks or conversion rules.
- If modifiers confuse new players, restrict them to opt-in modes or improve rule cards.
- If ranked changes mid-season, communicate timing, reason, and expected impact.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Battle pass progression | [Progression](progression/index.html) |
| Economy rewards | [Economy](economy/index.html) |
| Featured modes | [Game Modes](gamemodes/index.html) |
| Ranked seasons | [Ranked Mode](rankedmode/index.html) |
| Clan competition | [Clan System](clansystem/index.html) |
