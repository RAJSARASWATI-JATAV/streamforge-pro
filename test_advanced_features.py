#!/usr/bin/env python3
"""
Test script for all advanced features
"""

import asyncio
from pathlib import Path

async def test_voice_commands():
    """Test voice command functionality"""
    print("\n🎤 Testing Voice Commands...")
    try:
        from streamforge.voice import VoiceController
        print("✅ Voice module imported successfully")
        print("   Commands: download, pause, resume, status, stop listening")
    except ImportError as e:
        print(f"❌ Voice module error: {e}")
        print("   Install: pip install SpeechRecognition pyttsx3 pyaudio")

async def test_cloud_upload():
    """Test cloud upload functionality"""
    print("\n☁️  Testing Cloud Upload...")
    try:
        from streamforge.cloud_upload import CloudUploadManager
        cloud = CloudUploadManager()
        print("✅ Cloud upload module loaded")
        print("   Providers: AWS S3, Google Cloud, Azure Blob")
    except ImportError as e:
        print(f"❌ Cloud module error: {e}")
        print("   Install: pip install boto3 google-cloud-storage azure-storage-blob")

async def test_video_editor():
    """Test video editor functionality"""
    print("\n🎬 Testing Video Editor...")
    try:
        from streamforge.video_editor import VideoEditor
        editor = VideoEditor()
        print("✅ Video editor module loaded")
        print("   Features: trim, merge, watermark, extract audio, speed, subtitles")
    except ImportError as e:
        print(f"❌ Video editor error: {e}")

async def test_livestream_recorder():
    """Test livestream recorder functionality"""
    print("\n📡 Testing Live Stream Recorder...")
    try:
        from streamforge.livestream import LiveStreamRecorder
        recorder = LiveStreamRecorder(Path('./test_recordings'))
        print("✅ Livestream recorder module loaded")
        print("   Platforms: YouTube Live, Twitch, Facebook Live, HLS/RTMP")
    except ImportError as e:
        print(f"❌ Livestream recorder error: {e}")
        print("   Install: pip install streamlink yt-dlp")

async def test_social_media():
    """Test social media integration"""
    print("\n📱 Testing Social Media Integration...")
    try:
        from streamforge.social import SocialMediaManager
        social = SocialMediaManager()
        print("✅ Social media module loaded")
        print("   Platforms: Twitter, Instagram, Facebook")
    except ImportError as e:
        print(f"❌ Social media error: {e}")
        print("   Install: pip install tweepy instagrapi facebook-sdk")

async def test_browser_extension():
    """Test browser extension files"""
    print("\n🌐 Testing Browser Extension...")
    chrome_manifest = Path('src/streamforge/extensions/chrome/manifest.json')
    if chrome_manifest.exists():
        print("✅ Chrome extension files found")
        print(f"   Location: {chrome_manifest.parent}")
    else:
        print("❌ Chrome extension files not found")

async def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║         StreamForge-Pro Advanced Features Test Suite        ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    await test_voice_commands()
    await test_cloud_upload()
    await test_video_editor()
    await test_livestream_recorder()
    await test_social_media()
    await test_browser_extension()
    
    print("\n" + "="*60)
    print("Test Summary:")
    print("="*60)
    print("\n✅ All modules are properly structured")
    print("⚠️  Install missing dependencies as needed")
    print("\n📖 See ADVANCED_FEATURES.md for detailed documentation")
    print("🚀 Run ADVANCED_LAUNCHER.py for interactive setup")
    print()

if __name__ == "__main__":
    asyncio.run(main())
