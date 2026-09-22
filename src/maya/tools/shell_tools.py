import subprocess
from maya.tools.registry import Tool

class RunCommandTool(Tool):
    """Tool to execute a shell command in the terminal."""
    
    @property
    def name(self) -> str:
        return "run_command"
        
    @property
    def description(self) -> str:
        return "Executes a shell command. Arguments: {'command': 'the command to run'}. Note: Has a 30s timeout."
        
    def execute(self, **kwargs) -> str:
        command = kwargs.get("command")
        if not command:
            return "Error: Missing 'command' argument."
            
        try:
            # Run the command with a timeout to prevent the agent from hanging the system
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            
            output = ""
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}\n"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}\n"
                
            if not output:
                output = "Command executed successfully with no output."
                
            return f"Exit Code: {result.returncode}\n{output}"
            
        except subprocess.TimeoutExpired:
            return f"Error: Command '{command}' timed out after 30 seconds."
        except Exception as e:
            return f"Failed to run command '{command}': {e}"
