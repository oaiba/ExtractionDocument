# LiveOps Contract Test Matrix

Validation is tool-agnostic in this phase. Each row can later be implemented in Go or TypeScript without changing the expected result.

## Configuration Fixtures

| Fixture | Envelope | Payload | Expected result | Error |
|---|---|---|---|---|
| feature flags active | valid | valid | accept | — |
| maintenance scheduled | valid | valid | accept | — |
| queue disabled | valid | valid | accept | — |
| map rotation | valid | valid | accept | — |
| shop rotation | valid | valid | accept | — |
| season scheduled | valid | valid | accept | — |
| loot reference | valid | valid | accept | — |
| rollback candidate | valid | valid | accept | — |
| incompatible build | valid | incompatible | reject | `liveops_config_build_incompatible` |
| invalid type | valid | wrong type | reject | `liveops_config_invalid` |
| invalid date | valid | malformed date | reject | `liveops_config_invalid` |
| invalid range | valid | negative/out of range | reject | `liveops_config_value_out_of_range` |
| missing reference | valid | unknown item/reward | reject | `liveops_config_reference_missing` |
| schedule conflict | valid | overlapping rules | reject | `liveops_config_schedule_conflict` |
| forbidden projection | valid | server/admin field in client | reject/redact | `liveops_config_projection_forbidden` |

## Lifecycle Cases

| Case | Expected result |
|---|---|
| Draft validates | status becomes `validated` |
| Invalid draft submits review | rejected; remains `draft` |
| Approved config publishes | one active version |
| Draft directly publishes | rejected with `liveops_config_state_invalid` |
| Published config edited | rejected with `liveops_config_immutable` |
| Concurrent publish | one succeeds; other gets conflict |
| Valid rollback | new version with `rollbackOf` |
| Invalid rollback target | `liveops_rollback_target_invalid` |
| Scheduled activation | activates at UTC `effectiveFrom` |

## Command Cases

| Case | Expected result |
|---|---|
| Grant once | one command, one ledger/outbox effect |
| Grant duplicate same hash | original result returned |
| Grant duplicate different hash | conflict, no second effect |
| Revoke once | one command and audit event |
| Publish without approval | denied, no activation |
| Production without permission | `admin_environment_denied` |
| Auditor mutation | `admin_permission_denied` |
| Missing reason | `admin_reason_required` |
| Missing confirmation | `admin_confirmation_required` |

## Projection Cases

- client projection contains only client-safe fields;
- server projection contains approved server-only fields but no secrets;
- admin projection contains audit/workflow metadata only for authorized roles;
- player projection never contains internal credentials or authoritative mutation controls.
