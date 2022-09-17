from .Column import Column
from .Base import Base


class Table(Base):
    __slots__ = ("n", "dt", "cts", "kwgs")
    def __name__(self): return "table"
