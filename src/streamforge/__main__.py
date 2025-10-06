"""
StreamForge-Pro Main Entry Point
"""

import sys
import asyncio
from pathlib import Path

def print_banner():
    """Display StreamForge-Pro banner"""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗      ║
║   ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║      ║
║   ███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║      ║
║   ╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║      ║
║   ███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║      ║
║   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝      ║
║                                                               ║
║              ███████╗ ██████╗ ██████╗  ██████╗ ███████╗      ║
║              ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝      ║
║              █████╗  ██║   ██║██████╔╝██║  ███╗█████╗        ║
║              ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝        ║
║              ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗      ║
║              ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ║
║                                                               ║
║                         -═ PRO ═-                            ║
║                                                               ║
║              Advanced Multi-Platform Media Downloader        ║
║                      Version 1.0.0                           ║
║                                                               ║
║                    Created by Raj Saraswati                  ║
║              https://github.com/rajsaraswati/streamforge-pro ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
    print(banner)

async def main():
    """Main application entry point"""
    try:
        print_banner()
        print("\n🎬 Welcome to StreamForge-Pro!")
        print("\n📦 Installation successful!")
        print("\n🚀 Quick Start:")
        print("   streamforge --download <URL>     # Quick download")
        print("   streamforge --cli                # Interactive CLI")
        print("   streamforge --gui                # Launch GUI")
        print("   streamforge --web                # Start web server")
        print("   streamforge --help               # Show all options")
        print("\n📖 Documentation: https://docs.streamforge.pro")
        print("💬 Support: https://github.com/rajsaraswati/streamforge-pro/issues")
        print("\n✨ Happy Downloading!\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
