"""Instagram Pro - Highest Quality Downloader (No Compression)"""
import yt_dlp
import requests
import json
from pathlib import Path
import re

class InstagramProDownloader:
    """Instagram Highest Quality Downloader - Zero Compression"""
    
    def __init__(self, output_dir="downloads/instagram"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Instagram 219.0.0.12.117 Android',
            'Accept': '*/*',
            'Accept-Language': 'en-US',
        })
    
    def download_post(self, url, force_highest=True):
        """Download Instagram post in HIGHEST quality (no compression)"""
        print(f"\n📸 Instagram Pro Downloader")
        print(f"🎯 Mode: HIGHEST QUALITY (Zero Compression)")
        print(f"🔗 URL: {url}")
        
        # Extract post info
        post_info = self._extract_post_info(url)
        
        if not post_info:
            print("❌ Failed to extract post info")
            return False
        
        # Download with highest quality settings
        return self._download_highest_quality(url, post_info)
    
    def _extract_post_info(self, url):
        """Extract post information"""
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
            print(f"⚠️ Standard extraction failed, trying alternative method...")
            return self._alternative_extraction(url)
    
    def _alternative_extraction(self, url):
        """Alternative extraction method for Instagram"""
        try:
            # Extract shortcode from URL
            shortcode = re.search(r'instagram.com/(?:p|reel|tv)/([^/?]+)', url)
            if not shortcode:
                return None
            
            shortcode = shortcode.group(1)
            
            # Use Instagram's GraphQL API
            api_url = f"https://www.instagram.com/p/{shortcode}/?__a=1&__d=dis"
            response = self.session.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                return self._parse_instagram_data(data)
            
            return None
        except Exception as e:
            print(f"❌ Alternative extraction failed: {e}")
            return None
    
    def _parse_instagram_data(self, data):
        """Parse Instagram API data"""
        try:
            media = data['items'][0]
            return {
                'title': media.get('caption', {}).get('text', 'instagram_post')[:50],
                'id': media['id'],
                'type': media['media_type'],
            }
        except:
            return None
    
    def _download_highest_quality(self, url, post_info):
        """Download in ABSOLUTE HIGHEST quality"""
        
        # CRITICAL: Instagram highest quality settings
        ydl_opts = {
            'format': 'best',  # Always best available
            'outtmpl': str(self.output_dir / '%(title)s_ORIGINAL.%(ext)s'),
            
            # HIGHEST QUALITY SETTINGS
            'format_sort': [
                'res:2160',  # Prefer 4K
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
            'keepvideo': True,  # Keep original
            'no_post_overwrites': True,
            
            # METADATA PRESERVATION
            'writethumbnail': True,
            'write_all_thumbnails': True,
            'writeinfojson': True,
            'writedescription': True,
            
            # DOWNLOAD SETTINGS
            'retries': 10,
            'fragment_retries': 10,
            'concurrent_fragment_downloads': 5,
            
            # PROGRESS
            'progress_hooks': [self._progress_hook],
            'quiet': False,
            'no_warnings': False,
        }
        
        try:
            print("\n⏳ Downloading HIGHEST quality (no compression)...")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            print("\n✅ Downloaded in ORIGINAL quality!")
            print("📊 Quality: HIGHEST (Zero Compression)")
            print("🎯 Format: Original Instagram quality preserved")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Download failed: {e}")
            print("🔄 Trying alternative method...")
            return self._fallback_download(url)
    
    def _fallback_download(self, url):
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
    
    def download_story(self, username):
        """Download Instagram stories (highest quality)"""
        print(f"\n📖 Downloading stories from @{username}")
        print("⚠️ Note: Stories require authentication")
        
        # Stories download logic
        url = f"https://www.instagram.com/stories/{username}/"
        return self.download_post(url)
    
    def download_reel(self, url):
        """Download Instagram Reel (highest quality)"""
        print(f"\n🎬 Downloading Instagram Reel")
        return self.download_post(url, force_highest=True)
    
    def download_igtv(self, url):
        """Download IGTV (highest quality)"""
        print(f"\n📺 Downloading IGTV")
        return self.download_post(url, force_highest=True)
    
    def batch_download(self, urls):
        """Batch download multiple Instagram posts"""
        print(f"\n📋 Batch downloading {len(urls)} posts")
        
        results = []
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Processing...")
            success = self.download_post(url)
            results.append({'url': url, 'success': success})
        
        successful = sum(1 for r in results if r['success'])
        print(f"\n✅ Batch complete: {successful}/{len(urls)} successful")
        return results

def main():
    print("="*70)
    print("📸 INSTAGRAM PRO - HIGHEST QUALITY DOWNLOADER")
    print("🎯 Zero Compression | Original Quality Preserved")
    print("="*70)
    
    downloader = InstagramProDownloader()
    
    print("\n📋 Options:")
    print("1. Download Post/Video (Highest Quality)")
    print("2. Download Reel (Highest Quality)")
    print("3. Download IGTV (Highest Quality)")
    print("4. Download Story (Requires Auth)")
    print("5. Batch Download")
    
    choice = input("\n👉 Select: ").strip()
    
    if choice == '1':
        url = input("\n📝 Enter Instagram post URL: ")
        downloader.download_post(url)
    elif choice == '2':
        url = input("\n📝 Enter Instagram Reel URL: ")
        downloader.download_reel(url)
    elif choice == '3':
        url = input("\n📝 Enter IGTV URL: ")
        downloader.download_igtv(url)
    elif choice == '4':
        username = input("\n📝 Enter username: ")
        downloader.download_story(username)
    elif choice == '5':
        print("\n📝 Enter URLs (one per line, empty to finish):")
        urls = []
        while True:
            url = input()
            if not url:
                break
            urls.append(url)
        if urls:
            downloader.batch_download(urls)

if __name__ == "__main__":
    main()
