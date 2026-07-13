# LiveOps Observability Catalog

## Metrics

| Metric | Type | Source | Labels | Alert/owner |
|---|---|---|---|---|
| `liveops_config_publish_failure_total` | counter | config service | env,type,error | Sev2 / LiveOps |
| `liveops_config_rollback_total` | counter | config service | env,type,reason | dashboard / LiveOps |
| `liveops_config_validation_failure_total` | counter | validation service | env,type,error | warning / Designer |
| `liveops_config_fetch_failure_total` | counter | client/server gateway | env,consumer,error | Sev2 / Platform |
| `liveops_config_stale_usage_total` | counter | client/server gateway | env,consumer,age | Sev2 / Platform |
| `liveops_config_projection_denied_total` | counter | projection service | env,consumer,field | Sev2 / Security |
| `admin_command_success_total` | counter | command service | env,type,role | dashboard / Operations |
| `admin_command_failure_total` | counter | command service | env,type,error | Sev2 / Operations |
| `admin_command_duplicate_total` | counter | command service | env,type | warning / Backend |
| `admin_audit_write_failure_total` | counter | audit service | env,action,error | Sev1 / Security |
| `admin_permission_denied_total` | counter | Admin API | env,role,permission | warning / Security |
| `server_heartbeat_age_seconds` | gauge | server registry | env,region,server | Sev2 / Ops |
| `match_commit_failure_total` | counter | match service | env,region,error | Sev1 / Backend |
| `economy_ledger_mismatch_total` | counter | economy service | env,currency,error | Sev1 / Economy |
| `queue_wait_time_seconds` | histogram | matchmaking | env,queue,region | Sev2 / Matchmaking |

## Events

```text
liveops.config.created
liveops.config.validated
liveops.config.submitted
liveops.config.approved
liveops.config.published
liveops.config.rolled_back
admin.command.executed
admin.command.failed
admin.permission.denied
admin.audit.write_failed
```

Every event includes `eventId`, `eventType`, `occurredAt`, `environment`, `requestId`, `actorSubject` when applicable, `target`, and a redacted payload.

## Dashboard Mapping

- LiveOps dashboard: validation failures, publish failures, rollback count, stale usage, active version.
- Admin security dashboard: permission denied, audit write failure, failed OIDC, environment denied.
- Matchmaking dashboard: queue wait, queue depth, server heartbeat, allocation failures.
- Economy dashboard: command failures, duplicate commands, ledger mismatch, purchase/refund failures.
- Incident dashboard: severity, open duration, affected environment, active mitigation.

## Alert Rules

Every alert links to the Operations Runbook and specifies severity, owner, escalation, and acknowledgement target. Critical paths fail closed for unsafe writes when configuration, audit, idempotency, or authorization dependencies are unavailable.
