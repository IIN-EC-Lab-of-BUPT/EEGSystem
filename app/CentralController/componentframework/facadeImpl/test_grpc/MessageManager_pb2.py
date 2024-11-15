# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageManager.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14MessageManager.proto\x12/com.coreplantform.daemonproceed.controller.grpc\"d\n\x12\x42indMessageRequest\x12\x11\n\tserviceID\x18\x01 \x01(\t\x12\x12\n\nmessageKey\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\x12\x18\n\x10\x63omponentPattern\x18\x04 \x01(\t\"K\n\x13\x42indMessageResponse\x12\x11\n\tserviceID\x18\x01 \x01(\t\x12\x12\n\nmessageKey\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\"2\n\x1f\x41\x64\x64ListenerOnBindMessageRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\"X\n AddListenerOnBindMessageResponse\x12\x11\n\tserviceID\x18\x01 \x01(\t\x12\x12\n\nmessageKey\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\"Q\n\x19\x43onfirmBindMessageRequest\x12\x11\n\tserviceID\x18\x01 \x01(\t\x12\x12\n\nmessageKey\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\".\n\x1a\x43onfirmBindMessageResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"D\n\x1bGetTopicByMessageKeyRequest\x12\x12\n\nmessageKey\x18\x01 \x01(\t\x12\x11\n\tserviceID\x18\x02 \x01(\t\"-\n\x1cGetTopicByMessageKeyResponse\x12\r\n\x05topic\x18\x01 \x01(\t\"+\n\x15SubscribeTopicRequest\x12\x12\n\nmessageKey\x18\x01 \x01(\t\"*\n\x16SubscribeTopicResponse\x12\x10\n\x08response\x18\x01 \x01(\x0c\"7\n\x12SendMessageRequest\x12\x12\n\nmessageKey\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\'\n\x13SendMessageResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"6\n\x11SendResultRequest\x12\x12\n\nmessageKey\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"&\n\x12SendResultResponse\x12\x10\n\x08response\x18\x01 \x01(\t\">\n\x17UnsubscribeTopicRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\x12\x12\n\nmessageKey\x18\x02 \x01(\t\",\n\x18UnsubscribeTopicResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"8\n%CancelAddListenerOnBindMessageRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\":\n&CancelAddListenerOnBindMessageResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\xb5\x0c\n\x15MessageManagerService\x12\x98\x01\n\x0b\x42indMessage\x12\x43.com.coreplantform.daemonproceed.controller.grpc.BindMessageRequest\x1a\x44.com.coreplantform.daemonproceed.controller.grpc.BindMessageResponse\x12\xc1\x01\n\x18\x41\x64\x64ListenerOnBindMessage\x12P.com.coreplantform.daemonproceed.controller.grpc.AddListenerOnBindMessageRequest\x1aQ.com.coreplantform.daemonproceed.controller.grpc.AddListenerOnBindMessageResponse0\x01\x12\xad\x01\n\x12\x43onfirmBindMessage\x12J.com.coreplantform.daemonproceed.controller.grpc.ConfirmBindMessageRequest\x1aK.com.coreplantform.daemonproceed.controller.grpc.ConfirmBindMessageResponse\x12\xb3\x01\n\x14GetTopicByMessageKey\x12L.com.coreplantform.daemonproceed.controller.grpc.GetTopicByMessageKeyRequest\x1aM.com.coreplantform.daemonproceed.controller.grpc.GetTopicByMessageKeyResponse\x12\xa3\x01\n\x0eSubscribeTopic\x12\x46.com.coreplantform.daemonproceed.controller.grpc.SubscribeTopicRequest\x1aG.com.coreplantform.daemonproceed.controller.grpc.SubscribeTopicResponse0\x01\x12\x9a\x01\n\x0bSendMessage\x12\x43.com.coreplantform.daemonproceed.controller.grpc.SendMessageRequest\x1a\x44.com.coreplantform.daemonproceed.controller.grpc.SendMessageResponse(\x01\x12\x95\x01\n\nSendResult\x12\x42.com.coreplantform.daemonproceed.controller.grpc.SendResultRequest\x1a\x43.com.coreplantform.daemonproceed.controller.grpc.SendResultResponse\x12\xa7\x01\n\x10UnsubscribeTopic\x12H.com.coreplantform.daemonproceed.controller.grpc.UnsubscribeTopicRequest\x1aI.com.coreplantform.daemonproceed.controller.grpc.UnsubscribeTopicResponse\x12\xd1\x01\n\x1e\x43\x61ncelAddListenerOnBindMessage\x12V.com.coreplantform.daemonproceed.controller.grpc.CancelAddListenerOnBindMessageRequest\x1aW.com.coreplantform.daemonproceed.controller.grpc.CancelAddListenerOnBindMessageResponseBH\n/com.coreplantform.daemonproceed.controller.grpcB\x13MessageManagerProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MessageManager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n/com.coreplantform.daemonproceed.controller.grpcB\023MessageManagerProtoP\001'
  _globals['_BINDMESSAGEREQUEST']._serialized_start=73
  _globals['_BINDMESSAGEREQUEST']._serialized_end=173
  _globals['_BINDMESSAGERESPONSE']._serialized_start=175
  _globals['_BINDMESSAGERESPONSE']._serialized_end=250
  _globals['_ADDLISTENERONBINDMESSAGEREQUEST']._serialized_start=252
  _globals['_ADDLISTENERONBINDMESSAGEREQUEST']._serialized_end=302
  _globals['_ADDLISTENERONBINDMESSAGERESPONSE']._serialized_start=304
  _globals['_ADDLISTENERONBINDMESSAGERESPONSE']._serialized_end=392
  _globals['_CONFIRMBINDMESSAGEREQUEST']._serialized_start=394
  _globals['_CONFIRMBINDMESSAGEREQUEST']._serialized_end=475
  _globals['_CONFIRMBINDMESSAGERESPONSE']._serialized_start=477
  _globals['_CONFIRMBINDMESSAGERESPONSE']._serialized_end=523
  _globals['_GETTOPICBYMESSAGEKEYREQUEST']._serialized_start=525
  _globals['_GETTOPICBYMESSAGEKEYREQUEST']._serialized_end=593
  _globals['_GETTOPICBYMESSAGEKEYRESPONSE']._serialized_start=595
  _globals['_GETTOPICBYMESSAGEKEYRESPONSE']._serialized_end=640
  _globals['_SUBSCRIBETOPICREQUEST']._serialized_start=642
  _globals['_SUBSCRIBETOPICREQUEST']._serialized_end=685
  _globals['_SUBSCRIBETOPICRESPONSE']._serialized_start=687
  _globals['_SUBSCRIBETOPICRESPONSE']._serialized_end=729
  _globals['_SENDMESSAGEREQUEST']._serialized_start=731
  _globals['_SENDMESSAGEREQUEST']._serialized_end=786
  _globals['_SENDMESSAGERESPONSE']._serialized_start=788
  _globals['_SENDMESSAGERESPONSE']._serialized_end=827
  _globals['_SENDRESULTREQUEST']._serialized_start=829
  _globals['_SENDRESULTREQUEST']._serialized_end=883
  _globals['_SENDRESULTRESPONSE']._serialized_start=885
  _globals['_SENDRESULTRESPONSE']._serialized_end=923
  _globals['_UNSUBSCRIBETOPICREQUEST']._serialized_start=925
  _globals['_UNSUBSCRIBETOPICREQUEST']._serialized_end=987
  _globals['_UNSUBSCRIBETOPICRESPONSE']._serialized_start=989
  _globals['_UNSUBSCRIBETOPICRESPONSE']._serialized_end=1033
  _globals['_CANCELADDLISTENERONBINDMESSAGEREQUEST']._serialized_start=1035
  _globals['_CANCELADDLISTENERONBINDMESSAGEREQUEST']._serialized_end=1091
  _globals['_CANCELADDLISTENERONBINDMESSAGERESPONSE']._serialized_start=1093
  _globals['_CANCELADDLISTENERONBINDMESSAGERESPONSE']._serialized_end=1151
  _globals['_MESSAGEMANAGERSERVICE']._serialized_start=1154
  _globals['_MESSAGEMANAGERSERVICE']._serialized_end=2743
# @@protoc_insertion_point(module_scope)