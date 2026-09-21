import os
import json
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class OmniRouteConfig:
    provider: str
    model: str
    api_key_env: str

@dataclass
class AppConfig:
    env: str
    omniroute_endpoints: Dict[str, OmniRouteConfig]
    debug: bool = False

class ConfigManager:
    """Manages application configuration, environment variables, and model routing."""
    
    def __init__(self, root_dir: Optional[Path] = None):
        self.root_dir = root_dir or Path(__file__).resolve().parent.parent.parent.parent
        self.config_dir = self.root_dir / "config"
        self._load_env()
        self.config = self._load_config()

    def _load_env(self):
        """Simple standard library .env loader."""
        env_file = self.root_dir / ".env"
        if not env_file.exists():
            return
            
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip("'\"")
                    # Only set if not already in environment
                    if key not in os.environ:
                        os.environ[key] = value

    def _load_config(self) -> AppConfig:
        """Load configuration from JSON files."""
        models_file = self.config_dir / "models.json"
        
        models_data = {}
        if models_file.exists():
            with open(models_file, "r", encoding="utf-8") as f:
                models_data = json.load(f)
                
        endpoints = {}
        for task_type, data in models_data.get("routes", {}).items():
            endpoints[task_type] = OmniRouteConfig(
                provider=data.get("provider", "unknown"),
                model=data.get("model", "unknown"),
                api_key_env=data.get("api_key_env", "")
            )
            
        return AppConfig(
            env=os.getenv("MAYA_ENV", "development"),
            debug=os.getenv("MAYA_DEBUG", "false").lower() == "true",
            omniroute_endpoints=endpoints
        )

    def get_api_key(self, env_var_name: str) -> Optional[str]:
        """Safely retrieve an API key from the environment."""
        return os.getenv(env_var_name)

# Global configuration instance
config_manager = ConfigManager()
config = config_manager.config
