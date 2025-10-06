"""Video Metadata Editor"""
import subprocess

class MetadataEditor:
    def edit_metadata(self, file, title=None, artist=None, album=None):
        print(f"📝 Editing metadata for {file}")
        try:
            cmd = ['ffmpeg', '-i', file, '-c', 'copy']
            if title:
                cmd.extend(['-metadata', f'title={title}'])
            if artist:
                cmd.extend(['-metadata', f'artist={artist}'])
            if album:
                cmd.extend(['-metadata', f'album={album}'])
            cmd.append(f'edited_{file}')
            subprocess.run(cmd, check=True)
            print("✅ Metadata updated!")
        except Exception as e:
            print(f"❌ Error: {e}")
