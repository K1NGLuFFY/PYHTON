import unittest
import shutil
import tempfile
import os
import json
import sys

# Add Assignment to path
sys.path.append(os.path.join(os.getcwd(), "Assignment"))

import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "queue.json")

        # Patch the module's data constants
        self.original_data_dir = queue_app.DATA_DIR
        self.original_data_file = queue_app.DATA_FILE
        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = self.test_file

        # Reset any global state if exists
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
        if hasattr(queue_app, "_LAST_MTIME"):
            queue_app._LAST_MTIME = 0

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        queue_app.DATA_DIR = self.original_data_dir
        queue_app.DATA_FILE = self.original_data_file

        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
        if hasattr(queue_app, "_LAST_MTIME"):
            queue_app._LAST_MTIME = 0

    def test_initial_load(self):
        data = queue_app.load_data()
        self.assertEqual(data["next_id"], 1)
        self.assertEqual(data["queue"], [])
        self.assertEqual(data["history"], [])

    def test_add_person(self):
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry["name"], "Alice")
        self.assertEqual(entry["id"], 1)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Alice")
        self.assertEqual(data["next_id"], 2)

    def test_call_next(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")

        called = queue_app.call_next()
        self.assertEqual(called["name"], "Alice")
        self.assertIn("called_at", called)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Bob")
        self.assertEqual(len(data["history"]), 1)
        self.assertEqual(data["history"][0]["name"], "Alice")

    def test_persistence(self):
        queue_app.add_person("Charlie")
        # Verify file on disk
        with open(self.test_file, 'r') as f:
            content = json.load(f)
        self.assertEqual(content["queue"][0]["name"], "Charlie")

    def test_cache_safety(self):
        # Ensure that modifying the result of load_data does NOT affect internal state/subsequent calls
        # (unless save_data is called)
        data1 = queue_app.load_data()
        data1["queue"].append({"fake": "data"})

        data2 = queue_app.load_data()
        # data2 should be fresh from disk/cache, not affected by data1 mutation
        # If we returned a reference to cache without copying, this would fail.
        # queue is a list of dicts.
        self.assertEqual(len(data2["queue"]), 0)

if __name__ == "__main__":
    unittest.main()
