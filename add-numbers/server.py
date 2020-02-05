import grpc
from concurrent import futures
import time

import addnumbers_pb2
import addnumbers_pb2_grpc

import add_numbers

class AddNumbersServicer(addnumbers_pb2_grpc.AddNumbersServicer):
    def add(self, request, context):
        response = addnumbers_pb2.AddOut()
        response.value = add_numbers.add_numbers(request.x, request.y)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
addnumbers_pb2_grpc.add_AddNumbersServicer_to_server(
        AddNumbersServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)