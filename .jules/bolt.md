## 2024-10-25 - copy.deepcopy Performance
**Learning:** `copy.deepcopy` was found to be significantly slower (~3.5ms) than even reading from disk (~1.2ms) for the queue data structure.
**Action:** Implemented a custom `_clone_data` function that performs manual copying, achieving ~0.15ms (20x faster than deepcopy, 7x faster than disk read).
