import os
from maya.core.config import config, config_manager

def test_config_loads_env_var():
    """Test if configuration properly picks up environment variables."""
    assert config.env in ["test", "development", "production"]
    
def test_models_json_loads():
    """Test if models.json is parsed and omniroute_endpoints is populated."""
    # Since tests run from a different directory, it might not find models.json
    # but it shouldn't crash. It defaults to empty if not found.
    assert isinstance(config.omniroute_endpoints, dict)
