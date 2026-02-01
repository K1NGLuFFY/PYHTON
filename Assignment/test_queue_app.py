import unittest
import os
import json
import time
import shutil
import tempfile
import sys
import copy
from unittest.mock import patch

# Add current directory to path so we can import queue_app
sys.path.append(os.path.dirname(__file__))

import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.data_file = os.path.join(self.test_dir, "queue.json")

        # Patch the constants in the module
        self.patcher_file = patch('queue_app.DATA_FILE', self.data_file)
        self.patcher_dir = patch('queue_app.DATA_DIR', self.test_dir)

        self.patcher_file.start()
        self.patcher_dir.start()

        # Reset cache if it exists (for future tests)
        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def tearDown(self):
        self.patcher_file.stop()
        self.patcher_dir.stop()
        shutil.rmtree(self.test_dir)

        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def test_add_person(self):
        queue_app.ensure_data_file()
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry['name'], "Alice")

        data = queue_app.load_data()
        self.assertEqual(len(data['queue']), 1)
        self.assertEqual(data['queue'][0]['name'], "Alice")

    def test_call_next(self):
        queue_app.ensure_data_file()
        queue_app.add_person("Bob")
        called = queue_app.call_next()
        self.assertEqual(called['name'], "Bob")

        data = queue_app.load_data()
        self.assertEqual(len(data['queue']), 0)
        self.assertEqual(len(data['history']), 1)

    def test_read_performance(self):
        queue_app.ensure_data_file()
        # Fill with some data
        for i in range(100):
            queue_app.add_person(f"Person {i}")

        start_time = time.time()
        loops = 1000
        for _ in range(loops):
            queue_app.load_data()
        duration = time.time() - start_time
        print(f"\nRead {loops} times in {duration:.4f}s ({(duration/loops)*1000:.4f} ms/call)")

    def _manual_clone(self, data):
        return {
            "next_id": data["next_id"],
            "queue": [d.copy() for d in data.get("queue", [])],
            "history": [d.copy() for d in data.get("history", [])]
        }

    def test_benchmark_vs_raw(self):
        queue_app.ensure_data_file()
        for i in range(100):
            queue_app.add_person(f"Person {i}")

        data = queue_app.load_data()

        loops = 1000

        # Benchmark optimized load_data (with cache)
        start = time.time()
        for _ in range(loops):
            queue_app.load_data()
        optimized_time = time.time() - start

        # Benchmark simulated raw disk read (force reload)
        # We simulate this by clearing cache or assuming json.load cost
        # But better to just measure json.load cost separately
        start = time.time()
        for _ in range(loops):
            with open(self.data_file, "r") as f:
                json.load(f)
        raw_time = time.time() - start

        print(f"\nBenchmark results ({loops} loops):")
        print(f"Optimized load_data: {optimized_time:.4f}s")
        print(f"Raw json.load: {raw_time:.4f}s")
        print(f"Speedup: {raw_time/optimized_time:.2f}x")

if __name__ == '__main__':
    unittest.main()
