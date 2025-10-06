"""Thumbnail Extractor"""
import yt_dlp
import requests
from pathlib import Path

class ThumbnailExtractor:
    def __init__(self, output_dir="downloads/thumbnails"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def extract_thumbnail(self, url):
        print(f"\n🖼️  Thumbnail Extractor")
        
        ydl_opts = {'quiet': True}
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                thumbnail_url = info.get('thumbnail')
                title = info.get('title', 'thumbnail')
                
                if thumbnail_url:
                    response = requests.get(thumbnail_url)
                    filename = self.output_dir / f"{title}.jpg"
                    
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    
                    print(f"✅ Thumbnail saved: {filename}")
                    return str(filename)
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

def main():
    extractor = ThumbnailExtractor()
    url = input("Enter video URL: ")
    extractor.extract_thumbnail(url)

if __name__ == "__main__":
    main()
