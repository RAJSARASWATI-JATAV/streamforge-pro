#!/usr/bin/env python3
"""Live Server Launcher - Created by RAJSARASWATI JATAV"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from streamforge.web.live_server import start_live_server

if __name__ == "__main__":
    start_live_server()
