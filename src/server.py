#!/usr/bin/env python3

from concurrent import futures
import logging
import math
import time

import grpc
import memory_check_pb2_grpc
import memory_check_pb2



class MemoryCheckServicer(memory_check_pb2_grpc.MemoryCheckServicer):
    #def __init__(self):
    #    self.prev_notes = []
    def MemoryChat(self, request, context):
        print(len(request.message))
        return request
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    memory_check_pb2_grpc.add_MemoryCheckServicer_to_server(
        MemoryCheckServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
