#!/bin/bash
# Interactive Bash Practice Script

echo "=== Bash Tutorial Practice ==="
echo "This script will help you practice basic bash commands"
echo ""

# Create practice directory
PRACTICE_DIR="bash_practice_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$PRACTICE_DIR"
cd "$PRACTICE_DIR"

echo "Created practice directory: $PRACTICE_DIR"
echo ""

# Exercise 1: File creation
echo "Exercise 1: Creating files"
touch file1.txt file2.txt file3.txt
echo "Hello World" > file1.txt
echo "Bash is awesome" >> file1.txt
echo "Created 3 files and added content to file1.txt"

# Exercise 2: Directory operations
echo ""
echo "Exercise 2: Directory operations"
mkdir -p dir1/subdir
cp file1.txt dir1/
mv file2.txt dir1/renamed.txt
echo "Created directory structure and moved files"

# Exercise 3: Viewing content
echo ""
echo "Exercise 3: File content"
echo "Contents of file1.txt:"
cat file1.txt

# Exercise 4: Search operations
echo ""
echo "Exercise 4: Search operations"
echo "Files containing 'Hello':"
grep -r "Hello" .

# Exercise 5: Permissions
echo ""
echo "Exercise 5: Permissions"
chmod +x file3.txt
ls -la file3.txt

# Cleanup instructions
echo ""
echo "=== Practice Complete ==="
echo "Your practice files are in: $(pwd)"
echo "To clean up when done: rm -rf $PRACTICE_DIR"
echo ""
echo "Next steps:"
echo "1. Try the commands from the tutorial"
echo "2. Create your own bash scripts"
echo "3. Explore man pages: man ls, man grep, etc."
