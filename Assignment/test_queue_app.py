import unittest
import os
import json
import shutil
import tempfile
from datetime import datetime, timezone
import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for data
        self.test_dir = tempfile.mkdtemp()
        self.original_data_dir = queue_app.DATA_DIR
        self.original_data_file = queue_app.DATA_FILE

        queue_app.DATA_DIR = self.test_dir
        queue_app.DATA_FILE = os.path.join(self.test_dir, "queue.json")

        # Reset cache if we implement it later, for now just ensure clean state
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = {}

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        queue_app.DATA_DIR = self.original_data_dir
        queue_app.DATA_FILE = self.original_data_file
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = {}

    def test_ensure_data_file(self):
        queue_app.ensure_data_file()
        self.assertTrue(os.path.exists(queue_app.DATA_FILE))
        with open(queue_app.DATA_FILE, 'r') as f:
            data = json.load(f)
        self.assertEqual(data['next_id'], 1)
        self.assertEqual(data['queue'], [])

    def test_add_person(self):
        entry = queue_app.add_person("Alice")
        self.assertEqual(entry['id'], 1)
        self.assertEqual(entry['name'], "Alice")

        data = queue_app.load_data()
        self.assertEqual(len(data['queue']), 1)
        self.assertEqual(data['queue'][0]['name'], "Alice")
        self.assertEqual(data['next_id'], 2)

    def test_call_next(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")

        person = queue_app.call_next()
        self.assertEqual(person['name'], "Alice")
        self.assertIn("called_at", person)

        data = queue_app.load_data()
        self.assertEqual(len(data['queue']), 1)
        self.assertEqual(data['queue'][0]['name'], "Bob")
        self.assertEqual(len(data['history']), 1)
        self.assertEqual(data['history'][0]['name'], "Alice")

    def test_get_position(self):
        p1 = queue_app.add_person("Alice")
        p2 = queue_app.add_person("Bob")

        self.assertEqual(queue_app.get_position(p1['id']), 1)
        self.assertEqual(queue_app.get_position(p2['id']), 2)

        queue_app.call_next()
        self.assertEqual(queue_app.get_position(p1['id']), None)
        self.assertEqual(queue_app.get_position(p2['id']), 1)

    def test_find_person(self):
        queue_app.add_person("Alice")
        queue_app.add_person("Bob")
        queue_app.call_next() # Alice called

        # Find by name
        res = queue_app.find_person("Alice")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['name'], "Alice")
        self.assertEqual(res[0]['status'], "called")

        res = queue_app.find_person("Bob")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['name'], "Bob")
        self.assertEqual(res[0]['status'], "waiting")

        # Find by ID
        res = queue_app.find_person("1")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['name'], "Alice")

if __name__ == '__main__':
    unittest.main()
