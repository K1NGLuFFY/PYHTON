## 2024-05-23 - deepcopy is slow
**Learning:** `copy.deepcopy` is significantly slower (approx 3x) than `json.load` for the project's data structure (dict with list of dicts).
**Action:** Use manual cloning (creating a new dict and list comprehensions with shallow copies of inner dicts) when deep copy semantics are needed for performance-critical paths. Manual cloning proved to be ~7x faster than `json.load` in benchmarks.
