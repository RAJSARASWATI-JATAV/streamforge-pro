"""Video Trimmer"""
import subprocess

class VideoTrimmer:
    def trim(self, input_file, output_file, start_time, end_time):
        print(f"✂️  Trimming video: {start_time} to {end_time}")
        try:
            cmd = ['ffmpeg', '-i', input_file, '-ss', start_time, '-to', end_time, '-c', 'copy', output_file]
            subprocess.run(cmd, check=True)
            print(f"✅ Trimmed: {output_file}")
        except Exception as e:
            print(f"❌ Error: {e}")
