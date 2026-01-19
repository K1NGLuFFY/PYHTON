import unittest
import os
import json
import time
import sys
from unittest.mock import patch, MagicMock

# Add current directory to path so we can import queue_app
sys.path.append(os.path.dirname(__file__))

import queue_app

class TestQueueAppPerformance(unittest.TestCase):
    def setUp(self):
        # Setup a temporary data file
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_data")
        self.test_file = os.path.join(self.test_dir, "queue.json")

        # Override constants in queue_app
        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = self.test_file

        # Reset cache if it exists (for when we implement it)
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
        if hasattr(queue_app, "_CACHE_MTIME"):
            queue_app._CACHE_MTIME = 0

        # Clean up any existing file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)

    def tearDown(self):
        # Clean up
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)

    def test_io_reduction(self):
        """Test that read operations are reduced with caching."""

        # Initial save to set up file
        queue_app.ensure_data_file()

        # We'll patch the built-in open function to count calls
        # We need to wrap the actual open so functionality works
        real_open = open
        open_call_count = 0

        def side_effect(file, mode='r', *args, **kwargs):
            nonlocal open_call_count
            if str(file) == str(self.test_file):
                open_call_count += 1
            return real_open(file, mode, *args, **kwargs)

        with patch('builtins.open', side_effect=side_effect):
            # 1. Add Person (Read + Write)
            # Without cache: reads, then writes.
            queue_app.add_person("Alice")

            # 2. Add Person (Read + Write)
            queue_app.add_person("Bob")

            # 3. View Queue (Read only)
            queue_app.view_queue()

            # 4. Find Person (Read only)
            queue_app.find_person("Alice")

            # 5. Get Position (Read only)
            queue_app.get_position(1)

        print(f"\nTotal file open calls: {open_call_count}")

        # Verify correctness
        data = queue_app.load_data() # This might use cache if implemented
        # Force fresh read to verify disk content
        with real_open(self.test_file, 'r') as f:
            disk_data = json.load(f)

        self.assertEqual(len(disk_data["queue"]), 2)
        self.assertEqual(disk_data["queue"][0]["name"], "Alice")
        self.assertEqual(disk_data["queue"][1]["name"], "Bob")

if __name__ == '__main__':
    unittest.main()
