"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
from . import greetings_pb2
from . import greetings_pb2_grpc


def greet():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greetings_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greetings_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    greet()