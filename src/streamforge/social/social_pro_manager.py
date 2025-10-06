"""Social Pro Manager - Unified Instagram & TikTok Highest Quality Downloader"""
from pathlib import Path
import re

class SocialProManager:
    """Unified manager for Instagram and TikTok Pro downloads"""
    
    def __init__(self):
        self.instagram = None
        self.tiktok = None
    
    def _init_instagram(self):
        if not self.instagram:
            from streamforge.social.instagram_pro import InstagramProDownloader
            self.instagram = InstagramProDownloader()
        return self.instagram
    
    def _init_tiktok(self):
        if not self.tiktok:
            from streamforge.social.tiktok_pro import TikTokProDownloader
            self.tiktok = TikTokProDownloader()
        return self.tiktok
    
    def detect_platform(self, url):
        """Auto-detect platform from URL"""
        if 'instagram.com' in url:
            return 'instagram'
        elif 'tiktok.com' in url or 'vm.tiktok.com' in url:
            return 'tiktok'
        else:
            return None
    
    def smart_download(self, url, **kwargs):
        """Smart download - auto-detect platform and use highest quality"""
        platform = self.detect_platform(url)
        
        if platform == 'instagram':
            print("\n📸 Detected: Instagram")
            print("🎯 Using: Instagram Pro (Highest Quality)")
            downloader = self._init_instagram()
            return downloader.download_post(url)
        
        elif platform == 'tiktok':
            print("\n🎵 Detected: TikTok")
            print("🎯 Using: TikTok Pro (No Watermark, Highest Quality)")
            downloader = self._init_tiktok()
            no_watermark = kwargs.get('no_watermark', True)
            return downloader.download_video(url, no_watermark=no_watermark)
        
        else:
            print("❌ Unsupported platform")
            print("✅ Supported: Instagram, TikTok")
            return False
    
    def batch_smart_download(self, urls):
        """Batch download from mixed platforms"""
        print(f"\n📋 Smart Batch Download")
        print(f"📊 Total URLs: {len(urls)}")
        
        results = {'instagram': [], 'tiktok': [], 'unsupported': []}
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Processing: {url[:50]}...")
            
            platform = self.detect_platform(url)
            
            if platform == 'instagram':
                downloader = self._init_instagram()
                success = downloader.download_post(url)
                results['instagram'].append({'url': url, 'success': success})
            
            elif platform == 'tiktok':
                downloader = self._init_tiktok()
                success = downloader.download_video(url, no_watermark=True)
                results['tiktok'].append({'url': url, 'success': success})
            
            else:
                results['unsupported'].append(url)
                print(f"⚠️ Unsupported platform")
        
        # Summary
        print("\n" + "="*70)
        print("📊 BATCH DOWNLOAD SUMMARY")
        print("="*70)
        
        if results['instagram']:
            ig_success = sum(1 for r in results['instagram'] if r['success'])
            print(f"\n📸 Instagram: {ig_success}/{len(results['instagram'])} successful")
        
        if results['tiktok']:
            tt_success = sum(1 for r in results['tiktok'] if r['success'])
            print(f"🎵 TikTok: {tt_success}/{len(results['tiktok'])} successful")
        
        if results['unsupported']:
            print(f"\n⚠️ Unsupported: {len(results['unsupported'])} URLs")
        
        total_success = (
            sum(1 for r in results['instagram'] if r['success']) +
            sum(1 for r in results['tiktok'] if r['success'])
        )
        print(f"\n✅ Total Success: {total_success}/{len(urls)}")
        
        return results
    
    def compare_quality(self, url):
        """Compare quality options for a URL"""
        platform = self.detect_platform(url)
        
        print("\n🔍 Quality Comparison")
        print("="*70)
        
        if platform == 'instagram':
            print("\n📸 Instagram Quality Options:")
            print("  ✅ HIGHEST (Original) - Zero Compression")
            print("     • Resolution: Up to 1080p")
            print("     • Bitrate: Maximum available")
            print("     • Format: MP4 (H.264)")
            print("     • Audio: AAC (Best quality)")
            print("     • Metadata: Preserved")
            print("     • Thumbnails: Included")
            
        elif platform == 'tiktok':
            print("\n🎵 TikTok Quality Options:")
            print("  ✅ HIGHEST (No Watermark) - Zero Compression")
            print("     • Resolution: Up to 1080p")
            print("     • Bitrate: Maximum available")
            print("     • Format: MP4 (H.264)")
            print("     • Audio: AAC (Best quality)")
            print("     • Watermark: REMOVED ✅")
            print("     • Metadata: Preserved")
        
        else:
            print("❌ Unsupported platform")

def main():
    print("="*70)
    print("🌟 SOCIAL PRO MANAGER")
    print("📸 Instagram Pro | 🎵 TikTok Pro")
    print("🎯 Highest Quality | Zero Compression | No Watermark")
    print("="*70)
    
    manager = SocialProManager()
    
    print("\n📋 Options:")
    print("1. Smart Download (Auto-detect platform)")
    print("2. Instagram Download (Highest Quality)")
    print("3. TikTok Download (No Watermark, Highest Quality)")
    print("4. Batch Smart Download (Mixed platforms)")
    print("5. Compare Quality Options")
    
    choice = input("\n👉 Select: ").strip()
    
    if choice == '1':
        url = input("\n📝 Enter URL (Instagram or TikTok): ")
        manager.smart_download(url)
    
    elif choice == '2':
        url = input("\n📝 Enter Instagram URL: ")
        downloader = manager._init_instagram()
        downloader.download_post(url)
    
    elif choice == '3':
        url = input("\n📝 Enter TikTok URL: ")
        no_wm = input("Remove watermark? (y/n, default y): ").lower() != 'n'
        downloader = manager._init_tiktok()
        downloader.download_video(url, no_watermark=no_wm)
    
    elif choice == '4':
        print("\n📝 Enter URLs (one per line, empty to finish):")
        print("💡 Mix Instagram and TikTok URLs!")
        urls = []
        while True:
            url = input()
            if not url:
                break
            urls.append(url)
        if urls:
            manager.batch_smart_download(urls)
    
    elif choice == '5':
        url = input("\n📝 Enter URL: ")
        manager.compare_quality(url)

if __name__ == "__main__":
    main()
