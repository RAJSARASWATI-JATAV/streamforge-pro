# 💻 StreamForge-Pro - Complete Windows Guide

**Created by RAJSARASWATI JATAV**

## 🚀 One-Command Installation (PowerShell)

```powershell
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git; cd streamforge-pro; pip install -r requirements_complete.txt; python streamforge_hacker.py
```

## 📋 Step-by-Step Installation

### Step 1: Install Python
1. Download Python 3.8+ from https://python.org
2. ✅ Check "Add Python to PATH"
3. Install

### Step 2: Install Git (Optional)
Download from https://git-scm.com/download/win

### Step 3: Install FFmpeg
1. Download from https://ffmpeg.org/download.html
2. Extract to `C:\ffmpeg`
3. Add to PATH: `C:\ffmpeg\bin`

### Step 4: Clone Repository
```cmd
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro
```

### Step 5: Install Dependencies
```cmd
pip install --upgrade pip
pip install -r requirements_complete.txt
```

### Step 6: Run StreamForge-Pro
```cmd
python streamforge_hacker.py
```

## ⚡ Quick Install Script

Run `install_windows.bat` (double-click)

## 🎯 Quick Usage

### Download YouTube Video
```cmd
python streamforge_hacker.py
```
Select [01] Quick Download → Paste URL → Choose quality

### Instagram Pro (Zero Compression)
```cmd
python streamforge_hacker.py
```
Select [21] Instagram Pro → Paste URL

### TikTok Pro (No Watermark)
```cmd
python streamforge_hacker.py
```
Select [22] TikTok Pro → Paste URL

### API Server
```cmd
python streamforge_api.py
```
Access: http://localhost:8000/docs

### Live Server
```cmd
python streamforge_live.py
```
Access: http://localhost:8080

## 🖥️ Windows-Specific Features

### Desktop Shortcut
1. Right-click `streamforge_hacker.py`
2. Send to → Desktop (create shortcut)
3. Edit properties → Target:
   ```
   python "C:\path\to\streamforge_hacker.py"
   ```

### Start Menu Entry
```cmd
# Create shortcut in:
%APPDATA%\Microsoft\Windows\Start Menu\Programs
```

### Run on Startup
```cmd
# Copy shortcut to:
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
```

### Context Menu Integration
```cmd
# Right-click any video URL → "Download with StreamForge"
# Run: python setup_context_menu.py
```

## 📁 Default Locations

### Downloads
```
C:\Users\YourName\Downloads\StreamForge\
```

### Config
```
C:\Users\YourName\.streamforge\config\
```

### Logs
```
C:\Users\YourName\.streamforge\logs\
```

### Database
```
C:\Users\YourName\.streamforge\data\
```

## 🔧 Windows Commands

### Check Installation
```cmd
python --version
pip --version
ffmpeg -version
```

### Update StreamForge
```cmd
cd streamforge-pro
git pull origin main
pip install -r requirements_complete.txt --upgrade
```

### Clear Cache
```cmd
rmdir /s /q %USERPROFILE%\.streamforge\cache
```

### View Logs
```cmd
notepad %USERPROFILE%\.streamforge\logs\streamforge.log
```

## 🎨 Windows Customization

### PowerShell Profile
```powershell
# Edit profile
notepad $PROFILE

# Add alias
function sf { python C:\path\to\streamforge_hacker.py }
```

### CMD Alias
```cmd
# Create batch file: sf.bat in PATH
@echo off
python C:\path\to\streamforge_hacker.py %*
```

### Windows Terminal
```json
// Add to settings.json
{
  "name": "StreamForge-Pro",
  "commandline": "python C:\\path\\to\\streamforge_hacker.py",
  "icon": "🎬"
}
```

## 🚀 Performance Tips

### Use SSD
Move downloads to SSD for faster processing

### Increase RAM
```yaml
# Edit config: %USERPROFILE%\.streamforge\config\app_config.yml
download:
  max_concurrent: 5  # Increase for more RAM
```

