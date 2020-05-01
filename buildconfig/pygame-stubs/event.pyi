from typing import Any, Dict, List, Optional, Union, overload

class EventType(object):
    type: int
    __dict__: Dict[str, Any]
    @overload
    def __init__(self, type: int, dict: Dict[str, Any]) -> None: ...
    @overload
    def __init__(self, type: int, **attributes: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

# Event is actually a function that returns an EventType, but it's often used
# as an annotation.
Event = EventType

_EventIds = Union[int, List[int]]

def pump() -> None: ...
def get(type: _EventIds = ...) -> List[EventType]: ...
def poll() -> EventType: ...
def wait() -> EventType: ...
def peak(type: _EventIds) -> bool: ...
def clear(type: _EventIds = ...) -> None: ...
def event_name(type: int) -> str: ...
def set_blocked(type: Optional[_EventIds]) -> None: ...
def set_allowed(type: Optional[_EventIds]) -> None: ...
def get_blocked(type: int) -> bool: ...
def set_grab(grab: bool) -> None: ...
def get_grab() -> bool: ...
def post(event: EventType) -> None: ...
def custom_type() -> int: ...
