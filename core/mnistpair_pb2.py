# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mnistpair.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mnistpair.proto',
  package='mnist',
  syntax='proto2',
  serialized_pb=_b('\n\x0fmnistpair.proto\x12\x05mnist\"W\n\x05\x44\x61tum\x12\x10\n\x08\x63hannels\x18\x01 \x02(\x05\x12\x0e\n\x06height\x18\x02 \x02(\x05\x12\r\n\x05width\x18\x03 \x02(\x05\x12\x0e\n\x06\x66rames\x18\x04 \x03(\x0c\x12\r\n\x05label\x18\x05 \x02(\x05')
)




_DATUM = _descriptor.Descriptor(
  name='Datum',
  full_name='mnist.Datum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='mnist.Datum.channels', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='mnist.Datum.height', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='mnist.Datum.width', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frames', full_name='mnist.Datum.frames', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='mnist.Datum.label', index=4,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['Datum'] = _DATUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Datum = _reflection.GeneratedProtocolMessageType('Datum', (_message.Message,), dict(
  DESCRIPTOR = _DATUM,
  __module__ = 'mnistpair_pb2'
  # @@protoc_insertion_point(class_scope:mnist.Datum)
  ))
_sym_db.RegisterMessage(Datum)


# @@protoc_insertion_point(module_scope)