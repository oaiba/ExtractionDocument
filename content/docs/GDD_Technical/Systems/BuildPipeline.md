# Build Pipeline & Release Engineering

**[← Back to Index](../README.md)**

---

## 🏗️ Version Control Strategy

### Branching Model (Gitflow modified)
*   **`main` (Production):** The "Gold" standard. Stable, playable, deployable. Locked.
    *   *Rule:* Only merge via Pull Request (PR) after passing Automated Tests.
*   **`development` (Staging):** The integration branch for current sprint.
    *   *Rule:* Nightly builds run from here.
*   **`feature/xyz` (Task):** Individual developer branches. Short-lived (< 2 days).
    *   *Naming:* `feature/loot-spawner`, `fix/crash-inventory`

### Commits
*   **Message Format:** `[Category] Summary`.
    *   *Example:* `[Audio] Added reverb to warehouse zone`
    *   *Example:* `[Bugfix] Resolved inventory duping exploit`

---

## 🤖 CI/CD Automation (Jenkins / GitHub Actions)

### Continuous Integration (CI)
Run on every Push to `feature/*`:
1.  **Code Compilation:** Compile `Development Editor`. Fail on any warning.
2.  **Asset Validation:** Check for broken references or missing textures.
3.  **Unit Tests:** Run C++ core tests (Inventory logic, Damage calc).

### Continuous Delivery (CD)
Run Nightly (03:00 AM) on `development`:
1.  **Map Check:** Open every map and verify no errors.
2.  **Lighting Build:** Rebuild lighting on changed maps (Swarm Agent).
3.  **Package Build:** Create `WindowsNoEditor` and `Android_ASTC` builds.
4.  **Upload:** Push build to Steam (Beta branch) or Internal Server.

---

## 📋 Quality Assurance (QA) Process

### "Smoke Test" (Daily)
*   *Before testing any new feature, verify basic game health:*
    1.  Can launch game?
    2.  Can login / reach Main Menu?
    3.  Can start a Raid (Solo)?
    4.  Can shoot a gun?
    5.  Can Extract?

### Feature Testing (Weekly)
*   **New Mechanics:** Test all edge cases. (e.g., Vaulting while reloading, Vaulting while dying).
*   **Map Walkthrough:** Fly-through map in collision view (`show Collision`) looking for holes.

### Release Candidate (RC) Testing
*   **"Golden Path":** Complete a full progression loop (Lvl 1 -> Lvl 5).
*   **Multiplayer Stress:** 64 simulated clients connecting simultaneously.
*   **Platform Compliance:** Check TRCs (Technical Requirement Check) for Sony/Microsoft/Google.

---

## 🚀 Release Process

1.  **Code Freeze:** No new commits to `development` 48 hours before build.
2.  **Versioning:** Update `ProjectSettings` -> `Version`.
    *   Format: `Major.Minor.Patch` (e.g., `0.8.2`)
3.  **Changelog:** Auto-generate from commit history. Manually curate for readability.
4.  **Tagging:** Create Git Tag `v0.8.2`.
5.  **Distribution:** Push to public branches (Steam Main, App Store Review).

---
