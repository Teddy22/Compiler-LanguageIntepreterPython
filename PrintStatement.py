from Interface_mod import Statement
from Interface_mod import ArithmeticExpression


class PrintStatement(Statement):

    def __init__(self, expr):
        if expr is None:
            raise Exception('null arithmetic expression argument at ' + self.__name__)
        if not isinstance(expr, ArithmeticExpression):
            raise TypeError('invalid type of argument at ' + self.__name__)

        self.expr = expr

    def execute(self):
        print(self.expr.evaluate())