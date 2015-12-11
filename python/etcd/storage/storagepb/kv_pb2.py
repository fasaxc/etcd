# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: etcd/storage/storagepb/kv.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='etcd/storage/storagepb/kv.proto',
  package='storagepb',
  syntax='proto3',
  serialized_pb=b'\n\x1f\x65tcd/storage/storagepb/kv.proto\x12\tstoragepb\x1a\x14gogoproto/gogo.proto\"f\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x17\n\x0f\x63reate_revision\x18\x02 \x01(\x03\x12\x14\n\x0cmod_revision\x18\x03 \x01(\x03\x12\x0f\n\x07version\x18\x04 \x01(\x03\x12\r\n\x05value\x18\x05 \x01(\x0c\"\x91\x01\n\x05\x45vent\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.storagepb.Event.EventType\x12\x1f\n\x02kv\x18\x02 \x01(\x0b\x32\x13.storagepb.KeyValue\x12\x0f\n\x07watchID\x18\x03 \x01(\x03\",\n\tEventType\x12\x07\n\x03PUT\x10\x00\x12\n\n\x06\x44\x45LETE\x10\x01\x12\n\n\x06\x45XPIRE\x10\x02\x42\x14\xc8\xe2\x1e\x01\xe0\xe2\x1e\x01\xd0\xe2\x1e\x01\xc8\xe1\x1e\x00\xd0\xe1\x1e\x00\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_EVENT_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='storagepb.Event.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PUT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=274,
  serialized_end=318,
)
_sym_db.RegisterEnumDescriptor(_EVENT_EVENTTYPE)


_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='storagepb.KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='storagepb.KeyValue.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_revision', full_name='storagepb.KeyValue.create_revision', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mod_revision', full_name='storagepb.KeyValue.mod_revision', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='storagepb.KeyValue.version', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='storagepb.KeyValue.value', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=170,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='storagepb.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='storagepb.Event.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kv', full_name='storagepb.Event.kv', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='watchID', full_name='storagepb.Event.watchID', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENT_EVENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=318,
)

_EVENT.fields_by_name['type'].enum_type = _EVENT_EVENTTYPE
_EVENT.fields_by_name['kv'].message_type = _KEYVALUE
_EVENT_EVENTTYPE.containing_type = _EVENT
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUE,
  __module__ = 'etcd.storage.storagepb.kv_pb2'
  # @@protoc_insertion_point(class_scope:storagepb.KeyValue)
  ))
_sym_db.RegisterMessage(KeyValue)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'etcd.storage.storagepb.kv_pb2'
  # @@protoc_insertion_point(class_scope:storagepb.Event)
  ))
_sym_db.RegisterMessage(Event)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\310\342\036\001\340\342\036\001\320\342\036\001\310\341\036\000\320\341\036\000')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
