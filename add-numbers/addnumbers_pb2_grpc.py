# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import addnumbers_pb2 as addnumbers__pb2


class AddNumbersStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.add = channel.unary_unary(
        '/AddNumbers/add',
        request_serializer=addnumbers__pb2.AddIn.SerializeToString,
        response_deserializer=addnumbers__pb2.AddOut.FromString,
        )


class AddNumbersServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def add(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AddNumbersServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'add': grpc.unary_unary_rpc_method_handler(
          servicer.add,
          request_deserializer=addnumbers__pb2.AddIn.FromString,
          response_serializer=addnumbers__pb2.AddOut.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'AddNumbers', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
