# Basic type system to enable query validation
from typing import Generic, TypeVar, Callable

# Type bounded within the base class
T = TypeVar("T", bound='Callable')

class CType(Generic[T]):
    """
    Base class for all column types in the system
    """
    DEF_ENCODING = 'utf-8'
    def __init__(self, b: bytes) -> None:
        self.b = b
    def val(self) -> T:
        "this needs to be defined for all types"
        pass

class IntType(CType[int]):
    """
    Integer type
    """
    def val(self) -> int:
        return int(self.b)

class StringType(CType[str]):
    """
    Immutable String type
    """
    def val(self) -> str:
        return self.b.decode(CType.DEF_ENCODING)

class BoolType(CType[bool]):
    """
    Boolean or short integer type
    """
    def val(self) -> bool:
        return bool(self.b)
