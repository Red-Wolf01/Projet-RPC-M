# xml-rpc/server.py
from xmlrpc.server import SimpleXMLRPCServer
import logging

# Optional: nice logs to see what happens
logging.basicConfig(level=logging.INFO)

def add(x: int, y: int) -> int:
    """Add two integers"""
    result = x + y
    print(f"Server: add({x}, {y}) = {result}")
    return result

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 9000), logRequests=True)
    print("XML-RPC Server running on http://localhost:9000")
    server.register_function(add, "add")
    server.register_introspection_functions()  # optional, nice for debugging
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nXML-RPC Server stopped.")