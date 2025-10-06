"""Advanced Quality Selector with User Preferences & Custom Choices"""
import json
from pathlib import Path
import psutil

class UserPreferences:
    def __init__(self, config_file="user_preferences.json"):
        self.config_file = Path(config_file)
        self.prefs = self._load_preferences()
    
    def _load_preferences(self):
        if self.config_file.exists():
            with open(self.config_file) as f:
                return json.load(f)
        return {
            'default_quality': 'auto',
            'preferred_format': 'mp4',
            'max_filesize_mb': 0,  # 0 = unlimited
            'prefer_audio_quality': '192k',
            'auto_subtitle': False,
            'auto_thumbnail': True,
            'bandwidth_limit': 0,
            'quality_profiles': {
                'mobile': {'resolution': '480p', 'format': 'mp4'},
                'standard': {'resolution': '720p', 'format': 'mp4'},
                'hd': {'resolution': '1080p', 'format': 'mp4'},
                'ultra': {'resolution': '4K', 'format': 'mp4'},
                'audio_only': {'resolution': 'audio', 'format': 'mp3'}
            }
        }
    
    def save_preferences(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.prefs, f, indent=2)
    
    def set_preference(self, key, value):
        self.prefs[key] = value
        self.save_preferences()
    
    def get_preference(self, key, default=None):
        return self.prefs.get(key, default)

