"""Network Speed Monitor"""
import time
import requests

class NetworkMonitor:
    def __init__(self):
        self.speeds = []
    
    def test_speed(self):
        try:
            start = time.time()
            response = requests.get('https://www.google.com', timeout=5)
            elapsed = time.time() - start
            speed = len(response.content) / elapsed / 1024  # KB/s
            self.speeds.append(speed)
            return speed
        except:
            return 0
    
    def get_average_speed(self):
        return sum(self.speeds) / len(self.speeds) if self.speeds else 0
    
    def is_fast_connection(self):
        return self.get_average_speed() > 500  # 500 KB/s threshold
