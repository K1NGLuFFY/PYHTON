
import unittest
import os
import shutil
import json
import queue_app
from unittest.mock import patch

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Setup a temporary data directory for testing
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_data")
        self.test_file = os.path.join(self.test_dir, "queue.json")

        # Override the constants in queue_app
        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = self.test_file

        # Reset any global state if we add any later (like cache)
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
        if hasattr(queue_app, "_CACHE_MTIME"):
            queue_app._CACHE_MTIME = 0

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_ensure_data_file(self):
        queue_app.ensure_data_file()
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        self.assertEqual(data["next_id"], 1)
        self.assertEqual(data["queue"], [])

    def test_add_person(self):
        queue_app.add_person("Alice")
        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Alice")
        self.assertEqual(data["next_id"], 2)

    def test_call_next(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")

        called = queue_app.call_next()
        self.assertEqual(called["name"], "Alice")

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Bob")
        self.assertEqual(len(data["history"]), 1)
        self.assertEqual(data["history"][0]["name"], "Alice")

    def test_get_position(self):
        p1 = queue_app.add_person("Alice")
        p2 = queue_app.add_person("Bob")

        self.assertEqual(queue_app.get_position(p1["id"]), 1)
        self.assertEqual(queue_app.get_position(p2["id"]), 2)

        queue_app.call_next()
        self.assertEqual(queue_app.get_position(p2["id"]), 1)
        self.assertIsNone(queue_app.get_position(p1["id"]))

    def test_find_person(self):
        p1 = queue_app.add_person("Alice")
        queue_app.call_next() # Call Alice
        p2 = queue_app.add_person("Alice") # Another Alice

        results = queue_app.find_person("Alice")
        self.assertEqual(len(results), 2)
        # Verify one is called, one is waiting
        statuses = sorted([r["status"] for r in results])
        self.assertEqual(statuses, ["called", "waiting"])

    def test_cache_isolation(self):
        queue_app.add_person("Alice")
        data1 = queue_app.load_data()
        data1["queue"][0]["name"] = "Bob" # Mutate returned data

        data2 = queue_app.load_data() # Should get fresh data (or cached original)
        self.assertEqual(data2["queue"][0]["name"], "Alice")

if __name__ == '__main__':
    unittest.main()
