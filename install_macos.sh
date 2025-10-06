#!/bin/bash
# StreamForge-Pro macOS Installer
# Created by RAJSARASWATI JATAV
# Copyright (c) 2025 RAJSARASWATI JATAV

echo ""
echo "========================================"
echo " StreamForge-Pro macOS Installer"
echo " Created by RAJSARASWATI JATAV"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 not found!"
    echo "Install: brew install python3"
    exit 1
fi

echo "[OK] Python3 found"

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "[ERROR] pip3 not found!"
    exit 1
fi

echo "[OK] pip3 found"

# Check FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "[WARNING] FFmpeg not found"
    echo "Installing FFmpeg..."
    brew install ffmpeg
fi

echo "[OK] FFmpeg ready"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements_complete.txt

if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi

echo ""
echo "[SUCCESS] Installation complete!"
echo ""
echo "Run: python3 streamforge_hacker.py"
echo ""
