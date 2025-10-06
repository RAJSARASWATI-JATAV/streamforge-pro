"""Add creator headers to all Python files"""
import os
from pathlib import Path

HEADER = '''"""
╔═══════════════════════════════════════════════════════════════════════════╗
║ StreamForge-Pro - Advanced Multi-Platform Media Downloader               ║
║                                                                           ║
║ Created by: Raj Saraswati (@rajsaraswati)                               ║
║ GitHub: github.com/RAJSARASWATI-JATAV/streamforge-pro                   ║
║ Copyright © 2025 Raj Saraswati - All Rights Reserved                    ║
║                                                                           ║
║ This file is part of StreamForge-Pro.                                   ║
║ Educational and ethical use only.                                        ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""
'''

def add_header_to_file(file_path):
    """Add header to a Python file if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if header already exists
        if 'Created by: Raj Saraswati' in content:
            print(f"✓ Already has header: {file_path}")
            return
        
        # Add header
        new_content = HEADER + '\n' + content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Added header: {file_path}")
    except Exception as e:
        print(f"❌ Error: {file_path} - {e}")

def main():
    """Add headers to all Python files"""
    print("Adding creator headers to all Python files...\n")
    
    # Get all Python files in src/streamforge
    src_dir = Path('src/streamforge')
    
    if not src_dir.exists():
        print("❌ src/streamforge directory not found!")
        return
    
    python_files = list(src_dir.rglob('*.py'))
    
    print(f"Found {len(python_files)} Python files\n")
    
    for file_path in python_files:
        add_header_to_file(file_path)
    
    print(f"\nCompleted! Processed {len(python_files)} files")

if __name__ == "__main__":
    main()
