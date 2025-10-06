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

# Create desktop shortcut
echo "Creating shortcuts..."
mkdir -p ~/.shortcuts
echo '#!/bin/bash
cd ~/streamforge-pro && python streamforge_hacker.py' > ~/.shortcuts/streamforge
chmod +x ~/.shortcuts/streamforge

# Setup alias
echo "alias sf='cd ~/streamforge-pro && python streamforge_hacker.py'" >> ~/.bashrc

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                    ✅ INSTALLATION COMPLETE                   ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🚀 Quick Start:"
echo "   python streamforge_hacker.py"
echo "   OR just type: sf"
echo ""
echo "📖 Full Guide: cat TERMUX_COMPLETE_GUIDE.md"
echo ""
echo "© 2025 RAJSARASWATI JATAV - Gwalior, India"
echo ""
