from Interface_mod import Statement
from Interface_mod import NullException


class StatementList:

    def __init__(self):
        self.statements = []

    def add(self, statement):
        if statement is None:
            raise NullException('null statement argument at ' + self.__name__)
        if not isinstance(statement, Statement):
            raise TypeError('invalid type for statement argument at ' + self.__name__)

        self.statements.append(statement)

    def execute(self):
        for statement in self.statements:
            statement.execute()
