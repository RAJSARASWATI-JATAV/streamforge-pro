"""Voice Command Controller"""
import speech_recognition as sr
import pyttsx3
import re
from typing import Optional, Callable

class VoiceController:
    """Handle voice commands for StreamForge"""
    
    def __init__(self, download_manager):
        self.download_manager = download_manager
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.listening = False
        
    def speak(self, text: str):
        """Text-to-speech output"""
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self) -> Optional[str]:
        """Listen for voice command"""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio).lower()
                return command
            except sr.UnknownValueError:
                return None
            except sr.RequestError:
                self.speak("Speech recognition service unavailable")
                return None
                
    async def process_command(self, command: str):
        """Process voice command"""
        if "download" in command:
            url_match = re.search(r'(https?://[^\s]+)', command)
            if url_match:
                url = url_match.group(1)
                quality = "1080p" if "high quality" in command else "best"
                await self.download_manager.add_download(url, quality)
                self.speak("Download started")
            else:
                self.speak("Please provide a URL")
                
        elif "pause" in command:
            self.speak("Pausing downloads")
            
        elif "resume" in command:
            self.speak("Resuming downloads")
            
        elif "status" in command:
            active = len(self.download_manager.active_downloads)
            self.speak(f"You have {active} active downloads")
            
        elif "stop listening" in command or "exit" in command:
            self.speak("Goodbye")
            self.listening = False
            
    async def start_listening(self):
        """Start voice command loop"""
        self.listening = True
        self.speak("Voice control activated. Say 'stop listening' to exit")
        
        while self.listening:
            command = self.listen()
            if command:
                print(f"Command: {command}")
                await self.process_command(command)
