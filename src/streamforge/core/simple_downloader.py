"""
Simple Video Downloader - StreamForge-Pro
A basic implementation to get you started
"""

import yt_dlp
import os
from pathlib import Path


class SimpleDownloader:
    """Simple video downloader using yt-dlp"""
    
    def __init__(self, output_dir="downloads"):
        """Initialize downloader with output directory"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def download(self, url, quality="best", audio_only=False):
        """
        Download video from URL
        
        Args:
            url: Video URL to download
            quality: Video quality (best, 1080p, 720p, 480p, etc.)
            audio_only: Extract audio only (mp3)
        """
        print(f"\n🎬 StreamForge-Pro Downloader")
        print(f"📥 URL: {url}")
        print(f"📁 Output: {self.output_dir}")
        print(f"🎯 Quality: {quality}")
        
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best' if audio_only else f'best[height<={quality.replace("p", "")}]' if quality != 'best' else 'best',
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'progress_hooks': [self._progress_hook],
        }
        
        # Add audio extraction if needed
        if audio_only:
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print("\n⏳ Starting download...")
                ydl.download([url])
                print("\n✅ Download complete!")
                return True
                
        except Exception as e:
            print(f"\n❌ Error: {e}")
            return False
    
    def _progress_hook(self, d):
        """Display download progress"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"\r📊 Progress: {percent} | Speed: {speed} | ETA: {eta}", end='')
        elif d['status'] == 'finished':
            print("\n🎉 Download finished, processing...")
    
    def get_video_info(self, url):
        """Get video information without downloading"""
        ydl_opts = {'quiet': True}
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                print(f"\n📺 Video Information:")
                print(f"   Title: {info.get('title', 'N/A')}")
                print(f"   Uploader: {info.get('uploader', 'N/A')}")
                print(f"   Duration: {info.get('duration', 0)} seconds")
                print(f"   Views: {info.get('view_count', 'N/A')}")
                print(f"   Upload Date: {info.get('upload_date', 'N/A')}")
                
                return info
                
        except Exception as e:
            print(f"❌ Error getting info: {e}")
            return None


def main():
    """Main function for testing"""
    print("🎬 StreamForge-Pro Simple Downloader")
    print("=" * 50)
    
    # Create downloader
    downloader = SimpleDownloader()
    
    # Get URL from user
    url = input("\n📝 Enter video URL: ").strip()
    
    if not url:
        print("❌ No URL provided!")
        return
    
    # Ask for options
    print("\n🎯 Download Options:")
    print("1. Best quality video")
    print("2. 1080p video")
    print("3. 720p video")
    print("4. Audio only (MP3)")
    
    choice = input("\nSelect option (1-4): ").strip()
    
    # Download based on choice
    if choice == "1":
        downloader.download(url, quality="best")
    elif choice == "2":
        downloader.download(url, quality="1080p")
    elif choice == "3":
        downloader.download(url, quality="720p")
    elif choice == "4":
        downloader.download(url, audio_only=True)
    else:
        print("❌ Invalid choice!")
        return
    
    print("\n✨ Thank you for using StreamForge-Pro!")


if __name__ == "__main__":
    main()
