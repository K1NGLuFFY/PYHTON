## 2024-05-23 - `copy.deepcopy` vs `json.load` Performance
**Learning:** `copy.deepcopy` was found to be significantly slower (approx 3x) than `json.load` for the dictionary structure used in this project. Using it to clone cached data negates the benefits of caching.
**Action:** Use manual cloning (shallow copying nested structures) which was benchmarked to be ~7x faster than `json.load`.

## 2024-05-23 - Robustness of Manual Cloning
**Learning:** Manual cloning for performance must account for schema evolution. A purely hardcoded clone function drops unknown keys.
**Action:** Use `data.copy()` (shallow copy) first to preserve unknown keys, then manually deep-copy known mutable fields (`queue`, `history`) to ensure isolation.
