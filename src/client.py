#!/usr/bin/env python3
from __future__ import print_function

import logging
import random


import grpc
import memory_check_pb2
import memory_check_pb2_grpc
import numpy as np
import time


def make_route_note(message):
    return memory_check_pb2.Payload(
        message= message)
def generate_messages():
    #while(True):
    for _ in range(100):
            msg = make_route_note("Msg# "+str(_))
            print("Sending %d", _)
            yield msg


def guide_route_chat(stub):
    msg = ""
    for _ in np.arange(70*100*100).tolist():
        msg+=str(_)
    total_lag = 0
    for _ in range(100):
        start_time = int(time.time_ns())
        #time.sleep(1)
        response = stub.MemoryChat(make_route_note(msg))
        print(
                "Received message %d" % (_)
            )
        end_time = int(time.time_ns())
        #print("Lag is: %d", (end_time - start_time)/1000000)
        total_lag+=(end_time - start_time)/1000000

    print("Total lag across 100 request to the remote server is: %dms" %(total_lag/100))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("192.168.122.1:50051") as channel:
        stub = memory_check_pb2_grpc.MemoryCheckStub(channel)
        guide_route_chat(stub)


if __name__ == "__main__":
    logging.basicConfig()
    run()
