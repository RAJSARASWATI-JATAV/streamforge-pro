"""Download Scheduler"""
import asyncio
from datetime import datetime, timedelta
import json
from pathlib import Path

class DownloadScheduler:
    def __init__(self, schedule_file="schedule.json"):
        self.schedule_file = Path(schedule_file)
        self.scheduled_downloads = self._load_schedule()
        self.running = False
    
    def _load_schedule(self):
        if self.schedule_file.exists():
            with open(self.schedule_file) as f:
                return json.load(f)
        return []
    
    def _save_schedule(self):
        with open(self.schedule_file, 'w') as f:
            json.dump(self.scheduled_downloads, f, indent=2)
    
    def schedule_download(self, url, scheduled_time, quality='best', recurring=None):
        """Schedule a download
        
        Args:
            url: Video URL
            scheduled_time: datetime object or ISO format string
            quality: Video quality
            recurring: 'daily', 'weekly', or None
        """
        if isinstance(scheduled_time, str):
            scheduled_time = datetime.fromisoformat(scheduled_time)
        
        download = {
            'url': url,
            'scheduled_time': scheduled_time.isoformat(),
            'quality': quality,
            'recurring': recurring,
            'status': 'scheduled'
        }
        
        self.scheduled_downloads.append(download)
        self._save_schedule()
        print(f"✅ Scheduled: {url} at {scheduled_time}")
    
    async def start_scheduler(self):
        """Start the scheduler loop"""
        self.running = True
        print("⏰ Scheduler started")
        
        while self.running:
            now = datetime.now()
            
            for download in self.scheduled_downloads:
                if download['status'] != 'scheduled':
                    continue
                
                scheduled_time = datetime.fromisoformat(download['scheduled_time'])
                
                if now >= scheduled_time:
                    print(f"\n⏰ Starting scheduled download: {download['url']}")
                    await self._execute_download(download)
                    
                    # Handle recurring
                    if download['recurring'] == 'daily':
                        download['scheduled_time'] = (scheduled_time + timedelta(days=1)).isoformat()
                    elif download['recurring'] == 'weekly':
                        download['scheduled_time'] = (scheduled_time + timedelta(weeks=1)).isoformat()
                    else:
                        download['status'] = 'completed'
                    
                    self._save_schedule()
            
            await asyncio.sleep(60)  # Check every minute
    
    async def _execute_download(self, download):
        """Execute a scheduled download"""
        import yt_dlp
        
        ydl_opts = {
            'format': download['quality'],
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'quiet': True
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([download['url']])
            print(f"✅ Completed: {download['url']}")
        except Exception as e:
            print(f"❌ Failed: {e}")
            download['status'] = 'failed'
    
    def list_scheduled(self):
        """List all scheduled downloads"""
        print("\n⏰ Scheduled Downloads:")
        print("="*60)
        
        for i, download in enumerate(self.scheduled_downloads, 1):
            if download['status'] == 'scheduled':
                print(f"{i}. {download['url']}")
                print(f"   Time: {download['scheduled_time']}")
                print(f"   Quality: {download['quality']}")
                if download['recurring']:
                    print(f"   Recurring: {download['recurring']}")
                print()
    
    def stop_scheduler(self):
        """Stop the scheduler"""
        self.running = False
        print("⏹️ Scheduler stopped")

if __name__ == "__main__":
    scheduler = DownloadScheduler()
    
    print("⏰ Download Scheduler")
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
        asyncio.run(scheduler.start_scheduler())
