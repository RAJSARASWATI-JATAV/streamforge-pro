"""Subtitle Downloader & Translator"""
import yt_dlp
from pathlib import Path

class SubtitleDownloader:
    def __init__(self, output_dir="downloads/subtitles"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def download_subtitles(self, url, languages=['en', 'hi']):
        print(f"\n📝 Subtitle Downloader")
        print(f"🌐 Languages: {', '.join(languages)}")
        
        ydl_opts = {
            'skip_download': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': languages,
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print("✅ Subtitles downloaded!")
                return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

def main():
    downloader = SubtitleDownloader()
    url = input("Enter video URL: ")
    downloader.download_subtitles(url)

if __name__ == "__main__":
    main()
