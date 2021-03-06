# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: friend.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2
import stage_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='friend.proto',
  package='',
  serialized_pb='\n\x0c\x66riend.proto\x1a\x0c\x63ommon.proto\x1a\x0bstage.proto\"\"\n\x0c\x46riendCommon\x12\x12\n\ntarget_ids\x18\x01 \x03(\x05\"#\n\x11\x41\x64\x64\x46riendResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\"+\n\x11\x46indFriendRequest\x12\x16\n\x0eid_or_nickname\x18\x01 \x01(\x0c\"3\n\x12\x46indFriendResponse\x12\x1d\n\x05infos\x18\x01 \x03(\x0b\x32\x0e.CharacterInfo\"\x19\n\x17GetPlayerFriendsRequest\"\xc6\x02\n\rCharacterInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x0f\n\x07hero_no\x18\x03 \x01(\x05\x12\x0f\n\x04gift\x18\x04 \x01(\x05:\x01\x30\x12\x13\n\x05power\x18\x05 \x01(\x02:\x04\x31\x30\x31\x30\x12\x14\n\tlast_time\x18\n \x01(\x05:\x01\x30\x12\x0f\n\x07\x63urrent\x18\x0c \x01(\x05\x12\x0e\n\x06target\x18\r \x01(\x05\x12\x0c\n\x04stat\x18\x0e \x01(\x05\x12\r\n\x05level\x18\x0f \x01(\x05\x12\x11\n\x06\x62_rank\x18\x10 \x01(\x05:\x01\x31\x12\x11\n\tvip_level\x18\x13 \x01(\x05\x12\x13\n\x0b\x66ight_times\x18\x14 \x01(\x05\x12\x17\n\x0f\x66ight_last_time\x18\x15 \x01(\x05\x12 \n\x0b\x66riend_info\x18\x16 \x01(\x0b\x32\x0b.BattleUnit\x12\x16\n\x0eguild_position\x18\x17 \x01(\x05\"\xae\x01\n\x18GetPlayerFriendsResponse\x12\x14\n\x0copen_receive\x18\x01 \x01(\x05\x12\x10\n\x08page_num\x18\x02 \x01(\x05\x12\x1f\n\x07\x66riends\x18\x03 \x03(\x0b\x32\x0e.CharacterInfo\x12!\n\tblacklist\x18\x04 \x03(\x0b\x32\x0e.CharacterInfo\x12&\n\x0e\x61pplicant_list\x18\x05 \x03(\x0b\x32\x0e.CharacterInfo\"?\n\x18\x46riendPrivateChatRequest\x12\x12\n\ntarget_uid\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"h\n\x1bGetRecommendFriendsResponse\x12\x14\n\x0copen_receive\x18\x01 \x01(\x05\x12\x10\n\x08page_num\x18\x02 \x01(\x05\x12!\n\trecommend\x18\x03 \x03(\x0b\x32\x0e.CharacterInfo\"\x1c\n\rDrawRewardReq\x12\x0b\n\x03\x66id\x18\x01 \x02(\x05\"`\n\rDrawRewardRsp\x12\x0b\n\x03\x66id\x18\x01 \x02(\x05\x12\x1c\n\x03res\x18\x02 \x02(\x0b\x32\x0f.CommonResponse\x12$\n\x04gain\x18\x03 \x01(\x0b\x32\x16.GameResourcesResponse\"\x0e\n\x0cRecommendReq\"/\n\x0cRecommendRes\x12\x1f\n\x07rfriend\x18\x01 \x03(\x0b\x32\x0e.CharacterInfo')




_FRIENDCOMMON = _descriptor.Descriptor(
  name='FriendCommon',
  full_name='FriendCommon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_ids', full_name='FriendCommon.target_ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=43,
  serialized_end=77,
)


_ADDFRIENDRESPONSE = _descriptor.Descriptor(
  name='AddFriendResponse',
  full_name='AddFriendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='AddFriendResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=79,
  serialized_end=114,
)


