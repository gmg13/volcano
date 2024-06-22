from typing import Generator

from common.types import CType

# All the base classes
# -------------------
class Operator:
    def __init__(self, args, inp, state) -> None:
        # all the variable needed to define an operator
        self.args = args
        self.inp = inp
        self.state = state

class Iterator:
    def __init__(self, op: Operator) -> None:
        self.op = op
    def open(self) -> None:
        pass
    def close(self) -> None:
        pass
    def next(self) -> Generator[CType, None, None]:
        pass
# -------------------