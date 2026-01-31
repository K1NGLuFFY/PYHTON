## 2026-01-31 - [Manual Clone vs Deepcopy]
**Learning:** `copy.deepcopy` is surprisingly slow for medium-sized nested dictionaries (200+ items), actually slower than `json.load` (I/O). Manual cloning (shallow copy + explicit list comprehension) is ~40x faster.
**Action:** When cloning known schemas in hot paths, prefer manual cloning over `copy.deepcopy` to avoid severe performance penalties.
