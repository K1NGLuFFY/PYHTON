## 2024-10-24 - File I/O Caching and Manual Cloning
**Learning:** `json.load` is fast, but disk I/O is the bottleneck. Manual shallow+deep copy (`_clone_data`) is significantly faster than `copy.deepcopy` for simple nested structures like this project's queue data. Restoring the read-through cache reduced read times by ~5x.
**Action:** Always prefer manual cloning for known schemas over generic deepcopy in hot paths. Ensure file-based persistence layers implement in-memory caching with mtime invalidation.
