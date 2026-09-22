import os
from pathlib import Path
from maya.tools.registry import Tool

class ReadFileTool(Tool):
    """Tool to read the contents of a file."""
    
    @property
    def name(self) -> str:
        return "read_file"
        
    @property
    def description(self) -> str:
        return "Reads the contents of a file. Arguments: {'path': 'absolute or relative path to file'}."
        
    def execute(self, **kwargs) -> str:
        path = kwargs.get("path")
        if not path:
            return "Error: Missing 'path' argument."
            
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            return f"--- FILE CONTENT: {path} ---\n{content}\n--- EOF ---"
        except Exception as e:
            return f"Failed to read file '{path}': {e}"

class WriteFileTool(Tool):
    """Tool to write or overwrite a file."""
    
    @property
    def name(self) -> str:
        return "write_file"
        
    @property
    def description(self) -> str:
        return "Creates or overwrites a file. Arguments: {'path': 'path to file', 'content': 'exact string content to write'}."
        
    def execute(self, **kwargs) -> str:
        path = kwargs.get("path")
        content = kwargs.get("content")
        
        if not path or content is None:
            return "Error: Missing 'path' or 'content' argument."
            
        try:
            # Create parent directories if they don't exist
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"Successfully wrote to file '{path}'."
        except Exception as e:
            return f"Failed to write file '{path}': {e}"

class ListDirectoryTool(Tool):
    """Tool to list files in a directory."""
    
    @property
    def name(self) -> str:
        return "list_directory"
        
    @property
    def description(self) -> str:
        return "Lists the contents of a directory. Arguments: {'path': 'path to directory'}."
        
    def execute(self, **kwargs) -> str:
        path = kwargs.get("path", ".")
            
        try:
            items = os.listdir(path)
            if not items:
                return f"Directory '{path}' is empty."
                
            formatted_items = []
            for item in items:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    formatted_items.append(f"[DIR]  {item}")
                else:
                    formatted_items.append(f"[FILE] {item}")
                    
            return f"--- DIRECTORY: {path} ---\n" + "\n".join(formatted_items)
        except Exception as e:
            return f"Failed to list directory '{path}': {e}"
