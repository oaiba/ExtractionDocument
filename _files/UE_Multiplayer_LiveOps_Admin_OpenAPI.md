# LiveOps Admin API Contract

## 1. Contract Rules

- Base path: `/v1`.
- Transport: HTTPS.
- Authentication: OIDC-derived backend admin session/token.
- All timestamps: UTC ISO-8601.
- JSON fields: lower camel case.
- Mutations require `Idempotency-Key`, `reason`, request ID, permission, and audit event.
- Actor identity is derived from the authenticated session; `actorId`, `role`, and wallet balances are never trusted from request bodies.
- Published configuration versions are immutable.

## 2. Common Schemas

### ErrorEnvelope

```yaml
ErrorEnvelope:
  type: object
  required: [error]
  properties:
    error:
      type: object
      required: [code, message, requestId, retryable]
      properties:
        code: {type: string}
        message: {type: string}
        requestId: {type: string}
        retryable: {type: boolean}
```

### AdminIdentity

```yaml
AdminIdentity:
  type: object
  required: [subject, email, roles, environments]
  properties:
    subject: {type: string}
    email: {type: string, format: email}
    displayName: {type: string}
    roles: {type: array, items: {type: string}}
    environments: {type: array, items: {type: string, enum: [development, stage, production]}}
```

### MutationRequest

```yaml
MutationRequest:
  type: object
  required: [idempotencyKey, reason, payload]
  properties:
    idempotencyKey: {type: string, format: uuid}
    reason: {type: string, minLength: 3, maxLength: 1000}
    confirmation: {type: string, enum: [CONFIRM]}
    payload: {type: object}
```

### LiveOpsConfig

```yaml
LiveOpsConfig:
  type: object
  required: [configId, configType, schemaVersion, configVersion, environment, status, payload]
  properties:
    configId: {type: string}
    configType: {type: string}
    schemaVersion: {type: integer, minimum: 1}
    configVersion: {type: integer, minimum: 1}
    environment: {type: string, enum: [development, stage, production]}
    status: {type: string, enum: [draft, validated, in_review, approved, scheduled, published, active, rolled_back, archived, rejected, expired]}
    effectiveFrom: {type: string, format: date-time}
    effectiveTo: {type: string, format: date-time, nullable: true}
    createdBy: {type: string}
    publishedBy: {type: string, nullable: true}
    reason: {type: string}
    checksum: {type: string}
    clientBuildConstraints: {type: array, items: {type: object}}
    serverBuildConstraints: {type: array, items: {type: object}}
    payload: {type: object}
```

### AuditEvent

```yaml
AuditEvent:
  type: object
  required: [id, actorSubject, action, target, environment, requestId, occurredAt]
  properties:
    id: {type: string, format: uuid}
    actorSubject: {type: string}
    actorRole: {type: string}
    action: {type: string}
    target: {type: object}
    before: {type: object, nullable: true}
    after: {type: object, nullable: true}
    reason: {type: string}
    environment: {type: string}
    requestId: {type: string}
    occurredAt: {type: string, format: date-time}
```

## 3. Endpoint Contract Matrix

