# xdr-rpc/client.py
import socket
import xdrlib

def remote_reverse(text: str) -> str:
    packer = xdrlib.Packer()
    packer.pack_string(text.encode('utf-8'))
    request = packer.get_buffer()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 9001))
    s.sendall(request)

    unpacker = xdrlib.Unpacker(s.recv(4096))
    result = unpacker.unpack_string().decode('utf-8')
    unpacker.done()
    s.close()

    return result

# Tests
if __name__ == "__main__":
    print(remote_reverse("hello"))        # → olleh
    print(remote_reverse("Python"))       # → nohtyP
    print(remote_reverse("12345"))        # → 54321
    print(remote_reverse(""))             # → (empty string)