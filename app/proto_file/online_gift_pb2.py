# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: online_gift.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='online_gift.proto',
  package='',
  serialized_pb='\n\x11online_gift.proto\x1a\x0c\x63ommon.proto\" \n\rGetOnlineGift\x12\x0f\n\x07gift_id\x18\x01 \x02(\x05\"M\n\x15GetOnlineGiftResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\"n\n\x16GetOnlineLevelGiftData\x12\x13\n\x0bonline_time\x18\x01 \x01(\x05\x12\x1f\n\x17received_online_gift_id\x18\x02 \x03(\x05\x12\x1e\n\x16received_level_gift_id\x18\x03 \x03(\x05\"K\n\x13GetActivityResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse')




_GETONLINEGIFT = _descriptor.Descriptor(
  name='GetOnlineGift',
  full_name='GetOnlineGift',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='GetOnlineGift.gift_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=35,
  serialized_end=67,
)


_GETONLINEGIFTRESPONSE = _descriptor.Descriptor(
  name='GetOnlineGiftResponse',
  full_name='GetOnlineGiftResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GetOnlineGiftResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='GetOnlineGiftResponse.gain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=69,
  serialized_end=146,
)


_GETONLINELEVELGIFTDATA = _descriptor.Descriptor(
  name='GetOnlineLevelGiftData',
  full_name='GetOnlineLevelGiftData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='online_time', full_name='GetOnlineLevelGiftData.online_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='received_online_gift_id', full_name='GetOnlineLevelGiftData.received_online_gift_id', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='received_level_gift_id', full_name='GetOnlineLevelGiftData.received_level_gift_id', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=148,
  serialized_end=258,
)


_GETACTIVITYRESPONSE = _descriptor.Descriptor(
  name='GetActivityResponse',
  full_name='GetActivityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GetActivityResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='GetActivityResponse.gain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=260,
  serialized_end=335,
)

_GETONLINEGIFTRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_GETACTIVITYRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['GetOnlineGift'] = _GETONLINEGIFT
DESCRIPTOR.message_types_by_name['GetOnlineGiftResponse'] = _GETONLINEGIFTRESPONSE
DESCRIPTOR.message_types_by_name['GetOnlineLevelGiftData'] = _GETONLINELEVELGIFTDATA
DESCRIPTOR.message_types_by_name['GetActivityResponse'] = _GETACTIVITYRESPONSE

class GetOnlineGift(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETONLINEGIFT

  # @@protoc_insertion_point(class_scope:GetOnlineGift)

class GetOnlineGiftResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETONLINEGIFTRESPONSE

  # @@protoc_insertion_point(class_scope:GetOnlineGiftResponse)

class GetOnlineLevelGiftData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETONLINELEVELGIFTDATA

  # @@protoc_insertion_point(class_scope:GetOnlineLevelGiftData)

class GetActivityResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETACTIVITYRESPONSE

  # @@protoc_insertion_point(class_scope:GetActivityResponse)


# @@protoc_insertion_point(module_scope)
