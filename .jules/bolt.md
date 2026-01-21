## 2026-01-21 - [Python Module Patching Quirks]
**Learning:** When testing a Python script that imports standard modules (like `json`), patching `json.load` works reliably when the test script and the target script share the same module namespace. However, improper `sys.path` manipulations in tests can lead to confusing import behaviors where the patched module isn't the one used by the code under test.
**Action:** Simplify test setups by running tests from the correct directory and avoiding unnecessary `sys.path` hacks. Verify `module` identity if mocks are unexpectedly ignored.
