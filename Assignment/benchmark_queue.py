
import time
import os
import sys
import unittest.mock
from contextlib import contextmanager

# Add current directory to path so we can import queue_app
sys.path.append(os.path.dirname(__file__))

import queue_app

@contextmanager
def count_file_opens():
    open_count = 0
    original_open = open

    def mocked_open(*args, **kwargs):
        nonlocal open_count
        # Only count opens for the data file
        if args and isinstance(args[0], str) and "queue.json" in args[0]:
            open_count += 1
        return original_open(*args, **kwargs)

    with unittest.mock.patch('builtins.open', side_effect=mocked_open):
        yield lambda: open_count

def run_benchmark():
    # Ensure data file exists
    queue_app.ensure_data_file()

    print("Running benchmark...")

    # 1. Measure read performance (view_queue)
    iterations = 1000
    start_time = time.time()

    with count_file_opens() as get_open_count:
        for _ in range(iterations):
            queue_app.load_data()

        duration = time.time() - start_time
        opens = get_open_count()

    print(f"Read Benchmark ({iterations} iterations):")
    print(f"  Time: {duration:.4f} seconds")
    print(f"  File Opens: {opens}")
    print(f"  Avg Time/Op: {duration/iterations*1000:.4f} ms")

if __name__ == "__main__":
    run_benchmark()
