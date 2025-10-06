"""Video Compressor"""
import subprocess

class VideoCompressor:
    def compress(self, input_file, output_file, quality='medium'):
        crf = {'low': 28, 'medium': 23, 'high': 18}[quality]
        print(f"🗜️  Compressing video (quality: {quality})")
        try:
            cmd = ['ffmpeg', '-i', input_file, '-vcodec', 'libx264', '-crf', str(crf), output_file]
            subprocess.run(cmd, check=True)
            print(f"✅ Compressed: {output_file}")
        except Exception as e:
            print(f"❌ Error: {e}")
