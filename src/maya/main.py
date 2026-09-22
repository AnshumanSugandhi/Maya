import sys
from pathlib import Path

# Ensure the src directory is in the path
src_path = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(src_path))

from maya.core.config import config
from maya.core.logger import logger
from maya.brain.omniroute import OmniRouteGateway
from maya.tools.registry import ToolRegistry
from maya.tools.system_tools import GetTimeTool
from maya.tools.fs_tools import ReadFileTool, WriteFileTool, ListDirectoryTool
from maya.tools.shell_tools import RunCommandTool
from maya.core.agent import MayaAgent
from maya.dashboard.server import start_server

def main():
    logger.info("Initializing MAYA OS...")
    logger.info(f"Environment: {config.env}")
    
    print("\n==================================")
    print("      MAYA OS Initialized         ")
    print("==================================\n")
    
    # Setup Brain & Tools
    gateway = OmniRouteGateway()
    registry = ToolRegistry()
    registry.register(GetTimeTool())
    registry.register(ReadFileTool())
    registry.register(WriteFileTool())
    registry.register(ListDirectoryTool())
    registry.register(RunCommandTool())
    
    # Initialize Agent
    agent = MayaAgent(gateway=gateway, registry=registry)
    
    # Start the local UI Server instead of terminal loop
    start_server(agent)
    
if __name__ == "__main__":
    main()
