"""Channel Downloader - Download all videos from a channel"""
import yt_dlp
from pathlib import Path

class ChannelDownloader:
    def __init__(self, output_dir="downloads/channels"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def download_channel(self, channel_url, max_videos=None):
        print(f"\n📺 Channel Downloader")
        print(f"🔗 URL: {channel_url}")
        
        ydl_opts = {
            'outtmpl': str(self.output_dir / '%(uploader)s/%(title)s.%(ext)s'),
            'format': 'best',
            'playlistend': max_videos,
            'ignoreerrors': True,
            'progress_hooks': [self._progress_hook],
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(channel_url, download=False)
                total = len(info.get('entries', []))
                print(f"📊 Found {total} videos")
                
                ydl.download([channel_url])
                print(f"\n✅ Channel downloaded!")
                return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def _progress_hook(self, d):
        if d['status'] == 'downloading':
            print(f"\r⏬ {d.get('_percent_str', 'N/A')}", end='')
        elif d['status'] == 'finished':
            print("\n✅ Video complete")

if __name__ == "__main__":
    downloader = ChannelDownloader()
    url = input("Enter channel URL: ")
    downloader.download_channel(url)
