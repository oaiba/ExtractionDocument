# Multiplayer LiveOps Admin Backoffice Specification

## 1. Purpose

This document is the implementation companion to `UE_Multiplayer_Live_Services_Architecture_Go_RedpointEOS.md`. It specifies the MVP control plane for safe post-launch configuration, player support, moderation, server operations, and auditable administration.

The Admin Backoffice is an operator client. The Go backend remains authoritative, PostgreSQL remains the source of truth, Redis remains ephemeral, and no Admin UI may write directly to storage.

## 2. MVP Scope

### Included

- OIDC/SSO + MFA login;
- backend-enforced RBAC;
- dashboard for service and game health;
- LiveOps draft/review/publish/rollback;
- feature flags, maintenance, queue availability, rotations, schedules, minimum builds;
- player search and read-only support views;
- session revoke;
- safe grant/revoke commands with idempotency and audit;
- moderation and sanctions;
- server and queue monitoring;
- immutable audit history;
- OpenAPI and PostgreSQL migration requirements.

### Deferred

- A/B testing and personalization;
- automatic optimization;
- multi-region active-active operations;
- direct asset authoring or patch delivery;
- arbitrary database query console;
- autonomous economy balancing;
- secret management through the Backoffice.

## 3. Roles and Permissions

| Role | Permissions |
|---|---|
| support | player.read, match.read, inventory.read, ledger.read, session.revoke |
| moderator | player.read, reports.read, sanctions.create, sanctions.remove |
| game_designer | config.read, config.create, config.validate, config.submit_review |
| economy_operator | catalog.write, loot.write, reward.write, config.submit_review |
| liveops_operator | flags.write, schedule.write, rotation.write, maintenance.write, config.publish |
| ops_engineer | dashboard.read, servers.read, queues.read, incidents.write |
| admin | role.manage, privileged.approve, privileged.execute |
| auditor | audit.read, config.read, commands.read |

Production permissions must be environment-scoped. A user may be allowed to edit Stage without being allowed to publish Production.

## 4. Configuration Lifecycle

```text
Draft -> Validated -> In Review -> Approved -> Scheduled -> Published -> Active
                                                                    |
                                                    Rolled Back / Archived
```

Rules:

- published versions are immutable;
- every mutation has an idempotency key and reason;
- creator and reviewer should be different identities for production;
- publish is atomic from the consumer’s perspective;
- rollback creates a new version;
- all timestamps are UTC;
- configuration has a checksum and schema version;
- client and server projections are filtered separately;
- failed validation cannot be submitted for review;
- expired configuration is not silently treated as permanent configuration.

## 5. Admin Web Screens

### Overview

Cards and tables for CCU, API latency/error rate, queue depth, server capacity, heartbeat age, match failures, economy anomalies, configuration version, and active incidents.

### LiveOps

List, filter, create, validate, compare, review, schedule, publish, and rollback configurations. The publish screen must show environment, effective time, compatibility constraints, payload diff, validation result, reason, and approver.

### Player Support

Search by internal player ID, EOS Product User ID, display name, or session/device identifier. Show profile, sessions, match history, inventory audit, wallet ledger, sanctions, and available support commands.

### Content and Economy

Show versioned item definitions, loot tables, catalogs, rotations, quests, seasons, and inbox templates. All writes use the same lifecycle as LiveOps config.

### Moderation

Show reports, evidence metadata, sanctions, appeals, active restrictions, reason codes, actor, dates, and review state.

### Infrastructure

Show server registration, build, region, capacity, heartbeat, status, active matches, drain state, queue, and compatibility.

### Audit

Search by actor, target, action, environment, request ID, command ID, config ID, date range, and severity. Show complete before/after diff and related approval/publish events.

## 6. API Contract

