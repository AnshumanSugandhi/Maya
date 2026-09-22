import json
import re
from typing import List
from maya.brain.gateway import ModelGateway
from maya.brain.messages import Message, Role
from maya.tools.registry import ToolRegistry
from maya.core.planner import Planner
from maya.core.logger import logger
from maya.memory.history import HistoryManager

class MayaAgent:
    """
    The core runtime loop for MAYA.
    """
    
    def __init__(self, gateway: ModelGateway, registry: ToolRegistry, max_context_messages: int = 30):
        self.gateway = gateway
        self.registry = registry
        self.planner = Planner(registry)
        self.history_manager = HistoryManager()
        self.max_context_messages = max_context_messages
        
        # Load long-term memory
        self.conversation: List[Message] = self.history_manager.load()
        
    def _get_context_window(self) -> List[Message]:
        """
        Truncates the conversation for short-term memory to prevent LLM context overflow.
        Always keeps the system prompt (first message) and the last N messages.
        """
        if len(self.conversation) <= self.max_context_messages:
            return self.conversation
            
        # Keep the first message (system prompt) if it exists and is a system message
        sys_prompt = []
        if self.conversation and self.conversation[0].role == Role.SYSTEM:
            sys_prompt = [self.conversation[0]]
            
        # Grab the last N messages
        recent_messages = self.conversation[-(self.max_context_messages - len(sys_prompt)):]
        
        return sys_prompt + recent_messages
        
    def run(self, user_input: str) -> str:
        """
        Executes a single turn of the agent loop based on user input.
        """
        logger.info(f"User: {user_input}")
        
        # 1. UNDERSTAND: Add user input to conversation
        self.conversation.append(Message(role=Role.USER, content=user_input))
        
        # We will loop until the agent decides to stop (i.e., when it just talks to the user without calling a tool)
        loop_count = 0
        max_loops = 5
        
        while loop_count < max_loops:
            loop_count += 1
            logger.debug(f"Agent Loop Step {loop_count}")
            
            # 2. PLAN: Let the planner potentially inject or update system prompts based on state
            # (Currently planner just builds the static system prompt with tool schemas)
            if not any(msg.role == Role.SYSTEM for msg in self.conversation):
                system_prompt = self.planner.build_system_prompt()
                self.conversation.insert(0, Message(role=Role.SYSTEM, content=system_prompt))
                
            # Grab the truncated context window so we don't overflow the LLM
            context_window = self._get_context_window()
                
            # 3. EXECUTE: Ask the LLM to think and respond
            logger.debug("Planner invoking model gateway...")
            response_msg = self.gateway.invoke(context_window)
            
            if not response_msg:
                logger.error("Planner received no response from the gateway.")
                return "I'm sorry, I couldn't reach my reasoning engine."
                
            # Add assistant's response to history
            self.conversation.append(response_msg)
            
            content = response_msg.content.strip()
            
            # CHECK IF TOOL CALL
            json_match = re.search(r'(\{.*\})', content, re.DOTALL)
            
            if json_match:
                try:
                    call_data = json.loads(json_match.group(1))
                    if "tool" in call_data:
                        tool_name = call_data["tool"]
                        args = call_data.get("arguments", {})
                        
                        logger.info(f"Executing Tool: {tool_name} with args {args}")
                        
                        # Execute the tool
                        result = self.registry.execute(tool_name, **args)
                        
                        # 4. OBSERVE: Feed the tool result back into the conversation as a TOOL role
                        self.conversation.append(Message(role=Role.TOOL, content=str(result), name=tool_name))
                        
                        # Loop continues so the agent can see the result and respond
                        continue
                except json.JSONDecodeError:
                    logger.warning("Agent attempted to output JSON but it was malformed.")
                    
            # 5. RESPOND: If no tool was called (or JSON parsing failed), the agent's content is meant for the user
            logger.info(f"MAYA: {content}")
            
            # Save long-term memory at the end of the turn
            self.history_manager.save(self.conversation)
            
            return content
            
        # Save memory even if we hit the loop limit
        self.history_manager.save(self.conversation)
        return "I had to stop thinking because I reached my maximum step limit."
