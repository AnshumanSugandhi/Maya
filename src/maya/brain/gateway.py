from abc import ABC, abstractmethod
from typing import List, Optional
from maya.brain.messages import Message

class ModelGateway(ABC):
    """Abstract interface for all model interactions."""
    
    @abstractmethod
    def invoke(self, messages: List[Message], task_type: str = "reasoning") -> Optional[Message]:
        """
        Send messages to a model and get a response.
        
        Args:
            messages: List of conversation messages
            task_type: A hint for routing (e.g., 'coding', 'reasoning', 'simple_task')
            
        Returns:
            The model's response Message, or None if it failed.
        """
        pass
