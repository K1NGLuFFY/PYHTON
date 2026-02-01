## 2024-05-23 - deepcopy vs manual clone
**Learning:** `copy.deepcopy` is significantly slower (~25x slower in this case) than manually cloning a known simple structure (dict of lists of dicts) in Python. `json.load` is also faster than `deepcopy`.
**Action:** For performance-critical paths involving known data structures, prefer manual shallow copying of nested elements over `copy.deepcopy`.
