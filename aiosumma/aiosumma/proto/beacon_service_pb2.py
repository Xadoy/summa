# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: beacon_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x62\x65\x61\x63on_service.proto\x12\x0bsumma.proto\"L\n\x13PublishIndexRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x14\n\x07payload\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_payload\"\x16\n\x14PublishIndexResponse2c\n\tBeaconApi\x12V\n\rpublish_index\x12 .summa.proto.PublishIndexRequest\x1a!.summa.proto.PublishIndexResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'beacon_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PUBLISHINDEXREQUEST._serialized_start=37
  _PUBLISHINDEXREQUEST._serialized_end=113
  _PUBLISHINDEXRESPONSE._serialized_start=115
  _PUBLISHINDEXRESPONSE._serialized_end=137
  _BEACONAPI._serialized_start=139
  _BEACONAPI._serialized_end=238
# @@protoc_insertion_point(module_scope)
