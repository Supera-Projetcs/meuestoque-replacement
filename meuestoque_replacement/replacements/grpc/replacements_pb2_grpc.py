# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from meuestoque_replacement.replacements.grpc import replacements_pb2 as meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2


class ReplacementControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/config.replacements.ReplacementController/Create',
                request_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRequest.SerializeToString,
                response_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/config.replacements.ReplacementController/Destroy',
                request_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementDestroyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.List = channel.unary_unary(
                '/config.replacements.ReplacementController/List',
                request_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementListRequest.SerializeToString,
                response_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementListResponse.FromString,
                )
        self.PartialUpdate = channel.unary_unary(
                '/config.replacements.ReplacementController/PartialUpdate',
                request_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementPartialUpdateRequest.SerializeToString,
                response_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/config.replacements.ReplacementController/Retrieve',
                request_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRetrieveRequest.SerializeToString,
                response_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/config.replacements.ReplacementController/Update',
                request_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRequest.SerializeToString,
                response_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.FromString,
                )


class ReplacementControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PartialUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReplacementControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRequest.FromString,
                    response_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementDestroyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementListRequest.FromString,
                    response_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementListResponse.SerializeToString,
            ),
            'PartialUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.PartialUpdate,
                    request_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementPartialUpdateRequest.FromString,
                    response_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRetrieveRequest.FromString,
                    response_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRequest.FromString,
                    response_serializer=meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'config.replacements.ReplacementController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReplacementController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.replacements.ReplacementController/Create',
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRequest.SerializeToString,
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.replacements.ReplacementController/Destroy',
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementDestroyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.replacements.ReplacementController/List',
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementListRequest.SerializeToString,
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PartialUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.replacements.ReplacementController/PartialUpdate',
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementPartialUpdateRequest.SerializeToString,
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.replacements.ReplacementController/Retrieve',
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRetrieveRequest.SerializeToString,
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.replacements.ReplacementController/Update',
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementRequest.SerializeToString,
            meuestoque__replacement_dot_replacements_dot_grpc_dot_replacements__pb2.ReplacementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)