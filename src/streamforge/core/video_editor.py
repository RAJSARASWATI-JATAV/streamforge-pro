"""Video Editor - Trim, Merge, Add Watermark"""
import subprocess
from pathlib import Path

class VideoEditor:
    def __init__(self):
        self.ffmpeg = 'ffmpeg'
    
    def trim_video(self, input_file, output_file, start_time, end_time):
        """Trim video from start_time to end_time (format: HH:MM:SS)"""
        print(f"\n✂️ Trimming video...")
        print(f"📁 Input: {input_file}")
        print(f"⏱️ From {start_time} to {end_time}")
        
        try:
            cmd = [
                self.ffmpeg, '-i', input_file,
                '-ss', start_time, '-to', end_time,
                '-c', 'copy', output_file, '-y'
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✅ Trimmed: {output_file}")
            return output_file
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def merge_videos(self, video_files, output_file):
        """Merge multiple videos"""
        print(f"\n🔗 Merging {len(video_files)} videos...")
        
        # Create file list
        list_file = Path("temp_filelist.txt")
        with open(list_file, 'w') as f:
            for video in video_files:
                f.write(f"file '{video}'\n")
        
        try:
            cmd = [
                self.ffmpeg, '-f', 'concat', '-safe', '0',
                '-i', str(list_file), '-c', 'copy',
                output_file, '-y'
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            list_file.unlink()
            print(f"✅ Merged: {output_file}")
            return output_file
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def add_watermark(self, input_file, output_file, watermark_text, position='bottom-right'):
        """Add text watermark"""
        print(f"\n💧 Adding watermark: {watermark_text}")
        
        positions = {
            'top-left': 'x=10:y=10',
            'top-right': 'x=w-tw-10:y=10',
            'bottom-left': 'x=10:y=h-th-10',
            'bottom-right': 'x=w-tw-10:y=h-th-10',
            'center': 'x=(w-tw)/2:y=(h-th)/2'
        }
        
        pos = positions.get(position, positions['bottom-right'])
        
        try:
            cmd = [
                self.ffmpeg, '-i', input_file,
                '-vf', f"drawtext=text='{watermark_text}':fontsize=24:fontcolor=white:{pos}",
                '-codec:a', 'copy', output_file, '-y'
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✅ Watermarked: {output_file}")
            return output_file
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def extract_audio(self, input_file, output_file):
        """Extract audio from video"""
        print(f"\n🎵 Extracting audio...")
        
        try:
            cmd = [
                self.ffmpeg, '-i', input_file,
                '-vn', '-acodec', 'libmp3lame',
                '-q:a', '2', output_file, '-y'
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✅ Audio extracted: {output_file}")
            return output_file
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def create_gif(self, input_file, output_file, start_time='00:00:00', duration=5):
        """Create GIF from video"""
        print(f"\n🎞️ Creating GIF...")
        
        try:
            cmd = [
                self.ffmpeg, '-i', input_file,
                '-ss', start_time, '-t', str(duration),
                '-vf', 'fps=10,scale=480:-1:flags=lanczos',
                output_file, '-y'
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✅ GIF created: {output_file}")
            return output_file
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

if __name__ == "__main__":
    editor = VideoEditor()
    print("\n🎬 Video Editor")
    print("1. Trim video")
    print("2. Add watermark")
    print("3. Extract audio")
    print("4. Create GIF")
    
    choice = input("\nSelect: ")
    
    if choice == '1':
        input_file = input("Input file: ")
        output_file = input("Output file: ")
        start = input("Start time (HH:MM:SS): ")
        end = input("End time (HH:MM:SS): ")
        editor.trim_video(input_file, output_file, start, end)
    elif choice == '2':
        input_file = input("Input file: ")
        output_file = input("Output file: ")
        text = input("Watermark text: ")
        editor.add_watermark(input_file, output_file, text)
    elif choice == '3':
        input_file = input("Input file: ")
        output_file = input("Output file (mp3): ")
        editor.extract_audio(input_file, output_file)
    elif choice == '4':
        input_file = input("Input file: ")
        output_file = input("Output file (gif): ")
        editor.create_gif(input_file, output_file)
