"""Video Information Extractor"""
import yt_dlp

class VideoInfo:
    def get_info(self, url):
        print(f"\n📊 Video Information Extractor")
        
        ydl_opts = {'quiet': True}
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                print(f"\n📺 Title: {info.get('title')}")
                print(f"👤 Channel: {info.get('uploader')}")
                print(f"⏱️  Duration: {info.get('duration')}s")
                print(f"👁️  Views: {info.get('view_count'):,}")
                print(f"👍 Likes: {info.get('like_count', 'N/A')}")
                print(f"📅 Upload Date: {info.get('upload_date')}")
                print(f"📝 Description: {info.get('description', '')[:100]}...")
                
                formats = info.get('formats', [])
                print(f"\n🎬 Available Formats: {len(formats)}")
                
                for fmt in formats[:5]:
                    print(f"   - {fmt.get('format_note', 'N/A')} | {fmt.get('ext')} | {fmt.get('filesize', 0) / (1024*1024):.1f}MB")
                
                return info
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

def main():
    extractor = VideoInfo()
    url = input("Enter video URL: ")
    extractor.get_info(url)

if __name__ == "__main__":
    main()
