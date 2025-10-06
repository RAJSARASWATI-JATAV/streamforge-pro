"""
StreamForge-Pro Voice Commands
Created by RAJSARASWATI JATAV
Copyright (c) 2025 RAJSARASWATI JATAV
"""

import speech_recognition as sr
from typing import Optional

class VoiceCommands:
    """Voice command handler for StreamForge-Pro"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.commands = {
            'download': self.download_video,
            'pause': self.pause_download,
            'resume': self.resume_download,
            'stop': self.stop_download,
            'status': self.check_status,
            'help': self.show_help
        }
    
    def listen(self) -> Optional[str]:
        """Listen for voice command"""
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
                
            command = self.recognizer.recognize_google(audio).lower()
            print(f"✅ Heard: {command}")
            return command
            
        except sr.WaitTimeoutError:
            print("⏱️ Timeout")
            return None
        except sr.UnknownValueError:
            print("❌ Could not understand")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def process_command(self, command: str):
        """Process voice command"""
        for keyword, func in self.commands.items():
            if keyword in command:
                func(command)
                return
        print("❌ Unknown command. Say 'help' for commands.")
    
    def download_video(self, command: str):
        """Download video command"""
        print("📥 Starting download...")
        # Integration with downloader
    
    def pause_download(self, command: str):
        """Pause download"""
        print("⏸️ Pausing download...")
    
    def resume_download(self, command: str):
        """Resume download"""
        print("▶️ Resuming download...")
    
    def stop_download(self, command: str):
        """Stop download"""
        print("⏹️ Stopping download...")
    
    def check_status(self, command: str):
        """Check download status"""
        print("📊 Checking status...")
    
    def show_help(self, command: str):
        """Show available commands"""
        print("""
🎤 Available Voice Commands:
- "download [URL]" - Start download
- "pause" - Pause current download
- "resume" - Resume download
- "stop" - Stop download
- "status" - Check download status
- "help" - Show this help
        """)
    
    def run(self):
        """Run voice command loop"""
        print("🎤 StreamForge-Pro Voice Commands")
        print("Created by RAJSARASWATI JATAV")
        print("Say 'help' for available commands\n")
        
        while True:
            command = self.listen()
            if command:
                if 'exit' in command or 'quit' in command:
                    print("👋 Goodbye!")
                    break
                self.process_command(command)

if __name__ == '__main__':
    voice = VoiceCommands()
    voice.run()
