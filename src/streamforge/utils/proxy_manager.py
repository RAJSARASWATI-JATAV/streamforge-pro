"""Proxy Manager for Anonymous Downloads"""
import requests

class ProxyManager:
    def __init__(self):
        self.proxies = []
    
    def add_proxy(self, proxy):
        self.proxies.append(proxy)
        print(f"✅ Proxy added: {proxy}")
    
    def test_proxy(self, proxy):
        try:
            response = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=5)
            print(f"✅ Proxy working: {response.json()}")
            return True
        except:
            print(f"❌ Proxy failed: {proxy}")
            return False
