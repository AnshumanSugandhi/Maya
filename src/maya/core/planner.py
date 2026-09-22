from typing import List, Optional
import json
from maya.brain.gateway import ModelGateway
from maya.brain.messages import Message, Role
from maya.tools.registry import ToolRegistry
from maya.core.logger import logger

class Planner:
    """The Planner decides the next step based on the objective and available tools."""
    
    def __init__(self, gateway: ModelGateway, registry: ToolRegistry):
        self.gateway = gateway
        self.registry = registry
        
    def _build_system_prompt(self) -> str:
        """Builds the system prompt injecting tool definitions."""
        prompt = (
            "You are MAYA, a powerful desktop AI assistant.\n"
            "You have access to the following tools:\n\n"
            f"{self.registry.get_tool_descriptions()}\n\n"
            "To use a tool, respond ONLY with a JSON object in this format:\n"
            '{"tool": "tool_name", "arguments": {"arg1": "value"}}\n\n'
            "If you do not need to use a tool, just respond with your regular text reply."
        )
        return prompt
        
    def plan_next_step(self, conversation: List[Message]) -> Message:
        """Determines the next step by invoking the model."""
        # Prepend the system prompt dynamically
        sys_msg = Message(role=Role.SYSTEM, content=self._build_system_prompt())
        full_conversation = [sys_msg] + conversation
        
        logger.debug("Planner invoking model gateway...")
        response = self.gateway.invoke(full_conversation, task_type="reasoning")
        
        if not response:
            logger.error("Planner received no response from the gateway.")
            return Message(role=Role.ASSISTANT, content="I'm sorry, I couldn't reach my reasoning engine.")
            
        return response
