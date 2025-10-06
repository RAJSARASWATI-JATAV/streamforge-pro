#!/usr/bin/env python3
"""API Server Launcher - Created by RAJSARASWATI JATAV"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from streamforge.api import start_api_server

if __name__ == "__main__":
    start_api_server()
