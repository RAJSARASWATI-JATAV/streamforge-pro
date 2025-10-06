"""Analytics Dashboard"""
from pathlib import Path
import json
from datetime import datetime

class Analytics:
    def __init__(self, data_file="analytics.json"):
        self.data_file = Path(data_file)
        self.data = self._load_data()
    
    def _load_data(self):
        if self.data_file.exists():
            with open(self.data_file) as f:
                return json.load(f)
        return {
            'total_downloads': 0,
            'total_size_mb': 0,
            'downloads_by_platform': {},
            'downloads_by_quality': {},
            'history': []
        }
    
    def _save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def track_download(self, url, platform, quality, size_mb, status='completed'):
        """Track a download"""
        self.data['total_downloads'] += 1
        self.data['total_size_mb'] += size_mb
        
        # By platform
        if platform not in self.data['downloads_by_platform']:
            self.data['downloads_by_platform'][platform] = 0
        self.data['downloads_by_platform'][platform] += 1
        
        # By quality
        if quality not in self.data['downloads_by_quality']:
            self.data['downloads_by_quality'][quality] = 0
        self.data['downloads_by_quality'][quality] += 1
        
        # History
        self.data['history'].append({
            'url': url,
            'platform': platform,
            'quality': quality,
            'size_mb': size_mb,
            'status': status,
            'timestamp': datetime.now().isoformat()
        })
        
        self._save_data()
    
    def get_stats(self):
        """Get statistics"""
        return {
            'total_downloads': self.data['total_downloads'],
            'total_size_gb': round(self.data['total_size_mb'] / 1024, 2),
            'avg_size_mb': round(self.data['total_size_mb'] / max(self.data['total_downloads'], 1), 2),
            'by_platform': self.data['downloads_by_platform'],
            'by_quality': self.data['downloads_by_quality']
        }
    
    def print_dashboard(self):
        """Print analytics dashboard"""
        stats = self.get_stats()
        
        print("\n" + "="*60)
        print("📊 ANALYTICS DASHBOARD")
        print("="*60)
        
        print(f"\n📈 Overall Stats:")
        print(f"   Total Downloads: {stats['total_downloads']}")
        print(f"   Total Size: {stats['total_size_gb']} GB")
        print(f"   Average Size: {stats['avg_size_mb']} MB")
        
        print(f"\n🌐 By Platform:")
        for platform, count in stats['by_platform'].items():
            print(f"   {platform}: {count}")
        
        print(f"\n🎯 By Quality:")
        for quality, count in stats['by_quality'].items():
            print(f"   {quality}: {count}")
        
        print("\n" + "="*60)

if __name__ == "__main__":
    analytics = Analytics()
    analytics.print_dashboard()
