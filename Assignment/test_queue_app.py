import unittest
import os
import json
import shutil
import queue_app
from unittest.mock import patch, MagicMock

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Setup a temporary data directory for testing
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_data")
        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = os.path.join(self.test_dir, "queue.json")

        # Reset cache
        queue_app._CACHE = None
        queue_app._CACHE_MTIME = 0.0

        # Ensure clean slate
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        queue_app.ensure_data_file()

    def tearDown(self):
        # Cleanup
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

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

    def test_find_person(self):
        p1 = queue_app.add_person("Alice")
        queue_app.call_next() # Call Alice
        p2 = queue_app.add_person("Alice") # Another Alice

        results = queue_app.find_person("Alice")
        self.assertEqual(len(results), 2)
        # One waiting, one called
        statuses = sorted([r["status"] for r in results])
        self.assertEqual(statuses, ["called", "waiting"])

    def test_load_data_creates_default(self):
        if os.path.exists(queue_app.DATA_FILE):
            os.remove(queue_app.DATA_FILE)
        data = queue_app.load_data()
        self.assertEqual(data["next_id"], 1)
        self.assertEqual(data["queue"], [])

if __name__ == '__main__':
    unittest.main()
