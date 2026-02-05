## 2026-02-05 - Read-Through Caching for JSON Stores
**Learning:** For small JSON-based data stores, blindly reading the file on every access is a major bottleneck (0.11ms/call).
**Action:** Implement a read-through cache using `os.stat().st_mtime` for invalidation. Use manual shallow/deep copying instead of `copy.deepcopy` to achieve ~6x speedup (to 0.017ms/call).
