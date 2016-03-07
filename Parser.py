from LexicalAnalyzer import LexicalAnalyzer
from Interface_mod import ParserException
from Program import Program
from TokenType import TokenType
from Token import Token
from StatementBlock import StatementBlock
from StatementList import StatementList
from PrintStatement import PrintStatement
from BinaryExpression import BinaryExpression
from Operators import ArithmeticOperator
from Id import Id
from LiteralConstant import LiteralConstant
from IfStatement import IfStatement
from BooleanExpression import BooleanExpression
from Operators import RelationalOperator
from WhileStatement import WhileStatement
from AssignmentStatement import AssignmentStatement
from Interface_mod import LexicalException
from Interface_mod import NullException
import sys



class Parser:

    def __init__(self, file_name):
        if not isinstance(file_name, str):
            raise ParserException('null file name argument')

        self.lex = LexicalAnalyzer(file_name)

    def parse(self):

        token = self.get_next_token()
        self.match(token, TokenType.MAIN_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.LEFT_PAREN_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.RIGHT_PAREN_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.EOL_TOK)

        block = self.get_statement_block()
        token = self.get_next_token()

        if token.get_tok_type() != TokenType.EOS_TOK:
            raise ParserException('garbage at end of file')

        return Program(block)

    def get_statement_block(self):
        token = self.get_next_token()
        self.match(token, TokenType.INDENT_TOK)

        statements = self.get_statement_list()

        token = self.get_next_token()
        self.match(token, TokenType.DEDENT_TOK)

        return StatementBlock(statements)

    def get_statement_list(self):
        statements = StatementList()
        statement = self.get_statement()
        statements.add(statement)
        token = self.get_look_ahead_token()

        while self.is_valid_start_of_stream(token):
            statement = self.get_statement()
            statements.add(statement)
            token = self.get_look_ahead_token()

        return statements

    def get_statement(self):
        statement = None
        token = self.get_look_ahead_token()

        if token.get_tok_type() == TokenType.PRINT_TOK:
            statement = self.get_print_statement()
        elif token.get_tok_type() == TokenType.IF_TOK:
            statement = self.get_if_statement()
        elif token.get_tok_type() == TokenType.WHILE_TOK:
            statement = self.get_while_statement()
        else:
            statement = self.get_assignment_statement()

        return statement

    def get_print_statement(self):

        token = self.get_next_token()
        self.match(token, TokenType.PRINT_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.LEFT_PAREN_TOK)

        expr = self.get_arithmetic_expression()

        token = self.get_next_token()
        self.match(token, TokenType.RIGHT_PAREN_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.EOL_TOK)

        return PrintStatement(expr)

    def get_arithmetic_expression(self):
        token = self.get_look_ahead_token()

        if token.get_tok_type() == TokenType.ID_TOK:
            expr = self.get_id()
        elif token.get_tok_type() == TokenType.CONST_TOK:
            expr = self.get_literal_constant()
        else:
            operator = self.get_arithmetic_operator()
            expr1 = self.get_arithmetic_expression()
            expr2 = self.get_arithmetic_expression()
            expr = BinaryExpression(operator, expr1, expr2)

        return expr

    def get_arithmetic_operator(self):
        operator = None
        token = self.get_next_token()

        if token.get_tok_type() == TokenType.ADD_TOK:
            operator = ArithmeticOperator.ADD_OP
        elif token.get_tok_type() == TokenType.SUB_TOK:
            operator = ArithmeticOperator.SUB_OP
        elif token.get_tok_type() == TokenType.MUL_TOK:
            operator = ArithmeticOperator.MUL_OP
        elif token.get_tok_type() == TokenType.DIV_TOK:
            operator = ArithmeticOperator.DIV_OP
        else:
            raise ParserException('arithmetic operator expected at row number '
                                   + str(token.get_row_num()) + ' column number '
                                   + str(token.get_column_num()))

        return operator

    def get_arithmetic_expression(self):

        expr = None
        token = self.get_look_ahead_token()

        if token.get_tok_type() == TokenType.ID_TOK:
            expr = self.get_id()
        elif token.get_tok_type() == TokenType.CONST_TOK:
            expr = self.get_literal_constant()
        else:
            operator = self.get_arithmetic_operator()
            expr1 = self.get_arithmetic_expression()
            expr2 = self.get_arithmetic_expression()
            expr = BinaryExpression(operator, expr1, expr2)

        return expr

