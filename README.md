# 🎬 StreamForge-Pro

**Advanced Multi-Platform Media Downloader**

Created by **Raj Saraswati** (@rajsaraswati)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](https://github.com/rajsaraswati/streamforge-pro)

---

## 🌟 Features

### Core Features
- ✅ **Multi-Platform Support**: YouTube, Twitter, Instagram, Facebook, TikTok, Twitch, Vimeo, and 1000+ sites
- ✅ **Multiple Interfaces**: CLI, GUI, Web, and Mobile/Termux
- ✅ **Smart Quality Selection**: AI-powered automatic quality optimization
- ✅ **Batch Downloads**: Download multiple videos simultaneously
- ✅ **Playlist Support**: Full playlist and channel downloads
- ✅ **Format Conversion**: Convert between video/audio formats
- ✅ **Subtitle Support**: Download and embed subtitles
- ✅ **Thumbnail Extraction**: Auto-generate and save thumbnails

### Advanced Features
- 🚀 **Intelligent Download Manager**: Priority queuing, retry logic, resume support
- 🎯 **Quality Selector**: Automatic quality selection based on network and device
- 🔄 **Stream Processor**: Post-processing, format conversion, watermarking
- 📊 **Analytics Dashboard**: Track download statistics and performance
- ☁️ **Cloud Sync**: Sync downloads across devices (optional)
- 🔐 **Security**: Encrypted storage, secure authentication
- 🌐 **Internationalization**: Support for 15+ languages
- 📱 **Mobile Optimized**: Full Termux and Android support

---

## 📦 Installation

### Quick Install (Recommended)

```bash
# Clone repository
git clone https://github.com/rajsaraswati/streamforge-pro.git
cd streamforge-pro

# Install with pip
pip install -e .
```

### Install with Specific Features

```bash
# CLI only (minimal)
pip install -e .

# With GUI
pip install -e ".[gui]"

# With Web Interface
pip install -e ".[web]"

# With Mobile Support
pip install -e ".[mobile]"

# Everything
pip install -e ".[all]"

# Development
pip install -e ".[dev]"
```

### System Requirements

- **Python**: 3.8 or higher
- **FFmpeg**: Required for format conversion
- **Operating Systems**: Windows, macOS, Linux, Android (Termux)

#### Install FFmpeg

**Windows:**
```bash
# Using Chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch
sudo pacman -S ffmpeg
```

**Android (Termux):**
```bash
pkg install ffmpeg
```

---

## 🚀 Quick Start

### Command Line Interface (CLI)

```bash
# Quick download
streamforge --download "https://youtube.com/watch?v=VIDEO_ID"

# Download playlist
streamforge --playlist "https://youtube.com/playlist?list=PLAYLIST_ID"

# Batch download from file
streamforge --batch urls.txt

# Interactive mode
streamforge --cli

# Specify quality
streamforge --download "URL" --quality 1080p

# Extract audio only
streamforge --download "URL" --format mp3

# Custom output directory
streamforge --download "URL" --output ~/Downloads/Videos
```

### Graphical User Interface (GUI)

```bash
# Launch GUI
streamforge --gui
```

### Web Interface

```bash
# Start web server
streamforge --web

# Custom host and port
streamforge-web --host 0.0.0.0 --port 8000

# Access at: http://localhost:8000
```

### Mobile/Termux

```bash
# Launch mobile interface
streamforge --mobile
```

---

## 📖 Usage Examples

### Python API

```python
import asyncio
from streamforge import DownloadManager, YTDLPEngine

async def main():
    # Initialize download manager
    manager = DownloadManager()
    await manager.initialize()
    
    # Add download
    job_id = await manager.add_download(
        url="https://youtube.com/watch?v=VIDEO_ID",
        quality="1080p"
    )
    
    # Monitor progress
    while True:
        status = manager.get_download_status(job_id)
        if status.is_complete:
            break
        print(f"Progress: {status.progress}%")
        await asyncio.sleep(1)
    
    await manager.shutdown()

asyncio.run(main())
```

### Advanced Configuration

```python
from streamforge import DownloadManagerConfig, QualityProfile

# Custom configuration
config = DownloadManagerConfig(
    max_concurrent_downloads=5,
    enable_bandwidth_limiting=True,
    bandwidth_limit_mbps=10.0,
    enable_retry=True,
    retry_attempts=3
)

# Custom quality profile
profile = QualityProfile(
    name="My Profile",
    strategy=SelectionStrategy.BALANCED,
    max_resolution="1080p",
    max_filesize_mb=500
)
```

---

## 🎨 Interfaces

### 1. Command Line Interface (CLI)
- Interactive menu system
- Rich terminal UI with progress bars
- Keyboard shortcuts
- Batch operations

### 2. Graphical User Interface (GUI)
- Modern Qt6-based interface
- Drag-and-drop support
- Real-time progress tracking
- Download queue management
- Settings panel

### 3. Web Interface
- Responsive web design
- RESTful API
- WebSocket for real-time updates
- Multi-user support
- Remote access capability

### 4. Mobile Interface (Termux)
- Touch-optimized UI
- Notification support
- Background downloads
- Storage management

---

## ⚙️ Configuration

### Configuration File

Create `~/.streamforge/config/app_config.yml`:

```yaml
# StreamForge-Pro Configuration

download:
  output_directory: ~/Downloads/StreamForge
  max_concurrent: 5
  enable_resume: true
  
quality:
  default_profile: balanced
  auto_select: true
  prefer_format: mp4
  
network:
  timeout: 30
  retries: 3
  bandwidth_limit: 0  # 0 = unlimited
  
processing:
  enable_conversion: true
  enable_thumbnails: true
  enable_subtitles: true
  
security:
  enable_encryption: false
  require_authentication: false
```

### Environment Variables

```bash
export STREAMFORGE_CONFIG=~/.streamforge/config/app_config.yml
export STREAMFORGE_DATA_DIR=~/.streamforge/data
export STREAMFORGE_DEBUG=false
```

---

## 🔧 Advanced Features

### Scheduling Downloads

```bash
# Schedule download for later
streamforge schedule --url "URL" --time "2024-01-20 14:30"

# Recurring downloads (subscriptions)
streamforge subscribe --channel "CHANNEL_URL" --frequency daily
```

### Format Conversion

```bash
# Convert video format
streamforge convert input.webm output.mp4 --quality high

# Extract audio
streamforge extract-audio video.mp4 audio.mp3 --bitrate 320k

# Add watermark
streamforge watermark input.mp4 output.mp4 --text "© Raj Saraswati"
```

### Batch Operations

```bash
# Create batch file (urls.txt)
https://youtube.com/watch?v=VIDEO1
https://youtube.com/watch?v=VIDEO2
https://youtube.com/watch?v=VIDEO3

# Process batch
streamforge batch urls.txt --quality 720p --format mp4
```

---

## 🐳 Docker Support

### Using Docker

```bash
# Build image
docker build -t streamforge-pro .

# Run container
docker run -d \
  -p 8000:8000 \
  -v $(pwd)/downloads:/data/downloads \
  streamforge-pro

# Using docker-compose
docker-compose up -d
```

### Docker Compose

```yaml
version: '3.8'

services:
  streamforge:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./downloads:/data/downloads
      - ./config:/data/config
    environment:
      - STREAMFORGE_DATA_DIR=/data
    restart: unless-stopped
```

---

## 📊 Supported Platforms

### Video Platforms
- YouTube (videos, playlists, channels, live streams)
- Twitter/X
- Instagram (posts, reels, stories)
- Facebook (videos, watch)
- TikTok
- Twitch (VODs, clips)
- Vimeo
- Dailymotion
- Rumble
- Bilibili

### Audio Platforms
- SoundCloud
- Spotify (with premium)
- Bandcamp
- Mixcloud

### Educational Platforms
- Coursera
- Udemy
- Khan Academy
- TED Talks
- edX

**Total: 1000+ supported sites via yt-dlp**

---

## 🛠️ Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/rajsaraswati/streamforge-pro.git
cd streamforge-pro

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Code formatting
black src/

# Linting
flake8 src/

# Type checking
mypy src/
```

### Project Structure

```
streamforge-pro/
├── src/
│   └── streamforge/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core/           # Core engines
│       ├── cli/            # CLI interface
│       ├── gui/            # GUI interface
│       ├── web/            # Web interface
│       ├── mobile/         # Mobile interface
│       ├── models/         # Data models
│       ├── database/       # Database layer
│       ├── utils/          # Utilities
│       ├── config/         # Configuration
│       └── logging/        # Logging system
├── tests/                  # Test suite
├── docs/                   # Documentation
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide
- Write tests for new features
- Update documentation
- Add type hints
- Use meaningful commit messages

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Raj Saraswati**

- GitHub: [@rajsaraswati](https://github.com/rajsaraswati)
- Website: [rajsaraswati.dev](https://rajsaraswati.dev)
- Email: raj@streamforge.pro

---

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Core download engine
- [FFmpeg](https://ffmpeg.org/) - Media processing
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) - GUI framework
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/rajsaraswati/streamforge-pro/issues)
- **Discussions**: [GitHub Discussions](https://github.com/rajsaraswati/streamforge-pro/discussions)
- **Discord**: [Join our Discord](https://discord.gg/streamforge)
- **Email**: support@streamforge.pro

---

## 🗺️ Roadmap

### Version 1.1 (Q2 2024)
- [ ] Browser extension (Chrome, Firefox)
- [ ] Voice command support
- [ ] Advanced AI quality prediction
- [ ] Multi-language subtitle generation

### Version 2.0 (Q3 2024)
- [ ] Blockchain-based content verification
- [ ] VR interface support
- [ ] Distributed download network
- [ ] Advanced analytics dashboard

---

## ⚠️ Disclaimer

This tool is for personal use only. Please respect copyright laws and terms of service of the platforms you download from. The developers are not responsible for any misuse of this software.

---

## 📈 Statistics

![GitHub stars](https://img.shields.io/github/stars/rajsaraswati/streamforge-pro?style=social)
![GitHub forks](https://img.shields.io/github/forks/rajsaraswati/streamforge-pro?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/rajsaraswati/streamforge-pro?style=social)

---

**Made with ❤️ by Raj Saraswati**

*StreamForge-Pro - Download Smarter, Not Harder*
