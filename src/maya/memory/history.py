import json
from pathlib import Path
from typing import List
from maya.brain.messages import Message, Role
from maya.core.logger import logger

class HistoryManager:
    """Manages long-term persistence of conversation history to disk."""
    
    def __init__(self, filepath: str = "data/history.json"):
        self.filepath = Path(filepath)
        # Ensure the data directory exists
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        
    def save(self, conversation: List[Message]):
        """Saves the conversation to disk in JSON format."""
        try:
            data = [msg.to_dict() for msg in conversation]
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            logger.debug(f"Saved {len(conversation)} messages to {self.filepath}")
        except Exception as e:
            logger.error(f"Failed to save history: {e}")
            
    def load(self) -> List[Message]:
        """Loads the conversation from disk if it exists."""
        if not self.filepath.exists():
            return []
            
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            conversation = []
            for item in data:
                role = Role(item["role"])
                msg = Message(role=role, content=item["content"], name=item.get("name"))
                conversation.append(msg)
                
            logger.info(f"Loaded {len(conversation)} messages from history.")
            return conversation
        except Exception as e:
            logger.error(f"Failed to load history: {e}")
            return []
