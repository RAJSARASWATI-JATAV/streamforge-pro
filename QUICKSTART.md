# 🚀 StreamForge-Pro - Quick Start Guide

## 📦 Installation (5 Minutes)

### Step 1: Open Terminal/Command Prompt

**Windows:**
- Press `Win + R`
- Type `cmd` and press Enter

**Mac/Linux:**
- Press `Ctrl + Alt + T`

### Step 2: Navigate to Project

```bash
cd "c:\Users\Rajsa\Downloads\STREAM PROJECT"
```

### Step 3: Install StreamForge-Pro

```bash
# Install the package
pip install -e .

# Verify installation
python -m streamforge
```

### Step 4: Install FFmpeg (Required)

**Windows (Easy Method):**
```bash
# Using Chocolatey (if installed)
choco install ffmpeg

# Or download manually from: https://ffmpeg.org/download.html
```

**Mac:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg  # Ubuntu/Debian
```

---

## 🎬 Your First Download (1 Minute)

### Method 1: Using Python

Create a file `test_download.py`:

```python
import asyncio
from streamforge import __version__

async def main():
    print(f"🎬 StreamForge-Pro v{__version__}")
    print("✅ Installation successful!")
    print("\n📖 Next steps:")
    print("1. Implement core download engine")
    print("2. Add your favorite video URL")
    print("3. Start downloading!")

asyncio.run(main())
```

Run it:
```bash
python test_download.py
```

### Method 2: Using Command Line

```bash
# Run StreamForge
python -m streamforge

# You should see the welcome banner!
```

---

## 🛠️ Next Steps

### 1. Implement Core Download Function

Create `src/streamforge/core/simple_downloader.py`:

```python
import yt_dlp

def download_video(url, output_path="downloads"):
    """Simple video downloader"""
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"📥 Downloading: {url}")
        ydl.download([url])
        print("✅ Download complete!")

if __name__ == "__main__":
    # Test download
    url = input("Enter video URL: ")
    download_video(url)
```

### 2. Test Your Downloader

```bash
python src/streamforge/core/simple_downloader.py
```

Enter a YouTube URL and watch it download!

---

## 📚 Common Tasks

### Download a Video

```python
from streamforge.core.simple_downloader import download_video

# Download to default location
download_video("https://youtube.com/watch?v=VIDEO_ID")

# Download to custom location
download_video("https://youtube.com/watch?v=VIDEO_ID", "my_videos")
```

### Extract Audio Only

```python
import yt_dlp

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Usage
download_audio("https://youtube.com/watch?v=VIDEO_ID")
```

### Download with Progress

```python
import yt_dlp

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"📊 Progress: {d['_percent_str']} | Speed: {d['_speed_str']}")
    elif d['status'] == 'finished':
        print("✅ Download finished!")

def download_with_progress(url):
    ydl_opts = {
        'format': 'best',
        'progress_hooks': [progress_hook],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Usage
download_with_progress("https://youtube.com/watch?v=VIDEO_ID")
```

---

## 🎯 Project Structure Overview

```
STREAM PROJECT/
├── src/streamforge/          # Main package
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point
│   ├── core/                # Core functionality
│   ├── cli/                 # Command-line interface
│   ├── gui/                 # Graphical interface
│   ├── web/                 # Web interface
│   ├── models/              # Data models
│   ├── utils/               # Utility functions
│   └── config/              # Configuration
├── tests/                   # Test files
├── docs/                    # Documentation
├── requirements.txt         # Dependencies
├── setup.py                # Installation script
└── README.md               # Main documentation
```

---

## 💡 Tips & Tricks

### 1. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install StreamForge
pip install -e .
```

### 2. Check Supported Sites

```python
import yt_dlp

# Get list of supported sites
ydl = yt_dlp.YoutubeDL()
sites = ydl._get_supported_sites()
print(f"Supported sites: {len(sites)}")
print(sites[:10])  # Show first 10
```

### 3. Download Playlist

```python
def download_playlist(playlist_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(playlist)s/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Usage
download_playlist("https://youtube.com/playlist?list=PLAYLIST_ID")
```

---

## 🐛 Troubleshooting

### Problem: "yt-dlp not found"

**Solution:**
```bash
pip install yt-dlp
```

### Problem: "FFmpeg not found"

**Solution:**
- Windows: Download from https://ffmpeg.org/download.html
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

### Problem: "Permission denied"

**Solution:**
```bash
# Run as administrator (Windows)
# Or use sudo (Mac/Linux)
sudo pip install -e .
```

### Problem: "Module not found"

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

---

## 📖 Learning Resources

### Official Documentation
- **YT-DLP**: https://github.com/yt-dlp/yt-dlp
- **Python Async**: https://docs.python.org/3/library/asyncio.html
- **Click (CLI)**: https://click.palletsprojects.com/

### Video Tutorials
- Python Async Programming
- Building CLI Applications
- Working with FFmpeg

### Community
- GitHub Issues: Report bugs and ask questions
- Discord: Join our community (coming soon)
- Stack Overflow: Tag your questions with `streamforge`

---

## 🎓 Next Learning Steps

### Week 1: Basics
- [ ] Understand project structure
- [ ] Learn yt-dlp basics
- [ ] Create simple download script
- [ ] Test with different URLs

### Week 2: Intermediate
- [ ] Implement download manager
- [ ] Add progress tracking
- [ ] Handle errors gracefully
- [ ] Add quality selection

### Week 3: Advanced
- [ ] Create CLI interface
- [ ] Add configuration system
- [ ] Implement database storage
- [ ] Add batch downloads

### Week 4: Expert
- [ ] Build GUI interface
- [ ] Create web API
- [ ] Add cloud sync
- [ ] Implement AI features

---

## 🎉 Success Checklist

- [x] ✅ Project structure created
- [x] ✅ Dependencies installed
- [x] ✅ FFmpeg installed
- [ ] ⏳ First download completed
- [ ] ⏳ Core engine implemented
- [ ] ⏳ CLI interface working
- [ ] ⏳ Tests written
- [ ] ⏳ Documentation complete

---

## 🚀 Ready to Code!

You're all set! Start with:

1. **Test the installation**: `python -m streamforge`
2. **Create simple downloader**: Follow examples above
3. **Implement core features**: Check PROJECT_COMPLETE.md
4. **Build your vision**: Make it your own!

---

## 📞 Need Help?

- **Documentation**: Read README.md
- **Examples**: Check code snippets above
- **Issues**: Create GitHub issue
- **Email**: raj@streamforge.pro

---

**Happy Coding! 🎊**

*Made with ❤️ by Raj Saraswati*
