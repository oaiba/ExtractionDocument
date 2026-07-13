# LiveOps Operations Runbook

## 1. Operating Rules

- Use UTC for all times.
- Confirm environment before every mutation.
- Use the Admin API or Backoffice; never edit PostgreSQL directly.
- Record reason, incident ID, and request ID for privileged actions.
- Verify the resulting active config and audit event after each operation.
- Use rollback for configuration mistakes; do not delete history.

## 2. Enable Maintenance Mode

Trigger: planned maintenance or an active service incident.

Permission: `maintenance.write`; Production emergency activation also requires `privileged.execute`.

Steps:

1. Confirm environment and incident/maintenance reference.
2. Create a `maintenance_mode` draft with UTC start/end and allowed operations.
3. Validate message keys, time window, and affected services.
4. Submit for review or use the emergency procedure.
5. Publish the configuration.
6. Verify `/v1/liveops/config`, client behavior, queue admission, and dashboard status.
7. Record the active config version in the incident.

Rollback: publish a new version with `enabled=false` after the incident owner confirms recovery.

## 3. Disable a Queue

1. Confirm queue, region, reason, and expected duration.
2. Create a `queue_availability` draft with `enabled=false`.
3. Validate that active tickets are handled by the documented cancellation/drain policy.
4. Publish and verify new ticket creation returns the stable queue-disabled response.
5. Monitor queue depth, active matches, and player-facing messaging.

Rollback: restore the previous queue version only after server capacity and compatibility are healthy.

## 4. Restore a Previous Configuration

1. Identify the faulty active version and the last known-good version.
2. Compare the two versions and attach an incident/reason.
3. Confirm the target version is compatible with the current client/DS/backend.
4. Submit rollback through the Admin API.
5. Revalidate and publish the new rollback version.
6. Verify ETag invalidation, client/server projections, and audit history.

Never update or delete the faulty version in place.

## 5. Handle Stale Dedicated Server Heartbeat

1. Confirm server ID, region, build, last heartbeat, and active matches.
2. Mark the server draining through the allocator/ops path.
3. Prevent new assignments.
4. Check process logs and network/credential health without exposing secrets.
5. Re-register or restart only under the server deployment procedure.
6. Verify heartbeat recovery and assignment eligibility.
7. Record the incident and resulting server state.

## 6. Handle Match Commit Failure

1. Locate match ID, server ID, commit version, and idempotency key.
2. Check whether the original transaction committed.
3. Never infer rewards from client UI or retry with a different key.
4. Retry only using the original idempotent commit path when the backend marks it retryable.
5. If the match is abandoned, run the documented reservation recovery policy.
6. Verify inventory/economy ledger consistency and audit records.

## 7. Handle Economy Ledger Mismatch

1. Freeze automated compensation for the affected aggregate if policy requires it.
2. Capture player, transaction, match, request, and audit IDs.
3. Compare wallet projection with append-only ledger and outbox state.
4. Do not edit wallet balance directly.
5. Create an approved compensation/reversal command if required.
6. Verify ledger, inbox, and audit consistency.
7. Escalate repeated mismatches to economy and engineering owners.

## 8. Grant Incident Compensation

1. Link the grant to an incident and eligibility rule.
2. Use an approved reward package, not arbitrary item ownership or balance replacement.
3. Confirm target player/segment and expiry.
4. Submit the idempotent command with reason and confirmation.
5. Verify ledger, inbox, outbox, and audit event.
6. Communicate the result through the approved support channel.

## 9. Revoke Player Sessions

1. Verify player identity using internal ID and a second support signal.
2. Confirm reason and incident/reference.
3. Execute `session.revoke` through the Admin API.
4. Verify active sessions are revoked and refresh reuse is rejected.
5. Record the command result and audit event.

## 10. Ban or Unban a Player

1. Review reports, evidence metadata, match context, and prior sanctions.
2. Confirm policy reason code, scope, and duration.
3. Require `sanction.execute` permission and confirmation.
4. Execute the sanction command.
5. Verify login, matchmaking, and active-session behavior according to policy.
6. Record appeal/review state and audit metadata.

## 11. Configuration Service Outage

1. Check config fetch error rate and last active version.
2. Confirm client/server fallback is using a known-safe snapshot.
3. Do not publish new configuration until the service and database are healthy.
4. Keep purchases, rewards, and authoritative operations fail-closed if required configuration is unavailable.
5. Restore service, revalidate active version, and monitor stale-config usage.
6. Create an incident update with duration and affected versions.

## 12. Redis Outage

1. Treat Admin publish and privileged commands as fail-closed.
2. Do not bypass idempotency or rate limiting by editing Redis manually.
3. Verify PostgreSQL-backed audit and command state.
4. Restore Redis or use the approved degraded-mode procedure.
5. Reconcile failed/retryable commands using original idempotency keys.

## 13. Database Restore Verification

1. Restore into an isolated environment.
2. Verify config versions, publications, reviews, audit events, commands, ledger, and outbox relationships.
3. Confirm no published version was mutated or lost.
4. Run schema/constraint/integrity checks.
5. Record RTO/RPO and corrective work.

## 14. Production Access Review

Monthly:

1. Export active OIDC subjects, roles, permissions, and environments.
2. Remove departed users and stale bindings.
3. Review Production publish and privileged-command usage.
4. Verify MFA and creator/reviewer separation.
5. Record reviewer, date, findings, and remediation.

## 15. Live Incident Escalation

Escalate when there is repeated economy mismatch, data corruption risk, authentication outage, widespread queue failure, unsafe config exposure, or inability to rollback.

Incident record must include:

- start/end time in UTC;
- affected environment/region/build;
- active config version;
- symptoms and player impact;
- actions and request IDs;
- rollback/mitigation;
- owner and escalation path;
- follow-up actions.
