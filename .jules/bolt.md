## 2024-05-23 - Deepcopy vs JSON Load Performance
**Learning:** `copy.deepcopy()` can be significantly slower (3x in this case) than `json.load()` for simple data structures in Python. `json.load` uses C-optimized parsing, while `deepcopy` is pure Python with high overhead.
**Action:** When implementing in-memory caching for JSON data, avoid `copy.deepcopy()`. Use manual cloning (list comprehensions + shallow dict copies) or separate read-only vs mutable access patterns.