### GPU Acceleration
```cmd
# Install CUDA for GPU encoding
pip install torch torchvision
```

### Disable Antivirus Scan
Add StreamForge folder to exclusions

## 🐛 Troubleshooting

### Python Not Found
```cmd
# Add to PATH
setx PATH "%PATH%;C:\Python39"
```

### FFmpeg Error
```cmd
# Download and add to PATH
# Or use: pip install ffmpeg-python
```

### Permission Denied
Run CMD/PowerShell as Administrator

### Module Not Found
```cmd
pip install -r requirements_complete.txt --force-reinstall
```

### Firewall Blocking
```cmd
# Allow in Windows Firewall
netsh advfirewall firewall add rule name="StreamForge" dir=in action=allow program="python.exe"
```

## 📊 System Requirements

- **Windows:** 10/11 (64-bit)
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
```cmd
set HTTP_PROXY=http://proxy:port
set HTTPS_PROXY=http://proxy:port
```

### Check Connection
```cmd
ping google.com
```

## 💾 Backup & Restore

### Backup Downloads
```cmd
xcopy /E /I C:\Users\YourName\Downloads\StreamForge D:\Backup\StreamForge
```

### Backup Config
```cmd
xcopy /E /I %USERPROFILE%\.streamforge D:\Backup\.streamforge
```

### Restore
```cmd
xcopy /E /I D:\Backup\StreamForge C:\Users\YourName\Downloads\StreamForge
```

## 🔐 Security

### Windows Defender
Add exclusion for StreamForge folder

### Encrypt Downloads
```cmd
# Use BitLocker or VeraCrypt
```

### Clear History
```cmd
del %USERPROFILE%\.streamforge\data\download_history.db
```

## 📱 Integration

### Browser Extension
1. Open Chrome/Edge
2. Go to `chrome://extensions`
3. Enable Developer Mode
4. Load unpacked: `src/streamforge/extensions/chrome`

### Windows Notifications
```python
# Automatic notifications on download complete
from win10toast import ToastNotifier
```

### Task Scheduler
```cmd
# Schedule downloads
schtasks /create /tn "StreamForge" /tr "python C:\path\to\streamforge_hacker.py" /sc daily /st 02:00
```

## 🎮 Advanced Usage

### Batch File for Quick Download
```batch
@echo off
echo Enter video URL:
set /p url=
python streamforge_hacker.py --url "%url%" --quality best
pause
```

### PowerShell Script
```powershell
param([string]$url)
python streamforge_hacker.py --url $url --quality best
```

### Scheduled Downloads
```cmd
# Download at specific time
schtasks /create /tn "DailyDownload" /tr "python streamforge_hacker.py" /sc daily /st 02:00
```

## 📞 Support

- **GitHub Issues:** https://github.com/RAJSARASWATI-JATAV/streamforge-pro/issues
- **Email:** rajsaraswatijatav@outlook.com
- **Telegram:** @Rajsaraswati_bot

## 🎉 Quick Start Commands

```cmd
# Install
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro
pip install -r requirements_complete.txt

# Run
python streamforge_hacker.py

# Update
cd streamforge-pro
git pull
pip install -r requirements_complete.txt --upgrade

# Uninstall
cd ..
rmdir /s /q streamforge-pro
```

## 🔥 Pro Tips

### Create Desktop Icon
1. Create shortcut of `streamforge_hacker.py`
2. Right-click → Properties
3. Change icon to custom .ico file

### Quick Access Toolbar
Pin StreamForge folder to Quick Access

### Windows Search
Index StreamForge folder for fast search

### Multiple Instances
```cmd
start python streamforge_hacker.py
start python streamforge_api.py
start python streamforge_live.py
```

---

**© 2025 RAJSARASWATI JATAV**
**Location: Gwalior, Madhya Pradesh, India**
**Made with ❤️ for Windows Users**
