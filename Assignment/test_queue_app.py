import unittest
import os
import shutil
import tempfile
import json
from unittest import mock
import sys

# Ensure we can import the module
sys.path.append(os.path.dirname(__file__))
import queue_app

class TestQueueApp(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "queue.json")

        # Patch the constants in the module
        self.patcher_dir = mock.patch('queue_app.DATA_DIR', self.test_dir)
        self.patcher_file = mock.patch('queue_app.DATA_FILE', self.test_file)

        self.patcher_dir.start()
        self.patcher_file.start()

        # Reset any global state if necessary (none currently, but good practice)
        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def tearDown(self):
        self.patcher_file.stop()
        self.patcher_dir.stop()
        shutil.rmtree(self.test_dir)

        if hasattr(queue_app, '_CACHE'):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def test_ensure_data_file(self):
        queue_app.ensure_data_file()
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
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

        called = queue_app.call_next()
        self.assertEqual(called['name'], "Alice")
        self.assertIn('called_at', called)

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
        self.assertEqual(queue_app.get_position(p1['id']), None) # Alice is in history
        self.assertEqual(queue_app.get_position(p2['id']), 1)

    def test_find_person(self):
        p1 = queue_app.add_person("Alice")
        p2 = queue_app.add_person("Bob")
        queue_app.call_next() # Alice called

        # Find by ID
        res = queue_app.find_person(str(p1['id']))
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['name'], "Alice")
        self.assertEqual(res[0]['status'], "called")

        res = queue_app.find_person(str(p2['id']))
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['name'], "Bob")
        self.assertEqual(res[0]['status'], "waiting")

        # Find by Name
        res = queue_app.find_person("alice")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['name'], "Alice")

if __name__ == '__main__':
    unittest.main()
