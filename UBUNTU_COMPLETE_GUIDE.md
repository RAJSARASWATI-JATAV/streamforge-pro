# 🐧 StreamForge-Pro - Complete Ubuntu/Linux Guide

**Created by RAJSARASWATI JATAV**

## 🚀 One-Command Installation

```bash
sudo apt update && sudo apt install -y python3 python3-pip git ffmpeg && git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git && cd streamforge-pro && pip3 install -r requirements_complete.txt && python3 streamforge_hacker.py
```

## 📋 Step-by-Step Installation

### Step 1: Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Dependencies
```bash
sudo apt install -y python3 python3-pip git ffmpeg
```

### Step 3: Clone Repository
```bash
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro
```

### Step 4: Install Python Packages
```bash
pip3 install --upgrade pip
pip3 install -r requirements_complete.txt
```

### Step 5: Run StreamForge-Pro
```bash
python3 streamforge_hacker.py
```

## ⚡ Quick Install Script

```bash
chmod +x install_ubuntu.sh
./install_ubuntu.sh
```

## 🎯 Quick Usage

### Download YouTube Video
```bash
python3 streamforge_hacker.py
```

### Instagram Pro
```bash
python3 streamforge_hacker.py
# Select [21] Instagram Pro
```

### TikTok Pro
```bash
python3 streamforge_hacker.py
# Select [22] TikTok Pro
```

### API Server
```bash
python3 streamforge_api.py
# Access: http://localhost:8000/docs
```

### Live Server
```bash
python3 streamforge_live.py
# Access: http://localhost:8080
```

## 🐧 Ubuntu-Specific Features

### Desktop Entry
```bash
cat > ~/.local/share/applications/streamforge.desktop << EOF
[Desktop Entry]
Name=StreamForge-Pro
Exec=python3 ~/streamforge-pro/streamforge_hacker.py
Icon=video-x-generic
Type=Application
Categories=AudioVideo;Video;
EOF
```

### Nautilus Integration
Right-click context menu for downloads

### System Tray
```bash
pip3 install pystray pillow
```

### Keyboard Shortcuts
```bash
# Settings → Keyboard → Custom Shortcuts
# Add: python3 ~/streamforge-pro/streamforge_hacker.py
```

## 📁 Default Locations

### Downloads
```
~/Downloads/StreamForge/
```

### Config
```
~/.streamforge/config/
```

### Logs
```
~/.streamforge/logs/
```

## 🔧 Ubuntu Commands

### Check Installation
```bash
python3 --version
pip3 --version
ffmpeg -version
```

### Update StreamForge
```bash
cd streamforge-pro
git pull origin main
pip3 install -r requirements_complete.txt --upgrade
```

### Clear Cache
```bash
rm -rf ~/.streamforge/cache/*
```

### View Logs
```bash
tail -f ~/.streamforge/logs/streamforge.log
```

## 🎨 Ubuntu Customization

### Bash Alias
```bash
echo "alias sf='cd ~/streamforge-pro && python3 streamforge_hacker.py'" >> ~/.bashrc
source ~/.bashrc
```

### Zsh Alias
```bash
echo "alias sf='cd ~/streamforge-pro && python3 streamforge_hacker.py'" >> ~/.zshrc
source ~/.zshrc
```

## 🚀 Performance Tips

### Use SSD
```bash
# Move downloads to SSD
ln -s /mnt/ssd/StreamForge ~/Downloads/StreamForge
```

### Increase Concurrent Downloads
```yaml
# Edit: ~/.streamforge/config/app_config.yml
download:
  max_concurrent: 5
```

### GPU Acceleration
```bash
# Install CUDA
sudo apt install nvidia-cuda-toolkit
pip3 install torch torchvision
```

## 🐛 Troubleshooting

### Python3 Not Found
```bash
sudo apt install python3
```

### FFmpeg Error
```bash
sudo apt install ffmpeg
```

### Permission Denied
```bash
chmod +x streamforge_hacker.py
```

### Module Not Found
```bash
pip3 install -r requirements_complete.txt --force-reinstall
```

## 📊 System Requirements

- **Ubuntu:** 20.04 LTS or later
- **Python:** 3.8+
- **RAM:** 2GB minimum
- **Storage:** 1GB free
- **Internet:** Active connection

## 🎯 All Features Available

✅ All platforms supported
✅ Full feature set
✅ GPU acceleration
✅ System integration

## 🌐 Network Configuration

### Use Proxy
```bash
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port
```

## 💾 Backup & Restore

### Backup
```bash
tar -czf streamforge_backup.tar.gz ~/streamforge-pro ~/.streamforge
```

### Restore
```bash
tar -xzf streamforge_backup.tar.gz -C ~/
```

## 📞 Support

- **GitHub:** https://github.com/RAJSARASWATI-JATAV/streamforge-pro
- **Email:** rajsaraswatijatav@outlook.com

---

**© 2025 RAJSARASWATI JATAV**
**Gwalior, Madhya Pradesh, India**