_FINDFRIENDREQUEST = _descriptor.Descriptor(
  name='FindFriendRequest',
  full_name='FindFriendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_or_nickname', full_name='FindFriendRequest.id_or_nickname', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=116,
  serialized_end=159,
)


_FINDFRIENDRESPONSE = _descriptor.Descriptor(
  name='FindFriendResponse',
  full_name='FindFriendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='infos', full_name='FindFriendResponse.infos', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=161,
  serialized_end=212,
)


_GETPLAYERFRIENDSREQUEST = _descriptor.Descriptor(
  name='GetPlayerFriendsRequest',
  full_name='GetPlayerFriendsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=214,
  serialized_end=239,
)


_CHARACTERINFO = _descriptor.Descriptor(
  name='CharacterInfo',
  full_name='CharacterInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CharacterInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='CharacterInfo.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='CharacterInfo.hero_no', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift', full_name='CharacterInfo.gift', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='CharacterInfo.power', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1010,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_time', full_name='CharacterInfo.last_time', index=5,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current', full_name='CharacterInfo.current', index=6,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='CharacterInfo.target', index=7,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stat', full_name='CharacterInfo.stat', index=8,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='CharacterInfo.level', index=9,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b_rank', full_name='CharacterInfo.b_rank', index=10,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='CharacterInfo.vip_level', index=11,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight_times', full_name='CharacterInfo.fight_times', index=12,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight_last_time', full_name='CharacterInfo.fight_last_time', index=13,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_info', full_name='CharacterInfo.friend_info', index=14,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_position', full_name='CharacterInfo.guild_position', index=15,
      number=23, type=5, cpp_type=1, label=1,
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
  serialized_start=242,
  serialized_end=568,
)


_GETPLAYERFRIENDSRESPONSE = _descriptor.Descriptor(
  name='GetPlayerFriendsResponse',
  full_name='GetPlayerFriendsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='open_receive', full_name='GetPlayerFriendsResponse.open_receive', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_num', full_name='GetPlayerFriendsResponse.page_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friends', full_name='GetPlayerFriendsResponse.friends', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blacklist', full_name='GetPlayerFriendsResponse.blacklist', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applicant_list', full_name='GetPlayerFriendsResponse.applicant_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=571,
  serialized_end=745,
)


_FRIENDPRIVATECHATREQUEST = _descriptor.Descriptor(
  name='FriendPrivateChatRequest',
  full_name='FriendPrivateChatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_uid', full_name='FriendPrivateChatRequest.target_uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='FriendPrivateChatRequest.content', index=1,
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
  serialized_start=747,
  serialized_end=810,
)


_GETRECOMMENDFRIENDSRESPONSE = _descriptor.Descriptor(
  name='GetRecommendFriendsResponse',
  full_name='GetRecommendFriendsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='open_receive', full_name='GetRecommendFriendsResponse.open_receive', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_num', full_name='GetRecommendFriendsResponse.page_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recommend', full_name='GetRecommendFriendsResponse.recommend', index=2,
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
  serialized_start=812,
  serialized_end=916,
)


_DRAWREWARDREQ = _descriptor.Descriptor(
  name='DrawRewardReq',
  full_name='DrawRewardReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fid', full_name='DrawRewardReq.fid', index=0,
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
  serialized_start=918,
  serialized_end=946,
)


_DRAWREWARDRSP = _descriptor.Descriptor(
  name='DrawRewardRsp',
  full_name='DrawRewardRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fid', full_name='DrawRewardRsp.fid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res', full_name='DrawRewardRsp.res', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='DrawRewardRsp.gain', index=2,
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
  serialized_start=948,
  serialized_end=1044,
)


_RECOMMENDREQ = _descriptor.Descriptor(
  name='RecommendReq',
  full_name='RecommendReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1046,
  serialized_end=1060,
)


_RECOMMENDRES = _descriptor.Descriptor(
  name='RecommendRes',
  full_name='RecommendRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rfriend', full_name='RecommendRes.rfriend', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1062,
  serialized_end=1109,
)

