from .Datatype import Datatype
from .Constraint import Constraint
from .Base import Base


class Column(Base):
    __slots__ = ("n", "dt", "cts")

    def __init__(self, n: str, dt: Datatype = None, *cts: Constraint):
        self.n = n
        self.dt = dt
        self.cts = cts

    def __name__(self) -> str: return "column"
