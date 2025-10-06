#!/usr/bin/env python3
"""
StreamForge-Pro Voice Control Launcher
Created by RAJSARASWATI JATAV
Copyright (c) 2025 RAJSARASWATI JATAV
"""

import sys
sys.path.insert(0, 'src')

from streamforge.voice.voice_commands import VoiceCommands

def main():
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║              StreamForge-Pro v2.1.0 - Voice Control                      ║
║                                                                           ║
║              👨💻 Created by: RAJSARASWATI JATAV 👨💻                    ║
║              🎤 Voice Commands Enabled                                    ║
║                                                                           ║
║              Copyright © 2025 RAJSARASWATI JATAV                         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)
    
    try:
        voice = VoiceCommands()
        voice.run()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
