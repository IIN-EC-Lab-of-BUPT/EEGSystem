# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import componentframework.facadeImpl.test_grpc.ConnectManager_pb2 as ConnectManager__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in ConnectManager_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ConnectManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ShutDown = channel.unary_unary(
                '/com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService/ShutDown',
                request_serializer=ConnectManager__pb2.ShutDownRequest.SerializeToString,
                response_deserializer=ConnectManager__pb2.ShutDownResponse.FromString,
                _registered_method=True)
        self.AddListenerOnRequestComponentStop = channel.unary_stream(
                '/com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService/AddListenerOnRequestComponentStop',
                request_serializer=ConnectManager__pb2.AddListenerOnRequestComponentStopRequest.SerializeToString,
                response_deserializer=ConnectManager__pb2.AddListenerOnRequestComponentStopResponse.FromString,
                _registered_method=True)
        self.ConfirmRequestComponentStop = channel.unary_unary(
                '/com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService/ConfirmRequestComponentStop',
                request_serializer=ConnectManager__pb2.ConfirmRequestComponentStopRequest.SerializeToString,
                response_deserializer=ConnectManager__pb2.ConfirmRequestComponentStopResponse.FromString,
                _registered_method=True)
        self.CancelAddListenerOnRequestComponentStop = channel.unary_unary(
                '/com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService/CancelAddListenerOnRequestComponentStop',
                request_serializer=ConnectManager__pb2.CancelAddListenerOnRequestComponentStopRequest.SerializeToString,
                response_deserializer=ConnectManager__pb2.CancelAddListenerOnRequestComponentStopResponse.FromString,
                _registered_method=True)


class ConnectManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ShutDown(self, request, context):
        """2.4.2.2.关闭
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddListenerOnRequestComponentStop(self, request, context):
        """监听请求组件停止
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmRequestComponentStop(self, request, context):
        """确认请求组件停止
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelAddListenerOnRequestComponentStop(self, request, context):
        """取消监听请求组件停止
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ShutDown': grpc.unary_unary_rpc_method_handler(
                    servicer.ShutDown,
                    request_deserializer=ConnectManager__pb2.ShutDownRequest.FromString,
                    response_serializer=ConnectManager__pb2.ShutDownResponse.SerializeToString,
            ),
            'AddListenerOnRequestComponentStop': grpc.unary_stream_rpc_method_handler(
                    servicer.AddListenerOnRequestComponentStop,
                    request_deserializer=ConnectManager__pb2.AddListenerOnRequestComponentStopRequest.FromString,
                    response_serializer=ConnectManager__pb2.AddListenerOnRequestComponentStopResponse.SerializeToString,
            ),
            'ConfirmRequestComponentStop': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfirmRequestComponentStop,
                    request_deserializer=ConnectManager__pb2.ConfirmRequestComponentStopRequest.FromString,
                    response_serializer=ConnectManager__pb2.ConfirmRequestComponentStopResponse.SerializeToString,
            ),
            'CancelAddListenerOnRequestComponentStop': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelAddListenerOnRequestComponentStop,
                    request_deserializer=ConnectManager__pb2.CancelAddListenerOnRequestComponentStopRequest.FromString,
                    response_serializer=ConnectManager__pb2.CancelAddListenerOnRequestComponentStopResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ConnectManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ShutDown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService/ShutDown',
            ConnectManager__pb2.ShutDownRequest.SerializeToString,
            ConnectManager__pb2.ShutDownResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddListenerOnRequestComponentStop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService/AddListenerOnRequestComponentStop',
            ConnectManager__pb2.AddListenerOnRequestComponentStopRequest.SerializeToString,
            ConnectManager__pb2.AddListenerOnRequestComponentStopResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ConfirmRequestComponentStop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService/ConfirmRequestComponentStop',
            ConnectManager__pb2.ConfirmRequestComponentStopRequest.SerializeToString,
            ConnectManager__pb2.ConfirmRequestComponentStopResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CancelAddListenerOnRequestComponentStop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.coreplantform.daemonproceed.controller.grpc.ConnectManagerService/CancelAddListenerOnRequestComponentStop',
            ConnectManager__pb2.CancelAddListenerOnRequestComponentStopRequest.SerializeToString,
            ConnectManager__pb2.CancelAddListenerOnRequestComponentStopResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)