## 2026-01-15 - Atomic File Stat for Cache Validation
**Learning:** When implementing file-based caching, `os.path.getmtime(path)` introduces a race condition (TOCTOU) because the file could change between reading it and checking its time.
**Action:** Use `os.fstat(f.fileno()).st_mtime` on the open file descriptor to ensure the timestamp corresponds exactly to the data read.
