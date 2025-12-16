# grpc/client.py
import grpc
import length_pb2
import length_pb2_grpc

def remote_length(text: str) -> int:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = length_pb2_grpc.LengthServiceStub(channel)
        response = stub.GetLength(length_pb2.LengthRequest(value=text))
        return response.length

# Tests
if __name__ == "__main__":
    print(remote_length("hello"))        # → 5
    print(remote_length("Python gRPC"))  # → 11
    print(remote_length(""))            # → 0
    print(remote_length("été 2025"))     # → 8 (UTF-8 correct)