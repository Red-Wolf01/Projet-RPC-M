# grpc/server.py
import grpc
from concurrent import futures
import length_pb2
import length_pb2_grpc

class LengthServiceServicer(length_pb2_grpc.LengthServiceServicer):
    def GetLength(self, request, context):
        result = len(request.value)
        print(f"gRPC Server: len('{request.value}') = {result}")
        return length_pb2.LengthResponse(length=result)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    length_pb2_grpc.add_LengthServiceServicer_to_server(LengthServiceServicer(), server)
    server.add_insecure_port('localhost:50051')
    print("gRPC server running on localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()