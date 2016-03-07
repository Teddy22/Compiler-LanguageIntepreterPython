from enum import Enum


class TokenType(Enum):

    MAIN_TOK = 1
    LEFT_PAREN_TOK = 2
    RIGHT_PAREN_TOK = 3
    EOL_TOK = 4
    INDENT_TOK = 5
    DEDENT_TOK = 6
    IF_TOK = 7
    COLON_TOK = 8
    ELSE_TOK = 9
    EL_IF_TOK = 10
    WHILE_TOK = 11
    ID_TOK = 12
    PRINT_TOK = 13
    CONST_TOK = 14
    GE_TOK = 15
    GT_TOK = 16
    LE_TOK = 17
    LT_TOK = 18
    EQ_TOK = 19
    NE_TOK = 20
    ADD_TOK = 21
    SUB_TOK = 22
    MUL_TOK = 23
    DIV_TOK = 24
    ASSIGN_TOK = 25
    EOS_TOK = 26

