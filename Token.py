from TokenType import TokenType
from Interface_mod import NullException
from Interface_mod import IllegalArgumentError

class Token():

    def __init__(self, tok_type, lexeme, row_number, column_number):

        if tok_type is None:
            raise NullException('null TokenType argument at Token')
        if row_number is None:
            raise NullException('null row number argument at Token')
        if column_number is None:
            raise NullException('null column number argument at Token')
        if lexeme is None:
            raise NullException('null lexeme argument at Token')
        if not isinstance(tok_type, TokenType):
            raise TypeError('invalid type for token type argument at Token')
        if not isinstance(lexeme, str):
            raise TypeError('invalid type lexeme argument at Token')
        if not isinstance(row_number, int):
            raise TypeError('invalid argument for row number argument at Token')
        if not isinstance(column_number, int):
            raise TypeError('invalid type for column number argument at Token')
        if len(lexeme) < 1:
            raise IllegalArgumentError('invalid value for length of lexeme string argument at Token')

        self.tok_type = tok_type
        self.row_num = row_number
        self.column_num = column_number
        self.lexeme = lexeme

    def get_tok_type(self):
        return self.tok_type

    def get_lexeme(self):
        return self.lexeme

    def get_row_num(self):
        return self.row_num

    def get_column_num(self):
        return self.column_num