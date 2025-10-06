#!/usr/bin/env python3
"""Quick Download Script"""
import yt_dlp
import sys

def download(url, quality='best'):
    """Download video from URL"""
    print(f"\nStreamForge-Pro Quick Download")
    print(f"URL: {url}")
    print(f"Quality: {quality}\n")
    
    ydl_opts = {
        'format': f'{quality}/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Title: {info.get('title', 'Unknown')}")
            print(f"Duration: {info.get('duration', 0)//60} min\n")
            ydl.download([url])
        print("\nDownload complete!")
        print(f"Saved to: downloads/\n")
    except Exception as e:
        print(f"\nError: {e}\n")

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rDownloading: {percent} | Speed: {speed} | ETA: {eta}", end='')
    elif d['status'] == 'finished':
        print("\nProcessing...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nStreamForge-Pro Quick Download")
        print("\nUsage:")
        print("  python quick_download.py <URL> [quality]")
        print("\nExamples:")
        print("  python quick_download.py https://youtube.com/watch?v=VIDEO_ID")
        print("  python quick_download.py https://youtube.com/watch?v=VIDEO_ID 1080p")
        print("\nQuality options: best, 1080p, 720p, 480p, audio\n")
    else:
        url = sys.argv[1]
        quality = sys.argv[2] if len(sys.argv) > 2 else 'best'
        download(url, quality)
