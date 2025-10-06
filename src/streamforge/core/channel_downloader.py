"""YouTube Channel Downloader"""
import yt_dlp

class ChannelDownloader:
    def download_channel(self, channel_url, max_videos=50):
        print(f"📺 Downloading channel videos (max {max_videos})")
        ydl_opts = {
            'outtmpl': 'downloads/channels/%(uploader)s/%(title)s.%(ext)s',
            'playlistend': max_videos,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([channel_url])
            print("✅ Channel downloaded!")
        except Exception as e:
            print(f"❌ Error: {e}")
