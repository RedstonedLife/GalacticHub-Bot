from .Datatype import Datatype
from .Constraint import Constraint
from .Base import Base


class Column(Base):
    __slots__ = ("n", "dt", "cts", "kwgs")

    def __init__(self, name: str = None, datatype: Datatype = None, *constraints: Constraint, **kwargs):
        """
        Column class is a building block of the Table class a table must consist of some columns at least 1
        the parameters that Column intakes are quite simple, the name is the name of the column,
        datatype is the data type of the column whether it'd be INT, STRING, BLOB, or NUMERIC.
        Constraints are a bit more interesting, you can have multiple constraints, although some might conflict with
        each other, If you have the UNIQUE constraint, and you say that the DEFAULT is NULL, It will throw an error
        before creating the table.
        The kwargs are simple too!, If you have the DEFAULT constraint you must add defualt=PARAMETER.
        otherwise by default it will be Type.NULL

        :param name: Name of the column (String)
        :param datatype: Data Type (Datatype Object)
        :param constraints: List of Constraints
        :param kwargs: Additions to constraints
        """
        self.n = name
        self.dt = datatype
        self.cts = constraints
        self.kwgs = kwargs

    def __name__(self) -> str: return "column"
