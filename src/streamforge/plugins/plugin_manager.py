"""
Plugin System for StreamForge-Pro
Created by RAJSARASWATI JATAV
"""
import importlib
import inspect
from pathlib import Path
from typing import Dict, List, Any

class BasePlugin:
    """Base class for all plugins"""
    name = "Base Plugin"
    version = "1.0.0"
    author = "RAJSARASWATI JATAV"
    
    def initialize(self):
        """Initialize plugin"""
        pass
    
    def execute(self, *args, **kwargs):
        """Execute plugin functionality"""
        raise NotImplementedError

class PluginManager:
    """Manage plugins for StreamForge-Pro"""
    
    def __init__(self):
        self.plugins: Dict[str, BasePlugin] = {}
        self.plugin_dir = Path(__file__).parent / "community"
        self.plugin_dir.mkdir(exist_ok=True)
    
    def load_plugin(self, plugin_path: str) -> bool:
        """Load a plugin from file"""
        try:
            spec = importlib.util.spec_from_file_location("plugin", plugin_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, BasePlugin) and obj != BasePlugin:
                    plugin = obj()
                    plugin.initialize()
                    self.plugins[plugin.name] = plugin
                    return True
            return False
        except Exception as e:
            print(f"Error loading plugin: {e}")
            return False
    
    def load_all_plugins(self):
        """Load all plugins from plugin directory"""
        for plugin_file in self.plugin_dir.glob("*.py"):
            if plugin_file.name != "__init__.py":
                self.load_plugin(str(plugin_file))
    
    def get_plugin(self, name: str) -> BasePlugin:
        """Get plugin by name"""
        return self.plugins.get(name)
    
    def list_plugins(self) -> List[str]:
        """List all loaded plugins"""
        return list(self.plugins.keys())
    
    def execute_plugin(self, name: str, *args, **kwargs) -> Any:
        """Execute a plugin"""
        plugin = self.get_plugin(name)
        if plugin:
            return plugin.execute(*args, **kwargs)
        raise ValueError(f"Plugin '{name}' not found")
