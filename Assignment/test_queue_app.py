import unittest
import os
import sys
import json
import tempfile
import shutil
from unittest.mock import patch

# Add Assignment to path to import queue_app
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Assignment import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.data_file = os.path.join(self.test_dir, "queue.json")

        # Patch the DATA_FILE in queue_app
        self.patcher = patch('Assignment.queue_app.DATA_FILE', self.data_file)
        self.mock_data_file = self.patcher.start()

        # Also patch DATA_DIR to ensure it gets created in temp dir
        self.dir_patcher = patch('Assignment.queue_app.DATA_DIR', self.test_dir)
        self.mock_data_dir = self.dir_patcher.start()

        # Reset cache if it exists (for when we implement it)
        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def tearDown(self):
        self.patcher.stop()
        self.dir_patcher.stop()
        shutil.rmtree(self.test_dir)
        # Reset cache again
        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def test_add_person(self):
        queue_app.ensure_data_file()
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry["name"], "Alice")
        self.assertEqual(entry["id"], 1)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Alice")

    def test_call_next(self):
        queue_app.ensure_data_file()
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

    def test_persistence(self):
        # Test that data is actually written to file (simulated by reloading)
        queue_app.ensure_data_file()
        queue_app.add_person("Charlie")

        # Force reload from file by clearing cache (if implemented) or just calling load_data
        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Charlie")

    def test_find_person(self):
        queue_app.ensure_data_file()
        p1 = queue_app.add_person("Dave")
        p2 = queue_app.add_person("Eve")
        queue_app.call_next() # Call Dave

        # Find by name
        results = queue_app.find_person("Eve")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Eve")
        self.assertEqual(results[0]["status"], "waiting")

        # Find by ID
        results = queue_app.find_person(str(p1["id"]))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Dave")
        self.assertEqual(results[0]["status"], "called")

if __name__ == '__main__':
    unittest.main()
