## 2024-05-23 - Deepcopy Performance Trap
**Learning:** `copy.deepcopy` is significantly slower (approx 2.5x slower) than `json.load` for the project's data structure (dict with list of dicts). Manual cloning (shallow copy of list + shallow copy of dicts) is ~8.5x faster than `json.load`.
**Action:** Prefer manual cloning of known schemas over `copy.deepcopy` in performance-critical paths, especially when avoiding I/O.
