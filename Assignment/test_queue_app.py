import unittest
import os
import shutil
import json
from unittest.mock import patch, MagicMock
# Adjusting path to import queue_app
import sys
sys.path.append(os.path.join(os.getcwd(), 'Assignment'))
import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Use a temporary file for testing
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_data")
        self.test_file = os.path.join(self.test_dir, "queue.json")

        # Patch the constants in queue_app
        self.orig_data_dir = queue_app.DATA_DIR
        self.orig_data_file = queue_app.DATA_FILE

        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = self.test_file

        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        queue_app.DATA_DIR = self.orig_data_dir
        queue_app.DATA_FILE = self.orig_data_file

        # Reset internal state if we introduce any global variables
        if hasattr(queue_app, "_CACHE"):
             queue_app._CACHE = None
        if hasattr(queue_app, "_LAST_MTIME"):
             queue_app._LAST_MTIME = 0

    def test_ensure_data_file(self):
        queue_app.ensure_data_file()
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['next_id'], 1)

    def test_add_person(self):
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry['name'], "Alice")
        self.assertEqual(entry['id'], 1)

        data = queue_app.load_data()
        self.assertEqual(len(data['queue']), 1)
        self.assertEqual(data['queue'][0]['name'], "Alice")

    def test_call_next(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")

        person = queue_app.call_next()
        self.assertEqual(person['name'], "Alice")

        data = queue_app.load_data()
        self.assertEqual(len(data['queue']), 1)
        self.assertEqual(data['queue'][0]['name'], "Bob")
        self.assertEqual(len(data['history']), 1)
        self.assertEqual(data['history'][0]['name'], "Alice")

    def test_persistence_across_loads(self):
        queue_app.add_person("Charlie")
        # Modify file manually to simulate external change if we weren't mocking constants?
        # Here we just want to ensure load_data reads what was saved.
        data = queue_app.load_data()
        self.assertEqual(data['queue'][0]['name'], "Charlie")

    def test_file_modification_detection(self):
        # This test is specifically to verify that if I modify the file "externally",
        # the app picks it up (which is the current behavior, and should be preserved or handled).
        queue_app.add_person("David")

        # Ensure mtime resolution is respected.
        # If the file system has low resolution, fast writes might end up with same mtime.
        # We can force a newer mtime using os.utime

        # Simulate external modification
        with open(self.test_file, 'r') as f:
            content = json.load(f)

        content['queue'][0]['name'] = "Davide"

        with open(self.test_file, 'w') as f:
            json.dump(content, f)
            f.flush()
            os.fsync(f.fileno())

        # Force the mtime to be definitely strictly greater than what might be cached
        # We need to know what was cached? No, we just need to make sure the file's mtime is distinct.
        # But queue_app saved it just now.
        # Let's just update the mtime of the file to be +1 second from now.
        stat = os.stat(self.test_file)
        new_mtime = stat.st_mtime + 1.0
        os.utime(self.test_file, (stat.st_atime, new_mtime))

        # Re-load
        data = queue_app.load_data()
        self.assertEqual(data['queue'][0]['name'], "Davide")

if __name__ == '__main__':
    unittest.main()
