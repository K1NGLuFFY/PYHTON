
import unittest
import os
import shutil
import json
import time
from unittest.mock import patch, MagicMock
import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_data_dir"
        self.test_file = os.path.join(self.test_dir, "queue.json")
        os.makedirs(self.test_dir, exist_ok=True)

        # Patch the module-level variables
        self.orig_data_dir = queue_app.DATA_DIR
        self.orig_data_file = queue_app.DATA_FILE
        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = self.test_file

        # Reset cache if it exists (for future proofing)
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

        # Initialize file
        with open(self.test_file, "w") as f:
            json.dump({"next_id": 1, "queue": [], "history": []}, f)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        queue_app.DATA_DIR = self.orig_data_dir
        queue_app.DATA_FILE = self.orig_data_file

        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def test_add_person(self):
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry["name"], "Alice")
        self.assertEqual(entry["id"], 1)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Alice")

    def test_call_next(self):
        queue_app.add_person("Bob")
        called = queue_app.call_next()
        self.assertEqual(called["name"], "Bob")

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 0)
        self.assertEqual(len(data["history"]), 1)

    def test_persistence(self):
        queue_app.add_person("Charlie")
        # Verify file on disk has it
        with open(self.test_file, "r") as f:
            disk_data = json.load(f)
        self.assertEqual(disk_data["queue"][0]["name"], "Charlie")

    def test_caching_behavior(self):
        # Initial load to populate cache
        queue_app.load_data()

        # Patch json.load to ensure we don't read from disk
        with patch("json.load", side_effect=Exception("Should not hit disk!")) as mock_load:
            # Second load should use cache
            data = queue_app.load_data()
            self.assertIsInstance(data, dict)

        # Verify immutability: modifying the returned data shouldn't affect the cache
        data["queue"].append({"id": 999, "name": "Fake"})

        # Load again - should still use cache (if file hasn't changed), and shouldn't have the fake entry
        data2 = queue_app.load_data()
        # check that data2 does not contain the fake entry
        fake_entries = [p for p in data2["queue"] if p.get("id") == 999]
        self.assertEqual(len(fake_entries), 0)

if __name__ == "__main__":
    unittest.main()
