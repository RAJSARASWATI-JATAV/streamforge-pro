"""Download Scheduler"""
import asyncio
from datetime import datetime, timedelta
import json
from pathlib import Path

class DownloadScheduler:
    def __init__(self):
        self.scheduled_downloads = []
        self.schedule_file = Path("scheduled_downloads.json")
        self.load_schedule()
    
    def schedule_download(self, url, scheduled_time, quality='best'):
        download = {
            'url': url,
            'scheduled_time': scheduled_time.isoformat(),
            'quality': quality,
            'status': 'scheduled'
        }
        self.scheduled_downloads.append(download)
        self.save_schedule()
        print(f"⏰ Scheduled for {scheduled_time}")
    
    def save_schedule(self):
        with open(self.schedule_file, 'w') as f:
            json.dump(self.scheduled_downloads, f, indent=2)
    
    def load_schedule(self):
        if self.schedule_file.exists():
            with open(self.schedule_file) as f:
                self.scheduled_downloads = json.load(f)
    
    async def run_scheduler(self):
        print("⏰ Scheduler running...")
        while True:
            now = datetime.now()
            for download in self.scheduled_downloads:
                if download['status'] == 'scheduled':
                    scheduled_time = datetime.fromisoformat(download['scheduled_time'])
                    if now >= scheduled_time:
                        print(f"\n🚀 Starting scheduled download: {download['url']}")
                        download['status'] = 'completed'
                        self.save_schedule()
            await asyncio.sleep(60)

def main():
    scheduler = DownloadScheduler()
    url = input("Enter URL: ")
    hours = int(input("Schedule after how many hours? "))
    scheduled_time = datetime.now() + timedelta(hours=hours)
    scheduler.schedule_download(url, scheduled_time)

if __name__ == "__main__":
    main()
