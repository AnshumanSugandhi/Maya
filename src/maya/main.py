import sys
from pathlib import Path

# Ensure the src directory is in the path
src_path = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(src_path))

from maya.core.config import config
from maya.core.logger import logger

def main():
    logger.info("Initializing MAYA OS...")
    logger.info(f"Environment: {config.env}")
    logger.info(f"Debug Mode: {config.debug}")
    logger.info(f"Loaded {len(config.omniroute_endpoints)} OmniRoute endpoints.")
    
    print("\n==================================")
    print("      MAYA OS Initialized         ")
    print("==================================\n")
    
if __name__ == "__main__":
    main()
