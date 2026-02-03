import unittest
import os
import json
import shutil
from datetime import datetime
import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Use a temporary directory for testing
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_data")
        self.test_file = os.path.join(self.test_dir, "queue.json")

        # Override constants in queue_app
        self.original_data_dir = queue_app.DATA_DIR
        self.original_data_file = queue_app.DATA_FILE
        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = self.test_file

        # Ensure clean state
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

        # Reset cache if it existed (for later)
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

        queue_app.DATA_DIR = self.original_data_dir
        queue_app.DATA_FILE = self.original_data_file

    def test_ensure_data_file(self):
        queue_app.ensure_data_file()
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        self.assertEqual(data["next_id"], 1)
        self.assertEqual(data["queue"], [])

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

        person = queue_app.call_next()
        self.assertEqual(person["name"], "Alice")
        self.assertIn("called_at", person)

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
        self.assertIsNone(queue_app.get_position(p1["id"]))
        self.assertEqual(queue_app.get_position(p2["id"]), 1)

    def test_find_person(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")
        queue_app.call_next() # Call Alice

        # Find by name
        results = queue_app.find_person("Alice")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["status"], "called")

        results = queue_app.find_person("Bob")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["status"], "waiting")

        # Find by ID
        results = queue_app.find_person("1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Alice")

    def test_reset_all(self):
        queue_app.add_person("Alice")
        queue_app.reset_all(confirm=True)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 0)
        self.assertEqual(data["next_id"], 1)

if __name__ == '__main__':
    unittest.main()
