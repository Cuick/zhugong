# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gm.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gm.proto',
  package='',
  serialized_pb='\n\x08gm.proto\"$\n\x13GmCommonModifyLevel\x12\r\n\x05level\x18\x02 \x01(\x05')




_GMCOMMONMODIFYLEVEL = _descriptor.Descriptor(
  name='GmCommonModifyLevel',
  full_name='GmCommonModifyLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='GmCommonModifyLevel.level', index=0,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=12,
  serialized_end=48,
)

DESCRIPTOR.message_types_by_name['GmCommonModifyLevel'] = _GMCOMMONMODIFYLEVEL

class GmCommonModifyLevel(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GMCOMMONMODIFYLEVEL

  # @@protoc_insertion_point(class_scope:GmCommonModifyLevel)


# @@protoc_insertion_point(module_scope)