class AdvancedQualitySelector:
    """Next-level quality selector with AI-powered recommendations"""
    
    QUALITY_PRESETS = {
        '8K': {'height': 4320, 'bitrate': '50M', 'size_estimate': 5000},
        '4K': {'height': 2160, 'bitrate': '20M', 'size_estimate': 2000},
        '1440p': {'height': 1440, 'bitrate': '10M', 'size_estimate': 1000},
        '1080p': {'height': 1080, 'bitrate': '5M', 'size_estimate': 500},
        '720p': {'height': 720, 'bitrate': '2.5M', 'size_estimate': 250},
        '480p': {'height': 480, 'bitrate': '1M', 'size_estimate': 100},
        '360p': {'height': 360, 'bitrate': '500k', 'size_estimate': 50},
        'audio': {'height': 0, 'bitrate': '192k', 'size_estimate': 10}
    }
    
    def __init__(self):
        self.user_prefs = UserPreferences()
        self.network_speed = self._detect_network_speed()
        self.storage_available = self._get_storage()
        self.device_type = self._detect_device()
    
    def _detect_network_speed(self):
        """Detect network speed (simplified)"""
        # In production, would do actual speed test
        return 'fast'  # fast, medium, slow
    
    def _get_storage(self):
        """Get available storage in GB"""
        disk = psutil.disk_usage('/')
        return disk.free / (1024**3)
    
    def _detect_device(self):
        """Detect device type"""
        # Check screen resolution, CPU, etc.
        return 'desktop'  # desktop, laptop, mobile
    
    def get_custom_quality(self, video_info=None):
        """Get custom quality based on user preferences and video info"""
        default = self.user_prefs.get_preference('default_quality', 'auto')
        
        if default != 'auto':
            return default
        
        # AI-powered recommendation
        if self.storage_available < 5:
            return '480p'
        elif self.network_speed == 'slow':
            return '480p'
        elif self.network_speed == 'medium':
            return '720p'
        elif self.device_type == 'mobile':
            return '720p'
        else:
            return '1080p'
    
    def get_format_options(self, quality):
        """Get yt-dlp format string with custom options"""
        preset = self.QUALITY_PRESETS.get(quality, self.QUALITY_PRESETS['1080p'])
        
        if quality == 'audio':
            return 'bestaudio/best'
        
        format_str = f'bestvideo[height<={preset["height"]}]+bestaudio/best'
        
        # Add filesize limit if set
        max_size = self.user_prefs.get_preference('max_filesize_mb', 0)
        if max_size > 0:
            format_str += f'[filesize<{max_size}M]'
        
        return format_str
    
    def get_download_options(self, quality='auto', custom_options=None):
        """Get complete yt-dlp options with user preferences"""
        if quality == 'auto':
            quality = self.get_custom_quality()
        
        format_str = self.get_format_options(quality)
        preferred_format = self.user_prefs.get_preference('preferred_format', 'mp4')
        
        options = {
            'format': format_str,
            'merge_output_format': preferred_format,
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }
        
        # Add subtitle if enabled
        if self.user_prefs.get_preference('auto_subtitle', False):
            options['writesubtitles'] = True
            options['writeautomaticsub'] = True
        
        # Add thumbnail if enabled
        if self.user_prefs.get_preference('auto_thumbnail', True):
            options['writethumbnail'] = True
        
        # Bandwidth limit
        bandwidth = self.user_prefs.get_preference('bandwidth_limit', 0)
        if bandwidth > 0:
            options['ratelimit'] = bandwidth * 1024 * 1024  # Convert to bytes
        
        # Merge custom options
        if custom_options:
            options.update(custom_options)
        
        return options
    
    def interactive_quality_selection(self):
        """Interactive quality selection menu"""
        print("\n🎯 Quality Selection")
        print("="*60)
        print("\n📊 System Analysis:")
        print(f"   Network: {self.network_speed}")
        print(f"   Storage: {self.storage_available:.1f} GB")
        print(f"   Device: {self.device_type}")
        
        recommended = self.get_custom_quality()
        print(f"\n💡 Recommended: {recommended}")
        
        print("\n📋 Available Qualities:")
        qualities = list(self.QUALITY_PRESETS.keys())
        for i, q in enumerate(qualities, 1):
            preset = self.QUALITY_PRESETS[q]
            print(f"   {i}. {q} (~{preset['size_estimate']}MB per 10min)")
        
        print(f"\n   {len(qualities)+1}. Auto (Recommended)")
        print(f"   {len(qualities)+2}. Custom")
        
        choice = input("\n👉 Select quality: ").strip()
        
        try:
            idx = int(choice) - 1
            if idx < len(qualities):
                return qualities[idx]
            elif idx == len(qualities):
                return 'auto'
            else:
                return self._custom_quality_input()
        except:
            return recommended
    
    def _custom_quality_input(self):
        """Custom quality input"""
        print("\n⚙️ Custom Quality Settings")
        resolution = input("Resolution (e.g., 1080p, 720p): ").strip()
        return resolution if resolution else '1080p'
    
    def save_as_profile(self, profile_name, quality, format='mp4'):
        """Save quality settings as profile"""
        profiles = self.user_prefs.get_preference('quality_profiles', {})
        profiles[profile_name] = {
            'resolution': quality,
            'format': format
        }
        self.user_prefs.set_preference('quality_profiles', profiles)
        print(f"✅ Profile '{profile_name}' saved!")
    
    def load_profile(self, profile_name):
        """Load quality profile"""
        profiles = self.user_prefs.get_preference('quality_profiles', {})
        return profiles.get(profile_name)

if __name__ == "__main__":
    selector = AdvancedQualitySelector()
    
    print("🎬 Advanced Quality Selector")
    print("\n1. Interactive selection")
    print("2. View preferences")
    print("3. Set default quality")
    print("4. Save profile")
    
    choice = input("\nSelect: ")
    
    if choice == '1':
        quality = selector.interactive_quality_selection()
        print(f"\n✅ Selected: {quality}")
        options = selector.get_download_options(quality)
        print(f"\n📝 Download options:")
        for k, v in options.items():
            print(f"   {k}: {v}")
    elif choice == '2':
        print("\n⚙️ Current Preferences:")
        for k, v in selector.user_prefs.prefs.items():
            print(f"   {k}: {v}")
    elif choice == '3':
        quality = input("Default quality (auto/1080p/720p/etc): ")
        selector.user_prefs.set_preference('default_quality', quality)
        print("✅ Saved!")
    elif choice == '4':
        name = input("Profile name: ")
        quality = input("Quality: ")
        selector.save_as_profile(name, quality)
