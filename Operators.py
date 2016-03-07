from enum import Enum


class ArithmeticOperator(Enum):
    ADD_OP = 1
    SUB_OP = 2
    MUL_OP = 3
    DIV_OP = 4


class RelationalOperator(Enum):
    EQ_OP = 1
    NE_OP = 2
    LT_OP = 3
    LE_OP = 4
    GT_OP = 5
    GE_OP = 6