_FINDFRIENDRESPONSE.fields_by_name['infos'].message_type = _CHARACTERINFO
_CHARACTERINFO.fields_by_name['friend_info'].message_type = stage_pb2._BATTLEUNIT
_GETPLAYERFRIENDSRESPONSE.fields_by_name['friends'].message_type = _CHARACTERINFO
_GETPLAYERFRIENDSRESPONSE.fields_by_name['blacklist'].message_type = _CHARACTERINFO
_GETPLAYERFRIENDSRESPONSE.fields_by_name['applicant_list'].message_type = _CHARACTERINFO
_GETRECOMMENDFRIENDSRESPONSE.fields_by_name['recommend'].message_type = _CHARACTERINFO
_DRAWREWARDRSP.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_DRAWREWARDRSP.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_RECOMMENDRES.fields_by_name['rfriend'].message_type = _CHARACTERINFO
DESCRIPTOR.message_types_by_name['FriendCommon'] = _FRIENDCOMMON
DESCRIPTOR.message_types_by_name['AddFriendResponse'] = _ADDFRIENDRESPONSE
DESCRIPTOR.message_types_by_name['FindFriendRequest'] = _FINDFRIENDREQUEST
DESCRIPTOR.message_types_by_name['FindFriendResponse'] = _FINDFRIENDRESPONSE
DESCRIPTOR.message_types_by_name['GetPlayerFriendsRequest'] = _GETPLAYERFRIENDSREQUEST
DESCRIPTOR.message_types_by_name['CharacterInfo'] = _CHARACTERINFO
DESCRIPTOR.message_types_by_name['GetPlayerFriendsResponse'] = _GETPLAYERFRIENDSRESPONSE
DESCRIPTOR.message_types_by_name['FriendPrivateChatRequest'] = _FRIENDPRIVATECHATREQUEST
DESCRIPTOR.message_types_by_name['GetRecommendFriendsResponse'] = _GETRECOMMENDFRIENDSRESPONSE
DESCRIPTOR.message_types_by_name['DrawRewardReq'] = _DRAWREWARDREQ
DESCRIPTOR.message_types_by_name['DrawRewardRsp'] = _DRAWREWARDRSP
DESCRIPTOR.message_types_by_name['RecommendReq'] = _RECOMMENDREQ
DESCRIPTOR.message_types_by_name['RecommendRes'] = _RECOMMENDRES

class FriendCommon(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDCOMMON

  # @@protoc_insertion_point(class_scope:FriendCommon)

class AddFriendResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDFRIENDRESPONSE

  # @@protoc_insertion_point(class_scope:AddFriendResponse)

class FindFriendRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FINDFRIENDREQUEST

  # @@protoc_insertion_point(class_scope:FindFriendRequest)

class FindFriendResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FINDFRIENDRESPONSE

  # @@protoc_insertion_point(class_scope:FindFriendResponse)

class GetPlayerFriendsRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPLAYERFRIENDSREQUEST

  # @@protoc_insertion_point(class_scope:GetPlayerFriendsRequest)

class CharacterInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARACTERINFO

  # @@protoc_insertion_point(class_scope:CharacterInfo)

class GetPlayerFriendsResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPLAYERFRIENDSRESPONSE

  # @@protoc_insertion_point(class_scope:GetPlayerFriendsResponse)

class FriendPrivateChatRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDPRIVATECHATREQUEST

  # @@protoc_insertion_point(class_scope:FriendPrivateChatRequest)

class GetRecommendFriendsResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETRECOMMENDFRIENDSRESPONSE

  # @@protoc_insertion_point(class_scope:GetRecommendFriendsResponse)

class DrawRewardReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DRAWREWARDREQ

  # @@protoc_insertion_point(class_scope:DrawRewardReq)

class DrawRewardRsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DRAWREWARDRSP

  # @@protoc_insertion_point(class_scope:DrawRewardRsp)

class RecommendReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECOMMENDREQ

  # @@protoc_insertion_point(class_scope:RecommendReq)

class RecommendRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECOMMENDRES

  # @@protoc_insertion_point(class_scope:RecommendRes)


# @@protoc_insertion_point(module_scope)
