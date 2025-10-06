#!/bin/bash
# StreamForge-Pro Termux Installer
# Created by RAJSARASWATI JATAV
# Copyright (c) 2025 RAJSARASWATI JATAV

echo ""
echo "========================================"
echo " StreamForge-Pro Termux Installer"
echo " Created by RAJSARASWATI JATAV"
echo "========================================"
echo ""

# Update packages
echo "Updating packages..."
pkg update -y && pkg upgrade -y

# Install Python
echo "Installing Python..."
pkg install python -y

# Install FFmpeg
echo "Installing FFmpeg..."
pkg install ffmpeg -y

# Install git
echo "Installing git..."
pkg install git -y

# Check Python
if ! command -v python &> /dev/null; then
    echo "[ERROR] Python installation failed!"
    exit 1
fi

echo "[OK] Python installed"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements_complete.txt

if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi

# Setup storage
echo "Setting up storage access..."
termux-setup-storage

echo ""
echo "[SUCCESS] Installation complete!"
echo ""
echo "Run: python streamforge_hacker.py"
echo ""
