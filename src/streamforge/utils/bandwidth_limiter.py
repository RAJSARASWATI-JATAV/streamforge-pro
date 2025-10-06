"""Bandwidth Limiter"""
import time

class BandwidthLimiter:
    def __init__(self, limit_mbps=10):
        self.limit_mbps = limit_mbps
        self.limit_bytes_per_sec = limit_mbps * 1024 * 1024 / 8
    
    def limit(self, bytes_downloaded, elapsed_time):
        expected_time = bytes_downloaded / self.limit_bytes_per_sec
        if elapsed_time < expected_time:
            time.sleep(expected_time - elapsed_time)
