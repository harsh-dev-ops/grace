"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
from rpc import greetings_pb2, greetings_pb2_grpc


async def greet():
    print("Will try to greet world ...")
    with grpc.insecure_channel("grpc_server:50051") as channel:
        stub = greetings_pb2_grpc.GreeterStub(channel)
        response = stub.sayHello(greetings_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)
    return response


if __name__ == "__main__":
    logging.basicConfig()
    greet()