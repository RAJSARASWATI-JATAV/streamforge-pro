# Browser Extension Guide

**Created by RAJSARASWATI JATAV**

## 🌐 StreamForge-Pro Browser Extension v2.1.0

### Features
- ✅ Auto-detect videos on any webpage
- ✅ One-click download
- ✅ Quality selection
- ✅ Batch download
- ✅ Download history
- ✅ Native app integration

---

## 📦 Installation

### Chrome/Edge
1. Open `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select `src/streamforge/extensions/chrome/`
5. Extension installed! ✅

### Firefox
1. Open `about:debugging#/runtime/this-firefox`
2. Click "Load Temporary Add-on"
3. Select `manifest.json` from `src/streamforge/extensions/firefox/`
4. Extension installed! ✅

---

## 🎯 Usage

### Detect Videos
1. Visit any video website
2. Click extension icon
3. Videos automatically detected
4. Click "Download" button

### Download Options
- Select quality (1080p, 720p, 480p, etc.)
- Choose format (MP4, WEBM, etc.)
- Set download location
- Enable/disable notifications

### Keyboard Shortcuts
- `Alt+D` - Quick download
- `Alt+Q` - Quality selector
- `Alt+H` - Show history

---

## 🔧 Configuration

### Settings
- Default quality
- Auto-download
- Notification preferences
- Download location
- Theme (Light/Dark)

### Native Messaging
Extension communicates with StreamForge-Pro desktop app for advanced features.

**Setup:**
```bash
python -m streamforge.extensions.native_host
```

---

## 🎤 Voice Commands Integration

Extension supports voice commands when native app is running:
- "Download this video"
- "Show download history"
- "Pause download"
- "Resume download"

---

## 🐛 Troubleshooting

### Extension not detecting videos
- Refresh the page
- Check if site is supported
- Update extension

### Download fails
- Check internet connection
- Verify download permissions
- Try different quality

### Native messaging error
- Install desktop app
- Run native host setup
- Check permissions

---

## 📞 Support

**Creator:** RAJSARASWATI JATAV  
**Email:** rajsaraswatijatav@outlook.com  
**GitHub:** @rajsaraswati | @RAJSARASWATI-JATAV

---

**© 2025 RAJSARASWATI JATAV - All Rights Reserved**
