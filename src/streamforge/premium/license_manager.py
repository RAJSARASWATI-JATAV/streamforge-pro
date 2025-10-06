"""
StreamForge-Pro Premium License Manager
Created by RAJSARASWATI JATAV
Copyright (c) 2025 RAJSARASWATI JATAV
"""

import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path

class LicenseManager:
    """Manage premium licenses"""
    
    TIERS = {
        'free': {
            'name': 'Free (All Features Unlocked)',
            'price': 0,
            'downloads_per_day': -1,  # Unlimited
            'max_quality': '8K',
            'concurrent_downloads': 10,
            'features': ['all_features', 'unlimited', 'instagram_pro', 'tiktok_pro', 'cloud_upload', 'voice_commands', 'api_access']
        },
        'basic': {
            'name': 'Basic',
            'price': 9.99,
            'downloads_per_day': 50,
            'max_quality': '1080p',
            'concurrent_downloads': 3,
            'features': ['batch_download', 'playlist', 'quality_selector']
        },
        'pro': {
            'name': 'Pro',
            'price': 19.99,
            'downloads_per_day': 200,
            'max_quality': '4K',
            'concurrent_downloads': 5,
            'features': ['instagram_pro', 'tiktok_pro', 'cloud_upload', 'no_watermark', 'voice_commands']
        },
        'enterprise': {
            'name': 'Enterprise',
            'price': 49.99,
            'downloads_per_day': -1,
            'max_quality': '8K',
            'concurrent_downloads': 10,
            'features': ['api_access', 'priority_support', 'custom_branding', 'team_management', 'unlimited']
        }
    }
    
    def __init__(self):
        self.license_file = Path.home() / '.streamforge' / 'license.json'
        self.license_file.parent.mkdir(exist_ok=True)
    
    def generate_license_key(self, email: str, tier: str) -> str:
        """Generate license key"""
        data = f"{email}:{tier}:{datetime.now().isoformat()}"
        key = hashlib.sha256(data.encode()).hexdigest()[:24].upper()
        return f"SF-{tier[:3].upper()}-{key[:8]}-{key[8:16]}-{key[16:24]}"
    
    def activate_license(self, license_key: str, email: str) -> bool:
        """Activate premium license"""
        try:
            tier_map = {'FRE': 'free', 'BAS': 'basic', 'PRO': 'pro', 'ENT': 'enterprise'}
            tier = tier_map.get(license_key.split('-')[1], 'free')
            
            license_data = {
                'key': license_key,
                'email': email,
                'tier': tier,
                'activated_at': datetime.now().isoformat(),
                'expires_at': (datetime.now() + timedelta(days=365)).isoformat(),
                'status': 'active'
            }
            
            with open(self.license_file, 'w') as f:
                json.dump(license_data, f, indent=2)
            
            return True
        except:
            return False
    
    def get_license_info(self) -> dict:
        """Get current license information"""
        try:
            if not self.license_file.exists():
                return self.TIERS['free']
            
            with open(self.license_file, 'r') as f:
                license_data = json.load(f)
            
            expires_at = datetime.fromisoformat(license_data['expires_at'])
            if datetime.now() > expires_at:
                license_data['tier'] = 'free'
            
            tier_info = self.TIERS[license_data['tier']].copy()
            tier_info.update(license_data)
            return tier_info
        except:
            return self.TIERS['free']
    
    def check_feature(self, feature: str) -> bool:
        """Check if feature is available"""
        license_info = self.get_license_info()
        return feature in license_info.get('features', [])
