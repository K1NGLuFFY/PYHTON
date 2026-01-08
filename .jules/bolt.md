## 2024-10-27 - [Recursive Dict Copy Performance]
**Learning:** A recursive dictionary/list comprehension copy function (`fast_copy`) is significantly faster (~3x) than `copy.deepcopy()` for JSON-like data structures in Python, and close enough to `json.load()` performance to make caching viable while maintaining safety (returning copies).
**Action:** Use custom recursive copy functions for JSON data when performance is critical and `deepcopy` is too slow, but data safety (immutability/copying) is required.
