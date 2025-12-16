# json-rpc/server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class JSONRPCHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read request
        length = int(self.headers['Content-Length'])
        raw_data = self.rfile.read(length)
        request = json.loads(raw_data)

        # Debug print
        print(f"JSON-RPC request: {request}")

        # Handle only "min" method
        if request.get("method") == "min":
            params = request.get("params", [])
            if len(params) != 2:
                result = None
            else:
                result = min(params[0], params[1])
        else:
            result = None

        # JSON-RPC 2.0 response
        response = {
            "jsonrpc": "2.0",
            "result": result,
            "id": request.get("id")
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("localhost", 9001), JSONRPCHandler)
    print("JSON-RPC server running on http://localhost:9001")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nJSON-RPC server stopped.")