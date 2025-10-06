#!/usr/bin/env python3
"""
StreamForge-Pro - HACKER EDITION
Complete CLI Launcher with Hacker Visual Effects
"""
import sys
import asyncio
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from streamforge.utils.hacker_ui import HackerUI

async def quick_download():
    from streamforge.core.simple_downloader import SimpleDownloader
    HackerUI.status_line('info', 'Initializing Quick Download Module...')
    time.sleep(0.5)
    
    downloader = SimpleDownloader()
    url = input(f"\n{HackerUI.COLORS['cyan']}[INPUT] Enter target URL: {HackerUI.COLORS['white']}")
    
    HackerUI.status_line('info', 'Quality selection interface loading...')
    print(f"\n{HackerUI.COLORS['yellow']}[QUALITY OPTIONS]")
    print(f"{HackerUI.COLORS['green']}  [1] Best Available")
    print(f"{HackerUI.COLORS['green']}  [2] 1080p HD")
    print(f"{HackerUI.COLORS['green']}  [3] 720p HD")
    print(f"{HackerUI.COLORS['green']}  [4] Audio Only (MP3)")
    
    choice = input(f"\n{HackerUI.COLORS['cyan']}[SELECT] Choose option (1-4): {HackerUI.COLORS['white']}")
    
    quality_map = {'1': 'best', '2': '1080p', '3': '720p'}
    
    HackerUI.status_line('loading', 'Initiating download sequence...')
    time.sleep(0.5)
    
    if choice == '4':
        downloader.download(url, audio_only=True)
    else:
        downloader.download(url, quality=quality_map.get(choice, 'best'))
    
    HackerUI.status_line('success', 'Download operation completed')

async def playlist_download():
    from streamforge.core.playlist_downloader import PlaylistDownloader
    HackerUI.status_line('info', 'Initializing Playlist Extraction Module...')
    time.sleep(0.5)
    
    downloader = PlaylistDownloader()
    url = input(f"\n{HackerUI.COLORS['cyan']}[INPUT] Enter playlist URL: {HackerUI.COLORS['white']}")
    
    HackerUI.status_line('loading', 'Analyzing playlist structure...')
    await downloader.download_playlist(url)
    HackerUI.status_line('success', 'Playlist extraction completed')

async def batch_download():
    from streamforge.core.batch_processor import BatchProcessor
    HackerUI.status_line('info', 'Initializing Batch Processing Module...')
    time.sleep(0.5)
    
    processor = BatchProcessor()
    
    print(f"\n{HackerUI.COLORS['yellow']}[BATCH MODE]")
    print(f"{HackerUI.COLORS['green']}  [1] Load from file")
    print(f"{HackerUI.COLORS['green']}  [2] Manual entry")
    
    choice = input(f"\n{HackerUI.COLORS['cyan']}[SELECT] Choose mode: {HackerUI.COLORS['white']}")
    
    if choice == '1':
        file_path = input(f"{HackerUI.COLORS['cyan']}[INPUT] File path: {HackerUI.COLORS['white']}")
        HackerUI.status_line('loading', 'Processing file...')
        await processor.process_file(file_path)
    else:
        print(f"\n{HackerUI.COLORS['yellow']}[INPUT] Enter URLs (empty line to finish):")
        urls = []
        while True:
            url = input(f"{HackerUI.COLORS['green']}> {HackerUI.COLORS['white']}")
            if not url:
                break
            urls.append(url)
            HackerUI.status_line('info', f'URL {len(urls)} added to queue')
        
        if urls:
            HackerUI.status_line('loading', f'Processing {len(urls)} URLs...')
            await processor.process_urls(urls)
    
    HackerUI.status_line('success', 'Batch operation completed')

