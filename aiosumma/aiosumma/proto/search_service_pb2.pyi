from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import query_pb2 as _query_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class SearchRequest(_message.Message):
    __slots__ = ["collectors", "index_alias", "query", "tags"]
    class TagsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COLLECTORS_FIELD_NUMBER: _ClassVar[int]
    INDEX_ALIAS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    collectors: _containers.RepeatedCompositeFieldContainer[_query_pb2.Collector]
    index_alias: str
    query: _query_pb2.Query
    tags: _containers.ScalarMap[str, str]
    def __init__(self, index_alias: _Optional[str] = ..., query: _Optional[_Union[_query_pb2.Query, _Mapping]] = ..., collectors: _Optional[_Iterable[_Union[_query_pb2.Collector, _Mapping]]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...
