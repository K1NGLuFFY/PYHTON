"""
File Organizer - A Python script to organize files in a directory
Organizes files by type, date, and other criteria
"""

import os
import shutil
import datetime
from pathlib import Path

def get_file_type(file_path):
    """Determine the file type based on extension"""
    extension = Path(file_path).suffix.lower()
    
    # Common file type categories
    file_types = {
        '.txt': 'Text',
        '.pdf': 'Documents',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.xls': 'Documents',
        '.xlsx': 'Documents',
        '.ppt': 'Documents',
        '.pptx': 'Documents',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.bmp': 'Images',
        '.mp4': 'Videos',
        '.avi': 'Videos',
        '.mov': 'Videos',
        '.mkv': 'Videos',
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.flac': 'Audio',
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.7z': 'Archives',
        '.tar': 'Archives',
        '.gz': 'Archives',
        '.py': 'Python',
        '.js': 'Code',
        '.html': 'Code',
        '.css': 'Code',
        '.java': 'Code',
        '.cpp': 'Code',
        '.c': 'Code',
        '.exe': 'Executables',
        '.msi': 'Executables'
    }
    
    return file_types.get(extension, 'Other')

def get_file_date(file_path):
    """Get the creation date of the file"""
    creation_time = os.path.getctime(file_path)
    return datetime.datetime.fromtimestamp(creation_time)

def create_directory(directory_path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")

def organize_by_type(directory_path):
    """Organize files by their type"""
    print(f"Organizing files in: {directory_path}")
    print("-" * 50)
    
    # Get all files in the directory
    files = [f for f in os.listdir(directory_path) 
             if os.path.isfile(os.path.join(directory_path, f))]
    
    if not files:
        print("No files found to organize!")
        return
    
    moved_count = 0
    
    for file in files:
        file_path = os.path.join(directory_path, file)
        file_type = get_file_type(file_path)
        
        # Create target directory
        target_dir = os.path.join(directory_path, file_type)
        create_directory(target_dir)
        
        # Move file
        target_path = os.path.join(target_dir, file)
        
        # Handle file name conflicts
        counter = 1
        while os.path.exists(target_path):
            name, ext = os.path.splitext(file)
            target_path = os.path.join(target_dir, f"{name}_{counter}{ext}")
            counter += 1
        
        shutil.move(file_path, target_path)
        print(f"Moved: {file} -> {file_type}/")
        moved_count += 1
    
    print("-" * 50)
    print(f"Organization complete! Moved {moved_count} files.")

def organize_by_date(directory_path, date_format="%Y-%m"):
    """Organize files by creation date"""
    print(f"Organizing files by date in: {directory_path}")
    print("-" * 50)
    
    files = [f for f in os.listdir(directory_path) 
             if os.path.isfile(os.path.join(directory_path, f))]
    
    if not files:
        print("No files found to organize!")
        return
    
    moved_count = 0
    
    for file in files:
        file_path = os.path.join(directory_path, file)
        file_date = get_file_date(file_path)
        date_folder = file_date.strftime(date_format)
        
        # Create date directory
        target_dir = os.path.join(directory_path, date_folder)
        create_directory(target_dir)
        
        # Move file
        target_path = os.path.join(target_dir, file)
        
        # Handle file name conflicts
        counter = 1
        while os.path.exists(target_path):
            name, ext = os.path.splitext(file)
            target_path = os.path.join(target_dir, f"{name}_{counter}{ext}")
            counter += 1
        
        shutil.move(file_path, target_path)
        print(f"Moved: {file} -> {date_folder}/")
        moved_count += 1
    
    print("-" * 50)
    print(f"Date organization complete! Moved {moved_count} files.")

def list_files(directory_path):
    """List all files in the directory with their types"""
    print(f"Files in: {directory_path}")
    print("-" * 50)
    
    files = [f for f in os.listdir(directory_path) 
             if os.path.isfile(os.path.join(directory_path, f))]
    
    if not files:
        print("No files found!")
        return
    
    for file in files:
        file_path = os.path.join(directory_path, file)
        file_type = get_file_type(file_path)
        file_size = os.path.getsize(file_path)
        print(f"{file:<30} | {file_type:<15} | {file_size:>8} bytes")
    
    print("-" * 50)
    print(f"Total files: {len(files)}")

def show_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("FILE ORGANIZER - Python File Management Tool")
    print("="*60)
    print("1. Organize files by type (Images, Documents, Videos, etc.)")
    print("2. Organize files by date (Year-Month folders)")
    print("3. List all files in current directory")
    print("4. Change directory")
    print("5. Exit")
    print("="*60)

def main():
    """Main function to run the file organizer"""
    current_directory = os.getcwd()
    
    while True:
        show_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                organize_by_type(current_directory)
            elif choice == '2':
                organize_by_date(current_directory)
            elif choice == '3':
                list_files(current_directory)
            elif choice == '4':
                new_dir = input("Enter new directory path: ").strip()
                if os.path.exists(new_dir) and os.path.isdir(new_dir):
                    current_directory = new_dir
                    print(f"Changed to directory: {current_directory}")
                else:
                    print("Invalid directory path!")
            elif choice == '5':
                print("Thank you for using File Organizer!")
                break
            else:
                print("Invalid choice! Please enter 1-5.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    print("Welcome to File Organizer!")
    print(f"Current working directory: {os.getcwd()}")
    
    # Ask if user wants to use current directory or specify another
    use_current = input("Use current directory? (y/n): ").lower().strip()
    
    if use_current != 'y':
        new_dir = input("Enter directory path to organize: ").strip()
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            os.chdir(new_dir)
            print(f"Changed to directory: {new_dir}")
        else:
            print("Invalid directory! Using current directory.")
    
    main()
