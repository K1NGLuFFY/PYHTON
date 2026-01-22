## 2024-05-23 - File I/O Caching in CLI App
**Learning:** In a single-user CLI app that frequently reads a state file, implementing a read-through cache with `mtime` invalidation drastically reduces I/O.
**Action:** Always check if a read-heavy CLI tool is re-reading the same file repeatedly. Use `os.stat().st_mtime` to invalidate cache cheaply.
**Metric:** Reduced file opens from N (per operation) to 0 (for subsequent reads) in `queue_app.py`.
