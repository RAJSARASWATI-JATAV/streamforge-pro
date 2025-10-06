"""Audio File Merger"""
import subprocess

class AudioMerger:
    def merge_audio_files(self, files, output='merged.mp3'):
        print(f"🎵 Merging {len(files)} audio files")
        try:
            with open('filelist.txt', 'w') as f:
                for file in files:
                    f.write(f"file '{file}'\n")
            
            cmd = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c', 'copy', output]
            subprocess.run(cmd, check=True)
            print(f"✅ Merged: {output}")
        except Exception as e:
            print(f"❌ Error: {e}")
