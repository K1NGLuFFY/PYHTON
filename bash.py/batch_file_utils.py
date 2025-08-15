"""
Simple Batch File Operations Utility
==================================

This module provides easy-to-use functions for common batch file operations.
"""

import os
import glob
import shutil
from pathlib import Path
from typing import List, Callable, Optional

def batch_rename_files(directory: str, prefix: str = "", suffix: str = "", 
                      extension: str = None) -> List[str]:
    """
    Rename multiple files in a directory with prefix/suffix.
    
    Args:
        directory: Directory containing files
        prefix: Prefix to add to filenames
        suffix: Suffix to add to filenames (before extension)
        extension: Filter by file extension (e.g., '.txt')
    
    Returns:
        List of new filenames
    """
    path = Path(directory)
    pattern = f"*{extension}" if extension else "*"
    files = list(path.glob(pattern))
    
    renamed = []
    for file_path in files:
        if file_path.is_file():
            name = file_path.stem
            new_name = f"{prefix}{name}{suffix}{file_path.suffix}"
            new_path = file_path.parent / new_name
            file_path.rename(new_path)
            renamed.append(new_name)
    
    return renamed

def batch_copy_files(source_pattern: str, dest_dir: str) -> List[str]:
    """
    Copy files matching a pattern to destination directory.
    
    Args:
        source_pattern: Glob pattern (e.g., "*.txt" or "data/*.csv")
        dest_dir: Destination directory
    
    Returns:
        List of copied file paths
    """
    files = glob.glob(source_pattern)
    os.makedirs(dest_dir, exist_ok=True)
    
    copied = []
    for file_path in files:
        if os.path.isfile(file_path):
            dest_path = os.path.join(dest_dir, os.path.basename(file_path))
            shutil.copy2(file_path, dest_path)
            copied.append(dest_path)
    
    return copied

def batch_delete_files(pattern: str, confirm: bool = True) -> List[str]:
    """
    Delete files matching a pattern.
    
    Args:
        pattern: Glob pattern for files to delete
        confirm: Ask for confirmation before deletion
    
    Returns:
        List of deleted file paths
    """
    files = glob.glob(pattern)
    
    if confirm:
        print(f"About to delete {len(files)} files:")
        for f in files:
            print(f"  {f}")
        response = input("Proceed? (y/n): ")
        if response.lower() != 'y':
            return []
    
    deleted = []
    for file_path in files:
        if os.path.isfile(file_path):
            os.remove(file_path)
            deleted.append(file_path)
    
    return deleted

def batch_process_files_with_callback(directory: str, callback: Callable[[str], None],
                                   extension: str = None) -> None:
    """
    Process all files in a directory with a callback function.
    
    Args:
        directory: Directory to process
        callback: Function to call for each file
        extension: Filter by file extension
    """
    path = Path(directory)
    pattern = f"*{extension}" if extension else "*"
    
    for file_path in path.glob(pattern):
        if file_path.is_file():
            callback(str(file_path))

def create_sample_files(directory: str, count: int = 10) -> List[str]:
    """Create sample files for testing."""
    os.makedirs(directory, exist_ok=True)
    
    created = []
    for i in range(count):
        file_path = os.path.join(directory, f"sample_{i}.txt")
        with open(file_path, 'w') as f:
            f.write(f"This is sample file {i}")
        created.append(file_path)
    
    return created

# Example usage
if __name__ == "__main__":
    # Create sample files
    sample_dir = "batch_test"
    files = create_sample_files(sample_dir, 5)
    print(f"Created {len(files)} sample files")
    
    # Rename files
    renamed = batch_rename_files(sample_dir, prefix="new_", suffix="_updated")
    print(f"Renamed {len(renamed)} files")
    
    # Copy files
    copied = batch_copy_files(f"{sample_dir}/*.txt", "batch_test_backup")
    print(f"Copied {len(copied)} files to backup")
    
    # Clean up
    import shutil
    shutil.rmtree(sample_dir)
    shutil.rmtree("batch_test_backup")
    print("Cleanup completed")
