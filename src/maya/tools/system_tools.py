import datetime
from maya.tools.registry import Tool

class GetTimeTool(Tool):
    """A simple tool that returns the current system time."""
    
    @property
    def name(self) -> str:
        return "get_current_time"
        
    @property
    def description(self) -> str:
        return "Returns the current local system time. Takes no arguments."
        
    def execute(self, **kwargs) -> str:
        now = datetime.datetime.now()
        return f"The current system time is {now.strftime('%Y-%m-%d %H:%M:%S')}."
