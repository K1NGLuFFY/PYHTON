import unittest
import queue_app
import os
import json
import shutil

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Use a temporary file for testing
        self.original_data_file = queue_app.DATA_FILE
        self.test_data_dir = os.path.join(queue_app.DATA_DIR, "test_data")
        os.makedirs(self.test_data_dir, exist_ok=True)
        queue_app.DATA_FILE = os.path.join(self.test_data_dir, "test_queue.json")

        # Ensure clean state
        if os.path.exists(queue_app.DATA_FILE):
            os.remove(queue_app.DATA_FILE)

    def tearDown(self):
        if os.path.exists(queue_app.DATA_FILE):
            os.remove(queue_app.DATA_FILE)
        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)
        queue_app.DATA_FILE = self.original_data_file

    def test_add_person(self):
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry["name"], "Alice")
        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Alice")

    def test_call_next(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")
        called = queue_app.call_next()
        self.assertEqual(called["name"], "Alice")
        data = queue_app.load_data()
        self.assertEqual(len(data["queue"]), 1)
        self.assertEqual(data["queue"][0]["name"], "Bob")
        self.assertEqual(len(data["history"]), 1)

    def test_get_position(self):
        p1 = queue_app.add_person("P1")
        p2 = queue_app.add_person("P2")
        self.assertEqual(queue_app.get_position(p1["id"]), 1)
        self.assertEqual(queue_app.get_position(p2["id"]), 2)
        queue_app.call_next()
        self.assertEqual(queue_app.get_position(p1["id"]), None)
        self.assertEqual(queue_app.get_position(p2["id"]), 1)

    def test_find_person(self):
        p1 = queue_app.add_person("UniqueName")
        results = queue_app.find_person("UniqueName")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], p1["id"])

        results_id = queue_app.find_person(str(p1["id"]))
        self.assertEqual(len(results_id), 1)
        self.assertEqual(results_id[0]["name"], "UniqueName")

if __name__ == "__main__":
    unittest.main()
