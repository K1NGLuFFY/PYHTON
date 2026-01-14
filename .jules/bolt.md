## 2026-01-14 - [Read-Through Caching for JSON Stores]
**Learning:** Frequent file I/O for small JSON stores kills performance. `json.load` is expensive.
**Action:** Implement in-memory read-through caching with `os.path.getmtime` invalidation for file-backed stores.
