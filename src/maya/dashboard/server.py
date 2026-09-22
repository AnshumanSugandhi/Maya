import json
import http.server
import socketserver
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse, parse_qs
from maya.core.logger import logger
from maya.core.agent import MayaAgent

PORT = 8080

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    
    def __init__(self, agent: MayaAgent, *args, **kwargs):
        self.agent = agent
        
        # Define directory for static files
        self.static_dir = Path(__file__).resolve().parent / "static"
        
        super().__init__(*args, directory=str(self.static_dir), **kwargs)

    def do_POST(self):
        """Handle API requests from the frontend."""
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                user_input = data.get("message", "")
                
                if user_input:
                    # Track how many tools exist before the run
                    prev_tool_count = sum(1 for m in self.agent.conversation if m.role.value == "tool")
                    
                    # Run the agent loop
                    response = self.agent.run(user_input)
                    
                    # Find newly executed tools
                    new_tools = [m for m in self.agent.conversation if m.role.value == "tool"][prev_tool_count:]
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    
                    # Return the response and the newly executed tools
                    response_data = {
                        "response": response,
                        "new_tools": [
                            {"name": msg.name, "content": msg.content}
                            for msg in new_tools
                        ]
                    }
                    self.wfile.write(json.dumps(response_data).encode('utf-8'))
                else:
                    self.send_error(400, "Empty message provided.")
            except Exception as e:
                logger.error(f"Error in dashboard API: {e}")
                self.send_error(500, str(e))
        else:
            self.send_error(404, "Not Found")

def start_server(agent: MayaAgent):
    """Start the dashboard web server."""
    # Create a custom handler class with the agent injected
    handler = lambda *args, **kwargs: DashboardHandler(agent, *args, **kwargs)
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        logger.info(f"Dashboard server started at http://localhost:{PORT}")
        print(f"\n=============================================")
        print(f" MAYA Dashboard available at: http://localhost:{PORT}")
        print(f"=============================================\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("Dashboard server shutting down.")
            httpd.shutdown()
