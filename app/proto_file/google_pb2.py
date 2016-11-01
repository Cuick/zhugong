# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google.proto',
  package='',
  serialized_pb='\n\x0cgoogle.proto\x1a\x0c\x63ommon.proto\"$\n\x0cRechargeTest\x12\x14\n\x0crecharge_num\x18\x01 \x01(\x05\"*\n\x17GoogleGenerateIDRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x05\"\'\n\x18GoogleGenerateIDResponse\x12\x0b\n\x03uid\x18\x01 \x01(\t\"$\n\x14GoogleConsumeRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"5\n\x15GoogleConsumeResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\"=\n\x1aGoogleConsumeVerifyRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\t\"\x81\x01\n\x1bGoogleConsumeVerifyResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\x12\x1e\n\x04info\x18\x03 \x01(\x0b\x32\x10.GetGoldResponse')




_RECHARGETEST = _descriptor.Descriptor(
  name='RechargeTest',
  full_name='RechargeTest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recharge_num', full_name='RechargeTest.recharge_num', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=30,
  serialized_end=66,
)


_GOOGLEGENERATEIDREQUEST = _descriptor.Descriptor(
  name='GoogleGenerateIDRequest',
  full_name='GoogleGenerateIDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='GoogleGenerateIDRequest.channel', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=68,
  serialized_end=110,
)


_GOOGLEGENERATEIDRESPONSE = _descriptor.Descriptor(
  name='GoogleGenerateIDResponse',
  full_name='GoogleGenerateIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='GoogleGenerateIDResponse.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=112,
  serialized_end=151,
)


_GOOGLECONSUMEREQUEST = _descriptor.Descriptor(
  name='GoogleConsumeRequest',
  full_name='GoogleConsumeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='GoogleConsumeRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=153,
  serialized_end=189,
)


_GOOGLECONSUMERESPONSE = _descriptor.Descriptor(
  name='GoogleConsumeResponse',
  full_name='GoogleConsumeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='GoogleConsumeResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=191,
  serialized_end=244,
)


_GOOGLECONSUMEVERIFYREQUEST = _descriptor.Descriptor(
  name='GoogleConsumeVerifyRequest',
  full_name='GoogleConsumeVerifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='GoogleConsumeVerifyRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='GoogleConsumeVerifyRequest.signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=246,
  serialized_end=307,
)


_GOOGLECONSUMEVERIFYRESPONSE = _descriptor.Descriptor(
  name='GoogleConsumeVerifyResponse',
  full_name='GoogleConsumeVerifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='GoogleConsumeVerifyResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='GoogleConsumeVerifyResponse.gain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='GoogleConsumeVerifyResponse.info', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=310,
  serialized_end=439,
)

_GOOGLECONSUMERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_GOOGLECONSUMEVERIFYRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_GOOGLECONSUMEVERIFYRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_GOOGLECONSUMEVERIFYRESPONSE.fields_by_name['info'].message_type = common_pb2._GETGOLDRESPONSE
DESCRIPTOR.message_types_by_name['RechargeTest'] = _RECHARGETEST
DESCRIPTOR.message_types_by_name['GoogleGenerateIDRequest'] = _GOOGLEGENERATEIDREQUEST
DESCRIPTOR.message_types_by_name['GoogleGenerateIDResponse'] = _GOOGLEGENERATEIDRESPONSE
DESCRIPTOR.message_types_by_name['GoogleConsumeRequest'] = _GOOGLECONSUMEREQUEST
DESCRIPTOR.message_types_by_name['GoogleConsumeResponse'] = _GOOGLECONSUMERESPONSE
DESCRIPTOR.message_types_by_name['GoogleConsumeVerifyRequest'] = _GOOGLECONSUMEVERIFYREQUEST
DESCRIPTOR.message_types_by_name['GoogleConsumeVerifyResponse'] = _GOOGLECONSUMEVERIFYRESPONSE

class RechargeTest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECHARGETEST

  # @@protoc_insertion_point(class_scope:RechargeTest)

class GoogleGenerateIDRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GOOGLEGENERATEIDREQUEST

  # @@protoc_insertion_point(class_scope:GoogleGenerateIDRequest)

class GoogleGenerateIDResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GOOGLEGENERATEIDRESPONSE

  # @@protoc_insertion_point(class_scope:GoogleGenerateIDResponse)

class GoogleConsumeRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GOOGLECONSUMEREQUEST

  # @@protoc_insertion_point(class_scope:GoogleConsumeRequest)

class GoogleConsumeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GOOGLECONSUMERESPONSE

  # @@protoc_insertion_point(class_scope:GoogleConsumeResponse)

class GoogleConsumeVerifyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GOOGLECONSUMEVERIFYREQUEST

  # @@protoc_insertion_point(class_scope:GoogleConsumeVerifyRequest)

class GoogleConsumeVerifyResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GOOGLECONSUMEVERIFYRESPONSE

  # @@protoc_insertion_point(class_scope:GoogleConsumeVerifyResponse)


# @@protoc_insertion_point(module_scope)