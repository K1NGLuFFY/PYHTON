## 2024-10-24 - File I/O Caching in queue_app.py
**Learning:** For single-user local file-based apps, checking `os.stat().st_mtime` is significantly faster than reading/parsing the file, effectively allowing a read-through cache.
**Action:** When optimizing file-backed scripts, always consider a global cache invalidated by `mtime` to reduce IOPS.
