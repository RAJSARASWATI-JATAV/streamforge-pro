"""Intelligent Quality Selector"""
import psutil
from enum import Enum

class NetworkSpeed(Enum):
    SLOW = "slow"      # < 5 Mbps
    MEDIUM = "medium"  # 5-20 Mbps
    FAST = "fast"      # > 20 Mbps

class QualityProfile:
    def __init__(self, name: str, max_resolution: str, max_filesize_mb: int):
        self.name = name
        self.max_resolution = max_resolution
        self.max_filesize_mb = max_filesize_mb

class QualitySelector:
    """Smart quality selection based on network and device"""
    
    PROFILES = {
        'mobile': QualityProfile('Mobile', '480p', 100),
        'balanced': QualityProfile('Balanced', '720p', 300),
        'high': QualityProfile('High Quality', '1080p', 800),
        'ultra': QualityProfile('Ultra', '4K', 2000),
    }
    
    def __init__(self):
        self.network_speed = self._detect_network_speed()
        self.available_storage = self._get_available_storage()
    
    def _detect_network_speed(self) -> NetworkSpeed:
        """Detect network speed (simplified)"""
        # In real implementation, would do actual speed test
        return NetworkSpeed.MEDIUM
    
    def _get_available_storage(self) -> float:
        """Get available disk space in GB"""
        disk = psutil.disk_usage('/')
        return disk.free / (1024**3)  # Convert to GB
    
    def select_quality(self, auto=True, preferred=None) -> str:
        """Select optimal quality"""
        if not auto and preferred:
            return preferred
        
        # Auto selection logic
        if self.available_storage < 5:
            return '480p'
        elif self.network_speed == NetworkSpeed.SLOW:
            return '480p'
        elif self.network_speed == NetworkSpeed.MEDIUM:
            return '720p'
        else:
            return '1080p'
    
    def get_format_string(self, quality: str) -> str:
        """Get yt-dlp format string"""
        quality_map = {
            '4K': 'bestvideo[height<=2160]+bestaudio/best',
            '1080p': 'bestvideo[height<=1080]+bestaudio/best',
            '720p': 'bestvideo[height<=720]+bestaudio/best',
            '480p': 'bestvideo[height<=480]+bestaudio/best',
            'best': 'best',
        }
        return quality_map.get(quality, 'best')
    
    def get_recommendation(self) -> dict:
        """Get quality recommendation with reasoning"""
        quality = self.select_quality()
        
        return {
            'quality': quality,
            'network': self.network_speed.value,
            'storage_gb': round(self.available_storage, 2),
            'reason': f"Based on {self.network_speed.value} network and {round(self.available_storage, 1)}GB storage"
        }

def main():
    """Test quality selector"""
    selector = QualitySelector()
    
    print("🎯 Quality Selector")
    print(f"\n📊 System Info:")
    print(f"   Network: {selector.network_speed.value}")
    print(f"   Storage: {selector.available_storage:.1f} GB")
    
    rec = selector.get_recommendation()
    print(f"\n✅ Recommended Quality: {rec['quality']}")
    print(f"   Reason: {rec['reason']}")
    
    print(f"\n📝 Format String: {selector.get_format_string(rec['quality'])}")

if __name__ == "__main__":
    main()
