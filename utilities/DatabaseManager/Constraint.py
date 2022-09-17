from enum import Enum


class Constraint(Enum):
    UNIQUE = "UNIQUE"
    NNULL = "NOT NULL"
    PKEY = "PRIMARY KEY"
    FKEY = "FOREIGN KEY"
    CHECK = "CHECK"
    DEFAULT = "DEFAULT"