async def instagram_pro():
    from streamforge.social.instagram_pro import InstagramProDownloader
    HackerUI.box_message('INSTAGRAM PRO', 'Zero Compression Technology', 'magenta')
    
    downloader = InstagramProDownloader()
    
    print(f"{HackerUI.COLORS['yellow']}[INSTAGRAM PRO OPTIONS]")
    print(f"{HackerUI.COLORS['magenta']}  [1] Post/Video Extraction")
    print(f"{HackerUI.COLORS['magenta']}  [2] Reel Extraction")
    print(f"{HackerUI.COLORS['magenta']}  [3] IGTV Extraction")
    print(f"{HackerUI.COLORS['magenta']}  [4] Batch Extraction")
    
    choice = input(f"\n{HackerUI.COLORS['cyan']}[SELECT] Choose operation: {HackerUI.COLORS['white']}")
    
    if choice == '1':
        url = input(f"{HackerUI.COLORS['cyan']}[INPUT] Instagram URL: {HackerUI.COLORS['white']}")
        HackerUI.status_line('loading', 'Extracting highest quality...')
        downloader.download_post(url)
    elif choice == '2':
        url = input(f"{HackerUI.COLORS['cyan']}[INPUT] Reel URL: {HackerUI.COLORS['white']}")
        HackerUI.status_line('loading', 'Extracting Reel...')
        downloader.download_reel(url)
    elif choice == '3':
        url = input(f"{HackerUI.COLORS['cyan']}[INPUT] IGTV URL: {HackerUI.COLORS['white']}")
        HackerUI.status_line('loading', 'Extracting IGTV...')
        downloader.download_igtv(url)
    elif choice == '4':
        print(f"\n{HackerUI.COLORS['yellow']}[INPUT] Enter URLs (empty to finish):")
        urls = []
        while True:
            url = input(f"{HackerUI.COLORS['green']}> {HackerUI.COLORS['white']}")
            if not url:
                break
            urls.append(url)
        if urls:
            HackerUI.status_line('loading', f'Batch extracting {len(urls)} items...')
            downloader.batch_download(urls)

async def tiktok_pro():
    from streamforge.social.tiktok_pro import TikTokProDownloader
    HackerUI.box_message('TIKTOK PRO', 'No Watermark | Highest Quality', 'magenta')
    
    downloader = TikTokProDownloader()
    
    print(f"{HackerUI.COLORS['yellow']}[TIKTOK PRO OPTIONS]")
    print(f"{HackerUI.COLORS['magenta']}  [1] Video Extraction (No Watermark)")
    print(f"{HackerUI.COLORS['magenta']}  [2] User Videos Extraction")
    print(f"{HackerUI.COLORS['magenta']}  [3] Hashtag Videos Extraction")
    print(f"{HackerUI.COLORS['magenta']}  [4] Batch Extraction")
    
    choice = input(f"\n{HackerUI.COLORS['cyan']}[SELECT] Choose operation: {HackerUI.COLORS['white']}")
    
    if choice == '1':
        url = input(f"{HackerUI.COLORS['cyan']}[INPUT] TikTok URL: {HackerUI.COLORS['white']}")
        HackerUI.status_line('loading', 'Removing watermark & extracting...')
        downloader.download_video(url, no_watermark=True)
    elif choice == '2':
        username = input(f"{HackerUI.COLORS['cyan']}[INPUT] Username: {HackerUI.COLORS['white']}")
        max_videos = input(f"{HackerUI.COLORS['cyan']}[INPUT] Max videos (default 10): {HackerUI.COLORS['white']}") or "10"
        HackerUI.status_line('loading', f'Extracting videos from @{username}...')
        downloader.download_user_videos(username, int(max_videos))
    elif choice == '3':
        hashtag = input(f"{HackerUI.COLORS['cyan']}[INPUT] Hashtag: {HackerUI.COLORS['white']}")
        max_videos = input(f"{HackerUI.COLORS['cyan']}[INPUT] Max videos (default 10): {HackerUI.COLORS['white']}") or "10"
        HackerUI.status_line('loading', f'Extracting videos from #{hashtag}...')
        downloader.download_hashtag(hashtag, int(max_videos))
    elif choice == '4':
        print(f"\n{HackerUI.COLORS['yellow']}[INPUT] Enter URLs (empty to finish):")
        urls = []
        while True:
            url = input(f"{HackerUI.COLORS['green']}> {HackerUI.COLORS['white']}")
            if not url:
                break
            urls.append(url)
        if urls:
            HackerUI.status_line('loading', f'Batch extracting {len(urls)} videos...')
            downloader.batch_download(urls, no_watermark=True)

