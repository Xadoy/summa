from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Consumer(_message.Message):
    __slots__ = ["consumer_name", "index_name"]
    CONSUMER_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    consumer_name: str
    index_name: str
    def __init__(self, consumer_name: _Optional[str] = ..., index_name: _Optional[str] = ...) -> None: ...

class CreateConsumerRequest(_message.Message):
    __slots__ = ["bootstrap_servers", "consumer_name", "group_id", "index_name", "topics"]
    BOOTSTRAP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    bootstrap_servers: _containers.RepeatedScalarFieldContainer[str]
    consumer_name: str
    group_id: str
    index_name: str
    topics: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, bootstrap_servers: _Optional[_Iterable[str]] = ..., group_id: _Optional[str] = ..., index_name: _Optional[str] = ..., consumer_name: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateConsumerResponse(_message.Message):
    __slots__ = ["consumer"]
    CONSUMER_FIELD_NUMBER: _ClassVar[int]
    consumer: Consumer
    def __init__(self, consumer: _Optional[_Union[Consumer, _Mapping]] = ...) -> None: ...

class DeleteConsumerRequest(_message.Message):
    __slots__ = ["consumer_name"]
    CONSUMER_NAME_FIELD_NUMBER: _ClassVar[int]
    consumer_name: str
    def __init__(self, consumer_name: _Optional[str] = ...) -> None: ...

class DeleteConsumerResponse(_message.Message):
    __slots__ = ["consumer_name"]
    CONSUMER_NAME_FIELD_NUMBER: _ClassVar[int]
    consumer_name: str
    def __init__(self, consumer_name: _Optional[str] = ...) -> None: ...

class GetConsumerRequest(_message.Message):
    __slots__ = ["consumer_name", "index_alias"]
    CONSUMER_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_ALIAS_FIELD_NUMBER: _ClassVar[int]
    consumer_name: str
    index_alias: str
    def __init__(self, index_alias: _Optional[str] = ..., consumer_name: _Optional[str] = ...) -> None: ...

class GetConsumerResponse(_message.Message):
    __slots__ = ["consumer"]
    CONSUMER_FIELD_NUMBER: _ClassVar[int]
    consumer: Consumer
    def __init__(self, consumer: _Optional[_Union[Consumer, _Mapping]] = ...) -> None: ...

class GetConsumersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetConsumersResponse(_message.Message):
    __slots__ = ["consumers"]
    CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    consumers: _containers.RepeatedCompositeFieldContainer[Consumer]
    def __init__(self, consumers: _Optional[_Iterable[_Union[Consumer, _Mapping]]] = ...) -> None: ...
