#!/bin/bash
# StreamForge-Pro Ubuntu Installer
# Created by RAJSARASWATI JATAV

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║           StreamForge-Pro Ubuntu Installer                    ║"
echo "║           Created by: RAJSARASWATI JATAV                      ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

sudo apt update
sudo apt install -y python3 python3-pip git ffmpeg

pip3 install --upgrade pip
pip3 install -r requirements_complete.txt

echo "alias sf='cd ~/streamforge-pro && python3 streamforge_hacker.py'" >> ~/.bashrc

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                    ✅ INSTALLATION COMPLETE                   ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🚀 Run: python3 streamforge_hacker.py"
echo "   OR: sf"
echo ""
echo "© 2025 RAJSARASWATI JATAV"
echo ""
