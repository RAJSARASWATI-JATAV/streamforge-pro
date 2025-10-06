"""Video Editor using FFmpeg"""
import asyncio
import subprocess
from pathlib import Path
from typing import Optional, Tuple

class VideoEditor:
    """Video editing operations using FFmpeg"""
    
    def __init__(self):
        self.ffmpeg_path = "ffmpeg"
        
    async def _run_ffmpeg(self, args: list) -> bool:
        """Run FFmpeg command asynchronously"""
        cmd = [self.ffmpeg_path] + args
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await process.communicate()
        return process.returncode == 0
        
    async def trim(self, input_path: Path, output_path: Path, start: str, duration: str) -> bool:
        """Trim video (start: HH:MM:SS, duration: HH:MM:SS)"""
        args = [
            '-i', str(input_path),
            '-ss', start,
            '-t', duration,
            '-c', 'copy',
            str(output_path)
        ]
        return await self._run_ffmpeg(args)
        
    async def merge(self, input_paths: list, output_path: Path) -> bool:
        """Merge multiple videos"""
        concat_file = output_path.parent / 'concat_list.txt'
        with open(concat_file, 'w') as f:
            for path in input_paths:
                f.write(f"file '{path}'\n")
                
        args = [
            '-f', 'concat',
            '-safe', '0',
            '-i', str(concat_file),
            '-c', 'copy',
            str(output_path)
        ]
        result = await self._run_ffmpeg(args)
        concat_file.unlink()
        return result
        
    async def add_watermark(self, input_path: Path, output_path: Path, 
                           watermark_text: str, position: str = 'bottomright') -> bool:
        """Add text watermark"""
        positions = {
            'topleft': '10:10',
            'topright': 'W-tw-10:10',
            'bottomleft': '10:H-th-10',
            'bottomright': 'W-tw-10:H-th-10',
            'center': '(W-tw)/2:(H-th)/2'
        }
        
        args = [
            '-i', str(input_path),
            '-vf', f"drawtext=text='{watermark_text}':fontsize=24:fontcolor=white:x={positions.get(position, positions['bottomright'])}",
            '-codec:a', 'copy',
            str(output_path)
        ]
        return await self._run_ffmpeg(args)
        
    async def extract_audio(self, input_path: Path, output_path: Path, bitrate: str = '192k') -> bool:
        """Extract audio from video"""
        args = [
            '-i', str(input_path),
            '-vn',
            '-acodec', 'libmp3lame',
            '-ab', bitrate,
            str(output_path)
        ]
        return await self._run_ffmpeg(args)
        
    async def change_speed(self, input_path: Path, output_path: Path, speed: float) -> bool:
        """Change video speed (0.5 = half speed, 2.0 = double speed)"""
        video_speed = 1 / speed
        audio_speed = speed
        
        args = [
            '-i', str(input_path),
            '-filter_complex', f'[0:v]setpts={video_speed}*PTS[v];[0:a]atempo={audio_speed}[a]',
            '-map', '[v]',
            '-map', '[a]',
            str(output_path)
        ]
        return await self._run_ffmpeg(args)
        
    async def add_subtitles(self, input_path: Path, output_path: Path, subtitle_path: Path) -> bool:
        """Add subtitles to video"""
        args = [
            '-i', str(input_path),
            '-vf', f"subtitles={subtitle_path}",
            str(output_path)
        ]
        return await self._run_ffmpeg(args)
        
    async def resize(self, input_path: Path, output_path: Path, width: int, height: int) -> bool:
        """Resize video"""
        args = [
            '-i', str(input_path),
            '-vf', f'scale={width}:{height}',
            str(output_path)
        ]
        return await self._run_ffmpeg(args)
        
    async def rotate(self, input_path: Path, output_path: Path, angle: int) -> bool:
        """Rotate video (90, 180, 270 degrees)"""
        transpose_map = {90: '1', 180: '2,transpose=2', 270: '2'}
        args = [
            '-i', str(input_path),
            '-vf', f'transpose={transpose_map.get(angle, "1")}',
            str(output_path)
        ]
        return await self._run_ffmpeg(args)
        
    async def create_gif(self, input_path: Path, output_path: Path, 
                        start: str = '0', duration: str = '5', fps: int = 10) -> bool:
        """Create GIF from video"""
        args = [
            '-i', str(input_path),
            '-ss', start,
            '-t', duration,
            '-vf', f'fps={fps},scale=480:-1:flags=lanczos',
            str(output_path)
        ]
        return await self._run_ffmpeg(args)
