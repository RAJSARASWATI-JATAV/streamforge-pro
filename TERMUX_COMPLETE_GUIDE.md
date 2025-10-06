# 📱 StreamForge-Pro - Complete Termux Guide

**Created by RAJSARASWATI JATAV**

## 🚀 One-Command Installation

```bash
pkg update -y && pkg install git python ffmpeg -y && git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git && cd streamforge-pro && pip install -r requirements_complete.txt && python streamforge_hacker.py
```

## 📋 Step-by-Step Installation

### Step 1: Update Termux
```bash
pkg update -y && pkg upgrade -y
```

### Step 2: Install Dependencies
```bash
pkg install python git ffmpeg -y
```

### Step 3: Clone Repository
```bash
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro
```

### Step 4: Install Python Packages
```bash
pip install --upgrade pip
pip install -r requirements_complete.txt
```

### Step 5: Setup Storage (Optional)
```bash
termux-setup-storage
```

### Step 6: Run StreamForge-Pro
```bash
python streamforge_hacker.py
```

## 🎯 Quick Usage

### Download YouTube Video
```bash
python streamforge_hacker.py
# Select [01] Quick Download
# Paste URL
# Choose quality
```

### Instagram Pro (Zero Compression)
```bash
python streamforge_hacker.py
# Select [21] Instagram Pro
# Paste Instagram URL
```

### TikTok Pro (No Watermark)
```bash
python streamforge_hacker.py
# Select [22] TikTok Pro
# Paste TikTok URL
```

### API Server
```bash
python streamforge_api.py
# Access from browser: http://localhost:8000/docs
```

### Live Server
```bash
python streamforge_live.py
# Access: http://localhost:8080
```

## 🔧 Termux-Specific Features

### Storage Access
```bash
# Download to phone storage
termux-setup-storage
# Files saved to: ~/storage/downloads/
```

### Background Running
```bash
# Install termux-services
pkg install termux-services -y

# Run in background
nohup python streamforge_hacker.py &
```

### Notifications
```bash
# Install termux-api
pkg install termux-api -y

# Get notifications on download complete
termux-notification -t "Download Complete" -c "Video downloaded successfully"
```

## 📱 Termux Commands

### Check Status
```bash
python -c "from streamforge.utils.analytics import Analytics; print(Analytics().get_stats())"
```

### Update StreamForge
```bash
cd streamforge-pro
git pull origin main
pip install -r requirements_complete.txt --upgrade
```

### Clear Cache
```bash
rm -rf ~/.streamforge/cache/*
```

### View Logs
```bash
cat ~/.streamforge/logs/streamforge.log
```

## 🎨 Termux Customization

### Install Oh-My-Termux
```bash
pkg install curl -y
sh -c "$(curl -fsSL https://git.io/oh-my-termux)"
```

### Custom Colors
```bash
# Edit .bashrc
nano ~/.bashrc

# Add:
export PS1="\[\033[01;32m\]StreamForge\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "
```

## 🚀 Performance Tips

### Reduce Memory Usage
```bash
# Use CLI instead of GUI
python streamforge_cli.py
```

### Faster Downloads
```bash
# Increase concurrent downloads
# Edit config: ~/.streamforge/config/app_config.yml
# Set: max_concurrent: 3
```

### Save Battery
```bash
# Use audio-only mode
python streamforge_hacker.py
# Select audio-only option
```

## 🐛 Troubleshooting

### Python Not Found
```bash
pkg install python -y
```

### FFmpeg Error
```bash
pkg install ffmpeg -y
```

### Permission Denied
```bash
chmod +x streamforge_hacker.py
```

### Storage Access
```bash
termux-setup-storage
# Allow storage permission in Android settings
```

### Module Not Found
```bash
pip install -r requirements_complete.txt --force-reinstall
```

## 📊 System Requirements

- **Android:** 7.0+
- **Termux:** Latest version
- **Storage:** 500MB free
- **RAM:** 2GB minimum
- **Internet:** Active connection

## 🎯 All Features Available

✅ YouTube downloads
✅ Instagram Pro (zero compression)
✅ TikTok Pro (no watermark)
✅ Playlist downloads
✅ Batch downloads
✅ AI quality optimizer
✅ Cloud upload
✅ Telegram bot
✅ API server
✅ Live server
✅ Voice commands
✅ Custom themes
✅ Plugin system

## 📱 Termux Shortcuts

### Create Alias
```bash
echo "alias sf='python ~/streamforge-pro/streamforge_hacker.py'" >> ~/.bashrc
source ~/.bashrc

# Now just type: sf
```

### Quick Download Alias
```bash
echo "alias sfd='cd ~/streamforge-pro && python streamforge_hacker.py'" >> ~/.bashrc
```

## 🌐 Network Configuration

### Use Proxy
```bash
export HTTP_PROXY="http://proxy:port"
export HTTPS_PROXY="http://proxy:port"
```

### Check Connection
```bash
ping -c 4 google.com
```

## 💾 Backup & Restore

### Backup Downloads
```bash
tar -czf streamforge_backup.tar.gz ~/storage/downloads/StreamForge
```

### Restore
```bash
tar -xzf streamforge_backup.tar.gz -C ~/storage/downloads/
```

## 🔐 Security

### Secure Storage
```bash
# Encrypt downloads folder
pkg install openssl -y
```

### Clear History
```bash
rm ~/.streamforge/data/download_history.db
```

## 📞 Support

- **GitHub Issues:** https://github.com/RAJSARASWATI-JATAV/streamforge-pro/issues
- **Email:** rajsaraswatijatav@outlook.com
- **Telegram:** @Rajsaraswati_bot

## 🎉 Quick Start Commands

```bash
# Install
pkg update && pkg install git python ffmpeg -y && git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git && cd streamforge-pro && pip install -r requirements_complete.txt

# Run
python streamforge_hacker.py

# Update
cd streamforge-pro && git pull && pip install -r requirements_complete.txt --upgrade

# Uninstall
cd ~ && rm -rf streamforge-pro
```

---

**© 2025 RAJSARASWATI JATAV**
**Location: Gwalior, Madhya Pradesh, India**
**Made with ❤️ for Termux Users**
