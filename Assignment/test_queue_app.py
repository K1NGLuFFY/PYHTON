import unittest
from unittest.mock import patch
import os
import json
import queue_app

class TestQueueAppPerformance(unittest.TestCase):
    def setUp(self):
        self.original_data_file = queue_app.DATA_FILE
        queue_app.DATA_FILE = "test_queue_repro.json"
        # Create a dummy file
        with open(queue_app.DATA_FILE, "w") as f:
            json.dump({"next_id": 1, "queue": [], "history": []}, f)

        # Reset any potential cache (future proofing)
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def tearDown(self):
        if os.path.exists(queue_app.DATA_FILE):
            os.remove(queue_app.DATA_FILE)
        queue_app.DATA_FILE = self.original_data_file
        if hasattr(queue_app, "_CACHE"):
            queue_app._CACHE = None
            queue_app._CACHE_MTIME = 0

    def test_load_data_frequency(self):
        # We wrap json.load to count calls
        real_json_load = json.load

        with patch("json.load", side_effect=real_json_load) as mock_load:
            # 1. Call load_data multiple times
            queue_app.load_data()
            queue_app.load_data()
            queue_app.load_data()

            self.assertEqual(mock_load.call_count, 1)

    def test_cache_invalidation(self):
        queue_app.load_data()

        # Modify file externally
        with open(queue_app.DATA_FILE, "w") as f:
            json.dump({"next_id": 999, "queue": [], "history": []}, f)

        # Force mtime update
        st = os.stat(queue_app.DATA_FILE)
        os.utime(queue_app.DATA_FILE, (st.st_atime, st.st_mtime + 2))

        data = queue_app.load_data()
        self.assertEqual(data["next_id"], 999)

if __name__ == '__main__':
    unittest.main()
