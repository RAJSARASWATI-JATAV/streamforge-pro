"""Quick launcher for interactive CLI"""
import sys
import asyncio
sys.path.insert(0, 'src')

from streamforge.cli.interactive_cli import main

if __name__ == "__main__":
    asyncio.run(main())
