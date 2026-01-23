
import unittest
import os
import sys
import shutil
import json
from unittest.mock import patch, MagicMock

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Use a temporary data directory for tests
        self.test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")
        self.test_data_file = os.path.join(self.test_data_dir, "queue.json")

        # Override constants in queue_app
        self.original_data_dir = queue_app.DATA_DIR
        self.original_data_file = queue_app.DATA_FILE
        queue_app.DATA_DIR = self.test_data_dir
        queue_app.DATA_FILE = self.test_data_file

        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)
        queue_app.ensure_data_file()

    def tearDown(self):
        # Restore constants
        queue_app.DATA_DIR = self.original_data_dir
        queue_app.DATA_FILE = self.original_data_file

        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)

    def test_ensure_data_file_creates_file(self):
        self.assertTrue(os.path.exists(self.test_data_file))
        with open(self.test_data_file, 'r') as f:
            data = json.load(f)
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

    def test_call_next_empty(self):
        result = queue_app.call_next()
        self.assertIsNone(result)

    def test_get_position(self):
        entry1 = queue_app.add_person("Alice")
        entry2 = queue_app.add_person("Bob")

        self.assertEqual(queue_app.get_position(entry1["id"]), 1)
        self.assertEqual(queue_app.get_position(entry2["id"]), 2)

        queue_app.call_next()
        self.assertIsNone(queue_app.get_position(entry1["id"]))
        self.assertEqual(queue_app.get_position(entry2["id"]), 1)

    def test_find_person(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")
        queue_app.call_next() # Call Alice

        # Search by name
        results = queue_app.find_person("Alice")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["status"], "called")

        results = queue_app.find_person("Bob")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["status"], "waiting")

        # Search by ID
        results = queue_app.find_person("1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Alice")

if __name__ == "__main__":
    unittest.main()
