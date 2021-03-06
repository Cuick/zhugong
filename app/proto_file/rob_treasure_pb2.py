# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rob_treasure.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2
import equipment_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rob_treasure.proto',
  package='',
  serialized_pb='\n\x12rob_treasure.proto\x1a\x0c\x63ommon.proto\x1a\x0f\x65quipment.proto\"\xa5\x01\n\x17RobTreasureInitResponse\x12\x13\n\x0bstart_truce\x18\x01 \x01(\x05\x12\x16\n\x0etruce_item_num\x18\x02 \x01(\x05\x12\x1a\n\x12truce_item_num_day\x18\x03 \x02(\x05\x12+\n\x0bplayer_info\x18\x04 \x03(\x0b\x32\x16.PlayerRobTreasureInfo\x12\x14\n\x0crefresh_time\x18\x05 \x02(\x05\"&\n\x17RobTreasureTruceRequest\x12\x0b\n\x03num\x18\x01 \x02(\x05\"\xaa\x01\n\x18RobTreasureTruceResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x13\n\x0bstart_truce\x18\x02 \x01(\x05\x12\x16\n\x0etruce_item_num\x18\x03 \x01(\x05\x12\x1a\n\x12truce_item_num_day\x18\x04 \x01(\x05\x12\'\n\x07\x63onsume\x18\x05 \x01(\x0b\x32\x16.GameResourcesResponse\"-\n\x16\x43omposeTreasureRequest\x12\x13\n\x0btreasure_id\x18\x01 \x02(\x05\"R\n\x17\x43omposeTreasureResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x19\n\x03\x65qu\x18\x02 \x01(\x0b\x32\x0c.EquipmentPB\"\"\n\x13\x42uyTruceItemRequest\x12\x0b\n\x03num\x18\x01 \x02(\x05\"\x83\x01\n\x14\x42uyTruceItemResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\'\n\x07\x63onsume\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\x12$\n\x04gain\x18\x03 \x01(\x0b\x32\x16.GameResourcesResponse\"\x99\x01\n\x15PlayerRobTreasureInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05power\x18\x03 \x01(\x05\x12\x10\n\x08guild_id\x18\x04 \x01(\t\x12\x11\n\tvip_level\x18\x05 \x01(\x05\x12\x10\n\x08now_head\x18\x06 \x01(\x05\x12\r\n\x05level\x18\x07 \x01(\x05\x12\r\n\x05\x63olor\x18\x08 \x01(\x05\"}\n\x1aRefreshRobTreasureResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12+\n\x0bplayer_info\x18\x02 \x03(\x0b\x32\x16.PlayerRobTreasureInfo\x12\x14\n\x0crefresh_time\x18\x03 \x01(\x05\"\x8a\x01\n\x19RobTreasureRewardResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\x12)\n\tlook_gain\x18\x03 \x03(\x0b\x32\x16.GameResourcesResponse\" \n\rBeRobTreasure\x12\x0f\n\x07\x63hip_id\x18\x01 \x02(\x05\"7\n\x19RobTreasureEnhanceRequest\x12\n\n\x02no\x18\x01 \x02(\t\x12\x0e\n\x06use_no\x18\x02 \x03(\t\":\n\x1aRobTreasureEnhanceResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse')




_ROBTREASUREINITRESPONSE = _descriptor.Descriptor(
  name='RobTreasureInitResponse',
  full_name='RobTreasureInitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_truce', full_name='RobTreasureInitResponse.start_truce', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truce_item_num', full_name='RobTreasureInitResponse.truce_item_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truce_item_num_day', full_name='RobTreasureInitResponse.truce_item_num_day', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_info', full_name='RobTreasureInitResponse.player_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refresh_time', full_name='RobTreasureInitResponse.refresh_time', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=54,
  serialized_end=219,
)


_ROBTREASURETRUCEREQUEST = _descriptor.Descriptor(
  name='RobTreasureTruceRequest',
  full_name='RobTreasureTruceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='RobTreasureTruceRequest.num', index=0,
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
  serialized_start=221,
  serialized_end=259,
)


