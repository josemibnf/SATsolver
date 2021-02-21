# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobufs/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobufs import instances_pb2 as protobufs_dot_instances__pb2
from protobufs import ipss_pb2 as protobufs_dot_ipss__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobufs/service.proto',
  package='protobufs.service',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17protobufs/service.proto\x12\x11protobufs.service\x1a\x19protobufs/instances.proto\x1a\x14protobufs/ipss.proto\"\x12\n\x10WhoAreYourParams\"i\n\x0fServiceExtended\x12,\n\tmultihash\x18\x01 \x01(\x0b\x32\x19.protobufs.ipss.Multihash\x12(\n\x07service\x18\x02 \x01(\x0b\x32\x17.protobufs.ipss.Service\"\x14\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t2\xfe\x03\n\x06Solver\x12X\n\nStartTrain\x12#.protobufs.service.WhoAreYourParams\x1a#.protobufs.service.WhoAreYourParams\"\x00\x12W\n\tStopTrain\x12#.protobufs.service.WhoAreYourParams\x1a#.protobufs.service.WhoAreYourParams\"\x00\x12L\n\tGetTensor\x12#.protobufs.service.WhoAreYourParams\x1a\x16.protobufs.ipss.Tensor\"\x00\x30\x01\x12Y\n\x0cUploadSolver\x12\".protobufs.service.ServiceExtended\x1a#.protobufs.service.WhoAreYourParams\"\x00\x12N\n\nStreamLogs\x12#.protobufs.service.WhoAreYourParams\x1a\x17.protobufs.service.File\"\x00\x30\x01\x12H\n\x05Solve\x12\x18.protobufs.instances.Cnf\x1a#.protobufs.instances.Interpretation\"\x00\x62\x06proto3'
  ,
  dependencies=[protobufs_dot_instances__pb2.DESCRIPTOR,protobufs_dot_ipss__pb2.DESCRIPTOR,])




_WHOAREYOURPARAMS = _descriptor.Descriptor(
  name='WhoAreYourParams',
  full_name='protobufs.service.WhoAreYourParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=113,
)


_SERVICEEXTENDED = _descriptor.Descriptor(
  name='ServiceExtended',
  full_name='protobufs.service.ServiceExtended',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='multihash', full_name='protobufs.service.ServiceExtended.multihash', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='protobufs.service.ServiceExtended.service', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=220,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='protobufs.service.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='protobufs.service.File.file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=242,
)

_SERVICEEXTENDED.fields_by_name['multihash'].message_type = protobufs_dot_ipss__pb2._MULTIHASH
_SERVICEEXTENDED.fields_by_name['service'].message_type = protobufs_dot_ipss__pb2._SERVICE
DESCRIPTOR.message_types_by_name['WhoAreYourParams'] = _WHOAREYOURPARAMS
DESCRIPTOR.message_types_by_name['ServiceExtended'] = _SERVICEEXTENDED
DESCRIPTOR.message_types_by_name['File'] = _FILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WhoAreYourParams = _reflection.GeneratedProtocolMessageType('WhoAreYourParams', (_message.Message,), {
  'DESCRIPTOR' : _WHOAREYOURPARAMS,
  '__module__' : 'protobufs.service_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.service.WhoAreYourParams)
  })
_sym_db.RegisterMessage(WhoAreYourParams)

ServiceExtended = _reflection.GeneratedProtocolMessageType('ServiceExtended', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEEXTENDED,
  '__module__' : 'protobufs.service_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.service.ServiceExtended)
  })
_sym_db.RegisterMessage(ServiceExtended)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'protobufs.service_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.service.File)
  })
_sym_db.RegisterMessage(File)



_SOLVER = _descriptor.ServiceDescriptor(
  name='Solver',
  full_name='protobufs.service.Solver',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=245,
  serialized_end=755,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartTrain',
    full_name='protobufs.service.Solver.StartTrain',
    index=0,
    containing_service=None,
    input_type=_WHOAREYOURPARAMS,
    output_type=_WHOAREYOURPARAMS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopTrain',
    full_name='protobufs.service.Solver.StopTrain',
    index=1,
    containing_service=None,
    input_type=_WHOAREYOURPARAMS,
    output_type=_WHOAREYOURPARAMS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTensor',
    full_name='protobufs.service.Solver.GetTensor',
    index=2,
    containing_service=None,
    input_type=_WHOAREYOURPARAMS,
    output_type=protobufs_dot_ipss__pb2._TENSOR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadSolver',
    full_name='protobufs.service.Solver.UploadSolver',
    index=3,
    containing_service=None,
    input_type=_SERVICEEXTENDED,
    output_type=_WHOAREYOURPARAMS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamLogs',
    full_name='protobufs.service.Solver.StreamLogs',
    index=4,
    containing_service=None,
    input_type=_WHOAREYOURPARAMS,
    output_type=_FILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Solve',
    full_name='protobufs.service.Solver.Solve',
    index=5,
    containing_service=None,
    input_type=protobufs_dot_instances__pb2._CNF,
    output_type=protobufs_dot_instances__pb2._INTERPRETATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SOLVER)

DESCRIPTOR.services_by_name['Solver'] = _SOLVER

# @@protoc_insertion_point(module_scope)
