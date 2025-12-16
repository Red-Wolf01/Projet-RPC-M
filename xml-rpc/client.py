# xml-rpc/client.py
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9000")

# Test calls
print(proxy.add(5, 3))      # → 8
print(proxy.add(-10, 20))   # → 10
print(proxy.add(100, 200))  # → 300