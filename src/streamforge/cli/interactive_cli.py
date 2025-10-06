"""Interactive CLI for StreamForge-Pro"""
import asyncio
import sys

def print_menu():
    print("\n" + "="*60)
    print("🎬 StreamForge-Pro - Interactive CLI")
    print("="*60)
    print("\n1. Download Video")
    print("2. Download Playlist")
    print("3. Download Channel")
    print("4. Batch Download")
    print("5. Live Stream Recording")
    print("6. Video Editor")
    print("7. Settings")
    print("0. Exit")
    print()

async def download_video():
    import yt_dlp
    url = input("Enter video URL: ")
    quality = input("Quality (best/1080p/720p/480p): ") or "best"
    
    print(f"\n✅ Downloading: {url}")
    print(f"Quality: {quality}\n")
    
    ydl_opts = {
        'format': f'{quality}/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'progress_hooks': [lambda d: print(f"Progress: {d.get('_percent_str', 'N/A')}") if d['status'] == 'downloading' else None],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download complete!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

async def download_playlist():
    import yt_dlp
    url = input("Enter playlist URL: ")
    print(f"\n✅ Downloading playlist: {url}\n")
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(playlist)s/%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Playlist download complete!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

async def download_channel():
    url = input("Enter channel URL: ")
    print(f"\n✅ Downloading channel: {url}")
    print("Download started! (Feature in development)")

async def batch_download():
    import yt_dlp
    print("\nEnter URLs (one per line, empty line to finish):")
    urls = []
    while True:
        url = input()
        if not url:
            break
        urls.append(url)
    
    print(f"\n✅ Batch downloading {len(urls)} videos\n")
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
        print("\n✅ Batch download complete!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

async def live_recording():
    url = input("Enter live stream URL: ")
    print(f"\n✅ Recording: {url}")
    print("Recording started! (Feature in development)")

async def video_editor():
    print("\n🎬 Video Editor")
    print("1. Trim video")
    print("2. Add watermark")
    print("3. Extract audio")
    print("4. Create GIF")
    choice = input("Select option: ")
    print("Editor feature in development!")

async def settings():
    print("\n⚙️ Settings")
    print("1. Output directory")
    print("2. Default quality")
    print("3. Cloud upload settings")
    print("Settings feature in development!")

async def main():
    print("\n" + "="*60)
    print("StreamForge-Pro Interactive CLI")
    print("="*60)
    
    while True:
        print_menu()
        choice = input("Select option: ").strip()
        
        if choice == '0':
            print("\n👋 Goodbye!\n")
            break
        elif choice == '1':
            await download_video()
        elif choice == '2':
            await download_playlist()
        elif choice == '3':
            await download_channel()
        elif choice == '4':
            await batch_download()
        elif choice == '5':
            await live_recording()
        elif choice == '6':
            await video_editor()
        elif choice == '7':
            await settings()
        else:
            print("\n❌ Invalid option!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)
