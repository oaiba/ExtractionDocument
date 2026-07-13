# LiveOps PostgreSQL Migration Draft

## Migration Order

```text
001_admin_identity.sql
002_liveops_config.sql
003_admin_commands.sql
004_audit_events.sql
005_incidents.sql
```

## Review Constraints

- These files are drafts and must not be run against production directly.
- Apply with the selected migration runner after adapting transaction/rollback conventions.
- Test clean install and upgrade from the current v1 baseline.
- Test duplicate idempotency keys with equal and different request hashes.
- Test concurrent active-version publication.
- Test review creator/reviewer separation in application logic and database procedure/service code.
- Do not update or delete published versions or audit events in application flows.
- Use forward-fix migrations after merge; do not rewrite historical migrations.

## Known Implementation Notes

- The review creator/reviewer check must be implemented in the service transaction; a subquery check constraint is shown as a design intent and may need to become a trigger or service guard depending on PostgreSQL migration policy.
- `active_version` must be updated atomically with activation and guarded by the unique active index.
- Audit writes are part of the mutation transaction for authoritative commands.
- Retention jobs may archive audit data only after the documented legal/operational retention period.
