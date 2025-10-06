"""
Custom Theme System for StreamForge-Pro
Created by RAJSARASWATI JATAV
"""
from typing import Dict
import json
from pathlib import Path

class Theme:
    """Theme configuration"""
    def __init__(self, name: str, colors: Dict[str, str]):
        self.name = name
        self.colors = colors
    
    def get_color(self, key: str) -> str:
        return self.colors.get(key, "\033[0m")

class ThemeManager:
    """Manage custom themes"""
    
    THEMES = {
        "hacker": {
            "primary": "\033[92m",      # Green
            "secondary": "\033[96m",    # Cyan
            "accent": "\033[93m",       # Yellow
            "error": "\033[91m",        # Red
            "success": "\033[92m",      # Green
            "warning": "\033[93m",      # Yellow
            "info": "\033[94m",         # Blue
            "reset": "\033[0m"
        },
        "cyberpunk": {
            "primary": "\033[95m",      # Magenta
            "secondary": "\033[96m",    # Cyan
            "accent": "\033[93m",       # Yellow
            "error": "\033[91m",        # Red
            "success": "\033[92m",      # Green
            "warning": "\033[93m",      # Yellow
            "info": "\033[94m",         # Blue
            "reset": "\033[0m"
        },
        "ocean": {
            "primary": "\033[94m",      # Blue
            "secondary": "\033[96m",    # Cyan
            "accent": "\033[92m",       # Green
            "error": "\033[91m",        # Red
            "success": "\033[92m",      # Green
            "warning": "\033[93m",      # Yellow
            "info": "\033[94m",         # Blue
            "reset": "\033[0m"
        },
        "sunset": {
            "primary": "\033[91m",      # Red
            "secondary": "\033[93m",    # Yellow
            "accent": "\033[95m",       # Magenta
            "error": "\033[91m",        # Red
            "success": "\033[92m",      # Green
            "warning": "\033[93m",      # Yellow
            "info": "\033[94m",         # Blue
            "reset": "\033[0m"
        },
        "forest": {
            "primary": "\033[92m",      # Green
            "secondary": "\033[32m",    # Dark Green
            "accent": "\033[93m",       # Yellow
            "error": "\033[91m",        # Red
            "success": "\033[92m",      # Green
            "warning": "\033[93m",      # Yellow
            "info": "\033[94m",         # Blue
            "reset": "\033[0m"
        }
    }
    
    def __init__(self):
        self.current_theme = "hacker"
        self.custom_themes_dir = Path.home() / ".streamforge" / "themes"
        self.custom_themes_dir.mkdir(parents=True, exist_ok=True)
        self.load_custom_themes()
    
    def load_custom_themes(self):
        """Load custom themes from user directory"""
        for theme_file in self.custom_themes_dir.glob("*.json"):
            try:
                with open(theme_file, 'r') as f:
                    theme_data = json.load(f)
                    self.THEMES[theme_data['name']] = theme_data['colors']
            except Exception as e:
                print(f"Error loading theme {theme_file}: {e}")
    
    def set_theme(self, theme_name: str) -> bool:
        """Set active theme"""
        if theme_name in self.THEMES:
            self.current_theme = theme_name
            return True
        return False
    
    def get_theme(self, theme_name: str = None) -> Theme:
        """Get theme by name"""
        name = theme_name or self.current_theme
        colors = self.THEMES.get(name, self.THEMES["hacker"])
        return Theme(name, colors)
    
    def list_themes(self) -> list:
        """List all available themes"""
        return list(self.THEMES.keys())
    
    def create_custom_theme(self, name: str, colors: Dict[str, str]):
        """Create a custom theme"""
        theme_file = self.custom_themes_dir / f"{name}.json"
        theme_data = {"name": name, "colors": colors}
        with open(theme_file, 'w') as f:
            json.dump(theme_data, f, indent=2)
        self.THEMES[name] = colors
        return True
    
    def preview_theme(self, theme_name: str):
        """Preview a theme"""
        theme = self.get_theme(theme_name)
        print(f"\n{theme.get_color('primary')}╔═══════════════════════════════════════╗")
        print(f"{theme.get_color('primary')}║  Theme Preview: {theme_name.upper():<20} ║")
        print(f"{theme.get_color('primary')}╚═══════════════════════════════════════╝{theme.get_color('reset')}")
        print(f"{theme.get_color('primary')}Primary: Sample Text")
        print(f"{theme.get_color('secondary')}Secondary: Sample Text")
        print(f"{theme.get_color('accent')}Accent: Sample Text")
        print(f"{theme.get_color('success')}Success: Operation completed")
        print(f"{theme.get_color('warning')}Warning: Check this")
        print(f"{theme.get_color('error')}Error: Something failed")
        print(f"{theme.get_color('info')}Info: Information message{theme.get_color('reset')}\n")
