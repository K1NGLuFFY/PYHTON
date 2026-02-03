## 2024-05-22 - Deep Copy Performance
**Learning:** `copy.deepcopy` is significantly slower (~3x) than `json.load` for typical JSON-like dictionaries in Python. Manual cloning (shallow copy of containers + deep copy of mutable elements) is ~7x faster than `json.load`.
**Action:** Prefer manual cloning over `copy.deepcopy` in performance-critical paths, especially for known schemas.
