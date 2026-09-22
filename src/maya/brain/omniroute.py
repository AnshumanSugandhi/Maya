import json
import urllib.request
import urllib.error
from typing import List, Optional
from maya.brain.gateway import ModelGateway
from maya.brain.messages import Message, Role
from maya.core.config import config, config_manager
from maya.core.logger import logger

class OmniRouteGateway(ModelGateway):
    """Concrete implementation for routing requests via OmniRoute."""
    
    def __init__(self, endpoint_url: str = None, default_timeout: int = 30):
        # We allow overriding the endpoint, otherwise it pulls from config (which might not be set yet)
        self.endpoint_url = endpoint_url or config_manager.get_api_key("OMNIROUTE_ENDPOINT") or "https://openrouter.ai/api/v1/chat/completions"
        self.timeout = default_timeout

    def invoke(self, messages: List[Message], task_type: str = "reasoning") -> Optional[Message]:
        route = config.omniroute_endpoints.get(task_type)
        if not route:
            logger.warning(f"No OmniRoute config found for task_type '{task_type}'. Using 'reasoning' fallback.")
            route = config.omniroute_endpoints.get("reasoning")
            if not route:
                logger.error("No valid routing configuration available.")
                return None
                
        api_key = config_manager.get_api_key(route.api_key_env)
        if not api_key:
            logger.error(f"Missing API key for {route.provider}. Check your {route.api_key_env} environment variable.")
            return None
            
        payload = {
            "model": route.model,
            "messages": [msg.to_dict() for msg in messages],
            "max_tokens": 1024
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        req = urllib.request.Request(
            url=self.endpoint_url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST"
        )
        
        logger.debug(f"Sending prompt to OmniRoute -> {route.provider}/{route.model} (task: {task_type})")
        
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                result = json.loads(response.read().decode("utf-8"))
                
                # Assuming an OpenAI-compatible response format
                if "choices" in result and len(result["choices"]) > 0:
                    reply = result["choices"][0].get("message", {})
                    content = reply.get("content", "")
                    return Message(role=Role.ASSISTANT, content=content)
                else:
                    logger.error(f"Unexpected API response format: {result}")
                    return None
                    
        except urllib.error.HTTPError as e:
            logger.error(f"HTTP Error {e.code} from OmniRoute: {e.read().decode('utf-8')}")
            return None
        except urllib.error.URLError as e:
            logger.error(f"Network Error connecting to OmniRoute: {e.reason}")
            return None
        except TimeoutError:
            logger.error(f"Timeout Error: Model request exceeded {self.timeout}s.")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in OmniRoute Gateway: {e}")
            return None
