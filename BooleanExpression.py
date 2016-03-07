from Interface_mod import ArithmeticExpression
from Interface_mod import NullException
from Operators import RelationalOperator


class BooleanExpression():

    def __init__(self, relational_op, arithmetic_expr1, arithmetic_expr2):
        if relational_op is None:
            raise NullException('null relation operator argument at BooleanExpression')
        if arithmetic_expr1 is None:
            raise NullException('null arithmetic expression 1 argument at BooleanExpression')
        if arithmetic_expr2 is None:
            raise NullException('null arithmetic expression 2 argument at BooleanExpression')
        if not isinstance(relational_op, RelationalOperator):
            raise TypeError('invalid type for relational operator argument at BooleanExpression')
        if not isinstance(arithmetic_expr1, ArithmeticExpression):
            raise TypeError('invalid type for arithmetic expression 1 argument at BooleanExpression')
        if not isinstance(arithmetic_expr2, ArithmeticExpression):
            raise TypeError('invalid type for arithmetic expression 2 argument at BooleanExpression')

        self.relation_op = relational_op
        self.arithmetic_expr1 = arithmetic_expr1
        self.arithmetic_expr2 = arithmetic_expr2

    def evaluate(self):

        if self.relation_op == RelationalOperator.EQ_OP:
            result = self.arithmetic_expr1.evaluate() == self.arithmetic_expr2.evaluate()
        elif self.relation_op == RelationalOperator.NE_OP:
            result = self.arithmetic_expr1.evaluate() != self.arithmetic_expr2.evaluate()
        elif self.relation_op == RelationalOperator.LT_OP:
            result = self.arithmetic_expr1.evaluate() < self.arithmetic_expr2.evaluate()
        elif self.relation_op == RelationalOperator.LE_OP:
            result = self.arithmetic_expr1.evaluate() <= self.arithmetic_expr2.evaluate()
        elif self.relation_op == RelationalOperator.GT_OP:
            result = self.arithmetic_expr1.evaluate() > self.arithmetic_expr2.evaluate()
        elif self.relation_op == RelationalOperator.GE_OP:
            result = self.arithmetic_expr1.evaluate() >= self.arithmetic_expr2.evaluate()
        else:
            raise Exception('unexpected relational operator symbol or token')

        return result