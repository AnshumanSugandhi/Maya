from abc import ABC, abstractmethod
from typing import Dict, Any, List

class Tool(ABC):
    """Abstract base class for all MAYA tools."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """The name of the tool (used by the model to call it)."""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """A detailed description of what the tool does and its parameters."""
        pass
        
    @abstractmethod
    def execute(self, **kwargs) -> str:
        """Execute the tool with the provided arguments and return a string result."""
        pass

class ToolRegistry:
    """Manages available tools and provides formatting for the model."""
    
    def __init__(self):
        self._tools: Dict[str, Tool] = {}
        
    def register(self, tool: Tool):
        """Register a new tool."""
        self._tools[tool.name] = tool
        
    def get_tool(self, name: str) -> Tool:
        """Retrieve a tool by name."""
        return self._tools.get(name)
        
    def execute_tool(self, name: str, **kwargs) -> str:
        """Execute a tool by name."""
        tool = self.get_tool(name)
        if not tool:
            return f"Error: Tool '{name}' not found."
        try:
            return str(tool.execute(**kwargs))
        except Exception as e:
            return f"Error executing '{name}': {str(e)}"
            
    def get_tool_descriptions(self) -> str:
        """Get a formatted string of all tools for the model prompt."""
        if not self._tools:
            return "No tools available."
            
        descriptions = []
        for name, tool in self._tools.items():
            descriptions.append(f"- {name}: {tool.description}")
            
        return "\n".join(descriptions)
