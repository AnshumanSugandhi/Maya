from enum import Enum
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

@dataclass
class Message:
    role: Role
    content: str
    name: str = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts the message to a dictionary suitable for JSON serialization."""
        d = {"role": self.role.value, "content": self.content}
        if self.name is not None:
            d["name"] = self.name
        return d
