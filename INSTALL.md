# 📦 Installation Guide

**Created by RAJSARASWATI JATAV**

## 🪟 Windows Installation

### Method 1: Automatic (Recommended)
```bash
# Run installer
install_windows.bat
```

### Method 2: Manual
```bash
# Install Python 3.8+ from https://python.org
# Then run:
pip install -r requirements_complete.txt
python streamforge_hacker.py
```

---

## 🍎 macOS Installation

### Method 1: Automatic (Recommended)
```bash
# Make executable
chmod +x install_macos.sh

# Run installer
./install_macos.sh
```

### Method 2: Manual
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and FFmpeg
brew install python3 ffmpeg

# Install dependencies
pip3 install -r requirements_complete.txt

# Run
python3 streamforge_hacker.py
```

---

## 📱 Termux Installation (Android)

### Method 1: Automatic (Recommended)
```bash
# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro

# Make executable
chmod +x install_termux.sh

# Run installer
./install_termux.sh
```

### Method 2: Manual
```bash
# Update packages
pkg update -y && pkg upgrade -y

# Install dependencies
pkg install python ffmpeg git -y

# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro

# Install Python packages
pip install -r requirements_complete.txt

# Setup storage
termux-setup-storage

# Run
python streamforge_hacker.py
```

---

## 🐧 Linux Installation

### Ubuntu/Debian
```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip ffmpeg git -y

# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro

# Install Python packages
pip3 install -r requirements_complete.txt

# Run
python3 streamforge_hacker.py
```

### Arch Linux
```bash
# Install dependencies
sudo pacman -S python python-pip ffmpeg git

# Clone repository
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro

# Install Python packages
pip install -r requirements_complete.txt

# Run
python streamforge_hacker.py
```

---

## ✅ Verify Installation

```bash
# Check Python
python --version  # or python3 --version

# Check FFmpeg
ffmpeg -version

# Test StreamForge-Pro
python streamforge_hacker.py
```

---

## 🚀 Quick Start

After installation:

```bash
# Hacker Edition (Recommended)
python streamforge_hacker.py

# Standard Edition
python streamforge_cli.py

# Instagram Pro
python -m streamforge.social.instagram_pro

# TikTok Pro
python -m streamforge.social.tiktok_pro
```

---

## 🔧 Troubleshooting

### Python not found
- **Windows**: Install from https://python.org
- **macOS**: `brew install python3`
- **Linux**: `sudo apt install python3`
- **Termux**: `pkg install python`

### FFmpeg not found
- **Windows**: Download from https://ffmpeg.org
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`
- **Termux**: `pkg install ffmpeg`

### Permission denied
```bash
chmod +x install_*.sh
```

### pip install fails
```bash
pip install --upgrade pip
pip install -r requirements_complete.txt --no-cache-dir
```

---

## 📞 Support

**Creator:** RAJSARASWATI JATAV  
**Email:** rajsaraswatijatav@outlook.com  
**GitHub:** @rajsaraswati | @RAJSARASWATI-JATAV  
**Telegram:** @Rajsaraswati_bot

---

**© 2025 RAJSARASWATI JATAV - All Rights Reserved**
