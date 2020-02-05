import grpc
import sys

# import the generated classes
import addnumbers_pb2
import addnumbers_pb2_grpc

if len(sys.argv) < 4:
    sys.exit(1)

# open a gRPC channel
channel = grpc.insecure_channel('{}:50051'.format(sys.argv[1]))

# create a stub (client)
stub = addnumbers_pb2_grpc.AddNumbersStub(channel)

# create a valid request message
number = addnumbers_pb2.AddIn(x=int(sys.argv[2]), y=int(sys.argv[3]))

# make the call
response = stub.add(number)
print(response.value)
