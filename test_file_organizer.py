"""
Test script for File Organizer
Creates sample files to demonstrate the organizer functionality
"""

import os
import shutil
from pathlib import Path

def create_test_files():
    """Create sample test files for demonstration"""
    test_dir = "test_files"
    
    # Create test directory
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        print(f"Created test directory: {test_dir}")
    
    # Create sample files of different types
    test_files = [
        "document.pdf",
        "report.docx",
        "spreadsheet.xlsx",
        "photo.jpg",
        "image.png",
        "video.mp4",
        "music.mp3",
        "archive.zip",
        "script.py",
        "webpage.html",
        "stylesheet.css",
        "readme.txt",
        "program.exe"
    ]
    
    created_count = 0
    for file in test_files:
        file_path = os.path.join(test_dir, file)
        with open(file_path, 'w') as f:
            f.write(f"This is a sample {file} file for testing.")
        created_count += 1
        print(f"Created: {file}")
    
    print(f"\nCreated {created_count} test files in '{test_dir}' directory")
    return test_dir

def run_demo():
    """Run a demonstration of the file organizer"""
    print("=" * 60)
    print("FILE ORGANIZER DEMONSTRATION")
    print("=" * 60)
    
    # Create test files
    test_dir = create_test_files()
    
    print("\n" + "=" * 60)
    print("ORIGINAL FILE STRUCTURE:")
    print("=" * 60)
    
    # Show original files
    files = os.listdir(test_dir)
    for file in files:
        print(f"  {file}")
    
    print(f"\nTotal files: {len(files)}")
    
    print("\n" + "=" * 60)
    print("RUNNING FILE ORGANIZER...")
    print("=" * 60)
    
    # Change to test directory and run organizer
    original_dir = os.getcwd()
    os.chdir(test_dir)
    
    # Import and run the organizer
    import file_organizer
    
    # Show organized structure
    print("\n" + "=" * 60)
    print("ORGANIZED FILE STRUCTURE:")
    print("=" * 60)
    
    organized_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            rel_path = os.path.join(root, file)
            organized_files.append(rel_path)
    
    for file in sorted(organized_files):
        print(f"  {file}")
    
    print(f"\nTotal organized files: {len(organized_files)}")
    
    # Return to original directory
    os.chdir(original_dir)
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 60)
    print(f"Test files created in: {test_dir}")
    print("You can now run 'python file_organizer.py' to organize your own files!")

if __name__ == "__main__":
    run_demo()
