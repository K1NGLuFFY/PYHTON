## 2024-05-23 - Read-Through Cache Effectiveness
**Learning:** Replacing direct disk I/O with a mtime-based read-through cache reduced `load_data` latency by ~84% (0.15s -> 0.02s).
**Action:** Look for similar I/O bottlenecks in frequently accessed data files in other assignments.

## 2024-05-23 - Missing Tests
**Learning:** `Assignment/test_queue_app.py` was referenced in memory but missing from the repo, requiring recreation to safely optimize.
**Action:** Always verify existence of test files mentioned in memory/docs before assuming coverage.
