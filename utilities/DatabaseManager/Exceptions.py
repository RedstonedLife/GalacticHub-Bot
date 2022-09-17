from .Column import Column
from .Constraint import Constraint
from .Datatype import Datatype
from .Base import Base


class DatatypeCannotBeNone(Exception):
    def __init__(self, column: Column, *args):
        super().__init__(args)
        self.column = column

    def __str__(self):
        return f'The datatype of column.{self.column.n} cannot be NULL or NONE'


class NameCannotBeNone(Exception):
    def __init__(self, o: Base, *args):
        super().__init__(args)
        self.o = o

    def __str__(self):
        return f'The datatype of {self.o.__name__()} cannot be NULL or NONE'