| Method | Path | Permission | Success | Errors |
|---|---|---|---|---|
| GET | `/v1/admin/me` | authenticated admin | `AdminIdentity` | `admin_auth_required` |
| GET | `/v1/admin/roles` | `role.read` | roles | `admin_permission_denied` |
| GET | `/v1/admin/permissions` | `permission.read` | permissions | `admin_permission_denied` |
| GET | `/v1/admin/dashboard/summary` | `dashboard.read` | summary metrics | `admin_permission_denied` |
| GET | `/v1/admin/servers` | `server.read` | paginated servers | `admin_permission_denied` |
| GET | `/v1/admin/queues` | `queue.read` | paginated queues | `admin_permission_denied` |
| GET | `/v1/admin/incidents` | `incident.read` | paginated incidents | `admin_permission_denied` |
| GET | `/v1/admin/liveops/configs` | `config.read` | paginated configs | `admin_permission_denied` |
| POST | `/v1/admin/liveops/configs` | `config.create` | `LiveOpsConfig` | `liveops_config_invalid`, `admin_environment_denied` |
| GET | `/v1/admin/liveops/configs/{id}` | `config.read` | `LiveOpsConfig` | `liveops_config_not_found` |
| PATCH | `/v1/admin/liveops/configs/{id}` | `config.write` | `LiveOpsConfig` | `liveops_config_immutable`, `liveops_config_conflict` |
| POST | `/v1/admin/liveops/configs/{id}/validate` | `config.validate` | validation result | `liveops_config_invalid` |
| POST | `/v1/admin/liveops/configs/{id}/submit-review` | `config.submit_review` | config | `liveops_config_state_invalid` |
| POST | `/v1/admin/liveops/configs/{id}/approve` | `config.approve` | review | `liveops_config_state_invalid` |
| POST | `/v1/admin/liveops/configs/{id}/publish` | `config.publish` | publication | `liveops_publish_not_approved`, `liveops_config_conflict` |
| POST | `/v1/admin/liveops/configs/{id}/rollback` | `config.rollback` | new config version | `liveops_rollback_target_invalid` |
| GET | `/v1/admin/liveops/configs/{id}/diff` | `config.read` | diff | `liveops_config_not_found` |
| GET | `/v1/admin/players` | `player.read` | paginated players | `admin_permission_denied` |
| GET | `/v1/admin/players/{id}` | `player.read` | player detail | `player_not_found` |
| GET | `/v1/admin/players/{id}/matches` | `match.read` | paginated matches | `player_not_found` |
| GET | `/v1/admin/players/{id}/inventory-audit` | `inventory.read` | audit rows | `player_not_found` |
| GET | `/v1/admin/players/{id}/wallet-ledger` | `ledger.read` | ledger rows | `player_not_found` |
| POST | `/v1/admin/players/{id}/revoke-sessions` | `session.revoke` | command result | `admin_command_failed` |
| POST | `/v1/admin/players/{id}/grant` | `grant.execute` | command result | `admin_confirmation_required`, `admin_command_duplicate` |
| POST | `/v1/admin/players/{id}/revoke` | `revoke.execute` | command result | `admin_confirmation_required`, `admin_command_duplicate` |
| POST | `/v1/admin/players/{id}/sanctions` | `sanction.execute` | command result | `admin_command_failed` |
| POST | `/v1/admin/players/{id}/unsanction` | `sanction.execute` | command result | `admin_command_failed` |
| GET | `/v1/admin/audit-events` | `audit.read` | paginated events | `admin_permission_denied` |
| GET | `/v1/admin/audit-events/{id}` | `audit.read` | `AuditEvent` | `audit_event_not_found` |

List endpoints support `limit`, `cursor`, `sort`, and domain-specific filters. Maximum `limit` is 100. Responses expose `nextCursor` when more rows exist.

## 4. Error Catalog

```text
admin_auth_required
admin_permission_denied
admin_reason_required
admin_confirmation_required
admin_environment_denied
liveops_config_not_found
liveops_config_invalid
liveops_config_state_invalid
liveops_config_conflict
liveops_config_immutable
liveops_publish_not_approved
liveops_rollback_target_invalid
admin_command_duplicate
admin_command_failed
admin_audit_write_failed
player_not_found
audit_event_not_found
```

All errors use the architecture error envelope. A duplicate idempotency key with the same request hash returns the original result. The same key with a different hash returns a non-retryable conflict.

## 5. Security and Audit Requirements

- actor identity is derived from the OIDC session;
- every mutation records actor, role, permission, reason, request ID, environment, before/after, and result;
- publish, rollback, grant, revoke, sanction, and session revoke require explicit permission;
- production publish requires approval and creator/reviewer separation;
- Admin Web never receives secrets or raw payment information;
- all endpoints are HTTPS and rate-limited.