async def ai_optimizer():
    from streamforge.utils.ai_quality_optimizer import AIQualityOptimizer
    HackerUI.box_message('AI OPTIMIZER', 'Machine Learning Analysis', 'cyan')
    
    optimizer = AIQualityOptimizer()
    
    HackerUI.status_line('loading', 'Analyzing system resources...')
    time.sleep(0.5)
    
    system = optimizer.analyze_system()
    
    print(f"\n{HackerUI.COLORS['yellow']}[SYSTEM ANALYSIS]")
    print(f"{HackerUI.COLORS['green']}  CPU Usage: {HackerUI.COLORS['white']}{system['cpu_usage']:.1f}%")
    print(f"{HackerUI.COLORS['green']}  Memory Available: {HackerUI.COLORS['white']}{system['memory_available_gb']:.1f} GB")
    print(f"{HackerUI.COLORS['green']}  Disk Free: {HackerUI.COLORS['white']}{system['disk_free_gb']:.1f} GB")
    print(f"{HackerUI.COLORS['green']}  Performance Score: {HackerUI.COLORS['white']}{system['performance_score']:.1f}/100")
    
    recommendations = optimizer.get_recommendations()
    
    print(f"\n{HackerUI.COLORS['yellow']}[AI RECOMMENDATIONS]")
    print(f"{HackerUI.COLORS['cyan']}  Quality: {HackerUI.COLORS['white']}{recommendations['recommended_quality']}")
    print(f"{HackerUI.COLORS['cyan']}  Reason: {HackerUI.COLORS['white']}{recommendations['reason']}")
    print(f"{HackerUI.COLORS['cyan']}  System Health: {HackerUI.COLORS['white']}{recommendations['system_health']}")
    
    HackerUI.status_line('success', 'Analysis completed')

async def main():
    # System initialization
    HackerUI.system_init()
    
    # Display banner
    print(HackerUI.banner_hacker())
    time.sleep(1)
    
    while True:
        # Display menu
        print(HackerUI.menu_hacker())
        
        choice = input(f"\n{HackerUI.COLORS['red']}[COMMAND] Enter option: {HackerUI.COLORS['white']}").strip()
        
        try:
            if choice == '00' or choice == '0':
                HackerUI.status_line('warning', 'Initiating system shutdown...')
                time.sleep(0.5)
                HackerUI.box_message('SYSTEM', 'Session Terminated', 'red')
                break
            
            elif choice == '01' or choice == '1':
                await quick_download()
            elif choice == '02' or choice == '2':
                await playlist_download()
            elif choice == '03' or choice == '3':
                await batch_download()
            elif choice == '16':
                await ai_optimizer()
            elif choice == '21':
                await instagram_pro()
            elif choice == '22':
                await tiktok_pro()
            else:
                HackerUI.status_line('error', 'Invalid command')
            
            input(f"\n{HackerUI.COLORS['yellow']}[SYSTEM] Press Enter to continue...{HackerUI.COLORS['white']}")
            HackerUI.clear_screen()
            print(HackerUI.banner_hacker())
            
        except KeyboardInterrupt:
            HackerUI.status_line('warning', 'Operation interrupted by user')
            HackerUI.box_message('SYSTEM', 'Session Terminated', 'red')
            break
        except Exception as e:
            HackerUI.status_line('error', f'System error: {str(e)}')
            input(f"\n{HackerUI.COLORS['yellow']}[SYSTEM] Press Enter to continue...{HackerUI.COLORS['white']}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n\n{HackerUI.COLORS['red']}[SYSTEM] Emergency shutdown initiated{HackerUI.COLORS['white']}\n")
