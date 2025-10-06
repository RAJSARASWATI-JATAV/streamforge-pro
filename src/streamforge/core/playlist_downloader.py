"""Playlist & Channel Downloader"""
import yt_dlp
import asyncio
from pathlib import Path

class PlaylistDownloader:
    def __init__(self, output_dir="downloads/playlists"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    async def download_playlist(self, url, max_videos=None):
        print(f"\n📋 Playlist Downloader")
        print(f"🔗 URL: {url}")
        
        ydl_opts = {
            'outtmpl': str(self.output_dir / '%(playlist)s/%(title)s.%(ext)s'),
            'format': 'best',
            'noplaylist': False,
            'playlistend': max_videos,
            'progress_hooks': [self._progress_hook],
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                total = len(info.get('entries', []))
                print(f"📊 Found {total} videos in playlist")
                
                ydl.download([url])
                print(f"\n✅ Playlist downloaded!")
                return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def _progress_hook(self, d):
        if d['status'] == 'downloading':
            print(f"\r⏬ {d.get('_percent_str', 'N/A')} | {d.get('_speed_str', 'N/A')}", end='')
        elif d['status'] == 'finished':
            print("\n✅ Video complete")

async def main():
    downloader = PlaylistDownloader()
    url = input("Enter playlist URL: ")
    await downloader.download_playlist(url)

if __name__ == "__main__":
    asyncio.run(main())
