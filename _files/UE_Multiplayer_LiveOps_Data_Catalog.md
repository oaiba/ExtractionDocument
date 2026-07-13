# Multiplayer LiveOps Data Catalog

## 1. Authority and Naming

This catalog is the domain-level authority for the LiveOps contract pack under `_files/`. It does not replace the architecture document, database migrations, or the executable OpenAPI contract that will be created during backend implementation.

- JSON/API fields use lower camel case.
- PostgreSQL fields use snake_case.
- All timestamps are UTC ISO-8601.
- Published versions are immutable.
- LiveOps never directly edits authoritative player state, wallet balances, item custody, match outcomes, secrets, or executable code.

## 2. Data Classes

| Data class | Authority | Consumer | Client-visible | LiveOps editable |
|---|---|---|---:|---:|
| Client-safe config | Go backend | Unreal Client | Yes | Yes, validated |
| Server-only tuning | Go backend | Backend/DS | No | Restricted |
| Admin operational state | Admin services | Backoffice/API | No | Permissioned |
| Authoritative player state | PostgreSQL domain services | Backend/DS | No | No direct edit |
| Secret/security material | Secret manager | Auth/security services | No | No |

## 3. Common Domain Contract

Each domain is wrapped by `configId`, `configType`, `schemaVersion`, `configVersion`, `environment`, `status`, `effectiveFrom`, `effectiveTo`, `createdBy`, `publishedBy`, `reason`, `checksum`, build constraints, and `payload`.

Valid lifecycle states:

```text
draft -> validated -> in_review -> approved -> scheduled -> published -> active
                                                                    -> rolled_back
                                                                    -> archived
                                                                    -> expired
                                                                    -> rejected
```

Every mutation requires an idempotency key and reason. Every lifecycle transition emits an audit event.

## 4. Domain Catalog

### 4.1 feature_flags

Purpose: enable or disable already-implemented behavior without a client rebuild.

Authority/consumers: Go backend; client and DS projections.

Editable fields: flag key, typed value, default value, target rules, priority, build constraints, effective window.

Forbidden fields: secrets, arbitrary code, permissions, wallet/inventory effects.

Validation: key format, supported type, deterministic condition priority, valid build/region rules, bounded rollout percentage.

Rollback: restore a previous published version as a new version.

Audit: creator, reviewer, publisher, reason, target rules, before/after diff.

Sample: `liveops/examples/feature-flags.json`.

### 4.2 maintenance_mode

Purpose: communicate or enforce service maintenance windows.

Authority/consumers: Go backend; client, matchmaking, and Admin Web.

Editable fields: enabled, message key, start/end, allowed roles/builds, blocked operations.

Forbidden fields: authentication bypass, secret values, direct database commands.

Validation: UTC window, message key exists, emergency activation permission, no conflicting active windows.

Rollback: disable or restore the prior active window through a new version.

Audit: activation, extension, disablement, emergency reason.

### 4.3 queue_availability

Purpose: control whether a matchmaking queue accepts tickets.

Authority/consumers: Go matchmaking service, client status UI, Admin Web.

Editable fields: queue ID, enabled state, regions, min/max build, capacity limits, schedule, disable reason.

Forbidden fields: player match result, inventory changes, server credentials.

Validation: known queue/mode/region, compatible builds, non-negative limits, no overlapping contradictory schedules.

Rollback: restore the previous queue state.

Audit: queue state, actor, reason, effective time.

### 4.4 map_rotation

Purpose: define active map/mode rotation.

Authority/consumers: backend matchmaker, DS, client presentation.

Editable fields: rotation ID, entries, weights/order, mode, region, effective window, compatibility.

Forbidden fields: loot seed, player assignment, authoritative match state.

Validation: referenced maps/modes exist, weights are bounded, schedule is unambiguous, build compatibility passes.

Rollback: activate a prior rotation version.

Audit: entry changes and effective window.

### 4.5 event_schedule

Purpose: schedule a time-bounded event or modifier.

Authority/consumers: backend, DS, client event UI, notifications.

Editable fields: event ID, status, start/end, eligibility, modifier references, reward package reference, communication keys.

Forbidden fields: arbitrary reward ownership, executable event code, hidden economy bypasses.

Validation: UTC ordering, referenced content exists, eligibility is deterministic, reward package is valid.

Rollback: deactivate or publish a corrected schedule; retain prior history.

Audit: event lifecycle and reward/config references.

### 4.6 minimum_build

Purpose: block incompatible client or DS builds before login, matchmaking, or admission.

Authority/consumers: auth, matchmaking, DS admission, client update UI.

Editable fields: platform, client/DS build, minimum supported version, enforcement time, message key.

Forbidden fields: patch binaries, signing keys, auth bypasses.

Validation: compatibility matrix exists and enforcement time is UTC.

Rollback: restore the previous compatibility policy only when safe.

Audit: build policy and affected environments.

### 4.7 loot_table_reference

Purpose: select a versioned loot table for a map/mode without changing DS code.

Authority/consumers: backend and DS; client receives only player-safe presentation data.

Editable fields: map/mode, table ID/version, effective window, bounded modifiers.

Forbidden fields: loot seed, player ownership, post-match rewards.

Validation: table exists, entries are valid, weights and quantities are bounded, table is compatible with DS.

Rollback: select a prior table version and retain the match version used for audit/replay.

Audit: table version and modifier changes.

### 4.8 shop_rotation

Purpose: select versioned shop/catalog items and prices for a time window.

