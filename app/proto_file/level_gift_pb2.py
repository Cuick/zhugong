# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: level_gift.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='level_gift.proto',
  package='',
  serialized_pb='\n\x10level_gift.proto\x1a\x0c\x63ommon.proto\"\x1f\n\x0cGetLevelGift\x12\x0f\n\x07gift_id\x18\x01 \x02(\x05\"L\n\x14GetLevelGiftResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\"X\n\x14NewLevelGiftResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\"\n\nlevel_info\x18\x02 \x03(\x0b\x32\x0e.LevelGiftInfo\"E\n\rLevelGiftInfo\x12\r\n\x05level\x18\x01 \x02(\x05\x12%\n\x05\x64rops\x18\x02 \x02(\x0b\x32\x16.GameResourcesResponse')




_GETLEVELGIFT = _descriptor.Descriptor(
  name='GetLevelGift',
  full_name='GetLevelGift',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='GetLevelGift.gift_id', index=0,
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
  serialized_start=34,
  serialized_end=65,
)


_GETLEVELGIFTRESPONSE = _descriptor.Descriptor(
  name='GetLevelGiftResponse',
  full_name='GetLevelGiftResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GetLevelGiftResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='GetLevelGiftResponse.gain', index=1,
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
  serialized_start=67,
  serialized_end=143,
)


_NEWLEVELGIFTRESPONSE = _descriptor.Descriptor(
  name='NewLevelGiftResponse',
  full_name='NewLevelGiftResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='NewLevelGiftResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_info', full_name='NewLevelGiftResponse.level_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=145,
  serialized_end=233,
)


_LEVELGIFTINFO = _descriptor.Descriptor(
  name='LevelGiftInfo',
  full_name='LevelGiftInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='LevelGiftInfo.level', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drops', full_name='LevelGiftInfo.drops', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=235,
  serialized_end=304,
)

_GETLEVELGIFTRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_NEWLEVELGIFTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_NEWLEVELGIFTRESPONSE.fields_by_name['level_info'].message_type = _LEVELGIFTINFO
_LEVELGIFTINFO.fields_by_name['drops'].message_type = common_pb2._GAMERESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['GetLevelGift'] = _GETLEVELGIFT
DESCRIPTOR.message_types_by_name['GetLevelGiftResponse'] = _GETLEVELGIFTRESPONSE
DESCRIPTOR.message_types_by_name['NewLevelGiftResponse'] = _NEWLEVELGIFTRESPONSE
DESCRIPTOR.message_types_by_name['LevelGiftInfo'] = _LEVELGIFTINFO

class GetLevelGift(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETLEVELGIFT

  # @@protoc_insertion_point(class_scope:GetLevelGift)

class GetLevelGiftResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETLEVELGIFTRESPONSE

  # @@protoc_insertion_point(class_scope:GetLevelGiftResponse)

class NewLevelGiftResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWLEVELGIFTRESPONSE

  # @@protoc_insertion_point(class_scope:NewLevelGiftResponse)

class LevelGiftInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEVELGIFTINFO

  # @@protoc_insertion_point(class_scope:LevelGiftInfo)


# @@protoc_insertion_point(module_scope)
