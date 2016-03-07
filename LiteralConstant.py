from Interface_mod import ArithmeticExpression
from Interface_mod import NullException


class LiteralConstant(ArithmeticExpression):

    def __init__(self, value):
        if value is None:
            raise NullException('null value argument at ' + self.__name__)
        if not isinstance(value, int):
            raise TypeError('invalid data type (non-integer) at ' + self.__name__)

        self.value = value

    def evaluate(self):
        return self.value
