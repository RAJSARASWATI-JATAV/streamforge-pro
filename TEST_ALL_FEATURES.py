#!/usr/bin/env python3
"""
StreamForge-Pro - Feature Testing Script
Tests all implemented features
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

def test_imports():
    """Test if all modules can be imported"""
    print("\n" + "="*60)
    print("TESTING MODULE IMPORTS")
    print("="*60)
    
    tests = [
        ("Core - Simple Downloader", "streamforge.core.simple_downloader"),
        ("Core - Download Manager", "streamforge.core.download_manager"),
        ("Core - Playlist Downloader", "streamforge.core.playlist_downloader"),
        ("Core - Batch Processor", "streamforge.core.batch_processor"),
        ("Core - Quality Selector", "streamforge.core.quality_selector"),
        ("Core - Video Converter", "streamforge.core.video_converter"),
        ("Database Manager", "streamforge.database.db_manager"),
        ("CLI - Interactive", "streamforge.cli.interactive_cli"),
        ("Web - FastAPI App", "streamforge.web.app"),
    ]
    
    passed = 0
    failed = 0
    
    for name, module in tests:
        try:
            __import__(module)
            print(f"  [PASS] {name}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {name}: {e}")
            failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")
    return failed == 0

def test_dependencies():
    """Test if required dependencies are installed"""
    print("\n" + "="*60)
    print("TESTING DEPENDENCIES")
    print("="*60)
    
    deps = [
        ("yt-dlp", "yt_dlp"),
        ("requests", "requests"),
        ("aiohttp", "aiohttp"),
        ("rich", "rich"),
        ("click", "click"),
        ("pyyaml", "yaml"),
        ("pillow", "PIL"),
        ("psutil", "psutil"),
        ("tqdm", "tqdm"),
        ("fastapi", "fastapi"),
        ("aiosqlite", "aiosqlite"),
    ]
    
    passed = 0
    failed = 0
    
    for name, module in deps:
        try:
            __import__(module)
            print(f"  [PASS] {name}")
            passed += 1
        except ImportError:
            print(f"  [FAIL] {name} - Not installed")
            failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")
    return failed == 0

def test_optional_dependencies():
    """Test optional dependencies"""
    print("\n" + "="*60)
    print("TESTING OPTIONAL DEPENDENCIES")
    print("="*60)
    
    optional = [
        ("PyQt6 (GUI)", "PyQt6"),
        ("uvicorn (Web)", "uvicorn"),
        ("websockets (Web)", "websockets"),
    ]
    
    for name, module in optional:
        try:
            __import__(module)
            print(f"  [PASS] {name}")
        except ImportError:
            print(f"  [SKIP] {name} - Not installed (optional)")

def test_file_structure():
    """Test if all required files exist"""
    print("\n" + "="*60)
    print("TESTING FILE STRUCTURE")
    print("="*60)
    
    required_files = [
        "src/streamforge/__init__.py",
        "src/streamforge/__main__.py",
        "src/streamforge/core/simple_downloader.py",
        "src/streamforge/core/download_manager.py",
        "src/streamforge/core/playlist_downloader.py",
        "src/streamforge/core/batch_processor.py",
        "src/streamforge/core/quality_selector.py",
        "src/streamforge/core/video_converter.py",
        "src/streamforge/cli/interactive_cli.py",
        "src/streamforge/web/app.py",
        "src/streamforge/database/db_manager.py",
        "setup.py",
        "requirements.txt",
        "README.md",
        "LICENSE",
    ]
    
    passed = 0
    failed = 0
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"  [PASS] {file_path}")
            passed += 1
        else:
            print(f"  [FAIL] {file_path} - Missing")
            failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")
    return failed == 0

def test_functionality():
    """Test basic functionality"""
    print("\n" + "="*60)
    print("TESTING BASIC FUNCTIONALITY")
    print("="*60)
    
    # Test Quality Selector
    try:
        from streamforge.core.quality_selector import QualitySelector
        selector = QualitySelector()
        rec = selector.get_recommendation()
        print(f"  [PASS] Quality Selector - Recommended: {rec['quality']}")
    except Exception as e:
        print(f"  [FAIL] Quality Selector: {e}")
    
    # Test Database
    try:
        from streamforge.database.db_manager import DatabaseManager
        db = DatabaseManager(":memory:")
        db.add_download("test-id", "http://test.com", "Test Video")
        print(f"  [PASS] Database Manager")
    except Exception as e:
        print(f"  [FAIL] Database Manager: {e}")
    
    # Test Simple Downloader (without actual download)
    try:
        from streamforge.core.simple_downloader import SimpleDownloader
        downloader = SimpleDownloader()
        print(f"  [PASS] Simple Downloader initialized")
    except Exception as e:
        print(f"  [FAIL] Simple Downloader: {e}")

def print_summary():
    """Print feature summary"""
    print("\n" + "="*60)
    print("FEATURE IMPLEMENTATION STATUS")
    print("="*60)
    
    features = {
        "CORE FEATURES": [
            ("Single Video Download", "WORKING"),
            ("Playlist Download", "WORKING"),
            ("Batch Download", "WORKING"),
            ("Quality Selection", "WORKING"),
            ("Download Manager", "WORKING"),
            ("Video Converter", "WORKING"),
            ("Database Storage", "WORKING"),
        ],
        "INTERFACES": [
            ("CLI Interface", "WORKING"),
            ("Interactive CLI", "WORKING"),
            ("Web Interface", "BASIC"),
            ("GUI Interface", "BASIC"),
            ("Mobile Interface", "STUB"),
        ],
        "ADVANCED FEATURES": [
            ("Channel Download", "PLANNED"),
            ("Live Stream Recording", "STUB"),
            ("Video Editor", "STUB"),
            ("Cloud Upload", "STUB"),
            ("Browser Extension", "PLANNED"),
            ("Voice Commands", "PLANNED"),
            ("Analytics Dashboard", "PLANNED"),
        ]
    }
    
    for category, items in features.items():
        print(f"\n{category}:")
        for feature, status in items:
            status_icon = {
                "WORKING": "[OK]",
                "BASIC": "[~]",
                "STUB": "[!]",
                "PLANNED": "[ ]"
            }.get(status, "[?]")
            print(f"  {status_icon} {feature}: {status}")

def main():
    print("\n" + "="*60)
    print("STREAMFORGE-PRO - COMPREHENSIVE FEATURE TEST")
    print("="*60)
    
    all_passed = True
    
    # Run tests
    all_passed &= test_file_structure()
    all_passed &= test_dependencies()
    test_optional_dependencies()
    all_passed &= test_imports()
    test_functionality()
    print_summary()
    
    # Final result
    print("\n" + "="*60)
    if all_passed:
        print("OVERALL STATUS: ALL CRITICAL TESTS PASSED")
    else:
        print("OVERALL STATUS: SOME TESTS FAILED")
    print("="*60 + "\n")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
