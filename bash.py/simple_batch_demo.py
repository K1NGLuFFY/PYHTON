"""
Simple Batch Processing Demo
===========================

A simple demonstration of batch processing concepts.
"""

import time
import random

def simple_batch_demo():
    """Demonstrate basic batch processing concepts."""
    
    # Sample data
    numbers = list(range(1, 101))
    print(f"Processing {len(numbers)} numbers in batches...")
    
    # Process in batches of 10
    batch_size = 10
    results = []
    
    for i in range(0, len(numbers), batch_size):
        batch = numbers[i:i + batch_size]
        
        # Simulate processing time
        print(f"Processing batch: {batch}")
        time.sleep(0.1)  # Simulate work
        
        # Process the batch (square each number)
        processed = [x * x for x in batch]
        results.extend(processed)
        
        print(f"  Result: {processed}")
    
    print(f"\nTotal processed: {len(results)}")
    print(f"Sum of squares: {sum(results)}")
    
    return results

def batch_with_progress(items: list, batch_size: int = 5):
    """Process items with progress tracking."""
    
    total = len(items)
    processed = 0
    
    for i in range(0, total, batch_size):
        batch = items[i:i + batch_size]
        
        # Process batch
        for item in batch:
            print(f"Processing: {item}")
            time.sleep(0.1)
        
        processed += len(batch)
        progress = (processed / total) * 100
        print(f"Progress: {progress:.1f}% ({processed}/{total})\n")

if __name__ == "__main__":
    print("=== Simple Batch Demo ===")
    simple_batch_demo()
    
    print("\n=== Batch with Progress ===")
    items = [f"task_{i}" for i in range(1, 11)]
    batch_with_progress(items, batch_size=3)
