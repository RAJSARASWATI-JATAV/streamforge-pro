# ⚡ Quick Start Guide - StreamForge-Pro v2.2.0

**Created by RAJSARASWATI JATAV**

## 🚀 Install & Run (30 seconds)

```bash
git clone https://github.com/RAJSARASWATI-JATAV/streamforge-pro.git
cd streamforge-pro
pip install -r requirements_complete.txt
python streamforge_hacker.py
```

## 🎯 Choose Your Interface

### 1. Hacker Edition (Recommended)
```bash
python streamforge_hacker.py
```
Matrix-style UI, cyberpunk aesthetics

### 2. API Server
```bash
python streamforge_api.py
```
Access: http://localhost:8000/docs

### 3. Live Server
```bash
python streamforge_live.py
```
Access: http://localhost:8080

### 4. Voice Control
```bash
python streamforge_voice.py
```
Say: "download", "pause", "resume"

## 📥 Quick Downloads

### YouTube
```python
from streamforge.core.simple_downloader import SimpleDownloader
SimpleDownloader().download("https://youtube.com/watch?v=...")
```

### Instagram (Zero Compression)
```python
from streamforge.social.instagram_pro import InstagramProDownloader
InstagramProDownloader().download_post("https://instagram.com/p/...")
```

### TikTok (No Watermark)
```python
from streamforge.social.tiktok_pro import TikTokProDownloader
TikTokProDownloader().download_video("https://tiktok.com/@user/video/...", no_watermark=True)
```

## 🎨 Customize Theme

```python
from streamforge.themes import ThemeManager
theme = ThemeManager()
theme.set_theme("cyberpunk")  # or ocean, sunset, forest, hacker
```

## 🔌 Use Plugins

```python
from streamforge.plugins import PluginManager
manager = PluginManager()
manager.load_all_plugins()
manager.list_plugins()
```

## 🌐 API Usage

```bash
curl -X POST http://localhost:8000/download \
  -H "Content-Type: application/json" \
  -d '{"url":"https://youtube.com/watch?v=...", "quality":"1080p"}'
```

## 🤖 AI Optimizer

```python
from streamforge.utils.ai_quality_optimizer import AIQualityOptimizer
ai = AIQualityOptimizer()
recommendations = ai.get_recommendations()
print(recommendations['recommended_quality'])
```

## ☁️ Cloud Upload

```python
from streamforge.cloud_upload import CloudManager
cloud = CloudManager()
cloud.upload_to_drive("video.mp4")
```

## 📊 Check Stats

```python
from streamforge.utils.analytics import Analytics
stats = Analytics().get_stats()
print(f"Total downloads: {stats['total']}")
```

## 🎯 All Features in One

```python
# Complete workflow
from streamforge.themes import ThemeManager
from streamforge.utils.ai_quality_optimizer import AIQualityOptimizer
from streamforge.core.simple_downloader import SimpleDownloader
from streamforge.cloud_upload import CloudManager

# 1. Set theme
ThemeManager().set_theme("cyberpunk")

# 2. Get AI recommendations
ai = AIQualityOptimizer()
quality = ai.get_recommendations()['recommended_quality']

# 3. Download
downloader = SimpleDownloader()
file = downloader.download(url, quality=quality)

# 4. Upload to cloud
CloudManager().upload_to_drive(file)
```

## 🆘 Need Help?

- **Docs**: Read all .md files
- **Issues**: https://github.com/RAJSARASWATI-JATAV/streamforge-pro/issues
- **Email**: rajsaraswatijatav@outlook.com
- **Telegram**: @Rajsaraswati_bot

---

**© 2025 RAJSARASWATI JATAV - Gwalior, India**
