from Token import Token
from TokenType import TokenType
from Interface_mod import LexicalException


class LexicalAnalyzer:

    def __init__(self, file_name):
        self.tokens = []

        try:
            file = open(file_name)
        except Exception as e:
            raise LexicalException('error opening file at - ' + str(e))

        line_num = 0
        indentation = 0

        for line in iter(file):
            line_num += 1

            num_tabs = self.find_num_preceding_tabs(line)

            if num_tabs > indentation:
                for i in range(0, num_tabs-indentation):
                    self.tokens.append(Token(TokenType.INDENT_TOK, 'indent', line_num, i+1))
                indentation = num_tabs

            elif indentation > num_tabs:
                for i in range(0, indentation-num_tabs):
                    self.tokens.append(Token(TokenType.DEDENT_TOK, 'dedent', line_num, i+1))
                indentation = num_tabs

            self.process_line(line, line_num, num_tabs)

        for i in range(0, indentation):
            self.tokens.append(Token(TokenType.DEDENT_TOK, 'dedent', line_num, i+1))

        self.tokens.append(Token(TokenType.EOS_TOK, 'eos', line_num+1, 1))

        file.close()

    def find_num_preceding_tabs(self, line):
        if line is None:
            raise LexicalException('null line argument at LexicalAnalyzer')
        if not isinstance(line, str):
            raise LexicalException('invalid type for file line argument at LexicalAnalyzer')
        if len(line) < 1:
            raise LexicalException('non-positive value for length of file line at LexicalAnalyzer')

        num = 0
        while num < len(line) and line[num] == '\t':
                num += 1

        return num

    def process_line(self, line, line_num, num_tabs):
        if line is None:
            raise LexicalException('null file line argument at ')
        if line_num is None:
            raise LexicalException('null file line number argument at ')
        if num_tabs is None:
            raise LexicalException('null number of tabs argument at ')
        if not isinstance(line, str):
            raise LexicalException('invalid type for file line string at ')
        if not isinstance(line_num, int):
            raise LexicalException('invalid type for file line number at ')
        if not isinstance(num_tabs, int):
            raise LexicalException('invalid type for number of tabs at ')
        if line_num <= 0:
            raise LexicalException('non-positive value for file line number( ' + str(line_num) + ')')
        if num_tabs < 0:
            raise LexicalException('negative value for number of tabs value( ' + str(num_tabs) + ')')
        if len(line) == 0:
            raise LexicalException('non-positive number for length of file line at line number ' + str(line_num))

        index = self.skip_white_space(line, num_tabs)

        while index < len(line):
            lexeme = self.get_next_lexeme(line, index)
            tok_type = self.get_lexeme_type(lexeme, line_num, index)
            self.tokens.append(Token(tok_type, lexeme, line_num, index+1))
            index += len(lexeme)
            index = self.skip_white_space(line, index)

        self.tokens.append(Token(TokenType.EOL_TOK, 'eol', line_num, index+1))

    def skip_white_space(self, line, index):
        while index < len(line) and line[index].isspace():
            index += 1

        return index

    def get_next_lexeme(self, line, index):
        if index is None:
            raise LexicalException('null index argument at ')
        if not isinstance(index, int):
            raise LexicalException('invalid type for index argument at ')
        if index < 0:
            raise LexicalException('non-positive value for the index argument(' + str(index) + ')')
        i = index

        while i < len(line) and not line[i].isspace():
            i += 1

        return line[index:i]

    def get_lexeme_type(self, lexeme, line_num, index):
        if lexeme is None:
            raise LexicalException('null lexeme argument at LexicalAnalyzer')
        if not isinstance(lexeme, str):
            raise LexicalException('invalid type argument for lexeme at LexicalAnalyzer')
        if len(lexeme) <= 0:
            raise LexicalException('non-positive length value for lexeme argument at LexicalAnalyzer')

        tok_type = TokenType.EOS_TOK

        if lexeme[0].isalpha():

            if len(lexeme) == 1:
                tok_type = TokenType.ID_TOK
            elif lexeme == 'main':
                tok_type = TokenType.MAIN_TOK
            elif lexeme == 'if':
                tok_type = TokenType.IF_TOK
            elif lexeme == 'else':
                tok_type = TokenType.ELSE_TOK
            elif lexeme == 'elif':
                tok_type = TokenType.EL_IF_TOK
            elif lexeme == 'while':
                tok_type = TokenType.WHILE_TOK
            elif lexeme == 'print':
                tok_type = TokenType.PRINT_TOK
            else:
                raise LexicalException('no reserved word found at line ' + str(line_num) +
                                       ' column number ' + str(index+1))
        elif lexeme[0].isnumeric():
            if lexeme.isnumeric():
                tok_type = TokenType.CONST_TOK
            else:
                raise LexicalException('literal integer expected at line ' + str(line_num) +
                                       ' column number ' + str(index+1))

        elif lexeme == '(':
            tok_type = TokenType.LEFT_PAREN_TOK
        elif lexeme == ')':
            tok_type = TokenType.RIGHT_PAREN_TOK
        elif lexeme == ':':
            tok_type = TokenType.COLON_TOK
        elif lexeme == '==':
            tok_type = TokenType.EQ_TOK
        elif lexeme == '!=':
            tok_type = TokenType.NE_TOK
        elif lexeme == '<':
            tok_type = TokenType.LT_TOK
        elif lexeme == '<=':
            tok_type = TokenType.LE_TOK
        elif lexeme == '>':
            tok_type = TokenType.GT_TOK
        elif lexeme == '>=':
            tok_type = TokenType.GE_TOK
        elif lexeme == '+':
            tok_type = TokenType.ADD_TOK
        elif lexeme == '-':
            tok_type = TokenType.ADD_TOK
        elif lexeme == '*':
            tok_type = TokenType.MUL_TOK
        elif lexeme == '/':
            tok_type = TokenType.DIV_TOK
        elif lexeme == '=':
            tok_type = TokenType.ASSIGN_TOK
        else:
            raise LexicalException('invalid lexeme at line ' + str(line_num) +
                                   ' column number ' + str(index+1))

        return tok_type

    def get_look_ahead_token(self):
        if len(self.tokens) == 0:
            raise LexicalException('no more tokens')

        return self.tokens[0]

    def get_next_token(self):
        if len(self.tokens) == 0:
            raise LexicalException('no more tokens')

        return self.tokens.pop(0)

