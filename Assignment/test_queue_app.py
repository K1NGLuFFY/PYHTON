import unittest
import os
import sys
import json
import shutil

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Backup existing data if any
        self.original_data = None
        if os.path.exists(queue_app.DATA_FILE):
            with open(queue_app.DATA_FILE, 'r') as f:
                self.original_data = f.read()

        # Reset data
        queue_app.reset_all(confirm=True)

    def tearDown(self):
        # Restore data
        if self.original_data:
            with open(queue_app.DATA_FILE, 'w') as f:
                f.write(self.original_data)
        else:
            if os.path.exists(queue_app.DATA_FILE):
                os.remove(queue_app.DATA_FILE)

    def test_add_person(self):
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry["name"], "Alice")
        self.assertEqual(entry["id"], 1)

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Alice")

    def test_call_next(self):
        queue_app.add_person("Bob")
        queue_app.add_person("Charlie")

        called = queue_app.call_next()
        self.assertEqual(called["name"], "Bob")

        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Charlie")
        self.assertEqual(len(data["history"]), 1)
        self.assertEqual(data["history"][0]["name"], "Bob")

    def test_get_position(self):
        p1 = queue_app.add_person("Dave")
        p2 = queue_app.add_person("Eve")

        pos1 = queue_app.get_position(p1["id"])
        pos2 = queue_app.get_position(p2["id"])

        self.assertEqual(pos1, 1)
        self.assertEqual(pos2, 2)

        queue_app.call_next()
        pos2_new = queue_app.get_position(p2["id"])
        self.assertEqual(pos2_new, 1)

    def test_find_person(self):
        queue_app.add_person("Frank")
        results = queue_app.find_person("Frank")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Frank")
        self.assertEqual(results[0]["status"], "waiting")

        queue_app.call_next()
        results = queue_app.find_person("Frank")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["status"], "called")

if __name__ == '__main__':
    unittest.main()
