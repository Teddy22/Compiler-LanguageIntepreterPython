import traceback


class Statement:

    def __init__(self):
        pass

    def execute(self):
        raise NotImplementedError()


class Expression:
    def __init__(self, expression):
        if expression is None:
            raise ExpressionError('null expression error')

        self.expression = expression

    def evaluate(self):
        raise NotImplementedError()

    def is_valid_expression(self):
        raise NotImplementedError()


class ArithmeticExpression:

    def evaluate(self):
        raise NotImplementedError()


class StatementError(Exception):

    def __init__(self, message):
        super().__init__('StatementError: ' + message)


class ExpressionError(Exception):

    def __init__(self, message):
        super().__init__('ExpressionError: ' + message)


class IllegalArgumentError(Exception):

    def __init__(self, message):
        super().__init__('IllegalArgumentError: ' + message)


class LexicalException(ExpressionError):

    def __init__(self, message):
        super().__init__('LexicalException: ' + message)


class ParserException(Exception):

    def __init__(self, message):
        super().__init__('ParserException: ' + message)
        traceback.print_stack()


class NullException(Exception):

    def __init__(self, message):
        super().__init__('NullException: ' + message)

'''
should be grouping by domain relationships - not coding
commonalities
'''