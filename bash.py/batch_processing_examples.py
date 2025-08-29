"""
Comprehensive Batch Processing Examples in Python
==============================================

This file demonstrates various batch processing techniques in Python,
including file processing, data batching, and batch operations.
"""

import os
import csv
import json
import time
from typing import List, Iterator, Any
import concurrent.futures
from pathlib import Path

# ============================================
# 1. BATCH FILE PROCESSING
# ============================================

def batch_process_files(directory: str, batch_size: int = 10) -> Iterator[List[str]]:
    """
    Process files in batches from a directory.
    
    Args:
        directory: Path to directory containing files
        batch_size: Number of files to process at once
    
    Yields:
        List of file paths in batches
    """
    
    files = [os.path.join(directory, f) for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f))]
    
    for i in range(0, len(files), batch_size):
        yield files[i:i + batch_size]

def process_file_batch(file_list: List[str]) -> None:
    """Process a batch of files."""
    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Processed: {file_path} ({len(content)} chars)")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# ============================================
# 2. BATCH DATA PROCESSING
# ============================================

def batch_iterator(data: List[Any], batch_size: int) -> Iterator[List[Any]]:
    """
    Create batches from a list of data.
    
    Args:
        data: List of items to batch
        batch_size: Size of each batch
    
    Yields:
        List of items in batches
    """
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

def process_data_batch(batch: List[Any]) -> List[Any]:
    """Process a batch of data (example transformation)."""
    return [item.upper() if isinstance(item, str) else item * 2 
            for item in batch]

# ============================================
# 3. CSV BATCH PROCESSING
# ============================================

def process_csv_in_batches(csv_file: str, batch_size: int = 1000) -> Iterator[List[dict]]:
    """
    Process CSV files in batches to handle large files efficiently.
    
    Args:
        csv_file: Path to CSV file
        batch_size: Number of rows per batch
    
    Yields:
        List of dictionaries (rows) in batches
    """
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        batch = []
        
        for row in reader:
            batch.append(row)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        
        if batch:  # Yield remaining rows
            yield batch

def transform_csv_batch(batch: List[dict]) -> List[dict]:
    """Transform a batch of CSV data."""
    transformed = []
    for row in batch:
        # Example transformation
        if 'price' in row:
            row['price_float'] = float(row['price'])
        transformed.append(row)
    return transformed

# ============================================
# 4. PARALLEL BATCH PROCESSING
# ============================================

def parallel_batch_process(data: List[Any], batch_size: int = 100, 
                          max_workers: int = 4) -> List[Any]:
    """
    Process batches in parallel using ThreadPoolExecutor.
    
    Args:
        data: List of items to process
        batch_size: Size of each batch
        max_workers: Number of parallel workers
    
    Returns:
        List of processed results
    """
    batches = list(batch_iterator(data, batch_size))
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_batch = {executor.submit(process_data_batch, batch): batch 
                          for batch in batches}
        
        for future in concurrent.futures.as_completed(future_to_batch):
            try:
                result = future.result()
                results.extend(result)
            except Exception as e:
                print(f"Error processing batch: {e}")
    
    return results

# ============================================
# 5. DATABASE BATCH OPERATIONS
# ============================================

class BatchDatabaseProcessor:
    """Simulate database batch operations."""
    
    def __init__(self, connection_string: str = "sqlite:///:memory:"):
        self.connection_string = connection_string
    
    def batch_insert(self, data: List[dict], table_name: str) -> None:
        """Insert data in batches to avoid memory issues."""
        batch_size = 1000
        
        for batch in batch_iterator(data, batch_size):
            # Simulate database insert
            print(f"Inserting batch of {len(batch)} records into {table_name}")
            # In real implementation, use SQLAlchemy or similar
    
    def batch_update(self, updates: List[dict], table_name: str) -> None:
        """Update records in batches."""
        batch_size = 500
        
        for batch in batch_iterator(updates, batch_size):
            print(f"Updating batch of {len(batch)} records in {table_name}")
            # In real implementation, use parameterized queries

# ============================================
# 6. ASYNCHRONOUS BATCH PROCESSING
# ============================================

import asyncio
import aiohttp
import aiofiles

