# 🚀 Quick Start - Advanced Features

## Installation

```bash
# Install all advanced features
pip install -r requirements_advanced.txt

# Or install specific features
pip install SpeechRecognition pyttsx3 pyaudio  # Voice
pip install boto3 google-cloud-storage azure-storage-blob  # Cloud
pip install streamlink yt-dlp  # Livestream
pip install tweepy instagrapi facebook-sdk  # Social Media
```

## 1. Browser Extension (5 minutes)

### Chrome:
1. Open `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select `src/streamforge/extensions/chrome/`

### Firefox:
1. Open `about:debugging`
2. Click "Load Temporary Add-on"
3. Select `src/streamforge/extensions/firefox/manifest.json`

**Usage:** Click extension icon on any video page → Select quality → Download!

---

## 2. Voice Commands (2 minutes)

```python
from streamforge.voice import VoiceController

voice = VoiceController(download_manager)
await voice.start_listening()

# Say: "Download https://youtube.com/watch?v=VIDEO_ID"
# Say: "Status"
# Say: "Stop listening"
```

---

## 3. Cloud Upload (3 minutes)

```python
from streamforge.cloud_upload import CloudUploadManager

cloud = CloudUploadManager()

# AWS S3
cloud.configure_aws('ACCESS_KEY', 'SECRET_KEY', 'bucket-name')
url = await cloud.upload_to_aws('video.mp4')
print(f"Uploaded: {url}")
```

---

## 4. Video Editor (2 minutes)

```python
from streamforge.video_editor import VideoEditor

editor = VideoEditor()

# Add watermark
await editor.add_watermark('input.mp4', 'output.mp4', '© Raj Saraswati')

# Create GIF
await editor.create_gif('video.mp4', 'animation.gif', start='5', duration='3')
```

---

## 5. Live Stream Recording (3 minutes)

```python
from streamforge.livestream import LiveStreamRecorder

recorder = LiveStreamRecorder('./recordings')

# Record YouTube live
recording_id = await recorder.record_youtube_live(
    'https://youtube.com/watch?v=LIVE_ID',
    quality='1080p'
)

# Stop recording
await recorder.stop_recording(recording_id)
```

---

## 6. Social Media Integration (5 minutes)

```python
from streamforge.social import SocialMediaManager

social = SocialMediaManager()

# Configure Twitter
social.configure_twitter(
    api_key='YOUR_KEY',
    api_secret='YOUR_SECRET',
    access_token='YOUR_TOKEN',
    access_secret='YOUR_SECRET'
)

# Post to Twitter
result = await social.post_to_twitter(
    'Check out this video! 🎬',
    media_path='video.mp4'
)
```

---

## Complete Workflow Example

```python
import asyncio
from streamforge import DownloadManager
from streamforge.cloud_upload import CloudUploadManager
from streamforge.video_editor import VideoEditor
from streamforge.social import SocialMediaManager

async def complete_workflow():
    # 1. Download
    dm = DownloadManager()
    await dm.initialize()
    job_id = await dm.add_download('https://youtube.com/watch?v=VIDEO_ID')
    
    # Wait for download
    while not dm.get_download_status(job_id).is_complete:
        await asyncio.sleep(1)
    
    file_path = dm.get_download_path(job_id)
    
    # 2. Edit
    editor = VideoEditor()
    edited = 'edited.mp4'
    await editor.add_watermark(file_path, edited, '© Raj Saraswati')
    
    # 3. Upload to cloud
    cloud = CloudUploadManager()
    cloud.configure_aws('key', 'secret', 'bucket')
    cloud_url = await cloud.upload_to_aws(edited)
    
    # 4. Share on social media
    social = SocialMediaManager()
    social.configure_twitter('key', 'secret', 'token', 'secret')
    await social.post_to_twitter(f'My video: {cloud_url}', edited)
    
    print("✅ Complete workflow finished!")

asyncio.run(complete_workflow())
```

---

## Interactive Launcher

```bash
# Run the interactive launcher
python ADVANCED_LAUNCHER.py
```

This will show you a menu with all features and examples!

---

## Test All Features

```bash
# Test if everything is working
python test_advanced_features.py
```

---

## CLI Commands

```bash
# Voice control
streamforge --voice

# Cloud upload
streamforge --download URL --upload-to aws

# Video editing
streamforge edit watermark video.mp4 output.mp4 --text "© Raj"

# Live recording
streamforge record https://youtube.com/watch?v=LIVE_ID

# Social media
streamforge --download URL --share twitter,facebook
```

---

## Configuration File

Create `~/.streamforge/config/advanced.yml`:

```yaml
voice:
  enabled: true
  
cloud:
  auto_upload: true
  provider: aws
  
editor:
  auto_watermark: true
  watermark_text: "© Raj Saraswati"
  
social:
  auto_share: true
  platforms:
    - twitter
    - facebook
```

---

## Need Help?

- 📖 Full docs: `ADVANCED_FEATURES.md`
- 🚀 Interactive setup: `python ADVANCED_LAUNCHER.py`
- 🧪 Test features: `python test_advanced_features.py`
- 💬 Support: support@streamforge.pro

---

**Total setup time: ~20 minutes**

**Created by Raj Saraswati** 🎬
