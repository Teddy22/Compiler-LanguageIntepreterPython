from Operators import ArithmeticOperator
from Interface_mod import ArithmeticExpression


class BinaryExpression(ArithmeticExpression):

    def __init__(self, operator, expr1, expr2):
        if operator is None:
            raise Exception('null operator argument at ArithmeticExpression')
        if expr1 is None:
            raise Exception('null expression 1 argument at ArithmeticExpression')
        if expr2 is None:
            raise Exception('null expression 2 argument at ArithmeticExpression')
        if not isinstance(operator, ArithmeticOperator):
            raise Exception('invalid type for arithmetic operator argument at ArithmeticExpression')
        if not isinstance(expr1, ArithmeticExpression):
            raise Exception('invalid type for arithmetic expression 1 argument at ArithmeticExpression')
        if not isinstance(expr2, ArithmeticExpression):
            raise Exception('invalid type for arithmetic expression 2 argument at ArithmeticExpression')

        self.operator = operator
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if self.operator == ArithmeticOperator.ADD_OP:
            result = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.operator == ArithmeticOperator.SUB_OP:
            result = self.expr1.evaluate() - self.expr2.evaluate()
        elif self.operator == ArithmeticOperator.MUL_OP:
            result = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.operator == ArithmeticOperator.DIV_OP:
            result = self.expr1.evaluate() / self.expr2.evaluate()
        else:
            raise Exception('unexpected arithmetic operator symbol or token')

        return result
