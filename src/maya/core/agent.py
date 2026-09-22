import json
from typing import List
from maya.brain.gateway import ModelGateway
from maya.tools.registry import ToolRegistry
from maya.core.planner import Planner
from maya.brain.messages import Message, Role
from maya.core.logger import logger

class MayaAgent:
    """The core agent runtime that orchestrates the understand->plan->execute loop."""
    
    def __init__(self, gateway: ModelGateway, registry: ToolRegistry):
        self.registry = registry
        self.planner = Planner(gateway, registry)
        self.conversation: List[Message] = []
        
    def run(self, user_input: str, max_steps: int = 5) -> str:
        """Runs the agent loop for a given user input."""
        logger.info(f"User: {user_input}")
        self.conversation.append(Message(role=Role.USER, content=user_input))
        
        step = 0
        while step < max_steps:
            step += 1
            logger.debug(f"Agent Loop Step {step}")
            
            # PLAN
            response_msg = self.planner.plan_next_step(self.conversation)
            self.conversation.append(response_msg)
            
            content = response_msg.content.strip()
            
            # CHECK IF TOOL CALL
            import re
            json_match = re.search(r'(\{.*\})', content, re.DOTALL)
            
            if json_match:
                try:
                    call_data = json.loads(json_match.group(1))
                    if "tool" in call_data:
                        tool_name = call_data["tool"]
                        args = call_data.get("arguments", {})
                        
                        logger.info(f"Executing Tool: {tool_name} with args {args}")
                        
                        # EXECUTE
                        result = self.registry.execute_tool(tool_name, **args)
                        
                        # OBSERVE (Add result back to conversation)
                        self.conversation.append(Message(
                            role=Role.TOOL, 
                            content=result,
                            name=tool_name
                        ))
                        continue # Re-plan with the new information
                except json.JSONDecodeError:
                    # Not a valid JSON tool call, treat as regular text
                    pass
            
            # If we reached here, it's a regular text response (or the loop finished)
            logger.info(f"MAYA: {content}")
            return content
            
        logger.warning("Agent reached maximum steps without a final text response.")
        return "I had to stop thinking because I reached my step limit."
