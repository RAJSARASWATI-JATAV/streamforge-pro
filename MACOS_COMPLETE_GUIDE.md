# 🍎 StreamForge-Pro - Complete macOS Guide

**Created by RAJSARASWATI JATAV**

## 🚀 One-Command Installation

```bash
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git && cd streamforge-pro && pip3 install -r requirements_complete.txt && python3 streamforge_hacker.py
```

## 📋 Step-by-Step Installation

### Step 1: Install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Install Python & FFmpeg
```bash
brew install python ffmpeg git
```

### Step 3: Clone Repository
```bash
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro
```

### Step 4: Install Dependencies
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
chmod +x install_macos.sh
./install_macos.sh
```

## 🎯 Quick Usage

### Download YouTube Video
```bash
python3 streamforge_hacker.py
```
Select [01] Quick Download → Paste URL → Choose quality

### Instagram Pro (Zero Compression)
```bash
python3 streamforge_hacker.py
```
Select [21] Instagram Pro → Paste URL

### TikTok Pro (No Watermark)
```bash
python3 streamforge_hacker.py
```
Select [22] TikTok Pro → Paste URL

### API Server
```bash
python3 streamforge_api.py
```
Access: http://localhost:8000/docs

### Live Server
```bash
python3 streamforge_live.py
```
Access: http://localhost:8080

## 🍎 macOS-Specific Features

### Create App Bundle
```bash
# Create StreamForge.app
mkdir -p StreamForge.app/Contents/MacOS
echo '#!/bin/bash
cd ~/streamforge-pro && python3 streamforge_hacker.py' > StreamForge.app/Contents/MacOS/StreamForge
chmod +x StreamForge.app/Contents/MacOS/StreamForge
```

### Dock Integration
Drag `StreamForge.app` to Dock

### Spotlight Search
```bash
# Index StreamForge folder
mdimport ~/streamforge-pro
```

### Quick Actions
Create Automator workflow for right-click download

### Touch Bar Support
Custom Touch Bar buttons for quick actions

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

### Database
```
~/.streamforge/data/
```

## 🔧 macOS Commands

### Check Installation
```bash
python3 --version
pip3 --version
ffmpeg -version
brew --version
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

## 🎨 macOS Customization

### Bash/Zsh Alias
```bash
# Edit ~/.zshrc or ~/.bash_profile
echo "alias sf='cd ~/streamforge-pro && python3 streamforge_hacker.py'" >> ~/.zshrc
source ~/.zshrc
```

### iTerm2 Profile
```json
{
  "name": "StreamForge-Pro",
  "command": "cd ~/streamforge-pro && python3 streamforge_hacker.py"
}
```

### Alfred Workflow
Create custom Alfred workflow for quick downloads

### Keyboard Shortcuts
```bash
# System Preferences → Keyboard → Shortcuts
# Add custom shortcut: Cmd+Shift+S
```

## 🚀 Performance Tips

### Use SSD
macOS automatically optimizes for SSD

### Increase Concurrent Downloads
```yaml
# Edit: ~/.streamforge/config/app_config.yml
download:
  max_concurrent: 5
```

### Metal Acceleration
```bash
# Use Metal for GPU encoding
pip3 install torch torchvision
```

### Disable Gatekeeper (Temporary)
```bash
sudo spctl --master-disable
# Re-enable after: sudo spctl --master-enable
```

## 🐛 Troubleshooting

### Python3 Not Found
```bash
brew install python
```

### FFmpeg Error
```bash
brew install ffmpeg
```

### Permission Denied
```bash
chmod +x streamforge_hacker.py
```

### SSL Certificate Error
```bash
pip3 install --upgrade certifi
/Applications/Python\ 3.*/Install\ Certificates.command
```

### Module Not Found
```bash
pip3 install -r requirements_complete.txt --force-reinstall
```

## 📊 System Requirements

- **macOS:** 10.15 Catalina or later
- **Python:** 3.8+
- **RAM:** 4GB minimum
- **Storage:** 1GB free
- **Internet:** Active connection

## 🎯 All Features Available

✅ YouTube downloads
✅ Instagram Pro (zero compression)
✅ TikTok Pro (no watermark)
✅ Playlist downloads
✅ Batch downloads
✅ AI quality optimizer
✅ Cloud upload (Google Drive, Dropbox)
✅ Telegram bot
✅ API server
✅ Live server
✅ Voice commands
✅ Custom themes
✅ Plugin system
✅ Browser extension

## 🌐 Network Configuration

### Use Proxy
```bash
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port
```

### Check Connection
```bash
ping google.com
```

## 💾 Backup & Restore

### Backup Downloads
```bash
cp -R ~/Downloads/StreamForge ~/Backups/
```

### Backup Config
```bash
cp -R ~/.streamforge ~/Backups/
```

### Restore
```bash
cp -R ~/Backups/StreamForge ~/Downloads/
cp -R ~/Backups/.streamforge ~/
```

## 🔐 Security

### Gatekeeper
```bash
# Allow app from anywhere
sudo spctl --master-disable
```

### FileVault
Encrypt StreamForge folder with FileVault

### Clear History
```bash
rm ~/.streamforge/data/download_history.db
```

## 📱 Integration

### Safari Extension
1. Open Safari → Preferences → Extensions
2. Enable Developer Mode
3. Load extension from: `src/streamforge/extensions/chrome`

### Notification Center
```bash
# Automatic notifications
osascript -e 'display notification "Download complete" with title "StreamForge-Pro"'
```

### Automator
Create Automator workflow for batch downloads

### Shortcuts App
Create Shortcuts for quick downloads

## 🎮 Advanced Usage

### Shell Script for Quick Download
```bash
#!/bin/bash
echo "Enter video URL:"
read url
python3 streamforge_hacker.py --url "$url" --quality best
```

### LaunchAgent for Auto-Start
```xml
<!-- ~/Library/LaunchAgents/com.streamforge.plist -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.streamforge</string>
    <key>ProgramArguments</key>
    <array>
        <string>python3</string>
        <string>/path/to/streamforge_hacker.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

### Scheduled Downloads
```bash
# Use cron
crontab -e
# Add: 0 2 * * * cd ~/streamforge-pro && python3 streamforge_hacker.py
```

## 📞 Support

- **GitHub Issues:** https://github.com/RAJSARASWATI-JATAV/streamforge-pro/issues
- **Email:** rajsaraswatijatav@outlook.com
- **Telegram:** @Rajsaraswati_bot

## 🎉 Quick Start Commands

```bash
# Install
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro
pip3 install -r requirements_complete.txt

# Run
python3 streamforge_hacker.py

# Update
cd streamforge-pro
git pull
pip3 install -r requirements_complete.txt --upgrade

# Uninstall
cd ~ && rm -rf streamforge-pro
```

## 🔥 Pro Tips

### Create Dock Icon
```bash
# Create .app bundle with custom icon
# Use Icon Composer or online tools
```

### Finder Integration
Add to Finder sidebar for quick access

### Spotlight Indexing
```bash
mdimport ~/streamforge-pro
```

### Multiple Instances
```bash
python3 streamforge_hacker.py &
python3 streamforge_api.py &
python3 streamforge_live.py &
```

### Use with Raycast
Create Raycast script for quick downloads

---

**© 2025 RAJSARASWATI JATAV**
**Location: Gwalior, Madhya Pradesh, India**
**Made with ❤️ for macOS Users**
