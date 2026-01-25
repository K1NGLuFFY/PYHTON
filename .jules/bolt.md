## 2025-01-25 - JSON File I/O Caching
**Learning:** Frequent reading of small JSON files (persistence layer) creates significant overhead (~1ms/read). Mtime-based in-memory caching reduced read latency by ~6.7x (to ~0.17ms) while maintaining consistency.
**Action:** For file-backed persistence, always implement an in-memory cache invalidated by file modification time.
