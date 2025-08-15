# Bash Tutorial: From Beginner to Intermediate

## 1. What is Bash?
Bash (Bourne Again Shell) is a command-line interface and scripting language used in Unix-like systems. It's the default shell on most Linux distributions and macOS.

## 2. Getting Started

### Opening a Terminal
- **Windows**: Use Git Bash, WSL, or PowerShell
- **macOS**: Open Terminal app
- **Linux**: Use Ctrl+Alt+T or search for "Terminal"

### Basic Navigation

#### pwd - Print Working Directory
```bash
pwd
```
Shows your current location in the file system.

#### ls - List Files
```bash
ls              # Basic listing
ls -l           # Detailed listing
ls -la          # All files including hidden ones
ls -lh          # Human-readable file sizes
```

#### cd - Change Directory
```bash
cd /path/to/directory    # Absolute path
cd ./relative/path       # Relative path
cd ~                     # Home directory
cd ..                    # Go up one level
cd -                     # Go to previous directory
```

## 3. File and Directory Operations

### Creating Files and Directories
```bash
touch filename.txt       # Create empty file
mkdir new_directory      # Create directory
mkdir -p path/to/nested  # Create nested directories
```

### Copying and Moving
```bash
cp source.txt destination.txt     # Copy file
cp -r source_dir/ dest_dir/       # Copy directory recursively
mv old_name.txt new_name.txt      # Move/rename
```

### Deleting
```bash
rm file.txt              # Delete file
rm -r directory/         # Delete directory recursively
rm -f file.txt           # Force delete without confirmation
```

## 4. File Content Commands

### Viewing File Contents
```bash
cat file.txt             # Display entire file
less file.txt            # View file with scrolling (q to quit)
head file.txt            # First 10 lines
tail file.txt            # Last 10 lines
head -n 20 file.txt      # First 20 lines
tail -f log.txt          # Follow file updates in real-time
```

### Searching in Files
```bash
grep "search_term" file.txt              # Search for text
grep -i "search" file.txt                # Case-insensitive
grep -r "search" directory/              # Search recursively
grep -n "error" log.txt                  # Show line numbers
```

## 5. Redirection and Pipes

### Output Redirection
```bash
command > file.txt       # Redirect output to file (overwrite)
command >> file.txt      # Append output to file
command 2> error.log     # Redirect error messages
command > output.txt 2>&1  # Redirect both output and errors
```

### Input Redirection
```bash
command < input.txt      # Use file as input
```

### Pipes
```bash
command1 | command2      # Pass output of command1 to command2
ls -la | grep ".txt"     # Find all .txt files
cat file.txt | sort      # Sort file contents
```

## 6. Permissions

### Understanding Permissions
```bash
ls -l                    # Shows permissions
# Format: -rwxr-xr-x 1 user group size date filename
#         ^^^^ ^^^ ^^^
#         owner group others
```

### Changing Permissions
```bash
chmod +x script.sh       # Make executable
chmod 755 file.txt       # Set specific permissions
chmod 600 private.txt    # Owner read/write only
```

### Ownership
```bash
chown user:group file.txt  # Change owner
sudo chown -R user:group dir/  # Change ownership recursively
```

## 7. Environment Variables

### Viewing Variables
```bash
printenv                 # Show all environment variables
echo $HOME               # Show specific variable
echo $PATH               # Show executable search path
```

### Setting Variables
```bash
export VAR_NAME="value"  # Set environment variable
MY_VAR="temp"           # Set shell variable (not exported)
```

### Using Variables
```bash
echo "Hello $USER"       # Use variable in string
echo "Path: $PATH"       # Use PATH variable
```

## 8. Useful System Commands

### Process Management
```bash
ps aux                   # Show all processes
top                      # Interactive process viewer
htop                     # Enhanced process viewer (if installed)
kill PID                 # Kill process by ID
killall process_name     # Kill all processes with name
```

### Disk Usage
```bash
df -h                    # Disk space usage
du -sh directory/        # Directory size
du -h --max-depth=1      # Size of each subdirectory
```

