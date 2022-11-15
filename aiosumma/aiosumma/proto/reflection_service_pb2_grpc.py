# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import reflection_service_pb2 as reflection__service__pb2


class ReflectionApiStub(object):
    """API

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_top_terms = channel.unary_unary(
                '/summa.proto.ReflectionApi/get_top_terms',
                request_serializer=reflection__service__pb2.GetTopTermsRequest.SerializeToString,
                response_deserializer=reflection__service__pb2.GetTopTermsResponse.FromString,
                )


class ReflectionApiServicer(object):
    """API

    """

    def get_top_terms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReflectionApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_top_terms': grpc.unary_unary_rpc_method_handler(
                    servicer.get_top_terms,
                    request_deserializer=reflection__service__pb2.GetTopTermsRequest.FromString,
                    response_serializer=reflection__service__pb2.GetTopTermsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'summa.proto.ReflectionApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReflectionApi(object):
    """API

    """

    @staticmethod
    def get_top_terms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.ReflectionApi/get_top_terms',
            reflection__service__pb2.GetTopTermsRequest.SerializeToString,
            reflection__service__pb2.GetTopTermsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
