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
from maya.cli.app import start_cli

def main():
    logger.info("Initializing MAYA OS CLI...")
    logger.info(f"Environment: {config.env}")
    
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
    
    # Start the interactive Terminal CLI
    start_cli(agent)
    
if __name__ == "__main__":
    main()
