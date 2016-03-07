from Interface_mod import Statement
from Interface_mod import NullException
from BooleanExpression import BooleanExpression
from StatementBlock import StatementBlock


class WhileStatement(Statement):

    def __init__(self, expr, block):
        if expr is None:
            raise NullException('null expression argument at ' + self.__name__)
        if block is None:
            raise NullException('null statement block argument at ' + self.__name__)
        if not isinstance(expr, BooleanExpression):
            raise TypeError('invalid type of argument for boolean expression argument at ' + self.__name__)
        if not isinstance(block, StatementBlock):
            raise TypeError('invalid type of argument for statement block at ' + self.__name__)

        self.expr = expr
        self.block = block

    def execute(self):
        while self.expr.evaluate():
            self.block.execute()