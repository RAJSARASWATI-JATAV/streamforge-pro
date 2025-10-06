"""Advanced Download Manager with Queue and Concurrency"""
import asyncio
import uuid
from pathlib import Path
from typing import Dict, Optional
import yt_dlp
from dataclasses import dataclass
from enum import Enum

class DownloadStatus(Enum):
    QUEUED = "queued"
    DOWNLOADING = "downloading"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"

@dataclass
class DownloadJob:
    id: str
    url: str
    status: DownloadStatus
    progress: float = 0.0
    title: str = ""
    output_path: str = ""
    error: Optional[str] = None

class DownloadManager:
    def __init__(self, output_dir="downloads", max_concurrent=3):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.max_concurrent = max_concurrent
        self.jobs: Dict[str, DownloadJob] = {}
        self.queue = asyncio.Queue()
        self.active_downloads = 0
        self.running = False
    
    async def initialize(self):
        """Start the download manager"""
        self.running = True
        asyncio.create_task(self._process_queue())
    
    async def add_download(self, url: str, quality="best") -> str:
        """Add a download to the queue"""
        job_id = str(uuid.uuid4())[:8]
        job = DownloadJob(
            id=job_id,
            url=url,
            status=DownloadStatus.QUEUED
        )
        self.jobs[job_id] = job
        await self.queue.put((job_id, quality))
        print(f"✅ Added to queue: {job_id}")
        return job_id
    
    async def _process_queue(self):
        """Process download queue"""
        while self.running:
            if self.active_downloads < self.max_concurrent:
                try:
                    job_id, quality = await asyncio.wait_for(
                        self.queue.get(), timeout=1.0
                    )
                    asyncio.create_task(self._download(job_id, quality))
                except asyncio.TimeoutError:
                    continue
            else:
                await asyncio.sleep(1)
    
    async def _download(self, job_id: str, quality: str):
        """Execute download"""
        job = self.jobs[job_id]
        self.active_downloads += 1
        job.status = DownloadStatus.DOWNLOADING
        
        def progress_hook(d):
            if d['status'] == 'downloading':
                try:
                    percent = d.get('_percent_str', '0%').replace('%', '')
                    job.progress = float(percent)
                except:
                    pass
            elif d['status'] == 'finished':
                job.progress = 100.0
        
        ydl_opts = {
            'format': quality if quality != 'best' else 'best',
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook],
            'quiet': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(job.url, download=False)
                job.title = info.get('title', 'Unknown')
                ydl.download([job.url])
                job.status = DownloadStatus.COMPLETED
                job.output_path = str(self.output_dir / f"{job.title}.mp4")
                print(f"✅ Completed: {job.title}")
        except Exception as e:
            job.status = DownloadStatus.FAILED
            job.error = str(e)
            print(f"❌ Failed: {job_id} - {e}")
        finally:
            self.active_downloads -= 1
    
    def get_status(self, job_id: str) -> Optional[DownloadJob]:
        """Get download status"""
        return self.jobs.get(job_id)
    
    def get_all_jobs(self):
        """Get all jobs"""
        return list(self.jobs.values())
    
    async def shutdown(self):
        """Shutdown manager"""
        self.running = False
        print("🛑 Download manager stopped")

async def main():
    """Test the download manager"""
    manager = DownloadManager(max_concurrent=2)
    await manager.initialize()
    
    # Add test downloads
    url = input("Enter video URL: ")
    job_id = await manager.add_download(url)
    
    # Monitor progress
    while True:
        job = manager.get_status(job_id)
        if job.status == DownloadStatus.COMPLETED:
            print(f"\n✅ Download complete: {job.title}")
            break
        elif job.status == DownloadStatus.FAILED:
            print(f"\n❌ Download failed: {job.error}")
            break
        print(f"\r📊 Progress: {job.progress:.1f}%", end='')
        await asyncio.sleep(1)
    
    await manager.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