```text
GET    /v1/admin/me
GET    /v1/admin/roles
GET    /v1/admin/permissions
GET    /v1/admin/dashboard/summary
GET    /v1/admin/servers
GET    /v1/admin/queues
GET    /v1/admin/incidents

GET    /v1/admin/liveops/configs
POST   /v1/admin/liveops/configs
GET    /v1/admin/liveops/configs/{id}
PATCH  /v1/admin/liveops/configs/{id}
POST   /v1/admin/liveops/configs/{id}/validate
POST   /v1/admin/liveops/configs/{id}/submit-review
POST   /v1/admin/liveops/configs/{id}/approve
POST   /v1/admin/liveops/configs/{id}/publish
POST   /v1/admin/liveops/configs/{id}/rollback
GET    /v1/admin/liveops/configs/{id}/diff

GET    /v1/admin/players
GET    /v1/admin/players/{id}
GET    /v1/admin/players/{id}/matches
GET    /v1/admin/players/{id}/inventory-audit
GET    /v1/admin/players/{id}/wallet-ledger
POST   /v1/admin/players/{id}/revoke-sessions
POST   /v1/admin/players/{id}/grant
POST   /v1/admin/players/{id}/revoke
POST   /v1/admin/players/{id}/sanctions
POST   /v1/admin/players/{id}/unsanction

GET    /v1/admin/audit-events
GET    /v1/admin/audit-events/{id}
```

### Mutation envelope

```json
{
  "idempotencyKey": "uuid",
  "reason": "Customer support compensation for incident INC-123",
  "confirmation": "CONFIRM",
  "payload": {}
}
```

The backend derives actor identity from the authenticated OIDC session. It must reject arbitrary actor IDs in the request body.

## 7. Data Model Requirements

Required migrations:

```text
admin_identities
admin_roles
admin_permissions
admin_role_bindings
liveops_configs
liveops_config_versions
liveops_config_reviews
liveops_config_publications
liveops_config_targets
admin_commands
admin_command_results
admin_audit_events
incidents
incident_updates
```

Minimum common fields:

```text
id
environment
status
created_at
updated_at
created_by
reason
request_id
```

Configuration versions additionally require `schema_version`, `payload`, `checksum`, `effective_from`, `effective_to`, `published_by`, `published_at`, `rollback_of`, and compatibility constraints.

Commands additionally require `command_type`, `target_type`, `target_id`, `request_hash`, `idempotency_key`, `status`, `result`, `failure_code`, and completion timestamps.

Audit events additionally require `actor_subject`, `actor_role`, `action`, `target`, `before`, `after`, `reason`, `environment`, and related config/command IDs.

## 8. Safe Player Commands

Supported commands:

- revoke active sessions;
- grant approved item/currency/reward package;
- revoke or compensate through an explicit ledger transaction;
- create/remove sanction;
- attach an operator note or incident reference.

Commands must be processed by domain services. The Admin API must never accept a new wallet balance, arbitrary item owner, or raw SQL. Every command is idempotent, transactional, auditable, and retry-safe.

## 9. Configuration Validation

Validation has three layers:

1. JSON schema and required fields.
2. Domain rules such as valid item IDs, non-overlapping schedules, compatible builds, valid map/mode combinations, non-negative prices, and bounded tuning ranges.
3. Cross-domain checks such as reward references, catalog references, season dates, content compatibility, and client/DS support.

The UI must show all validation errors before review. Publish must revalidate against the current database state to prevent stale drafts from activating invalid references.

## 10. Security and Failure Behavior

- OIDC token validation and role lookup happen in the backend.
- Production access requires MFA and environment permission.
- Admin endpoints are rate-limited and logged.
- Sensitive responses are redacted according to role.
- Redis outage fails closed for publish and privileged commands.
- Configuration read outage uses last-known-safe or compiled defaults.
- A stale configuration must be visible to operators and must not enable unsafe authoritative actions.
- Admin UI does not expose secrets, tokens, private keys, or raw payment data.

## 11. Observability

Every request and command emits structured logs with request ID, actor subject, environment, action, target, status, latency, and related config/command ID. Metrics include publish failures, rollback count, command success/failure, audit write failures, config fetch errors, stale-config usage, queue health, server health, and economy mismatch alerts.

