import unittest
import os
import json
import sys
import shutil
from unittest.mock import patch, mock_open, MagicMock

# Add Assignment directory to path to import queue_app
sys.path.append(os.path.join(os.path.dirname(__file__), "."))

import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Use a temporary directory for data
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_data")
        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = os.path.join(self.test_dir, "queue.json")

        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)

        # Initialize default data
        with open(queue_app.DATA_FILE, "w") as f:
            json.dump({"next_id": 1, "queue": [], "history": []}, f)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_add_person_file_ops(self):
        # We want to count how many times open() is called
        with patch("builtins.open", wraps=open) as mock_file:
            queue_app.add_person("Alice")
            # add_person calls load_data (read) and save_data (write)
            # It implies at least 2 opens
            print(f"add_person opens: {mock_file.call_count}")
            self.assertGreaterEqual(mock_file.call_count, 2)
            initial_count = mock_file.call_count

            # Now call get_position, which should hit the cache!
            queue_app.get_position(1)
            # Should add 0 reads
            print(f"get_position opens: {mock_file.call_count - initial_count}")
            self.assertEqual(mock_file.call_count, initial_count)

    def test_find_person_file_ops(self):
        queue_app.add_person("Bob")
        with patch("builtins.open", wraps=open) as mock_file:
            results = queue_app.find_person("Bob")
            # find_person should hit cache (populated by add_person)
            print(f"find_person opens: {mock_file.call_count}")
            self.assertEqual(mock_file.call_count, 0)

            # print_person_results should also hit cache
            with patch("builtins.print"):
                queue_app.print_person_results(results)

            print(f"print_person_results opens: {mock_file.call_count}")
            self.assertEqual(mock_file.call_count, 0)

    def test_functionality_preserved(self):
        # Verify basic functionality
        entry = queue_app.add_person("Charlie")
        self.assertEqual(entry["name"], "Charlie")
        self.assertEqual(entry["id"], 1)

        pos = queue_app.get_position(1)
        self.assertEqual(pos, 1)

        entry2 = queue_app.add_person("Dave")
        self.assertEqual(entry2["id"], 2)

        called = queue_app.call_next()
        self.assertEqual(called["name"], "Charlie")

        pos2 = queue_app.get_position(2)
        self.assertEqual(pos2, 1) # Dave moved up

if __name__ == "__main__":
    unittest.main()
