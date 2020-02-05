import grpc
from concurrent import futures
import time

import DigitClassifier_pb2
import DigitClassifier_pb2_grpc

import digit_classifier

class DigitClassifierServicer(DigitClassifier_pb2_grpc.DigitClassifierServicer):
    def Classify(self, request, context):
        response = DigitClassifier_pb2.Classification()
        response.value = digit_classifier.predict(request.width, request.height, request.bytes)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
DigitClassifier_pb2_grpc.add_DigitClassifierServicer_to_server(
        DigitClassifierServicer(), server)

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