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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13index_service.proto\x12\x0bsumma.proto\x1a\x0butils.proto\"\xef\x02\n\x11\x41lterIndexRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12\x32\n\x0b\x63ompression\x18\x02 \x01(\x0e\x32\x18.summa.proto.CompressionH\x00\x88\x01\x01\x12\x16\n\tblocksize\x18\x06 \x01(\rH\x01\x88\x01\x01\x12\x34\n\rsort_by_field\x18\x03 \x01(\x0b\x32\x18.summa.proto.SortByFieldH\x02\x88\x01\x01\x12=\n\x0e\x64\x65\x66\x61ult_fields\x18\x04 \x01(\x0b\x32%.summa.proto.AlterIndexRequest.Fields\x12;\n\x0cmulti_fields\x18\x05 \x01(\x0b\x32%.summa.proto.AlterIndexRequest.Fields\x1a\x18\n\x06\x46ields\x12\x0e\n\x06\x66ields\x18\x01 \x03(\tB\x0e\n\x0c_compressionB\x0c\n\n_blocksizeB\x10\n\x0e_sort_by_field\"7\n\x12\x41lterIndexResponse\x12!\n\x05index\x18\x01 \x01(\x0b\x32\x12.summa.proto.Index\"(\n\x12\x41ttachIndexRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\"8\n\x13\x41ttachIndexResponse\x12!\n\x05index\x18\x01 \x01(\x0b\x32\x12.summa.proto.Index\"W\n\x12\x43ommitIndexRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12,\n\x0b\x63ommit_mode\x18\x02 \x01(\x0e\x32\x17.summa.proto.CommitMode\"c\n\x13\x43ommitIndexResponse\x12\x14\n\x07opstamp\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x19\n\x0c\x65lapsed_secs\x18\x02 \x01(\x01H\x01\x88\x01\x01\x42\n\n\x08_opstampB\x0f\n\r_elapsed_secs\"?\n\x0bSortByField\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12!\n\x05order\x18\x02 \x01(\x0e\x32\x12.summa.proto.Order\"\x8d\x04\n\x12\x43reateIndexRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12.\n\x0cindex_engine\x18\n \x01(\x0e\x32\x18.summa.proto.IndexEngine\x12\x18\n\x0bprimary_key\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x16\n\x0e\x64\x65\x66\x61ult_fields\x18\x04 \x03(\t\x12-\n\x0b\x63ompression\x18\x05 \x01(\x0e\x32\x18.summa.proto.Compression\x12\x16\n\tblocksize\x18\x0c \x01(\rH\x01\x88\x01\x01\x12#\n\x16writer_heap_size_bytes\x18\x06 \x01(\x04H\x02\x88\x01\x01\x12\x1b\n\x0ewriter_threads\x18\x07 \x01(\x04H\x03\x88\x01\x01\x12#\n\x16\x61utocommit_interval_ms\x18\x08 \x01(\x04H\x04\x88\x01\x01\x12\x34\n\rsort_by_field\x18\t \x01(\x0b\x32\x18.summa.proto.SortByFieldH\x05\x88\x01\x01\x12\x14\n\x0cmulti_fields\x18\x0b \x03(\tB\x0e\n\x0c_primary_keyB\x0c\n\n_blocksizeB\x19\n\x17_writer_heap_size_bytesB\x11\n\x0f_writer_threadsB\x19\n\x17_autocommit_interval_msB\x10\n\x0e_sort_by_field\"8\n\x13\x43reateIndexResponse\x12!\n\x05index\x18\x01 \x01(\x0b\x32\x12.summa.proto.Index\"A\n\x15\x44\x65leteDocumentRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x13\n\x0bprimary_key\x18\x02 \x01(\x03\":\n\x16\x44\x65leteDocumentResponse\x12\x14\n\x07opstamp\x18\x01 \x01(\x04H\x00\x88\x01\x01\x42\n\n\x08_opstamp\"(\n\x12\x44\x65leteIndexRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\"\x15\n\x13\x44\x65leteIndexResponse\"\x1a\n\x18GetIndicesAliasesRequest\"\xa7\x01\n\x19GetIndicesAliasesResponse\x12S\n\x0findices_aliases\x18\x01 \x03(\x0b\x32:.summa.proto.GetIndicesAliasesResponse.IndicesAliasesEntry\x1a\x35\n\x13IndicesAliasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"&\n\x0fGetIndexRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\"5\n\x10GetIndexResponse\x12!\n\x05index\x18\x01 \x01(\x0b\x32\x12.summa.proto.Index\"\x13\n\x11GetIndicesRequest\"9\n\x12GetIndicesResponse\x12#\n\x07indices\x18\x01 \x03(\x0b\x32\x12.summa.proto.Index\"D\n\x1aIndexDocumentStreamRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x11\n\tdocuments\x18\x02 \x03(\x0c\"^\n\x1bIndexDocumentStreamResponse\x12\x14\n\x0csuccess_docs\x18\x01 \x01(\x04\x12\x13\n\x0b\x66\x61iled_docs\x18\x02 \x01(\x04\x12\x14\n\x0c\x65lapsed_secs\x18\x03 \x01(\x01\"=\n\x14IndexDocumentRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x10\n\x08\x64ocument\x18\x02 \x01(\x0c\"(\n\x15IndexDocumentResponse\x12\x0f\n\x07opstamp\x18\x01 \x01(\x04\"@\n\x14MergeSegmentsRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x13\n\x0bsegment_ids\x18\x02 \x03(\t\"\x17\n\x15MergeSegmentsResponse\"?\n\x14SetIndexAliasRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\"G\n\x15SetIndexAliasResponse\x12\x1b\n\x0eold_index_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x11\n\x0f_old_index_name\")\n\x12VacuumIndexRequest\x12\x13\n\x0bindex_alias\x18\x01 \x01(\t\"\x15\n\x13VacuumIndexResponse\"\x89\x01\n\x05Index\x12\x12\n\nindex_name\x18\x01 \x01(\t\x12\x15\n\rindex_aliases\x18\x02 \x03(\t\x12\x14\n\x0cindex_engine\x18\x03 \x01(\t\x12\x10\n\x08num_docs\x18\x04 \x01(\x04\x12-\n\x0b\x63ompression\x18\x05 \x01(\x0e\x32\x18.summa.proto.Compression\"*\n\x16IndexDocumentOperation\x12\x10\n\x08\x64ocument\x18\x01 \x01(\x0c\"\\\n\x0eIndexOperation\x12=\n\x0eindex_document\x18\x02 \x01(\x0b\x32#.summa.proto.IndexDocumentOperationH\x00\x42\x0b\n\toperation*B\n\x0b\x43ompression\x12\x08\n\x04None\x10\x00\x12\n\n\x06\x42rotli\x10\x01\x12\x07\n\x03Lz4\x10\x02\x12\n\n\x06Snappy\x10\x03\x12\x08\n\x04Zstd\x10\x04*#\n\x0bIndexEngine\x12\x08\n\x04\x46ile\x10\x00\x12\n\n\x06Memory\x10\x01*!\n\nCommitMode\x12\t\n\x05\x41sync\x10\x00\x12\x08\n\x04Sync\x10\x01\x32\xeb\t\n\x08IndexApi\x12P\n\x0b\x61lter_index\x12\x1e.summa.proto.AlterIndexRequest\x1a\x1f.summa.proto.AlterIndexResponse\"\x00\x12S\n\x0c\x61ttach_index\x12\x1f.summa.proto.AttachIndexRequest\x1a .summa.proto.AttachIndexResponse\"\x00\x12S\n\x0c\x63ommit_index\x12\x1f.summa.proto.CommitIndexRequest\x1a .summa.proto.CommitIndexResponse\"\x00\x12S\n\x0c\x63reate_index\x12\x1f.summa.proto.CreateIndexRequest\x1a .summa.proto.CreateIndexResponse\"\x00\x12\\\n\x0f\x64\x65lete_document\x12\".summa.proto.DeleteDocumentRequest\x1a#.summa.proto.DeleteDocumentResponse\"\x00\x12S\n\x0c\x64\x65lete_index\x12\x1f.summa.proto.DeleteIndexRequest\x1a .summa.proto.DeleteIndexResponse\"\x00\x12\x66\n\x13get_indices_aliases\x12%.summa.proto.GetIndicesAliasesRequest\x1a&.summa.proto.GetIndicesAliasesResponse\"\x00\x12J\n\tget_index\x12\x1c.summa.proto.GetIndexRequest\x1a\x1d.summa.proto.GetIndexResponse\"\x00\x12P\n\x0bget_indices\x12\x1e.summa.proto.GetIndicesRequest\x1a\x1f.summa.proto.GetIndicesResponse\"\x00\x12n\n\x15index_document_stream\x12\'.summa.proto.IndexDocumentStreamRequest\x1a(.summa.proto.IndexDocumentStreamResponse\"\x00(\x01\x12Y\n\x0eindex_document\x12!.summa.proto.IndexDocumentRequest\x1a\".summa.proto.IndexDocumentResponse\"\x00\x12Y\n\x0emerge_segments\x12!.summa.proto.MergeSegmentsRequest\x1a\".summa.proto.MergeSegmentsResponse\"\x00\x12Z\n\x0fset_index_alias\x12!.summa.proto.SetIndexAliasRequest\x1a\".summa.proto.SetIndexAliasResponse\"\x00\x12S\n\x0cvacuum_index\x12\x1f.summa.proto.VacuumIndexRequest\x1a .summa.proto.VacuumIndexResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'index_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETINDICESALIASESRESPONSE_INDICESALIASESENTRY._options = None
  _GETINDICESALIASESRESPONSE_INDICESALIASESENTRY._serialized_options = b'8\001'
  _COMPRESSION._serialized_start=2826
  _COMPRESSION._serialized_end=2892
  _INDEXENGINE._serialized_start=2894
  _INDEXENGINE._serialized_end=2929
  _COMMITMODE._serialized_start=2931
  _COMMITMODE._serialized_end=2964
  _ALTERINDEXREQUEST._serialized_start=50
  _ALTERINDEXREQUEST._serialized_end=417
  _ALTERINDEXREQUEST_FIELDS._serialized_start=345
  _ALTERINDEXREQUEST_FIELDS._serialized_end=369
  _ALTERINDEXRESPONSE._serialized_start=419
  _ALTERINDEXRESPONSE._serialized_end=474
  _ATTACHINDEXREQUEST._serialized_start=476
  _ATTACHINDEXREQUEST._serialized_end=516
  _ATTACHINDEXRESPONSE._serialized_start=518
  _ATTACHINDEXRESPONSE._serialized_end=574
  _COMMITINDEXREQUEST._serialized_start=576
  _COMMITINDEXREQUEST._serialized_end=663
  _COMMITINDEXRESPONSE._serialized_start=665
  _COMMITINDEXRESPONSE._serialized_end=764
  _SORTBYFIELD._serialized_start=766
  _SORTBYFIELD._serialized_end=829
  _CREATEINDEXREQUEST._serialized_start=832
  _CREATEINDEXREQUEST._serialized_end=1357
  _CREATEINDEXRESPONSE._serialized_start=1359
  _CREATEINDEXRESPONSE._serialized_end=1415
  _DELETEDOCUMENTREQUEST._serialized_start=1417
  _DELETEDOCUMENTREQUEST._serialized_end=1482
  _DELETEDOCUMENTRESPONSE._serialized_start=1484
  _DELETEDOCUMENTRESPONSE._serialized_end=1542
  _DELETEINDEXREQUEST._serialized_start=1544
  _DELETEINDEXREQUEST._serialized_end=1584
  _DELETEINDEXRESPONSE._serialized_start=1586
  _DELETEINDEXRESPONSE._serialized_end=1607
  _GETINDICESALIASESREQUEST._serialized_start=1609
  _GETINDICESALIASESREQUEST._serialized_end=1635
  _GETINDICESALIASESRESPONSE._serialized_start=1638
  _GETINDICESALIASESRESPONSE._serialized_end=1805
  _GETINDICESALIASESRESPONSE_INDICESALIASESENTRY._serialized_start=1752
  _GETINDICESALIASESRESPONSE_INDICESALIASESENTRY._serialized_end=1805
  _GETINDEXREQUEST._serialized_start=1807
  _GETINDEXREQUEST._serialized_end=1845
  _GETINDEXRESPONSE._serialized_start=1847
  _GETINDEXRESPONSE._serialized_end=1900
  _GETINDICESREQUEST._serialized_start=1902
  _GETINDICESREQUEST._serialized_end=1921
  _GETINDICESRESPONSE._serialized_start=1923
  _GETINDICESRESPONSE._serialized_end=1980
  _INDEXDOCUMENTSTREAMREQUEST._serialized_start=1982
  _INDEXDOCUMENTSTREAMREQUEST._serialized_end=2050
  _INDEXDOCUMENTSTREAMRESPONSE._serialized_start=2052
  _INDEXDOCUMENTSTREAMRESPONSE._serialized_end=2146
  _INDEXDOCUMENTREQUEST._serialized_start=2148
  _INDEXDOCUMENTREQUEST._serialized_end=2209
  _INDEXDOCUMENTRESPONSE._serialized_start=2211
  _INDEXDOCUMENTRESPONSE._serialized_end=2251
  _MERGESEGMENTSREQUEST._serialized_start=2253
  _MERGESEGMENTSREQUEST._serialized_end=2317
  _MERGESEGMENTSRESPONSE._serialized_start=2319
  _MERGESEGMENTSRESPONSE._serialized_end=2342
  _SETINDEXALIASREQUEST._serialized_start=2344
  _SETINDEXALIASREQUEST._serialized_end=2407
  _SETINDEXALIASRESPONSE._serialized_start=2409
  _SETINDEXALIASRESPONSE._serialized_end=2480
  _VACUUMINDEXREQUEST._serialized_start=2482
  _VACUUMINDEXREQUEST._serialized_end=2523
  _VACUUMINDEXRESPONSE._serialized_start=2525
  _VACUUMINDEXRESPONSE._serialized_end=2546
  _INDEX._serialized_start=2549
  _INDEX._serialized_end=2686
  _INDEXDOCUMENTOPERATION._serialized_start=2688
  _INDEXDOCUMENTOPERATION._serialized_end=2730
  _INDEXOPERATION._serialized_start=2732
  _INDEXOPERATION._serialized_end=2824
  _INDEXAPI._serialized_start=2967
  _INDEXAPI._serialized_end=4226
# @@protoc_insertion_point(module_scope)
