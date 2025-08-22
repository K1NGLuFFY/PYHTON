#!/usr/bin/env python3
"""
Utility functions for the Invoice Generator
"""

import os
import platform

def clear_screen():
    """Clear the terminal screen"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_user_input(prompt, input_type=str):
    """Get validated user input"""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Input cannot be empty. Please try again.")
                continue
            
            if input_type == float:
                return float(user_input)
            elif input_type == int:
                return int(user_input)
            else:
                return user_input
                
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def format_currency(amount):
    """Format amount as currency"""
    return f"${amount:.2f}"

def validate_email(email):
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def create_directories():
    """Create necessary directories for the application"""
    directories = ['data', 'invoices', 'backups']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def get_file_size(filepath):
    """Get file size in human readable format"""
    if not os.path.exists(filepath):
        return "File not found"
    
    size_bytes = os.path.getsize(filepath)
    
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"

def print_separator(char='=', length=50):
    """Print a separator line"""
    print(char * length)

def center_text(text, width=50):
    """Center text within a given width"""
    return text.center(width)

def display_header(title):
    """Display a formatted header"""
    clear_screen()
    print_separator()
    print(center_text(title))
    print_separator()

def confirm_action(prompt):
    """Ask for confirmation before proceeding"""
    response = input(f"{prompt} (y/n): ").lower().strip()
    return response == 'y'

def format_date(date_string):
    """Format date string to more readable format"""
    from datetime import datetime
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return date_string

def generate_random_string(length=8):
    """Generate a random string for temporary filenames"""
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def is_valid_filename(filename):
    """Check if filename is valid for the filesystem"""
    import re
    invalid_chars = r'[<>:\"/\\|?*]'
    return not re.search(invalid_chars, filename)

def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    import re
    invalid_chars = r'[<>:\"/\\|?*]'
    return re.sub(invalid_chars, '_', filename)

def get_system_info():
    """Get basic system information"""
    return {
        'platform': platform.system(),
        'python_version': platform.python_version(),
        'current_directory': os.getcwd()
    }

def countdown(seconds, message="Continuing in"):
    """Display a countdown timer"""
    import time
    for i in range(seconds, 0, -1):
        print(f"{message} {i} seconds...", end='\r')
        time.sleep(1)
    print(" " * 50)  # Clear the line
