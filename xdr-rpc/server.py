# xdr-rpc/server.py
import socket
import xdrlib

def reverse_string(s: str) -> str:
    return s[::-1]

def handle_client(conn):
    data = conn.recv(4096)
    if not data:
        return

    unpacker = xdrlib.Unpacker(data)
    # XDR string: length (4 bytes) + string bytes + padding to 4-byte boundary
    input_str = unpacker.unpack_string().decode('utf-8')
    unpacker.done()

    print(f"Server received: '{input_str}'")
    result = reverse_string(input_str)

    packer = xdrlib.Packer()
    packer.pack_string(result.encode('utf-8'))
    response = packer.get_buffer()

    conn.sendall(response)
    conn.close()

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", 9001))
    server.listen(5)
    print("XDR-RPC simulation server listening on port 9001...")

    try:
        while True:
            conn, addr = server.accept()
            print(f"Connection from {addr}")
            handle_client(conn)
    except KeyboardInterrupt:
        print("\nXDR-RPC Server stopped.")
        server.close()