# Project Components

## Folder Tree

```text
Projet-RPC-M/
├─ .venv/
├─ grpc/
│  ├─ client.py
│  ├─ length.proto
│  ├─ length_pb2.py
│  ├─ length_pb2_grpc.py
│  ├─ server.py
│  └─ __pycache__/
├─ json-rpc/
│  ├─ client.py
│  └─ server.py
├─ rest-json/
│  ├─ client.py
│  └─ server.py
├─ wireshark-captures/
├─ xdr-rpc/
│  ├─ client.py
│  └─ server.py
└─ xml-rpc/
  ├─ client.py
  └─ server.py
```

- **grpc/**
  - gRPC LengthService that returns the length of a string over port 50051; server implementation in [grpc/server.py](grpc/server.py#L1-L22) and client helper `remote_length` in [grpc/client.py](grpc/client.py#L1-L17).
  - Contract defined in [grpc/length.proto](grpc/length.proto#L1-L15); generated stubs in [grpc/length_pb2.py](grpc/length_pb2.py) and [grpc/length_pb2_grpc.py](grpc/length_pb2_grpc.py).

- **json-rpc/**
  - Minimal JSON-RPC 2.0 service over HTTP on port 9001 exposing a `min` method; handler in [json-rpc/server.py](json-rpc/server.py#L1-L40).
  - Client helper `remote_min` builds a JSON-RPC request and posts it to the server; see [json-rpc/client.py](json-rpc/client.py#L1-L19).

- **rest-json/**
  - Flask REST endpoint `/reverse` on port 9002 that reverses the posted string; implemented in [rest-json/server.py](rest-json/server.py#L1-L20).
  - Client helper `remote_reverse` posts JSON to the REST endpoint and returns the reversed string; see [rest-json/client.py](rest-json/client.py#L1-L15).

- **xdr-rpc/**
  - Socket-based demo using XDR serialization on port 9001; server accepts a UTF-8 string and returns its reverse; implemented in [xdr-rpc/server.py](xdr-rpc/server.py#L1-L38).
  - Client packs a string with XDR, sends it over TCP, and unpacks the reversed response; see [xdr-rpc/client.py](xdr-rpc/client.py#L1-L27).

- **xml-rpc/**
  - XML-RPC server exposing an `add` method on port 9000; implementation in [xml-rpc/server.py](xml-rpc/server.py#L1-L25).
  - Simple client invokes the remote `add` method; see [xml-rpc/client.py](xml-rpc/client.py#L1-L8).

- **wireshark-captures/**
  - Currently empty placeholder directory intended for storing packet captures or traces.