_ROBTREASURETRUCERESPONSE = _descriptor.Descriptor(
  name='RobTreasureTruceResponse',
  full_name='RobTreasureTruceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='RobTreasureTruceResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_truce', full_name='RobTreasureTruceResponse.start_truce', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truce_item_num', full_name='RobTreasureTruceResponse.truce_item_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='truce_item_num_day', full_name='RobTreasureTruceResponse.truce_item_num_day', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume', full_name='RobTreasureTruceResponse.consume', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=262,
  serialized_end=432,
)


_COMPOSETREASUREREQUEST = _descriptor.Descriptor(
  name='ComposeTreasureRequest',
  full_name='ComposeTreasureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='treasure_id', full_name='ComposeTreasureRequest.treasure_id', index=0,
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
  serialized_start=434,
  serialized_end=479,
)


_COMPOSETREASURERESPONSE = _descriptor.Descriptor(
  name='ComposeTreasureResponse',
  full_name='ComposeTreasureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='ComposeTreasureResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equ', full_name='ComposeTreasureResponse.equ', index=1,
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
  serialized_start=481,
  serialized_end=563,
)


_BUYTRUCEITEMREQUEST = _descriptor.Descriptor(
  name='BuyTruceItemRequest',
  full_name='BuyTruceItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='BuyTruceItemRequest.num', index=0,
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
  serialized_start=565,
  serialized_end=599,
)


_BUYTRUCEITEMRESPONSE = _descriptor.Descriptor(
  name='BuyTruceItemResponse',
  full_name='BuyTruceItemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='BuyTruceItemResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume', full_name='BuyTruceItemResponse.consume', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='BuyTruceItemResponse.gain', index=2,
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
  serialized_start=602,
  serialized_end=733,
)


_PLAYERROBTREASUREINFO = _descriptor.Descriptor(
  name='PlayerRobTreasureInfo',
  full_name='PlayerRobTreasureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PlayerRobTreasureInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='PlayerRobTreasureInfo.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='PlayerRobTreasureInfo.power', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='PlayerRobTreasureInfo.guild_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='PlayerRobTreasureInfo.vip_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='now_head', full_name='PlayerRobTreasureInfo.now_head', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='PlayerRobTreasureInfo.level', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color', full_name='PlayerRobTreasureInfo.color', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=736,
  serialized_end=889,
)


_REFRESHROBTREASURERESPONSE = _descriptor.Descriptor(
  name='RefreshRobTreasureResponse',
  full_name='RefreshRobTreasureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='RefreshRobTreasureResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_info', full_name='RefreshRobTreasureResponse.player_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refresh_time', full_name='RefreshRobTreasureResponse.refresh_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=891,
  serialized_end=1016,
)


_ROBTREASUREREWARDRESPONSE = _descriptor.Descriptor(
  name='RobTreasureRewardResponse',
  full_name='RobTreasureRewardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='RobTreasureRewardResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='RobTreasureRewardResponse.gain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='look_gain', full_name='RobTreasureRewardResponse.look_gain', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=1019,
  serialized_end=1157,
)


_BEROBTREASURE = _descriptor.Descriptor(
  name='BeRobTreasure',
  full_name='BeRobTreasure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chip_id', full_name='BeRobTreasure.chip_id', index=0,
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
  serialized_start=1159,
  serialized_end=1191,
)


_ROBTREASUREENHANCEREQUEST = _descriptor.Descriptor(
  name='RobTreasureEnhanceRequest',
  full_name='RobTreasureEnhanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no', full_name='RobTreasureEnhanceRequest.no', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_no', full_name='RobTreasureEnhanceRequest.use_no', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=1193,
  serialized_end=1248,
)


_ROBTREASUREENHANCERESPONSE = _descriptor.Descriptor(
  name='RobTreasureEnhanceResponse',
  full_name='RobTreasureEnhanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='RobTreasureEnhanceResponse.res', index=0,
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
  serialized_start=1250,
  serialized_end=1308,
)

