"""Video Format Converter using FFmpeg"""
import subprocess
from pathlib import Path

class VideoConverter:
    def __init__(self):
        self.formats = ['mp4', 'avi', 'mkv', 'webm', 'flv']
    
    def convert(self, input_file, output_format='mp4'):
        print(f"\n🔄 Video Converter")
        print(f"📁 Input: {input_file}")
        print(f"🎯 Format: {output_format}")
        
        input_path = Path(input_file)
        output_path = input_path.with_suffix(f'.{output_format}')
        
        try:
            cmd = [
                'ffmpeg', '-i', str(input_path),
                '-c:v', 'libx264', '-c:a', 'aac',
                str(output_path), '-y'
            ]
            
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✅ Converted: {output_path}")
            return str(output_path)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: {e}")
            return None
        except FileNotFoundError:
            print("❌ FFmpeg not found! Install: choco install ffmpeg")
            return None

def main():
    converter = VideoConverter()
    input_file = input("Enter video file path: ")
    format = input("Output format (mp4/avi/mkv): ") or 'mp4'
    converter.convert(input_file, format)

if __name__ == "__main__":
    main()
