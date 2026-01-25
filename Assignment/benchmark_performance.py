import time
import queue_app
import os
import shutil

def benchmark():
    print("Preparing benchmark...")
    # Setup
    queue_app.ensure_data_file()
    # Fill with some data
    data = {"next_id": 1, "queue": [], "history": []}
    for i in range(1000):
        data["queue"].append({"id": i, "name": f"Person {i}", "joined_at": queue_app.now_utc_iso()})
    queue_app.save_data(data)

    print("Running benchmark...")
    start_time = time.time()
    iterations = 2000
    for _ in range(iterations):
        # calling load_data explicitly to measure read performance
        _ = queue_app.load_data()
    end_time = time.time()

    duration = end_time - start_time
    print(f"Time for {iterations} load_data calls: {duration:.4f} seconds")
    print(f"Average time per call: {duration / iterations:.6f} seconds")

if __name__ == "__main__":
    benchmark()
