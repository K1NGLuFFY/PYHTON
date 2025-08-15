"""
Setup script for Web Scraper with Data Analysis
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully")
    except subprocess.CalledProcessError:
        print("✗ Failed to install requirements")
        sys.exit(1)

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'requests', 'bs4', 'pandas', 'matplotlib', 'seaborn', 'numpy'
    ]
    
    failed_imports = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            failed_imports.append(package)
    
    if failed_imports:
        print(f"✗ Failed to import: {', '.join(failed_imports)}")
        return False
    else:
        print("✓ All packages imported successfully")
        return True

def create_demo_files():
    """Create demo files for testing"""
    # Create a simple demo HTML file for testing
    demo_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Demo Page for Web Scraper</title>
    </head>
    <body>
        <h1>Welcome to Web Scraper Demo</h1>
        <h2>About This Demo</h2>
        <p>This is a sample paragraph for testing the web scraper.</p>
        <p>Web scraping is a powerful technique for data collection.</p>
        
        <h3>Features</h3>
        <ul>
            <li>Text analysis</li>
            <li>Link extraction</li>
            <li>Data visualization</li>
        </ul>
        
        <a href="https://example.com/about">About Us</a>
        <a href="https://example.com/contact">Contact</a>
        
        <img src="demo-image.jpg" alt="Demo Image">
    </body>
    </html>
    """
    
    with open('demo_page.html', 'w') as f:
        f.write(demo_html)
    
    print("✓ Demo files created")

def main():
    """Main setup function"""
    print("Setting up Web Scraper with Data Analysis...")
    print("=" * 50)
    
    # Install requirements
    print("1. Installing requirements...")
    install_requirements()
    
    # Test imports
    print("\n2. Testing package imports...")
    if not test_imports():
        print("Please install missing packages manually")
        return
    
    # Create demo files
    print("\n3. Creating demo files...")
    create_demo_files()
    
    print("\n" + "=" * 50)
    print("Setup complete! You can now:")
    print("1. Run 'python scraper_example.py' for a basic example")
    print("2. Run 'python web_scraper_analyzer.py' for the full demo")
    print("3. Check 'demo_page.html' for a local test file")
    print("\nHappy scraping!")

if __name__ == "__main__":
    main()