async def async_batch_http_requests(urls: List[str], batch_size: int = 10) -> List[str]:
    """
    Process HTTP requests in batches asynchronously.
    
    Args:
        urls: List of URLs to fetch
        batch_size: Number of concurrent requests
    
    Returns:
        List of response contents
    """
    results = []
    
    async with aiohttp.ClientSession() as session:
        for batch in batch_iterator(urls, batch_size):
            tasks = [fetch_url_async(session, url) for url in batch]
            batch_results = await asyncio.gather(*tasks)
            results.extend(batch_results)
    
    return results

async def fetch_url_async(session: aiohttp.ClientSession, url: str) -> str:
    """Fetch a single URL asynchronously."""
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error: {e}"

# ============================================
# 7. MEMORY-EFFICIENT BATCH PROCESSING
# ============================================

class LargeFileProcessor:
    """Process large files without loading everything into memory."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def process_line_by_line(self, processor_func) -> None:
        """Process file line by line to save memory."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                processor_func(line.strip())
    
    def process_in_chunks(self, chunk_size: int = 8192) -> Iterator[str]:
        """Process file in chunks."""
        with open(self.file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk.decode('utf-8', errors='ignore')

# ============================================
# 8. MONITORING AND PROGRESS TRACKING
# ============================================

class BatchProcessorWithProgress:
    """Batch processor with progress tracking."""
    
    def __init__(self, total_items: int):
        self.total_items = total_items
        self.processed = 0
    
    def process_with_progress(self, data: List[Any], batch_size: int) -> List[Any]:
        """Process batches with progress updates."""
        results = []
        
        for batch in batch_iterator(data, batch_size):
            batch_result = process_data_batch(batch)
            results.extend(batch_result)
            
            self.processed += len(batch)
            progress = (self.processed / self.total_items) * 100
            print(f"Progress: {progress:.1f}% ({self.processed}/{self.total_items})")
        
        return results

# ============================================
# 9. ERROR HANDLING IN BATCHES
# ============================================

def robust_batch_process(data: List[Any], batch_size: int = 100) -> dict:
    """
    Process batches with comprehensive error handling.
    
    Returns:
        Dictionary with results, errors, and statistics
    """
    results = []
    errors = []
    stats = {"total": len(data), "processed": 0, "failed": 0}
    
    for batch_num, batch in enumerate(batch_iterator(data, batch_size)):
        try:
            batch_result = process_data_batch(batch)
            results.extend(batch_result)
            stats["processed"] += len(batch)
        except Exception as e:
            error_info = {
                "batch_number": batch_num,
                "batch_size": len(batch),
                "error": str(e),
                "items": batch
            }
            errors.append(error_info)
            stats["failed"] += len(batch)
    
    return {
        "results": results,
        "errors": errors,
        "statistics": stats
    }

# ============================================
# 10. USAGE EXAMPLES
# ============================================

def demonstrate_batch_processing():
    """Demonstrate various batch processing techniques."""
    
    print("=== Batch File Processing ===")
    # Create sample files
    sample_dir = "sample_files"
    os.makedirs(sample_dir, exist_ok=True)
    
    for i in range(15):
        with open(f"{sample_dir}/file_{i}.txt", 'w') as f:
            f.write(f"Content of file {i}")
    
    # Process files in batches
    for batch in batch_process_files(sample_dir, batch_size=5):
        process_file_batch(batch)
    
    # Cleanup
    import shutil
    shutil.rmtree(sample_dir)
    
    print("\n=== Data Batch Processing ===")
    data = [f"item_{i}" for i in range(20)]
    batches = list(batch_iterator(data, batch_size=4))
    print(f"Created {len(batches)} batches from {len(data)} items")
    
    print("\n=== Parallel Processing ===")
    start_time = time.time()
    results = parallel_batch_process(data, batch_size=5, max_workers=2)
    end_time = time.time()
    print(f"Parallel processing took {end_time - start_time:.2f} seconds")
    
    print("\n=== Robust Processing ===")
    # Include some invalid data
    mixed_data = ["valid", 123, "another", None, "test"]
    result = robust_batch_process(mixed_data, batch_size=2)
    print(f"Results: {len(result['results'])}")
    print(f"Errors: {len(result['errors'])}")
    print(f"Stats: {result['statistics']}")

if __name__ == "__main__":
    demonstrate_batch_processing()
