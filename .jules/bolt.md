## 2026-01-18 - Deep copy cost vs Disk Read
**Learning:** `json.loads(json.dumps(x))` for deep copying a ~1000 item dictionary took ~2.2ms, while reading the same JSON from disk (likely OS cached) took ~1.2ms. The overhead of serialization/deserialization exceeded the cached I/O cost.
**Action:** When implementing caching, always allow accessing the immutable reference (`mutable=False`) for read-only operations to bypass the copy cost (0.009ms vs 2.2ms). Only pay the copy cost when mutation is required.
