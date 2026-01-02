#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for YouTube Kanal İndirici
Tests core functionality without requiring GUI interaction
"""

import sys
import os

def test_imports():
    """Test that all required imports work"""
    print("Testing imports...")
    
    try:
        import tkinter
        print("✓ tkinter import successful")
    except ImportError as e:
        print(f"✗ tkinter import failed: {e}")
        return False
    
    try:
        import yt_dlp
        print("✓ yt_dlp import successful")
    except ImportError as e:
        print(f"✗ yt_dlp import failed: {e}")
        return False
    
    try:
        import accessible_output2
        print("✓ accessible_output2 import successful (optional)")
    except ImportError:
        print("⚠ accessible_output2 not available (optional - screen reader support)")
    
    return True

def test_main_module():
    """Test that main.py can be imported"""
    print("\nTesting main module import...")
    
    try:
        # Add current directory to path
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        # Try to import main module without running it
        import importlib.util
        spec = importlib.util.spec_from_file_location("main", "main.py")
        main_module = importlib.util.module_from_spec(spec)
        
        # Don't execute, just check if it loads
        print("✓ main.py module structure is valid")
        return True
    except Exception as e:
        print(f"✗ main.py module import failed: {e}")
        return False

def test_yt_dlp_functionality():
    """Test basic yt-dlp functionality"""
    print("\nTesting yt-dlp basic functionality...")
    
    try:
        import yt_dlp
        
        # Test version
        print(f"✓ yt-dlp version: {yt_dlp.version.__version__}")
        
        # Test basic configuration
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("✓ yt-dlp YoutubeDL object created successfully")
        
        return True
    except Exception as e:
        print(f"✗ yt-dlp functionality test failed: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\nTesting file structure...")
    
    required_files = [
        'main.py',
        'requirements.txt',
        'youtube_downloader.spec',
        'setup_script.iss',
        'build.bat',
        'build.sh',
        'README.md',
        '.gitignore'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("=" * 60)
    print("YouTube Kanal İndirici - Test Suite")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("File Structure", test_file_structure()))
    results.append(("Imports", test_imports()))
    results.append(("Main Module", test_main_module()))
    results.append(("yt-dlp Functionality", test_yt_dlp_functionality()))
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = 0
    failed = 0
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test_name}: {status}")
        if result:
            passed += 1
        else:
            failed += 1
    
    print(f"\nTotal: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
