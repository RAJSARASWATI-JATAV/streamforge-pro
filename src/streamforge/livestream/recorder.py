"""Live Stream Recorder"""
import asyncio
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict
import streamlink

class LiveStreamRecorder:
    """Record live streams from various platforms"""
    
    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.active_recordings: Dict[str, asyncio.Task] = {}
        
    async def record_stream(self, url: str, quality: str = 'best', 
                           duration: Optional[int] = None) -> str:
        """Record live stream"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = self.output_dir / f'livestream_{timestamp}.mp4'
        
        try:
            streams = streamlink.streams(url)
            if not streams:
                raise ValueError("No streams found")
                
            stream = streams.get(quality) or streams.get('best')
            
            cmd = [
                'ffmpeg',
                '-i', stream.url,
                '-c', 'copy',
            ]
            
            if duration:
                cmd.extend(['-t', str(duration)])
                
            cmd.append(str(output_file))
            
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            recording_id = f"rec_{timestamp}"
            self.active_recordings[recording_id] = asyncio.create_task(process.wait())
            
            return recording_id
            
        except Exception as e:
            raise RuntimeError(f"Failed to start recording: {e}")
            
    async def record_youtube_live(self, url: str, quality: str = 'best') -> str:
        """Record YouTube live stream"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = self.output_dir / f'youtube_live_{timestamp}.mp4'
        
        cmd = [
            'yt-dlp',
            '--no-part',
            '-f', f'{quality}/best',
            '-o', str(output_file),
            url
        ]
        
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        recording_id = f"yt_{timestamp}"
        self.active_recordings[recording_id] = asyncio.create_task(process.wait())
        
        return recording_id
        
    async def record_twitch(self, channel: str, quality: str = 'best') -> str:
        """Record Twitch live stream"""
        url = f"https://twitch.tv/{channel}"
        return await self.record_stream(url, quality)
        
    async def stop_recording(self, recording_id: str) -> bool:
        """Stop active recording"""
        if recording_id in self.active_recordings:
            task = self.active_recordings[recording_id]
            task.cancel()
            del self.active_recordings[recording_id]
            return True
        return False
        
    async def schedule_recording(self, url: str, start_time: datetime, 
                                 duration: int, quality: str = 'best') -> str:
        """Schedule a recording for future time"""
        now = datetime.now()
        delay = (start_time - now).total_seconds()
        
        if delay > 0:
            await asyncio.sleep(delay)
            
        return await self.record_stream(url, quality, duration)
        
    def get_active_recordings(self) -> list:
        """Get list of active recordings"""
        return list(self.active_recordings.keys())
        
    async def monitor_channel(self, url: str, check_interval: int = 60):
        """Monitor channel and auto-record when live"""
        while True:
            try:
                streams = streamlink.streams(url)
                if streams:
                    print(f"Stream detected! Starting recording...")
                    await self.record_stream(url)
                    break
            except:
                pass
                
            await asyncio.sleep(check_interval)
