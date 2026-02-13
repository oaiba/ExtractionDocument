---
title: "Bug Fix Workflow"
type: docs
weight: 2
---

## Bug Fix Workflow

A systematic approach for AI agents and developers to diagnose, fix, and verify bugs.

---

### Phase 1: Reproduce & Understand

1. **Read the bug report** — Understand the expected vs. actual behavior
2. **Identify the system** — Which module/plugin is affected?
3. **Reproduce the issue** — Confirm the bug exists in the current build
4. **Check logs** — Look for relevant `UE_LOG` output, warnings, errors

```
// Key log files to check
Saved/Logs/ExtractionGame.log    ← Full session log
Saved/Crashes/                   ← Crash dumps
```

**Key Questions:**
- Does it reproduce consistently?
- Is it client-only, server-only, or both?
- Does it only happen with specific data/configuration?
- When did it start occurring? (check recent commits)

---

### Phase 2: Diagnose

1. **Trace the call stack** — Start from the symptom, work backwards
2. **Check recent changes** — `git log --oneline -20` for last 20 commits
3. **Add temporary logging** — Use `UE_LOG` with `Verbose` level
4. **Use breakpoints** — In Visual Studio or Rider
5. **Check replication** — Is the state mismatched between server/client?

**Common Bug Categories:**

| Category | Symptoms | Likely Cause |
|:---------|:---------|:-------------|
| **Null pointer** | Crash with access violation | Missing null check, wrong initialization order |
| **Replication** | Client shows wrong value | Missing `DOREPLIFETIME`, wrong condition |
| **Timing** | Works sometimes, not others | Race condition, order of BeginPlay |
| **Data** | Wrong values | Data Asset typo, wrong enum value |
| **UI** | Widget not updating | Delegate not bound, wrong binding target |
| **Animation** | Wrong pose/montage | ABP state error, wrong slot |
| **Physics** | Falling through floor | Missing collision, wrong channel |

---

### Phase 3: Fix

1. **Make the minimal fix** — Change as little code as possible
2. **Follow coding standards** — [CodingStandards.md](../../GDD_Technical/CodingStandards.md)
3. **Add a guard/check** — Prevent the root cause, not just the symptom
4. **Add logging** — Log warnings for edge cases that should not happen
5. **Update comments** — Explain *why* the fix is needed

```cpp
// Good fix — guard + log
void AExtractionZone::OnPlayerEnter(AExtractionCharacter* Player)
{
    if (!Player)
    {
        UE_LOG(LogExtraction, Warning, TEXT("OnPlayerEnter called with null player"));
        return;
    }
    
    // Previous bug: player could enter while already extracting elsewhere
    if (Player->IsCurrentlyExtracting())
    {
        UE_LOG(LogExtraction, Verbose, TEXT("Player %s already extracting, ignoring zone enter"), *Player->GetName());
        return;
    }
    
    // ...
}
```

---

### Phase 4: Verify

1. **Reproduce the original bug** — Confirm it no longer occurs
2. **Test edge cases** — Null inputs, boundary values, rapid actions
3. **Test multiplayer** — If the bug involves replication
4. **Check for regressions** — Test related systems still work
5. **Compile clean** — Zero warnings, zero errors

---

### Phase 5: Commit

```bash
# Commit message format
git commit -m "[Bugfix] Fix extraction timer not resetting on zone exit (EXT-456)"
```

Update relevant documentation if the bug exposed a design gap.
