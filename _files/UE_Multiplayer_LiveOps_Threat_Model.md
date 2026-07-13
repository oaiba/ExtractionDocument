# LiveOps STRIDE Threat Model and Abuse Cases

## Scope

This model covers OIDC admin identity, Admin Web, Go Admin API, LiveOps configuration lifecycle, PostgreSQL, Redis/idempotency, audit events, Dedicated Server projections, and player/economy commands.

## Assets

| Asset | Impact if compromised |
|---|---|
| Production configuration | Queue outage, incompatible builds, economy/content damage |
| Player inventory/wallet | Fraud, loss of trust, financial/audit impact |
| Admin identity and roles | Privilege escalation and unauthorized operations |
| Audit history | Loss of accountability and investigation evidence |
| Secrets/signing material | Full service compromise |
| Build compatibility policy | Client/DS admission failure |

## STRIDE Threat Register

| ID | Category | Actor/abuse case | Impact | Mitigation | Detection/recovery | Owner |
|---|---|---|---|---|---|---|
| T01 | Spoofing | Forged OIDC subject or stolen admin token | Unauthorized admin access | OIDC validation, MFA, short-lived token, subject mapping | auth failures, revoke sessions, access review | Security |
| T02 | Tampering | Admin sends actorId/role in request body | False attribution or privilege escalation | derive actor from session; reject client actor fields | audit mismatch alert | Backend |
| T03 | Tampering | Invalid config injection | Queue/economy/content failure | JSON schema and semantic validation | validation failure metrics, rollback | LiveOps |
| T04 | Repudiation | Operator denies a publish/grant | Missing accountability | append-only audit with actor/reason/request ID | audit search and retention | Operations |
| T05 | Information disclosure | Client receives server-only config | Security or gameplay leakage | explicit projections and redaction tests | projection-denied metric | Backend |
| T06 | Denial of service | Disable production queues or publish maintenance | Players cannot connect/play | production approval, RBAC, emergency rollback | queue/config alerts | LiveOps |
| T07 | Elevation | Support role calls grant or sanction endpoint | Economy/moderation abuse | backend permission checks, environment scope | 403 metrics, review | Security |
| T08 | Replay | Reuse grant or publish idempotency key | Duplicate reward or publication | request hash and scoped unique key | duplicate command metric | Backend |
| T09 | Tampering | Rollback to incompatible version | Client/DS failures | compatibility revalidation before publish | build mismatch alerts | Release |
| T10 | Tampering | Modify published version in place | Audit/history corruption | immutable versions and DB/service guards | integrity review | Data |
| T11 | Information disclosure | Secret in Remote Config payload | Credential exposure | schema/policy denylist; secret manager only | secret scanning | Security |
| T12 | Spoofing | Stage token used against Production | Environment crossover | environment-bound role/session and audience | environment-denied metric | Platform |
| T13 | Tampering | Audit event altered/deleted | Investigation failure | append-only table, restricted grants, archive policy | audit gap check | Operations |
| T14 | Denial of service | Redis outage bypassed by fail-open admin writes | Duplicate/rate-limit risk | fail closed for publish/privileged commands | Redis health alert | Platform |
| T15 | Tampering | Client claims reward/inventory ownership | Economy fraud | command service and authoritative ledger only | ledger mismatch alert | Economy |

## Required Abuse Cases

### Production publish without approval

Expected result: `403` or `liveops_publish_not_approved`; no active version change; audit event records denial.

### Duplicate grant with same key and hash

Expected result: original command result; exactly one ledger/outbox effect.

### Duplicate grant with same key and different hash

Expected result: non-retryable conflict; no second effect; audit event records misuse.

### Stolen Stage token calling Production

Expected result: `admin_environment_denied`; no database mutation; alert after repeated attempts.

### Client requests server-only projection

Expected result: server-only fields are absent; projection denial telemetry is emitted if the request is invalid.

## Review Requirements

Security review must confirm OIDC audience/issuer validation, MFA enforcement, role/environment binding, secret redaction, audit immutability, command idempotency, and rollback authorization before backend implementation.
