import os
import re
import sys
from pathlib import Path
from maya.core.agent import MayaAgent
from maya.core.logger import logger

# ANSI Colors
C_RESET = "\033[0m"
C_BLUE = "\033[94m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_CYAN = "\033[96m"
C_RED = "\033[91m"
C_GRAY = "\033[90m"

def print_welcome():
    print(f"{C_CYAN}===================================================={C_RESET}")
    print(f"{C_CYAN}  MAYA OS - Terminal Agent {C_RESET}")
    print(f"{C_GRAY}  Type '@filename' to include file context.{C_RESET}")
    print(f"{C_GRAY}  Type 'exit' or press Ctrl+C to quit.{C_RESET}")
    print(f"{C_CYAN}===================================================={C_RESET}\n")

def extract_mentions(user_input: str) -> tuple[str, str]:
    """
    Parses @filename mentions, reads the files, and returns (clean_input, injected_context).
    """
    # Regex to find @path/to/file.ext or @file.txt
    # Matches @ followed by word characters, dots, slashes, dashes.
    matches = re.findall(r'@([\w\.\/\-\\]+)', user_input)
    
    if not matches:
        return user_input, ""
        
    context = "\n\n[USER PROVIDED FILE CONTEXT]\n"
    files_added = 0
    
    for match in matches:
        # Check if the file exists
        filepath = Path(match)
        if filepath.is_file():
            try:
                content = filepath.read_text(encoding="utf-8")
                context += f"\n--- File: {match} ---\n{content}\n--- End File ---\n"
                print(f"{C_YELLOW}Attached context: {match}{C_RESET}")
                files_added += 1
            except Exception as e:
                print(f"{C_RED}Failed to read {match}: {e}{C_RESET}")
        else:
            print(f"{C_RED}Warning: File '{match}' not found.{C_RESET}")
            
    if files_added == 0:
        return user_input, ""
        
    # Strip the @mentions from the visual text sent to the agent so it just sees the context block cleanly
    # (Optional: we can leave them in so the agent knows exactly where they were referenced)
    return user_input, context

def start_cli(agent: MayaAgent):
    print_welcome()
    
    while True:
        try:
            # Print prompt
            user_input = input(f"\n{C_GREEN}maya> {C_RESET}").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit"]:
                print(f"{C_CYAN}Goodbye!{C_RESET}")
                break
                
            # Parse @ mentions
            clean_input, context_injection = extract_mentions(user_input)
            
            # Combine input and context
            final_prompt = clean_input + context_injection
            
            # Run Agent
            print(f"{C_GRAY}Thinking...{C_RESET}")
            response = agent.run(final_prompt)
            
            # Print response
            print(f"\n{C_BLUE}MAYA:{C_RESET}\n{response}\n")
            
        except KeyboardInterrupt:
            print(f"\n{C_CYAN}Goodbye!{C_RESET}")
            sys.exit(0)
        except Exception as e:
            logger.error(f"CLI Error: {e}")
            print(f"{C_RED}An error occurred: {e}{C_RESET}")
