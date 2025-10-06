"""Live Stream Recorder"""
import yt_dlp

class LiveStreamRecorder:
    def record_stream(self, url, duration=3600):
        print(f"🔴 Recording live stream for {duration}s")
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/livestreams/%(title)s.%(ext)s',
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("✅ Stream recorded!")
        except Exception as e:
            print(f"❌ Error: {e}")
