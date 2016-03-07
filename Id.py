from Interface_mod import NullException
from Interface_mod import ArithmeticExpression
from Memory import Memory


class Id(ArithmeticExpression):

    def __init__(self, char):
        if char is None:
            raise NullException('null argument for character at Id')
        if not isinstance(char, str):
            raise TypeError('invalid type for character argument at Id')
        if not char.isalpha() or len(char) != 1:
            raise TypeError('invalid character argument at Id')

        self.char = char

    def evaluate(self):
        return Memory.fetch(self.char)

    def get_char(self):
        return self.char