### System Information
```bash
uname -a                 # System info
whoami                   # Current user
date                     # Current date/time
uptime                   # System uptime
```

## 9. Text Processing

### Basic Text Tools
```bash
echo "Hello World"       # Print text
printf "Format: %s\n" "text"  # Formatted output
wc file.txt              # Count lines, words, characters
sort file.txt            # Sort lines
uniq file.txt            # Remove duplicate lines
cut -d',' -f1 file.csv   # Extract first column from CSV
```

### Advanced Text Processing
```bash
awk '{print $1}' file.txt  # Print first field
sed 's/old/new/g' file.txt # Replace text
tr 'a-z' 'A-Z'            # Translate lowercase to uppercase
```

## 10. Bash Scripting Basics

### Creating a Script
```bash
#!/bin/bash
# This is a comment

echo "Hello, World!"
```

### Making Script Executable
```bash
chmod +x script.sh
./script.sh
```

### Variables in Scripts
```bash
#!/bin/bash
NAME="John"
echo "Hello, $NAME!"
```

### User Input
```bash
#!/bin/bash
read -p "Enter your name: " USERNAME
echo "Hello, $USERNAME!"
```

### Conditional Statements
```bash
#!/bin/bash
if [ "$1" == "hello" ]; then
    echo "Hello to you too!"
elif [ "$1" == "bye" ]; then
    echo "Goodbye!"
else
    echo "I don't understand"
fi
```

### Loops
```bash
#!/bin/bash
# For loop
for file in *.txt; do
    echo "Processing $file"
done

# While loop
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

## 11. Command History and Shortcuts

### History
```bash
history                  # Show command history
!!                       # Repeat last command
!n                       # Repeat command number n
!string                  # Repeat last command starting with string
```

### Keyboard Shortcuts
- **Ctrl+C**: Cancel current command
- **Ctrl+D**: Logout/EOF
- **Ctrl+L**: Clear screen
- **Ctrl+A**: Go to beginning of line
- **Ctrl+E**: Go to end of line
- **Tab**: Auto-complete commands and filenames
- **Tab Tab**: Show all possible completions

## 12. Package Management (Linux/macOS)

### Debian/Ubuntu (apt)
```bash
sudo apt update          # Update package list
sudo apt install package # Install package
sudo apt remove package  # Remove package
```

### Red Hat/CentOS (yum/dnf)
```bash
sudo yum install package # Install package
sudo dnf install package # Newer versions
```

### macOS (Homebrew)
```bash
brew install package     # Install package
brew update              # Update Homebrew
```

## 13. Practical Examples

### Backup Script
```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
tar -czf backup_$DATE.tar.gz /important/directory
echo "Backup completed: backup_$DATE.tar.gz"
```

### File Search Script
```bash
#!/bin/bash
find . -name "*.log" -mtime -7 | xargs grep -l "ERROR"
```

### System Monitor
```bash
#!/bin/bash
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"
echo "Memory Usage:"
free -h
echo "Disk Usage:"
df -h
```

## 14. Tips and Best Practices

1. **Always backup before major operations**
2. **Use `man command` to read manual pages**
3. **Test commands with `--dry-run` when available**
4. **Use quotes around filenames with spaces**
5. **Be careful with `rm -rf` - it's irreversible**
6. **Use `set -e` in scripts to exit on errors**
7. **Check return codes with `$?`**

## 15. Next Steps

After mastering these basics, explore:
- Advanced bash scripting
- Regular expressions
- Cron jobs for automation
- SSH and remote commands
- Git version control
- Docker containers

---

## Practice Exercise

Create a simple bash script that:
1. Creates a backup directory
2. Copies all .txt files to it
3. Compresses the backup
4. Cleans up old backups (older than 7 days)

Save this as `backup_script.sh` and make it executable!

```bash
#!/bin/bash
# Simple backup script
BACKUP_DIR="backups"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"
cp *.txt "$BACKUP_DIR/"
tar -czf "backup_$DATE.tar.gz" "$BACKUP_DIR"
find . -name "backup_*.tar.gz" -mtime +7 -delete
echo "Backup completed: backup_$DATE.tar.gz"
