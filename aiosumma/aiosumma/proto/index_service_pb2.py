# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: index_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import utils_pb2 as utils__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13index_service.proto\x12\x0bsumma.proto\x1a\x0butils.proto\"3\n\nPrimaryKey\x12\r\n\x03str\x18\x01 \x01(\tH\x00\x12\r\n\x03i64\x18\x02 \x01(\x03H\x00\x42\x07\n\x05value\"\x19\n\x17\x41ttachFileEngineRequest\"\x1b\n\x19\x41ttachRemoteEngineRequest\"&\n\x17\x41ttachIpfsEngineRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\"\x9b\x02\n\x12\x41ttachIndexRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12J\n\x1a\x61ttach_file_engine_request\x18\x02 \x01(\x0b\x32$.summa.proto.AttachFileEngineRequestH\x00\x12N\n\x1c\x61ttach_remote_engine_request\x18\x03 \x01(\x0b\x32&.summa.proto.AttachRemoteEngineRequestH\x00\x12J\n\x1a\x61ttach_ipfs_engine_request\x18\x04 \x01(\x0b\x32$.summa.proto.AttachIpfsEngineRequestH\x00\x42\t\n\x07request\"C\n\x13\x41ttachIndexResponse\x12,\n\x05index\x18\x01 \x01(\x0b\x32\x1d.summa.proto.IndexDescription\"W\n\x12\x43ommitIndexRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12,\n\x0b\x63ommit_mode\x18\x02 \x01(\x0e\x32\x17.summa.proto.CommitMode\"A\n\x13\x43ommitIndexResponse\x12\x19\n\x0c\x65lapsed_secs\x18\x02 \x01(\x01H\x00\x88\x01\x01\x42\x0f\n\r_elapsed_secs\"\x8f\x01\n\x13MigrateIndexRequest\x12\x19\n\x11source_index_name\x18\x01 \x01(\t\x12\x19\n\x11target_index_name\x18\x02 \x01(\t\x12\x42\n\x13target_index_engine\x18\x03 \x01(\x0e\x32%.summa.proto.CreateIndexEngineRequest\"D\n\x14MigrateIndexResponse\x12,\n\x05index\x18\x01 \x01(\x0b\x32\x1d.summa.proto.IndexDescription\"?\n\x0bSortByField\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12!\n\x05order\x18\x02 \x01(\x0e\x32\x12.summa.proto.Order\"\xf9\x01\n\x0fIndexAttributes\x12\x12\n\ncreated_at\x18\x01 \x01(\x04\x12\x18\n\x0bprimary_key\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x16\n\x0e\x64\x65\x66\x61ult_fields\x18\x03 \x03(\t\x12\x14\n\x0cmulti_fields\x18\x04 \x03(\t\x12\x1f\n\x12\x64\x65\x66\x61ult_index_name\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x06 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x10\x64\x65\x66\x61ult_snippets\x18\x07 \x03(\tB\x0e\n\x0c_primary_keyB\x15\n\x13_default_index_nameB\x0e\n\x0c_description\"\xca\x02\n\x12\x43reateIndexRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12;\n\x0cindex_engine\x18\x02 \x01(\x0e\x32%.summa.proto.CreateIndexEngineRequest\x12\x0e\n\x06schema\x18\x03 \x01(\t\x12-\n\x0b\x63ompression\x18\x04 \x01(\x0e\x32\x18.summa.proto.Compression\x12\x16\n\tblocksize\x18\x05 \x01(\rH\x00\x88\x01\x01\x12\x34\n\rsort_by_field\x18\x06 \x01(\x0b\x32\x18.summa.proto.SortByFieldH\x01\x88\x01\x01\x12\x36\n\x10index_attributes\x18\x07 \x01(\x0b\x32\x1c.summa.proto.IndexAttributesB\x0c\n\n_blocksizeB\x10\n\x0e_sort_by_field\"C\n\x13\x43reateIndexResponse\x12,\n\x05index\x18\x01 \x01(\x0b\x32\x1d.summa.proto.IndexDescription\"Z\n\x15\x44\x65leteDocumentRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12,\n\x0bprimary_key\x18\x02 \x01(\x0b\x32\x17.summa.proto.PrimaryKey\"\x18\n\x16\x44\x65leteDocumentResponse\"(\n\x12\x44\x65leteIndexRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\")\n\x13\x44\x65leteIndexResponse\x12\x12\n\nindex_name\x18\x01 \x01(\t\"\x1a\n\x18GetIndicesAliasesRequest\"\xa7\x01\n\x19GetIndicesAliasesResponse\x12S\n\x0findices_aliases\x18\x01 \x03(\x0b\x32:.summa.proto.GetIndicesAliasesResponse.IndicesAliasesEntry\x1a\x35\n\x13IndicesAliasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"&\n\x0fGetIndexRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\"@\n\x10GetIndexResponse\x12,\n\x05index\x18\x01 \x01(\x0b\x32\x1d.summa.proto.IndexDescription\"\x13\n\x11GetIndicesRequest\"D\n\x12GetIndicesResponse\x12.\n\x07indices\x18\x01 \x03(\x0b\x32\x1d.summa.proto.IndexDescription\"D\n\x1aIndexDocumentStreamRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x11\n\tdocuments\x18\x02 \x03(\x0c\"^\n\x1bIndexDocumentStreamResponse\x12\x14\n\x0csuccess_docs\x18\x01 \x01(\x04\x12\x13\n\x0b\x66\x61iled_docs\x18\x02 \x01(\x04\x12\x14\n\x0c\x65lapsed_secs\x18\x03 \x01(\x01\"=\n\x14IndexDocumentRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x10\n\x08\x64ocument\x18\x02 \x01(\x0c\"\x17\n\x15IndexDocumentResponse\"@\n\x14MergeSegmentsRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x13\n\x0bsegment_ids\x18\x02 \x03(\t\"\x17\n\x15MergeSegmentsResponse\"?\n\x14SetIndexAliasRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\"G\n\x15SetIndexAliasResponse\x12\x1b\n\x0eold_index_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x11\n\x0f_old_index_name\")\n\x12VacuumIndexRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\"\x15\n\x13VacuumIndexResponse\":\n\x12WarmupIndexRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x0f\n\x07is_full\x18\x02 \x01(\x08\"+\n\x13WarmupIndexResponse\x12\x14\n\x0c\x65lapsed_secs\x18\x01 \x01(\x01\" \n\x10\x46ileEngineConfig\x12\x0c\n\x04path\x18\x01 \x01(\t\"$\n\x12MemoryEngineConfig\x12\x0e\n\x06schema\x18\x01 \x01(\t\"P\n\x12\x43hunkedCacheConfig\x12\x12\n\nchunk_size\x18\x01 \x01(\x04\x12\x17\n\ncache_size\x18\x02 \x01(\x04H\x00\x88\x01\x01\x42\r\n\x0b_cache_size\"\x81\x02\n\x12RemoteEngineConfig\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x14\n\x0curl_template\x18\x02 \x01(\t\x12N\n\x10headers_template\x18\x03 \x03(\x0b\x32\x34.summa.proto.RemoteEngineConfig.HeadersTemplateEntry\x12=\n\x14\x63hunked_cache_config\x18\x04 \x01(\x0b\x32\x1f.summa.proto.ChunkedCacheConfig\x1a\x36\n\x14HeadersTemplateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"l\n\x10IpfsEngineConfig\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12=\n\x14\x63hunked_cache_config\x18\x02 \x01(\x0b\x32\x1f.summa.proto.ChunkedCacheConfig\x12\x0c\n\x04path\x18\x03 \x01(\t\"\xe1\x01\n\x11IndexEngineConfig\x12-\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x1d.summa.proto.FileEngineConfigH\x00\x12\x31\n\x06memory\x18\x02 \x01(\x0b\x32\x1f.summa.proto.MemoryEngineConfigH\x00\x12\x31\n\x06remote\x18\x03 \x01(\x0b\x32\x1f.summa.proto.RemoteEngineConfigH\x00\x12-\n\x04ipfs\x18\x04 \x01(\x0b\x32\x1d.summa.proto.IpfsEngineConfigH\x00\x42\x08\n\x06\x63onfig\"\xb4\x01\n\x10IndexDescription\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12\x15\n\rindex_aliases\x18\x02 \x03(\t\x12\x34\n\x0cindex_engine\x18\x03 \x01(\x0b\x32\x1e.summa.proto.IndexEngineConfig\x12\x10\n\x08num_docs\x18\x04 \x01(\x04\x12-\n\x0b\x63ompression\x18\x05 \x01(\x0e\x32\x18.summa.proto.Compression\"*\n\x16IndexDocumentOperation\x12\x10\n\x08\x64ocument\x18\x01 \x01(\x0c\"\\\n\x0eIndexOperation\x12=\n\x0eindex_document\x18\x02 \x01(\x0b\x32#.summa.proto.IndexDocumentOperationH\x00\x42\x0b\n\toperation*:\n\x18\x43reateIndexEngineRequest\x12\x08\n\x04\x46ile\x10\x00\x12\n\n\x06Memory\x10\x01\x12\x08\n\x04Ipfs\x10\x02*B\n\x0b\x43ompression\x12\x08\n\x04None\x10\x00\x12\n\n\x06\x42rotli\x10\x01\x12\x07\n\x03Lz4\x10\x02\x12\n\n\x06Snappy\x10\x03\x12\x08\n\x04Zstd\x10\x04*!\n\nCommitMode\x12\t\n\x05\x41sync\x10\x00\x12\x08\n\x04Sync\x10\x01\x32\xc6\n\n\x08IndexApi\x12S\n\x0c\x61ttach_index\x12\x1f.summa.proto.AttachIndexRequest\x1a .summa.proto.AttachIndexResponse\"\x00\x12S\n\x0c\x63ommit_index\x12\x1f.summa.proto.CommitIndexRequest\x1a .summa.proto.CommitIndexResponse\"\x00\x12S\n\x0c\x63reate_index\x12\x1f.summa.proto.CreateIndexRequest\x1a .summa.proto.CreateIndexResponse\"\x00\x12V\n\rmigrate_index\x12 .summa.proto.MigrateIndexRequest\x1a!.summa.proto.MigrateIndexResponse\"\x00\x12\\\n\x0f\x64\x65lete_document\x12\".summa.proto.DeleteDocumentRequest\x1a#.summa.proto.DeleteDocumentResponse\"\x00\x12S\n\x0c\x64\x65lete_index\x12\x1f.summa.proto.DeleteIndexRequest\x1a .summa.proto.DeleteIndexResponse\"\x00\x12\x66\n\x13get_indices_aliases\x12%.summa.proto.GetIndicesAliasesRequest\x1a&.summa.proto.GetIndicesAliasesResponse\"\x00\x12J\n\tget_index\x12\x1c.summa.proto.GetIndexRequest\x1a\x1d.summa.proto.GetIndexResponse\"\x00\x12P\n\x0bget_indices\x12\x1e.summa.proto.GetIndicesRequest\x1a\x1f.summa.proto.GetIndicesResponse\"\x00\x12n\n\x15index_document_stream\x12\'.summa.proto.IndexDocumentStreamRequest\x1a(.summa.proto.IndexDocumentStreamResponse\"\x00(\x01\x12Y\n\x0eindex_document\x12!.summa.proto.IndexDocumentRequest\x1a\".summa.proto.IndexDocumentResponse\"\x00\x12Y\n\x0emerge_segments\x12!.summa.proto.MergeSegmentsRequest\x1a\".summa.proto.MergeSegmentsResponse\"\x00\x12Z\n\x0fset_index_alias\x12!.summa.proto.SetIndexAliasRequest\x1a\".summa.proto.SetIndexAliasResponse\"\x00\x12S\n\x0cvacuum_index\x12\x1f.summa.proto.VacuumIndexRequest\x1a .summa.proto.VacuumIndexResponse\"\x00\x12S\n\x0cwarmup_index\x12\x1f.summa.proto.WarmupIndexRequest\x1a .summa.proto.WarmupIndexResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'index_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETINDICESALIASESRESPONSE_INDICESALIASESENTRY._options = None
  _GETINDICESALIASESRESPONSE_INDICESALIASESENTRY._serialized_options = b'8\001'
  _REMOTEENGINECONFIG_HEADERSTEMPLATEENTRY._options = None
  _REMOTEENGINECONFIG_HEADERSTEMPLATEENTRY._serialized_options = b'8\001'
  _CREATEINDEXENGINEREQUEST._serialized_start=3969
  _CREATEINDEXENGINEREQUEST._serialized_end=4027
  _COMPRESSION._serialized_start=4029
  _COMPRESSION._serialized_end=4095
  _COMMITMODE._serialized_start=4097
  _COMMITMODE._serialized_end=4130
  _PRIMARYKEY._serialized_start=49
  _PRIMARYKEY._serialized_end=100
  _ATTACHFILEENGINEREQUEST._serialized_start=102
  _ATTACHFILEENGINEREQUEST._serialized_end=127
  _ATTACHREMOTEENGINEREQUEST._serialized_start=129
  _ATTACHREMOTEENGINEREQUEST._serialized_end=156
  _ATTACHIPFSENGINEREQUEST._serialized_start=158
  _ATTACHIPFSENGINEREQUEST._serialized_end=196
  _ATTACHINDEXREQUEST._serialized_start=199
  _ATTACHINDEXREQUEST._serialized_end=482
  _ATTACHINDEXRESPONSE._serialized_start=484
  _ATTACHINDEXRESPONSE._serialized_end=551
  _COMMITINDEXREQUEST._serialized_start=553
  _COMMITINDEXREQUEST._serialized_end=640
  _COMMITINDEXRESPONSE._serialized_start=642
  _COMMITINDEXRESPONSE._serialized_end=707
  _MIGRATEINDEXREQUEST._serialized_start=710
  _MIGRATEINDEXREQUEST._serialized_end=853
  _MIGRATEINDEXRESPONSE._serialized_start=855
  _MIGRATEINDEXRESPONSE._serialized_end=923
  _SORTBYFIELD._serialized_start=925
  _SORTBYFIELD._serialized_end=988
  _INDEXATTRIBUTES._serialized_start=991
  _INDEXATTRIBUTES._serialized_end=1240
  _CREATEINDEXREQUEST._serialized_start=1243
  _CREATEINDEXREQUEST._serialized_end=1573
  _CREATEINDEXRESPONSE._serialized_start=1575
  _CREATEINDEXRESPONSE._serialized_end=1642
  _DELETEDOCUMENTREQUEST._serialized_start=1644
  _DELETEDOCUMENTREQUEST._serialized_end=1734
  _DELETEDOCUMENTRESPONSE._serialized_start=1736
  _DELETEDOCUMENTRESPONSE._serialized_end=1760
  _DELETEINDEXREQUEST._serialized_start=1762
  _DELETEINDEXREQUEST._serialized_end=1802
  _DELETEINDEXRESPONSE._serialized_start=1804
  _DELETEINDEXRESPONSE._serialized_end=1845
  _GETINDICESALIASESREQUEST._serialized_start=1847
  _GETINDICESALIASESREQUEST._serialized_end=1873
  _GETINDICESALIASESRESPONSE._serialized_start=1876
  _GETINDICESALIASESRESPONSE._serialized_end=2043
  _GETINDICESALIASESRESPONSE_INDICESALIASESENTRY._serialized_start=1990
  _GETINDICESALIASESRESPONSE_INDICESALIASESENTRY._serialized_end=2043
  _GETINDEXREQUEST._serialized_start=2045
  _GETINDEXREQUEST._serialized_end=2083
  _GETINDEXRESPONSE._serialized_start=2085
  _GETINDEXRESPONSE._serialized_end=2149
  _GETINDICESREQUEST._serialized_start=2151
  _GETINDICESREQUEST._serialized_end=2170
  _GETINDICESRESPONSE._serialized_start=2172
  _GETINDICESRESPONSE._serialized_end=2240
  _INDEXDOCUMENTSTREAMREQUEST._serialized_start=2242
  _INDEXDOCUMENTSTREAMREQUEST._serialized_end=2310
  _INDEXDOCUMENTSTREAMRESPONSE._serialized_start=2312
  _INDEXDOCUMENTSTREAMRESPONSE._serialized_end=2406
  _INDEXDOCUMENTREQUEST._serialized_start=2408
  _INDEXDOCUMENTREQUEST._serialized_end=2469
  _INDEXDOCUMENTRESPONSE._serialized_start=2471
  _INDEXDOCUMENTRESPONSE._serialized_end=2494
  _MERGESEGMENTSREQUEST._serialized_start=2496
  _MERGESEGMENTSREQUEST._serialized_end=2560
  _MERGESEGMENTSRESPONSE._serialized_start=2562
  _MERGESEGMENTSRESPONSE._serialized_end=2585
  _SETINDEXALIASREQUEST._serialized_start=2587
  _SETINDEXALIASREQUEST._serialized_end=2650
  _SETINDEXALIASRESPONSE._serialized_start=2652
  _SETINDEXALIASRESPONSE._serialized_end=2723
  _VACUUMINDEXREQUEST._serialized_start=2725
  _VACUUMINDEXREQUEST._serialized_end=2766
  _VACUUMINDEXRESPONSE._serialized_start=2768
  _VACUUMINDEXRESPONSE._serialized_end=2789
  _WARMUPINDEXREQUEST._serialized_start=2791
  _WARMUPINDEXREQUEST._serialized_end=2849
  _WARMUPINDEXRESPONSE._serialized_start=2851
  _WARMUPINDEXRESPONSE._serialized_end=2894
  _FILEENGINECONFIG._serialized_start=2896
  _FILEENGINECONFIG._serialized_end=2928
  _MEMORYENGINECONFIG._serialized_start=2930
  _MEMORYENGINECONFIG._serialized_end=2966
  _CHUNKEDCACHECONFIG._serialized_start=2968
  _CHUNKEDCACHECONFIG._serialized_end=3048
  _REMOTEENGINECONFIG._serialized_start=3051
  _REMOTEENGINECONFIG._serialized_end=3308
  _REMOTEENGINECONFIG_HEADERSTEMPLATEENTRY._serialized_start=3254
  _REMOTEENGINECONFIG_HEADERSTEMPLATEENTRY._serialized_end=3308
  _IPFSENGINECONFIG._serialized_start=3310
  _IPFSENGINECONFIG._serialized_end=3418
  _INDEXENGINECONFIG._serialized_start=3421
  _INDEXENGINECONFIG._serialized_end=3646
  _INDEXDESCRIPTION._serialized_start=3649
  _INDEXDESCRIPTION._serialized_end=3829
  _INDEXDOCUMENTOPERATION._serialized_start=3831
  _INDEXDOCUMENTOPERATION._serialized_end=3873
  _INDEXOPERATION._serialized_start=3875
  _INDEXOPERATION._serialized_end=3967
  _INDEXAPI._serialized_start=4133
  _INDEXAPI._serialized_end=5483
# @@protoc_insertion_point(module_scope)
