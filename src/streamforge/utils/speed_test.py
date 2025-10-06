"""Internet Speed Test"""
import time
import requests

class SpeedTest:
    def __init__(self):
        self.test_url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
    
    def test_download_speed(self):
        print("\n🚀 Testing download speed...")
        try:
            start = time.time()
            response = requests.get(self.test_url, timeout=10)
            elapsed = time.time() - start
            
            size_mb = len(response.content) / (1024 * 1024)
            speed_mbps = (size_mb / elapsed) * 8
            
            print(f"📊 Download Speed: {speed_mbps:.2f} Mbps")
            print(f"⏱️  Time: {elapsed:.2f}s")
            
            if speed_mbps > 10:
                print("✅ Excellent connection!")
            elif speed_mbps > 5:
                print("✅ Good connection")
            else:
                print("⚠️  Slow connection")
            
            return speed_mbps
        except Exception as e:
            print(f"❌ Error: {e}")
            return 0

def main():
    tester = SpeedTest()
    tester.test_download_speed()

if __name__ == "__main__":
    main()