'''
has already been implemented!
'''

    def get_id(self):
        token = self.get_next_token()
        self.match(token, TokenType.ID_TOK)
        return Id(token.get_lexeme())

    def get_literal_constant(self):
        token = self.get_next_token()
        self.match(token, TokenType.CONST_TOK)
        value = token.get_lexeme()

        return LiteralConstant(int(value))

    def get_if_statement(self):
        if_statement = IfStatement()

        token = self.get_next_token()
        self.match(token, TokenType.IF_TOK)

        expr = self.get_boolean_expression()
        if_statement.add_expression(expr)

        token = self.get_next_token()
        self.match(token, TokenType.COLON_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.EOL_TOK)

        block = self.get_statement_block()
        if_statement.add_block(block)

        token = self.get_next_token()

        while token.get_tok_type() == TokenType.EL_IF_TOK:

            self.match(token, TokenType.EL_IF_TOK)
            expr = self.get_boolean_expression()

            if_statement.add_expression(expr)

            token = self.get_next_token()
            self.match(token, TokenType.COLON_TOK)

            token = self.get_next_token()
            self.match(token, TokenType.EOL_TOK)

            block = self.get_statement_block()
            if_statement.add_block(block)

            token = self.get_next_token()

        self.match(token, TokenType.ELSE_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.COLON_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.EOL_TOK)

        block = self.get_statement_block()
        if_statement.add_block(block)

        return if_statement

    def get_boolean_expression(self):

        operator = self.get_relational_operator()
        expr1 = self.get_arithmetic_expression()
        exp2 = self.get_arithmetic_expression()

        return BooleanExpression(operator, expr1, exp2)

    def get_relational_operator(self):
        operator = None

        token = self.get_next_token()

        if token.get_tok_type() == TokenType.EQ_TOK:
            operator = RelationalOperator.EQ_OP
        elif token.get_tok_type() == TokenType.NE_TOK:
            operator = RelationalOperator.NE_OP
        elif token.get_tok_type() == TokenType.LT_TOK:
            operator = RelationalOperator.LT_OP
        elif token.get_tok_type() == TokenType.LE_TOK:
            operator = RelationalOperator.LE_OP
        elif token.get_tok_type() == TokenType.GT_TOK:
            operator = RelationalOperator.GT_OP
        elif token.get_tok_type() == TokenType.GE_TOK:
            operator = RelationalOperator.GE_OP
        else:
            raise ParserException('relational operator expected at row '
                                  + str(token.get_row_num()) + ' and column '
                                  + str(token.get_column_num()))

        return operator

    def get_while_statement(self):

        token = self.get_next_token()
        self.match(token,TokenType.WHILE_TOK)

        expr = self.get_boolean_expression()

        token = self.get_next_token()
        self.match(token, TokenType.COLON_TOK)

        token = self.get_next_token()
        self.match(token, TokenType.EOL_TOK)

        block = self.get_statement_block()

        return WhileStatement(expr, block)

    def get_assignment_statement(self):
        var = self.get_id()

        token = self.get_next_token()
        self.match(token, TokenType.ASSIGN_TOK)

        expr = self.get_arithmetic_expression()

        token = self.get_next_token()
        self.match(token, TokenType.EOL_TOK)

        return AssignmentStatement(var, expr)

    def get_next_token(self):

        token = None

        try:
            token = self.lex.get_next_token()
        except LexicalException as e:
            raise ParserException('no more tokens - ' + e)
        return token

    def get_look_ahead_token(self):

        token = None

        try:
            token = self.lex.get_look_ahead_token()
        except LexicalException as e:
            raise ParserException('no more tokens - ' + e)

        return token

    def is_valid_start_of_stream(self, token):
        if token is None:
            raise NullException('null token argument at ' + self.__name__)
        if not isinstance(token, Token):
            raise TypeError('invalid type for token argument at ' + self.__name__)

        return (token.get_tok_type() == TokenType.PRINT_TOK
                or token.get_tok_type() == TokenType.ID_TOK
                or token.get_tok_type() == TokenType.WHILE_TOK
                or token.get_tok_type() == TokenType.IF_TOK)

    def match(self, token, tok_type):

        if token is None:
            raise NullException('null token argument at ' + self.__name__)
        if tok_type is None:
            raise NullException('null token type argument at ' + self.__name__)
        if not isinstance(token, Token):
            raise TypeError('invalid type for token argument at ' + self.__name__)
        if not isinstance(tok_type, TokenType):
            raise TypeError('invalid type for token type argument at ' + self.__name__)

        if token.get_tok_type() != tok_type:
            raise ParserException(tok_type.name + ' expected at row '
                                  + str(token.get_row_num()) + ' and column '
                                  + str(token.get_column_num()))
