# File Organizer - Python Script

A powerful Python script to organize files in any directory by type, date, and other criteria.

## Features

- **Organize by File Type**: Automatically categorizes files into folders like:
  - Images (jpg, png, gif, etc.)
  - Documents (pdf, docx, xlsx, etc.)
  - Videos (mp4, avi, mov, etc.)
  - Audio (mp3, wav, flac, etc.)
  - Code (py, js, html, css, etc.)
  - Archives (zip, rar, 7z, etc.)
  - Executables (exe, msi)
  - Text files (txt)
  - And more!

- **Organize by Date**: Creates folders based on file creation date (Year-Month format)

- **File Listing**: View all files with their types and sizes

- **Safe Operations**: Handles file name conflicts automatically

## How to Use

1. **Run the script**:
   ```bash
   python file_organizer.py
   ```

2. **Choose an option**:
   - Press `1` to organize files by type
   - Press `2` to organize files by date
   - Press `3` to list all files in current directory
   - Press `4` to change to a different directory
   - Press `5` to exit

3. **Follow the prompts**:
   - The script will ask if you want to use the current directory
   - You can specify any directory path to organize

## Example Usage

```bash
# Run the organizer
python file_organizer.py

# Choose to organize by type (option 1)
# Files will be moved to folders like:
# - Documents/ (for pdf, docx files)
# - Images/ (for jpg, png files)
# - Videos/ (for mp4, mov files)
# - etc.
```

## Requirements

- Python 3.x
- Standard Python libraries (no external dependencies required)

## Safety Features

- Creates directories only when needed
- Handles duplicate file names automatically
- Shows preview before moving files
- Error handling for invalid paths

## Customization

You can easily modify the `get_file_type()` function to add more file extensions or change the categorization.

## Supported File Types

The script currently supports over 30 different file extensions including:
- **Documents**: .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx
- **Images**: .jpg, .jpeg, .png, .gif, .bmp
- **Videos**: .mp4, .avi, .mov, .mkv
- **Audio**: .mp3, .wav, .flac
- **Code**: .py, .js, .html, .css, .java, .cpp, .c
- **Archives**: .zip, .rar, .7z, .tar, .gz
- **Executables**: .exe, .msi
- **Text**: .txt

## Notes

- The script only moves files (not directories)
- Original file structure is preserved within the organized folders
- Always test with a backup copy of your files first