Authority/consumers: Go economy service and client catalog UI.

Editable fields: catalog version, rotation entries, price references, availability window, region/platform constraints.

Forbidden fields: wallet balances, purchase receipts, entitlement ownership.

Validation: item/catalog references exist, prices are non-negative integer minor units, duplicate entries are rejected, currency policy passes.

Rollback: restore the previous active rotation; never delete purchase/audit history.

Audit: item, price, window, and actor.

### 4.9 quest_definition

Purpose: define versioned daily, weekly, seasonal, or storyline objectives.

Authority/consumers: backend progression service and client quest UI.

Editable fields: objective type, thresholds, eligibility, schedule, reward package reference, display keys.

Forbidden fields: client-completed state, direct reward ownership, unvalidated event trust.

Validation: supported objective type, valid threshold, reward package exists, schedule is valid.

Rollback: stop new assignment or restore a previous definition; retain player progress policy.

Audit: definition and reward changes.

### 4.10 season_definition

Purpose: define a versioned season, progression window, tracks, and reset policy.

Authority/consumers: backend progression, economy, client season UI.

Editable fields: season ID, start/end, tier definitions, track entitlements, XP rules, claim grace window, content references.

Forbidden fields: arbitrary player XP, unearned claims, premium entitlement ownership.

Validation: dates, tier ordering, reward references, entitlement references, reset policy, compatibility.

Rollback: correct future schedule or publish a compensating policy; do not rewrite completed claims.

Audit: season lifecycle and reward changes.

### 4.11 inbox_template

Purpose: define localized inbox messages and approved reward references.

Authority/consumers: backend inbox/outbox workers and client inbox UI.

Editable fields: message keys, expiry policy, reward package reference, notification policy.

Forbidden fields: raw secrets, arbitrary player data, direct wallet/item ownership.

Validation: localization keys, expiry, reward package reference, payload size.

Rollback: archive template or stop future creation; existing grants remain auditable.

Audit: template and reward reference changes.

### 4.12 reward_package

Purpose: define approved, reusable reward bundles for events, quests, seasons, and compensation.

Authority/consumers: backend reward service only; client receives resulting inbox/reward state.

Editable fields: package ID/version, item definitions, quantities, currency codes, expiry policy, eligibility reference.

Forbidden fields: direct player ID ownership, wallet balance replacement, ledger deletion.

Validation: item/currency references, quantity bounds, entitlement policy, no circular references.

Rollback: stop future grants or publish a corrected package; never undo ledger history by deletion.

Audit: package version and grant policy changes.

### 4.13 content_compatibility

Purpose: bind config to compatible client, DS, backend API, schema, and content versions.

Authority/consumers: auth, matchmaking, DS admission, config service.

Editable fields: build IDs, compatibility hash, content version, required chunks, effective window.

Forbidden fields: unsigned binaries, secrets, auth credentials.

Validation: referenced builds/manifests exist, hashes match, compatibility matrix is complete.

Rollback: restore a known-compatible matrix only after verification.

Audit: build/content policy and affected domains.

## 5. Cross-Domain Rules

- A domain cannot reference an unpublished or incompatible version.
- A published configuration is immutable.
- A rollback is a new publication.
- A failed config fetch uses safe fallback and emits telemetry.
- Client projections never include server-only or admin-only fields.
- Player inventory, wallet, match result, secrets, and executable code remain outside this catalog.

## 6. Contract Consistency Matrix

Before backend implementation, every row must be checked against the OpenAPI YAML, payload schema, SQL column, permission, projection, and rollback rule.

| Domain | Schema | API family | Primary consumer | Projection | Required permission |
|---|---|---|---|---|---|
| feature_flags | `feature-flags.schema.json` | `/admin/liveops/configs` | Client/DS | client/server | `config.write` |
| maintenance_mode | `maintenance-mode.schema.json` | `/admin/liveops/configs` | Client/API | client/admin | `maintenance.write` |
| queue_availability | `queue-availability.schema.json` | `/admin/liveops/configs` | Matchmaker | client/server | `queue.write` |
| map_rotation | `map-rotation.schema.json` | `/admin/liveops/configs` | Matchmaker/DS | client/server | `rotation.write` |
| event_schedule | `event-schedule.schema.json` | `/admin/liveops/configs` | Backend/client | client/server | `schedule.write` |
| minimum_build | `minimum-build.schema.json` | `/admin/liveops/configs` | Auth/DS | client/server | `compatibility.write` |
| loot_table_reference | `loot-table-reference.schema.json` | `/admin/liveops/configs` | Backend/DS | server | `loot.write` |
| shop_rotation | `shop-rotation.schema.json` | `/admin/liveops/configs` | Economy/client | client/server | `catalog.write` |
| quest_definition | `quest-definition.schema.json` | `/admin/liveops/configs` | Progression/client | client/server | `quest.write` |
| season_definition | `season-definition.schema.json` | `/admin/liveops/configs` | Progression/client | client/server | `season.write` |
| inbox_template | `inbox-template.schema.json` | `/admin/liveops/configs` | Inbox/client | client/server | `inbox.write` |
| reward_package | domain service schema | `/admin/liveops/configs` | Reward service | server | `reward.write` |
| content_compatibility | `content-compatibility.schema.json` | `/admin/liveops/configs` | Auth/DS | server | `compatibility.write` |

The matrix is a review artifact, not a replacement for the executable OpenAPI contract or SQL migrations.
