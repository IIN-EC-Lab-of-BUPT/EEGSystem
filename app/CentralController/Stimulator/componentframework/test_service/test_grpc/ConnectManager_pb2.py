# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ConnectManager.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x43onnectManager.proto\x12/com.coreplantform.daemonproceed.controller.grpc\"\"\n\x0fShutDownRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\"$\n\x10ShutDownResponse\x12\x10\n\x08response\x18\x01 \x01(\t\";\n(AddListenerOnRequestComponentStopRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\"=\n)AddListenerOnRequestComponentStopResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"5\n\"ConfirmRequestComponentStopRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\"7\n#ConfirmRequestComponentStopResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\xd3\x04\n\x15\x43onnectManagerService\x12\x8f\x01\n\x08ShutDown\x12@.com.coreplantform.daemonproceed.controller.grpc.ShutDownRequest\x1a\x41.com.coreplantform.daemonproceed.controller.grpc.ShutDownResponse\x12\xdc\x01\n!AddListenerOnRequestComponentStop\x12Y.com.coreplantform.daemonproceed.controller.grpc.AddListenerOnRequestComponentStopRequest\x1aZ.com.coreplantform.daemonproceed.controller.grpc.AddListenerOnRequestComponentStopResponse0\x01\x12\xc8\x01\n\x1b\x43onfirmRequestComponentStop\x12S.com.coreplantform.daemonproceed.controller.grpc.ConfirmRequestComponentStopRequest\x1aT.com.coreplantform.daemonproceed.controller.grpc.ConfirmRequestComponentStopResponseBH\n/com.coreplantform.daemonproceed.controller.grpcB\x13\x43onnectManagerProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ConnectManager_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n/com.coreplantform.daemonproceed.controller.grpcB\023ConnectManagerProtoP\001'
  _globals['_SHUTDOWNREQUEST']._serialized_start=73
  _globals['_SHUTDOWNREQUEST']._serialized_end=107
  _globals['_SHUTDOWNRESPONSE']._serialized_start=109
  _globals['_SHUTDOWNRESPONSE']._serialized_end=145
  _globals['_ADDLISTENERONREQUESTCOMPONENTSTOPREQUEST']._serialized_start=147
  _globals['_ADDLISTENERONREQUESTCOMPONENTSTOPREQUEST']._serialized_end=206
  _globals['_ADDLISTENERONREQUESTCOMPONENTSTOPRESPONSE']._serialized_start=208
  _globals['_ADDLISTENERONREQUESTCOMPONENTSTOPRESPONSE']._serialized_end=269
  _globals['_CONFIRMREQUESTCOMPONENTSTOPREQUEST']._serialized_start=271
  _globals['_CONFIRMREQUESTCOMPONENTSTOPREQUEST']._serialized_end=324
  _globals['_CONFIRMREQUESTCOMPONENTSTOPRESPONSE']._serialized_start=326
  _globals['_CONFIRMREQUESTCOMPONENTSTOPRESPONSE']._serialized_end=381
  _globals['_CONNECTMANAGERSERVICE']._serialized_start=384
  _globals['_CONNECTMANAGERSERVICE']._serialized_end=979
# @@protoc_insertion_point(module_scope)
