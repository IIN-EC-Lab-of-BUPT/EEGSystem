# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import componentframework.test_service.test_grpc.ConfigManager_pb2 as ConfigManager__pb2

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
        + f' but the generated code in ConfigManager_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ConfigManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadGlobalConfig = channel.unary_unary(
                '/ConfigManagerService/ReadGlobalConfig',
                request_serializer=ConfigManager__pb2.ReadGlobalConfigRequest.SerializeToString,
                response_deserializer=ConfigManager__pb2.ReadGlobalConfigResponse.FromString,
                _registered_method=True)
        self.RegisterGlobalConfigUpdateCallback = channel.unary_stream(
                '/ConfigManagerService/RegisterGlobalConfigUpdateCallback',
                request_serializer=ConfigManager__pb2.RegisterGlobalConfigUpdateCallbackRequest.SerializeToString,
                response_deserializer=ConfigManager__pb2.RegisterGlobalConfigUpdateCallbackResponse.FromString,
                _registered_method=True)
        self.UpdateGlobalConfig = channel.unary_unary(
                '/ConfigManagerService/UpdateGlobalConfig',
                request_serializer=ConfigManager__pb2.UpdateGlobalConfigRequest.SerializeToString,
                response_deserializer=ConfigManager__pb2.UpdateGlobalConfigResponse.FromString,
                _registered_method=True)


class ConfigManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReadGlobalConfig(self, request, context):
        """2.2.1.	全局配置读取
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterGlobalConfigUpdateCallback(self, request, context):
        """2.2.2.	全局参数配置更新回调注册
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateGlobalConfig(self, request, context):
        """2.2.3.	手动更新全局配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConfigManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadGlobalConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadGlobalConfig,
                    request_deserializer=ConfigManager__pb2.ReadGlobalConfigRequest.FromString,
                    response_serializer=ConfigManager__pb2.ReadGlobalConfigResponse.SerializeToString,
            ),
            'RegisterGlobalConfigUpdateCallback': grpc.unary_stream_rpc_method_handler(
                    servicer.RegisterGlobalConfigUpdateCallback,
                    request_deserializer=ConfigManager__pb2.RegisterGlobalConfigUpdateCallbackRequest.FromString,
                    response_serializer=ConfigManager__pb2.RegisterGlobalConfigUpdateCallbackResponse.SerializeToString,
            ),
            'UpdateGlobalConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateGlobalConfig,
                    request_deserializer=ConfigManager__pb2.UpdateGlobalConfigRequest.FromString,
                    response_serializer=ConfigManager__pb2.UpdateGlobalConfigResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ConfigManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ConfigManagerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ConfigManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReadGlobalConfig(request,
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
            '/ConfigManagerService/ReadGlobalConfig',
            ConfigManager__pb2.ReadGlobalConfigRequest.SerializeToString,
            ConfigManager__pb2.ReadGlobalConfigResponse.FromString,
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
    def RegisterGlobalConfigUpdateCallback(request,
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
            '/ConfigManagerService/RegisterGlobalConfigUpdateCallback',
            ConfigManager__pb2.RegisterGlobalConfigUpdateCallbackRequest.SerializeToString,
            ConfigManager__pb2.RegisterGlobalConfigUpdateCallbackResponse.FromString,
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
    def UpdateGlobalConfig(request,
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
            '/ConfigManagerService/UpdateGlobalConfig',
            ConfigManager__pb2.UpdateGlobalConfigRequest.SerializeToString,
            ConfigManager__pb2.UpdateGlobalConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