Each alert links to an incident runbook and has an owner, severity, threshold, and escalation path.

## 12. Test and Acceptance Matrix

| Area | Acceptance |
|---|---|
| Auth | OIDC user without role receives 403; expired session redirects to login |
| RBAC | Backend blocks unauthorized endpoint even when UI is bypassed |
| Lifecycle | Invalid config cannot review/publish; published version is immutable |
| Concurrency | Concurrent publish and duplicate command do not double-apply |
| Rollback | Rollback creates a new version and invalidates caches |
| Projection | Client response excludes server-only and admin-only fields |
| Economy | Grant/revoke writes ledger, audit, and outbox exactly once |
| Audit | Actor, reason, before/after, request ID, environment, and timestamp exist |
| Resilience | Config outage uses safe fallback; Redis outage fails closed for writes |
| UI | Diff, confirmation, error, loading, empty, stale, and permission states work |
| Recovery | Database restore preserves versions, audit, commands, and ledger consistency |

## 13. Delivery Order

1. Threat model, roles, permissions, config classification, and audit contract.
2. Migrations and backend OIDC/RBAC/audit foundations.
3. Admin API read paths and dashboard data.
4. Config lifecycle and public/server configuration projections.
5. Admin Web authentication, LiveOps, audit, server, and queue screens.
6. Player support and safe commands.
7. Content domains: catalog, loot, events, quests, seasons, inbox.
8. Staging promotion, load testing, rollback drill, access review, and operator runbooks.

## 14. External References

- PlayFab Game Manager: https://learn.microsoft.com/en-us/xbox/playfab/live-service-management/gamemanager/reference
- Firebase Remote Config parameters and conditions: https://firebase.google.com/docs/remote-config/parameters
- Firebase Remote Config versioning and rollback: https://firebase.google.com/docs/remote-config/templates
- Unity LiveOps: https://docs.unity.com/en-us/liveops
- Epic Fortnite seasons: https://dev.epicgames.com/documentation/fortnite/chapter
- Bungie Destiny 2 content: https://help.bungie.net/hc/en-us/articles/44243991218196--2-Available-Content-Expansions-Seasons-and-More
- GDC Effective LiveOps Strategies: https://media.gdcvault.com/gdc2015/presentations/EffectiveLiveOps_Gwertzman_2015.03.01.pdf

## 15. Contract Pack and Source of Truth

The companion artifacts are:

```text
UE_Multiplayer_LiveOps_Data_Catalog.md
UE_Multiplayer_LiveOps_Admin_OpenAPI.md
UE_Multiplayer_LiveOps_Operations_Runbook.md
liveops/*.schema.json
liveops/examples/*.json
```

The data catalog defines domain meaning and ownership. The JSON schemas define payload shape. The OpenAPI-ready contract defines the HTTP interface. This document defines the Admin Backoffice behavior and security boundary. All timestamps are UTC; JSON uses lower camel case; PostgreSQL uses snake_case.

## 16. Documentation Acceptance Gate

The contract pack is ready for backend implementation only when every v1 domain has a catalog entry, schema, valid example, visibility projection, validation rule, rollback rule, and audit requirement. Every Admin API must have authentication, permission, request/response, error, idempotency, audit, and concurrency definitions.

## 17. Contract Hardening Artifacts

The executable contract and review artifacts are:

```text
liveops/openapi/liveops-admin-v1.yaml
liveops/schemas/*.schema.json
liveops/sql/*.sql
UE_Multiplayer_LiveOps_Threat_Model.md
UE_Multiplayer_LiveOps_Admin_UI_Page_Spec.md
liveops/fixtures/contract-test-matrix.md
UE_Multiplayer_LiveOps_Observability_Catalog.md
```

OpenAPI 3.1 YAML is the source for later DTO/code generation. SQL files are migration drafts and are not executed by this document phase. The UI page specification uses Mermaid and ASCII layout descriptions; it is not a production frontend implementation.
