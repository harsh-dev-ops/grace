"""The Python implementation of the GRPC greetings.Greeter server."""

from concurrent import futures
import logging

import grpc
from rpc import greetings_pb2, greetings_pb2_grpc


class Greeter(greetings_pb2_grpc.GreeterServicer):
    def sayHello(self, request, context):
        return greetings_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greetings_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
