# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Algorithm/api/proto/AlgorithmRPCService.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Common.protobuf import BaseDataClassMessage_pb2 as Common_dot_protobuf_dot_BaseDataClassMessage__pb2
from Common.protobuf import CommonMessage_pb2 as Common_dot_protobuf_dot_CommonMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-Algorithm/api/proto/AlgorithmRPCService.proto\x12\x16\x41lgorithm.api.protobuf\x1a*Common/protobuf/BaseDataClassMessage.proto\x1a#Common/protobuf/CommonMessage.proto\"\xab\x03\n\x14\x41lgorithmDataMessage\x12\x13\n\x0bsourceLabel\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x02\x12\x37\n\rdevicePackage\x18\x03 \x01(\x0b\x32\x1e.Common.protobuf.DevicePackageH\x00\x12\x35\n\x0c\x65ventPackage\x18\x04 \x01(\x0b\x32\x1d.Common.protobuf.EventPackageH\x00\x12\x33\n\x0b\x64\x61taPackage\x18\x05 \x01(\x0b\x32\x1c.Common.protobuf.DataPackageH\x00\x12=\n\x10impedancePackage\x18\x06 \x01(\x0b\x32!.Common.protobuf.ImpedancePackageH\x00\x12\x41\n\x12informationPackage\x18\x07 \x01(\x0b\x32#.Common.protobuf.InformationPackageH\x00\x12\x39\n\x0e\x63ontrolPackage\x18\x08 \x01(\x0b\x32\x1f.Common.protobuf.ControlPackageH\x00\x42\t\n\x07package\"\xe9\x01\n\x16\x41lgorithmReportMessage\x12\x11\n\ttimestamp\x18\x01 \x01(\x02\x12\x37\n\rresultPackage\x18\x02 \x01(\x0b\x32\x1e.Common.protobuf.ResultPackageH\x00\x12\x39\n\x0e\x63ontrolPackage\x18\x03 \x01(\x0b\x32\x1f.Common.protobuf.ControlPackageH\x00\x12=\n\x10\x65xceptionPackage\x18\x04 \x01(\x0b\x32!.Common.protobuf.ExceptionPackageH\x00\x42\t\n\x07package\"U\n\x16\x41lgorithmStatusMessage\x12;\n\x06status\x18\x01 \x01(\x0e\x32+.Algorithm.api.protobuf.AlgorithmStatusEnum*s\n\x13\x41lgorithmStatusEnum\x12\x10\n\x0cINITIALIZING\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08STARTING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x32\x81\x02\n\x1a\x41lgorithmRPCServiceControl\x12K\n\nsendConfig\x12\x1e.Common.protobuf.StringMessage\x1a\x1d.Common.protobuf.EmptyMessage\x12J\n\tgetConfig\x12\x1d.Common.protobuf.EmptyMessage\x1a\x1e.Common.protobuf.StringMessage\x12J\n\x08shutdown\x12\x1d.Common.protobuf.EmptyMessage\x1a\x1f.Common.protobuf.BooleanMessage2\x86\x01\n\x17\x41lgorithmRPCDataConnect\x12k\n\x07\x63onnect\x12,.Algorithm.api.protobuf.AlgorithmDataMessage\x1a..Algorithm.api.protobuf.AlgorithmReportMessage(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Algorithm.api.proto.AlgorithmRPCService_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ALGORITHMSTATUSENUM']._serialized_start=907
  _globals['_ALGORITHMSTATUSENUM']._serialized_end=1022
  _globals['_ALGORITHMDATAMESSAGE']._serialized_start=155
  _globals['_ALGORITHMDATAMESSAGE']._serialized_end=582
  _globals['_ALGORITHMREPORTMESSAGE']._serialized_start=585
  _globals['_ALGORITHMREPORTMESSAGE']._serialized_end=818
  _globals['_ALGORITHMSTATUSMESSAGE']._serialized_start=820
  _globals['_ALGORITHMSTATUSMESSAGE']._serialized_end=905
  _globals['_ALGORITHMRPCSERVICECONTROL']._serialized_start=1025
  _globals['_ALGORITHMRPCSERVICECONTROL']._serialized_end=1282
  _globals['_ALGORITHMRPCDATACONNECT']._serialized_start=1285
  _globals['_ALGORITHMRPCDATACONNECT']._serialized_end=1419
# @@protoc_insertion_point(module_scope)
