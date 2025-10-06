#!/usr/bin/env python3
"""
StreamForge-Pro - Complete CLI Launcher
Quick access to all features
"""
import sys
import asyncio
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════════╗
║              🎬 STREAMFORGE-PRO v1.0.0                       ║
║         Advanced Multi-Platform Media Downloader              ║
║              Created by Raj Saraswati                         ║
╚═══════════════════════════════════════════════════════════════╝
""")

def print_menu():
    print("\n" + "="*60)
    print("🚀 MAIN MENU")
    print("="*60)
    print("\n📥 DOWNLOAD OPTIONS:")
    print("  1. Quick Download (Single Video)")
    print("  2. Playlist Download")
    print("  3. Batch Download (Multiple URLs)")
    print("  4. Channel Download")
    
    print("\n🎬 ADVANCED FEATURES:")
    print("  5. Video Converter")
    print("  6. Video Editor")
    print("  7. Live Stream Recorder")
    print("  8. Quality Selector Test")
    
    print("\n🖥️  INTERFACES:")
    print("  9. Interactive CLI")
    print("  10. Launch GUI (Enhanced)")
    print("  11. Start Web Server (Enhanced)")
    
    print("\n⚙️  UTILITIES:")
    print("  12. Download Manager Test")
    print("  13. View Download History")
    print("  14. Analytics Dashboard")
    print("  15. Download Scheduler")
    print("  16. Settings")
    
    print("\n  0. Exit")
    print("="*60)

async def quick_download():
    from streamforge.core.simple_downloader import SimpleDownloader
    downloader = SimpleDownloader()
    url = input("\n📝 Enter video URL: ")
    print("\n🎯 Quality Options:")
    print("  1. Best")
    print("  2. 1080p")
    print("  3. 720p")
    print("  4. Audio Only (MP3)")
    choice = input("\nSelect (1-4): ")
    
    quality_map = {'1': 'best', '2': '1080p', '3': '720p'}
    if choice == '4':
        downloader.download(url, audio_only=True)
    else:
        downloader.download(url, quality=quality_map.get(choice, 'best'))

async def playlist_download():
    from streamforge.core.playlist_downloader import PlaylistDownloader
    downloader = PlaylistDownloader()
    url = input("\n📝 Enter playlist URL: ")
    await downloader.download_playlist(url)

async def batch_download():
    from streamforge.core.batch_processor import BatchProcessor
    processor = BatchProcessor()
    
    print("\n📋 Batch Download")
    print("1. From file")
    print("2. Manual entry")
    choice = input("\nSelect: ")
    
    if choice == '1':
        file_path = input("Enter file path: ")
        await processor.process_file(file_path)
    else:
        print("\nEnter URLs (empty line to finish):")
        urls = []
        while True:
            url = input()
            if not url:
                break
            urls.append(url)
        if urls:
            await processor.process_urls(urls)

async def video_converter():
    from streamforge.core.video_converter import VideoConverter
    converter = VideoConverter()
    input_file = input("\n📁 Enter video file path: ")
    format = input("Output format (mp4/avi/mkv/webm): ") or 'mp4'
    converter.convert(input_file, format)

async def video_editor():
    from streamforge.core.video_editor import VideoEditor
    editor = VideoEditor()
    
    print("\n🎬 Video Editor")
    print("1. Trim video")
    print("2. Add watermark")
    print("3. Extract audio")
    print("4. Create GIF")
    print("5. Merge videos")
    
    choice = input("\nSelect: ")
    
    if choice == '1':
        input_file = input("Input file: ")
        output_file = input("Output file: ")
        start = input("Start time (HH:MM:SS): ")
        end = input("End time (HH:MM:SS): ")
        editor.trim_video(input_file, output_file, start, end)
    elif choice == '2':
        input_file = input("Input file: ")
        output_file = input("Output file: ")
        text = input("Watermark text: ")
        editor.add_watermark(input_file, output_file, text)
    elif choice == '3':
        input_file = input("Input file: ")
        output_file = input("Output file (mp3): ")
        editor.extract_audio(input_file, output_file)
    elif choice == '4':
        input_file = input("Input file: ")
        output_file = input("Output file (gif): ")
        editor.create_gif(input_file, output_file)

async def channel_download():
    from streamforge.core.channel_downloader import ChannelDownloader
    downloader = ChannelDownloader()
    url = input("\n📝 Enter channel URL: ")
    max_videos = input("Max videos (leave empty for all): ")
    max_videos = int(max_videos) if max_videos else None
    downloader.download_channel(url, max_videos)

async def live_recorder():
    from streamforge.core.live_stream_recorder import LiveStreamRecorder
    recorder = LiveStreamRecorder()
    url = input("\n📝 Enter live stream URL: ")
    duration = input("Duration in seconds (leave empty for full): ")
    duration = int(duration) if duration else None
    await recorder.record_stream(url, duration)

async def analytics_dashboard():
    from streamforge.utils.analytics import Analytics
    analytics = Analytics()
    analytics.print_dashboard()

async def scheduler_menu():
    from streamforge.utils.scheduler import DownloadScheduler
    from datetime import datetime
    
    scheduler = DownloadScheduler()
    
    print("\n⏰ Download Scheduler")
    print("1. Schedule download")
    print("2. List scheduled")
    print("3. Start scheduler")
    
    choice = input("\nSelect: ")
    
    if choice == '1':
        url = input("URL: ")
        time_str = input("Time (YYYY-MM-DD HH:MM): ")
        scheduled_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        scheduler.schedule_download(url, scheduled_time)
    elif choice == '2':
        scheduler.list_scheduled()
    elif choice == '3':
        await scheduler.start_scheduler()

async def quality_test():
    from streamforge.core.quality_selector import QualitySelector
    selector = QualitySelector()
    rec = selector.get_recommendation()
    print(f"\n🎯 Recommended Quality: {rec['quality']}")
    print(f"📊 Network: {rec['network']}")
    print(f"💾 Storage: {rec['storage_gb']} GB")
    print(f"💡 Reason: {rec['reason']}")

async def download_manager_test():
    from streamforge.core.download_manager import DownloadManager
    manager = DownloadManager(max_concurrent=2)
    await manager.initialize()
    
    url = input("\n📝 Enter video URL: ")
    job_id = await manager.add_download(url)
    
    print(f"\n✅ Job added: {job_id}")
    print("📊 Monitoring progress...\n")
    
    while True:
        job = manager.get_status(job_id)
        if job.status.value == 'completed':
            print(f"\n✅ Complete: {job.title}")
            break
        elif job.status.value == 'failed':
            print(f"\n❌ Failed: {job.error}")
            break
        print(f"\r📊 {job.status.value.upper()}: {job.progress:.1f}%", end='')
        await asyncio.sleep(1)
    
    await manager.shutdown()

async def interactive_cli():
    from streamforge.cli.interactive_cli import main
    await main()

def launch_gui():
    print("\n🖥️ Launching GUI...")
    print("1. Basic GUI")
    print("2. Enhanced GUI (Recommended)")
    choice = input("\nSelect: ")
    
    if choice == '2':
        from streamforge.gui.enhanced_gui import launch_gui
        launch_gui()
    else:
        from streamforge.gui.desktop_app import launch_gui
        launch_gui()

def start_web_server():
    print("\n🌐 Starting web server...")
    print("1. Basic Web Server")
    print("2. Enhanced Web Server (Recommended)")
    choice = input("\nSelect: ")
    
    print("\n📍 URL: http://localhost:8000")
    print("Press Ctrl+C to stop\n")
    
    import uvicorn
    if choice == '2':
        from streamforge.web.enhanced_web import app
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        from streamforge.web.app import app
        uvicorn.run(app, host="0.0.0.0", port=8000)

def view_history():
    from streamforge.database.db_manager import DatabaseManager
    db = DatabaseManager()
    downloads = db.get_all_downloads()
    
    print("\n📊 Download History:")
    print("="*60)
    for dl in downloads[:10]:  # Show last 10
        print(f"  {dl[2][:50]} - {dl[3]} ({dl[4]}%)")
    
    stats = db.get_stats()
    print(f"\n📈 Stats: {stats[1]}/{stats[0]} completed")

async def main():
    print_banner()
    
    while True:
        print_menu()
        choice = input("\n👉 Select option: ").strip()
        
        try:
            if choice == '0':
                print("\n👋 Thank you for using StreamForge-Pro!\n")
                break
            elif choice == '1':
                await quick_download()
            elif choice == '2':
                await playlist_download()
            elif choice == '3':
                await batch_download()
            elif choice == '4':
                await channel_download()
            elif choice == '5':
                await video_converter()
            elif choice == '6':
                await video_editor()
            elif choice == '7':
                await live_recorder()
            elif choice == '8':
                await quality_test()
            elif choice == '9':
                await interactive_cli()
            elif choice == '10':
                launch_gui()
            elif choice == '11':
                start_web_server()
            elif choice == '12':
                await download_manager_test()
            elif choice == '13':
                view_history()
            elif choice == '14':
                await analytics_dashboard()
            elif choice == '15':
                await scheduler_menu()
            elif choice == '16':
                print("\n⚠️  Settings - Coming soon!")
            else:
                print("\n❌ Invalid option!")
            
            if choice != '0':
                input("\n⏎ Press Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            input("\n⏎ Press Enter to continue...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
