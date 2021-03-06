# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.PlayerPath_pb2 import (
    PlayerPath as pyatv___mrp___protobuf___PlayerPath_pb2___PlayerPath,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class SendError(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Enum(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'SendError.Enum': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['SendError.Enum']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SendError.Enum']]: ...
        NoError = typing___cast('SendError.Enum', 0)
        ApplicationNotFound = typing___cast('SendError.Enum', 1)
        ConnectionFailed = typing___cast('SendError.Enum', 2)
        Ignored = typing___cast('SendError.Enum', 3)
        CouldNotLaunchApplication = typing___cast('SendError.Enum', 4)
        TimedOut = typing___cast('SendError.Enum', 5)
        OriginDoesNotExist = typing___cast('SendError.Enum', 6)
        InvalidOptions = typing___cast('SendError.Enum', 7)
        NoCommandHandlers = typing___cast('SendError.Enum', 8)
        ApplicationNotInstalled = typing___cast('SendError.Enum', 9)
    NoError = typing___cast('SendError.Enum', 0)
    ApplicationNotFound = typing___cast('SendError.Enum', 1)
    ConnectionFailed = typing___cast('SendError.Enum', 2)
    Ignored = typing___cast('SendError.Enum', 3)
    CouldNotLaunchApplication = typing___cast('SendError.Enum', 4)
    TimedOut = typing___cast('SendError.Enum', 5)
    OriginDoesNotExist = typing___cast('SendError.Enum', 6)
    InvalidOptions = typing___cast('SendError.Enum', 7)
    NoCommandHandlers = typing___cast('SendError.Enum', 8)
    ApplicationNotInstalled = typing___cast('SendError.Enum', 9)
    global___Enum = Enum


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SendError: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SendError: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___SendError = SendError

class HandlerReturnStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Enum(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'HandlerReturnStatus.Enum': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['HandlerReturnStatus.Enum']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'HandlerReturnStatus.Enum']]: ...
        Success = typing___cast('HandlerReturnStatus.Enum', 0)
        NoSuchContent = typing___cast('HandlerReturnStatus.Enum', 1)
        CommandFailed = typing___cast('HandlerReturnStatus.Enum', 2)
        NoActionableNowPlayingItem = typing___cast('HandlerReturnStatus.Enum', 10)
        DeviceNotFound = typing___cast('HandlerReturnStatus.Enum', 20)
        UIKitLegacy = typing___cast('HandlerReturnStatus.Enum', 3)
        SkipAdProhibited = typing___cast('HandlerReturnStatus.Enum', 100)
        QueueIsUserCurated = typing___cast('HandlerReturnStatus.Enum', 101)
        UserModifiedQueueDisabled = typing___cast('HandlerReturnStatus.Enum', 102)
        UserQueueModificationNotSupportedForCurrentItem = typing___cast('HandlerReturnStatus.Enum', 103)
        SubscriptionRequiredForSharedQueue = typing___cast('HandlerReturnStatus.Enum', 104)
    Success = typing___cast('HandlerReturnStatus.Enum', 0)
    NoSuchContent = typing___cast('HandlerReturnStatus.Enum', 1)
    CommandFailed = typing___cast('HandlerReturnStatus.Enum', 2)
    NoActionableNowPlayingItem = typing___cast('HandlerReturnStatus.Enum', 10)
    DeviceNotFound = typing___cast('HandlerReturnStatus.Enum', 20)
    UIKitLegacy = typing___cast('HandlerReturnStatus.Enum', 3)
    SkipAdProhibited = typing___cast('HandlerReturnStatus.Enum', 100)
    QueueIsUserCurated = typing___cast('HandlerReturnStatus.Enum', 101)
    UserModifiedQueueDisabled = typing___cast('HandlerReturnStatus.Enum', 102)
    UserQueueModificationNotSupportedForCurrentItem = typing___cast('HandlerReturnStatus.Enum', 103)
    SubscriptionRequiredForSharedQueue = typing___cast('HandlerReturnStatus.Enum', 104)
    global___Enum = Enum


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> HandlerReturnStatus: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HandlerReturnStatus: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___HandlerReturnStatus = HandlerReturnStatus

class SendCommandResultMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    sendError = ... # type: global___SendError.Enum
    handlerReturnStatus = ... # type: global___HandlerReturnStatus.Enum
    handlerReturnStatusDatas = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes]
    commandID = ... # type: typing___Text

    @property
    def playerPath(self) -> pyatv___mrp___protobuf___PlayerPath_pb2___PlayerPath: ...

    def __init__(self,
        *,
        sendError : typing___Optional[global___SendError.Enum] = None,
        handlerReturnStatus : typing___Optional[global___HandlerReturnStatus.Enum] = None,
        handlerReturnStatusDatas : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        commandID : typing___Optional[typing___Text] = None,
        playerPath : typing___Optional[pyatv___mrp___protobuf___PlayerPath_pb2___PlayerPath] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SendCommandResultMessage: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SendCommandResultMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"commandID",b"commandID",u"handlerReturnStatus",b"handlerReturnStatus",u"playerPath",b"playerPath",u"sendError",b"sendError"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"commandID",b"commandID",u"handlerReturnStatus",b"handlerReturnStatus",u"handlerReturnStatusDatas",b"handlerReturnStatusDatas",u"playerPath",b"playerPath",u"sendError",b"sendError"]) -> None: ...
global___SendCommandResultMessage = SendCommandResultMessage

sendCommandResultMessage = ... # type: google___protobuf___descriptor___FieldDescriptor
