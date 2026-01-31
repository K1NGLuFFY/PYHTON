import unittest
import os
import shutil
import tempfile
import sys
import json

# Ensure we can import queue_app
sys.path.append(os.path.join(os.getcwd(), 'Assignment'))
import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Create a temp dir
        self.test_dir = tempfile.mkdtemp()
        self.original_data_dir = queue_app.DATA_DIR
        self.original_data_file = queue_app.DATA_FILE

        # Override constants
        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = os.path.join(self.test_dir, "queue.json")

        # Reset cache if it exists (for future steps)
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def tearDown(self):
        # Restore constants
        queue_app.DATA_DIR = self.original_data_dir
        queue_app.DATA_FILE = self.original_data_file

        # Remove temp dir
        shutil.rmtree(self.test_dir)

        # Reset cache
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def test_ensure_data_file(self):
        queue_app.ensure_data_file()
        self.assertTrue(os.path.exists(queue_app.DATA_FILE))
        with open(queue_app.DATA_FILE, 'r') as f:
            data = json.load(f)
            self.assertEqual(data["next_id"], 1)
            self.assertEqual(data["queue"], [])

    def test_add_person(self):
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry["name"], "Alice")
        self.assertEqual(entry["id"], 1)

        entry2 = queue_app.add_person("Bob")
        self.assertEqual(entry2["id"], 2)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 2)

    def test_call_next(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")

        called = queue_app.call_next()
        self.assertEqual(called["name"], "Alice")
        self.assertTrue("called_at" in called)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Bob")
        self.assertEqual(len(data["history"]), 1)

    def test_get_position(self):
        p1 = queue_app.add_person("Alice")
        p2 = queue_app.add_person("Bob")

        self.assertEqual(queue_app.get_position(p1["id"]), 1)
        self.assertEqual(queue_app.get_position(p2["id"]), 2)

        queue_app.call_next()
        self.assertEqual(queue_app.get_position(p2["id"]), 1)
        self.assertIsNone(queue_app.get_position(p1["id"]))

    def test_reset_all(self):
        queue_app.add_person("Alice")
        queue_app.reset_all(confirm=True)
        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 0)
        self.assertEqual(data["next_id"], 1)

if __name__ == "__main__":
    unittest.main()
