"""AI-Powered Quality Optimizer"""
import psutil
import json
from pathlib import Path
from datetime import datetime

class AIQualityOptimizer:
    def __init__(self):
        self.history_file = Path("quality_history.json")
        self.history = self._load_history()
        self.learning_enabled = True
    
    def _load_history(self):
        if self.history_file.exists():
            with open(self.history_file) as f:
                return json.load(f)
        return {'downloads': [], 'preferences': {}}
    
    def _save_history(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def analyze_system(self):
        """Analyze system capabilities"""
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return {
            'cpu_usage': cpu_percent,
            'memory_available_gb': memory.available / (1024**3),
            'disk_free_gb': disk.free / (1024**3),
            'performance_score': self._calculate_performance_score(cpu_percent, memory.percent)
        }
    
    def _calculate_performance_score(self, cpu, memory_percent):
        """Calculate system performance score (0-100)"""
        cpu_score = 100 - cpu
        memory_score = 100 - memory_percent
        return (cpu_score + memory_score) / 2
    
    def predict_best_quality(self, video_duration=600, platform='youtube'):
        """AI prediction for best quality"""
        system = self.analyze_system()
        
        # Learn from history
        if self.history['downloads']:
            user_preference = self._analyze_user_preference()
        else:
            user_preference = '1080p'
        
        # Decision logic
        if system['disk_free_gb'] < 5:
            return '480p', 'Low disk space'
        elif system['performance_score'] < 30:
            return '720p', 'System under load'
        elif system['memory_available_gb'] < 2:
            return '720p', 'Low memory'
        elif video_duration > 3600:  # > 1 hour
            return '720p', 'Long video - optimize size'
        else:
            return user_preference, 'Based on your preferences'
    
    def _analyze_user_preference(self):
        """Analyze user's quality preferences from history"""
        quality_counts = {}
        for download in self.history['downloads'][-20:]:  # Last 20
            quality = download.get('quality', '1080p')
            quality_counts[quality] = quality_counts.get(quality, 0) + 1
        
        if quality_counts:
            return max(quality_counts, key=quality_counts.get)
        return '1080p'
    
    def record_download(self, url, quality, success, filesize_mb):
        """Record download for learning"""
        self.history['downloads'].append({
            'url': url,
            'quality': quality,
            'success': success,
            'filesize_mb': filesize_mb,
            'timestamp': datetime.now().isoformat()
        })
        
        # Keep only last 100 downloads
        if len(self.history['downloads']) > 100:
            self.history['downloads'] = self.history['downloads'][-100:]
        
        self._save_history()
    
    def get_recommendations(self):
        """Get AI recommendations"""
        system = self.analyze_system()
        quality, reason = self.predict_best_quality()
        
        return {
            'recommended_quality': quality,
            'reason': reason,
            'system_health': 'Good' if system['performance_score'] > 70 else 'Fair' if system['performance_score'] > 40 else 'Poor',
            'disk_warning': system['disk_free_gb'] < 10,
            'memory_warning': system['memory_available_gb'] < 4
        }
    
    def optimize_for_device(self, device_type='desktop'):
        """Optimize quality for device type"""
        device_profiles = {
            'mobile': '480p',
            'tablet': '720p',
            'laptop': '1080p',
            'desktop': '1080p',
            '4k_tv': '4K'
        }
        return device_profiles.get(device_type, '1080p')

if __name__ == "__main__":
    optimizer = AIQualityOptimizer()
    
    print("🤖 AI Quality Optimizer")
    print("="*60)
    
    system = optimizer.analyze_system()
    print(f"\n📊 System Analysis:")
    print(f"   CPU Usage: {system['cpu_usage']:.1f}%")
    print(f"   Memory Available: {system['memory_available_gb']:.1f} GB")
    print(f"   Disk Free: {system['disk_free_gb']:.1f} GB")
    print(f"   Performance Score: {system['performance_score']:.1f}/100")
    
    recommendations = optimizer.get_recommendations()
    print(f"\n💡 AI Recommendations:")
    print(f"   Quality: {recommendations['recommended_quality']}")
    print(f"   Reason: {recommendations['reason']}")
    print(f"   System Health: {recommendations['system_health']}")
    
    if recommendations['disk_warning']:
        print(f"   ⚠️ Warning: Low disk space!")
    if recommendations['memory_warning']:
        print(f"   ⚠️ Warning: Low memory!")