_ROBTREASUREINITRESPONSE.fields_by_name['player_info'].message_type = _PLAYERROBTREASUREINFO
_ROBTREASURETRUCERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_ROBTREASURETRUCERESPONSE.fields_by_name['consume'].message_type = common_pb2._GAMERESOURCESRESPONSE
_COMPOSETREASURERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_COMPOSETREASURERESPONSE.fields_by_name['equ'].message_type = equipment_pb2._EQUIPMENTPB
_BUYTRUCEITEMRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_BUYTRUCEITEMRESPONSE.fields_by_name['consume'].message_type = common_pb2._GAMERESOURCESRESPONSE
_BUYTRUCEITEMRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_REFRESHROBTREASURERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_REFRESHROBTREASURERESPONSE.fields_by_name['player_info'].message_type = _PLAYERROBTREASUREINFO
_ROBTREASUREREWARDRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_ROBTREASUREREWARDRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_ROBTREASUREREWARDRESPONSE.fields_by_name['look_gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_ROBTREASUREENHANCERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['RobTreasureInitResponse'] = _ROBTREASUREINITRESPONSE
DESCRIPTOR.message_types_by_name['RobTreasureTruceRequest'] = _ROBTREASURETRUCEREQUEST
DESCRIPTOR.message_types_by_name['RobTreasureTruceResponse'] = _ROBTREASURETRUCERESPONSE
DESCRIPTOR.message_types_by_name['ComposeTreasureRequest'] = _COMPOSETREASUREREQUEST
DESCRIPTOR.message_types_by_name['ComposeTreasureResponse'] = _COMPOSETREASURERESPONSE
DESCRIPTOR.message_types_by_name['BuyTruceItemRequest'] = _BUYTRUCEITEMREQUEST
DESCRIPTOR.message_types_by_name['BuyTruceItemResponse'] = _BUYTRUCEITEMRESPONSE
DESCRIPTOR.message_types_by_name['PlayerRobTreasureInfo'] = _PLAYERROBTREASUREINFO
DESCRIPTOR.message_types_by_name['RefreshRobTreasureResponse'] = _REFRESHROBTREASURERESPONSE
DESCRIPTOR.message_types_by_name['RobTreasureRewardResponse'] = _ROBTREASUREREWARDRESPONSE
DESCRIPTOR.message_types_by_name['BeRobTreasure'] = _BEROBTREASURE
DESCRIPTOR.message_types_by_name['RobTreasureEnhanceRequest'] = _ROBTREASUREENHANCEREQUEST
DESCRIPTOR.message_types_by_name['RobTreasureEnhanceResponse'] = _ROBTREASUREENHANCERESPONSE

class RobTreasureInitResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBTREASUREINITRESPONSE

  # @@protoc_insertion_point(class_scope:RobTreasureInitResponse)

class RobTreasureTruceRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBTREASURETRUCEREQUEST

  # @@protoc_insertion_point(class_scope:RobTreasureTruceRequest)

class RobTreasureTruceResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBTREASURETRUCERESPONSE

  # @@protoc_insertion_point(class_scope:RobTreasureTruceResponse)

class ComposeTreasureRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMPOSETREASUREREQUEST

  # @@protoc_insertion_point(class_scope:ComposeTreasureRequest)

class ComposeTreasureResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMPOSETREASURERESPONSE

  # @@protoc_insertion_point(class_scope:ComposeTreasureResponse)

class BuyTruceItemRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYTRUCEITEMREQUEST

  # @@protoc_insertion_point(class_scope:BuyTruceItemRequest)

class BuyTruceItemResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYTRUCEITEMRESPONSE

  # @@protoc_insertion_point(class_scope:BuyTruceItemResponse)

class PlayerRobTreasureInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PLAYERROBTREASUREINFO

  # @@protoc_insertion_point(class_scope:PlayerRobTreasureInfo)

class RefreshRobTreasureResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REFRESHROBTREASURERESPONSE

  # @@protoc_insertion_point(class_scope:RefreshRobTreasureResponse)

class RobTreasureRewardResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBTREASUREREWARDRESPONSE

  # @@protoc_insertion_point(class_scope:RobTreasureRewardResponse)

class BeRobTreasure(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BEROBTREASURE

  # @@protoc_insertion_point(class_scope:BeRobTreasure)

class RobTreasureEnhanceRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBTREASUREENHANCEREQUEST

  # @@protoc_insertion_point(class_scope:RobTreasureEnhanceRequest)

class RobTreasureEnhanceResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBTREASUREENHANCERESPONSE

  # @@protoc_insertion_point(class_scope:RobTreasureEnhanceResponse)


# @@protoc_insertion_point(module_scope)
