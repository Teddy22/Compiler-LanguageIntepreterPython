from Interface_mod import Statement
from Interface_mod import NullException
from Memory import Memory
from Id import Id
from Interface_mod import ArithmeticExpression


class AssignmentStatement(Statement):

    def __init__(self, i_d, arithmetic_expr):
        if i_d is None:
            raise NullException('null id argument at AssignmentStatement')
        if arithmetic_expr is None:
            raise NullException('null expression argument at ')
        if not isinstance(i_d, Id):
            raise TypeError('invalid type for id at AssignmentStatement')
        if not isinstance(arithmetic_expr, ArithmeticExpression):
            raise TypeError('invalid type for arithmetic operation at AssignmentStatement')

        self.i_d = i_d
        self.arithmetic_expr = arithmetic_expr

    def execute(self):
        Memory.store(self.i_d.get_char(), self.arithmetic_expr.evaluate())