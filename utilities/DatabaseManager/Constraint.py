from enum import Enum


class Constraint(Enum):
    UNIQUE = "UNIQUE"
    N_NULL = "NOT NULL"
    P_KEY = "PRIMARY KEY"
    F_KEY = "FOREIGN KEY"
    CHECK = "CHECK"
    DEFAULT = "DEFAULT"