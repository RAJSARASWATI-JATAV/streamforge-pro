"""Live Stream Recorder"""
import yt_dlp
from pathlib import Path
import asyncio

class LiveStreamRecorder:
    def __init__(self, output_dir="downloads/live"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.recording = False
    
    async def record_stream(self, stream_url, duration=None):
        print(f"\n🔴 Live Stream Recorder")
        print(f"🔗 URL: {stream_url}")
        
        ydl_opts = {
            'outtmpl': str(self.output_dir / '%(title)s-%(timestamp)s.%(ext)s'),
            'format': 'best',
            'live_from_start': True,
            'progress_hooks': [self._progress_hook],
        }
        
        if duration:
            ydl_opts['download_ranges'] = lambda info, ydl: [{'start_time': 0, 'end_time': duration}]
        
        try:
            self.recording = True
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print("🎥 Recording started...")
                ydl.download([stream_url])
                print(f"\n✅ Recording complete!")
                return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            self.recording = False
    
    def _progress_hook(self, d):
        if d['status'] == 'downloading':
            print(f"\r🔴 LIVE: {d.get('_percent_str', 'N/A')} | {d.get('_speed_str', 'N/A')}", end='')
    
    def stop_recording(self):
        self.recording = False
        print("\n⏹️ Stopping recording...")

if __name__ == "__main__":
    recorder = LiveStreamRecorder()
    url = input("Enter live stream URL: ")
    asyncio.run(recorder.record_stream(url))
