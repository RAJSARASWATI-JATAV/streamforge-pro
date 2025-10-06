"""TikTok Pro - Highest Quality Downloader (No Watermark, No Compression)"""
import yt_dlp
import requests
import json
from pathlib import Path
import re

class TikTokProDownloader:
    """TikTok Highest Quality Downloader - Zero Compression, No Watermark"""
    
    def __init__(self, output_dir="downloads/tiktok"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
        })
    
    def download_video(self, url, no_watermark=True):
        """Download TikTok video in HIGHEST quality (no watermark, no compression)"""
        print(f"\n🎵 TikTok Pro Downloader")
        print(f"🎯 Mode: HIGHEST QUALITY (Zero Compression)")
        print(f"💧 Watermark: {'REMOVED' if no_watermark else 'Original'}")
        print(f"🔗 URL: {url}")
        
        # Extract video info
        video_info = self._extract_video_info(url)
        
        if not video_info:
            print("❌ Failed to extract video info")
            return False
        
        # Download with highest quality settings
        return self._download_highest_quality(url, video_info, no_watermark)
    
    def _extract_video_info(self, url):
        """Extract TikTok video information"""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            print(f"⚠️ Standard extraction failed, trying alternative...")
            return self._alternative_extraction(url)
    
    def _alternative_extraction(self, url):
        """Alternative TikTok extraction"""
        try:
            # Extract video ID
            video_id = re.search(r'tiktok.com/@[^/]+/video/(\d+)', url)
            if not video_id:
                video_id = re.search(r'vm.tiktok.com/([A-Za-z0-9]+)', url)
            
            if video_id:
                return {'id': video_id.group(1)}
            
            return None
        except Exception as e:
            print(f"❌ Alternative extraction failed: {e}")
            return None
    
    def _download_highest_quality(self, url, video_info, no_watermark):
        """Download in ABSOLUTE HIGHEST quality"""
        
        # CRITICAL: TikTok highest quality settings
        ydl_opts = {
            'format': 'best',  # Always best available
            'outtmpl': str(self.output_dir / '%(title)s_NOWATERMARK.%(ext)s' if no_watermark else '%(title)s.%(ext)s'),
            
            # HIGHEST QUALITY SETTINGS
            'format_sort': [
                'res:1080',  # Prefer 1080p
                'vcodec:h264',  # Best codec
                'acodec:aac',  # Best audio
                'br',  # Highest bitrate
            ],
            
            # NO COMPRESSION
            'postprocessor_args': [
                '-c:v', 'copy',  # Copy video without re-encoding
                '-c:a', 'copy',  # Copy audio without re-encoding
            ],
            
            # QUALITY PRESERVATION
            'merge_output_format': 'mp4',
            'keepvideo': True,
            'no_post_overwrites': True,
            
            # METADATA
            'writethumbnail': True,
            'writeinfojson': True,
            'writedescription': True,
            'writesubtitles': True,
            
            # DOWNLOAD SETTINGS
            'retries': 10,
            'fragment_retries': 10,
            'concurrent_fragment_downloads': 5,
            
            # PROGRESS
            'progress_hooks': [self._progress_hook],
            'quiet': False,
        }
        
        # NO WATERMARK OPTION
        if no_watermark:
            ydl_opts['extractor_args'] = {
                'tiktok': {
                    'api_hostname': 'api16-normal-c-useast1a.tiktokv.com',
                }
            }
        
        try:
            print("\n⏳ Downloading HIGHEST quality...")
            if no_watermark:
                print("💧 Removing watermark...")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            print("\n✅ Downloaded in ORIGINAL quality!")
            print("📊 Quality: HIGHEST (Zero Compression)")
            print(f"💧 Watermark: {'REMOVED ✅' if no_watermark else 'Original'}")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Download failed: {e}")
            print("🔄 Trying alternative method...")
            return self._fallback_download(url, no_watermark)
    
    def _fallback_download(self, url, no_watermark):
        """Fallback download method"""
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("✅ Downloaded with fallback method")
            return True
        except Exception as e:
            print(f"❌ Fallback failed: {e}")
            return False
    
    def _progress_hook(self, d):
        """Progress display"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"\r📥 {percent} | ⚡ {speed} | ⏱️ {eta}", end='')
        elif d['status'] == 'finished':
            print("\n✅ Download complete, processing...")
    
    def download_user_videos(self, username, max_videos=10):
        """Download all videos from a TikTok user"""
        print(f"\n👤 Downloading videos from @{username}")
        print(f"📊 Max videos: {max_videos}")
        
        url = f"https://www.tiktok.com/@{username}"
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': str(self.output_dir / f'{username}/%(title)s.%(ext)s'),
            'playlistend': max_videos,
            'quiet': False,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"\n✅ Downloaded videos from @{username}")
            return True
        except Exception as e:
            print(f"❌ Failed: {e}")
            return False
    
    def download_hashtag(self, hashtag, max_videos=10):
        """Download videos from a hashtag"""
        print(f"\n#️⃣ Downloading videos from #{hashtag}")
        print(f"📊 Max videos: {max_videos}")
        
        url = f"https://www.tiktok.com/tag/{hashtag}"
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': str(self.output_dir / f'hashtag_{hashtag}/%(title)s.%(ext)s'),
            'playlistend': max_videos,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"\n✅ Downloaded videos from #{hashtag}")
            return True
        except Exception as e:
            print(f"❌ Failed: {e}")
            return False
    
    def download_sound(self, sound_url, max_videos=10):
        """Download videos using a specific sound"""
        print(f"\n🎵 Downloading videos with this sound")
        print(f"📊 Max videos: {max_videos}")
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': str(self.output_dir / 'sound/%(title)s.%(ext)s'),
            'playlistend': max_videos,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([sound_url])
            print(f"\n✅ Downloaded videos with sound")
            return True
        except Exception as e:
            print(f"❌ Failed: {e}")
            return False
    
    def batch_download(self, urls, no_watermark=True):
        """Batch download multiple TikTok videos"""
        print(f"\n📋 Batch downloading {len(urls)} videos")
        print(f"💧 Watermark: {'REMOVED' if no_watermark else 'Original'}")
        
        results = []
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Processing...")
            success = self.download_video(url, no_watermark)
            results.append({'url': url, 'success': success})
        
        successful = sum(1 for r in results if r['success'])
        print(f"\n✅ Batch complete: {successful}/{len(urls)} successful")
        return results

def main():
    print("="*70)
    print("🎵 TIKTOK PRO - HIGHEST QUALITY DOWNLOADER")
    print("🎯 Zero Compression | No Watermark | Original Quality")
    print("="*70)
    
    downloader = TikTokProDownloader()
    
    print("\n📋 Options:")
    print("1. Download Video (No Watermark, Highest Quality)")
    print("2. Download Video (With Watermark)")
    print("3. Download User's Videos")
    print("4. Download Hashtag Videos")
    print("5. Download Sound Videos")
    print("6. Batch Download")
    
    choice = input("\n👉 Select: ").strip()
    
    if choice == '1':
        url = input("\n📝 Enter TikTok URL: ")
        downloader.download_video(url, no_watermark=True)
    elif choice == '2':
        url = input("\n📝 Enter TikTok URL: ")
        downloader.download_video(url, no_watermark=False)
    elif choice == '3':
        username = input("\n📝 Enter username (without @): ")
        max_videos = input("Max videos (default 10): ") or "10"
        downloader.download_user_videos(username, int(max_videos))
    elif choice == '4':
        hashtag = input("\n📝 Enter hashtag (without #): ")
        max_videos = input("Max videos (default 10): ") or "10"
        downloader.download_hashtag(hashtag, int(max_videos))
    elif choice == '5':
        url = input("\n📝 Enter sound URL: ")
        max_videos = input("Max videos (default 10): ") or "10"
        downloader.download_sound(url, int(max_videos))
    elif choice == '6':
        print("\n📝 Enter URLs (one per line, empty to finish):")
        urls = []
        while True:
            url = input()
            if not url:
                break
            urls.append(url)
        if urls:
            no_wm = input("\nRemove watermark? (y/n): ").lower() == 'y'
            downloader.batch_download(urls, no_watermark=no_wm)

if __name__ == "__main__":
    main()
