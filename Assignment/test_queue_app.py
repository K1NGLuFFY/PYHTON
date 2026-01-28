import unittest
import os
import shutil
import sys

# Ensure we can import queue_app
sys.path.append(os.path.dirname(__file__))
import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Reset the data directory before each test
        if os.path.exists(queue_app.DATA_DIR):
            shutil.rmtree(queue_app.DATA_DIR)
        queue_app.ensure_data_file()

        # Reset cache if it exists (for future compatibility)
        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None
        if hasattr(queue_app, '_CACHE_MTIME'):
            queue_app._CACHE_MTIME = 0

    def test_add_and_load(self):
        """Test adding a person and retrieving the data."""
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry["name"], "Alice")
        self.assertEqual(entry["id"], 1)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Alice")
        self.assertEqual(data["next_id"], 2)

    def test_call_next(self):
        """Test calling the next person in the queue."""
        queue_app.add_person("Bob")
        queue_app.add_person("Charlie")

        # Call Bob
        called = queue_app.call_next()
        self.assertEqual(called["name"], "Bob")
        self.assertEqual(called["id"], 1)

        # Verify Bob is in history and Charlie is in queue
        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Charlie")
        self.assertEqual(len(data["history"]), 1)
        self.assertEqual(data["history"][0]["name"], "Bob")

    def test_persistence(self):
        """Test that data persists across 'sessions' (loading from disk)."""
        queue_app.add_person("Dave")

        # Force a reload from disk (simulated by clearing cache if it existed,
        # but here we rely on load_data doing the right thing)
        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Dave")

    def test_empty_queue(self):
        """Test calling next on empty queue."""
        result = queue_app.call_next()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
